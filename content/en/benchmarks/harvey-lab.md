# Harvey LAB（Legal Agent Benchmark）

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

Harvey LAB requires an agent to process a case file and deliver legal documents that can be audited. What it measures is completion of long-horizon work, rather than isolated legal multiple-choice questions. The public task bank is now larger than the initial release, but the AA and Vals leaderboards still each use 120 private tasks; two-judge all-pass and the AA hallucination gate are independent tracks.

Sources for the reading guide: [https://artificialanalysis.ai/evaluations/harvey-lab-aa](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [https://www.vals.ai/benchmarks/hlab](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

## Basic information

### Short name

Harvey LAB（Legal Agent Benchmark）

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Full name

Harvey's Legal Agent Benchmark (LAB)

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Dataset version

Open-source repository lab-core v1.3.0; the AA implementation is Harvey LAB-AA v1.1; the Vals implementation is HLAB-Vals-1.1

Note: The three uses of “v1.1” belong to different implementations and cannot be compared with one another.

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [3](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### Paper version

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Release date

2026-05-06 (Harvey official blog)

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Section

Agent

Note: Benchmark Constitution editorial filing.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Subfields

- 法律
- Professional knowledge work

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### License

MIT (harvey-labs repository)

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07)

### Paper

Unverified

Note: Officially released as a blog; no standalone paper was found.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 代码入口

https://github.com/harveyai/harvey-labs

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07)

### Dataset

https://github.com/harveyai/harvey-labs

Note: The open-source task set is in the tasks/ directory of the repository.

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07)

### Official homepage

https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Paper title

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Origin and maintenance

### 发起团队

Harvey

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 合作及署名机构

Artificial Analysis (v1.1 jointly developed the AA implementation); Vals AI (industry collaborative evaluation)

Sources: [1](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [2](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### Authors

Niko Grupen, Gabe Pereyra, and Julio Pereyra (blog byline)

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Maintainer

Harvey（harveyai/harvey-labs）

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07)

### Funders

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Design goals

### 评测能力

As when a law firm assigns work: instructions and the client case file are given, and the agent is required to produce reviewable legal work product (documents, tables, and presentations).

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07); [2](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 设计动机

LegalBench, CUAD, LEXam, BigLaw Bench, and similar benchmarks evaluate only short-horizon reasoning and lack a long-horizon legal agent benchmark.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Construction

### 材料来源

The tasks start from real client matters handled by lawyers in each area of practice and are split into specific tasks that can be assigned to an associate; the instruction, the case file, and the requirements for the deliverable are given. The source does not demonstrate, item by item, the details of de-identification or of authorization for the public materials, and the related process is Unverified.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 编制背景

Practicing lawyers took part in sourcing the tasks, and the rubrics were written by domain experts; the launch states 75,000+ criteria, and that historical figure cannot be treated as the measured count.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Review process

Facts, conclusions, citations, risk levels, and delivery formats that a partner or a client would review are split into binary criteria, and each criterion is bound to a specific output file; the public set allows legal professionals to examine the tasks and to review the rubrics.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md) (accessed 2026-11-07)

### Quality control

Vals v1.1 discloses that 17 criteria that could not be completed were removed and that 1 mismatched source file was replaced. The hold-out remains 120 tasks. An official change on 2026-11-05 lets the judge see DOCX revisions and comments. Output that carries revisions cannot be compared directly with the old scores.

Sources: [1](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md) (accessed 2026-11-07)

### 去污染边界

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Data format

### Size

The current README badge is 2,010 tasks. The evaluation document writes 2,010 tasks and 27 areas of practice, while the README still writes 24+contracting (the classification scope is not unified). The launch blog has 1,200+ tasks, 24 areas, and 75,000+ expert rubric items, which belong to the first version rather than the current total. AA and Vals each use 120 private hold-out tasks, and 2,010 cannot be used as the leaderboard denominator.

Sources: [1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/README.md) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md) (accessed 2026-11-07); [3](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07); [4](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [5](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### Question types

Long-horizon agent tasks, producing deliverables such as docx, xlsx, and pptx.

Sources: [1](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### Modalities

- 文本
- 办公文档

Sources: [1](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### Languages

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Difficulty

Long-horizon professional legal deliverables; all-pass requires one judge to find that every criterion passes, and the criteria pass rate cannot stand in for the task solve rate. AA adds a further gate for substantive hallucination.

Sources: [1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [3](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 公开及隐藏划分

There is a public set and a held-out test set; Vals results come from the held-out set; AA uses a private dataset

Sources: [1](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07)

## Evaluation

### Metrics

AA: Hallucination-Gated All-Pass Rate (every criterion is met and there is no substantive hallucination). Vals: Task Pass Rate and Criteria Pass Rate.

Sources: [1](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [2](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 计分

The open-source standard uses two judges, claude-sonnet-4-6 and gpt-5.5: task all-pass is computed for each judge and then averaged. A question may be 0, 0.5, or 1, and cases in which both judges strictly pass are listed separately. AA v1.1 uses three judges and has a substantive hallucination gate; Vals is the mean of the task pass rates of two judges.

Sources: [1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [3](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 提示与运行设置

Vals: the six tools Read, Edit, Write File, Glob, Bash, and Grep, together with docx/pptx/xlsx skills; AA: Stirrup harness

Sources: [1](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07)

### 评测入口

https://github.com/harveyai/harvey-labs

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07)

### 可比性边界

AA v1.1 and v1.0 are not comparable; Vals HLAB-Vals-1.1 and AA LAB-AA are not comparable (the Vals page states this explicitly).

Sources: [1](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [2](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/README.md) (accessed 2026-11-07)

### 已核实版本

version：Open-source repository lab-core v1.3.0; the AA implementation is Harvey LAB-AA v1.1; the Vals implementation is HLAB-Vals-1.1；evidence_2026_h2：- url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；organization：Artificial Analysis；note：The current methods page lists the Harvey Legal Agent Benchmark (LAB v1.1) as an evaluation under way, and it discloses the tasks or the scoring protocol.；- url：https://artificialanalysis.ai/evaluations；date：2026-11-07；organization：Artificial Analysis；note：The current public evaluation catalog lists Harvey Legal Agent Benchmark (LAB v1.1) on its own; it is not a news mention.；- url：https://www.vals.ai/benchmarks/hlab；date：2026-11-05；organization：Vals AI；note：On November 5, Vals updated the HLAB-Vals-1.1 leaderboard of professional legal deliverables; it is recorded separately from the AA setting.；trending：heat_confidence：A；summary：The AA catalog marks it Updated. It has been jointly upgraded with Harvey into a hallucination-gated evaluation; Vals also evaluates HLAB-Vals-1.1 independently.

Note: Recent popularity evidence is taken from candidate studies and reopened pages; grade A: adopted independently by multiple frontier laboratories or evaluation organizations.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations) (accessed 2026-11-07); [3](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 论文历史及后续证据

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Saturation

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 已知问题

Public tasks may be used for research and for training, and they cannot be treated as uncontaminated. Current open-source scoring is affected by changes in parsing for the harness, the SDK, and DOCX revisions; results on revised-document tasks from before November 5 and from after November 5 should be versioned separately. The AA and Vals private hold-out and the public full set are not the same scope of data.

Sources: [1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/README.md) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md) (accessed 2026-11-07); [3](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [4](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 衍生关系

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07)

### 官方结果入口

https://artificialanalysis.ai/evaluations/harvey-lab-aa

Note: Harvey itself has no official leaderboard; AA is an implementation in cooperation with Harvey.

Sources: [1](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07)

### 第三方结果入口

https://www.vals.ai/benchmarks/hlab

Sources: [1](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| AA LAB-AA v1.1; 120 private tasks; Stirrup; three judges. | 1 | Muse Wonder Full (Max) | 13.1 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07；Unverified (page does not state an update date) |
| AA LAB-AA v1.1; 120 private tasks; Stirrup; three judges. | 2 | Muse Wonder (Max) | 10.0 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07；Unverified (page does not state an update date) |
| AA LAB-AA v1.1; 120 private tasks; Stirrup; three judges. | 3 | Grok 4.7 (Xhigh) | 9.4 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07；Unverified (page does not state an update date) |
| AA LAB-AA v1.1; 120 private tasks; Stirrup; three judges. | 4 | Muse Spark 1.3 (Max) | 8.9 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07；Unverified (page does not state an update date) |
| AA LAB-AA v1.1; 120 private tasks; Stirrup; three judges. | 5 | GPT-6 Astra (Max) | 8.6 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07；Unverified (page does not state an update date) |
| HLAB-Vals-1.1; 120 private tasks; Harvey/Valkyrie; dual judges | 1 | Gemini 4 Argon | 27.08 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07；2026-11-05 (update date reported by the page) |
| HLAB-Vals-1.1; 120 private tasks; Harvey/Valkyrie; dual judges | 2 | Muse Spark Open | 25.0 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07；2026-11-05 (update date reported by the page) |
| HLAB-Vals-1.1; 120 private tasks; Harvey/Valkyrie; dual judges | 3 | Wonder | 23.75 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07；2026-11-05 (update date reported by the page) |
| HLAB-Vals-1.1; 120 private tasks; Harvey/Valkyrie; dual judges | 4 | Wonder Full | 23.33 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07；2026-11-05 (update date reported by the page) |
| HLAB-Vals-1.1; 120 private tasks; Harvey/Valkyrie; dual judges | 5 | Inkling 2 Small | 21.67 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07；2026-11-05 (update date reported by the page) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

The top five of AA v1.1 and the top five of Vals v1.1 are transcribed separately. The two leaderboards differ in harness, judge, hallucination gating, and the version of the fix, and their ranks must not be compared with each other. AA does not display a date on which the leaderboard was updated. The Vals page states explicitly: Updated 11/5/2026.

Sources: [1](https://artificialanalysis.ai/evaluations/harvey-lab-aa) (accessed 2026-11-07); [2](https://www.vals.ai/benchmarks/hlab) (accessed 2026-11-07)

## Contact

### 公开研究联系邮箱

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 问题反馈

https://github.com/harveyai/harvey-labs/issues

Sources: [1](https://github.com/harveyai/harvey-labs) (accessed 2026-11-07)

### 官方账号

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 隐私政策

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Original files

### 原文PDF

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### PDF SHA-256

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### PDF bytes

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### Folder

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

### 其他原始材料

- type：Official launch blog (not a paper)；url：https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- type：评分方法；url：https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md
- type：Version log that affects scores；url：https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md) (accessed 2026-11-07); [3](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md) (accessed 2026-11-07)

### PDF

Unverified

Note: This group does not upload, as the task requires; the original PDF URL is in original_files.

Sources: [1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) (accessed 2026-11-07)

## Changelog

### 本页修订

- date：2026-11-07；；change：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。
- date：2026-11-07；；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07)
