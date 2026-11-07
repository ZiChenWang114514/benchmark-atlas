# AutomationBench-AA

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE/view?usp=drivesdk)

## 基本信息

### 简称

AutomationBench-AA

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 全称

AutomationBench-AA（Artificial Analysis 对 Zapier AutomationBench 的实现）

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 基准版本

AA使用AutomationBench数据集1.0.6的私有657任务划分；AA评分协议独立。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 论文版本

arXiv v1

> 论文修订版本不等同数据集版本。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 发布日期

2026-04-21 09:14:59 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 领域标签

- 长程自动化任务

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 许可证

母仓库Zapier原创部分为MIT；第三方API结构表示不主张原创版权，也不授予第三方IP权；AA私有集使用权另行核实。

[来源1](https://github.com/zapier/AutomationBench/blob/main/LICENSE)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2604.18934

> 2604.18934是Zapier母协议论文，不把AA的657题部分得分口径归给母论文。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 官方代码

https://github.com/zapier/AutomationBench

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 数据地址

未公开（AA使用的657任务held-out测试集）；母项目公开任务另见https://github.com/zapier/AutomationBench。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 官方入口

https://artificialanalysis.ai/evaluations/automationbench-aa

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 论文标题

AutomationBench

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

母基准：Zapier；AA实现与独立评测：Artificial Analysis。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 合作方

母论文致谢Prime Intellect等早期反馈；不意味着这些机构共同维护AA私有集。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 作者

- Daniel Shepard

- Robin Salimans

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 当前维护方

AutomationBench母项目由Zapier维护；AA运行与榜单由Artificial Analysis维护。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

## 设计目标

### 衡量能力

跨SaaS应用自主发现API、处理数据、遵守分层业务规则并完成多步工作流。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 设计背景

很多工具基准只测单应用/函数选择，缺少跨应用协调、端点发现和业务政策组合。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

## 构建方式

### 题目来源

根据Zapier客户工作流形状合成，未使用PII/客户机密；涵盖6领域、约500端点与47模拟应用。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 出题者背景

Zapier研究/工程团队；Opus4.6、GPT5.3Codex、Gemini3参与生成，再做审查。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 审核流程

多轮现实性/难度迭代、抽样人工审计；通过不含实际参数的提示模式验证可解性。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 质量控制

每题要求可观察状态修改、确定性检查与负断言防止撒网行为；RL试验识别奖励漏洞。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 去污染

母协议公开600题，至少同规模私有题；AA保留657评测题，公开示例不是官方完整评分集。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

## 数据形式

### 题量与规模

AA实现：657任务，6领域（Finance/HR/Marketing/Operations/Sales/Support）；母论文公开600及600+私有不是同一精确分母。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 题型

一次任务指令后自主多步API检索/调用，最后核对多个应用状态。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 模态

- 文本

- 结构化API与数据库

- 模拟SaaS应用

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 语言

英语业务指令与API schema。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 难度

分层政策、噪声和相似记录造成困难；不等于真实生产SaaS连通性或凭证权限测试。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 公开与隐藏划分

AA评分题保留私有，部分样例公开；母项目公开题可研究，不能作为AA分数完全复现集。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

## 评测方法

### 指标

headline为每题objective完成比例，经guardrail门控后平均；另有严格整题成功率。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 评分

任一guardrail违规整题0；否则按该任务objective满足比例记分。无条件objective得分不是同一指标。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 提示与运行设置

每任务独立运行1次；50轮上限；模型经结构化工具自主发现并调用REST API；按终态程序断言评分，不使用独立LLM裁判。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方评测脚本

https://github.com/zapier/AutomationBench

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 可比性警示

AA对无guardrail违规任务按目标完成比例给分，违规或执行错误记0；Zapier主榜按所有断言全通过的任务比例评分。公开600任务、AA私有657任务、另200条simple任务不能混用。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **版本**：AutomationBench 1.0.6；AA私有657任务
- **2026H2引用／使用证据**：- **来源URL**：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
  - **日期**：2026-10-28
  - **说明**：Artificial Analysis 2026-10-28文章明确列出 AutomationBench-AA 为 Intelligence Index v5 的评测组成并报告模型领先表现。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）

### 论文修订历史

Submission history From: Daniel Shepard [ view email ] [v1] 2026-04-21 09:14:59 KST (420 KB)

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 污染与争议

合成任务与模拟API可能偏离真实业务；仅终态评分不完整检查行为过程，guardrail口径影响解读。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 衍生与版本关系

AutomationBench-AA为AA实现；母协议600公开题与657私有评测不拆计两条，应用/领域子项不另计。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 官方榜单

https://artificialanalysis.ai/evaluations/automationbench-aa

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 独立评测覆盖

https://artificialanalysis.ai/evaluations/automationbench-aa

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 核验结果

- **模型 / Agent**：Gemini 4 Carbon (High)
- **分数**：77.8
- **指标**：AutomationBench-AA Score (%)
- **基准版本**：AA / 1.0.6 private split
- **结果性质**：AA独立评测实时网页快照
- **来源日期**：待核实（网页未注明榜表更新时间）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：Gemini 4 Carbon (Medium)
- **分数**：77.6
- **指标**：AutomationBench-AA Score (%)
- **基准版本**：AA / 1.0.6 private split
- **结果性质**：AA独立评测实时网页快照
- **来源日期**：待核实（网页未注明榜表更新时间）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：Gemini 4 Argon (High)
- **分数**：77.5
- **指标**：AutomationBench-AA Score (%)
- **基准版本**：AA / 1.0.6 private split
- **结果性质**：AA独立评测实时网页快照
- **来源日期**：待核实（网页未注明榜表更新时间）
- **采集日期**：2026-11-07 KST

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 覆盖与时效说明

AA既是本实现发布/维护方，也是相对Zapier母协议的独立评测方；同一URL不冒充两份独立证据。母论文9.9%列作不同协议对照。原母榜另见https://zapier.com/benchmarks。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- daniel.shepard@zapier.com

- robin.salimans@zapier.com

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 公开反馈

https://github.com/zapier/AutomationBench/issues

> 公开仓库反馈入口；未发送问题。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2604.18934)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2604.18934

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

[来源1](https://arxiv.org/pdf/2604.18934)（访问 2026-11-07）

### 原始PDF SHA-256

348360cd2ccefc52d1a8ea65e0a334cb3363fab85e66f71e09f6f5935233cbc5

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2604.18934)（访问 2026-11-07）

### 原始PDF字节数

684375

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2604.18934)（访问 2026-11-07）

### Drive资料文件夹

- **id**：1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O
- **webViewLink**：https://drive.google.com/drive/folders/1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O

[来源1](https://drive.google.com/drive/folders/1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O)（访问 2026-11-07）

### 其他文档

- **type**：中文介绍Google Doc
- **id**：1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM
- **webViewLink**：https://docs.google.com/document/d/1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM/edit?usp=drivesdk

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）；[来源2](https://docs.google.com/document/d/1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE
- **webViewLink**：https://drive.google.com/file/d/1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)（访问 2026-11-07）
