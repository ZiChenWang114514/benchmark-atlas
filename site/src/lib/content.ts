import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { Marked } from 'marked';
import { repoRoot } from './data';

export type TocItem = { id: string; text: string };

function escapeHtml(value: string): string {
  return value.replace(/[&<>"']/g, (char) => {
    switch (char) {
      case '&':
        return '&amp;';
      case '<':
        return '&lt;';
      case '>':
        return '&gt;';
      case '"':
        return '&quot;';
      default:
        return '&#39;';
    }
  });
}

export function loadConstitution(): { title: string; html: string; toc: TocItem[] } {
  const markdown = readFileSync(join(repoRoot(), 'CONSTITUTION.md'), 'utf8');
  const title = markdown.match(/^#\s+(.+)\s*$/m)?.[1]?.trim() ?? '收集宪法';
  const body = markdown.replace(/^#\s+.+\s*$/m, '').trim();
  const toc: TocItem[] = [];
  let count = 0;
  const marked = new Marked();
  marked.use({
    gfm: true,
    renderer: {
      html({ text }) {
        return escapeHtml(text);
      },
      heading({ text, depth }) {
        const plain = String(text).replace(/<[^>]+>/g, '');
        if (depth < 2) return `<h${depth}>${escapeHtml(plain)}</h${depth}>\n`;
        const id = `c${++count}`;
        if (depth === 2) toc.push({ id, text: plain });
        return `<h${depth} id="${id}">${escapeHtml(plain)}</h${depth}>\n`;
      },
    },
  });
  const parsed = marked.parse(body, { async: false });
  if (typeof parsed !== 'string') {
    throw new Error('宪法 Markdown 没有同步渲染');
  }
  return { title, html: parsed, toc };
}

export function renderMarkdownDocument(markdown: string): string {
  const marked = new Marked();
  marked.use({
    gfm: true,
    renderer: {
      html({ text }) {
        return escapeHtml(text);
      },
    },
  });
  const parsed = marked.parse(markdown, { async: false });
  if (typeof parsed !== 'string') throw new Error('Markdown 没有同步渲染');
  return parsed;
}
