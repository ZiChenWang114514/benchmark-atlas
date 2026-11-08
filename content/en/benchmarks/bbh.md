# BIG-Bench Hard (BBH)

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

BIG-Bench Hard (BBH)

Sources: [1]

### Full name

BIG-Bench Hard

Sources: [1]

### 数据/软件版本

Public task set from 2022; the repository commit is not pinned

Sources: [2][1]

### Paper version

arXiv v1

Sources: [1]

### Release date

2022-10-18 01:08:26 (first submission of arXiv v1).

Sources: [1]

### Section

Reasoning

Sources: [2]

### 学科标签

Multi-task complex reasoning

Sources: [1]

### 许可证与范围

The LICENSE of the repository is MIT (Copyright 2022 suzgunmirac). The wording of what it applies to is software and documentation. It is not expanded, on its own, into one license for the original tasks of BIG-Bench or for the paper.

Sources: [3]

### 论文入口

https://arxiv.org/abs/2210.09261

Sources: [1]

### Paper title

Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them

Sources: [1]

### Code

https://github.com/suzgunmirac/BIG-Bench-Hard

Sources: [2]

### Dataset

https://github.com/suzgunmirac/BIG-Bench-Hard

Sources: [2][1]

### Official homepage

https://github.com/suzgunmirac/BIG-Bench-Hard

Sources: [2][1]

## Origin and maintenance

### 发起团队

Google Research, Stanford University (institutions named on the paper)

Sources: [1]

### 署名/合作机构

Google Research；Stanford University

Sources: [4]

Note: Author affiliations on the paper; not a funding or collaboration agreement confirmed separately.

### Authors

Suzgun, Mirac；Scales, Nathan；Schärli, Nathanael；Gehrmann, Sebastian；Tay, Yi；Chung, Hyung Won；Chowdhery, Aakanksha；Le, Quoc V.；Chi, Ed H.；Zhou, Denny；Wei, Jason

Sources: [1]

### 维护入口

The public data, the CoT examples, and the Codex outputs are released and maintained by suzgunmirac/BIG-Bench-Hard, following the source of the Google Research/Stanford author team.

Sources: [5][4]

### 资助与计算资源

Unverified

Sources: [1]

Note: Paper acknowledgments and current operational funding were not verified item by item; institutional affiliation is not a funding source

Status: Unverified (part of this field is still unconfirmed).

## Design goals

23任务是论文等权平均的单位，27个JSON子任务和6511道题是发布组织方式；换成所有题微平均会改变权重。3-shot直接回答、CoT、slow/fast-thinking和基础模型不能混排。
Sources: [1][1]

### 测量能力

Measures compositional logic, symbolic manipulation, execution of algorithms, and multi-step reasoning, and whether an explicit chain of thought can improve these abilities.

Sources: [1]

### 为何需要这个基准

A BIG-Bench multi-task average can mask hard problems; this study selects tasks on which language models previously still lagged humans and measures the reasoning bottleneck separately.

Sources: [1]

## Construction

### 材料来源

From the 209 tasks in BIG-Bench, 23 task categories were selected by question count, suitability for automatic scoring, and earlier model performance relative to humans; some tasks were subdivided, forming 27 evaluation subtasks.

Sources: [1]

### 命题/编制背景

It inherits BIG-Bench community tasks; BBH researchers select them and handwrite chain-of-thought demonstrations for each task type.

Sources: [1]

### Review process

Filtered by the human baseline and by earlier model results; this is not a new examination originally written, question by question, by experts.

Sources: [1]

### Quality control

Each subtask is limited to at most 250 questions, so that a large task does not dominate the comparison; most have 250 questions, with causal_judgement at 187, penguins_in_a_table at 146, and snarks at 178.

Sources: [1]

### 去污染与证据边界

The paper includes warnings about evaluation contamination and measures for identifying it; public tasks cannot, on that basis, guarantee that future models have no training contamination.

Sources: [1]

## Data format

### 规模与分母

23 task categories and 27 subtasks, 6511 evaluation questions in total; the statistical definition is the BBH used in the original paper.

Sources: [1]

### Question types

Multiple choice, Boolean judgments, short answers, and string output, varying by subtask.

Sources: [1]

### 模态与字段

Text (mathematical symbols expressed as text); not an original image or video recognition task

Sources: [1]

### Languages

English question text; for formal or mathematical notation, see the modality and the repository format

Sources: [1]

### 难度定位

Filtered by earlier models scoring below the human baseline; this is a definition of relative difficulty, not a unified grade or difficulty level.

Sources: [1]

### 公开、隐藏与划分

Public evaluation questions, and 3 human CoT examples per task; the examples should not be counted in the number of evaluation questions.

Sources: [1]

## Evaluation

### Metrics

Exact-match accuracy of the final answer; it is also reported by task, and all questions are not pooled directly into a single score.

Sources: [1]

### 评分流程

The final answer is extracted and compared with the target answer; the original paper compares direct answering with chain-of-thought prompts.

Sources: [1]

### 运行与提示

The original paper uses 3-shot examples, compares the setting with and without CoT, and uses greedy decoding at temperature 0; context and output format must be recorded separately for different models.

Sources: [1]

### 评测实现

The official repository releases the questions under bbh/, prompts of three examples under cot-prompts/, and code-davinci-002-outputs/. The README does not give one runner for modern LLMs. The repository itself cannot be described as a scoring script that has already been verified for every model.

Sources: [5]

### 不能混比的设置

The task macro-average and the all-question micro-average, the 23 categories and the 27 subtasks, and direct answering and CoT are not the same definition.

Sources: [1][6]

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

Sources: [1]

### 当前发布

Public task set from 2022; the repository commit is not pinned

Sources: [2][1]

### 版本脉络

original_v1：2022-10-18；subsequent_use：url：https://arxiv.org/html/2609.27284v1；evidence：BBH is reported separately for base/slow-thinking/fast-thinking; they are not the same track

Sources: [1][6]

### 分数上限与饱和度

The Hunyuan-A13B report lists the base model at 87.56, slow-thinking at 89.1, and fast-thinking at 87.0, separately. These are vendor self-reports under specific protocols, and they are not used to conclude that every model is saturated as of 2026-11.

Sources: [6]

### 争议与局限

Public answers, demonstrations, and task-generation rules may enter training; a score reported by the model is not independent proof that contamination was removed.

Sources: [1][2]

### 衍生版本

BBH is a subset of BIG-Bench and is not the complete BIG-Bench; this library does not split the subtasks out as additional benchmarks.

Sources: [1][2]

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

Sources: [1]

### Official entry

Unverified

Sources: [1]

Note: No independent, continuously updated official leaderboard has been confirmed; experiments in the paper are not presented as an official live leaderboard

Status: Unverified (part of this field is still unconfirmed).

### 第三方/补充实验

Unverified

Sources: [1]

Note: No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### Hunyuan report Table 2: base model, BBH 3-shot

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Qwen3-A22B | 88.87 | accuracy (%) |
| 2 | Hunyuan-A13B | 87.56 | accuracy (%) |
| 3 | Hunyuan-Large-1116 | 86.3 | accuracy (%) |
| 4 | Qwen2.5-72B | 85.8 | accuracy (%) |

- Qwen3-A22B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Hunyuan-A13B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Hunyuan-Large-1116：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Qwen2.5-72B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons

#### Hunyuan report Table 3: slow-thinking

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Hunyuan-A13B | 89.1 | accuracy (%) |
| 2 | Qwen3-A22B | 88.9 | accuracy (%) |
| 3 | Deepseek-R1-0120 | 83.7 | accuracy (%) |
| 4 | OpenAI-o1-1217 | 80.4 | accuracy (%) |

- Hunyuan-A13B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Qwen3-A22B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Deepseek-R1-0120：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- OpenAI-o1-1217：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons

#### Hunyuan report Table 4: fast-thinking

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Hunyuan-A13B | 87.0 | accuracy (%) |
| 2 | Hunyuan-Large-1116 | 86.5 | accuracy (%) |
| 3 | Qwen2.5-72B-instruct | 80.5 | accuracy (%) |
| 4 | Qwen3-A22B | 68.1 | accuracy (%) |

- Hunyuan-A13B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Hunyuan-Large-1116：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Qwen2.5-72B-instruct：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons
- Qwen3-A22B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：Vendor technical-report self-report and its comparisons

#### Original paper Table 2: 3-shot CoT, equal-weight macro-average over 23 tasks

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Codex (code-davinci-002) | 73.9 | accuracy (%) |
| 2 | InstructGPT (text-davinci-002) | 68.4 | accuracy (%) |
| 3 | PaLM 540B | 65.2 | accuracy (%) |

- Codex (code-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022 historical experiment
- InstructGPT (text-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022 historical experiment
- PaLM 540B：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022 historical experiment

#### Original paper Table 2: 3-shot Answer-only, equal-weight macro-average over 23 tasks

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Codex (code-davinci-002) | 56.6 | accuracy (%) |
| 2 | PaLM 540B | 52.3 | accuracy (%) |
| 3 | InstructGPT (text-davinci-002) | 51.8 | accuracy (%) |

- Codex (code-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022 historical experiment
- PaLM 540B：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022 historical experiment
- InstructGPT (text-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022 historical experiment

Sources: [6][4]

### 覆盖边界

The public repository is not a leaderboard that keeps rolling forward. Table 2 of the original paper, and Tables 2, 3, and 4 of the Hunyuan report, were read again. Base, slow thinking, fast thinking, the original CoT, and a direct answer are kept on separate tracks. Different settings are not ordered as one SOTA. The macro-average for BBH follows the original paper's scope of 23 tasks.

Sources: [5][6][4]

## Contact

### 公开作者工作邮箱

msuzgun@cs.stanford.edu

Sources: [2][1]

### 公开反馈

https://github.com/suzgunmirac/BIG-Bench-Hard/issues

Sources: [2]

### 官方账号

Unverified

Sources: [1]

Note: No dedicated official social account has been verified, and personal accounts of the same name are not included

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Sources: [1]

Note: A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://arxiv.org/pdf/2210.09261

Sources: [1]

### 下载源文件SHA-256

168f6fff020e9fde7563905f69e6a59d0648f195f48820d52c83c7adfaee18ec

Sources: [4]

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

5375941

Sources: [4]

### 既有文件夹

id：1ISeb201NpVdzOdwUQ5IA9veSJL8smlBq；webViewLink：

Sources: [7]

### 其他材料

chinese_intro_doc：id：1N0fQBJOZu3qwT8NX-UfZwCJuvdJnfJzP3HGJtXaKrqs；webViewLink：

Sources: [7]

### 既有 PDF链接

id：1nmUl5QNGTZKijqLcX6GXqLqwODkV0-GW；webViewLink：

Sources: [8]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
- 2026-11-07（ ()）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

Sources: [2]

### 来源索引

[1]: https://arxiv.org/abs/2210.09261 "访问 2026-11-07"
[2]: https://github.com/suzgunmirac/BIG-Bench-Hard "访问 2026-11-07"
[3]: https://raw.githubusercontent.com/suzgunmirac/BIG-Bench-Hard/main/LICENSE "访问 2026-11-07"
[4]: https://arxiv.org/pdf/2210.09261 "访问 2026-11-07"
[5]: https://raw.githubusercontent.com/suzgunmirac/BIG-Bench-Hard/main/README.md "访问 2026-11-07"
[6]: https://arxiv.org/html/2609.27284v1 "访问 2026-11-07"
[7]: "访问 2026-11-07"
[8]: "访问 2026-11-07"
