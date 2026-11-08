# GSM8K

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

GSM8K tests the ability to solve a problem and to select a solution, using English multi-step arithmetic word problems. The concepts in the questions are simple, but a single generation, a calculator, selection of the best answer by a verifier, and voting over multiple samples are not the same protocol; this page retains the exact public split and keeps vendor reports separate from independent evaluation.

Sources for the reading guide: [https://arxiv.org/abs/2110.14168](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07); [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07)

## Basic information

### Short name

GSM8K

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Full name

Grade School Math 8K

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Dataset version

main data; the repository is marked Archive, and the code is provided as is

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Paper version

v2; 2021-11-18 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Release date

2021-10-27 (submission time of the first arXiv draft; not an inferred data first-release date).

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Section

Mathematics

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 )

### Subfields

- 数学应用题

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### License

MIT (the LICENSE of the official repository; rights in third-party original materials are not inferred from it).

Sources: [1](https://raw.githubusercontent.com/openai/grade-school-math/master/LICENSE) (accessed 2026-11-07 )

### Paper

https://arxiv.org/abs/2110.14168

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 代码入口

https://github.com/openai/grade-school-math

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 )

### Dataset

https://github.com/openai/grade-school-math

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Official homepage

https://github.com/openai/grade-school-math

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Paper title

Training Verifiers to Solve Math Word Problems

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )


## Origin and maintenance

### 发起团队

OpenAI

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 合作及署名机构

Unverified

Note: Only the institutions named on the paper are confirmed; not every listed affiliation is automatically treated as a formal partner

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Authors

- Cobbe, Karl
- Kosaraju, Vineet
- Bavarian, Mohammad
- Chen, Mark
- Jun, Heewoo
- Kaiser, Lukasz
- Plappert, Matthias
- Tworek, Jerry
- Hilton, Jacob
- Nakano, Reiichiro
- Hesse, Christopher
- Schulman, John

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Maintainer

The official OpenAI repository; currently in Archive status

Sources: [1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md) (accessed 2026-11-07 )

### Funders

Unverified

Note: Paper acknowledgments and current operational funding were not verified item by item; institutional affiliation is not a funding source

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )


## Design goals

### 评测能力

Evaluates multi-step arithmetic, and the ability of a verifier to select a solution, in linguistically diverse elementary and lower-secondary mathematics word problems.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 设计动机

Conceptual simplicity is not equivalent to stable solvability by a language model; memorizing only fixed question-type templates should be avoided.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )


## Construction

### 材料来源

Contracted human question writers write word problems and natural-language solutions; the paper's process includes Upwork, Surge AI, and model-generated question seeds that can be rewritten.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 编制背景

Paid human question writers, with the research team performing a second solve and data review; it cannot be stated that every question comes from a mathematics expert.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Review process

A second person solves each question independently; questions in disagreement are revised or removed, and question similarity is checked.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Quality control

Natural-language solutions include calculation notes, and the final numeric value follows ####; a version with automatically generated Socratic sub-questions is also provided.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 去污染边界

Checking templates and similar questions at the time of collection helps quality control; it does not guarantee that future pretraining data contain no public questions.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )


## Data format

### Size

The official HF dataset card for openai/gsm8k: train 7,473 and test 1,319, 8,792 in total; main and socratic each use the same split and cannot be added together into 17,584 independent questions. The 8.5K and the 7.5K/1K in the README are round numbers given by the authors, and exact reproduction follows the dataset card and the files.

Sources: [1](https://huggingface.co/datasets/openai/gsm8k/raw/main/README.md) (accessed 2026-11-07 ) ; [2](https://raw.githubusercontent.com/openai/grade-school-math/HEAD/README.md) (accessed 2026-11-07 )

### Question types

Basic arithmetic word problems of 2 to 8 steps, outputting a solution in natural language and a final numerical value.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Modalities

Text (mathematical symbols expressed as text); not an original image or video recognition task

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Languages

English question text; for formal or mathematical notation, see the modality and the repository format

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Difficulty

A bright middle school student should be able to solve them (the design intent of the authors); this is not the difficulty of higher mathematics or an olympiad.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 公开及隐藏划分

Both train.jsonl and test.jsonl are public; there is also a Socratic format, which cannot be treated as an independent new benchmark.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )


## Evaluation

### Metrics

Accuracy of the final numeric answer; a score in which a verifier chooses among multiple candidates must be labeled separately.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 计分

The official dataset.py extracts the number after ####; the calculator runs through <<...>> annotations, and tools are not inherently prohibited.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 提示与运行设置

The original paper trains a generator and a verifier and compares selection of the best among multiple candidates; best-of-100 is not equal to pass@1.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 评测入口

https://github.com/openai/grade-school-math

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 可比性边界

Single-sample, voting, verifier best-of-N, calculator, and few-shot settings must not be ranked together.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07 )


## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 已核实版本

main data; the repository is marked Archive, and the code is provided as is

Sources: [1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md) (accessed 2026-11-07 )

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2021-10-27；timezone：；- version：v2；submitted_at：2021-11-18；timezone：；2026_h2_evidence：- url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1–4.2 and Tables 2–4 actually report GSM8K. Different years of AIME are filed under the same entry and are not split by year in order to pad the count.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### Saturation

Unverified

Note: Whether it is saturated depends on the specific split, the tools, and the protocol; the scores below are only a snapshot from a limited source and are not a judgment of overall saturation or of SOTA

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07 )

### 已知问题

The repository notes that an old calculator in the example model solutions once failed on about 1% of cases; the code has been fixed, but the examples were not regenerated. This is a historical sample problem, not the current overall label error rate.

Sources: [1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md) (accessed 2026-11-07 )

### 衍生关系

The Socratic format automatically adds sub-questions; the original paper did not experiment with it. This repository does not count it separately.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 ) ; [2](https://github.com/openai/grade-school-math) (accessed 2026-11-07 )


## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 官方结果入口

Unverified

Note: No independent, continuously updated official leaderboard has been confirmed; experiments in the paper are not presented as an official live leaderboard

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 第三方结果入口

Unverified

Note: No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Hunyuan-A13B report, Table 2: base model, 4-shot CoT. | — | Hunyuan-Large-1116 | 92.8 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09 (arXiv identifier month; exact experiment date Unverified) |
| Hunyuan-A13B report, Table 2: base model, 4-shot CoT. | — | Qwen2.5-72B | 91.5 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09 (arXiv identifier month; exact experiment date Unverified) |
| Hunyuan-A13B report, Table 2: base model, 4-shot CoT. | — | Qwen3-A22B | 94.39 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09 (arXiv identifier month; exact experiment date Unverified) |
| Hunyuan-A13B report, Table 2: base model, 4-shot CoT. | — | Hunyuan-A13B | 91.83 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09 (arXiv identifier month; exact experiment date Unverified) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

Not an exhaustive ranking, and not a ranking across protocols. Only the listed rows from sources that were opened are transcribed; a model that is not listed is not thereby shown to rank below the listed models. Results whose dates are unknown remain Unverified, and a display name is not an API checkpoint.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07 )


## Contact

### 公开研究联系邮箱

- karl@openai.com
- vineet@openai.com

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 问题反馈

https://github.com/openai/grade-school-math/issues

Sources: [1](https://github.com/openai/grade-school-math) (accessed 2026-11-07 )

### 官方账号

Unverified

Note: No dedicated official social account has been verified, and personal accounts of the same name are not included

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### 隐私政策

Unverified

Note: A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )


## Original files

### 原文PDF

https://arxiv.org/pdf/2110.14168

Sources: [1](https://arxiv.org/abs/2110.14168) (accessed 2026-11-07 )

### PDF SHA-256

a52417d8fcd006de882e3b404850e2cc4246815828897c18c6ce6c7a448985a4

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/2110.14168) (accessed 2026-11-07 )

### PDF bytes

2935719

Sources: [1](https://arxiv.org/pdf/2110.14168) (accessed 2026-11-07 )

### Folder

id：1C6D6YXK-yBTIxFc1sWyfYFIxKjH54dmb；webViewLink：

Sources: [1]( 2026-11-07 )

### 其他原始材料

chinese_intro_doc：id：1mgSxjZ0tSOCdaQ6bYp18z1g7T9ZZldF9DGBNzoeOnb8；webViewLink：

Sources: [1]( 2026-11-07 )

### PDF

id：1TjNp6myEAC_TGomPvMQItLdxd9AUTS1y；webViewLink：

Sources: [1]( 2026-11-07 )


## Changelog

### 本页修订

- date：2026-11-07；timezone：；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- date：2026-11-07；timezone：；change：深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07 )

