import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

function zhRoutes() {
  const routes = [
    ['/zh', './src/pages/index.astro'],
    ['/zh/trending', './src/pages/trending.astro'],
    ['/zh/frontier-heat', './src/pages/frontier-heat.astro'],
    ['/zh/impact', './src/pages/impact/index.astro'],
    ['/zh/impact/method', './src/pages/impact/method.astro'],
    ['/zh/registry', './src/pages/registry.astro'],
    ['/zh/constitution', './src/pages/constitution.astro'],
    ['/zh/benchmarks/[id]', './src/pages/benchmarks/[id].astro'],
  ];
  return {
    name: 'zh-routes',
    hooks: {
      'astro:config:setup'({ injectRoute }) {
        for (const [pattern, entrypoint] of routes) {
          injectRoute({ pattern, entrypoint, prerender: true });
        }
      },
    },
  };
}

function syncPublicApi() {
  return {
    name: 'sync-public-api',
    hooks: {
      'astro:config:setup'() {
        const script = fileURLToPath(new URL('./scripts/sync-api.mjs', import.meta.url));
        const result = spawnSync(process.execPath, [script], { stdio: 'inherit' });
        if (result.status !== 0) {
          throw new Error(`sync-api.mjs 退出码 ${result.status ?? 'null'}`);
        }
      },
    },
  };
}

// GitHub Pages project site. `base` must stay in sync with the repository name.
export default defineConfig({
  site: 'https://zichenwang114514.github.io',
  base: '/benchmark-constitution',
  trailingSlash: 'always',
  integrations: [
    syncPublicApi(),
    zhRoutes(),
    sitemap({
      i18n: {
        defaultLocale: 'en',
        locales: { en: 'en', zh: 'zh-Hans' },
      },
    }),
  ],
  build: {
    format: 'directory',
  },
});
