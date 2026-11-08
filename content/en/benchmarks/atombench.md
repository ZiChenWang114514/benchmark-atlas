# AtomBench

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

AtomBench

Sources: [1]

### Full name

AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors

Sources: [1]

### 数据/软件版本

Package atombench 0.1.0 (current pyproject.toml); paper v2 and the underlying data-source versions are recorded separately.

Sources: [2][1]

### Paper version

v2; latest paper date 2026-07-07

Sources: [1]

### Release date

2025-10-18 03:07:37 (arXiv v1 first submission; not a presumed date on which the software was listed)

Sources: [1]

### Section

Materials

Sources: [3]

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

### 学科标签

Crystal-structure generation and reconstruction

Sources: [3]

### 许可证与范围

Software: MIT; the underlying data license is to be verified separately.

Sources: [4]

### 论文入口

https://arxiv.org/abs/2510.16165

Sources: [1]

### Paper title

AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors

Sources: [1]

### Code

https://github.com/atomgptlab/atombench

Sources: [4]

### Dataset

https://doi.org/10.6084/m9.figshare.6815699；https://doi.org/10.6084/m9.figshare.31045597

Sources: [5]

Note: The DOI of the underlying data, as explicitly listed under Data Availability in the original paper; kept separate from the address of the software repository.

### Official homepage

https://atomgptlab.github.io/atombench/

Sources: [4][6]

## Origin and maintenance

### 发起团队

The credited team of West Virginia University and Johns Hopkins University.

Sources: [1]

### 署名/合作机构

West Virginia University；Johns Hopkins University

Sources: [5]

Note: Author affiliations in the paper; the author-contributions section states that KC proposed the project, that CC and KC developed it and ran the computation, and that AHR/KC/CC carried out the analysis jointly.

### Authors

Charles Rhys Campbell；Aldo H. Romero；Kamal Choudhary

Sources: [1]

### 维护入口

The official atomgptlab/atombench repository.

Sources: [1]

### 资助与计算资源

ACCESS allocation DMR140031 (Bridges2/Expanse), and NSF 2138259/2138286/2138307/2137603/2138296. Part of WVU Dolly Sods received support from NSF OAC-2117575. West Virginia Higher Education Policy Commission Research Challenge Grant 2022, RCG23-007. AtomGPTLab provided cluster computing support.

Sources: [5]

## Design goals

这是给定条件下重构已知晶体的评测框架，而不是无条件发现超导体的成功率。配方、配方+Tc与全结构latent所含目标信息不同；必须先按条件分组，再比较误差。
Sources: [1][1]

### 测量能力

Reconstruction fidelity given crystal-related information, quantifying lattice and atomic coordinates and the coverage of the match.

Sources: [1]

### 为何需要这个基准

Generators receive unequal conditioning information, so looking only at the RMSD of successfully matched samples conceals failures; the emphasis is on full-sample ccRMSD.

Sources: [1]

## Construction

### 材料来源

Superconductor structure data from JARVIS Supercon-3D and Alexandria DS-A/B.

Sources: [1]

### 命题/编制背景

Researchers in condensed-matter physics, generative models for materials, and computational materials.

Sources: [1]

### Review process

Target structures, train and test splits, and model-condition groups are fixed; reconstruction metrics are computed with a unified structure matcher.

Sources: [1]

### Quality control

The CSV retains the target and predicted CIF/POSCAR, with unified structure matching and continuously corrected error.

Sources: [1]

### 去污染与证据边界

The authors use a hash of the CIF text to check that splits do not overlap and that entries are unique; this is an author report and is not equivalent to a full audit of near-duplicate structures.

Sources: [1]

## Data format

### 规模与分母

JARVIS Supercon-3D has 1,058 structure/Tc pairs; Alexandria DS-A/B has 8,253 pairs; the demonstration study uses four models, two datasets, and an optional Tc condition, for 12 training instances in all.

Sources: [1]

### Question types

Conditional reconstruction of crystals; not unconditional discovery of new crystals from scratch.

Sources: [1]

### 模态与字段

Atomic crystal structures; the CSV contains id, target, and prediction, and the last two columns are POSCAR strings (the paper also describes CIF).

Sources: [4][1]

### Languages

Structural and numeric formats, with Python tools.

Sources: [1]

### 难度定位

Varies with the given conditional information and the target structure; there is no fixed natural-language difficulty banding.

Sources: [1]

### 公开、隐藏与划分

Each dataset uses one fixed 10% test set; models that need a validation set use 80/10/10, and models that do not use 90/10; the seed is fixed at 123; cross-validation is not used.

Sources: [1]

## Evaluation

### Metrics

Lattice-parameter KLD and MAE, the match rate, the mean RMSD of matched structures, and ccRMSD over every test structure (AMD k=100); the RMSD of the matched subset cannot be treated as the error on the full test set.

Sources: [1]

### 评分流程

The structure matcher handles symmetry and tolerance; ccRMSD is defined for every test structure, avoiding a report of only the successes.

Sources: [1]

### 运行与提示

Not a unified LLM prompt; AtomGPT, CDVAE, FlowMM, and MatterGen need to be grouped by the information visible under the given conditions.

Sources: [1]

### 评测实现

https://github.com/atomgptlab/atombench

Sources: [1]

### 不能混比的设置

This is an evaluation of crystal reconstruction, not of de novo generation; CDVAE sees the latent representation of the full structure, while the other models see only the composition, or the composition plus Tc. A score across conditions cannot be attributed to the merit of the architecture.

Sources: [1]

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

Sources: [1]

### 当前发布

Software package 0.1.0; the benchmark in paper v2 uses JARVIS Supercon-3D and Alexandria DS-A/B. An independent semantic version number for the dataset remains Unverified; the version of the software is not used in place of the version of the structural data.

Sources: [2][5]

Status: Unverified (part of this field is still unconfirmed).

### 版本脉络

v1：2025-10-18；v2：2026-07-07；change_boundary：The title and the protocol of v2 emphasize generative crystal reconstruction; ccRMSD is not the single-lattice-parameter RMSE of the old web page.

Sources: [1][5]

### 分数上限与饱和度

The leading model differs by condition and by metric; saturation should not be declared uniformly.

Sources: [1]

### 争议与局限

The current paper, v2, explicitly reconstructs rather than generating de novo; the old site name AtomGenBench and the metrics of the new AtomBench differ. The boundary between versions is kept.

Sources: [1][3]

### 衍生版本

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

Sources: [1]

### Official entry

https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/

Sources: [7]

### 第三方/补充实验

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### Paper v2, Table 2: Alexandria / composition.

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | MatterGen | 0.238 | ccRMSD (Å), lower is better |
| 2 | AtomGPT | 0.5224 | ccRMSD (Å), lower is better |
| 3 | FlowMM | 1.3998 | ccRMSD (Å), lower is better |

- MatterGen：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition；k：100；source_type：Paper-fixed experiment
- AtomGPT：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition；k：100；source_type：Paper-fixed experiment
- FlowMM：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition；k：100；source_type：Paper-fixed experiment

#### Paper v2, Table 2: Alexandria / composition+Tc.

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | MatterGen Tc | 0.244 | ccRMSD (Å), lower is better |
| 2 | AtomGPT Tc | 0.5228 | ccRMSD (Å), lower is better |

- MatterGen Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition+Tc；k：100；source_type：Paper-fixed experiment
- AtomGPT Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition+Tc；k：100；source_type：Paper-fixed experiment

#### Paper v2 Table 2: Alexandria / full-structure latent

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | CDVAE | 1.2218 | ccRMSD (Å), lower is better |

- CDVAE：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：full-structure latent；k：100；source_type：Paper-fixed experiment

#### Paper v2 Table 2: JARVIS / composition

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | MatterGen | 0.4854 | ccRMSD (Å), lower is better |
| 2 | AtomGPT | 0.8262 | ccRMSD (Å), lower is better |
| 3 | FlowMM | 1.5392 | ccRMSD (Å), lower is better |

- MatterGen：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition；k：100；source_type：Paper-fixed experiment
- AtomGPT：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition；k：100；source_type：Paper-fixed experiment
- FlowMM：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition；k：100；source_type：Paper-fixed experiment

#### Paper v2, Table 2: JARVIS / composition+Tc.

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | MatterGen Tc | 0.4988 | ccRMSD (Å), lower is better |
| 2 | AtomGPT Tc | 0.7665 | ccRMSD (Å), lower is better |

- MatterGen Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition+Tc；k：100；source_type：Paper-fixed experiment
- AtomGPT Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition+Tc；k：100；source_type：Paper-fixed experiment

#### Paper v2 Table 2: JARVIS / full-structure latent

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | CDVAE | 1.1555 | ccRMSD (Å), lower is better |

- CDVAE：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：full-structure latent；k：100；source_type：Paper-fixed experiment

#### Legacy alex_supercon_Tc_a on the JARVIS official website: lattice parameter a.

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | cdvae_invatoms | 0.3137 | lattice-a RMSE, lower is better |
| 2 | atomgpt_invatoms | 0.4821 | lattice-a RMSE, lower is better |
| 3 | flowmm_invatoms | 1.003 | lattice-a RMSE, lower is better |

- cdvae_invatoms：source_url：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/；accessed：2026-11-07；submitted_date：2025-10-17 (the source gives only a date)；source_type：A submission leaderboard on the official web page; conditions differ by model, so it is not treated as a contest under strictly matched conditions
- atomgpt_invatoms：source_url：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/；accessed：2026-11-07；submitted_date：2025-10-17 (the source gives only a date)；source_type：A submission leaderboard on the official web page; conditions differ by model, so it is not treated as a contest under strictly matched conditions
- flowmm_invatoms：source_url：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/；accessed：2026-11-07；submitted_date：2025-10-17 (the source gives only a date)；source_type：A submission leaderboard on the official web page; conditions differ by model, so it is not treated as a contest under strictly matched conditions

Sources: [5][7]

### 覆盖边界

In the paper, ccRMSD is tracked separately for two datasets × three conditions. The old official webpage compares only the RMSE of lattice parameter a. The values 0.3137, 0.4821, and 1.003 cannot be mixed into the ccRMSD of the paper. The figure 8253 on the webpage is the total amount of data, and a test denominator is not inferred from it on its own.

Sources: [5][7]

## Contact

### 公开作者工作邮箱

crhysc@gmail.com；alromero@mail.wvu.edu；kchoudh2@jhu.edu

Sources: [1]

### 公开反馈

https://github.com/atomgptlab/atombench/issues

Sources: [4]

Note: The issue-feedback entry of the official public repository; no message was sent.

### 官方账号

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://arxiv.org/pdf/2510.16165

Sources: [1]

### 下载源文件SHA-256

cf0464f374b215992e91190f1bc398d1dbb01af8199cb2fcb7b4fdb0ae39dcf6

Sources: [5]

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

5917762

Sources: [5]

### 既有文件夹

id：1AGppe7PfAY02bOHYn6m1h1RjoUZ2h3ON；webViewLink：

Sources: [1]

### 其他材料

- type：中文介绍；id：1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY；webViewLink：https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit

Sources: [8]

### 既有 PDF链接

id：11zXVL6xA5D2JNgNvaptGg3rlfXdkUOo0；webViewLink：

Sources: [1]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：：核对Official README、许可、评测与分任务分数；补2026H2使用证据，区分Paper-fixed experiment和实时榜，保留官方标签冲突。
- 2026-11-07（ ()）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

Sources: [1]

### 来源索引

[1]: https://arxiv.org/abs/2510.16165 "访问 2026-11-07"
[2]: https://raw.githubusercontent.com/atomgptlab/atombench/main/pyproject.toml "访问 2026-11-07"
[3]: https://arxiv.org/html/2609.19487v1 "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/atomgptlab/atombench/main/README.md "访问 2026-11-07"
[5]: https://arxiv.org/pdf/2510.16165 "访问 2026-11-07"
[6]: https://atomgptlab.github.io/atombench/ "访问 2026-11-07"
[7]: https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/ "访问 2026-11-07"
[8]: https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit "访问 2026-11-07"
