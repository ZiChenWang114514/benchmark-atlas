import { existsSync, readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import type { Locale } from './index';
import { sectionLabel } from '../lib/sections';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');

let lexicon: Record<string, string> | null = null;

function loadLexicon(): Record<string, string> {
  if (lexicon) return lexicon;
  const path = join(ROOT, 'data/en/lexicon.json');
  lexicon = existsSync(path) ? (JSON.parse(readFileSync(path, 'utf8')) as Record<string, string>) : {};
  return lexicon;
}

const STATUS: Record<string, string> = {
  待核实: 'Unverified',
  未公开: 'Not disclosed',
};

export function translateContent(text: string, locale: Locale): string {
  if (locale !== 'en' || !text) return text;
  if (STATUS[text]) return STATUS[text];
  const mapped = loadLexicon()[text];
  return mapped ?? text;
}

const KEEP_VALUE_KEYS = new Set(['section', 'domain']);

export function localizeData<T>(value: T, locale: Locale, parentKey = ''): T {
  if (locale !== 'en') return value;
  if (typeof value === 'string') {
    if (KEEP_VALUE_KEYS.has(parentKey)) return value;
    if (/^(https?:|urn:|mailto:)/.test(value)) return value;
    return translateContent(value, locale) as T;
  }
  if (Array.isArray(value)) return value.map((item) => localizeData(item, locale)) as T;
  if (value && typeof value === 'object') {
    const out: Record<string, unknown> = {};
    for (const [key, item] of Object.entries(value as Record<string, unknown>)) {
      if (key === 'sources' || key === 'url' || key === 'webViewLink') {
        out[key] = item;
        continue;
      }
      if (key === 'sha256' && typeof item === 'string') {
        out[key] = item;
        continue;
      }
      if (key === 'value' && KEEP_VALUE_KEYS.has(parentKey) && typeof item === 'string') {
        out[key] = sectionLabel(item, locale) || item;
        continue;
      }
      out[key] = localizeData(item, locale, key);
    }
    return out as T;
  }
  return value;
}
