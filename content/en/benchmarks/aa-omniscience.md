# AA-Omniscience

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

Latest review

"Knowing the answer" and "admitting that one does not know" are scored together. Current v1.1 has 3000 questions, and the abstract of the original 6000-question paper, or scores from older versions, cannot be used to interpret the current leaderboard.

## Basic information

### Short name

AA-Omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Full name

AA-Omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Benchmark version

AA-Omniscience v1.1; v1.0 is a historical version, and the scores are not directly comparable

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）

### Paper version

arXiv v1

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### Release date

v1.1: 2026-10 (the official data card confirms only the month; the exact day and time are Unverified).

> Release dates of the original paper and of older versions are kept in the historical material of the latest status; when a source gives only a date, no time zone is inferred.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）

### Section

Language

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### Field tags

- Knowledge accuracy, hallucination, and calibration

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### License

Apache-2.0 (public v1.1 subset); the redistribution license for the private 2700 questions cannot be inferred from this.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2511.13029

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### Code

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

### Official entry

https://artificialanalysis.ai/evaluations/omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Paper title

AA-Omniscience: Evaluating Cross-Domain Knowledge Reliability in Large Language Models

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Artificial Analysis。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 合作方

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Authors

- Jackson, Declan
- Keating, William
- Cameron, George
- Hill-Smith, Micah

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### Maintainer

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Funders

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

## Design goals

### Abilities measured

Measures cross-domain factual knowledge and the calibration of knowing when not to answer, and penalizes incorrect guesses.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Design background

A general capability score cannot stand for reliable factual output, and it does not show whether the model acknowledges a gap in its knowledge.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

## Construction

### Question sources

An LLM question-generation agent generates questions from authoritative academic and industry materials.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 出题者背景

The Artificial Analysis research team designed the automatic generation and evaluation process.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Review process

Original paper §2.2: question proxies are generated from authoritative materials and filtered by similarity, difficulty, and ambiguity, with human review; the v1.1 data card states that ambiguities and errors were corrected, but it does not give a per-question count of human review.

> Describes the process that has been disclosed; a human count that was not given is not encoded as 0 or as the full total.

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

### Quality control

v1.1 removes questions that are already saturated, and the official website also displays an analysis of the consistency of performance on public and private questions.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Decontamination

v1.1 removes questions from the v1.0 public set, filters out saturated questions, adds new questions, and corrects ambiguities and errors; 2700 questions are kept private in order to maintain evaluation integrity. These measures do not constitute proof that model training is free of contamination.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问 2026-11-07）

## Data format

### 题量与规模

v1.1 has 3000 questions in full, 300 public and 2700 private; v1.0 has 6000 questions, of which 600 are public.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

### Question types

Open-ended factual question answering, with abstention allowed

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Modalities

Text

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Languages

Questions in the public subset, and the answering and scoring prompts, are in English; a complete statement of languages for the private question bank is Unverified.

> 字段状态：待核实

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

### Difficulty

v1.1 removes saturated questions; a lower score can come from a change in the question bank, and it cannot be asserted directly as regression of the model.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Public and hidden splits

v1.1 has 3000 questions in full, a public test subset of 300 questions, and 2700 private questions; the public proportion in each of the six domains matches the full set: science-engineering-mathematics 60/600, software engineering 60/600, and 45/450 in each of the other four domains.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

## Evaluation

### Metrics

Net Score (-100 to 100), accuracy, and hallucination rate; the three are different.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 评分

AA-Omniscience Index = 100×(correct−incorrect)/total number of questions, ranging from −100 to 100; partially correct answers and abstentions score 0. The judge model is GPT-5.6 Luna (medium), and the four judgment classes are correct, incorrect, partially correct, and not answered.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问 2026-11-07）

### 运行设置

No context or tools are provided; the prompt asks for the answer only and explicitly encourages abstention when uncertain or when context or tools are needed.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问 2026-11-07）

### 官方脚本

https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1

> The dataset card publishes the answer prompt and the full four-class judge template directly; this is a reproducible protocol, and it does not claim an independent executable evaluation repository.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

### 可比性警示

The question banks and the scores of v1 and of v1.1 cannot be mixed in direct comparison; the current page still keeps the Claude4.1Opus score of 4.8 from the abstract of the v1 paper, and that score is not the current leader.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 最新版本与采用证据

```json
{
 "current_version": "AA-Omniscience v1.1; v1.0 is a historical version, and the scores are not directly comparable"
 "release_date": "v1.1: 2026-10 (the official data card confirms only the month; the exact day and time are Unverified)."
 "version_changes": "v1.0 has 6000 questions, of which 600 are public; v1.1 has 3000 questions, of which 300 are public and 2700 are private, and it keeps 6 major domains. Saturated questions and old public questions are removed, new questions are added, and ambiguities and errors are corrected; v1.0 scores and v1.1 scores cannot be compared directly. The public subset is licensed Apache-2.0, and that license is not extrapolated automatically to the private questions."
 "trending": "B"
 "why_trending": "The official AA dataset card states that v1.1 went online in October 2026 and compared 86 models at release; the AA article of 2026-10-28 explicitly reports v1.1, and the current official page continues to track 124 model configurations. The recent evidence comes mainly from AA, the same organization, so it is listed conservatively as B and is not written as general adoption across the field."
 "history": {
 "previous_version_field": {
 "value": "v1.1"
 "sources": [
 {
 "url": "https://artificialanalysis.ai/evaluations/omniscience"
 "accessed": "2026-11-07"
 }
 ]
 }
 "previous_release_date_field": {
 "value": "2025-11-17"
 "sources": [
 {
 "url": "https://arxiv.org/abs/2511.13029"
 "accessed": "2026-11-07"
 }
 ]
 "note": "The first-release date of the original paper; it is not guaranteed to equal the date the data files were first made public."
 }
 "previous_status_field": {
 "value": "v1.1 (the official card states that it went online in October 2026); the scores are not directly comparable with v1.0."
 "sources": [
 {
 "url": "https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md"
 "accessed": "2026-11-07"
 }
 ]
 }
 "previous_results_field": {
 "value": [
 {
 "model_version": "Gemini 4 Carbon (High)"
 "score": "54"
 "unit": "指数点"
 "scope_and_protocol": "AA-Omniscience v1.1 Net Score, on a range from −100 to 100; only the top three readable in the official page summary."
 "result_date": "待核实"
 "snapshot_date": "2026-11-07"
 "source_url": "https://artificialanalysis.ai/evaluations/omniscience"
 "source_class": "Tier 1: official leaderboard"
 "checkpoint_note": "Recorded as the source display name, without inferring an API checkpoint."
 }
 {
 "model_version": "Claude Opus 5.5 (Max, Default Fallback)"
 "score": "48"
 "unit": "指数点"
 "scope_and_protocol": "AA-Omniscience v1.1 Net Score, on a range from −100 to 100; only the top three readable in the official page summary."
 "result_date": "待核实"
 "snapshot_date": "2026-11-07"
 "source_url": "https://artificialanalysis.ai/evaluations/omniscience"
 "source_class": "Tier 1: official leaderboard"
 "checkpoint_note": "Recorded as the source display name, without inferring an API checkpoint."
 }
 {
 "model_version": "Gemini 4 Carbon (Medium)"
 "score": "47"
 "unit": "指数点"
 "scope_and_protocol": "AA-Omniscience v1.1 Net Score, on a range from −100 to 100; only the top three readable in the official page summary."
 "result_date": "待核实"
 "snapshot_date": "2026-11-07"
 "source_url": "https://artificialanalysis.ai/evaluations/omniscience"
 "source_class": "Tier 1: official leaderboard"
 "checkpoint_note": "Recorded as the source display name, without inferring an API checkpoint."
 }
 {
 "model": "Gemini 4 Carbon (High)"
 "score": 54
 "unit": "points"
 "metric": "v1.1 Net Score"
 "scope": "Readable leading rows on the AA independent-evaluation site"
 "snapshot_date": "2026-11-07"
 "model_release_date": "2026-10-28"
 }
 {
 "model": "Claude Opus 5.5 (Max, Default Fallback)"
 "score": 48
 "unit": "points"
 "metric": "v1.1 Net Score"
 "scope": "Readable leading rows on the AA independent-evaluation site"
 "snapshot_date": "2026-11-07"
 }
 {
 "model": "Gemini 4 Carbon (Medium)"
 "score": 47
 "unit": "points"
 "metric": "v1.1 Net Score"
 "scope": "Readable leading rows on the AA independent-evaluation site"
 "snapshot_date": "2026-11-07"
 }
 ]
 "sources": [
 {
 "url": "https://artificialanalysis.ai/evaluations/omniscience"
 "accessed": "2026-11-07"
 }
 {
 "url": "https://artificialanalysis.ai/evaluations/omniscience"
 "accessed": "2026-11-07"
 }
 ]
 }
 }
}
```

> Historical fields are kept as they were; an old snapshot is not a new ranking. Heat grades are a grading of editorial evidence, not an official certification.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2025-11-17"
 }
]
```

> arXiv lists only v1; the original paper has 6000 questions, not the 3000-question technical report of v1.1.

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### Saturation

The official notes state that v1.1 removed saturated questions; this shows that the question bank was filtered, and it does not mean the entire knowledge task is saturated.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Contamination and disputes

The same page contains the abstract of the v1 paper and the current method of v1.1. The question count, the highest score, and the meaning of the score must be distinguished by version; the denominator of the current hallucination rate uses the definition given on the official site, and it is not rewritten by convention.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 版本与衍生关系

AA-Omniscience-Public v1.0 and v1.1 are public subsets of the same family; results on the public 300 questions must not be treated as the official leaderboard for the private 2700 questions, and items are not split in order to make up a count.

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Official leaderboard

https://artificialanalysis.ai/evaluations/omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 第三方覆盖

Unverified

> 字段状态：待核实

> The original value is identical to the official leaderboard and has been corrected; an AA self-evaluation is not labeled as an independent re-evaluation.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 分轨结果

#### v1.1 Net Score

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (High) | 54 | 100×(correct−incorrect)/total | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |
| 2 | Claude Opus 5.5 (Max, Default Fallback) | 48 | 100×(correct−incorrect)/total | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |
| 3 | Gemini 4 Carbon (Medium) | 47 | 100×(correct−incorrect)/total | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |

#### v1.1 Accuracy

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Claude Fable 5.1 (Max, Default Fallback) | 68 | Accuracy (%) | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |
| 2 | Claude Fable 5.1 (Xhigh, Default Fallback) | 67 | Accuracy (%) | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |
| 3 | Claude Opus 5.5 (Xhigh, Default Fallback) | 66 | Accuracy (%) | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |

#### v1.1 Hallucination Rate

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (Medium) | 4 | Official-site hallucination rate (%); lower is better | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |
| 1 | Gemini 4 Argon (High) | 4 | Official-site hallucination rate (%); lower is better | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |
| 3 | Gemini 4 Carbon (High) | 11 | Official-site hallucination rate (%); lower is better | [原表](https://artificialanalysis.ai/evaluations/omniscience)，2026-11-07 |

> 字段状态：待核实

> The integer precision shown on the original web page is retained; the overall update time and each model's runtime are Unverified; the three metric tracks must not be ranked together.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### Coverage note

Source of the current snapshot: https://artificialanalysis.ai/evaluations/omniscience. Original names of model configurations are kept. The overall update time and the actual run date of each model are Unverified.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07）

## Contact

### 公开科研联系邮箱

- declan@artificialanalysis.ai
- william@artificialanalysis.ai
- george@artificialanalysis.ai
- micah@artificialanalysis.ai

> A research correspondence address is public on the paper's first page.

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### 公开反馈

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 官方社交

- https://x.com/ArtificialAnlys
- https://www.linkedin.com/company/artificial-analysis/

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 隐私说明/政策

https://artificialanalysis.ai/privacy-policy

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2511.13029

[来源1](https://arxiv.org/abs/2511.13029)（访问 2026-11-07）

### PDF SHA-256

abedc69e8235329cbfe0fe49cc33928a5b1732bc054637328c00b07f588b5dfa

> SHA-256 of the bytes actually downloaded. It does not mean an existing copy was replaced.

[来源1](https://arxiv.org/pdf/2511.13029)（访问 2026-11-07）

### PDF bytes

3786016

[来源1](https://arxiv.org/pdf/2511.13029)（访问 2026-11-07）

### 论文副本

## Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 "fields_updated": [
 "basic_info.license"
 "construction.decontamination"
 "data_format.size"
 "evaluation.scoring"
 "evaluation.prompt_settings"
 "latest_status.latest_dataset_version"
 "latest_status.paper_revision_history"
 "leaderboard.results"
 "leaderboard.coverage_note"
 ]
 }
 {
 "date": "2026-11-07"
 Latest review
 "sources": [
 {
 "url": "https://artificialanalysis.ai/evaluations/omniscience"
 "accessed": "2026-11-07"
 }
 {
 "url": "https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1"
 "accessed": "2026-11-07"
 }
 {
 "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1"
 "accessed": "2026-11-07"
 }
 ]
 }
 {
 "date": "2026-11-07"
 Latest review
 }
]
```

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）
