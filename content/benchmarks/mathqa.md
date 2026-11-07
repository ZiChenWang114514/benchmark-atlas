# MathQA
> 核验：2026-11-08（KST / Asia/Seoul）。第1轮官方证据复核；授权与版本冲突显式保留；未核实项不补造

MathQA将AQuA题目转成可执行运算程序，既测最终答案，也为分析步骤提供形式监督。它不是MATH竞赛集，也不等于原AQuA全部题目。本轮修正dev/test比例顺序，并查明网站模板MIT与HF数据卡Apache-2.0的许可范围差别。

概述依据：[S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319) [S1](https://arxiv.org/abs/1905.13319) [S3](https://arxiv.org/html/2610.11978v1)

## 基本信息

**简称**：MathQA [S1](https://arxiv.org/abs/1905.13319)

**全称**：MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms [S1](https://arxiv.org/abs/1905.13319)

**版本口径**：2019 Operation-Based Formalisms数据；未固定本轮数据commit [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319)

**论文修订**：arXiv v1 [S4](https://arxiv.org/abs/1905.13319)

**发布时间**：2019-05-31（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明） [S1](https://arxiv.org/abs/1905.13319)

**主板块**：数学 [S2](https://math-qa.github.io/math-QA/)

**领域**：多步数学应用题 [S1](https://arxiv.org/abs/1905.13319)

**许可与权利边界**：AllenAI HF数据卡明确声明Apache-2.0；GitHub根LICENSE为MIT但署名2013–2019 Blackrock Digital LLC（网页模板），不能把它当整个MathQA数据集的无条件MIT授权。保留来源差异，使用数据优先核对数据卡与原始题权利。 [S5](https://huggingface.co/datasets/allenai/math_qa) [S6](https://github.com/math-qa/math-QA/blob/master/LICENSE)

**论文**：https://arxiv.org/abs/1905.13319 [S1](https://arxiv.org/abs/1905.13319)

**代码入口**：https://github.com/math-qa/math-QA [S2](https://math-qa.github.io/math-QA/)

**数据入口**：https://math-qa.github.io/math-QA/data/MathQA.zip [S2](https://math-qa.github.io/math-QA/) [S7](https://math-qa.github.io/math-QA/data/MathQA.zip)

**官网**：https://math-qa.github.io/math-QA/ [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319)

**论文标题**：MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms [S1](https://arxiv.org/abs/1905.13319)

## 发起与维护

**发起方**：University of Washington、Allen Institute for AI [S1](https://arxiv.org/abs/1905.13319)

**署名与合作**：论文首页机构为University of Washington及Allen Institute for AI；Figure Eight是众包平台，不额外视为作者机构。 [S8](https://arxiv.org/pdf/1905.13319)

**作者**：Aida Amini；Saadia Gabriel；Shanchuan Lin；Rik Koncel-Kedziorski；Yejin Choi；Hannaneh Hajishirzi [S8](https://arxiv.org/pdf/1905.13319) [S5](https://huggingface.co/datasets/allenai/math_qa)

> 按PDF与NAACL引用记录Shanchuan Lin；arXiv元数据及项目BibTeX的Peter Lin不同，保留原来源差异。

**维护入口**：MathQA 作者项目主页（Aida Amini 等）；主页列公开联系单位为 University of Washington，不据此断言现行服务承诺。 [S2](https://math-qa.github.io/math-QA/)

**资助**：ONR N00014-18-1-2826、NSF IIS 1616112、Allen Distinguished Investigator Award及Google、Allen Institute for AI、Amazon、Bloomberg捐助；论文致谢。 [S8](https://arxiv.org/pdf/1905.13319)

## 设计目标

**衡量能力**：从文字应用题生成可执行的运算程序，检验最终答案与可解释计算步骤。 [S1](https://arxiv.org/abs/1905.13319)

**设计动机**：仅看自然语言rationale可能掩盖逻辑错误，需要机器可执行、步骤明确的形式语言。 [S1](https://arxiv.org/abs/1905.13319)

## 构建方式

**题目/样本来源**：在AQuA-RAT上重新标注和修正部分题目，以58种运算和6个领域构造形式程序。 [S1](https://arxiv.org/abs/1905.13319)

**构建者背景**：Figure Eight众包标注者，作者设计运算接口、质量题与专家抽查。 [S1](https://arxiv.org/abs/1905.13319)

**审查流程**：程序最终值接近正确答案才可提交，之后验证程序与题目/解释是否逻辑一致，至少2/3验证者认可。 [S1](https://arxiv.org/abs/1905.13319)

**质量控制**：验证通过率94.64%；500题专家样本92%正确（论文口径）；数值碰巧正确仍可能逻辑不对。 [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/)

**去污染与防泄漏**：论文诊断AQuA近重复及rationale不匹配；标注扩展用Levenshtein距离阈值4词进行相似题迁移。随机划分不是模板级隔离，不能据此证明无跨划分相似性或后续LLM污染。 [S8](https://arxiv.org/pdf/1905.13319)

## 数据形式

**规模**：官方 MathQA.zip 实读：train 29,837、dev 4,475、test 2,985（主划分共37,297）；另有 challenge_test 604，不自动计作互斥新题。 [S7](https://math-qa.github.io/math-QA/data/MathQA.zip)

**任务形式**：5选1应用题，同时提供运算程序、rationale、领域标签。 [S1](https://arxiv.org/abs/1905.13319)

**模态**：文本（数学符号按文本表达）；并非原始图像视频识别任务 [S1](https://arxiv.org/abs/1905.13319)

**语言**：英语题面；形式化/数学符号另见模态与仓库格式 [S1](https://arxiv.org/abs/1905.13319)

**难度与覆盖**：一般应用数学/考试题，涵盖6类领域；不是MATH竞赛集的别名。 [S1](https://arxiv.org/abs/1905.13319)

**公开与测试划分**：原论文§6.1写80/12/8%顺序为training/dev/test（此前条目错写training/test/dev）。实际公开包train=29,837、dev=4,475、test=2,985，与HF一致；challenge_test=604单独保留。 [S8](https://arxiv.org/pdf/1905.13319) [S9](https://math-qa.github.io/math-QA/data/MathQA.zip) [S5](https://huggingface.co/datasets/allenai/math_qa)

## 评测方法

**指标**：答案准确率，程序可执行性和步骤合理性可作补充指标。 [S1](https://arxiv.org/abs/1905.13319)

**评分**：执行生成程序得到数值并映射选项；只检查最终数值不足以证明每一步推理正确。 [S1](https://arxiv.org/abs/1905.13319)

**提示/训练/运行设置**：原论文用双向RNN/LSTM序列到程序、OpenNMT，编码/解码各2层、hidden size=100、Adam lr=0.001；MathQA beam=100，AQuA beam=200。研究LLM结果须另记提示协议。 [S8](https://arxiv.org/pdf/1905.13319)

**官方脚本**：https://github.com/math-qa/math-QA [S10](https://github.com/math-qa/math-QA) [S1](https://arxiv.org/abs/1905.13319)

**可比性警示**：MathQA程序监督、AQuA原rationale和MATH竞赛集不是同一基准；不可只因题源重叠就合并得分。 [S1](https://arxiv.org/abs/1905.13319) [S3](https://arxiv.org/html/2610.11978v1)

## 最新情况

**核查日**：2026-11-08 KST / Asia/Seoul [S11](https://math-qa.github.io/math-QA/)

**数据版本与持续使用**：2019 Operation-Based Formalisms数据；未固定本轮数据commit [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319)

**论文版本与证据历史**：v1 2019-05-31T06:28:12+09:00（KST）。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S4](https://arxiv.org/abs/1905.13319)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为KST。

**饱和度边界**：待核实 [S1](https://arxiv.org/abs/1905.13319) [S3](https://arxiv.org/html/2610.11978v1)

> 是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

**已知问题与争议**：作者官网明确承认原rationale可能嘈杂/不完整/错误；官网与arXiv元数据作者名Peter Lin、PDF Shanchuan Lin有差异，保持来源原样。 [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/)

**版本/衍生关系**：AQuA-RAT的操作程序重标注子集；不应混为原AQuA全部约10万题。 [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/)

## 榜单快照

**快照日**：2026-11-08 KST / Asia/Seoul [S12](https://math-qa.github.io/math-QA/html/)

**官方榜入口**：https://math-qa.github.io/math-QA/html/ [S13](https://math-qa.github.io/math-QA/html/)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/1905.13319)

> 未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

### 历史研究论文 / 保留原采集日期

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Qwen3.8 Max | 94.4 | % | [来源](https://arxiv.org/html/2610.11978v1) · 2026-11-07 |
| 2 | Qwen3.8 Flash | 93.3 | % | [来源](https://arxiv.org/html/2610.11978v1) · 2026-11-07 |
| 3 | Gemini 3.8 Flash | 92.7 | % | [来源](https://arxiv.org/html/2610.11978v1) · 2026-11-07 |
| 1 | Seq2Prog+Cat | 37.4% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |
| 1 | Seq2Prog+Cat | 40.2% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |
| 1 | Seq2Prog+Cat | 37.8% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |
| 1 | Seq2Prog+Cat | 36.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |
| 1 | Seq2Prog+Cat | 38.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |
| 1 | Seq2Prog+Cat | 35.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |
| 1 | Seq2Prog+Cat | 33.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / MathQA Challenge

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 37.4% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / Geometry

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 40.2% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / Physics

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 37.8% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / General

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 36.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / Gain

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 38.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / Probability

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 35.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

### 官方静态 / Other

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 33.3% | 官网历史榜得分 | [来源](https://math-qa.github.io/math-QA/html/) · 2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S12](https://math-qa.github.io/math-QA/html/) [S12](https://math-qa.github.io/math-QA/html/) [S14](https://arxiv.org/html/2610.11978v1)

**覆盖与时效**：保留既有研究论文成绩及原采集日；新增本次重开官网七个历史赛道。MathQA Challenge 37.4与各领域分数不能混成全行业总榜；官网未标统一结果更新时间。 [S12](https://math-qa.github.io/math-QA/html/)

## 联系方式

**公开研究邮箱**：amini91@cs.washington.edu [S2](https://math-qa.github.io/math-QA/)

**问题反馈**：https://github.com/math-qa/math-QA/issues [S10](https://github.com/math-qa/math-QA)

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/1905.13319)

> 未核实专门官方社交账号，不收录同名个人账户

**隐私口径**：待核实 [S1](https://arxiv.org/abs/1905.13319)

> 未核实benchmark专门隐私条款；许可证不能代替隐私政策

## 原始文件

**源站PDF**：https://arxiv.org/pdf/1905.13319 [S1](https://arxiv.org/abs/1905.13319)

**PDF SHA-256**：220cd30ed121d4472bace7ce7a1a80c28cd4ed65669d248d5773ed3b866fdaf2 [S8](https://arxiv.org/pdf/1905.13319)

> 本次下载的源站PDF字节校验；不声称重传或替换既有Drive副本。

**PDF字节数**：850027 [S8](https://arxiv.org/pdf/1905.13319)

**原有Drive文件夹**：{"id": "1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-", "webViewLink": "https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-"} [S15](https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-)

**其他材料**：{"chinese_intro_doc": {"id": "1YKyOOE-Xx6_XxZAJbkBTqSlXhvtnUM4QRxJCRThRgBs", "webViewLink": "https://docs.google.com/document/d/1YKyOOE-Xx6_XxZAJbkBTqSlXhvtnUM4QRxJCRThRgBs/edit?usp=drivesdk", "mimeType": "application/vnd.google-apps.document"}, "local_markdown": "content/benchmarks/mathqa.md"} [S15](https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-)

**原有Drive PDF**：{"id": "1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE", "webViewLink": "https://drive.google.com/file/d/1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE/view?usp=drivesdk"} [S16](https://drive.google.com/file/d/1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE/view?usp=drivesdk)

## 变更记录

- 2026-11-07 · 核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07 · 深度优化第1轮：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- 2026-11-08 · 第二轮逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
- 2026-11-08 · 第二轮逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://math-qa.github.io/math-QA/) [S11](https://math-qa.github.io/math-QA/) [S11](https://math-qa.github.io/math-QA/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1 · [https://arxiv.org/abs/1905.13319](https://arxiv.org/abs/1905.13319) · 访问 2026-11-07
- S2 · [https://math-qa.github.io/math-QA/](https://math-qa.github.io/math-QA/) · 访问 2026-11-07
- S3 · [https://arxiv.org/html/2610.11978v1](https://arxiv.org/html/2610.11978v1) · 访问 2026-11-07
- S4 · [https://arxiv.org/abs/1905.13319](https://arxiv.org/abs/1905.13319) · 访问 2026-11-08
- S5 · [https://huggingface.co/datasets/allenai/math_qa](https://huggingface.co/datasets/allenai/math_qa) · 访问 2026-11-08
- S6 · [https://github.com/math-qa/math-QA/blob/master/LICENSE](https://github.com/math-qa/math-QA/blob/master/LICENSE) · 访问 2026-11-08
- S7 · [https://math-qa.github.io/math-QA/data/MathQA.zip](https://math-qa.github.io/math-QA/data/MathQA.zip) · 访问 2026-11-07
- S8 · [https://arxiv.org/pdf/1905.13319](https://arxiv.org/pdf/1905.13319) · 访问 2026-11-08
- S9 · [https://math-qa.github.io/math-QA/data/MathQA.zip](https://math-qa.github.io/math-QA/data/MathQA.zip) · 访问 2026-11-08
- S10 · [https://github.com/math-qa/math-QA](https://github.com/math-qa/math-QA) · 访问 2026-11-07
- S11 · [https://math-qa.github.io/math-QA/](https://math-qa.github.io/math-QA/) · 访问 2026-11-08
- S12 · [https://math-qa.github.io/math-QA/html/](https://math-qa.github.io/math-QA/html/) · 访问 2026-11-08
- S13 · [https://math-qa.github.io/math-QA/html/](https://math-qa.github.io/math-QA/html/) · 访问 2026-11-07
- S14 · [https://arxiv.org/html/2610.11978v1](https://arxiv.org/html/2610.11978v1) · 访问 2026-11-08
- S15 · [https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-](https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-) · 访问 2026-11-07
- S16 · [https://drive.google.com/file/d/1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE/view?usp=drivesdk](https://drive.google.com/file/d/1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE/view?usp=drivesdk) · 访问 2026-11-07
