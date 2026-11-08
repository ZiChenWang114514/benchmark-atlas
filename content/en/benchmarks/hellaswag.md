# HellaSwag

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

HellaSwag builds four-choice continuation questions from ActivityNet captions and WikiHow instructions, and it uses generated negatives and adversarial filtering to reduce surface language cues. Official submission to test closed in November 2024; validation scores in common use today cannot be attached to that historical leaderboard and presented as progress on the same track.

Sources for the reading guide: [https://arxiv.org/abs/1905.07830](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07); [https://arxiv.org/html/2610.11978v1](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07)

## Basic information

### Short name

HellaSwag

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Full name

HellaSwag: Can a Machine Really Finish Your Sentence?

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Dataset version

2019 dataset; the official test leaderboard stopped accepting submissions in November 2024

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07); [2](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Paper version

v1; 2019-05-20 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Release date

2019-05-20 (submission time of the first arXiv draft; not an inferred data first-release date).

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Section

Reasoning

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### Subfields

- Commonsense situational reasoning

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### License

The Rowan/hellaswag data card on HF marks MIT and links the LICENSE of the original repository; access to the original LICENSE failed, this limit on the level of evidence is retained, and a word-for-word check of the original license was not completed.

Sources: [1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/1905.07830

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 代码入口

https://github.com/rowanz/hellaswag

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### Dataset

https://github.com/rowanz/hellaswag

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07); [2](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Official homepage

https://rowanzellers.com/hellaswag/

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07); [2](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Paper title

HellaSwag: Can a Machine Really Finish Your Sentence?

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

## Origin and maintenance

### 发起团队

University of Washington、Allen Institute for AI

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 合作及署名机构

Unverified

Note: Only the institutions named on the paper are confirmed; not every listed affiliation is automatically treated as a formal partner

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Authors

- Zellers, Rowan
- Holtzman, Ari
- Bisk, Yonatan
- Farhadi, Ali
- Choi, Yejin

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Maintainer

The official page is provided by the Rowan Zellers team and states that test-leaderboard submission closed in November 2024; the old leaderboard is not used to infer an ongoing maintenance commitment.

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### Funders

NSF Graduate Research Fellowship and research grants, DARPA CwC (via ARO), IARPA DIVA, Sloan Fellowship, Allen Institute for AI, NVIDIA AI Lab, and gifts from Google/Facebook. The Google Cloud TPU team provided computing assistance.

Sources: [1](https://arxiv.org/pdf/1905.07830) (accessed 2026-11-07)

## Design goals

### 评测能力

Measures commonsense judgments of whether the next event is plausible in everyday activities and in procedural instructions.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 设计动机

Language models may use surface fluency without understanding physical and event commonsense; distractors that are easy for humans and difficult for models are needed.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

## Construction

### 材料来源

ActivityNet video captions and WikiHow instructions serve as context and the correct ending, and a generative model produces incorrect endings.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 编制背景

The research team designed adversarial filtering; crowd workers judged the plausibility of candidate endings.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Review process

A multi-round discriminator filters model-generated negatives, and human verification retains distinguishable samples.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Quality control

Adversarial filtering iteratively selects incorrect answers that the discriminative models of the time do not easily recognize, while also controlling length and context.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 去污染边界

In-domain and zero-shot categories are set by activity category; this is not the same as a modern audit of pretraining contamination.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

## Data format

### Size

Public row counts on the HF data card: train 39,905, validation 10,042, and test 10,003, totaling 59,950. The paper's collection scale of about 70,000 cannot replace this exact count of the public package.

Sources: [1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md) (accessed 2026-11-07); [2](https://arxiv.org/pdf/1905.07830) (accessed 2026-11-07)

### Question types

Given a context and 4 candidate endings, choose the only reasonable continuation.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Modalities

Text context and 4 text endings; ActivityNet videos supply the caption source of the questions, but the public standard task does not require the model to watch the video directly.

Sources: [1](https://arxiv.org/pdf/1905.07830) (accessed 2026-11-07); [2](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md) (accessed 2026-11-07)

### Languages

English question text; for formal or mathematical notation, see the modality and the repository format

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Difficulty

The original paper's human result of 95.6% and the gap to models of that time are historical context and cannot be used to describe 2026 models as still below 48%.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 公开及隐藏划分

The HF card lists train 39905, validation 10042, and test 10003; the test leaderboard on the official website and the validation evaluation in general use are not the same split.

Sources: [1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md) (accessed 2026-11-07); [2](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

## Evaluation

### Metrics

4-choice (select 1) accuracy; the official leaderboard also separates in-domain/zero-shot and ActivityNet/WikiHow.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 计分

The choice label is matched to the reference answer; an implementation that uses a letter generated by an LLM, or log-likelihood, must be stated.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 提示与运行设置

On the official historical leaderboard, GPT-4 base uses 10-shot; contemporary generation and likelihood templates, length normalization, and the number of shots must be stated.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 评测入口

https://github.com/rowanz/hellaswag

Sources: [1](https://github.com/rowanz/hellaswag) (accessed 2026-11-07); [2](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 可比性边界

An official test leaderboard that is no longer updated is not contemporary validation-set SOTA; the two splits must not be ranked together.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07)

## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 已核实版本

The official site states that submission has been closed since November 2024; what can be read now is a historical test leaderboard, and it should not be called a leaderboard that is still being updated in 2026.

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2019-05-20；；2026_h2_evidence：- url：https://arxiv.org/html/2610.11978v1；date：2026-10-08；note：Jev research Tables 1–2 and §3.1 actually compare multiple classes of models on HellaSwag and do not count ARC-Easy or other subsets separately.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### Saturation

Unverified

Note: Whether it is saturated depends on the specific split, the tools, and the protocol; the scores below are only a snapshot from a limited source and are not a judgment of overall saturation or of SOTA

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07); [2](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07); [3](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07)

### 已知问题

The validation set is in general public use; adversarial filtering is a method of construction, not a guarantee against future training contamination.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07); [2](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### 衍生关系

It follows the direction of SWAG but increases distractor difficulty; this entry does not treat ActivityNet and WikiHow as independent benchmarks.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07); [2](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### 官方结果入口

https://rowanzellers.com/hellaswag/

Sources: [1](https://github.com/rowanz/hellaswag) (accessed 2026-11-07); [2](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

### 第三方结果入口

Unverified

Note: No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Official historical test leaderboard; submissions stopped being accepted in 2024-11 | 1 | GPT4 base 10-shot | 95.3 | overall test accuracy % | [原始来源](https://rowanzellers.com/hellaswag/)；采集2026-11-07；2023-03-08 (date listed on the official site) |
| Official historical test leaderboard; submissions stopped being accepted in 2024-11 | 2 | ALUM | 85.6 | overall test accuracy % | [原始来源](https://rowanzellers.com/hellaswag/)；采集2026-11-07；2020-03-23 (date listed on the official site) |
| Official historical test leaderboard; submissions stopped being accepted in 2024-11 | 3 | RoBERTa | 85.2 | overall test accuracy % | [原始来源](https://rowanzellers.com/hellaswag/)；采集2026-11-07；2019-07-25 (date listed on the official site) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

Duplicate GPT-4/ALUM rows are removed, and only the top three models that can be checked on the official closed leaderboard are listed. Validation research results are not mixed in. The leaderboard's closing month is 2024-11, and the date of the last update is Unverified. Dates beside model names are not collection dates.

Sources: [1](https://rowanzellers.com/hellaswag/) (accessed 2026-11-07)

## Contact

### 公开研究联系邮箱

Unverified

Note: No dedicated contact email was recorded from official material already verified; personal email addresses are not guessed

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 问题反馈

https://github.com/rowanz/hellaswag/issues

Sources: [1](https://github.com/rowanz/hellaswag) (accessed 2026-11-07)

### 官方账号

Unverified

Note: No dedicated official social account has been verified, and personal accounts of the same name are not included

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### 隐私政策

Unverified

Note: A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

## Original files

### 原文PDF

https://arxiv.org/pdf/1905.07830

Sources: [1](https://arxiv.org/abs/1905.07830) (accessed 2026-11-07)

### PDF SHA-256

9a042fdcc4a22848cffde37e9c5257e423443980172bab7367dffb4e779aac37

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/1905.07830) (accessed 2026-11-07)

### PDF bytes

1192712

Sources: [1](https://arxiv.org/pdf/1905.07830) (accessed 2026-11-07)

## Changelog

### 本页修订

- date：2026-11-07；；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- date：2026-11-07；；change：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。；fields_updated：- basic_info.license；- latest_status.latest_dataset_version；- data_format.public_hidden_split；- leaderboard.results；- leaderboard.coverage_note
- date：2026-11-07；；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07)
