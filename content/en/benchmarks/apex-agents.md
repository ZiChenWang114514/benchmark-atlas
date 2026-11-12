# APEX-Agents

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

11-section research snapshot

An evaluation of agents for professional services that cross applications. The 480 questions published with the paper and on HF, the 452 questions at AA, and the 240 questions current at Mercor are three different scopes. The static Score of 84.2 on the official site was checked against data embedded in the page and is Pass@1. Mean Score is 90.4. The two are kept on separate tracks.

## Basic information

### Short name

APEX-Agents

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Full name

AI Productivity Index for Agents (APEX–Agents)

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Benchmark version

Unverified

> 字段状态：待核实

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Paper version

arXiv v3（2026-02-24 01:49:38）

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Release date

2026-01-21 02:53:44 (arXiv first draft; the source UTC date is January 20)

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Section

Agent

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Field tags

- 职业服务
- Cross-application workflow
- 金融
- 公司法
- 管理咨询

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### License

The dataset card is labeled CC-BY 4.0 and separately states that use is limited to evaluation, that training and parameter fitting are forbidden, and that programmatic scraping is forbidden; the additional restrictions must be checked, and it cannot be written as unconditionally open.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2601.14242

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Code

https://github.com/Mercor-Intelligence/archipelago

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/mercor/apex-agents

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Official entry

https://www.mercor.com/apex/apex-agents-leaderboard/

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Paper title

APEX–Agents

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Mercor

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### 合作方

The current official site of Mercor states explicitly that development is joint with Box and Harvey; a list of the experts' employers is not automatically the same as a partner institution.

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

### Authors

Bertie Vidgen, Austin Mann, Abby Fennelly, John Wright Stanly, and others; the full list is in the paper.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Maintainer

Mercor

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Funders

Unverified

> 字段状态：待核实

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

## Design goals

### Abilities measured

Long-horizon, cross-application professional-service tasks in investment banking, management consulting, and corporate law.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Design background

Uses a file-rich world of work to reduce the gap between narrow, artificial agent tasks and real professional work.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

## Construction

### Question sources

Experts spend 5–10 days building the project world, the materials, and the professional deliverables, then create tasks, binary rubrics, and gold outputs from that world.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### 出题者背景

256 professionals, with an average of 12.9 years of experience; the fields are investment banking, consulting, and corporate law.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Review process

Tasks and rubrics are reviewed over multiple rounds; experts check that gold outputs are consistent with the prompts.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Quality control

96 tasks were completed independently by people who did not take part in creation or review; problems that were found were corrected and extended to the remaining data.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Decontamination

Data are for evaluation only; web search is disabled, and the world supplies the files needed to complete the task.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

## Data format

### 题量与规模

Original paper v3 and the public HF card: 480 tasks and 33 worlds, with 160 for each of three occupations. The current Mercor site: 240 tasks and 31 worlds. The independent AA implementation: 452 tasks. The three scopes are listed side by side, and differences among the web pages are not smoothed away.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）；[来源3](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）；[来源4](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问 2026-11-07）

### Question types

One task instruction and multi-step execution across applications; 422 tasks return text, and 58 tasks create or modify files.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Modalities

- 文本
- 电子表格
- 文档
- PDF
- 演示文稿
- Email/chat/calendar environments

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Languages

English (official HF card Languages: English).

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Difficulty

Experts estimate a mean of 1.82 hours per task; this is not the time a model actually runs.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Public and hidden splits

The HF card describes 480 public questions, with all gold labels and assets. The current Mercor site instead says that the full question set is private and that only a subset is open for reproduction. The sources differ by time or version, and the exact mapping is Unverified. The 9GB of material is not downloaded in order to guess.

> 字段状态：待核实

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

## Evaluation

### Metrics

Both the original paper and the current official site distinguish Pass@1, the proportion of tasks that pass every rubric item, and Mean Score, the average across tasks of the proportion of criteria passed; the original paper also has Pass@8 and Pass^8. The FAQ on the official site says that Mean Score is the primary metric, but the static HTML displays Pass@1 by default, and the embedded data can be checked.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

### 评分

Gemini 3 Flash low judges Met/Not met independently, item by item. It reads the prompt, the output, the file changes, and the criterion, and it does not read the full trajectory.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### 运行设置

The original paper uses 8 trajectories and 250 steps per question; AA uses 452 tasks, 3 runs per question, and Stirrup for 200 turns, excluding investment-banking worlds 244 and 246.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### 官方脚本

Archipelago provides the execution environment, the agent runner, and the grading system.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### 可比性警示

The 480 questions of the original paper, the AA452 questions, and the 240 questions currently on Mercor are three tracks that cannot be compared directly. The default Score=84.2 in the static HTML of the official site corresponds to pass-1, and mean-score=90.4, which the embedded data keys have disambiguated; the FAQ still says that Mean Score is the primary sort. n_samples is not treated as an independent question count.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问 2026-11-07）；[来源3](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### 最新版本与采用证据

```json
{
 "version": "待核实"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://artificialanalysis.ai/evaluations/apex-agents-aa"
 "date": "2026-11-07"
 "note": "The current independent AA implementation and leaderboard for 452 questions, as of the observation date."
 }
 ]
}
```

> A: the original benchmark and independent evaluation materials are cross-checked; citation alone is not equated with an independent actual run.

[来源1](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-01-21"
 }
 {
 "version": "v2"
 "submitted_at": "2026-01-28"
 }
 {
 "version": "v3"
 "submitted_at": "2026-02-24"
 }
]
```

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Saturation

On Mercor's current Loop harness, Pass@1 peaks at 84.2% and Mean Score peaks at 90.4%. The highest Pass@1 of 24.0 on the 480 questions of the original paper is not a direct curve of progress against the current 240 questions. Saturation cannot be claimed from pools of tasks that differ.

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

### Contamination and disputes

The current official website and the HF card differ in the number of questions, in worlds, in the private or open policy, and in the main metric; the data card marks both CC-BY-4.0 and a prohibition on training, on fitting of parameters, and on automatic scraping, those additional terms must be checked, and the card must not be reduced to openness without conditions.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

### 版本与衍生关系

APEX is a family of benchmarks from the same organization. The current official site lists APEX-Agents, APEX-SWE, APEX-Accounting, and APEX-1 side by side. The three occupational components of Agents are not, for that reason, counted again as independent benchmarks.

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### Official leaderboard

https://www.mercor.com/apex/apex-agents-leaderboard/

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）

### 第三方覆盖

https://artificialanalysis.ai/evaluations/apex-agents-aa

[来源1](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问 2026-11-07）

### 分轨结果

#### Mercor current 240 questions/31 worlds, pass-1

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (high) | 84.2 | Pass@1 (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=pass-1)，2026-11-07 |
| 2 | Gemini 4 Argon (high) | 82.4 | Pass@1 (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=pass-1)，2026-11-07 |
| 3 | Hy4 (high) | 77.6 | Pass@1 (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=pass-1)，2026-11-07 |

> Gemini 4 Carbon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 4.3, "n_samples_source": 960, "sample_count_note": "The original field on the page is n_samples; it does not equal the number of independent tasks, and the number of repetitions is not inferred."}

> Gemini 4 Argon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 4.3, "n_samples_source": 954, "sample_count_note": "The original field on the page is n_samples; it does not equal the number of independent tasks, and the number of repetitions is not inferred."}

> Hy4 (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 4.5, "n_samples_source": 960, "sample_count_note": "The original field on the page is n_samples; it does not equal the number of independent tasks, and the number of repetitions is not inferred."}

#### Mercor currently has 240 questions/31worlds, mean-score.

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (high) | 90.4 | Mean Score (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=mean-score)，2026-11-07 |
| 2 | Gemini 4 Argon (high) | 87.4 | Mean Score (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=mean-score)，2026-11-07 |
| 3 | Hy4 (high) | 85.1 | Mean Score (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=mean-score)，2026-11-07 |

> Gemini 4 Carbon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 3.1, "n_samples_source": 960, "sample_count_note": "The original field on the page is n_samples; it does not equal the number of independent tasks, and the number of repetitions is not inferred."}

> Gemini 4 Argon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 3.3, "n_samples_source": 954, "sample_count_note": "The original field on the page is n_samples; it does not equal the number of independent tasks, and the number of repetitions is not inferred."}

> Hy4 (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 3.6, "n_samples_source": 960, "sample_count_note": "The original field on the page is n_samples; it does not equal the number of independent tasks, and the number of repetitions is not inferred."}

#### Artificial Analysis independent set of 452 questions

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 3.5 Flash (High) | 47.1 | pass@1 (%) | [原表](https://artificialanalysis.ai/evaluations/apex-agents-aa)，2026-11-07 |
| 2 | Qwen3.8 Max (0902) | 42.4 | pass@1 (%) | [原表](https://artificialanalysis.ai/evaluations/apex-agents-aa)，2026-11-07 |
| 3 | Kimi K3 (Max) | 41.3 | pass@1 (%) | [原表](https://artificialanalysis.ai/evaluations/apex-agents-aa)，2026-11-07 |

#### Paper v3/480-question historical baseline

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 3 Flash (Thinking=High) | 24.0 | Pass@1 (%) | [原表](https://arxiv.org/abs/2601.14242)，2026-11-07 |
| 2 | GPT-5.2 (Thinking=High) | 23.0 | Pass@1 (%) | [原表](https://arxiv.org/abs/2601.14242)，2026-11-07 |
| 3 | Claude Opus 4.5 (Thinking=High) | 18.4 | Pass@1 (%) | [原表](https://arxiv.org/abs/2601.14242)，2026-11-07 |

> 字段状态：待核实

> The embedded __NEXT_DATA__.props.pageProps.leaderboardData on the official page was read, and the pass-1 key and the mean-score key are clearly distinguished; the default 84.2 in the original HTML corresponds to Pass@1, and the Mean Score is 90.4. The overall update time and the actual run date are Unverified.

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### Coverage note

The public Mercor page embeds 70 model configurations. The top three are taken by sorting, item by item, on the pass-1 key, the mean-score key, and the Loop harness, and the meaning of the static Score is not guessed; AA452 questions and the 480 questions of the original paper are listed separately. The official site's 240/31 still conflicts with HF480/33 and with the openness policy.

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问 2026-11-07）；[来源3](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

## Contact

### 公开科研联系邮箱

apex@mercor.com

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### 公开反馈

https://github.com/Mercor-Intelligence/archipelago/issues

[来源1](https://github.com/Mercor-Intelligence/archipelago)（访问 2026-11-07）

### 官方社交

Unverified

> 字段状态：待核实

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### 隐私说明/政策

Unverified

> 字段状态：待核实

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2601.14242

[来源1](https://arxiv.org/abs/2601.14242)（访问 2026-11-07）

### PDF SHA-256

4f253c14f71cb9a1d17c9204e5b0812f42280f867d1f189f817286029e63594a

> SHA-256 of the bytes actually downloaded. It does not mean an existing copy was replaced.

[来源1](https://arxiv.org/pdf/2601.14242)（访问 2026-11-07）

### PDF bytes

1645464

[来源1](https://arxiv.org/pdf/2601.14242)（访问 2026-11-07）

### Folder

Unverified

> 字段状态：待核实

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### 其他官方材料

```json
[
 {
 "type": "Official introduction/protocol"
 "url": "https://huggingface.co/datasets/mercor/apex-agents"
 }
]
```

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

### 论文副本

Unverified

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问 2026-11-07）

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

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问 2026-11-07）
