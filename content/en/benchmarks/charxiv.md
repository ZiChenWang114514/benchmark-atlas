# CharXiv

> Benchmark Constitution, in-depth review: 2026-11-08. Official materials were searched again; historical leaderboards, the current snapshot, and vendor self-reports are kept separate; fields without empirical support retain Unverified

CharXiv selects naturally complex charts from research papers and separately examines recognition of descriptive elements and reasoning across visual elements. Each figure has four descriptive questions and one human-reviewed reasoning question. A reasoning question may be selected and revised from GPT-4V candidates, and not every first draft is purely original to a human. The official-site CSV has two Overall columns, corresponding to reasoning and descriptive, and they must be split into two leaderboards. Public val answers and hidden test answers also cannot be mixed.

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

## Basic information

### Short name

CharXiv

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

### Full name

CharXiv

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

### 版本边界

v1.0

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### Paper version

arXiv v1

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### Release date

2024-06-27 02:50:11 (arXiv v1; the calendar date on the original site is 2024-06-26)

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-08）

### 板块

Multimodal

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. The classification is not claimed to be set by the benchmark's maintainers.

### 领域

```json
[
  "Understanding of real research charts"
]
```

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

### 许可与限制

Original questions and answers are CC BY-SA 4.0, and the code is Apache-2.0; copyright in the charts belongs to the original authors. The official HF card further states that the material is for evaluation only and is not allowed for training, and these restrictions on use must be read together.

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

### Paper

https://arxiv.org/abs/2406.18521

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

### Code

https://github.com/princeton-nlp/CharXiv

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

### Dataset

https://huggingface.co/datasets/princeton-nlp/CharXiv

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/princeton-nlp/CharXiv)（访问2026-11-07）

### Official homepage

https://charxiv.github.io/

[Source 1](https://charxiv.github.io/) (accessed 2026-11-07); [Source 2](https://arxiv.org/abs/2406.18521) (accessed 2026-11-07)

### 论文题名

CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

## Origin and maintenance

### Initiators

The lead author team is Princeton Language and Intelligence (Princeton University), and collaborating author affiliations include the University of Wisconsin-Madison and the University of Hong Kong.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### Partner organizations

```json
[
  "Princeton Language and Intelligence (PLI), Princeton University"
  "University of Wisconsin–Madison"
  "The University of Hong Kong"
]
```

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### Authors

```json
[
  "Wang, Zirui"
  "Xia, Mengzhou"
  "He, Luxi"
  "Chen, Howard"
  "Liu, Yitao"
  "Zhu, Richard"
  "Liang, Kaiqu"
  "Wu, Xindi"
  "Liu, Haotian"
  "Malladi, Sadhika"
  "Chevalier, Alexis"
  "Arora, Sanjeev"
  "Chen, Danqi"
]
```

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 维护入口

The princeton-nlp / CharXiv author team; the official README welcomes Issues and PRs, and Zirui Wang receives inquiries about the data-construction scripts.

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 资助披露

Microsoft Accelerate Foundation Models Academic Research Initiative; personal support for the authors also includes the Apple Scholars in AIML Fellowship and the Gordon Wu Fellowship.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

## Design goals

### 测量对象

Recognition of basic elements in real scientific figures and integrated reasoning across complex visual elements.

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### 既有评测的缺口

Homogenized charts and template questions overestimate model ability; charts native to scientific research contain richer structure and visual variation.

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

## Construction

### 题源

Charts are selected by hand from arXiv papers in eight major disciplines, and descriptive questions and reasoning questions are designed; some reasoning questions were generated or inspired by GPT and then screened and verified by hand. Not every first draft is purely the work of a person.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### 构建人员

Annotators of the reasoning questions are graduate students; for each figure they first see 10 candidate QA sets generated by GPT-4V, then select, edit, or write a question themselves. Not every draft is called purely original work by a human expert.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-08）

### 审核

All charts and questions are selected, organized, and verified by human experts; description questions focus on basic elements, and reasoning questions require integrating information within the figure.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 质控

All charts and questions are selected, organized, and verified by human experts; description questions focus on basic elements, and reasoning questions require integrating information within the figure.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源3](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

> The HF dataset card also carries a public Erratum: the reasoning answer for 0.jpg is wrong; expert manual review does not justify a claim of zero annotation errors.

### 去污染及边界

Test answers are deliberately set to null and are not published, so that the test answers do not leak. The datasheet of the paper also acknowledges that figures may overlap with SciCap, SciGraphQA, and Multimodal Arxiv, so it cannot be guaranteed that the images have not entered pretraining.

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

## Data format

### 规模与计数口径

```json
{
  "charts": 2323
  "descriptive_questions": 9292
  "reasoning_questions": 2323
  "validation_charts": 1000
  "test_charts": 1323
  "documentation_conflict": "The README overview separately states 2333 images, which disagrees with 2323 in paper Table 2 and in the body of the README; the conflict is retained."
}
```

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-08）；[来源2](https://github.com/princeton-nlp/CharXiv)（访问2026-11-08）

### Question types

Open question answering of the descriptive and reasoning kinds; the validation set has 1,000 charts and 5,000 questions.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### Modalities

Image+text

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### Languages

English (official HF dataset card language: en); this is the official language label and is not used to infer the language proportions of all original-paper text in the figures.

[来源1](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

### Difficulty

Naturally complex charts from eight major disciplines; no unified easy/medium/hard distribution was verified in this batch.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 划分与公开范围

Charts are split at random into val 1000 and test 1323; val publishes the full 5,000 QA items, and the answers of test are set to null in the public JSON. The unit of the split is the chart, and 1,323 is not written as the total number of test questions.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-08）；[来源2](https://github.com/princeton-nlp/CharXiv)（访问2026-11-08）

## Evaluation

### Metrics

GPT-4o judges the answers and aggregates description accuracy and reasoning accuracy; the two scores are not merged.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 评分

GPT-4o judges the answers and aggregates description accuracy and reasoning accuracy; the two scores are not merged.

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 提示与运行条件

Zero-shot, with natural instructions by question category; the official scripts generate, score, and aggregate separately, and the grader model snapshot must be recorded.

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### 官方评测入口

https://github.com/princeton-nlp/CharXiv

[来源1](https://github.com/princeton-nlp/CharXiv)（访问2026-11-07）

### 可比性边界

Both the official CSV and the leaderboard in the README may be historical results; CharXiv reas. in MMVistaReason is the CompassVerifier protocol of another study, not a refresh of the official leaderboard.

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源3](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）

## Current status

### 复核时间

2026-11-08

[来源1](https://charxiv.github.io/)（访问2026-11-08）

### 当前版本

v1.0

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 论文修订与后续使用

```json
{
  "revisions": [
    {
      "version": "v1"
      "date_kst": "2024-06-27"
    }
  ]
  "continued_use_2026h2": [
    {
      "url": "https://arxiv.org/html/2610.01352v2"
      "date": "2026-10-23"
      "note": "MMVistaReason v2 §4.1 and Table 2 actually evaluate CharXiv (the reasoning setting), comparing 4B/9B and other vision-language models; splits such as mini/val are not counted separately."
      "date_kst": "2026-10-23"
      "verified_in_round1": "The body of arXiv v2, §4.1 and Table2, and the abs submission history were opened again, and the actual evaluation was confirmed; source-site v2 is 2026-10-22 16:54:37 UTC."
    }
  ]
  "verification": "The actual evaluation sections and tables whose evidence text was opened and checked, not judged only by whether a reference or web page is still available."
  "arxiv_revisions_kst": [
    {
      "version": "v1"
      "submitted_at_kst": "2024-06-27"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-08）

### Saturation

The top three on official val reasoning are 78.6%, 72.0%, and 64.2%. Human is 80.5%, but the metric for descriptive questions is independent, and the hidden test is not the same as val. Only the degree of closeness is recorded here. Being close to a historical human reference is not declared to be saturation of the whole task.

[来源1](https://charxiv.github.io/data/val_result.csv)（访问2026-11-07）

### 风险与冲突

The official-site CSV and the static leaderboard in the README were not updated together. The current snapshot prefers the official-site CSV. The conflict between 2,323 charts and 2,333 images in the README guide is retained side by side. Hidden test answers do not mean the images are free of contamination. The CompassVerifier protocol of MMVistaReason cannot be mixed with the official GPT-judge results. The official HF Erratum states that the reasoning reference answer for 0.jpg is wrong (found by the community, #2). The dataset card says a future version will correct it, and the answer is not rewritten here.

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://charxiv.github.io/data/val_result.csv)（访问2026-11-07）；[来源3](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源4](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）；[来源5](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

### 衍生与后续工作

Unverified

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://charxiv.github.io/)（访问2026-11-08）

### 官方榜入口

https://charxiv.github.io/#leaderboard

[来源1](https://charxiv.github.io/)（访问2026-11-07）

### 第三方榜入口

Unverified

[来源1](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问2026-11-07）

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

### 逐轨结果

```json
[
  {
    "rank": 1
    "model": "o3 (high)"
    "score": 78.6
    "metric": "accuracy (%)"
    "track": "Official-site CSV/val/reasoning overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 2
    "model": "o4 mini (high)"
    "score": 72.0
    "metric": "accuracy (%)"
    "track": "Official-site CSV/val/reasoning overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 3
    "model": "Claude 3.7 Sonnet"
    "score": 64.2
    "metric": "accuracy (%)"
    "track": "Official-site CSV/val/reasoning overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 1
    "model": "o3 (high)"
    "score": 95.0
    "metric": "accuracy (%)"
    "track": "Official-site CSV/val/descriptive overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 2
    "model": "o4 mini (high)"
    "score": 94.3
    "metric": "accuracy (%)"
    "track": "Official-site CSV/val/descriptive overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 3
    "model": "GPT 4.5"
    "score": 90.0
    "metric": "accuracy (%)"
    "track": "Official-site CSV/val/descriptive overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "model": "MMVistaReason-4B (MVR-4B)"
    "score": 66.9
    "unit": "%"
    "metric": "Answer accuracy under the protocol of the paper (CompassVerifier)"
    "scope": "CharXiv reasoning"
    "date": "2026-10-23"
    "accessed": "2026-11-08"
    "source_url": "https://arxiv.org/html/2610.01352v2"
    "provenance": "Table 2 as reported by the MMVistaReason authors themselves; VLMEvalKit, T=0, max16384; §7.3 replaces traditional string matching with CompassVerifier, and this is not the official leaderboard or an independent evaluation by AA"
    "date_basis": "Converted from the arXiv v2 submission time; it is not a Not disclosed evaluation-run date."
    "track": "MMVistaReason v2/reasoning/CompassVerifier/author self-report"
    "rank": null
  }
  {
    "model": "MMVistaReason-9B (MVR-9B)"
    "score": 68.8
    "unit": "%"
    "metric": "Answer accuracy under the protocol of the paper (CompassVerifier)"
    "scope": "CharXiv reasoning"
    "date": "2026-10-23"
    "accessed": "2026-11-08"
    "source_url": "https://arxiv.org/html/2610.01352v2"
    "provenance": "MMVistaReason author self-report Table 2; the same protocol, and not ranked together with other leaderboards without conditions"
    "date_basis": "Converted from the arXiv v2 submission time; it is not a Not disclosed evaluation-run date."
    "track": "MMVistaReason v2/reasoning/CompassVerifier/author self-report"
    "rank": null
  }
]
```

[来源1](https://charxiv.github.io/data/val_result.csv)（访问2026-11-08）；[来源2](https://arxiv.org/html/2610.01352v2)（访问2026-11-08）

### 覆盖边界

The official-site CSV was read again. The reasoning and descriptive columns are each ranked on their own, and the Human and Random baselines are excluded; the API snapshot and the run date missing from the CSV remain Unverified. MMVistaReason uses another judge protocol and is listed on its own, and is never ranked across tracks.

[来源1](https://charxiv.github.io/data/val_result.csv)（访问2026-11-08）；[来源2](https://arxiv.org/html/2610.01352v2)（访问2026-11-08）

## Contact

### 公开研究联系

```json
[
  "zw1300@cs.princeton.edu"
]
```

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

> The consultation email explicitly provided in the README is used; the email in the paper byline may differ, and the old address is not treated as no longer valid.

### 项目反馈

https://github.com/princeton-nlp/CharXiv/issues

[来源1](https://github.com/princeton-nlp/CharXiv)（访问2026-11-07）

### 官方社交入口

https://x.com/zwcolin/status/1816948825036071196

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

> The project discussion link cited in the official README; X content was not visited, and no message was sent.

### 联系信息边界

Only officially published project feedback channels are recorded; private contact details are neither collected nor inferred.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-07）

## Original files

### 原始PDF

https://arxiv.org/pdf/2406.18521

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### PDF SHA-256

696ad9488b3d5f6d842fd1278d5be0fa2263676740d65bf1469bdd618af8a36c

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

> Checksum of the originally downloaded bytes. They were not compressed or rewritten.

### PDF bytes

12563743

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### 目录

```json
{
  "id": "1pSe5r0MWe3eNJElkRmQkwLD06Lmy7nLh"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
[
  {
    "kind": "Chinese introduction"
    "id": "1TenxIC3WJjBkQ8biE0hfhDWmbMFdwrml9zIJH1UlYf4"
    "webViewLink": "
  }
]
```

[来源1](

### 论文归档

```json
{
  "id": "18fClV3CX6-yQ6K_VIjCX64Rbe-IFRP8J"
  "webViewLink": "
}
```

[来源1](

## Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-07"
    "timezone": ""
    "round": "1 / 深度实证复核"
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]
```

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-08）；[来源2](https://charxiv.github.io/)（访问2026-11-08）
