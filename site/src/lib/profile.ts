export const AMBER_RAMP = [
  '#5c3a05',
  '#6b3e14',
  '#7a4e08',
  '#8a5a10',
  '#9a6a18',
  '#a87408',
  '#b0893e',
  '#c4962a',
  '#d4a24a',
  '#e0b04a',
  '#e8b423',
  '#f0c56a',
  '#f3d48a',
  '#f6e2a8',
  '#f8e7b8',
];

export const PROFILE_GROUPS = [
  { id: 'citations', keys: ['citations_total', 'citation_velocity'] },
  { id: 'github', keys: ['github'] },
  { id: 'hf', keys: ['huggingface'] },
  { id: 'adoption', keys: ['model_adoption', 'evaluator_adoption'] },
  { id: 'community', keys: ['community'] },
  { id: 'novelty', keys: ['novelty'] },
  { id: 'quality', keys: ['quality'] },
  { id: 'penalties', keys: ['distinctiveness'] },
] as const;

export type ProfileGroupId = (typeof PROFILE_GROUPS)[number]['id'];

export type ProfilePart = {
  id: ProfileGroupId;
  value: number;
};

type Review = {
  formal_quality_audit_complete?: boolean;
  independent_reviewers?: number;
};

export function isQualityPrior(review: Review | undefined, value: number | null): boolean {
  if (value !== 50) return false;
  const audited = review?.formal_quality_audit_complete === true && (review.independent_reviewers ?? 0) > 0;
  return !audited;
}

export function profileParts(
  components: Record<string, number | null> | undefined,
  weights: Map<string, number>,
  review?: Review,
): ProfilePart[] {
  const source = components ?? {};
  const parts: ProfilePart[] = [];
  for (const group of PROFILE_GROUPS) {
    let weighted = 0;
    let weightSum = 0;
    for (const key of group.keys) {
      const value = source[key];
      if (typeof value !== 'number' || !Number.isFinite(value)) continue;
      if (key === 'quality' && isQualityPrior(review, value)) continue;
      const weight = weights.get(key) ?? 1;
      weighted += value * weight;
      weightSum += weight;
    }
    if (weightSum > 0) {
      parts.push({ id: group.id, value: Math.round((weighted / weightSum) * 10) / 10 });
    }
  }
  return parts;
}

export function scoreTier(value: number): string {
  if (value >= 68) return 'tier-high';
  if (value >= 60) return 'tier-mid';
  return 'tier-low';
}

function esc(value: string): string {
  return value.replace(/[&<>"']/g, (char) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char] || char
  ));
}

function clamp(value: number): number {
  return Math.max(0, Math.min(100, value));
}

type Drawn = { label: string; value: number };

function radar(parts: Drawn[], aria: string): string {
  const n = parts.length;
  const cx = 160;
  const cy = 112;
  const radius = 58;
  const point = (index: number, scale: number) => {
    const angle = -Math.PI / 2 + (index / n) * Math.PI * 2;
    return [cx + Math.cos(angle) * radius * scale, cy + Math.sin(angle) * radius * scale];
  };
  const ring = (scale: number) => parts.map((_, index) => point(index, scale).map((n) => n.toFixed(1)).join(',')).join(' ');
  const data = parts.map((part, index) => point(index, clamp(part.value) / 100).map((n) => n.toFixed(1)).join(',')).join(' ');
  const axes = parts.map((_, index) => {
    const [x, y] = point(index, 1);
    return `<line x1="${cx}" y1="${cy}" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}" stroke="#e6dcc8" stroke-width="1" />`;
  }).join('');
  const labels = parts.map((part, index) => {
    const [x, y] = point(index, 1.28);
    const anchor = x < cx - 10 ? 'end' : x > cx + 10 ? 'start' : 'middle';
    const dy = y < cy - 8 ? -2 : y > cy + 8 ? 8 : 3;
    return `<text x="${x.toFixed(1)}" y="${(y + dy).toFixed(1)}" text-anchor="${anchor}" fill="#3a342c" font-size="9">${esc(part.label)}</text>`;
  }).join('');
  const dots = parts.map((part, index) => {
    const [x, y] = point(index, clamp(part.value) / 100);
    return `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="2.2" fill="#7a4e08" />`;
  }).join('');
  return `<svg class="chart-svg" viewBox="0 0 320 236" role="img" aria-label="${esc(aria)}"><polygon points="${ring(0.34)}" fill="none" stroke="#f0e2c4" stroke-width="1" /><polygon points="${ring(0.67)}" fill="none" stroke="#e6dcc8" stroke-width="1" /><polygon points="${ring(1)}" fill="#fffdf8" stroke="#d4c4a4" stroke-width="1" />${axes}<polygon points="${data}" fill="rgba(232,180,35,0.42)" stroke="#a87408" stroke-width="1.6" />${dots}${labels}</svg>`;
}

function bars(parts: Drawn[], aria: string): string {
  const row = 28;
  const height = Math.max(36, parts.length * row + 8);
  const body = parts.map((part, index) => {
    const y = 8 + index * row;
    const width = (clamp(part.value) / 100) * 148;
    const fill = AMBER_RAMP[Math.min(AMBER_RAMP.length - 1, 4 + index)];
    return `<text x="0" y="${y + 14}" fill="#3a342c" font-size="11">${esc(part.label)}</text><rect x="112" y="${y + 4}" width="148" height="10" rx="5" fill="#efe4cc" /><rect x="112" y="${y + 4}" width="${width.toFixed(1)}" height="10" rx="5" fill="${fill}" /><text x="268" y="${y + 14}" fill="#1b1916" font-size="11">${part.value.toFixed(1)}</text>`;
  }).join('');
  return `<svg class="chart-svg" viewBox="0 0 320 ${height}" role="img" aria-label="${esc(aria)}">${body}</svg>`;
}

export function chartSvg(parts: Drawn[], aria: string): string {
  if (!parts.length) return '';
  return parts.length >= 3 ? radar(parts, aria) : bars(parts, aria);
}

export function profileHtml(
  parts: { label: string; value: number; note?: string }[],
  title: string,
  aria: string,
  compact = false,
): string {
  if (!parts.length) return '';
  const svg = chartSvg(parts.map((part) => ({ label: part.label, value: part.value })), aria);
  const items = parts.map((part) => (
    `<li><span>${esc(part.label)}</span><b class="num">${part.value.toFixed(1)}</b>${part.note ? `<small>${esc(part.note)}</small>` : ''}</li>`
  )).join('');
  const cls = compact ? 'profile profile-compact' : 'profile';
  return `<figure class="${cls}"><figcaption>${esc(title)}</figcaption><div class="profile-svg">${svg}</div><ul class="profile-list">${items}</ul></figure>`;
}
