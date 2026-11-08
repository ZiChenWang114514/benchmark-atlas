# CHIPS-FF

> Benchmark Constitution，深度核验快照 2026-11-07。待核实不等于未公开；采集日期不等于榜单更新时间。

CHIPS-FF是材料仿真工作流与性质分榜，不是问答题库，也没有可信的统一总准确率。它用JARVIS-DFT参照检验通用机器学习力场的结构、弹性、缺陷、表面、声子及计算成本；需要把参考数据、优化器、失败处理和每个性质的分母一起锁定。

导读依据：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）；[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

## 基本信息

**简称**：CHIPS-FF

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**全称**：Computational High-Performance Infrastructure for Predictive Simulation-based Force Fields

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**基准版本**：论文v4对应104材料性质套件；持续演进的软件工作流，不能将论文v4当数据语义版本。

来源：[1](https://arxiv.org/pdf/2412.10516)（访问2026-11-07）；[2](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

**论文版本**：v4；最近论文日期 2025-03-19

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**发布日期**：2024-12-13（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**主板块**：材料

来源：[1](https://arxiv.org/html/2609.19487v1)（访问2026-11-07）

核验说明：编辑分类沿用入选清单；不代表该基准只测本板块。

**领域**：力场与材料物性

来源：[1](https://arxiv.org/html/2609.19487v1)（访问2026-11-07）

**许可与范围**：NIST LICENSE.rst：美国联邦政府员工职务作品在美国不受版权保护；境外授予免费、非独占使用/修改/分发许可，保留通知与免责声明。第三方模型和数据各按其授权。

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/LICENSE.rst)（访问2026-11-07）

**论文/技术报告**：https://arxiv.org/abs/2412.10516

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**代码**：https://github.com/usnistgov/chipsff

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

**数据**：https://github.com/usnistgov/chipsff

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**主页**：https://pages.nist.gov/jarvis_leaderboard/Special/CHIPS_FF/

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**论文标题**：CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

## 发起与维护

**发起/作者单位**：NIST Material Measurement Laboratory。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**合作关系**：待核实

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

核验说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

**作者**：Wines, Daniel；Choudhary, Kamal

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**维护方**：usnistgov/chipsff，Daniel Wines、Kamal Choudhary。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**资助**：CHIPS Metrology Program（CHIPS for America），美国商务部国家标准与技术研究院 NIST。

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

## 设计目标

**测量能力**：通用ML力场的结构弛豫、弹性、声子、缺陷、表面、界面与非晶物性及计算开销。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**针对的不足**：仅看能量/力测试误差不足以说明真实半导体材料的下游物性可靠性。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

## 构建方式

**材料来源**：JARVIS-DFT参考与半导体部件相关材料，ASE+JARVIS-Tools自动化仿真。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**出题背景**：NIST材料计算与机器学习研究者。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**审核**：以JARVIS-DFT参考属性和公开计算流程核对模型收敛、误差与耗时；论文同时比较FrechetCellFilter和ExpCellFilter，优化器改变结果。

来源：[1](https://arxiv.org/pdf/2412.10516)（访问2026-11-07）

**质控**：比较模型收敛、DFT偏差与成本，多种物性独立评分。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**去污染边界**：uMLFF可能在重叠材料上训练；需要模型训练集与测试结构重叠审计，不能默认OOD。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

## 数据形式

**规模与统计口径**：原论文104材料、16个MLFF，另近200万结构力预测评测。H2工作流104晶格/弹性、49vacancy、82surface、15界面对；官网vacancy榜为48，协议不同。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问2026-11-07）；[3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（访问2026-11-07）

**任务形式**：从原子结构与 JSON 配置驱动弛豫、弹性常数、缺陷/表面/界面、声子、热性质与分子动力学；不是文本问答。

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

**模态**：原子结构、能量/力、弹性张量、声子与缺陷/表面数值。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**语言**：数值与Python/ASE；无自然语言考试语言。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**难度**：不同属性及材料族有独立难度；无统一总分。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**公开/保留划分**：公开JARVIS参考与提交预测；每个物性榜的分母可不同，非统一train/test问答集。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问2026-11-07）

## 评测方法

**指标**：属性级MAE及相关指标，收敛率/时间；官网总页称PCC，但vacancy子页实际定义MAE。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）；[2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（访问2026-11-07）

**评分**：自动将 MLFF 模拟结果与 JARVIS-DFT 比较；具体指标需绑定性质任务页，不能只写一个全平台指标。

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）；[2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)（访问2026-11-07）

**提示与运行设定**：非提示评测；须固定MLFF checkpoint、ASE弛豫器、阈值、参考晶胞与失败处理。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**脚本/运行入口**：https://github.com/usnistgov/chipsff

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**可比性**：官网vacancy48点与H2的49点不同；H2界面参考晶胞不匹配改用split-slab protocol；不同参考流程不可直接比SOTA。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**当前版本证据**：当前官网晶格a任务使用104材料；各性质子集分母独立，软件更新不等于统一题集版本。

来源：[1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)（访问2026-11-07）

**修订历史**：arXiv：v1 2024-12-14 04:22:31；v2 2024-12-21 11:49:32；v3 2025-01-15 13:10:22；v4 2025-03-19 12:10:46。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**饱和**：各物性收敛/缺陷误差差异大，无统一饱和结论。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**争议与局限**：参考结构、界面基线和失败处理影响误差；总页PCC与子页MAE命名冲突，以具体子页及物性定义为准。

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问2026-11-07）；[3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（访问2026-11-07）

**派生/去重**：待核实

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

核验说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 榜单快照

**快照日**：2026-11-07 （网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**官方榜**：https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a

来源：[1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)（访问2026-11-07）

**独立评测**：待核实

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

核验说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 分轨结果（不合并来源/题集/协议）

**JARVIS / dft_3d_chipsff_a**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | alignn_ff | 0.0111 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 2 | orb-v2 | 0.0154 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 2 | eqV2_31M_omat | 0.0154 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 4 | eqV2_31M_omat_mp_salex | 0.0161 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 5 | eqV2_86M_omat_mp_salex | 0.0164 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 6 | eqV2_153M_omat | 0.0217 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 7 | eqV2_86M_omat | 0.022 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 8 | orb-d3-v2 | 0.025 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 9 | mace | 0.0265 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 9 | mattersim | 0.0265 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 11 | sevennet | 0.0281 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 12 | chgnet | 0.0361 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 13 | mace-mpa | 0.0401 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 14 | matgl-direct | 0.0427 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 15 | matgl | 0.0429 | 晶格a MAE (Å)，页面表头ACC有冲突 |
| 16 | mace-alexandria | 0.068 | 晶格a MAE (Å)，页面表头ACC有冲突 |

direction：lower_is_better

来源：[https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：完整录入晶格a子榜16配置并按描述中的MAE升序；orb-v2与eqV2_31M_omat并列第2。原表ACC、专题总页PCC与任务MAE标签冲突保留；3-11-2025提交日格式未获澄清，不推断月份或整体更新时间。

来源：[1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)（访问2026-11-07）

## 联系方式

**公开研究邮箱**：daniel.wines@nist.gov；kamal.choudhary@nist.gov

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

**Issues**：https://github.com/usnistgov/chipsff/issues

来源：[1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)（访问2026-11-07）

核验说明：官方公开仓库的问题反馈入口；未发送消息。

**公开社区**：待核实

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

核验说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

**隐私原则**：待核实

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

核验说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 原始文件

**PDF**：https://arxiv.org/pdf/2412.10516

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**原件SHA-256**：f92bd2357b20db020e1cb92584f8b8882427ee86133019d91b75ac14c4844102

来源：[1](https://arxiv.org/pdf/2412.10516)（访问2026-11-07）

**PDF字节数**：4721218

来源：[1](https://arxiv.org/pdf/2412.10516)（访问2026-11-07）

**目录**：id：1VwsQVL22mQmsezJ5BqVl6vjHB-pYsNFl；webViewLink：

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

**其他文档**：type：中文介绍；id：19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo；webViewLink：https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit

来源：[1](https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit)（访问2026-11-07）

** PDF**：id：1R6k7Ykwhzm_clyHspieXbcEpedlyMJPL；webViewLink：

来源：[1](https://arxiv.org/abs/2412.10516)（访问2026-11-07）

## 变更记录

- date：2026-11-07；timezone：；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- date：2026-11-07；timezone：；change：：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。
- date：2026-11-07；timezone：；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
