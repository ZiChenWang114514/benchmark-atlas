import type { Locale } from '../i18n';
import { t } from '../i18n';

/** Canonical section ids stay in the data files. English pages render the slug and the translated label. */
export const SECTION_SLUG: Record<string, string> = {
  物理: 'physics',
  化学: 'chemistry',
  生物与医学: 'biomedicine',
  地球与天文: 'earth-astronomy',
  材料: 'materials',
  综合科学: 'general-science',
  语言: 'language',
  推理: 'reasoning',
  数学: 'mathematics',
  代码: 'code',
  多模态: 'multimodal',
  Agent: 'agent',
  安全: 'safety',
  语音: 'speech',
  机器人与具身: 'embodied',
  其他: 'other',
};

const SLUG_TO_CANONICAL = Object.fromEntries(Object.entries(SECTION_SLUG).map(([canonical, slug]) => [slug, canonical]));

export function sectionSlug(value: string | null | undefined): string {
  if (!value) return '';
  if (SECTION_SLUG[value]) return SECTION_SLUG[value];
  if (SLUG_TO_CANONICAL[value]) return value;
  if (/^[a-z0-9-]+$/.test(value)) return value;
  return 'other';
}

export function sectionLabel(value: string | null | undefined, locale: Locale): string {
  if (!value) return '';
  const slug = sectionSlug(value);
  const key = `section.${slug}`;
  const label = t(locale, key);
  return label === key ? value : label;
}

export function sectionBlurb(value: string | null | undefined, locale: Locale): string {
  const slug = sectionSlug(value);
  if (!slug) return '';
  const key = `section.${slug}.blurb`;
  const label = t(locale, key);
  return label === key ? '' : label;
}
