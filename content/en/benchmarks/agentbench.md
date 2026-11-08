# AgentBench

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

Official materials were searched again; the historical leaderboard, the current snapshot, and vendor self-reports are kept separate; fields without empirical support remain Unverified

The original eight environments and the current five-environment FC edition are two scopes of aggregation. This page keeps both the official FC CSV and the baselines from the original paper, and it does not place percentage success rates and normalized Overall scores on one ranking.

## Basic information

### Short name

AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### Full name

AgentBench

> The official name is retained, and the paper title is not automatically expanded into a full name.

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### Benchmark version

The current repository is AgentBench FC (released 2025-10-10, with 5 function-calling environments); the original 8 environments remain on the v0.1 and v0.2 branches.

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）

### Paper version

arXiv v3

> A paper revision is not the same as a dataset version.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Release date

2023-08-08 00:08:11 (first arXiv draft).

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Section

Agent

> Benchmark Constitution editorial filing. Only the main section is counted.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Field tags

- Overall capability of interactive agents

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### License

Apache-2.0 (the marking on the code of the GitHub repository; it does not automatically cover the original questions, third-party materials, or private test data)

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### Paper

https://arxiv.org/abs/2308.03688

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Code

https://github.com/THUDM/AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### 数据地址

https://github.com/THUDM/AgentBench/tree/main/data

> The data directory of the official repository; the KG also requires Freebase, and the directory cannot be treated as a one-click data package that contains every third-party environment dependency.

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）

### Official entry

https://github.com/THUDM/AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### Paper title

AgentBench: Evaluating LLMs as Agents

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

## Origin and maintenance

### Initiators

Author affiliations including Tsinghua University, Ohio State University, and UC Berkeley.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### 合作方

Unverified

> 字段状态：待核实

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Authors

- Liu, Xiao
- Yu, Hao
- Zhang, Hanchen
- Xu, Yifan
- Lei, Xuanyu
- Lai, Hanyu
- Gu, Yu
- Ding, Hangliang
- Men, Kaiwen
- Yang, Kejuan
- Zhang, Shudan
- Deng, Xiang
- Zeng, Aohan
- Du, Zhengxiao
- Zhang, Chenhui
- Shen, Sheng
- Zhang, Tianjun
- Su, Yu
- Sun, Huan
- Huang, Minlie
- Dong, Yuxiao
- Tang, Jie

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Maintainer

THUDM / AgentBench project team

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Funders

The paper thanks Zhipu AI for GPU/API support and for funding of the research project; the full list of funding is in the original text.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

## Design goals

### Abilities measured

Comprehensive agent ability across long-horizon cross-environment interaction, tool execution, decision-making, following feedback, and completing goals.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Design background

Single-turn static language/knowledge tasks have difficulty evaluating an agent that can act, and capability differences across interaction environments are hidden by a single task.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

## Construction

### Question sources

8 environments: OS, Database, Knowledge Graph, Digital Card Game, Lateral Thinking Puzzles, Household (ALFWorld), Web Shopping (WebShop), and Web Browsing (Mind2Web).

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### 出题者背景

A multi-university research team; a mix of self-built environments and existing tasks, not a uniform set of expert-original questions.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Review process

Each environment constructs tasks, interaction interfaces, and a dedicated evaluation; not every environment can be described as the same review process.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Quality control

A unified message and action framework, environment-specific budgets, and validity checks; failed trajectories are used for error analysis.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Decontamination

It includes data and environments that are already public, so training overlap cannot be guaranteed to be fully excluded; the original paper's setting is not the same as hidden new questions.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

## Data format

### 题量与规模

Original dev 269 and test 1,014; question counts and metrics differ by environment.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Question types

The original version's 8 environments include OS, DB, KG, DCG, LTP, ALFWorld, WebShop, and Mind2Web. The current FC version supports 5 environments in total, alfworld, dbbench, knowledgegraph, os_interaction, and webshop, with function-calling prompts and Docker Compose support.

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）

### Modalities

- 文本
- Code/tool action
- 模拟环境

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Languages

Instructions are mainly in English, and include action languages such as SQL and shell.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Difficulty

It varies with the environment and the task and cannot be summarized as one distribution of question difficulty.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Public and hidden splits

The original paper reports a dev/test split, and the code and environment are public; the use of a split is not the same as permanently hidden tests.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

## Evaluation

### Metrics

SR, F1, reward, game progress, step SR, and related figures are reported per environment; Overall is a normalized weighted average across environments, not percentage accuracy.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### 评分

Environment-specific success is judged first and then aggregated after normalization; individual scores and the method of normalization must be retained.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### 运行设置

The original paper uses a simple CoT strategy, temperature 0, no multiple retries or ensembles, context truncated at about 3500 tokens, and a fixed action budget in each environment.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### 官方脚本

https://github.com/THUDM/AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### 可比性警示

The mean pass@1 of the FC version across five environments, and the Overall normalized score of the original eight environments, are different protocols. 70.4% and 4.01 cannot be compared directly. The branch, the container, and the Prompt or Function Calling mode must be fixed.

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）；[来源2](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问2026-11-07）

## Current status

### 核查日期

2026-11-07 （）

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### 最新版本与采用证据

```json
{
  "version": "AgentBench FC (2025-10-10), current main; the original 8 environments v0.1/v0.2 are retained separately"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1"
      "date": "2026-09-17"
      "note": "ScienceIDE §4.2 and the references explicitly cite AgentBench as a prior benchmark for language-model agents and interactive environments; this is an H2 academic citation, and it does not claim that this paper ran the benchmark."
      "date_shanghai": "2026-09-17"
      "verified_in_round1": "The ScienceIDE text and references were reopened and confirmed by the original paper ID; it belongs to the related-work citations in §4.2 and is not an actual run in this paper."
    }
  ]
}
```

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/html/2609.19134v1)（访问2026-11-07）；[来源3](https://arxiv.org/abs/2609.19134)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2023-08-08"
  }
  {
    "version": "v2"
    "submitted_at": "2023-10-25"
  }
  {
    "version": "v3"
    "submitted_at": "2025-10-04"
  }
]
```

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Saturation

The highest five-environment AVG pass@1 on the current FC leaderboard is 70.4%; the gap among environments such as ALFWorld and OS is clear, so one mean cannot be used to say that the original eight environments, or every agent capability, is saturated.

[来源1](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问2026-11-07）

### Contamination and disputes

Aggregation of heterogeneous environments and metrics may conceal different weaknesses; contamination of public tasks and context/tool failures must be separated from reasoning ability.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### 版本与衍生关系

AgentBench FC: function calling in 5 environments, with AgentRL and Docker integration. VisualAgentBench: dated 2024-08-13, with 5 independent environments for visual agents. Rankings are not merged with the original 8 environments.

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07 （）

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### Official leaderboard

https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pubhtml

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）；[来源2](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问2026-11-07）

### 第三方覆盖

Unverified

> 字段状态：待核实

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### 分轨结果

#### Official AgentBench FC Sheet

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | AgentRL w/ Qwen2.5-32B-Instruct | 70.4 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 2 | AgentRL w/ Qwen2.5-14B-Instruct | 67.7 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 3 | AgentRL w/ GLM-4-9B-0414 | 65.0 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 4 | AgentRL w/ Qwen2.5-7B-Instruct | 62.0 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 5 | AgentRL w/ Qwen2.5-3B-Instruct | 60.0 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 6 | Claude Sonnet 4.5 (2025-09-29) | 58.9 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 7 | Claude Sonnet 4.5 Thinking (2025-09-29) | 58.3 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 8 | Claude Sonnet 4 Thinking (2025-05-14) | 58.2 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 9 | Claude Sonnet 4 (2025-05-14) | 57.4 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 10 | Claude Sonnet 3.7 (2025-02-19) | 53.2 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 11 | GPT-5 (2025-08-07) | 52.2 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 12 | AgentLM-70B | 51.4 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 13 | Claude Sonnet 3.7 Thinking (2025-02-19) | 50.0 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 14 | DeepSeek-R1 (2025-05-28) | 49.3 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 15 | AgentLM-13B | 45.1 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 16 | AgentLM-7B | 42.7 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 17 | o3-mini (2025-01-31) | 40.9 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 18 | Qwen2.5-72B-Instruct | 40.8 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 19 | o4-mini (2025-04-16) | 39.7 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 20 | GPT-4o (2024-11-20) | 39.6 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 21 | Qwen2.5-32B-Instruct | 37.2 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 22 | Hephaestus-8B-IFT | 36.3 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 23 | DeepSeek-V3 (2025-03-24) | 36.1 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 24 | Hephaestus-8B-Base | 31.9 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |
| 25 | Qwen2.5-14B-Instruct | 27.2 | Five-environment AVG pass@1 (%) | [原表](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)，2026-11-07 |

> AgentRL w/ Qwen2.5-32B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 94.5, "DB": 70.4, "KG": 77.0, "OS": 51.7, "WebShop": 58.6}}

> AgentRL w/ Qwen2.5-14B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 91.5, "DB": 72.2, "KG": 72.8, "OS": 43.6, "WebShop": 58.5}}

> AgentRL w/ GLM-4-9B-0414：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 93.3, "DB": 66.9, "KG": 75.7, "OS": 33.2, "WebShop": 55.9}}

> AgentRL w/ Qwen2.5-7B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 91.5, "DB": 63.7, "KG": 57.8, "OS": 40.8, "WebShop": 56.1}}

> AgentRL w/ Qwen2.5-3B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 92.4, "DB": 60.0, "KG": 55.0, "OS": 40.5, "WebShop": 52.1}}

> Claude Sonnet 4.5 (2025-09-29)：{"model_organization": "Anthropic", "result_source": "-", "source_release_month": "11/2025", "subscores": {"ALFWorld": 82.5, "DB": 71.2, "KG": 64.1, "OS": 38.0, "WebShop": 38.6}}

> Claude Sonnet 4.5 Thinking (2025-09-29)：{"model_organization": "Anthropic", "result_source": "-", "source_release_month": "11/2025", "subscores": {"ALFWorld": 80.7, "DB": 70.3, "KG": 62.7, "OS": 39.4, "WebShop": 38.2}}

> Claude Sonnet 4 Thinking (2025-05-14)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 69.0, "DB": 68.4, "KG": 64.4, "OS": 51.0, "WebShop": 38.3}}

> Claude Sonnet 4 (2025-05-14)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 73.6, "DB": 70.1, "KG": 63.4, "OS": 45.3, "WebShop": 34.6}}

> Claude Sonnet 3.7 (2025-02-19)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 61.1, "DB": 68.5, "KG": 59.8, "OS": 36.5, "WebShop": 40.1}}

> GPT-5 (2025-08-07)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 65.4, "DB": 63.2, "KG": 64.1, "OS": 34.5, "WebShop": 33.7}}

> AgentLM-70B：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 86.0, "DB": 37.7, "KG": 47.0, "OS": 21.5, "WebShop": 64.9}}

> Claude Sonnet 3.7 Thinking (2025-02-19)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 54.1, "DB": 68.4, "KG": 38.2, "OS": 53.1, "WebShop": 36.0}}

> DeepSeek-R1 (2025-05-28)：{"model_organization": "DeepSeek", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 51.4, "DB": 60.4, "KG": 50.2, "OS": 53.6, "WebShop": 31.0}}

> AgentLM-13B：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 76.0, "DB": 33.7, "KG": 26.8, "OS": 18.1, "WebShop": 70.8}}

> AgentLM-7B：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 84.0, "DB": 30.6, "KG": 18.1, "OS": 17.4, "WebShop": 63.6}}

> o3-mini (2025-01-31)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 28.4, "DB": 56.5, "KG": 51.8, "OS": 35.1, "WebShop": 32.7}}

> Qwen2.5-72B-Instruct：{"model_organization": "Alibaba", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 47.5, "DB": 45.3, "KG": 26.5, "OS": 49.5, "WebShop": 35.4}}

> o4-mini (2025-04-16)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 32.6, "DB": 63.4, "KG": 32.4, "OS": 41.8, "WebShop": 28.5}}

> GPT-4o (2024-11-20)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 28.3, "DB": 54.3, "KG": 49.3, "OS": 38.5, "WebShop": 27.8}}

> Qwen2.5-32B-Instruct：{"model_organization": "Alibaba", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 32.1, "DB": 55.8, "KG": 33.8, "OS": 37.0, "WebShop": 27.5}}

> Hephaestus-8B-IFT：{"model_organization": "Amazon", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 46.0, "DB": 29.7, "KG": 21.2, "OS": 20.8, "WebShop": 63.9}}

> DeepSeek-V3 (2025-03-24)：{"model_organization": "DeepSeek", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 31.9, "DB": 58.4, "KG": 14.0, "OS": 53.0, "WebShop": 23.4}}

> Hephaestus-8B-Base：{"model_organization": "Amazon", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 30.0, "DB": 32.3, "KG": 16.0, "OS": 20.8, "WebShop": 60.5}}

> Qwen2.5-14B-Instruct：{"model_organization": "Alibaba", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 8.7, "DB": 48.4, "KG": 35.3, "OS": 26.0, "WebShop": 17.6}}

#### Original 8 environments/paper historical Table3

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| Not applicable (columns selected within the source, not a global ranking) | GPT-4-0613 | 4.01 | Overall normalized score | [原表](https://arxiv.org/abs/2308.03688)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | Claude 3 Opus | 3.11 | Overall normalized score | [原表](https://arxiv.org/abs/2308.03688)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | GLM-4 | 2.89 | Overall normalized score | [原表](https://arxiv.org/abs/2308.03688)，2026-11-07 |



> The FC results come from the official CSV that was actually downloaded; the Release Date column is kept under the original name in the source and is not presented as the time the experiment was run.

[来源1](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### Coverage note

The official CSV has 25 rows of FC models and, separately, three historical rows for the original 8 environments. The FC top three are 70.4/67.7/65.0; the Release Date of the top three is 10/2025, and the rest include 11/2025, which is not presented as the actual run date. The original Overall normalized scores and the FC percentage means cannot be ranked together.

[来源1](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问2026-11-07）

## Contact

### 公开科研联系邮箱

- agentbench_fc@googlegroups.com
- agentbench@googlegroups.com

> Result submissions for the FC version contact the former; the original Google Group entry in the repository is the latter.

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问2026-11-07）

### 公开反馈

https://github.com/THUDM/AgentBench/issues

> Public repository feedback entry point; no question was sent.

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### 官方社交

https://twitter.com/thukeg

> The team-account link shown in the official repository; the content on X was not visited.

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）

### 隐私说明/政策

Unverified

> 字段状态：待核实

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2308.03688

[来源1](https://arxiv.org/abs/2308.03688)（访问2026-11-07）

### PDF SHA-256

9c780e35fc0b2de6c2e21e0572f6aaaadcf7ecdd56d63cfaae2b415bc0dc83c3

> SHA-256 of the bytes actually downloaded. It does not mean an existing copy was replaced.

[来源1](https://arxiv.org/pdf/2308.03688)（访问2026-11-07）

### PDF bytes

23017024

[来源1](https://arxiv.org/pdf/2308.03688)（访问2026-11-07）

### Folder

```json
{
  "id": "1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
[
  {
    "type": "Chinese-language introductory Google Doc"
    "id": "1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA"
    "webViewLink": "
  }
]
```

> The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）；[来源2](

### 论文副本

```json
{
  "id": "16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp"
  "webViewLink": "
}
```

[来源1](

## Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": "（）"
    Latest review
  }
  {
    "date": "2026-11-07"
    "timezone": "（）"
    "round": "1 / 深度实证复核"
    Latest review
  }
  {
    "date": "2026-11-07"
    "timezone": " ()"
    Latest review
  }
]
```

[来源1](https://github.com/THUDM/AgentBench)（访问2026-11-07）
