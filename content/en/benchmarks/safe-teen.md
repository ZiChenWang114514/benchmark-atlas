# SAFE-Teen

> Verification date: 2026-11-08. The access date is not the publication date or the run date; a field that cannot be confirmed remains Unverified.

SAFE-Teen uses fictional scenarios and branching dialogues written by clinicians to test whether a chat model fails when an adolescent implies a risk, refuses outside help, or challenges the boundary of a relationship. What it evaluates is the rubric failure rate in a simulated interaction, not a medical effect, and scores without a prompt and scores under a teen-aware prompt cannot be mixed into one safety ranking.

Reading source: [Official materials](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08). Specific facts and historical access dates are given in the individual fields.

## Basic information

### Short name

SAFE-Teen

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Full name

Scenario-based Assessment of Failure Emergence in Teen Chats (SAFE-Teen)

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Benchmark version

Official-site update snapshot of 2026-10-13; no independent semantic version number is marked.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Paper version

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Release date

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Section

Safety

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Field tags

- 心理健康
- 多轮对话

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 许可与适用范围

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Paper

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Code repository

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 数据地址

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Official homepage

https://www.vals.ai/benchmarks/mental-health

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Paper title

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Origin and maintenance

### 机构与发起关系

Vals AI

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 合作机构/署名单位

A collaboration among Valerie Chen, Diyi Yang (Stanford SALT Lab), and Eric Lin (Stanford School of Medicine). Endorsement by either school as a whole is not inferred.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Authors

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 当前维护入口

Vals AI

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Funders

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Design goals

### Abilities measured

In adolescent mental-health conversations: emergency safety, the boundary of clinical advice, and the boundaries of emotional dependence and of relationships.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Design background

Risk develops with multi-turn dialogue and with adolescents refusing help; a fixed single-turn reply cannot reflect this change.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Construction

### 题目或数据来源

12 clinicians constructed 106 fictional scenarios for ages 13–17, grounded in clinical experience.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 出题背景

Clinicians take part in writing questions, peer review, and evaluation of the dialogues.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Review process

Realism, clinical plausibility, and age appropriateness are reviewed; 4 clinical advisors rate simulator candidates blind.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Quality control

8 clinicians independently rated 20 conversations, comparing agreement between the model and the clinicians; the simulated adolescent is GPT-5.6 Terra.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 去污染措施

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Data format

### Size

106 fictional scenarios; 32,555 dialogue segments that have been scored; 17 models, 18 configurations, and two system prompts per configuration. The risk domains have 35/36/35 cases; ages 13 through 17 have 21/21/21/22/21 cases, in that order.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Question types

6, 10, 15, or 20 exchanges; the path branches when a question is disclosed, when outside help is accepted, or when a boundary is accepted.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Modalities

- Multi-turn text dialogue

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Languages

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Difficulty

Risk may be implicit, disclosed gradually, or resistant to advice; this is not a real clinical trial of adolescents.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 数据划分

The official site discloses the protocol and examples; the full question set, the hidden-set split, and the license are Unverified.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Evaluation

### Metrics

Failure rate by risk domain; lower is better, and there is no single overall rank that can be substituted directly.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Scoring

Claude Sonnet 5.5 judges pass, partial, or fail by a safety rubric; for each model, prompt, scenario, and check, the worst score among the branches is taken; partial enters the denominator but is not counted as fail.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 提示与运行设置

The same scenarios and simulator; each model is run once with no system prompt and once with a teen-aware prompt.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 评测脚本

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 可比性提醒

The 18 rows on this page are 17 model configurations (Muse has two reasoning levels). The homepage of the official site states that the 15%–56% range of urgent safety-failure rates corresponds to the setting without a teen-aware prompt, so this table is recorded on that track. The teen-aware track must not be ranked together with it. An entry left unanswered because of API safety filtering is excluded, and exclusion is not the same as a pass.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， ) ; [2](https://www.vals.ai/home) (accessed 2026-11-08， )

## Current status

### Date checked

2026-11-08

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 数据版本与更新

- **version**：Update snapshot on the official site dated 2026-10-13; no separate semantic version number is marked
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/mental-health", "date": "2026-10-13", "note": "The update date written on the Vals official site; adopted mainly by a single organization."}]

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 论文修订记录

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 饱和程度

The official site reports an overall failure rate of 43.3% without a teen-aware prompt, and 24.9% after the prompt is added; this is not the simple arithmetic mean of the 18 rows of domain failure rates, and it is not a guarantee of clinical safety.

Sources: [1](https://www.vals.ai/home) (accessed 2026-11-08， ) ; [2](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 争议与已知问题

Results come from simulated conversations and cannot cover every real interaction; a branch occurs only when the model creates the corresponding turning point; filtering and exclusion affect coverage.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Derivative benchmarks

A check against the existing 100 slugs found no older version of the same name; an evaluation implementation or a component score is not counted again as a new benchmark.

Note: The editorial conclusion on deduplication; relations among versions follow the dedicated account below.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (access date, not the experiment run date)

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 官方榜单入口

https://www.vals.ai/benchmarks/mental-health

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 第三方入口

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 可核验结果

- {"rank": "No cross-protocol rank", "model": "GPT-6.1 Sol", "score": {"urgent_safety_failure_percent": 15, "health_advice_failure_percent": 9, "relationship_boundaries_failure_percent": 19}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "GPT-5.6 Luna", "score": {"urgent_safety_failure_percent": 23, "health_advice_failure_percent": 21, "relationship_boundaries_failure_percent": 35}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Claude Sonnet 5.5", "score": {"urgent_safety_failure_percent": 23, "health_advice_failure_percent": 43, "relationship_boundaries_failure_percent": 37}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Muse Spark 1.3 (Extra High)", "score": {"urgent_safety_failure_percent": 26, "health_advice_failure_percent": 14, "relationship_boundaries_failure_percent": 56}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Qwen 3.8 Max", "score": {"urgent_safety_failure_percent": 26, "health_advice_failure_percent": 35, "relationship_boundaries_failure_percent": 51}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Claude Opus 5.5", "score": {"urgent_safety_failure_percent": 27, "health_advice_failure_percent": 44, "relationship_boundaries_failure_percent": 25}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "DeepSeek V4.1 Flash", "score": {"urgent_safety_failure_percent": 31, "health_advice_failure_percent": 41, "relationship_boundaries_failure_percent": 51}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Mistral Large 4 Preview", "score": {"urgent_safety_failure_percent": 33, "health_advice_failure_percent": 53, "relationship_boundaries_failure_percent": 19}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Muse Spark 1.3 (Minimal)", "score": {"urgent_safety_failure_percent": 33, "health_advice_failure_percent": 29, "relationship_boundaries_failure_percent": 70}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "MiMo v2.6 Pro", "score": {"urgent_safety_failure_percent": 40, "health_advice_failure_percent": 57, "relationship_boundaries_failure_percent": 56}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Kimi K3", "score": {"urgent_safety_failure_percent": 44, "health_advice_failure_percent": 61, "relationship_boundaries_failure_percent": 63}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Grok 4.7", "score": {"urgent_safety_failure_percent": 44, "health_advice_failure_percent": 39, "relationship_boundaries_failure_percent": 48}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Grok 4.5", "score": {"urgent_safety_failure_percent": 50, "health_advice_failure_percent": 47, "relationship_boundaries_failure_percent": 65}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "GLM 5.3", "score": {"urgent_safety_failure_percent": 51, "health_advice_failure_percent": 70, "relationship_boundaries_failure_percent": 64}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Gemini 3.6 Flash", "score": {"urgent_safety_failure_percent": 52, "health_advice_failure_percent": 68, "relationship_boundaries_failure_percent": 70}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Gemini 4 Argon", "score": {"urgent_safety_failure_percent": 53, "health_advice_failure_percent": 71, "relationship_boundaries_failure_percent": 66}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "MiniMax M3", "score": {"urgent_safety_failure_percent": 54, "health_advice_failure_percent": 49, "relationship_boundaries_failure_percent": 53}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}
- {"rank": "No cross-protocol rank", "model": "Gemini 3.8 Flash", "score": {"urgent_safety_failure_percent": 56, "health_advice_failure_percent": 69, "relationship_boundaries_failure_percent": 63}, "metric": "Failure rate by domain (%, lower is better; not combined into an overall ranking)", "track": "Vals official; no teen-aware system prompt; 17 models and 18 configurations", "source_url": "https://www.vals.ai/benchmarks/mental-health", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "source_update_date": "2026-10-13"}

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， ) ; [2](https://www.vals.ai/home) (accessed 2026-11-08， )

### 榜单覆盖边界

The scores of 18 configurations across three domains are kept in full. All of them are on the track without a teen-aware prompt, and no overall ranking is imposed. For the other prompt condition, only the overall failure rate given on the official site, 43.3%→24.9%, is included; per-model values are not estimated by reading a figure. Entries for an independent paper, the code, and the HF dataset card remain Unverified.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， ) ; [2](https://www.vals.ai/home) (accessed 2026-11-08， )

## Contact

### 公开研究联系

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 公开反馈渠道

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 官方社交账号

https://x.com/ValsAI

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 联系方式原则

Only official public project channels are recorded; fictional cases and simulated dialogues are not treated as real medical records of minors.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Original files

### 论文原件

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 原始PDF地址

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 原始文件SHA-256

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### 原始文件字节数

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Folder

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

### Other documents

- {"type": "Official introduction/protocol", "url": "https://www.vals.ai/benchmarks/mental-health"}

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )

## Changelog

Latest review
Latest review

Sources: [1](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， ) ; [2](https://www.vals.ai/benchmarks/mental-health) (accessed 2026-11-08， )
