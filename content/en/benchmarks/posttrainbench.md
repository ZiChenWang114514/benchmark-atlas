# PostTrainBench

> Benchmark Constitution, verification 2026-11-08. Unknowns remain "Unverified"; an access date is not an experiment date.

PostTrainBench evaluates whether an agent can actually improve a base model within a limited GPU budget and a limited time, outputting post-training weights rather than answering the test questions directly. The six-target protocol of the current v1.2, the solutions and trajectories of the old seven targets, different CLIs, and results that include model fallback each have their own boundary, and they cannot be written as one unconditional score of model ability.

Sources: [Original description](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08); [Results evidence](https://posttrainbench.com/scores-v1.2.js) (accessed 2026-11-08); [Results evidence](https://posttrainbench.com/config.js) (accessed 2026-11-08)

## Basic information

### Short name

PostTrainBench

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Full name

PostTrainBench

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Benchmark version

v1.2

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Paper version

arXiv v2 (2026-03-11 00:55:40 ); distinct from benchmark v1.2.

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### Release date

First submission of the paper: 2026-03-10 02:18:00; benchmark v1.2 was released separately on 2026-09-30, and the v1.2 date is not treated as the benchmark’s first publication.

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08); [2](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Section

Code

Note: Filed under one main section. That filing does not limit coverage of other disciplines.

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### Field tags

[]（源记录为空；不据此认定官方不存在）

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### 许可与适用范围

The LICENSE of the code repository is MIT; the trajectory data that the author organization PostTrainBench-Trajectories publishes on HF are Apache-2.0. The four base models and the downstream data still each follow their original license.

Sources: [1](https://raw.githubusercontent.com/aisa-group/PostTrainBench/main/LICENSE) (accessed 2026-11-08); [2](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2603.08640

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Code repository

https://github.com/aisa-group/PostTrainBench

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### 数据地址

https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories

Note: Agent trajectories made public by the official author organization, not a unified re-release of the original test questions of the 6 downstream benchmarks.

Sources: [1](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md) (accessed 2026-11-08)

### Official homepage

https://posttrainbench.com/

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### Paper title

PostTrainBench: Can LLM Agents Automate LLM Post-Training?

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

## Origin and maintenance

### 发起与机构归属

Author team of ELLIS Institute Tübingen, MPI for Intelligent Systems, Tübingen AI Center, University of Tübingen, and Thoughtful Lab

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 合作关系

Affiliations of the paper's authors include ELLIS Institute Tübingen, MPI for Intelligent Systems, Tübingen AI Center, University of Tübingen, and Thoughtful Lab; funders, and later parties who reported external results, are listed separately.

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

### Authors

- Ben Rank
- Hardik Bhatnagar
- Ameya Prabhu
- Shira Eisenberg
- Karina Nguyen
- Matthias Bethge
- Maksym Andriushchenko

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### Current maintainer

PostTrainBench team

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 资助与支持

Support from Thoughtful. AP/MB received support from BMBF FKZ16IS24085B and from Coefficient Giving, funded by the Good Ventures Foundation. MA received Coefficient Giving. HB received Digital Europe OpenEuroLLM101195233. HB/BR received support from IMPRS-IS. Modal for Academics provided compute credits (paper acknowledgments).

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

## Design goals

### Abilities measured

Data, training, and experimental workflows are built autonomously, so as to improve the target capabilities of a given small base LLM.

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 设计背景与适用边界

Software-engineering ability does not directly represent autonomous AI research and development; the benchmark requires an agent, within fixed hardware and time, to choose data and a training plan on its own, submit real post-training weights, and undergo review for contamination and weight substitution.

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Four base models are combined with six target benchmarks (v1.2): AIME2025, Arena Hard Writing, GPQA Main, GSM8K, HealthBench Easy, and HumanEval. The HF trajectory card still lists the historical BFCL, and the current six-benchmark protocol cannot be rolled back on that basis.

Sources: [1](https://github.com/aisa-group/PostTrainBench) (accessed 2026-11-08); [2](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08); [3](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md) (accessed 2026-11-08)

### 构建者背景

An author team in machine-learning and AI-safety research. Data curation and training experiments are arranged automatically through a terminal agent, and the benchmark designers do not prescribe a post-training strategy that every agent must use.

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08); [2](https://github.com/aisa-group/PostTrainBench) (accessed 2026-11-08)

### Review process

Independent checks of data contamination, API use, consultation of historical PostTrainBench trajectories, and model identity.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Quality control

v1.2 isolates the HumanEval scoring process, removes trust-remote-code, and uses a three-vote majority for the contamination judge.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### 去污染与泄漏边界

Deriving training data from specific test items is prohibited; the same n-gram tool is provided; runs that violate the rule use the base-model score.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

## Data format

### Size

4 base models × 6 target benchmarks (v1.2); the 4×7 of the old paper and old page does not represent the current protocol.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### 题型与交付物

What is submitted is the trained weights final_model, rather than downstream test answers submitted directly.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Modalities

- 代码
- 训练数据
- 模型权重

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Languages

Instructions for the public tasks are in English, and the submissions are training scripts, data processing, and model weights; the language and task properties of the six downstream benchmarks follow each benchmark’s own protocol. The suite is not claimed to cover only a single language.

Sources: [1](https://github.com/aisa-group/PostTrainBench) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

### Difficulty

Automatic post-training under a limited compute budget of 10 hours per run and a single H100; four base models at the 1.7B–4B scale, aimed at mathematics, general reasoning, writing, medicine, and code. What is limited is the training budget, not a difficulty banding of multiple-choice questions.

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08); [2](https://github.com/aisa-group/PostTrainBench) (accessed 2026-11-08); [3](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Public and hidden splits

The agent must not train on test items; the specific public and hidden scope of each downstream benchmark follows its protocol.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

## Evaluation

### Metrics

A reweighted average of six benchmarks on four base models; the weights are normalized by the reciprocal of the instruct-base performance difference.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### Scoring

The final AIME evaluation uses 5 seeds, GSM8K, GPQA, and HumanEval use 3 seeds, and ArenaHard and HealthBench use 1 seed; a violation is replaced by the base score.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### 提示与运行设置

10 hours and one H100 per run; the terminal and the network may be used; Reprompted is listed separately.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### 评测脚本

aisa-group/PostTrainBench; v1.2 adds a Harbor adapter.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

### 可比性提醒

Dimensions, HumanEval scoring, and the judge all change between v1.1 and v1.2; the H20 results and the different CLIs in the Kimi release post are not placed directly on the same ranking as the official H100 leaderboard.

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 数据版本与更新

```json
{
 "version": "v1.2"
 "evidence_2026_h2": [
 {
 "url": "https://posttrainbench.com/blog/posttrainbench-1-2/"
 "date": "2026-09-30"
 "note": "A new version was released and frontier models were added."
 }
 {
 "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
 "date": "2026-09-09"
 "note": "Epoch reviewed v1.1 as Verified; this does not automatically extend to certification of v1.2."
 }
 ]
}
```

Sources: [1](https://posttrainbench.com/blog/posttrainbench-1-2/) (accessed 2026-11-08); [2](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks) (accessed 2026-11-07)

### 论文修订记录

```json
{
 "arxiv": [
 {
 "version": "v1"
 "submitted_at": "2026-03-10 "
 }
 {
 "version": "v2"
 "submitted_at": "2026-03-11 "
 }
 ]
 "benchmark_release_note": "v1.2 removes BFCL, fixes scoring and isolation, and adds multiple seeds and majority vote; the homepage still describes seven benchmarks, and the explicit v1.2 changes together with scores-v1.2.js are the current basis."
}
```

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 饱和程度

The highest entry recorded in the current official v1.2 aggregate is Fable5.1 at 44.65 (std2.72, n2), including the Opus5 GPQA fallback noted by the official source; this is a weighted downstream score, not a post-training success rate. The 23.2/51.1 of the old 7 benchmarks in the original paper is not used directly as a v1.2 comparison.

Sources: [1](https://posttrainbench.com/scores-v1.2.js) (accessed 2026-11-08); [2](https://posttrainbench.com/config.js) (accessed 2026-11-08); [3](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

### 争议与已知问题

Recorded patterns of violation include training on the test set, substitution of ready-made instruct weights, synthesis of data through an API without permission, and inspection of historical trajectories. The current v1.2 removes BFCL and strengthens isolation; the historical HF trajectory card still lists seven benchmarks, and the data grant Apache2.0 also differs from MIT for the code. The Fable5/5.1 GPQA result is a mixed fallback, and its source must be shown.

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08); [2](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md) (accessed 2026-11-08); [3](https://posttrainbench.com/config.js) (accessed 2026-11-08)

### 衍生与后续使用

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (date the web page was accessed; dates of historical results are kept separately).

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### 官方结果入口

https://posttrainbench.com/

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### 第三方入口

https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks

Sources: [1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks) (accessed 2026-11-07)

### 分赛道结果

- {"model": "Fable 5.1", "score": 44.65, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "fable-5.1", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 2.72, "n": 2, "provenance_note": "The official annotation marks 5 GPQA Main units as falling back to Opus 5.", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 1}
- {"model": "Opus 5.5", "score": 43.8, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-5.5-max", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 3.0, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 2}
- {"model": "GPT 6 (Astra)", "score": 41.88, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-6-astra", "scaffold": "Codex CLI", "reasoning_effort": "Max", "std": 0.76, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 3}
- {"model": "GPT 6.1 (Sol)", "score": 38.79, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-6.1-sol", "scaffold": "Codex CLI", "reasoning_effort": "Max", "std": 0.36, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 4}
- {"model": "Fable 5", "score": 37.27, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "fable-5", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 1.65, "n": 2, "provenance_note": "The official annotation states that GPQA Main uses an Opus4.8 Max fallback.", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 5}
- {"model": "GLM 5.3 Flash", "score": 36.79, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "glm-5.3-flash", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 0.11, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 6}
- {"model": "Opus 5", "score": 35.66, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-5", "scaffold": "Claude Code", "reasoning_effort": "Official configuration not itemized", "std": 2.62, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 7}
- {"model": "GLM 5.3", "score": 34.52, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "glm-5.3", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 3.39, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 8}
- {"model": "Kimi K3", "score": 31.48, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "kimi-k3", "scaffold": "Claude Code", "reasoning_effort": "Official configuration not itemized", "std": 0.63, "n": 3, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 9}
- {"model": "GPT 5.6 (Sol)", "score": 31.01, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-5.6-sol", "scaffold": "Codex CLI", "reasoning_effort": "Max", "std": 0.2, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 10}
- {"model": "Opus 4.8", "score": 31.0, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-4.8-max", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 3.0, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 11}
- {"model": "Opus 4.8", "score": 30.66, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-4.8", "scaffold": "Claude Code", "reasoning_effort": "High", "std": 3.04, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 12}
- {"model": "GLM 5.2", "score": 30.4, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "glm-5.2", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 1.46, "n": 3, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 13}
- {"model": "Opus 4.7", "score": 24.34, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-4.7", "scaffold": "Claude Code", "reasoning_effort": "xHigh", "std": 1.63, "n": 3, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 14}
- {"model": "GPT 5.5", "score": 23.87, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-5.5-xhigh", "scaffold": "Codex CLI", "reasoning_effort": "xHigh", "std": 0.48, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 15}
- {"model": "Grok 4.5", "score": 22.62, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "grok-4.5-high", "scaffold": "Cursor CLI", "reasoning_effort": "High", "std": 0.94, "n": 2, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 16}
- {"model": "Gemini 3.1 Pro", "score": 18.11, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gemini-3.1-pro", "scaffold": "OpenCode", "reasoning_effort": "Official configuration not itemized", "std": 1.68, "n": 3, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 17}
- {"model": "GPT 5.4", "score": 17.76, "track": "Official run/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-5.4-high", "scaffold": "Codex CLI", "reasoning_effort": "High", "std": 1.8, "n": 3, "provenance_note": "", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 18}
- {"model": "Locus / Opus 5", "score": 41.66, "track": "Official inclusion/external-run review/v1.2", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "locus", "scaffold": "Intology", "reasoning_effort": "See the official description for configuration", "std": 0.82, "n": 3, "provenance_note": "Run by Intology and reviewed by PostTrainBench; not run by the official team itself.", "result_type": "The current official JS aggregate; no unified update time is given", "rank": 1}

Sources: [1](https://posttrainbench.com/scores-v1.2.js) (accessed 2026-11-08); [2](https://posttrainbench.com/config.js) (accessed 2026-11-08)

### 覆盖边界

All 19 aggregate configurations in scores-v1.2.js are included in full. 18 official runs and 1 external Locus review result are on separate tracks. std/n, the CLI, and reasoning effort are retained. The Fable5/5.1 mixed GPQA fallback is marked explicitly. They are not ranked together with the old v1/v1.1, the vendor H20 experiment, or the official instruct reference. The data asset has no unified update date, and only the actual access date is recorded.

Sources: [1](https://posttrainbench.com/scores-v1.2.js) (accessed 2026-11-08); [2](https://posttrainbench.com/config.js) (accessed 2026-11-08)

## Contact

### 公开项目邮箱

- maksym.andriushchenko@tue.ellis.eu

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 公开反馈渠道

https://github.com/aisa-group/PostTrainBench/issues

Sources: [1](https://github.com/aisa-group/PostTrainBench) (accessed 2026-11-08)

### 官方社交渠道

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### 联系方式收录原则

Benchmark Constitution includes only project contact channels that the paper or the official site has made public, and it does not collect private information; this is not a certification of an external site’s privacy policy.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08)

## Original files

### 既存论文原件

Unverified

Note: This group is local research only and was not uploaded.

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### 原始PDF地址

https://arxiv.org/pdf/2603.08640

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)

### 下载SHA-256

823f11de21206c9ba5be0531bee62f1d29d97cfeb5c8e9a6c90a2256f1f948bc

Note: Checksum of the bytes downloaded on 2026-11-08. Nothing was overwritten or uploaded, so this does not establish that an existing original is the same version.

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

### 下载字节数

```json
366334
```

Sources: [1](https://arxiv.org/pdf/2603.08640) (accessed 2026-11-08)

### 既存文件夹

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

### Other documents

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://posttrainbench.com/) (accessed 2026-11-08)

## Changelog

Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2603.08640) (accessed 2026-11-08)
