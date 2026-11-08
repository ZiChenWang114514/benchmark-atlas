import { AsyncLocalStorage } from 'node:async_hooks';
import en from './en.json';
import zh from './zh.json';

export type Locale = 'en' | 'zh';

const localeStore = new AsyncLocalStorage<Locale>();

export function currentLocale(): Locale {
  return localeStore.getStore() ?? 'en';
}

export function runWithLocale<T>(locale: Locale, fn: () => T): T {
  return localeStore.run(locale, fn);
}

const dictionaries: Record<Locale, Record<string, string>> = { en, zh };

export function otherLocale(locale: Locale): Locale {
  return locale === 'en' ? 'zh' : 'en';
}

export function localeFromPathname(pathname: string): Locale {
  const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '');
  let path = pathname || '/';
  if (base && path.startsWith(base)) path = path.slice(base.length) || '/';
  if (!path.startsWith('/')) path = `/${path}`;
  return path === '/zh' || path.startsWith('/zh/') ? 'zh' : 'en';
}

export function hrefForLocale(pathname: string, search: string, target: Locale): string {
  const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '');
  let path = pathname || '/';
  if (base && path.startsWith(base)) path = path.slice(base.length) || '/';
  if (!path.startsWith('/')) path = `/${path}`;
  path = path.replace(/^\/zh(?=\/|$)/, '') || '/';
  if (!path.startsWith('/')) path = `/${path}`;
  if (target === 'zh') path = path === '/' ? '/zh/' : `/zh${path}`;
  if (!path.endsWith('/')) path = `${path}/`;
  return `${base}${path}${search || ''}`;
}

export function t(locale: Locale, key: string, vars?: Record<string, string | number>): string {
  const text = dictionaries[locale][key] ?? dictionaries.en[key];
  if (text == null) return key;
  if (!vars) return text;
  return text.replace(/\{(\w+)\}/g, (match, name: string) => (vars[name] == null ? match : String(vars[name])));
}
