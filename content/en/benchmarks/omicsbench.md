# OmicsBench

> Benchmark Constitution, verification 2026-11-08. Unknowns remain "Unverified"; an access date is not an experiment date.

OmicsBench splits analysis dependencies in omics research into multi-turn DAG tasks, and it observes whether an agent can move forward along preceding results and use feedback to correct errors. A gated protocol with thresholded feedback is not a substitute for single-pass ability without feedback. This page keeps separate the two sets of paper scores for the 14 model and scaffold combinations.

Source: [Original description](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08); [Result evidence](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

## Basic information

### Short name

OmicsBench

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Full name

OmicsBench

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Benchmark version

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Paper version

v1; latest paper date 2026-10-15

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Release date

2026-10-15 (date of the first arXiv version; not an inferred date on which the data went online).

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Section

Biology and medicine

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### Field tags

- Research-scale multi-turn omics analysis

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### 许可与适用范围

Runner and every grader are MIT; the three public tasks and their answers are CC BY 4.0; the attached biological data and the identifier databases still follow the license of each original source.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2610.21074

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Code repository

https://huggingface.co/datasets/gideonshaked/OmicsBench

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### 数据地址

https://huggingface.co/datasets/gideonshaked/OmicsBench

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Official homepage

https://huggingface.co/datasets/gideonshaked/OmicsBench

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Paper title

OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

## Origin and maintenance

### 发起与机构归属

The authors Gideon Shaked and Siddharth Nagisetty are both signed as the Department of Computational Medicine and Bioinformatics at the University of Michigan and as AfterQuery. The record follows the authors' affiliations. One legal person as the sole sponsor is not presumed.

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### 合作关系

- University of Michigan, Department of Computational Medicine and Bioinformatics
- AfterQuery

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### Authors

- Shaked, Gideon
- Nagisetty, Siddharth

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Current maintainer

The release accounts are gideonshaked/OmicsBench and grader-databases.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 资助与支持

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

## Design goals

### Abilities measured

Research-scale, long-horizon multi-turn omics workflows that, across dependent subtasks, produce biological analyses that can be checked automatically.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 设计背景与适用边界

A single prompt cannot reflect the turn-by-turn delegation, dependence on earlier results, and recovery after feedback that occur in real omics research; this benchmark splits the research workflow into multi-turn subtasks with DAG dependencies.

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Published biological research and the corresponding public datasets, split into task DAGs according to the research workflow.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 构建者背景

Curated by graduate-level experts in computational biology; writer/reviewer agents assist, and humans then edit.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Review process

Human experts trained in computational biology at graduate level select the papers and the data; a writer agent drafts the item, a reviewer agent checks whether it is supported and whether it leaks information, with at most three rounds of revision; after an automatic check of format, a human reviews the item and edits it or rejects it.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### Quality control

58 classes of deterministic biology graders and a reference library of entity synonyms; dependencies are checked step by step with a DAG.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 去污染与泄漏边界

94 private tasks control access to the answers, and 3 public tasks serve as examples; publication of the source paper and grader feedback may leave memorization and reward hacking still possible.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

## Data format

### Size

97 tasks, 662 subtasks, and 58 deterministic biological scorers; 3 public and 94 private.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 题型与交付物

Long multi-turn analysis of omics data, with subtasks in a directed acyclic dependency.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Modalities

Omics matrices, tables, code, analysis products, and written results.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Languages

Task examples and the runner documentation are in English, and the analysis tools include Python/R and biological-entity identifiers; multilingual coverage is not inferred.

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08); [2](https://huggingface.co/datasets/gideonshaked/OmicsBench/raw/main/omicsbench_runner/README.md) (accessed 2026-11-08)

### Difficulty

At research scale, not as short questions; dependency chains and iterative analysis are the difficult points.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Public and hidden splits

97 tasks and 662 subtasks; 3 tasks and their answers are public, and 94 are a private test set. Evaluation requires contacting the authors.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

## Evaluation

### Metrics

Biological grader scores for tasks and subtasks; the single-pass and gated protocols are kept separate.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### Scoring

58 classes of deterministic graders first give the answer fields a score from 0 to 1. A subtask takes the mean of its fields, and a task takes the mean of its subtasks. single-pass has no feedback. The gated threshold is 0.7, with at most 3 attempts and 1800 seconds per round. Both modes record the best attempt.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### 提示与运行设置

1800 seconds per turn; Docker with no network, 4 cores, 12GB of memory, and a 20GB disk; reasoning high when it is supported. 12 models, 3 harnesses, and 14 combinations.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 评测脚本

The official HF repository omicsbench_runner/ contains the runner and every grader; installation and running instructions are in omicsbench_runner/README.md.

Sources: [1](https://huggingface.co/datasets/gideonshaked/OmicsBench) (accessed 2026-11-08)

### 可比性提醒

Model and harness are confounded; gated feedback may lead to reward hacking, so a gain can be treated as an upper bound rather than as an independent capability gain.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 数据版本与更新

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 论文修订记录

```json
{
 "2026_H2_evidence": [
 {
 "url": "https://arxiv.org/html/2610.21074v1"
 "date": "2026-10-15"
 "note": "The original OmicsBench paper was released in H2 and evaluates research-scale, multi-turn omics data-analysis agents."
 }
 ]
 "evidence_boundary": "A citation is not a rerun; this page keeps the historical experiments in the paper separate from the current leaderboard."
 "paper_metadata": {
 "title": "OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics"
 "authors": [
 "Shaked, Gideon"
 "Nagisetty, Siddharth"
 ]
 "release": "2026-10-15"
 "latest": "2026-10-15"
 "version": "v1"
 }
}
```

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### 饱和程度

In the original paper's experiments with 12 models and 3 harnesses, the best result, Opus 5/OpenCode, is 0.57 single-pass and 0.67 gated. The authors consider it unsaturated. This is a judgment in the paper, not a conclusion from a live leaderboard.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### 争议与已知问题

The 94 private tests prevent public answers from being exposed. Gated feedback allows guessing, or adjustment of a threshold, that causes reward hacking, and the gain is an upper bound on the effect of the feedback. Effects of the model and of the harness are not fully separated. The judge used in the failure analysis has not been checked against human annotation.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07)

### 衍生与后续使用

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (date the web page was accessed; dates of historical results are kept separately).

Sources: [1](https://huggingface.co/datasets/gideonshaked/OmicsBench) (accessed 2026-11-08)

### 官方结果入口

https://huggingface.co/datasets/gideonshaked/OmicsBench

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 第三方入口

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 分赛道结果

- {"model": "Opus 5", "score": 0.57, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.56, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 2}
- {"model": "Grok 4.6", "score": 0.55, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 3}
- {"model": "Muse-Spark 1.1", "score": 0.54, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 4}
- {"model": "Kimi K3", "score": 0.49, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 5}
- {"model": "GLM-5.2", "score": 0.48, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 6}
- {"model": "Qwen3.8-Max", "score": 0.48, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 6}
- {"model": "Gemini 3.1 Pro", "score": 0.47, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 8}
- {"model": "MiniMax-M3", "score": 0.46, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 9}
- {"model": "DeepSeek-V4-Pro", "score": 0.45, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 10}
- {"model": "Qwen3.7-Max", "score": 0.44, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 11}
- {"model": "Grok 4.3", "score": 0.43, "track": "Original paper v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 12}
- {"model": "Opus 5", "score": 0.67, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.66, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 2}
- {"model": "Grok 4.6", "score": 0.66, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 2}
- {"model": "Muse-Spark 1.1", "score": 0.63, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 4}
- {"model": "Kimi K3", "score": 0.59, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 5}
- {"model": "GLM-5.2", "score": 0.59, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 5}
- {"model": "Qwen3.8-Max", "score": 0.59, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 5}
- {"model": "Gemini 3.1 Pro", "score": 0.58, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 8}
- {"model": "MiniMax-M3", "score": 0.58, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 8}
- {"model": "DeepSeek-V4-Pro", "score": 0.58, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 8}
- {"model": "Qwen3.7-Max", "score": 0.56, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 11}
- {"model": "Grok 4.3", "score": 0.54, "track": "Original paper v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 12}
- {"model": "Opus 5", "score": 0.56, "track": "Original paper v1/Claude Code/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Claude Code", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 1}
- {"model": "Opus 5", "score": 0.66, "track": "Original paper v1/Claude Code/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Claude Code", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.55, "track": "Original paper v1/Codex/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Codex", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.67, "track": "Original paper v1/Codex/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Codex", "runs_per_task": 3, "result_type": "The exact figures to two decimal places marked in Figure4A of the paper; they were checked visually number by number, and were not estimated from bar height.", "rank": 1}

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### 覆盖边界

All 14 model/harness combinations × two protocols = 28 published numbers in Figure4A of the paper were transcribed in full. The text in the PDF figure was checked visually item by item, and values are not estimated from bar heights. OpenCode, ClaudeCode, and Codex, and single-pass and gated, each form tracks. The original paper has 12 models and 14 combinations. There is no independent live dynamic leaderboard, and every score is a historical result from the paper.

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

## Contact

### 公开项目邮箱

- gshaked@umich.edu

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### 公开反馈渠道

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 官方社交渠道

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 联系方式收录原则

Benchmark Constitution includes only project contact channels that the paper or the official site has made public, and it does not collect private information; this is not a certification of an external site’s privacy policy.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08)

## Original files

### 既存论文原件

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 原始PDF地址

https://arxiv.org/pdf/2610.21074

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)

### 下载SHA-256

34555d4ef285b66a95fc368bc903980f44d436e0de2987992bc3729a7f4f0171

Note: Checksum of the bytes downloaded on 2026-11-08. Nothing was overwritten or uploaded, so this does not establish that an existing original is the same version.

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### 下载字节数

```json
1891438
```

Sources: [1](https://arxiv.org/pdf/2610.21074) (accessed 2026-11-08)

### Other documents

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2610.21074) (accessed 2026-11-08)
