# 维护与重新发布

网站是静态的。构建时读取仓库里的 `data/`、`content/benchmarks/` 和 `CONSTITUTION.md`，生成 HTML，并把原始 JSON 复制到站点上。浏览器里没有另一份会变的数据库。

日常更新数据：改文件，推到 `main`。GitHub Actions 会安装依赖、校验数据、生成网站，并发布到 GitHub Pages。不需要改页面代码，也不要在仓库里添加密钥。

## 地址

- 网站：https://zichenwang114514.github.io/benchmark-constitution/
- 一条档案：https://zichenwang114514.github.io/benchmark-constitution/benchmarks/gpqa/
- 宪法：https://zichenwang114514.github.io/benchmark-constitution/constitution/
- 接口说明：https://zichenwang114514.github.io/benchmark-constitution/api/
- 原始 JSON：https://zichenwang114514.github.io/benchmark-constitution/api/benchmarks/gpqa.json

站点前缀是 `/benchmark-constitution/`。如果仓库改名，要同时改 `site/astro.config.mjs` 里的 `site` 和 `base`。

## 改哪些文件

- `data/benchmarks/<id>.json`：十一节字段。事实写成 `{ "value", "sources": [{ "url", "accessed" }] }`，需要时加上 `status` 和 `note`。没核验完写 `待核实`；确认没有公开才写 `未公开`。
- `data/index.json`：首页卡片用的名称、板块、标签、摘要和 Drive 链接。新增基准要在这里登记。
- `content/benchmarks/<id>.md`：同名中文介绍。接口会原样提供这份原稿。
- `data/news.json`：首页动态。`observed_date` 是观察日；事件日期没有证实时写 `待核实`，不要写成“今天发布”。
- `data/trending.json`：近期热门。每条要有 `slug`、`name`、`heat_confidence`（A 或 B）、`rationale`，以及至少一条带来源地址的 `evidence`。还没有 `data/benchmarks/<slug>.json` 时，站点只展示证据链接，不链到不存在的档案页。
- `CONSTITUTION.md`：宪法页面和 `/api/constitution.md`。
- `data/drive-manifest.json`、`data/quality-report.json`、`data/master-index.csv`：随只读接口一起发布。

`id` 只用小写字母、数字和连字符。索引里的 `json`、`content` 路径要分别是 `data/benchmarks/<id>.json` 和 `content/benchmarks/<id>.md`。

构建会检查：索引和文件是否一一对应、文件内 `id` 是否一致、十一节和 `drive_pdf`、`changelog` 是否都在、每条事实是否至少有一条带来源地址和访问日期的来源。校验失败时，Actions 不会发布半成品。

次要板块（语言、推理、数学、代码、多模态、Agent、安全）在没有条目时只显示为待收录。某条记录的 `section` 一旦写成这些名字，首页会自动把它收进板块导航，不再留在虚线占位里。

## 本地预览

```bash
cd site
npm install
npm run dev
```

打开 http://127.0.0.1:4321/benchmark-constitution/

发布前可以先在本地构建并校验：

```bash
npm run build
npm run check
npm run preview
```

`npm run build` 会先把数据复制到 `site/public/api/`。这个目录和 `site/dist/` 都是生成的，不要提交，下一次构建会覆盖。

## 发布

工作流在 `.github/workflows/pages.yml`。

- 推送到 `main`，或在 Actions 里手动运行，会构建并发布。
- 拉取请求只构建和校验，不覆盖正式站点。
- 权限只有 `contents: read`、`pages: write`、`id-token: write`。部署用 Actions 自带的 `GITHUB_TOKEN`，通过官方的 Pages actions 完成。不要添加 `secrets`。

仓库的 Pages 来源需要是 GitHub Actions：

```bash
gh api repos/ZiChenWang114514/benchmark-constitution/pages -X POST -f build_type=workflow
```

如果 Pages 已经开过，改用更新：

```bash
gh api repos/ZiChenWang114514/benchmark-constitution/pages -X PUT -f build_type=workflow
```

发布完成后，上面的网站、详情页和 JSON 地址应返回 200。JSON 正文以 `{` 开头；详情页应能看到该基准的名称和「待核实」。

## 不做什么

- 不把论文 PDF 放进仓库。页面链接到 Drive 里的原件。
- 不在页面里估算、补全或覆盖数据里的待核实字段。
- 不手改 `site/dist` 或 `site/public/api`。
