# Chartography

> Benchmark Constitution, in-depth review: 2026-11-08. Verified to exist; a Chinese-language research snapshot; note: trending: A; the mark for what has not been verified is retained

Chartography focuses on graphics that professionals actually use for judgment, including survival curves, contour plots, Sankey diagrams, Bode plots, and financial charts, and it is not limited to ordinary bar, line, and pie charts. The 100 questions were written by practitioners and verified by three further experts. The fixed July 2026 snapshot in the original paper already differs clearly from the current official site. The difference between 20 runs per question in the paper and 10 runs in the README leaderboard example must also be retained. The historical ceiling of 45% cannot be taken as the current capability boundary.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

## Basic information

### Short name

Chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

### Full name

Chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The official name is kept; the paper title is not fabricated as a full name.

### 版本边界

Independent benchmark; semantic version Unverified

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Paper version

arXiv v1（2026-08-11）

[来源1](https://arxiv.org/abs/2608.10677)（访问2026-11-08）

### Release date

2026-08-11 17:57:25 (first arXiv submission; not an inferred first launch date of the project)

[来源1](https://arxiv.org/abs/2608.10677)（访问2026-11-08）

### 板块

Multimodal

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> Benchmark Constitution editorial classification.

### 领域

```json
[
  "Professional chart"
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

### 许可与限制

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

### Paper

https://arxiv.org/abs/2608.10677

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Code

https://github.com/surge-ai/chartography

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Dataset

https://huggingface.co/datasets/surgeai/chartography

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Official homepage

https://surgehq.ai/benchmarks/chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

### 论文题名

Chartography: A Benchmark for Professional Chart Understanding

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

## Origin and maintenance

### Initiators

Surge AI

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Partner organizations

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

### Authors

```json
[
  "Suhaas Garre"
  "Chris Mutty"
  "Sushant Mehta"
  "Edwin Chen"
]
```

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 维护入口

Surge AI

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 资助披露

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

## Design goals

### 测量对象

Visual perception of professional charts, domain interpretation, and multi-step graphical reasoning, covering survival curves, contours, Sankey, Bode, and financial graphics.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 既有评测的缺口

Earlier chart collections leaned mostly toward bar, line, and pie charts and toward short-chain reasoning, and can hardly measure chart reading in real professional decisions.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

## Construction

### 题源

81 figures from online sources and 19 figures created by experts; the questions are written by practitioners in the corresponding fields.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 构建人员

Professionals in clinical work, engineering, science, and finance.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 审核

Each question is independently reviewed by 3 other domain experts, who check the answer, the wording, and the acceptable range.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 质控

Two pilot rounds improved the question-writing specification; only questions that produce a meaningful failure in at least one frontier model are kept.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 去污染及边界

All tasks and images are released, with source metadata; public labels carry a long-term contamination risk, and no hidden test is claimed.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

## Data format

### 规模与计数口径

100 task–image records; 98 image files that differ in bytes; 12 professional-domain labels.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Question types

Single-image and free-response questions; numerical estimates, categories, sets, rankings, and multi-part answers.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Modalities

```json
[
  "图像"
  "文本"
]
```

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### Languages

The task prompts in the public paper and the README use English; on this access the HF card returned 401 and could not be read, and the full language metadata of the data remains Unverified.

[来源1](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）；[来源2](https://github.com/surge-ai/chartography)（访问2026-11-08）

### Difficulty

Professionally formatted and screened for difficulty; 51 questions have expert ranges, 25 have exact numeric values, and 24 have categorical answers.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 划分与公开范围

A public single test split; expert derivations are used in construction review but are not in the public fields.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

## Evaluation

### Metrics

mean pass@1 (%). The snapshot fixed at July 2026 in the paper uses 20 runs of each question, so that 100 questions give 2000 runs of each configuration. The example in the current README for reproducing the leaderboard uses 10 runs of each question. The difference between those two versions must be stated. pass@K and pass^K are listed apart from each other and are not interchangeable.

[来源1](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）；[来源2](https://github.com/surge-ai/chartography/blob/main/README.md)（访问2026-11-08）

### 评分

Gemini 3.5 Flash sees only the question, the reference answer, and the response, not the image; experts set a tolerance per question, and a score is given only when every part is correct.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 提示与运行条件

A single user message gives the question and the original image, with no system message, few-shot examples, or code, crop, or zoom tools.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 官方评测入口

The Inspect AI evaluation harness is in the official code repository.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 可比性边界

The paper's release snapshot differs from the live leaderboard; scores of 80–90% on other chart benchmarks are not taken as results of this benchmark.

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

## Current status

### 复核时间

2026-11-08

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）

### 当前版本

```json
{
  "version": "Independent benchmark; semantic version Unverified"
  "heat_confidence": "A"
  "evidence_2026_h2": [
    {
      "url": "https://www.anthropic.com/claude-haiku-5-5"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Anthropic actually reports Chartography in the Haiku 5.5 release table of 2026-10-07; Epoch carried out a review on 2026-10-21, and the conclusion was that the information is insufficient."
    }
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Anthropic actually reports Chartography in the Haiku 5.5 release table of 2026-10-07; Epoch carried out a review on 2026-10-21, and the conclusion was that the information is insufficient."
    }
  ]
}
```

[来源1](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07）；[来源2](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07）

> Anthropic actually reports Chartography in the Haiku 5.5 release table of 2026-10-07; Epoch carried out a review on 2026-10-21, and the conclusion was that the information is insufficient.

### 论文修订与后续使用

```json
{
  "arxiv_revisions_kst": [
    {
      "version": "v1"
      "submitted_at_kst": "2026-08-11"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2608.10677)（访问2026-11-08）

### Saturation

The launch snapshot in the paper peaks at 45.0%, and the current official site peaks at 71.6%; this shows that the scores have improved. It is not, on its own, enough to conclude that professional chart tasks are saturated, and the number of runs and the configuration need to be aligned.

[来源1](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）；[来源2](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）

### 风险与冲突

The July 2026 launch snapshot in the paper peaks at 45.0%. The current official site's top three are 71.6/71.0/66.3, while the README still says "no model exceeds 45%," so the old assertion cannot be used for the current leaderboard. The README leaderboard configuration of 10 runs differs from the paper's 20 runs. HF returned 401, and no claim is made that its license was read. No LICENSE file was found in the repository root, and the license is Unverified.

[来源1](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）；[来源2](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）；[来源3](https://github.com/surge-ai/chartography/blob/main/README.md)（访问2026-11-08）

### 衍生与后续工作

Professional chart tasks distinct from existing ChartQA and CharXiv.

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> Editorial note on deduplication; the same benchmark subset, metric, or version is not counted more than once.

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）

### 官方榜入口

https://surgehq.ai/benchmarks/chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

### 第三方榜入口

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

### 逐轨结果

```json
[
  {
    "rank": 1
    "model": "Gemini 4 Argon (High reasoning)"
    "score": 71.6
    "metric": "Chartography pass@1 (%)"
    "source_url": "https://surgehq.ai/benchmarks/chartography"
    "source_date": "Unverified (page does not explicitly state the leaderboard update time)"
    "collected_at": "2026-11-07 "
    "track": "Current Chartography leaderboard on the official site / configuration such as the model name"
    "unit": "%"
    "accessed": "2026-11-08"
  }
  {
    "rank": 2
    "model": "GPT 6 Astra (Max reasoning)"
    "score": 71.0
    "metric": "Chartography pass@1 (%)"
    "source_url": "https://surgehq.ai/benchmarks/chartography"
    "source_date": "Unverified (page does not explicitly state the leaderboard update time)"
    "collected_at": "2026-11-07 "
    "track": "Current Chartography leaderboard on the official site / configuration such as the model name"
    "unit": "%"
    "accessed": "2026-11-08"
  }
  {
    "rank": 3
    "model": "Claude Opus 5.5 (Adaptive/Max)"
    "score": 66.3
    "metric": "Chartography pass@1 (%)"
    "source_url": "https://surgehq.ai/benchmarks/chartography"
    "source_date": "Unverified (page does not explicitly state the leaderboard update time)"
    "collected_at": "2026-11-07 "
    "track": "Current Chartography leaderboard on the official site / configuration such as the model name"
    "unit": "%"
    "accessed": "2026-11-08"
  }
  {
    "rank": 1
    "model": "GPT-5.6 Sol (Max reasoning)"
    "score": 45.0
    "metric": "mean pass@1 (%)"
    "track": "Paper Table 3/July 2026/20 trials no tools"
    "source_url": "https://arxiv.org/pdf/2608.10677"
    "accessed": "2026-11-08"
    "unit": "%"
    "source_context": "Frozen launch snapshot, not ranked together with the current web-page leaderboard"
    "ci95_half_width_pp": 1.1
  }
  {
    "rank": 2
    "model": "GPT-5.6 Sol (default)"
    "score": 39.5
    "metric": "mean pass@1 (%)"
    "track": "Paper Table 3/July 2026/20 trials no tools"
    "source_url": "https://arxiv.org/pdf/2608.10677"
    "accessed": "2026-11-08"
    "unit": "%"
    "ci95_half_width_pp": 1.2
  }
  {
    "rank": 3
    "model": "Gemini 3.5 Flash"
    "score": 35.9
    "metric": "mean pass@1 (%)"
    "track": "Paper Table 3/July 2026/20 trials no tools"
    "source_url": "https://arxiv.org/pdf/2608.10677"
    "accessed": "2026-11-08"
    "unit": "%"
    "ci95_half_width_pp": 1.3
  }
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）；[来源2](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）

### 覆盖边界

The current top three on the official website have been reread, and the historical first place from the July 2026 paper is listed separately; the table on the web page does not give a verifiable run date for each row. HF access returns 401, and the root directory has no LICENSE, so a license cannot be inferred from public visibility.

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）；[来源2](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）；[来源3](https://github.com/surge-ai/chartography)（访问2026-11-08）

## Contact

### 公开研究联系

```json
[
  "benchmarks@surgehq.ai"
]
```

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

### 项目反馈

https://github.com/surge-ai/chartography/issues

[来源1](https://github.com/surge-ai/chartography)（访问2026-11-08）

### 官方社交入口

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

### 联系信息边界

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

## Original files

### 原始PDF

https://arxiv.org/pdf/2608.10677

[Source 1](https://arxiv.org/abs/2608.10677) (accessed 2026-11-07)

> Entry point for the original paper PDF; not downloaded or uploaded; hash and byte count Unverified.

### PDF SHA-256

77ef3accf5fe10db02baaa5ae6a7e8f9783cea449a1b8c2f9b8ea3bc803990fb

[来源1](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）

> SHA-256 of the downloaded PDF bytes. It does not mean the file was uploaded.

### PDF bytes

1575099

[来源1](https://arxiv.org/pdf/2608.10677)（访问2026-11-08）

> Downloaded PDF byte count; the archive remains Unverified.

### 目录

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

### 其他官方材料

```json
[
  {
    "type": "Official web-page methods and leaderboard (not a PDF)"
    "url": "https://surgehq.ai/benchmarks/chartography"
  }
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

### 论文归档

Unverified

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

## Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问2026-11-08）
