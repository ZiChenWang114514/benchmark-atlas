# GAIA

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

What the original GAIA measures is tool-assisted information lookup and short-answer tasks. A high score cannot be equated with broad general agent ability. The current leaderboard scores submitted answers with the official scorer, and that does not mean the maintainer fully reran the systems under evaluation. The later Gaia2 tests dynamic read-and-write tasks separately.

Latest review

## Basic information

**简称**：GAIA

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07)

**全称**：GAIA: a benchmark for General AI Assistants

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**基准版本**：The original 466 GAIA questions; data released in 2023

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**论文版本**：arXiv v1

核验说明：A paper revision is not the same as a dataset version.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**发布日期**：2023-11-22 05:34:47

核验说明：The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**主板块**：Agent

核验说明：Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**领域标签**：General assistants and tool use

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**许可证与授权边界**：Unverified; the current official card explicitly requires agreement to the gating conditions and prohibits forwarding the question bank to a location that can be crawled or that has no gate, but a unified copyright license is not confirmed from that. The CC-BY-4.0 of GAIA2 does not extend to GAIA.

状态：待核实。

Sources: [1](https://huggingface.co/datasets/gaia-benchmark/GAIA) (accessed 2026-11-07)

**论文或技术报告**：https://arxiv.org/abs/2311.12983

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**官方代码**：https://huggingface.co/spaces/gaia-benchmark/leaderboard/tree/main

核验说明：Official evaluation Space source code, including app.py and scorer.py; it is not an inferred third-party GitHub repository.

Sources: [1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07); [2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/README.md) (accessed 2026-11-07)

**数据地址**：https://huggingface.co/datasets/gaia-benchmark/GAIA

Sources: [1](https://huggingface.co/datasets/gaia-benchmark/GAIA) (accessed 2026-11-07)

**官方主页**：https://huggingface.co/gaia-benchmark

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07)

**论文题名**：GAIA: a benchmark for General AI Assistants

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

## Origin and maintenance

**发起方**：The author teams of Meta FAIR / GenAI, Hugging Face, and AutoGPT (affiliation and project definition)

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**协作与机构边界**：Surge AI provides paid human annotation.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**作者**：Mialon, Grégoire；Fourrier, Clémentine；Swift, Craig；Wolf, Thomas；LeCun, Yann；Scialom, Thomas

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**维护方**：The official Hugging Face organization gaia-benchmark.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**资助方**：待核实

状态：待核实。

核验说明：The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

## Design goals

**测量能力**：General-assistant capability that combines realistic information seeking, multimodal understanding, web-page access, tools, and multi-step reasoning.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**相对既有评测的缺口**：Tasks that people finish easily but that require tools to be combined may reveal the limits of an assistant system more clearly than isolated professional-knowledge questions.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

## Construction

**题目来源**：Human-designed verifiable real-world questions; answers are usually short and definite, and some include attachments.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**出题与研究背景**：The research authors and Surge AI annotators recruited for pay; not every question writer is called an expert.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**审核流程**：Two independent verifiers besides the creator review it; if they disagree, it is revised or discarded.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**质量控制**：Aims at unique or stable answers that a person can complete; 3 tiers are set by the number of reasoning steps and by tool complexity.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**去污染与泄漏边界**：Answers are prevented from being retrieved directly as plain text on the web, and test answers are hidden; once questions are public they may still enter later training.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

## Data format

**规模与口径**：466 manually written questions; answers are public for 166 development questions, and answers are hidden for 300 test questions.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**任务类型**：Open questions with short answers, which may require the web, files, vision, and computation.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**模态**：文本；Image and file attachments (depending on the question)；工具/网页

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**语言**：英语为主。

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**难度**：The three levels are a coarse division by the tools and steps a person needs: Level1 is usually at most 1 tool and 5 steps, Level2 is about 5–10 steps and combines tools, and Level3 is a longer sequence of operations; these are not strict thresholds on the number of steps.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**公开与隐藏划分**：466 questions: validation 165, with Level1/2/3 at 53/86/26, and test 301, at 93/159/49. The test answers are held by the official scoring endpoint. The current HF question bank requires the gating conditions to be accepted, and it must not be forwarded to a place that can be crawled.

Sources: [1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07); [2](https://huggingface.co/datasets/gaia-benchmark/GAIA) (accessed 2026-11-07)

## Evaluation

**指标**：Accuracy, reported by Level and overall.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**评分方式**：Official scorer.py: a number has $, %, and commas removed and is then converted to float for strict equality; a list is split on commas or semicolons, and the length and the order must be equal; a string has spaces removed, has punctuation removed by default, and is lowercased, and is then matched exactly. There is no LLM judge.

Sources: [1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/scorer.py) (accessed 2026-11-07)

**提示与运行设置**：The original protocol is zero-shot; a complete assistant system may use tools and must report the tools, the budget, and attachment handling.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**官方复现入口**：https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/scorer.py

Sources: [1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/scorer.py) (accessed 2026-11-07); [2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07)

**可比性警告**：validation and test, the overall score and each Level, and differing multimodal permissions cannot be placed on one ranking; a score from an LLM alone and a score from a full agent system are not treated as equivalent.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07)

**数据及热度证据**：```json
{
 "version": "The original 466 GAIA questions; data released in 2023"
 "evidence_2026_h2": [
 {
 "url": "https://arxiv.org/html/2609.19134v1"
 "date": "2026-09-17"
 "note": "ScienceIDE §4.2 and its references explicitly cite GAIA as a prior benchmark for language-model agents and for interactive environments; this is an H2 academic citation, and this paper does not claim to have run the benchmark."
 "date": "2026-09-17"

 }
 {
 "url": "https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet"
 "date": "2026-11-03"
 "note": "In the public result set 2023/test of the official HF leaderboard, the submission record of Keen AgenticOS V1.1 has score 0.9435215946843853; this is evidence of a submission scored by the official scorer."
 }
 ]
 "format_update": "2025-10: the HF dataset was changed to Parquet shards (metadata.parquet and a shard for each level), with the column names unchanged; access to the dataset has been gated."
}
```

核验说明：Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

Sources: [1](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07); [2](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07); [3](https://huggingface.co/datasets/gaia-benchmark/GAIA) (accessed 2026-11-07); [4](https://arxiv.org/abs/2609.19134) (accessed 2026-11-07); [5](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) (accessed 2026-11-07); [6](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07)

**论文与版本历史**：Submission history From: Grégoire Mialon [ view email ] [v1] 2023-11-22 05:34:47 (3,688 KB)

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**饱和程度**：The official leaderboard of test submissions peaks at 94.35%; this reflects results scored automatically by the submission system against hidden answers, it is not a rerun by an independent audit, and it is not sufficient to prove saturation of broad human ability. The human reference of 92% in the original paper cannot be compared with the current system unless the conditions are stated.

Sources: [1](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) (accessed 2026-11-07); [2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07); [3](https://arxiv.org/pdf/2311.12983) (accessed 2026-11-07)

**已知问题与局限**：Changes over time in web content and online tools, later contamination of public questions, and answer normalization all affect reproduction; scores from the original paper cannot be treated as the current capability ceiling.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**后续与衍生**：Gaia2 is a later independent benchmark, released on 2025-09-22, and together with Meta ARE it tests dynamic reading and writing, ambiguity, timing, and noise; it is not an interchangeable version of the original GAIA question bank, and the two leaderboards must not be mixed.

Sources: [1](https://huggingface.co/blog/gaia2) (accessed 2026-11-07)

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07)

**官方入口**：https://huggingface.co/spaces/gaia-benchmark/leaderboard

Sources: [1](https://huggingface.co/spaces/gaia-benchmark/leaderboard) (accessed 2026-11-07)

**第三方入口**：待核实

状态：待核实。

核验说明：The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07)

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | Keen AgenticOS V1.1 | 94.35 | GAIA 2023 test 301 Average score (%) | 2026-11-03 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 2 | Shadow Harness V8.01 | 94.02 | GAIA 2023 test 301 Average score (%) | 2026-10-12 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 2 | Keen AgenticOS V1.0 | 94.02 | GAIA 2023 test 301 Average score (%) | 2026-10-29 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 4 | Ops-Agentic-Search-2.0 | 93.69 | GAIA 2023 test 301 Average score (%) | 2026-09-22 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 5 | CustomGPT.ai Research Lab v44 | 93.36 | GAIA 2023 test 301 Average score (%) | 2026-06-03 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 5 | OmniSeek_Preview_v1.1 | 93.36 | GAIA 2023 test 301 Average score (%) | 2026-10-30 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 7 | 1028-9 | 93.02 | GAIA 2023 test 301 Average score (%) | 2026-10-28 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |
| 当前官方网页榜 | 7 | Shadow Harness V5.01 | 93.02 | GAIA 2023 test 301 Average score (%) | 2026-10-11 | [原始来源](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：The results_public specified by the official Space was retrieved again, sorted by score, multiplied by 100, and kept to two decimal places. The top 8 are listed, and tied scores share a rank. The leader is 94.35%, and the next two entries are 94.02%. date is the submission date of each entry and is not treated as the update date of the leaderboard as a whole; it is not claimed that the submitting party's agent was rerun.

Sources: [1](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet) (accessed 2026-11-07); [2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07)

## Contact

**公开联系邮箱**：gmialon@meta.com；tscialom@meta.com；clementine@huggingface.co

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**Issues或讨论入口**：https://huggingface.co/spaces/gaia-benchmark/leaderboard/discussions

核验说明：Community feedback on the official HF Space; GitHub Issues that do not exist are not fabricated.

Sources: [1](https://huggingface.co/spaces/gaia-benchmark/leaderboard) (accessed 2026-11-07); [2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py) (accessed 2026-11-07)

**官方社交**：待核实

状态：待核实。

核验说明：The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

**隐私政策**：待核实

状态：待核实。

核验说明：The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Sources: [1](https://arxiv.org/abs/2311.12983) (accessed 2026-11-07)

## Original files

**原始PDF**：https://arxiv.org/pdf/2311.12983

核验说明：Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

Sources: [1](https://arxiv.org/pdf/2311.12983) (accessed 2026-11-07)

**PDF SHA-256**：5bf6f968d4f5cd20acdfca6e81e3c9f5277bb66061fad7a02e35442dff812ba0

核验说明：Byte count of the original downloaded PDF, not the size displayed on the arXiv page.

Sources: [1](https://arxiv.org/pdf/2311.12983) (accessed 2026-11-07)

**PDF字节数**：```json
4254059
```

核验说明：Actual downloaded byte count; it does not mean the file was uploaded.

Sources: [1](https://arxiv.org/pdf/2311.12983) (accessed 2026-11-07)

**文件夹**：

**其他官方文档**：

核验说明：The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07); [2](

**论文链接**：

## Changelog

**及历史变更**：```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 "round": "1 / 深度实证复核"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 }
]
```

Sources: [1](https://huggingface.co/gaia-benchmark) (accessed 2026-11-07)
