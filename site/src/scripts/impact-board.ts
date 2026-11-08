import { profileHtml, scoreTier, type ProfileGroupId } from '../lib/profile';

type Part = { id: ProfileGroupId; value: number };
type Row = {
  rank: number | null;
  id: string;
  name: string;
  domain: string;
  score: number | null;
  quality: number | null;
  qualityPrior?: boolean;
  community: number | null;
  saturation: number | null;
  github: number | null;
  tier: 'ranked' | 'insufficient';
  href: string;
  parts: Part[];
};

const PAGE = 40;
const PARTS: ProfileGroupId[] = ['citations', 'github', 'hf', 'adoption', 'community', 'novelty', 'quality', 'penalties'];

function esc(value: unknown): string {
  return String(value ?? '').replace(/[&<>"']/g, (char) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char] || char
  ));
}

function metric(value: number | null, label: string, prior = false, priorTip = '', nullTip = ''): string {
  if (prior) return `<td data-label="${esc(label)}"><span class="na prior" title="${esc(priorTip)}">—</span></td>`;
  if (value == null || Number.isNaN(value)) return `<td data-label="${esc(label)}"><span class="na" title="${esc(nullTip)}">—</span></td>`;
  const width = Math.max(0, Math.min(100, value));
  return `<td data-label="${esc(label)}"><span class="mini"><b class="num">${value.toFixed(1)}</b><span class="track" aria-hidden="true"><span class="${scoreTier(value)} grow" style="width:${width}%"></span></span></span></td>`;
}

export function mountImpactBoard(): void {
  const dataNode = document.querySelector('#impact-data');
  const table = document.querySelector<HTMLTableElement>('#impact-table');
  if (!table) return;
  const rows = JSON.parse(dataNode?.textContent || '[]') as Row[];
  const label = {
    rank: table.dataset.labelRank || '',
    name: table.dataset.labelName || '',
    domain: table.dataset.labelDomain || '',
    score: table.dataset.labelScore || '',
    quality: table.dataset.labelQuality || '',
    community: table.dataset.labelCommunity || '',
    headroom: table.dataset.labelHeadroom || '',
    github: table.dataset.labelGithub || '',
  };
  const partLabel = Object.fromEntries(PARTS.map((id) => {
    const key = `part${id.charAt(0).toUpperCase()}${id.slice(1)}`;
    return [id, table.dataset[key] || id];
  })) as Record<ProfileGroupId, string>;
  const nullTip = table.dataset.nullTip || '';
  const priorTip = table.dataset.priorTip || '';
  const unranked = table.dataset.unranked || nullTip;
  const expand = table.dataset.expand || '';
  const breakdown = table.dataset.breakdown || '';
  const penaltiesNote = table.dataset.penaltiesNote || '';
  const count = document.querySelector<HTMLElement>('#impact-count');
  const empty = document.querySelector<HTMLElement>('#impact-empty');
  const pageLabel = document.querySelector('#impact-page');
  const prev = document.querySelector<HTMLButtonElement>('#impact-prev');
  const next = document.querySelector<HTMLButtonElement>('#impact-next');
  const queryInput = document.querySelector<HTMLInputElement>('#impact-q');
  const domain = document.querySelector<HTMLSelectElement>('#impact-domain');
  const sortSelect = document.querySelector<HTMLSelectElement>('#impact-sort');
  const tabs = [...document.querySelectorAll<HTMLButtonElement>('[data-tier]')];
  const sortButtons = [...table.querySelectorAll<HTMLButtonElement>('[data-sort]')];
  const toolbar = document.querySelector<HTMLElement>('#impact-form');
  const locale = document.documentElement.lang.toLowerCase().startsWith('zh') ? 'zh' : 'en';
  let tier: 'ranked' | 'insufficient' = 'ranked';
  let page = 0;
  let sortKey = 'rank';
  let sortDir: 'asc' | 'desc' = 'asc';
  let thinBuilt = false;

  const syncBar = () => {
    if (toolbar) document.documentElement.style.setProperty('--toolbar', `${toolbar.offsetHeight}px`);
  };

  const labeled = (row: Row) => row.parts.map((part) => ({
    label: partLabel[part.id] || part.id,
    value: part.value,
    note: part.id === 'penalties' ? penaltiesNote : '',
  }));

  const entryHtml = (row: Row) => {
    const podium = row.tier === 'ranked' && row.rank != null && row.rank <= 3 ? `podium-${row.rank}` : '';
    const rank = row.rank == null
      ? `<span class="na" title="${esc(unranked)}">—</span>`
      : `<span class="rank-no">${row.rank}</span>`;
    const name = row.href ? `<a href="${esc(row.href)}">${esc(row.name)}</a>` : esc(row.name);
    const domainText = row.domain
      ? `<span class="domain-tag">${esc(row.domain)}</span>`
      : `<span class="na" title="${esc(nullTip)}">—</span>`;
    const width = Math.max(0, Math.min(100, row.score ?? 0));
    const score = row.score == null
      ? `<span class="na" title="${esc(nullTip)}">—</span>`
      : `<details><summary class="score-summary" aria-controls="bd-${esc(row.id)}" aria-label="${esc(`${expand} ${row.name}`)}"><span class="score-wrap"><span class="score-num">${row.score.toFixed(1)}</span><span class="track" aria-hidden="true"><span class="${scoreTier(row.score)} grow" style="width:${width}%"></span></span></span></summary></details>`;
    const tip = row.parts.length
      ? `<div class="tip" role="tooltip"><p>${esc(row.name)}</p><ul>${labeled(row).map((part) => `<li><span>${esc(part.label)}</span><b class="num">${part.value.toFixed(1)}</b></li>`).join('')}</ul></div>`
      : '';
    const chart = row.parts.length
      ? `<div data-chart data-name="${esc(row.name)}"></div>`
      : '';
    const search = `${row.name} ${row.id} ${row.domain}`.toLowerCase();
    return `<tbody class="entry ${podium}" data-tier="${row.tier}" data-rank="${row.rank ?? ''}" data-name="${esc(row.name)}" data-domain="${esc(row.domain)}" data-score="${row.score ?? ''}" data-quality="${row.quality ?? ''}" data-community="${row.community ?? ''}" data-headroom="${row.saturation ?? ''}" data-github="${row.github ?? ''}" data-search="${esc(search)}" data-parts="${esc(JSON.stringify(row.parts))}">
      <tr>
        <td class="rank-cell" data-label="${esc(label.rank)}">${rank}</td>
        <td class="name-cell" data-label="${esc(label.name)}">${name}</td>
        <td data-label="${esc(label.domain)}">${domainText}</td>
        <td class="score-cell" data-label="${esc(label.score)}"><div class="tip-host">${score}${tip}</div></td>
        ${metric(row.community, label.community, false, '', nullTip)}
        ${metric(row.github, label.github, false, '', nullTip)}
      </tr>
      <tr class="detail" id="bd-${esc(row.id)}"><td colspan="6">${chart}</td></tr>
    </tbody>`;
  };

  const buildThin = () => {
    if (thinBuilt) return;
    thinBuilt = true;
    const html = rows.filter((row) => row.tier === 'insufficient').map(entryHtml).join('');
    table.insertAdjacentHTML('beforeend', html);
  };

  const entries = () => [...table.querySelectorAll<HTMLElement>('tbody.entry')];

  const num = (value: string | undefined): number | null => {
    if (value == null || value === '') return null;
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  };

  const compare = (a: HTMLElement, b: HTMLElement) => {
    const dir = sortDir === 'asc' ? 1 : -1;
    const nameOrder = (a.dataset.name || '').localeCompare(b.dataset.name || '', locale);
    if (sortKey === 'name' || sortKey === 'domain') {
      const text = (a.dataset[sortKey] || '').localeCompare(b.dataset[sortKey] || '', locale);
      return text * dir || nameOrder;
    }
    const left = num(a.dataset[sortKey]);
    const right = num(b.dataset[sortKey]);
    if (left == null && right == null) return nameOrder;
    if (left == null) return 1;
    if (right == null) return -1;
    return (left - right) * dir || nameOrder;
  };

  const markSort = () => {
    for (const button of sortButtons) {
      const header = button.closest('th');
      const active = button.dataset.sort === sortKey;
      button.dataset.dir = active ? sortDir : '';
      header?.setAttribute('aria-sort', active ? (sortDir === 'asc' ? 'ascending' : 'descending') : 'none');
    }
    if (sortSelect) sortSelect.value = `${sortKey}:${sortDir}`;
  };

  const fillChart = (host: HTMLElement) => {
    const slot = host.querySelector<HTMLElement>('[data-chart]');
    if (!slot || slot.dataset.ready === '1') return;
    let parts: Part[] = [];
    try {
      parts = JSON.parse(host.dataset.parts || '[]') as Part[];
    } catch {
      parts = [];
    }
    const drawn = parts.map((part) => ({
      label: partLabel[part.id] || part.id,
      value: part.value,
      note: part.id === 'penalties' ? penaltiesNote : '',
    }));
    const name = slot.dataset.name || host.dataset.name || '';
    slot.innerHTML = profileHtml(drawn, breakdown, `${breakdown} ${name}`, true);
    slot.dataset.ready = '1';
  };

  const draw = () => {
    if (tier === 'insufficient') buildThin();
    const query = (queryInput?.value || '').trim().toLowerCase();
    const selected = domain?.value || '';
    const matched = entries().filter((row) => {
      if (row.dataset.tier !== tier) return false;
      if (selected && row.dataset.domain !== selected) return false;
      if (query && !(row.dataset.search || '').includes(query)) return false;
      return true;
    }).sort(compare);
    const pages = Math.max(1, Math.ceil(matched.length / PAGE));
    if (page >= pages) page = pages - 1;
    if (page < 0) page = 0;
    const visible = new Set(matched.slice(page * PAGE, page * PAGE + PAGE));
    const matchedSet = new Set(matched);
    for (const row of entries()) {
      if (row.dataset.tier !== tier || !matchedSet.has(row)) row.hidden = true;
    }
    for (const row of matched) {
      table.append(row);
      row.hidden = !visible.has(row);
    }
    table.classList.add('is-paged');
    if (count) count.textContent = `${count.dataset.showing || ''} ${matched.length} ${count.dataset.unit || ''}`.replace(/\s+/g, ' ').trim();
    if (empty) empty.hidden = matched.length !== 0;
    if (pageLabel) pageLabel.textContent = `${page + 1} / ${pages}`;
    if (prev) prev.disabled = page <= 0;
    if (next) next.disabled = page >= pages - 1;
    markSort();
    syncBar();
  };

  const setSort = (key: string, dir: 'asc' | 'desc') => {
    sortKey = key;
    sortDir = dir;
    page = 0;
    draw();
  };

  table.addEventListener('click', (event) => {
    const target = event.target as HTMLElement | null;
    if (!target) return;
    const entry = target.closest<HTMLElement>('tbody.entry');
    if (!entry || target.closest('a, summary, button, input, select')) return;
    const details = entry.querySelector('details');
    if (!details) return;
    details.open = !details.open;
  });
  table.addEventListener('toggle', (event) => {
    const details = event.target as HTMLDetailsElement | null;
    if (!details || details.tagName !== 'DETAILS' || !details.open) return;
    const entry = details.closest<HTMLElement>('tbody.entry');
    if (entry) fillChart(entry);
  }, true);

  queryInput?.addEventListener('input', () => { page = 0; draw(); });
  domain?.addEventListener('change', () => { page = 0; draw(); });
  sortSelect?.addEventListener('change', () => {
    const [key, dir] = (sortSelect.value || 'rank:asc').split(':');
    setSort(key || 'rank', dir === 'desc' ? 'desc' : 'asc');
  });
  prev?.addEventListener('click', () => { page -= 1; draw(); });
  next?.addEventListener('click', () => { page += 1; draw(); });
  for (const button of sortButtons) {
    button.addEventListener('click', () => {
      const key = button.dataset.sort || 'rank';
      const numeric = key !== 'name' && key !== 'domain' && key !== 'rank';
      const dir = sortKey === key
        ? (sortDir === 'asc' ? 'desc' : 'asc')
        : (numeric ? 'desc' : 'asc');
      setSort(key, dir);
    });
  }
  for (const tab of tabs) {
    tab.addEventListener('click', () => {
      tier = (tab.dataset.tier as 'ranked' | 'insufficient') || 'ranked';
      for (const other of tabs) other.setAttribute('aria-selected', other === tab ? 'true' : 'false');
      page = 0;
      draw();
    });
  }
  document.querySelector('#impact-form')?.addEventListener('submit', (event) => event.preventDefault());
  window.addEventListener('resize', syncBar);
  draw();
}
