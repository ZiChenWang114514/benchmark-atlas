const PAGE = 40;

function mountMatrix(): void {
  const table = document.querySelector<HTMLTableElement>('#heat-matrix');
  const tip = document.querySelector<HTMLElement>('#heat-tip');
  if (!table || !tip) return;
  const cells = [...table.querySelectorAll<HTMLButtonElement>('.heat-cell')];
  if (!cells.length) return;
  let current = cells.findIndex((cell) => cell.tabIndex === 0);
  if (current < 0) current = 0;
  let shownAt = 0;

  const columns = () => {
    const first = table.querySelector('tbody tr');
    return first ? first.querySelectorAll<HTMLButtonElement>('.heat-cell').length : 0;
  };

  const clear = () => {
    table.querySelectorAll('.is-hot').forEach((node) => node.classList.remove('is-hot'));
  };

  const place = (cell: HTMLButtonElement) => {
    const text = cell.getAttribute('aria-label') || '';
    tip.textContent = text;
    tip.hidden = false;
    const rect = cell.getBoundingClientRect();
    const width = Math.min(tip.offsetWidth, window.innerWidth - 16);
    let left = rect.left + rect.width / 2 - width / 2;
    left = Math.max(8, Math.min(left, window.innerWidth - width - 8));
    let top = rect.bottom + 8;
    if (top + tip.offsetHeight > window.innerHeight - 8) top = Math.max(8, rect.top - tip.offsetHeight - 8);
    tip.style.left = `${left}px`;
    tip.style.top = `${top}px`;
  };

  const hide = () => {
    tip.hidden = true;
    clear();
  };

  const show = (cell: HTMLButtonElement) => {
    clear();
    const row = cell.closest('tr');
    const col = cell.dataset.col;
    row?.classList.add('is-hot');
    if (col != null) table.querySelectorAll(`[data-col="${col}"]`).forEach((node) => node.classList.add('is-hot'));
    tip.dataset.for = cell.getAttribute('aria-label') || '';
    shownAt = performance.now();
    place(cell);
  };

  const move = (next: number) => {
    if (next < 0 || next >= cells.length) return;
    cells[current]?.setAttribute('tabindex', '-1');
    current = next;
    const cell = cells[current];
    cell.setAttribute('tabindex', '0');
    cell.focus();
    show(cell);
  };

  const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const hoverCell = (event: Event) => {
    if (!fine) return;
    const cell = (event.target as HTMLElement | null)?.closest<HTMLButtonElement>('.heat-cell');
    if (cell) show(cell);
  };
  table.addEventListener('pointerover', hoverCell);
  table.addEventListener('mouseover', hoverCell);
  table.addEventListener('pointerleave', () => {
    if (fine) hide();
  });
  table.addEventListener('mouseleave', () => {
    if (fine) hide();
  });
  table.addEventListener('focusin', (event) => {
    if (!fine) return;
    const cell = (event.target as HTMLElement | null)?.closest<HTMLButtonElement>('.heat-cell');
    if (cell) show(cell);
  });
  table.addEventListener('click', (event) => {
    if (fine) return;
    const cell = (event.target as HTMLElement | null)?.closest<HTMLButtonElement>('.heat-cell');
    if (!cell) return;
    const same = !tip.hidden && tip.dataset.for === (cell.getAttribute('aria-label') || '');
    if (same) hide();
    else show(cell);
  });
  table.addEventListener('keydown', (event) => {
    const cell = (event.target as HTMLElement | null)?.closest<HTMLButtonElement>('.heat-cell');
    if (!cell) return;
    const width = columns();
    const index = cells.indexOf(cell);
    if (index < 0 || !width) return;
    let next = index;
    if (event.key === 'ArrowRight') next = index + 1;
    else if (event.key === 'ArrowLeft') next = index - 1;
    else if (event.key === 'ArrowDown') next = index + width;
    else if (event.key === 'ArrowUp') next = index - width;
    else if (event.key === 'Home') next = index - (index % width);
    else if (event.key === 'End') next = index - (index % width) + width - 1;
    else if (event.key === 'Escape') {
      hide();
      return;
    } else return;
    event.preventDefault();
    move(Math.max(0, Math.min(cells.length - 1, next)));
  });
  const scroller = table.closest('.matrix-scroll');
  scroller?.addEventListener('scroll', () => {
    if (performance.now() - shownAt < 180) return;
    hide();
  }, { passive: true });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') hide();
  });
}

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
  mountMatrix();
}
