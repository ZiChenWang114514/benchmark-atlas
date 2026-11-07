import { mkdirSync, readFileSync, writeFileSync, rmSync, statSync, readdirSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const repoRoot = resolve(siteRoot, '..');
const outDir = join(siteRoot, 'public', 'api');

const CHAPTERS = [
  'basic_info',
  'organization',
  'design_goals',
  'construction',
  'data_format',
  'evaluation',
  'latest_status',
  'leaderboard',
  'contact',
  'original_files',
];

function readJson(path) {
  return JSON.parse(readFileSync(path, 'utf8'));
}

function fail(errors) {
  console.error('数据校验失败：');
  for (const error of errors.slice(0, 40)) console.error(` - ${error}`);
  if (errors.length > 40) console.error(` - 另有 ${errors.length - 40} 条`);
  process.exit(1);
}

function walkFields(node, path, errors) {
  if (Array.isArray(node) || !node || typeof node !== 'object') return;
  if ('value' in node && 'sources' in node) {
    if (!Array.isArray(node.sources) || node.sources.length < 1) {
      errors.push(`${path} 缺少来源`);
      return;
    }
    node.sources.forEach((source, index) => {
      if (!source || typeof source.url !== 'string' || !source.url) errors.push(`${path}.sources[${index}] 缺少 url`);
      if (!source || typeof source.accessed !== 'string' || !source.accessed) errors.push(`${path}.sources[${index}] 缺少 accessed`);
    });
    return;
  }
  for (const [key, value] of Object.entries(node)) walkFields(value, path ? `${path}.${key}` : key, errors);
}

const errors = [];
const index = readJson(join(repoRoot, 'data/index.json'));
const news = readJson(join(repoRoot, 'data/news.json'));
if (!Array.isArray(index.benchmarks)) errors.push('data/index.json 缺少 benchmarks 数组');
if (index.count != null && index.count !== index.benchmarks.length) {
  errors.push(`index.count 为 ${index.count}，实际 ${index.benchmarks.length} 条`);
}
if (!Array.isArray(news)) errors.push('data/news.json 应该是数组');

const ids = new Set();
for (const item of index.benchmarks ?? []) {
  if (!item?.id || !/^[a-z0-9-]+$/.test(item.id)) errors.push(`非法 id：${item?.id}`);
  if (ids.has(item.id)) errors.push(`重复 id：${item.id}`);
  ids.add(item.id);
  if (item.json !== `data/benchmarks/${item.id}.json`) errors.push(`${item.id} 的 json 路径不符合 data/benchmarks/${item.id}.json`);
  if (item.content !== `content/benchmarks/${item.id}.md`) errors.push(`${item.id} 的 content 路径不符合约定`);
  const jsonPath = join(repoRoot, 'data/benchmarks', `${item.id}.json`);
  const mdPath = join(repoRoot, 'content/benchmarks', `${item.id}.md`);
  if (!existsSync(jsonPath)) errors.push(`缺少 ${item.id}.json`);
  if (!existsSync(mdPath)) errors.push(`缺少 ${item.id}.md`);
  if (!existsSync(jsonPath)) continue;
  const record = readJson(jsonPath);
  if (record.id !== item.id) errors.push(`${item.id} 文件内 id 为 ${record.id}`);
  if (typeof record.basic_info?.name?.value !== 'string' || !record.basic_info.name.value) errors.push(`${item.id} 缺少名称`);
  if (typeof record.basic_info?.section?.value !== 'string') errors.push(`${item.id} 缺少板块`);
  for (const key of [...CHAPTERS, 'drive_pdf', 'changelog']) {
    if (!record[key] || typeof record[key] !== 'object') errors.push(`${item.id} 缺少 ${key}`);
  }
  walkFields(record, item.id, errors);
}

const benchmarkFiles = readdirSync(join(repoRoot, 'data/benchmarks')).filter((name) => name.endsWith('.json'));
for (const file of benchmarkFiles) {
  if (!ids.has(file.replace(/\.json$/, ''))) errors.push(`索引未收录 data/benchmarks/${file}`);
}
const contentFiles = readdirSync(join(repoRoot, 'content/benchmarks')).filter((name) => name.endsWith('.md'));
for (const file of contentFiles) {
  if (!ids.has(file.replace(/\.md$/, ''))) errors.push(`索引未收录 content/benchmarks/${file}`);
}

for (const item of news ?? []) {
  if (!item?.id) errors.push('动态缺少 id');
  if (!item?.title || !item?.body || !item?.observed_date) errors.push(`动态 ${item?.id ?? ''} 缺少标题、正文或观察日`);
  if (!Array.isArray(item?.sources) || item.sources.length < 1) errors.push(`动态 ${item?.id ?? ''} 缺少来源`);
}

if (!existsSync(join(repoRoot, 'CONSTITUTION.md'))) errors.push('缺少 CONSTITUTION.md');
if (!existsSync(join(repoRoot, 'schema/benchmark.schema.json'))) errors.push('缺少 schema');

const trendingPath = join(repoRoot, 'data/trending.json');
if (!existsSync(trendingPath)) {
  errors.push('缺少 data/trending.json');
} else {
  const trending = readJson(trendingPath);
  if (!Array.isArray(trending.items) || trending.items.length < 1) errors.push('data/trending.json 缺少 items');
  const slugs = new Set();
  for (const item of trending.items ?? []) {
    if (!item?.slug || typeof item.slug !== 'string') errors.push('热门条目缺少 slug');
    else if (slugs.has(item.slug)) errors.push(`热门 slug 重复：${item.slug}`);
    else slugs.add(item.slug);
    if (!item?.name) errors.push(`${item?.slug ?? '热门条目'} 缺少 name`);
    if (item?.heat_confidence !== 'A' && item?.heat_confidence !== 'B') {
      errors.push(`${item?.slug ?? '热门条目'} 的 heat_confidence 必须是 A 或 B`);
    }
    if (!item?.rationale || typeof item.rationale !== 'string') errors.push(`${item?.slug ?? '热门条目'} 缺少 rationale`);
    const urls = (item?.evidence ?? []).filter((entry) => entry && typeof entry.url === 'string' && entry.url);
    if (urls.length < 1) errors.push(`${item?.slug ?? '热门条目'} 至少需要一条证据 url`);
  }
}
if (errors.length) fail(errors);

rmSync(outDir, { recursive: true, force: true });
mkdirSync(join(outDir, 'benchmarks'), { recursive: true });
mkdirSync(join(outDir, 'content'), { recursive: true });
mkdirSync(join(outDir, 'schema'), { recursive: true });

const resources = [];
function publish(from, to, description, group, page) {
  writeFileSync(join(outDir, to), readFileSync(from));
  resources.push({
    path: to,
    description,
    bytes: statSync(join(outDir, to)).size,
    group,
    ...(page ? { page } : {}),
  });
}

publish(join(repoRoot, 'data/index.json'), 'index.json', '导航索引：名称、主板块、标签、摘要、来源和 Drive 链接。', 'overview');
publish(join(repoRoot, 'data/news.json'), 'news.json', '最新动态。观察日和事件日分开；没有证实的事件日写“待核实”。', 'overview');
publish(join(repoRoot, 'data/trending.json'), 'trending.json', '近期热门。heat_confidence 为 A 或 B；没有对应档案的 slug 不会因此构建失败。', 'overview');
publish(join(repoRoot, 'data/drive-manifest.json'), 'drive-manifest.json', 'Drive 总目录、宪法文档、总表，以及每条基准的 PDF 和介绍文档。', 'overview');
publish(join(repoRoot, 'data/quality-report.json'), 'quality-report.json', '校验摘要、待核实字段路径，以及暂缓收录的说明。', 'overview');
publish(join(repoRoot, 'data/master-index.csv'), 'master-index.csv', '总表，可供表格软件导入。', 'overview');
publish(join(repoRoot, 'CONSTITUTION.md'), 'constitution.md', '《收集宪法》原文。', 'overview');
publish(join(repoRoot, 'schema/benchmark.schema.json'), 'schema/benchmark.schema.json', '单条基准 JSON 的字段契约。', 'overview');

for (const item of index.benchmarks) {
  publish(
    join(repoRoot, 'data/benchmarks', `${item.id}.json`),
    `benchmarks/${item.id}.json`,
    `${item.name} 的完整记录。事实字段为 value、sources，可选 status 与 note。`,
    'records',
    `benchmarks/${item.id}`,
  );
}
for (const item of index.benchmarks) {
  publish(
    join(repoRoot, 'content/benchmarks', `${item.id}.md`),
    `content/${item.id}.md`,
    `${item.name} 的中文介绍原稿。`,
    'content',
  );
}

const catalog = {
  name: 'Benchmark Atlas',
  read_only: true,
  generated_at: index.generated_at ?? '',
  timezone: index.timezone ?? '',
  resources,
};
writeFileSync(join(outDir, 'catalog.json'), `${JSON.stringify(catalog, null, 2)}\n`);
console.log(`已发布 ${resources.length} 个只读文件到 site/public/api`);
