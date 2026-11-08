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

function readData(path) {
  const full = join(repoRoot, path);
  if (!existsSync(full)) {
    fail(`缺少 ${path}`);
    return '';
  }
  return readFileSync(full, 'utf8');
}

const home = read('index.html');
const zhHome = read('zh/index.html');
const constitution = read('constitution/index.html');
const zhConstitution = read('zh/constitution/index.html');
const index = JSON.parse(readData('data/index.json') || '{}');
const zhBoilerplate = '该字段尚未完成精确核验，不表示官方未公开。';
const enBoilerplate = 'This field has not been confirmed exactly. It does not mean the information is unpublished.';
const zhChapters = ['基本信息', '发起与维护', '设计目标', '构建方式', '数据形式', '评测方法', '最新情况', '榜单快照', '联系方式', '原始文件', '变更记录'];
const enChapters = ['Basic information', 'Origin and maintenance', 'Design goals', 'Construction', 'Data format', 'Evaluation', 'Current status', 'Leaderboard snapshot', 'Contact', 'Original files', 'Changelog'];

const sectionOrder = ['物理', '化学', '生物与医学', '地球与天文', '材料', '语言', '推理', '数学', '代码', '多模态', 'Agent', '安全', '语音', '机器人与具身'];
const sectionCounts = {};
for (const item of index.benchmarks ?? []) {
  sectionCounts[item.section] = (sectionCounts[item.section] || 0) + 1;
}

if (!home.includes('hreflang="en"') || !home.includes('hreflang="zh-Hans"') || !home.includes('hreflang="x-default"')) {
  fail('英文首页缺少 hreflang');
}
if (!home.includes('>Benchmark Constitution<')) fail('英文首页标题不是 Benchmark Constitution');
if (home.includes('基准收集宪法')) fail('英文首页仍有译名副标题');
if (!home.includes('News')) fail('英文首页缺少 News');
if (!home.includes('Trending')) fail('英文首页缺少 Trending');
if (!zhHome.includes('最新动态')) fail('中文首页缺少最新动态');
if (!zhHome.includes('近期热门')) fail('中文首页缺少近期热门');
if (!zhHome.includes('收集宪法')) fail('中文首页缺少宪法入口');
if (!zhHome.includes('/benchmark-constitution/zh/benchmarks/')) fail('中文首页链接没有语言前缀');
if (!home.includes('/benchmark-constitution/benchmarks/')) fail('首页链接没有站点前缀');
if (index.count != null && index.count !== index.benchmarks.length) {
  fail(`index.count ${index.count} 与条目数 ${index.benchmarks.length} 不一致`);
}
if (!zhHome.includes(`${index.benchmarks.length} 个基准`)) fail('中文首页基准总数与索引不一致');
if (!home.includes(`${index.benchmarks.length} benchmarks`)) fail('英文首页基准总数与索引不一致');
if ((home.match(/class="card"/g) || []).length !== index.benchmarks?.length) {
  fail(`首页卡片数与索引不一致`);
}
if ((zhHome.match(/class="card"/g) || []).length !== index.benchmarks?.length) {
  fail(`中文首页卡片数与索引不一致`);
}
for (const section of sectionOrder) {
  if (!sectionCounts[section]) fail(`索引里没有板块 ${section}`);
}
const sectionLabels = {
  物理: 'Physics', 化学: 'Chemistry', '生物与医学': 'Biology and medicine', '地球与天文': 'Earth and astronomy',
  材料: 'Materials', 综合科学: 'General science', 语言: 'Language', 推理: 'Reasoning', 数学: 'Mathematics',
  代码: 'Code', 多模态: 'Multimodal', Agent: 'Agent', 安全: 'Safety', 语音: 'Speech', '机器人与具身': 'Robotics and embodied AI',
};
for (const [section, count] of Object.entries(sectionCounts)) {
  if (!zhHome.includes(section)) fail(`中文首页缺少板块 ${section}`);
  if (!zhHome.includes(`>${count} 个基准<`)) fail(`中文首页没有写出 ${section} 的 ${count} 个基准`);
  const label = sectionLabels[section];
  if (label && !home.includes(label)) fail(`英文首页缺少板块 ${label}`);
  if (!home.includes(`>${count} benchmarks<`)) fail(`英文首页没有写出 ${section} 的 ${count} benchmarks`);
}
const cited = (index.benchmarks ?? []).filter((item) => item.cited_2026h2).length;
if (cited && !zhHome.includes('2026下半年仍被引用')) fail('中文首页没有标出 2026下半年引用');
if (cited && !home.includes('Cited in 2026 H2')) fail('英文首页没有标出 2026 H2 citation');
if (home.lastIndexOf('<script') > home.lastIndexOf('</html>')) {
  fail('首页脚本落在 </html> 之外');
}

for (const item of index.benchmarks ?? []) {
  if (!home.includes(item.name)) fail(`首页缺少 ${item.name}`);
  if (!zhHome.includes(item.name)) fail(`中文首页缺少 ${item.name}`);
  for (const [prefix, chapters, boilerplate, locale] of [
    ['', enChapters, enBoilerplate, 'en'],
    ['zh/', zhChapters, zhBoilerplate, 'zh'],
  ]) {
    const detail = read(`${prefix}benchmarks/${item.id}/index.html`);
    if (!detail) continue;
    for (const title of chapters) {
      if (!detail.includes(title)) fail(`${locale} ${item.id} 缺少章节 ${title}`);
    }
    if (detail.includes('drive.google.com') || detail.includes('Drive')) fail(`${locale} ${item.id} 仍暴露网盘链接`);
    if (detail.includes('[object Object]')) fail(`${locale} ${item.id} 出现了未格式化的对象`);
    const copies = detail.split(boilerplate).length - 1;
    if (copies !== 1) fail(`${locale} ${item.id} 的待核实说明出现 ${copies} 次`);
    if (!detail.includes(item.name)) fail(`${locale} ${item.id} 详情页缺少名称`);
  }
}

const gpqa = read('benchmarks/gpqa/index.html');
const zhGpqa = read('zh/benchmarks/gpqa/index.html');
const gpqaJson = JSON.parse(readData('data/benchmarks/gpqa.json') || '{}');
const model = gpqaJson.leaderboard?.results?.value?.[0]?.model;
if (model && !gpqa.includes(model)) fail('GPQA 榜单没有渲染首行模型');
if (!gpqa.includes('<table')) fail('GPQA 榜单没有表格');
if (!gpqa.includes('Unverified')) fail('英文 GPQA 缺少 Unverified');
if (!zhGpqa.includes('待核实')) fail('中文 GPQA 缺少待核实');
if (!zhGpqa.includes('使用官方名称')) fail('GPQA 缺少字段备注');
if (!zhGpqa.includes('2026下半年仍被引用')) fail('中文 GPQA 没有标出 2026下半年引用');
if (!gpqa.includes('Cited in 2026 H2')) fail('英文 GPQA 没有标出 2026 H2 citation');
if (!read('zh/benchmarks/frontiermath/index.html').includes('2026下半年证据')) fail('FrontierMath 的嵌套证据没有按字段展开');
if (!read('benchmarks/hle/index.html').includes('https://lastexam.ai')) fail('HLE 榜单来源链接没有渲染');
if (!read('benchmarks/hle/index.html').includes('Humanity’s')) fail('HLE 英文页缺少弯引号撇号');
if (read('benchmarks/mmlu/index.html').includes('[object Object]')) fail('MMLU 仍有未格式化对象');
const tbs = read('benchmarks/terminal-bench-science/index.html');
const zhTbs = read('zh/benchmarks/terminal-bench-science/index.html');
if (!tbs.includes('General science')) fail('英文 Terminal-Bench Science 不是综合科学');
if (!zhTbs.includes('综合科学')) fail('中文 Terminal-Bench Science 不是综合科学');
if (tbs.includes('>Physics<') || zhTbs.includes('>物理<')) fail('Terminal-Bench Science 仍被标成物理');

const matbench = read('benchmarks/matbench/index.html');
if (!matbench.includes('mailto:ardunn@lbl.gov')) fail('Matbench 公开邮箱没有做成邮件链接');
if (!read('zh/benchmarks/matbench-discovery/index.html').includes('名次')) fail('带名次的榜单没有名次列');
if (!read('benchmarks/matbench-discovery/index.html').includes('Rank')) fail('英文榜单没有 Rank 列');

if (!zhConstitution.includes('真实性原则')) fail('中文宪法页缺少真实性原则');
if (!zhConstitution.includes('第八章')) fail('中文宪法页缺少第八章');
if (!constitution.includes('Chapter 8')) fail('英文宪法页缺少 Chapter 8');
if (!constitution.includes('Accuracy')) fail('英文宪法页缺少准确性原则');
const published = readdirSync(join(repoRoot, 'data/benchmarks')).filter((name) => name.endsWith('.json'));
if (published.length !== index.benchmarks.length) fail(`档案 JSON 数量 ${published.length} 与索引不一致`);
if (!existsSync(join(repoRoot, 'schema/benchmark.schema.json'))) fail('缺少 schema');
if (!existsSync(join(repoRoot, 'data/news.json'))) fail('缺少 news.json');
if (existsSync(join(dist, 'api'))) fail('构建结果仍包含 api 目录');
if (!existsSync(join(dist, '404.html'))) fail('缺少 404 页');
const trendingPage = read('trending/index.html');
const zhTrendingPage = read('zh/trending/index.html');
if (!trendingPage) fail('缺少近期热门页');
if (!zhTrendingPage) fail('缺少中文近期热门页');
if (trendingPage && !trendingPage.includes('Terminal-Bench-Science')) fail('热门页缺少 Terminal-Bench-Science');
if (trendingPage && trendingPage.includes('[object Object]')) fail('热门页出现了未格式化的对象');
if (home.includes('[object Object]')) fail('首页出现了未格式化的对象');
if (!zhHome.includes('🔥 近期热门')) fail('中文首页卡片没有近期热门徽章');
if (!home.includes('🔥 Trending')) fail('英文首页卡片没有近期热门徽章');
const trendingJson = JSON.parse(readData('data/trending.json') || '{}');
if (!Array.isArray(trendingJson.items) || trendingJson.items.length < 1) fail('data/trending.json 没有条目');
if (existsSync(join(dist, 'benchmarks/terminal-bench-science/index.html'))) {
  if (!trendingPage.includes('/benchmark-constitution/benchmarks/terminal-bench-science/')) {
    fail('Terminal-Bench-Science 已有档案，热门页却没有链过去');
  }
  const hotDetail = read('benchmarks/terminal-bench-science/index.html');
  const zhHotDetail = read('zh/benchmarks/terminal-bench-science/index.html');
  if (!zhHotDetail.includes('为什么近期热门')) fail('中文详情页缺少为什么近期热门');
  if (!hotDetail.includes('Why it is trending')) fail('英文详情页缺少为什么近期热门');
  if (!zhHotDetail.includes('🔥 近期热门')) fail('中文详情页缺少热门徽章');
}

const news = JSON.parse(readData('data/news.json') || '[]');
for (const item of news) {
  if (!zhHome.includes(item.title)) fail(`中文首页缺少动态：${item.title}`);
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
  [/docs\.google\.com/, 'docs.google.com'],
  [/webViewLink/, 'webViewLink'],
  [/_kst/, '_kst'],
  [/\/home\/box/, '/home/box'],
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

const properNames = new Set(['中文']);
const lexicon = JSON.parse(readData('data/en/lexicon.json') || '{}');
for (const [key, value] of Object.entries(lexicon)) {
  if (typeof value !== 'string' || !/[\u4e00-\u9fff]/.test(value)) continue;
  const latin = (value.match(/[A-Za-z]/g) || []).length;
  const cjkCount = (value.match(/[\u4e00-\u9fff]/g) || []).length;
  const keptName = value === key && cjkCount <= 40;
  if (latin > 0 || keptName) {
    for (const run of value.match(/[\u4e00-\u9fff]{2,}/g) || []) properNames.add(run);
  }
}
const cjkRun = /[\u4e00-\u9fff]{1,}/g;
for (const file of readdirSync(join(repoRoot, 'data/benchmarks')).filter((name) => name.endsWith('.json'))) {
  const record = JSON.parse(readData(join('data/benchmarks', file)) || '{}');
  const authors = record.organization?.authors?.value;
  const pools = [authors, record.organization?.initiators?.value, record.organization?.maintainer?.value];
  for (const pool of pools) {
    const values = Array.isArray(pool) ? pool : [pool];
    for (const value of values) {
      if (typeof value !== 'string') continue;
      for (const token of value.split(/[、,，;；]/)) {
        const name = token.trim();
        if (name && /^[\u4e00-\u9fff·]{2,30}$/.test(name)) properNames.add(name.replace(/·/g, ''));
      }
    }
  }
}
function visibleEnglish(html) {
  return html
    .replace(/<a class="lang-switch"[^>]*>[\s\S]*?<\/a>/g, '')
    .replace(/<script[\s\S]*?<\/script>/g, '');
}
for (const file of readdirSync(dist, { recursive: true })) {
  const rel = String(file);
  if (!rel.endsWith('.html') || rel.startsWith('zh/') || rel.startsWith('zh\\')) continue;
  const html = visibleEnglish(read(rel));
  const runs = html.match(cjkRun) || [];
  const stray = [...new Set(runs.filter((run) => !properNames.has(run) && ![...properNames].some((name) => name.includes(run) && run.length >= 2)))];
  if (stray.length) fail(`英文页 ${rel} 含非专名汉字：${stray.slice(0, 4).join(' / ')}`);
}
if (!existsSync(join(repoRoot, 'data/trending.json'))) fail('缺少 data/trending.json');
if (!home.includes('/benchmark-constitution/frontier-heat/')) fail('首页没有链到业界热度榜');
if (!home.includes('/benchmark-constitution/impact/')) fail('首页没有链到学术影响力榜');
if (!home.includes('/benchmark-constitution/registry/')) fail('首页没有链到名录');

if (errors.length) {
  console.error('站点校验失败：');
  for (const error of errors) console.error(` - ${error}`);
  process.exit(1);
}
console.log(`站点校验通过：${index.benchmarks.length} 条档案，${news.length} 条动态。`);
