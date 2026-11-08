# ITBench / ITBench-AA

> Benchmark Constitution, source-by-source in-depth check: 2026-11-08. The collection date does not represent the experiment date; Unverified is not the same as Not disclosed.

The original ITBench framework evaluates diagnosis and repair inside a deployable IT environment, covering SRE, CISO, and FinOps; ITBench-AA measures only offline root-cause analysis on 59 snapshot scenarios. This page keeps the actual repair rate and root-cause entity precision on separate tracks, and the latter cannot be called the success rate of incident repair.

Basis of the reading guide: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-08); [2](https://github.com/itbench-hub/ITBench) (accessed 2026-11-08); [3](https://github.com/itbench-hub/ITBench#scenarios) (accessed 2026-11-08).

## Basic information

### Short name

ITBench / ITBench-AA

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Full name

ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Benchmark version

The original ITBench and the independent AA implementation of 59 scenarios are recorded on separate tracks

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Paper version

arXiv v1

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-08).

### Release date

2025-02-08 (date of the first arXiv draft; not the separate release date of the dataset).

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-08).

### Section

Code

> Benchmark Constitution editorial classification.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

### 领域

```json
[
 "运维"
 "Root-cause analysis"
]
```

> Editorial tags; an empty list means finer-grained tags have not yet been added.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

### 许可与使用范围

The original ITBench repository is Apache-2.0; the license for AA private scenarios cannot be inferred from that.

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/LICENSE) (accessed 2026-11-08).

### 论文入口

https://arxiv.org/abs/2502.05352

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Code

https://github.com/itbench-hub/ITBench

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Dataset

https://github.com/itbench-hub/ITBench#scenarios

> This is a deployable scenario, not a single HF table; the README also links the IBM Enterprise Agents and Benchmarks collection.

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

### Official homepage

https://github.com/itbench-hub/ITBench

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

### Paper title

ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

## Origin and maintenance

### Initiators

IBM; the original paper includes authors from the University of Illinois at Urbana-Champaign

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### 合作与作者单位

Artificial Analysis and the ITBench team share 19 private scenarios for the AA implementation; this is not used to expand the original list of institutional collaborators.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Authors

Saurabh Jha, Rohan Arora, Yuji Watanabe, Takumi Yanagawa, and others; the full list of authors is in the paper.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Maintainer

The ITBench team maintains the original project, and Artificial Analysis maintains the independent ITBench-AA results.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### 资助与资源支持

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

## Design goals

### 测量能力

Real IT automation: SRE incident diagnosis and mitigation, CISO compliance assessment, and FinOps cost optimization. AA focuses on offline root-cause diagnosis for Kubernetes.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### 与既有基准的差异

Distinct from ordinary code generation or a static ticket: it requires an environment, telemetry, fault propagation, and interpretable metrics at task level.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

## Construction

### Question sources

The original SRE is based on real incidents from its own SaaS, CISO is based on the CIS specifications, and FinOps is based on FinOps Foundation capabilities and outcomes.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### 出题者背景

The IBM research and engineering team and researchers at UIUC.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Review process

The original framework deploys a scenario, injects a fault, then checks the target alert, and then runs diagnosis and repair. The SRE material comes from real operations experience and is reproduced through fault mechanisms. AA changes this to a static incident snapshot, judges only the root-cause entity, and does not verify the online fix.

Sources: [1](https://arxiv.org/pdf/2502.05352) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08).

### Quality control

The original framework deploys an environment, injects faults, and asserts alerts; AA instead uses an offline incident snapshot and identifies the root-cause entity.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### 去污染与泄漏控制

The 59 tasks of AA include 40 public and 19 private, which is not the same as the public figure of 11/94 in the original paper.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

## Data format

### 规模与统计口径

The original 94 scenarios: SRE 42, CISO 50, FinOps 2; AA: 59 Kubernetes scenarios, 3 runs per question.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Question types

The original setting carries out tasks by interaction with the environment; AA reads alerts/events/traces/metrics/topology and writes a structured JSON entity for the root cause.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Modalities

```json
[
 "文本"
 "日志"
 "指标"
 "Call trace"
 "拓扑"
 "Structured JSON diagnostics"
]
```

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Languages

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

### Difficulty

Easy/Medium/Hard were originally set by the fault-propagation chain, the operational steps, and technical diversity, and generic code-problem difficulty is not used as a substitute.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### Public and hidden splits

The original paper: 11 open-source examples out of 94 scenarios; the current README lists 6 SRE scenarios / 21 mechanisms, 4 categories of CISO, and 1 FinOps scenario, and the basis of classification differs from the historical question count. AA fixes 40 public scenarios plus 19 private scenarios.

Sources: [1](https://arxiv.org/pdf/2502.05352) (accessed 2026-11-08); [2](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08); [3](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08).

## Evaluation

### Metrics

Original pass@1, fault localization and propagation-chain NTAM, and time spent on diagnosis and repair; AA’s primary metric is Average precision at full recall.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 评分规则

For each AA task, TP/(TP+FP) if FN=0, otherwise 0; LLM-normalized entity matching, then averaged over tasks and over 3 repetitions.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 提示、采样与工具设置

In the Stirrup offline sandbox, AA reads a mounted Kubernetes snapshot, explores with a shell for at most 100 turns, and submits a JSON file.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 官方脚本

AA implementation: https://github.com/ArtificialAnalysis/ITBench-AA. Original project: https://github.com/itbench-hub/ITBench.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 可比性警告

AA covers only offline recognition of the root-cause entity, not an actual rate of successful repair; the 94 scenarios in the original paper and the 59 scenarios in AA cannot have their scores compared directly.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07); [3](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

## Current status

### 核查时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-08); [2](https://github.com/itbench-hub/ITBench) (accessed 2026-11-08).

### 最新数据状态

```json
{
 "version": "The original ITBench and the independent AA implementation of 59 scenarios are recorded on separate tracks"
 "heat_confidence": "B"
 "evidence_2026_h2": [
 {
 "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "AA is currently continuing root-cause analysis across 59 ITBench-AA scenarios."
 }
 ]
}
```

> Heat B: recent heat is supported mainly by one evaluation organization continuing to run and display it, and does not indicate wide adoption across the industry.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07).

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2025-02-08"
 }
]
```

> The original arXiv UTC time has been converted; this does not constitute a dataset version change.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-08).

### 饱和度与证据边界

The current AA high is 56.2%; on the original repository’s SRE single-run track, GPT-4o repair is 25.00%, and on the multi-run track it is 24.79%. Neither is evidence that tasks are generally solved; each is read within its own protocol, and rankings are not mixed.

Sources: [1](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08); [2](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md) (accessed 2026-11-08).

### 污染与已知问题

AA contains 40 public scenarios and 19 private scenarios; leakage on the public scenarios and generalization on the private scenarios need to be examined separately. Diagnostic repair as actually executed in the original work, and the offline root-cause metric in AA, are not the same task, and 56.2% cannot be interpreted as the success rate of repairing a real incident.

Sources: [1](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2502.05352) (accessed 2026-11-08).

### 相关与衍生基准

ITBench-AA (announced in the README on 2026-05-27, with 59 SRE tasks). The STRATUS paper is a multi-agent SRE system based on that environment. IBM also has AssetOpsBench, but that is not a new version of ITBench.

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not a run date or a leaderboard-update date)

Sources: [1](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08); [2](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md) (accessed 2026-11-08).

### 官方结果入口

https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md) (accessed 2026-11-08).

### 独立评测入口

https://artificialanalysis.ai/evaluations/itbench-aa

Sources: [1](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-07).

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "GPT-5.6 Sol (Max)"
 "score": "56.2"
 "metric": "Average precision at full recall (%)"
 "track": "AA independent 59 scenarios, static root-cause analysis"
 "source_url": "https://artificialanalysis.ai/evaluations/itbench-aa"
 "source_date": "Unverified (page snapshot)"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "Step 5 Preview"
 "score": "55.6"
 "metric": "Average precision at full recall (%)"
 "track": "AA independent 59 scenarios, static root-cause analysis"
 "source_url": "https://artificialanalysis.ai/evaluations/itbench-aa"
 "source_date": "Unverified (page snapshot)"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "Gemini 3.8 Flash (High)"
 "score": "52.5"
 "metric": "Average precision at full recall (%)"
 "track": "AA independent 59 scenarios, static root-cause analysis"
 "source_url": "https://artificialanalysis.ai/evaluations/itbench-aa"
 "source_date": "Unverified (page snapshot)"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "ITBench-SRE-Agent-GPT-4o"
 "score": "25.00"
 "metric": "% Resolved"
 "track": "Original SRE Single Trial / 16 incidents."
 "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
 "source_update_label": "02/05/2025 18:06:54 (the original text does not state the day-month order; the original label is kept and the date is not converted)"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "ITBench-SRE-Agent-LLama-3-3-70B"
 "score": "12.50"
 "metric": "% Resolved"
 "track": "Original SRE Single Trial / 16 incidents."
 "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
 "source_update_label": "02/05/2025 18:06:54 (the original text does not state the day-month order; the original label is kept and the date is not converted)"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "ITBench-SRE-Agent-Granite-3-2"
 "score": "0.00"
 "metric": "% Resolved"
 "track": "Original SRE Single Trial / 16 incidents."
 "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
 "source_update_label": "02/05/2025 18:06:54 (the original text does not state the day-month order; the original label is kept and the date is not converted)"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "ITBench-SRE-Agent-GPT-4o"
 "score": "24.79"
 "metric": "% Resolved"
 "track": "Original SRE Multiple Trials / 162 incidents"
 "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": null
 "model": "ciso-agent-expert-rhel9-opa"
 "score": "0.30"
 "metric": "Average benchmark score (0–1)"
 "track": "Original CISO / respective scenario categories"
 "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_CISO.md"
 "scenario_category": "Gen-CIS-b-RHEL9-Ansible-OPA"
 "passed": 3
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": null
 "model": "pre-release-agent-2025-0428"
 "score": "0.20"
 "metric": "Average benchmark score (0–1)"
 "track": "Original CISO / respective scenario categories"
 "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_CISO.md"
 "scenario_category": "Gen-CIS-b-K8s-Kyverno"
 "passed": 2
 "snapshot_date": "2026-11-08 "
 }
]
```

Sources: [1](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08); [2](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md) (accessed 2026-11-08); [3](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_CISO.md) (accessed 2026-11-08).

### 覆盖与局限

The original project's single-run and multi-run tracks for the SRE operating environment are kept separate from AA's static root-cause track. The README now has SRE/CISO leaderboards, correcting the earlier practice of linking only AA as the official leaderboard. The update-time label on the original leaderboard does not make the timezone or the day-month format clear, and it is not treated as a run date.

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/itbench-aa) (accessed 2026-11-08); [3](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

## Contact

### 官方公开邮箱

```json
[
 "agent-bench-automation@ibm.com"
 "saurabh.jha@ibm.com"
 "muew@jp.ibm.com"
]
```

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

### 仓库反馈

https://github.com/itbench-hub/ITBench/issues

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

### 官方社区

https://discord.gg/6fzy3JRHmt

> The community discussion entry listed in the official README.

Sources: [1](https://github.com/itbench-hub/ITBench/blob/main/README.md) (accessed 2026-11-08).

### 隐私与联系边界

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

## Original files

### Paper PDF

https://arxiv.org/pdf/2502.05352

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

### PDF SHA-256

da47aa02d9cf0cd2a330d3c9890e0338d4f3c3cdd89521c7b8979ab4986f932c

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2502.05352) (accessed 2026-11-08).

### PDF bytes

```json
4068098
```

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2502.05352) (accessed 2026-11-08).

### 已有文件夹

Unverified

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

### 其他官方文档

```json
[
 {
 "type": "Official methods and introduction page (not the paper PDF)"
 "url": "https://arxiv.org/abs/2502.05352"
 }
]
```

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

### 已有 PDF归档

Unverified

> This group only creates local research files and does not upload a PDF or claim that one already exists.

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07).

## Changelog

### 历次核查

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

Sources: [1](https://arxiv.org/abs/2502.05352) (accessed 2026-11-07); [2](https://arxiv.org/abs/2502.05352) (accessed 2026-11-08); [3](https://github.com/itbench-hub/ITBench) (accessed 2026-11-08).
