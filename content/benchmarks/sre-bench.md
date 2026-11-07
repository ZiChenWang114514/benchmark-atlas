# SRE Bench（SRE-Bench）

> 近期热门批次核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。已核验存在；近期热门新建条目，未核实字段保留标记；trending: A

原始论文 PDF：https://arxiv.org/pdf/2608.11469

## 为什么近期热门

SRE Bench 把 agent 网络安全评测从“有源码”推进到“只有二进制”，OpenAI GPT-6 Astra 发布表直接引用，Vals 持续更新。

- 2026-11-05 · Vals AI：当前方法与榜单页展示多家前沿模型的实测结果；11月5日更新、37模型二进制逆向理解测试；不能误译为站点可靠性工程基准。（[链接](https://www.vals.ai/benchmarks/srebench)）
- 2026-11-05 · Vals AI：目录卡片：Cyber Proprietary SRE Bench Updated: 11/5/2026 Models Tested: 37 Can AI agents work out what a real-world binary does without its source code? Top Models 1 GPT-6 Astra 2 GPT-6.1 Sol 3 Gemini 4 Argon View Details（[链接](https://www.vals.ai/benchmarks)）
- 2026-11-07 · OpenAI：GPT-6 Astra正式发布评测表明确报告SRE Bench，作为近期厂商采用证据。（[链接](https://openai.com/index/gpt-6-astra/)）

热度等级：**trending: A**。

## 基本信息

### 简称

SRE Bench（SRE-Bench）

> 此处 SRE 指软件逆向工程，不是站点可靠性工程。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 全称

The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 基准版本

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 论文版本

arXiv v2（2026-10-01 修订）

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 发布日期

2026-08-11（arXiv v1 提交）

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 主板块

代码

> Benchmark Atlas 编辑归档；Vals 归入 Cyber。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 领域标签

- 二进制逆向工程
- 网络安全

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 许可证

未公开

> Vals 页面标注 Proprietary，19个程序为私有。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2608.11469

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 官方代码

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 数据地址

未公开

> 论文说明19个程序为 private。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/srebench

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 论文标题

The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 合作方

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 作者

Jeremy Spence、Nicholas Assaderaghi、Feng Xiao、Jinhao Zhu、Nikil Ravi、Xiangyu Qi、Matthew Jagielski、Raluca Ada Popa、Eric Wallace、Guannan Wei、Yangruibo Ding、Zhuo Zhang

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 当前维护方

Vals AI（当前榜单维护）

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 设计目标

### 衡量能力

在没有源代码的情况下理解真实规模、带反分析保护的二进制程序（协议、固件、游戏、文件格式恢复、恶意软件）。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 设计背景

现有 RE 相关基准依赖已有 CTF 或玩具程序，易被记忆污染且规模与保护不真实。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 构建方式

### 题目来源

RE 专家从零构建19个内部程序（平均约16.9K行代码），配合44种自研反分析机制（27K行代码的保护套件）。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 出题者背景

逆向工程领域专家，投入超过5,000专家小时

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 审核流程

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 质量控制

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 去污染

全部从零 clean-room 构建、程序私有，以避免出现在训练数据中

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 数据形式

### 题量与规模

19个程序 → 262个二进制实例 → 1,572个确定性评分任务（每实例6个）

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 题型

shell 环境中的 agent 逆向任务，确定性验证

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 模态

- 二进制文件
- 文本/命令行

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 语言

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 难度

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 公开与隐藏划分

私有（Vals 标注 Proprietary）

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 评测方法

### 指标

Fully Solved（实例6任务全对才计）与 Capability Score（1,572任务完成比例）；Vals 榜显示 Accuracy

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 评分

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 提示与运行设置

所有 agent 在相同的仅 shell 循环与相同逆向工具箱中运行

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 官方评测脚本

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 可比性警示

论文中有公开设置与关闭安全护栏、无预算上限的内部设置，两者不可混比；Vals 榜分数与论文表格口径可能不同。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **version**：待核实
- **evidence_2026_h2**：- **url**：https://www.vals.ai/benchmarks/srebench
- **date**：2026-11-05
- **organization**：Vals AI
- **note**：当前方法与榜单页展示多家前沿模型的实测结果；11月5日更新、37模型二进制逆向理解测试；不能误译为站点可靠性工程基准。

- **url**：https://www.vals.ai/benchmarks
- **date**：2026-11-05
- **organization**：Vals AI
- **note**：目录卡片：Cyber Proprietary SRE Bench Updated: 11/5/2026 Models Tested: 37 Can AI agents work out what a real-world binary does without its source code? Top Models 1 GPT-6 Astra 2 GPT-6.1 Sol 3 Gemini 4 Argon View Details

- **url**：https://openai.com/index/gpt-6-astra/
- **date**：2026-11-07
- **organization**：OpenAI
- **note**：GPT-6 Astra正式发布评测表明确报告SRE Bench，作为近期厂商采用证据。
- **trending**：- **heat_confidence**：A
- **summary**：8月发布的二进制逆向评测已进入 GPT-6 Astra 正式发布表，Vals 11月仍更新37模型榜。

> 近期热门证据取自候选研究与本轮重开页面；A级：多家前沿实验室或评测机构独立采用。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks)（访问 2026-11-07）；[来源3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### 论文修订历史

v1 2026-08-11；v2 2026-10-01

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 污染与争议

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 衍生与版本关系

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 官方榜单

https://www.vals.ai/benchmarks/srebench

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 独立评测覆盖

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：GPT-6 Astra
- **score**：56.87%
- **metric**：Accuracy
- **result_type**：官方榜单快照
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST

- **rank**：2
- **model**：GPT-6.1 Sol
- **score**：50.76%
- **metric**：Accuracy
- **result_type**：官方榜单快照
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST

- **rank**：3
- **model**：Gemini 4 Argon
- **score**：44.27%
- **metric**：Accuracy
- **result_type**：官方榜单快照
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST

- **rank**：4
- **model**：Claude Opus 5.5
- **score**：33.59%
- **metric**：Accuracy
- **result_type**：官方榜单快照
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST

- **rank**：5
- **model**：Daybreak Blue
- **score**：31.68%
- **metric**：Accuracy
- **result_type**：官方榜单快照
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 覆盖与时效说明

Vals 页面自写更新 2026-11-05，共37个模型。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 公开反馈

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2608.11469

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 其他文档

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组按任务要求不上传Drive；原始PDF URL见original_files。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 变更记录

### changelog

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

