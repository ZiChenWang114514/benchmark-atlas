# AstroMMBench

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

AstroMMBench

### Full name

AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy

### 数据/软件版本

2026 formal journal version (592 questions)

### Paper version

arXiv v2 (2025-10-22 01:29:47) is the preprint of 621 questions; Universe 12(10),296 (2026-09-30) is the official version of 592 questions.

### Release date

2025-09-29 17:02:30 (arXiv v1); 2026-09-30 is the date of formal publication in Universe, not the date of first proposal.

### Section

Earth and astronomy

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

### 学科标签

Multimodal question answering on astronomy research images

### 许可证与范围

hf_card：The README marks apache-2.0；preprint_promise：The Ethics Statement of the 2025 preprint says a CC-BY-4.0 release is planned；journal_restriction：The 2026 official paper states explicitly that reuse of the original figures and text is subject to the license of each arXiv submission.

Note: Three official statements disagree in scope and in time. The overall HF label cannot erase rights in the original images; no README or LICENSE file was found at the root of the code repository, and the license of the code remains Unverified.

Status: Unverified (part of this field is still unconfirmed).

### 论文入口

https://www.mdpi.com/2218-1997/12/10/296

### Paper title

AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy

### Code

https://github.com/Shijinghang/benchmark_pipeline

### Dataset

https://huggingface.co/datasets/sjh11/AstroMMBench

### Official homepage

https://www.mdpi.com/2218-1997/12/10/296

## Origin and maintenance

### 发起团队

Author team from the National Astronomical Observatories of the Chinese Academy of Sciences, the University of Chinese Academy of Sciences, Zhejiang Lab, and Tianjin University; author affiliations are not the same as legal ownership.

### 署名/合作机构

University of Chinese Academy of Sciences, Zhejiang Lab, and Tianjin University (author affiliations).

### Authors

Jinghang Shi；Xiaoyu Tang；Yang Huang；Yuyang Li；Yanxia Zhang；Xiao Kong；Caizhan Yue；A-Li Luo

### 维护入口

The official release accounts Shijinghang/benchmark_pipeline and sjh11/AstroMMBench.

### 资助与计算资源

NSFC 12273076, 12203077, 12373110, and 12133001; National Key R&D Program 2025YFA1614101; crewed spaceflight CMS-CSST-2025-A06; Hebei Natural Science Foundation A2024205020.

## Design goals

应同时保留2025年621题预印本和2026年592题正式版。正式版更明确讨论训练暴露、单主审和统计区间限制，分数变化首先是题集/协议变化，不能直接解释为模型进步。

### 测量能力

Read astronomical research charts, instrument diagrams, and observational images, and answer specialized physics questions.

### 为何需要这个基准

General VQA cannot cover the conventions of astronomical images or domain reasoning; it is complementary to text AstroLLM and to cross-modal representation learning.

## Construction

### 材料来源

From 3592 arXiv astro-ph papers dated 2024-01-01 to 2024-07-31, 19,299 figure-text pairs were extracted; LLaMA3.3-70B-Instruct organizes the text, and InternVL2.5-78B generates four-choice candidates.

### 命题/编制背景

15 reviewers from the National Astronomical Observatories: 8 astronomy doctoral students, 5 master's students, and 2 professors; questions are assigned by research area.

### Review process

Five text-only LLMs each answer 5 times, and a model is judged able to answer when it is correct at least 3 times; a question is discarded when at least two models are able to answer it. From the remaining 9677 questions, 1800 are drawn for expert review, and 592 are kept.

### Quality control

Experts check scientific correctness, correspondence between figure and question, sufficiency of context, uniqueness of the answer, and the distractors. Each question has one lead reviewer, who can see the answer and the caption; there is no independent double review and no agreement statistic.

### 去污染与证据边界

## Data format

### 规模与分母

592 four-choice questions: GA97, CO108, EP97, HE101, IM83, and SR106; 25 MLLMs (22 open, 3 closed-source). The old summary of 621 questions cannot be mixed with the formal version.

### Question types

Image + question + four options, with a single correct answer.

### 模态与字段

Figures, charts, and text from astronomical research; not analysis of raw FITS time series.

### Languages

English.

### 难度定位

Six subfields; cosmology has the lowest mean score, and the high-energy field has the largest variance among models, so it should not be called the hardest in every case.

### 公开、隐藏与划分

The HF card explicitly states a final 592 questions; the paper fixes the same 592 questions for every model. This differs from the early arXiv version of 621 questions; the naming of an independent train/validation/test split and the answer-hiding policy remain Unverified.

Status: Unverified (part of this field is still unconfirmed).

## Evaluation

### Metrics

Four-choice accuracy; the overall denominator is fixed at 592, and subfields are computed from their own question counts.

### 评分流程

A single letter from A–D is exact-matched first; other free answers are given to a fixed binary judge, DeepSeek-V3. A failure to parse, an illegal output, or an API failure counts as wrong and is not removed from the denominator.

### 运行与提示

VLMEvalKit 0.2. The input is an image, a question stem, and four labeled options. The specific text and the judge prompts are in Supplementary File S1. Image processing follows each model's adapter and is not a single fixed resolution.

### 评测实现

https://github.com/Shijinghang/benchmark_pipeline

### 不能混比的设置

Effective image input size is not unified across the board; the intervals at the top overlap, and a point estimate cannot be treated as a significant ranking. Paired tests and repeated runs are required.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

The 2026 official edition has 592 questions; the version follows the scope of this official paper.

### 版本脉络

arxiv_v1：2025-09-29；arxiv_v2：2025-10-22；preprint_questions：621；journal_publication：2026-09-30；journal_questions：592；version_boundary：Question counts, author tables, and scores change with the official version; this is not a simple renaming that keeps the same denominator.

### 分数上限与饱和度

The highest point estimate in this group is 71.28%; the paper considers the benchmark unsaturated. The Wilson 95% intervals of the top three overall accuracies overlap, so a small gap cannot be read as a significant advantage or disadvantage.

### 争议与局限

Public arXiv sources may enter model pretraining. A single lead reviewer, visible answers and captions, a single-institution review panel, and the lack of repeated runs all limit interpretation of the score.

### 衍生版本

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

https://www.mdpi.com/2218-1997/12/10/296#table_body_display_universe-12-00296-t002

### 第三方/补充实验

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### 2026 Universe Table 2: official edition of 592 questions

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Ovis2-34B | 71.28 | accuracy (%) |
| 2 | ChatGPT-4o | 69.76 | accuracy (%) |
| 3 | Doubao-1.5-vision-pro | 69.09 | accuracy (%) |
| 4 | InternVL3-38B | 68.24 | accuracy (%) |
| 4 | Qwen2.5-VL-72B | 68.24 | accuracy (%) |

- Ovis2-34B：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：Fixed experiments in the official original paper；dataset_size：592
- ChatGPT-4o：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：Fixed experiments in the official original paper；dataset_size：592
- Doubao-1.5-vision-pro：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：Fixed experiments in the official original paper；dataset_size：592
- InternVL3-38B：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：Fixed experiments in the official original paper；dataset_size：592
- Qwen2.5-VL-72B：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：Fixed experiments in the official original paper；dataset_size：592

#### 2025 arXiv v2 Table 1: historical edition of 621 questions

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Ovis2-34B | 70.53 | accuracy (%) |
| 2 | ChatGPT-4o | 69.07 | accuracy (%) |
| 3 | Doubao-1.5-vision-pro | 68.12 | accuracy (%) |

- Ovis2-34B：source_url：https://arxiv.org/pdf/2510.00063v2；accessed：2026-11-07；source_type：Historical experiments from the official preprint；dataset_size：621
- ChatGPT-4o：source_url：https://arxiv.org/pdf/2510.00063v2；accessed：2026-11-07；source_type：Historical experiments from the official preprint；dataset_size：621
- Doubao-1.5-vision-pro：source_url：https://arxiv.org/pdf/2510.00063v2；accessed：2026-11-07；source_type：Historical experiments from the official preprint；dataset_size：621

### 覆盖边界

The official 592 questions and the historical 621 questions are on separate tracks, and the exact table values are kept; the OpenCompass column is a general multimodal comparison, not a third-party rerun score for AstroMMBench. A request for README and LICENSE at the root returned 404, and the journal HTML returned 403; the official PDF, the HF card, and the full text of the original arXiv paper were all actually read.

## Contact

### 公开作者工作邮箱

tangxiaoyu@zhejianglab.org；zyx@bao.ac.cn

### 公开反馈

https://github.com/Shijinghang/benchmark_pipeline/issues

### 官方账号

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf

### 下载源文件SHA-256

5098322dcf0f8cbccdc5682a22fa6a4565c73464ef54937174540916f5f05a0c

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

7134595

### 既有 PDF链接

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：：核对Official README、许可、评测与分任务分数；补2026H2使用证据，区分Paper-fixed experiment和实时榜，保留官方标签冲突。
- 2026-11-07（）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

### 来源索引

[1]: https://www.mdpi.com/2218-1997/12/10/296 "访问 2026-11-07"
[2]: https://arxiv.org/abs/2510.00063 "访问 2026-11-07"
[3]: https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf "访问 2026-11-07"
[4]: https://huggingface.co/datasets/sjh11/AstroMMBench "访问 2026-11-07"
[5]: https://arxiv.org/pdf/2510.00063v2 "访问 2026-11-07"
[6]: https://github.com/Shijinghang/benchmark_pipeline "访问 2026-11-07"
[7]: "访问 2026-11-07"
