# Code Migration v1.1

> Benchmark Constitution, in-depth verification snapshot 2026-11-07. Unverified is not the same as Not disclosed; the collection date is not the leaderboard update time.

Vals Code Migration v1.1 tests whether behavior is preserved after a complete program is migrated: 30 CLI repositories are each migrated to four other languages, plus 10 COBOL→Java repositories. The main score weights 40 source repositories equally, and it is not a simple equal weighting of 130 migrations; code quality such as readability is only an independent diagnostic.

Basis of the reading guide: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07); [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Basic information

**简称**：Code Migration v1.1

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**全称**：Code Migration v1.1

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The official name is kept; the paper title is not fabricated as a full name.

**基准版本**：v1.1

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**论文版本**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**发布日期**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：2026-10-30 on the page is the update date of this leaderboard; it is not sufficient to verify the first-release date of v1.1.

**主板块**：代码

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：Benchmark Constitution editorial classification.

**领域**：代码

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**许可与范围**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**论文/技术报告**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**代码**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**数据**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**主页**：https://www.vals.ai/benchmarks/code-migration-v1-1

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**论文标题**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

## Origin and maintenance

**发起/作者单位**：Vals AI

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**合作关系**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**作者**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**维护方**：Vals AI

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**资助**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

## Design goals

**测量能力**：Migrate a complete runnable program to another language and faithfully reproduce its behavior, including modernization of legacy COBOL.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**针对的不足**：Short code translation cannot represent repository-level CLI migration or stateful legacy business systems.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Construction

**材料来源**：CLI covers 30 open-source repositories; COBOL covers 10 repositories, mixing open-source programs with business systems synthesized for this benchmark.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**出题背景**：Vals AI built an engineering-migration benchmark; the official method states that the COBOL portion includes business systems synthesized for the evaluation, and the backgrounds of the specific question writers remain Unverified.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**审核**：An independent anti-cheating review is carried out before hidden-behavior tests are scored; the target language is checked, and wrapping the original program, copying reference artifacts, or hardcoding the expected output is rejected.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**质控**：Before the hidden-behavior tests, anti-cheating checks are applied: wrapping the original program, copying reference material, and hard-coded output are forbidden, and the target language is checked.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**去污染边界**：Hidden behavior tests are not shown to the model; the source repository itself is public, which cannot guarantee that pretraining did not see it.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Data format

**规模与统计口径**：For CLI, 30 source repositories are each migrated to 4 other languages, 120 migrations in all; COBOL→Java adds another 10 repositories. The headline weights 40 source repositories equally, not a simple equal weight over 130 tasks.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**任务形式**：A source program and instructions are provided; a target-language implementation and a Dockerfile are submitted.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**模态**：代码；文本；CLI执行

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**语言**：CLI source/target Python, Java, Kotlin, Rust, and C++; COBOL→Java is also included.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**难度**：Cross-language migration of complete CLI repositories; COBOL→Java covers file formats, batch processing, terminal interfaces, and persistent state. This is not the same as translation at the level of a function, and the official source does not give a single numeric level of difficulty.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**公开/保留划分**：30 CLI source repositories come from open-source projects, and COBOL is a mix of open-source and synthetic material; hidden behavioral tests are explicitly withheld from the model. Authorization to download the full questions and the dataset remains Unverified.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Evaluation

**指标**：Hidden-test pass rate (%); code quality is diagnosed separately and does not affect the main score.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**评分**：A submission is built as a Docker image and run on hidden tests; the CLI first takes the mean of 4 targets in each source repository, then weights 40 source repositories equally, with a CLI:COBOL weight of 3:1. A submission that cheats scores 0.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**提示与运行设定**：v1.1 uses a unified Pi agent harness and an offline sandbox, and it provides the source program and the task instructions. The specific token and time limits are Unverified.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**脚本/运行入口**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**可比性**：v1.1 replaces mini-SWE-agent with Pi and revises the hidden tests; the tasks are unchanged, but the scores cannot be compared directly with those of v1.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**当前版本证据**：version：v1.1；heat_confidence：B；evidence_2026_h2：url：https://www.vals.ai/benchmarks/code-migration-v1-1；date：2026-11-07；date_type：observed_on；note：The Vals leaderboard explicitly records an update on 2026-10-30 listing 29 models. Heat B: a current leaderboard mainly from a single organization, not described as rapid growth across the industry.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The Vals leaderboard explicitly records an update on 2026-10-30 listing 29 models. Heat B: a current leaderboard mainly from a single organization, not described as rapid growth across the industry.

**修订历史**：v1.1 replaces the harness with Pi and revises the hidden tests; the independent paper and the revision history are Unverified.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**饱和**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**争议与局限**：Passing a test indicates only the behavior under test. Readability, documentation, file structure, and language conventions are separate review dimensions, and a hidden-test score cannot be treated as code quality.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**派生/去重**：v1.1 keeps the tasks of v1, changes to the Pi harness, and revises the hidden tests; it is retained as a protocol version. v1 and v1.1 are not counted as two independent benchmarks.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Leaderboard snapshot

**快照日**：2026-11-07

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**官方榜**：https://www.vals.ai/benchmarks/code-migration-v1-1

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

**独立评测**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

### 分轨结果（不合并来源/题集/协议）

**Vals / v1.1 / Overall**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | Claude Sonnet 5.5 | 86.88 | hidden-test pass rate (%) |
| 2 | Claude Opus 5.5 | 81.01 | hidden-test pass rate (%) |
| 3 | GPT-6 Astra | 80.58 | hidden-test pass rate (%) |
| 4 | GPT-6.1 Sol | 77.32 | hidden-test pass rate (%) |
| 5 | Wonder | 72.36 | hidden-test pass rate (%) |
| 6 | Gemini 4 Argon | 70.8 | hidden-test pass rate (%) |
| 7 | DeepSeek V4.1 Flash 1017 | 67.52 | hidden-test pass rate (%) |
| 8 | Wonder Full | 62.79 | hidden-test pass rate (%) |
| 9 | DeepSeek V4.1 Flash | 58.94 | hidden-test pass rate (%) |
| 10 | Qwen 3.8 Max 0902 | 57.19 | hidden-test pass rate (%) |
| 11 | GLM 5.3 | 55.07 | hidden-test pass rate (%) |
| 12 | Grok 4.7 | 53.22 | hidden-test pass rate (%) |
| 13 | Claude Haiku 5.5 | 52.36 | hidden-test pass rate (%) |
| 14 | DeepSeek V4 Pro 0813 | 51.99 | hidden-test pass rate (%) |
| 15 | GLM 5.3 Flash | 51.65 | hidden-test pass rate (%) |
| 16 | MiMo V2.6 Pro | 48.79 | hidden-test pass rate (%) |
| 17 | Step 5 Preview | 47.0 | hidden-test pass rate (%) |
| 18 | GPT-6 Luna | 46.67 | hidden-test pass rate (%) |
| 19 | Hy4 Preview | 45.36 | hidden-test pass rate (%) |
| 20 | MiMo V2.6 Flash | 39.55 | hidden-test pass rate (%) |
| 21 | Mercury 3 | 39.26 | hidden-test pass rate (%) |
| 22 | Gemini 3.8 Flash | 38.65 | hidden-test pass rate (%) |
| 23 | Kimi K3 | 28.59 | hidden-test pass rate (%) |
| 24 | Muse Spark Open | 26.89 | hidden-test pass rate (%) |
| 25 | Beam 1.0 | 22.85 | hidden-test pass rate (%) |
| 26 | MiniMax-M3 | 20.9 | hidden-test pass rate (%) |
| 27 | Nemotron 3.5 Super VL | 16.44 | hidden-test pass rate (%) |
| 28 | Inkling Small | 10.43 | hidden-test pass rate (%) |
| 29 | Inkling | 8.82 | hidden-test pass rate (%) |

Sources: [https://www.vals.ai/benchmarks/code-migration-v1-1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：All 29 models in the current official Overall table are entered. Scores keep the percentage precision of the webpage and are not inverted into a simple mean over 130 tasks. The page is marked as updated on 2026-10-30. CLI, COBOL, and effort curves are not mixed into the Overall ranking.

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Contact

**公开研究邮箱**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**Issues**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**公开社区**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**隐私原则**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

## Original files

**PDF**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**原件SHA-256**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**PDF字节数**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**目录**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

核验说明：The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

**其他文档**：type：Official web-page methods and leaderboard (not a PDF)；url：https://www.vals.ai/benchmarks/code-migration-v1-1

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

** PDF**：待核实

Sources: [1](https://www.vals.ai/benchmarks/code-migration-v1-1) (accessed 2026-11-07)

## Changelog

- date：2026-11-07；；change：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。
- date：2026-11-07；；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
