# StrongREJECT

Latest review

StrongREJECT is, first, an evaluator of jailbreak outputs and a prompt set of 313 requests, rather than a general leaderboard of model safety. It asks whether an answer is specific, credible, and genuinely of help to a harmful request, and it corrects the misjudgment that “the absence of a refusal is a successful jailbreak.” The MAE leaderboard below only checks agreement between automatic scores and human labels. Lower is better, and it does not mean that the target model is safer.

[Source 1](https://arxiv.org/abs/2402.10260) (accessed 2026-11-08); [Source 2](https://github.com/dsbowen/strong_reject) (accessed 2026-11-08); [Source 3](https://strong-reject.readthedocs.io/en/latest/) (accessed 2026-11-08)

## Basic information

### Short name

StrongREJECT

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Full name

StrongREJECT

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Benchmark version

A public prompt set of 313 requests; the rubric and the Gemma-2B fine-tuned evaluator are two implementations, and the release version of the independent package is Unverified.

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### Paper version

v2 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### Release date

2024-02-16 (arXiv v1 2024-02-16; the arXiv web-page calendar date is 2024-02-15 UTC)

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### Section

Safety

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 领域

```json
[
  "Harmful-request completion and refusal evaluation"
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 许可与适用范围

MIT (this project's code); the assembled data inherit the constraints of their sources: the README notes that some sources have no license, so MIT cannot be applied directly to all of the data.

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2402.10260

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Code

https://github.com/dsbowen/strong_reject

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 数据

https://github.com/dsbowen/strong_reject

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Official entry

https://strong-reject.readthedocs.io/

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Paper title

A StrongREJECT for Empty Jailbreaks

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## Origin and maintenance

### Initiators

The associated author team at UC Berkeley / Center for Human-Compatible AI.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 合作/参与机构

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Authors

```json
[
  "Souly, Alexandra"
  "Lu, Qingyuan"
  "Bowen, Dillon"
  "Trinh, Tu"
  "Hsieh, Elvis"
  "Pandey, Sana"
  "Abbeel, Pieter"
  "Svegliato, Justin"
  "Emmons, Scott"
  "Watkins, Olivia"
  "Toyer, Sam"
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Maintainer

Official code and feedback are provided by the dsbowen/strong_reject repository; individual responsibility for continued maintenance, and response-time limits, have not been verified.

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### Funders

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## Design goals

### Abilities measured

Judges whether a jailbreak output truly provides specific, credible harmful assistance, rather than judging only whether it refuses.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Design background

A simple non-refusal metric wrongly counts vague, useless, or untrustworthy answers as jailbreak successes.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## Construction

### Question sources

Screened and organized from existing jailbreak data and system cards, including AdvBench, DAN, MasterKey, MaliciousInstruct, HarmfulQ, and the GPT-4 System Card. Organized into 6 categories of harm.

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 出题者背景

The research team combined human work with GPT-4 and pplx-70b-online to assist in writing and checking.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Review process

Semantic deduplication; checks of refusals, answerability, and prompt quality, with human review.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Quality control

Human annotation is used to validate the structured rubric and the fine-tuned evaluator.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 污染控制

Existing public harmful requests are compiled, and the paper does not claim that the prompt collection is free of pretraining contamination; prompts in the evaluator’s validation set are distinguished from fine-tuning training and validation prompts. Agreement on the evaluator’s validation set cannot be taken as proof that the target model has not seen the requests.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

## Data format

### 题量

313 prohibited requests, 6 major categories.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 任务形式

An evaluation of response completeness for prohibited requests; harmful operational content is not reproduced on this page

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Modalities

Text

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Languages

English

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Difficulty

Focuses on the specificity and the persuasiveness of the answer, rather than only counting whether refusal words appear.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### Public and hidden splits

The prompts and the evaluator are public; the validation set of the model judge and the attack tests on the actual target model are not the same object.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## Evaluation

### Metrics

A combined score of refusal, specificity, and persuasiveness, normalized to 0–1; there is also a metric of agreement between the evaluator and humans.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 评分

A refusal is scored zero; otherwise specificity and persuasiveness are combined. A rubric evaluator and a Gemma-2B fine-tuned evaluator are provided.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 运行设置

Harmful requests and target responses are scored according to the official evaluation prompt, and the version of the judge model must be recorded.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 评测工具

The strong_reject package provides evaluate_dataset. A rubric-based LLM evaluator and a fine-tuned Gemma 2B evaluator are two different implementations, and a report has to say which of the two was used.

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### Comparability

Rubric scores, fine-tuned evaluator scores, and binary ASR are different; evaluator MAE is also not a safety score for the target model.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 当前版本及历史热度证据

The current official documentation still describes six request categories and two StrongREJECT evaluators; WMDP beta is not mixed into the original inventory of 313 questions.

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2024-02-16"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2024-08-27"
    "timezone": ""
  }
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 饱和与能力边界

The core of this benchmark is a jailbreak evaluator, not a unified leaderboard of model capability. The paper’s MAE of 0.077/0.084 measures error relative to human labels, and closeness to 0 or 1 cannot be used to judge whether the target model’s safety capability is saturated.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 风险与争议

The README states that some of the source data have no license. The MIT license of the project does not, by itself, make up the missing authorization of a source. The H2 comparison of judges uses the rubric version that shares the Qwen3.8-27B-Uncensored backbone, and it cannot be treated as a check of a scorer that was fine-tuned on its own.

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 系列与衍生关系

The official documentation also has a WMDP open question-answering beta: multiple choice is converted to open questions, with hazard weights and a StrongREJECT-style evaluator; it is not a same-version expansion of the original set of 313 requests.

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2402.10260) (accessed 2026-11-08); [Source 2](https://github.com/dsbowen/strong_reject) (accessed 2026-11-08); [Source 3](https://strong-reject.readthedocs.io/en/latest/) (accessed 2026-11-08)

### Official entry

https://arxiv.org/abs/2402.10260

> When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 独立来源

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 分来源与协议结果

#### paper v2 Table 1 evaluator validation

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 9 | String matching | 0.58 | MAE vs human labels；lower is better | {"bias":0.484,"mae_95ci_plus_minus":0.03,"mae_human_nonzero":0.372,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":-0.394} |
| 8 | Jailbroken - binary | 0.407 | MAE vs human labels；lower is better | {"bias":0.354,"mae_95ci_plus_minus":0.03,"mae_human_nonzero":0.254,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":-0.291} |
| 7 | PICT | 0.291 | MAE vs human labels；lower is better | {"bias":0.232,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.278,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":0.101} |
| 6 | GPT-4 Judge | 0.262 | MAE vs human labels；lower is better | {"bias":0.208,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.212,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.157} |
| 5 | PAIR | 0.205 | MAE vs human labels；lower is better | {"bias":0.152,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.224,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.249} |
| 4 | OpenAI moderation API | 0.197 | MAE vs human labels；lower is better | {"bias":-0.161,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.761,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":-0.103} |
| 3 | HarmBench | 0.09 | MAE vs human labels；lower is better | {"bias":0.013,"mae_95ci_plus_minus":0.01,"mae_human_nonzero":0.239,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.819} |
| 2 | StrongREJECT fine-tuned | 0.084 | MAE vs human labels；lower is better | {"bias":-0.023,"mae_95ci_plus_minus":0.01,"mae_human_nonzero":0.244,"mae_human_nonzero_95ci_plus_minus":0.02,"spearman_jailbreak_rank":0.9} |
| 1 | StrongREJECT rubric | 0.077 | MAE vs human labels；lower is better | {"bias":0.012,"mae_95ci_plus_minus":0.01,"mae_human_nonzero":0.196,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.846} |

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 覆盖与时效

The validation statistics in Table 1 of the paper, including MAE for the nine automatic evaluators, are included in full; rank is reordered only by MAE, lower is better, and is not a safety ranking of the attacked models. The HF walledai/StrongREJECT card has been opened, but it is a third-party mirror and does not list an independent real-time unified safety leaderboard.

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/walledai/StrongREJECT)（访问 2026-11-08）

## Contact

### 公开工作邮箱

```json
[
  "alexandrasouly@gmail.com"
  "sdt@berkeley.edu"
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方反馈

https://github.com/dsbowen/strong_reject/issues

> Public feedback entry point; no question was sent.

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 公开社区

The official documentation and GitHub Issues are verified channels for feedback; a third-party HF mirror is not treated as an official maintenance account.

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）；[来源2](https://github.com/dsbowen/strong_reject)（访问 2026-11-08）

### 隐私边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2402.10260

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-08）

### PDF SHA-256

10caab98ed5a75b019ef3c8a6697527f83edda067516996d2cb612f02ff746bc

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-08）

### PDF bytes

```json
600542
```

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-08）

### Folder

```json
{
  "id": "1Rjik34iUFEZBTeLqjtMXs8us5Ea3NsvV"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

### 其他材料

```json
[
  {
    "kind": "Chinese introduction"
    "id": "15uyExEs5PXDPaRliDItqwcrgvzhdto9GUXOBBbZueIE"
    "webViewLink": "
  }
  {
    "type": "Opened primary material"
    "url": "https://arxiv.org/abs/2402.10260"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://github.com/dsbowen/strong_reject"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://strong-reject.readthedocs.io/en/latest/"
    "accessed": "2026-11-08"
  }
]
```

[Source 1](https://arxiv.org/abs/2402.10260) (accessed 2026-11-08); [Source 2](https://github.com/dsbowen/strong_reject) (accessed 2026-11-08); [Source 3](https://strong-reject.readthedocs.io/en/latest/) (accessed 2026-11-08)

### PDF归档

```json
{
  "id": "1qVDkFDcnFVOGYrw9wE7T7e6myH6wJoor"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

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
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]
```

[Source 1](https://arxiv.org/abs/2402.10260) (accessed 2026-11-08); [Source 2](https://github.com/dsbowen/strong_reject) (accessed 2026-11-08); [Source 3](https://strong-reject.readthedocs.io/en/latest/) (accessed 2026-11-08)
