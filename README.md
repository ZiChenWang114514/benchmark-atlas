# Benchmark Atlas · 自然科学首批资料

核验日期：2026-11-07（Asia/Seoul / KST）。本批为可持续维护数据库的数据底座，不是完整应用或已启动的自动更新服务。

## 已交付

- 24 个已由官方论文/材料证实存在的 benchmark；24 份逐字段来源 JSON；24 份中文介绍 Markdown。
- 主归档：物理 9、化学 3、生物与医学 4、地球与天文 5、材料 3。跨学科条目用标签交叉导航，避免重复计数。
- 24 份未改动的原论文 PDF 已存 Google Drive；JSON 同时记录 Drive 文件 ID/链接、下载来源、字节数与 SHA-256。
- 宪法 v0.1 全文、JSON Schema、总索引、CSV 总表、6 条有来源的动态/核验观察。

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
8. 本次没有在 GitHub 推送、创建 GitHub 仓库、提交公开表单、联系维护者、改变 Drive 共享权限，也没有建立每日计划任务。
9. PDF 下载暂存于 `/workspace/benchmark-atlas-papers/`；仓库仅保留云端链接与哈希，不把大体积 PDF 混入源码库。

## 下一批优先工作

- 补全许可、版本、出题背景、逐任务数据划分、评分脚本与提示设置。
- 对已发现的冲突，保留旧证据并等待官方澄清，不覆盖历史。
- MMLU-Pro 科学子集、HLE 自然科学切片、BioASQ 各年度挑战暂缓为独立条目，避免把非锁定子集/不同年度任务伪装成统一 benchmark。
- 由应用层接入 JSON/Markdown 后再实现导航与 PDF 浏览；每日维护须单独建立可审计任务及失败告警。
