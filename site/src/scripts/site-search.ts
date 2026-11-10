import { filterSearchIndex, type SearchHit } from '../lib/search-match';

type SearchIndex = { items: SearchHit[] };

const cache = new Map<string, Promise<SearchHit[]>>();
const DROPDOWN_LIMIT = 8;

function indexUrl(node: HTMLElement): string {
  return node.dataset.index || '';
}

function loadIndex(url: string): Promise<SearchHit[]> {
  const existing = cache.get(url);
  if (existing) return existing;
  const request = fetch(url)
    .then((response) => {
      if (!response.ok) throw new Error('search index missing');
      return response.json() as Promise<SearchIndex>;
    })
    .then((data) => data.items ?? [])
    .catch(() => []);
  cache.set(url, request);
  return request;
}

function isTypingTarget(target: EventTarget | null): boolean {
  if (!(target instanceof HTMLElement)) return false;
  if (target.isContentEditable) return true;
  const tag = target.tagName;
  return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT';
}

function subtitle(item: SearchHit): string {
  const parts = [item.domain, item.organization, item.aliases.slice(0, 2).join(', ')].filter(Boolean);
  return parts.slice(0, 2).join(', ');
}

function fillList(list: HTMLElement, items: SearchHit[], active: number, prefix: string): void {
  list.replaceChildren();
  items.forEach((item, index) => {
    const option = document.createElement('a');
    option.className = 'site-search-hit';
    option.id = `${prefix}-${index}`;
    option.href = item.href;
    option.setAttribute('role', 'option');
    option.setAttribute('aria-selected', index === active ? 'true' : 'false');
    const name = document.createElement('strong');
    name.textContent = item.name;
    const meta = document.createElement('span');
    meta.textContent = subtitle(item);
    option.append(name, meta);
    list.append(option);
  });
}

function currentHits(list: HTMLElement): HTMLAnchorElement[] {
  return [...list.querySelectorAll<HTMLAnchorElement>('.site-search-hit')];
}

function setActive(list: HTMLElement, input: HTMLInputElement, index: number): number {
  const hits = currentHits(list);
  if (!hits.length) {
    input.removeAttribute('aria-activedescendant');
    return -1;
  }
  const next = (index + hits.length) % hits.length;
  hits.forEach((hit, i) => hit.setAttribute('aria-selected', i === next ? 'true' : 'false'));
  const active = hits[next];
  if (active) {
    input.setAttribute('aria-activedescendant', active.id);
    active.scrollIntoView({ block: 'nearest' });
  }
  return next;
}

function openHit(list: HTMLElement, index: number): boolean {
  const hits = currentHits(list);
  const target = hits[index] ?? hits[0];
  if (!target) return false;
  target.click();
  return true;
}

function initHeaderSearch(root: HTMLElement) {
  const form = root.querySelector<HTMLFormElement>('.site-search-form');
  const input = root.querySelector<HTMLInputElement>('.site-search-input');
  const panel = root.querySelector<HTMLElement>('.site-search-panel');
  const list = root.querySelector<HTMLElement>('.site-search-results');
  const empty = root.querySelector<HTMLElement>('.site-search-empty');
  const more = root.querySelector<HTMLAnchorElement>('[data-search-more]');
  const toggle = root.querySelector<HTMLButtonElement>('.search-toggle');
  const header = document.querySelector<HTMLElement>('.site-header');
  if (!form || !input || !panel || !list || !empty) return;

  let items: SearchHit[] = [];
  let ready = false;
  let active = -1;
  let open = false;

  const setExpanded = (value: boolean) => {
    open = value;
    panel.hidden = !value;
    input.setAttribute('aria-expanded', value ? 'true' : 'false');
    root.classList.toggle('is-open', value);
  };

  const setSheet = (value: boolean) => {
    root.classList.toggle('is-sheet', value);
    header?.classList.toggle('search-open', value);
    if (toggle) {
      toggle.setAttribute('aria-expanded', value ? 'true' : 'false');
      const close = toggle.dataset.close || '';
      const openLabel = toggle.dataset.open || '';
      if (close && openLabel) toggle.textContent = value ? close : openLabel;
    }
    if (value) input.focus();
  };

  const render = (query: string) => {
    const hits = filterSearchIndex(items, query).slice(0, DROPDOWN_LIMIT);
    const hasQuery = query.trim().length > 0;
    fillList(list, hits, -1, 'site-hit');
    active = hits.length ? 0 : -1;
    if (active >= 0) setActive(list, input, active);
    empty.hidden = !hasQuery || hits.length > 0;
    if (more) {
      const href = new URL(form.action, window.location.href);
      if (hasQuery) href.searchParams.set('q', query.trim());
      else href.searchParams.delete('q');
      more.href = href.pathname + href.search + href.hash;
      more.hidden = !hasQuery;
    }
    setExpanded(hasQuery && ready);
  };

  const ensure = () => {
    if (ready) return Promise.resolve(items);
    return loadIndex(indexUrl(root)).then((data) => {
      items = data;
      ready = true;
      return items;
    });
  };

  input.addEventListener('focus', () => {
    void ensure().then(() => {
      if (input.value.trim()) render(input.value);
    });
  });
  input.addEventListener('input', () => {
    void ensure().then(() => render(input.value));
  });
  input.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowDown') {
      event.preventDefault();
      active = setActive(list, input, active < 0 ? 0 : active + 1);
    } else if (event.key === 'ArrowUp') {
      event.preventDefault();
      active = setActive(list, input, active < 0 ? 0 : active - 1);
    } else if (event.key === 'Enter') {
      if (open && openHit(list, active)) event.preventDefault();
    } else if (event.key === 'Escape') {
      event.preventDefault();
      setExpanded(false);
      setSheet(false);
      input.blur();
    }
  });
  form.addEventListener('submit', (event) => {
    if (open && openHit(list, active)) event.preventDefault();
  });
  document.addEventListener('click', (event) => {
    if (!root.contains(event.target as Node)) {
      setExpanded(false);
    }
  });
  toggle?.addEventListener('click', () => {
    const next = !root.classList.contains('is-sheet');
    setSheet(next);
    if (next) void ensure();
    else setExpanded(false);
  });

  window.addEventListener('keydown', (event) => {
    const slash = event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey;
    const chord = event.key.toLowerCase() === 'k' && (event.ctrlKey || event.metaKey) && !event.altKey;
    if (!slash && !chord) return;
    if (slash && isTypingTarget(event.target)) return;
    event.preventDefault();
    if (window.matchMedia('(max-width: 860px)').matches) setSheet(true);
    input.focus();
    input.select();
    void ensure();
  });
}

function card(item: SearchHit): HTMLAnchorElement {
  const link = document.createElement('a');
  link.className = 'card';
  link.href = item.href;
  const domain = document.createElement('span');
  domain.className = 'card-section';
  const tag = document.createElement('span');
  tag.className = 'domain-tag';
  tag.textContent = item.domain;
  domain.append(tag);
  const title = document.createElement('h3');
  title.textContent = item.name;
  link.append(domain, title);
  if (item.organization) {
    const org = document.createElement('p');
    org.className = 'card-summary';
    org.textContent = item.organization;
    link.append(org);
  }
  if (item.tags.length) {
    const tags = document.createElement('p');
    tags.className = 'card-tags';
    tags.textContent = item.tags.join(', ');
    link.append(tags);
  }
  return link;
}

function initSearchPage(root: HTMLElement) {
  const form = root.querySelector<HTMLFormElement>('.search-page-form');
  const input = root.querySelector<HTMLInputElement>('#search-q');
  const count = root.querySelector<HTMLElement>('[data-search-count]');
  const status = root.querySelector<HTMLElement>('[data-search-status]');
  const list = root.querySelector<HTMLElement>('[data-search-list]');
  if (!form || !input || !count || !status || !list) return;

  const params = new URLSearchParams(window.location.search);
  if (params.get('q') && !input.value) input.value = params.get('q') ?? '';

  const paint = (query: string, items: SearchHit[]) => {
    const hits = query.trim() ? filterSearchIndex(items, query) : [];
    list.replaceChildren(...hits.map(card));
    if (!query.trim()) {
      count.textContent = '';
      status.hidden = false;
      status.textContent = root.dataset.prompt || '';
      return;
    }
    count.textContent = (root.dataset.count || '{n}').replaceAll('{n}', String(hits.length));
    const title = document.querySelector('.page-hero h1');
    if (title && root.dataset.resultsFor) title.textContent = root.dataset.resultsFor.replaceAll('{q}', query.trim());
    status.hidden = hits.length > 0;
    status.textContent = hits.length ? '' : (root.dataset.empty || '');
  };

  void loadIndex(indexUrl(root)).then((items) => {
    const run = () => paint(input.value, items);
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const next = new URL(window.location.href);
      const query = input.value.trim();
      if (query) next.searchParams.set('q', query);
      else next.searchParams.delete('q');
      history.replaceState(null, '', next.pathname + next.search);
      run();
    });
    input.addEventListener('input', () => {
      const next = new URL(window.location.href);
      const query = input.value.trim();
      if (query) next.searchParams.set('q', query);
      else next.searchParams.delete('q');
      history.replaceState(null, '', next.pathname + next.search);
      run();
    });
    run();
  });
}

function init() {
  document.querySelectorAll<HTMLElement>('[data-search]').forEach(initHeaderSearch);
  document.querySelectorAll<HTMLElement>('[data-search-page]').forEach(initSearchPage);
}

init();
