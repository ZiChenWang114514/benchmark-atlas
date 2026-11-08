# HLE-Diamond

> Benchmark Constitution, source-by-source in-depth check: 2026-11-08. The collection date does not represent the experiment date; Unverified is not the same as Not disclosed.

HLE-Diamond is a cleaned subset of 1000 questions released on 2026-09-22, with 500 questions for knowledge and 500 for reasoning, and it is not another name for the original HLE. The official high closed-book setting, web+code, and the independent AA evaluation are three different protocols; this page does not mix high scores that come from tools into the closed-book ranking.

Basis of the reading guide: [1](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08); [2](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [3](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-08).

## Basic information

### Short name

HLE-Diamond

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Full name

Humanity’s Last Exam: Diamond

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Benchmark version

HLE-Diamond (named version)

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Paper version

Linked to the original HLE paper, arXiv v12

Sources: [1](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08).

### Release date

2026-09-22 (date of the official release article)

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Section

Reasoning

> Benchmark Constitution editorial classification.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 领域

```json
[
 "多模态"
 "Cross-disciplinary science"
]
```

> Editorial tags; an empty list means finer-grained tags have not yet been added.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 许可与使用范围

```json
{
 "code": "Associated HLE repository MIT"
 "dataset_metadata": "HF labeled MIT"
 "additional_notice": "The HF dataset card requires that the dataset not be shared in public, re-uploaded, or distributed; entry into a training corpus is prohibited. Access to the data files is subject to a separate HF condition of consent."
}
```

Sources: [1](https://github.com/centerforaisafety/hle/blob/main/LICENSE) (accessed 2026-11-08); [2](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-08).

### 论文入口

https://arxiv.org/abs/2501.14249

> The official site cites the original HLE paper and the Nature published version; these are related papers, not an independent Diamond paper.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08).

### Code

https://github.com/centerforaisafety/hle

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Dataset

https://huggingface.co/datasets/cais/hle-diamond

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Official homepage

https://lastexam.ai/blog/hle-diamond

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Paper title

```json
{
 "related_arxiv": "Humanity’s Last Exam"
 "related_journal": "A benchmark of expert-level academic questions to assess AI capabilities"
 "relationship": "The Diamond release article cites the original HLE paper and is not treated as an independent Diamond paper."
}
```

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08).

## Origin and maintenance

### Initiators

```json
[
 "Center for AI Safety"
 "Scale AI"
]
```

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 合作与作者单位

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Authors

The Center for AI Safety, Scale AI, and the HLE Contributors Consortium; the work of cleaning Diamond thanks the research community and the contributors of the questions.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Maintainer

Center for AI Safety / Scale AI

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 资助与资源支持

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

## Design goals

### 测量能力

Closed-book expert knowledge and cross-disciplinary reasoning; image questions are included, and the knowledge and reasoning partitions are reported separately.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 与既有基准的差异

Directed at the quality of the original HLE questions, cleaned and refined from research-community feedback, to establish a new subset that can be compared on a continuing basis.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

## Construction

### Question sources

Cleaned and refined from the original HLE question set.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 出题者背景

It carries forward questions written by HLE’s domain experts worldwide, after a year of cleaning; the release article thanks the people who contributed questions and the HLE-Rolling research community, and it does not automatically count every author of the original HLE as an independent author of Diamond.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-08).

### Review process

A year of cleaning and refinement, drawing on feedback from the research community and from HLE-Rolling.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### Quality control

500 questions each for knowledge and reasoning; the original HLE total score is not taken directly as the Diamond score.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 去污染与泄漏控制

The data card adds a canary string for training-data filtering and explicitly requires that benchmark data not enter the training corpus.

Sources: [1](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-07).

## Data format

### 规模与统计口径

1,000 questions: 500 on reasoning and 500 on knowledge.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07); [2](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### Question types

Follows the HLE field format; AA scores with open answers and an equivalence-check judge.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07); [2](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### Modalities

```json
[
 "文本"
 "Image (272 questions)"
]
```

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### Languages

The public dataset card states that every column follows the HLE format; AA uses the official English HLE system prompt. A complete per-question language count is Unverified, and this is not a basis for claiming that all items are monolingual.

Sources: [1](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08).

### Difficulty

Expert-level knowledge and expert-level reasoning have 500 questions each; on the official high setting, tool-free Astra scores 74.2% on reasoning and 45.6% on knowledge, and the two partitions cannot simply be read as one and the same level of difficulty.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08).

### Public and hidden splits

The test split is public; the partition column distinguishes reasoning from knowledge.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07); [2](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

## Evaluation

### Metrics

pass@1 / accuracy; reasoning and knowledge are also reported.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 评分规则

AA follows the official HLE judge prompt and format, and GPT-5.6 Luna (medium) judges whether the answer is correct.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 提示、采样与工具设置

```json
{
 "AA": "1000 questions, 1 time each, with no tools; the official HLE system prompt; judged by GPT-5.6 Luna (medium); vision models receive the images, and non-vision models receive text only but are still scored on every question."
 "official_tools": "The web+code tool track uses Python 3.11.16 and pinned dependencies; the code sandbox does not connect to the network directly and obtains external information only through web_search and web_fetch; the official blocklist filters leakage of questions and answers; runs follow the provider's agent harness."
}
```

Sources: [1](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08); [2](https://github.com/centerforaisafety/hle/blob/main/docs/evaluation-with-tools.md) (accessed 2026-11-08).

### 官方脚本

https://github.com/centerforaisafety/hle

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 可比性警告

The official article’s high-reasoning, max-reasoning, and tool tracks differ; AA uses its own judge implementation. Results on the original HLE’s 2,158 plain-text questions cannot be compared directly with Diamond’s 1,000 questions.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

## Current status

### 核查时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08); [2](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08).

### 最新数据状态

```json
{
 "version": "HLE-Diamond (named version)"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
 "date": "2026-10-27"
 "date_type": "source_calendar_date"
 "note": "AA v5 replaces the original HLE with HLE-Diamond, at an index weight of 10%."
 }
 ]
}
```

> Heat A follows the candidate grading; the nature of the evidence is labeled item by item. Multiple URLs do not automatically equal multiple independent adopters, and what is currently visible is not treated as a recent first release.

Sources: [1](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) (accessed 2026-11-07).

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2025-01-24"
 }
 {
 "version": "v2"
 "submitted_at": "2025-02-06"
 }
 {
 "version": "v3"
 "submitted_at": "2025-02-12"
 }
 {
 "version": "v4"
 "submitted_at": "2025-02-19"
 }
 {
 "version": "v5"
 "submitted_at": "2025-02-21"
 }
 {
 "version": "v6"
 "submitted_at": "2025-04-11"
 }
 {
 "version": "v7"
 "submitted_at": "2025-04-20"
 }
 {
 "version": "v8"
 "submitted_at": "2025-09-12"
 }
 {
 "version": "v9"
 "submitted_at": "2025-09-26"
 }
 {
 "version": "v10"
 "submitted_at": "2026-02-20"
 }
 {
 "version": "v11"
 "submitted_at": "2026-07-29"
 }
 {
 "version": "v12"
 "submitted_at": "2026-10-19"
 }
]
```

> This is history associated with the original HLE paper, not a record of revisions to the Diamond data.

Sources: [1](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08).

### 饱和度与证据边界

On the current official site, the high with no tools is 59.9% and the high with web+code is 82.9%; the current AA high with no tools is 69.1%. These are snapshots of three different implementations, and they are not a single claim that the benchmark is saturated.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08).

### 污染与已知问题

The question set is cleaned from HLE that has already been published, so it cannot be claimed never to have been public; the canary only assists filtering. The tool track must restrict accessible sources so that the question bank or the answers are not hit directly; HF explicitly requires that questions not be shared.

Sources: [1](https://huggingface.co/datasets/cais/hle-diamond) (accessed 2026-11-08); [2](https://github.com/centerforaisafety/hle/blob/main/docs/evaluation-with-tools.md) (accessed 2026-11-08).

### 相关与衍生基准

A newer subset in the same family as the hle already included; the relation between the two is kept, and the knowledge/reasoning/tool tracks are not counted again.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not a run date or a leaderboard-update date)

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08); [3](https://github.com/centerforaisafety/hle/blob/main/docs/evaluation-with-tools.md) (accessed 2026-11-08).

### 官方结果入口

https://lastexam.ai/blog/hle-diamond

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 独立评测入口

https://artificialanalysis.ai/evaluations/hle-diamond

Sources: [1](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08).

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "GPT-6 Astra"
 "score": "59.9"
 "metric": "Accuracy (%)"
 "track": "Official high, no tools"
 "source_url": "https://lastexam.ai/blog/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "Gemini 4 Argon"
 "score": "56.9"
 "metric": "Accuracy (%)"
 "track": "Official high, no tools"
 "source_url": "https://lastexam.ai/blog/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "Claude Opus 5.5"
 "score": "54.6"
 "metric": "Accuracy (%)"
 "track": "Official high, no tools"
 "source_url": "https://lastexam.ai/blog/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-6 Astra"
 "score": "82.9"
 "metric": "Accuracy (%)"
 "track": "Official high, web+code"
 "source_url": "https://lastexam.ai/blog/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "Claude Opus 5.5"
 "score": "73.9"
 "metric": "Accuracy (%)"
 "track": "Official high, web+code"
 "source_url": "https://lastexam.ai/blog/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "Claude Fable 5.1"
 "score": "72.3"
 "metric": "Accuracy (%)"
 "track": "Official high, web+code"
 "source_url": "https://lastexam.ai/blog/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "Gemini 4 Carbon (High)"
 "score": "69.1"
 "metric": "pass@1 (%)"
 "track": "AA independent, no tools, 1000 questions, GPT-5.6 Luna medium judge"
 "source_url": "https://artificialanalysis.ai/evaluations/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "Claude Opus 5.5 (Max, Default Fallback)"
 "score": "67.9"
 "metric": "pass@1 (%)"
 "track": "AA independent, no tools, 1000 questions, GPT-5.6 Luna medium judge"
 "source_url": "https://artificialanalysis.ai/evaluations/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "Gemini 4 Carbon (Medium)"
 "score": "67.4"
 "metric": "pass@1 (%)"
 "track": "AA independent, no tools, 1000 questions, GPT-5.6 Luna medium judge"
 "source_url": "https://artificialanalysis.ai/evaluations/hle-diamond"
 "source_date": "Unverified (the run date of each model is not listed; the date of the official release article is 2026-09-22)."
 "snapshot_date": "2026-11-08 "
 }
]
```

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08); [3](https://github.com/centerforaisafety/hle/blob/main/docs/evaluation-with-tools.md) (accessed 2026-11-08).

### 覆盖与局限

Read from AA’s direct evaluation page, and do not present rounded figures such as 68% from the index article as exact leaderboard scores; three tracks are kept: official high with no tools, official high with web+code, and AA independent with no tools.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/hle-diamond) (accessed 2026-11-08).

## Contact

### 官方公开邮箱

```json
[
 "agibenchmark@safe.ai"
]
```

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 仓库反馈

https://github.com/centerforaisafety/hle/issues

> Linked to the feedback entry of the HLE repository; it is not an independent Diamond repository.

Sources: [1](https://github.com/centerforaisafety/hle/blob/main/README.md) (accessed 2026-11-08).

### 官方社区

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 隐私与联系边界

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

## Original files

### Paper PDF

https://arxiv.org/pdf/2501.14249

> Linked to the PDF of the original HLE paper, not an independent Diamond paper.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08); [2](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08).

### PDF SHA-256

e1f7a776446cc02b80d8a50a296cb055a8abddc3cffdfd606ee694f5fd47c937

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2501.14249) (accessed 2026-11-08).

### PDF bytes

```json
2021060
```

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2501.14249) (accessed 2026-11-08).

### 已有文件夹

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 其他官方文档

```json
[
 {
 "type": "Official methods and introduction page (not the paper PDF)"
 "url": "https://lastexam.ai/blog/hle-diamond"
 }
]
```

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

### 已有 PDF归档

Unverified

> This group only creates local research files and does not upload a PDF or claim that one already exists.

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07).

## Changelog

### 历次核查

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

Sources: [1](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-07); [2](https://arxiv.org/abs/2501.14249) (accessed 2026-11-08); [3](https://lastexam.ai/blog/hle-diamond) (accessed 2026-11-08).
