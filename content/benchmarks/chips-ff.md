# CHIPS-FF

> 第1轮实证核查 · 2026-11-07（KST）。正文与权威 JSON 同步；访问时间不是来源发表时间。未知保留，不以旧论文结果冒充最新总榜。

## 1. 基本信息

- **名称**：CHIPS-FF （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **全称**：Computational High-Performance Infrastructure for Predictive Simulation-based Force Fields （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **版本**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **论文版本**：v4；最近论文日期 2025-03-19 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **发布日期**：2024-12-13（首个arXiv版本日期；非推定数据上线日） （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **板块**：材料 编辑分类沿用入选清单；不代表该基准只测本板块。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **子领域**：力场与材料物性 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **许可**：NIST Terms of Use：美国政府雇员作品在美国不受版权保护；境外按声明授予非独占免费使用/修改/分发许可，须保留通知及免责声明。 （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/LICENSE.rst)；访问：2026-11-07）

- **论文**：https://arxiv.org/abs/2412.10516 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **代码**：https://github.com/usnistgov/chipsff （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)；访问：2026-11-07）

- **数据**：https://github.com/usnistgov/chipsff （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **官方主页**：https://pages.nist.gov/jarvis_leaderboard/Special/CHIPS_FF/ （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **论文标题**：CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

## 2. 发起与维护

- **发起机构**：NIST Material Measurement Laboratory。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **合作机构**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **作者**：Wines, Daniel；Choudhary, Kamal （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **维护方**：usnistgov/chipsff，Daniel Wines、Kamal Choudhary。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **资助方**：CHIPS Metrology Program（CHIPS for America），美国商务部国家标准与技术研究院 NIST。 （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)；访问：2026-11-07）

## 3. 设计目标

- **能力目标**：通用ML力场的结构弛豫、弹性、声子、缺陷、表面、界面与非晶物性及计算开销。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **设计动机**：仅看能量/力测试误差不足以说明真实半导体材料的下游物性可靠性。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

## 4. 构建方式

- **数据来源**：JARVIS-DFT参考与半导体部件相关材料，ASE+JARVIS-Tools自动化仿真。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **评审背景**：NIST材料计算与机器学习研究者。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **审核流程**：固定参考DFT属性与自动收敛/弛豫工作流比较；独立人工逐结构审核规模待核实。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **质量控制**：比较模型收敛、DFT偏差与成本，多种物性独立评分。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **去污染**：uMLFF可能在重叠材料上训练；需要模型训练集与测试结构重叠审计，不能默认OOD。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

## 5. 数据形式

- **规模**：原论文104材料、16个MLFF，另近200万结构力预测评测。H2工作流104晶格/弹性、49vacancy、82surface、15界面对；官网vacancy榜为48，协议不同。 （[来源1](https://arxiv.org/abs/2412.10516) [来源2](https://arxiv.org/html/2609.19487v1) [来源3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)；访问：2026-11-07）

- **任务形式**：从原子结构与 JSON 配置驱动弛豫、弹性常数、缺陷/表面/界面、声子、热性质与分子动力学；不是文本问答。 （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)；访问：2026-11-07）

- **模态**：原子结构、能量/力、弹性张量、声子与缺陷/表面数值。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **语言**：数值与Python/ASE；无自然语言考试语言。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **难度**：不同属性及材料族有独立难度；无统一总分。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **公开与隐藏划分**：公开JARVIS参考与提交预测；每个物性榜的分母可不同，非统一train/test问答集。 （[来源1](https://arxiv.org/abs/2412.10516) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

## 6. 评测方法

- **指标**：属性级MAE及相关指标，收敛率/时间；官网总页称PCC，但vacancy子页实际定义MAE。 （[来源1](https://arxiv.org/abs/2412.10516) [来源2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)；访问：2026-11-07）

- **评分方式**：自动将 MLFF 模拟结果与 JARVIS-DFT 比较；具体指标需绑定性质任务页，不能只写一个全平台指标。 （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md) [来源2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)；访问：2026-11-07）

- **提示设置**：非提示评测；须固定MLFF checkpoint、ASE弛豫器、阈值、参考晶胞与失败处理。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **评测脚本**：https://github.com/usnistgov/chipsff （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **可比性提示**：官网vacancy48点与H2的49点不同；H2界面参考晶胞不匹配改用split-slab protocol；不同参考流程不可直接比SOTA。 （[来源1](https://arxiv.org/abs/2412.10516) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

## 7. 最新情况

- **核查日期**：2026-11-07 Asia/Seoul （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **最新版本**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **修订与2026H2证据**：2026H2 使用证据：ALIGNN 2.0（2026-09-16）表5使用 CHIPS-FF 性质套件；采用自洽元素参照和统一弛豫协议，不应与不同协议的旧榜直接合并。 （[来源1](https://arxiv.org/abs/2609.19487)；访问：2026-11-07）

- **饱和度**：各物性收敛/缺陷误差差异大，无统一饱和结论。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **已知问题**：参考结构、界面基线和失败处理影响误差；总页PCC与子页MAE命名冲突，以具体子页及物性定义为准。 （[来源1](https://arxiv.org/abs/2412.10516) [来源2](https://arxiv.org/html/2609.19487v1) [来源3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)；访问：2026-11-07）

- **后继资源**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

## 8. 榜单快照

- **采集日期**：2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期） （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **官方榜单**：https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a （[来源1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)；访问：2026-11-07）

- **第三方榜单**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **结果**：晶格常数 a（104材料）子任务：alignn_ff 0.0111；orb-v2 与 eqV2_31M_omat 均0.0154；eqV2_31M_omat_mp_salex 0.0161。官方表头标 ACC，描述却明确 MAE（Å），保留此冲突，暂按描述解释为越小越好。 （[来源1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a)；访问：2026-11-07）

- **口径说明**：2026-11-07 读取；每行提交日期原样为3-11-2025，日期格式未核实，不能当整体更新日。专题页称 Pearson，但该a子任务描述用MAE、表头ACC；三种标签冲突须官方澄清。 （[来源1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_a) [来源2](https://pages.nist.gov/jarvis_leaderboard/Special/CHIPS_FF/)；访问：2026-11-07）

## 9. 联系方式

- **公开邮箱**：daniel.wines@nist.gov；kamal.choudhary@nist.gov （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)；访问：2026-11-07）

- **问题反馈**：https://github.com/usnistgov/chipsff/issues 官方公开仓库的问题反馈入口；未发送消息。 （[来源1](https://raw.githubusercontent.com/usnistgov/chipsff/main/README.md)；访问：2026-11-07）

- **官方社交**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **隐私原则**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

## 10. 原始文件

- **PDF来源**：https://arxiv.org/pdf/2412.10516 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **SHA256**：f92bd2357b20db020e1cb92584f8b8882427ee86133019d91b75ac14c4844102 （[来源1](https://arxiv.org/pdf/2412.10516)；访问：2026-11-07）

- **PDF字节**：4721218 （[来源1](https://arxiv.org/pdf/2412.10516)；访问：2026-11-07）

- **Drive文件夹**：id：1VwsQVL22mQmsezJ5BqVl6vjHB-pYsNFl；webViewLink：https://drive.google.com/drive/folders/1VwsQVL22mQmsezJ5BqVl6vjHB-pYsNFl （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

- **其他文档**：type：中文介绍 Google Doc；id：19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo；webViewLink：https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit （[来源1](https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit)；访问：2026-11-07）

- **Drive PDF**：id：1R6k7Ykwhzm_clyHspieXbcEpedlyMJPL；webViewLink：https://drive.google.com/file/d/1R6k7Ykwhzm_clyHspieXbcEpedlyMJPL/view （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）

## 11. 变更记录

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。 （[来源1](https://arxiv.org/abs/2412.10516)；访问：2026-11-07）
