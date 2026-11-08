# SRE Bench（SRE-Bench）

> Benchmark Constitution, in-depth review 2026-11-08. Verified to exist; a recently popular newly created entry, with marks retained on fields that have not been verified; trending: A

SRE-Bench evaluates the ability to recover program semantics from an unknown binary. It is not site reliability engineering. 19 private programs are built into 262 binary instances, with 6 deterministically verifiable tasks per instance. The most important constraint on reading the scores is the denominator: the paper computes conditional scores only on gradable runs, while Vals includes all 262 instances. Multi-attempt scores with the internal guardrails turned off are a third set of conditions.

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)

## Basic information

### Short name

SRE Bench（SRE-Bench）

> Here SRE means software reverse engineering, not site reliability engineering.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Full name

The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Benchmark version

262 instances/1,572 tasks as defined by paper v2; there is no separate semantic version number for the dataset.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Paper version

v2 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Release date

2026-08-11 (arXiv v1 submission)

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Section

Code

> Benchmark Constitution editorial filing. Vals places it under Cyber.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 领域

```json
[
  "Binary reverse engineering"
  "Cybersecurity"
]
```

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 许可与适用范围

Unverified

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2608.11469

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Code

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 数据

Not disclosed

> The paper states that 19 programs are private.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Official entry

https://www.vals.ai/benchmarks/srebench

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Paper title

The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

## Origin and maintenance

### Initiators

The paper’s author team includes Columbia University and others, and Vals AI took part in building the benchmark and in hosting it; affiliations include UC Berkeley, UCLA, Tufts, and authors from industrial research.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 合作/参与机构

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Authors

Jeremy Spence、Nicholas Assaderaghi、Feng Xiao、Jinhao Zhu、Nikil Ravi、Xiangyu Qi、Matthew Jagielski、Raluca Ada Popa、Eric Wallace、Guannan Wei、Yangruibo Ding、Zhuo Zhang

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Maintainer

Vals AI (current leaderboard maintenance)

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Funders

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## Design goals

### Abilities measured

Understand real-scale binary programs with anti-analysis protection, without source code (protocols, firmware, games, file-format recovery, and malware).

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### Design background

Existing RE-related benchmarks depend on existing CTFs or toy programs, are easily contaminated by memorization, and have unrealistic scale and protections.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## Construction

### Question sources

Reverse-engineering experts built 19 internal programs from scratch (about 16.9K lines of code on average), together with 44 in-house anti-analysis mechanisms (a protection suite of 27K lines of code).

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 出题者背景

The reverse-engineering experts average 6 years of experience, with a total of more than 5,000 expert hours. The 19 programs were each implemented independently from private design specifications; they share no code and are not based on public projects.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Review process

Each program's private reference solution must score 6/6, as a gate for solvability and regression. Opus 4.8 and GPT-6-Astra were used for an adversarial reward-hacking audit. After readable strings of hidden behavior were found, they were removed and a build regression check was added.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Quality control

The objectives, the scoring infrastructure, and the protection suite are all built internally; scoring code, reference solutions, and development artifacts are removed from the agent container, and no scoring feedback is provided during the run; domain-level tasks are verified by a deterministic server, by replay, or by a sandbox.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 污染控制

Built entirely from scratch in a clean-room, with the programs kept private, so that they do not appear in training data

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## Data format

### 题量

19 programs → 262 binary instances → 1,572 deterministic scoring tasks (6 per instance)

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 任务形式

Agent reverse-engineering tasks in a shell environment, with deterministic verification

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Modalities

```json
[
  "Binary file"
  "Text/command line"
]
```

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Languages

Implementation languages of the target programs: C, C++, Rust, and Go; the firmware does not include Go. The full distribution of natural language in the interactions and the questions is Unverified.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Difficulty

19 programs average 16,915.8 lines of code. 44 protection primitives form 8 presets. There are 262 binary instances, and each instance has 6 deterministic subtasks. In the paper's public-API evaluation, the best result fully solves 149 of the 181 instances that have already been scored. This is not a conditional success rate of 149/262.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### Public and hidden splits

Private (Vals labels it Proprietary)

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## Evaluation

### Metrics

Fully Solved: an instance counts as solved only when all 6 items are correct. Capability Score: the proportion of the 6 items completed on each instance. Table 4 of the paper averages only the instances that can be scored; Vals Accuracy includes all 262 instances and counts a failure as 0. The total task inventory is 262×6=1,572, which is not the fixed denominator of the conditional average in the paper.

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

### 评分

Score, Solved, and Zeros in Table 4 of the paper are computed only on gradable runs. Refusals and context failures do not enter the denominator. The Vals method states explicitly that all 262 instances are the denominator, and that a failure is scored as zero. The two sets of percentages cannot be compared directly.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 运行设置

The public setting in the paper: mini-SWE-agent, the highest reasoning level, at most 500 model steps and 6 hours, and the standard RE toolbox. The internal unconstrained setting: Codex and Claude Code, with cyber safeguards turned off and no budget cap.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 评测工具

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### Comparability

The conditional scores on gradable runs in the paper and the Vals scores on all 262 instances have denominators that are explicitly different; turning the safety guardrails off internally, imposing no budget cap, and making several attempts with Codex or Claude Code are a further protocol of their own, and the results cannot be ranked together.

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "待核实"
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/srebench"
      "date": "2026-11-05"
      "organization": "Vals AI"
      "note": "The current method and leaderboard pages show measured results for multiple frontier models; updated November 5, a binary reverse-engineering comprehension test of 37 models. It must not be mistranslated as a site-reliability engineering benchmark."
    }
    {
      "url": "https://www.vals.ai/benchmarks"
      "date": "2026-11-05"
      "organization": "Vals AI"
      "note": "Catalog card: Cyber Proprietary SRE Bench Updated: 11/5/2026 Models Tested: 37 Can AI agents work out what a real-world binary does without its source code? Top Models 1 GPT-6 Astra 2 GPT-6.1 Sol 3 Gemini 4 Argon View Details"
    }
    {
      "url": "https://openai.com/index/gpt-6-astra/"
      "date": "2026-11-07"
      "organization": "OpenAI"
      "note": "The official-release evaluation table for GPT-6 Astra explicitly reports SRE Bench, as evidence of recent vendor adoption."
    }
  ]
  "trending": {
    "heat_confidence": "A"
    "summary": "The binary reverse-engineering evaluation released in August is now on the official GPT-6 Astra release table, and in November Vals still updates a 37-model leaderboard."
  }
}
```

> Recent popularity evidence is taken from candidate studies and reopened pages; grade A: adopted independently by multiple frontier laboratories or evaluation organizations.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks)（访问 2026-11-07）；[来源3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-08-12"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2026-10-01"
    "timezone": ""
  }
]
```

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 饱和与能力边界

The highest Accuracy currently on Vals is 56.87%; the internal unconstrained configuration in the paper, GPT-6-Astra Max, reaches 88.0% pass@1 and 99.2% pass@4 (4 attempts). The latter does not measure the ability to select the correct candidate without a private grader, and it does not mean that a single evaluation through the public API is saturated.

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)

### 风险与争议

The paper explicitly withholds the binaries and the task instances in order to maintain resistance to contamination, and it provides a controlled evaluation service; coverage of the 19 programs is limited, and their average scale is still smaller than that of large real software. “contamination-free” is a design claim by the authors and does not mean that an independent audit has shown every future training run to be free of leakage.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 系列与衍生关系

Here SRE means a binary reverse-engineering evaluation, not Site Reliability Engineering. It differs from behavioral reimplementation in ProgramBench, and the latter provides known public programs and their documentation.

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)

### Official entry

https://www.vals.ai/benchmarks/srebench

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 独立来源

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 分来源与协议结果

#### Vals current / denominator 262

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra | 56.87 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 2 | GPT-6.1 Sol | 50.76 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 3 | Gemini 4 Argon | 44.27 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 4 | Claude Opus 5.5 | 33.59 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 5 | Daybreak Blue | 31.68 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 6 | GPT-5.6 Sol | 30.53 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 7 | GPT-6 Sol | 30.53 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 8 | Claude Sonnet 5.5 | 30.15 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 9 | Kimi K3.1 Pro | 27.1 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 10 | Claude Fable 5.1 | 22.9 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 11 | Claude Opus 5.5 (CVP) | 21.76 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 12 | Claude Opus 5 | 12.21 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 13 | Wonder Full | 11.83 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 14 | Gemini 3.8 Flash | 11.07 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 15 | GPT-5.6 Terra | 9.54 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 16 | GLM 5.3 | 9.16 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 17 | Claude Haiku 5.5 | 5.72 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 18 | Gemini 3.7 Flash | 4.58 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 19 | MiMo V2.6 Flash | 4.2 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 20 | Grok 4.7 | 3.82 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 21 | GPT 5.5 | 3.82 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 22 | Muse Spark 1.3 Max | 3.82 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 23 | MiMo V2.6 Pro | 3.05 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 24 | GPT-6 Luna | 2.67 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 25 | Hy4 Preview | 2.29 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 26 | DeepSeek V4 Pro 0813 | 1.91 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 27 | Inkling 2 Small | 1.91 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 28 | GPT-5.6 Luna | 1.53 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 29 | DeepSeek V4.1 Flash | 0.76 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 30 | GLM 5.3 Flash | 0.76 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 31 | Grok 4.5 | 0.76 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 32 | Claude Sonnet 5 | 0.38 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 33 | Step 5 Preview | 0.38 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 34 | GLM 5.2 | 0.0 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 35 | Muse Spark 1.2 | 0.0 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 36 | Gemini 3.1 Pro Preview (02/26) | 0.0 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |
| 37 | Inkling | 0.0 | Accuracy (%); all 262 instances | {"source_date":"2026-11-05"} |

#### paper v2 Table 4 public / graded-only

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | gpt-6-astra | 5.55 | mean successful tasks per graded binary (0–6) | {"n_graded":181,"total_instances":262,"fully_solved_percent_of_graded":82.3} |
| — | gpt-5.6-sol | 3.69 | mean successful tasks per graded binary (0–6) | {"n_graded":254,"total_instances":262,"fully_solved_percent_of_graded":31.5} |
| — | claude-fable-5.1 | 2.58 | mean successful tasks per graded binary (0–6) | {"n_graded":223,"total_instances":262,"fully_solved_percent_of_graded":26.9} |
| — | claude-opus-5 | 1.91 | mean successful tasks per graded binary (0–6) | {"n_graded":256,"total_instances":262,"fully_solved_percent_of_graded":12.5} |
| — | gpt-5.5 | 1.02 | mean successful tasks per graded binary (0–6) | {"n_graded":262,"total_instances":262,"fully_solved_percent_of_graded":3.8} |
| — | deepseek-v4.1-flash | 0.85 | mean successful tasks per graded binary (0–6) | {"n_graded":262,"total_instances":262,"fully_solved_percent_of_graded":0.8} |
| — | grok-4.5 | 0.45 | mean successful tasks per graded binary (0–6) | {"n_graded":218,"total_instances":262,"fully_solved_percent_of_graded":0.9} |
| — | glm-5.2 | 0.21 | mean successful tasks per graded binary (0–6) | {"n_graded":262,"total_instances":262,"fully_solved_percent_of_graded":0.0} |

#### paper v2 Table 11 internal unconstrained Max / pass@1

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | GPT-5.6 Sol | 55.8 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-5.6 Cyber | 56.8 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-6-Astra | 88.0 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | Opus 5.5 | 82.1 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |

#### paper v2 Table 11 internal unconstrained Max / pass@4

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | GPT-5.6 Sol | 68.7 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-5.6 Cyber | 72.5 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-6-Astra | 99.2 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | Opus 5.5 | 98.1 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)

### 覆盖与时效

Accuracy for all 37 Vals models, with a denominator of 262 instances, forms its own track. The 8 models in paper Table 4 record conditional Score and conditional Solved separately, with n_graded stated. Table 11, internal Max pass@1/pass@4, is another track and is not mixed in as a public API leaderboard. The official site's BibTeX says forthcoming, but arXiv v2 is in fact already open. The full arXiv byline and revision history are authoritative.

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)

## Contact

### 公开工作邮箱

```json
[
  "js6721@columbia.edu"
  "41zz@cs.columbia.edu"
]
```

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 官方反馈

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 公开社区

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 隐私边界

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2608.11469

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）

### PDF SHA-256

04416ad347e07e0cb2d4eda5e80fba82bcb3e296ed9ef16b38edbc1a4e5d2905

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）

### PDF bytes

```json
692156
```

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）

### Folder

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Opened primary material"
    "url": "https://arxiv.org/abs/2608.11469"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://www.vals.ai/benchmarks/srebench"
    "accessed": "2026-11-08"
  }
]
```

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

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

[Source 1](https://arxiv.org/abs/2608.11469) (accessed 2026-11-08); [Source 2](https://www.vals.ai/benchmarks/srebench) (accessed 2026-11-08)
