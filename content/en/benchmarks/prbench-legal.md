# PRBench – Legal

> In-depth verification: 2026-11-08. The access date is not the publication date or the experiment run date; unknowns are retained, and "Not disclosed" is not inferred.

The legal track of PRBench evaluates open legal reasoning in work for clients and in professional work. The 500 questions cover 12 legal subject areas. Each question has 10–30 weighted rubric items, and scoring is by an independent expert and by an o4-mini judge. Jurisdiction, disclosure of risk, and transparency of process should be read together with the score, and the rubric total should not be taken as reliability in practice or as objective legal correctness.

Latest review

## Basic information

### Short name

PRBench – Legal

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Full name

Professional Reasoning Bench (PRBench) – Legal

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### Dataset version

The public release set of PRBench: Legal, 500 questions, and its Hard subset of 250 questions; the version is anchored to paper v1 and the HF release files, and no semantic version number is invented.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### Paper version

arXiv:2511.11562v1; the current abs lists only v1.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### 发布时间

First release of the paper: 2025-11-15 03:55:12; this is not presented as the moment the data were first made public.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### 板块

Reasoning

> Benchmark Constitution editorial filing. It is not an official classification.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Subfields

```json
[
  "法律"
  "Professional reasoning"
]
```

> Editorial tag

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### License

The dataset is CC BY 4.0; the official evaluation code is MIT. The two licenses apply to different objects.

[1](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/scaleapi/PRBench/main/LICENSE)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2511.11562

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 代码

https://github.com/scaleapi/PRBench

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Dataset

https://huggingface.co/datasets/ScaleAI/PRBench

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Official homepage

https://labs.scale.com/leaderboard/prbench-legal

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 论文题名

PRBench: Large-Scale Expert Rubrics for Evaluating High-Stakes Professional Reasoning

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Scale AI

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 合作单位

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Authors

```json
[
  "Afra Feyza Akyürek"
  "Advait Gosai"
  "Chen Bo Calvin Zhang"
  "Vipul Gupta"
  "Jaehwan Jeong"
  "Anisha Gunjal"
  "Tahseen Rabbani"
  "Maria Mazzone"
  "David Randolph"
  "Mohammad Mahmoudi Meymand"
  "Gurshaan Chattha"
  "Paula Rodriguez"
  "Diego Mares"
  "Pavit Singh"
  "Michael Liu"
  "Subodh Chawla"
  "Pete Cline"
  "Lucy Ogaz"
  "Ernesto Hernandez"
  "Zihao Wang"
  "Pavi Bhatter"
  "Marcos Ayestaran"
  "Bing Liu"
  "Yunzhong He"
]
```

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### Maintainer

Scale Labs

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Funders

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

## Design goals

### 目标能力

It evaluates open-ended reasoning, jurisdictional context, legal accuracy, application of rules, transparency of process, handling of uncertainty, and disclosure of risk in real legal work, and it is not limited to multiple-choice examination questions.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### 相对既有评测的缺口

General academic examinations cannot adequately measure economic consequences, legal liability, and transparent reasoning.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

## Construction

### 题目与标签来源

182 legal and finance professionals wrote questions from their own work and client problems; law covers 12 topics. 182 is the total number of experts across the two domains and cannot be taken as the number of legal experts.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### 出题/标注背景

Legal annotators hold a JD or an internationally equivalent qualification, have passed a check of their record and an internal qualification test, and contribute only on topics that match their own expertise.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### Review process

Expert 1 writes the dialogue and the rubric; expert 2 checks, revises, and gives feedback. A program checks conformance, a sample receives a final human review, and an independent expert judges whether each criterion is clear and valid.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### Quality control

Independent experts endorse rubric validity at a rate of 93.9%; the judge was also tested on 101 questions, with o4-mini agreeing with experts at 80.2% and experts agreeing with one another at 79.6%. The two percentages cannot be exchanged.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### 去污染与隔离

The paper publishes 1,100 conversations and also keeps a private held-out set to monitor contamination of future models; the size of the private set is Unverified. The public data contain a canary field, which is not enough to treat exclusion from the training corpus as completed.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

## Data format

### Size

The full Legal set has 500 questions and Legal-Hard has 250; 9,092 rubric criteria; the 600 finance questions are a separate track.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### Question types

Open-ended professional dialogue of one turn or at most 10 turns, scored on the model's answer in the last turn; about 30% of full PRBench is multi-turn, and this is not presented as a separate proportion for the legal domain.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### Modalities

```json
[
  "文本"
]
```

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### Languages

Every user turn is written by experts in English; historical assistant turns are sampled from GPT OSS 20B, Mistral Medium, and DeepSeek R1.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### Difficulty

Legal-Hard is a hard subset of 250 questions.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 公开/隐藏划分

The official dataset card publishes Finance, Finance-Hard, Legal, and Legal-Hard; overlapping subsets cannot be added together to produce a question count.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

## Evaluation

### Metrics

Rubric-weighted scoring, clipped to 0–1; values on the leaderboard are kept as displayed on the page.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 判分

o4-mini assigns a binary satisfaction label to each rubric item; the weights are the nonzero values from −10 to +10. For each question, the sum of the weighted satisfaction values is first divided by the sum of the positive weights (a single question may score below zero), the mean is then taken across questions, and finally max(0, mean) is applied. Negative scores are not clipped to 0 on each question before the average. Category charts use min-normalized values separately, and they are not mixed with the main metric.

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/scaleapi/PRBench/main/evals.py)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/scaleapi/PRBench/main/util.py)（访问 2026-11-08）

### 提示/推理设置

The paper evaluates each model independently 3 times and reports the mean and the 95% confidence interval. GPT-5/O3/Grok-4 are set to High. Claude Sonnet 4.5 and Opus 4.1 have thinking budgets of 32K/16K. Gemini 2.5 Pro uses dynamic. The timeout is 60 minutes, with at most 5 attempts, and the last attempt is lowered to low. Tool experiments are listed separately and are not mixed with results that use no tools.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### 官方实现

https://github.com/scaleapi/PRBench. The command is python evals.py config.yaml. results/ reports mean_clipped, and outputs/ keeps the score of each question.

[1](https://raw.githubusercontent.com/scaleapi/PRBench/main/README.md)（访问 2026-11-08）

### 可比性边界

The current web page's Performance Comparison does not explicitly label Full or Hard. The displayed scores are saved as shown, and the scope is not inferred backward from the values. The paper's Hard scores on the 0–1 scale are a separate track. Rank(UB) is 1 plus the number of models whose confidence-interval lower bound is above this model's upper bound. The HF card's 18,692 rubric criteria conflict with 19,356 in the paper and the README, and they cannot be silently unified. The Full/Hard range of the current leaderboard is Unverified.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）；[2](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/scaleapi/PRBench/main/README.md)（访问 2026-11-08）

## Current status

### 核验日

2026-11-08

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

### 本次版本快照

```json
{
  "version": "PRBench public Legal 500 questions / Hard 250 questions (release set verifiable in this check)"
  "heat_confidence": "B"
  "why_trending": "This is mainly a current presentation by a single organization, or continued self-evaluation by a vendor, and it does not represent broad adoption across the industry."
  "evidence_2026_h2": [
    {
      "url": "https://labs.scale.com/leaderboard/prbench-legal"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "organization": "Official maintainer"
      "note": "The current official methods and leaderboard have been opened; the observation date is not presented as the publication date."
    }
  ]
}
```

[1](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）；[2](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

### Paper revisions

```json
[
  {
    "version": "v1"
    "submitted_at": "2025-11-15"
    "timezone": ""
  }
]
```

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

### Saturation

The highest score shown on the current web page is 61.56 and has not reached the top of its percentage scale; Full/Hard labels are missing, so the saturation of the hard subset cannot be determined from this.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

### 污染/限制/争议

The body of the HF card has 18,692 criteria. The paper and the README have 19,356. The paper's split by domain is finance 10,264 and law 9,092. LLM judges and experts agree only 80.2% of the time, and experts agree with one another 79.6% of the time. The results are not a guarantee of safety in professional practice.

[1](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/scaleapi/PRBench/main/README.md)（访问 2026-11-08）；[4](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

### 衍生与相关版本

The same PRBench contains the Finance and Legal domains and the difficult subsets Finance-Hard and Legal-Hard; Hard is a subset of the original domain, not a set of newly added independent questions.

[1](https://arxiv.org/abs/2511.11562)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not the experiment run date)

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

### 官方结果入口

https://labs.scale.com/leaderboard/prbench-legal

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 第三方入口

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| Official current web page / Legal | 1 | [Muse Spark 1.3](https://labs.scale.com/leaderboard/prbench-legal) | 61.56 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 2 | [Muse Spark Open](https://labs.scale.com/leaderboard/prbench-legal) | 59.76 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 3 | [Muse Wonder 1.0](https://labs.scale.com/leaderboard/prbench-legal) | 58.4 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 4 | [Muse Spark 1.1](https://labs.scale.com/leaderboard/prbench-legal) | 57.05 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 5 | [claude-fable 5](https://labs.scale.com/leaderboard/prbench-legal) | 52.56 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 6 | [Muse Spark](https://labs.scale.com/leaderboard/prbench-legal) | 52.29 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 7 | [claude-opus-4-6 (Non-Thinking)](https://labs.scale.com/leaderboard/prbench-legal) | 52.27 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 8 | [Fable 5.1](https://labs.scale.com/leaderboard/prbench-legal) | 51.6 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 9 | [gpt-5.6-sol (max)](https://labs.scale.com/leaderboard/prbench-legal) | 50.5 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 10 | [gpt-5-pro](https://labs.scale.com/leaderboard/prbench-legal) | 49.89 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 11 | [o3-pro](https://labs.scale.com/leaderboard/prbench-legal) | 49.67 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 12 | [Gemini 4 Argon](https://labs.scale.com/leaderboard/prbench-legal) | 49.41 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 13 | [gpt-5.1-thinking](https://labs.scale.com/leaderboard/prbench-legal) | 49.33 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 14 | [gpt-5](https://labs.scale.com/leaderboard/prbench-legal) | 48.96 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 15 | [Gemini 3.8 Flash](https://labs.scale.com/leaderboard/prbench-legal) | 48.9 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 16 | [o3](https://labs.scale.com/leaderboard/prbench-legal) | 48.57 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 17 | [GPT 6 Astra](https://labs.scale.com/leaderboard/prbench-legal) | 48.36 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 18 | [GPT 6.1 Sol](https://labs.scale.com/leaderboard/prbench-legal) | 47.87 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 19 | [Grok 4.7 (xHigh)](https://labs.scale.com/leaderboard/prbench-legal) | 47.62 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 20 | [claude-opus-5-5](https://labs.scale.com/leaderboard/prbench-legal) | 47.58 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 21 | [Deepseek V4p1 Flash 1017](https://labs.scale.com/leaderboard/prbench-legal) | 47.26 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 22 | [gpt-5.2-pro-2025-12-11](https://labs.scale.com/leaderboard/prbench-legal) | 45.44 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 23 | [Minimax M3p1 Flash](https://labs.scale.com/leaderboard/prbench-legal) | 45.08 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 24 | [gpt-5.4 (High)](https://labs.scale.com/leaderboard/prbench-legal) | 44.35 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 25 | [claude-opus-4-5-20251101-thinking](https://labs.scale.com/leaderboard/prbench-legal) | 44.21 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 26 | [gemini-3.1-pro](https://labs.scale.com/leaderboard/prbench-legal) | 44.02 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 27 | [kimi-k2.5](https://labs.scale.com/leaderboard/prbench-legal) | 43.83 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 28 | [gpt-6-luna](https://labs.scale.com/leaderboard/prbench-legal) | 42.85 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 29 | [gemini-2.5-pro](https://labs.scale.com/leaderboard/prbench-legal) | 41.43 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 30 | [gemini-2.5-flash](https://labs.scale.com/leaderboard/prbench-legal) | 41.02 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 31 | [kimi-k2-thinking](https://labs.scale.com/leaderboard/prbench-legal) | 40.9 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 32 | [claude-sonnet-4-5-20250929](https://labs.scale.com/leaderboard/prbench-legal) | 40.84 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 33 | [gemini-3-pro-preview](https://labs.scale.com/leaderboard/prbench-legal) | 40.6 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 34 | [gpt-oss-120b](https://labs.scale.com/leaderboard/prbench-legal) | 40.21 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 35 | [mistral-medium-latest](https://labs.scale.com/leaderboard/prbench-legal) | 39.55 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 36 | [gpt-6-sol](https://labs.scale.com/leaderboard/prbench-legal) | 38.6 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 37 | [qwen.qwen3-235b-a22b-2507-v1:0](https://labs.scale.com/leaderboard/prbench-legal) | 38.3 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 38 | [o4-mini](https://labs.scale.com/leaderboard/prbench-legal) | 38.11 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 39 | [deepseek-v3p1](https://labs.scale.com/leaderboard/prbench-legal) | 37.62 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 40 | [deepseek-r1-0528](https://labs.scale.com/leaderboard/prbench-legal) | 36.61 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 41 | [gpt-4.1](https://labs.scale.com/leaderboard/prbench-legal) | 36.48 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 42 | [kimi-k2-instruct](https://labs.scale.com/leaderboard/prbench-legal) | 36.38 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 43 | [claude-opus-4-1-20250805](https://labs.scale.com/leaderboard/prbench-legal) | 34.0 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 44 | [gpt-4.1-mini](https://labs.scale.com/leaderboard/prbench-legal) | 30.38 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Official current web page / Legal | 45 | [llama4-maverick-instruct-basic](https://labs.scale.com/leaderboard/prbench-legal) | 24.84 | The web page displays weighted rubric scores (a percentage scale; for the data range, see the note on comparability). | 未标注 |
| Body of the official page / historical Legal-Hard | 1 | [GPT-5 Pro](https://labs.scale.com/leaderboard/prbench-legal) | 0.37 | Hard weighted rubric score (0–1) | 未标注 |
| Body of the official page / historical Legal-Hard | 2 | [GPT-5](https://labs.scale.com/leaderboard/prbench-legal) | 0.36 | Hard weighted rubric score (0–1) | 未标注 |
| Body of the official page / historical Legal-Hard | 3 | [o3 (High)](https://labs.scale.com/leaderboard/prbench-legal) | 0.35 | Hard weighted rubric score (0–1) | 未标注 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

### 覆盖与限制

All 45 rows of the current web page were collected, together with 3 historical Hard results from the body text, kept strictly on separate tracks. Rank(UB) on the web page and the display names of the models are kept as they appear; a confidence interval is not used as a standard deviation. The historical high score in the body text was not updated together with the current leaderboard.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）

## Contact

### 项目公开邮箱

```json
[
  "yunzhong.he@scale.com"
]
```

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### GitHub反馈

https://github.com/scaleapi/PRBench/issues

[1](https://raw.githubusercontent.com/scaleapi/PRBench/main/README.md)（访问 2026-11-08）

### 官方社交

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 隐私边界

Only research contact channels explicitly made public in the paper and the official project are used; private information is not collected.

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08）

## Original files

### 原始PDF

https://arxiv.org/pdf/2511.11562v1

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### SHA-256

f36249e74c865bbd352546aa9d9014031dd22e6c86b88a7ab1d07c6b4bb05c59

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### PDF bytes

21111596

[1](https://arxiv.org/pdf/2511.11562)（访问 2026-11-08）

### Folder

Unverified

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Official README"
    "url": "https://raw.githubusercontent.com/scaleapi/PRBench/main/README.md"
  }
  {
    "type": "HF dataset card"
    "url": "https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md"
  }
  {
    "type": "Code MIT license"
    "url": "https://raw.githubusercontent.com/scaleapi/PRBench/main/LICENSE"
  }
]
```

[1](https://raw.githubusercontent.com/scaleapi/PRBench/main/README.md)（访问 2026-11-08）；[2](https://huggingface.co/datasets/ScaleAI/PRBench/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/scaleapi/PRBench/main/LICENSE)（访问 2026-11-08）

### Paper PDF

Unverified

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-07）

## Changelog

[
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

[1](https://labs.scale.com/leaderboard/prbench-legal)（访问 2026-11-08）
