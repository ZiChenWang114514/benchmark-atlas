# miniF2F

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

miniF2F测的是给定形式化定理之后生成可被内核检查的证明，不是自然语言自动形式化，也不是只输出数值答案。原论文明确v1为488题；不同形式系统对同一题的翻译不能重复计作独立样本。阅读成绩时，必须同时看证明器、数学库及搜索预算。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### Short name

miniF2F

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Full name

miniF2F: a cross-system benchmark for formal Olympiad-level mathematics

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Benchmark version

v1 (frozen in August 2021; the official requirement is to report the v1 branch rather than the development main).

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### Paper version

arXiv v2

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Release date

2021-09-01 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Section

Mathematics

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

### Field tags

- Formal mathematical proofs in Lean

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 许可证与权利边界

Licenses follow the system directories: Lean and Isabelle are Apache-2.0, Metamath is MIT, and HOL Light is FreeBSD. All four LICENSE files were opened one by one. This cannot be abbreviated as MIT for the whole repository.

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/lean/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/isabelle/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/metamath/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/hollight/LICENSE)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2109.00110

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Code repository

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

### 数据集入口

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Official homepage

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Paper title

MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

École Polytechnique, OpenAI, and the University of Pittsburgh (paper credits)

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 合作方

Unverified

> Only the institutions named on the paper are confirmed; not every listed affiliation is automatically treated as a formal partner

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Authors

- Zheng, Kunhao
- Han, Jesse Michael
- Polu, Stanislas

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Maintainer

Contributors to the official openai/miniF2F repository; the README welcomes additional formalized problems and proofs, which is not a basis for asserting a frequency of active maintenance.

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### Funders

Unverified

> Paper acknowledgments and current operational funding were not verified item by item; institutional affiliation is not a funding source

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## Design goals

### Abilities measured

Generated proofs are checked with a formal mathematics system, and a shared contest-mathematics evaluation is established across theorem provers.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Design background

Scoring non-formal final answers cannot strictly prove that the reasoning is correct, and the difficulty of problems in older formal libraries does not match contest mathematics.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## Construction

### Question sources

Formalized by hand from AMC, AIME, IMO, MATH, and from high-school and undergraduate mathematics problems, across Lean, Metamath, Isabelle, and HOL Light.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 出题与审阅者背景

Practitioners trained in formalization take part in the human translation, including students who are new to formal systems; the paper does not require all of them to be domain experts.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### Review process

The paper records manual formalization followed by review; formalization averages about 15 minutes per question, and review takes about half that time. Natural-language questions that are hard to formalize faithfully may be discarded, and passing compilation alone cannot be treated as a review of the question’s meaning.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### Quality control

A stratified random split is made by question source and by MATH difficulty so that the types and the difficulties of valid and test are balanced; multiple-choice questions and questions that ask for a witness sometimes write the correct answer into the formal statement, which lowers the difficulty relative to the original question.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 去污染及其证据边界

Public questions and formal statements can enter pretraining; a pass by the kernel still requires a check for whether sorry, axiom, or an overly strong assumption is invoked.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## Data format

### 题量与版本口径

Table 1 of original paper v2 states it clearly: v1 has 488 distinct mathematics questions in total, with 244 for valid and 244 for test; in the current README table, Lean, Metamath, and Isabelle are each 244+244, and HOL Light is 165+165. The phrase “244 statements” in the version section of the README cannot replace the paper's definition of the full question count.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### Question types

A formal theorem statement is given as input, a proof script is generated, and a proof kernel checks it.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Modalities

Formal symbols/code and mathematical text

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Languages

English question text; for formal or mathematical notation, see the modality and the repository format

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Difficulty

Olympiad and high-school/undergraduate mathematics; formal statements sometimes give the answer or a witness, which changes the difficulty relative to the original problem.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### Public and hidden splits

Public valid/test sets of 244 each; during training, test proofs or variants of the same problem must not be mixed in without disclosure.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## Evaluation

### Metrics

Proof success rate under a fixed search budget, pass@N, and similar measures; H2 research additionally uses PAB.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 评分方法

Correctness is decided by the kernel of the formal system; the axioms it depends on and the trusted environment still have to be audited, and successful compilation is not itself a proof that there is no vulnerability.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 运行与提示设置

The MCTS study fixes Lean4.15, Mathlib4.15(commit9837ca9d), and KiminaServer2.0, with 5 seeds; the budget PAB must be kept.

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 官方脚本

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 可比性警示

Differences in Lean3/Lean4, Mathlib version, the tactic set, the number of attempts, and PAB mean that results cannot be compared directly across tables.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

Original v1 cross-system collection; a modern Lean4 port must record its commit separately

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2021-09-01；- **timezone**：；- - **version**：v2；- **submitted_at**：2022-02-28；- **timezone**：
- **2026_h2_evidence**：- - **url**：https://arxiv.org/html/2608.28639v1；- **date**：2026-08-11；- **note**：The original Reward-Oracle MCTS study actually compares three proof models and different search budgets on miniF2F; it also audits the validity of proofs at the kernel level.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### Saturation

The 2026 MCTS study that was checked again reports Goedel at 87.1 ± 0.2% under test 244 and PAB256; this is an experiment under a specified toolchain and a specified budget, and a single degree of saturation for every ported version, or for a higher budget, cannot be derived from it.

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 污染、争议与限制

The sorryAx issue in the H2 MCTS study affects the audit of PutnamBench; the authors state explicitly that the successful miniF2F proofs in this study did not depend on sorryAx, and a flaw in another collection cannot be carried over into a conclusion about miniF2F.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 衍生与版本关系

The Lean4 port and each prover fork should state the source commit; scores from all forks cannot be attributed to one fixed v1 toolchain.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### Official entry

https://github.com/openai/miniF2F

> The original paper states explicitly that there is no formal process for submitting scores; this link is the project entry, not an assumption that an official live leaderboard exists.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 第三方覆盖入口

Unverified

> No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Original paper v2 Table 3 / Metamath / Pass@1

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| GPT-f | 1.3 | Pass@1 / % |

- **GPT-f**：- **scope**：v1 test244; 128 expansions per search; GPT-f uses 16 tactics per expansion, tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### Original paper v2 Table 3 / Metamath / Pass@8

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| GPT-f | 1.6 | Pass@8 / % |

- **GPT-f**：- **scope**：v1 test244; 128 expansions per search; GPT-f uses 16 tactics per expansion, tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### Original paper v2 Table 3 / Lean / Pass@1

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| tidy | 18.0 | Pass@1 / % |
| GPT-f / PACT 700M | 24.6 | Pass@1 / % |

- **tidy**：- **scope**：v1 test244; 128 expansions per search; GPT-f uses 16 tactics per expansion, tidy17
- **GPT-f / PACT 700M**：- **scope**：v1 test244; 128 expansions per search; GPT-f uses 16 tactics per expansion, tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### Original paper v2 Table 3 / Lean / Pass@8

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| GPT-f / PACT 700M | 29.2 | Pass@8 / % |

- **GPT-f / PACT 700M**：- **scope**：v1 test244; 128 expansions per search; GPT-f uses 16 tactics per expansion, tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### Independent research MCTS / miniF2F test244, PAB256, 5 seeds

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Goedel-Prover-V2-8B + MCTS | 87.1 ± 0.2 | 证明成功率 / % |

- **Goedel-Prover-V2-8B + MCTS**：- **scope_and_protocol**：miniF2F test244, PAB256, 5 seeds；- **result_date**：2026-08-11；- **snapshot_date**：2026-11-08；- **source_class**：Research-paper experiments, not an official live leaderboard；- **checkpoint_note**：Model names are kept as in the source; if the source does not list an API checkpoint, one is not invented.

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

#### Independent-research MCTS / same study, PAB32; a different budget from the previous row

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Goedel-Prover-V2-8B + MCTS | 84.2 ± 0.5 | 证明成功率 / % |

- **Goedel-Prover-V2-8B + MCTS**：- **scope_and_protocol**：The same study, PAB32; a different budget from the row above；- **result_date**：2026-08-11；- **snapshot_date**：2026-11-08；- **source_class**：Research-paper experiments, not an official live leaderboard；- **checkpoint_note**：Model names are kept as in the source; if the source does not list an API checkpoint, one is not invented.

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

#### Independent research MCTS / test244, PAB256

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| DeepSeek-Prover-V2-7B + MCTS | 82.6 ± 0.1 | 证明成功率 / % |

- **DeepSeek-Prover-V2-7B + MCTS**：- **scope_and_protocol**：test244，PAB256；- **result_date**：2026-08-11；- **snapshot_date**：2026-11-08；- **source_class**：Research-paper experiments, not an official live leaderboard；- **checkpoint_note**：Model names are kept as in the source; if the source does not list an API checkpoint, one is not invented.

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）


[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 覆盖范围与时效

The historical baselines of the original paper and the experiments in the 2026 MCTS paper are kept on separate tracks; the latter is not an official live leaderboard. Different proof systems, different PAB settings, and different Lean/Mathlib versions cannot be ranked together; the still unknown entry point of an independent third-party leaderboard remains Unverified.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

## Contact

### 公开工作邮箱

- kunhao.zheng@polytechnique.edu
- jessemichaelhan@openai.com

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 公开反馈

https://github.com/openai/miniF2F/issues

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

### 官方社交

Unverified

> No dedicated official social account has been verified, and personal accounts of the same name are not included

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 隐私边界

Unverified

> A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2109.00110

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### PDF SHA-256

e4dcbd37330caffea6ebe2baa0f2f4cd3596d8a873c00f44ea2ce62ab0aaeea2

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### PDF bytes

267937

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### Folder

- **id**：1Z3ygLn9nvmJ7OL77CifV-VTo5oGqwfIa
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- **chinese_intro_doc**：- **id**：1SmDycpie2iIEWiJN5gjyYjX8Uqpogk5wCu4yuuFHLug；- **webViewLink**： **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/minif2f.md

[来源]( 2026-11-07）

### PDF归档

- **id**：1B_2BIieglqoGSpFwqs_vdOHBFMK1e4U8
- **webViewLink**：

[来源]( 2026-11-07）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）
