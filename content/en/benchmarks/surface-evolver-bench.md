# Surface Evolver Bench

> Benchmark Constitution, in-depth review 2026-11-08. Verified to exist; an 11-section research snapshot; note: trending: B; unknown fields remain Unverified

Surface Evolver Bench requires the model to submit a .fe file that a physics simulator can execute. Geometry, orientation, contact angle, volume, and energy must be consistent with one another. Scoring is not a model judge. It is deterministic static checks, hidden simulation, and numerical tolerance. The official aggregate JSON was obtained directly, distinguishing a partial score of 95% from a strict pass rate of 87.5%. The entry is no longer left blank because an interactive figure is hard to read.

[Source 1](https://github.com/yhenon/surface-evolver-llm-eval) (accessed 2026-11-08); [Source 2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json) (accessed 2026-11-08)

## Basic information

### Short name

Surface Evolver Bench

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Full name

Surface Evolver Bench

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Benchmark version

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Paper version

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Release date

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Section

Physics

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 领域

```json
[
  "材料"
  "流体"
  "Scientific code"
]
```

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 许可与适用范围

Apache-2.0 (the official LICENSE was opened); Surface Evolver and the other dependencies remain under their own licenses.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### Paper

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Code

https://github.com/yhenon/surface-evolver-llm-eval

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 数据

https://github.com/yhenon/surface-evolver-llm-eval/tree/main/tasks_public

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### Official entry

https://yhenon.github.io/surface-evolver-llm-eval/

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Paper title

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Yann Henon

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 合作/参与机构

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Authors

Yann Henon (an author of the official project; not the author list of an independent paper that has been found).

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### Maintainer

Yann Henon

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### Funders

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## Design goals

### Abilities measured

Three-dimensional liquid surfaces are described in a low-resource custom format, handling contact angle, gravity, volume constraints, and boundary integrals.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Design background

Tests executable computational-physics modeling, not only textual physics knowledge; reading the documentation and iterative repair are allowed.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## Construction

### Question sources

The authors wrote a reference solution for each question, simulated the converged liquid surface, and precomputed volume, area, and energy.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 出题者背景

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Review process

The authors wrote the reference solutions by hand and solved for a converged liquid surface; acceptance checks on the static simulator and the hidden simulator are used together. An independent human review process with multiple experts is Unverified.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### Quality control

Static checks, a hidden Evolver script, and tolerance comparison with reference physical quantities; an LLM judge is not used.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 污染控制

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## Data format

### 题量

16 tasks; the official aggregate comprises 448 model-task runs and 28 configurations, with 16 tasks per configuration.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）；[来源2](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-08）

### 任务形式

In multiple steps, read the documentation, run the simulation, repair it, and submit the original .fe data file through a structured tool.

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### Modalities

```json
[
  "文本"
  "Surface Evolver .fe files"
  "Simulator feedback"
]
```

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### Languages

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Difficulty

Complex liquid configurations in grooves, wells, and channels; partial credit is given by task score.

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### Public and hidden splits

The repository separates tasks_public/ and tasks_private/, and by default it runs the private task directory; the agent sees only the prompt, the documents it may read, and the public run feedback, and acceptance is finally by hidden_command_script and by hidden thresholds on physical quantities. The directory name private does not mean that the files are necessarily impossible to download.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

The mean partial score and the strict pass rate are recorded separately.

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 评分

Weighted partial score: static checks 0.3, hidden Surface Evolver runs 0.3, and hidden tolerance checks on physical quantities 0.4; passed requires that the static checks and every dynamic check pass.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 运行设置

The tools are get_evolver_doc, run_surface_evolver, and submit_fe_file; repair may iterate up to the max-rounds limit; the original .fe file must be submitted through the structured tool. The reasoning level and the API provider are kept as part of the run configuration.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 评测工具

se_eval.run_eval (generate/grade), se_eval.run_matrix, and se_eval.rescore_results; the task JSON provides static_checks and dynamic_checks.evolver_metrics.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### Comparability

The mean score displayed by Epoch is not a pass rate; the harness documentation and the feedback loop can significantly affect scores.

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://github.com/yhenon/surface-evolver-llm-eval)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "待核实"
  "heat_confidence": "B"
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/benchmarks/surface-evolver-bench"
      "date": "2026-11-07"
      "note": "Epoch currently displays results and the protocol; on the observation date, tracking is mainly by a single institution."
    }
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
      "date": "2026-10-09"
      "note": "The Epoch review is Not enough info; this does not mean that the quality is acceptable."
    }
  ]
}
```

> B: current evaluation or vendor adoption mainly by a single institution; broad industry adoption cannot be claimed.

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 修订历史

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 饱和与能力边界

The highest official aggregate mean_score is 0.95 (claude-fable-5 high and kimi-k3); both have a strict pass_rate of 0.875 (14/16). Partial credit near a full score does not mean that every physics check has been solved.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

### 风险与争议

A low-resource domain is not the same as an absence of contamination. The authors say that early harnesses with no documentation, or with weak feedback, scored very low, and that tools, documentation, and the feedback loop materially affect the results; a small set of 16 questions and a single run do not support treating a tiny difference of rank as a statistically significant difference.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 系列与衍生关系

Surface Evolver is the underlying solver, and this evaluation is an LLM modeling harness for its 16 tasks; the mean partial score and the strict pass rate are two metrics of the same task, not two independent benchmarks.

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://github.com/yhenon/surface-evolver-llm-eval) (accessed 2026-11-08); [Source 2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json) (accessed 2026-11-08)

### Official entry

https://yhenon.github.io/surface-evolver-llm-eval/

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 独立来源

https://epoch.ai/benchmarks/surface-evolver-bench

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 分来源与协议结果

#### official aggregate / mean score

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | claude-fable-5 (high) | 0.95 | mean partial-credit score (0–1) | {"runs":16,"passed":14,"pass_rate":0.875} |
| 1 | kimi-k3 | 0.95 | mean partial-credit score (0–1) | {"runs":16,"passed":14,"pass_rate":0.875} |
| 3 | gpt-5.6-sol (xhigh) | 0.93125 | mean partial-credit score (0–1) | {"runs":16,"passed":14,"pass_rate":0.875} |
| 4 | gpt-5.5 (high) | 0.88125 | mean partial-credit score (0–1) | {"runs":16,"passed":12,"pass_rate":0.75} |
| 5 | claude-opus-4.8 (high) | 0.875 | mean partial-credit score (0–1) | {"runs":16,"passed":11,"pass_rate":0.6875} |
| 6 | gpt-5.6-terra (xhigh) | 0.8375 | mean partial-credit score (0–1) | {"runs":16,"passed":11,"pass_rate":0.6875} |
| 7 | gpt-5.5 (medium) | 0.8125 | mean partial-credit score (0–1) | {"runs":16,"passed":10,"pass_rate":0.625} |
| 8 | gemini-3.8-flash (high) | 0.76875 | mean partial-credit score (0–1) | {"runs":16,"passed":9,"pass_rate":0.5625} |
| 9 | grok-4.5 (high) | 0.74375 | mean partial-credit score (0–1) | {"runs":16,"passed":8,"pass_rate":0.5} |
| 10 | claude-opus-4.8 (none) | 0.68125 | mean partial-credit score (0–1) | {"runs":16,"passed":4,"pass_rate":0.25} |
| 11 | gpt-5.6-luna (medium) | 0.61875 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 12 | claude-sonnet-5 (medium) | 0.6 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 13 | gemini-3.5-flash (medium) | 0.58125 | mean partial-credit score (0–1) | {"runs":16,"passed":6,"pass_rate":0.375} |
| 14 | glm-5.2 (high) | 0.55625 | mean partial-credit score (0–1) | {"runs":16,"passed":5,"pass_rate":0.3125} |
| 15 | minimax-m3 | 0.5499999999999999 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 16 | muse-spark-1.1 (high) | 0.525 | mean partial-credit score (0–1) | {"runs":16,"passed":6,"pass_rate":0.375} |
| 16 | glm-5.3-flash (max) | 0.525 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 18 | kimi-k2.7-code | 0.4875 | mean partial-credit score (0–1) | {"runs":16,"passed":6,"pass_rate":0.375} |
| 19 | deepseek-v4.1-flash (high) | 0.4625 | mean partial-credit score (0–1) | {"runs":16,"passed":5,"pass_rate":0.3125} |
| 20 | qwen3.8-27b (xhigh) | 0.45 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 21 | qwen3.6-35b-a3b | 0.44375 | mean partial-credit score (0–1) | {"runs":16,"passed":2,"pass_rate":0.125} |
| 22 | deepseek-v4-pro (high) | 0.4 | mean partial-credit score (0–1) | {"runs":16,"passed":4,"pass_rate":0.25} |
| 23 | gemma-4-31b-it (none) | 0.30624999999999997 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 24 | mistral-large-4-0 | 0.28125 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 25 | mistral-medium-3-5 (high) | 0.26875 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 26 | gpt-oss-120b | 0.25 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 27 | laguna-m.1 | 0.15625 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 27 | trinity-large-thinking | 0.15625 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

### 覆盖与时效

The officially released data/aggregates.json is parsed directly. The original mean_score, pass_rate, passed, and runs of all 28 configurations are kept in full, and identical mean_score values share a rank; values are not estimated by reading a chart, and a republication by Epoch is not treated as an independent retest. The source file has no update time for the full leaderboard.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

## Contact

### 公开工作邮箱

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 官方反馈

https://github.com/yhenon/surface-evolver-llm-eval/issues

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 公开社区

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 隐私边界

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## Original files

### 源站PDF

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### PDF SHA-256

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### PDF bytes

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Folder

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Official introduction/protocol"
    "url": "https://yhenon.github.io/surface-evolver-llm-eval/"
  }
  {
    "type": "Opened primary material"
    "url": "https://github.com/yhenon/surface-evolver-llm-eval"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json"
    "accessed": "2026-11-08"
  }
]
```

[Source 1](https://github.com/yhenon/surface-evolver-llm-eval) (accessed 2026-11-08); [Source 2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

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

[Source 1](https://github.com/yhenon/surface-evolver-llm-eval) (accessed 2026-11-08); [Source 2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json) (accessed 2026-11-08)
