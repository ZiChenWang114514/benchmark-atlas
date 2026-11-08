# Terminal-Bench-Science

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

Terminal-Bench-Science builds verifiable terminal workflows around researchers' real work, covering the life sciences, physics, Earth science, mathematics, and engineering. This page interprets the AA scores strictly with the released 0.1.0 set of 70 questions; the 86 questions under development on main, and 2.0 in preparation, do not change the historical denominator.

Source: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08)

## Basic information

### Short name

Terminal-Bench-Science

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Full name

Terminal-Bench-Science

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Benchmark version

0.1.0 (the release explicitly identified by AA; the official site abbreviates it as 0.1)

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Paper version

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### Release date

v0.1.0: 2026-08-26 19:24:33 (GitHub published_at); the announcement date is separately 2026-08-27, and the two are not treated as one event.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) (accessed 2026-11-08， )

### Section

综合科学

Note: A general-science benchmark. It covers several disciplines and is not filed under physics.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### Field tags

- 跨学科科学
- 化学
- 生物与医学
- 地球与天文
- 数学
- 工程

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### 许可与适用范围

Apache-2.0 (current repository LICENSE and the software citation in the README); third-party data included in each task should still be checked separately.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science/blob/main/LICENSE) (accessed 2026-11-08， )

### Paper

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### Code repository

https://github.com/harbor-framework/terminal-bench-science

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### 数据地址

https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?tab=tasks

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Official homepage

https://terminal-bench-science.ai/

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### Paper title

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

## Origin and maintenance

### 机构与发起关系

Stanford University researchers and the Terminal-Bench / Harbor team

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Partner organizations

- Laude Institute
- SAIL
- HAI
- AIMS
- IFML
- Allen Institute
- Ai2

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Authors

Terminal-Bench-Science Team; the release article is signed Steven Dillmann

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Current maintainer

The Terminal-Bench / Harbor team and the community of scientific contributors.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### 资助与支持

Laude Slingshots, Snorkel AI Open Benchmarks Grants, and others; API credits are understood separately from the standing of a research collaboration.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

## Design goals

### Abilities measured

Completes real scientific-research workflows in a terminal, producing analyses, simulations, proofs, code, and data products.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Design background

Research tasks contributed by practicing scientists, rather than textbook recall questions, are used to measure verifiable ability to carry out research.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

## Construction

### 题目或数据来源

Scientific researchers propose tasks from their own work, and the tasks are built in public through GitHub proposals and PRs.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### 出题背景

Researchers across the life, physical, Earth, mathematical, and engineering sciences.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Review process

Implemented after review of the proposal; domain review, technical review, and a final bar-raiser quality check.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### Quality control

Proposal, then implementation, then review: automatic checks, parallel domain and technical review, and final approval by a bar-raiser. This includes oracle pass and no-op failure, and adversarial checks for cheating. The official recommendation is to run the oracle 5 times in the target sandbox first, to confirm that the environment is stable.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science) (accessed 2026-11-08， )

### 去污染与泄漏

The official page carries a canary statement forbidding inclusion of the benchmark data in training corpora; the statement cannot be read as proof that there is no contamination.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

## Data format

### Size

The fixed v0.1.0 release has 70 questions: life 19, physics 17, mathematics 17, engineering 9, and earth 8; the count of 86 questions in the current main README belongs to the development state, and it must not be used to change the denominator of the 0.1.0 leaderboard.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) (accessed 2026-11-08， ) ; [2](https://github.com/harbor-framework/terminal-bench-science) (accessed 2026-11-08， ) ; [3](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08， )

### Question types

Terminal workflows such as scientific data analysis, statistical inference, simulation, optimization, proof, image reconstruction, and signal processing.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

### Modalities

- 文本
- 代码
- Scientific data/computational artifacts

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

### Languages

The official public task descriptions and the AA examples are in English; the workflows also include Python, the command line, and domain data files, and this is not a pure language question-answering set.

Source: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08)

### Difficulty

Domain experts propose real research workflows that must be objectively verifiable and challenging for frontier agents; no unified difficulty-grading scale has been released officially.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science) (accessed 2026-11-08， )

### 数据划分

The 0.1.0 tasks are public; the formal train/validation/hidden-test split is Unverified.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

## Evaluation

### Metrics

Test-suite pass rate / resolution rate, pass@1.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

### Scoring

Every task must pass all tests; AA uses an independent verifier container.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

### 提示与运行设置

AA: 70 tasks × 3 repeats, mini-swe-agent, at most 1000 steps; the official-site launch uses each vendor's CLI and must be kept on a separate track.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

### 评测脚本

The Harbor runtime framework and the official task repository; it can run on Modal or in other environments that Harbor supports.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

### 可比性提醒

Results released on the official site, results from the AA unified harness, and vendor-self-reported results cannot be treated as the same leaderboard; the Science Index composite score is not this individual score.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07， )

## Current status

### Date checked

2026-11-08

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-08， )

### 数据版本与更新

The latest visible formal release is v0.1.0, with 70 questions; main already has 86 questions, and the call for 2.0 submissions is still open. The question count on a development branch cannot be treated as a released 2.0.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0) (accessed 2026-11-08， ) ; [2](https://github.com/harbor-framework/terminal-bench-science) (accessed 2026-11-08， )

### 论文修订记录

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### 饱和证据与局限

AA’s fixed high on 0.1.0 / 70 questions is 64.8%; this is the average single-run success rate under one mini-swe-agent, and it cannot be compared in the same ranking with different CLI systems on the official site or with the 86 questions on main.

Source: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08)

### 争议与已知问题

The official requirement is that a public task carry a canary, and reports are welcome of taking the answer directly, of ambiguous instructions, of a verifier judging wrongly, and of an unstable oracle; a mark against contamination is not the same as a confirmed absence of contamination.

Sources: [1](https://github.com/harbor-framework/terminal-bench-science) (accessed 2026-11-08， )

### 衍生或后继基准

An independent suite of scientific workflows, not an alias of Terminal-Bench 4.0; development of 0.2 is mentioned in the launch announcement, which is not a basis for asserting an official release.

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Source: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08)

### 官方榜单入口

https://terminal-bench-science.ai/

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### 第三方入口

https://artificialanalysis.ai/evaluations/terminal-bench-science

Sources: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-07， )

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| AA unified harness / 0.1.0 | 1 | Gemini 4 Carbon (High) | 64.8 | pass@1 (%) | 0.1.0 / 70 tasks；mini-swe-agent；3 repeats/task | [Unverified (web page does not mark a run date for each result)](https://artificialanalysis.ai/evaluations/terminal-bench-science)；采集2026-11-08 |
| AA unified harness / 0.1.0 | 2 | GPT-6 Astra (Max) | 63.3 | pass@1 (%) | 0.1.0 / 70 tasks；mini-swe-agent；3 repeats/task | [Unverified (web page does not mark a run date for each result)](https://artificialanalysis.ai/evaluations/terminal-bench-science)；采集2026-11-08 |
| AA unified harness / 0.1.0 | 3 | Gemini 4 Carbon (Medium) | 62.4 | pass@1 (%) | 0.1.0 / 70 tasks；mini-swe-agent；3 repeats/task | [Unverified (web page does not mark a run date for each result)](https://artificialanalysis.ai/evaluations/terminal-bench-science)；采集2026-11-08 |

Source: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08)

### 榜单覆盖边界

The top three explicitly reported on the AA page. The first screen of the official site did not return CLI system scores. The 70 questions fixed at 0.1.0 are the ones used. The 86 questions on main, and 2.0, which is in preparation, are not part of this snapshot. No independent arXiv paper linked from the official site was found. A software DOI is not presented as the paper PDF.

Source: [1](https://artificialanalysis.ai/evaluations/terminal-bench-science) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

- stevendi@stanford.edu

Sources: [1](https://terminal-bench-science.ai/run) (accessed 2026-11-07， )

### 公开反馈渠道

https://github.com/harbor-framework/terminal-bench-science/issues

Sources: [1](https://github.com/harbor-framework/terminal-bench-science) (accessed 2026-11-08， )

### 官方社交账号

https://discord.com/invite/2Pe5uWGcV3

Sources: [1](https://terminal-bench-science.ai/run) (accessed 2026-11-07， )

### 联系方式/隐私原则

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

## Original files

### 原始PDF

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### PDF SHA-256

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### PDF bytes

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### Folder

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

### Other documents

- {"type": "Official software-release citation (not a paper PDF)", "url": "https://doi.org/10.5281/zenodo.22110253"}

Sources: [1](https://terminal-bench-science.ai/announcement) (accessed 2026-11-07， )

### 论文原件

Unverified

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-07， )

## Changelog

Latest review
Latest review

Sources: [1](https://terminal-bench-science.ai/) (accessed 2026-11-08， )
