# MathVerse
> 核验：2026-11-08。已核实存在且有2026年下半年实际使用证据；官方实时榜单覆盖及未核验字段逐项标示。

MathVerse通过改变同一题中图文信息的分配，检查模型是否真的利用数学图解。应分清2,612原题、六版本构建总量及公开testmini的788原题；All只汇总五种多模态版本，Text Only另作消融，CoT-E与w/o成绩也不得混排。

概述依据：[S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

## 基本信息

**简称**：MathVerse [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**全称**：MathVerse [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**版本口径**：公开testmini评测集（788原题；五多模态版本+单独Text Only消融）；完整构建集为2,612原题。 [S4](https://github.com/ZrrSkywalker/MathVerse) [S5](https://huggingface.co/datasets/AI4Math/MathVerse)

**论文修订**：arXiv v2 [S6](https://arxiv.org/abs/2403.14624)

**发布时间**：2024-03-21 [S2](https://arxiv.org/abs/2403.14624)

> arXiv元数据首发日期原值；不是推测数据集首次上线时间。

**主板块**：多模态 [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

> Benchmark Atlas编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

**领域**：图解数学推理 [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**许可与权利边界**：MIT（官方HF元数据；来源图/题第三方权利须单独检查） [S7](https://huggingface.co/datasets/AI4Math/MathVerse/blob/main/README.md)

**论文**：https://arxiv.org/abs/2403.14624 [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**代码入口**：https://github.com/ZrrSkywalker/MathVerse [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**数据入口**：https://huggingface.co/datasets/AI4Math/MathVerse [S1](https://mathverse-cuhk.github.io/) [S8](https://huggingface.co/datasets/AI4Math/MathVerse)

**官网**：https://mathverse-cuhk.github.io/ [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**论文标题**：MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems? [S2](https://arxiv.org/abs/2403.14624)

## 发起与维护

**发起方**：论文作者单位：香港中文大学MMLab、上海人工智能实验室、UCLA。 [S9](https://arxiv.org/pdf/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**署名与合作**：论文作者单位为CUHK MMLab、Shanghai AI Laboratory及UCLA；按署名记录，不扩大为其他合作协议。 [S10](https://arxiv.org/pdf/2403.14624)

**作者**：Zhang, Renrui；Jiang, Dongzhi；Zhang, Yichi；Lin, Haokun；Guo, Ziyu；Qiu, Pengshuo；Zhou, Aojun；Lu, Pan；Chang, Kai-Wei；Gao, Peng；Li, Hongsheng [S2](https://arxiv.org/abs/2403.14624)

**维护入口**：官方公开维护入口ZrrSkywalker/MathVerse，LICENSE署名Renrui Zhang；责任人分工不从GitHub名称推定。 [S4](https://github.com/ZrrSkywalker/MathVerse) [S11](https://github.com/ZrrSkywalker/MathVerse/blob/main/LICENSE)

**资助**：待核实 [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

> 本批尚未完成此字段的精确核验；不等于官方未公开。

## 设计目标

**衡量能力**：检验模型是否真正读取数学图解，而非依赖题干中的视觉信息转述。 [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**设计动机**：现有视觉数学题常在文字中泄露图中信息，模型不看图也能答对。 [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

## 构建方式

**题目/样本来源**：收集2,612道带图数学题，其中1,236来自公开题库、1,376来自已有基准；人工生成六种图文信息量不同的版本。 [S9](https://arxiv.org/pdf/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**构建者背景**：专业标注者审查平面几何、立体几何、函数题并分类。 [S9](https://arxiv.org/pdf/2403.14624)

**审查流程**：专家逐题审核，按12个细类别分类；构造Text Dominant、Text Lite、Text Only、Vision Intensive、Vision Dominant、Vision Only版本。 [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**质量控制**：专家逐题审核，按12个细类别分类；构造Text Dominant、Text Lite、Text Only、Vision Intensive、Vision Dominant、Vision Only版本。 [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**去污染与防泄漏**：从公开题源和已有基准收集，再人工改写图文信息；六版本控制的是可见信息量，不是训练集污染检测。原论文未给可验证的全体前沿模型无污染保证。 [S10](https://arxiv.org/pdf/2403.14624) [S4](https://github.com/ZrrSkywalker/MathVerse)

## 数据形式

**规模**：2,612原始题、15,672版本化样本；testmini 788原题、4,728样本。当前HF多模态配置3,940行与text-only配置788行分开，不能把3,940当原题数。 [S9](https://arxiv.org/pdf/2403.14624) [S8](https://huggingface.co/datasets/AI4Math/MathVerse)

**任务形式**：数学图解单选/开放问答；同一道题的六个信息版本。 [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**模态**：图像+文本（部分样本或版本仅文本） [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**语言**：英语题面与提示（数据卡language与公开样例）；不把题源网站的原始语种自动算成数据集语言。 [S5](https://huggingface.co/datasets/AI4Math/MathVerse)

**难度与覆盖**：平面几何、立体几何、函数三个大类、12细类；不是难度等级分布。 [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**公开与测试划分**：testmini公开788原题；五种多模态版本共3,940样本计算All，另788个Text Only样本做消融，不计入五版本All。 [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

## 评测方法

**指标**：官方目前以w/o CoT-E答案准确率为主；CoT-E另由GPT-4(V)提取关键步骤并逐步判定推理。 [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**评分**：官方目前以w/o CoT-E答案准确率为主；CoT-E另由GPT-4(V)提取关键步骤并逐步判定推理。 [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**提示/训练/运行设置**：官方w/o主指标采用query_wo直接回答；CoT-E采用query_cot；优先lmms-eval mathverse_testmini并记录单版本子任务及提示。自评分两阶段为答案抽取和答案评分。 [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**官方脚本**：https://github.com/ZrrSkywalker/MathVerse [S12](https://github.com/ZrrSkywalker/MathVerse)

**可比性警示**：All只聚合五种多模态版本；Text Only为另行消融。--quick_match字符串匹配更快但官方提示不够准确；CoT-E、w/o及MMVistaReason CompassVerifier研究设置不能直接混排。 [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

## 最新情况

**核查日**：2026-11-08 [S13](https://mathverse-cuhk.github.io/)

**数据版本与持续使用**：公开评测仍按testmini及testmini_text_only两配置；论文2,612原题总量与HF 3,940+788版本化行数各有不同分母。 [S4](https://github.com/ZrrSkywalker/MathVerse) [S5](https://huggingface.co/datasets/AI4Math/MathVerse)

**论文版本与证据历史**：v1 2024-03-22；v2 2024-08-18。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S6](https://arxiv.org/abs/2403.14624)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为。

**饱和度边界**：官方testmini w/o CoT-E表最高61.7%，不能把另列CoT-E分数混入判断，也不能代替完整2,612原题表现的结论。 [S13](https://mathverse-cuhk.github.io/)

**已知问题与争议**：六种版本、CoT-E/w/o及All定义须固定；3,940多模态样本和788原题不是题量冲突。 [S2](https://arxiv.org/abs/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md) [S14](https://arxiv.org/html/2610.01352v2)

**版本/衍生关系**：六种图文版本是同一原题的信息消融，不作六套独立基准；lmms-eval的mathverse_testmini是实现入口，亦不扩充基准计数。 [S4](https://github.com/ZrrSkywalker/MathVerse)

## 榜单快照

**快照日**：2026-11-08 [S15](https://mathverse-cuhk.github.io/#leaderboard)

**官方榜入口**：https://mathverse-cuhk.github.io/#leaderboard [S1](https://mathverse-cuhk.github.io/)

**第三方入口**：待核实 [S16](https://artificialanalysis.ai/evaluations?skill=multimodal)

> 本次打开AA评测目录，未确认该原始基准的独立追踪页。AA追踪MMMU-Pro不等于追踪MMMU原版；不拿LMArena偏好Elo或其他基准分数替代。Epoch/LMArena的同口径结果仍待逐项核实。

### 历史研究论文 / 保留原采集日期

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | MMVistaReason-4B (MVR-4B) | 79.7 | 论文协议答案正确率（CompassVerifier） | [来源](https://arxiv.org/html/2610.01352v2) · 2026-11-07 |
| 2 | MMVistaReason-9B (MVR-9B) | 82.4 | 论文协议答案正确率（CompassVerifier） | [来源](https://arxiv.org/html/2610.01352v2) · 2026-11-07 |

### 官方testmini / All CoT-E

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | GPT-4V | 54.4% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 2 | Qwen-VL-Max | 37.2% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 3 | Gemini-Pro | 35.3% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 4 | LLaVA-NeXT-34B | 34.6% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 5 | InternLM-XComposer2-VL-7B | 25.9% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 6 | SPHINX-MoE | 22.8% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 7 | Qwen-VL-Plus | 21.3% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 8 | ShareGPT4V-13B | 17.4% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 9 | LLaVA-NeXT-13B | 17.2% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 10 | G-LLaVA-13B | 16.4% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 11 | G-LLaVA-7B | 15.7% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 12 | SPHINX-Plus | 14.0% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 13 | LLaVA-1.5-13B | 12.7% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 14 | MiniGPT-v2-7B | 10.9% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 15 | mPLUG-Owl2-7B | 10.3% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 16 | ImageBind-LLM | 10.0% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 17 | LLaMA-Adapter V2 | 5.8% | 官方All CoT-E | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |

### 官方testmini / All w/o CoT-E

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Human Performance* | 64.9% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 2 | VL-Rethinker-72B | 61.7% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 3 | VL-Rethinker-7B | 54.2% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 4 | GPT-4V | 39.4% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 5 | Qwen-VL-Max | 25.3% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 6 | LLaVA-NeXT-34B | 23.8% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 7 | Gemini-Pro | 23.5% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 8 | G-LLaVA-13B | 16.9% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 9 | G-LLaVA-7B | 16.6% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 10 | InternLM-XComposer2-VL-7B | 16.5% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 11 | LLaVA-NeXT-13B | 15.6% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 12 | SPHINX-MoE | 15.0% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 13 | ShareGPT4V-13B | 13.1% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 14 | Random Chance | 12.4% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 15 | SPHINX-Plus | 12.2% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 16 | Qwen-VL-Plus | 11.8% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 17 | MiniGPT-v2-7B | 11.0% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 18 | ImageBind-LLM | 9.2% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 19 | LLaVA-1.5-13B | 7.6% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 20 | mPLUG-Owl2-7B | 5.9% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |
| 21 | LLaMA-Adapter V2 | 5.7% | 官方All w/o | [来源](https://mathverse-cuhk.github.io/) · 2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S13](https://mathverse-cuhk.github.io/) [S13](https://mathverse-cuhk.github.io/) [S17](https://arxiv.org/html/2610.01352v2)

**覆盖与时效**：完整转录官方可读All CoT-E与w/o两条赛道，并保存六版本单元格；Text Only仅消融，不算五版本All。保留已有H2论文记录及旧采集日，不当本次重测或全球SOTA。 [S13](https://mathverse-cuhk.github.io/)

## 联系方式

**公开研究邮箱**：jdzcarr7@gmail.com [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

> 项目官方公开联系/榜单提交或版权反馈邮箱；未发送任何邮件。

**问题反馈**：https://github.com/ZrrSkywalker/MathVerse/issues [S12](https://github.com/ZrrSkywalker/MathVerse)

**官方发布渠道**：待核实 [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

> 本批尚未完成此字段的精确核验；不等于官方未公开。

**隐私口径**：仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。 [S18](urn:benchmark-atlas:constitution:v0.1)

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2403.14624 [S2](https://arxiv.org/abs/2403.14624) [S9](https://arxiv.org/pdf/2403.14624)

**PDF SHA-256**：9eb1f3c95cb78e80ab280191a3c459599af725152121f1d987c5c6282c09b18b [S10](https://arxiv.org/pdf/2403.14624)

> 本次下载的源站PDF字节校验；不声称重传或替换既有副本。

**PDF字节数**：5598195 [S10](https://arxiv.org/pdf/2403.14624)

**原有文件夹**：{"id": "1EgsP1-Zm7CkY5a_mLHgspdKsiyOsnFOi", "webViewLink": " [S19](

**其他材料**：[{"kind": "中文介绍 Google Doc", "id": "1Y-1EkoyNsWvUfR9pJbYn4DN1YqP3N_DRHMN9RZht_n4", "webViewLink": " [S20](

**原有 PDF**：{"id": "1XMpETqBdB0LhwZVfNfFhnyaVHnt_R5Yy", "webViewLink": " [S21](

## 变更记录

- 2026-11-07 · 核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- 2026-11-07 · 深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- 2026-11-08 · 逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/) [S13](https://mathverse-cuhk.github.io/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1 · [https://mathverse-cuhk.github.io/](https://mathverse-cuhk.github.io/) · 访问 2026-11-07
- S2 · [https://arxiv.org/abs/2403.14624](https://arxiv.org/abs/2403.14624) · 访问 2026-11-07
- S3 · [https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md) · 访问 2026-11-07
- S4 · [https://github.com/ZrrSkywalker/MathVerse](https://github.com/ZrrSkywalker/MathVerse) · 访问 2026-11-08
- S5 · [https://huggingface.co/datasets/AI4Math/MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse) · 访问 2026-11-08
- S6 · [https://arxiv.org/abs/2403.14624](https://arxiv.org/abs/2403.14624) · 访问 2026-11-08
- S7 · [https://huggingface.co/datasets/AI4Math/MathVerse/blob/main/README.md](https://huggingface.co/datasets/AI4Math/MathVerse/blob/main/README.md) · 访问 2026-11-07
- S8 · [https://huggingface.co/datasets/AI4Math/MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse) · 访问 2026-11-07
- S9 · [https://arxiv.org/pdf/2403.14624](https://arxiv.org/pdf/2403.14624) · 访问 2026-11-07
- S10 · [https://arxiv.org/pdf/2403.14624](https://arxiv.org/pdf/2403.14624) · 访问 2026-11-08
- S11 · [https://github.com/ZrrSkywalker/MathVerse/blob/main/LICENSE](https://github.com/ZrrSkywalker/MathVerse/blob/main/LICENSE) · 访问 2026-11-08
- S12 · [https://github.com/ZrrSkywalker/MathVerse](https://github.com/ZrrSkywalker/MathVerse) · 访问 2026-11-07
- S13 · [https://mathverse-cuhk.github.io/](https://mathverse-cuhk.github.io/) · 访问 2026-11-08
- S14 · [https://arxiv.org/html/2610.01352v2](https://arxiv.org/html/2610.01352v2) · 访问 2026-11-07
- S15 · [https://mathverse-cuhk.github.io/#leaderboard](https://mathverse-cuhk.github.io/#leaderboard) · 访问 2026-11-08
- S16 · [https://artificialanalysis.ai/evaluations?skill=multimodal](https://artificialanalysis.ai/evaluations?skill=multimodal) · 访问 2026-11-07
- S17 · [https://arxiv.org/html/2610.01352v2](https://arxiv.org/html/2610.01352v2) · 访问 2026-11-08
- S18 · [urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1) · 访问 2026-11-07
- S19 · [ · 访问 2026-11-07
- S20 · [ · 访问 2026-11-07
- S21 · [ · 访问 2026-11-07
