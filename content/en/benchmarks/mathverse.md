# MathVerse
> Verification: 2026-11-08. Verified to exist, with evidence of actual use in the second half of 2026; official live-leaderboard coverage and unverified fields are marked item by item.

MathVerse checks whether a model truly uses a mathematical diagram, by changing how information is divided between the figure and the text in the same question. The 2,612 original questions, the total constructed across the six versions, and the 788 original questions in the public testmini should be kept distinct; All summarizes only the five multimodal versions, Text Only is a separate ablation, and CoT-E scores and w/o scores must not be ranked together.

Basis of the overview: [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

## Basic information

**简称**：MathVerse [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**全称**：MathVerse [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**版本口径**：The public testmini evaluation set (788 original questions; five multimodal versions plus a separate Text Only ablation); the full construction set is 2,612 original questions. [S4](https://github.com/ZrrSkywalker/MathVerse) [S5](https://huggingface.co/datasets/AI4Math/MathVerse)

**论文修订**：arXiv v2 [S6](https://arxiv.org/abs/2403.14624)

**发布时间**：2024-03-21 [S2](https://arxiv.org/abs/2403.14624)

> The original first-release date in the arXiv metadata; not an inferred time when the dataset first went online.

**主板块**：多模态 [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. The classification is not claimed to be set by the benchmark's maintainers.

**领域**：Diagrammatic mathematical reasoning [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**许可与权利边界**：MIT (official HF metadata; third-party rights in source figures and questions must be checked separately) [S7](https://huggingface.co/datasets/AI4Math/MathVerse/blob/main/README.md)

**论文**：https://arxiv.org/abs/2403.14624 [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**代码入口**：https://github.com/ZrrSkywalker/MathVerse [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**数据入口**：https://huggingface.co/datasets/AI4Math/MathVerse [S1](https://mathverse-cuhk.github.io/) [S8](https://huggingface.co/datasets/AI4Math/MathVerse)

**官网**：https://mathverse-cuhk.github.io/ [S1](https://mathverse-cuhk.github.io/) [S2](https://arxiv.org/abs/2403.14624)

**论文标题**：MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems? [S2](https://arxiv.org/abs/2403.14624)

## Origin and maintenance

**发起方**：Author affiliations in the paper: MMLab of The Chinese University of Hong Kong, Shanghai Artificial Intelligence Laboratory, and UCLA. [S9](https://arxiv.org/pdf/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**署名与合作**：The paper’s author affiliations are CUHK MMLab, Shanghai AI Laboratory, and UCLA; they are recorded as signed, and they are not expanded into other collaboration agreements. [S10](https://arxiv.org/pdf/2403.14624)

**作者**：Zhang, Renrui；Jiang, Dongzhi；Zhang, Yichi；Lin, Haokun；Guo, Ziyu；Qiu, Pengshuo；Zhou, Aojun；Lu, Pan；Chang, Kai-Wei；Gao, Peng；Li, Hongsheng [S2](https://arxiv.org/abs/2403.14624)

**维护入口**：The official public maintenance entry is ZrrSkywalker/MathVerse, and the LICENSE is signed Renrui Zhang; the division of responsibility is not inferred from the GitHub name. [S4](https://github.com/ZrrSkywalker/MathVerse) [S11](https://github.com/ZrrSkywalker/MathVerse/blob/main/LICENSE)

**资助**：待核实 [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

## Design goals

**衡量能力**：Tests whether the model truly reads mathematical diagrams, rather than relying on a restatement of the visual information in the stem. [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**设计动机**：Existing visual-mathematics questions often leak, in the text, information that is in the figure, so a model can answer correctly without looking at the figure. [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

## Construction

**题目/样本来源**：2,612 illustrated mathematics questions were collected, of which 1,236 come from public question banks and 1,376 from existing benchmarks; humans produced six versions that differ in how much information is in the figure and the text. [S9](https://arxiv.org/pdf/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**构建者背景**：Professional annotators review and classify questions in plane geometry, solid geometry, and functions. [S9](https://arxiv.org/pdf/2403.14624)

**审查流程**：Experts review each question and classify it into 12 fine-grained categories. Versions are built for Text Dominant, Text Lite, Text Only, Vision Intensive, Vision Dominant, and Vision Only. [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**质量控制**：Experts review each question and classify it into 12 fine-grained categories. Versions are built for Text Dominant, Text Lite, Text Only, Vision Intensive, Vision Dominant, and Vision Only. [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**去污染与防泄漏**：Collected from public sources of questions and from existing benchmarks, then rewritten by hand in its figure and text information; what the six versions control is the amount of information that is visible, not a test for contamination of the training set. The original paper does not give a verifiable guarantee that every frontier model is free of contamination. [S10](https://arxiv.org/pdf/2403.14624) [S4](https://github.com/ZrrSkywalker/MathVerse)

## Data format

**规模**：There are 2,612 original questions and 15,672 versioned samples. testmini has 788 original questions and 4,728 samples. The current HF multimodal configuration of 3,940 rows and the text-only configuration of 788 rows are kept separate. 3,940 cannot be treated as the original question count. [S9](https://arxiv.org/pdf/2403.14624) [S8](https://huggingface.co/datasets/AI4Math/MathVerse)

**任务形式**：Multiple-choice and open question answering on mathematical diagrams; six informational versions of the same question. [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**模态**：Image + text (some samples or versions are text only) [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

**语言**：English question text and prompts (the language field of the dataset card and the public examples); the original language of the site the questions came from is not automatically counted as the language of the dataset. [S5](https://huggingface.co/datasets/AI4Math/MathVerse)

**难度与覆盖**：3 broad categories, plane geometry, solid geometry, and functions, and 12 fine categories; this is not a distribution of difficulty levels. [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**公开与测试划分**：testmini makes 788 original questions public; five multimodal versions, 3,940 samples in all, are used to compute All, and another 788 Text Only samples are used for ablation and are not counted in the five-version All. [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

## Evaluation

**指标**：The official results currently take w/o CoT-E answer accuracy as primary; CoT-E separately uses GPT-4(V) to extract key steps and judge the reasoning step by step. [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**评分**：The official results currently take w/o CoT-E answer accuracy as primary; CoT-E separately uses GPT-4(V) to extract key steps and judge the reasoning step by step. [S9](https://arxiv.org/pdf/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**提示/训练/运行设置**：The official primary metric in the w/o setting uses a direct answer from query_wo. CoT-E uses query_cot. Priority goes to lmms-eval mathverse_testmini, and the subtasks and the prompts of one version are recorded. The two stages of scoring by the model itself are extraction of the answer and scoring of the answer. [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

**官方脚本**：https://github.com/ZrrSkywalker/MathVerse [S12](https://github.com/ZrrSkywalker/MathVerse)

**可比性警示**：All aggregates only the five multimodal versions; Text Only is a separate ablation. --quick_match string matching is faster, but the official note says it is not accurate enough; the CoT-E, w/o, and MMVistaReason CompassVerifier research settings cannot be ranked together directly. [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

## Current status

**核查日**：2026-11-08 [S13](https://mathverse-cuhk.github.io/)

**数据版本与持续使用**：Public evaluation still uses the two configs testmini and testmini_text_only; the paper’s total of 2,612 original questions and the versioned HF row counts of 3,940+788 have different denominators. [S4](https://github.com/ZrrSkywalker/MathVerse) [S5](https://huggingface.co/datasets/AI4Math/MathVerse)

**论文版本与证据历史**：v1 2024-03-22；v2 2024-08-18。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S6](https://arxiv.org/abs/2403.14624)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The highest value on the official testmini table for w/o CoT-E is 61.7%. A CoT-E score listed separately cannot be mixed into that judgment, and it cannot stand in for a conclusion about performance on the full set of 2,612 original questions. [S13](https://mathverse-cuhk.github.io/)

**已知问题与争议**：The six versions, CoT-E/w/o, and the definition of All must be held fixed; 3,940 multimodal samples and 788 original questions are not a conflict of question counts. [S2](https://arxiv.org/abs/2403.14624) [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md) [S14](https://arxiv.org/html/2610.01352v2)

**版本/衍生关系**：The six image-text versions are information ablations of the same original questions, not six independent benchmarks; mathverse_testmini in lmms-eval is an implementation entry point and does not expand the benchmark count. [S4](https://github.com/ZrrSkywalker/MathVerse)

## Leaderboard snapshot

**快照日**：2026-11-08 [S15](https://mathverse-cuhk.github.io/#leaderboard)

**官方榜入口**：https://mathverse-cuhk.github.io/#leaderboard [S1](https://mathverse-cuhk.github.io/)

**第三方入口**：待核实 [S16](https://artificialanalysis.ai/evaluations?skill=multimodal)

> The AA directory of evaluations was opened in this pass. A separate tracking page for this original benchmark was not confirmed. AA tracking MMMU-Pro is not the same as AA tracking the original MMMU. Preference Elo from LMArena, or a score on another benchmark, is not put in its place. Results from Epoch and from LMArena under the same definition remain Unverified, item by item.

### Historical research paper / original collection date retained

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | MMVistaReason-4B (MVR-4B) | 79.7 | Answer accuracy under the protocol of the paper (CompassVerifier) | [来源](https://arxiv.org/html/2610.01352v2)，2026-11-07 |
| 2 | MMVistaReason-9B (MVR-9B) | 82.4 | Answer accuracy under the protocol of the paper (CompassVerifier) | [来源](https://arxiv.org/html/2610.01352v2)，2026-11-07 |

### Official testmini / All CoT-E

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | GPT-4V | 54.4% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 2 | Qwen-VL-Max | 37.2% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 3 | Gemini-Pro | 35.3% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 4 | LLaVA-NeXT-34B | 34.6% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 5 | InternLM-XComposer2-VL-7B | 25.9% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 6 | SPHINX-MoE | 22.8% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 7 | Qwen-VL-Plus | 21.3% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 8 | ShareGPT4V-13B | 17.4% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 9 | LLaVA-NeXT-13B | 17.2% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 10 | G-LLaVA-13B | 16.4% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 11 | G-LLaVA-7B | 15.7% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 12 | SPHINX-Plus | 14.0% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 13 | LLaVA-1.5-13B | 12.7% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 14 | MiniGPT-v2-7B | 10.9% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 15 | mPLUG-Owl2-7B | 10.3% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 16 | ImageBind-LLM | 10.0% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 17 | LLaMA-Adapter V2 | 5.8% | Official All CoT-E | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |

### Official testmini / All w/o CoT-E

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Human Performance* | 64.9% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 2 | VL-Rethinker-72B | 61.7% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 3 | VL-Rethinker-7B | 54.2% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 4 | GPT-4V | 39.4% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 5 | Qwen-VL-Max | 25.3% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 6 | LLaVA-NeXT-34B | 23.8% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 7 | Gemini-Pro | 23.5% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 8 | G-LLaVA-13B | 16.9% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 9 | G-LLaVA-7B | 16.6% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 10 | InternLM-XComposer2-VL-7B | 16.5% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 11 | LLaVA-NeXT-13B | 15.6% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 12 | SPHINX-MoE | 15.0% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 13 | ShareGPT4V-13B | 13.1% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 14 | Random Chance | 12.4% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 15 | SPHINX-Plus | 12.2% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 16 | Qwen-VL-Plus | 11.8% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 17 | MiniGPT-v2-7B | 11.0% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 18 | ImageBind-LLM | 9.2% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 19 | LLaVA-1.5-13B | 7.6% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 20 | mPLUG-Owl2-7B | 5.9% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |
| 21 | LLaMA-Adapter V2 | 5.7% | Official All w/o | [来源](https://mathverse-cuhk.github.io/)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S13](https://mathverse-cuhk.github.io/) [S13](https://mathverse-cuhk.github.io/) [S17](https://arxiv.org/html/2610.01352v2)

**覆盖与时效**：The two tracks that can be read officially, All CoT-E and w/o, are transcribed in full, and the cells of the six versions are kept; Text Only is only an ablation and does not count as the five-version All. Existing records from the H2 paper and the old collection date are retained, and this is not treated as a retest on this occasion or as a global SOTA. [S13](https://mathverse-cuhk.github.io/)

## Contact

**公开研究邮箱**：jdzcarr7@gmail.com [S3](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)

> Officially published project email for contact, leaderboard submission, or copyright feedback; no email was sent.

**问题反馈**：https://github.com/ZrrSkywalker/MathVerse/issues [S12](https://github.com/ZrrSkywalker/MathVerse)

**官方发布渠道**：待核实 [S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/)

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

**隐私口径**：Only officially published project feedback channels are recorded; private contact details are neither collected nor inferred. [S18](urn:benchmark-atlas:constitution:v0.1)

## Original files

**源站PDF**：https://arxiv.org/pdf/2403.14624 [S2](https://arxiv.org/abs/2403.14624) [S9](https://arxiv.org/pdf/2403.14624)

**PDF SHA-256**：9eb1f3c95cb78e80ab280191a3c459599af725152121f1d987c5c6282c09b18b [S10](https://arxiv.org/pdf/2403.14624)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：5598195 [S10](https://arxiv.org/pdf/2403.14624)

**原有文件夹**：{"id": "1EgsP1-Zm7CkY5a_mLHgspdKsiyOsnFOi", "webViewLink": " [S19](

**其他材料**：[{"kind": "Chinese introduction", "id": "1Y-1EkoyNsWvUfR9pJbYn4DN1YqP3N_DRHMN9RZht_n4", "webViewLink": " [S20](

**原有 PDF**：{"id": "1XMpETqBdB0LhwZVfNfFhnyaVHnt_R5Yy", "webViewLink": " [S21](

## Changelog

- 2026-11-07，核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- 2026-11-07，深度优化续核：打开Official README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://arxiv.org/abs/2403.14624) [S1](https://mathverse-cuhk.github.io/) [S13](https://mathverse-cuhk.github.io/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://mathverse-cuhk.github.io/](https://mathverse-cuhk.github.io/)，访问 2026-11-07
- S2，[https://arxiv.org/abs/2403.14624](https://arxiv.org/abs/2403.14624)，访问 2026-11-07
- S3，[https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md](https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/main/README.md)，访问 2026-11-07
- S4，[https://github.com/ZrrSkywalker/MathVerse](https://github.com/ZrrSkywalker/MathVerse)，访问 2026-11-08
- S5，[https://huggingface.co/datasets/AI4Math/MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse)，访问 2026-11-08
- S6，[https://arxiv.org/abs/2403.14624](https://arxiv.org/abs/2403.14624)，访问 2026-11-08
- S7，[https://huggingface.co/datasets/AI4Math/MathVerse/blob/main/README.md](https://huggingface.co/datasets/AI4Math/MathVerse/blob/main/README.md)，访问 2026-11-07
- S8，[https://huggingface.co/datasets/AI4Math/MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse)，访问 2026-11-07
- S9，[https://arxiv.org/pdf/2403.14624](https://arxiv.org/pdf/2403.14624)，访问 2026-11-07
- S10，[https://arxiv.org/pdf/2403.14624](https://arxiv.org/pdf/2403.14624)，访问 2026-11-08
- S11，[https://github.com/ZrrSkywalker/MathVerse/blob/main/LICENSE](https://github.com/ZrrSkywalker/MathVerse/blob/main/LICENSE)，访问 2026-11-08
- S12，[https://github.com/ZrrSkywalker/MathVerse](https://github.com/ZrrSkywalker/MathVerse)，访问 2026-11-07
- S13，[https://mathverse-cuhk.github.io/](https://mathverse-cuhk.github.io/)，访问 2026-11-08
- S14，[https://arxiv.org/html/2610.01352v2](https://arxiv.org/html/2610.01352v2)，访问 2026-11-07
- S15，[https://mathverse-cuhk.github.io/#leaderboard](https://mathverse-cuhk.github.io/#leaderboard)，访问 2026-11-08
- S16，[https://artificialanalysis.ai/evaluations?skill=multimodal](https://artificialanalysis.ai/evaluations?skill=multimodal)，访问 2026-11-07
- S17，[https://arxiv.org/html/2610.01352v2](https://arxiv.org/html/2610.01352v2)，访问 2026-11-08
- S18，[urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1)，访问 2026-11-07
- S19，[，访问 2026-11-07
- S20，[，访问 2026-11-07
- S21，[，访问 2026-11-07
