# LongBench v2
> 核验：2026-11-08（KST / Asia/Seoul）。第一轮官方证据复核完成；2026-H2使用证据已回读；未知字段和文档冲突显式保留

LongBench v2使用真实长材料上的四选一问题，重点是深层理解与推理而非单纯检索。长度单位是words；503道题虽在HF命名为train，实为公开评测题。直接回答和CoT是两个独立协议，官网数据许可与软件许可也应分开。

概述依据：[S1](https://arxiv.org/abs/2412.15204)

## 基本信息

**简称**：LongBench v2 [S1](https://arxiv.org/abs/2412.15204)

**全称**：LongBench v2 [S1](https://arxiv.org/abs/2412.15204)

**版本口径**：LongBench v2（与旧版LongBench v1区分） [S2](https://github.com/THUDM/LongBench)

**论文修订**：arXiv v2 [S3](https://arxiv.org/abs/2412.15204)

**发布时间**：2024-12-20 [S2](https://github.com/THUDM/LongBench)

> 官方README发布公告日期；与论文首发日期区分。

**主板块**：语言 [S1](https://arxiv.org/abs/2412.15204)

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

**领域**：长上下文理解 [S1](https://arxiv.org/abs/2412.15204)

**许可与权利边界**：LongBench-v2数据卡为Apache-2.0；THUDM/LongBench仓库根LICENSE为MIT（2023 THU-KEG & Zhipu AI）。分别记录数据和仓库软件授权，不混写。 [S4](https://huggingface.co/datasets/THUDM/LongBench-v2) [S5](https://github.com/THUDM/LongBench/blob/main/LICENSE)

**论文**：https://arxiv.org/abs/2412.15204 [S1](https://arxiv.org/abs/2412.15204)

**代码入口**：https://github.com/THUDM/LongBench [S1](https://arxiv.org/abs/2412.15204)

**数据入口**：https://huggingface.co/datasets/THUDM/LongBench-v2 [S1](https://arxiv.org/abs/2412.15204)

**官网**：https://longbench2.github.io/ [S1](https://arxiv.org/abs/2412.15204)

**论文标题**：LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks [S1](https://arxiv.org/abs/2412.15204)

## 发起与维护

**发起方**：论文作者单位包括清华大学、智谱；Yushi Bai 为首作者。 [S1](https://arxiv.org/abs/2412.15204)

**署名与合作**：论文首页明确作者单位为清华大学与Zhipu.AI；24名审核者从97名标注者中选出，并非额外招募24名完全独立出题者。 [S6](https://arxiv.org/pdf/2412.15204)

**作者**：Bai, Yushi；Tu, Shangqing；Zhang, Jiajie；Peng, Hao；Wang, Xiaozhi；Lv, Xin；Cao, Shulin；Xu, Jiazheng；Hou, Lei；Dong, Yuxiao；Tang, Jie；Li, Juanzi [S1](https://arxiv.org/abs/2412.15204)

**维护入口**：官方公开代码托管于 THUDM；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。 [S2](https://github.com/THUDM/LongBench)

**资助**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

**衡量能力**：检验真实长上下文中的深层理解与推理，超越简单大海捞针。 [S1](https://arxiv.org/abs/2412.15204)

**设计动机**：仅检索固定针或较易短问答不足以测量长文档、多文档、代码仓库和结构数据理解。 [S1](https://arxiv.org/abs/2412.15204)

## 构建方式

**题目/样本来源**：由标注者提交实际接触的学术、法律、小说、代码及表格材料，再依据材料编题。 [S1](https://arxiv.org/abs/2412.15204)

**构建者背景**：97 名受过高等教育的标注者、24 名专家审阅者。 [S1](https://arxiv.org/abs/2412.15204)

**审查流程**：三模型难度筛选、人工审查与返工；只有通过审核的条目才获得奖励。 [S1](https://arxiv.org/abs/2412.15204)

**质量控制**：使用选择题提高评分一致性，同时用专家限时作答估计难度。 [S1](https://arxiv.org/abs/2412.15204)

**去污染与防泄漏**：KG推理匿名化实体以防记忆；标注指南要求避免常见经典文献或设计冷门问题，拒绝不看材料即可答题，且检查文档重复。这是缓解措施，不是训练集全量无重叠保证。 [S6](https://arxiv.org/pdf/2412.15204)

## 数据形式

**规模**：503 道四选一题，6 大任务类、20 子任务；上下文 8k–2M words（词，非 token）。 [S1](https://arxiv.org/abs/2412.15204)

**任务形式**：基于长上下文的四选一选择题 [S1](https://arxiv.org/abs/2412.15204)

**模态**：文本 [S1](https://arxiv.org/abs/2412.15204)

**语言**：英语 [S1](https://arxiv.org/abs/2412.15204)

**难度与覆盖**：192 easy、311 hard；长度short<32k词180题、medium 32k–128k词215题、long>128k词108题。专家15分钟限制下53.7%，不是无时间限制的人类能力上限。 [S6](https://arxiv.org/pdf/2412.15204)

**公开与测试划分**：官方HF以 split=train 加载503道评测题，答案公开；这里的train是文件划分名，不代表适合用于训练。 [S2](https://github.com/THUDM/LongBench)

## 评测方法

**指标**：总体准确率，以及 easy/hard 和 short/medium/long 分组准确率。 [S1](https://arxiv.org/abs/2412.15204)

**评分**：从模型生成中提取最终选项，与金标准比较。 [S1](https://arxiv.org/abs/2412.15204)

**提示/训练/运行设置**：原论文零样本temperature=0.1、max_new_tokens=128；CoT先1024 tokens再第二次调用128 tokens取最终答案。代码另支持--cot、--no_context、--rag N；网页新增模型设置不可默认等于论文。 [S6](https://arxiv.org/pdf/2412.15204) [S7](https://github.com/THUDM/LongBench)

**官方脚本**：https://github.com/THUDM/LongBench [S2](https://github.com/THUDM/LongBench)

**可比性警示**：words 不等于 tokens；上下文截断、CoT、思考预算和 YaRN 会影响结果。官网脚注说明 Qwen 结果使用 YaRN factor4，不能照搬为原论文所有模型设置。 [S1](https://arxiv.org/abs/2412.15204)

## 最新情况

**核查日**：2026-11-08 KST / Asia/Seoul [S8](https://longbench2.github.io/)

**数据版本与持续使用**：v2 [S9](https://huggingface.co/datasets/THUDM/LongBench-v2)

**论文版本与证据历史**：v1 2024-12-20T03:59:17+09:00（KST）；v2 2025-01-03T20:44:51+09:00（KST）。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S3](https://arxiv.org/abs/2412.15204)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为KST。

**饱和度边界**：官网可读最高 overall w/CoT 为 63.3%，不足以据此宣布全部长上下文任务已饱和；其静态表更新时间也需谨慎。 [S10](https://longbench2.github.io/)

**已知问题与争议**：论文主体与官网人类分数为 53.7%；论文结论曾出现 50.1%，该数值亦为 GPT-4o 的历史直接回答分数。本条采用主体及官网的人类 53.7%，保留冲突说明。 [S1](https://arxiv.org/abs/2412.15204)

**版本/衍生关系**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

**快照日**：2026-11-08 KST / Asia/Seoul [S11](https://longbench2.github.io/#leaderboard)

**官方榜入口**：https://longbench2.github.io/#leaderboard [S10](https://longbench2.github.io/)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 官方：直接回答

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Human | 53.7% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 2 | MiniMax-Text-01 MiniMax | 52.9% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 3 | GPT-4o OpenAI | 50.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 4 | Gemini-Exp-1206 Google | 49.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 5 | Gemini-2.0-Flash Google | 47.4% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 6 | Qwen3-235B-A22B-Instruct-2507 Alibaba | 46.7% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 7 | GPT-4o OpenAI | 46.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 8 | Kimi-K2-Instruct Moonshot AI | 44.9% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 9 | GLM-4-Plus Z.ai & Tsinghua | 44.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 10 | Qwen2.5-72B Alibaba | 42.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 11 | Claude 3.5 Sonnet Anthropic | 41.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 12 | Qwen3-235B-A22B | 40.4% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 13 | Qwen3-32B | 38.8% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 14 | o1-mini OpenAI | 37.8% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 15 | Mistral Large 24.11 Mistral AI | 34.4% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 16 | Qwen3-30B-A3B | 32.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 17 | Llama 3.1 70B Meta | 31.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 18 | Nemotron 70B Nvidia | 31.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 19 | NExtLong 8B CAS | 30.8% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 20 | GLM-4-9B Z.ai & Tsinghua | 30.2% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 21 | Qwen2.5-7B Alibaba | 30.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 22 | Llama 3.1 8B Meta | 30.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 23 | Llama 3.3 70B Meta | 29.8% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 24 | GPT-4o mini OpenAI | 29.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 25 | Command R+ Cohere | 27.8% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 26 | Mistral Large 2 Mistral AI | 26.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 27 | Random | 25.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |

### 官方：w/ CoT

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Gemini-2.5-Pro | 63.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 2 | Gemini-2.5-Flash | 62.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 3 | Qwen3-235B-A22B-Thinking-2507 | 60.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 4 | DeepSeek-R1 | 58.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 5 | Qwen3-235B-A22B-Instruct-2507 Alibaba | 58.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 6 | o1-preview | 57.7% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 7 | DeepSeek-R1-0528 | 56.7% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 8 | MiniMax-Text-01 MiniMax | 56.5% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 9 | Gemini-2.0-Flash-Thinking | 56.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 10 | Human | 53.7% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 11 | Gemini-Exp-1206 Google | 52.5% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 12 | GPT-4o OpenAI | 51.4% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 13 | GPT-4o OpenAI | 51.2% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 14 | Gemini-2.0-Flash Google | 51.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 15 | GLM-4.5 | 50.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 16 | Qwen3-30B-A3B-Thinking-2507 | 50.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 17 | Qwen3-235B-A22B | 50.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 18 | Qwen3-32B | 49.2% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 19 | QwQ-32B | 48.9% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 20 | GLM-4.5-Air | 48.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 21 | Claude 3.5 Sonnet Anthropic | 46.7% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 22 | GLM-4-Plus Z.ai & Tsinghua | 46.1% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 23 | Kimi-K2-Instruct Moonshot AI | 44.3% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 24 | Qwen2.5-72B Alibaba | 43.5% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 25 | Qwen3-30B-A3B | 42.5% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 26 | Mistral Large 24.11 Mistral AI | 39.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 27 | o1-mini OpenAI | 38.9% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 28 | Llama 3.1 70B Meta | 36.2% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 29 | Llama 3.3 70B Meta | 36.2% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 30 | Qwen2.5-7B Alibaba | 35.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 31 | Nemotron 70B Nvidia | 35.2% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 32 | Mistral Large 2 Mistral AI | 33.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 33 | GPT-4o mini OpenAI | 32.4% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 34 | NExtLong 8B CAS | 32.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 35 | Command R+ Cohere | 31.6% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 36 | GLM-4-9B Z.ai & Tsinghua | 30.8% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 37 | Llama 3.1 8B Meta | 30.4% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |
| 38 | Random | 25.0% | Overall accuracy | [来源](https://longbench2.github.io/) · 2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S8](https://longbench2.github.io/)

**覆盖与时效**：转录官方表全部可读直接回答与CoT单元格，分别排序，不把“-”填0；保留模型名、上下文长度及原Date。网页页脚Last Update 2025-05-06但表内有2025-07行，日期矛盾仍保留。 [S8](https://longbench2.github.io/)

## 联系方式

**公开研究邮箱**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

**问题反馈**：https://github.com/THUDM/LongBench/issues [S2](https://github.com/THUDM/LongBench)

**官方发布渠道**：https://x.com/realYushiBai/status/1869946577349132766 [S7](https://github.com/THUDM/LongBench)

> 官方README所链接的项目发布Thread；未在本轮读取X内容。

**隐私口径**：只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。 [S12](urn:benchmark-atlas:constitution:v0.1)

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2412.15204 [S13](https://arxiv.org/pdf/2412.15204)

**PDF SHA-256**：35e7e66bb3323d8da0a6dde553a9f5fc9be97ed3232d87a24be89f5a8f9024d5 [S6](https://arxiv.org/pdf/2412.15204)

> 本次下载的源站PDF字节校验；不声称重传或替换既有Drive副本。

**PDF字节数**：9951437 [S6](https://arxiv.org/pdf/2412.15204)

**原有Drive文件夹**：{"id": "1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE", "webViewLink": "https://drive.google.com/drive/folders/1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE"} [S14](https://drive.google.com/drive/folders/1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE)

**其他材料**：[{"kind": "中文介绍 Google Doc", "id": "17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8", "webViewLink": "https://docs.google.com/document/d/17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8/edit?usp=drivesdk"}] [S15](https://docs.google.com/document/d/17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8/edit?usp=drivesdk)

**原有Drive PDF**：{"id": "1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx", "webViewLink": "https://drive.google.com/file/d/1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx/view?usp=drivesdk"} [S16](https://drive.google.com/file/d/1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx/view?usp=drivesdk)

## 变更记录

- 2026-11-07 · 首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- 2026-11-07 · 第一轮深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- 2026-11-08 · 第二轮逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S1](https://arxiv.org/abs/2412.15204) [S13](https://arxiv.org/pdf/2412.15204) [S2](https://github.com/THUDM/LongBench) [S8](https://longbench2.github.io/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1 · [https://arxiv.org/abs/2412.15204](https://arxiv.org/abs/2412.15204) · 访问 2026-11-07
- S2 · [https://github.com/THUDM/LongBench](https://github.com/THUDM/LongBench) · 访问 2026-11-07
- S3 · [https://arxiv.org/abs/2412.15204](https://arxiv.org/abs/2412.15204) · 访问 2026-11-08
- S4 · [https://huggingface.co/datasets/THUDM/LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2) · 访问 2026-11-08
- S5 · [https://github.com/THUDM/LongBench/blob/main/LICENSE](https://github.com/THUDM/LongBench/blob/main/LICENSE) · 访问 2026-11-08
- S6 · [https://arxiv.org/pdf/2412.15204](https://arxiv.org/pdf/2412.15204) · 访问 2026-11-08
- S7 · [https://github.com/THUDM/LongBench](https://github.com/THUDM/LongBench) · 访问 2026-11-08
- S8 · [https://longbench2.github.io/](https://longbench2.github.io/) · 访问 2026-11-08
- S9 · [https://huggingface.co/datasets/THUDM/LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2) · 访问 2026-11-07
- S10 · [https://longbench2.github.io/](https://longbench2.github.io/) · 访问 2026-11-07
- S11 · [https://longbench2.github.io/#leaderboard](https://longbench2.github.io/#leaderboard) · 访问 2026-11-08
- S12 · [urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1) · 访问 2026-11-07
- S13 · [https://arxiv.org/pdf/2412.15204](https://arxiv.org/pdf/2412.15204) · 访问 2026-11-07
- S14 · [https://drive.google.com/drive/folders/1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE](https://drive.google.com/drive/folders/1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE) · 访问 2026-11-07
- S15 · [https://docs.google.com/document/d/17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8/edit?usp=drivesdk](https://docs.google.com/document/d/17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8/edit?usp=drivesdk) · 访问 2026-11-07
- S16 · [https://drive.google.com/file/d/1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx/view?usp=drivesdk](https://drive.google.com/file/d/1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx/view?usp=drivesdk) · 访问 2026-11-07
