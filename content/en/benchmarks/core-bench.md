# CORE-Bench

> Benchmark Constitution, in-depth verification snapshot 2026-11-07. Unverified is not the same as Not disclosed; the collection date is not the leaderboard update time.

CORE-Bench requires an Agent to use code and data that the researchers have already published, to reproduce the results, and to answer questions. It does not reimplement the whole study from the description in the paper. 90 papers generate 270 tasks at different difficulties, and Easy, Medium, and Hard within the same paper share the research question; the paper-level split of 45/45, correctness of every question inside a task, and the average of multiple runs are what make a score interpretable.

Basis of the guide: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07); [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

## Basic information

**简称**：CORE-Bench

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

**全称**：Computational Reproducibility Agent Benchmark（CORE-Bench）

Sources: [1](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07)

**基准版本**：Original 90 papers × 3 levels = 270 tasks

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**论文版本**：arXiv v2

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：A paper revision is not the same as a dataset version.

**发布日期**：2024-09-18 02:13:19

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

**主板块**：Agent

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：Benchmark Constitution editorial filing. Only the main section is counted.

**领域**：Agent that reproduces scientific computation results

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**许可与范围**：The official GitHub code and LICENSE, and the HF data card, are all marked MIT; HF mainly provides task metadata rather than the research capsule, and code and data from the papers that the capsule contains are still checked under their own licenses.

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/LICENSE) (accessed 2026-11-07); [2](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md) (accessed 2026-11-07)

**论文/技术报告**：https://arxiv.org/abs/2409.11363

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**代码**：https://github.com/siegelz/core-bench

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

**数据**：https://huggingface.co/datasets/siegelz/core-bench

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07)

**主页**：https://github.com/siegelz/core-bench

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

**论文标题**：CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

## Origin and maintenance

**发起/作者单位**：Princeton University author team

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**合作关系**：待核实

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**作者**：Zachary S. Siegel；Sayash Kapoor；Nitya Nadgir；Benedikt Stroebl；Arvind Narayanan

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**维护方**：siegelz / CORE-Bench project team

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**资助**：Princeton CSML compute; OpenAI researcher access support.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

## Design goals

**测量能力**：Experiments are run again with existing research code and environments, the outputs are read, and questions about the scientific results are answered.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**针对的不足**：Computational reproducibility is both a question of research credibility and a composite agent task that requires tools, a software environment, and interpretation of the results.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

## Construction

**材料来源**：Code capsules for 90 computer-science, social-science, and medicine papers on Code Ocean.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**出题背景**：The Princeton research team manually curated reproducible questions.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**审核**：Each capsule is run manually 3 times to verify that the question is answerable and that the output is stable.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**质控**：Deterministic outputs are exact answers; for non-deterministic numerical values, repeated runs are used to construct a 95% prediction interval.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**去污染边界**：A split at paper level keeps the same paper from appearing in both train and test; evaluation forbids taking a ready-made output from Code Ocean. The test metadata and the method of decryption are public, so leakage into pretraining from public code and papers cannot be ruled out.

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07)

## Data format

**规模与统计口径**：90 papers and 270 tasks (3 difficulty levels per paper); 45 papers for train and 45 for test; 181 unique questions are reused across the difficulty levels, which is not 270 papers.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**任务形式**：Read the research task and question, install dependencies, run Python or R code to reproduce the result, and write question-to-answer key-value pairs into report.json.

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07)

**模态**：Paper/README text；代码；Experimental data/result files

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**语言**：Research code in Python and R; questions and documentation in English.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**难度**：Easy provides the output; Medium provides a Dockerfile+README; Hard has only a README, and execution must be configured by the solver.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**公开/保留划分**：Following the paper, there are 45 train tasks and 45 test tasks. Metadata for the test tasks are released as a GPG file, and the official README gives a public method of decryption. Capsule code and data are downloaded separately by ID from a Princeton server. This is not a permanently private question bank.

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07); [2](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md) (accessed 2026-11-07); [3](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07)

## Evaluation

**指标**：The rate at which every question in a task is correct; reported separately for Easy, Medium, and Hard.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**评分**：A task is passed only when every question within it is correct; numeric values may be checked against official intervals.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**提示与运行设定**：The harness, such as CORE-Agent or AutoGPT, the model snapshot, and the information permissions of the environment must be stated; browsing Code Ocean in order to find outputs is prohibited.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**脚本/运行入口**：Recommended HAL harness: https://github.com/princeton-pli/hal-harness; older version: https://github.com/siegelz/core-bench (no longer actively maintained).

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07)

**可比性**：Different difficulty levels supply different information; the 270 tasks reuse the same papers and the same questions and cannot be read as 270 independent reproductions of scientific research.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

**当前版本证据**：version：Original 270 tasks; the original harness is no longer actively maintained, and the official recommendation is the HAL harness；evidence_2026_h2：url：https://arxiv.org/html/2609.19134v1；date：2026-09-16；note：ScienceIDE §4.1 and its references explicitly cite CORE-Bench and discuss evaluation aimed at reproducing existing research results; this is an H2 academic citation.

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07)

**修订历史**：Submission history From: Zachary Siegel [ view email ] [v1] 2024-09-18 02:13:19 (2,912 KB) [v2] 2026-06-23 07:36:12 (2,906 KB)

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**饱和**：待核实

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**争议与局限**：Nondeterministic experiments, dependency installation, and data downloads can affect reproduction; the paper's Easy result has a textual conflict of 60.00/60.60, which is retained and not corrected.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

**派生/去重**：Easy, Medium, and Hard are levels of information permission within one suite and count as one benchmark; this differs from PaperBench, which rewrites a paper from scratch.

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

## Leaderboard snapshot

**快照日**：2026-11-07

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

**官方榜**：https://agent-evals-leaderboard.hf.space

Sources: [1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07)

核验说明：Specified by the official README; access returned 503, and the score and the leaderboard update date remain Unverified.

**独立评测**：待核实

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

核验说明：Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

### 分轨结果（不合并来源/题集/协议）

**Paper v2 Table 5 / test / Easy**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | CORE-Agent + gpt-4o-2024-05-13 | 60.0 | task pass@1 (%) |
| 2 | CORE-Agent + gpt-4o-mini-2024-07-18 | 44.44 | task pass@1 (%) |
| 3 | AutoGPT + gpt-4o-2024-05-13 | 35.56 | task pass@1 (%) |
| 4 | AutoGPT + gpt-4o-mini-2024-07-18 | 8.89 | task pass@1 (%) |

protocol：CORE-Agent mean of 3 runs; AutoGPT, 1 run

Sources: [https://arxiv.org/pdf/2409.11363](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**Paper v2 Table 5 / test / Medium**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | CORE-Agent + gpt-4o-2024-05-13 | 57.78 | task pass@1 (%) |
| 3 | CORE-Agent + gpt-4o-mini-2024-07-18 | 32.59 | task pass@1 (%) |
| 2 | AutoGPT + gpt-4o-2024-05-13 | 37.78 | task pass@1 (%) |
| 4 | AutoGPT + gpt-4o-mini-2024-07-18 | 2.22 | task pass@1 (%) |

protocol：CORE-Agent mean of 3 runs; AutoGPT, 1 run

Sources: [https://arxiv.org/pdf/2409.11363](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**Paper v2 Table 5 / test / Hard**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | CORE-Agent + gpt-4o-2024-05-13 | 21.48 | task pass@1 (%) |
| 2 | CORE-Agent + gpt-4o-mini-2024-07-18 | 16.3 | task pass@1 (%) |
| 3 | AutoGPT + gpt-4o-2024-05-13 | 6.67 | task pass@1 (%) |
| 4 | AutoGPT + gpt-4o-mini-2024-07-18 | 2.22 | task pass@1 (%) |

protocol：CORE-Agent mean of 3 runs; AutoGPT, 1 run

Sources: [https://arxiv.org/pdf/2409.11363](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：The live HAL link returned 503 this time, and the current overall leaderboard was not obtained; the historical baselines of four configurations by three difficulties in Table 5 of paper v2 are entered in full, correcting an older entry that pointed by mistake to Table 1. The conflict between Easy 60.00 in the main table and 60.60 in the body and the appendix is noted side by side. A single-run Hard test pass@1 of 22.2 in the appendix differs from the three-run average of 21.48, and the two cannot be ranked together.

Sources: [1](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md) (accessed 2026-11-07); [3](https://agent-evals-leaderboard.hf.space) (accessed 2026-11-07)

## Contact

**公开研究邮箱**：zachary@siegel.com；zss@princeton.edu；sayashk@princeton.edu；nn7887@princeton.edu；stroebl@princeton.edu；arvindn@cs.princeton.edu

Sources: [1](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07); [2](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md) (accessed 2026-11-07)

核验说明：The paper publishes zachary@siegel.com, and the HF data card also lists zss@princeton.edu; the difference between the sources is kept, and only public addresses for research contact are listed.

**Issues**：https://github.com/siegelz/core-bench/issues

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07)

核验说明：Public repository feedback entry point; no question was sent.

**公开社区**：待核实

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**隐私原则**：待核实

Sources: [1](https://arxiv.org/abs/2409.11363) (accessed 2026-11-07)

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Original files

**PDF**：https://arxiv.org/pdf/2409.11363

Sources: [1](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07)

核验说明：Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

**原件SHA-256**：1d1fbe8a3cf472fc468495e6a3bcd6b90224ba1eae3dac8d8174f98d666c3d76

Sources: [1](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07)

核验说明：The original bytes downloaded from the source site, neither compressed nor rewritten; the SHA-256 and the byte count were computed from this download.

**PDF字节数**：2885202

Sources: [1](https://arxiv.org/pdf/2409.11363) (accessed 2026-11-07)

核验说明：The original bytes downloaded from the source site, neither compressed nor rewritten; the SHA-256 and the byte count were computed from this download.

Sources: [1](https://github.com/siegelz/core-bench) (accessed 2026-11-07); [2](

核验说明：The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

## Changelog

- date：2026-11-07；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；change：深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。
- date：2026-11-07；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
