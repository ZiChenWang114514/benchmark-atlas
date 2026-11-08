# SciGym

> Verification date: 2026-11-08. The access date is not the publication date or the run date; a field that cannot be confirmed remains Unverified.

SciGym turns systems-biology models into an interactive dry laboratory: the agent perturbs initial concentrations, analyzes time trajectories, proposes missing reactions, and submits an SBML model. Structural recovery and kinetic reproduction are measured by different metrics; the public large split is not a hidden test set, and the number of public evaluation records is not a count of new biological systems.

Guide source: [Official materials](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08); specific facts and historical access dates are given in the individual fields.

## Basic information

### Short name

SciGym

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Full name

SciGym systems-biology dry-lab benchmark

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Benchmark version

Original SciGym release: small 137, large 213; no independent semantic-version label is given.

Sources: [1](https://github.com/h4duan/SciGym) (accessed 2026-11-08); [2](https://huggingface.co/datasets/h4duan/scigym-sbml/raw/main/README.md) (accessed 2026-11-08)

### Paper version

v2; latest submission 2025-07-15

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Release date

2025-07-03 (first arXiv submission; the date the data went online is not inferred).

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Section

Biology and medicine

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

Sources: [1](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07)

### Field tags

- Systems-biology dry lab

Sources: [1](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07)

### 许可与适用范围

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2507.02083

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Code repository

https://github.com/h4duan/SciGym

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 数据地址

https://huggingface.co/datasets/h4duan/scigym-sbml

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Official homepage

https://h4duan.github.io/scigym-benchmark/

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Paper title

Measuring Scientific Capabilities of Language Models with a Systems Biology Dry Lab

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

## Origin and maintenance

### 机构与发起关系

Paper-credited teams including Toronto, SickKids, Axiom, Mila, and Vector; a formal collaboration agreement is not inferred.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 合作机构/署名单位

Author affiliations on the project page include the University of Toronto, SickKids, Axiom, Mila, and the Vector Institute; only the affiliations that are named are recorded here, and a legal agreement of collaboration is not inferred.

Sources: [1](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08)

### Authors

- Duan, Haonan
- Lu, Stephen Zhewen
- Harrigan, Caitlin Fiona
- Desai, Nishkrit
- Lu, Jiarui
- Koziarski, Michał
- Cotta, Leonardo
- Maddison, Chris J.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 当前维护入口

The h4duan/SciGym and project-page team.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Funders

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

## Design goals

### Abilities measured

Interactive experimental design: change the initial concentrations, observe the dynamics, reconstruct the hidden biochemical reaction system, and validate the model.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Design background

Static question answering cannot test falsifiable hypotheses, active experimentation, or iterative scientific modeling.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

## Construction

### 题目或数据来源

1,096 manually curated models from BioModels are filtered to 350 executable SBML systems.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 出题背景

Researchers in systems biology, machine learning, and molecular modeling; the source library is of human-curated models.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Review process

Models that cannot be executed, that have no reactions or species, or that contain unsupported rules or events are excluded; they are checked by program simulation.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Quality control

Comments/metadata are removed, IDs are anonymized, elements are shuffled, and reaction citations are removed; Tellurium simulation compatibility is verified.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 去污染措施

Anonymization reduces shortcuts that rely on memorizing names; the source BioModels are public, so it is not claimed that they did not enter model pretraining.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

## Data format

### Size

350 systems; 137 small systems (fewer than 10 reactions) and 213 large systems (at most about 400 reactions).

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Question types

Multi-step interactive experiments, Python modeling, hidden reaction networks, and reconstruction of dynamics.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Modalities

Numerical concentration trajectories, with interaction in SBML/XML, Python, and English.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Languages

English task and agent prompts, and Python/SBML.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Difficulty

Split into small/large by reaction-system scale; strong models remain limited in recovering reaction structure.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 数据划分

small is the 137 models evaluated in the paper; large is an additional 213 models that were not evaluated in the paper. Both can be downloaded with the official data/download.py, and large should not be miswritten as a hidden test set.

Sources: [1](https://raw.githubusercontent.com/h4duan/SciGym/main/README.md) (accessed 2026-11-07)

## Evaluation

### Metrics

Reaction Matching Score (RMS): matching is by the sets of reactants, products, and modifiers, and Precision, Recall, and F1 are reported. Simulation Trajectory Error (STE) compares trajectories by SMAPE, and lower is better.

Sources: [1](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08)

### Scoring

Reaction graphs and predicted trajectories are compared; similar system behavior does not mean that the dynamical expression is uniquely correct.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 提示与运行设置

A ReAct agent, at most 20 iterations, plus 3 debug attempts; Python/Tellurium simulation and a perturbation of concentration.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 评测脚本

https://github.com/h4duan/SciGym

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 可比性提醒

Whether a modifier is present, small or large, and the direction of the dynamics error must be retained; simulation without noise does not stand for a wet-lab experiment.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 数据版本与更新

The HF default configuration has 350 rows in total: small 137 and large 213. small is the evaluation set of the paper, and the additional systems in large are not a hidden set. The official materials also link scigym-eval. The small split contains 2466 records of model evaluation, not 2466 new biological systems.

Sources: [1](https://huggingface.co/datasets/h4duan/scigym-sbml/raw/main/README.md) (accessed 2026-11-08); [2](https://huggingface.co/datasets/h4duan/scigym-eval/raw/main/README.md) (accessed 2026-11-08); [3](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08)

### 论文修订记录

- **2026_H2_evidence**：[{"url": "https://arxiv.org/html/2609.19134v1", "date": "2026-09-16", "note": "ScienceIDE §4.1 explicitly lists the systems-biology SciGym and cites its original paper, arXiv:2507.02083; this is an H2 academic citation, not a run in this paper."}]
- **evidence_boundary**：A citation is not a rerun; this page keeps the historical experiments in the paper separate from the current leaderboard.
- **paper_metadata**：{"title": "Measuring Scientific Capabilities of Language Models with a Systems Biology Dry Lab", "authors": ["Duan, Haonan", "Lu, Stephen Zhewen", "Harrigan, Caitlin Fiona", "Desai, Nishkrit", "Lu, Jiarui", "Koziarski, Michał", "Cotta, Leonardo", "Maddison, Chris J."], "release": "2025-07-02", "latest": "2025-07-14", "version": "v2", "source_date_basis": "The old release and latest labels are date labels from the arXiv source site."}
- **arxiv_submission_history**：[{"version": "v1", "submitted_at": "2025-07-03"}, {"version": "v2", "submitted_at": "2025-07-15"}]

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 饱和程度

Given the historically low F1 on hidden-system recovery, it cannot be called saturated; H2 only cites it and does not provide an updated leading score.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 争议与已知问题

Ideal noiseless simulation and limits of identifiability; reconstructing a similar trajectory does not uniquely recover the true reaction mechanism.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### Derivative benchmarks

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (access date, not the experiment run date)

Sources: [1](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08)

### 官方榜单入口

https://h4duan.github.io/scigym-benchmark/

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 第三方入口

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 可核验结果

- {"rank": "No cross-protocol rank", "model": "Gemini-2.5-Flash", "score": {"STE": 0.4181, "RMS_precision_with_modifiers": 0.1527, "RMS_recall_with_modifiers": 0.1071, "RMS_F1_with_modifiers": 0.1217, "RMS_precision_without_modifiers": 0.2399, "RMS_recall_without_modifiers": 0.1839, "RMS_F1_without_modifiers": 0.2005}, "metric": "Lower STE is better; higher is better for the six RMS items; all keep the original proportions and are not converted to percentages", "track": "Official project page/paper v2 Table1; a historical experiment on the small set of 137 systems.", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_row": 1}
- {"rank": "No cross-protocol rank", "model": "GPT-4.1-mini", "score": {"STE": 0.6007, "RMS_precision_with_modifiers": 0.1516, "RMS_recall_with_modifiers": 0.1253, "RMS_F1_with_modifiers": 0.132, "RMS_precision_without_modifiers": 0.253, "RMS_recall_without_modifiers": 0.2313, "RMS_F1_without_modifiers": 0.2322}, "metric": "Lower STE is better; higher is better for the six RMS items; all keep the original proportions and are not converted to percentages", "track": "Official project page/paper v2 Table1; a historical experiment on the small set of 137 systems.", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_row": 2}
- {"rank": "No cross-protocol rank", "model": "Claude-3.5-Haiku", "score": {"STE": 0.6281, "RMS_precision_with_modifiers": 0.0858, "RMS_recall_with_modifiers": 0.0421, "RMS_F1_with_modifiers": 0.053, "RMS_precision_without_modifiers": 0.1454, "RMS_recall_without_modifiers": 0.0805, "RMS_F1_without_modifiers": 0.0987}, "metric": "Lower STE is better; higher is better for the six RMS items; all keep the original proportions and are not converted to percentages", "track": "Official project page/paper v2 Table1; a historical experiment on the small set of 137 systems.", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_row": 3}
- {"rank": "No cross-protocol rank", "model": "Gemini-2.5-Pro", "score": {"STE": 0.3212, "RMS_precision_with_modifiers": 0.2138, "RMS_recall_with_modifiers": 0.1664, "RMS_F1_with_modifiers": 0.1817, "RMS_precision_without_modifiers": 0.3781, "RMS_recall_without_modifiers": 0.3219, "RMS_F1_without_modifiers": 0.3383}, "metric": "Lower STE is better; higher is better for the six RMS items; all keep the original proportions and are not converted to percentages", "track": "Official project page/paper v2 Table1; a historical experiment on the small set of 137 systems.", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_row": 4}
- {"rank": "No cross-protocol rank", "model": "GPT-4.1", "score": {"STE": 0.4611, "RMS_precision_with_modifiers": 0.2067, "RMS_recall_with_modifiers": 0.1597, "RMS_F1_with_modifiers": 0.174, "RMS_precision_without_modifiers": 0.3517, "RMS_recall_without_modifiers": 0.2888, "RMS_F1_without_modifiers": 0.3038}, "metric": "Lower STE is better; higher is better for the six RMS items; all keep the original proportions and are not converted to percentages", "track": "Official project page/paper v2 Table1; a historical experiment on the small set of 137 systems.", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_row": 5}
- {"rank": "No cross-protocol rank", "model": "Claude-3.7-Sonnet", "score": {"STE": 0.3615, "RMS_precision_with_modifiers": 0.178, "RMS_recall_with_modifiers": 0.1698, "RMS_F1_with_modifiers": 0.1688, "RMS_precision_without_modifiers": 0.316, "RMS_recall_without_modifiers": 0.317, "RMS_F1_without_modifiers": 0.3047}, "metric": "Lower STE is better; higher is better for the six RMS items; all keep the original proportions and are not converted to percentages", "track": "Official project page/paper v2 Table1; a historical experiment on the small set of 137 systems.", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_row": 6}

Sources: [1](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2507.02083) (accessed 2026-11-08)

### 榜单覆盖边界

The six models and seven metrics are transcribed in full. The STE ordering and the RMS ordering differ, and no unified overall place is assigned. The page agrees with paper v2, and the access date is not treated as the run date. HF scigym-eval provides a public record of model dialogues and of the final SBML. That is not the same as an additional test system.

Sources: [1](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2507.02083) (accessed 2026-11-08); [3](https://huggingface.co/datasets/h4duan/scigym-eval/raw/main/README.md) (accessed 2026-11-08)

## Contact

### 公开研究联系

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 公开反馈渠道

https://github.com/h4duan/SciGym/issues

Sources: [1](https://github.com/h4duan/SciGym) (accessed 2026-11-07)

### 官方社交账号

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 联系方式原则

Only public feedback channels on the project site, in the paper, and in the official repository are used; private contact details are not gathered.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08)

## Original files

### 论文原件

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 原始PDF地址

https://arxiv.org/pdf/2507.02083

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08)

### 原始文件SHA-256

8f490e009f6448434412f43ec8c89cd97d6100ebfa001bf6b38d17f7433f86b1

Note: Byte count of the original PDF actually downloaded. The existing file is not changed on that basis.

Sources: [1](https://arxiv.org/pdf/2507.02083) (accessed 2026-11-08)

### 原始文件字节数

7093862

Sources: [1](https://arxiv.org/pdf/2507.02083) (accessed 2026-11-08)

### Other documents

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2507.02083) (accessed 2026-11-08); [2](https://h4duan.github.io/scigym-benchmark/) (accessed 2026-11-08)
