# SWE-bench Verified

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

SWE-bench Verified is the subset of 500 questions that remains after human review of whether the original software-repair questions can be solved. It is not a newly scraped hidden test set. The full submission leaderboard embedded in the homepage of the official site was found in this reading, and the system, the agent, the release, and whether the official side checked it are kept; the score after the same model changes scaffold cannot be read as a direct upgrade of the model itself.

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08); [2](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-08); [3](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-08)

## Basic information

### Short name

SWE-bench Verified

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### Full name

SWE-bench Verified

Note: The official name is retained, and the paper title is not automatically expanded into a full name.

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### Benchmark version

SWE-bench Verified, 500 questions

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### Paper version

arXiv v3; submitted at 2024-11-12 08:05:04.

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-08)

### Release date

2024-08-13 (official announcement date; time and time zone not indicated)

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Section

Code

Note: Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-08)

### Field tags

- Repository-level repair of real software issues

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-08)

### 许可与适用范围

The code is MIT (the LICENSE of the current repository). The original HF Verified data card read this time has no license metadata. The scope of the data license is Unverified. The MIT license of the code cannot be extended automatically to the original issues, the patches, and third-party software.

Sources: [1](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE) (accessed 2026-11-08); [2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2310.06770

Note: 2310.06770 is the parent-benchmark paper of SWE-bench; the selection protocol for Verified is mainly in the official announcement, and it is not claimed to be an independent Verified paper.

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-08)

### Code repository

https://github.com/SWE-bench/SWE-bench

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### 数据地址

https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Official homepage

https://www.swebench.com/verified

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### Paper title

SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-08)

## Origin and maintenance

### 机构与发起关系

Released in collaboration between OpenAI and the original SWE-bench authors.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Partner organizations

OpenAI (the official site states explicitly that Verified was built with OpenAI in the human filtering).

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### Authors

Verified announcement: Neil Chowdhury, James Aung, Chan Jun Shern, Oliver Jaffe, Dane Sherburn, Giulio Starace, and others; authors of the parent paper are given separately in the paper metadata.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Current maintainer

The official SWE-bench team maintains the data and the evaluation framework; OpenAI provides the human annotation and the Verified announcement.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### 资助与支持

The SWE-bench official site acknowledges support from Open Philanthropy, AWS, Modal, Andreessen Horowitz, OpenAI, and Anthropic; this list is not an allocation table for Verified-specific funding.

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08)

## Design goals

### Abilities measured

Understands a real GitHub issue, locates the code, and submits a repository-level patch that solves the problem without causing a regression.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Design background

In the original SWE-bench, an underspecified description, an overly narrow test, or a failed environment install can mark a reasonable solution wrong; Verified removes these unfair instances.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

## Construction

### 题目或数据来源

Resolved issues and PRs from 12 open-source Python repositories; 500 were screened from 1,699 randomly annotated samples in the original test set.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### 出题背景

93 professional developers with Python experience; they first pass 50 high-confidence onboarding questions and receive feedback.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Review process

Each sample's description and tests are rated by 3 independent annotators; the highest-severity label is used, and any serious problem leads to exclusion.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Quality control

Description and test severity 0–3; an item is removed if any dimension is ≥2 or if there is another major problem; a Docker harness improves run stability.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### 去污染与泄漏

The original issues, the repository, and the PRs are public; the official account explicitly acknowledges that data scraped from the static internet may already have entered pretraining. Human Verified does not mean decontamination.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

## Data format

### Size

500 questions; 196 easy questions estimated at under 15 minutes and 45 hard questions estimated at more than 1 hour (human estimates, not model time limits).

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Question types

Repository and problem statement → edited files or a code patch.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Modalities

- 文本
- 代码
- 仓库环境

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Languages

The repository is mainly Python; the dataset card states that the question text is mainly English, but it was not filtered or cleaned by language, and it is not guaranteed that all of it is purely English.

Sources: [1](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified) (accessed 2026-11-08)

### Difficulty

Manually annotated as <15min, 15min–1h, 1–4h, and >4h; kept separate from the filter for whether a problem is solvable.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### 数据划分

The Verified data are public; at runtime the agent is not given the gold patch or the grading tests, and public availability still carries a risk of contamination.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

## Evaluation

### Metrics

Resolved rate: the proportion of tasks fully resolved.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### Scoring

A case counts as resolved only when the patch applies and every test in both FAIL_TO_PASS and PASS_TO_PASS passes.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07)

### 提示与运行设置

The official Bash Only setting uses the minimal ReAct loop of mini-SWE-agent. Where release 1.x supports it, temperature=0. From 2.x onward, temperature is not set. The version record must be kept together with the score.

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### 评测脚本

Current v5 CLI: swebench eval verified -p <predictions> --run-id <run_id> -j <workers>. The old python -m swebench.harness.run_evaluation is still supported. Re-evaluation of a new patch must use a new run_id, so that old results are not cached by run_id/instance_id.

Sources: [1](https://github.com/SWE-bench/SWE-bench) (accessed 2026-11-08)

### 可比性提醒

The full leaderboard compares arbitrary agent systems, and only Bash Only pins mini-SWE-agent; 1.x parses an output string, and 2.x uses tool calling. The official site states explicitly that results from the two generations are not necessarily comparable. The 500-question Verified set is not the full SWE-bench and is not SWE-bench Pro.

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

## Current status

### Date checked

2026-11-08

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-08)

### 数据版本与更新

```json
{
 "version": "SWE-bench Verified, 500 questions"
 "evidence_2026_h2": [
 {
 "url": "https://arxiv.org/html/2609.20804v1"
 "date": "2026-09-17"
 "note": "§3.1 of the Harness Design study actually uses 500 GitHub issues that were verified by humans and compares different harness settings; it is not the SWE-Bench Pro Verified of the same name."
 }
 ]
}
```

Note: Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

Sources: [1](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-07); [2](https://www.swebench.com/verified) (accessed 2026-11-07)

### 论文修订记录

- {"version": "v1", "submitted_at": "2023-10-11 01:47:29 "}
- {"version": "v2", "submitted_at": "2024-04-06 03:16:29 "}
- {"version": "v3", "submitted_at": "2024-11-12 08:05:04 "}

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-08)

### 饱和证据与局限

The highest system result in the collection snapshot from the official site is 79.2% (two tied); this is a result visible on the submission leaderboard, not evidence that "all models are saturated."

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08)

### 争议与已知问题

Verified is a quality filter rather than a set of hidden new questions, and it mainly covers Python software issues; it cannot be treated as general software development or as a guarantee of no contamination.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-07)

### 衍生或后继基准

Related to SWE-bench Lite, Multimodal, Multilingual, and SWE-bench Pro, but on different bases, and rankings are not mixed.

Sources: [1](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-07)

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08); [2](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-08); [3](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-08)

### 官方榜单入口

https://www.swebench.com/?tab=verified

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08)

### 第三方入口

Unverified

Note: Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Official complete system leaderboard | 1 | Sonar Foundation Agent + Claude 4.5 Opus | 79.2 | resolved (%) | Verified500；['Model: claude-opus-4-5', 'Org: Sonar', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 1 | live-SWE-agent + Claude 4.5 Opus medium (20251101) | 79.2 | resolved (%) | Verified500；['Model: claude-opus-4-5-20251101', 'Org: UIUC', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 3 | TRAE + Doubao-Seed-Code | 78.8 | resolved (%) | Verified500；['Model: Doubao-Seed-Code', 'Model: Doubao-Seed-1.6', 'Org: ByteDance', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 4 | live-SWE-agent + Gemini 3 Pro Preview (2025-11-18) | 77.4 | resolved (%) | Verified500；['Model: gemini-3-pro-preview', 'Org: UIUC', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 5 | EPAM AI/Run Developer Agent v20250719 + Claude 4 Sonnet | 76.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Org: EPAM Systems, Inc.', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 5 | Atlassian Rovo Dev (2025-09-02) | 76.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Model: gpt-5', 'Org: Atlassian', 'System: Attempts - 2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 1 | Claude 4.5 Opus (high) | 76.8 | resolved (%) | Verified500；['Model: claude-4-5-opus', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 7 | ACoder | 76.4 | resolved (%) | Verified500；['Model: claude-4-sonnet', 'Model: claude-4.1-opus', 'Model: gpt-5-0807-global', 'Model: gemini-2.5-pro-06-17', 'Org: ACoder', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 2 | Gemini 3 Flash (high) | 75.8 | resolved (%) | Verified500；['Model: gemini-3-flash-preview', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 2 | MiniMax M2.5 (high) | 75.8 | resolved (%) | Verified500；['Model: minimax-m2.5', 'Org: Minimax', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 8 | Warp | 75.6 | resolved (%) | Verified500；['Model: gpt-5', 'Model: claude-sonnet-4-20250514', 'Org: Warp', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 4 | Claude 4.6 Opus | 75.6 | resolved (%) | Verified500；['Model: claude-opus-4-6', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 9 | TRAE + Claude Sonnet 4 + Opus 4 + Sonnet 3.7 + Gemini 2.5 Pro | 75.2 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250522', 'Model: claude-4-opus-20250522', 'Model: claude-3-7-sonnet-20250219', 'Model: gemini-2.5-pro-preview-06-05', 'Org: TRAE', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 10 | Harness AI | 74.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Org: Harness', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 10 | Sonar Foundation Agent + Claude 4.5 Sonnet | 74.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-5', 'Org: Sonar', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 12 | Lingxi-v1.5_claude-4-sonnet-20250514 | 74.6 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Lingxi', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 12 | JoyCode + Claude 4 Sonnet + GPT-4.1 | 74.6 | resolved (%) | Verified500；['Model: claude-4-sonnet', 'Model: gpt-4.1', 'Org: JoyCode', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 14 | Refact.ai Agent + Claude 4 Sonnet + o4-mini | 74.4 | resolved (%) | Verified500；['Model: claude-4-sonnet', 'Model: o4-mini', 'Org: Refact.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 14 | Prometheus-v1.2.1 + GPT-5 | 74.4 | resolved (%) | Verified500；['Model: gpt-5-2025-08-07', 'Org: EuniAI', 'Org: Delysium', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.16.0 | 1 | Claude 4.5 Opus (20251101) (medium) | 74.4 | resolved (%) | Verified500；['Model: claude-opus-4-5-20251101', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.16.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.15.0 | 1 | Gemini 3 Pro Preview (2025-11-18) | 74.2 | resolved (%) | Verified500；['Model: gemini-3-pro-preview', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 1.15.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 16 | Salesforce AI Research SAGE (OpenHands) | 73.8 | resolved (%) | Verified500；['Model: claude-sonnet-4.5', 'Model: gpt-5', 'Org: Salesforce AI Research', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 17 | Tools + Claude 4 Opus (2025-05-22) | 73.2 | resolved (%) | Verified500；['Model: claude-4-opus-20250514', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 18 | Salesforce AI Research SAGE (bash-only) | 73.0 | resolved (%) | Verified500；['Model: claude-sonnet-4.5', 'Model: gpt-5', 'Org: Salesforce AI Research', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 5 | GLM 5 (high) | 72.8 | resolved (%) | Verified500；['Model: glm-5', 'Org: Z-AI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 5 | GPT 5.2 (high) | 72.8 | resolved (%) | Verified500；['Model: gpt-5-2', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 5 | GPT 5.2 Codex | 72.8 | resolved (%) | Verified500；['Model: gpt-5-2-codex', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 19 | Tools + Claude 4 Sonnet (2025-05-22) | 72.4 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 20 | OpenHands + GPT-5 | 71.8 | resolved (%) | Verified500；['Model: openai/gpt-5-2025-08-07', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.2 | 1 | GPT 5.2 (2025-12-11) (high) | 71.8 | resolved (%) | Verified500；['Model: gpt-5.2-2025-12-11', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 8 | Claude 4.5 Sonnet (high) | 71.4 | resolved (%) | Verified500；['Model: claude-sonnet-4-5-20250929', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 21 | Bloop | 71.2 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Bloop AI', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 21 | Qodo Command | 71.2 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Model: gpt-4o', 'Org: Qodo', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 21 | Prometheus-v1.2 + GPT-5 | 71.2 | resolved (%) | Verified500；['Model: gpt-5-2025-08-07', 'Org: EuniAI', 'Org: Delysium', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 21 | Lingxi v1.5 x Kimi K2 | 71.2 | resolved (%) | Verified500；['Model: kimi-k2-0905-preview', 'Org: Huawei', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 25 | Warp | 71.0 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Model: claude-3-7-sonnet-20250219', 'Model: gemini-2.5-pro', 'Model: gpt-4.1-2025-04-14', 'Org: Warp', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 26 | Moatless Tools + Claude 4 Sonnet | 70.8 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Moatless AI', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 9 | Kimi K2.5 (high) | 70.8 | resolved (%) | Verified500；['Model: kimi-k2.5', 'Org: Moonshot AI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 27 | TRAE | 70.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.13.3 | 1 | Claude 4.5 Sonnet (20250929) | 70.6 | resolved (%) | Verified500；['Model: claude-sonnet-4-5-20250929', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.13.3'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 28 | Refact.ai Agent | 70.4 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Model: o3', 'Model: o4-mini', 'Org: Refact.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 28 | OpenHands + Claude 4 Sonnet | 70.4 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 28 | Augment Agent v1 | 70.4 | resolved (%) | Verified500；['System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 31 | devlo | 70.2 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Model: o3', 'Model: gemini-2.5-pro', 'Org: devlo', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 32 | Zencoder (2025-04-30) | 70.0 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Model: o4-mini', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 10 | DeepSeek V3.2 (high) | 70.0 | resolved (%) | Verified500；['Model: deepseek-v3.2', 'Org: DeepSeek', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 33 | OpenHands + Qwen3-Coder-480B-A35B-Instruct | 69.6 | resolved (%) | Verified500；['Model: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct', 'Org: Qwen', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 11 | Gemini 3 Pro | 69.6 | resolved (%) | Verified500；['Model: gemini-3-pro-preview', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.2 | 2 | GPT 5.2 (2025-12-11) | 69.0 | resolved (%) | Verified500；['Model: gpt-5.2-2025-12-11', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 34 | Nemotron-CORTEXA | 68.2 | resolved (%) | Verified500；['Model: NV-EmbedCode', 'Model: o3', 'Model: o3-mini', 'Model: o1', 'Model: gpt-4.1', 'Model: gpt-4o-2024-05-13', 'Model: gpt-4-turbo-2024-04-09', 'Model: claude-3-7-sonnet-20250219', 'Model: deepseek-v3', 'Model: Qwen/Qwen2.5-72B-Instruct', 'Model: meta-llama/Llama-3.1-405B-Instruct', 'Model: meta-llama/Llama-3.3-70B-Instruct', 'Org: NVIDIA', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 34 | GLM-4.6 | 68.2 | resolved (%) | Verified500；['Model: https://huggingface.co/zai-org/GLM-4.6', 'Org: Z.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 1 | Claude 4 Opus (20250514) | 67.6 | resolved (%) | Verified500；['Model: claude-4-opus-20250514', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 36 | SWE-agent + Claude 4 Sonnet | 66.6 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 12 | Claude 4.5 Haiku (high) | 66.6 | resolved (%) | Verified500；['Model: claude-haiku-4-5-20251001', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 37 | Aime-coder v1 + Anthopic Claude 3.7 Sonnet | 66.4 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Org: ByteDance DevInfra', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.15.0 | 2 | GPT 5.1 (2025-11-13) (medium) | 66.0 | resolved (%) | Verified500；['Model: gpt-5.1-2025-11-13', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.15.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.16.0 | 2 | GPT 5.1 Codex (medium) | 66.0 | resolved (%) | Verified500；['Model: gpt-5.1-codex', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.16.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 38 | OpenHands | 65.8 | resolved (%) | Verified500；['Org: OpenHands', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 39 | Augment Agent v0 | 65.4 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 39 | Amazon Q Developer Agent (v20250405-dev) | 65.4 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 39 | OpenHands + Kimi K2 | 65.4 | resolved (%) | Verified500；['Model: moonshot/kimi-k2-0711-preview', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.7.0. | 1 | GPT 5 (2025-08-07) (medium) | 65.0 | resolved (%) | Verified500；['Model: gpt-5-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 2 | Claude 4 Sonnet (20250514) | 64.93 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 42 | W&B Programmer O1 crosscheck5 | 64.6 | resolved (%) | Verified500；['Model: o1-preview', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 42 | PatchPilot-v1.1 | 64.6 | resolved (%) | Verified500；['Model: o4-mini', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 44 | GLM-4.5 | 64.2 | resolved (%) | Verified500；['Model: https://huggingface.co/zai-org/GLM-4.5', 'Org: Z.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 45 | AgentScope | 63.4 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.2 | 3 | Kimi K2 Thinking | 63.4 | resolved (%) | Verified500；['Model: Kimi-K2-Thinking', 'Org: Moonshot AI', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 46 | Tools + Claude 3.7 Sonnet (2025-02-24) | 63.2 | resolved (%) | Verified500；['Org: Anthropic', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 47 | Blackbox AI Agent | 62.8 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 47 | EPAM AI/Run Developer Agent v20250219 + Anthopic Claude 3.5 Sonnet | 62.8 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 49 | SWE-agent + Claude 3.7 Sonnet w/ Review Heavy | 62.4 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Org: SWE-agent', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 50 | CodeStory Midwit Agent + swe-search | 62.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.0 | 1 | MiniMax M2 | 61.0 | resolved (%) | Verified500；['Model: minimax-m2', 'Org: Minimax', 'System: Attempts - 1', 'Mini: 1.17.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 51 | OpenHands + 4x Scaled (2024-02-03) | 60.8 | resolved (%) | Verified500；['Org: OpenHands', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 52 | EntroPO + R2E + Qwen3-Coder-30B-A3B-Instruct | 60.4 | resolved (%) | Verified500；['Model: Qwen3-Coder-30B-A3B-Instruct', 'Org: 42-b3yond-6ug', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 53 | Learn-by-interact | 60.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Google', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.1 | 1 | DeepSeek V3.2 Reasoner | 60.0 | resolved (%) | Verified500；['Model: deepseek-v3.2-reasoner', 'Org: deepseek', 'System: Attempts - 1', 'Mini: 1.17.1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.7.0. | 2 | GPT 5 mini (2025-08-07) (medium) | 59.8 | resolved (%) | Verified500；['Model: gpt-5-mini-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 54 | DeepSWE-Preview + TTS(Bo16) | 58.8 | resolved (%) | Verified500；['Model: https://huggingface.co/agentica-org/DeepSWE-Preview', 'Org: Agentica', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 3 | o3 (2025-04-16) | 58.4 | resolved (%) | Verified500；['Model: o3-20250416', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 55 | devlo | 58.2 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 55 | Nemotron-CORTEXA | 58.2 | resolved (%) | Verified500；['Model: NV-EmbedCode', 'Model: claude-3-5-sonnet-20241022', 'Model: deepseek-v3', 'Model: o3-mini', 'Model: gpt-4o-2024-05-13', 'Model: gpt-4-turbo-2024-04-09', 'Model: Qwen/Qwen2.5-72B-Instruct', 'Model: meta-llama/Llama-3.1-405B-Instruct', 'Model: meta-llama/Llama-3.3-70B-Instruct', 'Org: NVIDIA', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 57 | Emergent E1 (v2024-12-23) | 57.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 58 | Gru(2024-12-08) | 57.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 58 | Artemis Agent v2 (2025-09-24) | 57.0 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Org: Turintech', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 60 | SWE-Rizzo | 56.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.2 | 4 | Devstral Small (2512) | 56.4 | resolved (%) | Verified500；['Model: devstral-small-2512', 'Org: mistral', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 2.0.0. | 13 | GPT 5 mini | 56.2 | resolved (%) | Verified500；['Model: gpt-5-mini-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 61 | EPAM AI/Run Developer Agent v20241212 + Anthopic Claude 3.5 Sonnet | 55.4 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 4 | Qwen3-Coder 480B/A35B Instruct | 55.4 | resolved (%) | Verified500；['Model: Qwen3-Coder-480B-A35B-Instruct', 'Org: Qwen', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.1 | 2 | GLM 4.6 (T=1) | 55.4 | resolved (%) | Verified500；['Model: glm-4.6', 'Org: Z.ai', 'System: Attempts - 1', 'Mini: 1.17.1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 62 | Amazon Q Developer Agent (v20241202-dev) | 55.0 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 63 | devlo | 54.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.9.1. | 1 | GLM 4.5 (2025-08-22) | 54.2 | resolved (%) | Verified500；['Model: GLM-4.5', 'Org: Z.ai', 'System: Attempts - 1', 'Mini: 1.9.1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.17.2 | 5 | Devstral (2512) | 53.8 | resolved (%) | Verified500；['Model: devstral-2512', 'Org: mistral', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 64 | FrogBoss-32B-2510 | 53.6 | resolved (%) | Verified500；['Model: FrogBoss-32B-2510', 'Org: Microsoft', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 5 | Gemini 2.5 Pro (2025-05-06) | 53.6 | resolved (%) | Verified500；['Model: gemini-2.5-pro', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 65 | CodeSweep - SWE-agent - Kimi K2 Instruct | 53.4 | resolved (%) | Verified500；['Model: kimi-k2-instruct', 'Org: CodeSweep Inc.', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 66 | Bracket.sh | 53.2 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 67 | OpenHands + CodeAct v2.1 (claude-3-5-sonnet-20241022) | 53.0 | resolved (%) | Verified500；['Org: OpenHands', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 0.0.0. | 1 | Claude 3.7 Sonnet (20250219) | 52.8 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 68 | Google Jules + Gemini 2.0 Flash (v20241212-experimental) | 52.2 | resolved (%) | Verified500；['Org: Google', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 68 | EntroPO + R2E + Qwen3-Coder-30B-A3B-Instruct | 52.2 | resolved (%) | Verified500；['Model: Qwen3-Coder-30B-A3B-Instruct', 'Org: 42-b3yond-6ug', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 70 | Engine Labs (2024-11-25) | 51.8 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Engine Labs', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 71 | AutoCodeRover-v2.1 (Claude-3.5-Sonnet-20241022) | 51.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 71 | OpenHands + Qwen3-Coder-30B-A3B-Instruct | 51.6 | resolved (%) | Verified500；['Model: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct', 'Org: Qwen', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 73 | Agentless-1.5 + Claude-3.5 Sonnet (20241022) | 50.8 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Agentless', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 74 | Solver (2024-10-28) | 50.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 74 | Bytedance MarsCode Agent | 50.0 | resolved (%) | Verified500；['Org: Bytedance', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 76 | nFactorial (2024-11-05) | 49.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 77 | Tools + Claude 3.5 Sonnet (2024-10-22) | 49.0 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: claude-3.5-sonnet-20241022', 'Org: Anthropic', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 78 | Composio SWE-Kit (2024-10-25) | 48.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: o1-mini', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 79 | AppMap Navie v2 | 47.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 80 | Skywork-SWE-32B + TTS(Bo8) | 47.0 | resolved (%) | Verified500；['Model: Qwen2.5-Coder-32B-Instruct', 'Org: Skywork AI', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 81 | OpenHands + DevStral Small 2505 | 46.8 | resolved (%) | Verified500；['Model: mistralai/Devstral-Small-2505', 'Org: OpenHands', 'Org: Mistral', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 82 | Emergent E1 (v2024-10-12) | 46.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 83 | AutoCodeRover-v2.0 (Claude-3.5-Sonnet-20241022) | 46.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 84 | PatchPilot + Co-PatcheR | 46.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 85 | Solver (2024-09-12) | 45.4 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 86 | Gru(2024-08-24) | 45.2 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 87 | FrogMini-14B-2510 | 45.0 | resolved (%) | Verified500；['Model: FrogMini-14B-2510', 'Org: Microsoft', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 6 | o4-mini (2025-04-16) | 45.0 | resolved (%) | Verified500；['Model: o4-mini-20250416', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 88 | CodeShellAgent + Gemini 2.0 Flash (Experimental) | 44.2 | resolved (%) | Verified500；['Model: gemini-2.0-flash-exp', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.7.0. | 3 | Kimi K2 Instruct | 43.8 | resolved (%) | Verified500；['Model: Kimi-K2-Instruct', 'Org: Moonshot AI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 89 | Solver (2024-09-12) | 43.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 90 | Agentless Lite + O3 Mini (20250214) | 42.4 | resolved (%) | Verified500；['Model: o3-mini', 'Org: Agentless', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 90 | Amazon Nova Premier 1.0 (2025-04-30) | 42.4 | resolved (%) | Verified500；['Model: amazon.nova-premier-v1:0', 'Org: Amazon Nova', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 92 | DeepSWE-Preview | 42.2 | resolved (%) | Verified500；['Model: https://huggingface.co/agentica-org/DeepSWE-Preview', 'Org: Agentica', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 93 | SWE-Exp | 42.0 | resolved (%) | Verified500；['Model: DeepSeek-V3-0324', 'Org: SWE-Exp', 'System: Attempts - 2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 94 | nFactorial (2024-10-30) | 41.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'Model: o1-preview', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 94 | ugaiforge | 41.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 96 | SWE-RL (Llama3-SWE-RL-70B + Agentless Mini) (20250226) | 41.2 | resolved (%) | Verified500；['Model: Llama3-SWE-RL-70B', 'Model_size: 70', 'Org: Agentless', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 97 | Honeycomb | 40.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 97 | Composio SWEkit + Claude 3.5 Sonnet (2024-10-16) | 40.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: claude-3.5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 97 | Tools + Claude 3.5 Haiku | 40.6 | resolved (%) | Verified500；['Model: claude-3-haiku-20240307', 'Org: Anthropic', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 97 | Nebius AI Qwen 2.5 72B Generator + LLama 3.1 70B Critic | 40.6 | resolved (%) | Verified500；['Model: Llama 3.1', 'Model: Qwen 2.5', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 101 | SWE-agent + SWE-agent-LM-32B | 40.2 | resolved (%) | Verified500；['Model: Qwen 2.5', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 102 | EPAM AI/Run Developer Agent v20241029 + Anthopic Claude 3.5 Sonnet | 39.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 7 | GPT 4.1 (2025-04-14) | 39.58 | resolved (%) | Verified500；['Model: gpt-4.1-20250414', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 103 | Amazon Q Developer Agent (v20240719-dev) | 38.8 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 103 | Agentless-1.5 + GPT 4o (2024-05-13) | 38.8 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'Org: Agentless', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 105 | AutoCodeRover (v20240620) + GPT 4o (2024-05-13) | 38.4 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 106 | Skywork-SWE-32B | 38.0 | resolved (%) | Verified500；['Model: Qwen2.5-Coder-32B-Instruct', 'Org: Skywork AI', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 106 | SWE-agent + DevStral Small 2507 | 38.0 | resolved (%) | Verified500；['Model: devstral-small-2507', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 108 | Factory Code Droid | 37.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.7.0. | 4 | GPT 5 nano (2025-08-07) (medium) | 34.8 | resolved (%) | Verified500；['Model: gpt-5-nano-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 109 | SWE-agent + Claude 3.5 Sonnet | 33.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 110 | SWE-Fixer (Qwen2.5-7b retriever + Qwen2.5-72b editor) | 32.8 | resolved (%) | Verified500；['Model: Qwen 2.5', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 111 | MASAI + GPT 4o (2024-06-12) | 32.6 | resolved (%) | Verified500；['Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 112 | Artemis Agent v1 (2024-11-20) | 32.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 113 | nFactorial (2024-10-07) | 31.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 114 | SWE-Fixer (Qwen2.5-7b retriever + Qwen2.5-72b editor) 20241128 | 30.2 | resolved (%) | Verified500；['Model: Qwen 2.5', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 115 | Lingma Agent + Lingma SWE-GPT 72b (v0925) | 28.8 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 8 | Gemini 2.5 Flash (2025-04-17) | 28.73 | resolved (%) | Verified500；['Model: gemini-2.5-flash', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 116 | EPAM AI/Run Developer Agent + GPT4o | 27.0 | resolved (%) | Verified500；['Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 117 | AppMap Navie + GPT 4o (2024-05-13) | 26.2 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.7.0. | 5 | gpt-oss-120b | 26.0 | resolved (%) | Verified500；['Model: gpt-oss-120b', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 118 | nFactorial (2024-10-01) | 25.8 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 119 | Amazon Q Developer Agent (v20240430-dev) | 25.6 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 120 | Lingma Agent + Lingma SWE-GPT 72b (v0918) | 25.0 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 121 | EPAM AI/Run Developer Agent + GPT4o | 24.0 | resolved (%) | Verified500；['Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 0.0.0. | 2 | GPT 4.1 mini (2025-04-14) | 23.94 | resolved (%) | Verified500；['Model: gpt-4.1-mini-20250414', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 122 | SWE-agent + GPT 4o (2024-05-13) | 23.2 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 122 | MCTS-Refine-7B | 23.2 | resolved (%) | Verified500；['Model: MCTS-Refine-7B', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 124 | SWE-agent + GPT 4 (1106) | 22.4 | resolved (%) | Verified500；['Model: gpt-4-1106-preview', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 0.0.0. | 3 | GPT 4o (2024-11-20) | 21.62 | resolved (%) | Verified500；['Model: gpt-4o-20241120', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 0.0.0. | 4 | Llama 4 Maverick Instruct | 21.04 | resolved (%) | Verified500；['Model: llama-4-maverick-instruct', 'Org: Meta', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 125 | Lingma Agent + Lingma SWE-GPT 7b (v0925) | 18.2 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 126 | SWE-agent + Claude 3 Opus | 15.8 | resolved (%) | Verified500；['Model: claude-3-opus-20240229', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 0.0.0. | 5 | Gemini 2.0 Flash | 13.52 | resolved (%) | Verified500；['Model: gemini-2.0-flash', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 127 | Lingma Agent + Lingma SWE-GPT 7b (v0918) | 10.2 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 0.0.0. | 6 | Llama 4 Scout Instruct | 9.06 | resolved (%) | Verified500；['Model: llama-4-scout-instruct', 'Org: Meta', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official Bash Only / mini-SWE-agent 1.0.0. | 9 | Qwen2.5-Coder 32B Instruct | 9.0 | resolved (%) | Verified500；['Model: Qwen2.5-Coder-32B-Instruct', 'Org: Qwen', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 128 | RAG + Claude 3 Opus | 7.0 | resolved (%) | Verified500；['Model: claude-3-opus-20240229', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 129 | RAG + Claude 2 | 4.4 | resolved (%) | Verified500；['Model: claude-2', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 130 | RAG + GPT 4 (1106) | 2.8 | resolved (%) | Verified500；['Model: gpt-4-1106-preview', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 131 | RAG + SWE-Llama 7B | 1.4 | resolved (%) | Verified500；['Model: SWE-Llama', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 132 | RAG + SWE-Llama 13B | 1.2 | resolved (%) | Verified500；['Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official complete system leaderboard | 133 | RAG + ChatGPT 3.5 | 0.4 | resolved (%) | Verified500；['Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| Official-announcement historical baseline | 1 | gpt-4o-2024-05-13 + Agentless | 33.2 | resolved (%) | Verified500； | [2024-08-13](https://openai.com/index/introducing-swe-bench-verified/)；采集2026-11-07 |
| H2 academic experiment | 1 | Nemotron-3 550B / research harness | 69.4 | SR (%) | Verified500；T4/128k, planning, bash-only, at most 300 steps, temperature 0 | [2026-09-17](https://arxiv.org/html/2609.20804v1)；采集2026-11-07 |

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08); [2](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-08); [3](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-08)

### 榜单覆盖边界

All 180 Verified system results were read from the public leaderboard-data JSON on the official homepage, rather than from the blank dynamic region of the /verified introduction page. Full systems and the Bash Only release are on separate tracks. checked=false is not an official reproduction experiment, and the submitted system leaderboard cannot be called a fixed model leaderboard. Two historical experiments verified earlier are retained, with their original collection dates.

Sources: [1](https://www.swebench.com/) (accessed 2026-11-08); [2](https://openai.com/index/introducing-swe-bench-verified/) (accessed 2026-11-08); [3](https://arxiv.org/html/2609.20804v1) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

- carlosej@princeton.edu
- johnby@stanford.edu

Sources: [1](https://github.com/SWE-bench/SWE-bench) (accessed 2026-11-08)

### 公开反馈渠道

https://github.com/SWE-bench/SWE-bench/issues

Note: Public repository feedback entry point; no question was sent.

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07)

### 官方社交账号

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-07)

### 联系方式/隐私原则

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2310.06770) (accessed 2026-11-07)

## Original files

### 原始PDF

https://arxiv.org/pdf/2310.06770

Sources: [1](https://arxiv.org/pdf/2310.06770) (accessed 2026-11-08)

### PDF SHA-256

f7e8e1df64129742b8199a21a042734519a823a1dafd6f48f8f3ddcfb48ee296

Sources: [1](https://arxiv.org/pdf/2310.06770) (accessed 2026-11-08)

### PDF bytes

```json
4533722
```

Sources: [1](https://arxiv.org/pdf/2310.06770) (accessed 2026-11-08)

### Other documents

Note: The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-07); [2]( 2026-11-07， )

### 论文原件

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://www.swebench.com/verified) (accessed 2026-11-08)
