/**
 * Visual chrome from the design pass.
 * Strings live in site/src/i18n/{zh,en}.json under visual.* so both locales stay in one dictionary.
 */
import { currentLocale, t, type Locale } from './index';

const VISUAL_KEYS = [
  'menu',
  'close',
  'statDossiers',
  'statNews',
  'statRanked',
  'statHeat',
  'statAll',
  'statThin',
  'statListed',
  'statModels',
  'impactTabRanked',
  'impactTabThin',
  'searchBenchmarks',
  'heatSearch',
  'allDomains',
  'prev',
  'next',
  'nullTip',
  'unranked',
  'colRank',
  'colName',
  'colDomain',
  'colScore',
  'evQuality',
  'evCommunity',
  'evHeadroom',
  'evGithub',
  'emptyFilter',
  'showing',
  'rows',
  'footerAbout',
  'footerAboutTitle',
  'footerSections',
  'footerSources',
  'snapshot',
  'dossierLink',
  'reported',
  'share',
  'models',
  'organization',
  'release',
  'source',
  'open',
  'reportedModels',
  'scriptNote',
  'repo',
] as const;

export type VisualKey = (typeof VISUAL_KEYS)[number];
export type VisualCopy = Record<VisualKey, string>;
export type VisualLocale = Locale;

export function visualCopy(locale: Locale = currentLocale()): VisualCopy {
  const copy = {} as VisualCopy;
  for (const key of VISUAL_KEYS) copy[key] = t(locale, `visual.${key}`);
  return copy;
}
