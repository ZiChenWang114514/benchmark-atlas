# ARC-AGI-3

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

An evaluation of interactive games with no written rules, measuring efficiency of action relative to humans rather than an ordinary win rate. The real AI Verified leaderboard is at /leaderboard. The highest scores of Standard and of Provider Adapter differ and must be kept on separate tracks.

## Basic information

### Short name

ARC-AGI-3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Full name

ARC-AGI-3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Benchmark version

3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Paper version

Technical report, 2026-04-22

> The date on the title page of the report; it is not presented as the first-release date of the benchmark.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Release date

2026-03-25 (the calendar day announced for the official release, with no exact time given; the technical report is dated April 22)

[来源1](https://arcprize.org/blog/arc-agi-3-launch)（访问 2026-11-07）

### Section

Reasoning

> Benchmark Constitution editorial filing. It is not an official classification.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Field tags

- 交互式推理
- Exploration and world model
- 行动效率

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### License

The ARC-AGI Toolkit software is MIT; this is not a basis for inferring that all game content or the private test environment is also MIT, and the license for the latter is Unverified.

> 字段状态：待核实

[来源1](https://github.com/arcprize/arc-agi/blob/main/LICENSE)（访问 2026-11-07）

### Paper

https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Code

https://github.com/arcprize/arc-agi

[来源1](https://docs.arcprize.org/)（访问 2026-11-07）

### 数据地址

https://arcprize.org/tasks?v=3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Official entry

https://arcprize.org/arc-agi/3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Paper title

ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

## Origin and maintenance

### Initiators

ARC Prize

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 合作方

Unverified

> 字段状态：待核实

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Authors

ARC Prize Foundation. Environment design by Hunter Henry, engineering by David Wexler and Derek Smith, and benchmark design by François Chollet. The full list of developers is on the first page of the report.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Maintainer

ARC Prize Foundation

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://docs.arcprize.org/)（访问 2026-11-07）

### Funders

Unverified

> 字段状态：待核实

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## Design goals

### Abilities measured

Explore a new interactive environment, acquire goals, form a world model, and adapt across steps.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Design background

Static puzzles are not enough to show learning from experience and efficiency of action; interactive evaluation attends to the learning process rather than the final answer.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## Construction

### Question sources

Entirely new interactive game environments.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 出题者背景

A game-design studio inside the foundation designs new environments by hand; these are not levels taken from existing video games, and they are not natural-language exam questions.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Review process

Design → engineering implementation → structural and platform reliability testing → human calibration; each environment is given a first-exposure test by 10 ordinary participants, and only environments that humans can complete are included.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Quality control

Qualification checks the environment interface and whether a run is reliable, and it studies the probability that a random policy clears a level by exploring the graph of reachable states; human calibration establishes an upper-median best action baseline. The reported acceptance threshold is that a random policy clears a single level no more often than 1/10000, but the graph of the first level in the example ls20 also gives 1/355. The exception must be kept, and it is not claimed that every level is guaranteed to agree.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Decontamination

The public demo deliberately does not cover the private mechanisms in full; the semi-private set is for testing API models, and the fully private set is for the competition, with the aim of OOD mechanisms rather than fine-tuning on public questions. The official design aim is not the same as having proved that model training has zero contamination.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

## Data format

### 题量与规模

Report Table1: 25 public demo environments, 55 semi-private, and 55 fully private; environments contain multi-level games, and the number of environments cannot be treated as a count of single-level questions.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Question types

Multi-step game exploration without natural-language task instructions.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Modalities

- 视觉网格
- 离散动作
- 反馈

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Languages

The core game has no natural-language rules, instructions, or statement of the goal; observation is a 64×64 grid in 16 colors, and interaction is by discrete actions. Tool API code is an interface, not an English-comprehension question.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://github.com/arcprize/arc-agi)（访问 2026-11-07）

### Difficulty

Efficiency of long-horizon planning and skill acquisition under sparse feedback.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Public and hidden splits

25 public demos are easier and lean toward being playable; 55 semi-private items are used to evaluate frontier API models; 55 fully private items are used for the competition. The public set is not a training set with the same distribution as the test set.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

## Evaluation

### Metrics

RHAE (Relative Human Action Efficiency): efficiency of learning and of completion relative to the human baseline count of actions, rather than a simple win rate in the game.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 评分

Per-level efficiency is min(1.15,(human_actions/agent_actions)^2), and an unfinished level is 0; levels are weighted linearly by level index, the environment score is capped by the weight proportion of completed levels, and the result is then averaged over all environments. Each level may reach 115%, and the final overall score is 0–100%.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 运行设置

The Standard harness carries notes chosen by the model. The Provider Adapter keeps reasoning state and compresses long dialogues. The two implementations are listed on separate leaderboards. Games are encountered for the first time, with no natural-language task instructions. The budget must be kept together with the specific official result.

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 官方脚本

https://github.com/arcprize/arc-agi

> The Toolkit, the scorecard interface, and the game version are public; SDK0.9.9 in the README is not a new version number for benchmark v3.

[来源1](https://github.com/arcprize/arc-agi)（访问 2026-11-07）；[来源2](https://docs.arcprize.org/)（访问 2026-11-07）

### 可比性警示

Standard and Provider Adapter are on separate tracks, and 99.9% on Adapter cannot replace 62.7% on Standard. /arc-agi/3/leaderboard is the entry to the human leaderboard, and the verified AI leaderboard is actually at /leaderboard; a banner that the contest has ended is not the absence of the AI leaderboard.

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 最新版本与采用证据

```json
{
 "version": "3"
 "heat_confidence": "A"
 "why_trending": "Candidate heat tier A; the evidence reopened below is labeled, item by item, with the evaluating party and the nature of the evidence, and the number of web pages is not treated as the number of independently adopting organizations."
 "evidence_2026_h2": [
 {
 "url": "https://openai.com/index/gpt-6-astra/"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "OpenAI"
 "note": "The current release page actually reports this benchmark score; vendor self-reported."
 }
 {
 "url": "https://arcprize.org/arc-agi/3"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Official maintainer"
 "note": "The current official methods and leaderboard have been opened; the observation date is not presented as the publication date."
 }
 ]
}
```

[来源1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）；[来源2](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 修订历史

The cover of the official PDF is dated 2026-04-22; it is not an arXiv paper, no independently verifiable history of revisions was seen, and that point is Unverified.

> 字段状态：待核实

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Saturation

On the current official table, Standard peaks at 62.7% and Provider Adapter peaks at 99.9%. Conclusions from different harnesses are entirely different. Adapter approaching 100% alone cannot be used to claim that general intelligence has been solved.

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）；[来源2](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Contamination and disputes

The public demo and the private test are deliberately OOD; previews of the leaderboard and tests that are not finished have a separate policy. The reported acceptance threshold for a random clear differs from the example of the first level of ls20, and it is described as evidence of design and of calibration rather than a mathematical guarantee for every level.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 版本与衍生关系

ARC-AGI-3 adds interactive exploration beyond the static visual reasoning of ARC-AGI-1 and ARC-AGI-2. The tasks, scores, and harnesses of the three versions are presented independently. Toolkit0.9.9 is a version of the runtime library, not a new benchmark entry.

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://github.com/arcprize/arc-agi)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### Official leaderboard

https://arcprize.org/leaderboard

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 第三方覆盖

Unverified

> 字段状态：待核实

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 分轨结果

#### Official Verified / Standard

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | GPT-6 Astra | 62.7 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 2 | GPT-6.1 Sol | 52.7 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 3 | Gemini 4 Argon | 49.8 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |

> GPT-6 Astra：{"source_date_column": "2026-09-02", "date_column_note": "The Date/Release date column on the web page is not automatically interpreted as the actual run date."}

> GPT-6.1 Sol：{"source_date_column": "2026-09-29", "date_column_note": "The Date/Release date column on the web page is not automatically interpreted as the actual run date."}

> Gemini 4 Argon：{"source_date_column": "2026-10-13", "date_column_note": "The Date/Release date column on the web page is not automatically interpreted as the actual run date."}

#### Official Verified / Provider Adapter

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | GPT-6 Astra | 99.9 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 2 | Gemini 4 Argon | 97.5 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 3 | GPT-6.1 Sol | 96.4 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |

> GPT-6 Astra：{"source_date_column": "2026-09-02", "date_column_note": "The Date/Release date column on the web page is not automatically interpreted as the actual run date."}

> Gemini 4 Argon：{"source_date_column": "2026-10-13", "date_column_note": "The Date/Release date column on the web page is not automatically interpreted as the actual run date."}

> GPT-6.1 Sol：{"source_date_column": "2026-09-29", "date_column_note": "The Date/Release date column on the web page is not automatically interpreted as the actual run date."}

> The ordering is read separately from the two v3 columns of the official complete table; v1/v2 columns and community Kaggle scores are not mixed in.

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

### Coverage note

A genuine AI Verified leaderboard was obtained for the first time. The old entry captured only the contest banner of the human leaderboard and therefore stated, wrongly, that verification was impossible; the top three for Standard and the top three for Provider Adapter are now supplied, and the date on which the data were collected is not the run date.

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

## Contact

### 公开科研联系邮箱

Unverified

> 字段状态：待核实

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 公开反馈

https://github.com/arcprize/arc-agi/issues

[来源1](https://github.com/arcprize/arc-agi)（访问 2026-11-07）

### 官方社交

https://discord.gg/9b77dPAmcA

[来源1](https://docs.arcprize.org/)（访问 2026-11-07）

### 隐私说明/政策

https://arcprize.org/privacy

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## Original files

### 源站论文PDF

https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### PDF SHA-256

33a19ce7973afb5c15a91566a340e3745f8c9fd6f041f601c0f544cbe982799f

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### PDF bytes

1184316

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### Folder

Unverified

> 字段状态：待核实

> The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 其他官方材料

```json
[
 {
 "type": "Formally released article"
 "url": "https://arcprize.org/blog/arc-agi-3-launch"
 "accessed": "2026-11-07"
 }
 {
 "type": "Toolkit documentation"
 "url": "https://docs.arcprize.org/"
 "accessed": "2026-11-07"
 }
 {
 "type": "AI Verified leaderboard"
 "url": "https://arcprize.org/leaderboard"
 "accessed": "2026-11-07"
 }
]
```

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 论文副本

Unverified

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

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
]
```

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）
