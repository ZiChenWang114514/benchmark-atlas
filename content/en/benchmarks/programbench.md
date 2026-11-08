# ProgramBench

> In-depth verification: 2026-11-08. The access date is not the publication date or the experiment run date; unknowns are retained, and "Not disclosed" is not inferred.

ProgramBench requires an agent to build, from scratch, a software project whose behavior matches, using only the executable program and its documentation. The evaluated agent cannot see the original source code, cannot connect to the network, and cannot decompile. The agent that builds the tests may consult the source code and existing tests, so the permissions of the two stages must be distinguished. The primary metric is the proportion of tasks that pass all hidden tests. The mean test pass rate and the 95% threshold are only auxiliary diagnostics.

Latest review

## Basic information

### Short name

ProgramBench

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Full name

ProgramBench

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Dataset version

A public release set of 200 tasks, with the code and the generated tests released separately; the original program is pinned by the short repository commit in the task directory, rather than a self-assigned v1.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### Paper version

arXiv:2605.03546v1; the abs currently lists only v1.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 发布时间

First release of the paper: 2026-05-05 18:17:02; the PDF cover separately marks May 6, 2026, and the two date conventions are kept apart.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 板块

Code

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Subfields

```json
[
  "Program reconstruction from scratch"
  "Software architecture"
  "Behavioral equivalence test"
  "Code agent"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### License

The evaluation repository is MIT. The metadata of the HF card marks MIT, but inside the tasks the LICENSE and ATTRIBUTION of the original repository are also attached. A generated test may draw on the original tests. A derivative portion under GPL, LGPL, MPL, or a similar license remains bound by that original license. It cannot be said, as a blanket statement, that every task is MIT with no conditions.

[1](https://raw.githubusercontent.com/facebookresearch/ProgramBench/main/LICENSE)（访问 2026-11-08）；[2](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2605.03546

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 代码

https://github.com/facebookresearch/ProgramBench

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### Dataset

https://huggingface.co/datasets/programbench/ProgramBench-Tests

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/facebookresearch/ProgramBench/main/README.md)（访问 2026-11-08）

### Official homepage

https://programbench.com

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 论文题名

ProgramBench: Can Language Models Rebuild Programs From Scratch?

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## Origin and maintenance

### Initiators

```json
[
  "Meta Superintelligence Labs"
  "Stanford University"
  "Harvard University"
]
```

[1](https://programbench.com)（访问 2026-11-07）

### 合作单位

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Authors

```json
[
  "John Yang"
  "Kilian Lieret"
  "Jeffrey Ma"
  "Parth Thakkar"
  "Dmitrii Pedchenko"
  "Sten Sootla"
  "Emily McMilin"
  "Pengcheng Yin"
  "Rui Hou"
  "Gabriel Synnaeve"
  "Diyi Yang"
  "Ofir Press"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### Maintainer

The facebookresearch/ProgramBench team; the public maintenance contacts on HF are John Yang and Kilian Lieret.

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/facebookresearch/ProgramBench/main/README.md)（访问 2026-11-08）

### Funders

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## Design goals

### 目标能力

Given only an executable program and documentation, design the architecture, choose a language, and implement a behaviorally equivalent program from scratch.

[1](https://programbench.com)（访问 2026-11-07）

### 相对既有评测的缺口

No function signatures, class skeletons, or preset directories are provided, which distinguishes it from local bug fixing and fill-in whole-repository generation.

[1](https://programbench.com)（访问 2026-11-07）

## Construction

### 题目与标签来源

Executable programs and documentation from 200 open-source projects. The stages must be kept apart: the agent that builds the tests may consult the original source code and the existing tests; the reconstruction agent under evaluation cannot access that source code or those tests.

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 出题/标注背景

The authors are from Meta Superintelligence Labs, Stanford, and Harvard; the tests are generated in an agent-driven way, and the 200 questions were not each originally written by humans, question by question.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### Review process

The agent explores the original program, coverage-guided fuzzing generates behavioral assertions, and existing behavioral tests are collected.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### Quality control

A static linter screens out weak assertions; tests that do not stably pass the original program, or that pass a dummy program, are removed.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 去污染与隔离

An offline sandbox, in which the original binary may only be executed; decompilation, retrieval of source, and wrapping the original program are not allowed. Public availability of the original repository creates a potential memorization risk.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## Data format

### Size

200 tasks; the version in the paper has 248,853 test functions in all.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### Question types

Generated from complete source-code projects and build scripts; behavioral tests compare standard output/error, exit codes, and file side effects.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### Modalities

```json
[
  "Program binary"
  "文档"
  "源代码"
  "Terminal interaction"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### Languages

Reference programs: Rust 107, Go 46, C 33, C++ 12, Haskell 1, Java 1; the HF card marks English. The reconstruction model may choose its own implementation language.

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### Difficulty

HF card: 27 easy, 120 medium, 18 hard, and 35 unrated; this is task metadata, not a re-bucketing by the model scores of this run.

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 公开/隐藏划分

200 tasks and AI-generated behavioral tests are publicly released; the tests are hidden during one evaluated agent run. Public release does not mean the assertions can be viewed at inference time.

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

## Evaluation

### Metrics

Fully Resolved/Resolved: every hidden behavioral test passes; Almost Resolved: at least 95% of the tests pass; Raw Pass Rate: the mean of the pass rates of the tests inside a task.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 判分

After the submitted implementation is compiled, behavioral tests compare it with the original program; scoring does not rely on subjective LLM judgment, and finite tests cannot prove equivalence on all inputs.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 提示/推理设置

mini-SWE-agent, 1000 steps, 6 hours, offline cleanroom; Vals unifies the bash tool and the sandbox.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 官方实现

The official code entry point is facebookresearch/ProgramBench, and the paper gives the data-construction and evaluation procedure.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 可比性边界

The samples and the run results from the official website on 2026-10-22 and from Vals on 2026-11-05 are kept separate; Fully Resolved is not the Raw Pass Rate, and it is not the 95% test threshold.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## Current status

### 核验日

2026-11-08

[1](https://programbench.com)（访问 2026-11-08）

### 本次版本快照

```json
{
  "version": "200 public tasks and ProgramBench-Tests (access-date snapshot; no semantic version was invented)"
  "heat_confidence": "A"
  "evidence_2026_h2": [
    {
      "url": "https://programbench.com"
      "date": "2026-10-22"
      "note": "Update date stated on the official leaderboard."
    }
    {
      "url": "https://www.vals.ai/benchmarks/programbench"
      "date": "2026-11-05"
      "note": "Update date stated on the Vals independent-evaluation leaderboard."
    }
  ]
}
```

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://programbench.com)（访问 2026-11-08）

### Paper revisions

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-05-05"
    "timezone": ""
  }
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### Saturation

On 2026-10-22 the highest Fully Resolved on the official site is 18.5% and Almost Resolved is 70.5%; on 2026-11-05 the highest Fully Resolved on Vals is 18.50%. Passing every test remains the strict primary metric, and a higher Raw Pass Rate cannot be treated as fully resolved.

[1](https://programbench.com)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

### 污染/限制/争议

The original repository is public, so there is a risk of memorization; the official site reports a cross-language implementation ablation and continues to monitor it. Disconnecting the network, execute-only permission, and a ban on decompilation are used to block copying of the source code, and they cannot prove that the training corpus never saw the project. A limited set of tests cannot prove that behavior is equivalent for every input; the tests may be constrained by the copyleft terms of the original repository.

[1](https://programbench.com)（访问 2026-11-08）；[2](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 衍生与相关版本

The official site cross-recommends SWE-sweep, but this is not used to treat it as a new version of ProgramBench or to split individual tasks into independent benchmarks.

[1](https://programbench.com)（访问 2026-11-08）

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not the experiment run date)

[1](https://programbench.com)（访问 2026-11-08）

### 官方结果入口

https://programbench.com

[1](https://programbench.com)（访问 2026-11-07）

### 第三方入口

https://www.vals.ai/benchmarks/programbench

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| Official / 200 tasks / mini-SWE-agent | 1 | [Claude Opus 5.5 (xhigh)](https://programbench.com) | 18.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 2 | [Claude Fable 5.1 (xhigh)](https://programbench.com) | 9.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 3 | [Muse Wonder Full](https://programbench.com) | 8.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 4 | [Muse Wonder (xhigh)](https://programbench.com) | 5.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 5 | [GPT 6 Astra (max)](https://programbench.com) | 5.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 6 | [Claude Opus 5 (xhigh)](https://programbench.com) | 4.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 7 | [Muse Spark 1.3 (max)](https://programbench.com) | 2.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 8 | [Muse Spark 1.3 (xhigh)](https://programbench.com) | 1.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 9 | [GPT-5.6 Sol (xhigh)](https://programbench.com) | 1.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 10 | [GPT 5.5 (xhigh)](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 11 | [GPT 5.5 (high)](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 12 | [Gemini 3.6 Flash](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 13 | [GPT-5.6 Sol](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 14 | [Claude Opus 4.8 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 15 | [GLM-5.2](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 16 | [Gemini 3.7 Flash](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 17 | [Muse Spark 1.2 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 18 | [Claude Opus 4.7 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 19 | [Muse Spark 1.1 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 20 | [Gemini 3.5 Flash](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 21 | [Claude Opus 4.7](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 22 | [Claude Opus 4.6](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 23 | [GPT 5.5](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 24 | [Claude Sonnet 4.6](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 25 | [GPT 5.4](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 26 | [Gemini 3.1 Pro](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 27 | [Gemini 3 Flash](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 28 | [Claude Haiku 4.5](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 29 | [GPT 5.4 mini](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Official / 200 tasks / mini-SWE-agent | 30 | [GPT 5 mini](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 1 | [Claude Opus 5.5](https://www.vals.ai/benchmarks/programbench) | 18.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 2 | [Claude Fable 5.1](https://www.vals.ai/benchmarks/programbench) | 7.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 3 | [Claude Sonnet 5.5](https://www.vals.ai/benchmarks/programbench) | 6.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 4 | [GPT-6 Astra](https://www.vals.ai/benchmarks/programbench) | 5.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 5 | [GPT-6.1 Sol](https://www.vals.ai/benchmarks/programbench) | 3.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 6 | [Claude Opus 5](https://www.vals.ai/benchmarks/programbench) | 3.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 7 | [Gemini 4 Argon](https://www.vals.ai/benchmarks/programbench) | 2.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 8 | [Claude Haiku 5.5](https://www.vals.ai/benchmarks/programbench) | 2.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 9 | [Muse Spark 1.3 Max](https://www.vals.ai/benchmarks/programbench) | 2.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 10 | [Claude Fable 5](https://www.vals.ai/benchmarks/programbench) | 2.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 11 | [GPT-6 Sol](https://www.vals.ai/benchmarks/programbench) | 2.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 12 | [Kimi K3](https://www.vals.ai/benchmarks/programbench) | 2.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 13 | [GPT-5.6 Sol](https://www.vals.ai/benchmarks/programbench) | 1.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 14 | [GLM 5.3](https://www.vals.ai/benchmarks/programbench) | 1.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 15 | [Grok 4.6](https://www.vals.ai/benchmarks/programbench) | 1.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 16 | [Claude Opus 4.8](https://www.vals.ai/benchmarks/programbench) | 1.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 17 | [Gemini 3.8 Flash](https://www.vals.ai/benchmarks/programbench) | 1.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 18 | [Grok 4.7](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 19 | [MiMo V2.6 Flash](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 20 | [DeepSeek V4.1 Flash](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 21 | [GPT-5.6 Terra](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 22 | [Muse Spark 1.3](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 23 | [MiMo V2.6 Pro](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 24 | [Inkling 2 Small](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 25 | [GPT 5.5](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 26 | [GLM 5.2](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 27 | [GPT-6 Luna](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 28 | [Wonder Full](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 29 | [GPT 5.4 (high)](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 30 | [Muse Spark 1.2](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 31 | [Claude Sonnet 4.6](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 32 | [Inkling Small](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 33 | [Hy4 Preview](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 34 | [DeepSeek V4 Pro 0813](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 35 | [Claude Sonnet 5](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 36 | [Qwen 3.8 Max](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 37 | [Gemini 3.7 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 38 | [Claude Opus 4.7](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 39 | [GPT-5.6 Luna](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 40 | [DeepSeek V4 Flash 0731](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 41 | [GPT 5.4 (xhigh)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 42 | [GLM 5.3 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 43 | [Grok 4.5](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 44 | [GPT 5.4 Mini](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 45 | [Gemini 3.6 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 46 | [Muse Spark 1.1](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 47 | [Gemini 3.5 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 48 | [GLM 5.1](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 49 | [Gemini 3.1 Pro Preview (02/26)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 50 | [Qwen 3.6 Plus](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 51 | [Qwen 3.8 27B](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 52 | [Kimi K2.7 Code](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 53 | [Kimi K2.6](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 54 | [Nemotron 3 Ultra](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 55 | [DeepSeek V4](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 56 | [Gemini 3 Flash (12/25)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 57 | [Gemini 3.5 Flash Lite](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 58 | [Claude Haiku 4.5 (Thinking)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 59 | [Grok 4.3](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 60 | [Nemotron 3.5 Lightning](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 61 | [Laguna XS.2](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 62 | [Inkling](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 63 | [Laguna M.1](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 64 | [Gemini 3.1 Flash Lite Preview](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals independent retest / 200 tasks / mini-SWE-agent. | 65 | [MiniMax-M2.7](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals raw test pass-rate diagnostic table | — | [Claude Opus 5.5](https://www.vals.ai/benchmarks/programbench) | 87.0 | Raw Pass Rate (%) | 2026-11-05 |
| Vals raw test pass-rate diagnostic table | — | [GPT-6 Astra](https://www.vals.ai/benchmarks/programbench) | 85.4 | Raw Pass Rate (%) | 2026-11-05 |
| Vals raw test pass-rate diagnostic table | — | [GPT-6.1 Sol](https://www.vals.ai/benchmarks/programbench) | 85.3 | Raw Pass Rate (%) | 2026-11-05 |
| Vals raw test pass-rate diagnostic table | — | [Gemini 4 Argon](https://www.vals.ai/benchmarks/programbench) | 83.7 | Raw Pass Rate (%) | 2026-11-05 |
| Vals raw test pass-rate diagnostic table | — | [Claude Fable 5.1](https://www.vals.ai/benchmarks/programbench) | 82.7 | Raw Pass Rate (%) | 2026-11-05 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://programbench.com)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

### 覆盖与限制

Of the 31 rows on the official site, 30 have a numeric rank. The full Vals leaderboard has 65 rows, and a diagnostic table of 5 rows of Raw Pass Rate is also included. Independent leaderboards are kept separate, and the same 18.5% is not used to assert that the run is the same. Almost Resolved on the official site is a proportion; figures such as 130/37 in the Vals diagnostic table are counts of tasks, not 130% or 37%.

[1](https://programbench.com)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

## Contact

### 项目公开邮箱

```json
[
  "johnby@meta.com"
  "klieret@meta.com"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### GitHub反馈

https://github.com/facebookresearch/ProgramBench/issues

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 官方社交

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 隐私边界

Only the project email and the Issues made public on the HF card and in the paper are recorded; private contact details are not inferred.

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

## Original files

### 原始PDF

https://arxiv.org/pdf/2605.03546

> The PDF entry corresponding to the text of the official paper; it was not downloaded, so the hash and the byte count are Unverified.

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### SHA-256

87c67873f06f48044ef3a1bcd5bed21be2c90d92090bfb3b73b6ca7b9b13781c

[1](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### PDF bytes

2568568

[1](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### Folder

Unverified

> The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Official introduction/protocol"
    "url": "https://www.vals.ai/benchmarks/programbench"
  }
]
```

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Paper PDF

Unverified

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

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

[1](https://programbench.com)（访问 2026-11-08）
