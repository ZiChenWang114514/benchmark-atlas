import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { currentLocale, t } from '../i18n';
import { repoRoot } from './data';

export type HeatModel = {
  id: string;
  name: string;
  organization?: string | null;
  release_date?: string | null;
  sources?: { url?: string; accessed?: string }[];
  benchmarks?: string[];
};

export type HeatRank = {
  rank: number;
  benchmark_id: string;
  name: string;
  domain?: string | null;
  count: number;
  share?: number | null;
  models?: string[];
  first_seen?: string | null;
  rank_change?: number | 'new' | null;
};

export type HeatFile = {
  generated_at?: string;
  window?: { n_models?: number; rule?: string };
  models: HeatModel[];
  ranking: HeatRank[];
  history?: { date: string; top: string[] }[];
  coverage?: {
    interpretation_zh?: string;
    rank_change_reference_date?: string | null;
  };
};

export type ImpactDimension = {
  key: string;
  name_zh: string;
  weight: number;
  description_zh?: string;
};

export type ImpactRow = {
  rank: number | null;
  id: string;
  name: string;
  domain?: string | null;
  release_date?: string | null;
  score: number | null;
  components?: Record<string, number | null>;
  raw?: Record<string, number | string | null>;
  flags?: string[];
  assessment_review?: {
    formal_quality_audit_complete?: boolean;
    independent_reviewers?: number;
  };
};

export type ImpactFile = {
  generated_at?: string;
  method_version?: string;
  dimensions: ImpactDimension[];
  ranking: ImpactRow[];
  unscored?: ImpactRow[];
  minimum_ranking_coverage?: number;
  official_ranking_count?: number;
  publication_warning_zh?: string;
  ranking_status?: string;
};

export type RegistryItem = {
  id: string;
  name: string;
  aliases?: string[];
  domain?: string | null;
  subdomain?: string | null;
  description_zh?: string | null;
  organization?: string | null;
  release_date?: string | null;
  paper_url?: string | null;
  github_url?: string | null;
  hf_dataset?: string | null;
  homepage?: string | null;
  metrics?: {
    citations?: number | null;
    gh_stars?: number | null;
    [key: string]: number | string | null | undefined;
  };
};

export type RegistryFile = {
  generated_at?: string;
  count?: number;
  items: RegistryItem[];
};

function readOptional<T>(relative: string): T | null {
  const path = join(repoRoot(), relative);
  if (!existsSync(path)) return null;
  return JSON.parse(readFileSync(path, 'utf8')) as T;
}

export function loadHeat(): HeatFile | null {
  return readOptional<HeatFile>('data/frontier/heat.json');
}

export function loadImpact(): ImpactFile | null {
  return readOptional<ImpactFile>('data/impact/index.json');
}

export function loadRegistry(): RegistryFile | null {
  return readOptional<RegistryFile>('data/registry/registry.json');
}

export function loadMethodology(): string | null {
  const name = currentLocale() === 'en' ? 'docs/impact-methodology.en.md' : 'docs/impact-methodology.md';
  const path = join(repoRoot(), name);
  if (!existsSync(path)) return null;
  return readFileSync(path, 'utf8');
}

export function rankArrow(change: HeatRank['rank_change']): { mark: string; label: string } {
  const locale = currentLocale();
  if (change === 'new') return { mark: t(locale, 'rank.new_mark'), label: t(locale, 'rank.new') };
  if (typeof change === 'number' && change < 0) {
    const n = Math.abs(change);
    return { mark: t(locale, 'rank.up_mark', { n }), label: t(locale, 'rank.up', { n }) };
  }
  if (typeof change === 'number' && change > 0) return { mark: t(locale, 'rank.down_mark', { n: change }), label: t(locale, 'rank.down', { n: change }) };
  return { mark: t(locale, 'rank.same_mark'), label: t(locale, 'rank.same') };
}
