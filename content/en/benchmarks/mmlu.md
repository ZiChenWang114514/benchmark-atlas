# MMLU

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MMLU是覆盖57学科的英语四选一知识与问题求解测试，不是专家新编的隐藏题库。官方原论文与当前Hugging Face发行的实际划分数量不同，本页同时保留两种口径，不把历史README榜当作当代前沿排名。MMLU-Pro、Redux和多语变体改变了题库或协议，不能用名字相近就直接合并分数。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### Short name

MMLU

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Full name

Massive Multitask Language Understanding

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Benchmark version

The original MMLU (ICLR2021); the current HF cais/mmlu is the 57-subject configuration, and it is not the same as MMLU-Pro, Redux, or a multilingual derivative edition.

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### Paper version

arXiv v3

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Release date

2020-09-08 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Section

Language

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Field tags

- 多学科知识

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 许可证与权利边界

MIT (the official hendrycks/test master/LICENSE and the cais/mmlu data card); rights in third-party sources of questions should be examined separately.

[来源](https://raw.githubusercontent.com/hendrycks/test/master/LICENSE)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2009.03300

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Code repository

https://github.com/hendrycks/test

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/cais/mmlu

> The official original data.tar is still linked from the README; the HF release statistics differ from the paper. See the question-count field.

[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）

### Official homepage

https://github.com/hendrycks/test

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Paper title

Measuring Massive Multitask Language Understanding

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

Author affiliations in the paper include UC Berkeley, Columbia University, University of Chicago, and UIUC. Author affiliations are recorded here. A formal institutional sponsoring relationship is not inferred.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 合作方

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Authors

- Hendrycks, Dan
- Burns, Collin
- Basart, Steven
- Zou, Andy
- Mazeika, Mantas
- Song, Dawn
- Steinhardt, Jacob

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Maintainer

The official public code is hosted under hendrycks; this records the repository maintenance entry point and is not a basis for inferring institutional legal liability or a commitment to continued maintenance.

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### Funders

The acknowledgments in the paper list support including the NSF Graduate Research Fellowship, the Open Philanthropy AI Fellowship, and NSF Frontier Award 1804794.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## Design goals

### Abilities measured

Measures a language model's knowledge and problem-solving ability across a wide range of subjects, rather than evaluating it only after training on a single task.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Design background

Earlier datasets of language understanding were often narrow and easy to overcome by fine-tuning on the task or by pattern matching; this benchmark uses cross-disciplinary testing in the zero-shot or few-shot setting.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## Construction

### Question sources

Student contributors manually collected freely available exams, textbooks, and practice problems from the web, covering the humanities, the social sciences, STEM, and professional knowledge.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 出题与审阅者背景

The paper states that the questions were collected mainly by undergraduates, and that not every question is original work by a domain expert.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Review process

The authors organize multiple-choice questions by subject and form development, validation, and test splits; the precise assignment of per-question review responsibility is Unverified pending further verification.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Quality control

Every question uses the same four-choice format; later MMLU-Redux research still finds ambiguity, annotation errors, and question errors, so the set cannot be regarded as fully corrected.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 去污染及其证据边界

An appendix of the original paper analyzes the risk that GPT-3 memorized items, using the correlation of question compression and entropy with answer accuracy; for most items from the sources, the question and the answer are on different pages of the PDF or of the web page. This diagnoses the model of that time, and it cannot be used to conclude that the question bank published later is free of contamination.

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

## Data format

### 题量与版本口径

Original paper §3: test14,079, validation1,540, and dev of 5 questions per subject. The 57-subject configuration on the current cais/mmlu dataset card sums, subject by subject, to test14,042, validation1,531, and dev285, excluding auxiliary_train. The two version scopes are kept side by side. The baseless "15,908 questions in total" is removed.

> The count on the data card is the exact sum of num_examples across 57 subject configurations, without adding the all aggregate configuration a second time.

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### Question types

Four-option multiple-choice question

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Modalities

Text

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Languages

English

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Difficulty

Difficulty runs from knowledge in basic education to university and professional-qualification level; difficulty differs across subjects.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Public and hidden splits

Development examples, the validation set, and the test set are all public; do not mix the splits in evaluation.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## Evaluation

### Metrics

Multiple-choice accuracy, aggregated by task.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 评分方法

The original experiment compares the model probabilities of options A, B, C, and D, and takes the option with the highest probability.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 运行与提示设置

The original paper reports zero-shot, few-shot, and other settings; standard few-shot uses 5 development questions per subject.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 官方脚本

https://github.com/hendrycks/test

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 可比性警示

Zero-shot, 5-shot, CoT, the subject macro-average, and the question micro-average cannot be compared without labels; MMLU also differs from its error-corrected, extended, and translated versions.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## Current status

### 核查日期

2026-11-08

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 当前数据与工具版本

The basis of the original MMLU paper and the basis of the current HF release both stand; the current HF counts are test 14,042 / validation 1,531 / dev 285, the release file that is adopted must be fixed inside the experiment, and the original counts in the paper cannot be assumed by default.

[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2020-09-08；- **timezone**：；- - **version**：v2；- **submitted_at**：2020-09-21；- **timezone**：；- - **version**：v3；- **submitted_at**：2021-01-13；- **timezone**：

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Saturation

The original MMLU-Pro paper takes the plateau of frontier scores on the original MMLU as its design motivation; the historical leaderboard in the original repository does not include contemporary frontier models, so its highest score of 67.5% cannot be used to assert that the benchmark is currently unsaturated.

[来源](https://arxiv.org/pdf/2406.01574)（访问 2026-11-08）

### 污染、争议与限制

The original studies of MMLU-Pro and of MMLU-Redux respectively point out easy questions, and noise and label errors; error rates vary by subject, and an error rate from a local sample should not be extrapolated to every question.

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 衍生与版本关系

- MMLU-Pro
- MMLU-Redux
- MMMLU

[来源](https://arxiv.org/abs/2610.11978)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）

### Official entry

https://github.com/hendrycks/test#test-leaderboard

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 第三方覆盖入口

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Original official README historical leaderboard

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Chinchilla (70B, few-shot) | 67.5 | Average accuracy / % |
| Gopher (280B, few-shot) | 60.0 | Average accuracy / % |
| GPT-3 (175B, fine-tuned) | 53.9 | Average accuracy / % |
| flan-T5-xl | 49.3 | Average accuracy / % |
| UnifiedQA | 48.9 | Average accuracy / % |
| GPT-3 (175B, few-shot) | 43.9 | Average accuracy / % |
| GPT-3 (6.7B, fine-tuned) | 43.2 | Average accuracy / % |
| flan-T5-large | 41.9 | Average accuracy / % |
| flan-T5-base | 34.2 | Average accuracy / % |
| GPT-2 | 32.4 | Average accuracy / % |
| flan-T5-small | 29.5 | Average accuracy / % |
| Random Baseline | 25.0 | Average accuracy / % |

- **Chinchilla (70B, few-shot)**：- **humanities**：63.6；- **social_sciences**：79.3；- **stem**：54.9；- **other**：73.9；- **authors**：Hoffmann et al., 2022；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **Gopher (280B, few-shot)**：- **humanities**：56.2；- **social_sciences**：71.9；- **stem**：47.4；- **other**：66.1；- **authors**：Rae et al., 2021；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **GPT-3 (175B, fine-tuned)**：- **humanities**：52.5；- **social_sciences**：63.9；- **stem**：41.4；- **other**：57.9；- **authors**：Brown et al., 2020；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **flan-T5-xl**：- **humanities**：46.3；- **social_sciences**：57.7；- **stem**：39.0；- **other**：55.1；- **authors**：Chung et al., 2022；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **UnifiedQA**：- **humanities**：45.6；- **social_sciences**：56.6；- **stem**：40.2；- **other**：54.6；- **authors**：Khashabi et al., 2020；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **GPT-3 (175B, few-shot)**：- **humanities**：40.8；- **social_sciences**：50.4；- **stem**：36.7；- **other**：48.8；- **authors**：Brown et al., 2020；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **GPT-3 (6.7B, fine-tuned)**：- **humanities**：42.1；- **social_sciences**：49.2；- **stem**：35.1；- **other**：46.9；- **authors**：Brown et al., 2020；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **flan-T5-large**：- **humanities**：39.1；- **social_sciences**：49.1；- **stem**：33.2；- **other**：47.4；- **authors**：Chung et al., 2022；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **flan-T5-base**：- **humanities**：34.0；- **social_sciences**：38.1；- **stem**：27.6；- **other**：37.0；- **authors**：Chung et al., 2022；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **GPT-2**：- **humanities**：32.8；- **social_sciences**：33.3；- **stem**：30.2；- **other**：33.1；- **authors**：Radford et al., 2019；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **flan-T5-small**：- **humanities**：29.9；- **social_sciences**：30.9；- **stem**：27.5；- **other**：29.7；- **authors**：Chung et al., 2022；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard
- **Random Baseline**：- **humanities**：25.0；- **social_sciences**：25.0；- **stem**：25.0；- **other**：25.0；- **authors**：N/A；- **scope**：Different few-shot/fine-tuned settings are retained as in the original table; this is not a unified 2026 live leaderboard

[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）


[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）

### 覆盖范围与时效

The readable table in the official README replaces an unofficial research comparison table as the snapshot for this column; the leaderboard does not give a single update date, the vintages of the models and the prompt protocols differ, and it must not be treated as a frontier ranking for 2026.

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

## Contact

### 公开工作邮箱

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 公开反馈

https://github.com/hendrycks/test/issues

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 官方社交

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 隐私边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2009.03300

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF SHA-256

d3a7b0f8589f5365ebfd34a3876a9a8b3fde83e0adb9ed19ccf8f0034bb48fc1

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF bytes

2074939

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### Folder

- **id**：16jdkBY7vMWPeny-ZoCn5i4limN90OF26
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍；- **id**：10X_jNgeT4GCIeP3q17ZGinf7YmmYmD1g4wxlM6aLIOc；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：1_7QVvJvbgngMAfsCYTyOLG7QjAa1NbO9
- **webViewLink**：

[来源]( 2026-11-07）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）
