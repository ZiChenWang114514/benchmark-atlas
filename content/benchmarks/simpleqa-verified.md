# SimpleQA Verified

> Benchmark Constitution，深度复核 2026-11-08。

SimpleQA Verified是面向参数知识、禁止搜索工具的1,000题短事实问答集。它的贡献不只是缩小原SimpleQA，而是去重、纠正来源冲突、平衡答案类型并改进数值判分。本档将官方Kaggle当前Score、论文历史F1和Epoch反弃答mean_score严格分轨，避免相似名称掩盖不同协议。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）；[来源3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）

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

v2（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 发布日期

2025-09-10 （arXiv v1提交2025-09-10；PDF首页同日）

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 主板块

语言

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 领域

```json
[
 "语言"
]
```

> 编辑标签

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 许可与适用范围

MIT（HF官方README YAML明确license: mit）

[来源1](https://huggingface.co/datasets/google/simpleqa-verified/raw/main/README.md)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2509.07968

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 官方代码

https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified

> 官方提供Kaggle starter notebook与评测提示；没有把另一个项目的GitHub冒充本基准代码。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 数据

https://huggingface.co/datasets/google/simpleqa-verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 官方入口

https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）

### 论文标题

SimpleQA Verified: A Reliable Factuality Benchmark to Measure Parametric Knowledge

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 发起与维护

### 发起方

Google DeepMind 与 Google Research

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 合作/参与机构

Kaggle托管数据与官方榜；论文致谢Gemini Factuality团队提供反馈。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 作者

```json
[
 "Lukas Haas"
 "Gal Yona"
 "Giovanni D’Antonio"
 "Sasha Goldshtein"
 "Dipanjan Das"
]
```

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 维护方

Google DeepMind / Google Research

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 资助

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

### 污染控制

清洗不等于完整去污染证明；公开数据不应用于训练后再报告无污染成绩。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 数据形式

### 题量

1,000题

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 任务形式

问题、gold短答案、原始索引、topic、answer_type、multi_step、requires_reasoning及来源URLs。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 模态

```json
[
 "文本"
]
```

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 语言

英语

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 难度

长尾事实知识；构建时优先保留GPT-4o、Gemini 2.0 Flash与Claude 3.7 Sonnet均答错的题，再选择最终1,000道较难题。元数据中3.7%需推理、7.3%为多步。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 公开与隐藏划分

公开1,000题；无本次核实到的独立隐藏测试划分。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 评测方法

### 指标

原始论文同时报告Accuracy、Accuracy given attempted、F1、Attempted与Hedged。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 评分

gpt-4.1-2025-04-14自动分成CORRECT、INCORRECT、NOT_ATTEMPTED；F1是Accuracy与Accuracy given attempted的调和平均，非token级F1；数字答案按题目明确允许区间判分。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 运行设置

禁止搜索／检索工具；开启工具会使基准过易。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 评测工具

Kaggle官方starter notebook；论文附录A完整公布autorater提示。

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 可比性

Epoch anti-abstention配置的mean_score不得直接冒充论文F1；不同任务版本分轨。

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
 "version": "待核实"
 "heat_confidence": "A"
 "why_trending": "候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。"
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "当前ECI组成明确列出该benchmark；纳入不等于运行。"
 }
 {
 "url": "https://epoch.ai/data/benchmarks.csv"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "本次读取CSV并提取成功运行记录，含2026H2运行。"
 }
 ]
}
```

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2025-09-10"
 }
 {
 "version": "v2"
 "submitted_at": "2026-03-10"
 }
]
```

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 饱和与能力边界

Kaggle 2026-10-20展示最高Score 77.5%；论文v2历史F1最高55.6。工具检索会使任务近乎可解完，故不能把有工具成绩解释为参数知识饱和。

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 风险与争议

题集公开、依赖参数知识；检索增强结果与无工具协议不具可比性。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-07）

### 系列与衍生关系

基于OpenAI SimpleQA的4,326题筛选与修订；Verified为1,000题独立清洗版，不能把原SimpleQA分数直接替代。

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）；[来源3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）

### 官方入口

https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）

### 独立来源

https://epoch.ai/data/benchmarks.csv

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 分来源与协议结果

#### official Kaggle current

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Gemini 3.1 Pro Preview | 77.5 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.6,"source_date":"2026-10-20"} |
| 2 | GPT-6 Astra | 75.8 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.6,"source_date":"2026-10-20"} |
| 3 | Gemini 4 Argon | 75.6 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.6,"source_date":"2026-10-20"} |
| 4 | Gemini 3.8 Flash | 74.6 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.7,"source_date":"2026-10-20"} |
| 5 | GPT-6.1 Sol | 73.8 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.8,"source_date":"2026-10-20"} |
| 6 | Gemini 3 Pro Preview | 72.1 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.9,"source_date":"2026-10-20"} |
| 7 | GPT-5.6 Sol | 69.2 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":2.9,"source_date":"2026-10-20"} |
| 8 | GPT-6 Sol | 64.4 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.0,"source_date":"2026-10-20"} |
| 9 | Claude Opus 5 | 63.3 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 10 | Grok 4.7 | 59.4 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 11 | Grok 4.5 | 53.8 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 12 | Qwen 3 235B A22B Thinking | 53.7 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.4,"source_date":"2026-10-20"} |
| 13 | Grok 4.6 | 52.9 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.1,"source_date":"2026-10-20"} |
| 14 | Claude Opus 4.6 | 45.2 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.1,"source_date":"2026-10-20"} |
| 15 | Claude Sonnet 5.5 | 44.7 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 16 | Claude Opus 4.8 | 44.5 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.1,"source_date":"2026-10-20"} |
| 17 | Deepseek V4.1 Flash | 42.3 | Kaggle页面Score (%)；不擅自改名为F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |

#### paper v2 Table 7 historical; no tools

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Gemini 2.5 Pro | 55.6 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 2 | GPT 5 | 52.3 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 3 | o3 | 51.9 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 4 | GPT 4.1 | 39.9 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 5 | GPT 4o | 34.9 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 6 | DeepSeek R1 (0528) | 33.3 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 7 | Claude Opus 4 | 28.3 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 8 | Gemini 2.5 Flash | 28.2 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 9 | GPT 5 Mini | 24.6 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 10 | o4-mini | 23.4 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 11 | Claude Sonnet 4 | 18.7 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 12 | GPT 5 Nano | 14.4 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |
| 13 | Gemini 2.5 Flash Lite | 11.1 | F1 (%) | {"judge":"gpt-4.1-2025-04-14"} |

#### Epoch anti-abstention 1.0.0

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Gemini 3.1 Pro Preview | 0.735 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"VGeF8Xac4WcSAGgSXVdEBi","run_started_at":"2026-08-11","stderr":"0.013963164754810065"} |
| 2 | Claude Fable 5 (xhigh) | 0.707 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"SEnvgtunRa5GwAtU2sHa87","run_started_at":"2026-08-11","stderr":"0.014399942998441292"} |
| 3 | GPT-5.6 Sol (max) | 0.697 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"UnRUSuZzm2X27TUbpeMPva","run_started_at":"2026-08-11","stderr":"0.014539683710535193"} |
| 4 | Claude Opus 5 (max) | 0.599 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"Zftz2yk4X5NF28JQzjN3hZ","run_started_at":"2026-08-11","stderr":"0.01550610974549837"} |
| 5 | GPT-5.6 Terra (max) | 0.432 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"DienatPbgfgn3EzM7Gvzxr","run_started_at":"2026-08-11","stderr":"0.015672320237336324"} |
| 6 | GPT-5.6 Luna (max) | 0.41 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"CeDghdBk8CqtiFSbUzxNH5","run_started_at":"2026-08-11","stderr":"0.015560917136921657"} |
| 7 | Claude Sonnet 4.6 (high) | 0.355 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"LJyKf8Xy4dymxNHbGLwNdA","run_started_at":"2026-08-11","stderr":"0.015139491543780595"} |
| 8 | Kimi K2.6 | 0.349 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"hHnQVatVTbQjM4sfrjw7GH","run_started_at":"2026-08-11","stderr":"0.015080663991563052"} |
| 9 | Claude Sonnet 4.5 (no thinking) | 0.237 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"MhqeuRVx4JcRfxPQDYPq7Z","run_started_at":"2026-08-11","stderr":"0.013454070462577935"} |
| 10 | GPT-5 mini (high) | 0.216 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"8d5RuFTTJKuJ5iJYmPZVJe","run_started_at":"2026-08-11","stderr":"0.013019735539307761"} |
| 11 | Claude Haiku 4.5 | 0.132 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"J2kUEjR9r6Spd594qDNTTf","run_started_at":"2026-08-11","stderr":"0.010709373963527967"} |
| 12 | GPT-5 nano (high) | 0.117 | mean_score (0–1) | {"task_version":"1.0.0","run_id":"KgUCEfVCyRnY8B5kVChyiD","run_started_at":"2026-08-11","stderr":"0.010169287802713343"} |

#### Epoch anti-abstention 1.2.0

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Gemini 4 Argon (high) | 0.76 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"iq4Y9tXpiyLP25yotySxJW","run_started_at":"2026-10-14","stderr":"0.013512312258920845"} |
| 2 | GPT-6 Astra (max) | 0.756 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"PppwnX7EjXx2SeTcFN8Ujn","run_started_at":"2026-08-30","stderr":"0.013588548437881386"} |
| 3 | GPT-6.1 Sol (max) | 0.739 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"dfT5VD7cQug8XW6GQHyJUF","run_started_at":"2026-09-30","stderr":"0.013895037677965185"} |
| 4 | Claude Opus 5.5 (max) | 0.722 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"CgLfiGcNwMPVzxr8GdNUAK","run_started_at":"2026-09-23","stderr":"0.014174516461485273"} |
| 5 | Claude Fable 5.1 (max) | 0.708 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"ExyL3GN8s34tizrXV3VmS3","run_started_at":"2026-09-02","stderr":"0.014385511563477433"} |
| 6 | Gemini 3.8 Flash (high) | 0.697 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"gZ4bwozTKtpmZTqnqX3a33","run_started_at":"2026-09-03","stderr":"0.014539683710535193"} |
| 7 | Gemini 3.7 Flash (high) | 0.692 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"84ARuGyhQsjgh8umRmBvas","run_started_at":"2026-08-28","stderr":"0.01460648312734278"} |
| 8 | Gemini 3 Flash Preview | 0.668 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"7cc6cDCXjsPjtKt36bbeMR","run_started_at":"2026-08-28","stderr":"0.014899597242811567"} |
| 9 | Gemini 3.5 Flash | 0.662 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"GJ6YsSuzyRD9YXe6SBwvsu","run_started_at":"2026-08-28","stderr":"0.014965960710224383"} |
| 9 | Gemini 3.6 Flash | 0.662 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"F83pa7Gfsb4UNVttTnS5Hk","run_started_at":"2026-08-28","stderr":"0.014965960710224383"} |
| 11 | GPT-5.5 (xhigh) | 0.63 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"TijCafTTJUFrJ6jPGvBbgq","run_started_at":"2026-08-28","stderr":"0.015275252316519465"} |
| 12 | Kimi K3.1 Pro (Together, max) | 0.622 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"HumfsXVh5BZWuTo6Z8Gqnf","run_started_at":"2026-11-06","stderr":"0.015341165254026547"} |
| 13 | GPT-6 Sol (max) | 0.607 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"donMeEKBZZdqpQsojKWJEm","run_started_at":"2026-09-23","stderr":"0.015452824654081525"} |
| 14 | Muse Spark 1.2 (xhigh) | 0.6030150753768844 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"mLLmVVvo6t23MM5yxq7ryW","run_started_at":"2026-08-28","stderr":"0.015518791563606454"} |
| 15 | Muse Spark 1.1 | 0.5778894472361809 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"bCdwpRXgZtvQLYC4wA9JXr","run_started_at":"2026-09-01","stderr":"0.015665429072238852"} |
| 16 | GPT-6.1 Terra (max) | 0.573 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Bixeio8A6SejZtUzFXFSXK","run_started_at":"2026-10-27","stderr":"0.01564978964446219"} |
| 17 | Muse Spark Open (xhigh) | 0.566 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"dNuxLdV4DWqfSvtTq6NnK8","run_started_at":"2026-10-16","stderr":"0.01568087656637504"} |
| 18 | Grok 4.7 (xhigh) | 0.56 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"6izDCw5ygCLZJEKPS8jV5T","run_started_at":"2026-09-23","stderr":"0.015704987954361718"} |
| 19 | Qwen3.7 Max | 0.5576730190571715 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"DMjUrG6eZEqwcQ4SqUoViu","run_started_at":"2026-08-28","stderr":"0.015737359397180177"} |
| 20 | Claude Opus 4.8 | 0.53 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"ViC6pxQZUVS3E9M9iEubF7","run_started_at":"2026-08-28","stderr":"0.015790799515836722"} |
| 21 | DeepSeek V4 Pro 0813 (max) | 0.5290581162324649 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"2xfFf6KZAp2gUWYhHGkFgs","run_started_at":"2026-08-28","stderr":"0.015808394665706597"} |
| 22 | Qwen 3.6 Max (Preview) | 0.5200400801603207 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"iyPiR8GUuyNNA6Fssziq32","run_started_at":"2026-08-28","stderr":"0.015822434816352416"} |
| 23 | Claude Opus 4.7 (xhigh) | 0.517 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"2c4rvmf5N7QXTugrFLMZ83","run_started_at":"2026-08-28","stderr":"0.015810153729833274"} |
| 24 | Kimi K3 (max) | 0.506 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"mZLWt2JSYvJyGhMvji7CT8","run_started_at":"2026-08-28","stderr":"0.015818160898606836"} |
| 25 | GPT-5 (high) | 0.501 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"gTLurbyKU63i2opsGkJGwh","run_started_at":"2026-08-28","stderr":"0.015819268290576817"} |
| 26 | o3 (high) | 0.494 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"CxHSa2gY7ySiPPGTZEZaRt","run_started_at":"2026-08-28","stderr":"0.015818160898606833"} |
| 27 | Grok 4.6 (high) | 0.493 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"TpHYtuPG6kYZFvMK7Z6Hqj","run_started_at":"2026-08-28","stderr":"0.01581774956184353"} |
| 28 | Grok 4.6 (xhigh) | 0.489 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"dKCWFaoGCWJTnD5CPWQGru","run_started_at":"2026-08-28","stderr":"0.015815471195292575"} |
| 29 | Qwen3-Max-Instruct | 0.4874874874874875 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"fXG2GPt5F25tHRTPhAoZ4K","run_started_at":"2026-08-28","stderr":"0.01582226675546796"} |
| 30 | Grok 4.5 (high) | 0.483 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"7HWW3sjRstKzb9JpcnvLaV","run_started_at":"2026-08-28","stderr":"0.015810153729833274"} |
| 31 | GPT-5.1 (high) | 0.48 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"QCLnRy69NBH9ip3VYtQneh","run_started_at":"2026-08-28","stderr":"0.015806639423035177"} |
| 32 | Qwen3.8 Max (0902) (xhigh) | 0.473 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"nBcLJJomVoeg2zh5F8Mnsu","run_started_at":"2026-09-03","stderr":"0.01579621855130273"} |
| 33 | Claude Opus 4.6 (max) | 0.47 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"85fhMxLaebWtLoi6oLpTbi","run_started_at":"2026-08-28","stderr":"0.015790799515836722"} |
| 34 | DeepSeek v4 Pro (max) | 0.46993987975951906 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Sq9xqkVTmFvELpQy9KH5TM","run_started_at":"2026-08-28","stderr":"0.015806515332355317"} |
| 35 | Claude Sonnet 5.5 (max) | 0.465 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"GtJ5yd3ZPQ7HVcm6Q9ssQz","run_started_at":"2026-09-30","stderr":"0.015780495050030086"} |
| 36 | GPT-5.4 Pro (xhigh) | 0.463 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"RfSJbuuuMkeVHQj7xrth4u","run_started_at":"2026-08-28","stderr":"0.015775927227262426"} |
| 37 | Qwen3.8 Max (xhigh) | 0.458 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"bfftd5EzUK9yAekafEofvK","run_started_at":"2026-08-28","stderr":"0.015763390640483554"} |
| 38 | Claude Opus 4.5 (32k thinking) | 0.457 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"CA5LW4phRnHSsZUGXEm8H6","run_started_at":"2026-08-28","stderr":"0.0157606915901365"} |
| 39 | GPT-5.4 (xhigh) | 0.451 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"AzCkm282PLhDdLJ8DnAQQc","run_started_at":"2026-08-28","stderr":"0.015743152379585443"} |
| 40 | Doubao Seed 2.1 Pro (high) | 0.447 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"7TdGnviq5zZhNSXK5nJSAL","run_started_at":"2026-10-29","stderr":"0.0157301760460091"} |
| 41 | Qwen 3.6 Plus (2026-04-02) | 0.44144144144144143 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"4LWNorP8Fy8V8doxirNFcH","run_started_at":"2026-08-28","stderr":"0.015718302238794238"} |
| 42 | DeepSeek V4.1 Flash (max) | 0.429 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"3JJ4ChNxMo8CGAh3HrKNrw","run_started_at":"2026-10-13","stderr":"0.015658997547870177"} |
| 43 | DeepSeek V4.1 Flash 1017 (max) | 0.425 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Ei4XWaCH5drYUnDRo2MYCW","run_started_at":"2026-10-20","stderr":"0.01564032031704017"} |
| 44 | Doubao Seed Evolving (Nov 2026, high) | 0.419 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"PWieWgMJqvCcm7zkN9iYqH","run_started_at":"2026-11-03","stderr":"0.015610338967577953"} |
| 45 | GPT-6 Luna (max) | 0.414 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"HX9sRVWJtZiNvneALnVzs8","run_started_at":"2026-09-23","stderr":"0.015583544104177553"} |
| 46 | o1 (high) | 0.411 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"LQfu4ngArcgMEyQZxuR7r4","run_started_at":"2026-09-01","stderr":"0.01556667341859915"} |
| 47 | GLM-5.3 (max) | 0.41 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"TY8R8FV7zCwByEipkqyg2P","run_started_at":"2026-08-29","stderr":"0.015560917136921659"} |
| 48 | Qwen3-235B-A22B (Jul 2025) | 0.4044044044044044 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"4ACEC4x26HWRGiAepHGw43","run_started_at":"2026-08-28","stderr":"0.015535255725079345"} |
| 49 | Inkling (xhigh) | 0.403 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"bpnzC6CCi3hWuKCfqX4KEY","run_started_at":"2026-08-28","stderr":"0.015518757419066513"} |
| 50 | Doubao-Seed-2.0 Pro (high) | 0.394 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"GvNEYw523w8aUy63WpgovD","run_started_at":"2026-10-29","stderr":"0.015459721957493382"} |
| 51 | GPT-5.2 (xhigh) | 0.371 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"E3325ytkSNYP8ez53VA4fE","run_started_at":"2026-08-28","stderr":"0.015283736211823095"} |
| 52 | Kimi K2.7 Code | 0.365 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"5AijYw5bFJtSuahnbzNo6Z","run_started_at":"2026-08-28","stderr":"0.015231776226264846"} |
| 53 | Kimi K2.5 | 0.343 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"RbXXg4JEbTSBnzw3CMSHnD","run_started_at":"2026-08-28","stderr":"0.015019206922357007"} |
| 53 | GPT-5.2 (high) | 0.343 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Xp4qkZ32zjDeSYii2eQpnm","run_started_at":"2026-08-28","stderr":"0.015019206922357007"} |
| 55 | GLM-5.2 | 0.342 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"WgjFZzojpiv54XqUhvfuUG","run_started_at":"2026-08-28","stderr":"0.015008706182121802"} |
| 56 | GLM-5.1 | 0.34 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"R2fMFAtRXah864hMifdQGV","run_started_at":"2026-08-28","stderr":"0.014987482264363972"} |
| 57 | Claude Sonnet 5 (max) | 0.337 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"LPo74T9L3CawnKX5LLUrSZ","run_started_at":"2026-08-28","stderr":"0.014955087918653461"} |
| 58 | DeepSeek V4 Flash 0731 (max) | 0.33633633633633636 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"TqFmiGvqozt7TSZYmhgF8m","run_started_at":"2026-08-28","stderr":"0.01495531772489948"} |
| 59 | Grok 4.3 Beta | 0.332 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Y39ZRp553ULpUDBV2XrBbc","run_started_at":"2026-08-28","stderr":"0.014899597242811567"} |
| 60 | Claude Sonnet 5 (xhigh) | 0.329 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Qw4tGw38pk4sdsEehhrLSR","run_started_at":"2026-08-28","stderr":"0.014865395385928355"} |
| 61 | GPT-5.2 (low) | 0.328 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Cyw3GA9a64AmT4pqLAhtTF","run_started_at":"2026-08-28","stderr":"0.014853842487270312"} |
| 61 | Claude Sonnet 4.6 (max) | 0.328 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Zs5fCvNzaz8LhqgwDSAztU","run_started_at":"2026-08-28","stderr":"0.014853842487270312"} |
| 63 | GPT-5.2 (medium) | 0.327 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"esr5dcSuHiVoteo6vZfHjP","run_started_at":"2026-08-28","stderr":"0.014842213153411162"} |
| 64 | GLM-4.7 | 0.322 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"aYau6EG7CCaWVSyVq3vvQc","run_started_at":"2026-08-28","stderr":"0.014782913600996744"} |
| 65 | Doubao Seed 2.0 Lite (Apr 2026, high) | 0.315 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"3rTiRa2THK8MWXtVJZQHxS","run_started_at":"2026-10-29","stderr":"0.014696631960792619"} |
| 66 | GPT-4.1 | 0.311 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"avdYKfKUuY6EvfVdxftBE8","run_started_at":"2026-09-01","stderr":"0.014645596385722692"} |
| 67 | Claude Sonnet 4.5 (59k thinking) | 0.307 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"XQEGUQjpXupjdyKoGuSmum","run_started_at":"2026-08-28","stderr":"0.014593284892852741"} |
| 68 | Grok 4.20 | 0.302 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"GVm7khGvtdnQKGfkgAHD8q","run_started_at":"2026-08-28","stderr":"0.014526080235459494"} |
| 69 | Doubao Seed 2.1 Turbo (high) | 0.297 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"9wS2NJacFaJp9tkq8FSRyF","run_started_at":"2026-10-30","stderr":"0.01445683229480096"} |
| 70 | GPT-5.4 mini (high) | 0.294 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Z3pjKgAULY9j9wmzQpdqZG","run_started_at":"2026-08-28","stderr":"0.014414290540008265"} |
| 71 | GPT-4o (Aug 2024) | 0.26 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"bDFqfWxMG7gLDq4Mz8PRTP","run_started_at":"2026-09-01","stderr":"0.01387777332977422"} |
| 72 | Qwen3.5 Plus | 0.2535070140280561 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"jrawnM2wHFbVfJFJsap4kS","run_started_at":"2026-08-28","stderr":"0.013777178222916077"} |
| 73 | Claude Haiku 5.5 (max) | 0.238 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"NwnrUMtveqHDYB2Um4ycmA","run_started_at":"2026-10-09","stderr":"0.013473586661967093"} |
| 74 | Mistral Large 4 (high) | 0.224 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"JYSfRXRddi6hYzpnSD3G7V","run_started_at":"2026-11-02","stderr":"0.013190830072364589"} |
| 75 | Qwen3.5 Flash | 0.2032032032032032 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"K8zTckSXLKLesoLBv24TWc","run_started_at":"2026-08-28","stderr":"0.012737194890497593"} |
| 76 | Mistral Large 4 Preview (high) | 0.2 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"hvNNKdnzLvr9X8zVxWKcfk","run_started_at":"2026-10-09","stderr":"0.012655439943366657"} |
| 77 | o4-mini (low) | 0.196 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"Dzky9brdTFbSoVd2zTKiUp","run_started_at":"2026-08-28","stderr":"0.012559527926707347"} |
| 78 | Inkling Small (xhigh) | 0.191 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"eJfbDKqeg9kNXFoxpeV7HG","run_started_at":"2026-08-28","stderr":"0.012436787112179482"} |
| 79 | o4-mini (high) | 0.188 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"gaGdPvvfvAw7MjP4HaVQCT","run_started_at":"2026-08-28","stderr":"0.012361586015103758"} |
| 80 | Doubao-Seed-1.6 (thinking) | 0.174 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"jn6ts6NmQFtBGauL9n5i82","run_started_at":"2026-10-31","stderr":"0.01199449323097345"} |
| 81 | Qwen 3.6 Flash (2026-04-16) | 0.15915915915915915 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"FoMSS4FmH3VxpsvZiUJPCv","run_started_at":"2026-08-28","stderr":"0.011579970321213651"} |
| 82 | o3-mini (high) | 0.153 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"UCba4H3NNtUiWXMisWnh9g","run_started_at":"2026-09-01","stderr":"0.011389500459665504"} |
| 83 | GPT-4.1 mini | 0.127 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"gYV4CJTjSd7VonfzMmnwcw","run_started_at":"2026-09-01","stderr":"0.010534798620855644"} |
| 84 | Claude 3 Opus | 0.126 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"NxVp4VF8uQbL5S6hx6HFRB","run_started_at":"2026-09-01","stderr":"0.010499249222407964"} |
| 84 | Claude Haiku 4.5 | 0.126 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"VhBM9HgJ2RuSVwXriRXMVJ","run_started_at":"2026-08-28","stderr":"0.010499249222407964"} |
| 86 | GPT-5.4 nano (high) | 0.117 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"3QBsxKkbF2R2LEXTd6HDrJ","run_started_at":"2026-08-28","stderr":"0.010169287802713345"} |
| 87 | Gemma 4 31B IT | 0.104 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"D5cbXacPnJ8akq2jAtifEQ","run_started_at":"2026-08-28","stderr":"0.009658016218524242"} |
| 88 | GPT-4o mini | 0.083 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"DLr586bZUHpghAf8m3GRSm","run_started_at":"2026-09-01","stderr":"0.008728527206074758"} |
| 89 | GPT-4.1 nano | 0.06 | mean_score (0–1) | {"task_version":"1.2.0","run_id":"A4JEeJR5LQfLR3Hb8z7kL2","run_started_at":"2026-09-01","stderr":"0.007513751157474971"} |

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源3](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖与时效

官方Kaggle可读17行（页称显示48/58，并不声称本档收齐58模型）；论文Table 7完整13行历史F1独立成轨；Epoch对每个精确model+task_version取最新成功run，1.0.0/1.2.0分轨。Kaggle Score列名称、论文F1与anti-abstention mean_score不得混同。

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源3](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 官方反馈

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 公开社区

https://huggingface.co/datasets/google/simpleqa-verified/discussions

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）

### 隐私边界

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2509.07968v2

[来源1](https://arxiv.org/pdf/2509.07968v2)（访问 2026-11-08）

### PDF SHA-256

df3bf66ebdba21e01dec4fc760d53ca8944ed2010bf1a15e9e57b5a404ed8686

> 本次实际下载的PDF字节计算；未上传。

[来源1](https://arxiv.org/pdf/2509.07968v2)（访问 2026-11-08）

### PDF字节数

```json
815212
```

[来源1](https://arxiv.org/pdf/2509.07968v2)（访问 2026-11-08）

### 文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "已打开一手材料"
 "url": "https://arxiv.org/abs/2509.07968"
 "accessed": "2026-11-08"
 }
 {
 "type": "已打开一手材料"
 "url": "https://huggingface.co/datasets/google/simpleqa-verified"
 "accessed": "2026-11-08"
 }
 {
 "type": "已打开一手材料"
 "url": "https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified"
 "accessed": "2026-11-08"
 }
]
```

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）；[来源3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）

### PDF归档

待核实

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## 变更记录

```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-08"
 最近复核
 }
]
```

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）；[来源3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）
