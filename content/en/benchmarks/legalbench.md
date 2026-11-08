# LegalBench
> Verification: 2026-11-08. Existence has been verified; a recently popular newly created entry, with markers retained on fields that are not verified; trending: B

LegalBench is not one unified legal examination paper. It is a collection of 162 tasks organized around six kinds of legal reasoning. The original classification uses balanced accuracy, and rule application also includes human review by people with a legal background; the Accuracy ranking on Vals is another evaluation implementation. In use, the task, the prompt, and the license are settled first, and only then is a total score discussed.

Basis of the overview: [S1](https://arxiv.org/abs/2308.11462) [S2](https://github.com/HazyResearch/legalbench) [S3](https://www.vals.ai/benchmarks/legal_bench)

## Basic information

**简称**：LegalBench [S1](https://arxiv.org/abs/2308.11462)

**全称**：LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models [S1](https://arxiv.org/abs/2308.11462)

**版本口径**：A public suite of 162 tasks (this README snapshot; no semantic version number is specified). [S2](https://github.com/HazyResearch/legalbench)

**论文修订**：arXiv v1 [S4](https://arxiv.org/abs/2308.11462)

**发布时间**：2023-08-21 07:08:03 (arXiv v1); the PDF cover says 2023-08-23, and the two are not the same date definition. [S4](https://arxiv.org/abs/2308.11462)

**主板块**：推理 [S3](https://www.vals.ai/benchmarks/legal_bench)

> Benchmark Constitution editorial filing.

**领域**：法律推理 [S1](https://arxiv.org/abs/2308.11462)

**许可与权利边界**：The repository requires each task to follow the license of the original creator of the data; the HF collection card is marked CC BY 4.0. The collection card cannot override a different grant at task level. Before use, the note for the corresponding task and the original license control. [S2](https://github.com/HazyResearch/legalbench) [S5](https://huggingface.co/datasets/nguha/legalbench)

**论文**：https://arxiv.org/abs/2308.11462 [S1](https://arxiv.org/abs/2308.11462)

**代码入口**：https://github.com/HazyResearch/legalbench [S6](https://github.com/HazyResearch/legalbench)

**数据入口**：https://huggingface.co/datasets/nguha/legalbench [S2](https://github.com/HazyResearch/legalbench)

**官网**：https://hazyresearch.stanford.edu/legalbench/ [S2](https://github.com/HazyResearch/legalbench)

**论文标题**：LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models [S1](https://arxiv.org/abs/2308.11462)

## Origin and maintenance

**发起方**：An interdisciplinary collaboration including HazyResearch (Stanford) and others [S6](https://github.com/HazyResearch/legalbench)

> Institutional affiliation follows the GitHub organization; the complete list of author affiliations is Unverified.

**署名与合作**：Author affiliations named in the paper include Stanford, University of Chicago, Dartmouth, Maxime Tools, LawBeta, Toronto, Harvard Law School, CodeX, USC, Georgetown, Virginia, Télécom Paris, York, and Casetext. This is a list of author affiliations, not a new institutional collaboration agreement. [S7](https://arxiv.org/pdf/2308.11462)

**作者**：Neel Guha and others, 40 authors (including Julian Nyarko, Daniel E. Ho, Christopher Ré, and others) [S1](https://arxiv.org/abs/2308.11462)

**维护入口**：HazyResearch/legalbench [S6](https://github.com/HazyResearch/legalbench)

**资助**：Appendix A lists NIH U54EB020405, NSF CCF1763315/CCF1563078/2204926/1937301, DEVCOM ARL W911NF-21-2-0251, ONR, Stanford CRFM/DAWN, and support from multiple companies. PH also received an Open Philanthropy AI Fellowship. The full list, and the statement that this does not represent endorsement by the funders, are in the appendix. [S7](https://arxiv.org/pdf/2308.11462)

## Design goals

**衡量能力**：Six types of reasoning: issue spotting, rule recall, rule application, rule conclusion, interpretation of legal text, and rhetorical understanding; a task with a definite answer cannot represent all of legal practice, or the quality of a legal opinion. [S7](https://arxiv.org/pdf/2308.11462)

**设计动机**：Provides a shared vocabulary for the legal profession and LLM developers, measuring reasoning skills that are practically useful or of interest to lawyers. [S1](https://arxiv.org/abs/2308.11462)

## Construction

**题目/样本来源**：36 original source collections: published datasets, human-coded data that legal scholars had not previously released, and tasks written specifically for LegalBench; for example, span extraction over long CUAD documents is changed into binary classification of clauses. [S7](https://arxiv.org/pdf/2308.11462)

**构建者背景**：40 contributors, mainly legal professionals [S6](https://github.com/HazyResearch/legalbench)

**审查流程**：After a public call in August 2022, contributors with a legal background submitted them; the authors reviewed the tasks for legal correctness and task validity (§4.1). [S7](https://arxiv.org/pdf/2308.11462)

**质量控制**：Each task provides construction notes, the legal point, a base prompt, and an example; tasks about applying a rule also have an answer guide, and they are graded by hand for correctness and for whether the necessary inferences are included. The appendix acknowledges the risk of character errors from OCR. [S7](https://arxiv.org/pdf/2308.11462)

**去污染与防泄漏**：Only some of the newly constructed tasks use a time constraint: citation_prediction takes cases dated after 2023-01-01 and interprets them under the training-cutoff assumption of that time; this is not proof of an absence of contamination for the full suite of 162 tasks or for later models. [S7](https://arxiv.org/pdf/2308.11462)

## Data format

**规模**：162 tasks, from 36 corpora; paper §4.2 lists 35 multiple-choice tasks, 7 open-generation tasks, 112 binary-classification tasks, and 8 multi-class or multi-label tasks. A task is not a sample, and 162 cannot be treated as a question count. [S7](https://arxiv.org/pdf/2308.11462)

**任务形式**：Input-output pairs (classification, extraction, generation, and others) [S6](https://github.com/HazyResearch/legalbench)

**模态**：文本 [S6](https://github.com/HazyResearch/legalbench)

**语言**：英语 [S6](https://github.com/HazyResearch/legalbench)

**难度与覆盖**：Task types and legal domains are diverse, and the paper analyzes difficulty through performance on specific tasks; no unified level or difficulty proportion was constructed from that. [S7](https://arxiv.org/pdf/2308.11462)

**公开与测试划分**：Each task publishes train/test; in the original paper, train is only a random draw of 2–8 items used as few-shot demonstrations, not a large-scale training set. [S7](https://arxiv.org/pdf/2308.11462) [S5](https://huggingface.co/datasets/nguha/legalbench)

## Evaluation

**指标**：The original paper: classification balanced accuracy, normalized extraction matching, multi-objective F1, and human correctness and analysis for rule application; the Vals leaderboard additionally reports Accuracy. [S7](https://arxiv.org/pdf/2308.11462) [S8](https://www.vals.ai/benchmarks/legal_bench)

**评分**：Classification requires an exact match first and then computes balanced accuracy. Extraction normalizes tense, case, and punctuation. Multi-label F1 is used. People with legal training score the application of rules against the answer guide. A single Accuracy cannot summarize the original version. [S7](https://arxiv.org/pdf/2308.11462)

**提示/训练/运行设置**：The original paper uses temperature=0.0; classification and extraction stop at a newline, rule_qa and most application tasks use at most 150 tokens, and diversity_jurisdiction_6 uses 300; Claude additionally receives an example tag and instructions for the answer space. [S7](https://arxiv.org/pdf/2308.11462)

**官方脚本**：evaluation.py, tasks.py, and the HELM prompt-settings files [S6](https://github.com/HazyResearch/legalbench)

**可比性警示**：Vals uses its own task subset and prompts, which differ from the original paper evaluation; the gaps among the leading scores are very small (<0.3 percentage points). [S3](https://www.vals.ai/benchmarks/legal_bench)

## Current status

**核查日**：2026-11-08 [S9](https://hazyresearch.stanford.edu/legalbench/)

**数据版本与持续使用**：A public suite of 162 tasks (this snapshot of the README)；历史持续使用证据：2026-10-13 The current method and leaderboard pages show measured results for multiple frontier models; updated October 13, a large-scale legal-reasoning comparison of 151 models, covering current frontier models. https://www.vals.ai/benchmarks/legal_bench；2026-10-13 Catalog card: Legal Academic LegalBench Updated: 10/13/2026 Models Tested: 151 Evaluating language models on a wide range of open source legal reasoning tasks. Top Models 1 Claude Fable 5 2 Claude Fable 5.1 3 Gemini 4 Argon View Details https://www.vals.ai/benchmarks [S2](https://github.com/HazyResearch/legalbench) [S8](https://www.vals.ai/benchmarks/legal_bench)

**论文版本与证据历史**：v1 2023-08-21。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S4](https://arxiv.org/abs/2308.11462)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The current first place on Vals is 88.56%, which is not a 100% ceiling; clustering of scores is not enough to show that the whole suite of 162 tasks is near saturation, and the earlier generalized judgment is withdrawn. [S8](https://www.vals.ai/benchmarks/legal_bench)

**已知问题与争议**：The original version leans toward United States law, contracts, and short text, and it covers only objective answers; OCR and sensitivity to the prompt sample can affect the results. The category counts in the original text are inconsistent in individual places between §4.2 and §4.3, and the finer statistics are not forced into alignment. [S7](https://arxiv.org/pdf/2308.11462)

**版本/衍生关系**：The README lists the adopted frameworks Vals AI and HELM Lite; they are usage and evaluation specifications, not data versions that replace the original. [S2](https://github.com/HazyResearch/legalbench)

## Leaderboard snapshot

**快照日**：2026-11-08 [S9](https://hazyresearch.stanford.edu/legalbench/)

**官方榜入口**：待核实 [S9](https://hazyresearch.stanford.edu/legalbench/)

> On this occasion the official site and the README mainly point to external evaluations; a live overall leaderboard operated by the project itself has not been verified, and "not found" is not written as "officially unmaintained."

**第三方入口**：https://www.vals.ai/benchmarks/legal_bench [S3](https://www.vals.ai/benchmarks/legal_bench)

### Vals AI independent third party

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Claude Fable 5 | 88.56% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 2 | Claude Fable 5.1 | 88.51% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 3 | Gemini 4 Argon | 88.30% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 4 | Wonder Full | 87.42% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 5 | Gemini 3.1 Pro Preview (02/26) | 87.40% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 6 | Gemini 3.7 Flash | 87.26% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 7 | Gemini 3 Pro (11/25) | 87.03% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 8 | Gemini 3.8 Flash | 86.99% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 9 | Claude Opus 5 | 86.97% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |
| 10 | GPT-5.6 Sol | 86.97% | Accuracy | [来源](https://www.vals.ai/benchmarks/legal_bench)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S8](https://www.vals.ai/benchmarks/legal_bench)

**覆盖与时效**：The Vals page that can be read now says Updated 2026-10-13 and lists 151 models in all; this entry transcribes the top ten and keeps the source order, including ties. This date is the date the page was updated, not the measurement date of each model. [S8](https://www.vals.ai/benchmarks/legal_bench)

## Contact

**公开研究邮箱**：nguha@stanford.edu [S2](https://github.com/HazyResearch/legalbench)

**问题反馈**：https://github.com/HazyResearch/legalbench/issues [S6](https://github.com/HazyResearch/legalbench)

**官方发布渠道**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**隐私口径**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Original files

**源站PDF**：https://arxiv.org/pdf/2308.11462 [S1](https://arxiv.org/abs/2308.11462)

**PDF SHA-256**：47a0759d5f5dfcc7516579c083ff5e44bfdd12164db86149f2fee8792d382122 [S7](https://arxiv.org/pdf/2308.11462)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：1204779 [S7](https://arxiv.org/pdf/2308.11462)

**原有文件夹**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**其他材料**：[{"type": "Official usage guide", "url": "https://hazyresearch.stanford.edu/legalbench/getting-started/"}, {"type": "Official HF dataset card", "url": "https://huggingface.co/datasets/nguha/legalbench"}] [S2](https://github.com/HazyResearch/legalbench)

**原有 PDF**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> This group does not upload, as the task requires; the original PDF URL is in original_files.

## Changelog

- 2026-11-07，近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S6](https://github.com/HazyResearch/legalbench) [S9](https://hazyresearch.stanford.edu/legalbench/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2308.11462](https://arxiv.org/abs/2308.11462)，访问 2026-11-07
- S2，[https://github.com/HazyResearch/legalbench](https://github.com/HazyResearch/legalbench)，访问 2026-11-08
- S3，[https://www.vals.ai/benchmarks/legal_bench](https://www.vals.ai/benchmarks/legal_bench)，访问 2026-11-07
- S4，[https://arxiv.org/abs/2308.11462](https://arxiv.org/abs/2308.11462)，访问 2026-11-08
- S5，[https://huggingface.co/datasets/nguha/legalbench](https://huggingface.co/datasets/nguha/legalbench)，访问 2026-11-08
- S6，[https://github.com/HazyResearch/legalbench](https://github.com/HazyResearch/legalbench)，访问 2026-11-07
- S7，[https://arxiv.org/pdf/2308.11462](https://arxiv.org/pdf/2308.11462)，访问 2026-11-08
- S8，[https://www.vals.ai/benchmarks/legal_bench](https://www.vals.ai/benchmarks/legal_bench)，访问 2026-11-08
- S9，[https://hazyresearch.stanford.edu/legalbench/](https://hazyresearch.stanford.edu/legalbench/)，访问 2026-11-08
