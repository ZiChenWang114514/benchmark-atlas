# Mystery Game Puzzles

> Verification date: 2026-11-08. Unknowns are not filled in; the date on which the source was accessed is not the experiment run date.

Epoch AI provides 100 mid-game states from confidential game variants. Each question asks for the single optimal next move. It is not a full-game win rate, and it is not a guess of the game's name. The official source deliberately does not release prompts, example questions, or trajectories, in order to lower the risk of targeted preparation. 144 successful runs were read, in four task versions: 1.0.4, 1.1.0, 1.2.0, and 1.2.1. Historical highs from different versions cannot be combined into a leaderboard for one version.
[Reading basis for this page](https://epoch.ai/benchmarks/mystery-game-puzzles) (accessed 2026-11-08)

[Supplementary reading basis](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-08)

## Basic information

### Short name

Mystery Game Puzzles

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Full name

Mystery Game Puzzles

> The official name is kept; the paper title is not fabricated as a full name.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 数据/基准版本

1.2.1 (the latest run version in the current CSV)

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### Paper version

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Release date

2026-07 (official BibTeX month; exact day Unverified)

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Section

Reasoning

> Benchmark Constitution editorial classification.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Subfields

Reasoning

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 许可边界

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 论文入口

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 代码入口

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Dataset

Not disclosed: the official site explicitly does not currently release prompts, example positions, or model trajectories, in order to keep the game's identity confidential. The public CSV contains model scores, not the question bank.

> 状态：未公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Official homepage

https://epoch.ai/benchmarks/mystery-game-puzzles

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Paper title

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Origin and maintenance

### Initiators

Epoch AI

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Partner organizations

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Authors

Epoch AI (the official BibTeX gives an institutional author; a list of personal authors was not invented on that basis).

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Current maintainer

Epoch AI

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Funders

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Design goals

### Abilities measured

Given a position in a variant of a well-known game, select the single best next move.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 设计动机

Similar to Chess Puzzles, but the identity of the game is hidden in order to reduce the risk of targeted pretraining or of preparation for the evaluation; it is not a sufficiently evidenced task of “exploring the hidden rules of the game.”

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Construction

### Question sources

Games are sampled at random by a program, advanced to the middlegame, and filtered to states with a unique best next move.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 出题/构建者背景

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Review process

Programmatically filtered to a unique best move; whether there is also independent manual review, and the game-engine version and search depth, are Unverified.

> 状态：待核实。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Quality control

Filtered to positions that have a unique best move; the specific verifier and search depth are Unverified.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 去污染/泄漏控制

The identity of the game, the prompts, the example questions, and the trajectories are kept confidential, to reduce preparation aimed at the benchmark.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Data format

### 精确规模与统计口径

100 puzzle positions

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Question types

100 mid-game positions, choosing the single best next move; this is not a win rate over a full game, and it is not a task that asks the model to discover a confidential game name.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Modalities

文本；工具交互

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 语言/代码语种

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 难度结构

The program samples random games and advances them to the midgame, keeping only states with a unique optimal next move; the official source gives no public difficulty table, and cross-game difficulty is not inferred from model scores.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Public and hidden splits

Not disclosed: game identity, prompts, example positions, and model trajectories (explicitly stated on the official website).

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Evaluation

### Metrics

Proportion of correct best next steps

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 评分规则

A submission is normalized to game notation and compared with the answer; if a valid move cannot be extracted, the result is unanswered and scores nothing, and an illegal move is marked wrong.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 运行与提示设置

A minimal agent scaffold, with text position input and use of the submission tool.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Official evaluation scripts

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 可比性警示

The CSV contains 1.0.4, 1.1.0, and 1.2.1, so historical highs from different versions cannot be treated directly as a leaderboard for one version.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Current status

### Date checked

2026-11-08

> Access date of the source site for this visit; not the leaderboard run date.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
 "version": "1.2.1 (the latest run version in the current CSV)"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/benchmarks.csv"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "The most recent row in the Epoch CSV is Kimi K3.1 Pro, started at 2026-11-06 09:59:23; it is currently included in ECI. The main evidence still comes from Epoch itself."
 }
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "The most recent row in the Epoch CSV is Kimi K3.1 Pro, started at 2026-11-06 09:59:23; it is currently included in ECI. The main evidence still comes from Epoch itself."
 }
 ]
 "csv_versions": {
 "1.2.1": 6
 "1.2.0": 1
 "1.1.0": 5
 "1.0.4": 132
 }
 "observed_on": "2026-11-08"
}
```

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 论文/数据修订历史

The BibTeX on the official webpage lists July 2026. Task versions now present in the CSV are 1.0.4, 1.1.0, 1.2.0, and 1.2.1. The technical changes in each version, and an independent history of paper revisions, are Unverified. A model run date cannot be treated as the release date of the benchmark.

> 状态：待核实。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 饱和性证据

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 污染与已知争议

The official source does not release the identity of the game, the prompts, the example questions, or the trajectories, in order to reduce the risk of preparation aimed at this task, so what the public can recheck is limited. The name of the game cannot be guessed. The current CSV contains four task versions. The highest score of 0.84 on v1.0.4 cannot be mixed with the highest score of 0.74 on v1.2.1 into a ranking of one version.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 衍生与条目关系

The method is similar to Epoch Chess Puzzles, but the identity of the game is kept confidential. It is not the scientific-mechanism discovery of MysteryMechanism, and each task version is not counted as an independent benchmark.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mysterymechanism)（访问 2026-11-08）

## Leaderboard snapshot

### 本次榜单采集日

2026-11-08

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 官方榜源

https://epoch.ai/benchmarks/mystery-game-puzzles

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 第三方覆盖

Unverified

> 状态：待核实。

> epoch.ai/data/benchmarks.csv is a score source of the creator, Epoch, itself, and not an independent third party; this corrects the earlier misclassification.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Epoch official CSV / task version 1.2.1.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | GPT-6.1 Terra (max) | 0.74；stderr 0.04408440022768081 0–1 | mean_score | 2026-10-27 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 2 | Gemini 4 Argon (high) | 0.64；stderr 0.048241815132442176 0–1 | mean_score | 2026-10-14 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | Muse Wonder (max) | 0.51；stderr 0.05024183937956913 0–1 | mean_score | 2026-10-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 4 | DeepSeek V4.1 Flash 1017 (max) | 0.49；stderr 0.05024183937956914 0–1 | mean_score | 2026-10-20 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | Kimi K3.1 Pro (Together, max) | 0.42；stderr 0.04960449637488583 0–1 | mean_score | 2026-11-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 6 | Mistral Large 4 (high) | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-11-02 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- Scores are ranked within this same version, duplicate model runs are retained, and the highest values are not merged across versions.

- Evaluation by the creators themselves; distinct configurations and run IDs are kept separate

#### Epoch official CSV / task version 1.2.0.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Mistral Large 4 Preview (high) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-10-14 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- Scores are ranked within this same version, duplicate model runs are retained, and the highest values are not merged across versions.

- Evaluation by the creators themselves; distinct configurations and run IDs are kept separate

#### Epoch official CSV / task version 1.1.0.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | GPT-6.1 Sol (max) | 0.8；stderr 0.04020151261036849 0–1 | mean_score | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 2 | Claude Opus 5.5 (max) | 0.71；stderr 0.04560480215720687 0–1 | mean_score | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | Claude Sonnet 5.5 (max) | 0.65；stderr 0.04793724854411022 0–1 | mean_score | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 4 | DeepSeek V4.1 Flash (max) | 0.43；stderr 0.0497569851956243 0–1 | mean_score | 2026-10-09 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | Claude Haiku 5.5 (max) | 0.3；stderr 0.04605661864718382 0–1 | mean_score | 2026-10-08 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- Scores are ranked within this same version, duplicate model runs are retained, and the highest values are not merged across versions.

- Evaluation by the creators themselves; distinct configurations and run IDs are kept separate

#### Epoch official CSV / task version 1.0.4.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.84；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 2 | Claude Opus 5 (max) | 0.59；stderr 0.04943110704237103 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | Claude Fable 5.1 (max) | 0.58；stderr 0.04960449637488583 0–1 | mean_score | 2026-09-02 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | GPT-5.6 Sol (max) | 0.58；stderr 0.04960449637488583 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | GPT-6 Sol (max) | 0.56；stderr 0.049888765156985884 0–1 | mean_score | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | GPT-5.5 (xhigh) | 0.56；stderr 0.049888765156985884 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 7 | Claude Fable 5 (max) | 0.52；stderr 0.05021167315686782 0–1 | mean_score | 2026-08-01 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 7 | GPT-5.5 (high) | 0.52；stderr 0.05021167315686782 0–1 | mean_score | 2026-07-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 9 | Gemini 3.8 Flash (high) | 0.47；stderr 0.05016135580465918 0–1 | mean_score | 2026-09-03 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 10 | DeepSeek V4 Pro 0813 (max) | 0.43；stderr 0.0497569851956243 0–1 | mean_score | 2026-08-20 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 11 | Qwen3.8 Max (xhigh) | 0.38；stderr 0.048783173121456344 0–1 | mean_score | 2026-08-05 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 12 | Gemini 3.7 Flash (high) | 0.37；stderr 0.048523658709390974 0–1 | mean_score | 2026-08-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 12 | Claude Opus 5 | 0.37；stderr 0.048523658709390974 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 12 | GPT-5.4 (xhigh) | 0.37；stderr 0.048523658709390974 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 15 | Claude Opus 4.8 | 0.36；stderr 0.04824181513244218 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 16 | Claude Sonnet 5 (max) | 0.35；stderr 0.04793724854411023 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 16 | GPT-5.6 Terra (max) | 0.35；stderr 0.047937248544110224 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 18 | Grok 4.6 (xhigh) | 0.34；stderr 0.04760952285695234 0–1 | mean_score | 2026-08-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 18 | DeepSeek V4 Flash 0731 (max) | 0.34；stderr 0.04760952285695233 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 18 | Gemini 3.1 Pro Preview | 0.34；stderr 0.04760952285695234 0–1 | mean_score | 2026-07-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 21 | GLM-5.3 (max) | 0.33；stderr 0.04725815626252608 0–1 | mean_score | 2026-08-31 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 21 | GPT-5.6 Sol (none) | 0.33；stderr 0.04725815626252608 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 23 | Gemini 3.1 Pro Preview | 0.32；stderr 0.04688261722621506 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 23 | Qwen3.7 Max | 0.32；stderr 0.04688261722621506 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 23 | Gemini 3.5 Flash | 0.32；stderr 0.04688261722621506 0–1 | mean_score | 2026-07-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 26 | Claude Opus 4.8 | 0.31；stderr 0.04648231987117317 0–1 | mean_score | 2026-07-27 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 27 | Gemini 3.6 Flash | 0.3；stderr 0.04605661864718382 0–1 | mean_score | 2026-08-05 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 28 | Grok 4.7 (xhigh) | 0.29；stderr 0.045604802157206865 0–1 | mean_score | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 28 | o3 (high) | 0.29；stderr 0.04560480215720687 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 28 | Gemini 3.1 Pro Preview | 0.29；stderr 0.04560480215720687 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | GPT-5.5 (low) | 0.28；stderr 0.045126085985421296 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | GPT-5.4 (medium) | 0.28；stderr 0.04512608598542129 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | Gemini 3.5 Flash | 0.28；stderr 0.045126085985421296 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | Claude Opus 4.7 (max) | 0.28；stderr 0.04512608598542129 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | GPT-5.6 Sol (low) | 0.26；stderr 0.04408440022768081 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | qwen3.7-max_none | 0.26；stderr 0.0440844002276808 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | Gemini 3 Flash Preview | 0.26；stderr 0.0440844002276808 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | Kimi K3 (max) | 0.26；stderr 0.0440844002276808 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Muse Spark 1.3 (max) | 0.25；stderr 0.044640484731156636 0–1 | mean_score | 2026-09-19 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Gemini 3.6 Flash | 0.25；stderr 0.04351941398892446 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Gemini 3 Flash Preview | 0.25；stderr 0.04351941398892446 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Claude Opus 4.6 (max) | 0.25；stderr 0.04351941398892446 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | o3 (medium) | 0.23；stderr 0.04229525846816507 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | GPT-5.2 (high) | 0.23；stderr 0.04229525846816508 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | Gemini 3.6 Flash | 0.23；stderr 0.04229525846816508 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | GPT-5 (high) | 0.23；stderr 0.04229525846816508 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 47 | GPT-5.2 (medium) | 0.22；stderr 0.041633319989322654 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 47 | Qwen3.6 35B-A3B | 0.22；stderr 0.041633319989322654 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 47 | Claude Opus 4.5 (48k thinking) | 0.22；stderr 0.04163331998932266 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 50 | GPT-5.6 Luna (max) | 0.21；stderr 0.040936018074033236 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 50 | claude-opus-4-1-20250805_24K | 0.21；stderr 0.040936018074033236 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | GPT-5.6 Luna (none) | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-31 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | Qwen3.5 Flash | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | nemotron-3-ultra | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | Gemini 3 Flash Preview | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | Qwen 3.6 Max (Preview) | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | GPT-5.6 Terra (low) | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | GPT-5.1 (low) | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | GLM-5.2 | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | Gemini 3.5 Flash-Lite | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | Qwen3.5 397B-A17B | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | Qwen 3.6 Flash (2026-04-16) | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | GPT-5.5 (no thinking) | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | glm-5.2_minimal | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | GLM-5.2 | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | Kimi K2.6 | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-07-18 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Qwen3.7 Plus | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | GPT-5.4 (low) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | qwen3.5-122b-a10b_none | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Qwen3.5 Plus | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | GPT-5.6 Luna (low) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Qwen3.7 Plus | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | DeepSeek v4 Pro (unknown thinking) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Claude Sonnet 4.5 (48k thinking) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | GPT-5.4 (none) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-31 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | GPT-5.1 (medium) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | GPT-5 (low) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Qwen3.5 Flash | 0.16；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Claude Sonnet 4.6 (low) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Claude Sonnet 5 (no thinking) | 0.16；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Qwen3.5 Plus | 0.16；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | Qwen3.7 Flash | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | GPT-5 (medium) | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | GLM-5.2 | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | GPT-5.1 (no thinking) | 0.15；stderr 0.03588702812826368 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | Claude Opus 4.6 (no thinking) | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 87 | Muse Spark 1.3 (xhigh) | 0.1414141414141414；stderr 0.03519858850692775 0–1 | mean_score | 2026-09-17 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | Qwen3.7 Flash | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | GPT-5.2 (none) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | GPT-5.6 Terra (none) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | GPT-5 (minimal) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | Claude Sonnet 4.6 (no thinking) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 93 | Claude Opus 4.7 (no thinking) | 0.13；stderr 0.033799766898963114 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Kimi K3 (low) | 0.12；stderr 0.032659863237109045 0–1 | mean_score | 2026-08-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | kimi-k2.6_none | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | GPT-4 (Jun 2023) | 0.12；stderr 0.032659863237109045 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Qwen 3.6 Flash (2026-04-16) | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | GPT-5.6 Luna (medium) | 0.12；stderr 0.032659863237109045 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Qwen 3.6 Plus (2026-04-02) | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | gpt-4o-mini-2024-07-18 | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Gemini 3.5 Flash-Lite | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 102 | GPT-5.4 mini (none) | 0.11；stderr 0.03144660377352201 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 103 | GPT-5.6 Terra (medium) | 0.1；stderr 0.03015113445777636 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 103 | GPT-5.2 (low) | 0.1；stderr 0.03015113445777636 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 103 | GPT-5 mini (minimal) | 0.1；stderr 0.03015113445777636 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | GPT-5 nano (medium) | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | Qwen3-235B-A22B-Thinking-2507 | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | GPT-5 nano (low) | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | GPT-5.4 nano (no thinking) | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | GLM-5.3-Flash (max) | 0.08；stderr 0.027265992434429072 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | GPT-5.4 mini (low) | 0.08；stderr 0.027265992434429072 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | MiniMax-M3_none | 0.08；stderr 0.027265992434429075 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | GPT-5 nano (high) | 0.08；stderr 0.027265992434429075 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | GPT-6 Luna (max) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | MiniMax-M3 | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | o3-mini (high) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | Qwen3.6 27B | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | GPT-5.4 mini (medium) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | GPT-4.1 mini | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | Claude Opus 4.6 (low) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 121 | GPT-5.4 nano (medium) | 0.06；stderr 0.0238683256575942 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 121 | Inkling Small (xhigh) | 0.06；stderr 0.023868325657594204 0–1 | mean_score | 2026-08-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | o4-mini (high) | 0.05；stderr 0.02190429135575903 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | GPT-5 mini (high) | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | GPT-5.4 nano (high) | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | Qwen3-Max-Instruct | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | GPT-5 nano (minimal) | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 128 | GPT-5 mini (medium) | 0.04；stderr 0.019694638556693237 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 129 | GPT-5.4 nano (low) | 0.03；stderr 0.01714466079977653 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 129 | GPT-3.5 Turbo (Jan 2024) | 0.03；stderr 0.01714466079977653 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 131 | gpt-oss-120b_medium | 0.02；stderr 0.014070529413628966 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 132 | gpt-oss-120b_high | 0.0；stderr 0.0 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- Scores are ranked within this same version, duplicate model runs are retained, and the highest values are not merged across versions.

- Evaluation by the creators themselves; distinct configurations and run IDs are kept separate

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖范围与限制

All 144 successful runs in this CSV are included in full. They are separated into four tracks, 1.0.4, 1.1.0, 1.2.0, and 1.2.1, and the original stderr precision, the model configuration, and the run_id are retained. The latest, Kimi K3.1 Pro (Together, max), started at 2026-11-06 09:59:23. The CSV is Epoch's own evaluation and does not count as an independent third party. Scores from different versions are not assumed to be fully comparable.

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

## Contact

### 公开研究邮箱

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 项目反馈入口

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 官方公开社交入口

https://www.linkedin.com/company/epochai (official link in the footer of the official site)

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 公开渠道/隐私边界

https://epoch.ai/privacy (privacy-policy entry in the official-site footer)

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## Original files

### 源站PDF

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### PDF SHA-256

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### PDF bytes

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### Folder

Unverified

> 状态：待核实。

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 其他官方文档

```json
[
 {
 "type": "Official methods web page (not a standalone paper PDF)"
 "url": "https://epoch.ai/benchmarks/mystery-game-puzzles"
 "accessed": "2026-11-08"
 }
 {
 "type": "Official original run-score CSV (not the question bank)"
 "url": "https://epoch.ai/data/benchmarks.csv"
 "accessed": "2026-11-08"
 }
 {
 "type": "Official/research sources opened for verification"
 "url": "https://www.vals.ai/benchmarks/mysterymechanism"
 "accessed": "2026-11-08"
 }
]
```

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源3](https://www.vals.ai/benchmarks/mysterymechanism)（访问 2026-11-08）

### 原始PDF

Unverified

> 状态：待核实。

> Not uploaded within the scope of this batch; this is not an official Not disclosed.

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

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

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）
