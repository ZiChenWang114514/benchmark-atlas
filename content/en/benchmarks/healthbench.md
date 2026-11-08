# HealthBench

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

The original HealthBench uses rubrics written by physicians to evaluate the last reply in 5,000 medical dialogues; Hard and Consensus are slices of it. It is not the same as the 525 cases of HealthBench Professional. The length-adjusted leaderboard of the latter cannot be treated as an updated score for the original, and a rubric score cannot be treated as clinical accuracy.

Guide source: [https://arxiv.org/abs/2505.08775](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07)

## Basic information

### Short name

HealthBench

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Full name

HealthBench

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Dataset version

Original HealthBench (not Professional)

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Paper version

v1; 2025-05-14 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Release date

2025-05-14 (submission time of the first arXiv draft; not an inferred data first-release date).

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Section

Biology and medicine

Note: Editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Subfields

- 生物与医学

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### License

MIT; the HealthBench entry in the official simple-evals README explicitly links the MIT LICENSE of this repository, and the full text of the license was read.

Sources: [1](https://raw.githubusercontent.com/openai/simple-evals/HEAD/README.md) (accessed 2026-11-07 ) ; [2](https://raw.githubusercontent.com/openai/simple-evals/HEAD/LICENSE) (accessed 2026-11-07 )

### Paper

https://arxiv.org/abs/2505.08775

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 代码入口

https://github.com/openai/simple-evals

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Dataset

https://github.com/openai/simple-evals

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Official homepage

https://arxiv.org/abs/2505.08775

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Paper title

HealthBench: Evaluating Large Language Models Towards Improved Human Health

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Origin and maintenance

### 发起团队

OpenAI

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 合作及署名机构

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Authors

Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, and others; the full list is in the paper.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Maintainer

OpenAI

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Funders

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Design goals

### 评测能力

Quality, safety, context awareness, and communication ability of open-ended medical conversations for general users and healthcare workers.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 设计动机

Medical multiple-choice and short-answer questions poorly reflect real clinical interaction and often lack validation of agreement with physicians' judgments.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Construction

### 材料来源

Mainly synthetic scenarios, supplemented by physician red-teaming and HealthSearchQA rewrites; 262 physicians took part, with practice experience covering 60 countries and 26 specialties.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 编制背景

262 physicians, covering 26 specialties and practice experience in 60 countries; the paper lists 49 languages in which physicians can contribute, and this is not automatically taken as the dataset's exact language distribution.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Review process

Physicians are screened by paid onboarding tasks; continuous automatic and human review removes annotations from low-quality contributors.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Quality control

A consensus criterion requires endorsement by at least two physicians and by a majority of physicians; a meta-evaluation also compares the agreement between model scores and physician scores.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 去污染边界

A canary is published, together with a request not to circulate example items, and a small private hold-out from the same distribution is retained; its size is Unverified.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Data format

### Size

5,000 conversations; 48,562 unique rubric criteria; Hard is 1,000 questions; Consensus is 3,671 questions and retains only the consensus criteria.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Question types

Reply to the last user message given the complete single-turn or multi-turn history.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Modalities

- 文本

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Languages

Multilingual medical dialogue; the exact number of questions in each language is Unverified.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Difficulty

Hard is 1,000 difficult samples: o3, Grok 3, Gemini 2.5 Pro, Claude 3.7 Sonnet, and Llama 4 Maverick are first scored question by question, questions on which every model failed to obtain a positive score are removed, and then the lowest 1,000 questions by the five-model mean are selected. This is not a random sample of the natural distribution of medical cases.

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 )

### 公开及隐藏划分

A public main set and a small private hold-out from the same distribution; the exact hold-out question count is Unverified.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Evaluation

### Metrics

Overall normalized rubric score, scores by theme/axis, and worst-at-k; Hard and Consensus are reported independently.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 计分

Each rubric item has a weight from -10 to 10, and the weight is not 0. If the item is met, that item's full points are awarded; otherwise the item scores 0. Each question is divided by the sum of its positive weights, the results are then averaged over all questions, and finally the overall score is clipped to [0,1]. A single question may be negative, and questions should not be clipped one by one before the overall score. The default judge is GPT-4.1.

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 )

### 提示与运行设置

Generate a reply to the final user message; in the original paper the OpenAI models use temperature=1, and settings for other vendors are in Appendix H.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 评测入口

The HealthBench evaluation, meta-evaluation, Hard and Consensus settings, and plotting tools in OpenAI simple-evals.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 可比性边界

The original scores differ from AA’s length-adjusted scores; Hard, Consensus, and Professional on 525 questions are not the same metric; the Professional leaderboard cannot be moved onto this entry.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 已核实版本

version：Original HealthBench (not Professional)；evidence_2026_h2：- url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；date_type：observed_on；note：The current table of additional evaluations at AA lists, explicitly and separately, the original HealthBench of 5,000 questions and Professional with 525 questions. The Professional leaderboard on the web page is not assigned to this entry. A candidate note also lists a system card from October. That card has not been verified, and it cannot be counted as a second piece of heat evidence that has been verified.

Note: The heat grade is adopted from the candidate; only evidence that has been opened and can be verified is retained. A does not guarantee that every version received independent reruns by multiple institutions.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07 )

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2025-05-14；timezone：

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### Saturation

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 已知问题

The authors use a canary and a private set of the same distribution to check the risk of contamination from training; the public set cannot, on that basis, be declared free of contamination. The paper discusses disagreement among physicians about how the rubric is interpreted and about how much error they prefer to tolerate; a score from a model judge is not direct proof of a real clinical benefit or of the safety of a patient.

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 )

### 衍生关系

HealthBench Hard and Consensus are derivative slices of the original version. HealthBench Professional is a different benchmark of 525 clinical-work dialogues. This catalog files it separately and does not assign its leaderboard to this entry.

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07 )


## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 官方结果入口

https://arxiv.org/abs/2505.08775

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 第三方结果入口

https://artificialanalysis.ai/methodology/intelligence-benchmarking

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07 )

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Original paper Table 7: original 5,000 questions, mean of 16 runs, no length adjustment | — | o3 | 0.599 ± 0.0016 | HealthBench normalized rubric score (0–1) | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 (paper submission) |
| Original paper Table 7: original 5,000 questions, mean of 16 runs, no length adjustment | — | GPT-4.1 | 0.4778 ± 0.0022 | HealthBench normalized rubric score (0–1) | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 (paper submission) |
| Original paper Table 7: original 5,000 questions, mean of 16 runs, no length adjustment | — | o1 | 0.42 ± 0.0022 | HealthBench normalized rubric score (0–1) | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 (paper submission) |
| Original paper Table 7: original 5,000 questions, mean of 16 runs, no length adjustment | — | GPT-4o (Aug 2024) | 0.3233 ± 0.002 | HealthBench normalized rubric score (0–1) | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 (paper submission) |
| Original paper Table 7: original 5,000 questions, mean of 16 runs, no length adjustment | — | GPT-3.5 Turbo | 0.1554 ± 0.0029 | HealthBench normalized rubric score (0–1) | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 (paper submission) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

Exact means and standard deviations from 16 runs are restored from Table 7 of the original paper. The abstract's rounded 60% is not substituted for 0.5990, and this historical slice is not called current SOTA. The current AA leaderboard for Professional, with 525 questions, is a separate entry and cannot be moved into this entry.

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 )


## Contact

### 公开研究联系邮箱

- karan@openai.com

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 问题反馈

https://github.com/openai/simple-evals/issues

Sources: [1](https://raw.githubusercontent.com/openai/simple-evals/HEAD/README.md) (accessed 2026-11-07 )

### 官方账号

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 隐私政策

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Original files

### 原文PDF

https://arxiv.org/pdf/2505.08775

Note: Entry point for the official arXiv PDF of the original paper; this group does not download or upload it.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### PDF SHA-256

f61c53f6bde84a3964531efe04a75389f9bba9e70a35b4012c871c9ec0b512f3

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 )

### PDF bytes

8359760

Sources: [1](https://arxiv.org/pdf/2505.08775) (accessed 2026-11-07 )

### Folder

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### 其他原始材料

- type：Official methods or project page；url：https://arxiv.org/abs/2505.08775；accessed：2026-11-07

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )

### PDF

Unverified

Note: This group only created a staging entry and did not upload.

Sources: [1](https://arxiv.org/abs/2505.08775) (accessed 2026-11-07 )


## Changelog

### 本页修订

- date：2026-11-07；timezone： ()；change：首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07 )

