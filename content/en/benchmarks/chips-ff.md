# CHIPS-FF

> Benchmark Constitution, in-depth verification snapshot 2026-11-07. Unverified is not the same as Not disclosed; the collection date is not the leaderboard update time.

CHIPS-FF is a leaderboard split by materials-simulation workflow and by property. It is not a question bank, and it has no trustworthy unified overall accuracy. It uses JARVIS-DFT references to test structure, elasticity, defects, surfaces, phonons, and computational cost of general machine-learning force fields; the reference data, the optimizer, the handling of failures, and the denominator of each property need to be locked together.

Basis of the reading guide: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07); [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

## Basic information

**简称**：CHIPS-FF

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**全称**：Computational High-Performance Infrastructure for Predictive Simulation-based Force Fields

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**基准版本**：Paper v4 corresponds to the 104-material property suite; the software workflow continues to evolve, and paper v4 cannot be treated as the semantic version of the data.

Sources: [1](https://arxiv.org/pdf/2412.10516) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

**论文版本**：v4; latest paper date 2025-03-19

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**发布日期**：2024-12-13 (date of the first arXiv version; not an inferred date on which the data went online).

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**主板块**：材料

Sources: [1](https://arxiv.org/html/2609.19487v1) (accessed 2026-11-07)

核验说明：The editorial section follows the selection list. It does not mean the benchmark measures only that section.

**领域**：Force field and material properties

Sources: [1](https://arxiv.org/html/2609.19487v1) (accessed 2026-11-07)

**许可与范围**：NIST LICENSE.rst: a work made by an employee of the U.S. federal government in the course of duty is not protected by copyright in the United States; outside the United States a free, non-exclusive license is granted to use, modify, and distribute the work, and the notice and the disclaimer are retained. Third-party models and data each follow their own license.

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/LICENSE.rst) (accessed 2026-11-07)

**论文/技术报告**：https://arxiv.org/abs/2412.10516

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**代码**：https://github.com/usnistgov/chipsff

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

**数据**：https://github.com/usnistgov/chipsff

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**主页**：https://pages.nist.gov/jarvis_leaderboard/Special/CHIPS_FF/

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**论文标题**：CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

## Origin and maintenance

**发起/作者单位**：NIST Material Measurement Laboratory。

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**合作关系**：待核实

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

**作者**：Wines, Daniel；Choudhary, Kamal

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**维护方**：usnistgov/chipsff，Daniel Wines、Kamal Choudhary。

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**资助**：CHIPS Metrology Program (CHIPS for America), National Institute of Standards and Technology (NIST), U.S. Department of Commerce.

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

## Design goals

**测量能力**：Structure relaxation, elasticity, phonons, defects, surfaces, interfaces, and amorphous properties of general ML force fields, together with computational cost.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**针对的不足**：Looking only at energy and force test error is not enough to show the reliability of downstream physical properties of real semiconductor materials.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

## Construction

**材料来源**：JARVIS-DFT references and materials related to semiconductor components, with automated simulation in ASE+JARVIS-Tools.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**出题背景**：NIST researchers in materials computation and machine learning.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**审核**：Convergence of the model, error, and time consumed are checked against the JARVIS-DFT reference properties and the public computation procedure; the paper also compares FrechetCellFilter and ExpCellFilter, and the optimizer changes the results.

Sources: [1](https://arxiv.org/pdf/2412.10516) (accessed 2026-11-07)

**质控**：Compares model convergence, deviation from DFT, and cost, with separate scores for several material properties.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**去污染边界**：uMLFF may have been trained on overlapping materials; an audit of overlap between the model training set and the test structures is required, and OOD cannot be assumed by default.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

## Data format

**规模与统计口径**：The original paper covers 104 materials and 16 MLFFs, plus a force-prediction evaluation on nearly 2,000,000 structures. The H2 workflow covers 104 lattice/elasticity, 49 vacancy, 82 surface, and 15 interface pairs. The official vacancy leaderboard has 48. The protocols differ.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.19487v1) (accessed 2026-11-07); [3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/) (accessed 2026-11-07)

**任务形式**：Relaxation, elastic constants, defects, surfaces, and interfaces, phonons, thermal properties, and molecular dynamics are driven from atomic structures and JSON configuration; this is not text question answering.

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

**模态**：Atomic structures, energies and forces, elastic tensors, phonons, and numerical values for defects and surfaces.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**语言**：Numerical data and Python/ASE; there is no natural-language examination language.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**难度**：Different properties and families of materials have separate difficulties; there is no single total score.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**公开/保留划分**：Public JARVIS references and submitted predictions; the denominator of each property leaderboard may differ, and this is not a unified train/test question-answer set.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.19487v1) (accessed 2026-11-07)

## Evaluation

**指标**：Property-level MAE and related metrics, and the rate and time of convergence; the overview page of the official site says PCC, but the vacancy subpage actually defines MAE.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07); [2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/) (accessed 2026-11-07)

**评分**：MLFF simulation results are compared automatically with JARVIS-DFT; the specific metric must be tied to the property-task page and cannot be written as a single platform-wide metric.

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07); [2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a) (accessed 2026-11-07)

**提示与运行设定**：Not a prompt evaluation; the MLFF checkpoint, the ASE relaxer, the thresholds, the reference unit cell, and the handling of failure must be held fixed.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**脚本/运行入口**：https://github.com/usnistgov/chipsff

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**可比性**：The official site’s 48 vacancy points differ from H2’s 49 points; when the H2 interface reference unit cell does not match, the split-slab protocol is used instead; different reference procedures cannot be compared directly for SOTA.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.19487v1) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**当前版本证据**：The lattice-a task on the current official site uses 104 materials; each property subset has its own denominator, and a software update is not a unified question-set version.

Sources: [1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a) (accessed 2026-11-07)

**修订历史**：arXiv：v1 2024-12-14 04:22:31；v2 2024-12-21 11:49:32；v3 2025-01-15 13:10:22；v4 2025-03-19 12:10:46。

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**饱和**：Convergence errors and defect errors differ greatly from one property to another; there is no single conclusion on saturation.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**争议与局限**：Reference structures, interface baselines, and failure handling affect the error; the overall-page PCC and the subpage MAE conflict in naming, and the specific subpage and property definitions govern.

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.19487v1) (accessed 2026-11-07); [3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/) (accessed 2026-11-07)

**派生/去重**：待核实

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

## Leaderboard snapshot

**快照日**：2026-11-07 (web-page collection date; not equal to the model experiment date)

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**官方榜**：https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a

Sources: [1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a) (accessed 2026-11-07)

**独立评测**：待核实

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### 分轨结果（不合并来源/题集/协议）

**JARVIS / dft_3d_chipsff_a**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | alignn_ff | 0.0111 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 2 | orb-v2 | 0.0154 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 2 | eqV2_31M_omat | 0.0154 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 4 | eqV2_31M_omat_mp_salex | 0.0161 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 5 | eqV2_86M_omat_mp_salex | 0.0164 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 6 | eqV2_153M_omat | 0.0217 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 7 | eqV2_86M_omat | 0.022 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 8 | orb-d3-v2 | 0.025 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 9 | mace | 0.0265 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 9 | mattersim | 0.0265 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 11 | sevennet | 0.0281 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 12 | chgnet | 0.0361 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 13 | mace-mpa | 0.0401 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 14 | matgl-direct | 0.0427 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 15 | matgl | 0.0429 | Lattice a MAE (Å); the column header ACC on the page is in conflict |
| 16 | mace-alexandria | 0.068 | Lattice a MAE (Å); the column header ACC on the page is in conflict |

direction：lower_is_better

Sources: [https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：All 16 configurations on the lattice-a sub-leaderboard are entered and ordered by ascending MAE as given in the description; orb-v2 and eqV2_31M_omat are tied for 2nd. The conflict among the ACC label in the original table, the PCC label on the topic page, and the task MAE label is kept; the format of the submission date 3-11-2025 has not been clarified, and neither the month nor an overall update time is inferred.

Sources: [1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a) (accessed 2026-11-07)

## Contact

**公开研究邮箱**：daniel.wines@nist.gov；kamal.choudhary@nist.gov

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

**Issues**：https://github.com/usnistgov/chipsff/issues

Sources: [1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) (accessed 2026-11-07)

核验说明：The issue-feedback entry of the official public repository; no message was sent.

**公开社区**：待核实

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

**隐私原则**：待核实

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

## Original files

**PDF**：https://arxiv.org/pdf/2412.10516

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

**原件SHA-256**：f92bd2357b20db020e1cb92584f8b8882427ee86133019d91b75ac14c4844102

Sources: [1](https://arxiv.org/pdf/2412.10516) (accessed 2026-11-07)

**PDF字节数**：4721218

Sources: [1](https://arxiv.org/pdf/2412.10516) (accessed 2026-11-07)

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

Sources: [1](https://arxiv.org/abs/2412.10516) (accessed 2026-11-07)

## Changelog

- date：2026-11-07；；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- date：2026-11-07；；change：：核对Official README、许可、评测与分任务分数；补2026H2使用证据，区分Paper-fixed experiment和实时榜，保留官方标签冲突。
- date：2026-11-07；；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
