# MoleculeNet

> Verification date: 2026-11-08. Unknowns are not filled in; the date on which the source was accessed is not the experiment run date.

MoleculeNet is not a natural-language question bank. It is a supervised-learning evaluation collection that unifies data, feature representations, splits, and metrics for molecular property prediction. The core of the original paper is 17 datasets, with both classification and regression. MoleculeNet as currently maintained by the DeepChem community has expanded to a broader range of scientific data. The official README scores newly restored come from historical submissions in 2020–2021. They are shown only by subtask, and the old leaderboard, which can still be accessed, is not called a 2026 SOTA.
[Guide basis for this page](https://deepchem.io/tutorials/an-introduction-to-moleculenet/) (accessed 2026-11-08)

[Supplementary guide basis](https://github.com/deepchem/moleculenet/blob/master/README.md) (accessed 2026-11-08)

## Basic information

### Short name

MoleculeNet

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Full name

MoleculeNet

> The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 数据/基准版本

Unverified

> 状态：待核实。

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Paper version

arXiv v3

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Release date

2017-03-02 09:39:53 （arXiv v1）

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）

### Section

Chemistry

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）

### Subfields

化学；生物与医学

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 许可边界

The DeepChem code is MIT (Copyright 2017 PandeLab). MoleculeNet brings together independent upstream datasets. The code license cannot be extended into one data license for all 17 subsets. A complete list of the authorizations for each dataset is Unverified.

> 状态：待核实。

[来源1](https://github.com/deepchem/deepchem/blob/master/LICENSE)（访问 2026-11-08）；[来源2](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/1703.00564

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 代码入口

https://github.com/deepchem/deepchem

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

### Dataset

https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html (each sub-dataset is obtained through the dc.molnet.load_* interface; this is not a unified HF question bank)

[来源1](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）；[来源2](https://deepchem.io/tutorials/an-introduction-to-moleculenet/)（访问 2026-11-08）

### Official homepage

https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html

[来源1](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

### Paper title

MoleculeNet: A Benchmark for Molecular Machine Learning

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

## Origin and maintenance

### Initiators

Author team at Stanford University and Schrödinger

> Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Partner organizations

Unverified

> 状态：待核实。

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Authors

Wu, Zhenqin；Ramsundar, Bharath；Feinberg, Evan N.；Gomes, Joseph；Geniesse, Caleb；Pappu, Aneesh S.；Leswing, Karl；Pande, Vijay

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Current maintainer

The DeepChem developer community maintains the MoleculeNet loaders; the current official tutorial explicitly says that datasets continue to be added, so the eight authors of the original paper cannot be treated as the only current maintainers.

[来源1](https://deepchem.io/tutorials/an-introduction-to-moleculenet/)（访问 2026-11-08）

### Funders

Acknowledgments in the paper: the Pande Group received support from NIH R01 GM062868, U19 AI109662, and donations to Folding@home. Anders G. Frøseth and Christian Sundt supported the machine-learning work. Bharath Ramsundar was supported by the Fannie and John Hertz Foundation. Stanford Computing Resources provided Sherlock/Xstream GPU nodes.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

## Design goals

### Abilities measured

Unify the data, feature representations, splits, and evaluation methods of molecular machine learning, so that different studies do not use incompatible settings.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 设计动机

Unify the data, feature representations, splits, and evaluation methods of molecular machine learning, so that different studies do not use incompatible settings.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

## Construction

### Question sources

Brings together multiple public molecular databases, covering four major categories: quantum mechanics, physical chemistry, biophysics, and physiology.

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

### 出题/构建者背景

The authors are from the Department of Chemistry, the Department of Computer Science, and the Biophysics Program of the School of Medicine at Stanford, and from Schrödinger Inc.; this is a molecular machine-learning and chemistry research team, not a group that writes multiple-choice questions for textbooks.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Review process

Multiple public molecular datasets are organized, and featurization, learning algorithms, and splitting mechanisms are integrated into DeepChem.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Quality control

Data loading, feature representation, and subset splits are unified, and a metric is assigned to each task; PCBA and MUV use PRC-AUC for severe class imbalance, and ROC-AUC cannot be substituted. Different datasets may have missing task labels, invalid structures, or different results from loader filtering, and reproduction must pin the loader and the cache.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）；[来源2](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

### 去污染/泄漏控制

The original paper uses a scaffold split to test generalization to structures that have not been seen, a temporal split for PDBbind, and a random split for several other tasks; these are controls on leakage in the data of supervised learning, and they are not the same as decontamination of the training corpus of an LLM. A dedicated audit of contamination aimed at LLMs is Unverified.

> 状态：待核实。

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

## Data format

### 精确规模与统计口径

```json
{
 "scope": "Original paper v3 Table 1; 17 datasets; compounds may overlap across datasets, and the rows are not added together as a unique molecule count"
 "datasets": [
 {
 "dataset": "QM7"
 "compounds": 7160
 "tasks": 1
 "recommended_split": "stratified"
 "metric": "MAE"
 }
 {
 "dataset": "QM7b"
 "compounds": 7210
 "tasks": 14
 "recommended_split": "random"
 "metric": "MAE"
 }
 {
 "dataset": "QM8"
 "compounds": 21786
 "tasks": 12
 "recommended_split": "random"
 "metric": "MAE"
 }
 {
 "dataset": "QM9"
 "compounds": 133885
 "tasks": 12
 "recommended_split": "random"
 "metric": "MAE"
 }
 {
 "dataset": "ESOL"
 "compounds": 1128
 "tasks": 1
 "recommended_split": "random"
 "metric": "RMSE"
 }
 {
 "dataset": "FreeSolv"
 "compounds": 642
 "tasks": 1
 "recommended_split": "random"
 "metric": "RMSE"
 }
 {
 "dataset": "Lipophilicity"
 "compounds": 4200
 "tasks": 1
 "recommended_split": "random"
 "metric": "RMSE"
 }
 {
 "dataset": "PCBA"
 "compounds": 437929
 "tasks": 128
 "recommended_split": "random"
 "metric": "PRC-AUC"
 }
 {
 "dataset": "MUV"
 "compounds": 93087
 "tasks": 17
 "recommended_split": "random"
 "metric": "PRC-AUC"
 }
 {
 "dataset": "HIV"
 "compounds": 41127
 "tasks": 1
 "recommended_split": "scaffold"
 "metric": "ROC-AUC"
 }
 {
 "dataset": "PDBbind"
 "compounds": 11908
 "tasks": 1
 "recommended_split": "time"
 "metric": "RMSE"
 }
 {
 "dataset": "BACE"
 "compounds": 1513
 "tasks": 1
 "recommended_split": "scaffold"
 "metric": "ROC-AUC"
 }
 {
 "dataset": "BBBP"
 "compounds": 2039
 "tasks": 1
 "recommended_split": "scaffold"
 "metric": "ROC-AUC"
 }
 {
 "dataset": "Tox21"
 "compounds": 7831
 "tasks": 12
 "recommended_split": "random"
 "metric": "ROC-AUC"
 }
 {
 "dataset": "ToxCast"
 "compounds": 8575
 "tasks": 617
 "recommended_split": "random"
 "metric": "ROC-AUC"
 }
 {
 "dataset": "SIDER"
 "compounds": 1427
 "tasks": 27
 "recommended_split": "random"
 "metric": "ROC-AUC"
 }
 {
 "dataset": "ClinTox"
 "compounds": 1478
 "tasks": 2
 "recommended_split": "random"
 "metric": "ROC-AUC"
 }
 ]
 "current_scope": "The current MoleculeNet has been expanded into a broader scientific data collection; the current full set of loaders cannot be equated with the 17 subsets in the original paper."
}
```

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）；[来源2](https://deepchem.io/tutorials/an-introduction-to-moleculenet/)（访问 2026-11-08）

### Question types

Molecular-property classification and regression.

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

### Modalities

Molecular SMILES; some datasets also contain three-dimensional coordinates.

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

### 语言/代码语种

The objects are SMILES, molecular graphs, three-dimensional coordinates, and numerical labels, and they are not divided by natural language; this is not an English/Chinese question bank.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）；[来源2](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

### 难度结构

Distinguished by the hard points of the task, not by a label of question difficulty: small samples, highly imbalanced classes, quantum properties, and protein-ligand relations; the original paper does not give one difficulty total that applies to every dataset.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Public and hidden splits

The original paper uses an 80/10/10 train/validation/test split and, for different tasks, random, scaffold, or temporal splits; it is not one unified hidden test set.

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

## Evaluation

### Metrics

Classification uses ROC-AUC or PRC-AUC by task; regression uses an error metric by task, for example RMSE on PDBbind.

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

### 评分规则

Predictive performance is compared separately for each sub-dataset and specified split; different splits and metrics must not be combined into one total score.

[来源1](https://arxiv.org/html/1703.00564)（访问 2026-11-07）

### 运行与提示设置

The original protocol is supervised training, validation, and test, and zero-shot and few-shot prompt templates do not apply; the featurizer, the splitter, the seed, and the data version must be fixed. The official benchmark.py defaults to seed=123, and test defaults to False, so -t is required before test is evaluated.

[来源1](https://github.com/deepchem/deepchem/blob/master/examples/benchmark.py)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### Official evaluation scripts

https://github.com/deepchem/deepchem/blob/master/examples/benchmark.py

[来源1](https://github.com/deepchem/deepchem/blob/master/examples/benchmark.py)（访问 2026-11-08）

### 可比性警示

Random splits, scaffold splits, and temporal splits, subset versions, cleaning procedures, and error and AUC metrics cannot be mixed. The historical leaderboard in the official DeepChem README includes submissions from 2020–2021. That it can still be read does not make it the 2026 SOTA; the random-split result in the original ESOL paper and the current default settings of the loader should also not be assumed to agree.

[来源1](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）；[来源3](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

## Current status

### Date checked

2026-11-08

> Access date of the source site for this visit; not the leaderboard run date.

[来源1](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

### 最新数据状态与使用证据

Unverified

> 状态：待核实。

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
 "revisions": [
 {
 "version": "v1"
 "date": "2017-03-02"
 }
 {
 "version": "v2"
 "date": "2017-10-11"
 }
 {
 "version": "v3"
 "date": "2018-10-26"
 }
 ]
}
```

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）

### 饱和性证据

Unverified

> 状态：待核实。

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 污染与已知争议

Public training, validation, and test splits are not a mechanism of hidden examination questions; a random split can be relatively easy, while a scaffold split and temporal extrapolation make different demands. The error bars, the featurization, and the submission times in the official per-leaderboard README should be retained, and an average “overall leaderboard” across the 17 sets cannot be constructed.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）；[来源2](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）

### 衍生与条目关系

Current DeepChem MoleculeNet has been extended to a wider range of scientific data, including materials and others; the 17 molecular-property datasets in the original paper are the historical core; a later extension loader is not a new version, on the same questions, of the original 17 sets.

[来源1](https://deepchem.io/tutorials/an-introduction-to-moleculenet/)（访问 2026-11-08）；[来源2](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）

## Leaderboard snapshot

### 本次榜单采集日

2026-11-08

[来源1](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）

### 官方榜源

https://github.com/deepchem/moleculenet

[来源1](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）

### 第三方覆盖

Unverified

> 状态：待核实。

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### DeepChem official historical README / Delaney (ESOL)

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | GCN | 0.8851 ± 0.0292 | test RMSE | Jan 28th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | Random Forest | 1.7406 ± 0.0261 | test RMSE | Jan 28th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / Lipo

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | GCN | 0.7806 ± 0.0404 | test RMSE | Feb 13th, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | Random Forest | 0.9621 ± 0.0030 | test RMSE | Feb 13th, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / BACE Classification

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Random Forest | 0.8507 ± 0.0072 | test ROC-AUC | Dec 2nd, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | GCN | 0.8175 ± 0.0193 | test ROC-AUC | Dec 20th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / BACE Regression

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Random Forest | 1.3178 ± 0.0081 | test RMSE | Dec 26th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | GCN | 1.645 ± 0.1325 | test RMSE | Dec 26th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / PDBbind (core).

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | ACNN | 1.8604 ± 0.0540 | test RMSE | March 24, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / BBBP

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Random Forest | 0.7194 ± 0.0068 | test ROC-AUC | Dec 30th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | GCN | 0.676 ± 0.0195 | test ROC-AUC | Dec 30th, 2020 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / ClinTox

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | GCN | 0.9065 ± 0.0179 | test ROC-AUC | Jan 22nd, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | Random Forest | 0.7829 ± 0.0235 | test ROC-AUC | Jan 22nd, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / SIDER

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Random Forest | 0.6504 ± 0.0011 | test ROC-AUC | Feb 10th, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | GCN | 0.6265 ± 0.0076 | test ROC-AUC | Feb 10th, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

#### DeepChem official historical README / HOPV

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Random Forest | 3.7283 ± 0.0219 | test RMSE | Feb 4th, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |
| 2 | GCN | 5.4312 ± 2.4279 | test RMSE | Feb 4th, 2021 | [原始来源](https://github.com/deepchem/moleculenet/blob/master/README.md)（2026-11-08） |

- The original README does not list split and seed item by item; the cited code must still be checked before reproduction.

- A historical leaderboard of sub-datasets retained in the official repository; not the live 2026 SOTA

[来源1](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）

### 覆盖范围与限制

All 17 verifiable rows of the official README were restored, together with 9 subtask leaderboards, including BACE classification and regression, PDBbind core, and the later HOPV extension. The subtask leaderboards retain the original metrics and error bars. The submission dates are 2020–2021, and the access date 2026-11-08 cannot be rewritten as a new experiment date. A complete split and seed are not given, and the current SOTA is not claimed from the values.

[来源1](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）

## Contact

### 公开研究邮箱

pande@stanford.edu

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 项目反馈入口

https://github.com/deepchem/deepchem/issues

[来源1](https://github.com/deepchem/deepchem/blob/master/README.md)（访问 2026-11-08）

### 官方公开社交入口

Unverified

> 状态：待核实。

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 公开渠道/隐私边界

Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/1703.00564

[来源1](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### PDF SHA-256

a017e94ab6a9b3165a99035b4839a10646e07f632f9406de98dd4c220cae3701

> SHA-256 of the original bytes downloaded this time. They were not compressed or modified.

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### PDF bytes

8094211

[来源1](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）

### 其他官方文档

[来源2](https://arxiv.org/abs/1703.00564)（访问 2026-11-08）；[来源3](https://arxiv.org/pdf/1703.00564)（访问 2026-11-08）；[来源4](https://deepchem.io/tutorials/an-introduction-to-moleculenet/)（访问 2026-11-08）；[来源5](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）；[来源6](https://github.com/deepchem/deepchem/blob/master/LICENSE)（访问 2026-11-08）；[来源7](https://github.com/deepchem/deepchem/blob/master/README.md)（访问 2026-11-08）；[来源8](https://github.com/deepchem/deepchem/blob/master/examples/benchmark.py)（访问 2026-11-08）；[来源9](https://github.com/deepchem/moleculenet/blob/master/README.md)（访问 2026-11-08）

## Changelog

### Changelog

```json
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
```

[来源1](https://deepchem.readthedocs.io/en/stable/api_reference/moleculenet.html)（访问 2026-11-08）
