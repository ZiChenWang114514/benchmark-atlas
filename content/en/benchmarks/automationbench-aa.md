# AutomationBench-AA

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

AutomationBench-AA

### Full name

AutomationBench-AA (Artificial Analysis’s implementation of Zapier AutomationBench)

### 数据/软件版本

AA uses the private split of 657 tasks from AutomationBench dataset 1.0.6; the AA scoring protocol is independent.

### Paper version

arXiv v1

Note: A paper revision is not the same as a dataset version.

### Release date

2026-04-21 08:14:59 (Zapier parent-paper arXiv v1 submission; not presented as the first-release time of the AA implementation)

### Section

Agent

Note: Benchmark Constitution editorial filing. Only the main section is counted.

### 学科标签

Long-horizon automated task

### 许可证与范围

The original portion by Zapier in the parent repository is MIT; the LICENSE states that it claims no original copyright in third-party API structures and that it does not grant third-party IP rights; the separate data license for AA’s private 657 questions is Unverified.

Status: Unverified (part of this field is still unconfirmed).

### 论文入口

https://arxiv.org/abs/2604.18934

Note: 2604.18934 is the paper of the Zapier parent protocol; the partial-score convention AA uses on 657 questions is not attributed to the parent paper.

### Paper title

AutomationBench

### Code

https://github.com/zapier/AutomationBench

### Dataset

Not disclosed (the held-out test set of 657 tasks used by AA); public tasks of the parent project are given separately at https://github.com/zapier/AutomationBench.

### Official homepage

https://artificialanalysis.ai/evaluations/automationbench-aa

## Origin and maintenance

### 发起团队

Parent benchmark: Zapier; AA implementation and independent evaluation: Artificial Analysis.

### 署名/合作机构

The parent paper thanks Prime Intellect and others for early feedback; this does not mean that those organizations jointly maintain the AA private set.

### Authors

Daniel Shepard；Robin Salimans

### 维护入口

The AutomationBench parent project is maintained by Zapier; AA runs and the leaderboard are maintained by Artificial Analysis.

### 资助与计算资源

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Status: Unverified (part of this field is still unconfirmed).

## Design goals

AA实现和Zapier母基准共享任务形态却不共享主分数：AA对无guardrail违规任务给予目标完成比例，Zapier严格要求全断言成功。77.8%不能与母论文9.9%直接作同协议时间进步曲线。

### 测量能力

Autonomously discover APIs across SaaS applications, process data, follow layered business rules, and complete multi-step workflows.

### 为何需要这个基准

Many tool benchmarks test only a single application or function choice, and lack cross-application coordination, endpoint discovery, and combinations of business policy.

## Construction

### 材料来源

Synthesized from the shape of Zapier customer workflows, without using PII or customer secrets; it covers 6 domains, about 500 endpoints, and 47 simulated applications.

### 命题/编制背景

Zapier research and engineering team; Opus4.6, GPT5.3Codex, and Gemini3 take part in generation, which is then reviewed.

### Review process

Multiple rounds of iteration on realism and difficulty, with sampled manual audit; solvability is checked through prompt patterns that do not contain the actual parameters.

### Quality control

Each question requires an observable state change, a deterministic check, and negative assertions to prevent casting a wide net; RL trials identify reward loopholes.

### 去污染与证据边界

The parent protocol publishes 600 questions and at least as many private questions; AA keeps 657 evaluation questions, and the public examples are not the official complete scoring set.

## Data format

### 规模与分母

The AA implementation: 657 tasks and 6 domains (Finance/HR/Marketing/Operations/Sales/Support); the public 600 of the parent paper and its 600+ private tasks are not the same exact denominator.

### Question types

After a single task instruction, autonomous multi-step API retrieval and calls, and finally a check of the states of multiple applications.

### 模态与字段

文本；Structured APIs and databases；Simulated SaaS applications

### Languages

English business instructions and an API schema.

### 难度定位

Layered policies, noise, and similar records create the difficulty; this is not a test of real production SaaS connectivity or credential permissions.

### 公开、隐藏与划分

AA scoring questions remain private, and some examples are public; the parent project's public questions can be studied but cannot serve as a set that fully reproduces the AA score.

## Evaluation

### Metrics

The headline is the per-question proportion of objective completion, averaged after guardrail gating; there is also a strict whole-question success rate.

### 评分流程

Each task first checks the program assertions on the final state: any guardrail violation, or an error in the task, scores 0; otherwise the proportion of that task's objectives that were completed is taken, and the tasks are then averaged with equal weight. There is no independent LLM judge; Objectives Completed on the web page, without the guardrail gate, is only a diagnostic metric and is not the headline.

### 运行与提示

The private 657 questions come from AutomationBench 1.0.6; the six domains are Finance, HR, Marketing, Operations, Sales, and Support; each question is run once, for at most 50 turns, and structured tools discover and call a REST API. The domains are mutually exclusive; one question may involve more than one app, so the breakdown by application is not mutually exclusive.

### 评测实现

https://github.com/zapier/AutomationBench

### 不能混比的设置

For a task with no guardrail violation, AA gives a score by the proportion of the goal that was completed, and a violation or an execution error is scored 0. The Zapier main leaderboard scores by the proportion of tasks in which every assertion passes. The public 600 tasks, the private 657 tasks at AA, and a further 200 simple tasks cannot be mixed.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

version：AutomationBench 1.0.6; 657 private AA tasks.；evidence_2026_h2：- url：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1；date：2026-10-28；note：The Artificial Analysis article of 2026-10-28 explicitly lists AutomationBench-AA as an evaluation component of Intelligence Index v5 and reports leading performance by models.

### 版本脉络

mother_paper：arXiv:2604.18934v1；submitted_at：2026-04-21；boundary：The first release of the Zapier paper is not the date the private AA set went online.

### 分数上限与饱和度

The current top three on the AA web page are 77.8/77.6/77.5%. Clear unfinished objectives or guardrail errors remain, so complete saturation cannot be declared. The highest figure in the parent paper, 9.9%, is the historical strict whole-question success rate of 2026-04; the current highest in the README on the public 600 questions is 50.3%. Neither is mixed into a comparison with the AA partial scores.

### 争议与局限

Synthetic tasks and simulated APIs may depart from real business; scoring only the final state does not fully inspect the course of behavior, and the guardrail definition affects interpretation.

### 衍生版本

AutomationBench-AA is the AA implementation; the parent protocol's 600 public questions and 657 private evaluations are not counted as two entries, and application and domain subitems are not counted separately.

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

https://artificialanalysis.ai/evaluations/automationbench-aa

### 第三方/补充实验

https://artificialanalysis.ai/evaluations/automationbench-aa

### 分轨成绩

#### AA official current leaderboard: 657 private tasks / guardrail-gated objective credit

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Gemini 4 Carbon (High) | 77.8 | AutomationBench-AA Score (%) |
| 2 | Gemini 4 Carbon (Medium) | 77.6 | AutomationBench-AA Score (%) |
| 3 | Gemini 4 Argon (High) | 77.5 | AutomationBench-AA Score (%) |

- Gemini 4 Carbon (High)：source_url：https://artificialanalysis.ai/evaluations/automationbench-aa；accessed：2026-11-07；benchmark_version：AutomationBench 1.0.6 / AA private 657；source_type：Web-page snapshot of the AA implementer's independent evaluation；source_date：Unverified (the webpage does not state a run date for each model or an update date for the leaderboard)
- Gemini 4 Carbon (Medium)：source_url：https://artificialanalysis.ai/evaluations/automationbench-aa；accessed：2026-11-07；benchmark_version：AutomationBench 1.0.6 / AA private 657；source_type：Web-page snapshot of the AA implementer's independent evaluation；source_date：Unverified (the webpage does not state a run date for each model or an update date for the leaderboard)
- Gemini 4 Argon (High)：source_url：https://artificialanalysis.ai/evaluations/automationbench-aa；accessed：2026-11-07；benchmark_version：AutomationBench 1.0.6 / AA private 657；source_type：Web-page snapshot of the AA implementer's independent evaluation；source_date：Unverified (the webpage does not state a run date for each model or an update date for the leaderboard)

#### Zapier official README: 600 public tasks / strict all-assertions pass

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Claude Opus 5 (max) | 50.3 | strict task pass rate (%) |
| 2 | Kimi K3 (max) | 46.67 | strict task pass rate (%) |
| 3 | Claude Fable 5 (max) | 46.17 | strict task pass rate (%) |
| 4 | GPT-5.6 Sol (max) | 45.83 | strict task pass rate (%) |
| 5 | Gemini 3.6 Flash (high) | 45.0 | strict task pass rate (%) |

- Claude Opus 5 (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：The parent project's public-set README stores the scores; not the 657-question AA leaderboard and not the Zapier private main leaderboard；n_tasks：600；protocol：100 tasks in each of six domains; each model uses the highest reasoning effort available to it; Fable5 is the score after a stricter classifier in 2026-07
- Kimi K3 (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：The parent project's public-set README stores the scores; not the 657-question AA leaderboard and not the Zapier private main leaderboard；n_tasks：600；protocol：100 tasks in each of six domains; each model uses the highest reasoning effort available to it; Fable5 is the score after a stricter classifier in 2026-07
- Claude Fable 5 (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：The parent project's public-set README stores the scores; not the 657-question AA leaderboard and not the Zapier private main leaderboard；n_tasks：600；protocol：100 tasks in each of six domains; each model uses the highest reasoning effort available to it; Fable5 is the score after a stricter classifier in 2026-07
- GPT-5.6 Sol (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：The parent project's public-set README stores the scores; not the 657-question AA leaderboard and not the Zapier private main leaderboard；n_tasks：600；protocol：100 tasks in each of six domains; each model uses the highest reasoning effort available to it; Fable5 is the score after a stricter classifier in 2026-07
- Gemini 3.6 Flash (high)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：The parent project's public-set README stores the scores; not the 657-question AA leaderboard and not the Zapier private main leaderboard；n_tasks：600；protocol：100 tasks in each of six domains; each model uses the highest reasoning effort available to it; Fable5 is the score after a stricter classifier in 2026-07

### 覆盖边界

AA is both the maintainer of this implementation and an independent evaluator relative to the parent Zapier project. The same AA URL does not count as two independent pieces of evidence. The strict pass rate on the 600 public questions in the Zapier README is listed separately, and it is not treated as the score on the AA657 questions or on Zapier's harder private set. The top three Objectives Completed on the AA web page are separately 94/94/93, and they must not replace the 77.8/77.6/77.5 headline.

## Contact

### 公开作者工作邮箱

daniel.shepard@zapier.com；robin.salimans@zapier.com

### 公开反馈

https://github.com/zapier/AutomationBench/issues

Note: Public repository feedback entry point; no question was sent.

### 官方账号

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://arxiv.org/pdf/2604.18934

Note: Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

### 下载源文件SHA-256

348360cd2ccefc52d1a8ea65e0a334cb3363fab85e66f71e09f6f5935233cbc5

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

684375

### 其他材料

Note: The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

### 既有 PDF链接

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- 2026-11-07：深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。
- 2026-11-07：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

### 来源索引

[1]: https://artificialanalysis.ai/evaluations/automationbench-aa "访问 2026-11-07"
[2]: https://artificialanalysis.ai/methodology/intelligence-benchmarking "访问 2026-11-07"
[3]: https://arxiv.org/abs/2604.18934 "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/zapier/AutomationBench/main/LICENSE "访问 2026-11-07"
[5]: https://artificialanalysis.ai/methodology/intelligence-benchmarking#automation-bench-aa "访问 2026-11-07"
[6]: https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md "访问 2026-11-07"
[7]: https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 "访问 2026-11-07"
[8]: https://arxiv.org/pdf/2604.18934 "访问 2026-11-07"
[9]: "访问 2026-11-07"
[10]: "访问 2026-11-07"
[11]: "访问 2026-11-07"
