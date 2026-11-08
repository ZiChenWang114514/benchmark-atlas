# Matbench
> Verification: 2026-11-08. Empirically refined; official facts and per-task snapshots have been added, and Unverified items are explicitly retained

Matbench v0.1 is 13 supervised-learning tasks on materials properties, not a language-model question-answering set. Comparability rests on the same input type, the same physical units, and a fixed outer five-fold split, rather than some unified percentage scale. In particular, the erroneous label “ROC-AUC” in an old category on the official site must not be treated as a true probability-ranking AUC.

Basis of the overview: [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/) [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

## Basic information

**简称**：Matbench [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**全称**：Matbench [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

**版本口径**：matbench_v0.1 [S3](https://matbench.materialsproject.org/)

**论文修订**：arXiv v2 [S5](https://arxiv.org/abs/2005.00707)

**发布时间**：2020/05/02 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**主板块**：材料 [S1](https://arxiv.org/abs/2005.00707)

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

**领域**：材料 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**许可与权利边界**：Software: MIT (Copyright 2021 Hacking Materials Research Group); the license of each sub-data source is checked separately. [S6](https://raw.githubusercontent.com/materialsproject/matbench/main/LICENSE)

**论文**：https://arxiv.org/abs/2005.00707 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**代码入口**：https://github.com/materialsproject/matbench [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

**数据入口**：https://matbench.materialsproject.org/ [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**官网**：https://matbench.materialsproject.org/ [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**论文标题**：Benchmarking Materials Property Prediction Methods: The Matbench Test Set and Automatminer Reference Algorithm [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

## Origin and maintenance

**发起方**：Author team at Lawrence Berkeley National Laboratory and the University of California, Berkeley [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

**署名与合作**：The authors of the paper are from Lawrence Berkeley National Laboratory and from UC Berkeley; the Materials Project provides hosting of the data and the infrastructure of the project. [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

**作者**：Dunn, Alexander；Wang, Qi；Ganose, Alex；Dopp, Daniel；Jain, Anubhav [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**维护入口**：Materials Project; the site footer states that it is maintained by Alex Dunn of the HackingMaterials Group. [S3](https://matbench.materialsproject.org/)

**资助**：Funding from the Early Career Research Program of the Office of Basic Energy Sciences at the United States Department of Energy; computing support from LBNL and from Lawrencium/NERSC involves DE-AC02-05CH11231 (acknowledgments in the paper). [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

## Design goals

**衡量能力**：Provides standard supervised-learning tasks and repeatable comparisons for property prediction of inorganic solids. [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**设计动机**：Provides standard supervised-learning tasks and repeatable comparisons for property prediction of inorganic solids. [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

## Construction

**题目/样本来源**：Compiles precleaned data from density-functional calculations and experimental sources; the inputs are composition and/or crystal structure. [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**构建者背景**：A research team in materials informatics; AD, QW, and AJ conceived the work, AD/QW/DD/AJ designed the test suite, and AD/QW/AG implemented Automatminer (Author Contributions in the paper). [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

**审查流程**：Compiles precleaned data from density-functional calculations and experimental sources; the inputs are composition and/or crystal structure. [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**质量控制**：Non-physical moduli, a refractive index <1, and clearly anomalous formation energies, among other cases, are filtered by task; experimental compositions are cleared of conflicts and of near-duplicates; feature fitting, hyperparameters, and model selection are carried out only inside the training data of each fold. [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

**去污染与防泄漏**：An outer fixed five-fold split is used, with internal model selection only on the training portion, to prevent test leakage. Random or stratified cross-validation is not extrapolation by chemical system, and it is not a later check for LLM training contamination. [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

## Data format

**规模**：13 supervised-learning tasks; sample counts run from 312 for steels to 132,752 for mp_e_form. Each task stands alone, and the counts are not summed and deduplicated into a single question count. [S3](https://matbench.materialsproject.org/)

**任务形式**：Material structure or chemical composition is the input, and electronic, thermodynamic, mechanical, thermal, and similar properties are predicted; this includes regression and classification. [S3](https://matbench.materialsproject.org/)

**模态**：A chemical-composition string or a pymatgen.Structure crystal structure; the output is a continuous property value or a Boolean classification label, not visual question answering. [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**语言**：Not a natural-language question set: the inputs are chemical composition or crystal structure and numeric labels; a natural-language distribution does not apply. [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**难度与覆盖**：13 tasks span experiment and DFT, composition and structure, and different scales; difficulty is analyzed by task and by sample size, and there is no unified question grade. [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**公开与测试划分**：A fixed outer CV of five folds, each fold using 80% for training plus validation and 20% for testing; KFold for regression and StratifiedKFold for classification, with seed=18012019; the data are public, but at the time of scoring the test labels must not be used for tuning. [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

## Evaluation

**指标**：Regression metrics such as MAE, and classification metrics, are reported by task; the official site has warned that historical ROC-AUC is in fact equal to balanced accuracy. [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**评分**：Regression metrics such as MAE, and classification metrics, are reported by task; the official site has warned that historical ROC-AUC is in fact equal to balanced accuracy. [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**提示/训练/运行设置**：A non-prompt LLM evaluation. Five folds per task and the range of the hyperparameter search must be fixed; in the original paper, Automatminer Express has an internal optimization budget of 24 hours, and the other algorithms each record their own training settings. [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**官方脚本**：matbench.bench.MatbenchBenchmark: task.get_train_and_val_data, task.get_test_data(include_target=False), task.record, and mb.to_file. The official usage page gives the complete per-task, per-fold procedure. [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**可比性警示**：A major official erratum: the old scores that the v0.1 classification leaderboard labeled as ROC-AUC came from predictions thresholded at 0.5 and are in fact equal to balanced accuracy; the old leaderboard has not yet been recomputed. They must not be interpreted as true ROC-AUC. [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

## Current status

**核查日**：2026-11-08 [S8](https://matbench.materialsproject.org/)

**数据版本与持续使用**：v0.1 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**论文版本与证据历史**：v1 2020-05-02；v2 2020-05-08。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S5](https://arxiv.org/abs/2005.00707)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The task metrics are MAE with units, or classification performance, and saturation cannot be judged by one unified percentage; in this reading, the best MAE on each of the official 10 regression tasks is nonzero, which does not prove that the floor of experimental or DFT noise has been reached. [S8](https://matbench.materialsproject.org/)

**已知问题与争议**：The old classification scores are semantically wrong; see official issues #137 and #181. Scoring going forward has been fixed, but the existing leaderboard has not been recomputed. [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

**版本/衍生关系**：The official homepage points the DFT materials-discovery task to Matbench Discovery; the two differ in task goal and in split, so the CPS of the discovery leaderboard is not mixed in as a property-prediction score of Matbench v0.1. [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

## Leaderboard snapshot

**快照日**：2026-11-08 [S8](https://matbench.materialsproject.org/)

**官方榜入口**：https://matbench.materialsproject.org/ [S3](https://matbench.materialsproject.org/)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

### matbench_v0.1 / matbench_steels

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 87.7627 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_jdft2d

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 33.1918 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_phonons

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | MegNet (kgcnn v2.1.0) | 28.7606 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_expt_gap

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 0.3327 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_dielectric

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 0.2711 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_log_gvrh

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | coNGN | 0.0670 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_log_kvrh

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | coNGN | 0.0491 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_perovskites

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | coGN | 0.0269 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_mp_gap

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | coGN | 0.1559 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_mp_e_form

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | coGN | 0.0170 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S8](https://matbench.materialsproject.org/)

**覆盖与时效**：The leading homepage results and units were updated for all 10 regression tasks; dielectric is unitless, perovskites are eV/unit cell, and phonons are now 1,265 samples. The ROC-AUC labels on the old leaderboards for 3 classification tasks are in fact balanced accuracy. They are not mixed into the regression snapshot or interpreted as true ROC-AUC. [S8](https://matbench.materialsproject.org/) [S10](https://matbench.materialsproject.org/Benchmark%20Info/matbench_v0.1/)

## Contact

**公开研究邮箱**：ardunn@lbl.gov；ajain@lbl.gov [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**问题反馈**：https://github.com/materialsproject/matbench/issues [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

> The issue-feedback entry of the official public repository; no message was sent.

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

**隐私口径**：Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected. [S11](urn:benchmark-atlas:constitution:v0.1)

## Original files

**源站PDF**：https://arxiv.org/pdf/2005.00707 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707)

**PDF SHA-256**：fbdd140ca579e28117736df44e99c3bbe0c30464316a3ed46d13a0c5306d344d [S7](https://arxiv.org/pdf/2005.00707)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：2513518 [S7](https://arxiv.org/pdf/2005.00707)

**原有文件夹**：{"id": "1k3jZRqYR__FVaY_MxD5J4xmR-L2BiADe", "webViewLink": " [S12](

**其他材料**：[{"kind": "Chinese introduction", "id": "1NtknnmF6L_ZeGTOBdxqsJpfjOFzow2dvDfhYCTsIBkk", "webViewLink": " [S13](

**原有 PDF**：{"id": "1wRPaSl63GECWDwAqW5_HthOwRislygXV", "webViewLink": " [S14](

## Changelog

- 2026-11-07，首批官方材料核验、中文改写、；未核实字段显式标记。
- 2026-11-07，：核对Official README、许可、评测与分任务分数；补2026H2使用证据，区分Paper-fixed experiment和实时榜，保留官方标签冲突。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2005.00707](https://arxiv.org/abs/2005.00707)，访问 2026-11-07
- S2，[https://arxiv.org/pdf/2005.00707](https://arxiv.org/pdf/2005.00707)，访问 2026-11-07
- S3，[https://matbench.materialsproject.org/](https://matbench.materialsproject.org/)，访问 2026-11-07
- S4，[https://raw.githubusercontent.com/materialsproject/matbench/main/README.md](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)，访问 2026-11-07
- S5，[https://arxiv.org/abs/2005.00707](https://arxiv.org/abs/2005.00707)，访问 2026-11-08
- S6，[https://raw.githubusercontent.com/materialsproject/matbench/main/LICENSE](https://raw.githubusercontent.com/materialsproject/matbench/main/LICENSE)，访问 2026-11-07
- S7，[https://arxiv.org/pdf/2005.00707](https://arxiv.org/pdf/2005.00707)，访问 2026-11-08
- S8，[https://matbench.materialsproject.org/](https://matbench.materialsproject.org/)，访问 2026-11-08
- S9，[https://matbench.materialsproject.org/How%20To%20Use/2run/](https://matbench.materialsproject.org/How%20To%20Use/2run/)，访问 2026-11-08
- S10，[https://matbench.materialsproject.org/Benchmark%20Info/matbench_v0.1/](https://matbench.materialsproject.org/Benchmark%20Info/matbench_v0.1/)，访问 2026-11-08
- S11，[urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1)，访问 2026-11-07
- S12，[，访问 2026-11-07
- S13，[，访问 2026-11-07
- S14，[，访问 2026-11-07
