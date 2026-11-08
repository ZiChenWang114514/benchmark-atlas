# MirrorCode

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MirrorCode将软件工程评测从修改一个补丁推进到复刻完整CLI程序：模型只能查询可执行的黑箱、查看文档与可见测试，再独立实现同样行为。全25程序论文实验与当前15程序双语言在线榜是两套配置。严格的100%-solve指标不等于代码质量评分，也不能与99%用例通过率混用。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Short name

MirrorCode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Full name

MirrorCode

> The official name is kept; the paper title is not fabricated as a full name.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Benchmark version

pyproject.toml on the current main is 0.1.193; the run CSV also contains 0.1.198. The two are different snapshots of the code, so it cannot be asserted from them that main is the latest version that has been deployed.

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/pyproject.toml)（访问 2026-11-08）；[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### Paper version

arXiv v2

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### Release date

2026-06-29 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### Section

Code

> Benchmark Constitution editorial classification.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Field tags

- 代码

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 许可证与权利边界

MIT (official repository LICENSE and pyproject.toml); it does not automatically cover the preexisting rights of each target upstream project.

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/pyproject.toml)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2606.30182

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Code repository

https://github.com/epoch-research/MirrorCode/

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 数据集入口

https://github.com/epoch-research/MirrorCode/

> Public task definitions are released in the same repository as the harness; this is not an independent HF dataset.

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/README.md)（访问 2026-11-08）

### Official homepage

https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Paper title

MirrorCode: AI can rebuild entire programs from behavior alone

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

Epoch AI; developed jointly with METR

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 合作方

METR

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Authors

- Tom Adamczewski
- David Owen
- David Rein
- Florian Brand
- Giles Edkins
- Allen Hart
- Daniel O’Connell

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### Maintainer

Epoch AI

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Funders

METR grant

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

## Design goals

### Abilities measured

A complete CLI program is reconstructed end to end from program behavior and documentation, measuring long-horizon autonomous programming.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Design background

Short patch questions and one-off demonstrations with human guidance make it difficult to compare, systematically, autonomous implementation of a whole program.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Construction

### Question sources

25 target programs: Unix utilities, serialization, query, bioinformatics, interpreters, static analysis, cryptography, and compression.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 出题与审阅者背景

Program-task contributors and the Epoch AI/METR evaluation research team.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Review process

Task contributors review the tests; they check whether tests unsolved by every model are reasonably solvable.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Quality control

Scoring runs in a separate sandbox, with no reference binary; outputs are compared byte for byte, and explicit red-teaming for cheating is carried out.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 去污染及其证据边界

During development there is no source code and no network; hidden tests prevent table lookup. Open-source code may still have been seen in pretraining, so a contribution from memorization cannot be ruled out.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Data format

### 题量与版本口径

The full set has 25 programs; the current leaderboard takes the 15 Medium+Large programs, two languages each, for 30 tasks in total, with 3 runs per task.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Question types

A CLI black-box oracle, documentation, and visible input-output examples; code in the target language is submitted.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Modalities

- 文本
- 代码
- Program input and output

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Languages

The full set supports Python, C, Rust, Go, OCaml, and Ada; the current leaderboard's 2L mapping is mainly Go/Ada.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Difficulty

Small, Medium, and Large buckets; the current leaderboard does not include Small.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Public and hidden splits

22 of 25 target programs are released, for 132 language-task instances in total; 3 targets are private. Each program also contains hidden tests, 34% on average.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Evaluation

### Metrics

100%-solve rate: every attempt must pass all end-to-end tests; the average is taken across targets and runs.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 评分方法

The scoring harness compares stdout, stderr, and exit status outside an independent container. A 100%-solve requires every end-to-end case to pass. A 99%-solve is only a partial-implementation metric reported separately by the paper.

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 运行与提示设置

The current leaderboard is ML,+Private,2L: 3 times per question, with 100 × 10^8 tokens and 7 days each time; an Inspect ReAct scaffold, offline Docker, and support for shell, text_editor, evaluate_testcases, and submit.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 官方脚本

The official open-source scaffold and 22 target programs; the repository entry is given in the basic information.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 可比性警示

The current leaderboard has 15 programs × 2 languages and is not directly comparable with the paper's 25 programs, different language counts, and budget settings; the CSV also differs in task version.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

- **repository_package**：0.1.193 (current main)
- **observed_run_versions**：- 0.1.198；- 0.1.200
- **leaderboard_configuration**：ML,+Private,2L; kept separate from the paper's full 25-program protocol

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/pyproject.toml)（访问 2026-11-08）；[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 论文修订及历史证据

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）；[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### Saturation

In the experiment on all 25 programs in the paper, 8/25 never reached a 100% pass and 4/25 never reached a 99% pass; this belongs to the historical experiments in the paper. Scores on the current ML,+Private,2L leaderboard are listed separately, and saturation is not inferred across protocols.

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 污染、争议与限制

Memory screening in the original paper found potential evidence of memorization on 17 targets, but it also observed unmemorized targets being solved and memorized targets left unsolved. Offline black-box evaluation and hidden tests mainly suppress runtime cheating, and they do not prove the absence of pretraining contamination. They measure only function, not code quality.

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 衍生与版本关系

The paper lists ProgramBench as independent related work from the same period and states that the budget, the prompt, and the target coverage differ; it is not a new version of MirrorCode.

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### Official entry

https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 第三方覆盖入口

https://epoch.ai/data/benchmarks.csv

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Epoch run CSV / ML,+Private,2L

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Claude Opus 5.5 (high) | 0.7889 | solve_at_100 / proportion (0–1) |
| Claude Fable 5.1 (high) | 0.733 | solve_at_100 / proportion (0–1) |
| Claude Fable 5 (high) | 0.638888888888889 | solve_at_100 / proportion (0–1) |
| Gemini 4 Argon (high) | 0.5888888888888889 | solve_at_100 / proportion (0–1) |
| GPT-6 Astra (high) | 0.467 | solve_at_100 / proportion (0–1) |
| Gemini 3.7 Flash (high) | 0.4111111111111111 | solve_at_100 / proportion (0–1) |
| Grok 4.6 (xhigh) | 0.4111111111111111 | solve_at_100 / proportion (0–1) |
| Grok 4.5 (high) | 0.32222222222222224 | solve_at_100 / proportion (0–1) |
| Claude Opus 4.7 (high) | 0.3111111111111111 | solve_at_100 / proportion (0–1) |
| GPT-6 Luna (max) | 0.26666666666666666 | solve_at_100 / proportion (0–1) |
| GPT-5.6 Sol (high) | 0.2 | solve_at_100 / proportion (0–1) |
| GPT-5.4 (high) | 0.15555555555555556 | solve_at_100 / proportion (0–1) |
| GPT-5.5 (high) | 0.1 | solve_at_100 / proportion (0–1) |
| Gemini 3.1 Pro Preview (high) | 0.08888888888888888 | solve_at_100 / proportion (0–1) |
| GPT-5 (high) | 0.044444444444444446 | solve_at_100 / proportion (0–1) |

- **Claude Opus 5.5 (high)**：- **rank**：1；- **stderr**：0.0788；- **run_id**：mirrorcode-ml-2l-claude-opus-5-5；- **run_started_at**：2026-09-23；- **task_version**：0.1.198；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Claude Fable 5.1 (high)**：- **rank**：2；- **stderr**：0.0917；- **run_id**：mirrorcode-ml-2l-claude-fable-5-1；- **run_started_at**：2026-09-10；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Claude Fable 5 (high)**：- **rank**：3；- **stderr**：0.10404092940368063；- **run_id**：mirrorcode-ml-2l-claude-fable-5；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Gemini 4 Argon (high)**：- **rank**：4；- **stderr**：0.1171381252539371；- **run_id**：h7xMzFUTMGSGqUSKUpxkUW；- **run_started_at**：2026-10-14；- **task_version**：0.1.200；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **GPT-6 Astra (high)**：- **rank**：5；- **stderr**：0.1186；- **run_id**：mirrorcode-ml-2l-gpt-6-astra；- **run_started_at**：2026-08-31；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Gemini 3.7 Flash (high)**：- **rank**：6；- **stderr**：0.12157113738962926；- **run_id**：eeq6feqZLzfjfVsx4aeAWL；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Grok 4.6 (xhigh)**：- **rank**：7；- **stderr**：0.1101546131612538；- **run_id**：Hoz4Uioui4GNZaLD6fiAvD；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Grok 4.5 (high)**：- **rank**：8；- **stderr**：0.10723394129558436；- **run_id**：fiqzdAtVJVP9wdMT2QFeUn；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Claude Opus 4.7 (high)**：- **rank**：9；- **stderr**：0.09036473223803354；- **run_id**：mirrorcode-ml-2l-claude-opus-4-7；- **run_started_at**：2026-08-12；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **GPT-6 Luna (max)**：- **rank**：10；- **stderr**：0.09026709338484401；- **run_id**：WQ4gVVhGBfWoRkRwUvNYgs；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **GPT-5.6 Sol (high)**：- **rank**：11；- **stderr**：0.09229582069908972；- **run_id**：mirrorcode-ml-2l-gpt-5-6-sol；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **GPT-5.4 (high)**：- **rank**：12；- **stderr**：0.0770945044100374；- **run_id**：mirrorcode-ml-2l-gpt-5-4；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **GPT-5.5 (high)**：- **rank**：13；- **stderr**：0.06042179781166438；- **run_id**：mirrorcode-ml-2l-gpt-5-5；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **Gemini 3.1 Pro Preview (high)**：- **rank**：14；- **stderr**：0.04561939004190448；- **run_id**：mirrorcode-ml-2l-gemini-3-1-pro-preview；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.
- **GPT-5 (high)**：- **rank**：15；- **stderr**：0.034375250520170986；- **run_id**：Th39ihgvLFnsDGMed7Q55b；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：Interpreted by the configuration of the current leaderboard on the official site; task versions missing from the CSV are not invented and cannot be treated as repeated measurements of the same version.

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

> The original decimal strings in the CSV are retained and were not rounded; rank is only the display order of runs included in that CSV.

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖范围与时效

Runs of MirrorCode already included in the CSV are transcribed in full; Epoch is a co-creator, not an independent third party retesting the work. The time at which a run starts differs from the date on which the leaderboard page is updated; the missing task version is Unverified.

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Contact

### 公开工作邮箱

- tom@epoch.ai

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### 公开反馈

https://github.com/epoch-research/MirrorCode/issues

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 官方社交

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 隐私边界

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2606.30182

> Entry point for the original paper PDF; not downloaded or uploaded; hash and byte count Unverified.

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### PDF SHA-256

d0ab2a256a1ab9cee34842128aaee124c38bc2f43e95571d37aa1bec42df9e37

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### PDF bytes

660665

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### Folder

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 其他官方材料

- - **type**：Official web-page methods and leaderboard (not a PDF)；- **url**：https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### PDF归档

Unverified

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/README.md)（访问 2026-11-08）
