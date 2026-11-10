import type { APIRoute } from 'astro';
import { currentLocale } from '../i18n';
import { buildSearchIndex } from '../lib/search';

export const prerender = true;

export const GET: APIRoute = () => {
  const body = JSON.stringify(buildSearchIndex(currentLocale()));
  return new Response(body, {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
    },
  });
};
