import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const siteRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const repoRoot = resolve(siteRoot, '..');
const dist = join(siteRoot, 'dist');
const errors = [];
const fail = (message) => errors.push(message);

function read(path) {
  const full = join(dist, path);
  if (!existsSync(full)) {
    fail(`缺少 ${path}`);
    return '';
  }
  return readFileSync(full, 'utf8');
}

const home = read('index.html');
const constitution = read('constitution/index.html');
const apiPage = read('api/index.html');
const index = JSON.parse(read('api/index.json') || '{}');
const boilerplate = '本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。';
const chapters = ['基本信息', '发起与维护', '设计目标', '构建方式', '数据形式', '评测方法', '最新情况', '榜单快照', '联系方式', '原始文件', '变更记录'];

if (!home.includes('最新动态')) fail('首页缺少最新动态');
if (!home.includes('收集宪法')) fail('首页缺少宪法入口');
if (!home.includes('次要板块')) fail('首页缺少次要板块');
if (!home.includes('待收录')) fail('首页缺少待收录占位');
if (!home.includes('/benchmark-atlas/benchmarks/')) fail('首页链接没有站点前缀');
if ((home.match(/class="card"/g) || []).length !== index.benchmarks?.length) {
  fail(`首页卡片数与索引不一致`);
}
if (home.lastIndexOf('<script') > home.lastIndexOf('</html>')) {
  fail('首页脚本落在 </html> 之外');
}

for (const item of index.benchmarks ?? []) {
  if (!home.includes(item.name)) fail(`首页缺少 ${item.name}`);
  const detailPath = join('benchmarks', item.id, 'index.html');
  const detail = read(detailPath);
  if (!detail) continue;
  for (const title of chapters) {
    if (!detail.includes(title)) fail(`${item.id} 缺少章节 ${title}`);
  }
  if (!detail.includes('drive.google.com')) fail(`${item.id} 缺少 Drive 链接`);
  if (detail.includes('[object Object]')) fail(`${item.id} 出现了未格式化的对象`);
  const copies = detail.split(boilerplate).length - 1;
  if (copies !== 1) fail(`${item.id} 的待核实说明出现 ${copies} 次`);
  const json = read(join('api/benchmarks', `${item.id}.json`));
  if (json && !detail.includes(item.name)) fail(`${item.id} 详情页缺少名称`);
}

const gpqa = read('benchmarks/gpqa/index.html');
const gpqaJson = JSON.parse(read('api/benchmarks/gpqa.json') || '{}');
const model = gpqaJson.leaderboard?.results?.value?.[0]?.model;
if (model && !gpqa.includes(model)) fail('GPQA 榜单没有渲染首行模型');
if (!gpqa.includes('<table')) fail('GPQA 榜单没有表格');
if (!gpqa.includes('待核实')) fail('GPQA 缺少待核实');
if (!gpqa.includes('使用官方名称')) fail('GPQA 缺少字段备注');

const matbench = read('benchmarks/matbench/index.html');
if (!matbench.includes('mailto:ardunn@lbl.gov')) fail('Matbench 公开邮箱没有做成邮件链接');
if (!read('benchmarks/matbench-discovery/index.html').includes('名次')) fail('带名次的榜单没有名次列');

if (!constitution.includes('真实性原则')) fail('宪法页缺少真实性原则');
if (!constitution.includes('第八章')) fail('宪法页缺少第八章');
if (read('api/constitution.md') !== readFileSync(join(repoRoot, 'CONSTITUTION.md'), 'utf8')) {
  fail('发布的宪法原文与仓库不一致');
}

if (!apiPage.includes('只读')) fail('接口页没有说明只读');
if (!apiPage.includes('/benchmark-atlas/api/benchmarks/gpqa.json')) fail('接口页缺少 GPQA JSON 地址');
if (!apiPage.includes('catalog.json')) fail('接口页没有提到 catalog.json');

const catalog = JSON.parse(read('api/catalog.json') || '{"resources":[]}');
for (const resource of catalog.resources ?? []) {
  if (!existsSync(join(dist, 'api', resource.path))) fail(`catalog 指向缺失文件 ${resource.path}`);
}
const published = readdirSync(join(dist, 'api/benchmarks')).filter((name) => name.endsWith('.json'));
if (published.length !== index.benchmarks.length) fail(`公开 JSON 数量 ${published.length} 与索引不一致`);
if (!existsSync(join(dist, 'api/schema/benchmark.schema.json'))) fail('缺少 schema');
if (!existsSync(join(dist, 'api/news.json'))) fail('缺少 news.json');
if (!existsSync(join(dist, '404.html'))) fail('缺少 404 页');

const news = JSON.parse(read('api/news.json') || '[]');
for (const item of news) {
  if (!home.includes(item.title)) fail(`首页缺少动态：${item.title}`);
}

if (errors.length) {
  console.error('站点校验失败：');
  for (const error of errors) console.error(` - ${error}`);
  process.exit(1);
}
console.log(`站点校验通过：${index.benchmarks.length} 条档案，${news.length} 条动态，${catalog.resources.length} 个接口文件。`);
