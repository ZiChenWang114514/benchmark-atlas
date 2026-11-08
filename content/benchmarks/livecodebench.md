# LiveCodeBench
> 核验：2026-11-08。已核验存在；研究快照，未核实字段保留标记

LiveCodeBench通过滚动收集竞赛新题来降低静态题库污染风险，并把生成、自修复、执行与测试输出预测分开评估。滚动并不自动等于无污染：必须同时固定题目日期窗、模型训练截止信息、release、测试集lite设置及采样预算。

概述依据：[S1](https://arxiv.org/abs/2403.07974) [S2](https://livecodebench.github.io/) [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

## 基本信息

**简称**：LiveCodeBench [S2](https://livecodebench.github.io/)

**全称**：LiveCodeBench [S2](https://livecodebench.github.io/)

> 保留官方名称，不把论文标题自动扩写为全称。

**版本口径**：README列举到release_v6；默认release_latest是可变别名，复现须锁定release_version和题目日期窗。 [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**论文修订**：arXiv v2 [S7](https://arxiv.org/abs/2403.07974)

**发布时间**：2024-03-13 02:58:04 [S1](https://arxiv.org/abs/2403.07974)

> 首次 arXiv 论文提交时间，已转；不自动视为数据集首发时间。

**主板块**：代码 [S1](https://arxiv.org/abs/2403.07974)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

**领域**：滚动编程竞赛评测 [S1](https://arxiv.org/abs/2403.07974)

**许可与权利边界**：仓库代码MIT；官方HF code_generation_lite卡license字段仅写cc，未指定Creative Commons具体版本/条款。不得把MIT或一个模糊cc标签直接扩展为全部竞赛原题的使用许可。 [S8](https://github.com/LiveCodeBench/LiveCodeBench/blob/main/LICENSE) [S9](https://huggingface.co/datasets/livecodebench/code_generation_lite)

**论文**：https://arxiv.org/abs/2403.07974 [S1](https://arxiv.org/abs/2403.07974)

**代码入口**：https://github.com/LiveCodeBench/LiveCodeBench [S2](https://livecodebench.github.io/)

**数据入口**：https://huggingface.co/datasets/livecodebench/code_generation_lite [S10](https://github.com/LiveCodeBench/LiveCodeBench)

**官网**：https://livecodebench.github.io/ [S2](https://livecodebench.github.io/)

**论文标题**：LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code [S1](https://arxiv.org/abs/2403.07974)

## 发起与维护

**发起方**：UC Berkeley、MIT、Cornell University 作者团队（单位口径） [S1](https://arxiv.org/abs/2403.07974)

**署名与合作**：作者单位含UC Berkeley、MIT与Cornell；记录学术署名单位，不将SKY Lab资助企业自动视作出题合作机构。 [S11](https://arxiv.org/pdf/2403.07974)

**作者**：Jain, Naman；Han, King；Gu, Alex；Li, Wen-Ding；Yan, Fanjia；Zhang, Tianjun；Wang, Sida；Solar-Lezama, Armando；Sen, Koushik；Stoica, Ion [S1](https://arxiv.org/abs/2403.07974)

**维护入口**：LiveCodeBench 项目团队 [S1](https://arxiv.org/abs/2403.07974)

**资助**：NSF CCF:1900968、CCF:1908870及SKY Lab企业赞助/关联方；Alex Gu获NSF Graduate Research Fellowship 2141064，Armando Solar-Lezama获NSF与Intel CCF:2217064支持。详见论文致谢。 [S11](https://arxiv.org/pdf/2403.07974)

## 设计目标

**衡量能力**：代码生成、自修复、代码执行和测试输出预测的综合能力。 [S1](https://arxiv.org/abs/2403.07974)

**设计动机**：静态题库可能被训练反复接触；仅生成任务无法完整评估代码理解与修复。 [S1](https://arxiv.org/abs/2403.07974)

## 构建方式

**题目/样本来源**：持续收集 LeetCode、AtCoder、Codeforces 定期竞赛的新题，记录发布时间。 [S2](https://livecodebench.github.io/)

**构建者背景**：三校程序合成、软件与机器学习研究团队；原题来自竞赛平台。 [S2](https://livecodebench.github.io/)

**审查流程**：整理问题、测试与场景，官方接受附生成记录的 GitHub PR 并审核后入榜。 [S2](https://livecodebench.github.io/)

**质量控制**：ERRATA追踪错误测试及不适合自动评分的问题；code_generation_lite删减测试以加速，原始集需--not_fast。官方提示超时可造成小于0.5点分数变化。 [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**去污染与防泄漏**：可选在模型训练截止日期之后发布的题，以降低污染；截止日期不透明、题库公开后再训练仍会影响有效性。 [S2](https://livecodebench.github.io/)

## 数据形式

**规模**：README明确列出 release_v1 400、v2 511、v3 612、v4 713、v5 880、v6 1,055题；v6覆盖2023-05至2025-04。主页300+与论文500+属历史窗口，不能当作当前总量。 [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**任务形式**：算法程序生成、基于反馈的修复、程序执行、测试输出预测。 [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**模态**：文本；代码 [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**语言**：英语竞赛描述；生成代码支持范围依场景/脚本。 [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**难度与覆盖**：保留竞赛题难度差异，按 easy / medium / hard 分析；不能仅据旧 easy 子集判断整体饱和。 [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

**公开与测试划分**：题目与评测工具逐批公开；去污染依时间窗，不等同永久私有题库。 [S2](https://livecodebench.github.io/) [S1](https://arxiv.org/abs/2403.07974)

## 评测方法

**指标**：各场景执行正确率 / pass@k；生成、修复和输出预测分开。 [S1](https://arxiv.org/abs/2403.07974)

**评分**：根据竞赛测试或已知输入输出检查生成结果。 [S1](https://arxiv.org/abs/2403.07974)

**提示/训练/运行设置**：官方代码生成示例n=10、temperature=0.2；按模型设置提示；生成计算pass@1/pass@5。必须固定release_version、start_date/end_date、lite或原始测试。 [S6](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)

**官方脚本**：https://github.com/LiveCodeBench/LiveCodeBench [S2](https://livecodebench.github.io/)

**可比性警示**：官方默认网页窗口为2024-08-01至2025-05-01（题目日期）；按公开JSON及页面算法复算，与AA摘要未知窗口分赛道。release_latest是可变别名，lite/原始测试、采样参数及窗口都必须锁定。 [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

## 最新情况

**核查日**：2026-11-08 [S12](https://livecodebench.github.io/)

**数据版本与持续使用**：持续滚动采题；必须按评测时间窗固定快照；历史持续使用证据：2026-09-23 Hunyuan-A13B §4.1/§4.2及表2–4实际报告 LiveCodeBench；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。 https://arxiv.org/html/2609.27284v1 [S13](https://arxiv.org/html/2609.27284v1) [S2](https://livecodebench.github.io/)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

**论文版本与证据历史**：v1 2024-03-13；v2 2024-06-07。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S7](https://arxiv.org/abs/2403.07974)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为。

**饱和度边界**：动态窗口改变题目分母；当前AA摘要最高91.7%，官方默认窗口另行计算。没有一个可跨时窗引用的全套饱和结论。 [S3](https://livecodebench.github.io/leaderboard.html) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

**已知问题与争议**：“Contamination Free”是设计目标/标题；成立范围取决于模型截止日、题目发布时间和后续训练，不能绝对保证。 [S2](https://livecodebench.github.io/) [S14](https://artificialanalysis.ai/evaluations/livecodebench)

**版本/衍生关系**：代码生成、self-repair、execution、test-output prediction 为同套件场景，不拆为四条。 [S2](https://livecodebench.github.io/) [S14](https://artificialanalysis.ai/evaluations/livecodebench)

## 榜单快照

**快照日**：2026-11-08 [S3](https://livecodebench.github.io/leaderboard.html)

**官方榜入口**：https://livecodebench.github.io/leaderboard.html [S10](https://github.com/LiveCodeBench/LiveCodeBench)

**第三方入口**：https://artificialanalysis.ai/evaluations/livecodebench [S14](https://artificialanalysis.ai/evaluations/livecodebench)

### 官方网页默认窗口：2024-08-01–2025-05-01

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | O4-Mini (High) | 80.2 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 2 | O3 (High) | 75.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 3 | O4-Mini (Medium) | 74.2 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 4 | Gemini-2.5-Pro-06-05 | 73.6 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 5 | DeepSeek-R1-0528 | 73.1 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 6 | Gemini-2.5-Pro-05-06 | 71.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 7 | EXAONE-4.0-32B | 70.0 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 8 | OpenReasoning-Nemotron-32B | 69.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 9 | O3-Mini-2025-01-31 (High) | 67.4 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |
| 10 | OpenCodeReasoning-Nemotron-1.1-32B | 66.8 | Pass@1 (%) | [来源](https://livecodebench.github.io/performances_generation.json)，2026-11-08 |

### AA当前摘要；评测窗待核实

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Gemini 3 Pro Preview (High) | 91.7 | AA LiveCodeBench score (%) | [来源](https://artificialanalysis.ai/evaluations/livecodebench)，2026-11-08 |
| 2 | Gemini 3 Flash Preview (Reasoning) | 90.8 | AA LiveCodeBench score (%) | [来源](https://artificialanalysis.ai/evaluations/livecodebench)，2026-11-08 |
| 3 | DeepSeek V3.2 Speciale | 89.6 | AA LiveCodeBench score (%) | [来源](https://artificialanalysis.ai/evaluations/livecodebench)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

**覆盖与时效**：官方网页静态表只是Loading占位；本次读取其明确引用的performances_generation.json，并严格依网页筛窗/均值/一位小数显示规则重建前十有排名条目。日期标记止于2025-05-01，不伪装2026新题。每模型覆盖题数单列；AA成绩窗口不明，绝不混排。 [S3](https://livecodebench.github.io/leaderboard.html) [S4](https://livecodebench.github.io/performances_generation.json) [S5](https://artificialanalysis.ai/evaluations/livecodebench)

## 联系方式

**公开研究邮箱**：naman_jain@berkeley.edu [S2](https://livecodebench.github.io/)

**问题反馈**：https://github.com/LiveCodeBench/LiveCodeBench/issues [S2](https://livecodebench.github.io/)

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**隐私口径**：待核实 [S1](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2403.07974 [S15](https://arxiv.org/pdf/2403.07974)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

**PDF SHA-256**：a9bd3f7b96ac846ac53506e7b58197d9213919f18f402a27910dcf9fc948b427 [S11](https://arxiv.org/pdf/2403.07974)

> 本次下载的源站PDF字节校验；不声称重传或替换既有副本。

**PDF字节数**：4960954 [S11](https://arxiv.org/pdf/2403.07974)

**原有文件夹**：{"id": "1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV", "webViewLink": " [S16](

**其他材料**：[{"type": "中文介绍Google Doc", "id": "1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s", "webViewLink": " [S2](https://livecodebench.github.io/) [S17](

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

**原有 PDF**：{"id": "1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ", "webViewLink": " [S18](

## 变更记录

- 2026-11-07，首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- 2026-11-07，深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://livecodebench.github.io/) [S12](https://livecodebench.github.io/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)，访问 2026-11-07
- S2，[https://livecodebench.github.io/](https://livecodebench.github.io/)，访问 2026-11-07
- S3，[https://livecodebench.github.io/leaderboard.html](https://livecodebench.github.io/leaderboard.html)，访问 2026-11-08
- S4，[https://livecodebench.github.io/performances_generation.json](https://livecodebench.github.io/performances_generation.json)，访问 2026-11-08
- S5，[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)，访问 2026-11-08
- S6，[https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)，访问 2026-11-07
- S7，[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)，访问 2026-11-08
- S8，[https://github.com/LiveCodeBench/LiveCodeBench/blob/main/LICENSE](https://github.com/LiveCodeBench/LiveCodeBench/blob/main/LICENSE)，访问 2026-11-08
- S9，[https://huggingface.co/datasets/livecodebench/code_generation_lite](https://huggingface.co/datasets/livecodebench/code_generation_lite)，访问 2026-11-08
- S10，[https://github.com/LiveCodeBench/LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench)，访问 2026-11-08
- S11，[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)，访问 2026-11-08
- S12，[https://livecodebench.github.io/](https://livecodebench.github.io/)，访问 2026-11-08
- S13，[https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)，访问 2026-11-07
- S14，[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)，访问 2026-11-07
- S15，[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)，访问 2026-11-07
- S16，[，访问 2026-11-07
- S17，[，访问 2026-11-07
- S18，[，访问 2026-11-07
