# Legal Research Bench

> Benchmark Constitution, source-by-source in-depth check: 2026-11-08. The collection date does not represent the experiment date; Unverified is not the same as Not disclosed.

Legal Research Bench requires an agent to carry out open-ended retrieval in the law of the United States and, at the same time, to satisfy every required rubric item and the check of sources. The 208-question test leaderboard on the official site and the historical experiment of 413 questions in the paper are on separate tracks; MIT for the code does not mean that the full Proprietary question set is open, and it does not mean reliability sufficient for practice without supervision.

Basis of the reading guide: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08); [3](https://github.com/vals-ai/legal-research-bench) (accessed 2026-11-08).

## Basic information

### Short name

Legal Research Bench

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Full name

Legal Research Bench

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Benchmark version

LRB: a corpus of 413 questions; the current official web page evaluates only on the 208-question test. The 5 public questions, the 200 license-verifiable questions, and the 208 hidden test questions are kept separate.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08).

### Paper version

arXiv v1

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08).

### Release date

2026-10-01 (date of the first arXiv draft; not the separate release date of the dataset).

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08).

### Section

Agent

> Benchmark Constitution editorial filing. It is not an official classification.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 领域

```json
[
 "法律"
 "搜索"
]
```

> Editorial tag

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 许可与使用范围

```json
{
 "harness": "MIT，Copyright 2026 Vals AI, Inc."
 "dataset": "The official site marks it Proprietary; 5 questions are public examples, and access to the rest requires separate approval or a license. The MIT license on the code cannot be used to infer that the complete question set is open."
}
```

Sources: [1](https://github.com/vals-ai/legal-research-bench/blob/main/LICENSE) (accessed 2026-11-08); [2](https://github.com/vals-ai/legal-research-bench/blob/main/README.md) (accessed 2026-11-08); [3](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08).

### 论文入口

https://arxiv.org/abs/2610.00609

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Code

https://github.com/vals-ai/legal-research-bench

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Dataset

https://github.com/vals-ai/legal-research-bench

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Official homepage

https://www.vals.ai/benchmarks/legal_research

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Paper title

Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

## Origin and maintenance

### Initiators

Vals AI

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 合作与作者单位

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Authors

```json
[
 "Katrina Drozdov"
 "Oliver Chen"
 "Langston Nashold"
 "Rayan Krishnan"
]
```

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Maintainer

Vals AI

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 资助与资源支持

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

## Design goals

### 测量能力

Across U.S. federal and state law, it retrieves statutes and case law, judges validity, and synthesizes them into a legal-research answer supported by authority.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 与既有基准的差异

Partial correctness, or retrieval alone, cannot be treated as reliability for legal work; omitting one necessary point can also produce an error.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

## Construction

### Question sources

Real work-style research questions written originally by practicing lawyers, covering 8 categories of legal work.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 出题者背景

15 practicing lawyers, with 15 years of experience on average, who write the questions and review them.

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-07).

### Review process

Each question is independently reviewed by at least one additional practicing lawyer; 15 lawyers average 15 years of experience, about 4 lawyer-hours per question; gold materials are not generated with AI apart from light copyediting.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

### Quality control

The GPT-5.4 judge agrees with the majority-vote rubric labels of the lawyers at a rate of 87.4%.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 去污染与泄漏控制

The test set is kept private to prevent overfitting; public examples are separate from the licensable verification set.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

## Data format

### 规模与统计口径

413 questions: 5 public, 200 licensable for verification, and 208 private test.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Question types

Open legal research, including statutory interpretation, application of case-law rules, regulatory frameworks, reconciliation across sources, and validity over time.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Modalities

```json
[
 "文本"
 "Retrieved web pages and legal materials"
]
```

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Languages

U.S. law, English.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### Difficulty

Multi-label difficulty attributes: Reconciliation, 116 questions, and Temporal Validity, 66 questions (the paper's full-set basis of 413 questions); the two may overlap and should not be treated as mutually exclusive strata of difficulty.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

### Public and hidden splits

Scores on the current official web page are based only on the 208-question Test; the paper's results on all 413 questions are not the same definition.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

## Evaluation

### Metrics

All-Pass is primary; a rubric-weighted partial score is also reported.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 评分规则

A response counts as correct only when every required rubric item and the source verification pass; the judge is GPT-5.4.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 提示、采样与工具设置

A shared harness, 3 hours per question, with case-law search, web search, retrieve_information, parse_html_page, and submit_final_result.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 官方脚本

https://github.com/vals-ai/legal-research-bench

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 可比性警告

The live leaderboard of 208 questions on the official site and the historical results for 413 questions in the paper are kept on separate tracks; a score on a legal test cannot certify unsupervised legal practice.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

## Current status

### 核查时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08).

### 最新数据状态

```json
{
 "version": "The original LRB paper corpus of 413 questions; the current official site has a test track of 208 questions"
 "official_page_updated": "2026-11-05"
 "public": 5
 "validation": 200
 "test": 208
}
```

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08).

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-10-01"
 }
]
```

> The original arXiv UTC time has been converted; this does not constitute a dataset version change.

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08).

### 饱和度与证据边界

The current leader under strict All-Pass is 55.77% and has not reached reliability on every question.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 污染与已知问题

Depends on time anchoring, judges, and retrieval tools; a fluent answer does not equal legal reliability.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 相关与衍生基准

Related, and different: LegalBench and LegalBench-RAG measure static legal reasoning and retrieval; the Harvey Legal Agent Benchmark uses a restricted matter document, and LRB retrieves openly among authorities of United States law. This is not an alias or a new version of those benchmarks.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not a run date or a leaderboard-update date)

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

### 官方结果入口

https://www.vals.ai/benchmarks/legal_research

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 独立评测入口

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "Gemini 4 Carbon"
 "score": 55.77
 "metric": "All-Pass (%), Test on 208 questions"
 "source_url": "https://www.vals.ai/benchmarks/legal_research"
 "source_date": "2026-11-05"
 "collected_at": "2026-11-08 "
 "result_type": "Official leaderboard snapshot"
 "track": "Current official test of 208 questions / All-Pass"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "Muse Spark 1.3 Max"
 "score": 55.29
 "metric": "All-Pass (%), Test on 208 questions"
 "source_url": "https://www.vals.ai/benchmarks/legal_research"
 "source_date": "2026-11-05"
 "collected_at": "2026-11-08 "
 "result_type": "Official leaderboard snapshot"
 "track": "Current official test of 208 questions / All-Pass"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "Claude Opus 5"
 "score": 55.29
 "metric": "All-Pass (%), Test on 208 questions"
 "source_url": "https://www.vals.ai/benchmarks/legal_research"
 "source_date": "2026-11-05"
 "collected_at": "2026-11-08 "
 "result_type": "Official leaderboard snapshot"
 "track": "Current official test of 208 questions / All-Pass"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "Claude Opus 4.8"
 "score": "42.9"
 "metric": "All-Pass (%)"
 "track": "The full set of 413 questions from the original paper / historical author experiments"
 "source_url": "https://arxiv.org/pdf/2610.00609"
 "result_type": "Historical results in the paper abstract, not the current official-site leaderboard of 208 questions"
 "snapshot_date": "2026-11-08 "
 }
]
```

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

### 覆盖与局限

The official website states explicitly Updated 11/5/2026; that is the date on which the page was updated, and it is not necessarily the run date of each model. The current leaderboard for the test of 208 questions is retained, and the historical 42.9% on the 413 questions in the paper is listed separately; the two cannot be compared as one ranking.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

## Contact

### 官方公开邮箱

contact@vals.ai (access permission); katrina@vals.ai (corresponding author of the paper)

Sources: [1](https://arxiv.org/abs/2610.00609) (accessed 2026-11-07).

### 仓库反馈

https://github.com/vals-ai/legal-research-bench/issues

> The issue entry of the public repository; access permission should still be sought from Vals.

Sources: [1](https://github.com/vals-ai/legal-research-bench/blob/main/README.md) (accessed 2026-11-08).

### 官方社区

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 隐私与联系边界

The paper states that the questions are original hypothetical factual scenarios, containing no real client information, no personally identifiable information, and no privileged or confidential material; the participating lawyers were paid and consented to the use.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

## Original files

### Paper PDF

https://arxiv.org/pdf/2610.00609

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### PDF SHA-256

a7f99b089bb1ff218471ecab84557f79af3dbb607b1eb6fbb30e926133658876

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

### PDF bytes

```json
467211
```

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2610.00609) (accessed 2026-11-08).

### 已有文件夹

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

### 其他官方文档

```json
[
 {
 "type": "Official dataset card/methods entry"
 "url": "https://github.com/vals-ai/legal-research-bench"
 }
 {
 "type": "Public code documentation"
 "url": "https://github.com/vals-ai/legal-research-bench"
 }
]
```

Sources: [1](https://github.com/vals-ai/legal-research-bench) (accessed 2026-11-08); [2](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08).

### 已有 PDF归档

Unverified

> This group only created a local research entry and did not upload.

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07).

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

Sources: [1](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-07); [2](https://arxiv.org/abs/2610.00609) (accessed 2026-11-08); [3](https://www.vals.ai/benchmarks/legal_research) (accessed 2026-11-08).
