# WeatherBench

> In-depth review: 2026-11-08. The collection date is not the leaderboard update date; new evidence that has not been obtained does not overwrite an older source date.

WeatherBench turns data-driven medium-range weather prediction into a reproducible task on numerical fields. It is not a bank of climate questions; what matters is the target time of the prediction, the reanalysis ground truth, spatial regridding, and aggregation of error, rather than a natural-language prompt.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

## Basic information

### Short name

WeatherBench

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Full name

WeatherBench

> The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Benchmark version

The original WeatherBench (2020) framework; the README records revisions of the vertical levels and additions from CMIP, which were not released as a separate semantic version. The official recommendation is to use WeatherBench 2.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### Paper version

arXiv v3

Sources: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08 ).

### Release date

- **paper_first_submission_kst**：2020-02-03
- **date_type**：First submission of the paper; not the same as the first release of the dataset

Sources: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08 ).

### Section

Earth and astronomy

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

Sources: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08 ).

### Field tags

- 气象科学

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### License

Code: MIT (Copyright 2019 Stephan Rasp); the terms for ERA5 derived data must be verified separately.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/LICENSE) (accessed 2026-11-08 ).

### Paper

https://arxiv.org/abs/2002.00469

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Code

https://github.com/pangeo-data/WeatherBench

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 数据地址

https://mediatum.ub.tum.de/1524895

> The TUM data repository specified by the official README; the GitHub code address is not treated as the data-download address. The record page on this visit returned a too many requests page, and a downloaded and verified data package is not claimed.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### Official entry

https://github.com/pangeo-data/WeatherBench

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Paper title

WeatherBench: A benchmark dataset for data-driven weather forecasting

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

## Origin and maintenance

### Initiating organizations

Technical University of Munich, ECMWF, Stockholm University, the University of Washington, and the University of Toronto.

> Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### 署名合作机构

- Technical University of Munich
- ECMWF
- Stockholm University（Meteorology / Bolin Centre）
- University of Washington（Atmospheric Sciences）
- University of Toronto（Computer Science）

> Affiliations named on the paper are not equivalent to a legal partnership or to every funder.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### Authors

- Rasp, Stephan
- Dueben, Peter D.
- Scher, Sebastian
- Weyn, Jonathan A.
- Mouatadid, Soukayna
- Thuerey, Nils

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Maintainer

The project code and the feedback entry are at pangeo-data/WeatherBench. The corresponding author of the paper is Stephan Rasp. The README points toward a move to WeatherBench 2. Active maintenance cannot be inferred merely because the repository can still be reached.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### Funders

DFG supported Stephan Rasp. The Royal Society University Research Fellowship and ESIWACE2 supported Peter D. Dueben. ESIWACE2 received funding from EU Horizon 2020 No.823988. C3S permits redistribution of the data. The latter is not a statement of additional project funding.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

## Design goals

### Abilities measured

Unifies the data and the evaluation standard for data-driven medium-range global weather forecasting.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Design background

Early data-driven weather prediction used its own input variables, grids, forecast lead times, and evaluation data, and direct comparison across systems was difficult. This project places ERA5 preprocessing, verification on the same grid, and linear, CNN, and physics-model baselines in one reproducible workflow.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

## Construction

### 题目与数据来源

Monthly archives of the ERA5 reanalysis, after download and regridding; the IFS baseline comes from TIGGE; MPI-ESM-HR CMIP historical simulations are also provided.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 构建者背景

Researchers in meteorology, computer science, and physical simulation built the numerical data-processing pipeline. The author list involves TUM, ECMWF, the Department of Meteorology and the Bolin Centre at Stockholm University, Atmospheric Sciences at the University of Washington, and Computer Science at the University of Toronto. There is no author of natural-language questions.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### Review process

Data are processed from ERA5 reanalysis products, and linear, deep-learning, and physics-model baselines are provided.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### Quality control

Snakemake manages the monthly ERA5 download, bilinear regridding with xESMF, and the files by variable and year; evaluation is unified at 5.625°, and baselines from physical models are provided. The paper notes that reanalysis is not direct observation, and precipitation in particular has limits of quality. The README and the paper differ in how they state capacity and resolution, which must be confirmed from the specific data files.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 去污染与泄漏防范

Separated by contiguous years: the final test is 2017–2018. The training period is no later than 2016, and the paper uses 2016 as validation. The first validation time in the test period should be the start of 2017 plus the forecast lead time, so that input time and target time do not cross the boundary. Highly correlated weather time series cannot be split at random.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

## Data format

### Size

ERA5 hourly data for 1979–2018, with three target grids: 5.625° (32×64), 2.8125° (64×128), and 1.40625° (128×256). The upper-air fields have 13 pressure levels. The README says the full 5.625° package is 175G. Paper v3 says 191GB and miswrites the finest grid as 1.40525°. None of these is silently unified.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 任务形式

Historical and current meteorological fields are given as input, and future global meteorological fields are predicted; the main quantities used for verification are Z500 (500 hPa geopotential) and T850 (850 hPa temperature), and T2M, precipitation, and further variables are also provided. This is not multiple choice, and it is not question answering in natural language.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### Modalities

Numerical meteorological fields in space and time (not natural-language multiple-choice questions); predictions use NetCDF, with dimensions init_time, lead_time, lat, and lon.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### Languages

Not applicable: the core data are numerical meteorological fields with physical units and spatiotemporal coordinates; variable names and documentation use English and do not constitute a natural-language test set.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 难度与类型

Distinguished by forecast lead time and by variable; the main baselines report 3-day and 5-day Z500 and T850. There is no easy or hard label of the kind used in an LLM question bank, and a long lead time is limited by the growth of error and by predictability.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### Public and hidden splits

Public processed ERA5 data cover 1979–2018. The final test is 2017–2018. A contiguous validation segment is recommended to be chosen from 1979–2016, and the paper chooses 2016. Training must not use validation or test targets. The public test is not treated as hidden questions.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

## Evaluation

### Metrics

Z500 RMSE (m²/s²) and T850 RMSE (K), reporting 3-day and 5-day forecasts; the grid, the initial values, and the lead time must be aligned.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 评分

The latitude weight is cos(lat)/mean(cos(lat)). The current score.py by default takes the square root after averaging the weighted squared error over all dimensions. Equation (2) in the paper is written as spatial RMSE for each forecast first, then the average over forecasts. The two aggregation orders differ. Reproduction must fix the code version, mean_dims, and the order of temporal averaging. They are not treated as equivalent. ACC/MAE are also reported.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/src/score.py) (accessed 2026-11-08 ).

### 提示和复现设置

Prompting an LLM does not apply. A prediction is submitted as NetCDF, with the dimensions init_time, lead_time, lat, and lon. Before a score is computed, the fields are aligned on the valid time, and the prediction grid is downsampled to 5.625°. The input variables, the window of history, whether the prediction is direct or iterative, and the data used for pretraining have to be disclosed.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08  ) ; [3](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/src/score.py) (accessed 2026-11-08 ).

### 官方脚本

https://github.com/pangeo-data/WeatherBench/blob/master/src/score.py

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 可比性提示

Forecasts at 3 and 5 days, Z500 and T850, grid resolution, and direct and iterative prediction are kept separate; Z500 is geopotential in m²/s², not geopotential height in m. The historical table in the README includes physical models and CMIP-pretrained models and cannot be taken as a ranking of one architecture. The RMSE formula in the paper and the order of temporal aggregation in the current score.py should also be fixed.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08  ) ; [3](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/src/score.py) (accessed 2026-11-08 ).

## Current status

### 核验时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 数据版本与当前状态

The vertical levels of the old data have been adjusted. They are now 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 850, 925, and 1000 hPa. Derived data from the MPI-ESM-HR historical simulation are also added.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 论文修订与H2证据

- **previous_evidence_note**：2026H2 citation evidence: Spatial Generalization Tests for Machine Learning-based Weather Models to Assess Physical Consistency (arXiv:2607.20716v1) cites WeatherBench/Rasp et al. (2020) in the introduction. That paper's reference authors and its DOI metadata contain a suspicious inconsistency. The title and the citation context are retained, and its author list is not followed.
- **revisions**：- - **version**：v1
    - **date_kst**：2020-02-03
  - - **version**：v2
    - **date_kst**：2020-02-12
  - - **version**：v3
    - **date_kst**：2020-06-12
- **note**：The paper revision time cannot be treated as the data release date. Existing 2026-H2 evidence retains the original collection date.

Sources: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08  ) ; [2](https://arxiv.org/html/2607.20716v1) (accessed 2026-11-07 ).

### 饱和程度

This is a set of weather metrics that have units and for which a smaller error is better, and there is no unified saturation point of the kind represented by 100% accuracy. The older official table still gives the gaps among different physics-based and data-driven baselines; the overall limit of capability in 2026 is not inferred from the historical leaderboard.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08  ) ; [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### 污染、冲突与限制

Temporal autocorrelation requires contiguous validation segments, and a random split would overestimate generalization; training and test must be isolated by the date of the prediction target. ERA5 reanalysis and precipitation are not the same as real observations; CMIP pretraining must be disclosed. Differences in how the paper and the README state capacity and the finest resolution, and differences in aggregation order between the formula in the paper and score.py, are also recorded.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08  ) ; [3](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/src/score.py) (accessed 2026-11-08 ).

### 后续工作与衍生

The official repository recommends moving to WeatherBench 2: the updated data are more comprehensive and easier to access.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

## Leaderboard snapshot

### 快照采集日

2026-11-08

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### Official leaderboard

https://github.com/pangeo-data/WeatherBench#leaderboard

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 第三方覆盖

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### Official README historical table

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Operational IFS | 154.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Operational IFS | 334.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Operational IFS | 1.36 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Operational IFS | 2.03 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Rasp and Thuerey 2020 (direct/continuous) | 268.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Rasp and Thuerey 2020 (direct/continuous) | 499.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Rasp and Thuerey 2020 (direct/continuous) | 1.65 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Rasp and Thuerey 2020 (direct/continuous) | 2.41 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T63 | 268.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T63 | 463.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T63 | 1.85 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T63 | 2.52 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Weyn et al. 2020 (iterative) | 373.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Weyn et al. 2020 (iterative) | 611.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Weyn et al. 2020 (iterative) | 1.98 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Weyn et al. 2020 (iterative) | 2.87 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Clare et al. 2021 (direct) | 375.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Clare et al. 2021 (direct) | 627.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Clare et al. 2021 (direct) | 2.11 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Clare et al. 2021 (direct) | 2.91 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T42 | 489.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T42 | 743.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T42 | 3.09 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | IFS T42 | 3.83 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Weekly climatology | 816.0 m²/s² | Z500 RMSE | None；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Weekly climatology | 3.5 K | T850 RMSE | None；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Persistence | 936.0 m²/s² | Z500 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Persistence | 1033.0 m²/s² | Z500 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Persistence | 4.23 K | T850 RMSE | 3；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Persistence | 4.56 K | T850 RMSE | 5；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Climatology | 1075.0 m²/s² | Z500 RMSE | None；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |
| — | Climatology | 5.51 K | T850 RMSE | None；https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md |

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### Coverage note

The historical table in the full official README was read: 9 methods and 32 original values. Horizons of 3 days and of 5 days, and the two physical variables, are listed in separate columns. A single value for climatology, or for weekly climatology, is not given a lead time that the table does not contain. The original table lists no single date of update, and it does not stand for live SOTA in 2026.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

## Contact

### 公开联系邮箱

- stephan.rasp@tum.de

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### 问题反馈

https://github.com/pangeo-data/WeatherBench/issues

> The issue-feedback entry of the official public repository; no message was sent.

Sources: [1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).

### 官方讨论渠道

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### 隐私与数据使用

Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07 ).

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2002.00469

Source: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08).

### SHA-256

7d60b0fe08c470ee3e7c1985003837a6f21b8b692ae5b0604652da8c642677e4

> Original bytes of the PDF downloaded again. The existing copy was not overwritten.

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### 字节数

5734556

Sources: [1](https://arxiv.org/pdf/2002.00469) (accessed 2026-11-08 ).

### Folder

- **id**：1DrGzbkVTidm6O_FvSVbTgui8CwOFi0DH
- **webViewLink**：

Sources: [1]( 2026-11-07 ).

### Other documents

- - **kind**：中文介绍
  - **id**：1G4dF_ZzXwwKENT_Pq7fZ83060HU-Ha5MByRN08KmnYw
  - **webViewLink**：

Sources: [1]( 2026-11-07 ).

### 原文归档

- **id**：1CoA6xcHxeaeDVqAhG5_Mw5oLdP-K8kGp
- **webViewLink**：

Sources: [1]( 2026-11-07 ).

## Changelog

### 本页修订

- - **date**：2026-11-07
  - **timezone**：
  - **change**：首批官方材料核验、中文改写、；未核实字段显式标记。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：：核对Official README、许可、评测与分任务分数；补2026H2使用证据，区分Paper-fixed experiment和实时榜，保留官方标签冲突。
- - **date**：2026-11-08
  - **timezone**：
  - **round**：2
  - **change**：逐项打开arXiv摘要与PDF全文、Official README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

Sources: [1](https://arxiv.org/abs/2002.00469) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md) (accessed 2026-11-08 ).
