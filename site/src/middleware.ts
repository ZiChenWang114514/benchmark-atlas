import { defineMiddleware } from 'astro:middleware';
import { localeFromPathname, runWithLocale } from './i18n';

export const onRequest = defineMiddleware((context, next) => {
  const locale = localeFromPathname(context.url.pathname);
  context.locals.locale = locale;
  return runWithLocale(locale, () => next());
});
