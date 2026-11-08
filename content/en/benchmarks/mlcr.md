# MLCR / MLCR-AA

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MLCR关注医疗理赔记录中的长篇综合推理：模型需要重建时间线、临床因果与文档缺失，而非背诵医学考试知识。病例为合成但受现实案例启发；公开较易题与私有难题分开发布。MLCR-AA是Artificial Analysis独立运行的实现，准确性、完整性和联合通过率必须分别解读。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Short name

MLCR / MLCR-AA

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### Full name

Medical Long Context Reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### Benchmark version

MLCR v1.1 (2026-08-31); MLCR-AA is an independent-implementation definition

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### Paper version

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### Release date

First released on 2026-06-18; v1.1 on 2026-08-31

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### Section

Biology and medicine

> Filed under one main section. That filing does not limit coverage of other disciplines.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### Field tags

- 长上下文
- 保险记录

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 许可证与权利边界

The HF data card states license: other explicitly; the specific terms under which redistribution is allowed are Unverified. A request for main/LICENSE in the official repository returns 404, and MIT cannot be inferred from the README describing the project as open-source.

[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset/raw/main/README.md)（访问 2026-11-08）

### 论文入口

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### Code repository

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 数据集入口

https://huggingface.co/datasets/Wisedocs/mlcr-dataset

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### Official homepage

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### Paper title

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

Wisedocs

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 合作方

Artificial Analysis (co-releases MLCR-AA and independently runs its private evaluation)

[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Authors

- Denys Linkov (author of the official technical blog of 2026-06-18).
- Aryan Dhar (author of the official technical blog for v1.1 on 2026-08-31).

> These are the authors of the public technical material; this is not presented as the full author list of an academic paper.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### Maintainer

Wisedocs maintains the original MLCR; Artificial Analysis maintains the MLCR-AA evaluation.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Funders

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## Design goals

### Abilities measured

Reconstructs timelines, causality, treatment patterns, and the relevance of insurance claims across long and fragmented medical records.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Design background

Requires not only locating a single fact, but also expert-level clinical synthesis and multi-part reasoning.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

## Construction

### Question sources

Synthetic medical records, with irrelevant filler inserted deterministically into the model context from a fixed seed; cases, prompts, models, modalities, filler ratios, and thinking levels make up the experimental matrix.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 出题与审阅者背景

The questions imitate the work of medical and insurance-claims professionals reviewing records; the reference answers are verified by humans, and the synthetic cases are generated with the composition of real cases as inspiration. The credentials of the person who wrote each individual question are Unverified.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）

### Review process

Experts annotate the ground truth, and 3 judges compare it with the original record and the reference answer.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Quality control

An empty answer fails immediately; it passes only when a majority of judges confirm that it is complete and that the record contains no contradiction.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 去污染及其证据边界

The official release explicitly keeps the Tier4–6 hard questions for private evaluation, in order to reduce contamination; the cases and Tier1–3 are public. Keeping material private is a control, and it is not the same as having verified that every model under test never encountered the related material.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

## Data format

### 题量与版本口径

There are 10 synthetic cases, each with 50–150 medical summaries and 25k–64k tokens; the launch blog says 250 questions and publishes 100+ Tier1–3 questions. The public repository also has OCR of 131 blank forms and OCR of 131 synthetic filled forms; the AA private set of 60 questions × 3 repeats is counted on its own and is not added into the question count.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Question types

Single-fact retrieval, synthesis across documents, clinical causal reasoning, and multi-part questions.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### Modalities

- 文本
- OCR记录

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### Languages

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### Difficulty

The original MLCR has six tiers: Easy, Medium, Hard, Expert, Multi-part Compound, and Compound Hallucination Check. The current AA page says it uses the two hardest classes, expert/compound. The v1.1 blog says three difficult tiers. The conflicting scopes are recorded as they stand and are not forcibly unified.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Public and hidden splits

Tier1–3 and 10 cases are public; the official description states that Tier4–6 are private. The HF configurations questions, cases_summaries, and filler_files are all named train, which is only a label of the release split and should not be miscalled the model's training set. AA separately takes 60 private questions, with 3 repeats per question.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset/raw/main/README.md)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

## Evaluation

### Metrics

The primary metrics are pass rate / pass@1; accuracy and completeness are listed separately and must not be used interchangeably.

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 评分方法

A majority vote of 3 LLM judges: every part is complete, and there is no claim that contradicts the original record.

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 运行与提示设置

3 repeats per question; by default, one paragraph per part, citing the original record; the AA judges are Claude Opus5.5, GPT-6.1 Sol, and Grok4.7, at medium.

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方脚本

The official Wisedocs evaluation harness repository; the AA private set cannot be fully reproduced directly from the public data.

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 可比性警示

The public harness has a conciseness gate of ≤5 times the number of characters in the reference answer, and an older judge panel; the current private protocol and judge used by AA already differ. The results, the modalities, and the filler ratios of the two cannot be mixed in one comparison.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

- **version**：MLCR v1.1; the private AA implementation is counted separately
- **evidence_2026_h2**：- - **url**：https://artificialanalysis.ai/evaluations/mlcr-aa；- **date**：2026-11-07；- **date_type**：observed_on；- **note**：AA currently evaluates 27 models in an independent evaluation. This is an ongoing evaluation of long medical records, and it is not in the Intelligence Index.；- - **url**：https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md；- **date**：2026-08-31；- **note**：The Wisedocs README releases v1.1, improves judge calibration, and jointly releases the evaluation with AA.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 论文修订及历史证据

Timeline of the technical material: the launch blog on 2026-06-18; MLCR v1.1 released on 2026-08-31, covering calibration of the judge and revision of the reference answers. An independent arXiv paper version is Unverified.

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### Saturation

The highest joint pass rate on the current AA page is 41.7%; accuracy and completeness are independent dimensions, and an accuracy of 98.3% cannot be used to claim that the whole of MLCR-AA is saturated.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 污染、争议与限制

v1.1 separates accuracy errors from completeness omissions, relies on the original records and not only the reference answer, and relaxes the length threshold from 3× to 5×. The historical joint pass rate of 64.4% in the v1.1 blog and the current AA figure of 41.7% are not the same snapshot. The wording of two hard classes and of three tiers also conflicts. The HF card writes Multi-Length Context Retrieval, which does not match Medical Long Context Reasoning on the official blog. The name in this entry follows the blog and AA.

[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset/raw/main/README.md)（访问 2026-11-08）

### 衍生与版本关系

MLCR-AA is a private hard-question implementation carried out independently by Artificial Analysis; the public MLCR harness, the v1.1 blog snapshot, and the current AA leaderboard are not mixed in one ranking.

[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### Official entry

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 第三方覆盖入口

https://artificialanalysis.ai/evaluations/mlcr-aa

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Current independent AA evaluation / pass rate

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| GPT-6 Astra (Max) | 41.7 | pass rate / % |
| Claude Sonnet 5.5 (Max, Default Fallback) | 41.7 | pass rate / % |
| GPT-6.1 Sol (Max) | 38.3 | pass rate / % |

- **GPT-6 Astra (Max)**：- **rank**：1；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.
- **Claude Sonnet 5.5 (Max, Default Fallback)**：- **rank**：1；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.
- **GPT-6.1 Sol (Max)**：- **rank**：3；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

#### AA current independent evaluation / completeness

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Claude Sonnet 5.5 (Max, Default Fallback) | 64.8 | completeness / % |
| Claude Opus 5.5 (Max, Default Fallback) | 63.3 | completeness / % |
| Claude Fable 5.1 (Max, Default Fallback) | 61.1 | completeness / % |

- **Claude Sonnet 5.5 (Max, Default Fallback)**：- **rank**：1；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.
- **Claude Opus 5.5 (Max, Default Fallback)**：- **rank**：2；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.
- **Claude Fable 5.1 (Max, Default Fallback)**：- **rank**：3；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

#### Current independent AA evaluation / accuracy

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| GPT-6.1 Terra (Max) | 98.3 | accuracy / % |
| GPT-6.1 Sol (Max) | 96.7 | accuracy / % |
| GPT-6 Astra (Max) | 95.6 | accuracy / % |

- **GPT-6.1 Terra (Max)**：- **rank**：1；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.
- **GPT-6.1 Sol (Max)**：- **rank**：2；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.
- **GPT-6 Astra (Max)**：- **rank**：3；- **scope**：60 private questions, with 3 repeats each; only the top three listed in the page text are given, and the details of the remaining 27 models are not invented.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

#### Wisedocs v1.1 blog historical snapshot / overall

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Claude Fable 5 | 64.4 | overall pass rate / % |
| Claude Opus 5 | 59.4 | overall pass rate / % |
| Claude Opus 5 | 58.3 | overall pass rate / % |

- **Claude Fable 5**：- **published_date**：2026-08-31；- **configuration**：The body of the blog does not give a complete configuration for that range of values, and it cannot be mapped to the current AA model row.
- **Claude Opus 5**：- **published_date**：2026-08-31；- **configuration**：The body of the blog does not give a complete configuration for that range of values, and it cannot be mapped to the current AA model row.
- **Claude Opus 5**：- **published_date**：2026-08-31；- **configuration**：The body of the blog does not give a complete configuration for that range of values, and it cannot be mapped to the current AA model row.

[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### 覆盖范围与时效

The three AA metrics are kept on separate tracks; 41.7% is a tie at the precision that is displayed, so a significant difference cannot be claimed. The historical overall track from the blog is retained, and the exact run date, which is unknown, is Unverified; the full dynamic table of 27 models was not extracted.

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

## Contact

### 公开工作邮箱

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 公开反馈

https://github.com/Wisedocs-AI/medical-long-context-reasoning/issues

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 官方社交

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 隐私边界

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## Original files

### 原论文PDF

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### PDF SHA-256

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### PDF bytes

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### Folder

Unverified

> Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 其他官方材料

- - **title**：Benchmarking LLMs For Medical Document Work；- **url**：https://www.wisedocs.ai/blogs/medical-long-context-reasoning；- **published_date**：2026-06-18
- - **title**：MLCR v1.1: Calibrating LLM Judges for Long-Context Medical Reasoning；- **url**：https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning；- **published_date**：2026-08-31

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### PDF归档

Unverified

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：按官方材料新建中文条目；区分热度、质量和不同版本评分。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）
