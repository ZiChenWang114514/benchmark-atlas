# C-Eval

> Benchmark Constitution, in-depth review: 2026-11-08. Review of the official evidence is complete; the 2026-H2 evidence of use has been reread; unknown fields and conflicts in the documentation are retained explicitly

C-Eval measures knowledge and reasoning in 52 subjects against a background of education and qualification examinations native to Chinese, spanning junior high school, senior high school, university, and the professional level. It is not a simple translation of the English MMLU into Chinese. Reading a score first requires asking whether it is test or val, zero-shot or five-shot, and direct answering or CoT. The official source made the full test public on 2025-07-27, and the hidden-label statement in the old documentation cannot continue to be followed unconditionally.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

## Basic information

### Short name

C-Eval

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Full name

Chinese Evaluation Suite for Foundation Models

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 版本边界

Unverified

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

### Paper version

arXiv v3

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Release date

2023-05-15

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> The first-release date of the original paper; it is not guaranteed to equal the date the data files were first made public.

### 板块

Language

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

### 领域

```json
[
 "Chinese multidisciplinary knowledge"
]
```

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 许可与限制

The code is MIT; the dataset is CC BY-NC-SA 4.0, and the two must not be used interchangeably.

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2305.08322

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Code

https://github.com/hkust-nlp/ceval

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Dataset

https://huggingface.co/datasets/ceval/ceval-exam

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ceval/ceval-exam/blob/main/README.md)（访问 2026-11-08）

### Official homepage

https://cevalbenchmark.com

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 论文题名

C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

## Origin and maintenance

### Initiators

Paper author affiliations include Shanghai Jiao Tong University, Tsinghua University, the University of Edinburgh, and the Hong Kong University of Science and Technology; the author-contribution statement was initiated and organized by Junxian He.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Partner organizations

Unverified

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

### Authors

```json
[
 "Huang, Yuzhen"
 "Bai, Yuzhuo"
 "Zhu, Zhihao"
 "Zhang, Junlei"
 "Zhang, Jinghan"
 "Su, Tangjun"
 "Liu, Junteng"
 "Lv, Chuancheng"
 "Zhang, Yikai"
 "Lei, Jiayi"
 "Fu, Yao"
 "Sun, Maosong"
 "He, Junxian"
]
```

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 维护入口

The official public code is hosted under hkust-nlp; this records the repository maintenance entry point and is not a basis for inferring institutional legal liability or a commitment to continued maintenance.

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### 资助披露

The acknowledgments of the paper list funding of the authors that includes the National Key R&D Program of China 2020AAA0106502 and the Tsinghua University Guo Qiang Institute.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

## Design goals

### 测量对象

Measures foundation models' understanding and reasoning over multi-level, multi-disciplinary knowledge in a Chinese-language setting.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 既有评测的缺口

An English-centered evaluation is not sufficient to represent mastery of Chinese education and professional knowledge; translating English questions also cannot cover the Chinese curricular background.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

## Construction

### 题源

PDFs and Word files from mock and local examinations, some university final-exam questions, and about 2,000 authorized questions from 维普.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 构建人员

The authors organized students and researchers in the relevant subjects to collect, edit, and verify Chinese examination questions.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 审核

Documents are parsed, and formatting and LaTeX are corrected by hand; the authors cross-check stems and answers.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 质控

Duplicates are removed and formatting is checked, and national unified-examination questions that might leak are avoided as far as possible; this does not guarantee that model training is free of contamination.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 去污染及边界

Selection of question sources avoids some popular public exam items, and duplicates are removed; there is no evidence that can guarantee the training corpus of every model under test is entirely free of these questions.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

## Data format

### 规模与计数口径

13,948 questions in total, 52 subjects, and four difficulty levels; the validation set has 1,346 questions, with 5 development examples per subject.

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### Question types

Four-option multiple-choice question

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Modalities

Text

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Languages

Chinese

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### Difficulty

Four levels: junior high, senior high, university, and professional qualification.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 划分与公开范围

Each subject has 5 dev questions. val is used for tuning, and test is used for evaluation. News in the README says that the complete test set was made public on 2025-07-27, but the older Data section still says that the test labels are not public. There is a conflict in how current the documents are, and the test cannot continue to be called hidden without distinction.

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

## Evaluation

### Metrics

Accuracy; the official paper aggregates by subject or category, and the method of averaging must be recorded.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 评分

A/B/C/D is usually extracted from the generated content; when the format is not followed, the probabilities of the four options may be compared. The probability method does not apply to CoT; zero-shot, five-shot, and CoT are recorded separately.

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### 提示与运行条件

The original paper includes 0-shot/5-shot answer-only and 5-shot CoT; do not mix them in the same ranking.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 官方评测入口

https://github.com/hkust-nlp/ceval

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### 可比性边界

C-Eval's questions, written originally in Chinese, differ from translated MMLU; the hidden test, the validation set, 5-shot, CoT, and the method of averaging must all be labeled.

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

## Current status

### 复核时间

2026-11-08

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 当前版本

Official README news record: on 2025-07-27 the complete test set was released to the community.

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### 论文修订与后续使用

```json
{
 "arxiv_revisions": [
 {
 "version": "v1"
 "submitted_at": "2023-05-15"
 }
 {
 "version": "v2"
 "submitted_at": "2023-05-17"
 }
 {
 "version": "v3"
 "submitted_at": "2023-11-06"
 }
 ]
}
```

[来源1](https://arxiv.org/abs/2305.08322)（访问 2026-11-08）

### Saturation

Unverified

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

### 风险与冲突

The official README and the HF card announced on 2025-07-27 that the complete test set is public. The statement in the old Data section that “labels are not public” is a conflict of documentation currency. After the labels are public, contamination continues to be watched. Avoiding question sources and deduplication cannot prove that the training of every model under test is free of leakage.

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ceval/ceval-exam/blob/main/README.md)（访问 2026-11-08）

### 衍生与后续工作

C-Eval Hard: a fixed subset made up of 8 high-reasoning subjects in mathematics, physics, and chemistry; it is not combined with mean accuracy over all 52 subjects as one metric.

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://arxiv.org/abs/2305.08322)（访问 2026-11-08）

> A collection date; it does not represent the run date of every listed model, and result rows separately mark historical or live status.

### 官方榜入口

https://cevalbenchmark.com/static/leaderboard.html

[来源1](https://cevalbenchmark.com/static/leaderboard.html)（访问 2026-11-07）

### 第三方榜入口

Unverified

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

### 逐轨结果

```json
[
 {
 "rank": 1
 "model": "GPT-4"
 "score": 66.4
 "metric": "average accuracy (%)"
 "track": "Original test / 0-shot answer-only / README history."
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 2
 "model": "ChatGPT"
 "score": 51.0
 "metric": "average accuracy (%)"
 "track": "Original test / 0-shot answer-only / README history."
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 3
 "model": "Claude-v1.3"
 "score": 50.5
 "metric": "average accuracy (%)"
 "track": "Original test / 0-shot answer-only / README history."
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": 68.7
 "metric": "average accuracy (%)"
 "track": "Original test / 5-shot answer-only / README history."
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 2
 "model": "ChatGPT"
 "score": 54.4
 "metric": "average accuracy (%)"
 "track": "Original test / 5-shot answer-only / README history."
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 3
 "model": "Claude-v1.3"
 "score": 54.2
 "metric": "average accuracy (%)"
 "track": "Original test / 5-shot answer-only / README history."
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": 69.9
 "metric": "average accuracy (%)"
 "track": "validation/5-shot answer-only/README history"
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 2
 "model": "Claude-v1.3"
 "score": 55.5
 "metric": "average accuracy (%)"
 "track": "validation/5-shot answer-only/README history"
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
 {
 "rank": 3
 "model": "ChatGPT"
 "score": 53.5
 "metric": "average accuracy (%)"
 "track": "validation/5-shot answer-only/README history"
 "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
 "accessed": "2026-11-08"
 "unit": "%"
 "model_snapshot": "待核实"
 "evaluation_date": "待核实"
 }
]
```

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问 2026-11-08）

### 覆盖边界

On this pass the official live leaderboard returned 500 to WebFetch, and a direct HTTPS read failed certificate verification. The certificate check was not bypassed. Only three tracks that can be verified directly are updated: the historical test zero-shot and five-shot results in the README, and the val five-shot results. A live top three for 2026 cannot be claimed.

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问 2026-11-08）；[来源2](https://cevalbenchmark.com/static/leaderboard.html)（访问 2026-11-08）

## Contact

### 公开研究联系

```json
[
 "ceval.benchmark@gmail.com"
]
```

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

### 项目反馈

https://github.com/hkust-nlp/ceval/issues

[来源1](https://github.com/hkust-nlp/ceval)（访问 2026-11-07）

### 官方社交入口

Unverified

[Source 1](https://arxiv.org/abs/2305.08322) (accessed 2026-11-07)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

### 联系信息边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原始PDF

https://arxiv.org/pdf/2305.08322

[来源1](https://arxiv.org/pdf/2305.08322)（访问 2026-11-07）

### PDF SHA-256

88bfbd09fe554fc40538cb84fcff09681b86ff5c71398fd4b9beaf177d73acde

[来源1](https://arxiv.org/pdf/2305.08322)（访问 2026-11-07）

> SHA-256 of the originally downloaded bytes. They were not compressed or rewritten.

### PDF bytes

5123072

[来源1](https://arxiv.org/pdf/2305.08322)（访问 2026-11-07）

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
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

[来源1](https://arxiv.org/abs/2305.08322)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2305.08322)（访问 2026-11-08）；[来源3](https://github.com/hkust-nlp/ceval)（访问 2026-11-08）
