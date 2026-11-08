# ARC-Challenge

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

ARC-Challenge

### Full name

AI2 Reasoning Challenge — Challenge Set

### 数据/软件版本

ARC-Challenge (2018); ARC-Easy is not included.

### Paper version

arXiv v1

### Release date

2018-03-15 02:04:21 (time of the arXiv v1 submission; not the time at which the data went online on its own)

### Section

Reasoning

### 学科标签

Scientific common sense and compositional reasoning

### 许可证与范围

dataset：CC-BY-SA-4.0 (marked in the header of the allenai/ai2_arc card; the license section of the card body is still More Information Needed, and the conflict is retained)；baseline_code：Apache-2.0（arc-solvers/LICENSE）

### 论文入口

https://arxiv.org/abs/1803.05457

### Paper title

Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge

### Code

https://github.com/allenai/arc-solvers

### Dataset

https://huggingface.co/datasets/allenai/ai2_arc

### Official homepage

http://data.allenai.org/arc

## Origin and maintenance

### 发起团队

Allen Institute for AI

### 署名/合作机构

The only affiliation named for every author of the original paper is the Allen Institute for Artificial Intelligence; this field records the institution that is named in public, and a legal collaboration that is not listed is not inferred from it.

### Authors

Clark, Peter；Cowhey, Isaac；Etzioni, Oren；Khot, Tushar；Sabharwal, Ashish；Schoenick, Carissa；Tafjord, Oyvind

### 维护入口

The official AllenAI data-release account allenai and the arc-solvers repository; these are public-release entry points for maintenance and are not used to infer current staffing.

### 资助与计算资源

Unverified

Note: Paper acknowledgments and current operational funding were not verified item by item; institutional affiliation is not a funding source

Status: Unverified (part of this field is still unconfirmed).

## Design goals

它衡量的是自然科学考试选择题上的知识与组合推理，不是视觉ARC-AGI，也不是科研自动化。Challenge源于2018检索/PMI基线筛选，难度定义不随2026模型自动更新。

### 测量能力

Measures, on basic-science examination questions, knowledge integration and reasoning beyond retrieval and word co-occurrence.

### 为何需要这个基准

Existing choice question answering may be solved by information retrieval or lexical statistics, and can hardly measure deeper reasoning on its own.

## Construction

### 材料来源

Multiple-choice questions from science examinations in grades 3 through 9 are collected; questions answered incorrectly by both the retrieval baseline and the PMI baseline enter Challenge.

### 命题/编制背景

The original examination item writers and the AI2 curation team; not entirely synthesized by an LLM.

### Review process

Questions were cleaned and filtered with two baselines; questions that must depend on an image in order to be answered are not included.

### Quality control

Multiple scientific disciplines and reasoning demands are retained, and the original paper additionally provides about 14,000,000 sentences of scientific corpus for retrieval.

### 去污染与证据边界

Easy/Challenge is divided according to baseline performance and does not constitute isolation from pretraining corpora; examination questions may already be public on the web.

## Data format

### 规模与分母

ARC-Challenge: train 1119, validation 299, and test 1172, 2590 questions in all; the 7787 questions of the full ARC, or ARC-Easy, must not be substituted for it.

### Question types

Multiple-choice questions in science, given as text, mostly with 4 options and some with 3 to 5 options.

### 模态与字段

Text (mathematical symbols expressed as text); not an original image or video recognition task

### Languages

English question text; for formal or mathematical notation, see the modality and the repository format

### 难度定位

Challenge only denotes the set screened out by the original retrieval model and the PMI model; it is not a fixed 2026 frontier difficulty.

### 公开、隐藏与划分

Public training, development, and test question files; the test set in common modern use has 1172 questions.

## Evaluation

### Metrics

Answer accuracy; the original paper allows a score of 1/k for tied predictions.

### 评分流程

The original tie-credit implementation differs from modern generated-answer accuracy and from log-likelihood acc_norm, so the evaluator settings must be retained.

### 运行与提示

The original paper includes retrieval and supervised QA systems; an LLM needs to report the number of shots, whether CoT is used, whether retrieval is used, and length normalization of the likelihood.

### 评测实现

The official arc-solvers repository provides scripts/evaluate_solver.sh and scripts/evaluate_bidaf.sh. These are historical baselines for retrieval, entailment, and reading comprehension, not a unified prompting protocol for modern LLMs.

### 不能混比的设置

ARC-Challenge is a separate benchmark from ARC-Easy and from the visual abstract-reasoning benchmark ARC-AGI; results on 1172 questions and on the combined 3548 questions cannot be placed on one ranking.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

ARC-Challenge (2018); ARC-Easy is not included.

### 版本脉络

paper：v1；submitted_at：2018-03-15；later_use：report：https://arxiv.org/html/2610.11978v1；scope：ARC-Challenge; distinct from the combined ARC-Easy+Challenge set of 3548 questions

### 分数上限与饱和度

Table 2 of the Jev report lists, on ARC-Challenge, Jev at 97.6% and Gemini 3.8 Flash at 97.5%. The head of the listed protocol is already close to a full score. This is not a comprehensive audit of contamination, and it is not a single conclusion of saturation under every prompt setting.

### 争议与局限

Old examination questions and public answers carry a contamination risk; a high score cannot by itself prove that a system has broad scientific-research ability.

### 衍生版本

ARC-Easy, in the same family, is split out on its own; this entry includes only Challenge and is not counted again.

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

http://data.allenai.org/arc

### 第三方/补充实验

https://arxiv.org/html/2610.11978v1

Note: An experimental comparison in the paper, not a continuously updated official leaderboard from an independent third party.

### 分轨成绩

#### Jev report, Table 2: Jev+six frontier LLMs, ARC-Challenge.

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Jev | 97.6 | accuracy (%) |
| 2 | Gemini 3.8 Flash | 97.5 | accuracy (%) |
| 3 | Qwen3.8-Flash | 96.2 | accuracy (%) |
| 4 | DeepSeek-V4.1-Flash | 95.9 | accuracy (%) |
| 5 | GPT-5.6 Sol | 95.1 | accuracy (%) |
| 6 | Claude Opus 5.5 | 94.8 | accuracy (%) |
| 7 | Qwen3.8-Max | 91.4 | accuracy (%) |

- Jev：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.
- Gemini 3.8 Flash：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.
- Qwen3.8-Flash：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.
- DeepSeek-V4.1-Flash：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.
- GPT-5.6 Sol：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.
- Claude Opus 5.5：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.
- Qwen3.8-Max：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：Research-report experiments; not the current AllenAI leaderboard；protocol：Judged by the option; for the specific model prompt, see the report; older models under a different protocol, cited in its appendix, are not ranked together with these.

#### Original 2018 paper, Table 6: Challenge test, 1172 questions.

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | DGEM | 27.11 | tie-credit accuracy (%) |
| 2 | TableILP | 26.97 | tie-credit accuracy (%) |
| 3 | BiDAF | 26.54 | tie-credit accuracy (%) |

- DGEM：source_url：https://arxiv.org/pdf/1803.05457；accessed：2026-11-07；source_type：Original-paper historical baseline
- TableILP：source_url：https://arxiv.org/pdf/1803.05457；accessed：2026-11-07；source_type：Original-paper historical baseline
- BiDAF：source_url：https://arxiv.org/pdf/1803.05457；accessed：2026-11-07；source_type：Original-paper historical baseline

### 覆盖边界

The tracks are shown separately: Jev and six frontier models in the Jev report, kept apart from the original baselines of 2018. No leaderboard that could be read was obtained from the old official site. A front rank on an official AllenAI leaderboard of 2026 is not claimed. Table 2 of the Jev report also lists representative models, and some of those scores are carried over from an outside source. They are not ranked together with the models that were measured.

## Contact

### 公开作者工作邮箱

peterc@allenai.org；isaacc@allenai.org；orene@allenai.org；tushark@allenai.org；ashishs@allenai.org；carissas@allenai.org；oyvindt@allenai.org

Note: The original paper's first page publishes the authors' work email; it is a 2018 historical contact, and no email is sent to verify that it remains valid.

### 公开反馈

https://github.com/allenai/arc-solvers/issues

### 官方账号

Unverified

Note: No dedicated official social account has been verified, and personal accounts of the same name are not included

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Note: A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://arxiv.org/pdf/1803.05457

### 下载源文件SHA-256

b24b722c93f304df6c3b4a48ebbe429e836f3b3e80837bb613112398e59bde43

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

290564

### 既有 PDF链接

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
- 2026-11-07（）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

### 来源索引

[1]: https://arxiv.org/abs/1803.05457 "访问 2026-11-07"
[2]: http://data.allenai.org/arc "访问 2026-11-07"
[3]: https://huggingface.co/datasets/allenai/ai2_arc "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/allenai/arc-solvers/master/LICENSE "访问 2026-11-07"
[5]: https://arxiv.org/pdf/1803.05457 "访问 2026-11-07"
[6]: https://raw.githubusercontent.com/allenai/arc-solvers/master/README.md "访问 2026-11-07"
[7]: https://huggingface.co/datasets/allenai/ai2_arc/raw/main/README.md "访问 2026-11-07"
[8]: https://arxiv.org/html/2610.11978v1 "访问 2026-11-07"
[9]: https://github.com/allenai/arc-solvers "访问 2026-11-07"
[10]: "访问 2026-11-07"
[11]: "访问 2026-11-07"
