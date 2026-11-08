# The Well

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

The Well is not a set of scientific multiple-choice questions. It is a 15TB resource for spatiotemporal field prediction, made up of 16 physics-simulation datasets. The baseline task predicts the next step from four steps of history and tests autoregressive error; different systems and time windows cannot be combined into an undefined overall champion. The old viscoelastic-instability data were deprecated because of a processing error, and the corrected version must be distinguished.

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08); [2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md) (accessed 2026-11-08); [3](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08)

## Basic information

### Short name

The Well

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Full name

The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Benchmark version

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Paper version

arXiv v2; submitted at 2025-02-22 04:24:16.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Release date

2024-12-01 04:42:14 (arXiv v1 submission; not an inferred data go-live date)

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Section

Physics

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

Sources: [1](https://arxiv.org/html/2610.06095v3) (accessed 2026-11-07， )

### Field tags

- Multiphysics simulation and operator learning

Sources: [1](https://arxiv.org/html/2610.06095v3) (accessed 2026-11-07， )

### 许可与适用范围

The code is BSD-3-Clause (LICENSE of the current repository); Datasheet Q43 of the paper states that the full set of data is CC-BY-4.0, and the active_matter dataset card is likewise marked CC-BY-4.0. Some generation programs are proprietary code, and redistributability is not inferred.

Sources: [1](https://github.com/PolymathicAI/the_well/blob/master/LICENSE) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， ) ; [3](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md) (accessed 2026-11-08， )

### Paper

https://arxiv.org/abs/2412.00568

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Code repository

https://github.com/PolymathicAI/the_well

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### 数据地址

https://huggingface.co/polymathic-ai

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Official homepage

https://polymathic-ai.org/the_well/

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Paper title

The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

## Origin and maintenance

### 机构与发起关系

Polymathic AI; the project page states explicitly that it is the lead.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， ) ; [2](https://polymathic-ai.org/the_well/) (accessed 2026-11-07， )

### Partner organizations

Project partners include the Flatiron Institute, Colorado Boulder, Cambridge, NYU, Rutgers, Cornell, Tokyo, Los Alamos, UC Berkeley, Princeton, CEA DAM, and Liège; an independent funding relationship is not inferred.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， ) ; [2](https://polymathic-ai.org/the_well/) (accessed 2026-11-07， )

### Authors

- Ohana, Ruben
- McCabe, Michael
- Meyer, Lucas
- Morel, Rudy
- Agocs, Fruzsina J.
- Beneitez, Miguel
- Berger, Marsha
- Burkhart, Blakesley
- Burns, Keaton
- Dalziel, Stuart B.
- Fielding, Drummond B.
- Fortunato, Daniel
- Goldberg, Jared A.
- Hirashima, Keiya
- Jiang, Yan-Fei
- Kerswell, Rich R.
- Maddu, Suryanarayana
- Miller, Jonah
- Mukhopadhyay, Payel
- Nixon, Stefan S.
- Shen, Jeff
- Watteaux, Romain
- Blancard, Bruno Régaldo-Saint
- Rozet, François
- Parker, Liam H.
- Cranmer, Miles
- Ho, Shirley

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Current maintainer

The Polymathic AI project team; the official documentation lists Ruben Ohana and Michael McCabe as public contacts.

Sources: [1](https://polymathic-ai.org/the_well/) (accessed 2026-11-07， )

### 资助与支持

Polymathic AI received funding from the Simons Foundation and from Schmidt Sciences, and NVIDIA donated DGX Cloud node-hours; the paper also states, for each contributed dataset, support from EPSRC, NASA, LANL, DOE, CEA, and others. These cannot be merged into a single total budget.

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

## Design goals

### Abilities measured

Subsequent physical evolution is predicted from historical spatiotemporal fields; this covers surrogate-model/neural-operator learning across multiple physical systems, and long-time rollout stability.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Design background

Datasets of common operators cover only a narrow range of physical behavior; this library emphasizes diversity of dimension, boundary conditions, scale, and nonlinear mechanisms.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

## Construction

### 题目或数据来源

Domain scientists and developers of numerical software supply real numerical simulations; these are not question-answer pairs synthesized by an LLM.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### 出题背景

A collaboration among researchers in computational physics, fluids, astrophysics, numerical analysis, and machine learning.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Review process

The paper states, for each dataset, the governing equations, the generation procedure, the numerical methods, and the physical mechanisms; the number of independent external reviews is Unverified.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Quality control

Experts in each field provide the equations, numerical methods, boundary conditions, and parameters; HDF5 and tensor metadata are unified. The current repository states that viscoelastic_instability is deprecated because of a processing error, and viscoelastic_instability_v2 is a corrected version of the same data.

Sources: [1](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

### 去污染与泄漏

By default, each group of simulation parameters is split 80/10/10 by initial condition; a subset with too few simulations instead uses non-overlapping blocks of time, so it cannot be claimed that every subset is split completely by trajectory. An independent audit of contamination from the pretraining corpus is Unverified.

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

## Data format

### Size

16 datasets, 15TB in total (the official figure); each set is about 6.9GB to 5.1TB.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， ) ; [2](https://polymathic-ai.org/the_well/) (accessed 2026-11-07， )

### Question types

Numerical time-series regression; single-step prediction and autoregressive multi-step rollout.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Modalities

Numeric fields on a regular grid, time series, and physical metadata; an HDF5/float32 interface.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Languages

The principal content is numerical tensors and a Python interface; it is not natural-language multiple choice.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Difficulty

Errors differ markedly across systems; there is no single difficulty level for the questions.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### 数据划分

Public train/valid/test; usually split 80/10/10 by initial condition, and when there are not enough trajectories the split is made in the same proportions into time blocks that do not overlap, and a time block is not guaranteed to be ordered strictly by time (paper Datasheet Q12).

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

## Evaluation

### Metrics

VRMSE (lower is better; the mean of the predicted target field is about 1); NMSE/NRMSE, maximum error, per-spectrum error, and others are also provided.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### Scoring

Averaged after computation for each physical field; single-step results and rollouts over different time windows are reported separately.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### 提示与运行设置

Not a question-and-answer prompt evaluation; a Hydra configuration fixes the model, the data, the optimizer, and the training resources. The official example is FNO on active_matter.

Sources: [1](https://polymathic-ai.org/the_well/) (accessed 2026-11-07， )

### 评测脚本

https://github.com/PolymathicAI/the_well

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### 可比性提醒

Errors from different equations, resolutions, rollout horizons, or training compute cannot be combined directly into an overall winner. The original paper describes its results as example baselines, not an exhaustive search for optimal hyperparameters.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

## Current status

### Date checked

2026-11-08

Sources: [1](https://polymathic-ai.org/the_well/) (accessed 2026-11-08， )

### 数据版本与更新

The current official repository provides viscoelastic_instability_v2 and retires the old viscoelastic_instability, which is kept only so that older results can still be compared. One semantic version number for the dataset as a whole is Unverified. The version of a software package cannot stand in for the version of the data.

Sources: [1](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08， )

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-12-01 04:42:14 ", "timezone": ""}
- {"version": "v2", "submitted_at": "2025-02-22 04:24:16 ", "timezone": ""}

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-08， )

### 饱和证据与局限

The official statement explicitly says that the original paper is an example baseline on a single H100 with a 12-hour budget, not a SOTA result; the gap between single-step and rollout performance is large, so a low single-step error cannot be taken to mean that all of the physical dynamics are saturated.

Sources: [1](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

### 争议与已知问题

The old viscoelastic_instability version was deprecated because of a processing error and must be replaced by v2. Old-version results among the paper baselines are historical only. Some time-block splits of the data still share the physical parameters of the same simulation, so strict cross-trajectory extrapolation should not be claimed.

Sources: [1](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

### 衍生或后继基准

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08); [2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md) (accessed 2026-11-08); [3](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08)

### 官方榜单入口

https://polymathic-ai.org/the_well/

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

### 第三方入口

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Paper v2, Table 2 / acoustic_scattering (maze). | 4 | FNO | 0.5062 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / acoustic_scattering (maze). | 3 | TFNO | 0.5057 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / acoustic_scattering (maze). | 2 | U-net | 0.0351 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / acoustic_scattering (maze). | 1 | CNextU-net | 0.0153 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / active_matter | 4 | FNO | 0.3691 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / active_matter | 3 | TFNO | 0.3598 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / active_matter | 2 | U-net | 0.2489 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / active_matter | 1 | CNextU-net | 0.1034 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / convective_envelope_rsg. | 1 | FNO | 0.0269 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / convective_envelope_rsg. | 2 | TFNO | 0.0283 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / convective_envelope_rsg. | 3 | U-net | 0.0555 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / convective_envelope_rsg. | 4 | CNextU-net | 0.0799 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / euler_multi_quadrants (periodic b.c.) | 3 | FNO | 0.4081 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / euler_multi_quadrants (periodic b.c.) | 4 | TFNO | 0.4163 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / euler_multi_quadrants (periodic b.c.) | 2 | U-net | 0.1834 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / euler_multi_quadrants (periodic b.c.) | 1 | CNextU-net | 0.1531 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / gray_scott_reaction_diffusion | 1 | FNO | 0.1365 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / gray_scott_reaction_diffusion | 4 | TFNO | 0.3633 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / gray_scott_reaction_diffusion | 3 | U-net | 0.2252 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / gray_scott_reaction_diffusion | 2 | CNextU-net | 0.1761 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / helmholtz_staircase | 1 | FNO | 0.00046 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / helmholtz_staircase | 2 | TFNO | 0.00346 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / helmholtz_staircase | 3 | U-net | 0.01931 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / helmholtz_staircase | 4 | CNextU-net | 0.02758 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / MHD_64 | 4 | FNO | 0.3605 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / MHD_64 | 3 | TFNO | 0.3561 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / MHD_64 | 2 | U-net | 0.1798 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / MHD_64 | 1 | CNextU-net | 0.1633 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / planetswe | 2 | FNO | 0.1727 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / planetswe | 1 | TFNO | 0.0853 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / planetswe | 3 | U-net | 0.362 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / planetswe | 4 | CNextU-net | 0.3724 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / post_neutron_star_merger. | 2 | FNO | 0.3866 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / post_neutron_star_merger. | 1 | TFNO | 0.3793 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_benard | 3 | FNO | 0.8395 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_benard | 1 | TFNO | 0.6566 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_benard | 4 | U-net | 1.486 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_benard | 2 | CNextU-net | 0.6699 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_taylor_instability (At = 0.25) | — | FNO | >10 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_taylor_instability (At = 0.25) | — | TFNO | >10 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_taylor_instability (At = 0.25) | — | U-net | >10 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / rayleigh_taylor_instability (At = 0.25) | — | CNextU-net | >10 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / shear_flow | 2 | FNO | 1.189 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / shear_flow | 3 | TFNO | 1.472 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / shear_flow | 4 | U-net | 3.447 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / shear_flow | 1 | CNextU-net | 0.808 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / supernova_explosion_64. | 3 | FNO | 0.3783 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / supernova_explosion_64. | 4 | TFNO | 0.3785 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / supernova_explosion_64. | 1 | U-net | 0.3063 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / supernova_explosion_64. | 2 | CNextU-net | 0.3181 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / turbulence_gravity_cooling. | 2 | FNO | 0.2429 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / turbulence_gravity_cooling. | 3 | TFNO | 0.2673 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / turbulence_gravity_cooling. | 4 | U-net | 0.6753 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / turbulence_gravity_cooling. | 1 | CNextU-net | 0.2096 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_2D | 3 | FNO | 0.5001 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_2D | 4 | TFNO | 0.5016 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_2D | 2 | U-net | 0.2418 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_2D | 1 | CNextU-net | 0.1956 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_3D | 4 | FNO | 0.5278 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_3D | 3 | TFNO | 0.5187 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_3D | 2 | U-net | 0.3728 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 2 / turbulent_radiative_layer_3D | 1 | CNextU-net | 0.3667 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / viscoelastic_instability. | 4 | FNO | 0.7212 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / viscoelastic_instability. | 3 | TFNO | 0.7102 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / viscoelastic_instability. | 2 | U-net | 0.4185 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 2 / viscoelastic_instability. | 1 | CNextU-net | 0.2499 | one-step VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Predict the next step from 4 steps of history; a single H100 / 12h budget | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 6:12 | 3 | FNO | 1.06 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 13:30 | 4 | FNO | 1.72 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 6:12 | 4 | TFNO | 1.13 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 13:30 | 3 | TFNO | 1.23 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 6:12 | 1 | U-net | 0.56 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 13:30 | 1 | U-net | 0.92 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 6:12 | 2 | CNextU-net | 0.78 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / acoustic_scattering (maze) / 13:30 | 2 | CNextU-net | 1.13 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / active_matter / 6:12 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / active_matter / 13:30. | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / active_matter / 6:12 | 3 | TFNO | 7.52 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / active_matter / 13:30. | 3 | TFNO | 4.72 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / active_matter / 6:12 | 2 | U-net | 2.53 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / active_matter / 13:30. | 1 | U-net | 2.62 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / active_matter / 6:12 | 1 | CNextU-net | 2.11 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / active_matter / 13:30. | 2 | CNextU-net | 2.71 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 6:12 | 1 | FNO | 0.28 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 13:30 | 1 | FNO | 0.47 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 6:12 | 2 | TFNO | 0.32 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 13:30 | 2 | TFNO | 0.65 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 6:12 | 3 | U-net | 0.76 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 13:30 | 4 | U-net | 2.16 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 6:12 | 4 | CNextU-net | 1.15 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / convective_envelope_rsg / 13:30 | 3 | CNextU-net | 1.59 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 6:12 | 2 | FNO | 1.13 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 13:30 | 1 | FNO | 1.37 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 6:12 | 3 | TFNO | 1.23 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 13:30 | 2 | TFNO | 1.52 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 6:12 | 1 | U-net | 1.02 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 13:30 | 3 | U-net | 1.63 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 6:12 | 4 | CNextU-net | 4.98 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / euler_multi_quadrants / 13:30 | — | CNextU-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 6:12 | 3 | FNO | 0.89 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 13:30 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 6:12 | 4 | TFNO | 1.54 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 13:30 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 6:12 | 2 | U-net | 0.57 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 13:30 | — | U-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 6:12 | 1 | CNextU-net | 0.29 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / gray_scott_reaction_diffusion / 13:30 | 1 | CNextU-net | 7.62 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / helmholtz_staircase / 6:12. | 1 | FNO | 0.002 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / helmholtz_staircase / 13:30 | 1 | FNO | 0.003 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / helmholtz_staircase / 6:12. | 2 | TFNO | 0.011 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / helmholtz_staircase / 13:30 | 2 | TFNO | 0.019 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / helmholtz_staircase / 6:12. | 3 | U-net | 0.057 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / helmholtz_staircase / 13:30 | 3 | U-net | 0.097 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / helmholtz_staircase / 6:12. | 4 | CNextU-net | 0.11 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / helmholtz_staircase / 13:30 | 4 | CNextU-net | 0.194 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 6:12 | 1 | FNO | 1.24 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 13:30 | 1 | FNO | 1.61 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 6:12 | 2 | TFNO | 1.25 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 13:30 | 2 | TFNO | 1.81 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 6:12 | 4 | U-net | 1.65 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 13:30 | 4 | U-net | 4.66 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 6:12 | 3 | CNextU-net | 1.3 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / MHD_64 / 13:30 | 3 | CNextU-net | 2.23 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 6:12 | 3 | FNO | 0.81 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 13:30 | 4 | FNO | 2.96 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 6:12 | 1 | TFNO | 0.29 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 13:30 | 2 | TFNO | 0.55 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 6:12 | 4 | U-net | 1.18 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 13:30 | 3 | U-net | 1.92 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 6:12 | 2 | CNextU-net | 0.42 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / planetswe / 13:30 | 1 | CNextU-net | 0.52 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / post_neutron_star_merger / 6:12 | 2 | FNO | 0.76 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / post_neutron_star_merger / 13:30 | 1 | FNO | 1.05 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / post_neutron_star_merger / 6:12 | 1 | TFNO | 0.7 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / post_neutron_star_merger / 13:30 | 1 | TFNO | 1.05 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 6:12. | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 13:30. | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 6:12. | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 13:30. | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 6:12. | — | U-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 13:30. | — | U-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 6:12. | — | CNextU-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2, Table 3 / rayleigh_benard / 13:30. | — | CNextU-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 6:12 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 13:30 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 6:12 | 1 | TFNO | 6.72 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 13:30 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 6:12 | — | U-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 13:30 | 1 | U-net | 2.84 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 6:12 | — | CNextU-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / rayleigh_taylor_instability / 13:30 | 2 | CNextU-net | 7.43 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 6:12 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 13:30 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 6:12 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 13:30 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 6:12 | — | U-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 13:30 | — | U-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 6:12 | 1 | CNextU-net | 2.33 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / shear_flow / 13:30 | — | CNextU-net | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 6:12 | 4 | FNO | 2.41 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 13:30 | — | FNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 6:12 | 3 | TFNO | 1.86 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 13:30 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 6:12 | 1 | U-net | 0.94 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 13:30 | 1 | U-net | 1.69 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 6:12 | 2 | CNextU-net | 1.12 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / supernova_explosion_64 / 13:30 | 2 | CNextU-net | 4.55 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 6:12 | 2 | FNO | 3.55 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 13:30 | 3 | FNO | 5.63 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 6:12 | 3 | TFNO | 4.49 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 13:30 | 4 | TFNO | 6.95 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 6:12 | 4 | U-net | 7.14 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 13:30 | 2 | U-net | 4.15 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 6:12 | 1 | CNextU-net | 1.3 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulence_gravity_cooling / 13:30 | 1 | CNextU-net | 2.09 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 6:12 | 3 | FNO | 1.79 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 13:30 | 3 | FNO | 3.54 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 6:12 | 4 | TFNO | 6.01 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 13:30 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 6:12 | 2 | U-net | 0.66 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 13:30 | 2 | U-net | 1.04 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 6:12 | 1 | CNextU-net | 0.54 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_2D / 13:30 | 1 | CNextU-net | 1.01 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 6:12 | 2 | FNO | 0.81 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 13:30 | 2 | FNO | 0.94 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 6:12 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 13:30 | — | TFNO | >10 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 6:12 | 3 | U-net | 0.95 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 13:30 | 3 | U-net | 1.09 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 6:12 | 1 | CNextU-net | 0.77 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / turbulent_radiative_layer_3D / 13:30 | 1 | CNextU-net | 0.86 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / viscoelastic_instability / 6:12 | 4 | FNO | 4.11 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / viscoelastic_instability / 6:12 | 3 | TFNO | 0.93 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / viscoelastic_instability / 6:12 | 2 | U-net | 0.89 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| Paper v2 Table 3 / viscoelastic_instability / 6:12 | 1 | CNextU-net | 0.52 | time-averaged VRMSE (lower is better) | Original-paper data; viscoelastic_instability is a deprecated older version；Autoregressive from the start of the trajectory; different from sliding-window one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08); [2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md) (accessed 2026-11-08); [3](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08)

### 榜单覆盖边界

All non-missing values are restored for the single step in Table 2 of paper v2 and for the two rollout windows in Table 3; tracks are split by data subset and by window, and a lower VRMSE is better. A value >10 is kept as a lower-bound label meaning greater than 10, and — is not turned into 0; the viscoelastic_instability scores are explicitly the old version and cannot be relabeled as corrected v2. These are baselines from the paper, and the current SOTA is not claimed.

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08); [2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md) (accessed 2026-11-08); [3](https://github.com/PolymathicAI/the_well) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

- rohana@flatironinstitute.org
- mmccabe@flatironinstitute.org

Sources: [1](https://polymathic-ai.org/the_well/) (accessed 2026-11-07， )

### 公开反馈渠道

https://github.com/PolymathicAI/the_well/issues

Sources: [1](https://github.com/PolymathicAI/the_well) (accessed 2026-11-07， )

### 官方社交账号

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

### 联系方式/隐私原则

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

## Original files

### 原始PDF

https://arxiv.org/pdf/2412.00568

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

### PDF SHA-256

050ca3384f117252586c27ff9940781852cc457e2967d7879a7c8a0b30dc8e1f

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

### PDF bytes

```json
5375610
```

Sources: [1](https://arxiv.org/pdf/2412.00568) (accessed 2026-11-08， )

### Folder

```json
{
  "id": "1_3NZPzkcaCBep04AYI5UroGFMuDa3jpa"
  "webViewLink": "
}
```

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

### Other documents

- {"type": "Chinese introduction", "id": "1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8", "webViewLink": "https://docs.google.com/document/d/1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8/edit"}

Sources: [1](https://docs.google.com/document/d/1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8/edit) (accessed 2026-11-07， )

### 论文原件

```json
{
  "id": "1nF862k2HR4HHw4_5Jo8_3xJE2UgSYJ5l"
  "webViewLink": "
}
```

Sources: [1](https://arxiv.org/abs/2412.00568) (accessed 2026-11-07， )

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://polymathic-ai.org/the_well/) (accessed 2026-11-08， )
