# SkillsBench

> Benchmark Constitution, in-depth review 2026-11-08. Verified to exist; a research snapshot; note: trending: B; marks on fields that have not been verified are retained

SkillsBench turns the question “whether a skill is actually useful” into a paired experiment: the same model and the same agent complete expert tasks with a skill and without a skill. The default v1.1 contains 87 questions, and an additional 14 questions cannot be merged into the default inventory. The official release of 87 questions, the HF audit export, and the independent Vals implementation have different configurations and different snapshots in time, and this record does not join them into one leaderboard of the bare model.

[Source 1](https://arxiv.org/abs/2602.12670) (accessed 2026-11-08); [Source 2](https://github.com/benchflow-ai/skillsbench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/benchflow/skillsbench) (accessed 2026-11-08); [Source 4](https://www.skillsbench.ai) (accessed 2026-11-08)

## Basic information

### Short name

SkillsBench

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### Full name

SkillsBench

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### Benchmark version

SkillsBench v1.1 (87 default tasks; 14 tasks-extra are not counted in the default set)

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### Paper version

v4 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### Release date

2026-02-13 (arXiv v1 2026-02-13; not the release date of the v1.1 tag)

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### Section

Agent

> Editorial filing. It does not represent an official classification.

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 领域

```json
[
  "代码"
  "技能"
]
```

> Editorial filing. It does not represent an official classification.

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 许可与适用范围

Apache-2.0 (official repository LICENSE and README); external assets that the tasks depend on must still follow their own licenses.

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2602.12670

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Code

https://github.com/benchflow-ai/skillsbench

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 数据

https://huggingface.co/datasets/benchflow/skillsbench

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### Official entry

https://www.skillsbench.ai

[来源1](https://github.com/benchflow-ai/skillsbench)（访问 2026-11-08）；[来源2](https://www.skillsbench.ai)（访问 2026-11-08）

### Paper title

SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## Origin and maintenance

### Initiators

BenchFlow (original benchmark); Vals AI (independent implementation)

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 合作/参与机构

Contributors come from BenchFlow, OSU, Amazon, UC Berkeley, and other institutions, and from independent researchers; Vals explicitly collaborates with BenchFlow on integration into Valkyrie.

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

### Authors

Xiangyi Li, Yimin Liu, Wenbo Chen, and others; the full author list is in the paper. The author table cited by Vals differs from the revised list in the current paper.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Maintainer

BenchFlow (original benchmark); Vals AI (independent implementation)

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Funders

The acknowledgments in the paper state that model vendors provided model access and API support, that Google Cloud Platform and Amazon Bedrock provided infrastructure, that Lambda provided GPUs, and that Daytona provided credits. This is an inventory of resource support, and it is not presented as a cash funding amount.

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

## Design goals

### Abilities measured

Paired comparison of the same model and harness with and without a reusable skill package, measuring the gain from skill augmentation.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Design background

Traditional agent scores mix the base model, the tool architecture, and the augmentation effect; this benchmark treats skill as an independent experimental factor.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## Construction

### Question sources

142 contributors submitted 400 candidate tasks. After gating on structure, oracle execution, instruction source, and skill leakage, plus human review, 87 tasks are currently retained.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 出题者背景

142 contributors submitted tasks. The paper’s authorship includes BenchFlow and several universities, companies, and independent researchers; authors with an Amazon affiliation note that the work was done outside their regular duties.

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### Review process

Real work instructions written by people, a fixed container, a reference solution, and a deterministic verifier; a skill must not contain instance answers, a hard-coded path, or a magic number.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Quality control

Real work instructions written by people, a fixed container, a reference solution, and a deterministic verifier; a skill must not contain instance answers, a hard-coded path, or a magic number.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 污染控制

Skills are decoupled from the task answers, and instance filenames, magic numbers, verbatim oracle commands, and expected outputs are scanned for leakage; complete exclusion of pretraining contamination cannot be guaranteed.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## Data format

### 题量

v1.1: 87 default tasks and 8 domains; another 14 task packages that require credentials or are incompatible with the integration are explicitly excluded. The official site currently has 25 model–harness configurations (24 pairs plus 1 With only); paper v4 has 18 configurations, and the HF card and the export have 24 configurations. Source snapshots are kept separately.

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### 任务形式

Terminal tasks and file-artifact tasks; they include the natural sciences, mathematical optimization, security, engineering, finance, office work, and software.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Modalities

```json
[
  "文本"
  "代码"
  "Data file"
]
```

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Languages

Unverified

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### Difficulty

Expert workflows that require skills to be combined; the official target is combinations of more than 2 skills, but the target is not a demonstrated conclusion that every model's score is below 50%.

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### Public and hidden splits

Definitions, oracles, verifiers, and skill packages for 87 tasks are public; at runtime the agent cannot read the oracle or the verifier. The 14 questions in tasks-extra do not belong to the default evaluation set.

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

## Evaluation

### Metrics

Task macro-average pass rate, Skills absolute gain, and normalized gain.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 评分

Deterministic script/pytest verification; Vals runs 3 times per model per condition, averaging within each question first and then across questions.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 运行设置

Official v1.1 uses BenchFlow to pair with-skill and no-skill for the same model and the same agent. The HF export counts only reviewed non-timeout trials and retains partial coverage. The independent Vals implementation defaults to OpenHands-CLI commit 3ca17446c5d9c1e35e054803478a3501ec251ecf. GPT 5.5 additionally lists Codex, with 3 runs per condition, averaged within a question first and then across questions.

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

### 评测工具

https://github.com/benchflow-ai/skillsbench

> The link is the one indicated by an original paper or dataset card that was opened; the code was not verified file by file.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### Comparability

The paper and Vals differ in inventory, harness, and runtime; the paper’s results on 87 questions cannot replace the current Vals leaderboard. Skill gain is to be computed for the same model and the same harness.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "v1.1"
  "source_commit": "27738384b1df694ea2ae466e416f476e94d8fab9"
  "active_tasks": 87
  "excluded_tasks": 14
  "source_snapshots": "Official site: 25 configurations / 2026-07-16; HF archive: 24 configurations, and the card states 2026-06-16; Vals independently lists 35 rows / 2026-10-29. These cannot be forcibly merged."
}
```

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-02-13"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2026-03-07"
    "timezone": ""
  }
  {
    "version": "v3"
    "submitted_at": "2026-03-13"
    "timezone": ""
  }
  {
    "version": "v4"
    "submitted_at": "2026-06-15"
    "timezone": ""
  }
]
```

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### 饱和与能力边界

With Skills on the current official website peaks at 67.3%; the independent Vals leaderboard peaks at 69.80%. Different harnesses, inventories, and run times cannot be combined into a single degree of saturation, and there is not yet evidence of complete saturation.

[来源1](https://www.skillsbench.ai)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

### 风险与争议

The paper and Vals differ in inventory, harness, and runtime; the paper’s results on 87 questions cannot replace the current Vals leaderboard. Skill gain is to be computed for the same model and the same harness.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 系列与衍生关系

SkillsBench is a separate benchmark from AgentBench; With Skills and No Skills are experimental conditions of the same entry and are not added again as new entries.

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2602.12670) (accessed 2026-11-08); [Source 2](https://github.com/benchflow-ai/skillsbench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/benchflow/skillsbench) (accessed 2026-11-08); [Source 4](https://www.skillsbench.ai) (accessed 2026-11-08)

### Official entry

https://www.skillsbench.ai

[来源1](https://www.skillsbench.ai)（访问 2026-11-08）

### 独立来源

https://www.vals.ai/benchmarks/skillsbench

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 分来源与协议结果

#### official v1.1 export / With Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-5.5 | 67.3 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":15.8,"selected_trials":261} |
| 2 | GPT-5.5 | 66.5 | resolution rate (%) | {"condition":"With Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19.7,"selected_trials":261} |
| 3 | Opus 4.7 | 61.2 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.2,"selected_trials":261} |
| 4 | Gemini 3.1 Pro | 60.8 | resolution rate (%) | {"condition":"With Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":24.8,"selected_trials":261} |
| 5 | GLM 5.1 | 58.4 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":25.7,"selected_trials":261} |
| 6 | Gemini 3 Flash | 54.6068 | resolution rate (%) | {"condition":"With Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":20.3884,"selected_trials":261} |
| 7 | Opus 4.8 | 54.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":8.4,"selected_trials":261} |
| 8 | Kimi K2.6 | 54 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":20.6,"selected_trials":261} |
| 9 | Opus 4.7 | 53.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.1,"selected_trials":261} |
| 10 | MiniMax M3 | 53 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.3,"selected_trials":261} |
| 11 | Gemini 3.1 Pro | 52.8 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19,"selected_trials":261} |
| 12 | GPT-5.2 | 51.7046 | resolution rate (%) | {"condition":"With Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":22.0068,"selected_trials":261} |
| 13 | Opus 4.6 | 50.2241 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":16.5479,"selected_trials":259} |
| 14 | DeepSeek V4 Pro | 50.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.2,"selected_trials":261} |
| 15 | Opus 4.5 | 49.0395 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":25.223,"selected_trials":257} |
| 16 | Gemini 3.5 Flash | 48.2 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":7.1,"selected_trials":261} |
| 17 | Sonnet 4.6 | 47.2 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":13.6,"selected_trials":261} |
| 18 | DeepSeek V4 Flash | 44.7 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":17.2,"selected_trials":261} |
| 19 | Grok 4.3 | 41.7 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.8,"selected_trials":261} |
| 20 | GPT-5.4 Mini | 41.4 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.5,"selected_trials":261} |
| 21 | Sonnet 4.5 | 36.1723 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":19.4519,"selected_trials":260} |
| 22 | MiniMax M2.7 | 34.9 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":16.8,"selected_trials":261} |
| 23 | Haiku 4.5 | 30.0831 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":21.2897,"selected_trials":261} |
| 24 | Gemini 3.1 Flash Lite | 20.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":4.1,"selected_trials":261} |

#### official v1.1 export / Without Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-5.5 | 51.5 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":15.8,"selected_trials":261} |
| 2 | GPT-5.5 | 46.8 | resolution rate (%) | {"condition":"Without Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19.7,"selected_trials":261} |
| 4 | Opus 4.7 | 43 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.2,"selected_trials":261} |
| 7 | Gemini 3.1 Pro | 36 | resolution rate (%) | {"condition":"Without Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":24.8,"selected_trials":261} |
| 13 | GLM 5.1 | 32.7 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":25.7,"selected_trials":261} |
| 8 | Gemini 3 Flash | 34.2184 | resolution rate (%) | {"condition":"Without Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":20.3884,"selected_trials":261} |
| 3 | Opus 4.8 | 45.7 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":8.4,"selected_trials":261} |
| 12 | Kimi K2.6 | 33.4 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":20.6,"selected_trials":261} |
| 5 | Opus 4.7 | 42.1 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.1,"selected_trials":261} |
| 15 | MiniMax M3 | 29.7 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.3,"selected_trials":261} |
| 9 | Gemini 3.1 Pro | 33.8 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19,"selected_trials":261} |
| 16 | GPT-5.2 | 29.6978 | resolution rate (%) | {"condition":"Without Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":22.0068,"selected_trials":261} |
| 10 | Opus 4.6 | 33.6762 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":16.5479,"selected_trials":258} |
| 18 | DeepSeek V4 Pro | 26.9 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.2,"selected_trials":261} |
| 19 | Opus 4.5 | 23.8165 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":25.223,"selected_trials":261} |
| 6 | Gemini 3.5 Flash | 41.1 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":7.1,"selected_trials":261} |
| 11 | Sonnet 4.6 | 33.5 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":13.6,"selected_trials":261} |
| 17 | DeepSeek V4 Flash | 27.5 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":17.2,"selected_trials":261} |
| 20 | Grok 4.3 | 22.8 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.8,"selected_trials":261} |
| 14 | GPT-5.4 Mini | 29.9 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.5,"selected_trials":261} |
| 22 | Sonnet 4.5 | 16.7204 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":19.4519,"selected_trials":261} |
| 21 | MiniMax M2.7 | 18.1 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":16.8,"selected_trials":261} |
| 24 | Haiku 4.5 | 8.7935 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":21.2897,"selected_trials":261} |
| 23 | Gemini 3.1 Flash Lite | 16 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":4.1,"selected_trials":261} |

#### Vals With Skills / OpenHands

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | DeepSeek V4.1 Flash | 69.8 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 2 | Grok 4.5 | 66.03 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 3 | Gemini 3.7 Flash | 65.89 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 5 | GPT 5.5 | 62.21 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 6 | Claude Fable 5.1 | 61.55 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 7 | GPT-5.6 Luna | 60.45 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 8 | Claude Opus 5 | 60.44 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 9 | Claude Opus 4.8 | 59.23 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 10 | Muse Spark 1.1 | 59.19 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 11 | GPT-5.6 Terra | 58.9 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 12 | Gemini 3.8 Flash | 57.98 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 13 | Grok 4.6 | 55.77 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 14 | Qwen 3.7 Plus | 54.3 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 15 | GPT-5.6 Sol | 54.1 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 16 | DeepSeek V4 Pro 0813 | 53.83 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 17 | Muse Spark 1.2 | 53.04 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 18 | Gemini 3.5 Flash | 52.74 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 19 | GPT 5.4 (xhigh) | 51.71 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 20 | MiniMax-M3 | 51.5 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 21 | DeepSeek V4 | 51.27 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 22 | DeepSeek V4 Flash 0731 | 50.67 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 23 | Kimi K2.7 Code | 50.04 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 24 | Claude Sonnet 4.6 | 49.05 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 25 | GLM 5.3 | 47.51 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 26 | Claude Sonnet 5 | 46.48 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 27 | GLM 5.2 | 45.08 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 28 | Qwen 3.8 Max | 42.01 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 29 | Grok 4.3 | 40.64 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 30 | GLM 5.3 Flash | 40.16 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 31 | Qwen 3.8 27B | 38.11 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 32 | Inkling Small | 33.58 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 33 | Ling 3.0 Flash | 27.95 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 34 | Inkling | 26.09 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 35 | Mercury 2.5 | 18.06 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |

#### Vals With Skills / Codex

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 4 | GPT 5.5 | 62.55 | Accuracy (%) | {"harness":"Codex","condition":"With Skills","source_date":"2026-10-29"} |

#### official website 2026-07-16 / Without Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | OpenAI GPT-5.5 OpenHands | 51.5 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 15.8"} |
| 2 | OpenAI GPT-5.5 Codex | 46.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.7"} |
| 4 | Claude Opus 4.7 Claude Code | 43.0 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.2"} |
| 7 | Gemini Gemini 3.1 Pro Gemini CLI | 36.0 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 24.8"} |
| 13 | Z.ai GLM 5.1 OpenHands | 32.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.7"} |
| 8 | Gemini Gemini 3 Flash Gemini CLI | 34.2 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.4"} |
| 3 | Claude Opus 4.8 OpenHands | 45.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 8.4"} |
| 12 | MoonshotAI Kimi K2.6 OpenHands | 33.4 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.6"} |
| 5 | Claude Opus 4.7 OpenHands | 42.1 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.1"} |
| 15 | Minimax MiniMax M3 OpenHands | 29.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.3"} |
| 9 | Gemini Gemini 3.1 Pro OpenHands | 33.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.0"} |
| 15 | OpenAI GPT-5.2 Codex | 29.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 22.0"} |
| 10 | Claude Opus 4.6 Claude Code | 33.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.5"} |
| 18 | DeepSeek DeepSeek V4 Pro OpenHands | 26.9 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.2"} |
| 19 | Claude Opus 4.5 Claude Code | 23.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.2"} |
| 6 | Gemini Gemini 3.5 Flash OpenHands | 41.1 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 7.1"} |
| 11 | Claude Sonnet 4.6 OpenHands | 33.5 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 13.6"} |
| 17 | DeepSeek DeepSeek V4 Flash OpenHands | 27.5 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 17.2"} |
| 20 | Grok Grok 4.3 OpenHands | 22.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.8"} |
| 14 | OpenAI GPT-5.4 Mini OpenHands | 29.9 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.5"} |
| 22 | Claude Sonnet 4.5 Claude Code | 16.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.5"} |
| 21 | Minimax MiniMax M2.7 OpenHands | 18.1 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.8"} |
| 24 | Claude Haiku 4.5 Claude Code | 8.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 21.3"} |
| 23 | Gemini Gemini 3.1 Flash Lite OpenHands | 16.0 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 4.1"} |

#### official website 2026-07-16 / With Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | OpenAI GPT-5.5 OpenHands | 67.3 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 15.8"} |
| 2 | OpenAI GPT-5.5 Codex | 66.5 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.7"} |
| 3 | Claude Opus 4.7 Claude Code | 61.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.2"} |
| 4 | Gemini Gemini 3.1 Pro Gemini CLI | 60.8 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 24.8"} |
| 5 | Z.ai GLM 5.1 OpenHands | 58.4 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.7"} |
| 6 | Hunyuan HY3 Claude Code | 55.9 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"—"} |
| 7 | Gemini Gemini 3 Flash Gemini CLI | 54.6 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.4"} |
| 8 | Claude Opus 4.8 OpenHands | 54.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 8.4"} |
| 9 | MoonshotAI Kimi K2.6 OpenHands | 54.0 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.6"} |
| 10 | Claude Opus 4.7 OpenHands | 53.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.1"} |
| 11 | Minimax MiniMax M3 OpenHands | 53.0 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.3"} |
| 12 | Gemini Gemini 3.1 Pro OpenHands | 52.8 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.0"} |
| 13 | OpenAI GPT-5.2 Codex | 51.7 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 22.0"} |
| 14 | Claude Opus 4.6 Claude Code | 50.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.5"} |
| 15 | DeepSeek DeepSeek V4 Pro OpenHands | 50.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.2"} |
| 16 | Claude Opus 4.5 Claude Code | 49.0 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.2"} |
| 17 | Gemini Gemini 3.5 Flash OpenHands | 48.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 7.1"} |
| 18 | Claude Sonnet 4.6 OpenHands | 47.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 13.6"} |
| 19 | DeepSeek DeepSeek V4 Flash OpenHands | 44.7 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 17.2"} |
| 20 | Grok Grok 4.3 OpenHands | 41.7 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.8"} |
| 21 | OpenAI GPT-5.4 Mini OpenHands | 41.4 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.5"} |
| 22 | Claude Sonnet 4.5 Claude Code | 36.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.5"} |
| 23 | Minimax MiniMax M2.7 OpenHands | 34.9 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.8"} |
| 24 | Claude Haiku 4.5 Claude Code | 30.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 21.3"} |
| 25 | Gemini Gemini 3.1 Flash Lite OpenHands | 20.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 4.1"} |

[来源1](https://huggingface.co/datasets/benchflow/skillsbench-leaderboard/resolve/main/leaderboard/skillsbench/v1.1/official.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）；[来源3](https://www.skillsbench.ai)（访问 2026-11-08）

### 覆盖与时效

The machine export on HF, 24 configurations × 2 conditions = 48 rows, is an independently auditable track, and the original value of each condition is retained as is. The official site's 25 configurations, 24 pairs +HY3 With only, 49 rows in total, form a separate track, and their public decimal precision is retained. The HF card says 2026-06-16, the official site says 2026-07-16, and each row's recomputed_date differs again. They are recorded separately, and the access date is not presented as the recomputation date. The readable With Skills table on Vals, with 35 configurations, is a further track. The paired figure on that page has only rounded values, and a more precise No Skills leaderboard was not reverse-engineered.

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源2](https://www.skillsbench.ai)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/benchflow/skillsbench-leaderboard/resolve/main/leaderboard/skillsbench/v1.1/official.json)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

## Contact

### 公开工作邮箱

xiangyi@benchflow.ai

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 官方反馈

https://github.com/benchflow-ai/skillsbench/issues

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### 公开社区

https://discord.gg/G9dg3EfSva

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### 隐私边界

Unverified

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2602.12670

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### PDF SHA-256

e987ebc3f0084a1ffc8acbca58259e33120b95fcef3876abfad060e169cf210b

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### PDF bytes

```json
1769852
```

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### Folder

Unverified

> The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Official web page/paper opened"
    "url": "https://www.vals.ai/benchmarks/skillsbench"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://arxiv.org/abs/2602.12670"
  }
  {
    "type": "Opened primary material"
    "url": "https://github.com/benchflow-ai/skillsbench"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://huggingface.co/datasets/benchflow/skillsbench"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://www.skillsbench.ai"
    "accessed": "2026-11-08"
  }
]
```

[Source 1](https://arxiv.org/abs/2602.12670) (accessed 2026-11-08); [Source 2](https://github.com/benchflow-ai/skillsbench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/benchflow/skillsbench) (accessed 2026-11-08); [Source 4](https://www.skillsbench.ai) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

## Changelog

```json
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
```

[Source 1](https://arxiv.org/abs/2602.12670) (accessed 2026-11-08); [Source 2](https://github.com/benchflow-ai/skillsbench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/benchflow/skillsbench) (accessed 2026-11-08); [Source 4](https://www.skillsbench.ai) (accessed 2026-11-08)
