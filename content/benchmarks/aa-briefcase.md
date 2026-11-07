# AA-Briefcase

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

原始论文 PDF：待核实；不以网页打印或其他材料替代。

## 基本信息

### 简称

AA-Briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 全称

AA-Briefcase

> 保留官方名称，不把论文标题自动扩写为全称。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 基准版本

v1.1

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 论文版本

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 发布日期

2026-06-18（官方首发文章日期；v1.1具体上线日待核实）

[来源1](https://artificialanalysis.ai/articles/aa-briefcase)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 领域标签

- 职业知识工作与多交付物

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 许可证

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 论文

待核实

> 已核实官方方法页与发布文章；未找到独立原始论文PDF，不能把示例交付物PDF当论文。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 官方代码

https://github.com/ArtificialAnalysis/Stirrup

> 这是运行agent的公开harness，不代表私有题集和完整评分代码开源。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 官方入口

https://artificialanalysis.ai/evaluations/aa-briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 论文标题

待核实

> 官方介绍页是方法/发布文章，独立论文标题尚待核实。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 合作方

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 作者

Artificial Analysis 团队（方法页署名口径）

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 当前维护方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 设计目标

### 衡量能力

数据科学、产品管理、公司战略等专业知识工作的分析、格式化呈现和可用交付物。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 设计背景

只评短答案忽略真实职业流程中的文件分析、跨材料整合和电子表格/演示/备忘录品质。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 构建方式

### 题目来源

场景源文件混合真实、增强与合成材料，含Slack导出、邮件、表格、访谈和市场研究；后续周任务可提供全模型相同的标准参考产物。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 出题者背景

由行业专家历时数月构建，背景覆盖数据科学、产品管理、企业战略，官方举例包括Google、McKinsey & Company、Boston Consulting Group；不据从业背景推断机构合作。

[来源1](https://artificialanalysis.ai/articles/aa-briefcase)（访问 2026-11-07）

### 审核流程

为交付物设计明确rubric，再结合分析质量与呈现质量的成对比较。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 质量控制

区分客观要求核验与主观质量比较；场景共享背景不意味着模型错误自动连续传递。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 去污染

正式四场景评分材料保留私有；公开第五Lite示例只供体验，不纳入正式榜。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 数据形式

### 题量与规模

4个正式多周场景，共91任务、数千输入文件；公开Lite为额外示例场景。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 题型

产出电子表格、演示文稿、备忘录等多种文件交付物。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 模态

- 文本

- 数据文件

- 表格

- 演示文稿/视觉呈现

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 语言

英语专业工作任务；文件格式与任务相依。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 难度

多周情境分解为独立任务；不是让模型真实持续运行数周。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 公开与隐藏划分

未公开：正式4场景91任务的任务指令、输入文件与rubric；公开第5个Due Diligence示例场景不计入正式结果。

[来源1](https://artificialanalysis.ai/articles/aa-briefcase)（访问 2026-11-07）

## 评测方法

### 指标

复合Elo；另列binary rubric通过率、Analytical Quality与Presentation成对比较。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 评分

rubric结果转换为合成对局并与两类质量对局合成Elo；Elo不是百分正确率。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 提示与运行设置

每任务独立运行，无此前任务的自生成产物继承；Stirrup/E2B离线sandbox，最多500轮，代码执行、finish、放弃工具，支持视觉的模型可查看图像；正式任务1次运行。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方评测脚本

公开运行harness：ArtificialAnalysis/Stirrup；完整私有评测脚本发布情况待核实。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 可比性警示

Elo依对手池和评分协议变化；Presentation、Analytical Quality子指标和headline不可互换。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **版本**：v1.1
- **2026H2引用／使用证据**：- **来源URL**：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
  - **日期**：2026-10-28
  - **说明**：Artificial Analysis 2026-10-28文章实际报告 AA-Briefcase Elo以及Presentation、Analytical Quality等子维度结果；子维度不另计。

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

[来源1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 论文修订历史

v1.1仅改变Elo拟合：各scope采用Crowd-BT；不改变任务数量。论文修订历史待核实。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 污染与争议

主观成对判断和复合Elo受裁判、对手池与展示质量影响；正式材料私有降低泄漏但限制完整复现。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 衍生与版本关系

AA-Briefcase-Lite是公开示例，不另计正式benchmark；分析/呈现分项也不拆分。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 官方榜单

https://artificialanalysis.ai/evaluations/aa-briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 独立评测覆盖

https://artificialanalysis.ai/evaluations/aa-briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 核验结果

- **模型 / Agent**：Claude Sonnet 5.5 (Max, Default Fallback)
- **分数**：1813
- **指标**：AA-Briefcase v1.1 Elo
- **95%置信区间**：-11 / +12
- **结果性质**：官方实时榜表快照
- **来源日期**：待核实（表中Sep 2026是模型发布日期，不是榜表更新时间）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：Claude Opus 5.5 (Max, Default Fallback)
- **分数**：1800
- **指标**：AA-Briefcase v1.1 Elo
- **95%置信区间**：-11 / +12
- **结果性质**：官方实时榜表快照
- **来源日期**：待核实（表中Sep 2026是模型发布日期，不是榜表更新时间）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：Claude Opus 5.5 (Xhigh, Default Fallback)
- **分数**：1760
- **指标**：AA-Briefcase v1.1 Elo
- **95%置信区间**：-10 / +11
- **结果性质**：官方实时榜表快照
- **来源日期**：待核实（表中Sep 2026是模型发布日期，不是榜表更新时间）
- **采集日期**：2026-11-07 KST

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 覆盖与时效说明

AA为基准创建者；不存在把同机构数据称作另一独立复核。前三为11月7日采集页面，模型发行月不是评测运行时间；10月28日文章历史Elo单独保留。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 公开反馈

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 本轮检查官方评测页、首发文章和方法页及PDF检索，未定位原始论文PDF。网页方法材料不冒充原始PDF；drive_pdf维持缺失。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-briefcase)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）

### Drive资料文件夹

- **id**：1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv
- **webViewLink**：https://drive.google.com/drive/folders/1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv

[来源1](https://drive.google.com/drive/folders/1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv)（访问 2026-11-07）

### 其他文档

- **type**：官方方法页HTML归档（非论文PDF）
- **id**：1VG1TTaPBvlUifj4SjEE83SCeWJeFjjiM
- **webViewLink**：https://drive.google.com/file/d/1VG1TTaPBvlUifj4SjEE83SCeWJeFjjiM/view?usp=drivesdk
- **source_url**：https://artificialanalysis.ai/evaluations/aa-briefcase
- **accessed**：2026-11-07
- **sha256**：ba0e7c1f5b6e70c09d9a33f7ba0cf670630625c0edfde2d374b56fdeef8c0033
- **bytes**：1813260

- **type**：中文介绍Google Doc
- **id**：1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I
- **webViewLink**：https://docs.google.com/document/d/1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I/edit?usp=drivesdk

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）；[来源2](https://docs.google.com/document/d/1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

待核实

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问 2026-11-07）
