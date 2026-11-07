# MATH
> 核验：2026-11-08（KST / Asia/Seoul）。已核实存在；深度条目；显式待核实项保留

MATH提供有完整解答的竞赛数学题，完整测试集是5,000题；常见MATH-500只是其中一个子集。现代模型的推理预算、代码工具、投票及答案归一化会显著改变协议，不能把一个子集的接近满分扩展成所有竞赛数学能力已饱和。

概述依据：[S1](https://arxiv.org/abs/2103.03874) [S2](https://github.com/hendrycks/math) [S3](https://arxiv.org/html/2609.27284v1)

## 基本信息

**简称**：MATH [S1](https://arxiv.org/abs/2103.03874)

**全称**：Mathematics Aptitude Test of Heuristics [S1](https://arxiv.org/abs/2103.03874)

**版本口径**：完整MATH 12500题；MATH-500单列衍生口径 [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**论文修订**：arXiv v2 [S4](https://arxiv.org/abs/2103.03874)

**发布时间**：2021-03-06（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明） [S1](https://arxiv.org/abs/2103.03874)

**主板块**：数学 [S2](https://github.com/hendrycks/math)

**领域**：竞赛数学问题求解 [S1](https://arxiv.org/abs/2103.03874)

**许可与权利边界**：官方仓库LICENSE为MIT（2021 Dan Hendrycks），论文亦声明数据及代码MIT；HF qwedsacf镜像标MIT。原始竞赛题权利仍不可由仓库许可自动保证。 [S5](https://github.com/hendrycks/math/blob/main/LICENSE) [S6](https://arxiv.org/pdf/2103.03874) [S7](https://huggingface.co/datasets/qwedsacf/competition_math)

**论文**：https://arxiv.org/abs/2103.03874 [S1](https://arxiv.org/abs/2103.03874)

**代码入口**：https://github.com/hendrycks/math [S2](https://github.com/hendrycks/math)

**数据入口**：https://huggingface.co/datasets/qwedsacf/competition_math [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**官网**：https://github.com/hendrycks/math [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**论文标题**：Measuring Mathematical Problem Solving With the MATH Dataset [S1](https://arxiv.org/abs/2103.03874)

## 发起与维护

**发起方**：University of California Berkeley、University of Chicago（论文署名） [S1](https://arxiv.org/abs/2103.03874)

**署名与合作**：论文署名单位UC Berkeley与University of Chicago；不据此增列其他未证实合作关系。 [S6](https://arxiv.org/pdf/2103.03874)

**作者**：Hendrycks, Dan；Burns, Collin；Kadavath, Saurav；Arora, Akul；Basart, Steven；Tang, Eric；Song, Dawn；Steinhardt, Jacob [S1](https://arxiv.org/abs/2103.03874)

**维护入口**：官方公开入口为hendrycks/math及Dan Hendrycks；这是维护/反馈入口，不构成现行主动维护保证。 [S8](https://github.com/hendrycks/math)

**资助**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> 未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

## 设计目标

**衡量能力**：评估竞赛数学多步求解、符号操作及最终答案正确性。 [S1](https://arxiv.org/abs/2103.03874)

**设计动机**：简单算术或短步骤集合不足以反映代数、几何和数论等更广的数学能力。 [S1](https://arxiv.org/abs/2103.03874)

## 构建方式

**题目/样本来源**：来自AMC、AIME等竞赛及AoPS整理的数学题，保留完整解答与最终答案。 [S1](https://arxiv.org/abs/2103.03874)

**构建者背景**：研究者整理已有人类数学竞赛题及解答；并非12500题全由作者原创。 [S1](https://arxiv.org/abs/2103.03874)

**审查流程**：整理题目、解答、难度和学科信息，统一为可处理的文本格式。 [S1](https://arxiv.org/abs/2103.03874)

**质量控制**：用LaTeX表示数学式，最终答案以boxed标注；几何题部分通过Asymptote代码提供图形信息。 [S1](https://arxiv.org/abs/2103.03874)

**去污染与防泄漏**：题源长期公开；原论文讨论预训练与能力差距，但不能保证后续模型无题目记忆。 [S1](https://arxiv.org/abs/2103.03874)

## 数据形式

**规模**：共12500道竞赛数学题：训练7500、测试5000；MATH-500不可当成完整测试集。 [S1](https://arxiv.org/abs/2103.03874)

**任务形式**：数学开放式求解，评分重点为可规范化的最终答案而非逐步证明。 [S1](https://arxiv.org/abs/2103.03874)

**模态**：自然语言与LaTeX；几何图形由Asymptote代码表示，不是原生栅格图像评测。 [S1](https://arxiv.org/abs/2103.03874)

**语言**：英语题面；形式化/数学符号另见模态与仓库格式 [S1](https://arxiv.org/abs/2103.03874)

**难度与覆盖**：5级难度，7学科；不同级别和科目准确率应分别考察。 [S1](https://arxiv.org/abs/2103.03874)

**公开与测试划分**：完整训练7500与测试5000均公开；MATH-500仅选取测试中的500题，不能用其分数代表完整集。 [S1](https://arxiv.org/abs/2103.03874)

## 评测方法

**指标**：最终答案准确率（规范化精确匹配/等价判定）。 [S1](https://arxiv.org/abs/2103.03874)

**评分**：抽取boxed答案并处理数学字符串的规范化；格式归一化细节会改变得分。 [S1](https://arxiv.org/abs/2103.03874)

**提示/训练/运行设置**：原论文包含微调实验；现代CoT、计算器、代码、投票与单次生成必须另记。 [S1](https://arxiv.org/abs/2103.03874)

**官方脚本**：官方hendrycks/math仓库提供dataset loaders与evaluation code；复现须固定代码版本。 [S9](https://raw.githubusercontent.com/hendrycks/math/main/README.md)

**可比性警示**：MATH全量5000测试题与MATH-500是不同分母；Hunyuan报告写MATH但引用Lightman，子集口径尚不能确认。 [S1](https://arxiv.org/abs/2103.03874) [S3](https://arxiv.org/html/2609.27284v1)

## 最新情况

**核查日**：2026-11-08 KST / Asia/Seoul [S8](https://github.com/hendrycks/math)

**数据版本与持续使用**：完整MATH 12500题；MATH-500单列衍生口径 [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**论文版本与证据历史**：v1 2021-03-06T03:59:39+09:00（KST）；v2 2021-11-09T06:30:18+09:00（KST）。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S4](https://arxiv.org/abs/2103.03874)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为KST。

**饱和度边界**：AA MATH-500当前最高99.4%，只支持这个500题子集在该协议下接近满分；不能据此断定完整5,000测试题及每难度层都饱和。 [S10](https://artificialanalysis.ai/evaluations/math-500)

**已知问题与争议**：官方论文称数据/代码以MIT发布，但原竞赛内容的权利不能据此无条件外推；本轮未法律审查。 [S1](https://arxiv.org/abs/2103.03874) [S2](https://github.com/hendrycks/math)

**版本/衍生关系**：MATH-500/PRM800K围绕过程监督发展；AA只给MATH-500榜，不能冒充完整MATH榜。 [S1](https://arxiv.org/abs/2103.03874) [S2](https://github.com/hendrycks/math)

## 榜单快照

**快照日**：2026-11-08 KST / Asia/Seoul [S8](https://github.com/hendrycks/math)

**官方榜入口**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> 本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

**第三方入口**：https://artificialanalysis.ai/evaluations/math-500 [S11](https://artificialanalysis.ai/evaluations/math-500)

### AA 500题子集；非完整MATH

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | GPT-5 (High) | 99.4% | AA MATH-500 accuracy | [来源](https://artificialanalysis.ai/evaluations/math-500) · 2026-11-08 |
| 2 | o3 | 99.2% | AA MATH-500 accuracy | [来源](https://artificialanalysis.ai/evaluations/math-500) · 2026-11-08 |
| 3 | Grok 3 mini Reasoning (High) | 99.2% | AA MATH-500 accuracy | [来源](https://artificialanalysis.ai/evaluations/math-500) · 2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S10](https://artificialanalysis.ai/evaluations/math-500)

**覆盖与时效**：只记录当前打开AA摘要的MATH-500前三；并列分数保留来源叙述顺序，不推定统计显著差异。完整MATH官方实时总榜未核实。 [S10](https://artificialanalysis.ai/evaluations/math-500)

## 联系方式

**公开研究邮箱**：hendrycks@berkeley.edu [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**问题反馈**：https://github.com/hendrycks/math/issues [S2](https://github.com/hendrycks/math)

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> 未核实专门官方社交账号，不收录同名个人账户

**隐私口径**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> 未核实benchmark专门隐私条款；许可证不能代替隐私政策

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2103.03874 [S1](https://arxiv.org/abs/2103.03874)

**PDF SHA-256**：a6f448173e57d808a38679dd817bcc2e01324176cbf491d08c43cc0e7ca30bfe [S6](https://arxiv.org/pdf/2103.03874)

> 本次下载的源站PDF字节校验；不声称重传或替换既有Drive副本。

**PDF字节数**：2030715 [S6](https://arxiv.org/pdf/2103.03874)

**原有Drive文件夹**：{"id": "1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL", "webViewLink": "https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL"} [S12](https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL)

**其他材料**：{"chinese_intro_doc": {"id": "1s8SrmzMxF5AnMs2uZOKwSfgRQ18Qwu6IH1jsKu7qZ9o", "webViewLink": "https://docs.google.com/document/d/1s8SrmzMxF5AnMs2uZOKwSfgRQ18Qwu6IH1jsKu7qZ9o/edit?usp=drivesdk", "mimeType": "application/vnd.google-apps.document"}, "local_markdown": "content/benchmarks/math.md"} [S12](https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL)

**原有Drive PDF**：{"id": "1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu", "webViewLink": "https://drive.google.com/file/d/1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu/view?usp=drivesdk"} [S13](https://drive.google.com/file/d/1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu/view?usp=drivesdk)

## 变更记录

- 2026-11-07 · 核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07 · 第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
- 2026-11-08 · 第二轮逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://github.com/hendrycks/math) [S8](https://github.com/hendrycks/math)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1 · [https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874) · 访问 2026-11-07
- S2 · [https://github.com/hendrycks/math](https://github.com/hendrycks/math) · 访问 2026-11-07
- S3 · [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1) · 访问 2026-11-07
- S4 · [https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874) · 访问 2026-11-08
- S5 · [https://github.com/hendrycks/math/blob/main/LICENSE](https://github.com/hendrycks/math/blob/main/LICENSE) · 访问 2026-11-08
- S6 · [https://arxiv.org/pdf/2103.03874](https://arxiv.org/pdf/2103.03874) · 访问 2026-11-08
- S7 · [https://huggingface.co/datasets/qwedsacf/competition_math](https://huggingface.co/datasets/qwedsacf/competition_math) · 访问 2026-11-08
- S8 · [https://github.com/hendrycks/math](https://github.com/hendrycks/math) · 访问 2026-11-08
- S9 · [https://raw.githubusercontent.com/hendrycks/math/main/README.md](https://raw.githubusercontent.com/hendrycks/math/main/README.md) · 访问 2026-11-07
- S10 · [https://artificialanalysis.ai/evaluations/math-500](https://artificialanalysis.ai/evaluations/math-500) · 访问 2026-11-08
- S11 · [https://artificialanalysis.ai/evaluations/math-500](https://artificialanalysis.ai/evaluations/math-500) · 访问 2026-11-07
- S12 · [https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL](https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL) · 访问 2026-11-07
- S13 · [https://drive.google.com/file/d/1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu/view?usp=drivesdk](https://drive.google.com/file/d/1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu/view?usp=drivesdk) · 访问 2026-11-07
