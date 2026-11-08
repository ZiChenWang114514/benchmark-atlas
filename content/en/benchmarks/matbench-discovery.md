# Matbench Discovery
> Verification: 2026-11-08. Empirically refined; official facts and per-task snapshots have been added, and Unverified items are explicitly retained

Matbench Discovery is concerned with whether machine learning can pre-screen hypothetical crystals effectively and reduce expensive DFT verification, rather than looking only at the error of an energy regression. The current site also evaluates geometry, phonons, molecular dynamics, and diatomic potentials; CPS and discovery F1 are ranked separately, and the full WBM set and the unique-prototype subset cannot share a denominator.

Basis of the overview: [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920) [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

## Basic information

**简称**：Matbench Discovery [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**全称**：Matbench Discovery [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

**版本口径**：An online multi-task evaluation framework; the discovery task locks the WBM and MP v2022.10.28 reference convex hull, and a software-package version cannot replace the data protocol. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**论文修订**：arXiv v3 [S7](https://arxiv.org/abs/2308.14920)

**发布时间**：2023-08-29 07:29:57 (arXiv v1); later published in Nature Machine Intelligence 7, 836–847 (2025). [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**主板块**：材料 [S1](https://arxiv.org/abs/2308.14920)

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

**领域**：材料 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**许可与权利边界**：MIT (the LICENSE file of the GitHub repository janosh/matbench-discovery; it covers only the contents of the repository, and rights in original third-party materials are checked separately) [S8](https://github.com/janosh/matbench-discovery) [S9](https://api.github.com/repos/janosh/matbench-discovery)

**论文**：https://arxiv.org/abs/2308.14920 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**代码入口**：https://github.com/janosh/matbench-discovery [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

**数据入口**：https://matbench-discovery.materialsproject.org/ [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**官网**：https://matbench-discovery.materialsproject.org/ [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**论文标题**：Matbench Discovery -- A framework to evaluate machine learning crystal stability predictions [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

## Origin and maintenance

**发起方**：Author team of the University of Cambridge, Lawrence Berkeley National Laboratory, BAM, and the University of California, Berkeley. [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

**署名与合作**：Author affiliations in the paper: the Department of Physics at Cambridge, LBNL, BAM in Germany, and UC Berkeley. The WBM data were contributed by Hai-Chen Wang, Silvana Botti, and Miguel A. L. Marques. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**作者**：Riebesell, Janosh；Goodall, Rhys E. A.；Benner, Philipp；Chiang, Yuan；Deng, Bowen；Ceder, Gerbrand；Asta, Mark；Lee, Alpha A.；Jain, Anubhav；Persson, Kristin A. [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**维护入口**：The public site and the repository are signed Janosh Riebesell; feedback goes through the official GitHub Issues and Discussions, and an institutional promise of service is not inferred from the signature. [S10](https://github.com/janosh/matbench-discovery) [S11](https://matbench-discovery.materialsproject.org/models)

**资助**：JR received support from the German Studienstiftung, AAL from the Royal Society, and AJ and KAP from the U.S. DOE Office of Science/BES Materials Sciences and Engineering. NERSC resources under DE-AC02-05CH11231 were used. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## Design goals

**衡量能力**：Compares discovery of crystal stability, structure optimization, phonons and thermal conductivity, molecular dynamics, and diatomic potential-energy curves; it brings out the tradeoffs among accuracy, robustness, and computational cost. [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

**设计动机**：Evaluates the practical value of a model as a pre-screener for high-throughput discovery of stable inorganic crystals, rather than comparing energy-regression error alone. [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

## Construction

**题目/样本来源**：Discovery tasks are designed around the thermodynamic stability of crystals; an evaluation convex hull is built from DFT reference energies. [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**构建者背景**：A cross-institution team in physics, materials science, and materials machine learning; it evaluates the DFT stability of hypothetical crystals and learned potentials, and it is not a set of expert-written natural-language exam questions. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**审查流程**：Discovery tasks are designed around the thermodynamic stability of crystals; an evaluation convex hull is built from DFT reference energies. [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**质量控制**：The discovery set uses WBM DFT relaxations and the public initial and final structures; a fixed DFT reference convex hull is adopted, and the unique-prototype setting removes prototypes that coincide with MP and prototypes duplicated inside WBM, so as to avoid counting only structures that were already known. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**去污染与防泄漏**：The paper trains by default on MP v2022.10.28 and tests on WBM. The unique-prototype subset removes overlap with MP and prototype overlap inside WBM. Models are now trained on different material. The training-data column must be kept, and a blanket claim of no leakage cannot be made. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## Data format

**规模**：The official discovery page confirms the complete WBM of 256,963 crystals and 85 elements; the unique-prototype table in the paper has 215,488 materials, of which 32,942 are stable, and the full table contains 42,825 stable materials. The two denominators cannot be used one for the other. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**任务形式**：Predicts the stability of unrelaxed crystals relative to the DFT reference convex hull; there are also tasks for geometry optimization, phonons and thermal conductivity, molecular dynamics, and diatomic potential-energy curves. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**模态**：Numerical physics data on periodic crystal structures, atoms/elements, energy/force/stress, and phonons; not text multiple-choice or image question answering. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**语言**：Natural-language category does not apply: the main objects are structural and numeric physics labels, and the language of the web-page description is not the language of the evaluation questions. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**难度与覆盖**：Training goes from known MP materials to out-of-distribution generalization on WBM hypothetical crystals; classification difficulty concentrates near the reference convex hull, and discovery ability cannot be read directly from regression MAE. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**公开与测试划分**：The paper trains on MP and tests on WBM, rather than using a random five-fold split; WBM initial and relaxed structures, energies, and symmetry references are public. The default unique-prototype discovery subset and the full WBM are evaluated separately. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## Evaluation

**指标**：CPS combines discovery F1 (50%), geometric RMSD (10%), and phonon κ SRME (40%); molecular-dynamics tasks and diatomic tasks are not included in CPS. Discovery uses the Unique Prototypes subset. [S12](https://matbench-discovery.materialsproject.org/)

**评分**：Discovery F1 is the harmonic mean of precision and recall, and DAF is precision divided by the proportion of stable materials in the test set. The stable label is relative to a fixed DFT-MP convex hull; CPS is aggregated separately as discovery F1 50%, geometric RMSD 10%, and phonon κ SRME 40%. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**提示/训练/运行设置**：Not a language-prompt evaluation; predicting the relaxation energy of an unrelaxed structure, or estimating the energy after relaxation with a learned potential, requires the training data, the structure optimizer, and the test subset to be fixed. The current CPS also requires coverage of the other subtasks. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**官方脚本**：https://github.com/janosh/matbench-discovery [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**可比性警示**：The stability convex hull is built from DFT reference energies, not from the model’s predictions; different training data, test coverage, and subtasks cannot be compared as if they were the same. A high rank does not mean an endorsement by the Materials Project. [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

## Current status

**核查日**：2026-11-08 [S6](https://matbench-discovery.materialsproject.org/)

**数据版本与持续使用**：The discovery task uses the WBM/MP reference convex hull; the online framework has been extended to multiple tasks, and the current default is the unique-prototype setting. The date a model was added is not a data version number. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**论文版本与证据历史**：v1 2023-08-29；v2 2024-02-05；v3 2024-12-11。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S7](https://arxiv.org/abs/2308.14920)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The current highest CPS is 0.913, and the highest discovery F1 is 0.935; these still need to be read together with RMSD, κ SRME, and MD and diatomic robustness, and a high composite score cannot be treated as saturation of every simulation setting. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**已知问题与争议**：The current default require forces filter leaves 49 of 58 models qualified. The CPS ranking in the models directory shows 48 models that have a CPS rank. The denominators of the filters differ, and this cannot be treated as an error of collection. The reference convex hull comes strictly from DFT and is not rebuilt from the prediction model. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**版本/衍生关系**：The original paper centers on crystal stability; the current site extends the tasks to geometry, phonons, MD, and diatomic systems, and CPS is another composite ranking. Property prediction in Matbench v0.1 is kept as its own entry. [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## Leaderboard snapshot

**快照日**：2026-11-08 [S11](https://matbench-discovery.materialsproject.org/models)

**官方榜入口**：https://matbench-discovery.materialsproject.org/models [S13](https://matbench-discovery.materialsproject.org/models)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

### Official models / CPS

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | DPA-4.1-Max-OAM-PFT | 0.913 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 2 | Prophet-OAME-MBD | 0.912 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 3 | DPA-4.1-Max-OAM | 0.910 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 4 | TECE-OAM-RRA-1.0 | 0.908 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 5 | EquFlashV2 | 0.907 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |

### Official Discovery / Unique Prototypes / require forces

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | DPA-4.1-Max-OAM-PFT | 0.935 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 2 | DPA-4.1-Max-OAM | 0.933 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 3 | EquiformerV3+DeNS-OAM | 0.931 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 4 | TECE-OAM-RRA-1.0 | 0.929 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 5 | EquFlashV2 | 0.929 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S11](https://matbench-discovery.materialsproject.org/models) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery)

**覆盖与时效**：Public HTTP pages were read successfully in this pass. The top five for CPS and for discovery F1 are kept on separate tracks. RMSD is transcribed at the precision of the models directory, and the three decimal places on the homepage are not treated as exact to four places. Added is the date a result entered the leaderboard, not the run date. The current index update time is not stated. [S11](https://matbench-discovery.materialsproject.org/models) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery)

## Contact

**公开研究邮箱**：janosh.riebesell@gmail.com；kristinpersson@berkeley.edu [S4](https://arxiv.org/pdf/2308.14920)

> A public correspondence email explicitly listed on the paper's first page.

**问题反馈**：https://github.com/janosh/matbench-discovery/issues [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

> The official README recommends https://github.com/janosh/matbench-discovery/discussions for support questions.

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

**隐私口径**：Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected. [S14](urn:benchmark-atlas:constitution:v0.1)

## Original files

**源站PDF**：https://arxiv.org/pdf/2308.14920 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**PDF SHA-256**：6a37da286baaea80b902d6011fcd6e08a090dbec604b3988884baf57b3aed612 [S4](https://arxiv.org/pdf/2308.14920)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：4570226 [S4](https://arxiv.org/pdf/2308.14920)

**原有文件夹**：{"id": "1wBpI0F2UIXMsYTY0Fal14yFkONcE5FwM", "webViewLink": " [S15](

**其他材料**：[{"kind": "Chinese introduction", "id": "1ja6AV0EvEUik-shnO57oNO_n5urry23n_VpJS0sV_Ns", "webViewLink": " [S16](

**原有 PDF**：{"id": "1Zp7e0SyLqACycWpXq8DbQsiczNMjJCfO", "webViewLink": " [S17](

## Changelog

- 2026-11-07，首批官方材料核验、中文改写、；未核实字段显式标记。
- 2026-11-07，：核对Official README、许可、评测与分任务分数；补2026H2使用证据，区分Paper-fixed experiment和实时榜，保留官方标签冲突。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920) [S6](https://matbench-discovery.materialsproject.org/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2308.14920](https://arxiv.org/abs/2308.14920)，访问 2026-11-07
- S2，[https://arxiv.org/pdf/2308.14920](https://arxiv.org/pdf/2308.14920)，访问 2026-11-07
- S3，[https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)，访问 2026-11-07
- S4，[https://arxiv.org/pdf/2308.14920](https://arxiv.org/pdf/2308.14920)，访问 2026-11-08
- S5，[https://matbench-discovery.materialsproject.org/benchmarks/discovery](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，访问 2026-11-08
- S6，[https://matbench-discovery.materialsproject.org/](https://matbench-discovery.materialsproject.org/)，访问 2026-11-08
- S7，[https://arxiv.org/abs/2308.14920](https://arxiv.org/abs/2308.14920)，访问 2026-11-08
- S8，[https://github.com/janosh/matbench-discovery](https://github.com/janosh/matbench-discovery)，访问 2026-11-07
- S9，[https://api.github.com/repos/janosh/matbench-discovery](https://api.github.com/repos/janosh/matbench-discovery)，访问 2026-11-07
- S10，[https://github.com/janosh/matbench-discovery](https://github.com/janosh/matbench-discovery)，访问 2026-11-08
- S11，[https://matbench-discovery.materialsproject.org/models](https://matbench-discovery.materialsproject.org/models)，访问 2026-11-08
- S12，[https://matbench-discovery.materialsproject.org/](https://matbench-discovery.materialsproject.org/)，访问 2026-11-07
- S13，[https://matbench-discovery.materialsproject.org/models](https://matbench-discovery.materialsproject.org/models)，访问 2026-11-07
- S14，[urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1)，访问 2026-11-07
- S15，[，访问 2026-11-07
- S16，[，访问 2026-11-07
- S17，[，访问 2026-11-07
