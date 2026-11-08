# GenoTEX

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

GenoTEX splits analysis of gene expression into selection of the data, preprocessing, and association of a gene with a trait. What it examines at the core is carrying out the full analysis from the raw data, rather than only answering a question of biological knowledge. When the results are read, input that runs end to end and input that an expert has already preprocessed must be distinguished first. The AUROC of the two cannot be merged into one leaderboard.

Guide source: [https://arxiv.org/abs/2406.15341](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07)

## Basic information

### Short name

GenoTEX

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Full name

GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Dataset version

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Paper version

v3; 2025-04-09 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Release date

2024-06-22 (submission time of the first arXiv draft; not an inferred data first-release date).

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Section

Biology and medicine

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07 )

### Subfields

- Gene expression data analysis

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07 )

### License

The dataset is CC BY 4.0 (the License section of the official README).

Sources: [1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md) (accessed 2026-11-07 )

### Paper

https://arxiv.org/abs/2406.15341

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 代码入口

https://github.com/Liu-Hy/GenoTEX

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Dataset

https://huggingface.co/datasets/Liu-Hy/GenoTEX

Note: The official README also provides a Kaggle DOI; HF is a bundled distribution of the complete code and data, not a newly added benchmark.

Sources: [1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/HEAD/README.md) (accessed 2026-11-07 ) ; [2](https://huggingface.co/datasets/Liu-Hy/GenoTEX/raw/main/README.md) (accessed 2026-11-07 )

### Official homepage

https://github.com/Liu-Hy/GenoTEX

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Paper title

GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Origin and maintenance

### 发起团队

The bylined author team is UIUC/Novartis; a formal relationship as joint initiators is Unverified.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 合作及署名机构

The affiliations named on the paper are the University of Illinois Urbana-Champaign and Novartis; only the author affiliations are recorded, and a formal collaboration contract or joint ownership is not presumed.

Sources: [1](https://arxiv.org/pdf/2406.15341) (accessed 2026-11-07 )

### Authors

- Liu, Haoyang
- Chen, Shuyu
- Zhang, Ye
- Wang, Haohan

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Maintainer

The official Liu-Hy/GenoTEX repository.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Funders

National AI Research Resource（NAIRR），grant 240283。

Sources: [1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md) (accessed 2026-11-07 )


## Design goals

### 评测能力

Automated expression analysis from data selection and preprocessing through to gene–trait association.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 设计动机

Ordinary code questions lack complete screening and quality control of biological data, and are detached from the real research chain.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Construction

### 材料来源

GEO and TCGA/UCSC Xena expression data, with auxiliary materials such as OpenTargets/NCBI Gene.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 编制背景

Nine trained bioinformatics annotators; about 20 weeks of construction work.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Review process

Each trait is analyzed independently by two people, then rechecked by a senior reviewer; shared guidelines are iterated.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Quality control

A unified process of screening, selection, preprocessing, and linking references; usable data are distinguished from data that were successfully preprocessed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 去污染边界

Depends on public data and the public literature; human references and task splits are not equivalent to excluding exposure in foundation-model training.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Data format

### Size

1,384 GTA questions: 132 unconditional and 1,252 conditional. There are 911 input datasets, 152,415 samples, and 237,907 lines of analysis code. The README gives 41.5 GB for the input data and 82.0 GB for a full download. The two figures are different scopes.

Sources: [1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md) (accessed 2026-11-07 )

### Question types

Data screening, selection, preprocessing, and gene-trait association.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Modalities

Gene-expression matrices, phenotypic and clinical metadata, code, and result tables.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Languages

English task and data metadata and biological identifiers; primarily numerical omics.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Difficulty

End-to-end and preprocessed-data-only differ in difficulty and should be reported separately.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 公开及隐藏划分

The data and the reference analyses are public; full-pipeline tasks and tasks after preprocessing are different protocols, and their scores cannot be merged.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Evaluation

### Metrics

Screening uses F1 and selection uses accuracy; preprocessing is AJ/SJ/CSC; association is primarily AUROC, with additional P/R/F1/GSEA.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 计分

Compared with expert reference procedures and results; gene discovery is not proof of causal biological truth.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 提示与运行设置

A GenoAgent multi-agent workflow; the model and the existing preprocessed input conditions must be held fixed when comparing.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 评测入口

eval.py evaluates three classes of task: selection, preprocessing, and analysis. The prediction directory must match the format of the output reference directory. The evaluation can be selected by the gene, clinical, and linked subtasks.

Sources: [1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md) (accessed 2026-11-07 )

### 可比性边界

The paper's end-to-end task and preprocessed task differ; 0.97 and 0.74 AUROC cannot be treated as an improvement on the same leaderboard.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 已核实版本

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2024-06-22；timezone：；- version：v2；submitted_at：2025-03-28；timezone：；- version：v3；submitted_at：2025-04-09；timezone：；2026_H2_evidence：- url：https://arxiv.org/html/2610.21074v1；date：2026-10-15；note：OmicsBench §2 explicitly cites GenoTEX (Liu et al. 2025) and classifies it as a biological-analysis benchmark with given data and a single request.；evidence_boundary：A citation is not a rerun; this page keeps the historical experiments in the paper separate from the current leaderboard.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### Saturation

End-to-end results remain clearly behind the human reference; the H2 citation is not a new actual model run.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 已知问题

Manual analysis itself involves choices of method and statistical uncertainty; public data may have been exposed in training, and reference results are not causal ground truth.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 衍生关系

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://github.com/Liu-Hy/GenoTEX) (accessed 2026-11-07 )

### 官方结果入口

https://github.com/Liu-Hy/GenoTEX

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 第三方结果入口

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Paper v3 Table 2: end-to-end, starting from the raw data | — | GenoAgent + OpenAI o1 | 0.74 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 2: end-to-end, starting from the raw data | — | GenoAgent + Claude 3.5 Sonnet | 0.71 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 2: end-to-end, starting from the raw data | — | GenoAgent + OpenAI o3-mini | 0.7 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 2: end-to-end, starting from the raw data | — | GenoAgent + DeepSeek R1 | 0.7 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 3: given expert-preprocessed data | — | GenoAgent | 0.97 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 3: given expert-preprocessed data | — | Data Interpreter | 0.95 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 3: given expert-preprocessed data | — | MetaGPT | 0.95 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |
| Paper v3 Table 3: given expert-preprocessed data | — | CodeAct | 0.92 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 (paper revision) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

Table 2 and Table 3 are historical experiments under different input conditions; every row listed in the PDF was reviewed, but no live overall leaderboard that can be checked was obtained. rank=null means that no live rank across models was given; the model API snapshot remains Unverified.

Sources: [1](https://arxiv.org/pdf/2406.15341) (accessed 2026-11-07 ) ; [2](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/HEAD/README.md) (accessed 2026-11-07 )


## Contact

### 公开研究联系邮箱

- hl57@illinois.edu
- shuyu5@illinois.edu
- haohanw@illinois.edu
- ye-4.zhang@novartis.com

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 问题反馈

https://github.com/Liu-Hy/GenoTEX/issues

Sources: [1](https://github.com/Liu-Hy/GenoTEX) (accessed 2026-11-07 )

### 官方账号

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 隐私政策

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Original files

### 原文PDF

https://arxiv.org/pdf/2406.15341

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### PDF SHA-256

a736e1f4af1ac40df8d1727de6722e005292ffdc20ea002a847ac5114d2ce790

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/2406.15341) (accessed 2026-11-07 )

### PDF bytes

1364730

Sources: [1](https://arxiv.org/pdf/2406.15341) (accessed 2026-11-07 )

### Folder

id：1fUMNCa76uvA8Rrlhv0dnpnOz5L1LD5Di；webViewLink：

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )

### 其他原始材料

- type：中文介绍；id：1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts；webViewLink：https://docs.google.com/document/d/1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts/edit

Sources: [1](https://docs.google.com/document/d/1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts/edit) (accessed 2026-11-07 )

### PDF

id：14eUzgPi0ENwV5ruQZg9wUciFdtwVURCV；webViewLink：

Sources: [1](https://arxiv.org/abs/2406.15341) (accessed 2026-11-07 )


## Changelog

### 本页修订

- date：2026-11-07；timezone：；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- date：2026-11-07；timezone：；change：深度优化：打开Official README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07 )

