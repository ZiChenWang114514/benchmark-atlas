# HealthBench Professional

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

HealthBench Professional focuses on consultation, documentation, and research dialogues in a physician's work. The 525 public tasks include difficult cases and an enrichment of red-team cases, and they are not a sample of natural clinical frequency. The internal product evaluation in the paper, referenced external implementations, and the AA evaluation of the bare model need to be kept separate; the length correction rewards answers shorter than 2,000 characters, and it does not only penalize long answers.

Guide source: [https://arxiv.org/abs/2604.27470](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Basic information

### Short name

HealthBench Professional

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Full name

HealthBench Professional

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Dataset version

Paper v1 of 2026-04 is accompanied by a public data package of 525 cases (the README does not give a separate semantic version for the data)

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07); [2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07)

### Paper version

v1; 2026-04-30 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Release date

2026-04-30 (submission time of the first arXiv draft; not an inferred data first-release date).

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Section

Biology and medicine

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Subfields

- 临床咨询
- 医疗文书
- 医学研究
- Model judge and rubric evaluation

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07)

### License

MIT (LICENSE at the root of assets.zip, Copyright (c) 2026 OpenAI; the frontmatter of the README likewise marks license: mit).

Sources: [1](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/2604.27470

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 代码入口

https://github.com/openai/simple-evals

Note: A reference-only, unofficial external implementation; the original paper's results use an internal implementation, and the public code is not claimed to fully reproduce the original report.

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07); [2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07)

### Dataset

https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Official homepage

https://arxiv.org/abs/2604.27470

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Paper title

HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Origin and maintenance

### 发起团队

OpenAI

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 合作及署名机构

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Authors

Rebecca Soskin Hicks, Mikhail Trofimov, Dominick Lim, Rahul K. Arora, and others (the full list of authors is in the paper)

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Maintainer

OpenAI

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Funders

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Design goals

### 评测能力

Measures clinical consultation, writing and documentation, medical-research ability, and safety in real work conversations between physicians and models.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 设计动机

Medical multiple-choice questions or synthetic case records cannot cover ordinary clinical chat work; Professional supplements HealthBench for patients and physicians, and does not replace it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Construction

### 材料来源

Dialogues obtained when physicians tested ChatGPT for Clinicians; 525 cases were selected from 15,079 candidates by quality, representativeness, and difficulty.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 编制背景

190 physicians participated, with practical experience spanning 50 countries and 26 medical specialties.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Review process

At least 3 physicians write, review, and give the final adjudication in three stages; for difficult tasks, an independent physician confirms errors and realism.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Quality control

Difficult samples are enriched about 3.5-fold relative to the candidate pool, and about one third are red-team items; an untimed, internet-enabled baseline from specialty-matched physicians is collected for every task.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 去污染边界

The paper requests that the data not be published online question by question; a canary is used, and a small private held-out set is kept to monitor contamination from training.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Data format

### Size

The public assets.zip was read line by line: 525 cases, with consult 236, writing 142, and research 147; good_faith 334 and red_teaming 191; typical 256 and difficult 269. These are counts in the public package, not rates of occurrence in natural clinical practice.

Sources: [1](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07)

### Question types

Single-turn or multi-turn dialogue, generating the next free-text reply to the last user message.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Modalities

- 文本对话

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Languages

The paper says that the primary language is annotated example by example, but the actual keys of the public JSONL do not contain that field. It must not be claimed that the public package carries language labels. Proficiency in 52 languages among the group of physicians does not mean that the 525 questions contain 52 languages. The exact distribution of question languages is Unverified.

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07); [2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07)

### Difficulty

typical is a physician Likert score of 3–7, and difficult is 1–2; the difficult selection was aimed at the OpenAI models of that time, and it is not a natural clinical distribution.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 公开及隐藏划分

The conversations, rubrics, use_case, type, difficulty, specialty, and physician reference responses for 525 public tasks are published; a small private set is also retained, and its size is Unverified.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Evaluation

### Metrics

A rubric score adjusted for length; not clinical accuracy.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 计分

The score of a question is the sum of the satisfied rubric weights divided by the sum of all positive weights. The length correction is s_len=s−2.94×10^-5×(character count−2000), that is, 1.47 percentage points are subtracted for every additional 500 characters and the same amount is added for every 500 characters short. After the mean is taken over questions or samples, the overall score is clipped to [0,1]. It is not clipped question by question.

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/healthbench-professional) (accessed 2026-11-07)

### 提示与运行设置

The paper mainly compares 8 samples per question at the highest available reasoning setting; AA uses 4 repetitions, judged by GPT-5.4 low.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 评测入口

The official paper uses an internal implementation and explicitly does not release an official external implementation; simple-evals for HealthBench is a reference and cannot be called exactly the same implementation.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 可比性边界

The product harness, the bare model, whether there is network access, and length adjustment or truncation must be kept separate; a difficult sample cannot be read as a real-world clinical error rate.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 已核实版本

version：Companion data package of 525 cases for paper v1 of 2026-04; no separate semantic version is given；heat_confidence：A；evidence_2026_h2：- url：https://artificialanalysis.ai/evaluations/healthbench-professional；date：2026-11-07；note：Artificial Analysis currently evaluates 525 tasks independently; the date is the observation date.；- url：https://openai.com/index/gpt-6-astra/；date：2026-11-07；note：The vendor release table continues to list Professional on its own; this is an observation date, and it is not presented as the first-release date.

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07); [2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07)

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2026-04-30；Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### Saturation

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 已知问题

Epoch’s review on 2026-09-10 judged it Flawed; that entry does not state the specific error, and none is guessed. The limits on extrapolating from a model judge, from enrichment by difficulty, and from a correction for length also need attention.

Sources: [1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks) (accessed 2026-11-07)

### 衍生关系

Professional is a complementary evaluation of clinical work relative to HealthBench, not a Hard or Consensus slice, and it does not claim to replace HealthBench.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 官方结果入口

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 第三方结果入口

https://artificialanalysis.ai/evaluations/healthbench-professional

Sources: [1](https://artificialanalysis.ai/evaluations/healthbench-professional) (accessed 2026-11-07)

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Independent evaluation by Artificial Analysis | 1 | GPT-6 Astra (Max) | 66.0 | Length-adjusted rubric score % | [原始来源](https://artificialanalysis.ai/evaluations/healthbench-professional)；采集2026-11-07；Unverified (page does not show a measurement/update date) |
| Independent evaluation by Artificial Analysis | 2 | GPT-6.1 Sol (Max) | 65.1 | Length-adjusted rubric score % | [原始来源](https://artificialanalysis.ai/evaluations/healthbench-professional)；采集2026-11-07；Unverified (page does not show a measurement/update date) |
| Independent evaluation by Artificial Analysis | 3 | Claude Sonnet 5.5 (Max, Default Fallback) | 63.0 | Length-adjusted rubric score % | [原始来源](https://artificialanalysis.ai/evaluations/healthbench-professional)；采集2026-11-07；Unverified (page does not show a measurement/update date) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

Only results under the listed sources and protocols are retained; the update time stated on the leaderboard: Unverified. The access date is not the evaluation run date.

Sources: [1](https://artificialanalysis.ai/evaluations/healthbench-professional) (accessed 2026-11-07)

## Contact

### 公开研究联系邮箱

- rebecca.soskinhicks@openai.com
- mtrofimov@openai.com
- karan@openai.com

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 问题反馈

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 官方账号

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 隐私政策

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Original files

### 原文PDF

https://arxiv.org/pdf/2604.27470

Note: The PDF entry corresponding to the text of the official paper; it was not downloaded, so the hash and the byte count are Unverified.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### PDF SHA-256

ac61ef9d93b93e827e6543e7449d51381539a4bd37dbfa90e7e48b5fd235a628

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07)

### PDF bytes

1171376

Sources: [1](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07)

### Folder

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

### 其他原始材料

- type：README of the official public data package, and the MIT LICENSE；url：https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip
- type：论文与协议；url：https://arxiv.org/abs/2604.27470
- type：Unofficial external reference implementation；url：https://github.com/openai/simple-evals

Sources: [1](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2604.27470) (accessed 2026-11-07)

### PDF

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://arxiv.org/abs/2604.27470) (accessed 2026-11-07)

## Changelog

### 本页修订

- date：2026-11-07；change：首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传。
- date：2026-11-07；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07)
