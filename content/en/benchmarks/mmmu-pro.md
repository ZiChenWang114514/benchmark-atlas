# MMMU-Pro

> Verification date: 2026-11-08. Unknowns are not filled in; the date on which the source was accessed is not the experiment run date.

MMMU-Pro filters out questions from the original that a text shortcut can answer, expands the candidate options, and embeds the question in an image to test the joint ability to "see and read." The underlying 1730 questions correspond to three configurations, Standard with four options, Standard with ten options, and Vision. They are not 5190 independent questions. The original paper's overall score, each column of the official JSON, the Vals four-option scores, and the AA ten-option scores are each on separate tracks. Human performance in the paper is an estimate by the authors using the original MMMU data, and it is not treated as a new measurement for Pro.
[Guide source for this page](https://arxiv.org/pdf/2409.02813) (accessed 2026-11-08)

[Supplementary reading basis](https://huggingface.co/datasets/MMMU/MMMU_Pro) (accessed 2026-11-08)

## Basic information

### Short name

MMMU-Pro

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### Full name

MMMU-Pro

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 数据/基准版本

Pro (data revised through 2026-10-04)

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Paper version

arXiv v3 (2025-05-22 17:22:02; ACL 2025 paper)

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### Release date

2024-09-05 (official announcement of the first data release; arXiv v1 is 2024-09-05 00:31:26 )

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### Section

Multimodal

> Editorial filing. It does not represent an official classification.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### Subfields

Scientific visual reasoning

> Editorial filing. It does not represent an official classification.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 许可边界

Apache-2.0 (HF dataset card); copyright in the original materials follows the source site, and items may be removed after a copyright report.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问 2026-11-07）

### 论文入口

https://arxiv.org/abs/2409.02813

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 代码入口

https://github.com/MMMU-Benchmark/MMMU

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Dataset

https://huggingface.co/datasets/MMMU/MMMU_Pro

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Official homepage

https://mmmu-benchmark.github.io/

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）；[来源2](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### Paper title

MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## Origin and maintenance

### Initiators

MMMU Team

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Partner organizations

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### Authors

Xiang Yue、Tianyu Zheng、Yuansheng Ni、Yubo Wang、Kai Zhang、Shengbang Tong、Yuxuan Sun、Botao Yu、Ge Zhang、Huan Sun、Yu Su、Wenhu Chen、Graham Neubig

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Current maintainer

MMMU Team

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Funders

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

## Design goals

### Abilities measured

Cross-disciplinary visual understanding, knowledge reasoning, and integration of images and text; the task requires actually using the image, not only options or textual shortcuts.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 设计动机

Some questions in the original MMMU can be answered correctly without looking at the image, and four choices also allow guessing. Pro tightens the evaluation by filtering, expanding the options, and requiring vision-only input.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## Construction

### Question sources

Questions that a text-only model can answer are filtered out of the original MMMU; four text models are each repeated ten times, and a question is removed if a majority of at least three of the models answer it correctly; after 1,800 questions are drawn, relevance of the options to the image is reviewed, and 1,730 questions are kept.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 出题/构建者背景

Domain experts expanded the options and reviewed the link between the original answer and the image; a model screened the items first, then there were two rounds of human review, followed by a further check by two additional human experts. This is not a new expert examination that reorganizes the whole question set.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### Review process

GPT-4o generates additional options, Claude 3.5 filters them, and two rounds of human review follow; screenshots and photographs are collected by hand under different display backgrounds, fonts, and font sizes.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Quality control

GPT-4o generates additional options, Claude 3.5 filters them, and two rounds of human review follow; screenshots and photographs are collected by hand under different display backgrounds, fonts, and font sizes.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 去污染/泄漏控制

Filtering out text-only shortcuts does not prove an absence of training contamination; the public question set still carries a risk of memorization.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## Data format

### 精确规模与统计口径

1,730 underlying questions. The three configurations standard (4 options), standard (10 options), and vision each have 1,730 rows. The combined 5,190 configuration rows are not 5,190 independent questions.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问 2026-11-07）

### Question types

Multiple choice by subject; Standard pairs text with figures, and Vision embeds the question and the options in an image.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### Modalities

文本；图像

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 语言/代码语种

English questions and options (the Standard/Vision specification and examples shown in the original paper); programming languages and text recognition in images are not counted separately as natural-language coverage.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 难度结构

Questions that text models cannot answer reliably are screened out of the original MMMU; they are not graded as a newly added bank of elementary, high-school, or university questions. HF Standard keeps the topic_difficulty field. Human performance in the paper appendix is projected from the original MMMU data rather than measured again, and it is not treated as a newly added human examination score.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### Public and hidden splits

All three HF configurations are a test split; sample ids retain the original validation/test source and do not amount to a new training split.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问 2026-11-07）

## Evaluation

### Metrics

Accuracy; the paper's overall score is the mean of Standard 10-option accuracy and Vision accuracy, and Standard 4-option is only a control.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 评分规则

The chosen answer is extracted and compared with the reference label; a four-option score cannot be treated as the Pro ten-option/Vision composite score.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 运行与提示设置

The paper compares Direct and CoT and takes the better result; the current AA methods page lists 1730 questions with ten options, 1 run, and pass@1 by regular-expression extraction, and it explicitly states that this is an independent item and is not part of Intelligence Index v5.0.1. Vals uses four options and should be kept separate from the first two.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）；[来源3](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### Official evaluation scripts

https://github.com/MMMU-Benchmark/MMMU

> The link is the one indicated by an original paper or dataset card that was opened; the code was not verified file by file.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 可比性警示

Vals uses Standard with 4 options; AA uses 10 options; the original paper's composite also includes Vision. The three definitions cannot be ranked together directly.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## Current status

### Date checked

2026-11-08

> Access date of the source site for this visit; not the leaderboard run date.

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "version": "Pro (data revised through 2026-10-04)"
  "trending": "A"
  "heat_evidence": "The current AA method page still runs 1,730 ten-option questions; on 2026-10-04 HF corrected options and missing conditions. Vals retained the leaderboard on September 1, but it has now stopped evaluating new models, and it cannot be written as still being updated continuously."
  "evidence_2026_h2": [
    {
      "url": "https://huggingface.co/datasets/MMMU/MMMU_Pro"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
    }
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
    }
    {
      "url": "https://www.vals.ai/benchmarks/mmmu"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
    }
  ]
}
```

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）；[来源3](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "arxiv_revisions": [
    {
      "version": "v1"
      "date_kst": "2024-09-05"
    }
    {
      "version": "v2"
      "date_kst": "2024-09-10"
    }
    {
      "version": "v3"
      "date_kst": "2025-05-22"
    }
  ]
  "dataset_corrections": [
    {
      "date": "2026-05-30"
      "ids": [
        "validation_Diagnostics_and_Laboratory_Medicine_17"
      ]
      Latest review
    }
    {
      "date": "2026-07-10"
      "ids": [
        "validation_Design_15"
        "validation_Art_Theory_4"
      ]
      Latest review
    }
    {
      "date": "2026-10-04"
      "ids": [
        "test_Chemistry_240"
        "validation_Finance_5"
      ]
      Latest review
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 饱和性证据

Vals states explicitly that this implementation is saturated and that it has stopped running new models; this is not extrapolated to the ten-option setting at AA or to Pro Vision.

[来源1](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### 污染与已知争议

Filtering out questions that can be answered from text alone is not decontamination of the training data; through 2026, answers, options, and missing conditions continued to be corrected, and the data revision must be pinned. The ten-option Standard setting and the Vision mean in the original paper, the overall column of the official JSON, the four-option setting on Vals, and the ten-option setting on AA are not the same accounting; the human score in the original paper is an estimate by the authors, not an independent retest of Pro.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源3](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源5](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）

### 衍生与条目关系

This page includes only MMMU-Pro; the original remains at the existing entry /benchmarks/mmmu. Pro is its enhanced derivative against shortcuts, and the original version’s count of 11.5K questions cannot be entered on this page.

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## Leaderboard snapshot

### 本次榜单采集日

2026-11-08

[来源1](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### 官方榜源

https://mmmu-benchmark.github.io/#leaderboard

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）；[来源2](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### 第三方覆盖

https://www.vals.ai/benchmarks/mmmu；https://artificialanalysis.ai/evaluations/mmmu-pro

[来源1](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Official JSON / Pro overall (column as originally listed on the official site)

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Chance Vision 1.5 | 86.9 % | accuracy | 2026-07-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 2 | GPT-5.4 Thinking w/ tools | 82.1 % | accuracy | 2026-03-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 3 | GPT-5.4 Thinking w/o tools | 81.2 % | accuracy | 2026-03-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 4 | Gemini 3.0 Pro | 81.0 % | accuracy | 2025-11-18 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 5 | Gemini 3.1 Pro Thinking (High) | 80.5 % | accuracy | 2026-02-19 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | Muse Spark Thinking | 80.4 % | accuracy | 2026-04-08 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | GPT-5.2 Thinking w/o Python | 80.4 % | accuracy | 2025-12-11 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 8 | GPT-5.2 Thinking w/o tools | 79.5 % | accuracy | 2025-12-11 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 9 | GPT-5.1 Thinking | 79.0 % | accuracy | 2025-11-13 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 10 | GPT-5 w/ thinking | 78.4 % | accuracy | 2025-08-07 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |

- That original column already shows a ranking by score; tool and no-tool labels are retained, and this does not constitute a retest under the same protocol.

- When overall does not provide both components at once, component scores are not reverse-inferred or fabricated

#### Official JSON / Pro Standard ten options (JSON original column)

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Chance Vision 1.5 | 87.6 % | accuracy | 2026-07-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 2 | Claude 3.5 Sonnet | 55.0 % | accuracy | 2024-06-20 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 3 | GPT-4o (0513) | 54.0 % | accuracy | 2024-05-13 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 4 | InternVL2.5-78B | 51.4 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 5 | Gemini 1.5 Pro (0801) | 49.4 % | accuracy | 2024-08-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | Qwen2-VL-72B | 49.2 % | accuracy | 2024-08-29 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 7 | InternVL2.5-38B | 48.0 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 8 | Gemini 1.5 Pro (0523) | 46.5 % | accuracy | 2024-05-23 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 9 | MiMo-VL 7B-RL | 46.2 % | accuracy | 2025-06-04 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 10 | Llama 3.2 90B | 45.2 % | accuracy | 2024-09-25 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |

- That original column already shows a ranking by score; tool and no-tool labels are retained, and this does not constitute a retest under the same protocol.

- When overall does not provide both components at once, component scores are not reverse-inferred or fabricated

#### Official JSON / Pro Vision

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Chance Vision 1.5 | 86.1 % | accuracy | 2026-07-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 2 | GPT-4o (0513) | 49.7 % | accuracy | 2024-05-13 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 3 | Claude 3.5 Sonnet | 48.0 % | accuracy | 2024-06-20 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 4 | InternVL2.5-78B | 45.9 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 5 | Gemini 1.5 Pro (0801) | 44.4 % | accuracy | 2024-08-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | InternVL2.5-38B | 44.0 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 7 | Qwen2-VL-72B | 43.3 % | accuracy | 2024-08-29 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 8 | Gemini 1.5 Pro (0523) | 40.5 % | accuracy | 2024-05-23 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 9 | MiMo-VL 7B-RL | 40.3 % | accuracy | 2025-06-04 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 10 | MiMo-VL 7B-SFT | 39.4 % | accuracy | 2025-06-04 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |

- That original column already shows a ranking by score; tool and no-tool labels are retained, and this does not constitute a retest under the same protocol.

- When overall does not provide both components at once, component scores are not reverse-inferred or fabricated

#### Vals / Standard 4 options / evaluation of new models has stopped.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Claude Fable 5.1 | 90.64% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 2 | Claude Opus 5 | 89.88% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 3 | Claude Fable 5 | 89.31% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 4 | Gemini 3.8 Flash | 89.08% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 5 | Gemini 3.7 Flash | 88.96% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 6 | GPT-5.6 Sol | 88.84% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 7 | Gemini 3.6 Flash | 88.38% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 8 | Gemini 3.5 Flash | 88.27% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 9 | GPT 5.5 | 88.27% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 10 | Gemini 3.1 Pro Preview (02/26) | 88.21% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 11 | Kimi K3 | 88.15% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 12 | Qwen 3.8 Max | 88.03% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 13 | Gemini 3 Flash (12/25) | 87.63% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 14 | Gemini 3 Pro (11/25) | 87.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 15 | GPT 5.4 (xhigh) | 87.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 16 | Muse Spark | 87.40% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 17 | GPT 5.2 | 86.67% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 18 | Muse Spark 1.1 | 86.59% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 19 | Claude Opus 4.8 | 86.59% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 20 | GPT-5.6 Terra | 86.47% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 21 | Kimi K2.6 | 86.30% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 22 | Muse Spark 1.2 | 86.13% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 23 | GLM 5.3 Flash | 86.01% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 24 | Claude Opus 4.7 | 85.55% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 25 | GPT-5.6 Luna | 85.03% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 26 | Kimi K2.5 | 84.33% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 27 | Qwen 3.6 Plus | 84.16% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 28 | Qwen 3.8 27B | 83.93% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 29 | Claude Opus 4.6 (Thinking) | 83.87% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 30 | Gemini 3.5 Flash Lite | 83.58% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 31 | Claude Sonnet 4.6 | 83.58% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 32 | Grok 4.20 (Reasoning) | 83.47% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 33 | GPT 5.1 | 83.18% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 34 | Grok 4.3 | 83.06% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 35 | Claude Sonnet 5 | 83.01% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 36 | Claude Opus 4.5 (Thinking) | 82.95% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 37 | Gemini 3.1 Flash Lite Preview | 82.49% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 38 | Qwen 3.5 Flash | 81.91% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 39 | GPT 5 | 81.50% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 40 | Gemini 2.5 Pro Exp | 81.34% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 41 | MiniMax-M3 | 81.16% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 42 | Claude Opus 4.5 (Nonthinking) | 81.10% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 43 | Gemini 2.5 Flash Preview (9/25) (Thinking) | 80.75% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 44 | o3 | 80.42% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 45 | MiMo V2.5 | 80.00% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 46 | o4 Mini | 79.67% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 47 | Gemini 2.5 Flash Preview (9/25) (Nonthinking) | 79.48% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 48 | Claude Sonnet 4.5 (Thinking) | 79.31% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 49 | GPT 5.4 Mini | 79.25% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 50 | GPT 5 Mini | 78.91% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 51 | Inkling | 78.50% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 52 | Claude Opus 4.1 (Thinking) | 77.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 53 | o1 | 77.41% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 54 | Grok 4 | 76.27% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 55 | Gemini 2.5 Flash Lite (9/25) (Thinking) | 75.43% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 56 | Claude 3.7 Sonnet (Thinking) | 75.10% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 57 | Claude Sonnet 4 (Thinking) | 74.93% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 58 | Claude Opus 4.1 (Nonthinking) | 73.72% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 59 | GPT 5.4 Nano | 73.58% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 60 | Claude Opus 4 (Nonthinking) | 73.31% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 61 | Grok 4 Fast (Reasoning) | 72.78% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 62 | Grok 4.1 Fast (Reasoning) | 72.66% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 63 | Gemini 2.5 Flash Lite (9/25) (Nonthinking) | 72.54% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 64 | Claude Sonnet 4 (Nonthinking) | 72.39% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 65 | GPT 4.1 | 72.39% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 66 | Gemini 2.5 Flash Preview 4/17 (Thinking) | 71.92% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 67 | Llama 4 Maverick | 71.69% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 68 | Claude 3.7 Sonnet (Nonthinking) | 71.52% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 69 | GPT 5 Nano | 70.94% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 70 | GPT 4.1 Mini | 70.54% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 71 | Gemini 2.0 Flash (001) | 69.79% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 72 | Claude 3.5 Sonnet Latest | 68.80% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 73 | Gemini 2.5 Flash Preview 4/17 (Nonthinking) | 68.00% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 74 | Mistral Large 3 | 66.19% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 75 | Gemini 1.5 Pro (002) | 65.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 76 | Magistral Small 1.2 (09/2025) | 65.20% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 77 | Magistral Medium 1.2 (09/2025) | 64.57% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 78 | GPT 4o (2024-08-06) | 64.01% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 79 | Grok 4.1 Fast Non-Reasoning | 63.70% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 80 | Grok 4 Fast (Non-Reasoning) | 63.41% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 81 | Mistral Medium 3.1 (05/2025) | 62.97% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 82 | GPT 4o (2024-11-20) | 62.16% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 83 | Grok 4.5 | 61.79% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 84 | Mistral Small 3.1 (03/2025) | 60.08% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 85 | Llama 4 Scout | 58.75% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 86 | Grok 2 Vision | 57.25% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 87 | Gemini 1.5 Flash (002) | 57.19% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 88 | GPT 4o Mini | 56.56% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 89 | GPT 4.1 Nano | 55.05% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 90 | Llama 3.2 Vision (90B) | 48.06% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 91 | Claude Haiku 4.5 (Thinking) | 46.07% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 92 | Llama 3.2 Vision (11B) | 38.82% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 93 | Qwen 3.5 Plus | 22.77% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |

- Historically retained leaderboard of the Vals independent implementation

#### AA / Standard, ten options / 1730 questions / a single pass@1.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Gemini 4 Carbon (Medium) | 89 % | accuracy | 未逐项给出 | [原始来源](https://artificialanalysis.ai/evaluations/mmmu-pro)（2026-11-08） |
| 2 | Claude Opus 5.5 (Max, Default Fallback) | 88 % | accuracy | 未逐项给出 | [原始来源](https://artificialanalysis.ai/evaluations/mmmu-pro)（2026-11-08） |
| 3 | GPT-6 Astra (Max) | 87 % | accuracy | 未逐项给出 | [原始来源](https://artificialanalysis.ai/evaluations/mmmu-pro)（2026-11-08） |

- AA independent evaluation; not the Vision mean

- The page summary shows integer percentages; decimals were not back-calculated

#### Paper v3 Table 1 / Standard, ten options

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| — | GPT-4o (0513) | 54.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Claude 3.5 Sonnet | 55.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Gemini 1.5 Pro (0801) | 49.4 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |

- Historical baseline from the paper; the better of Direct and CoT is taken; not the current leaderboard

#### Paper v3 Table 1 / Vision

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| — | GPT-4o (0513) | 49.7 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Claude 3.5 Sonnet | 48.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Gemini 1.5 Pro (0801) | 44.4 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |

- Historical baseline from the paper; the better of Direct and CoT is taken; not the current leaderboard

[来源1](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### 覆盖范围与限制

The top 10 for Pro overall, for Standard, and for Vision in the official JSON are filled in here and listed in separate columns; tool permissions inside the model labels are kept, and a missing component is not inferred backward. The full readable historical leaderboard on Vals is listed on its own. From AA, only the three integer percentages that its summary can verify are copied, and no further precision is fabricated. The historical components in Table 1 of paper v3 are on another track. No track may be ranked across columns.

[来源1](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

## Contact

### 公开研究邮箱

xiangyue.work@gmail.com

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 项目反馈入口

https://github.com/MMMU-Benchmark/MMMU/issues

[来源1](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### 官方公开社交入口

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 公开渠道/隐私边界

This dossier includes only project channels that the official source has made public. Copyright in the original questions follows the source, and the team commits to removing a sample after an infringement report has been verified. An open-source license is not read as a waiver of rights in the original materials.

[来源1](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

## Original files

### 源站PDF

https://arxiv.org/pdf/2409.02813

> Verified by reading the raw PDF bytes directly; not uploaded.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### PDF SHA-256

f833d6273318d53487ace892ed54289216f5d6034fcf37af2499146d12860f5b

> Verified by reading the raw PDF bytes directly; not uploaded.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### PDF bytes

17320142

> Verified by reading the raw PDF bytes directly; not uploaded.

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### Folder

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-07）

### 其他官方文档

```json
[
  {
    "type": "Official web page/paper opened"
    "url": "https://huggingface.co/datasets/MMMU/MMMU_Pro"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://arxiv.org/abs/2409.02813"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://www.vals.ai/benchmarks/mmmu"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://artificialanalysis.ai/evaluations/mmmu-pro"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/pdf/2409.02813"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://mmmu-benchmark.github.io/"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://mmmu-benchmark.github.io/leaderboard_data.json"
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）；[来源4](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源5](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源6](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）；[来源7](https://mmmu-benchmark.github.io/)（访问 2026-11-08）；[来源8](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源9](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### 原始PDF

Unverified

> 状态：待核实。

> The page for this group was built only locally and was not uploaded; no archive link is fabricated.

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-07）

## Changelog

### Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": " (, UTC+9)"
    Latest review
  }
]
```

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）
