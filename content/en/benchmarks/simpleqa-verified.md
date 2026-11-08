# SimpleQA Verified

> Benchmark Constitution, in-depth review 2026-11-08.

SimpleQA Verified is a 1,000-question short factual question-answering set aimed at parametric knowledge, with search tools forbidden. Its contribution is not only that it shrinks the original SimpleQA. It also removes duplicates, corrects source conflicts, balances answer types, and improves numerical judging. This entry keeps the current official Kaggle Score, the historical F1 in the paper, and Epoch's anti-abstention mean_score on strictly separate tracks, so that similar names do not conceal different protocols.

[Source 1](https://arxiv.org/abs/2509.07968) (accessed 2026-11-08); [Source 2](https://huggingface.co/datasets/google/simpleqa-verified) (accessed 2026-11-08); [Source 3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified) (accessed 2026-11-08)

## Basic information

### Short name

SimpleQA Verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Full name

SimpleQA Verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Benchmark version

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### Paper version

v2 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### Release date

2025-09-10 (arXiv v1 submitted 2025-09-10; the PDF first page is the same day)

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### Section

Language

> Benchmark Constitution editorial filing. It is not an official classification.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 领域

```json
[
 "语言"
]
```

> Editorial tag

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 许可与适用范围

MIT (the official HF README YAML explicitly states license: mit).

[来源1](https://huggingface.co/datasets/google/simpleqa-verified/raw/main/README.md)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2509.07968

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Code

https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified

> The official source provides a Kaggle starter notebook and evaluation prompts; another project's GitHub is not presented as this benchmark's code.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 数据

https://huggingface.co/datasets/google/simpleqa-verified

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Official entry

https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）

### Paper title

SimpleQA Verified: A Reliable Factuality Benchmark to Measure Parametric Knowledge

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Google DeepMind and Google Research.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 合作/参与机构

Kaggle hosts the data and the official leaderboard; the paper thanks the Gemini Factuality team for feedback.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### Authors

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

### Maintainer

Google DeepMind / Google Research

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Funders

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## Design goals

### Abilities measured

Short-form factual question answering that uses no search tools and relies only on the model parameters.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Design background

Corrects label noise, question redundancy, and topic and answer-type bias in the original SimpleQA.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## Construction

### Question sources

Screened and revised from OpenAI SimpleQA.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 出题者背景

Paper authors from Google DeepMind and Google Research are responsible for multistage filtering and manual review.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-07）

### Review process

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Quality control

Each question provides at least 2 URLs supporting the gold answer, and the acceptable numeric range is revised.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 污染控制

Cleaning is not a complete proof of decontamination; public data should not be used for training and then reported as an uncontaminated score.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## Data format

### 题量

1,000 questions

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 任务形式

Questions, gold short answers, the original index, topic, answer_type, multi_step, requires_reasoning, and source URLs.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Modalities

```json
[
 "文本"
]
```

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Languages

English

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### Difficulty

Long-tail factual knowledge. During construction, questions that GPT-4o, Gemini 2.0 Flash, and Claude 3.7 Sonnet all answer incorrectly are kept first, and the final 1,000 harder questions are then selected. In the metadata, 3.7% require reasoning and 7.3% are multi-step.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### Public and hidden splits

1,000 questions are public; no independent hidden-test split was verified in this check.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## Evaluation

### Metrics

The original paper reports Accuracy, Accuracy given attempted, F1, Attempted, and Hedged together.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 评分

gpt-4.1-2025-04-14 classifies automatically into CORRECT, INCORRECT, and NOT_ATTEMPTED; F1 is the harmonic mean of Accuracy and of Accuracy given attempted, not a token-level F1; numeric answers are scored against the interval the question explicitly allows.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 运行设置

Search and retrieval tools are forbidden; turning tools on would make the benchmark too easy.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

### 评测工具

The official Kaggle starter notebook; Appendix A of the paper publishes the autorater prompt in full.

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### Comparability

The mean_score of the Epoch anti-abstention setting must not be presented directly as the paper's F1; different task versions are tracked separately.

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
 "version": "待核实"
 "heat_confidence": "A"
 "why_trending": "Candidate heat tier A; the evidence reopened below is labeled, item by item, with the evaluating party and the nature of the evidence, and the number of web pages is not treated as the number of independently adopting organizations."
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "The current ECI composition explicitly lists this benchmark; inclusion does not equal running it."
 }
 {
 "url": "https://epoch.ai/data/benchmarks.csv"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "The CSV was read and successful run records were extracted, including 2026H2 runs."
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

On 2026-10-20 Kaggle shows a highest Score of 77.5%; the historical F1 in paper v2 peaks at 55.6. Retrieval with tools makes the tasks nearly solvable in full, so a score obtained with tools cannot be interpreted as saturation of parametric knowledge.

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

### 风险与争议

The question set is public and depends on parametric knowledge; retrieval-augmented results are not comparable with the no-tool protocol.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-07）

### 系列与衍生关系

Selected and revised from the 4,326 questions of OpenAI SimpleQA; Verified is an independently cleaned set of 1,000 questions, and scores on the original SimpleQA cannot be substituted directly.

[来源1](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2509.07968) (accessed 2026-11-08); [Source 2](https://huggingface.co/datasets/google/simpleqa-verified) (accessed 2026-11-08); [Source 3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified) (accessed 2026-11-08)

### Official entry

https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）

### 独立来源

https://epoch.ai/data/benchmarks.csv

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 分来源与协议结果

#### official Kaggle current

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Gemini 3.1 Pro Preview | 77.5 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.6,"source_date":"2026-10-20"} |
| 2 | GPT-6 Astra | 75.8 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.6,"source_date":"2026-10-20"} |
| 3 | Gemini 4 Argon | 75.6 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.6,"source_date":"2026-10-20"} |
| 4 | Gemini 3.8 Flash | 74.6 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.7,"source_date":"2026-10-20"} |
| 5 | GPT-6.1 Sol | 73.8 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.8,"source_date":"2026-10-20"} |
| 6 | Gemini 3 Pro Preview | 72.1 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.9,"source_date":"2026-10-20"} |
| 7 | GPT-5.6 Sol | 69.2 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":2.9,"source_date":"2026-10-20"} |
| 8 | GPT-6 Sol | 64.4 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.0,"source_date":"2026-10-20"} |
| 9 | Claude Opus 5 | 63.3 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 10 | Grok 4.7 | 59.4 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 11 | Grok 4.5 | 53.8 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 12 | Qwen 3 235B A22B Thinking | 53.7 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.4,"source_date":"2026-10-20"} |
| 13 | Grok 4.6 | 52.9 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.1,"source_date":"2026-10-20"} |
| 14 | Claude Opus 4.6 | 45.2 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.1,"source_date":"2026-10-20"} |
| 15 | Claude Sonnet 5.5 | 44.7 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |
| 16 | Claude Opus 4.8 | 44.5 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.1,"source_date":"2026-10-20"} |
| 17 | Deepseek V4.1 Flash | 42.3 | Score (%) on the Kaggle page; it is not unilaterally renamed F1 | {"uncertainty_plus_minus":3.2,"source_date":"2026-10-20"} |

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

The official Kaggle page has 17 readable rows (the page says it displays 48/58, and this entry does not claim to have collected all 58 models). The full 13 rows of historical F1 in paper Table 7 form an independent track. Epoch takes the latest successful run for each exact model + task_version, with 1.0.0/1.2.0 on separate tracks. The name of the Kaggle Score column, the paper's F1, and anti-abstention mean_score must not be conflated.

[来源1](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2509.07968)（访问 2026-11-08）；[来源3](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

## Contact

### 公开工作邮箱

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 官方反馈

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 公开社区

https://huggingface.co/datasets/google/simpleqa-verified/discussions

[来源1](https://huggingface.co/datasets/google/simpleqa-verified)（访问 2026-11-08）

### 隐私边界

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2509.07968v2

[来源1](https://arxiv.org/pdf/2509.07968v2)（访问 2026-11-08）

### PDF SHA-256

df3bf66ebdba21e01dec4fc760d53ca8944ed2010bf1a15e9e57b5a404ed8686

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2509.07968v2)（访问 2026-11-08）

### PDF bytes

```json
815212
```

[来源1](https://arxiv.org/pdf/2509.07968v2)（访问 2026-11-08）

### Folder

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "Opened primary material"
 "url": "https://arxiv.org/abs/2509.07968"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://huggingface.co/datasets/google/simpleqa-verified"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified"
 "accessed": "2026-11-08"
 }
]
```

[Source 1](https://arxiv.org/abs/2509.07968) (accessed 2026-11-08); [Source 2](https://huggingface.co/datasets/google/simpleqa-verified) (accessed 2026-11-08); [Source 3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

## Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

[Source 1](https://arxiv.org/abs/2509.07968) (accessed 2026-11-08); [Source 2](https://huggingface.co/datasets/google/simpleqa-verified) (accessed 2026-11-08); [Source 3](https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified) (accessed 2026-11-08)
