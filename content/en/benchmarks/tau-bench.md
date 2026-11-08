# τ-bench

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

τ-bench requires an agent to complete a service workflow among a simulated user, business policies, and database tools; its pass^k measures success on every repeat, not pass@k for at least one success. The original repository now explicitly warns that the tasks are outdated. This page keeps the historical leaderboard of the original airline and retail protocol and does not substitute τ³ results.

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

## Basic information

### Short name

τ-bench

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### Full name

τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Benchmark version

Original retail / airline protocol; not mixed with τ²

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Paper version

arXiv v1; submitted at 2024-06-18 04:33:08.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Release date

2024-06-18 04:33:08

Note: The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Section

Agent

Note: Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Field tags

- Tool-agent-user interaction

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 许可与适用范围

MIT (as marked on the GitHub repository code; it does not automatically cover the original questions, third-party materials, or private test data)

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/2406.12045

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Code repository

https://github.com/sierra-research/tau-bench

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### 数据地址

https://github.com/sierra-research/tau-bench

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Official homepage

https://github.com/sierra-research/tau-bench

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### Paper title

$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

## Origin and maintenance

### 机构与发起关系

Sierra

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Partner organizations

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Authors

- Shunyu Yao
- Noah Shinn
- Pedram Razavi
- Karthik Narasimhan

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Current maintainer

Sierra Research / tau-bench team

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 资助与支持

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

## Design goals

### Abilities measured

Holds multi-turn exchanges with the user, calls database tools, and follows business policy, so as to complete realistic service tasks reliably.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Design background

A single-turn tool call or a fixed plan cannot clearly measure sustained user interaction, policy following, and reliability across repeated runs.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Retail and airline business policies, Python tool APIs, and a JSON database are designed by hand; a model assists in generating database contents, and humans write the task scenarios.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 出题背景

The Sierra research team; users are simulated by a language model and cannot be called real customer conversations.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Review process

Human-written scenarios and repeated agent runs iteratively verify that the tasks are feasible.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Quality control

Success is judged by the final state of the target database and by required substrings of user replies, and unrelated or prohibited changes are checked.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 去污染与泄漏

Public environments and tasks may be encountered by later training; randomness of simulated users cannot replace decontamination.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

## Data format

### Size

Original retail test of 115 questions and airline test of 50 questions.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Question types

Tool—Agent—user multi-turn business interaction.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Modalities

- 文本对话
- Structured database
- 函数调用

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Languages

English dialogue and Markdown policies; Python tools/JSON state.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Difficulty

Spans policies, collection of user information, and multiple actions; the original paper reports by domain and does not assume a unified mix of difficulty.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 数据划分

The original data, tools, policies, and evaluation code are public; user goals and gold-standard final states are not shown to the agent.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

## Evaluation

### Metrics

pass^k (all k repeated trials succeed); the average success rate is also reported; the definition is the opposite of pass@k, which counts at least one success.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### Scoring

The final-state database is compared with the gold standard, together with a check of required reply content; this is not a complete audit of all intermediate behavior.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 提示与运行设置

The original paper allows at most 30 agent actions per task; the main results use at least 3 trials, with agent temperature 0.0 and user temperature 1.0. The current README defaults to a gpt-4o user simulator, and the model and the llm, react, verify, or reflection strategy can be changed; the two must not be mixed as one setting.

Sources: [1](https://arxiv.org/pdf/2406.12045) (accessed 2026-11-08); [2](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

### 评测脚本

https://github.com/sierra-research/tau-bench

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### 可比性提醒

The domain average differs from the mean weighted by task; the user model, the number of runs, pass^k/pass@k, and the τ²/τ³ versions must be distinguished.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

### 数据版本与更新

This entry keeps the original τ-bench retail and airline protocol. The official README explicitly warns that the tasks are outdated and recommends migrating to τ³-bench; τ³ adds banking and voice and repairs retail and airline, and its scores cannot be relabeled as the original version.

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-06-18 04:33:08 "}

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-08)

### 饱和证据与局限

The highest Pass^1 visible in the old repository is 0.460 for airline and 0.692 for retail. The highest Pass^4 is 0.225 and 0.462 respectively, which shows a clear gap, for the same system, between a single run and reliability over several runs. The old questions are out of date, and ability on τ³ is not judged from them.

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

### 争议与已知问题

The official statement explicitly says that tasks in the original repository are no longer updated and are outdated; comparisons meant for external use must pin an old commit or use the τ³ revised tasks, and record them separately. Agreement of the final state does not guarantee that every intermediate action complies with policy.

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2406.12045) (accessed 2026-11-08)

### 衍生或后继基准

The successor repository of τ²-bench has now been upgraded to τ³-bench; it adds a banking domain, a voice modality, and repairs to the older domains.

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

### 官方榜单入口

https://github.com/sierra-research/tau-bench

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### 第三方入口

Unverified

Note: Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Official README legacy Airline / Pass^1 | 1 | claude-3-5-sonnet-20241022 | 0.46 | Pass^1 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^2 | 1 | claude-3-5-sonnet-20241022 | 0.326 | Pass^2 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^3 | 1 | claude-3-5-sonnet-20241022 | 0.263 | Pass^3 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^4 | 1 | claude-3-5-sonnet-20241022 | 0.225 | Pass^4 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^1 | 2 | gpt-4o | 0.42 | Pass^1 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^2 | 2 | gpt-4o | 0.273 | Pass^2 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^3 | 2 | gpt-4o | 0.22 | Pass^3 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^4 | 2 | gpt-4o | 0.2 | Pass^4 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^1 | 4 | claude-3-5-sonnet-20240620 | 0.36 | Pass^1 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^2 | 4 | claude-3-5-sonnet-20240620 | 0.224 | Pass^2 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^3 | 4 | claude-3-5-sonnet-20240620 | 0.169 | Pass^3 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^4 | 5 | claude-3-5-sonnet-20240620 | 0.139 | Pass^4 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^1 | 6 | gpt-4o-mini | 0.225 | Pass^1 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^2 | 6 | gpt-4o-mini | 0.14 | Pass^2 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^3 | 6 | gpt-4o-mini | 0.11 | Pass^3 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^4 | 6 | gpt-4o-mini | 0.1 | Pass^4 (0–1) | Original τ-bench / Airline；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^1 | 3 | gpt-4o | 0.365 | Pass^1 (0–1) | Original τ-bench / Airline；Act | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^2 | 5 | gpt-4o | 0.217 | Pass^2 (0–1) | Original τ-bench / Airline；Act | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^3 | 5 | gpt-4o | 0.16 | Pass^3 (0–1) | Original τ-bench / Airline；Act | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^4 | 4 | gpt-4o | 0.14 | Pass^4 (0–1) | Original τ-bench / Airline；Act | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^1 | 5 | gpt-4o | 0.325 | Pass^1 (0–1) | Original τ-bench / Airline；ReAct | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^2 | 3 | gpt-4o | 0.233 | Pass^2 (0–1) | Original τ-bench / Airline；ReAct | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^3 | 3 | gpt-4o | 0.185 | Pass^3 (0–1) | Original τ-bench / Airline；ReAct | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Airline / Pass^4 | 3 | gpt-4o | 0.16 | Pass^4 (0–1) | Original τ-bench / Airline；ReAct | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Older official README, Retail / Pass^1 | 1 | claude-3-5-sonnet-20241022 | 0.692 | Pass^1 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Retail / Pass^2 | 1 | claude-3-5-sonnet-20241022 | 0.576 | Pass^2 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Older official README, Retail / Pass^3 | 1 | claude-3-5-sonnet-20241022 | 0.509 | Pass^3 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Retail / Pass^4 | 1 | claude-3-5-sonnet-20241022 | 0.462 | Pass^4 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Older official README, Retail / Pass^1 | 3 | gpt-4o | 0.604 | Pass^1 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Retail / Pass^2 | 3 | gpt-4o | 0.491 | Pass^2 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Older official README, Retail / Pass^3 | 3 | gpt-4o | 0.43 | Pass^3 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Retail / Pass^4 | 3 | gpt-4o | 0.383 | Pass^4 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Older official README, Retail / Pass^1 | 2 | claude-3-5-sonnet-20240620 | 0.626 | Pass^1 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Retail / Pass^2 | 2 | claude-3-5-sonnet-20240620 | 0.506 | Pass^2 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Older official README, Retail / Pass^3 | 2 | claude-3-5-sonnet-20240620 | 0.435 | Pass^3 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| Official README legacy Retail / Pass^4 | 2 | claude-3-5-sonnet-20240620 | 0.387 | Pass^4 (0–1) | Original τ-bench / Retail；TC | [Unverified (the README does not mark an update time for this table)](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

### 榜单覆盖边界

All 36 rows in the README that contain a number are transcribed in full, from 9 systems × 4 Pass^k; ?? is explicitly unknown and is not filled in as zero. Each domain and each k is kept on its own track, and the strategy is retained; the original version has been marked outdated by the official source, and this table is not the latest τ³ leaderboard.

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-07)

### 公开反馈渠道

https://github.com/sierra-research/tau-bench/issues

Note: Public repository feedback entry point; no question was sent.

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07)

### 官方社交账号

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-07)

### 联系方式/隐私原则

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2406.12045) (accessed 2026-11-07)

## Original files

### 原始PDF

https://arxiv.org/pdf/2406.12045

Sources: [1](https://arxiv.org/pdf/2406.12045) (accessed 2026-11-08)

### PDF SHA-256

0ce66a1763d698c61bb311c3c874bf593d1e9a5bfff11bb35f6f72b981f6da56

Sources: [1](https://arxiv.org/pdf/2406.12045) (accessed 2026-11-08)

### PDF bytes

```json
663224
```

Sources: [1](https://arxiv.org/pdf/2406.12045) (accessed 2026-11-08)

### Other documents

Note: The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-07); [2]( 2026-11-07， )

### 论文原件

## Changelog

Latest review
Latest review
Latest review

Source: [1](https://github.com/sierra-research/tau-bench) (accessed 2026-11-08)
