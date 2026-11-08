# Agents’ Last Exam v1.1

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

of official materials, with unknowns retained as Unverified.

Long-horizon agents are tested with deliverables from real professional software; the current v1.1 makes 122 tasks public, and the collection pool of 1500+ cannot be used as the denominator for scoring. An independent review found serious shortcut problems, and the authors' response and the scope of the repair must be read side by side.

## Basic information

### Short name

Agents’ Last Exam v1.1

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Full name

Agents’ Last Exam v1.1

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Benchmark version

v1.1

[来源1](https://epoch.ai/benchmarks/agents-last-exam/review)（访问 2026-11-07）

### Paper version

arXiv v4 (authors and affiliations revised on 2026-10-25; the abstract says the scientific content is unchanged)

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### Release date

The first draft of the paper is 2026-06-04 04:20:46; the exact first-release date of the current data v1.1 is Unverified.

> 字段状态：待核实

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### Section

Agent

> Editorial filing. Only the main section is counted.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Field tags

- Professional software workflow
- Long-duration computer operation
- Verification of scientific and engineering deliverables

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### License

The framework code is Apache-2.0; data and content such as tasks, selected_tasks, and sample_run are CC-BY-4.0, and LICENSE and LICENSE-DATA apply respectively.

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam/blob/main/LICENSE)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2606.05405

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Code

https://github.com/rdi-berkeley/agents-last-exam

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/agents-last-exam/agents-last-exam

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问 2026-11-07）

### Official entry

https://agents-last-exam.org/

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Paper title

Agents’ Last Exam

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

## Origin and maintenance

### Initiators

UC Berkeley RDI and the RDI Foundation.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### 合作方

Unverified

> 字段状态：待核实

> The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Authors

Yiyou Sun, Xinyang Han, Weichen Zhang, Yuanbo Pang, Tianyu Wang, and others; the full author list is in the paper

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### Maintainer

UC Berkeley RDI and the RDI Foundation.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Funders

Tianqiao & Chrissy Chen Institute, Snorkel AI, and UniPat AI (financial and compute-credit support)

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

## Design goals

### Abilities measured

Long-horizon, high-economic-value workflows across professional software, combining interaction through the GUI, the CLI, files, and tools.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### Design background

Knowledge question answering or short-horizon operation is not enough to measure verifiable professional deliverables and actual occupational workflows.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

## Construction

### Question sources

Experts submit real projects that have already been completed, which pass an initial review, an engineering dry-run, and final quality control by an expert committee.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### 出题者背景

Practicing experts supply completed projects; they are not general crowd workers. The paper says 250+ industry experts and the current homepage says 300+, and the two should be distinguished by the date of the material.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://agents-last-exam.org/)（访问 2026-11-07）

### Review process

Initial review → engineering implementation and dry-run → final QC by an expert committee; the overall pool in the paper and the count of public questions in v1.1 are recorded separately.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### Quality control

Appendix B.2 of the paper: experts review the correctness of reference artifacts, acceptance boundaries, and sufficiency of context. The current v1.1 has 57 tasks that must be rerun and 65 that can be kept, with 47 instruction changes, 43 verification changes, 32 environment changes, and 23 data changes (the categories overlap). The official release states that this review is not a certification of complete agent verification.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam/blob/main/docs/releases/v1.1.md)（访问 2026-11-07）

### Decontamination

The design in the paper keeps a private pool and replaces public tasks on a rolling basis; the hidden reference answer is staged only after the agent has finished. This design does not rule out a shortcut through public scoring code or through answers on the external web, and an independent review by Epoch pointed out actual defects.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）；[来源3](https://epoch.ai/benchmarks/agents-last-exam/review)（访问 2026-11-07）

## Data format

### 题量与规模

v1.1 releases 122 tasks; the 1,500+ on the homepage is the overall collection pool, not the number of questions currently scored in public.

[来源1](https://epoch.ai/benchmarks/agents-last-exam/review)（访问 2026-11-07）

### Question types

Generate deliverables such as files, workbooks, designs, animations, and analyses, and carry out software operations.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Modalities

- 文本
- 图像
- 文件
- GUI/CLI interaction

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Languages

- English task description
- Chinese source documents (such as loss events and regulatory documents); the actual tasks also contain material in other languages, and it is not claimed that there are only two languages

[来源1](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问 2026-11-07）

### Difficulty

v1.1 is split into tracks of 45 Near-Term, 46 Full-Spectrum, and 36 Last-Exam. The tracks overlap, so they are not 45+46+36 mutually exclusive samples. Of the 122 active tasks, 119 are CPU and 3 are GPU.

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

### Public and hidden splits

The current v1.1 makes 122 active tasks public. This HF card contains only the prompt, taxonomy, software, and input descriptions. Input files, hidden reference artifacts, and images are released separately. Figure 5 of the original paper has a collection pool of 1490 = 150 public + 1017 private + 323 awaiting QC. The paper body also uses 152 public evaluation instances. That is a difference of time point and of instance scope, and it cannot be combined in calculation with v1.1.

[来源1](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

## Evaluation

### Metrics

mean score is the average of the fine-grained task scores on [0,1]. full-pass rate is the proportion of tasks that receive a full score. Both may be displayed as percentages. Current and historical results, ALL, stratified results, CLI, and different agent harnesses are kept on separate tracks.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

### 评分

Task evaluate returns a value in [0,1] and, according to the task, uses an exact value, a tolerance, or a geometric or behavioral check; a small number of visual or semantic tasks use a model judgment under a narrow rubric; mean score and full-pass are kept separate.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### 运行设置

Historical experiments in the paper allow at most 5 hours each. The main setting is GUI-as-Tool, with the task description provided and a CLI+GUI tool bridge; the current v1.1 must pin matching code, images, and data, and the agent configuration. The budget in the paper cannot be applied automatically to every community submission.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam/blob/main/docs/releases/v1.1.md)（访问 2026-11-07）

### 官方脚本

https://github.com/rdi-berkeley/agents-last-exam

> ale_run, task evaluate, the fixed active-task list, and the matching asset manifest are public; no download or run command is executed.

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

### 可比性警示

v1.1 must not be placed on the same leaderboard as the historical results of the paper’s original v1, or as a vendor score that does not state a version; Epoch rated it Flawed on 2026-10-18, and the authors’ response must be kept as well.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### 最新版本与采用证据

```json
{
 "version": "v1.1"
 "evidence_2026_h2": [
 {
 "url": "https://openai.com/index/introducing-gpt-6-1-terra/"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Vendors actually use ALE to measure professional computer work; the page does not give an explicit v1.1 results table, and a current ranking is not invented from it."
 }
 {
 "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
 "date": "2026-10-18"
 "date_type": "source_calendar_date"
 "note": "Epoch independently reviewed v1.1 and judged it Flawed; popularity is not the same as passing a quality review."
 }
 ]
}
```

> The heat grade is adopted from the candidate; only evidence that has been opened and can be verified is retained. A does not guarantee that every version received independent reruns by multiple institutions.

[来源1](https://openai.com/index/introducing-gpt-6-1-terra/)（访问 2026-11-07）；[来源2](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-06-04"
 }
 {
 "version": "v2"
 "submitted_at": "2026-06-11"
 }
 {
 "version": "v3"
 "submitted_at": "2026-10-09"
 }
 {
 "version": "v4"
 "submitted_at": "2026-10-25"
 }
]
```

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### Saturation

On the hardest Last-Exam track of the original paper, the average full-pass of the mainstream configuration is under 1%. That is a historical protocol, not the current first place on the v1.1 leaderboard. A third-party data card shows entries for current models, but the metric and the submission protocol are incomplete. Overall saturation cannot be asserted directly from 43.2.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问 2026-11-07）

### Contamination and disputes

```json
{
 "independent_review": "On 2026-10-18, Epoch reviewed a stratified 50 of the 122 public questions; 22 questions (44%) could receive a full score by an unintended shortcut and were judged Flawed; this is not extrapolated to the error rate of the whole private pool."
 "developer_response": "The authors hold that a white-box attack is not the same as an actual run under natural operation, and the report states that, after two tasks whose network rules were not shown to the agent are excluded, 3/1,617 trajectories received a full score for passing along the path that was indicated, and that network isolation is to be required in a later version; this is reported by the authors themselves and is not an independent review."
}
```

[来源1](https://epoch.ai/benchmarks/agents-last-exam/review)（访问 2026-11-07）；[来源2](https://agents-last-exam.org/blogs/verifier-check)（访问 2026-11-07）

### 版本与衍生关系

ALE-CLI is the Linux subset of the original paper (105 instances); the ale_cli list in the current v1.1 has 86 tasks. Version, and operating system or track, must be recorded separately.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### Official leaderboard

https://agents-last-exam.org/leaderboard

[来源1](https://agents-last-exam.org/leaderboard)（访问 2026-11-07）

### 第三方覆盖

Unverified

> 字段状态：待核实

> The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### 分轨结果

#### Paper Table1/historical 152 instances

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| Not applicable (columns selected within the source, not a global ranking) | Codex + GPT-5.5 | 24.0 | Overall full-pass rate (%) | [原表](https://arxiv.org/abs/2606.05405)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | ALE-Claw + GPT-5.5 | 23.0 | Overall full-pass rate (%) | [原表](https://arxiv.org/abs/2606.05405)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | Claude Code + Fable 5 | 22.0 | Overall full-pass rate (%) | [原表](https://arxiv.org/abs/2606.05405)，2026-11-07 |

#### HF model submission/not HF verification

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| Not applicable (columns selected within the source, not a global ranking) | moonshotai/Kimi-K3.1-Pro | 43.2 | The HF card states v1.1 ALL, and the metric is unnamed (the interface maps it to pass rate; Unverified) | [原表](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)，2026-11-07 |

> 字段状态：待核实

> The current official v1.1 leaderboard page returns only the title, and a verifiable full ranking was not obtained. Historical original-paper results and HF submissions are selectively listed, on strictly separate tracks; 43.2 is not a conclusion from a complete official ranking.

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问 2026-11-07）；[来源3](https://agents-last-exam.org/leaderboard)（访问 2026-11-07）

### Coverage note

The ranks and the update date of the current full official v1.1 leaderboard are Unverified; HF mixes an export of the original 152 questions with the current card of 122 questions, so the overall order on the HF page cannot be assembled into the v1.1 leaderboard. Three rows in the historical paper explicitly mark 152 instances.

> 字段状态：待核实

[来源1](https://agents-last-exam.org/leaderboard)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

## Contact

### 公开科研联系邮箱

- rdi_research@berkeley.edu

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### 公开反馈

https://github.com/rdi-berkeley/agents-last-exam/issues

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

### 官方社交

- https://discord.gg/jsG4Th3aVt
- https://groups.google.com/g/agenthle-news

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问 2026-11-07）

### 隐私说明/政策

https://agents-last-exam.org/privacy

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2606.05405

[来源1](https://arxiv.org/abs/2606.05405)（访问 2026-11-07）

### PDF SHA-256

300b7cf737cd52288e9bf34c8400adfa8a2331a99f05878681c7117ba67e68b3

> SHA-256 of the bytes actually downloaded. It does not mean an existing copy was replaced.

[来源1](https://arxiv.org/pdf/2606.05405)（访问 2026-11-07）

### PDF bytes

23530631

[来源1](https://arxiv.org/pdf/2606.05405)（访问 2026-11-07）

### Folder

Unverified

> 字段状态：待核实

> The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### 其他官方材料

```json
[
 {
 "type": "Official methods or project page"
 "url": "https://agents-last-exam.org/"
 "accessed": "2026-11-07"
 }
]
```

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

### 论文副本

Unverified

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）

## Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 }
]
```

[来源1](https://agents-last-exam.org/)（访问 2026-11-07）
