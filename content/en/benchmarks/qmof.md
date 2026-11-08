# QMOF

> In-depth verification: 2026-11-08. The access date is not the publication date or the experiment run date; unknowns are retained, and "Not disclosed" is not inferred.

QMOF is a DFT quantum-chemistry database of metal-organic frameworks and coordination polymers. It is not a leaderboard whose unified test set can be fixed by a single name. Band-gap prediction is only one of its downstream tasks. MAE must be read together with the database version, the DFT level, the structure split, and the training configuration. The maintainer's v13 table, the NIST fixed task, and the 2026 model paper are three sources on separate tracks, and they cannot be merged into a so-called global SOTA.

Latest review

## Basic information

### Short name

QMOF

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### Full name

Quantum MOF (QMOF) Database

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### Dataset version

The latest entry listed in the official updates.md is Figshare v18 (adding a preliminary QMOF Thermo Database); the version log of the repository is not the same as having verified, on this occasion, every latest release on Figshare.

[1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)（访问 2026-11-07）

### Paper version

Matter 4,1578–1597 (2021); the 20k+ version also cites the 2022 extension paper in npj Computational Materials.

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 发布时间

The official version log: the first release of the data, v1, is dated 2020-10-28; the version date on the ChemRxiv page is 2020-10-29. Formal publication in Matter is in 2021, and 2021 cannot be mistaken for the year in which the database was first released.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/updates.md)（访问 2026-11-08）；[2](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）

### 板块

Materials

> The editorial section follows the selection list. It does not mean the benchmark measures only that section.

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### Subfields

```json
[
 "Metal-organic framework band-gap prediction"
]
```

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### License

Database data are CC BY 4.0; the repository software LICENSE is MIT. The license scopes of data and code are kept distinct.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/LICENSE)（访问 2026-11-08）

### Paper

https://doi.org/10.1016/j.matt.2021.02.015

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 代码

https://github.com/Andrew-S-Rosen/QMOF

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### Dataset

https://doi.org/10.6084/m9.figshare.13147324

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### Official homepage

https://github.com/Andrew-S-Rosen/QMOF

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 论文题名

Machine learning the quantum-chemical properties of metal–organic frameworks for accelerated materials discovery

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

## Origin and maintenance

### Initiators

The QMOF research team of Rosen et al.; authors and affiliations of the original paper are in the ChemRxiv preprint and the formal literature, and the database is maintained over the long term by Andrew-S-Rosen/QMOF.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）；[2](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）

### 合作单位

Unverified

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### Authors

```json
[
 "Andrew S. Rosen"
 "Shaelyn M. Iyer"
 "Debmalya Ray"
 "Zhenpeng Yao"
 "Alán Aspuru-Guzik"
 "Laura Gagliardi"
 "Justin M. Notestein"
 "Randall Q. Snurr"
]
```

[1](https://www.osti.gov/pages/biblio/1774653)（访问 2026-11-07）

### Maintainer

Andrew-S-Rosen/QMOF; the Materials Project MOF Explorer is the entry point for browsing the data.

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### Funders

The ChemRxiv page of the original paper lists the National Defense Science and Engineering Graduate Fellowship and the Nanoporous Materials Genome Center (DE-FG02-17ER16362). OSTI additionally lists NSF and DOE/BES support. The source list is not presented as a share of funding.

[1](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）；[2](https://www.osti.gov/pages/biblio/1774653)（访问 2026-11-08）

## Design goals

### 目标能力

Quantum-chemical properties are predicted from MOF structures. The explicit evaluation task recorded here is band-gap regression on a fixed split, not treatment of the database as a unified agent benchmark.

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 相对既有评测的缺口

Large-scale DFT of MOF electronic structure is costly, so graph-model surrogates are needed for materials screening; different DFT functionals should be evaluated separately.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

## Construction

### 题目与标签来源

Experimental MOF/coordination-polymer structures receive property labels from high-throughput periodic DFT calculations; there are no natural-language propositions.

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 出题/标注背景

A collaboration among researchers in quantum chemistry, MOFs, DFT, and graph neural networks; author institutions in 2022 include Berkeley/LBNL, Northwestern, ORNL, and Minnesota.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### Review process

A unified DFT workflow, together with structural and electronic-state analysis; this is not expert review of examination questions one by one.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### Quality control

v9 uses pymatgen StructureMatcher to remove duplicate structures and corrects 186 EDIFF settings; v12 removes some structures that have incorrect bonding or that are missing hydrogens. This is cleaning that is recorded by version, and it does not mean that the data are free of error.

[1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)（访问 2026-11-07）

### 去污染与隔离

H2 uses a fixed train/val/test split to evaluate prediction error; structural overlap and multi-fidelity leakage need a separate audit. The 2022 multi-fidelity setting allows the same structure with different functionals to cross splits, which differs from structural extrapolation.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

## Data format

### Size

The current official overview states 20,000+ structures; the H2 fixed band-gap task has 16,340 training, 2,042 validation, and 2,042 test. The scale of the first release differs from later database versions and must not be mixed.

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### Question types

Continuous-value regression from structure to band gap; the database also contains other quantum-chemistry properties, but they are not split into separate entries by property.

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### Modalities

Atomic structures of MOFs and coordination polymers, and quantum-chemical properties from periodic DFT; the official FAQ states explicitly that trajectories are not provided.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### Languages

Numerical and structural data; the descriptions are in English, and there is no natural-language examination language.

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）

### Difficulty

Band-gap differences for open-shell transition metals and across functionals are harder; there is no unified label of question difficulty.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 公开/隐藏划分

The data are public; H2 uses a fixed 16340/2042/2042 split, while the 2022 original paper uses a random 80/5/15 split. The two protocols differ.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

## Evaluation

### Metrics

Band-gap MAE, in eV, lower is better; the corresponding DFT level is reported.

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 判分

Computes the mean absolute error between predicted band gaps of the test structures and the DFT reference values.

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 提示/推理设置

This is not an LLM question-answering prompt. Table 2 of the ALIGNN 2.0 paper compares a fixed 16340/2042/2042 split under the JARVIS protocol; 0.202 eV comes from the improved training setting, and the radius ablation is 0.208 eV. They cannot be referred to together as an unchanged base kNN.

[1](https://arxiv.org/pdf/2609.19487)（访问 2026-11-08）

### 官方实现

https://github.com/Andrew-S-Rosen/QMOF

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 可比性边界

QMOF is a database plus a downstream protocol, and there is no global leaderboard fixed uniquely by the database name. The PBE band gap is not the experimental optical band gap; splits by different structures or functionals cannot be ranked together.

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

## Current status

### 核验日

2026-11-08

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）

### 本次版本快照

The repository changelog is listed through v18; v15—v17 each remove one structure, and v18 adds a preliminary thermodynamic database. The release date is Unverified.

[1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)（访问 2026-11-07）

### Paper revisions

Evidence of use in 2026H2: Table 2 of ALIGNN 2.0 (2026-09-16) reports the QMOF band-gap task, with 16,340 for training, 2042 for validation, and 2042 for test. The MAE of ALIGNN 2.0 and the MAE of the original ALIGNN are both 0.202 eV.

[1](https://arxiv.org/abs/2609.19487)（访问 2026-11-07）

### Saturation

No improvement in MAE under the same H2 protocol does not mean that every MOF electronic property is saturated, and it does not prove that structural extrapolation is solved.

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 污染/限制/争议

The QMOF version, the training and test structures, and the DFT functional must be distinguished; the maintainer's v13 comparison and the NIST protocol cannot be assumed to be the same. Download of the original 2021 paper PDF and the Cell/chemistry preprint is still limited by a 403; only the ChemRxiv abstract, the repository, NIST, and 2026 downstream papers were opened again, and another paper is not passed off as the original PDF.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）；[2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）；[4](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）

### 衍生与相关版本

v18 adds a preliminary QMOF Thermo Database; this is an extension of the original database. This collection does not, on that basis, count each property again as an independent benchmark.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/updates.md)（访问 2026-11-08）

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not the experiment run date)

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）

### 官方结果入口

https://github.com/Andrew-S-Rosen/QMOF/blob/main/benchmarks.md

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）

### 第三方入口

https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/

[1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| ALIGNN 2.0 author paper v1 Table 2 / fixed 16340-2042-2042 | — | [ALIGNN 2.0 (improved recipe)](https://arxiv.org/pdf/2609.19487) | 0.202 | bandgap test MAE (eV), lower is better | 2026-09-17 |
| ALIGNN 2.0 author paper v1 Table 2 / fixed 16340-2042-2042 | — | [ALIGNN (pre-2.0)](https://arxiv.org/pdf/2609.19487) | 0.202 | bandgap test MAE (eV), lower is better | 2026-09-17 |
| ALIGNN 2.0 authors paper, supplementary Table S2 / radius ablation. | — | [ALIGNN 2.0 (radius graph)](https://arxiv.org/pdf/2609.19487) | 0.208 | bandgap test MAE (eV), lower is better | 2026-09-17 |
| QMOF maintainer / v13 / 80% training | — | [Mean of Dataset](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.94 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF maintainer / v13 / 80% training | — | [Sine Matrix Eigenspectrum](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.539 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF maintainer / v13 / 80% training | — | [Stoichiometric-45](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.459 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF maintainer / v13 / 80% training | — | [Stoichiometric-120](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.454 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF maintainer / v13 / 80% training | — | [Orbital Field Matrix](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.41 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF maintainer / v13 / 80% training | — | [Average SOAP kernel](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.344 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF maintainer / v13 / 80% training | — | [CGCNN](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.27 | bandgap MAE (eV), lower is better | 未标注 |
| NIST JARVIS / qmof_bandgap / 20424 samples | — | [alignn_model](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/) | 0.2019 | bandgap MAE (eV), lower is better | 01-14-2023 |
| NIST JARVIS / qmof_bandgap / 20424 samples | — | [matminer_rf](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/) | 0.3618 | bandgap MAE (eV), lower is better | 05-22-2023 |
| NIST JARVIS / qmof_bandgap / 20424 samples | — | [matminer_xgboost](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/) | 0.3421 | bandgap MAE (eV), lower is better | 05-22-2023 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://arxiv.org/pdf/2609.19487)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）；[3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）

### 覆盖与限制

Three independent protocols: 7 rows for the maintainer's v13/80% training; all 3 rows of NIST JARVIS qmof_bandgap (MAE exactly 0.2019, 0.3618, and 0.3421); and 3 rows from the main table and the ablation in the 2026 ALIGNN 2.0 paper. Although the column name on the NIST page is ACC, the description states clearly that it is band-gap MAE, and lower is better. Different versions, splits, and reporting precision are not mixed. 0.2019 must not be rewritten backward as the paper's 0.202.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）；[2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）；[3](https://arxiv.org/pdf/2609.19487)（访问 2026-11-08）

## Contact

### 项目公开邮箱

```json
[
 "rosen@u.northwestern.edu"
]
```

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### GitHub反馈

https://github.com/Andrew-S-Rosen/QMOF/issues

> The issue-feedback entry of the official public repository; no message was sent.

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### 官方社交

Unverified

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 隐私边界

Only research contact methods and Issues explicitly disclosed in official project materials are recorded; private information is not collected or inferred.

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08）

## Original files

### 原始PDF

Unverified

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### SHA-256

Unverified

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### PDF bytes

Unverified

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### Paper PDF

Unverified

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

## Changelog

[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）
