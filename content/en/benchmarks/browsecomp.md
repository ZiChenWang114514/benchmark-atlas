# BrowseComp

> Benchmark Constitution, in-depth review: 2026-11-08.

BrowseComp uses short answers to measure long-horizon web retrieval. The answer is easy to check, but finding it may require continued search, restating the query, and crossing constraints. It is not a random sample of real user queries, and it does not evaluate whether a long report is useful. The original paper explicitly uses an AI judge to check semantic equivalence, so a third-party tracking page's statement that "no LLM judge is required" cannot override the official protocol. Scores that differ in multi-agent setup, compression strategy, or run budget should not be treated as a ranking under the same protocol.

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

## Basic information

### Short name

BrowseComp

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Full name

BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 版本边界

v1 (1,266-question original set)

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Paper version

arXiv v1（2025-04-16）

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Release date

2025-04-16 (arXiv submission date)

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 板块

Agent

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

> Benchmark Constitution editorial filing.

### 领域

```json
[
 "Deep search"
 "Web browsing"
 "Information retrieval"
]
```

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 许可与限制

MIT (simple-evals repository)

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

> The license of the question dataset itself is separately Unverified; simple-evals issued a deprecation notice in July 2025.

### Paper

https://arxiv.org/abs/2504.12516

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Code

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### Dataset

https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv

[来源1](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问 2026-11-08）

### Official homepage

https://openai.com/index/browsecomp/

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2504.12516)（访问 2026-11-07）

### 论文题名

BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

## Origin and maintenance

### Initiators

OpenAI

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Partner organizations

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

### Authors

Jason Wei、Zhiqing Sun、Spencer Papay、Scott McKinney、Jeffrey Han、Isa Fulford、Hyung Won Chung、Alex Tachard Passos、William Fedus、Amelia Glaese

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 维护入口

OpenAI

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 资助披露

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Design goals

### 测量对象

Search the internet persistently and creatively for information that is hard to find and mutually entangled.

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 既有评测的缺口

Short, easily verified answers are used to test a browsing agent's core persistence and retrieval; the paper states that it sets aside the real user distribution, long answers, and ambiguity resolution.

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

## Construction

### 题源

Human trainers construct questions with multiple constraints by working backward from verifiable facts. The answer must be short, definite, stable, and supported by evidence; these are not model-synthesized questions, and they are not a random sample of real user queries.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 构建人员

Human trainers responsible for creating high-quality evaluation data; solving baselines come from the same population of trainers, but a trainer may not answer a question that trainer wrote. The paper does not call them competition-level search experts.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 审核

It was checked that GPT-4o, both with browsing and without it, together with o1 and with early Deep Research, could not solve the questions. 5 simple searches on Google were used to check that the answer does not appear on the first screen. On some questions another trainer was limited to 10 minutes. If more than 40% of that author's questions were solved, revision was required.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 质控

The requirements are a short, verifiable, and stable reference answer, authors who know the question domain and who add constraints, and feedback for revision if another trainer finds a different but valid answer. The paper explicitly acknowledges that it cannot exhaustively verify every possible answer, and the set cannot be called an absolutely unique set of answers.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 去污染及边界

Table 1 of the original paper states that a canary was added so that a training corpus can be filtered, and it asks that the questions not be published again on the web in plaintext or as images; the official public CSV applies a reversible encoding derived from the canary to the stems and to the answers, and that encoding is not a guarantee of secrecy or of access control.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问 2026-11-08）

## Data format

### 规模与计数口径

1,266 questions

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Question types

Short-answer question answering, verifiable against reference answers

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Modalities

```json
[
 "文本"
 "网页"
]
```

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### Languages

```json
[
 "英语"
]
```

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）

> The Chinese edition, BrowseComp-ZH, is a separate benchmark.

### Difficulty

§3 of the original paper: of the 1,255 questions that humans actually attempted, 888 were abandoned after two hours of search; of the 367 that were claimed to be solvable, 317 matched the reference. The questions were filtered with the models of that time in view, and the filter cannot be taken as the difficulty distribution of models in 2026.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 划分与公开范围

The official script reads the public browse_comp_test_set.csv, which contains encoded question stems, answers, and a canary; this is not a competition protocol of a separately public training set plus hidden test answers.

[来源1](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问 2026-11-08）

## Evaluation

### Metrics

Accuracy (compared with reference short answers)

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)；[来源2](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）

### 评分

§2.3 and Appendix B of the original paper use an AI judge to compare the semantic equivalence of the prediction and the short reference answer, with an HLE-style judge prompt; this is not simple exact matching, and it is not a setting that needs no LLM judge. The judge model is configured by the caller.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问 2026-11-08）

### 提示与运行条件

The official QUERY_TEMPLATE requires Explanation, Exact Answer, and Confidence. Browsing tools, context compression, reasoning level, the number of attempts, and the number of parallel agents are not fixed uniformly by the dataset.

[来源1](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问 2026-11-08）；[来源2](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 官方评测入口

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### 可比性边界

Scores depend heavily on tools, context-management strategy (such as the compression threshold), the number of attempts, and multi-agent parallelism; a model alone and a system with tools cannot be compared directly.

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）；[来源2](https://www.kimi.com/blog/kimi-k3)（访问 2026-11-07）

## Current status

### 复核时间

2026-11-08

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-08）

### 当前版本

```json
{
 "version": "v1 (1,266-question original set)"
 "evidence_2026_h2": [
 {
 "url": "https://www.kimi.com/blog/kimi-k3"
 "date": "2026-11-07"
 "organization": "Moonshot AI"
 "note": "The footnote of the Kimi K3 productivity evaluation specifies BrowseComp context compression in detail and reports a control without compression."
 }
 {
 "url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
 "date": "2026-10-11"
 "organization": "Steel.dev"
 "note": "An independent leaderboard updated on October 11 lists sourced results from several parties, OpenAI, Anthropic, and Moonshot."
 }
 {
 "url": "https://openai.com/index/gpt-6-astra/"
 "date": "2026-11-07"
 "organization": "OpenAI"
 "note": "The official-release evaluation table for GPT-6 Astra explicitly reports BrowseComp, as evidence of recent vendor adoption."
 }
 ]
 "trending": {
 "heat_confidence": "A"
 "summary": "Used repeatedly in frontier releases such as those from OpenAI and Moonshot; the independent tracker was still updating in October."
 }
}
```

[来源1](https://www.kimi.com/blog/kimi-k3)（访问 2026-11-07）；[来源2](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）；[来源3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

> Recent popularity evidence is taken from candidate studies and reopened pages; grade A: adopted independently by multiple frontier laboratories or evaluation organizations.

### 论文修订与后续使用

```json
{
 "arxiv_revisions": [
 {
 "version": "v1"
 "submitted_at": "2025-04-17"
 }
 ]
}
```

[来源1](https://arxiv.org/abs/2504.12516)（访问 2026-11-08）

### Saturation

Near saturation: the highest score tracked by Steel.dev has reached 92.2% (GPT-5.6 Sol Ultra, multi-agent), and the leading single-agent scores are around 90%.

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）

### 风险与冲突

The Steel methods page says that “an LLM judge is not required,” which conflicts with §2.3 of the original paper and with the official scoring template. The scoring method follows the primary source. Once the questions are public, there is a risk that answers will be retrieved and that training will be contaminated. A canary is a protective notice, not proof that there is no contamination.

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问 2026-11-08）；[来源3](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-08）

### 衍生与后续工作

Derivative benchmarks such as BrowseComp-ZH and BrowseComp-Plus are not merged into this entry.

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-08）

### 官方榜入口

https://openai.com/index/browsecomp/

[来源1](https://arxiv.org/abs/2504.12516)（访问 2026-11-08）

### 第三方榜入口

https://leaderboard.steel.dev/leaderboards/browsecomp.md

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）

### 逐轨结果

```json
[
 {
 "model": "GPT-5.6 Sol Ultra"
 "score": "92.2%"
 "metric": "BrowseComp accuracy"
 "note": "4 parallel agents"
 "result_type": "Steel compilation / vendor self-report, not an independent retest by Steel"
 "source_date": "2026-10-11"
 "collected_at": "2026-11-07 "
 "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
 "reported_rank": 1
 "rank": null
 "track": "Steel mixed-configuration reference table / not to be treated as a ranking under the same protocol"
 "accessed": "2026-11-08"
 }
 {
 "model": "GPT-6 Astra"
 "score": "91.5%"
 "metric": "BrowseComp accuracy"
 "note": "Single agent"
 "result_type": "Steel compilation / vendor self-report, not an independent retest by Steel"
 "source_date": "2026-10-11"
 "collected_at": "2026-11-07 "
 "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
 "reported_rank": 2
 "rank": null
 "track": "Steel mixed-configuration reference table / not to be treated as a ranking under the same protocol"
 "accessed": "2026-11-08"
 }
 {
 "model": "Kimi K3"
 "score": "91.2%"
 "metric": "BrowseComp accuracy"
 "note": "300K compression"
 "result_type": "Steel compilation / vendor self-report, not an independent retest by Steel"
 "source_date": "2026-10-11"
 "collected_at": "2026-11-07 "
 "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
 "reported_rank": 3
 "rank": null
 "track": "Steel mixed-configuration reference table / not to be treated as a ranking under the same protocol"
 "accessed": "2026-11-08"
 }
 {
 "model": "Claude Opus 5"
 "score": "90.8%"
 "metric": "BrowseComp accuracy"
 "result_type": "Steel compilation / vendor self-report, not an independent retest by Steel"
 "source_date": "2026-10-11"
 "collected_at": "2026-11-07 "
 "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
 "reported_rank": 4
 "rank": null
 "track": "Steel mixed-configuration reference table / not to be treated as a ranking under the same protocol"
 "accessed": "2026-11-08"
 }
 {
 "model": "GPT-5.6 Sol"
 "score": "90.4%"
 "metric": "BrowseComp accuracy"
 "result_type": "Steel compilation / vendor self-report, not an independent retest by Steel"
 "source_date": "2026-10-11"
 "collected_at": "2026-11-07 "
 "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
 "reported_rank": 5
 "rank": null
 "track": "Steel mixed-configuration reference table / not to be treated as a ranking under the same protocol"
 "accessed": "2026-11-08"
 }
 {
 "rank": null
 "model": "OpenAI Deep Research"
 "score": 51.5
 "metric": "accuracy (%)"
 "track": "Original paper Table 3 / historical experiments with a browsing system"
 "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
 "accessed": "2026-11-08"
 "unit": "%"
 }
 {
 "rank": null
 "model": "gpt-4o-search-preview-2025-03-11"
 "score": 1.9
 "metric": "accuracy (%)"
 "track": "Original paper Table 3 / historical experiments with a browsing system"
 "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
 "accessed": "2026-11-08"
 "unit": "%"
 }
 {
 "rank": 1
 "model": "o1-2024-12-17 (medium)"
 "score": 9.9
 "metric": "accuracy (%)"
 "track": "Original paper Table 3 / historical experiments without browsing"
 "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
 "accessed": "2026-11-08"
 "unit": "%"
 }
 {
 "rank": 2
 "model": "gpt-4.5-preview-2025-02-27"
 "score": 0.9
 "metric": "accuracy (%)"
 "track": "Original paper Table 3 / historical experiments without browsing"
 "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
 "accessed": "2026-11-08"
 "unit": "%"
 }
 {
 "rank": 3
 "model": "gpt-4o-2024-08-06"
 "score": 0.6
 "metric": "accuracy (%)"
 "track": "Original paper Table 3 / historical experiments without browsing"
 "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
 "accessed": "2026-11-08"
 "unit": "%"
 }
]
```

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-08）；[来源2](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

### 覆盖边界

The Steel page writes its own update time as 2026-10-11, but it includes new models from November, so that date should be treated as a statement on the page rather than as a reliable experiment date for each row; reported_rank is kept, and this record's rank under mixed protocols is dropped. Browsing and no browsing in the original paper are separate tracks, and 51.5% is historical Deep Research, not presented as the current first place.

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-08）；[来源2](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

## Contact

### 公开研究联系

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

### 项目反馈

https://github.com/openai/simple-evals/issues

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### 官方社交入口

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

### 联系信息边界

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Original files

### 原始PDF

https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问 2026-11-07）

### PDF SHA-256

1bd473341db82cb66ad7cdff3ee911f9d157c083bad08d33440fa7244a4b1916

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

> SHA-256 of the downloaded PDF bytes. It does not mean the file was uploaded.

### PDF bytes

335891

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问 2026-11-08）

> Downloaded PDF byte count; the archive remains Unverified.

### 目录

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

### 其他官方材料

```json
[
 "https://arxiv.org/pdf/2504.12516"
]
```

[Source 1](https://arxiv.org/abs/2504.12516) (accessed 2026-11-07)

### 论文归档

Unverified

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-07）

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

[来源1](https://openai.com/index/browsecomp/)（访问 2026-11-08）
