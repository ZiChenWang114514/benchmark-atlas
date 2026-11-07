# SimpleQA Verified

> 核验：2026-11-07（KST / Asia/Seoul）。官方资料中文改写；待核实不等于未公开。原始数据与第三方实现、历史论文与当前榜单分轨。

编辑状态：研究快照；trending: A；未核实字段保留标记

## 基本信息

### 简称

SimpleQA Verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 全称

SimpleQA Verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 论文版本

v2（本次arXiv返回版本）

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 主板块

语言

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 领域标签

- 语言

> 编辑标签

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 许可证

MIT（官方数据集卡声明）

[来源1](https://huggingface.co/datasets/google/simpleqa-verified/raw/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2509.07968

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 官方代码

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/google/simpleqa-verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 官方主页

https://huggingface.co/datasets/google/simpleqa-verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 论文标题

SimpleQA Verified: A Reliable Factuality Benchmark to Measure Parametric Knowledge

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 发起与维护

### 发起方

Google DeepMind 与 Google Research

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 作者

- Lukas Haas
- Gal Yona
- Giovanni D’Antonio
- Sasha Goldshtein
- Dipanjan Das

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 维护方

Google DeepMind / Google Research

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 资助方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## 设计目标

### 衡量能力

不用搜索工具、仅依赖模型参数的短格式事实知识问答。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 设计背景

修复原SimpleQA的标签噪声、题目冗余与主题／答案类型偏差。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 构建方式

### 题目来源

从OpenAI SimpleQA筛选、修订。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 出题者背景

Google DeepMind与Google Research论文作者负责多阶段过滤与手工复核。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-07）

### 审核流程

源文档去重、语义与TF-IDF去重、主题平衡、冲突来源调和、人工复核。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 质量控制

每题提供至少2条支持gold答案的URL，并修订数字可接受范围。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 去污染

清洗不等于完整去污染证明；公开数据不应用于训练后再报告无污染成绩。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 数据形式

### 题量与规模

1,000题

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 题型

问题、gold短答案、原始索引、topic、answer_type、multi_step、requires_reasoning及来源URLs。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 模态

- 文本

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 语言

英语

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 难度

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 公开与隐藏划分

公开1,000题；无本次核实到的独立隐藏测试划分。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 评测方法

### 指标

原始论文同时报告Accuracy、Accuracy given attempted、F1、Attempted与Hedged。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 评分

GPT-4.1版本autorater将回答分为正确、错误、未尝试；数字允许范围按题给定。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 提示与运行设置

禁止搜索／检索工具；开启工具会使基准过易。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 官方评测脚本

Kaggle官方starter notebook含autorater提示。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 可比性警示

Epoch anti-abstention配置的mean_score不得直接冒充论文F1；不同任务版本分轨。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 当前版本与热度证据

- **version**：待核实
- **heat_confidence**：A
- **why_trending**：候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。
- **evidence_2026_h2**：
  - **url**：https://epoch.ai/data/eci-documentation/data
  - **date**：2026-11-07
  - **date_type**：observed_on
  - **organization**：Epoch AI
  - **note**：当前ECI组成明确列出该benchmark；纳入不等于本轮运行。
  - **url**：https://epoch.ai/data/benchmarks.csv
  - **date**：2026-11-07
  - **date_type**：observed_on
  - **organization**：Epoch AI
  - **note**：本次读取CSV并提取成功运行记录，含2026H2运行。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 版本与材料差异

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 污染与争议

题集公开、依赖参数知识；检索增强结果与无工具协议不具可比性。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重口径；具体版本差异仍以官方材料为准。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 为什么近期热门

候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。

- 2026-11-07（observed_on）：当前ECI组成明确列出该benchmark；纳入不等于本轮运行。 [来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

- 2026-11-07（observed_on）：本次读取CSV并提取成功运行记录，含2026H2运行。 [来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 官方榜单

https://epoch.ai/data/eci-documentation/data

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 独立评测覆盖

https://epoch.ai/data/benchmarks.csv

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：Gemini 4 Argon (high)
- **score**：0.76
- **metric**：CSV mean_score (0–1)
- **task_version**：1.2.0
- **original_task_name**：SimpleQA Verified (anti-abstention)
- **run_id**：iq4Y9tXpiyLP25yotySxJW
- **run_started_at_kst**：2026-10-14T02:15:14+09:00
- **stderr**：0.013512312258920845
- **source_url**：https://epoch.ai/data/benchmarks.csv
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：Epoch CSV同task/版本已成功运行记录按mean_score排序；非跨harness完整总榜
- **rank**：2
- **model**：GPT-6 Astra (max)
- **score**：0.756
- **metric**：CSV mean_score (0–1)
- **task_version**：1.2.0
- **original_task_name**：SimpleQA Verified (anti-abstention)
- **run_id**：PppwnX7EjXx2SeTcFN8Ujn
- **run_started_at_kst**：2026-08-30T23:57:43+09:00
- **stderr**：0.013588548437881386
- **source_url**：https://epoch.ai/data/benchmarks.csv
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：Epoch CSV同task/版本已成功运行记录按mean_score排序；非跨harness完整总榜
- **rank**：3
- **model**：GPT-6.1 Sol (max)
- **score**：0.739
- **metric**：CSV mean_score (0–1)
- **task_version**：1.2.0
- **original_task_name**：SimpleQA Verified (anti-abstention)
- **run_id**：dfT5VD7cQug8XW6GQHyJUF
- **run_started_at_kst**：2026-09-30T07:00:34+09:00
- **stderr**：0.013895037677965185
- **source_url**：https://epoch.ai/data/benchmarks.csv
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：Epoch CSV同task/版本已成功运行记录按mean_score排序；非跨harness完整总榜

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 覆盖与时效说明

CSV快照；只对上述筛选配置已成功记录排序，不冒充所有模型官方统一排名。运行开始时间不等于榜单更新时间。SimpleQA的anti-abstention mean_score不等于原论文F1。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 官方社交／讨论渠道

数据集卡指向官方discussion forum作为问题反馈渠道。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2509.07968

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 其他文档

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### Drive PDF归档

待核实（本轮未上传）

## 变更记录

### 变更记录

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）
