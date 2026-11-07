# FrontierMath Erdős

> 核验：2026-11-07（KST / Asia/Seoul）。官方资料中文改写；待核实不等于未公开。原始数据与第三方实现、历史论文与当前榜单分轨。

编辑状态：研究快照；trending: A；未核实字段保留标记

## 基本信息

### 简称

FrontierMath Erdős

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 全称

FrontierMath Erdős

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 基准版本

68猜想固定题集（2026年8月构建）

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 主板块

数学

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 领域标签

- 数学

> 编辑标签

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2609.25050

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 官方代码

https://github.com/epoch-research/LeanOpenProblems

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 数据地址

https://github.com/epoch-research/LeanOpenProblems

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 官方主页

https://epoch.ai/benchmarks/frontiermath-erdos

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 论文标题

FrontierMath Erdős

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

## 发起与维护

### 发起方

Epoch AI

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 合作方

Thomas F. Bloom（University of Manchester）；不将引用上游库等同机构合作。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 作者

- Tom Adamczewski
- Thomas F. Bloom

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 维护方

Epoch AI

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 资助方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

## 设计目标

### 衡量能力

在统一预算下自主证明或推翻开放数学猜想，并提交Lean形式化证明。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 设计背景

避免只报道成功案例、预算不明和人工脚手架不透明；不用数值验证代替完整证明。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

## 构建方式

### 题目来源

Thomas Bloom从erdosproblems.com选取有数学意义与难度的未解问题。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 出题者背景

Thomas Bloom为数学家及ErdősProblems.com维护者。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 审核流程

50条猜想沿用Formal Conjectures；其余18条由自动形式化流程构造，Bloom逐条复核。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 质量控制

Comparator在独立容器中核对陈述与允许公理，并通过Lean内核重放。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 去污染

2026年8月均未解；后续已发表证明可能进入训练数据，应按模型知识截止时间过滤。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

## 数据形式

### 题量与规模

68条Lean猜想，对应65个ErdősProblems编号。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 题型

证明或否证；输出完整Lean证明。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 模态

- 形式化数学文本
- 代码

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 语言

Lean 4 / Mathlib；自然语言文献说明。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 难度

研究级开放猜想，形式化难度亦影响成绩。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 公开与隐藏划分

猜想Lean陈述与评测scaffold公开；不是隐藏答案标准问答。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

## 评测方法

### 指标

68条猜想中通过核验的比例；误差条为±1标准误。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 评分

仅接受与可信陈述完全一致、无额外公理、可由Lean内核重放的证明或否证。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 提示与运行设置

每猜想一次尝试；每次300美元及72小时；离线Docker，shell、编辑器、Mathlib、SageMath及截至2022年的数学文献快照。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 官方评测脚本

https://github.com/epoch-research/LeanOpenProblems

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 可比性警示

额外高预算或多次尝试不计入标准榜；已解问题总数不是任一模型标准分数。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 当前版本与热度证据

- **version**：68猜想固定题集（2026年8月构建）
- **heat_confidence**：A
- **why_trending**：候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。
- **evidence_2026_h2**：
  - **url**：https://epoch.ai/data/benchmarks.csv
  - **date**：2026-11-07
  - **date_type**：observed_on
  - **organization**：Epoch AI
  - **note**：本次读取CSV并提取成功运行记录，含2026H2运行。
  - **url**：https://epoch.ai/benchmarks/frontiermath-erdos
  - **date**：2026-11-07
  - **date_type**：observed_on
  - **organization**：官方维护方
  - **note**：已打开当前官方方法与榜单；观察日不冒充发布时间。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；[来源2](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 版本与材料差异

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 饱和情况

官网截至2026-10-29列出17个已解问题（包含外部研究及非标准尝试），不代表标准协议饱和。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 污染与争议

证明形式化成本可能低估数学能力；后续公开解答带来污染风险。

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 衍生与版本关系

原frontiermath已包含v2的Tier1–4；Erdős为独立命名未解问题套件，单独建条目。

> 编辑去重口径；具体版本差异仍以官方材料为准。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 为什么近期热门

候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。

- 2026-11-07（observed_on）：本次读取CSV并提取成功运行记录，含2026H2运行。 [来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

- 2026-11-07（observed_on）：已打开当前官方方法与榜单；观察日不冒充发布时间。 [来源](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 官方榜单

https://epoch.ai/benchmarks/frontiermath-erdos

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 独立评测覆盖

https://epoch.ai/data/benchmarks.csv

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：GPT-6.1 Sol (max)
- **score**：0.04411764705882353
- **metric**：CSV mean_score (0–1)
- **task_version**：待核实
- **original_task_name**：FrontierMath-Erdos
- **run_id**：bloom68-alv3junt54xqrybd
- **run_started_at_kst**：2026-10-02T05:26:05+09:00
- **stderr**：0.02508828598537234
- **source_url**：https://epoch.ai/data/benchmarks.csv
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：Epoch CSV同task/版本已成功运行记录按mean_score排序；非跨harness完整总榜
- **rank**：2
- **model**：GPT-6 Astra (max)
- **score**：0.029411764705882353
- **metric**：CSV mean_score (0–1)
- **task_version**：待核实
- **original_task_name**：FrontierMath-Erdos
- **run_id**：bloom68-ultima-e1dhs43ykrmakree
- **run_started_at_kst**：2026-08-29T01:33:49+09:00
- **stderr**：0.0206414713705158
- **source_url**：https://epoch.ai/data/benchmarks.csv
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：Epoch CSV同task/版本已成功运行记录按mean_score排序；非跨harness完整总榜
- **rank**：3
- **model**：Claude Opus 5.5 (max)
- **score**：0.0294
- **metric**：CSV mean_score (0–1)
- **task_version**：待核实
- **original_task_name**：FrontierMath-Erdos
- **run_id**：bloom68-opus55-m1pc5wbymin28jdj
- **run_started_at_kst**：2026-09-24T22:30:00+09:00
- **stderr**：0.0206
- **source_url**：https://epoch.ai/data/benchmarks.csv
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：Epoch CSV同task/版本已成功运行记录按mean_score排序；非跨harness完整总榜

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 覆盖与时效说明

CSV标准FrontierMath-Erdos任务已成功记录排序；不混入非系统高预算尝试。论文早期3%是历史值，不代替当前CSV结果。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 官方社交／讨论渠道

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2609.25050

[来源1](https://arxiv.org/abs/2609.25050)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### 其他文档

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）

### Drive PDF归档

待核实（本轮未上传）

## 变更记录

### 变更记录

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。

[来源1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问 2026-11-07）
