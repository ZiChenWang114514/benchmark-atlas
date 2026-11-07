import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

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
  base: '/benchmark-atlas',
  trailingSlash: 'always',
  integrations: [syncPublicApi(), sitemap()],
  build: {
    format: 'directory',
  },
});
