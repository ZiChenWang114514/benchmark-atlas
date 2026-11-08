const PAGE = 40;

export function mountHeatBoard(): void {
  const all = [...document.querySelectorAll<HTMLTableRowElement>('[data-heat-row]')];
  if (!all.length) return;
  const queryInput = document.querySelector<HTMLInputElement>('#heat-q');
  const domain = document.querySelector<HTMLSelectElement>('#heat-domain');
  const count = document.querySelector<HTMLElement>('#heat-count');
  const empty = document.querySelector<HTMLElement>('#heat-empty');
  const pageLabel = document.querySelector('#heat-page');
  const prev = document.querySelector<HTMLButtonElement>('#heat-prev');
  const next = document.querySelector<HTMLButtonElement>('#heat-next');
  const toolbar = document.querySelector<HTMLElement>('#heat-form');
  let page = 0;

  const draw = () => {
    const query = (queryInput?.value || '').trim().toLowerCase();
    const selected = domain?.value || '';
    const matched = all.filter((row) => {
      if (selected && row.dataset.domain !== selected) return false;
      if (query && !(row.dataset.search || '').includes(query)) return false;
      return true;
    });
    const pages = Math.max(1, Math.ceil(matched.length / PAGE));
    if (page >= pages) page = pages - 1;
    if (page < 0) page = 0;
    const visible = new Set(matched.slice(page * PAGE, page * PAGE + PAGE));
    for (const row of all) row.hidden = !visible.has(row);
    if (count) count.textContent = `${count.dataset.showing || ''} ${matched.length} ${count.dataset.unit || ''}`.replace(/\s+/g, ' ').trim();
    if (empty) empty.hidden = matched.length !== 0;
    if (pageLabel) pageLabel.textContent = `${page + 1} / ${pages}`;
    if (prev) prev.disabled = page <= 0;
    if (next) next.disabled = page >= pages - 1;
    if (toolbar) document.documentElement.style.setProperty('--toolbar', `${toolbar.offsetHeight}px`);
  };

  queryInput?.addEventListener('input', () => { page = 0; draw(); });
  domain?.addEventListener('change', () => { page = 0; draw(); });
  prev?.addEventListener('click', () => { page -= 1; draw(); });
  next?.addEventListener('click', () => { page += 1; draw(); });
  document.querySelector('#heat-form')?.addEventListener('submit', (event) => event.preventDefault());
  window.addEventListener('resize', draw);
  draw();
}
