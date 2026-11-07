export function bindToc(nav: ParentNode) {
  const links = [...nav.querySelectorAll<HTMLAnchorElement>('a[href^="#"]')];
  const heads: Element[] = [];
  const byHead = new Map<Element, HTMLAnchorElement>();
  for (const link of links) {
    const id = decodeURIComponent(link.getAttribute('href')?.slice(1) ?? '');
    const head = document.getElementById(id);
    if (!head) continue;
    heads.push(head);
    byHead.set(head, link);
  }
  if (!heads.length || typeof IntersectionObserver === 'undefined') return;
  const mark = (head: Element) => {
    for (const link of links) link.removeAttribute('aria-current');
    byHead.get(head)?.setAttribute('aria-current', 'true');
  };
  mark(heads[0]);
  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible) mark(visible.target);
    },
    { rootMargin: '-25% 0px -55% 0px', threshold: [0, 0.25, 1] },
  );
  for (const head of heads) observer.observe(head);
}
