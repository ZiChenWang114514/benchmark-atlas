# SciGym

> 核验日期：2026-11-08。访问日期不等于发布或运行日期；无法证实的字段保留待核实。

SciGym把系统生物学模型变成可交互的干实验室：代理扰动初始浓度，分析时间轨迹，提出缺失反应并提交SBML模型。结构恢复与动力学复现由不同指标衡量；公开large分割不是隐藏测试集，公开评测记录条数也不是新的生物系统数。

导读来源：[官方材料](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）；具体事实及历史访问日期见各字段。

## 基本信息

### 简称

SciGym

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 全称

SciGym systems-biology dry-lab benchmark

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 基准版本

原始SciGym发布：small 137、large 213；未给独立语义版本标签。

来源：[1](https://github.com/h4duan/SciGym)（访问 2026-11-08）；[2](https://huggingface.co/datasets/h4duan/scigym-sbml/raw/main/README.md)（访问 2026-11-08）

### 论文版本

v2；最近提交 2025-07-15

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 发布日期

2025-07-03（首个arXiv提交，不推定数据上线日）

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 主板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）

### 领域标签

- 系统生物学干实验室

来源：[1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）

### 许可与适用范围

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2507.02083

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 代码仓库

https://github.com/h4duan/SciGym

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 数据地址

https://huggingface.co/datasets/h4duan/scigym-sbml

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 官方主页

https://h4duan.github.io/scigym-benchmark/

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 论文标题

Measuring Scientific Capabilities of Language Models with a Systems Biology Dry Lab

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

## 发起与维护

### 机构与发起关系

Toronto、SickKids、Axiom、Mila与Vector等论文署名团队；不推断正式合作协议。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 合作机构/署名单位

项目页作者单位包括University of Toronto、SickKids、Axiom、Mila、Vector Institute；这里只记录署名单位，不推断法律合作协议。

来源：[1](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）

### 作者

- Duan, Haonan
- Lu, Stephen Zhewen
- Harrigan, Caitlin Fiona
- Desai, Nishkrit
- Lu, Jiarui
- Koziarski, Michał
- Cotta, Leonardo
- Maddison, Chris J.

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 当前维护入口

h4duan/SciGym与项目页团队。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 资助方

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

## 设计目标

### 衡量能力

交互实验设计：改变初始浓度、观察动力学，重建隐藏生化反应系统并验证模型。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 设计背景

静态问答不能测可证伪假设、主动实验与迭代科学建模。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

## 构建方式

### 题目或数据来源

BioModels的1,096个人工策展模型过滤为350个可执行SBML系统。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 出题背景

系统生物学、机器学习与分子建模研究者；源库为人工策展模型。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 审核流程

剔除无法执行、无反应/物种、含不支持规则/事件模型；以程序模拟检查。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 质量控制

去注释/元数据、匿名化ID、打乱元素、去反应引用；验证Tellurium仿真兼容。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 去污染措施

匿名化降低靠名称记忆的捷径；源BioModels公开，所以不宣称未进入模型预训练。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

## 数据形式

### 规模

350系统；小系统137个（少于10反应），大系统213个（最多约400反应）。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 题型

多步交互实验、Python建模、隐藏反应网络与动力学重建。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 模态

数值浓度轨迹、SBML/XML、Python与英语交互。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 语言

英语任务/代理提示及Python/SBML。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 难度

按反应系统规模分small/large；强模型在反应结构恢复上仍有限。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 数据划分

small为论文评测的137个模型；large是额外213个未在论文中评测的模型。两者均可由官方data/download.py下载，不应把large误写为隐藏测试集。

来源：[1](https://raw.githubusercontent.com/h4duan/SciGym/main/README.md)（访问 2026-11-07）

## 评测方法

### 指标

Reaction Matching Score（RMS）：按反应物、产物及modifier集合匹配，报告Precision/Recall/F1；Simulation Trajectory Error（STE）以SMAPE比较轨迹，越低越好。

来源：[1](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）

### 评分方式

比对反应图及预测轨迹；系统行为相近不等于动力学表达式唯一正确。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 提示与运行设置

ReAct代理最多20迭代，另3次debug；Python/Tellurium模拟与浓度扰动。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 评测脚本

https://github.com/h4duan/SciGym

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 可比性提醒

有无modifier、small/large与动力学误差方向必须保留；无噪声仿真不代表湿实验。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 数据版本与更新

HF default配置共350条：small 137、large 213；small为论文评测集，large额外系统并非隐藏集。官方还链接scigym-eval，small分割为2466条模型评测记录，不是2466个新生物系统。

来源：[1](https://huggingface.co/datasets/h4duan/scigym-sbml/raw/main/README.md)（访问 2026-11-08）；[2](https://huggingface.co/datasets/h4duan/scigym-eval/raw/main/README.md)（访问 2026-11-08）；[3](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）

### 论文修订记录

- **2026_H2_evidence**：[{"url": "https://arxiv.org/html/2609.19134v1", "date": "2026-09-16", "note": "ScienceIDE §4.1明确列举系统生物学 SciGym 并引用其原始论文 arXiv:2507.02083；为H2学术引用，不是本文实跑。"}]
- **evidence_boundary**：引用不等于重新运行；本页将论文历史实验与现榜分开。
- **paper_metadata**：{"title": "Measuring Scientific Capabilities of Language Models with a Systems Biology Dry Lab", "authors": ["Duan, Haonan", "Lu, Stephen Zhewen", "Harrigan, Caitlin Fiona", "Desai, Nishkrit", "Lu, Jiarui", "Koziarski, Michał", "Cotta, Leonardo", "Maddison, Chris J."], "release": "2025-07-02", "latest": "2025-07-14", "version": "v2", "source_date_basis": "旧release/latest为arXiv源站日期标签；精确时间以arxiv_submission_history为准。"}
- **arxiv_submission_history**：[{"version": "v1", "submitted_at": "2025-07-03"}, {"version": "v2", "submitted_at": "2025-07-15"}]

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 饱和程度

在隐藏系统恢复的历史低F1下不能称饱和；H2仅引用，未提供更新头部成绩。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 争议与已知问题

理想无噪声模拟及可识别性限制；重建相似轨迹不是唯一恢复真实反应机理。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 衍生基准

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

## 榜单快照

### 快照访问日期

2026-11-08 （访问日，不是实验运行日）

来源：[1](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）

### 官方榜单入口

https://h4duan.github.io/scigym-benchmark/

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 第三方入口

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 可核验结果

- {"rank": "不设跨协议名次", "model": "Gemini-2.5-Flash", "score": {"STE": 0.4181, "RMS_precision_with_modifiers": 0.1527, "RMS_recall_with_modifiers": 0.1071, "RMS_F1_with_modifiers": 0.1217, "RMS_precision_without_modifiers": 0.2399, "RMS_recall_without_modifiers": 0.1839, "RMS_F1_without_modifiers": 0.2005}, "metric": "STE越低越好；六项RMS越高越好；均保留原比例不转百分比", "track": "官方项目页/论文v2 Table1；small 137系统历史实验", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "source_row": 1}
- {"rank": "不设跨协议名次", "model": "GPT-4.1-mini", "score": {"STE": 0.6007, "RMS_precision_with_modifiers": 0.1516, "RMS_recall_with_modifiers": 0.1253, "RMS_F1_with_modifiers": 0.132, "RMS_precision_without_modifiers": 0.253, "RMS_recall_without_modifiers": 0.2313, "RMS_F1_without_modifiers": 0.2322}, "metric": "STE越低越好；六项RMS越高越好；均保留原比例不转百分比", "track": "官方项目页/论文v2 Table1；small 137系统历史实验", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "source_row": 2}
- {"rank": "不设跨协议名次", "model": "Claude-3.5-Haiku", "score": {"STE": 0.6281, "RMS_precision_with_modifiers": 0.0858, "RMS_recall_with_modifiers": 0.0421, "RMS_F1_with_modifiers": 0.053, "RMS_precision_without_modifiers": 0.1454, "RMS_recall_without_modifiers": 0.0805, "RMS_F1_without_modifiers": 0.0987}, "metric": "STE越低越好；六项RMS越高越好；均保留原比例不转百分比", "track": "官方项目页/论文v2 Table1；small 137系统历史实验", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "source_row": 3}
- {"rank": "不设跨协议名次", "model": "Gemini-2.5-Pro", "score": {"STE": 0.3212, "RMS_precision_with_modifiers": 0.2138, "RMS_recall_with_modifiers": 0.1664, "RMS_F1_with_modifiers": 0.1817, "RMS_precision_without_modifiers": 0.3781, "RMS_recall_without_modifiers": 0.3219, "RMS_F1_without_modifiers": 0.3383}, "metric": "STE越低越好；六项RMS越高越好；均保留原比例不转百分比", "track": "官方项目页/论文v2 Table1；small 137系统历史实验", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "source_row": 4}
- {"rank": "不设跨协议名次", "model": "GPT-4.1", "score": {"STE": 0.4611, "RMS_precision_with_modifiers": 0.2067, "RMS_recall_with_modifiers": 0.1597, "RMS_F1_with_modifiers": 0.174, "RMS_precision_without_modifiers": 0.3517, "RMS_recall_without_modifiers": 0.2888, "RMS_F1_without_modifiers": 0.3038}, "metric": "STE越低越好；六项RMS越高越好；均保留原比例不转百分比", "track": "官方项目页/论文v2 Table1；small 137系统历史实验", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "source_row": 5}
- {"rank": "不设跨协议名次", "model": "Claude-3.7-Sonnet", "score": {"STE": 0.3615, "RMS_precision_with_modifiers": 0.178, "RMS_recall_with_modifiers": 0.1698, "RMS_F1_with_modifiers": 0.1688, "RMS_precision_without_modifiers": 0.316, "RMS_recall_without_modifiers": 0.317, "RMS_F1_without_modifiers": 0.3047}, "metric": "STE越低越好；六项RMS越高越好；均保留原比例不转百分比", "track": "官方项目页/论文v2 Table1；small 137系统历史实验", "source_url": "https://h4duan.github.io/scigym-benchmark/", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "source_row": 6}

来源：[1](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02083)（访问 2026-11-08）

### 榜单覆盖边界

完整转录六模型七指标；STE排序与RMS排序不同，不设统一总名次。页面与论文v2一致，未把访问日当运行日。HF scigym-eval提供模型对话和最终SBML公开记录，不等于额外测试系统。

来源：[1](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02083)（访问 2026-11-08）；[3](https://huggingface.co/datasets/h4duan/scigym-eval/raw/main/README.md)（访问 2026-11-08）

## 联系方式

### 公开研究联系

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 公开反馈渠道

https://github.com/h4duan/SciGym/issues

来源：[1](https://github.com/h4duan/SciGym)（访问 2026-11-07）

### 官方社交账号

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 联系方式原则

仅使用项目站、论文和官方仓库公开反馈渠道，不采集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08）

## 原始文件

### 论文原件

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 原始PDF地址

https://arxiv.org/pdf/2507.02083

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 原始文件SHA-256

8f490e009f6448434412f43ec8c89cd97d6100ebfa001bf6b38d17f7433f86b1

说明：实际下载原始PDF字节计算；不据此更改既有文件。

来源：[1](https://arxiv.org/pdf/2507.02083)（访问 2026-11-08）

### 原始文件字节数

7093862

来源：[1](https://arxiv.org/pdf/2507.02083)（访问 2026-11-08）

### 文件夹

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）

### 其他文档

来源：[1]（访问 2026-11-07）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://arxiv.org/abs/2507.02083)（访问 2026-11-08）；[2](https://h4duan.github.io/scigym-benchmark/)（访问 2026-11-08）
