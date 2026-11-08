# MultiChallenge

> Verification date: 2026-11-08. Unknowns are not filled in; the date on which the source was accessed is not the experiment run date.

MultiChallenge examines multi-turn instruction following, inference and memory of user information, reliable version editing, and self-consistency. The original paper and the original GitHub data have 273 conversations. The current official HF test has 266 conversations. There is still no verifiable official explanation of this difference, and one denominator cannot be used to describe all scores in general. The online leaderboard has changed the judge and 54 rubric items. Multiple attempts in the original repository are scored as success if at least one attempt succeeds. Human evaluation, historical automatic evaluation, the current online leaderboard, and best-of-attempts must therefore be kept separate.
[Sources for this page](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md) (accessed 2026-11-08)

[Supplementary basis of the guide](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl) (accessed 2026-11-08)

[Additional sources for this page](https://github.com/ekwinox117/multi-challenge/blob/main/README.md) (accessed 2026-11-08)

[Supplementary guide basis](https://labs.scale.com/leaderboard/multichallenge?tab=large) (accessed 2026-11-08)

## Basic information

### Short name

MultiChallenge

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### Full name

MultiChallenge

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 数据/基准版本

Official-leaderboard convention for the judging and question revision of 2026-02-03

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Paper version

arXiv v2（2025-03-06 13:41:56 ）

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Release date

2025-01-29 12:29:24 （arXiv v1）

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Section

Language

> Editorial filing. It does not represent an official classification.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### Subfields

Multi-turn instruction retention；User-information inference memory；版本编辑；自洽

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/MultiChallenge)（访问 2026-11-08）

### 许可边界

The official HF data card is CC-BY-4.0; the root of the original GitHub repository does not list a LICENSE file, so the evaluation code cannot also be declared CC-BY-4.0 on that basis. The code license is Unverified.

> 状态：待核实。

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源2](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2501.17399

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 代码入口

https://github.com/ekwinox117/multi-challenge

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Dataset

https://huggingface.co/datasets/ScaleAI/MultiChallenge

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### Official homepage

https://labs.scale.com/leaderboard/multichallenge?tab=large

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### Paper title

MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

## Origin and maintenance

### Initiators

Scale AI

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Partner organizations

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### Authors

Ved Sirdeshmukh、Kaustubh Deshpande、Johannes Mols、Lifeng Jin、Ed-Yeremai Cardona、Dean Lee、Jeremy Kritz、Willow Primack、Summer Yue、Chen Xing

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Current maintainer

Scale AI

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Funders

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

## Design goals

### Abilities measured

Instruction retention, inferred memory of user information, reliable version editing, and self-coherence across multi-turn dialogue, jointly examining attention to context and reasoning.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 设计动机

MT-Bench is nearly saturated; multi-turn instruction tests that cover format alone do not cover mixed reasoning and constraints in natural conversation.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

## Construction

### Question sources

Multiple agents synthesize candidates, which trained annotators then review and edit; only samples that cause at least three of the six screening models to fail reasonably are retained.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 出题/构建者背景

Human annotators recruited and trained by Scale AI edit the multi-agent candidates; the review pool is independent of the editors, and an item is accepted only after two layers of review.

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### Review process

Reviews consistency of definitions, natural realism, and the plausibility of failures; after the initial edit there are two further layers of independent review.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Quality control

Reviews consistency of definitions, natural realism, and the plausibility of failures; after the initial edit there are two further layers of independent review.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 去污染/泄漏控制

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

## Data format

### 精确规模与统计口径

```json
{
 "paper_v2_conversations": 273
 "original_github_jsonl_rows": 273
 "original_axes": {
 "INFERENCE_MEMORY": 113
 "SELF_COHERENCE": 50
 "INSTRUCTION_RETENTION": 69
 "RELIABLE_VERSION_EDITING": 41
 }
 "current_hf_test_rows": 266
 "scope_caveat": "The count of 273 in the original paper and the original JSONL disagrees with the current HF count of 266; an announcement of 54 rubric revisions is not an explanation of the deletion of 7 questions. The reason for the difference of 7 questions, and the exact number of samples behind each current score on the official website, have not been verified, and a single denominator is not permitted."
 "turn_count": "The paper allows at most 10 turns (a user-assistant exchange); HF num_turns is a message count and shows 3 to 19, so 19 messages must not be written as 19 round trips."
}
```

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

### Question types

Given the dialogue history, produce an open answer to the last user request.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### Modalities

Text

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 语言/代码语种

English (stated explicitly by language: en on the official HF card and by the Dataset Description)

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

### 难度结构

Only examples in which at least three of the six screening models fail in a reasonable way are accepted; the difficulty comes from the instruction, the inference, the editing, and self-coherence, not from the length of a long context alone. Samples whose harder rubrics exceed what a reliable judge can do were not released.

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### Public and hidden splits

The current HF release publishes only the test split, 266 examples in total. The original paper and the original GitHub JSONL have 273 examples. The official source says it is temporarily holding back a portion of harder samples that cannot be graded reliably by automation. Those samples are not miswritten as hidden answers of the same public test.

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源3](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）

## Evaluation

### Metrics

Binary-pass accuracy on the instance rubric; official-leaderboard Rank(UB) is additionally computed from statistically significant relations under the 95% CI.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 评分规则

An instance-level yes/no rubric scores only the final answer. The original repository defaults to attempts=1. When there are multiple attempts, the total score counts a pass if at least one attempt passes. That best-of-attempts score cannot be mixed with single-attempt accuracy.

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 运行与提示设置

The example in the original README uses temp=0, and the default is attempts=1; --attempts 3 counts a success if any one attempt passes. On 2026-02-03 the official online leaderboard switched to a Gemini 2.5 Pro judge and rewrote the evaluation questions for 54 items; this cannot be presented as a retest, under the same protocol, of the GPT-4o judge in the paper.

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源3](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### Official evaluation scripts

https://github.com/ekwinox117/multi-challenge

> The link is the one indicated by an original paper or dataset card that was opened; the code was not verified file by file.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 可比性警示

Bias in model selection, the judge model, the rubric version, the different denominators 273 and 266, and multiple attempts all affect comparison. Rank(UB) on the official site is computed from non-overlap of 95% intervals; the order of the original scores in Performance Comparison is not the statistical Rank(UB).

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）

## Current status

### Date checked

2026-11-08

> Access date of the source site for this visit; not the leaderboard run date.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
 "version": "Official-leaderboard convention for the judging and question revision of 2026-02-03"
 "trending": "B"
 "heat_evidence": "Opening the official Scale leaderboard on 2026-11-07 shows new frontier models and current results; this shows only that the single creating organization still maintains the display (B). It is not evidence that a new run took place on 7 November."
 "evidence_2026_h2": [
 {
 "url": "https://labs.scale.com/leaderboard/multichallenge?tab=large"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
 }
 ]
}
```

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
 "revisions": [
 {
 "version": "v1"
 "date": "2025-01-29"
 }
 {
 "version": "v2"
 "date": "2025-03-06"
 }
 ]
 "online_update": {
 "date": "2026-02-03"
 "judge": "Gemini 2.5 Pro"
 "rubric_questions_modified": 54
 }
 "dataset_count_conflict": "The paper/original repository lists 273; the current official HF lists 266, and the reason for the difference is not clearly explained in the official materials that were read"
}
```

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）

### 饱和性证据

The current leader of the official Performance Comparison leaderboard is 81.95% (95% CI ±4.16); instances that do not pass remain, but a general threshold of “saturated/not saturated” is not defined from this.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 污染与已知争议

Text near Tables 2 and 3 of paper v2 still gives historical means that disagree with the tables. Historical scores included here follow the values stated in the tables, and human evaluation and automatic evaluation are listed separately. The official HF set now has 266 rows, while the original JSONL has 273 rows, and the unexplained difference in the denominator is kept. Samples selected for failures shared by six models have selection bias; a public test set does not guarantee that training never encountered it.

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源3](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）；[来源4](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 衍生与条目关系

Large/Small are model groupings and do not create separate benchmarks; they complement IFEval's single-turn format constraints and are not the same test.

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

## Leaderboard snapshot

### 本次榜单采集日

2026-11-08

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### 官方榜源

https://labs.scale.com/leaderboard/multichallenge?tab=large

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 第三方覆盖

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Scale official site / Performance Comparison / Large

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | gpt 6.1 Sol | 81.95 (±4.16 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 2 | Gemini 4 Argon | 78.7 (±5.30 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 3 | Muse Spark | 75.52 (±4.05 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 4 | Muse Spark 1.1 | 75.3 (±0.60 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 5 | Deepseek V4p1 Flash 1017 | 74.9 (±5.30 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 6 | GPT 6.1 Terra | 74.2 (±5.40 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 6 | Muse Spark Open | 74.2 (±5.60 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 8 | gemini-3.1-pro-preview | 71.37 (±1.74 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 9 | gpt-5.4-pro-2026-03-05 | 69.23 (±3.05 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 10 | Claude Haiku 5.5 | 67.67 (±5.34 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 11 | gemini-3-pro-preview | 65.67 (±2.20 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 12 | gpt-5.1-2025-11-13-thinking | 63.41 (±2.11 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 13 | gpt-5-thinking | 63.19 (±1.63 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 14 | o3-pro-2025-06-10-reasoning-high | 62.4 (±2.49 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 15 | kimi-k2.5 | 61.39 (±0.46 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 16 | gemini-3.1-flash-lite-preview | 60.61 (±0.38 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 17 | gpt-5-mini-thinking | 58.99 (±4.07 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 18 | claude-opus-4-5-20251101-thinking | 58.97 (±0.42 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 19 | claude-4-opus-thinking | 58.62 (±0.77 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 20 | claude-opus-4-1-20250805-thinking | 57.2 (±0.95 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 21 | claude-4-sonnet-thinking | 57.11 (±0.81 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 22 | o3-2025-04-16-reasoning-high | 56.62 (±3.32 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 23 | claude-opus-4-6 (Non-Thinking) | 56.02 (±1.08 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 24 | kimi-k2-thinking | 55.42 (±1.88 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 25 | claude-sonnet-4-5-20250929-thinking | 55.32 (±1.47 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 26 | gemini-2-5-pro | 53.62 (±1.32 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 27 | claude-3-7-sonnet-thinking | 51.58 (±3.07 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 28 | gpt-5.1-2025-11-13-instant | 51.23 (±1.79 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 29 | claude-haiku-4-5-20251001-thinking | 50.49 (±2.04 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 30 | deepseek-v3p1 | 46.1 (±1.11 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 31 | gpt-oss-120b | 45.34 (±2.15 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 32 | o4-mini-2025-04-16-reasoning-high | 44.9 (±0.88 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 33 | qwen3-235b-a22b | 41.22 (±1.79 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 34 | gpt-4.1 | 39.43 (±0.94 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 35 | claude-opus-4-6-thinking-max | 37.15 (±2.16 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 36 | gemini-2-0-flash | 36.35 (±0.78 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |

- Score order in the page Performance Comparison, not Rank(UB)

- Current official display; exact run dates are not given item by item

#### Paper v2 Table 2 / human judge

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| — | GPT-4o (August 2024) | 12.52 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Llama 3.1 405B Instruct | 14.92 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Mistral Large | 14.63 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Claude 3.5 Sonnet (June 2024) | 41.42 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Gemini 1.5 Pro (August 27 2024) | 19.96 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | o1-preview | 37.23 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |

- Historical table values from the paper; they are not ranked together with the current leaderboard judged by Gemini 2.5 Pro.

#### Paper v2 Table 3 / GPT-4o instance-rubric automatic judge

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| — | GPT-4o (August 2024) | 12.9 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Llama 3.1 405B Instruct | 16.5 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Mistral Large | 13.32 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Claude 3.5 Sonnet (June 2024) | 42.75 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Gemini 1.5 Pro (August 27 2024) | 21.3 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | o1-preview | 35.73 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |

- Historical table values from the paper; they are not ranked together with the current leaderboard judged by Gemini 2.5 Pro.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### 覆盖范围与限制

All 36 readable scores in the current Large Performance Comparison, and their 95%CI, are included in full. The original score order is retained, and a statistical Rank(UB) is not fabricated. The 6 human-evaluation rows of paper Table 2 and the 6 automatic-judge rows of Table 3 are stored separately. Where the paper's text conflicts with a table, the table is used and the conflict is stated. The same denominator is not assumed among the original 273-question JSONL, the current 266-question HF set, and the revised online leaderboard.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）

## Contact

### 公开研究邮箱

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 项目反馈入口

https://github.com/ekwinox117/multi-challenge/issues

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）

### 官方公开社交入口

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 公开渠道/隐私边界

This dossier records only the project feedback channels published officially; a role, an email, or a calendar example inside a synthetic dialogue is not treated as real personal contact information.

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

## Original files

### 源站PDF

https://arxiv.org/pdf/2501.17399

> Verified by reading the raw PDF bytes directly; not uploaded.

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### PDF SHA-256

70b688b241c7f4e5ec0b6639f6eaf044ddc19dcf60ee7329d8078ec8a3aa285f

> Verified by reading the raw PDF bytes directly; not uploaded.

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### PDF bytes

2789352

> Verified by reading the raw PDF bytes directly; not uploaded.

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### Folder

Unverified

> 状态：待核实。

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-07）

### 其他官方文档

```json
[
 {
 "type": "Official web page/paper opened"
 "url": "https://labs.scale.com/leaderboard/multichallenge?tab=large"
 }
 {
 "type": "Official web page/paper opened"
 "url": "https://arxiv.org/abs/2501.17399"
 }
 {
 "type": "Official/research sources opened for verification"
 "url": "https://arxiv.org/pdf/2501.17399"
 "accessed": "2026-11-08"
 }
 {
 "type": "Official/research sources opened for verification"
 "url": "https://github.com/ekwinox117/multi-challenge/blob/main/README.md"
 "accessed": "2026-11-08"
 }
 {
 "type": "Official/research sources opened for verification"
 "url": "https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl"
 "accessed": "2026-11-08"
 }
 {
 "type": "Official/research sources opened for verification"
 "url": "https://huggingface.co/datasets/ScaleAI/MultiChallenge"
 "accessed": "2026-11-08"
 }
 {
 "type": "Official/research sources opened for verification"
 "url": "https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md"
 "accessed": "2026-11-08"
 }
]
```

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）；[来源3](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源5](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）；[来源6](https://huggingface.co/datasets/ScaleAI/MultiChallenge)（访问 2026-11-08）；[来源7](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

### 原始PDF

Unverified

> 状态：待核实。

> The page for this group was built only locally and was not uploaded; no archive link is fabricated.

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-07）

## Changelog

### Changelog

```json
[
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

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）
