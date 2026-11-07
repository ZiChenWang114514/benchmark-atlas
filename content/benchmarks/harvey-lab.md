# Harvey LAB（Legal Agent Benchmark）

> 近期热门批次核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。已核验存在；近期热门新建条目，未核实字段保留标记；trending: A

原始论文 PDF：待核实

## 为什么近期热门

Harvey LAB 是首个大规模开源的长程法律 agent 基准，2026 下半年被 Artificial Analysis 与 Vals AI 两家独立评测机构分别实现并持续更新。

- 2026-11-07 · Artificial Analysis：当前方法页将Harvey Legal Agent Benchmark (LAB v1.1)列为正在实施的评测，披露任务或评分协议。（[链接](https://artificialanalysis.ai/methodology/intelligence-benchmarking)）
- 2026-11-07 · Artificial Analysis：当前公开评测目录单列Harvey Legal Agent Benchmark (LAB v1.1)，不是新闻提及。（[链接](https://artificialanalysis.ai/evaluations)）
- 2026-11-05 · Vals AI：Vals 11月5日更新HLAB-Vals-1.1专业法律交付物榜；与AA设置分开记录。（[链接](https://www.vals.ai/benchmarks/hlab)）

热度等级：**trending: A**。

## 基本信息

### 简称

Harvey LAB（Legal Agent Benchmark）

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 全称

Harvey's Legal Agent Benchmark (LAB)

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 基准版本

开源仓库 lab-core v1.3.0；AA 实现为 Harvey LAB-AA v1.1；Vals 实现为 HLAB-Vals-1.1

> 三处“v1.1”分属不同实现，彼此不可比。

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[来源3](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 论文版本

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 发布日期

2026-05-06（Harvey 官方博客）

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 领域标签

- 法律
- 专业知识工作

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 许可证

MIT（harvey-labs 仓库）

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 论文

待核实

> 官方以博客发布，未见独立论文。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 官方代码

https://github.com/harveyai/harvey-labs

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 数据地址

https://github.com/harveyai/harvey-labs

> 开源任务集在仓库 tasks/ 目录。

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 官方入口

https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 论文标题

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Harvey

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 合作方

Artificial Analysis（v1.1 联合开发 AA 实现）；Vals AI（行业合作评测）

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 作者

Niko Grupen、Gabe Pereyra、Julio Pereyra（博客署名）

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 当前维护方

Harvey（harveyai/harvey-labs）

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 设计目标

### 衡量能力

像律所分派工作那样：给出指令与客户案卷材料，要求 agent 产出可审阅的法律工作成果（文档、表格、演示）。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 设计背景

LegalBench、CUAD、LEXam、BigLaw Bench 等只评短程推理，缺少长程法律 agent 基准。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 构建方式

### 题目来源

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 出题者背景

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 审核流程

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 质量控制

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 去污染

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 数据形式

### 题量与规模

首版开源 1,200+ agent 任务、24 个执业领域、75,000+ 条专家撰写评分标准；AA 使用 Harvey 120 个私有任务

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 题型

长程 agent 任务，产出 docx/xlsx/pptx 等交付物

[来源1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 模态

- 文本
- 办公文档

[来源1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 语言

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 难度

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 公开与隐藏划分

有公开集与 held-out 测试集；Vals 结果来自 held-out 集；AA 使用私有数据集

[来源1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

## 评测方法

### 指标

AA：Hallucination-Gated All-Pass Rate（全部标准满足且无实质性幻觉）；Vals：Task Pass Rate 及 Criteria Pass Rate

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 评分

AA v1.1 用 GPT-6 Sol、Grok 4.7、Claude Opus 5.5 三裁判逐条评分并平均，另做两阶段幻觉检查

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 提示与运行设置

Vals：Read/Edit/Write File、Glob、Bash、Grep 六工具与 docx/pptx/xlsx 技能；AA：Stirrup harness

[来源1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 官方评测脚本

https://github.com/harveyai/harvey-labs

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 可比性警示

AA v1.1 与 v1.0 不可比；Vals HLAB-Vals-1.1 与 AA LAB-AA 不可比（Vals 页面明确说明）。

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **version**：开源仓库 lab-core v1.3.0；AA 实现为 Harvey LAB-AA v1.1；Vals 实现为 HLAB-Vals-1.1
- **evidence_2026_h2**：- **url**：https://artificialanalysis.ai/methodology/intelligence-benchmarking
- **date**：2026-11-07
- **organization**：Artificial Analysis
- **note**：当前方法页将Harvey Legal Agent Benchmark (LAB v1.1)列为正在实施的评测，披露任务或评分协议。

- **url**：https://artificialanalysis.ai/evaluations
- **date**：2026-11-07
- **organization**：Artificial Analysis
- **note**：当前公开评测目录单列Harvey Legal Agent Benchmark (LAB v1.1)，不是新闻提及。

- **url**：https://www.vals.ai/benchmarks/hlab
- **date**：2026-11-05
- **organization**：Vals AI
- **note**：Vals 11月5日更新HLAB-Vals-1.1专业法律交付物榜；与AA设置分开记录。
- **trending**：- **heat_confidence**：A
- **summary**：AA 目录标 Updated，已与 Harvey 联合升级为幻觉门控评测；Vals 也独立评 HLAB-Vals-1.1。

> 近期热门证据取自候选研究与本轮重开页面；A级：多家前沿实验室或评测机构独立采用。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations)（访问 2026-11-07）；[来源3](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 论文修订历史

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 污染与争议

Harvey 首发时有意不设榜单，预期数据集会持续演化。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 衍生与版本关系

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 官方榜单

https://artificialanalysis.ai/evaluations/harvey-lab-aa

> Harvey 本身无官方榜；AA 为与 Harvey 合作的实现。

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 独立评测覆盖

https://www.vals.ai/benchmarks/hlab

[来源1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：Muse Wonder Full (Max)
- **score**：13.1%
- **metric**：Harvey LAB-AA v1.1 Hallucination-Gated All-Pass Rate
- **result_type**：AA 实现榜快照
- **source_date**：待核实（采集日2026-11-07）
- **collected_at**：2026-11-07 KST

- **rank**：2
- **model**：Muse Wonder (Max)
- **score**：10.0%
- **metric**：Harvey LAB-AA v1.1 Hallucination-Gated All-Pass Rate
- **result_type**：AA 实现榜快照
- **source_date**：待核实（采集日2026-11-07）
- **collected_at**：2026-11-07 KST

- **rank**：3
- **model**：Grok 4.7 (Xhigh)
- **score**：9.4%
- **metric**：Harvey LAB-AA v1.1 Hallucination-Gated All-Pass Rate
- **result_type**：AA 实现榜快照
- **source_date**：待核实（采集日2026-11-07）
- **collected_at**：2026-11-07 KST

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 覆盖与时效说明

AA 榜采集于2026-11-07；Vals HLAB-Vals-1.1 自写更新2026-11-05，第一为 Gemini 4 Argon 27.08%、Muse Spark Open 25.00%、Wonder 23.75%，口径不同不合并。

[来源1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 公开反馈

https://github.com/harveyai/harvey-labs/issues

[来源1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 其他文档

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组按任务要求不上传Drive；原始PDF URL见original_files。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

## 变更记录

### changelog

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。

[来源1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

