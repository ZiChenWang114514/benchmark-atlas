# ChartQA

> Benchmark Constitution, in-depth review: 2026-11-08. Official materials were searched again; historical leaderboards, the current snapshot, and vendor self-reports are kept separate; fields without empirical support retain Unverified

ChartQA combines real charts, human question answering, and summary-driven machine question answering, and it measures visual reference and multi-step numerical reasoning. Its commonly used test set of 2,500 QA items contains 1,250 human questions and 1,250 machine questions. The number of questions is not equal to the number of independent images. Whether a baseline receives the underlying gold table changes the task substantially. A 5% numerical-tolerance protocol also cannot be mixed directly with LLM-judge scores from another paper.

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

## Basic information

### Short name

ChartQA

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

### Full name

ChartQA

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

### 版本边界

The official Full Version (including annotations); the First Version, which does not include annotations, is also retained. The README does not adopt a numeric version number that can be verified.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### Paper version

arXiv v1

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）

### Release date

2022-03-19

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）

> The original first-release date in the arXiv metadata; not an inferred time when the dataset first went online.

### 板块

Multimodal

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. The classification is not claimed to be set by the benchmark's maintainers.

### 领域

```json
[
 "Chart question answering"
]
```

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

### 许可与限制

The full text of the official repository LICENSE is GNU GPL v3; the HF card likewise labels GPL-3.0. Copyright in third-party original figures does not transfer automatically with the code license.

[来源1](https://github.com/vis-nlp/ChartQA/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/blob/main/README.md)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2203.10244

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

### Code

https://github.com/vis-nlp/ChartQA

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

### Dataset

https://huggingface.co/datasets/ahmed-masry/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA)（访问 2026-11-07）

### Official homepage

https://github.com/vis-nlp/ChartQA

[Source 1](https://github.com/vis-nlp/ChartQA) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2203.10244) (accessed 2026-11-07)

### 论文题名

ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Paper author affiliations: York University, Nanyang Technological University, and Salesforce Research.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### Partner organizations

```json
[
 "York University, Canada"
 "Nanyang Technological University, Singapore"
 "Salesforce Research"
]
```

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07）

> The institutions named by the authors of the paper; no additional commercial partnership is inferred.

### Authors

```json
[
 "Masry, Ahmed"
 "Long, Do Xuan"
 "Tan, Jia Qing"
 "Joty, Shafiq"
 "Hoque, Enamul"
]
```

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）

### 维护入口

vis-nlp / Ahmed Masry; the official repository Contact states that Ahmed Masry receives questions.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### 资助披露

Natural Sciences and Engineering Research Council (NSERC) of Canada。

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07）

> The Acknowledgement of the paper names the funding institutions; project numbers were not filled in by invention.

## Design goals

### 测量对象

Question answering on real charts, requiring visual reference and combined logical and arithmetic operations.

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### 既有评测的缺口

Existing chart QA mostly uses template questions and a fixed answer vocabulary, and can hardly cover naturally complex questions.

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

## Construction

### 题源

Real charts are collected from Statista, Pew, Our World in Data, and the OECD; ChartQA-H, the human question-answer set, coexists with ChartQA-M, generated automatically from human summaries of charts.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### 构建人员

Human annotators pose natural questions; the automatic portion is generated from abstracts, and the whole is not called expert-original.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）

### 审核

Human question-and-answer pairs are reviewed by another annotator. Answers that disagree are adjudicated by hand again. The paper reports a raw exact-match agreement of 61.04%, and agreement of 78.55% on a further sample of 500 after spelling and word-form variation are taken into account. Invalid questions are removed from the machine-generated test.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-08）

### 质控

The official release generates box annotations automatically from SVG; a damaged, missing, or noisy SVG introduces noise. Pew charts have no SVG and need manual annotation, sped up with heuristics; machine-generated test questions and answers are cleaned by hand as a further step.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）；[来源2](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07）

### 去污染及边界

Unverified

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

## Data format

### 规模与计数口径

```json
{
 "total_qa": 32719
 "train_qa": 28299
 "validation_qa": 1920
 "test_qa": 2500
 "paper_human_qa": 9608
 "paper_machine_qa": 23111
 "paper_human_charts": 4804
 "paper_machine_charts": 17141
}
```

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/raw/main/README.md)（访问 2026-11-07）

> Paper Table2 agrees with the official HF splits; the chart counts are the definitions of two source collections, and 4804+17141 is not presented as the deduplicated chart count for the whole collection.

### Question types

Open-ended numeric or text answers; bar charts, line charts, and pie charts, with the original tables and some box annotations.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### Modalities

Image+text

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### Languages

English (the questions made public here and the official description; the full language distribution is Unverified)

[来源1](https://huggingface.co/datasets/ahmed-masry/ChartQA)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### Difficulty

```json
{
 "proxy": "There is no unified easy/medium/hard labeling; the paper analyzes by task type and reasoning operation."
 "sample_analysis": "Table 4 of the paper, on a random sample of 300 questions written by people: data retrieval 13.0%, visual 10.7%, compositional 43.0%, and visual+compositional 33.3%."
}
```

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07）

> This is the distribution of sampled types in the paper, and it is not extrapolated to the difficulty distribution of the full 32,719 questions.

### 划分与公开范围

Public train, val, and test contain 28,299, 1,920, and 2,500 QA items. The test set has 1,250 questions written by humans and 1,250 written by machines. Table 2 of the paper corresponds to 625 human figures and 987 machine figures. A count of QA items must not be written as a count of independent images.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/blob/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

Relaxed accuracy: a numerical error within 5% of the reference value counts as correct, and non-numeric answers use string matching.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### 评分

Relaxed accuracy: a numerical error within 5% of the reference value counts as correct, and non-numeric answers use string matching.

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### 提示与运行条件

Baselines in the paper may use the images and the underlying data tables; an evaluation should state whether it uses oracle tables, OCR, or images only, and the results cannot be ranked on the same basis.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）

### 官方评测入口

https://github.com/vis-nlp/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### 可比性边界

The machine-generated subset and the human subset are reported separately; the official source points out that missing or damaged SVGs make the box annotations noisy. MMVistaReason uses CompassVerifier, which is not the same as the original numerical tolerance of 5%.

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）；[来源3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07）

## Current status

### 复核时间

2026-11-08

[来源1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-08）

### 当前版本

The official Full Version, including image box annotations, was verified. HF train, val, and test are 28,299, 1,920, and 2,500. The later official ChartQAPro is an independent benchmark and does not replace the data version of the original.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/raw/main/README.md)（访问 2026-11-07）

### 论文修订与后续使用

```json
{
 "revisions": [
 {
 "version": "v1"
 "date": "2022-03-19"
 }
 ]
 "continued_use_2026h2": [
 {
 "url": "https://arxiv.org/html/2610.01352v2"
 "date": "2026-10-23"
 "note": "MMVistaReason v2 §4.1 and Table 2 actually evaluate ChartQA (the ChartQA setting), comparing 4B/9B and other vision-language models; splits such as mini/val are not counted separately."
 "date": "2026-10-23"

 }
 ]
 "arxiv_revisions": [
 {
 "version": "v1"
 "submitted_at": "2022-03-19"
 }
 ]
}
```

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-08）

### Saturation

Unverified

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

### 风险与冲突

The machine-generated subset and the human subset are reported separately; the official source points out that missing or damaged SVGs make the box annotations noisy. MMVistaReason uses CompassVerifier, which is not the same as the original numerical tolerance of 5%.

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）；[来源3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07）

### 衍生与后续工作

ChartQAPro, a more challenging follow-on benchmark for real-chart QA recommended by the official repository; this entry does not count Pro in addition toward the original-version results.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-08）

### 官方榜入口

https://github.com/vis-nlp/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### 第三方榜入口

Unverified

[来源1](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07）

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

### 逐轨结果

```json
[
 {
 "model": "VisionTaPas"
 "score": 45.52
 "unit": "%"
 "metric": "Accuracy from the original paper (numeric answers allow a 5% tolerance)"
 "scope": "ChartQA original paper Table5, gold data table not provided, test; historical baseline"
 "date": "2022-05"
 "accessed": "2026-11-08"
 "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf"
 "provenance": "Published by the authors of the original benchmark; reread from the official ACL paper, and a current ranking is not claimed."
 "track": "Original paper Table 5/no gold table/historical baseline"
 "rank": null
 }
 {
 "model": "VL-T5"
 "score": 41.56
 "unit": "%"
 "metric": "Accuracy from the original paper (numeric answers allow a 5% tolerance)"
 "scope": "ChartQA original paper Table5, gold data table not provided, test; historical baseline"
 "date": "2022-05"
 "accessed": "2026-11-08"
 "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf"
 "provenance": "Published by the authors of the original benchmark; reread from the official ACL paper, and a current ranking is not claimed."
 "track": "Original paper Table 5/no gold table/historical baseline"
 "rank": null
 }
 {
 "model": "TaPas"
 "score": 41.28
 "unit": "%"
 "metric": "Accuracy from the original paper (numeric answers allow a 5% tolerance)"
 "scope": "ChartQA original paper Table5, gold data table not provided, test; historical baseline"
 "date": "2022-05"
 "accessed": "2026-11-08"
 "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf"
 "provenance": "Published by the authors of the original benchmark; reread from the official ACL paper, and a current ranking is not claimed."
 "track": "Original paper Table 5/no gold table/historical baseline"
 "rank": null
 }
 {
 "model": "MMVistaReason-4B (MVR-4B)"
 "score": 86.2
 "unit": "%"
 "metric": "Answer accuracy under the protocol of the paper (CompassVerifier)"
 "scope": "ChartQA"
 "date": "2026-10-23"
 "accessed": "2026-11-08"
 "source_url": "https://arxiv.org/html/2610.01352v2"
 "provenance": "Table 2 as reported by the MMVistaReason authors themselves; VLMEvalKit, T=0, max16384; §7.3 replaces traditional string matching with CompassVerifier, and this is not the official leaderboard or an independent evaluation by AA"
 "date_basis": "Converted from the arXiv v2 submission time; it is not a Not disclosed evaluation-run date."
 "track": "MMVistaReason v2/CompassVerifier/author self-report"
 "rank": null
 }
 {
 "model": "MMVistaReason-9B (MVR-9B)"
 "score": 87.6
 "unit": "%"
 "metric": "Answer accuracy under the protocol of the paper (CompassVerifier)"
 "scope": "ChartQA"
 "date": "2026-10-23"
 "accessed": "2026-11-08"
 "source_url": "https://arxiv.org/html/2610.01352v2"
 "provenance": "MMVistaReason author self-report Table 2; the same protocol, and not ranked together with other leaderboards without conditions"
 "date_basis": "Converted from the arXiv v2 submission time; it is not a Not disclosed evaluation-run date."
 "track": "MMVistaReason v2/CompassVerifier/author self-report"
 "rank": null
 }
]
```

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-08）；[来源2](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### 覆盖边界

The official README, the Full Version dataset card, and the AA evaluation catalog were checked again, and a continuously updated independent leaderboard for the original ChartQA was not found verified. The historical baselines newly collected from Table5 of the official paper (no gold table) are grouped with the author retest of 2026-H2; these are not the real-time top three of 2026. The current official ranking remains Unverified.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）；[来源2](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07）；[来源4](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07）

## Contact

### 公开研究联系

```json
[
 "amasry17@ku.edu.tr"
]
```

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

> The official README states explicitly that the old email masry20@yorku.ca has been discontinued; current contact no longer recommends the old email.

### 项目反馈

https://github.com/vis-nlp/ChartQA/issues

[来源1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07）

### 官方社交入口

The old university email masry20@yorku.ca has been discontinued, and the contact email currently published in the official README is used.

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07）

### 联系信息边界

Only officially published project feedback channels are recorded; private contact details are neither collected nor inferred.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原始PDF

https://arxiv.org/pdf/2203.10244

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07）；[来源2](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）

### PDF SHA-256

3b1d863e6f9ca45e84131bc51c8e47c8026faf6a6875edb9032bce2b9fadf0f9

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）

> Checksum of the originally downloaded bytes. They were not compressed or rewritten.

### PDF bytes

2938574

[来源1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07）

### 目录

## Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 "round": "1 / 深度实证复核"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

[来源1](https://arxiv.org/abs/2203.10244)（访问 2026-11-08）；[来源2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-08）
