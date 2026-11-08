# RAG-Safety-Bench

> In-depth verification: 2026-11-08. The access date is not the publication date or the experiment run date; unknowns are retained, and "Not disclosed" is not inferred.

RAG-Safety-Bench places the same harmful request under four controlled conditions: no retrieval, an oracle that contains the answer, same-topic documents without the answer, and random benign documents. It is used to explain why RAG changes safety behavior. Unsafe-capability accuracy, the harm rate, and the refusal rate are three different things: answering harmful questions more accurately does not mean the system is safer. The frozen public inputs can be used for independent retesting, but they do not include the paper's private v2 rescoring artifacts.

Latest review

## Basic information

### Short name

RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Full name

RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Dataset version

v14 frozen release: v14_full_987 and v14_balanced_346.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### Paper version

arXiv v1

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 发布时间

2026-09-10

> The first-release date of the original paper; it is not guaranteed to equal the date the data files were first made public.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 板块

Safety

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Subfields

```json
[
  "Retrieval-augmented system safety"
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### License

The official materials differ. The paper says the data are CC BY-SA 4.0. LICENSING.md in the repository is still a split proposal awaiting approval by the authors, with the data under CC BY-SA 4.0 and the original code under MIT. Before that approval, no further license is granted for reuse beyond the third-party terms.

[1](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2609.11758

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 代码

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Dataset

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Official homepage

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 论文题名

RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## Origin and maintenance

### Initiators

University of Ottawa; authors Adithiyan Rajan Indira Saravanan and Kathleen C. Fraser.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 合作单位

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Authors

```json
[
  "Saravanan, Adithiyan Rajan Indira"
  "Fraser, Kathleen C."
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Maintainer

Official code and feedback are provided by the repository The-Safe-AI-Lab/RAG-Safety-Bench; an individual’s duty of continued maintenance, and any limit on response time, are Unverified.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### Funders

NSERC Discovery Grant RGPIN-2026-05716. Computing support from Compute Ontario and the Digital Research Alliance of Canada.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## Design goals

### 目标能力

Retrieval conditions are controlled so that safety changes, capability changes, and refusal changes caused by RAG can be distinguished.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 相对既有评测的缺口

RAG evaluations often mix answer correctness, harmful output, and refusal, or do not control whether the evidence actually contains the answer.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## Construction

### 题目与标签来源

Generated with the aid of Wikipedia material and Claude Sonnet4.5, and with a self-check; four retrieval conditions are constructed.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 出题/标注背景

Both authors give their affiliation as the University of Ottawa Faculty of Engineering; Claude Sonnet-4.5 assisted in constructing candidate questions, and GPT-4.1-mini audited the context. The authors' institution can be verified, and clinical, legal, or other professional qualifications that were not stated are not inferred.

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### Review process

GPT-4.1-mini is used to audit the context; for the balanced sample, availability of the answer in the oracle is checked.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Quality control

The full/balanced selection manifest and the oracle audit record are frozen. The paper's balanced oracle audit is 200 yes/146 partial. Human verification of the refusal classification covers 100 outputs, with human-model agreement of 95–96% and κ 0.90–0.92. This verification is not generalized into the reliability of the three harmfulness judges.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 去污染与隔离

Wiki sources and the version manifest support tracing; the prompt used for generation by Claude requires questions that are not duplicates, and balanced is an exact subset of full. A dedicated check that excludes contamination of model pretraining remains Unverified.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

## Data format

### Size

987 queries in full, a balanced subset of 346, and 20 subcategories; the 346×4 conditions yield 1,384 experimental records per model, not 1,384 independent original questions.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Question types

Open question answering; four conditions: no RAG, oracle answers, same-topic material with no answers, and random benign material

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Modalities

Text

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Languages

English

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Difficulty

A controlled comparison of safe and unsafe knowledge under different retrieval conditions; accuracy on harmful knowledge is not treated directly as safety.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 公开/隐藏划分

Frozen inputs, provenance manifests, and generation configurations are public; the original model responses, judge traces, and the unsafe_majority_v2 rescoring artifacts are deliberately withheld, and the local judge configuration is only an implementation example.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

## Evaluation

### Metrics

harmfulness, accuracy, and refusal are reported separately.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 判分

Harmfulness is decided by a majority of the three judges Llama-Guard-3-8B, ShieldGemma-2B, and WildGuard; accuracy is judged by Claude Opus4.7; categories of refusal are analyzed separately.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 提示/推理设置

temperature=0.0, top_p=1.0, and max_new_tokens=1024; a document uses a cleaned prefix of the full text, at most 12,000 characters per document; the paper also specifies seed=42.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 官方实现

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench)（访问 2026-11-07）

### 可比性边界

A low unsafe accuracy does not necessarily mean strong safety; harmfulness and refusal should be looked at together; the oracle evidence still covers only some of the answers and cannot be treated as evidence that is 100% complete.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## Current status

### 核验日

2026-11-08

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

### 本次版本快照

```json
{
  "version": "v14: full 987 questions/3,948 condition rows; balanced 346 questions/1,384 condition rows"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.11758v1"
      "date": "2026-09"
      "note": "The original paper was released in H2 and actually reports experiments with five models and four retrieval conditions; these are the authors' first experiments, not an independent later citation."
    }
  ]
}
```

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### Paper revisions

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-09-11"
    "timezone": ""
  }
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### Saturation

This benchmark must analyze harmfulness, unsafe-capability, and refusal jointly. A single capability accuracy cannot be used to conclude that safety is saturated. The highest oracle unsafe-capability in the paper is 90.7%, and that is not a safety attainment rate.

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 污染/限制/争议

Oracle answerability is not, in every case, a complete answer: in the balanced set, 200 questions are yes and 146 are partial. The repository states explicitly that the private v2 rescoring procedure and the original outputs were not released with the package. An example of a local judge cannot replace the rescoring artifacts of the paper.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 衍生与相关版本

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not the experiment run date)

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

### 官方结果入口

https://arxiv.org/abs/2609.11758

> When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 第三方入口

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| Paper v1 Table 3 / balanced 346 / Non-RAG | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 25.7 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Oracle | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 74.9 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / On-topic | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 8.7 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Random | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 2.0 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Non-RAG | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 6.4 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Oracle | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 41.3 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / On-topic | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 4.3 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Random | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 0.3 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Non-RAG | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 26.0 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Oracle | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 90.7 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / On-topic | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 18.8 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Random | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 0.9 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Non-RAG | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 10.4 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Oracle | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 41.0 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / On-topic | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 12.7 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Random | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 3.2 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Non-RAG | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 15.9 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Oracle | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 82.9 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / On-topic | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 17.3 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |
| Paper v1 Table 3 / balanced 346 / Random | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 2.3 | unsafe-capability answer accuracy (%), not harmfulness | 2026-09-11 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 覆盖与限制

All 20 unsafe-capability values in Table 3, five models × four RAG conditions, are included in full. benign capability in the original table belongs to MIRAGE and was not mixed into this benchmark's leaderboard. Where harmfulness in the figure has no value that can be verified point by point, it is not estimated by reading the figure. Raw outputs, judge traces, and the private v2 rescoring artifacts are explicitly not public. A local judge implementation is not equivalent.

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

## Contact

### 项目公开邮箱

```json
[
  "aindi023@uottawa.ca"
  "kathleen.fraser@uottawa.ca"
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### GitHub反馈

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench/issues

> Public feedback entry point; no question was sent.

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 官方社交

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 隐私边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原始PDF

https://arxiv.org/pdf/2609.11758

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-07）

### SHA-256

0eb8c0582d538136e2ac32fd51bffab170bac16f9173309c9f68870808bdb490

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### PDF bytes

2137960

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### Folder

```json
{
  "id": "1qW8zMCcfafxtK0w_x4SyifexNN8DZ0uh"
  "webViewLink": "
}
```

[1]( 2026-11-07）

### 其他材料

```json
[
  {
    "kind": "Chinese introduction"
    "id": "1F6zykWwlZb0vzbaaDz6pW4mUcfqD5g4xRsQbwKbVm5o"
    "webViewLink": "
  }
  {
    "type": "Official dataset card (not an HF release)"
    "url": "https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md"
  }
  {
    "type": "License proposal and restrictions"
    "url": "https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md"
  }
]
```

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md)（访问 2026-11-08）

### Paper PDF

{
  "id": "1XGmcQ4mrUXYV6AjzHXA0P6xrauG_mn3z"
  "webViewLink": "
}

[1]( 2026-11-07）

## Changelog

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

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）
