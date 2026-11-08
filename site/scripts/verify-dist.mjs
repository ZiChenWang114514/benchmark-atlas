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
const index = JSON.parse(read('api/index.json') || '{}');
const boilerplate = '本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。';
const chapters = ['基本信息', '发起与维护', '设计目标', '构建方式', '数据形式', '评测方法', '最新情况', '榜单快照', '联系方式', '原始文件', '变更记录'];

const sectionOrder = ['物理', '化学', '生物与医学', '地球与天文', '材料', '语言', '推理', '数学', '代码', '多模态', 'Agent', '安全', '语音', '机器人与具身'];
const sectionCounts = {};
for (const item of index.benchmarks ?? []) {
  sectionCounts[item.section] = (sectionCounts[item.section] || 0) + 1;
}

if (!home.includes('最新动态')) fail('首页缺少最新动态');
if (!home.includes('近期热门')) fail('首页缺少近期热门');
if (!home.includes('收集宪法')) fail('首页缺少宪法入口');
if (!home.includes('/benchmark-constitution/benchmarks/')) fail('首页链接没有站点前缀');
if (index.count != null && index.count !== index.benchmarks.length) {
  fail(`index.count ${index.count} 与条目数 ${index.benchmarks.length} 不一致`);
}
if (!home.includes(`本批 ${index.benchmarks.length} 个基准`)) fail('首页基准总数与索引不一致');
if ((home.match(/class="card"/g) || []).length !== index.benchmarks?.length) {
  fail(`首页卡片数与索引不一致`);
}
for (const section of sectionOrder) {
  if (!sectionCounts[section]) fail(`索引里没有板块 ${section}`);
}
for (const [section, count] of Object.entries(sectionCounts)) {
  if (!home.includes(section)) fail(`首页缺少板块 ${section}`);
  if (!home.includes(`>${count} 个基准<`)) fail(`首页没有写出 ${section} 的 ${count} 个基准`);
}
const cited = (index.benchmarks ?? []).filter((item) => item.cited_2026h2).length;
if (cited && !home.includes('2026下半年仍被引用')) fail('首页没有标出 2026下半年引用');
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
  if (detail.includes('drive.google.com') || detail.includes('Drive')) fail(`${item.id} 仍暴露网盘链接`);
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
if (!gpqa.includes('2026下半年仍被引用')) fail('GPQA 没有标出 2026下半年引用');
if (!read('benchmarks/frontiermath/index.html').includes('2026下半年证据')) fail('FrontierMath 的嵌套证据没有按字段展开');
if (!read('benchmarks/hle/index.html').includes('https://lastexam.ai')) fail('HLE 榜单来源链接没有渲染');
if (read('benchmarks/mmlu/index.html').includes('[object Object]')) fail('MMLU 仍有未格式化对象');

const matbench = read('benchmarks/matbench/index.html');
if (!matbench.includes('mailto:ardunn@lbl.gov')) fail('Matbench 公开邮箱没有做成邮件链接');
if (!read('benchmarks/matbench-discovery/index.html').includes('名次')) fail('带名次的榜单没有名次列');

if (!constitution.includes('真实性原则')) fail('宪法页缺少真实性原则');
if (!constitution.includes('第八章')) fail('宪法页缺少第八章');
if (read('api/constitution.md') !== readFileSync(join(repoRoot, 'CONSTITUTION.md'), 'utf8')) {
  fail('发布的宪法原文与仓库不一致');
}

const catalog = JSON.parse(read('api/catalog.json') || '{"resources":[]}');
for (const resource of catalog.resources ?? []) {
  if (!existsSync(join(dist, 'api', resource.path))) fail(`catalog 指向缺失文件 ${resource.path}`);
}
const published = readdirSync(join(dist, 'api/benchmarks')).filter((name) => name.endsWith('.json'));
if (published.length !== index.benchmarks.length) fail(`公开 JSON 数量 ${published.length} 与索引不一致`);
if (!existsSync(join(dist, 'api/schema/benchmark.schema.json'))) fail('缺少 schema');
if (!existsSync(join(dist, 'api/news.json'))) fail('缺少 news.json');
if (!existsSync(join(dist, '404.html'))) fail('缺少 404 页');
const trendingPage = read('trending/index.html');
if (!trendingPage) fail('缺少近期热门页');
if (trendingPage && !trendingPage.includes('Terminal-Bench-Science')) fail('热门页缺少 Terminal-Bench-Science');
if (trendingPage && trendingPage.includes('[object Object]')) fail('热门页出现了未格式化的对象');
if (home.includes('[object Object]')) fail('首页出现了未格式化的对象');
if (!home.includes('🔥 近期热门')) fail('首页卡片没有近期热门徽章');
const trendingJson = JSON.parse(read('api/trending.json') || '{}');
if (!Array.isArray(trendingJson.items) || trendingJson.items.length < 1) fail('api/trending.json 没有条目');
if (existsSync(join(dist, 'benchmarks/terminal-bench-science/index.html'))) {
  if (!trendingPage.includes('/benchmark-constitution/benchmarks/terminal-bench-science/')) {
    fail('Terminal-Bench-Science 已有档案，热门页却没有链过去');
  }
  const hotDetail = read('benchmarks/terminal-bench-science/index.html');
  if (!hotDetail.includes('为什么近期热门')) fail('详情页缺少为什么近期热门');
  if (!hotDetail.includes('🔥 近期热门')) fail('详情页缺少热门徽章');
}

const news = JSON.parse(read('api/news.json') || '[]');
for (const item of news) {
  if (!home.includes(item.title)) fail(`首页缺少动态：${item.title}`);
}

const apiPagePath = join(dist, 'api/index.html');
const apiPage = existsSync(apiPagePath) ? readFileSync(apiPagePath, 'utf8') : '';
if (apiPage) fail('不应再发布接口说明页');
const heatPage = read('frontier-heat/index.html');
const impactPage = read('impact/index.html');
const methodPage = read('impact/method/index.html');
const registryPage = read('registry/index.html');
const boardData = { '业界热度榜': '../data/frontier/heat.json', '学术影响力榜': '../data/impact/index.json', '方法页': '../data/impact/index.json', '名录': '../data/registry/registry.json' };
for (const [label, html] of [['业界热度榜', heatPage], ['学术影响力榜', impactPage], ['方法页', methodPage], ['名录', registryPage]]) {
  const hasData = existsSync(new URL(boardData[label], new URL('../', import.meta.url)));
  if (!html) fail(`缺少${label}`);
  else if (!hasData && !html.includes('数据生成中')) fail(`${label}在数据文件缺席时应该显示数据生成中`);
  else if (hasData && label === '业界热度榜' && html.includes('数据生成中')) fail(`${label}已有数据却仍显示数据生成中`);
  else if (html.includes('Benchmark Atlas')) fail(`${label}仍出现旧名称`);
}
const bannedMarkers = [
  [/Asia\/Seoul/, 'Asia/Seoul'],
  [/KST/, 'KST'],
  [/首尔/, '首尔'],
  [/\bSeoul\b/, 'Seoul'],
  [/待核实字段数/, '待核实字段数'],
  [/项待核实/, '项待核实'],
  [/补传/, '补传'],
  [/第\s*[0-9一二三四五六七八九十两]+\s*轮/, '核验轮次'],
  [/\/api\//, '/api/'],
  [/\/workspace\//, '/workspace'],
  [/\/home\//, '/home'],
  [/drive\.google\.com/, 'drive.google.com'],
  [/drivesdk/, 'drivesdk'],
  [/\bDrive\b/, 'Drive'],
  [/\bTODO\b/, 'TODO'],
  [/GH_TOKEN|API_KEY/, '凭据名'],
];
function walkHtml(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) walkHtml(full);
    else if (entry.name.endsWith('.html')) {
      const html = readFileSync(full, 'utf8');
      const rel = full.replace(dist + '/', '');
      if (html.includes('Benchmark Atlas')) fail(`旧名称仍出现在 ${rel}`);
      for (const [pattern, label] of bannedMarkers) {
        if (pattern.test(html)) fail(`${rel} 含内部标记 ${label}`);
      }
    }
  }
}
walkHtml(dist);
if (!existsSync(join(dist, 'api/trending.json'))) fail('缺少 api/trending.json');
if (!home.includes('/benchmark-constitution/frontier-heat/')) fail('首页没有链到业界热度榜');
if (!home.includes('/benchmark-constitution/impact/')) fail('首页没有链到学术影响力榜');
if (!home.includes('/benchmark-constitution/registry/')) fail('首页没有链到名录');

if (errors.length) {
  console.error('站点校验失败：');
  for (const error of errors) console.error(` - ${error}`);
  process.exit(1);
}
console.log(`站点校验通过：${index.benchmarks.length} 条档案，${news.length} 条动态，${catalog.resources.length} 个接口文件。`);
