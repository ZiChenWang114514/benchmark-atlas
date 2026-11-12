# CRUXEval

> Benchmark Constitution, in-depth verification snapshot 2026-11-07. Unverified is not the same as Not disclosed; the collection date is not the leaderboard update time.

CRUXEval uses 800 short Python functions and the input-output pairs produced by actually running them, and it tests inference of the input and prediction of the output separately. Input and output share the samples and should not be assembled into two independent question banks; direct, CoT, pass@1, and pass@5 each mean something different. It is verified explicitly here that the HF data themselves are also MIT, and the static leaderboard is divided into eight protocol tracks.

Basis for this reading: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07); [1](https://crux-eval.github.io/) (accessed 2026-11-07)

## Basic information

**简称**：CRUXEval

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**全称**：Code Reasoning, Understanding, and eXecution Evaluation（CRUXEval）

Sources: [1](https://huggingface.co/datasets/cruxeval-org/cruxeval/raw/main/README.md) (accessed 2026-11-07)

**基准版本**：The original 800 functions; CRUXEval-I / CRUXEval-O in both directions

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**论文版本**：arXiv v1

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：A paper revision is not the same as a dataset version.

**发布日期**：2024-01-06 05:53:51

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

**主板块**：代码

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：Benchmark Constitution editorial filing. Only the main section is counted.

**领域**：Code input-output inference

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**许可与范围**：MIT: both the GitHub LICENSE and the official HF dataset card state it explicitly; the data license is therefore no longer inferred only from the code license.

Sources: [1](https://raw.githubusercontent.com/facebookresearch/cruxeval/main/LICENSE) (accessed 2026-11-07); [2](https://huggingface.co/datasets/cruxeval-org/cruxeval/raw/main/README.md) (accessed 2026-11-07)

**论文/技术报告**：https://arxiv.org/abs/2401.03065

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**代码**：https://github.com/facebookresearch/cruxeval

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**数据**：https://huggingface.co/datasets/cruxeval-org/cruxeval

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**主页**：https://crux-eval.github.io/

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**论文标题**：CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

## Origin and maintenance

**发起/作者单位**：Author team at MIT and Meta AI (by author affiliation)

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**合作关系**：The paper affiliations are MIT CSAIL and Meta AI; the first author states that the main work was completed during an internship at Meta AI. Recorded by research participation, without inferring a legal collaboration agreement.

Sources: [1](https://arxiv.org/pdf/2401.03065) (accessed 2026-11-07)

**作者**：Gu, Alex；Rozière, Baptiste；Leather, Hugh；Solar-Lezama, Armando；Synnaeve, Gabriel；Wang, Sida I.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**维护方**：facebookresearch/cruxeval is currently marked archived (verified on 2026-11-07); the historical maintainer is the CRUXEval team, and continued active maintenance cannot be inferred.

Sources: [1](https://github.com/facebookresearch/cruxeval) (accessed 2026-11-07)

**资助**：A. Gu received NSF Graduate Research Fellowship Grant 2141064; A. Solar-Lezama received support from the NSF and from Intel Corporation through NSF CCF:2217064 (acknowledgments in the paper).

Sources: [1](https://arxiv.org/pdf/2401.03065) (accessed 2026-11-07)

## Design goals

**测量能力**：Code understanding, backward inference of inputs, and output prediction, especially simulating program execution when the code is not run.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**针对的不足**：The success rate of generated code cannot by itself reveal whether the model understands the execution semantics of simple programs.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

## Construction

**材料来源**：CodeLlama-34B is used to generate candidate Python functions and inputs and outputs; after filtering, 800 are drawn at random.

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**出题背景**：MIT / Meta AI researchers; candidate programs are synthesized by a model.

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**审核**：Selects short functions and valid inputs and outputs that a programmer can compute mentally in about one minute.

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**质控**：Program complexity is limited and paired inputs and outputs are executed for verification; the two directions share programs and cannot be counted as two independent question banks.

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**去污染边界**：Synthesizing new programs is intended to reduce reuse of existing human-written problems, but it does not constitute proof of no contamination for every subsequent model.

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

## Data format

**规模与统计口径**：800 samples of Python functions, inputs, and outputs; predicting the input and predicting the output are two evaluations of the same data.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**任务形式**：CRUXEval-I: given a program and an output, find a feasible input. CRUXEval-O: given a program and an input, find the output.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**模态**：代码；文本

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**语言**：Python; English prompts.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**难度**：A short program that a human can calculate mentally may still be hard for a model; this is not the same as software-development difficulty.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**公开/保留划分**：The raw data, the scripts, and the prompts are public; a hidden set is not claimed from that fact.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

## Evaluation

**指标**：pass@1 / pass@5 and others are reported separately by direction; CoT and direct answering are kept separate.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**评分**：Output prediction checks the actual output of the program; input prediction accepts a valid input that, when executed, produces the target output.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**提示与运行设定**：The paper reports direct answering and chain-of-thought separately; the prompt, the number of samples, and whether an execution tool is used must be stated.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**脚本/运行入口**：https://github.com/facebookresearch/cruxeval

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**可比性**：CRUX-I / CRUX-O scores are not averaged and then presented as a single official total; a prompt that asks for an explanation is not ranked together with direct prediction.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**当前版本证据**：version：The original 800 functions; CRUXEval-I / CRUXEval-O in both directions；evidence_2026_h2：url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1 and §4.2, and Tables 2–4, actually report CRUXEval; CRUX-I/O is kept as the same CRUXEval entry and is not counted separately.

Sources: [1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07); [2](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

**修订历史**：Submission history From: Alex Gu [ view email ] [v1] 2024-01-06 05:53:51 (1,309 KB)

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

**饱和**：待核实

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**争议与局限**：The references in the Hunyuan report associate CRUXEval with Liu 2023 (EvalPlus); this entry identifies the original benchmark from Gu et al. 2401.03065.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07)

**派生/去重**：CRUXEval-I and CRUXEval-O are two subtasks of the same benchmark.

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07)

## Leaderboard snapshot

**快照日**：2026-11-07

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

**官方榜**：https://crux-eval.github.io/leaderboard.html

Sources: [1](https://crux-eval.github.io/leaderboard.html) (accessed 2026-11-07)

**独立评测**：待核实

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

核验说明：Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

### 分轨结果（不合并来源/题集/协议）

**CRUXEval official CSV / direct / i@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613 | 69.8 | i@1 (%) |
| 2 | gpt-4-turbo-2024-04-09 (n=3) | 68.5 | i@1 (%) |
| 3 | gpt-4o (n=3) | 65.1 | i@1 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / direct / i@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613 | 76.8 | i@5 (%) |
| 2 | codetulu-2-34b | 68.0 | i@5 (%) |
| 3 | starcoder2-15b | 66.9 | i@5 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / direct / o@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4o (n=3) | 70.0 | o@1 (%) |
| 2 | gpt-4-0613 | 68.7 | o@1 (%) |
| 3 | gpt-4-turbo-2024-04-09 (n=3) | 67.7 | o@1 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / direct / o@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613 | 73.0 | o@5 (%) |
| 2 | deepseek-instruct-33b | 61.8 | o@5 (%) |
| 3 | deepseek-base-33b | 61.6 | o@5 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / i@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-turbo-2024-04-09+cot (n=3) | 75.7 | i@1 (%) |
| 2 | gpt-4o+cot (n=3) | 75.6 | i@1 (%) |
| 3 | gpt-4-0613+cot | 75.5 | i@1 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / i@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613+cot | 88.9 | i@5 (%) |
| 2 | gpt-3.5-turbo-0613+cot | 74.9 | i@5 (%) |
| 3 | codellama-34b+cot | 73.8 | i@5 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / o@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-turbo-2024-04-09+cot (n=3) | 82.0 | o@1 (%) |
| 1 | claude-3-opus+cot (n=1) | 82.0 | o@1 (%) |
| 3 | gpt-4-0613+cot | 77.1 | o@1 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / o@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613+cot | 88.2 | o@5 (%) |
| 2 | gpt-3.5-turbo-0613+cot | 76.7 | o@5 (%) |
| 3 | codellama-34b+cot | 69.4 | o@5 (%) |

Sources: [https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：The official data.csv was reread directly (43 configurations). The top three are listed on each of 8 tracks: direct/CoT, I/O, and pass@1/pass@5. Two rows whose model names explicitly say under verification are removed, and n for the configuration is retained. Ties use competition rank. This is a static leaderboard snapshot, not the 2026 global SOTA. This snapshot does not mix old vendor self-reports into the official ranking.

Sources: [1](https://crux-eval.github.io/data.csv) (accessed 2026-11-07)

## Contact

**公开研究邮箱**：gua@mit.edu；broz@meta.com；hleather@meta.com；asolar@csail.mit.edu；gab@meta.com；sida@meta.com

Sources: [1](https://arxiv.org/pdf/2401.03065) (accessed 2026-11-07)

**Issues**：https://github.com/facebookresearch/cruxeval/issues

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07)

核验说明：Public repository feedback entry point; no question was sent.

**公开社区**：待核实

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**隐私原则**：待核实

Sources: [1](https://arxiv.org/abs/2401.03065) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Original files

**PDF**：https://arxiv.org/pdf/2401.03065

Sources: [1](https://arxiv.org/pdf/2401.03065) (accessed 2026-11-07)

核验说明：Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

**原件SHA-256**：1a356948d0d2543ab7b142029f208271a2581575cee4f5b37eb647cbbf0b435e

Sources: [1](https://arxiv.org/pdf/2401.03065) (accessed 2026-11-07)

核验说明：The original bytes downloaded from the source site, neither compressed nor rewritten; the SHA-256 and the byte count were computed from this download.

**PDF字节数**：2012215

Sources: [1](https://arxiv.org/pdf/2401.03065) (accessed 2026-11-07)

核验说明：The original bytes downloaded from the source site, neither compressed nor rewritten; the SHA-256 and the byte count were computed from this download.

Sources: [1](https://crux-eval.github.io/) (accessed 2026-11-07); [2](

核验说明：The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

## Changelog

- date：2026-11-07；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；change：深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- date：2026-11-07；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
