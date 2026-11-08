# LiveCodeBench
> Verification: 2026-11-08. Verified to exist; a research snapshot, with Unverified fields retaining their marks

LiveCodeBench lowers the contamination risk of a static question bank by collecting new contest questions on a rolling basis, and it evaluates generation, self-repair, execution, and test-output prediction separately. Rolling collection does not automatically equal an absence of contamination: the question date window, the model's training-cutoff information, the release, the lite setting of the test set, and the sampling budget must all be fixed together.

Basis of the overview: [S1](https://arxiv.org/abs/2403.07974) [S2](https://livecodebench.github.io/) [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

## Basic information

**简称**：LiveCodeBench [S2](https://livecodebench.github.io/)

**全称**：LiveCodeBench [S2](https://livecodebench.github.io/)

> The official name is retained, and the paper title is not automatically expanded into a full name.

**版本口径**：The README lists releases through release_v6; the default release_latest is a mutable alias, and reproduction must pin release_version and the question date window. [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**论文修订**：arXiv v2 [S7](https://arxiv.org/abs/2403.07974)

**发布时间**：2024-03-13 02:58:04 [S1](https://arxiv.org/abs/2403.07974)

> The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

**主板块**：代码 [S1](https://arxiv.org/abs/2403.07974)

> Benchmark Constitution editorial filing. Only the main section is counted.

**领域**：Rolling programming-contest evaluation [S1](https://arxiv.org/abs/2403.07974)

**许可与权利边界**：The repository code is MIT; the license field of the official HF code_generation_lite card writes only cc and does not specify a Creative Commons version or terms. MIT, or a vague cc label, must not be extended directly into a use license for every original contest question. [S8](https://github.com/LiveCodeBench/LiveCodeBench/blob/main/LICENSE) [S9](https://huggingface.co/datasets/livecodebench/code_generation_lite)

**论文**：https://arxiv.org/abs/2403.07974 [S1](https://arxiv.org/abs/2403.07974)

**代码入口**：https://github.com/LiveCodeBench/LiveCodeBench [S2](https://livecodebench.github.io/)

**数据入口**：https://huggingface.co/datasets/livecodebench/code_generation_lite [S10](https://github.com/LiveCodeBench/LiveCodeBench)

**官网**：https://livecodebench.github.io/ [S2](https://livecodebench.github.io/)

**论文标题**：LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code [S1](https://arxiv.org/abs/2403.07974)

## Origin and maintenance

**发起方**：Author team at UC Berkeley, MIT, and Cornell University (by affiliation) [S1](https://arxiv.org/abs/2403.07974)

**署名与合作**：Author affiliations include UC Berkeley, MIT, and Cornell; academic affiliations of authorship are recorded, and a company that funds SKY Lab is not automatically treated as a partner organization in the writing of questions. [S11](https://arxiv.org/pdf/2403.07974)

**作者**：Jain, Naman；Han, King；Gu, Alex；Li, Wen-Ding；Yan, Fanjia；Zhang, Tianjun；Wang, Sida；Solar-Lezama, Armando；Sen, Koushik；Stoica, Ion [S1](https://arxiv.org/abs/2403.07974)

**维护入口**：LiveCodeBench project team [S1](https://arxiv.org/abs/2403.07974)

**资助**：NSF CCF:1900968, CCF:1908870, and SKY Lab corporate sponsorship and affiliates. Alex Gu received NSF Graduate Research Fellowship 2141064. Armando Solar-Lezama received support from NSF and Intel under CCF:2217064. See the paper's acknowledgments for details. [S11](https://arxiv.org/pdf/2403.07974)

## Design goals

**衡量能力**：Combined ability in code generation, self-repair, code execution, and prediction of test output. [S1](https://arxiv.org/abs/2403.07974)

**设计动机**：A static question bank may be encountered repeatedly in training; generation tasks alone cannot fully evaluate code understanding and repair. [S1](https://arxiv.org/abs/2403.07974)

## Construction

**题目/样本来源**：New problems from the regular contests of LeetCode, AtCoder, and Codeforces are collected on an ongoing basis, and release times are recorded. [S2](https://livecodebench.github.io/)

**构建者背景**：Program-synthesis, software, and machine-learning research teams from three universities; the original problems come from contest platforms. [S2](https://livecodebench.github.io/)

**审查流程**：Questions, tests, and scenarios are organized; the official project accepts GitHub PRs that include generation records and adds them to the leaderboard after review. [S2](https://livecodebench.github.io/)

**质量控制**：ERRATA tracks tests that are wrong and questions that are unsuitable for automatic scoring; code_generation_lite removes tests in order to go faster, and the original set requires --not_fast. The official source notes that a timeout can cause a change of score of less than 0.5 points. [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**去污染与防泄漏**：Questions released after a model's training cutoff may optionally be used to reduce contamination; opaque cutoffs, and further training after the question bank is public, still affect validity. [S2](https://livecodebench.github.io/)

## Data format

**规模**：The README explicitly lists release_v1 400, v2 511, v3 612, v4 713, v5 880, and v6 1,055 questions; v6 covers 2023-05 through 2025-04. The 300+ on the homepage and the 500+ in the paper belong to historical windows and cannot be taken as the current total. [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**任务形式**：Algorithmic program generation, feedback-based repair, program execution, and test-output prediction. [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**模态**：文本；代码 [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**语言**：English contest descriptions; the range of generated code that is supported depends on the scenario or the script. [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**难度与覆盖**：Differences in contest-question difficulty are kept and analyzed as easy / medium / hard; overall saturation cannot be judged from the old easy subset alone. [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**公开与测试划分**：Questions and evaluation tools are released batch by batch; decontamination depends on a time window and is not equivalent to a permanently private question bank. [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

## Evaluation

**指标**：Execution correctness by scenario / pass@k; generation, repair, and output prediction are kept separate. [S1](https://arxiv.org/abs/2403.07974)

**评分**：Generated results are checked against contest tests or known inputs and outputs. [S1](https://arxiv.org/abs/2403.07974)

**提示/训练/运行设置**：The official code-generation example uses n=10 and temperature=0.2; the prompt is set per model; generation computes pass@1/pass@5. release_version, start_date/end_date, and lite or the original test must be fixed. [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**官方脚本**：https://github.com/LiveCodeBench/LiveCodeBench [S2](https://livecodebench.github.io/)

**可比性警示**：The official default web-page window is 2024-08-01 to 2025-05-01 (question dates); the result is recomputed from the public JSON and the page algorithm, and is kept on a separate track from the AA summary, whose window is unknown. release_latest is a mutable alias. Lite or the original test, the sampling parameters, and the window must all be locked. [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

## Current status

**核查日**：2026-11-08 [S12](https://livecodebench.github.io/)

**数据版本与持续使用**：Questions are collected on a rolling basis; the snapshot must be fixed to the evaluation time window；历史持续使用证据：2026-09-23 Hunyuan-A13B §4.1 and §4.2, and Tables 2–4, actually report LiveCodeBench; CRUX-I/O is kept as the same CRUXEval entry and is not counted separately. https://arxiv.org/html/2609.27284v1 [S13](https://arxiv.org/html/2609.27284v1) [S2](https://livecodebench.github.io/)

> Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

**论文版本与证据历史**：v1 2024-03-13；v2 2024-06-07。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S7](https://arxiv.org/abs/2403.07974)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The dynamic window changes the question denominator; the current AA summary reaches at most 91.7%, and the official default window is computed separately. There is no full-set saturation conclusion that can be cited across time windows. [S3](https://livecodebench.github.io/leaderboard.html) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

**已知问题与争议**：“Contamination Free” is a design goal and a title; the scope in which it holds depends on the model cutoff date, the time the questions were released, and later training, and it cannot be guaranteed absolutely. [S2](https://livecodebench.github.io/) [S14](https://artificialanalysis.ai/evaluations/livecodebench)

**版本/衍生关系**：Code generation, self-repair, execution, and test-output prediction are scenarios of the same suite and are not split into four entries. [S2](https://livecodebench.github.io/) [S14](https://artificialanalysis.ai/evaluations/livecodebench)

## Leaderboard snapshot

**快照日**：2026-11-08 [S3](https://livecodebench.github.io/leaderboard.html)

**官方榜入口**：https://livecodebench.github.io/leaderboard.html [S10](https://github.com/LiveCodeBench/LiveCodeBench)

**第三方入口**：https://artificialanalysis.ai/evaluations/livecodebench [S14](https://artificialanalysis.ai/evaluations/livecodebench)

### Default window on the official web page: 2024-08-01–2025-05-01.

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | O4-Mini (High) | 80.2 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 2 | O3 (High) | 75.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 3 | O4-Mini (Medium) | 74.2 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 4 | Gemini-2.5-Pro-06-05 | 73.6 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 5 | DeepSeek-R1-0528 | 73.1 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 6 | Gemini-2.5-Pro-05-06 | 71.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 7 | EXAONE-4.0-32B | 70.0 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 8 | OpenReasoning-Nemotron-32B | 69.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 9 | O3-Mini-2025-01-31 (High) | 67.4 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 10 | OpenCodeReasoning-Nemotron-1.1-32B | 66.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |

### AA current summary; evaluation window Unverified

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Gemini 3 Pro Preview (High) | 91.7 | AA LiveCodeBench score (%) | [来源](https://artificialanalysis.ai/evaluations/livecodebench)，2026-11-08 |
| 2 | Gemini 3 Flash Preview (Reasoning) | 90.8 | AA LiveCodeBench score (%) | [来源](https://artificialanalysis.ai/evaluations/livecodebench)，2026-11-08 |
| 3 | DeepSeek V3.2 Speciale | 89.6 | AA LiveCodeBench score (%) | [来源](https://artificialanalysis.ai/evaluations/livecodebench)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

**覆盖与时效**：The static table on the official web page is only a Loading placeholder. The performances_generation.json that it explicitly cites was read, and the top ten ranked entries were reconstructed strictly by the page's filter-window, mean, and one-decimal-place display rules. Date marks stop at 2025-05-01, and they are not disguised as new 2026 questions. The number of questions covered by each model is listed separately. The AA score window is unknown and is never mixed in. [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

## Contact

**公开研究邮箱**：naman_jain@berkeley.edu [S2](https://livecodebench.github.io/)

**问题反馈**：https://github.com/LiveCodeBench/LiveCodeBench/issues [S2](https://livecodebench.github.io/)

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2403.07974)

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**隐私口径**：待核实 [S1](https://arxiv.org/abs/2403.07974)

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Original files

**源站PDF**：https://arxiv.org/pdf/2403.07974 [S15](https://arxiv.org/pdf/2403.07974)

> Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

**PDF SHA-256**：a9bd3f7b96ac846ac53506e7b58197d9213919f18f402a27910dcf9fc948b427 [S11](https://arxiv.org/pdf/2403.07974)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：4960954 [S11](https://arxiv.org/pdf/2403.07974)

**原有文件夹**：{"id": "1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV", "webViewLink": " [S16](

**其他材料**：[{"type": "Chinese-language introductory Google Doc", "id": "1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s", "webViewLink": " [S2](https://livecodebench.github.io/) [S17](

> The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

**原有 PDF**：{"id": "1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ", "webViewLink": " [S18](

## Changelog

- 2026-11-07，首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- 2026-11-07，深度优化续核：打开Official README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://livecodebench.github.io/) [S12](https://livecodebench.github.io/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)，访问 2026-11-07
- S2，[https://livecodebench.github.io/](https://livecodebench.github.io/)，访问 2026-11-07
- S3，[https://livecodebench.github.io/leaderboard.html](https://livecodebench.github.io/leaderboard.html)，访问 2026-11-08
- S4，[https://livecodebench.github.io/performances_generation.json](https://livecodebench.github.io/performances_generation.json)，访问 2026-11-08
- S5，[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)，访问 2026-11-08
- S6，[https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)，访问 2026-11-07
- S7，[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)，访问 2026-11-08
- S8，[https://github.com/LiveCodeBench/LiveCodeBench/blob/main/LICENSE](https://github.com/LiveCodeBench/LiveCodeBench/blob/main/LICENSE)，访问 2026-11-08
- S9，[https://huggingface.co/datasets/livecodebench/code_generation_lite](https://huggingface.co/datasets/livecodebench/code_generation_lite)，访问 2026-11-08
- S10，[https://github.com/LiveCodeBench/LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench)，访问 2026-11-08
- S11，[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)，访问 2026-11-08
- S12，[https://livecodebench.github.io/](https://livecodebench.github.io/)，访问 2026-11-08
- S13，[https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)，访问 2026-11-07
- S14，[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)，访问 2026-11-07
- S15，[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)，访问 2026-11-07
- S16，[，访问 2026-11-07
- S17，[，访问 2026-11-07
- S18，[，访问 2026-11-07
