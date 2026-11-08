# AQuA-RAT

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

Official evidence review; authorization and version conflicts are kept explicit; unverified items are not fabricated

Five-choice algebraic word problems with natural-language explanations of the reasoning. The public crowdsourced release differs from an earlier version that the paper could not publish in full; raw and tokenized forms represent the same questions and must not be counted twice.

## Basic information

### Short name

AQuA-RAT

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Full name

Algebra Question Answering with Rationales

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Benchmark version

The public crowdsourced release differs from the experimental version in the original paper; the release file must be specified

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Paper version

arXiv v3

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Release date

2017-05-11 21:04:47 (arXiv first draft, not equivalent to a data-release statement)

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Section

Mathematics

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### Field tags

- Algebra word problems and reasoning

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### License

Apache-2.0 (official repository LICENSE; rights in the paper version and in third-party original materials need to be distinguished separately)

[来源1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/LICENSE)（访问2026-11-07）

### Paper

https://arxiv.org/abs/1705.04146

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Code

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 数据地址

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Official entry

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Paper title

Program Induction by Rationale Generation : Learning to Solve and Explain Algebraic Word Problems

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## Origin and maintenance

### Initiators

DeepMind, University of Oxford (paper byline).

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 合作方

Unverified

> 字段状态：待核实

> Only the institutions named on the paper are confirmed; not every listed affiliation is automatically treated as a formal partner

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Authors

- Ling, Wang
- Yogatama, Dani
- Dyer, Chris
- Blunsom, Phil

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Maintainer

The official AQuA repository of Google DeepMind; ongoing active maintenance is not inferred from repository ownership.

[来源1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问2026-11-07）

### Funders

Unverified

> 字段状态：待核实

> Paper acknowledgments and current operational funding were not verified item by item; institutional affiliation is not a funding source

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## Design goals

### Abilities measured

Generates a natural-language rationale from an algebra word problem and selects an answer, in order to study how the rationale helps solving and explanation.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Design background

Predicting only the option cannot show how the model organizes mathematical reasoning; the original work also models the explanation.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## Construction

### Question sources

The paper collected seeds of GRE/GMAT-style questions from the web and expanded them by crowdsourcing; the official README emphasizes that the public release is the complete crowdsourced data.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 出题者背景

Crowdsourced writing of questions and explanations; the research team developed a rationale-generation model.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Review process

A crowdsourcing process and near-duplicate filtering; the publicly released version and the initial experimental data of the paper are not exactly the same.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Quality control

Section §2 of the paper spot-checks crowdsourced tasks and requires that the answer and the reasoning of a new question differ from the seed; it does not guarantee that every label is correct. The public HF preview contains individual cases in which the derivation contradicts the correct label, for example an equilateral triangle of side 16 whose derivation is 64√3, corresponding to option B, yet labeled D. This is only an example of an error, and an overall error rate is not estimated.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）

### Decontamination

Edit-distance filtering targets near-duplicates and does not guarantee separation of semantic paraphrases, or that later LLMs are free of contamination.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## Data format

### 题量与规模

Each public raw and tokenized configuration has train 97,467, validation 254, and test 254, for a total of 97,975 items. The figure 195,950 on the HF page is the sum of the two configurations and cannot be treated as a count of different questions.

[来源1](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）；[来源2](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### Question types

Each item has question, 5 options, rationale, and correct, and the correct option is one of A–E.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Modalities

Text (mathematical symbols expressed as text); not an original image or video recognition task

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Languages

English question text; for formal or mathematical notation, see the modality and the repository format

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Difficulty

Algebra word problems in an examination style; a rationale can be written in more than one way, and a correct answer does not mean the explanation is logically complete.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Public and hidden splits

Public train, dev, and test files, including tokenized and raw representations of the same questions. Experiments in the original paper use an earlier version. The README states explicitly that this version cannot be released in full, so scores in the original tables are not guaranteed to be reproduced on the current release.

[来源1](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）；[来源2](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

## Evaluation

### Metrics

Option accuracy; the original paper also reports BLEU-4 and perplexity of the rationale, while modern evaluations usually look only at the answer.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 评分

The predicted option is compared with correct; if the explanation is evaluated, it should be reported separately, and option accuracy cannot stand in for the quality of the explanation.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 运行设置

The original work uses supervised training to generate a rationale and then to answer; the number of CoT demonstrations, the token budget, and how the answer is extracted need to be stated separately.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 官方脚本

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 可比性警示

The original paper's 250-item test and the public/Jev254 test, tok and untok, and whether the rationale is evaluated all need to be distinguished.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源2](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）

## Current status

### 核查日期

2026-11-07 （）

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 最新版本与采用证据

The public crowdsourced release differs from the experimental version in the original paper; the release file must be specified

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2017-05-11"
  }
  {
    "version": "v2"
    "submitted_at": "2017-10-10"
  }
  {
    "version": "v3"
    "submitted_at": "2017-10-24"
  }
]
```

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Saturation

A third-party Jev experiment reaches at most 94.1% on test254, but the models selected for the table, the prompts, and label noise all limit interpretation; this is not an official saturation conclusion.

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）

### Contamination and disputes

The official README states explicitly that the initial results in the paper used an old version that could not be released in full; the data that are public now are a version produced entirely by crowdsourcing, and the scores obtained by running the system of the paper will differ. The numbers from the old version in the paper and the question bank that is public now cannot be placed in one ranking.

[来源1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问2026-11-07）

### 版本与衍生关系

MathQA re-annotates operation programs from the AQuA question source; the two cannot be handled as the same data and scoring method.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源2](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07 （）

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### Official leaderboard

Unverified

> 字段状态：待核实

> No independent, continuously updated official leaderboard has been confirmed; experiments in the paper are not presented as an official live leaderboard

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 第三方覆盖

https://arxiv.org/html/2610.11978v1

> Research paper Table2, not a leaderboard kept up continuously.

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）

### 分轨结果

#### Jev paper Table2 / not an official live leaderboard

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Qwen3.8-Max | 94.1 | Accuracy (%), test254/single run | [原表](https://arxiv.org/html/2610.11978v1)，2026-11-07 |
| 2 | Qwen3.8-Flash | 91.7 | Accuracy (%), test254/single run | [原表](https://arxiv.org/html/2610.11978v1)，2026-11-07 |
| 3 | Gemini 3.8 Flash | 91.3 | Accuracy (%), test254/single run | [原表](https://arxiv.org/html/2610.11978v1)，2026-11-07 |



#### Original paper Table3 / an older version that cannot be released in full

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| Not applicable (columns selected within the source, not a global ranking) | Our Model（program induction） | 36.4 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | Seq2Seq | 20.8 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | Seq2Seq + Copy Input | 20.4 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | Seq2Seq + Copy Output | 20.2 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146)，2026-11-07 |



> 字段状态：待核实

> The full text of Jev was opened again to confirm the top three scores; the actual date of the experiment is Unverified, and the unconfirmed date 2026-10-08 is not carried forward. Current public data and the older version in the original paper are kept on strictly separate tracks.

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### Coverage note

Jev full-text Table2 and Appendix A (test254, a single run) and Table3 of the original paper were checked; the two are not the same version or the same protocol, and scores from selected columns are not used to claim an overall first place.

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源3](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

## Contact

### 公开科研联系邮箱

- lingwang@google.com
- dyogatama@google.com
- cdyer@google.com
- pblunsom@google.com

> Only a research email is public on the paper's first page.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 公开反馈

https://github.com/google-deepmind/AQuA/issues

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 官方社交

Unverified

> 字段状态：待核实

> No dedicated official social account has been verified, and personal accounts of the same name are not included

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 隐私说明/政策

Unverified

> 字段状态：待核实

> A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## Original files

### 源站论文PDF

https://arxiv.org/pdf/1705.04146

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### PDF SHA-256

5111754b10c77d287685cc64992c92989eecc9b7cca65089f97c0efd48a4feb7

> SHA-256 of the bytes actually downloaded. It does not mean an existing copy was replaced.

[来源1](https://arxiv.org/pdf/1705.04146)（访问2026-11-07）

### PDF bytes

534332

[来源1](https://arxiv.org/pdf/1705.04146)（访问2026-11-07）

### Folder

```json
{
  "id": "14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
{
  "chinese_intro_doc": {
    "id": "1eZjRI88WySYba1wenrGtoejhe6_rdLemJEcXKXDbWLU"
    "webViewLink": "
    "mimeType": "application/vnd.google-apps.document"
  }
  "local_markdown": "content/benchmarks/aqua-rat.md"
}
```

[来源1](

### 论文副本

```json
{
  "id": "1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J"
  "webViewLink": "
}
```

[来源1](

## Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": "（）"
    Latest review
  }
  {
    "date": "2026-11-07"
    "timezone": "（）"
    Latest review
  }
  {
    "date": "2026-11-07"
    "timezone": " ()"
    Latest review
  }
]
```

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）
