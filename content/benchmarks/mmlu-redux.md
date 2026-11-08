# MMLU-Redux

> Benchmark Constitution · 深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MMLU-Redux首先是一项对MMLU题目错误的人工审计，而不是把原题全部重写的全量替代题库。当前2.0覆盖57学科各100题；旧README的30科3,000题属于早期范围。评测需要区分原标签、无错子集和修正答案，也要把模型答题准确率与错误检测F1等指标分开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 简称

MMLU-Redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 全称

MMLU-Redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 基准版本

MMLU-Redux 2.0（本条目数据入口；原始论文和旧仓库描述不等于2.0全量统计）

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 论文版本

arXiv v3

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 发布日期

2024-06-06（；arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 主板块

语言

> Benchmark Constitution编辑归档，不是论文指定的唯一领域。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 领域标签

- 纠错后的多学科知识

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 许可证与权利边界

CC-BY-4.0（官方仓库LICENSE和2.0 HF卡片）；其原始MMLU题库来源另有MIT授权声明。

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/LICENSE)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0/raw/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2406.04127

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 代码仓库

https://github.com/aryopg/mmlu-redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 官方主页

https://github.com/aryopg/mmlu-redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 论文标题

Are We Done with MMLU?

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

论文作者来自 University of Edinburgh、Sapienza University of Rome、University of Bari、UCL、University of Trento 等；此为作者单位记录。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 合作方

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 作者

- Gema, Aryo Pradipta
- Leang, Joshua Ong Jun
- Hong, Giwon
- Devoto, Alessio
- Mancino, Alberto Carlo Maria
- Saxena, Rohit
- He, Xuanli
- Zhao, Yu
- Du, Xiaotang
- Madani, Mohammad Reza Ghasemi
- Barale, Claire
- McHardy, Robert
- Harris, Joshua
- Kaddour, Jean
- van Krieken, Emile
- Minervini, Pasquale

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 维护方

官方公开代码托管于 aryopg；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源](https://github.com/aryopg/mmlu-redux)（访问 2026-11-08）

### 资助

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## 设计目标

### 衡量能力

重新检查 MMLU 的题目与答案质量，区分模型失误和基准本身的错误。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 设计背景

已有高分不代表题库可靠；题干歧义、错误标签和缺少正确选项会扭曲模型排序与能力判断。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## 构建方式

### 题目来源

从 MMLU 每个学科抽取 100 题，并人工标注题目和答案中的错误。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 出题与审阅者背景

论文v3明确14名人类专家重新标注5,700题；原题沿用MMLU，不是5,700道专家新编题。

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### 审核流程

标注者先评估题目表述，再核验原标签；鼓励精确搜索原题并查询政府、教材等可信资料；超出专业判断能力时标为 expert。

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 质量控制

分层错误标注：题干/选项清晰度、无正确答案、多正确答案、错误ground truth；正确标为ok，无法判断为expert。论文表5在5,700条中报告93.51% OK，各学科错误率不应外推成全MMLU比例。

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0/raw/main/README.md)（访问 2026-11-08）

### 去污染及其证据边界

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

当前 2.0 数据卡与正式论文覆盖 57 学科、5,700 道人工标注题；早期仓库/版本介绍为 30 学科、3,000 题，不能混用。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 题型

MMLU 四选一题，加错误标签、修正答案及依据

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 模态

文本

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 语言

英语

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 难度

沿用 MMLU 跨教育阶段、跨学科难度；主要变化是质量核验，不是统一增加难度。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 公开与隐藏划分

2.0 数据卡按学科提供 test，每科 100 条；它是 MMLU 抽样纠错集，不是 MMLU 全量替代物。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## 评测方法

### 指标

纠错前后准确率与题目错误类型统计。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 评分方法

依据人工纠错结果分析模型评价变化；需明确是原始标签、无错子集还是修正标签得分。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 运行与提示设置

论文分析包含 HELM v1.3.0（2024-05-15）预测；不同模型/实验的提示设置需分别记录。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 官方脚本

https://github.com/aryopg/mmlu-redux

[来源](https://github.com/aryopg/mmlu-redux)（访问 2026-11-08）

### 可比性警示

原题与选项即使有歧义也不直接改写；应依 error_type 过滤并参考 correct_answer。2.0数据卡与旧版30学科描述并存，须记录实际配置和筛选口径。

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

官方发布入口 mmlu-redux-2.0；数据卡说明仍保留旧版30学科描述，版本统计需区分。

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2024-06-06；- **timezone**：；- - **version**：v2；- **submitted_at**：2024-06-08；- **timezone**：；- - **version**：v3；- **submitted_at**：2025-01-10；- **timezone**：

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 饱和情况

该工作主要诊断题库错误；不能由纠错集上的分数推出 MMLU 已饱和或尚未饱和。

[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 污染、争议与限制

版本冲突：早期材料 3,000 题/30 学科，2.0 与 NAACL 正式论文 5,700 题/57 学科。本条以当前 2.0 为规模基准，保留早期记录而不静默覆盖。

[来源](https://aclanthology.org/2025.naacl-long.262/)（访问 2026-11-07）

### 衍生与版本关系

LabelChaos为该研究用于训练错误检测器的合成扰动数据；由六个人工标注数据集合并生成，不是MMLU-Redux 2.0的新测评划分。

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/README.md)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（；采集日，不冒充评测运行日）

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### 官方入口

https://arxiv.org/abs/2406.04127

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 第三方覆盖入口

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### 原论文v3表2 / Virology / overall instances（HELM）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.60 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.58 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.57 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.60 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.55 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.60 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.56 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.60 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.58 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.58 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Virology / correct instances（Redux无错子集）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.91 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.88 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.93 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.91 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.91 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.86 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.88 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.93 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.93 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.93 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Logical Fallacies / overall instances（HELM）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.93 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.90 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.92 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.88 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.90 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.87 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.91 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.87 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.86 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.84 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Logical Fallacies / correct instances（Redux无错子集）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.96 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.96 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.96 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.99 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.99 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.99 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.96 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 1.00 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.92 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.96 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / College Chemistry / overall instances（HELM）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.59 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.60 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.60 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.61 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.62 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.55 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.65 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.53 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.58 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.59 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / College Chemistry / correct instances（Redux无错子集）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.73 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.72 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.76 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.71 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.72 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.75 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.68 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.76 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.67 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.64 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Professional Law / overall instances（HELM）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.75 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.72 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.70 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.72 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.67 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.73 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.66 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.67 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.64 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.67 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Professional Law / correct instances（Redux无错子集）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.77 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.72 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.72 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.70 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.67 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.68 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.74 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.63 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.61 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.65 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Human Sexuality / overall instances（HELM）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.94 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.91 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.86 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.91 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.37 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.91 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.89 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.90 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.40 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.86 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### 原论文v3表2 / Human Sexuality / correct instances（Redux无错子集）

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude 3.5 Sonnet (20240620) | 0.98 | accuracy / proportion (0–1) |
| Claude 3 Opus (20240229) | 0.96 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (405B) | 0.91 | accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.96 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (001) | 0.94 | accuracy / proportion (0–1) |
| GPT-4 (0613) | 0.43 | accuracy / proportion (0–1) |
| Qwen2 Instruct (72B) | 0.94 | accuracy / proportion (0–1) |
| GPT-4 Turbo (2024-04-09) | 0.93 | accuracy / proportion (0–1) |
| Gemini 1.5 Pro (0409 preview) | 0.95 | accuracy / proportion (0–1) |
| Llama 3.1 Instruct Turbo (70B) | 0.96 | accuracy / proportion (0–1) |

- **Claude 3.5 Sonnet (20240620)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Claude 3 Opus (20240229)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4o (2024-05-13)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (001)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 (0613)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Qwen2 Instruct (72B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **GPT-4 Turbo (2024-04-09)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：五个高错误率学科对照，不是57科全库总分；过滤无错子集≠改写所有答案

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Jev研究表2 / 混合来源比较

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Jev（研究表2原标签） | 95.0 | accuracy（研究表2口径） / % |
| Qwen3.8-Max（研究表2原标签） | 94.3 | accuracy（研究表2口径） / % |
| Claude Opus 5.5（研究表2原标签） | 94.2 | accuracy（研究表2口径） / % |

- **Jev（研究表2原标签）**：- **scope**：2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜；- **evaluation_date**：论文2026-10-08；精确运行日期和API版本待核实；- **snapshot_date**：2026-11-08
- **Qwen3.8-Max（研究表2原标签）**：- **scope**：2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜；- **evaluation_date**：论文2026-10-08；精确运行日期和API版本待核实；- **snapshot_date**：2026-11-08
- **Claude Opus 5.5（研究表2原标签）**：- **scope**：2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜；- **evaluation_date**：论文2026-10-08；精确运行日期和API版本待核实；- **snapshot_date**：2026-11-08

[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）


[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 覆盖范围与时效

新增原论文表2五科的overall/correct实例对照，均是原始小数精度；Jev研究95.0等结果另轨保留。后者表中含当篇实测和引用成绩，不是Redux官方统一重测榜或同协议实时排名。

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

- aryo.gema@ed.ac.uk
- p.minervini@ed.ac.uk

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 公开反馈

https://github.com/aryopg/mmlu-redux/issues

[来源](https://github.com/aryopg/mmlu-redux)（访问 2026-11-08）

### 官方社交

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2406.04127

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### PDF SHA-256

a45720c5df8c7e7fe243846a849e4799a07fa453d77b4cd55094c6e058b8b8ab

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### PDF字节数

747909

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### 文件夹

- **id**：1xg8wVXxTJ3hwpqxa6FxWizpKQXYGDW2c
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍 Google Doc；- **id**：1PvrGue4_EH6leNh5jz4DzwZGfpdqSK2qTbkzo-WgwSM；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：1ta0g5jbJkYUKiPSsZySck8P4n0Y-9zAn
- **webViewLink**：

[来源]( 2026-11-07）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/README.md)（访问 2026-11-08）
