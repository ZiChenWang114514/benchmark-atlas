function pressedSection(form: HTMLFormElement): string {
  const current = form.querySelector<HTMLButtonElement>('[data-section-chip][aria-pressed="true"]');
  return current?.dataset.sectionChip || form.dataset.all || 'all';
}

function apply(writeUrl: boolean) {
  const form = document.querySelector<HTMLFormElement>('#browse-form');
  if (!form) return;
  const queryInput = form.querySelector<HTMLInputElement>('#q');
  const tagSelect = form.querySelector<HTMLSelectElement>('#tag');
  const sortSelect = form.querySelector<HTMLSelectElement>('#sort');
  const count = document.querySelector('#result-count');
  const empty = document.querySelector<HTMLElement>('#empty');
  const tail = document.querySelector<HTMLElement>('#tail');
  if (!queryInput || !tagSelect || !sortSelect || !count || !empty || !tail) return;

  const all = form.dataset.all || 'all';
  const query = queryInput.value.trim().toLowerCase();
  const section = pressedSection(form);
  const tag = tagSelect.value;
  const mode = sortSelect.value;
  const cards = [...document.querySelectorAll<HTMLElement>('[data-card]')];
  const groups = [...document.querySelectorAll<HTMLElement>('[data-group]')];
  const visible = new Set<string>();
  let shown = 0;

  for (const card of cards) {
    const tags = (card.dataset.tags ?? '').split('|').filter(Boolean);
    const match =
      (!query || (card.dataset.search ?? '').includes(query)) &&
      (section === all || card.dataset.section === section) &&
      (!tag || tags.includes(tag));
    card.hidden = !match;
    if (match) {
      shown += 1;
      if (card.dataset.section) visible.add(card.dataset.section);
    }
  }

  for (const group of groups) group.hidden = !visible.has(group.dataset.group ?? '');

  for (const group of groups) {
    const grid = group.querySelector<HTMLElement>('[data-grid]');
    if (!grid) continue;
    const list = [...grid.querySelectorAll<HTMLElement>('[data-card]')];
    list.sort((a, b) => {
      if (mode === 'name') return (a.dataset.name ?? '').localeCompare(b.dataset.name ?? '', form.dataset.locale === 'zh' ? 'zh' : 'en');
      if (mode === 'date') {
        const left = a.dataset.date ?? '';
        const right = b.dataset.date ?? '';
        if (left !== right) {
          if (!left) return 1;
          if (!right) return -1;
          return right.localeCompare(left);
        }
      }
      return Number(a.dataset.order ?? 0) - Number(b.dataset.order ?? 0);
    });
    for (const card of list) grid.append(card);
  }

  const template = form.dataset.countTemplate || '{total} / {shown}';
  count.textContent = template.replaceAll('{total}', String(cards.length)).replaceAll('{shown}', String(shown));
  empty.hidden = shown !== 0;
  tail.hidden = query !== '' || section !== all || tag !== '';

  if (!writeUrl) return;
  const params = new URLSearchParams();
  if (query) params.set('q', queryInput.value.trim());
  if (section !== (form.dataset.all || 'all')) params.set('section', section);
  if (tag) params.set('tag', tag);
  if (mode !== 'section') params.set('sort', mode);
  const search = params.toString();
  const next = search ? `${location.pathname}?${search}${location.hash}` : `${location.pathname}${location.hash}`;
  history.replaceState(null, '', next);
}

function initBrowse() {
  const form = document.querySelector<HTMLFormElement>('#browse-form');
  if (!form) return;
  const params = new URLSearchParams(location.search);
  const queryInput = form.querySelector<HTMLInputElement>('#q');
  const tagSelect = form.querySelector<HTMLSelectElement>('#tag');
  const sortSelect = form.querySelector<HTMLSelectElement>('#sort');
  const chips = [...form.querySelectorAll<HTMLButtonElement>('[data-section-chip]')];
  if (queryInput && params.get('q')) queryInput.value = params.get('q') ?? '';
  if (tagSelect && [...tagSelect.options].some((option) => option.value === params.get('tag'))) {
    tagSelect.value = params.get('tag') ?? '';
  }
  if (sortSelect && [...sortSelect.options].some((option) => option.value === params.get('sort'))) {
    sortSelect.value = params.get('sort') ?? 'section';
  }
  const section = params.get('section');
  if (section && chips.some((chip) => chip.dataset.sectionChip === section)) {
    for (const chip of chips) chip.setAttribute('aria-pressed', chip.dataset.sectionChip === section ? 'true' : 'false');
  }
  const run = () => apply(true);
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    run();
  });
  queryInput?.addEventListener('input', run);
  tagSelect?.addEventListener('change', run);
  sortSelect?.addEventListener('change', run);
  for (const chip of chips) {
    chip.addEventListener('click', () => {
      for (const other of chips) other.setAttribute('aria-pressed', other === chip ? 'true' : 'false');
      run();
    });
  }
  form.querySelector('#reset')?.addEventListener('click', () => {
    if (queryInput) queryInput.value = '';
    if (tagSelect) tagSelect.value = '';
    if (sortSelect) sortSelect.value = 'section';
    const all = form.dataset.all || 'all';
    for (const chip of chips) chip.setAttribute('aria-pressed', chip.dataset.sectionChip === all ? 'true' : 'false');
    run();
  });
  apply(false);
}

initBrowse();
