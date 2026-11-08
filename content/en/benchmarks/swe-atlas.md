# SWE Atlas

> Benchmark Constitution, in-depth review 2026-11-08.

SWE Atlas addresses software-engineering work other than bug fixing: runtime understanding of a codebase, writing tests, and behavior-preserving refactoring. The 284 questions are split into three classes, 124/90/70. Scoring looks at both program behavior and an expert rubric. v1.1 under the new judge cannot be compared directly, as a growth comparison, with the old-judge results in the original paper. The full tasks and the tools for running them are already public. This entry adds the repository, rather than continuing to treat the project as one that has only a private leaderboard.

[Source 1](https://arxiv.org/abs/2605.08366) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-Atlas) (accessed 2026-11-08); [Source 3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall) (accessed 2026-11-08)

## Basic information

### Short name

SWE Atlas

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Full name

SWE Atlas

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Benchmark version

v1.1 (updated November 2026)

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Paper version

v1 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### Release date

2026-05-09 (arXiv v1 submitted 2026-05-09); the v1.1 announcement on the official site is 2026-11, precise only to the month.

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### Section

Code

> Benchmark Constitution editorial filing. It is not an official classification.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 领域

```json
[
 "代码"
]
```

> Editorial tag

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 许可与适用范围

Apache-2.0 (official LICENSE); third-party wording in QnA must retain the NOTICE, and each piece of upstream code remains under its original license.

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2605.08366

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### Code

https://github.com/scaleapi/SWE-Atlas

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 数据

https://github.com/scaleapi/SWE-Atlas/tree/main/data

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### Official entry

https://labs.scale.com/leaderboard/swe-atlas?tab=overall

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Paper title

SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Scale AI

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 合作/参与机构

v1.1 acknowledges Artificial Analysis and Inductive ML for contributions on scoring wording and reward-hacking feedback.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Authors

```json
[
 "Mohit Raghavendra"
 "Soham Dan"
 "Miguel Romero Calvo"
 "Yannis Yiming He"
 "Johannes Baptist Mols"
 "Gautam Anand"
 "Cole McCollum"
 "Edgar Arakelyan"
 "Vijay Bharadwaj"
 "Andrew Park"
 "Jeff Da"
 "MohammadHossein Rezaei"
 "Bing Liu"
 "Brad Kenstler"
 "Yunzhong He"
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://static.scale.com/uploads/6691558a94899f2f65a87a75/Coding_Agent_Eval%20(5).pdf)（访问 2026-11-08）

### Maintainer

Scale Labs

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Funders

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## Design goals

### Abilities measured

Codebase understanding, test writing, and refactoring.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Design background

Supplements software-engineering evaluations that attend only to issue resolution.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## Construction

### Question sources

Professional software-engineering work; the current methods page states that it comes from 15 production repositories and 6 languages.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 出题者背景

The questions are written by professional engineers with years of practical experience in software engineering, with a separate QC team and an audit by three trusted experts; the appendix states that the contract pay meets or exceeds the local wage requirement, and unpaid volunteer labor is not used.

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### Review process

Reference solutions must pass every check; an independent QC review follows; three experts then independently check the instructions, the verification, and the rubrics, and a rubric is removed if at least two of them judge it invalid, overly prescriptive about the implementation, or ambiguous.

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### Quality control

v1.1 reruns all models, updates the judge and the scoring conditions, and restricts network access.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 污染控制

Test Writing and Refactoring screen patches from a passing agent against the gold patch with Jaccard and with sequence similarity, as a check for memorization, and no clear verbatim reproduction was seen; this does not prove the absence of contamination. The container deletes the git history and initializes it again, and v1.1 restricts the network further.

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

## Data format

### 题量

284 tasks: Codebase QnA 124, Test Writing 90, and Refactoring 70. Paper v1 says 18 repositories, and the current official site for v1.1 says 15 repositories. Both use the same 284 questions, but the stated set of source repositories differs, and the two figures were not forced to agree.

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### 任务形式

One target prompt per task; the agent may build, run, and test inside the repository Docker.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Modalities

```json
[
 "代码"
 "文本"
]
```

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Languages

Go、Python、TypeScript、C、C++、JavaScript

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### Difficulty

Refactoring in the paper refers to edits of 35–2,073 lines and requires coordination across several files and preservation of behavior; QnA emphasizes evidence from runtime, and Test Writing must pass on the real implementation and must fail after that implementation is replaced by a stub.

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### Public and hidden splits

The complete 284 tasks in three categories, the reference solution, the grader, the rubric, the judge prompt, and the digest-pinned public images are public; the agent can see only the instruction and the runtime repository, and the scoring materials are used at the verification stage.

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

The overall index of v1.1 and the three category sub-leaderboards; the reward of each trial is 0/1, and the mean over 3 attempts is pass@1. In the paper, Pass 3 means that all three attempts succeed, and Pass@3 means that at least one attempt succeeds; the two must not be confused.

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 评分

QnA: every required rubric item passes. TW: the manifest, the mutation, and the required rubric pass at the same time. RF: behavior is preserved, or the regression tests pass, and the required rubric passes. v1.1 uses GPT-6.1 Sol high as the judge, with a majority of 3 votes; a refusal, an empty answer, or a response that cannot be scored is 0, and an infrastructure error must be rerun rather than counted as 0.

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 运行设置

The v1.1 configuration uses Claude Code 2.1.293 and Codex 0.142.1, with effort max and 3 runs per task; WebSearch and WebFetch are forbidden, and the network allowlist permits only model endpoints; the judge is gpt-6.1-sol high, with a majority of 3 votes.

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 评测工具

The entry point is Harbor run.sh. configs/ stores run configurations for oracle, nop, and the Anthropic and OpenAI leaderboards. data/qa, data/tw, and data/rf each have tests and scorers.

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### Comparability

The judge and the environment differ between v1.1 and v1.0, so the scores cannot be compared directly.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
 "version": "v1.1 (updated November 2026)"
 "heat_confidence": "B"
 "why_trending": "This is mainly a current presentation by a single organization, or continued self-evaluation by a vendor, and it does not represent broad adoption across the industry."
 "evidence_2026_h2": [
 {
 "url": "https://labs.scale.com/leaderboard/swe-atlas?tab=overall"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Official maintainer"
 "note": "The current official methods and leaderboard have been opened; the observation date is not presented as the publication date."
 }
 ]
}
```

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-05-09"
 }
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 饱和与能力边界

The current overall peak for v1.1 is 77.40±5.00; workflows and harnesses differ, and this is not yet close to a perfect score on every task. An old judge score in the original paper, such as 43.49, cannot be read together with 77.40 as an increment under the same protocol.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 风险与争议

v1.1 responds to reward-hacking feedback and strengthens the environment; the public upstream code still carries a risk of training contamination.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 系列与衍生关系

Distinct from SWE-bench; QnA, Test Writing, and Refactoring are sub-leaderboards of this entry and are not counted separately.

> The editorial standard for deduplication; concrete differences among versions still follow the official materials.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2605.08366) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-Atlas) (accessed 2026-11-08); [Source 3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall) (accessed 2026-11-08)

### Official entry

https://labs.scale.com/leaderboard/swe-atlas?tab=overall

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 独立来源

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 分来源与协议结果

#### Scale v1.1 / overall

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5.5 | 77.4 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5,"source_month":"2026-11"} |
| 2 | Fable 5.1 | 74.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.3,"source_month":"2026-11"} |
| 3 | Gemini 4 Argon | 70.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.5,"source_month":"2026-11"} |
| 4 | GPT-6 Astra | 69.4 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.6,"source_month":"2026-11"} |
| 5 | Sonnet 5.5 | 67.5 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.7,"source_month":"2026-11"} |
| 6 | GPT-6.1 Sol | 65.9 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.7,"source_month":"2026-11"} |
| 7 | Muse Wonder 1.0 | 64.8 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 8 | Grok 4.7 | 62.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 9 | DeepSeek V4.1 Flash | 62.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 10 | Inkling 2 Small | 61.9 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 11 | Kimi K3 | 61 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |
| 12 | Haiku 5.5 | 59.4 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |
| 13 | GPT-6.1 Terra | 57.7 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |
| 14 | Gemini 3.8 Flash | 57.3 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 15 | GPT-6 Luna | 50.8 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":6,"source_month":"2026-11"} |
| 16 | Muse Spark Open | 42.3 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |

#### Scale v1.1 / qna

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5.5 | 77.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.5,"source_month":"2026-11"} |
| 2 | Inkling 2 Small | 74.2 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.8,"source_month":"2026-11"} |
| 3 | Fable 5.1 | 73.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.9,"source_month":"2026-11"} |
| 4 | Muse Wonder 1.0 | 73.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.9,"source_month":"2026-11"} |
| 5 | Grok 4.7 | 73.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.9,"source_month":"2026-11"} |
| 6 | Sonnet 5.5 | 71.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8,"source_month":"2026-11"} |
| 7 | GPT-6.1 Sol | 71 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.1,"source_month":"2026-11"} |
| 8 | DeepSeek V4.1 Flash | 71 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.1,"source_month":"2026-11"} |
| 9 | GPT-6 Astra | 70.2 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.2,"source_month":"2026-11"} |
| 10 | Gemini 4 Argon | 65.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.5,"source_month":"2026-11"} |
| 11 | Kimi K3 | 65.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.5,"source_month":"2026-11"} |
| 12 | Haiku 5.5 | 62.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.7,"source_month":"2026-11"} |
| 13 | GPT-6.1 Terra | 54 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |
| 14 | GPT-6 Luna | 50.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |
| 15 | Muse Spark Open | 50 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |
| 16 | Gemini 3.8 Flash | 45.2 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |

#### Scale v1.1 / testwriting

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Fable 5.1 | 78.9 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.6,"source_month":"2026-11"} |
| 2 | Opus 5.5 | 77.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.8,"source_month":"2026-11"} |
| 3 | Gemini 4 Argon | 77.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.8,"source_month":"2026-11"} |
| 4 | Gemini 3.8 Flash | 71.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.5,"source_month":"2026-11"} |
| 5 | Sonnet 5.5 | 67.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.8,"source_month":"2026-11"} |
| 6 | GPT-6 Astra | 66.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.9,"source_month":"2026-11"} |
| 7 | GPT-6.1 Sol | 66.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.9,"source_month":"2026-11"} |
| 8 | Grok 4.7 | 64.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 9 | Kimi K3 | 63.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 10 | Haiku 5.5 | 63.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 11 | GPT-6.1 Terra | 63.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 12 | Muse Wonder 1.0 | 61.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.3,"source_month":"2026-11"} |
| 13 | DeepSeek V4.1 Flash | 61.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.3,"source_month":"2026-11"} |
| 14 | Inkling 2 Small | 58.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.4,"source_month":"2026-11"} |
| 15 | GPT-6 Luna | 54.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.5,"source_month":"2026-11"} |
| 16 | Muse Spark Open | 41.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.4,"source_month":"2026-11"} |

#### Scale v1.1 / refactoring

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5.5 | 77.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 2 | GPT-6 Astra | 71.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.8,"source_month":"2026-11"} |
| 3 | Fable 5.1 | 70 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11,"source_month":"2026-11"} |
| 4 | Gemini 4 Argon | 67.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.3,"source_month":"2026-11"} |
| 5 | Sonnet 5.5 | 62.9 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.6,"source_month":"2026-11"} |
| 6 | GPT-6.1 Sol | 60 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.8,"source_month":"2026-11"} |
| 7 | Muse Wonder 1.0 | 60 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.8,"source_month":"2026-11"} |
| 8 | GPT-6.1 Terra | 55.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.9,"source_month":"2026-11"} |
| 9 | Gemini 3.8 Flash | 55.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.9,"source_month":"2026-11"} |
| 10 | DeepSeek V4.1 Flash | 54.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 11 | Kimi K3 | 54.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 12 | Inkling 2 Small | 53.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 13 | Haiku 5.5 | 52.9 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 14 | Grok 4.7 | 48.6 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 15 | GPT-6 Luna | 47.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 16 | Muse Spark Open | 35.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.5,"source_month":"2026-11"} |

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### 覆盖与时效

From the variants embedded in the official page, 16 rows are extracted, item by item, for each of the four tracks Overall, QnA, Test Writing, and Refactoring, 64 rows in total, and the original rank and CI are kept. createdAt is metadata of the entry and is not presented as the date of the run or of the leaderboard update; the update on the official site is precise only to November 2026.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

## Contact

### 公开工作邮箱

```json
[
 "mohit.raghavendra@scale.com"
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 官方反馈

https://github.com/scaleapi/SWE-Atlas/issues

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 公开社区

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 隐私边界

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2605.08366v1

[来源1](https://arxiv.org/pdf/2605.08366v1)（访问 2026-11-08）

### PDF SHA-256

af39ccd39558020ce2229788542294d61342d791ef5e01547b78f160bf4dd5a7

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2605.08366v1)（访问 2026-11-08）

### PDF bytes

```json
2118311
```

[来源1](https://arxiv.org/pdf/2605.08366v1)（访问 2026-11-08）

### Folder

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "Opened primary material"
 "url": "https://arxiv.org/abs/2605.08366"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://github.com/scaleapi/SWE-Atlas"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://labs.scale.com/leaderboard/swe-atlas?tab=overall"
 "accessed": "2026-11-08"
 }
]
```

[Source 1](https://arxiv.org/abs/2605.08366) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-Atlas) (accessed 2026-11-08); [Source 3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

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

[Source 1](https://arxiv.org/abs/2605.08366) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-Atlas) (accessed 2026-11-08); [Source 3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall) (accessed 2026-11-08)
