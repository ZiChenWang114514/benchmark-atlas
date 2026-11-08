# SpireClimb

> Benchmark Constitution, in-depth review 2026-11-08.

SpireClimb has the model finish full games of two Slay the Spire titles at the highest difficulty, using screenshots and the mouse and keyboard, and it measures long-horizon decisions and the reliability of computer operation. The two games' win rates are weighted equally, and they cannot be pooled directly across 135 games. The 2026-11-05 fix to the opening Neow reward changed the test setting of the first-generation game. The frozen StS2 version is v0.107.1. The footnote 1 later on the web page is not a version suffix.

[Source 1](https://epoch.ai/benchmarks/spireclimb) (accessed 2026-11-08); [Source 2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-08)

## Basic information

### Short name

SpireClimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Full name

SpireClimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Benchmark version

StS2 is frozen at v0.107.1; dual tracks of StS1 A20 Heart and StS2 A10

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### Paper version

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Release date

2026-10-14 (date metadata on the official first-release analysis page: 2026-10-14; not the evaluation run date)

[来源1](https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel)（访问 2026-11-08）

### Section

Agent

> Benchmark Constitution editorial classification.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 领域

```json
[
 "游戏"
]
```

> Editorial tags; an empty list means finer-grained tags have not yet been added.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 许可与适用范围

The license of the evaluation code is Unverified; the game content is under copyright. Epoch states that use is only for research and commentary, and that the game itself is not distributed.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Paper

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Code

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 数据

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Official entry

https://epoch.ai/benchmarks/spireclimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Paper title

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Epoch AI

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 合作/参与机构

The evaluation is conducted by Epoch independently of Mega Crit Games, and the official statement is explicit that copyrighted content of the game is not distributed or sold; Mega Crit cannot, on that basis, be listed as a party to joint development.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### Authors

```json
[
 "Benjamin Ou"
 "Simon Chen"
]
```

> Byline of the official first-release analysis; it does not impersonate an as-yet unconfirmed independent academic-paper author list.

[来源1](https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel)（访问 2026-11-08）

### Maintainer

Epoch AI

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Funders

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## Design goals

### Abilities measured

Computer use, long-horizon reasoning, tactical decision-making, and reliability across a complete game.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Design background

Uses the end-to-end win rate on real games at the highest difficulty, rather than local actions in short rounds or isolated reasoning questions.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## Construction

### Question sources

Slay the Spire 1 and 2, each at the highest difficulty, with all content unlocked; each character uses a fixed set of 15 random seeds shared by all models.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 出题者背景

The authors of the first-release analysis are Benjamin Ou and Simon Chen. The author biography in the article describes Ou as an Epoch benchmarking researcher, with an undergraduate background in physics and computer science at UC Berkeley.

[来源1](https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel)（访问 2026-11-08）

### Review process

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Quality control

The StS2 game version is fixed; samples found to involve save scumming were excluded, and the run was repeated.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 污染控制

The official source acknowledges that popular games may become training targets; a frozen version improves interpretability but does not claim an absence of contamination.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## Data format

### 题量

StS1: 4 characters × 15 = 60 games; StS2: 5 characters × 15 = 75 games.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 任务形式

A complete game is played through screenshots and mouse and keyboard input.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Modalities

```json
[
 "截图"
 "Mouse and keyboard action"
 "Written note"
 "Restricted wiki search"
]
```

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Languages

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Difficulty

StS1 Ascension 20 Heart Kill；StS2 Ascension 10。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Public and hidden splits

15 fixed seeds, chosen arbitrarily, for each role, and every model uses the same seeds; the run configuration unlocks all of the content. The official site does not give a complete list of the seeds, or a description of an independent hidden set, and the related details are Unverified.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## Evaluation

### Metrics

The win rate of each of the two games, then an equal-weight average of the two games (not a win rate that directly pools 135 games).

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 评分

StS1 requires killing the Heart, and StS2 requires passing 3 acts; proportion of successful runs; the two tracks must keep the same version.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 运行设置

An Inspect ReAct computer-use harness; the model uses the maximum reasoning level, with a compression threshold of 300,000 tokens and with notes retained; only the Slay the Spire wiki may be retrieved; StS1 screenshots are 1280×720 and StS2 screenshots are 1280×800.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 评测工具

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Comparability

Rescored on 2026-11-05 after the missing Neow reward at the start of StS1 was fixed; the old version cannot be used directly as the current leaderboard under the same protocol, and it is not mixed in comparison with later public update versions of StS2.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
 "version": "StS2 v0.107.1"
 "method_update": "2026-11-05 Neow reward fix"
 "note": "The superscript 1 after v0.107.1 on the web page is a footnote, not a 4th-segment game version number."
}
```

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 修订历史

The method fix of 2026-11-05 for the Neow reward: GPT-6 Astra StS1 16.7%→33.3%, GPT-6.1 Sol 20%→18.3%, which is not a combined score of the two games.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 饱和与能力边界

The official view is that popular games may have been trained on in a targeted way and may saturate quickly, but the overall maximum in this CSV is 0.33999999999999997, which is not a perfect score; a high win rate at the lowest difficulty cannot be written as a result at the highest difficulty.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 风险与争议

The risks are training aimed at popular games and, once the version is frozen, drifting from players' latest strategies; save scumming is excluded by behavior checks rather than by a mechanical ban.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 系列与衍生关系

Slay the Spire 1 and 2 are two constituent tracks of the same benchmark; the overall score at the highest difficulty is the equal-weight average of the two games’ win rates, and they are not split into two newly added benchmarks.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://epoch.ai/benchmarks/spireclimb) (accessed 2026-11-08); [Source 2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-08)

### Official entry

https://epoch.ai/benchmarks/spireclimb

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 独立来源

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 分来源与协议结果

#### SpireClimb / the CSV does not mark a composite task version.

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.33999999999999997 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-cd6cd8bb290a7ae3+steambench-sts2-a10-cdf1c9fa85cb6300","run_started_at":"2026-11-05","stderr":"0.04131325151634216"} |
| 2 | GPT-6.1 Sol (max) | 0.23833333333333334 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-e795fd781f73bd66+steambench-sts2-a10-9a23c8dea53b6755","run_started_at":"2026-11-05","stderr":"0.03653377199465138"} |
| 3 | GPT-6.1 Terra (max) | 0.22333333333333333 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-263bd0e64b156075+steambench-sts2-a10-1102b0b9cf1785f6","run_started_at":"2026-11-05","stderr":"0.03386031744341088"} |
| 4 | GPT-6 Sol (max) | 0.09166666666666667 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-831fe00153e0f0b1+steambench-sts2-a10-edacf7bb0ae31edf","run_started_at":"2026-11-06","stderr":"0.024324094573715753"} |
| 5 | Claude Opus 5.5 (max) | 0.058333333333333334 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-789f946c67a789f5+steambench-sts2-a10-ef454c368767b2a0","run_started_at":"2026-11-05","stderr":"0.020285004230980282"} |
| 6 | Claude Fable 5.1 (max) | 0.02 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-2057a494867d184c+steambench-sts2-a10-413d1cc930f6d4c6","run_started_at":"2026-11-06","stderr":"0.011389895949029987"} |
| 7 | Claude Sonnet 5.5 (max) | 0.013333333333333334 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-e8f930bf4d4f1a14+steambench-sts2-a10-5db0e95e99f6b21c","run_started_at":"2026-11-06","stderr":"0.009364170421755878"} |
| 8 | GPT-6 Luna (max) | 0.0 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-f7325d71b8b16f57+steambench-sts2-a10-0e148062f8e47c4a","run_started_at":"2026-11-06","stderr":"0.0"} |

#### SpireClimb (Slay the Spire 1, Ascension 20 Heart) / 0.3.3_cd56aef

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.3333333333333333 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-cd6cd8bb290a7ae3","run_started_at":"2026-11-05","stderr":"0.06137164119322156","task_version":"0.3.3_cd56aef"} |
| 2 | GPT-6.1 Sol (max) | 0.18333333333333332 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-e795fd781f73bd66","run_started_at":"2026-11-05","stderr":"0.05037523978531015","task_version":"0.3.3_cd56aef"} |
| 3 | GPT-6.1 Terra (max) | 0.1 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-263bd0e64b156075","run_started_at":"2026-11-05","stderr":"0.039056673294247155","task_version":"0.3.3_cd56aef"} |
| 4 | GPT-6 Sol (max) | 0.05 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-831fe00153e0f0b1","run_started_at":"2026-11-06","stderr":"0.028374015326751195","task_version":"0.3.3_cd56aef"} |
| 4 | Claude Opus 5.5 (max) | 0.05 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-789f946c67a789f5","run_started_at":"2026-11-05","stderr":"0.028374015326751195","task_version":"0.3.3_cd56aef"} |
| 6 | Claude Fable 5.1 (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-2057a494867d184c","run_started_at":"2026-11-06","stderr":"0.0","task_version":"0.3.3_cd56aef"} |
| 6 | Claude Sonnet 5.5 (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-e8f930bf4d4f1a14","run_started_at":"2026-11-06","stderr":"0.0","task_version":"0.3.3_cd56aef"} |
| 6 | GPT-6 Luna (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-f7325d71b8b16f57","run_started_at":"2026-11-06","stderr":"0.0","task_version":"0.3.3_cd56aef"} |

#### SpireClimb (Slay the Spire 2, Ascension 10) / 0.3.3_447ebe2

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6.1 Terra (max) | 0.3466666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-1102b0b9cf1785f6","run_started_at":"2026-11-04","stderr":"0.055323237980623115","task_version":"0.3.3_447ebe2"} |

#### SpireClimb (Slay the Spire 2, Ascension 10) / 0.3.3_e52e280

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.3466666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-cdf1c9fa85cb6300","run_started_at":"2026-09-23","stderr":"0.055323237980623115","task_version":"0.3.3_e52e280"} |
| 2 | GPT-6.1 Sol (max) | 0.29333333333333333 | win rate (0–1) | {"run_id":"steambench-sts2-a10-9a23c8dea53b6755","run_started_at":"2026-09-30","stderr":"0.052926375288708374","task_version":"0.3.3_e52e280"} |
| 3 | GPT-6 Sol (max) | 0.13333333333333333 | win rate (0–1) | {"run_id":"steambench-sts2-a10-edacf7bb0ae31edf","run_started_at":"2026-09-23","stderr":"0.03951659855758794","task_version":"0.3.3_e52e280"} |
| 4 | Claude Opus 5.5 (max) | 0.06666666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-ef454c368767b2a0","run_started_at":"2026-09-23","stderr":"0.028997255746722662","task_version":"0.3.3_e52e280"} |
| 5 | Claude Fable 5.1 (max) | 0.04 | win rate (0–1) | {"run_id":"steambench-sts2-a10-413d1cc930f6d4c6","run_started_at":"2026-09-25","stderr":"0.022779791898059974","task_version":"0.3.3_e52e280"} |
| 6 | Claude Sonnet 5.5 (max) | 0.02666666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-5db0e95e99f6b21c","run_started_at":"2026-09-30","stderr":"0.018728340843511757","task_version":"0.3.3_e52e280"} |
| 7 | GPT-6 Luna (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts2-a10-0e148062f8e47c4a","run_started_at":"2026-09-29","stderr":"0.0","task_version":"0.3.3_e52e280"} |

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖与时效

All 24 current SpireClimb rows in the CSV were extracted in full. The latest successful run is taken by task + task_version + the exact model configuration. The overall 8 rows and the 16 rows for the two games are on separate tracks, and the two StS2 task versions are also separated. The overall mean_score is taken directly from the source value and is not resynthesized by approximation. The CSV has no full-leaderboard update time. started_at is used only as the run start time.

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源2](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## Contact

### 公开工作邮箱

```json
[
 "benchmarks@epoch.ai"
]
```

[来源1](https://epoch.ai/benchmarks)（访问 2026-11-07）

### 官方反馈

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 公开社区

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 隐私边界

Only the publicly stated Epoch contact channel for benchmark work is recorded; personal information of game players or third parties is not collected.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## Original files

### 源站PDF

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### PDF SHA-256

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### PDF bytes

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Folder

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "Official methods and introduction page (not the paper PDF)"
 "url": "https://epoch.ai/benchmarks/spireclimb"
 }
 {
 "type": "Opened primary material"
 "url": "https://epoch.ai/data/benchmarks.csv"
 "accessed": "2026-11-08"
 }
]
```

[Source 1](https://epoch.ai/benchmarks/spireclimb) (accessed 2026-11-08); [Source 2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## Changelog

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

[Source 1](https://epoch.ai/benchmarks/spireclimb) (accessed 2026-11-08); [Source 2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-08)
