import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
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
  drive_pdf?: { id?: string; webViewLink?: string } | string;
  drive_intro?: { id?: string; webViewLink?: string; kind?: string };
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
  root?: { webViewLink?: string };
  constitution?: { webViewLink?: string };
  master_sheet?: { webViewLink?: string };
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
  const news = readJson<NewsItem[]>('data/news.json');
  return news
    .map((item, index) => ({ item, index }))
    .sort((a, b) => b.item.observed_date.localeCompare(a.item.observed_date) || a.index - b.index)
    .map(({ item }) => item);
}

export function loadDrive(): DriveManifest {
  return readJson<DriveManifest>('data/drive-manifest.json');
}

export function loadQuality(): QualityReport {
  return readJson<QualityReport>('data/quality-report.json');
}

export function loadRecords(): RecordView[] {
  const index = loadIndex();
  return index.benchmarks.map((item, order) => {
    const file = readJson<BenchmarkFile>(`data/benchmarks/${item.id}.json`);
    const subfields = file.basic_info.subfields?.value;
    const tags = Array.isArray(subfields) ? subfields.filter((tag): tag is string => typeof tag === 'string') : item.tags;
    const search = [
      item.id,
      item.name,
      item.section,
      item.summary,
      item.tags.join(' '),
      textValue(file.basic_info.full_name),
      textValue(file.basic_info.paper_title),
      textValue(file.design_goals.capabilities),
      tags.join(' '),
    ]
      .join(' ')
      .toLowerCase();
    return {
      index: item,
      file,
      pending: countPending(file),
      order,
      search,
      date: sortDate(textValue(file.basic_info.release_date)),
    };
  });
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
    if (items?.length) groups.push({ id: section.id, blurb: section.blurb, items });
  }
  for (const [id, items] of bySection) {
    if (groups.some((group) => group.id === id)) continue;
    groups.push({ id, blurb: '新增板块', items });
  }
  const reserved = SECTIONS.filter((section) => !bySection.get(section.id)?.length).map((section) => section.id);
  return { groups, reserved };
}

export function allTags(records: RecordView[]): string[] {
  const tags = new Set<string>();
  for (const record of records) {
    for (const tag of record.index.tags ?? []) tags.add(tag);
  }
  return [...tags].sort((a, b) => a.localeCompare(b, 'zh'));
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
  const file = readJson<TrendingFile>('data/trending.json');
  return {
    ...file,
    items: [...(file.items ?? [])].sort((a, b) => a.rank - b.rank || a.name.localeCompare(b.name, 'zh')),
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
  const observed = `观察 ${item.observed_date}`;
  if (!item.event_date || item.event_date === '待核实') return `${observed} · 事件日期待核实`;
  return `${observed} · 事件 ${item.event_date}`;
}
