# MMLU-Redux

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MMLU-Redux首先是一项对MMLU题目错误的人工审计，而不是把原题全部重写的全量替代题库。当前2.0覆盖57学科各100题；旧README的30科3,000题属于早期范围。评测需要区分原标签、无错子集和修正答案，也要把模型答题准确率与错误检测F1等指标分开。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### Short name

MMLU-Redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Full name

MMLU-Redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Benchmark version

MMLU-Redux 2.0 (the data entry point for this item; the original paper and the description of the old repository are not the full statistics for 2.0)

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### Paper version

arXiv v3

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Release date

2024-06-06 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Section

Language

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Field tags

- Multidisciplinary knowledge after error correction

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 许可证与权利边界

CC-BY-4.0 (official repository LICENSE and the 2.0 HF card); the source of its original MMLU question bank has a separate MIT license statement.

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/LICENSE)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0/raw/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2406.04127

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Code repository

https://github.com/aryopg/mmlu-redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Official homepage

https://github.com/aryopg/mmlu-redux

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Paper title

Are We Done with MMLU?

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

The authors of the paper are from the University of Edinburgh, Sapienza University of Rome, University of Bari, UCL, the University of Trento, and others; this is a record of author affiliations.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 合作方

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Authors

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

### Maintainer

The official public code is hosted under aryopg; this records the maintenance entry point of the repository and is not a basis for inferring institutional legal liability or a commitment of continued maintenance.

[来源](https://github.com/aryopg/mmlu-redux)（访问 2026-11-08）

### Funders

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## Design goals

### Abilities measured

Re-examines the quality of the MMLU questions and answers, distinguishing errors of the model from errors of the benchmark itself.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Design background

An existing high score does not mean the question bank is reliable; ambiguous stems, incorrect labels, and missing correct options distort model rankings and capability judgments.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## Construction

### Question sources

100 questions are drawn from each MMLU subject, and errors in the questions and answers are annotated manually.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 出题与审阅者背景

Paper v3 states that 14 human experts re-annotated 5,700 questions; the original items are carried over from MMLU and are not 5,700 questions newly written by experts.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### Review process

Annotators first assess the wording of the question, then check the original label. They are encouraged to search precisely for the original question and to consult credible sources such as government materials and textbooks; when an item is beyond professional judgment, it is marked expert.

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### Quality control

Layered error annotation covers stem and option clarity, no correct answer, multiple correct answers, and incorrect ground truth; items that are correct are marked ok, and items that cannot be judged are marked expert. Table 5 of the paper reports 93.51% OK among 5,700 items. Error rates by subject should not be extrapolated to the proportion for all of MMLU.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0/raw/main/README.md)（访问 2026-11-08）

### 去污染及其证据边界

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## Data format

### 题量与版本口径

The current 2.0 data card and the formal paper cover 57 subjects and 5,700 questions annotated by people; early descriptions of the repository and of the version give 30 subjects and 3,000 questions, and the two cannot be mixed.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### Question types

Four-choice MMLU questions, plus error labels, corrected answers, and the grounds for the corrections

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Modalities

Text

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Languages

English

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Difficulty

It follows MMLU difficulty across educational stages and disciplines; the main change is quality verification, not a uniform increase in difficulty.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Public and hidden splits

The 2.0 dataset card provides a test set by subject, 100 items per subject; it is a sampled error-correction set for MMLU, not a full replacement for MMLU.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

## Evaluation

### Metrics

Accuracy before and after error correction, and statistics on question error types.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 评分方法

Changes in model evaluation are analyzed from the results of manual error correction; it must be stated whether the score uses the original labels, the error-free subset, or the corrected labels.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 运行与提示设置

The paper's analysis includes HELM v1.3.0 (2024-05-15) predictions; prompt settings for different models and experiments need to be recorded separately.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 官方脚本

https://github.com/aryopg/mmlu-redux

[来源](https://github.com/aryopg/mmlu-redux)（访问 2026-11-08）

### 可比性警示

An original question and its options are not rewritten directly even when they are ambiguous; filtering should follow error_type and should refer to correct_answer. The 2.0 data card and the older description of 30 subjects both stand, and the actual configuration and the basis of filtering must be recorded.

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

The official release entry is mmlu-redux-2.0; the description on the dataset card still keeps the older description of 30 subjects, and statistics must be distinguished by version.

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 论文修订及历史证据

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### Saturation

This work mainly diagnoses errors in the question bank; scores on the error-corrected set cannot be used to infer that MMLU is saturated or not yet saturated.

[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 污染、争议与限制

A conflict of versions: the early materials have 3,000 questions and 30 subjects, while 2.0 and the official NAACL paper have 5,700 questions and 57 subjects. This entry takes the current 2.0 as the baseline for scale and retains the early record rather than overwriting it in silence.

[来源](https://aclanthology.org/2025.naacl-long.262/)（访问 2026-11-07）

### 衍生与版本关系

LabelChaos is synthetic perturbation data used in this study to train an error detector; it is generated by merging six human-annotated datasets and is not a new evaluation split of MMLU-Redux 2.0.

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### Official entry

https://arxiv.org/abs/2406.04127

> When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 第三方覆盖入口

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Original paper v3 Table 2 / Virology / overall instances (HELM)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Virology / correct instances (Redux error-free subset)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Logical Fallacies / overall instances (HELM)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Logical Fallacies / correct instances (Redux error-free subset)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / College Chemistry / overall instances (HELM)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / College Chemistry / correct instances (Redux error-free subset)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Professional Law / overall instances (HELM)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Professional Law / correct instances (Redux error-free subset)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Human Sexuality / overall instances (HELM)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Original paper v3 Table 2 / Human Sexuality / correct instances (Redux error-free subset)

| Model / configuration | Raw score | Metric and unit |
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

- **Claude 3.5 Sonnet (20240620)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Claude 3 Opus (20240229)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (405B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4o (2024-05-13)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (001)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 (0613)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Qwen2 Instruct (72B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **GPT-4 Turbo (2024-04-09)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Gemini 1.5 Pro (0409 preview)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.
- **Llama 3.1 Instruct Turbo (70B)**：- **scope**：A comparison of five subjects with high error rates, not the full-bank total across 57 subjects; filtering the error-free subset ≠ rewriting all answers.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

#### Jev research Table 2 / mixed-source comparison

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Jev (original label in research Table 2) | 95.0 | accuracy (research Table 2 definition) / % |
| Qwen3.8-Max (the original label in research Table 2) | 94.3 | accuracy (research Table 2 definition) / % |
| Claude Opus 5.5 (original label in research Table 2) | 94.2 | accuracy (research Table 2 definition) / % |

- **Jev (original label in research Table 2)**：- **scope**：2026-H2 Jev comparison study, Table 2; this is not the official live leaderboard of the benchmark or an independent AA leaderboard.；- **evaluation_date**：Paper dated 2026-10-08; exact run date and API version Unverified；- **snapshot_date**：2026-11-08
- **Qwen3.8-Max (the original label in research Table 2)**：- **scope**：2026-H2 Jev comparison study, Table 2; this is not the official live leaderboard of the benchmark or an independent AA leaderboard.；- **evaluation_date**：Paper dated 2026-10-08; exact run date and API version Unverified；- **snapshot_date**：2026-11-08
- **Claude Opus 5.5 (original label in research Table 2)**：- **scope**：2026-H2 Jev comparison study, Table 2; this is not the official live leaderboard of the benchmark or an independent AA leaderboard.；- **evaluation_date**：Paper dated 2026-10-08; exact run date and API version Unverified；- **snapshot_date**：2026-11-08

[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 覆盖范围与时效

Comparisons of overall and correct instances for the five subjects in Table 2 of the original paper are newly added, all at the original decimal precision. Results such as 95.0 from the Jev study are kept on a separate track. That latter table contains measurements made in that paper and scores that are cited. It is not a unified official Redux leaderboard of retests, and it is not a live ranking under one protocol.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

## Contact

### 公开工作邮箱

- aryo.gema@ed.ac.uk
- p.minervini@ed.ac.uk

[来源](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（访问 2026-11-07）

### 公开反馈

https://github.com/aryopg/mmlu-redux/issues

[来源](https://github.com/aryopg/mmlu-redux)（访问 2026-11-08）

### 官方社交

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 隐私边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2406.04127

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### PDF SHA-256

a45720c5df8c7e7fe243846a849e4799a07fa453d77b4cd55094c6e058b8b8ab

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

### PDF bytes

747909

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2406.04127)（访问 2026-11-08）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/aryopg/mmlu-redux/main/README.md)（访问 2026-11-08）
