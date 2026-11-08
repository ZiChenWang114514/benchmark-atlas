# LegalBench
> 核验：2026-11-08。已核验存在；近期热门新建条目，未核实字段保留标记；trending: B

LegalBench不是一张统一的法律考试卷，而是围绕六类法律推理组织的162任务集合。原版分类采用balanced accuracy，规则适用还含法律背景人员的人工审阅；Vals的Accuracy排行是另一套评测实现。使用时先确定任务、提示和许可，再谈总分。

概述依据：[S1](https://arxiv.org/abs/2308.11462) [S2](https://github.com/HazyResearch/legalbench) [S3](https://www.vals.ai/benchmarks/legal_bench)

## 基本信息

**简称**：LegalBench [S1](https://arxiv.org/abs/2308.11462)

**全称**：LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models [S1](https://arxiv.org/abs/2308.11462)

**版本口径**：162任务公开套件（本次README快照；未指定语义版本号） [S2](https://github.com/HazyResearch/legalbench)

**论文修订**：arXiv v1 [S4](https://arxiv.org/abs/2308.11462)

**发布时间**：2023-08-21 07:08:03 （arXiv v1）；PDF封面写2023-08-23，二者不是同一日期口径。 [S4](https://arxiv.org/abs/2308.11462)

**主板块**：推理 [S3](https://www.vals.ai/benchmarks/legal_bench)

> Benchmark Atlas 编辑归档。

**领域**：法律推理 [S1](https://arxiv.org/abs/2308.11462)

**许可与权利边界**：仓库要求逐任务遵守原数据创建者许可；HF总卡标CC BY 4.0。总卡不能覆盖任务级不同授权，使用前以对应任务说明及原始许可为准。 [S2](https://github.com/HazyResearch/legalbench) [S5](https://huggingface.co/datasets/nguha/legalbench)

**论文**：https://arxiv.org/abs/2308.11462 [S1](https://arxiv.org/abs/2308.11462)

**代码入口**：https://github.com/HazyResearch/legalbench [S6](https://github.com/HazyResearch/legalbench)

**数据入口**：https://huggingface.co/datasets/nguha/legalbench [S2](https://github.com/HazyResearch/legalbench)

**官网**：https://hazyresearch.stanford.edu/legalbench/ [S2](https://github.com/HazyResearch/legalbench)

**论文标题**：LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models [S1](https://arxiv.org/abs/2308.11462)

## 发起与维护

**发起方**：HazyResearch（Stanford）等跨学科合作 [S6](https://github.com/HazyResearch/legalbench)

> 机构归属以 GitHub 组织为准，作者单位完整列表待核实。

**署名与合作**：论文署名单位包括Stanford、University of Chicago、Dartmouth、Maxime Tools、LawBeta、Toronto、Harvard Law School、CodeX、USC、Georgetown、Virginia、Télécom Paris、York、Casetext等；这是作者单位列表，不是新增机构合作协议。 [S7](https://arxiv.org/pdf/2308.11462)

**作者**：Neel Guha 等40位作者（含 Julian Nyarko、Daniel E. Ho、Christopher Ré 等） [S1](https://arxiv.org/abs/2308.11462)

**维护入口**：HazyResearch/legalbench [S6](https://github.com/HazyResearch/legalbench)

**资助**：附录A列NIH U54EB020405、NSF CCF1763315/CCF1563078/2204926/1937301、DEVCOM ARL W911NF-21-2-0251、ONR、Stanford CRFM/DAWN及多家企业支持；PH另获Open Philanthropy AI Fellowship。完整名单及不代表资助方背书声明见附录。 [S7](https://arxiv.org/pdf/2308.11462)

## 设计目标

**衡量能力**：问题识别、规则回忆、规则适用、规则结论、法律文本解释、修辞理解六类推理；有明确答案的任务不能代表所有法律实践或法律意见质量。 [S7](https://arxiv.org/pdf/2308.11462)

**设计动机**：为法律界与 LLM 开发者提供共同词汇，衡量实际有用或律师感兴趣的推理技能。 [S1](https://arxiv.org/abs/2308.11462)

## 构建方式

**题目/样本来源**：36种原始语料：已发表数据集、法律学者此前未发布的人工编码数据，以及专为LegalBench编写的任务；例如将CUAD长文档跨度抽取改成条款二分类。 [S7](https://arxiv.org/pdf/2308.11462)

**构建者背景**：40 位贡献者，以法律专业人士为主 [S6](https://github.com/HazyResearch/legalbench)

**审查流程**：2022年8月公开征集后，由法律背景贡献者提交；作者对任务进行法律正确性与任务有效性审查（§4.1）。 [S7](https://arxiv.org/pdf/2308.11462)

**质量控制**：每任务提供构建说明、法律意义、基础提示和示例；规则适用任务另有answer guide，按正确性与是否包含必要推断人工评阅。附录承认OCR字符错误风险。 [S7](https://arxiv.org/pdf/2308.11462)

**去污染与防泄漏**：仅部分新构任务采取时间约束：citation_prediction采2023-01-01之后判例，并以当时训练截止假设解释；不是全套162任务或后续模型的无污染证明。 [S7](https://arxiv.org/pdf/2308.11462)

## 数据形式

**规模**：162任务，来自36种语料；论文§4.2列35多选、7开放生成、112二分类、8多类/多标签任务。任务不是样本，不能将162当题量。 [S7](https://arxiv.org/pdf/2308.11462)

**任务形式**：输入-输出对（分类、抽取、生成等） [S6](https://github.com/HazyResearch/legalbench)

**模态**：文本 [S6](https://github.com/HazyResearch/legalbench)

**语言**：英语 [S6](https://github.com/HazyResearch/legalbench)

**难度与覆盖**：任务类型和法律领域多样，论文以具体任务表现分析难度；没有据此补造统一等级或难度比例。 [S7](https://arxiv.org/pdf/2308.11462)

**公开与测试划分**：各任务公开train/test；原论文train仅随机抽2–8条作为few-shot演示，而非大规模训练集。 [S7](https://arxiv.org/pdf/2308.11462) [S5](https://huggingface.co/datasets/nguha/legalbench)

## 评测方法

**指标**：原论文：分类balanced accuracy、归一化抽取匹配、多目标F1及规则适用人工正确性/分析；Vals榜另报Accuracy。 [S7](https://arxiv.org/pdf/2308.11462) [S8](https://www.vals.ai/benchmarks/legal_bench)

**评分**：分类先精确匹配再计算balanced accuracy；抽取做时态/大小写/标点归一化；多标签F1；法律训练人员参照answer guide评规则适用。不能用单一Accuracy概括原版。 [S7](https://arxiv.org/pdf/2308.11462)

**提示/训练/运行设置**：原论文temperature=0.0；分类/抽取遇换行停止，rule_qa及多数application最多150 tokens，diversity_jurisdiction_6为300；Claude另加example标签与答案空间指令。 [S7](https://arxiv.org/pdf/2308.11462)

**官方脚本**：evaluation.py、tasks.py 与 HELM 提示设置文件 [S6](https://github.com/HazyResearch/legalbench)

**可比性警示**：Vals 自定任务子集与提示，不同于论文原始评测；前列分差极小（<0.3个百分点）。 [S3](https://www.vals.ai/benchmarks/legal_bench)

## 最新情况

**核查日**：2026-11-08 [S9](https://hazyresearch.stanford.edu/legalbench/)

**数据版本与持续使用**：162任务公开套件（README本次快照）；历史持续使用证据：2026-10-13 当前方法与榜单页展示多家前沿模型的实测结果；10月13日更新、151模型的大规模法律推理对比，覆盖当前前沿模型。 https://www.vals.ai/benchmarks/legal_bench；2026-10-13 目录卡片：Legal Academic LegalBench Updated: 10/13/2026 Models Tested: 151 Evaluating language models on a wide range of open source legal reasoning tasks. Top Models 1 Claude Fable 5 2 Claude Fable 5.1 3 Gemini 4 Argon View Details https://www.vals.ai/benchmarks [S2](https://github.com/HazyResearch/legalbench) [S8](https://www.vals.ai/benchmarks/legal_bench)

**论文版本与证据历史**：v1 2023-08-21。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S4](https://arxiv.org/abs/2308.11462)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为。

**饱和度边界**：Vals当前第一名88.56%，不等于100%上限；分数聚集不足以证明整个162任务套件接近饱和，撤回此前泛化判断。 [S8](https://www.vals.ai/benchmarks/legal_bench)

**已知问题与争议**：原版偏美国法、合同与短文本，且仅覆盖客观答案；OCR和提示样本敏感性会影响结果。原文分类数量在§4.2与§4.3有个别不一致，细分统计不自行强行对齐。 [S7](https://arxiv.org/pdf/2308.11462)

**版本/衍生关系**：README列采用框架Vals AI与HELM Lite；它们是使用/评测口径而非替代原版的数据版本。 [S2](https://github.com/HazyResearch/legalbench)

## 榜单快照

**快照日**：2026-11-08 [S9](https://hazyresearch.stanford.edu/legalbench/)

**官方榜入口**：待核实 [S9](https://hazyresearch.stanford.edu/legalbench/)

> 本次官网与README主要指向外部评测；尚未核实一份项目自营实时总榜，不将“未找到”写成“官方不维护”。

**第三方入口**：https://www.vals.ai/benchmarks/legal_bench [S3](https://www.vals.ai/benchmarks/legal_bench)

### Vals AI独立第三方

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
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

**覆盖与时效**：当前可读Vals页写Updated 2026-10-13，共151模型；本条转录前十，保留来源顺序（含同分），此日期是页面更新日，不是逐模型测量日。 [S8](https://www.vals.ai/benchmarks/legal_bench)

## 联系方式

**公开研究邮箱**：nguha@stanford.edu [S2](https://github.com/HazyResearch/legalbench)

**问题反馈**：https://github.com/HazyResearch/legalbench/issues [S6](https://github.com/HazyResearch/legalbench)

**官方发布渠道**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**隐私口径**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2308.11462 [S1](https://arxiv.org/abs/2308.11462)

**PDF SHA-256**：47a0759d5f5dfcc7516579c083ff5e44bfdd12164db86149f2fee8792d382122 [S7](https://arxiv.org/pdf/2308.11462)

> 本次下载的源站PDF字节校验；不声称重传或替换既有副本。

**PDF字节数**：1204779 [S7](https://arxiv.org/pdf/2308.11462)

**原有文件夹**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**其他材料**：[{"type": "官方使用指南", "url": "https://hazyresearch.stanford.edu/legalbench/getting-started/"}, {"type": "官方HF数据卡", "url": "https://huggingface.co/datasets/nguha/legalbench"}] [S2](https://github.com/HazyResearch/legalbench)

**原有 PDF**：待核实 [S6](https://github.com/HazyResearch/legalbench)

> 本组按任务要求不上传；原始PDF URL见original_files。

## 变更记录

- 2026-11-07，近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
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
