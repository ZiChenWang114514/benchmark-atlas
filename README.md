# Benchmark Atlas · 2026H2 百项基准资料

核验日期：2026-11-07（Asia/Seoul / KST）。本批为可持续维护数据库的数据底座。公开网站由这些文件在构建时生成。

## 网站

[https://zichenwang114514.github.io/benchmark-atlas/](https://zichenwang114514.github.io/benchmark-atlas/)

更新 `data/`、`content/` 或 `CONSTITUTION.md` 后推送到 `main`，GitHub Actions 会重新发布。步骤、本地预览和只读 JSON 地址见 [MAINTAINING.md](MAINTAINING.md)。

## 已交付

- 100 个基准：原有24条 + 新增76条；100份带逐字段来源JSON和100份中文Markdown介绍；全部通过Draft2020-12及URI/date格式校验。
- 主板块：物理 12、化学 4、生物与医学 12、地球与天文 6、材料 6、语言 12、推理 7、数学 7、代码 10、多模态 10、Agent 9、安全 5。自然科学核心共40条。
- 95份原始/协议PDF归档；100份中文Google Docs。5份PDF仍待补：qmof, aime, frontiercode, realworldqa, aa-briefcase；不会用HTML或其他论文冒充。
- 100条均附2026H2引用/评测使用证据；引用不等于实时榜单、新发布或独立复测。
- 26条有来源、日期明确的动态/观察，按事件日期（未知时按观察日）倒序并去重。
- 1278个待核实字段；原有冲突及批次新增冲突均保留，不补猜。
- master Google Sheet 总表已扩充到100行。

## 入口

- [Drive 总目录](https://drive.google.com/drive/folders/1t7oyeKp0N9ZZf7pO3WpAor6ztUYVVgqQ)
- [Google Doc 宪法](https://docs.google.com/document/d/1gc-kP3iW-rK79h0GhSUpNgSjHtb3TDOkdjNq5WfykiM/edit)
- [Google Sheet 总表](https://docs.google.com/spreadsheets/d/1su106zLttcQLZ-C-thBABCfRruIMWvOXxIhPXVUhQOs/edit)

## 文件约定

- `CONSTITUTION.md`：对话中宪法 v0.1，全章保留；没有擅自修改政策。
- `data/benchmarks/*.json`：宪法第四章的 11 个部分。除记录 ID、schema 版本、编辑工作流状态外，事实字段均使用 `{value, sources: [{url, accessed}], status?, note?}`。
- `schema/benchmark.schema.json`：Draft 2020-12 数据契约，校验字段完整性与来源格式。
- `data/index.json`：供导航使用的摘要；来源直接继承逐条记录。
- `data/news.json`：按观察/事件日期倒序。`observed_date` 不等同于消息首次公布日期；未证实事件日期写“待核实”，不虚构“今日发布”。
- `content/benchmarks/*.md`：中文介绍，每节保留来源与访问日期。
- `data/evidence/`：研究时取得的官方摘要、论文版本历史、页面证据与下载哈希。
- `data/master-index.csv`：Google Sheet 导入源。
- `data/drive-manifest.json`：云端目录/文档及核验清单。
- `data/quality-report.json`：验证结果、未完成字段与排除/暂缓记录。

## 数据解释与已知缺口

1. “待核实”表示本批没有完成该字段的精确核验，不代表维护方没有公开。只有确认未公开才用“未公开”。
2. 论文作者单位不自动等于发起机构、所有者或当前维护方；机构栏保留这种区别。
3. 基准库版本与论文 arXiv 版本分开保存；未知数据版本不随意写 v1。Drive 文件夹中的“版本待核实”为明确占位，不是假版本。
4. GPQA Diamond 与 GPQA 全集不同；SciCode 主/子问题和背景条件不同；OlympiadBench 总题量不是物理子集题量。
5. 历史论文结果、官方站点示例结果、第三方当前榜单严格区分。没有读取到数值的动态图表不补写、不估计。
6. SciCode 测试审计、Matbench 历史 ROC-AUC 误标、BixBench 摘要/正文数字冲突、BioProBench 协议数量冲突及 WeatherBench 时间范围变化均有显式记录。
7. 未查清的许可、完整维护方/资助方、精确 API 模型快照、提示设置、饱和/污染状态等保留为待核实；不可作为已确认商用许可或“无污染”结论。
8. 既有GitHub仓库为ZiChenWang114514/benchmark-atlas。本次不fetch、pull、commit、push，也不修改site/或.github/workflows；仓库内容须经cloud coding agent应用。未改变Drive共享权限、联系维护者或建立每日计划。
9. PDF 下载暂存于 `/workspace/benchmark-atlas-papers/`；仓库仅保留云端链接与哈希，不把大体积 PDF 混入源码库。

## 下一批优先工作

- 补全许可、版本、出题背景、逐任务数据划分、评分脚本与提示设置。
- 对已发现的冲突，保留旧证据并等待官方澄清，不覆盖历史。
- MMLU-Pro与HLE整体已收录；单独的MMLU-Pro科学子集、HLE自然科学切片及BioASQ各年度挑战仍暂缓为独立条目，避免未锁定或重复切片。
- Library Page提供导航与归档入口；导航网站在 `site/`，由数据文件静态生成；推送到 `main` 后 GitHub Actions 发布到 Pages，见 MAINTAINING.md。每日维护须单独建立可审计任务及失败告警。
