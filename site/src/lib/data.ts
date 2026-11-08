import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { currentLocale } from '../i18n';
import { t } from '../i18n';
import { localizeData, translateContent } from '../i18n/content';
import { sectionBlurb, sectionLabel } from './sections';
import { SECTIONS } from './chapters';
import { countPending, sortDate, textValue, type Field, type Source } from './format';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');

export type IndexBenchmark = {
  id: string;
  name: string;
  section: string;
  tags: string[];
  summary: string;
  json: string;
  content: string;
  drive_pdf?: { id?: string } | string;
  drive_intro?: { id?: string; kind?: string };
  sources?: Source[];
  last_checked?: string;
  cited_2026h2?: boolean;
  citation_note?: string;
  cited_2026h2_evidence?: {
    url: string;
    date?: string;
    note?: string;
    accessed?: string;
    date_precision?: string;
  }[];
};

export type IndexFile = {
  generated_at?: string;
  timezone?: string;
  count?: number;
  benchmarks: IndexBenchmark[];
};

export type NewsItem = {
  id: string;
  observed_date: string;
  event_date?: string;
  timezone?: string;
  title: string;
  body: string;
  sources: Source[];
  type?: string;
};

export type QualityReport = {
  validated_date?: string;
  timezone?: string;
  deferred?: { name: string; reason: string }[];
  excluded_as_nonexistent?: { name?: string; reason?: string }[];
};

export type DriveManifest = {
  root?: { id?: string };
  constitution?: { id?: string };
  master_sheet?: { id?: string };
};

export type BenchmarkFile = {
  id: string;
  schema_version?: string;
  editorial_status?: string;
  basic_info: Record<string, Field>;
  organization: Record<string, Field>;
  design_goals: Record<string, Field>;
  construction: Record<string, Field>;
  data_format: Record<string, Field>;
  evaluation: Record<string, Field>;
  latest_status: Record<string, Field>;
  leaderboard: Record<string, Field>;
  contact: Record<string, Field>;
  original_files: Record<string, Field>;
  drive_pdf: Field;
  changelog: Field;
};

export type RecordView = {
  index: IndexBenchmark;
  file: BenchmarkFile;
  pending: number;
  order: number;
  search: string;
  date: string;
};

export type SectionGroup = {
  id: string;
  blurb: string;
  items: RecordView[];
};

export type CatalogResource = {
  path: string;
  description: string;
  bytes: number;
  group: 'overview' | 'records' | 'content';
  page?: string;
};

export type Catalog = {
  name: string;
  read_only: true;
  generated_at: string;
  timezone: string;
  resources: CatalogResource[];
};

function readJson<T>(path: string): T {
  return JSON.parse(readFileSync(join(ROOT, path), 'utf8')) as T;
}

export function repoRoot(): string {
  return ROOT;
}

export function loadIndex(): IndexFile {
  return readJson<IndexFile>('data/index.json');
}

export function loadNews(): NewsItem[] {
  const locale = currentLocale();
  const news = readJson<NewsItem[]>('data/news.json');
  return news
    .map((item, index) => ({ item, index }))
    .sort((a, b) => b.item.observed_date.localeCompare(a.item.observed_date) || a.index - b.index)
    .map(({ item }) =>
      locale === 'en'
        ? {
            ...item,
            title: translateContent(item.title, locale),
            body: translateContent(item.body, locale),
            type: item.type ? translateContent(item.type, locale) : item.type,
          }
        : item,
    );
}

export function loadDrive(): DriveManifest {
  return readJson<DriveManifest>('data/drive-manifest.json');
}

export function loadQuality(): QualityReport {
  return readJson<QualityReport>('data/quality-report.json');
}

const recordCache = new Map<string, RecordView[]>();

export function loadRecords(): RecordView[] {
  const locale = currentLocale();
  const cached = recordCache.get(locale);
  if (cached) return cached;
  const index = loadIndex();
  const records = index.benchmarks.map((item, order) => {
    const raw = readJson<BenchmarkFile>(`data/benchmarks/${item.id}.json`);
    const file = localizeData(raw, locale);
    const subfields = file.basic_info.subfields?.value;
    const tags = Array.isArray(subfields)
      ? subfields.filter((tag): tag is string => typeof tag === 'string')
      : item.tags.map((tag) => translateContent(tag, locale));
    const summary = translateContent(item.summary, locale);
    const localized = {
      ...item,
      summary,
      tags,
      citation_note: item.citation_note ? translateContent(item.citation_note, locale) : item.citation_note,
      cited_2026h2_evidence: item.cited_2026h2_evidence?.map((evidence) => ({
        ...evidence,
        note: evidence.note ? translateContent(evidence.note, locale) : evidence.note,
      })),
    };
    const search = [
      item.id,
      item.name,
      sectionLabel(item.section, locale),
      summary,
      tags.join(' '),
      textValue(file.basic_info.full_name),
      textValue(file.basic_info.paper_title),
      textValue(file.design_goals.capabilities),
    ]
      .join(' ')
      .toLowerCase();
    return {
      index: localized,
      file,
      pending: countPending(raw),
      order,
      search,
      date: sortDate(textValue(file.basic_info.release_date)),
    };
  });
  recordCache.set(locale, records);
  return records;
}

export function benchmarksMentioned(text: string, items: IndexBenchmark[]): IndexBenchmark[] {
  const hits = items.filter((item) => item.name && text.includes(item.name));
  return hits.filter(
    (item) => !hits.some((other) => other.id !== item.id && other.name.includes(item.name) && other.name.length > item.name.length),
  );
}

export function newsForBenchmark(record: RecordView, news: NewsItem[], items: IndexBenchmark[]): NewsItem[] {
  return news.filter((item) => benchmarksMentioned(`${item.title}\n${item.body}`, items).some((hit) => hit.id === record.index.id));
}

export function sectionGroups(records: RecordView[]): { groups: SectionGroup[]; reserved: string[] } {
  const bySection = new Map<string, RecordView[]>();
  for (const record of records) {
    const section = record.index.section;
    const list = bySection.get(section) ?? [];
    list.push(record);
    bySection.set(section, list);
  }
  const groups: SectionGroup[] = [];
  for (const section of SECTIONS) {
    const items = bySection.get(section.id);
    if (items?.length) groups.push({ id: section.id, blurb: sectionBlurb(section.id, currentLocale()) || section.blurb, items });
  }
  for (const [id, items] of bySection) {
    if (groups.some((group) => group.id === id)) continue;
    groups.push({ id, blurb: t(currentLocale(), 'section.new'), items });
  }
  const reserved = SECTIONS.filter((section) => !bySection.get(section.id)?.length).map((section) => section.id);
  return { groups, reserved };
}

export function allTags(records: RecordView[]): string[] {
  const tags = new Set<string>();
  for (const record of records) {
    for (const tag of record.index.tags ?? []) tags.add(tag);
  }
  const locale = currentLocale() === 'zh' ? 'zh' : 'en';
  return [...tags].sort((a, b) => a.localeCompare(b, locale));
}

export type TrendingEvidence = {
  url: string;
  what?: string;
  date?: string;
  organization?: string;
};

export type TrendingItem = {
  slug: string;
  name: string;
  section: string;
  rank: number;
  heat_score?: number;
  heat_confidence: 'A' | 'B';
  rationale: string;
  evidence: TrendingEvidence[];
};

export type TrendingFile = {
  generated_at?: string;
  window?: { from?: string; through?: string; frontier_launch_extension_from?: string };
  note?: string;
  items: TrendingItem[];
};

export type TrendingView = TrendingItem & { linked: boolean };

export function loadTrending(): TrendingFile {
  const locale = currentLocale();
  const file = readJson<TrendingFile>('data/trending.json');
  const items = [...(file.items ?? [])]
    .map((item) =>
      locale === 'en'
        ? {
            ...item,
            rationale: translateContent(item.rationale, locale),
            evidence: item.evidence.map((entry) => ({
              ...entry,
              what: entry.what ? translateContent(entry.what, locale) : entry.what,
            })),
          }
        : item,
    )
    .sort((a, b) => a.rank - b.rank || a.name.localeCompare(b.name, locale === 'zh' ? 'zh' : 'en'));
  return {
    ...file,
    note: file.note ? translateContent(file.note, locale) : file.note,
    items,
  };
}

export function trendingViews(): TrendingView[] {
  const known = new Set(loadIndex().benchmarks.map((item) => item.id));
  return loadTrending().items.map((item) => ({ ...item, linked: known.has(item.slug) }));
}

export function trendingFor(id: string): TrendingView | undefined {
  return trendingViews().find((item) => item.slug === id);
}

export function newsWhen(item: NewsItem): string {
  const locale = currentLocale();
  const observed = t(locale, 'news.observed', { date: item.observed_date });
  if (!item.event_date || item.event_date === '待核实' || item.event_date === 'Unverified') {
    return `${observed}, ${t(locale, 'news.event_unverified')}`;
  }
  return `${observed}, ${t(locale, 'news.event', { date: item.event_date })}`;
}
