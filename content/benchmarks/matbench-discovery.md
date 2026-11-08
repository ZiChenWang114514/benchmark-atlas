# Matbench Discovery
> 核验：2026-11-08。实证优化；已补官方事实与分任务快照，未核实项明确保留

Matbench Discovery关注机器学习是否能有效预筛假想晶体，减少昂贵DFT验证，而不只看能量回归误差。当前站点还评几何、声子、分子动力学和双原子势；CPS与发现F1分别排名，完整WBM与unique-prototype子集不能混用分母。

概述依据：[S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920) [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

## 基本信息

**简称**：Matbench Discovery [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**全称**：Matbench Discovery [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> 使用官方名称；未有已核实全称扩展时保留原名，不把论文标题误当基准全称。

**版本口径**：在线多任务评测框架；发现任务锁定WBM与MP v2022.10.28参考凸包，不能用软件包版本替代数据协议。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**论文修订**：arXiv v3 [S7](https://arxiv.org/abs/2308.14920)

**发布时间**：2023-08-29 07:29:57 （arXiv v1）；后发表于Nature Machine Intelligence 7, 836–847 (2025)。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**主板块**：材料 [S1](https://arxiv.org/abs/2308.14920)

> Benchmark Atlas 编辑归档；跨学科条目只在主板块计数，另用标签导航。

**领域**：材料 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**许可与权利边界**：MIT（GitHub 仓库 janosh/matbench-discovery 的 LICENSE 文件；仅覆盖仓库内容，第三方原始材料权利另行核查） [S8](https://github.com/janosh/matbench-discovery) [S9](https://api.github.com/repos/janosh/matbench-discovery)

**论文**：https://arxiv.org/abs/2308.14920 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**代码入口**：https://github.com/janosh/matbench-discovery [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

**数据入口**：https://matbench-discovery.materialsproject.org/ [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**官网**：https://matbench-discovery.materialsproject.org/ [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**论文标题**：Matbench Discovery -- A framework to evaluate machine learning crystal stability predictions [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

## 发起与维护

**发起方**：剑桥大学、劳伦斯伯克利国家实验室、BAM、加州大学伯克利分校作者团队 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> 主要依据论文作者单位/官方团队介绍；不据此推断法律所有权或唯一发起方。文本已明确标注未核实的正式发起关系。

**署名与合作**：论文作者单位：Cambridge物理系、LBNL、德国BAM、UC Berkeley；WBM数据由Hai-Chen Wang、Silvana Botti、Miguel A. L. Marques贡献。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**作者**：Riebesell, Janosh；Goodall, Rhys E. A.；Benner, Philipp；Chiang, Yuan；Deng, Bowen；Ceder, Gerbrand；Asta, Mark；Lee, Alpha A.；Jain, Anubhav；Persson, Kristin A. [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**维护入口**：公开站点与仓库署名Janosh Riebesell；问题反馈走官方GitHub Issues/Discussions，不据署名推定机构服务承诺。 [S10](https://github.com/janosh/matbench-discovery) [S11](https://matbench-discovery.materialsproject.org/models)

**资助**：JR获德国Studienstiftung，AAL获Royal Society，AJ与KAP获美国DOE Office of Science/BES Materials Sciences and Engineering支持；使用NERSC DE-AC02-05CH11231资源。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## 设计目标

**衡量能力**：比较晶体稳定性发现、结构优化、声子/热导率、分子动力学和双原子势能曲线；揭示精度、稳健性与计算成本权衡。 [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

**设计动机**：评估模型作为稳定无机晶体高通量发现预筛器的实际价值，而非只比较能量回归误差。 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

## 构建方式

**题目/样本来源**：围绕晶体热力学稳定性设计发现任务；用 DFT 参考能量构建评价凸包。 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**构建者背景**：物理、材料科学与材料机器学习跨机构团队；评价假想晶体DFT稳定性与学习势，不是专家手写自然语言试题。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**审查流程**：围绕晶体热力学稳定性设计发现任务；用 DFT 参考能量构建评价凸包。 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**质量控制**：发现集用WBM DFT弛豫及公开初始/最终结构；采用固定DFT参考凸包，unique-prototype设置剔除MP重合与WBM内部重复原型，以避免只记已知结构。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**去污染与防泄漏**：论文默认训练MP v2022.10.28，测试WBM；unique-prototype子集去除与MP重复及WBM内部原型重合。现在模型训练材料不同，必须保留训练数据列，不能一概称无泄漏。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## 数据形式

**规模**：官方发现页确认完整WBM 256,963晶体、85元素；论文独特原型表为215,488材料（其中32,942稳定），全量表含42,825稳定材料。两个分母不能混用。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**任务形式**：从未弛豫晶体预测相对DFT参考凸包的稳定性；另有几何优化、声子/热导、分子动力学和双原子势能曲线任务。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**模态**：周期晶体结构、原子/元素、能量/力/应力及声子等数值物理数据；不是文本多选或图像问答。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**语言**：自然语言语种不适用：主要对象是结构和数值物理标签，网页说明语言不是评测题目语言。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**难度与覆盖**：从已知MP材料训练到WBM假想晶体外分布泛化；分类困难集中在参考凸包附近，不能由回归MAE直接推出发现能力。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**公开与测试划分**：论文MP训练/WBM测试，不是随机五折；WBM初始/弛豫结构、能量和对称性参考公开。默认unique-prototype发现子集与完整WBM分别评测。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## 评测方法

**指标**：CPS综合发现F1（50%）、几何RMSD（10%）和声子κ SRME（40%）；分子动力学与双原子任务不计入CPS。发现使用Unique Prototypes子集。 [S12](https://matbench-discovery.materialsproject.org/)

**评分**：发现F1为precision/recall调和均值，DAF是precision除以测试集中稳定材料比例。稳定标签相对固定DFT-MP凸包；CPS另按发现F1 50%、几何RMSD 10%、声子κ SRME 40%聚合。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**提示/训练/运行设置**：非语言提示评测；预测未弛豫结构的弛豫能或用学习势弛豫后估能，须固定训练数据、结构优化器和测试子集；当前CPS还要求其他子任务覆盖。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**官方脚本**：https://github.com/janosh/matbench-discovery [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**可比性警示**：稳定性凸包由 DFT 参考能量构造，不由模型预测构造；不同训练数据、测试覆盖及子任务不可混比。高排名不代表 Materials Project 背书。 [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

## 最新情况

**核查日**：2026-11-08 [S6](https://matbench-discovery.materialsproject.org/)

**数据版本与持续使用**：发现任务WBM/MP参考凸包；在线框架已扩展多任务，当前默认unique-prototype设置。模型新增日期不是数据版本号。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**论文版本与证据历史**：v1 2023-08-29；v2 2024-02-05；v3 2024-12-11。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S7](https://arxiv.org/abs/2308.14920)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为。

**饱和度边界**：当前CPS最高0.913、发现F1最高0.935；仍需结合RMSD、κ SRME及MD/双原子稳健性，不能把综合高分当所有模拟情境已饱和。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**已知问题与争议**：当前默认require forces筛选为49/58合格模型；models目录的CPS名次显示48个具备CPS排名模型。筛选分母不同，不能当抓取错误。参考凸包严格来自DFT，不由预测模型重建。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

**版本/衍生关系**：原始论文以晶体稳定性为中心；现站扩展几何、声子、MD与双原子任务，CPS是另一个综合排行。Matbench v0.1性质预测独立保留。 [S4](https://arxiv.org/pdf/2308.14920) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery) [S6](https://matbench-discovery.materialsproject.org/)

## 榜单快照

**快照日**：2026-11-08 [S11](https://matbench-discovery.materialsproject.org/models)

**官方榜入口**：https://matbench-discovery.materialsproject.org/models [S13](https://matbench-discovery.materialsproject.org/models)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> 该字段尚未完成精确核验，不表示官方未公开。

### 官方models / CPS

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | DPA-4.1-Max-OAM-PFT | 0.913 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 2 | Prophet-OAME-MBD | 0.912 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 3 | DPA-4.1-Max-OAM | 0.910 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 4 | TECE-OAM-RRA-1.0 | 0.908 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |
| 5 | EquFlashV2 | 0.907 | CPS ↑ | [来源](https://matbench-discovery.materialsproject.org/models)，2026-11-08 |

### 官方发现 / Unique Prototypes / require forces

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | DPA-4.1-Max-OAM-PFT | 0.935 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 2 | DPA-4.1-Max-OAM | 0.933 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 3 | EquiformerV3+DeNS-OAM | 0.931 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 4 | TECE-OAM-RRA-1.0 | 0.929 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |
| 5 | EquFlashV2 | 0.929 | F1 ↑ | [来源](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S11](https://matbench-discovery.materialsproject.org/models) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery)

**覆盖与时效**：本次成功读取公开HTTP页面；CPS与发现F1各前五分赛道。RMSD按models目录精度转录，未将首页三位小数当精确到四位。Added是入榜日期，不是运行日；当前索引更新时间不明。 [S11](https://matbench-discovery.materialsproject.org/models) [S5](https://matbench-discovery.materialsproject.org/benchmarks/discovery)

## 联系方式

**公开研究邮箱**：janosh.riebesell@gmail.com；kristinpersson@berkeley.edu [S4](https://arxiv.org/pdf/2308.14920)

> 论文首页明确列出的公开通讯邮箱。

**问题反馈**：https://github.com/janosh/matbench-discovery/issues [S3](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)

> 官方README建议支持问题使用 https://github.com/janosh/matbench-discovery/discussions。

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

> 该字段尚未完成精确核验，不表示官方未公开。

**隐私口径**：只使用论文、官方站点或仓库公开联系方式；不收集私人渠道。 [S14](urn:benchmark-atlas:constitution:v0.1)

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2308.14920 [S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920)

**PDF SHA-256**：6a37da286baaea80b902d6011fcd6e08a090dbec604b3988884baf57b3aed612 [S4](https://arxiv.org/pdf/2308.14920)

> 本次下载的源站PDF字节校验；不声称重传或替换既有副本。

**PDF字节数**：4570226 [S4](https://arxiv.org/pdf/2308.14920)

**原有文件夹**：{"id": "1wBpI0F2UIXMsYTY0Fal14yFkONcE5FwM", "webViewLink": " [S15](

**其他材料**：[{"kind": "中文介绍", "id": "1ja6AV0EvEUik-shnO57oNO_n5urry23n_VpJS0sV_Ns", "webViewLink": " [S16](

**原有 PDF**：{"id": "1Zp7e0SyLqACycWpXq8DbQsiczNMjJCfO", "webViewLink": " [S17](

## 变更记录

- 2026-11-07，首批官方材料核验、中文改写、；未核实字段显式标记。
- 2026-11-07，：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S1](https://arxiv.org/abs/2308.14920) [S2](https://arxiv.org/pdf/2308.14920) [S6](https://matbench-discovery.materialsproject.org/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2308.14920](https://arxiv.org/abs/2308.14920)，访问 2026-11-07
- S2，[https://arxiv.org/pdf/2308.14920](https://arxiv.org/pdf/2308.14920)，访问 2026-11-07
- S3，[https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md](https://raw.githubusercontent.com/janosh/matbench-discovery/main/readme.md)，访问 2026-11-07
- S4，[https://arxiv.org/pdf/2308.14920](https://arxiv.org/pdf/2308.14920)，访问 2026-11-08
- S5，[https://matbench-discovery.materialsproject.org/benchmarks/discovery](https://matbench-discovery.materialsproject.org/benchmarks/discovery)，访问 2026-11-08
- S6，[https://matbench-discovery.materialsproject.org/](https://matbench-discovery.materialsproject.org/)，访问 2026-11-08
- S7，[https://arxiv.org/abs/2308.14920](https://arxiv.org/abs/2308.14920)，访问 2026-11-08
- S8，[https://github.com/janosh/matbench-discovery](https://github.com/janosh/matbench-discovery)，访问 2026-11-07
- S9，[https://api.github.com/repos/janosh/matbench-discovery](https://api.github.com/repos/janosh/matbench-discovery)，访问 2026-11-07
- S10，[https://github.com/janosh/matbench-discovery](https://github.com/janosh/matbench-discovery)，访问 2026-11-08
- S11，[https://matbench-discovery.materialsproject.org/models](https://matbench-discovery.materialsproject.org/models)，访问 2026-11-08
- S12，[https://matbench-discovery.materialsproject.org/](https://matbench-discovery.materialsproject.org/)，访问 2026-11-07
- S13，[https://matbench-discovery.materialsproject.org/models](https://matbench-discovery.materialsproject.org/models)，访问 2026-11-07
- S14，[urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1)，访问 2026-11-07
- S15，[，访问 2026-11-07
- S16，[，访问 2026-11-07
- S17，[，访问 2026-11-07
