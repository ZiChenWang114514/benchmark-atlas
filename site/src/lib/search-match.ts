export type SearchHit = {
  id: string;
  name: string;
  aliases: string[];
  domain: string;
  organization: string;
  tags: string[];
  href: string;
  haystack: string;
};

export function normalizeQuery(text: string): string {
  return text.normalize('NFKC').toLowerCase().replace(/\s+/g, ' ').trim();
}

export function scoreEntry(item: SearchHit, tokens: string[]): number {
  if (!tokens.length || !tokens.every((token) => item.haystack.includes(token))) return 0;
  const query = tokens.join(' ');
  const name = normalizeQuery(item.name);
  const id = normalizeQuery(item.id);
  const idSpaced = id.replace(/-/g, ' ');
  const aliases = item.aliases.map(normalizeQuery);
  let score = 1;
  if (name === query) score += 100;
  else if (name.startsWith(query)) score += 80;
  else if (tokens.every((token) => name.includes(token))) score += 50;
  if (aliases.some((alias) => alias === query)) score += 70;
  else if (aliases.some((alias) => alias.startsWith(query) || tokens.every((token) => alias.includes(token)))) score += 40;
  if (id === query || idSpaced === query) score += 60;
  else if (id.includes(query) || idSpaced.includes(query)) score += 25;
  if (normalizeQuery(item.domain).includes(query) || tokens.every((token) => normalizeQuery(item.domain).includes(token))) score += 15;
  if (item.tags.some((tag) => tokens.every((token) => normalizeQuery(tag).includes(token)))) score += 12;
  if (tokens.every((token) => normalizeQuery(item.organization).includes(token))) score += 10;
  score += Math.max(0, 8 - name.length / 12);
  return score;
}

export function filterSearchIndex(items: SearchHit[], query: string): SearchHit[] {
  const tokens = normalizeQuery(query).split(' ').filter(Boolean);
  if (!tokens.length) return [];
  return items
    .map((item) => ({ item, score: scoreEntry(item, tokens) }))
    .filter((entry) => entry.score > 0)
    .sort((a, b) => b.score - a.score || a.item.name.localeCompare(b.item.name))
    .map((entry) => entry.item);
}
