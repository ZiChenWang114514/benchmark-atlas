# BAISBench

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

BAISBench

Sources: [1]

### Full name

Biological AI Scientist Benchmark (BAISBench; the repository README still calls it AISBench)

Sources: [2][3][4]

### 数据/软件版本

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### Paper version

v2; latest paper date 2026-01-18

Sources: [1]

### Release date

2025-05-13 16:33:54 (first submission of arXiv v1).

Sources: [1]

### Section

Biology and medicine

Sources: [5]

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

### 学科标签

Omics-data-driven scientific-discovery agent

Sources: [5]

### 许可证与范围

code：MIT（Copyright 2025 Erpai Luo）；hf_dataset_card：Apache-2.0; the license of each underlying research h5ad must be observed separately

Sources: [6][3]

### 论文入口

https://arxiv.org/abs/2505.08341

Sources: [1]

### Paper title

Benchmarking AI scientists for omics data driven biological discovery

Sources: [1]

### Code

https://github.com/EperLuo/BAISBench

Sources: [1]

### Dataset

https://huggingface.co/datasets/EperLuo/BaisBench

Sources: [1]

### Official homepage

https://github.com/EperLuo/BAISBench

Sources: [1]

## Origin and maintenance

### 发起团队

The lead author credit is the bioinformatics team at Tsinghua University, and researchers from Beijing Jiaotong University and Capital Medical University are included. Attribution follows author affiliations and is not used to infer a separate formal legal agreement on who leads.

Sources: [2]

### 署名/合作机构

清华大学自动化系/BNRIST生物信息学团队；北京交通大学软件学院；首都医科大学基础医学院生理与病理生理系；清华大学合成与系统生物学中心

Sources: [2]

Note: A list of credited institutions, not inferred joint ownership.

### Authors

Luo, Erpai；Jia, Jinmeng；Xiong, Yifan；Li, Xiangyu；Guo, Xiaobo；Yu, Baoqi；Hao, Minsheng；Wei, Lei；Zhang, Xuegong

Sources: [1]

### 维护入口

Data accounts EperLuo/BAISBench and EperLuo/BaisBench.

Sources: [1]

### 资助与计算资源

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Design goals

这是已发表生物研究的再发现与细胞注释诊断，不是衡量新发现原创性。官方Notebook藏有可精确抄录的保存输出，但Pantheon只算6器官，必须独立于15器官宏平均和193题科学发现分数。
Sources: [1][1]

### 测量能力

From single-cell omics data to cell annotation and reproduction of research conclusions, evaluating an AI scientist.

Sources: [1]

### 为何需要这个基准

Ordinary question answering or code generation cannot confirm that an agent can reproduce a biological discovery on real omics data.

Sources: [1]

## Construction

### 材料来源

Public single-cell studies and CellxGene h5ad; BAIS-SD comes from the published conclusions of 41 studies.

Sources: [1]

### 命题/编制背景

Annotation by bioinformatics experts and human references from graduate students; 6 graduate students in bioinformatics take part in the comparison.

Sources: [1]

### Review process

Experts annotate the cell-type hierarchy; GPT-4o helps draft questions from paper conclusions, with manual correction and experimental checks.

Sources: [1]

### Quality control

The data are unified as h5ad; cell-type hierarchies are aligned with uHAF, and an exact type or a finer descendant type receives full credit. Official Task1 provides the mapping and the scoring implementation, and Task2 provides the questions and the reference answer. The human baseline was completed by 6 graduate students sharing the work, not by each person independently repeating the full set.

Sources: [2][7][8]

### 去污染与证据边界

The source studies and their conclusions are public, and the work is mainly rediscovery rather than genuinely unknown discovery; answers that rely on memory of the papers call for caution.

Sources: [1]

## Data format

### 规模与分母

BAIS_DPTA：datasets：15；evidence：HF BAISBench_task1.csv was checked row by row against 15 organ and tissue datasets; the typeset list in appendix S1 is not used as the basis for a reduced denominator；BAIS_SD：questions：193；studies：41；metadata_note：The 56 rows on the HF card are metadata records, not the total number of questions.

Sources: [3][9][2]

### Question types

Cell-type annotation, and single-choice or multiple-choice reproduction of conclusions drawn from omics data.

Sources: [1]

### 模态与字段

h5ad expression matrices, cell metadata, code, and answers in text or by choice.

Sources: [1]

### Languages

English research questions and biological identifiers; data-driven.

Sources: [1]

### 难度定位

Analysis of real research data; reproducing a published conclusion is distinct from an original discovery.

Sources: [1]

### 公开、隐藏与划分

The Task1/Task2 notebooks and the HF container provide the data; the Task2 README explicitly includes the reference answer. The design of a hidden test remains Unverified, and it cannot be said that every answer is hidden.

Sources: [4]

## Evaluation

### Metrics

DPTA expert uHAF hierarchical scores; SD is scored by single-choice and multiple-choice correctness.

Sources: [1]

### 评分流程

DPTA: a score of 1 is given when the type matches the reference type or is a descendant of it, 0.5 for the parent class, and 0.2 for the grandparent class. The code excludes reference Unclassified cells, scores each organ, and then takes the macro average. SD: 1 for a correct single choice; for a multiple choice, 1 if entirely correct and 0.5 if only partly correct and with no error; otherwise 0. The uHAF name-mapping procedure also affects reproduction.

Sources: [2][7][8]

### 运行与提示

Five AI scientist systems are compared, with six graduate students as a reference; the system tools and the model configuration must be retained with the score.

Sources: [1]

### 评测实现

Task1.ipynb downloads the data and evaluates data processing and cell annotation; Task2.ipynb provides the research background, multiple-choice questions, and reference answers, and the paper notes that they can be adjusted to the AI scientist under test.

Sources: [4]

### 不能混比的设置

In the saved Task1 output, Pantheon runs only organ_list[:6]. Its mean of 0.4207667294406579 must not be mixed into the 15-organ overall leaderboard, and it must not be used to reject the paper's statement that STELLA leads. For Task2, only Biomni's exactly saved output is currently available. Other bar heights in the paper's figure are not estimated by reading the figure. DPTA's 0–1 macro-average and SD's percentage scale are not compared by mixing them.

Sources: [7][8][2]

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

Sources: [1]

### 当前发布

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 版本脉络

v1：2025-05-13；v2：2026-01-18；scope：Official releases and reproduction notebooks for the two tasks; a citation does not mean that others reran them.

Sources: [1][4]

### 分数上限与饱和度

Both the paper and the Notebook show that a clear gap remains in cell annotation; the verified saved mean for STELLA across 15 organs is 0.39986219727575084, and the saved SD for Biomni is 136/193. These are public historical reproduction outputs, not the latest real-time ceiling across all models.

Sources: [7][8][2]

### 争议与局限

The repository name AISBench and the paper and HF name BAISBench coexist. Scientific discovery here means recovering published research conclusions, and it does not directly quantify novel discovery. Task2 explicitly makes the reference answer public, so memorizing only the answer must be guarded against. The HF task1 CSV confirms 15 datasets. Pantheon in the notebook covers only 6 organs and cannot be ranked on the 15-organ overall leaderboard.

Sources: [4][9][7][8][2]

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

https://github.com/EperLuo/BAISBench；https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task2.ipynb

Sources: [4][7][8]

### 第三方/补充实验

Unverified

Sources: [1]

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### Saved output of the official Task1.ipynb: DPTA, 15 organs

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | STELLA | 0.39986219727575084 | hierarchical annotation macro score (0–1) |
| 2 | Human with GPT-4o | 0.3477723428012859 | hierarchical annotation macro score (0–1) |
| 3 | Biomni | 0.2437880291331723 | hierarchical annotation macro score (0–1) |
| 4 | scChat | 0.15367114184342404 | hierarchical annotation macro score (0–1) |
| 5 | AutoBA | 0.0 | hierarchical annotation macro score (0–1) |

- STELLA：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：Existing output in the official reproduction notebook; not rerun；n_organs：15
- Human with GPT-4o：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：Existing output in the official reproduction notebook; not rerun；n_organs：15
- Biomni：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：Existing output in the official reproduction notebook; not rerun；n_organs：15
- scChat：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：Existing output in the official reproduction notebook; not rerun；n_organs：15
- AutoBA：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：Existing output in the official reproduction notebook; not rerun；n_organs：15

#### Saved output of the official Task1.ipynb: DPTA, first 6 organs only

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Pantheon | 0.4207667294406579 | hierarchical annotation macro score (0–1) |

- Pantheon：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：Reproduction outputs for a subset of organs; they do not constitute a full ranking；n_organs：6

#### Saved output of the official Task2.ipynb: SD, 193 questions

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Biomni | 70.46632124352331 | 100 point scale |

- Biomni：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task2.ipynb；accessed：2026-11-07；source_type：Saved output from the official reproduction notebook; not a live leaderboard；total_score：136.0；questions：193

Sources: [7][8]

### 覆盖边界

The saved outputs of two official Notebooks were actually read, and the bars in the figures of the paper are not estimated. The three tracks, DPTA15 organs, Pantheon6 organs, and SD193 questions, are kept separate; rank is ordered only among entries on the same track that have already been transcribed on this page, and it cannot be called the complete real-time ranking of the project. The Notebooks do not state the date of each run, and the collection date is not the experiment date. Exact figures for the other systems in the paper remain Unverified.

Sources: [7][8][2]

## Contact

### 公开作者工作邮箱

zhangxg@tsinghua.edu.cn

Sources: [1]

### 公开反馈

https://github.com/EperLuo/BAISBench/issues

Sources: [10]

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

https://arxiv.org/pdf/2505.08341

Sources: [1]

### 下载源文件SHA-256

72b6410e415b16c9de82f8bab63ba68978a3ecc735231b2b20ddaa5f7378ebc8

Sources: [2]

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

2666576

Sources: [2]

### 既有文件夹

id：1UnT52NfQw39t6FVzCs21Y3-XVIzVzNJC；webViewLink：

Sources: [1]

### 其他材料

- type：中文介绍；id：1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg；webViewLink：https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit

Sources: [11]

### 既有 PDF链接

id：1LLtrgHSJRkbgGS7FUtvJBdDl3mdbYPlo；webViewLink：

Sources: [1]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：深度优化：打开Official README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- 2026-11-07（ ()）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

Sources: [1]

### 来源索引

[1]: https://arxiv.org/abs/2505.08341 "访问 2026-11-07"
[2]: https://arxiv.org/pdf/2505.08341 "访问 2026-11-07"
[3]: https://huggingface.co/datasets/EperLuo/BaisBench "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/README.md "访问 2026-11-07"
[5]: https://arxiv.org/html/2610.21074v1 "访问 2026-11-07"
[6]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/LICENSE "访问 2026-11-07"
[7]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb "访问 2026-11-07"
[8]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task2.ipynb "访问 2026-11-07"
[9]: https://huggingface.co/datasets/EperLuo/BaisBench/resolve/main/BAISBench_task1.csv "访问 2026-11-07"
[10]: https://github.com/EperLuo/BAISBench "访问 2026-11-07"
[11]: https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit "访问 2026-11-07"
