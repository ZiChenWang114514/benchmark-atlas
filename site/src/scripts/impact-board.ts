type Row = {
  rank: number | null;
  id: string;
  name: string;
  domain: string;
  score: number | null;
  quality: number | null;
  community: number | null;
  saturation: number | null;
  github: number | null;
  tier: 'ranked' | 'insufficient';
  href: string;
};

const PAGE = 40;

function esc(value: unknown): string {
  return String(value ?? '').replace(/[&<>"']/g, (char) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char] || char
  ));
}

function metric(value: number | null, tip: string, label: string): string {
  if (value == null || Number.isNaN(value)) {
    return `<td data-label="${esc(label)}"><span class="na" title="${esc(tip)}">—</span></td>`;
  }
  const width = Math.max(0, Math.min(100, value));
  return `<td data-label="${esc(label)}"><span class="mini" title="${esc(tip)}"><b class="num">${value.toFixed(1)}</b><span class="track" aria-hidden="true"><span style="width:${width}%"></span></span></span></td>`;
}

export function mountImpactBoard(): void {
  const dataNode = document.querySelector('#impact-data');
  const body = document.querySelector('#impact-body');
  const table = document.querySelector<HTMLTableElement>('#impact-table');
  if (!dataNode || !body || !table) return;
  const rows = JSON.parse(dataNode.textContent || '[]') as Row[];
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
  const tipName = {
    quality: table.dataset.tipQuality || label.quality,
    community: table.dataset.tipCommunity || label.community,
    headroom: table.dataset.tipHeadroom || label.headroom,
    github: table.dataset.tipGithub || label.github,
  };
  const nullTip = table.dataset.nullTip || '';
  const unranked = table.dataset.unranked || nullTip;
  const count = document.querySelector<HTMLElement>('#impact-count');
  const empty = document.querySelector<HTMLElement>('#impact-empty');
  const pageLabel = document.querySelector('#impact-page');
  const prev = document.querySelector<HTMLButtonElement>('#impact-prev');
  const next = document.querySelector<HTMLButtonElement>('#impact-next');
  const queryInput = document.querySelector<HTMLInputElement>('#impact-q');
  const domain = document.querySelector<HTMLSelectElement>('#impact-domain');
  const tabs = [...document.querySelectorAll<HTMLButtonElement>('[data-tier]')];
  const toolbar = document.querySelector<HTMLElement>('#impact-form');
  let tier = 'ranked';
  let page = 0;

  const syncBar = () => {
    if (toolbar) document.documentElement.style.setProperty('--toolbar', `${toolbar.offsetHeight}px`);
  };
  const named = (name: string, value: number | null) => (value == null ? `${name} ${nullTip}` : `${name} ${value}`);

  const draw = () => {
    const query = (queryInput?.value || '').trim().toLowerCase();
    const selected = domain?.value || '';
    const matched = rows.filter((row) => {
      if (row.tier !== tier) return false;
      if (selected && row.domain !== selected) return false;
      if (!query) return true;
      return `${row.name} ${row.id} ${row.domain}`.toLowerCase().includes(query);
    });
    const pages = Math.max(1, Math.ceil(matched.length / PAGE));
    if (page >= pages) page = pages - 1;
    if (page < 0) page = 0;
    const slice = matched.slice(page * PAGE, page * PAGE + PAGE);
    body.innerHTML = slice.map((row) => {
      const podium = row.tier === 'ranked' && row.rank != null && row.rank <= 3 ? `podium podium-${row.rank}` : '';
      const rank = row.rank == null
        ? `<span class="na" title="${esc(unranked)}">—</span>`
        : `<span class="rank-no">${row.rank}</span>`;
      const name = row.href ? `<a href="${esc(row.href)}">${esc(row.name)}</a>` : esc(row.name);
      const domainText = row.domain
        ? `<span class="domain-tag">${esc(row.domain)}</span>`
        : `<span class="na" title="${esc(nullTip)}">—</span>`;
      const score = row.score == null
        ? `<span class="na" title="${esc(nullTip)}">—</span>`
        : `<span class="score-wrap" title="${esc(row.score)}"><span class="score-num">${row.score.toFixed(1)}</span><span class="track" aria-hidden="true"><span style="width:${Math.max(0, Math.min(100, row.score))}%"></span></span></span>`;
      return `<tr class="${podium}">
        <td class="rank-cell" data-label="${esc(label.rank)}">${rank}</td>
        <td class="name-cell" data-label="${esc(label.name)}">${name}</td>
        <td data-label="${esc(label.domain)}">${domainText}</td>
        <td class="score-cell" data-label="${esc(label.score)}">${score}</td>
        ${metric(row.quality, named(tipName.quality, row.quality), label.quality)}
        ${metric(row.community, named(tipName.community, row.community), label.community)}
        ${metric(row.saturation, named(tipName.headroom, row.saturation), label.headroom)}
        ${metric(row.github, named(tipName.github, row.github), label.github)}
      </tr>`;
    }).join('');
    if (count) count.textContent = `${count.dataset.showing || ''} ${matched.length} ${count.dataset.unit || ''}`.replace(/\s+/g, ' ').trim();
    if (empty) empty.hidden = matched.length !== 0;
    if (pageLabel) pageLabel.textContent = `${page + 1} / ${pages}`;
    if (prev) prev.disabled = page <= 0;
    if (next) next.disabled = page >= pages - 1;
    syncBar();
  };

  queryInput?.addEventListener('input', () => { page = 0; draw(); });
  domain?.addEventListener('change', () => { page = 0; draw(); });
  prev?.addEventListener('click', () => { page -= 1; draw(); });
  next?.addEventListener('click', () => { page += 1; draw(); });
  for (const tab of tabs) {
    tab.addEventListener('click', () => {
      tier = tab.dataset.tier || 'ranked';
      for (const other of tabs) other.setAttribute('aria-selected', other === tab ? 'true' : 'false');
      page = 0;
      draw();
    });
  }
  document.querySelector('#impact-form')?.addEventListener('submit', (event) => event.preventDefault());
  window.addEventListener('resize', syncBar);
  draw();
}
