# AstroBench

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

AstroBench

### Full name

AstroBench

Note: The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

### 数据/软件版本

Astrobench_MCQ_v1_Public (a cleaned public set of 3846 questions); kept distinct from the internal experimental set of 4425 questions in the AstroMLab-1 paper.

### Paper version

arXiv v2

### Release date

2024-07-16 03:28:14 (original-paper arXiv v1 submission time)

### Section

Earth and astronomy

Note: Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

### 学科标签

Astronomy

### 许可证与范围

MIT (stated on the official HF dataset card).

### 论文入口

https://arxiv.org/abs/2407.11194

### Paper title

AstroMLab 1: Who Wins Astronomy Jeopardy!?

### Code

Unverified

Status: Unverified (part of this field is still unconfirmed).

### Dataset

https://huggingface.co/datasets/AstroMLab/Astrobench_MCQ_v1_Public

### Official homepage

https://astromlab.org/

## Origin and maintenance

### 发起团队

A multi-institution author team including the Australian National University, The Ohio State University, and others (AstroMLab).

Note: Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

### 署名/合作机构

University of Pennsylvania；Oak Ridge National Laboratory；Hong Kong University of Science and Technology；IIT Patna；Tsinghua University；KEK/QUP；Argonne National Laboratory；Harvard & Smithsonian

Note: Author affiliations on the first page of the original paper; a legal partnership is not claimed from them.

### Authors

Ting, Yuan-Sen；Nguyen, Tuan Dung；Ghosal, Tirthankar；Pan, Rui；Arora, Hardik；Sun, Zechang；de Haan, Tijmen；Ramachandra, Nesar；Wells, Azton；Madireddy, Sandeep；Accomazzi, Alberto

### 维护入口

AstroMLab: a collaborative team of astronomy and AI researchers; the official HF organization maintains the data and model releases.

### 资助与计算资源

Computing resources: NCI, supported by the Australian Government, and the Oak Ridge Leadership Computing Facility Frontier; Microsoft AFMR. Part of the work at Argonne received support from U.S. DOE High Energy Physics and ASCR through SciDAC-RAPIDS2 (DE-AC02-06CH11357).

## Design goals

最重要的变化是补上官方后续论文：4425题原始内部实验与3846题公开清理版之间的差异已有明确清理说明。它主要测试天文知识召回；不能把博士领域定位直接当作原创科研能力证明。

### 测量能力

Measures understanding of astronomy and astrophysics, differences across subfields, and calibration of confidence.

### 为何需要这个基准

Broad tests such as MMLU lack depth of knowledge in astronomy research, and a general average score cannot reflect differences among models within the discipline or cost efficiency; the focus of this test is recall of astronomical knowledge and connections across subfields, not end-to-end ability to do original research.

## Construction

### 材料来源

Multiple-choice questions compiled from articles in the Annual Review of Astronomy and Astrophysics.

### 命题/编制背景

An invited review for ARAA supplies domain-expert knowledge; Gemini-1.5-Pro generates the questions and the explanations, researchers at AstroMLab design the prompts, and human experts spot-check a subset. An author of the review is not the same as the writer of each question.

### Review process

Gemini-1.5-Pro generated 5 questions from each of 885 ARAA surveys, with an explanation and an evidence passage attached; human experts reviewed only a subset. This is not original expert authorship of every question in the full set.

### Quality control

The original paper requires that a question be answerable independently of the source text, that the answer not cite a specific passage, and that the four options be similar in length, with an explanation and a supporting passage attached; experts spot-check. AstroMLab-4 further uses Claude-3.5-Sonnet to remove questions that depend on numbers or methods specific to a paper and revises unnecessary citations, producing 3846 questions.

### 去污染与证据边界

Public questions deliberately omit the answer key, in order to suppress training directly on the answers. The authors of AstroSage report that articles from ARAA sources were excluded from their training corpus. This is a training control for that model. It cannot be generalized into a claim that every model under test is uncontaminated, and it cannot rule out indirect exposure of the questions and of the source knowledge.

## Data format

### 规模与分母

original_internal_experiment：4425；public_cleaned_questions：3846；reason：AstroMLab-4 §4.1 explicitly states that cleaning with Claude-3.5-Sonnet removed questions that depended on the content of a particular article and revised the citations; the train metadata on the HF card has 3846 rows.

### Question types

Four-choice text question answering; the public cleaned set has 3846 questions and does not include the correct-answer key. The older count of 4425 questions in the paper must not be used as the denominator of the public version.

### 模态与字段

Plain-text stems and 4 string options, A/B/C/D; the public card has no image field.

### Languages

English

### 难度定位

The original paper presents the benchmark as doctoral-level knowledge in astronomy; the later AstroMLab-4 explicitly notes that it mainly tests recall of knowledge, and that reasoning modes did not generally raise the scores. A high score cannot be read as a success rate for autonomous astronomy research.

### 公开、隐藏与划分

The HF split named train publishes only the question stem and the options A/B/C/D, and it deliberately omits the correct answer; it is not a fully labeled set for supervised training. Predictions are submitted to the official email address to obtain an evaluation score.

## Evaluation

### Metrics

Multiple-choice accuracy and confidence-calibration analysis.

### 评分流程

The original paper first extracts the JSON answer with a regular expression and, on failure, parses it with GPT-4o. Refusals are removed separately for each model. For the strongest models the effect is at most 0.2% (10/4425), so not every model has a denominator that is strictly fixed and identical. A later cleaned edition is evaluated separately on 3846 questions and should be listed on its own.

### 运行与提示

The original paper uses Instruct and Chat models, requests the answer together with an explanation (CoT) and with JSON, and usually follows the default parameters of the vendor or of HF. RAG is not used. The cleaned edition that followed uses a short system prompt written as an expert in astronomy, and it turns explicit reasoning on when the model supports that setting.

### 评测实现

Unverified

Status: Unverified (part of this field is still unconfirmed).

### 不能混比的设置

The original 4425 questions and the cleaned 3846 questions cannot be mixed. The original paper excludes refusals model by model, and the denominators differ slightly. The 2025-05 table on the HF organization card is an old snapshot and cannot override Table 1 of the AstroMLab-4 revision of 2026-02. Its text says Gemini3Flash is the only model to exceed AstroSage, but in Table 1 GPT-5.2 = 89.4 also exceeds 89.0. This page follows the numeric table and retains the contradiction in the text.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

The public HF release Astrobench_MCQ_v1_Public was opened, and it has 3846 questions; the 2026-02 revision of AstroMLab-4 uses the same cleaned version, and the version in the model paper is not treated as a new data version.

### 版本脉络

original_paper：v1：2024-07-16；v2：2024-11-09；later_evaluation_paper：url：https://arxiv.org/abs/2505.17592；v1：2025-05-23；v2：2026-02-20

### 分数上限与饱和度

Table 1 of AstroMLab-4 in 2026-02 peaks at Gemini 3.0 Flash with 90.3% (3846 questions); errors remain, and a global live SOTA as of 2026-11, or complete saturation, is not declared from this.

### 争议与局限

The public set does not provide answers, in order to reduce contamination; the paper also acknowledges that LLM-synthesized questions may contain historically outdated conclusions or ambiguous wording. Hidden answers are not grounds for inferring that training is free of contamination.

### 衍生版本

The HF organization also lists Astrobench_MCQ_v1_Chinese_Public (the public Chinese version); AstroSage is a family of models under test and is not counted separately as an independent benchmark.

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

https://arxiv.org/pdf/2505.17592

Note: Table 1 of a later paper by the official authors; not a live interactive ranking.

### 第三方/补充实验

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### AstroMLab-4 v2 Table 1: cleaned edition of 3846 questions

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Gemini 3.0 Flash | 90.3 | accuracy (%) |
| 2 | GPT-5.2 | 89.4 | accuracy (%) |
| 3 | AstroSage-Llama-3.1-70B | 89.0 | accuracy (%) |
| 3 | Claude 4.5 Opus | 89.0 | accuracy (%) |
| 5 | Gemini 3.0 Pro | 88.9 | accuracy (%) |

- Gemini 3.0 Flash：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20 (paper revision date, not a per-model run date)；source_type：Historical experiments in the official authors' paper
- GPT-5.2：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20 (paper revision date, not a per-model run date)；source_type：Historical experiments in the official authors' paper
- AstroSage-Llama-3.1-70B：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20 (paper revision date, not a per-model run date)；source_type：Historical experiments in the official authors' paper
- Claude 4.5 Opus：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20 (paper revision date, not a per-model run date)；source_type：Historical experiments in the official authors' paper
- Gemini 3.0 Pro：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20 (paper revision date, not a per-model run date)；source_type：Historical experiments in the official authors' paper

#### AstroMLab-1 v2, Tables 1 and 2: an internal set of 4425 questions (historical).

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Claude-3.5-Sonnet | 85.0 | accuracy (%) |
| 2 | Claude-3.0-Opus | 82.7 | accuracy (%) |
| 3 | LLaMA-3-70B | 80.6 | accuracy (%) |
| 4 | GPT-4o | 80.4 | accuracy (%) |

- Claude-3.5-Sonnet：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：Original-paper historical experiment
- Claude-3.0-Opus：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：Original-paper historical experiment
- LLaMA-3-70B：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：Original-paper historical experiment
- GPT-4o：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：Original-paper historical experiment

### 覆盖边界

Priority is given to transcribing Table 1 of the AstroMLab-4 revision of 2026-02-20, and the original internal set of 2024 is kept as an independent historical track. The figure of 119 models is the number covered by that paper, not 119 of the latest models already evaluated as of 2026-11. Old scores on the HF organization card are not ranked together with the new table.

## Contact

### 公开作者工作邮箱

astromachinelearninglab@gmail.com

### 公开反馈

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 官方账号

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected.

## Original files

### 原文PDF

https://arxiv.org/pdf/2407.11194

### 下载源文件SHA-256

b31348a943177637d2e96d698974d5566a42a33f06e7c4a5772f2104984e074e

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

10805582

### 既有 PDF链接

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首批官方材料核验、中文改写、；未核实字段显式标记。
- 2026-11-07：深度优化：打开Official README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- 2026-11-07：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

### 来源索引

[1]: https://arxiv.org/abs/2407.11194 "访问 2026-11-07"
[2]: https://arxiv.org/pdf/2407.11194 "访问 2026-11-07"
[3]: https://huggingface.co/datasets/AstroMLab/Astrobench_MCQ_v1_Public "访问 2026-11-07"
[4]: https://arxiv.org/pdf/2505.17592 "访问 2026-11-07"
[5]: https://huggingface.co/AstroMLab "访问 2026-11-07"
[6]: https://arxiv.org/html/2407.11194v2 "访问 2026-11-07"
[7]: https://arxiv.org/abs/2505.17592 "访问 2026-11-07"
[8]: urn:benchmark-atlas:constitution:v0.1 "访问 2026-11-07"
[9]: "访问 2026-11-07"
[10]: "访问 2026-11-07"
[11]: "访问 2026-11-07"
