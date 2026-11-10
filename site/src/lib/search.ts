import { currentLocale, runWithLocale, type Locale } from '../i18n';
import { loadRegistry } from './boards';
import { loadRecords } from './data';
import { isStatusWord, page, statusOf, type Field } from './format';
import { sectionLabel } from './sections';
import { normalizeQuery, type SearchHit } from './search-match';

export type { SearchHit };
export type SearchEntry = SearchHit;
export type SearchIndex = {
  items: SearchEntry[];
};
export { filterSearchIndex, normalizeQuery, scoreEntry } from './search-match';

function publicFieldText(field?: Field): string {
  if (!field || statusOf(field)) return '';
  const value = field.value;
  if (isStatusWord(value) || value == null || value === '') return '';
  if (Array.isArray(value)) {
    return value
      .map((item) => (typeof item === 'string' ? item : ''))
      .filter((item) => item && !isStatusWord(item))
      .join(' ');
  }
  return typeof value === 'string' ? value : '';
}

function unique(values: string[]): string[] {
  const seen = new Set<string>();
  const out: string[] = [];
  for (const value of values) {
    const trimmed = value.trim();
    if (!trimmed || isStatusWord(trimmed)) continue;
    const key = normalizeQuery(trimmed);
    if (!key || seen.has(key)) continue;
    seen.add(key);
    out.push(trimmed);
  }
  return out;
}

function collect(locale: Locale): SearchEntry[] {
  const records = loadRecords();
  const registry = loadRegistry();
  const aliasesById = new Map<string, string[]>();
  for (const item of registry?.items ?? []) {
    if (item.id && item.aliases?.length) aliasesById.set(item.id, item.aliases);
  }
  return records.map((record) => {
    const domain = sectionLabel(record.index.section, locale);
    const fullName = publicFieldText(record.file.basic_info.full_name);
    const aliases = unique([
      ...(aliasesById.get(record.index.id) ?? []),
      fullName && fullName !== record.index.name ? fullName : '',
    ]);
    const organization = unique([
      publicFieldText(record.file.organization.initiators),
      publicFieldText(record.file.organization.maintainer),
      publicFieldText(record.file.organization.partners),
    ]).join(' ');
    const tags = record.index.tags ?? [];
    const haystack = normalizeQuery(
      [
        record.index.id,
        record.index.id.replace(/-/g, ' '),
        record.index.name,
        ...aliases,
        domain,
        record.index.section,
        organization,
        tags.join(' '),
        record.index.summary,
        publicFieldText(record.file.basic_info.paper_title),
      ].join(' '),
    );
    return {
      id: record.index.id,
      name: record.index.name,
      aliases,
      domain,
      organization,
      tags,
      href: page(`benchmarks/${record.index.id}`, locale),
      haystack,
    };
  });
}

export function buildSearchIndex(locale: Locale = currentLocale()): SearchIndex {
  return runWithLocale(locale, () => ({ items: collect(locale) }));
}
