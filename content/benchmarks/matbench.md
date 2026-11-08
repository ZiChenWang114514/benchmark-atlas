# Matbench
> 核验：2026-11-08。实证优化；已补官方事实与分任务快照，未核实项明确保留

Matbench v0.1是13项材料性质监督学习任务，不是语言模型问答集。可比性的核心是相同输入类型、物理单位和固定外层五折，而不是某个统一百分制。尤其要避免把官网旧分类“ROC-AUC”错误标签当成真正概率排序AUC。

概述依据：[S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/) [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

## 基本信息

**简称**：Matbench [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**全称**：Matbench [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> 使用官方名称；未有已核实全称扩展时保留原名，不把论文标题误当基准全称。

**版本口径**：matbench_v0.1 [S3](https://matbench.materialsproject.org/)

**论文修订**：arXiv v2 [S5](https://arxiv.org/abs/2005.00707)

**发布时间**：2020/05/02 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**主板块**：材料 [S1](https://arxiv.org/abs/2005.00707)

> Benchmark Atlas 编辑归档；跨学科条目只在主板块计数，另用标签导航。

**领域**：材料 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**许可与权利边界**：软件：MIT（Copyright 2021 Hacking Materials Research Group）；各子数据来源许可分别核对。 [S6](https://raw.githubusercontent.com/materialsproject/matbench/main/LICENSE)

**论文**：https://arxiv.org/abs/2005.00707 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**代码入口**：https://github.com/materialsproject/matbench [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

**数据入口**：https://matbench.materialsproject.org/ [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**官网**：https://matbench.materialsproject.org/ [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**论文标题**：Benchmarking Materials Property Prediction Methods: The Matbench Test Set and Automatminer Reference Algorithm [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

## 发起与维护

**发起方**：劳伦斯伯克利国家实验室、加州大学伯克利分校作者团队 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> 主要依据论文作者单位/官方团队介绍；不据此推断法律所有权或唯一发起方。文本已明确标注未核实的正式发起关系。

**署名与合作**：论文作者来自Lawrence Berkeley National Laboratory与UC Berkeley；Materials Project提供数据托管与项目基础设施。 [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

**作者**：Dunn, Alexander；Wang, Qi；Ganose, Alex；Dopp, Daniel；Jain, Anubhav [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**维护入口**：Materials Project；网站页脚注明由 HackingMaterials Group 的 Alex Dunn 维护。 [S3](https://matbench.materialsproject.org/)

**资助**：美国能源部Office of Basic Energy Sciences Early Career Research Program资助；LBNL与Lawrencium/NERSC算力支持涉及DE-AC02-05CH11231（论文致谢）。 [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

## 设计目标

**衡量能力**：为无机固体材料属性预测提供标准监督学习任务和可重复比较。 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**设计动机**：为无机固体材料属性预测提供标准监督学习任务和可重复比较。 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

## 构建方式

**题目/样本来源**：整理来自密度泛函计算和实验来源的预清洗数据，输入为组成和/或晶体结构。 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**构建者背景**：材料信息学研究团队；AD、QW、AJ构思，AD/QW/DD/AJ设计测试套件，AD/QW/AG实现Automatminer（论文Author Contributions）。 [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

**审查流程**：整理来自密度泛函计算和实验来源的预清洗数据，输入为组成和/或晶体结构。 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**质量控制**：按任务过滤非物理模量、折射率<1、明显异常形成能等；实验组成去冲突/近似重复；特征拟合、超参数与模型选择只在每折训练数据内部进行。 [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

**去污染与防泄漏**：用外层固定五折且仅在训练部分做内部模型选择，防测试泄漏；随机/分层CV并不是按化学体系外推或后续LLM训练污染排查。 [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

## 数据形式

**规模**：13项监督学习任务；样本数从 steels 的312到 mp_e_form 的132,752，各任务独立，不求和去重为单一题量。 [S3](https://matbench.materialsproject.org/)

**任务形式**：材料结构或化学组成作为输入，预测电子、热力学、力学、热学等性质；包括回归和分类。 [S3](https://matbench.materialsproject.org/)

**模态**：化学组成字符串或pymatgen.Structure晶体结构；输出连续性质值或布尔分类标签，不是视觉语言问答。 [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**语言**：非自然语言题集：输入是化学组成/晶体结构与数值标签；自然语言语言分布不适用。 [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**难度与覆盖**：13项任务跨实验/DFT、组成/结构与不同规模；难度按任务与样本量分析，无统一题目等级。 [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**公开与测试划分**：固定五折外层CV，每折80%训练+验证、20%测试；回归KFold、分类StratifiedKFold，seed=18012019；数据公开但评分时测试标签不得用于调参。 [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

## 评测方法

**指标**：回归 MAE 等、分类指标按任务报告；官网已警告历史 ROC-AUC 实际等于 balanced accuracy。 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**评分**：回归 MAE 等、分类指标按任务报告；官网已警告历史 ROC-AUC 实际等于 balanced accuracy。 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**提示/训练/运行设置**：非提示式LLM评测。须固定每任务五折及超参数搜索范围；原论文Automatminer Express内部优化预算24小时，其他算法各自记录训练设置。 [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**官方脚本**：matbench.bench.MatbenchBenchmark：task.get_train_and_val_data、task.get_test_data(include_target=False)、task.record及mb.to_file；官方使用页给完整逐任务逐折流程。 [S7](https://arxiv.org/pdf/2005.00707) [S9](https://matbench.materialsproject.org/How%20To%20Use/2run/)

**可比性警示**：官方重大勘误：v0.1 分类榜标作 ROC-AUC 的旧分数来自0.5阈值化预测，实际等于 balanced accuracy；旧榜尚未重算。不得解释为真正 ROC-AUC。 [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

## 最新情况

**核查日**：2026-11-08 [S8](https://matbench.materialsproject.org/)

**数据版本与持续使用**：v0.1 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**论文版本与证据历史**：v1 2020-05-02；v2 2020-05-08。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S5](https://arxiv.org/abs/2005.00707)

> 保留此前H2使用证据；只将本次打开arXiv的精确修订时间更新为。

**饱和度边界**：任务指标是带单位MAE或分类性能，不能以一个统一百分数判饱和；本次官方10回归任务最优MAE均非零，未证明已达实验/DFT噪声下限。 [S8](https://matbench.materialsproject.org/)

**已知问题与争议**：分类旧分数语义错误，见官方 issues #137、#181；未来评分已修复，但现有榜单没有重算。 [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

**版本/衍生关系**：官方首页将DFT材料发现任务指向Matbench Discovery；二者任务目标和划分不同，不把发现榜CPS混作Matbench v0.1性质预测分数。 [S7](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

## 榜单快照

**快照日**：2026-11-08 [S8](https://matbench.materialsproject.org/)

**官方榜入口**：https://matbench.materialsproject.org/ [S3](https://matbench.materialsproject.org/)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> 该字段尚未完成精确核验，不表示官方未公开。

### matbench_v0.1 / matbench_steels

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 87.7627 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_jdft2d

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 33.1918 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_phonons

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | MegNet (kgcnn v2.1.0) | 28.7606 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_expt_gap

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 0.3327 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_dielectric

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | MODNet (v0.1.12) | 0.2711 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_log_gvrh

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | coNGN | 0.0670 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_log_kvrh

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | coNGN | 0.0491 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_perovskites

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | coGN | 0.0269 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_mp_gap

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | coGN | 0.1559 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

### matbench_v0.1 / matbench_mp_e_form

| 名次/顺序 | 模型 | 分数 | 指标 | 来源与采集日 |
|---|---|---|---|---|
| 1 | coGN | 0.0170 | MAE ↓ | [来源](https://matbench.materialsproject.org/)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S8](https://matbench.materialsproject.org/)

**覆盖与时效**：更新全部10个回归任务的首页领先结果与单位；dielectric为unitless，perovskites为eV/unit cell，phonons现为1,265样本。3个分类旧榜标签ROC-AUC实为balanced accuracy，不混入回归快照或解释成真ROC-AUC。 [S8](https://matbench.materialsproject.org/) [S10](https://matbench.materialsproject.org/Benchmark%20Info/matbench_v0.1/)

## 联系方式

**公开研究邮箱**：ardunn@lbl.gov；ajain@lbl.gov [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

**问题反馈**：https://github.com/materialsproject/matbench/issues [S4](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)

> 官方公开仓库的问题反馈入口；未发送消息。

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S3](https://matbench.materialsproject.org/)

> 该字段尚未完成精确核验，不表示官方未公开。

**隐私口径**：只使用论文、官方站点或仓库公开联系方式；不收集私人渠道。 [S11](urn:benchmark-atlas:constitution:v0.1)

## 原始文件

**源站PDF**：https://arxiv.org/pdf/2005.00707 [S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707)

**PDF SHA-256**：fbdd140ca579e28117736df44e99c3bbe0c30464316a3ed46d13a0c5306d344d [S7](https://arxiv.org/pdf/2005.00707)

> 本次下载的源站PDF字节校验；不声称重传或替换既有副本。

**PDF字节数**：2513518 [S7](https://arxiv.org/pdf/2005.00707)

**原有文件夹**：{"id": "1k3jZRqYR__FVaY_MxD5J4xmR-L2BiADe", "webViewLink": " [S12](

**其他材料**：[{"kind": "中文介绍", "id": "1NtknnmF6L_ZeGTOBdxqsJpfjOFzow2dvDfhYCTsIBkk", "webViewLink": " [S13](

**原有 PDF**：{"id": "1wRPaSl63GECWDwAqW5_HthOwRislygXV", "webViewLink": " [S14](

## 变更记录

- 2026-11-07，首批官方材料核验、中文改写、；未核实字段显式标记。
- 2026-11-07，：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、官方README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S1](https://arxiv.org/abs/2005.00707) [S2](https://arxiv.org/pdf/2005.00707) [S8](https://matbench.materialsproject.org/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2005.00707](https://arxiv.org/abs/2005.00707)，访问 2026-11-07
- S2，[https://arxiv.org/pdf/2005.00707](https://arxiv.org/pdf/2005.00707)，访问 2026-11-07
- S3，[https://matbench.materialsproject.org/](https://matbench.materialsproject.org/)，访问 2026-11-07
- S4，[https://raw.githubusercontent.com/materialsproject/matbench/main/README.md](https://raw.githubusercontent.com/materialsproject/matbench/main/README.md)，访问 2026-11-07
- S5，[https://arxiv.org/abs/2005.00707](https://arxiv.org/abs/2005.00707)，访问 2026-11-08
- S6，[https://raw.githubusercontent.com/materialsproject/matbench/main/LICENSE](https://raw.githubusercontent.com/materialsproject/matbench/main/LICENSE)，访问 2026-11-07
- S7，[https://arxiv.org/pdf/2005.00707](https://arxiv.org/pdf/2005.00707)，访问 2026-11-08
- S8，[https://matbench.materialsproject.org/](https://matbench.materialsproject.org/)，访问 2026-11-08
- S9，[https://matbench.materialsproject.org/How%20To%20Use/2run/](https://matbench.materialsproject.org/How%20To%20Use/2run/)，访问 2026-11-08
- S10，[https://matbench.materialsproject.org/Benchmark%20Info/matbench_v0.1/](https://matbench.materialsproject.org/Benchmark%20Info/matbench_v0.1/)，访问 2026-11-08
- S11，[urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1)，访问 2026-11-07
- S12，[，访问 2026-11-07
- S13，[，访问 2026-11-07
- S14，[，访问 2026-11-07
