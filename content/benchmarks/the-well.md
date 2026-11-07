# The Well

> 本页依据官方材料中文整理；核验日期 2026-11-07（KST）。历史实验不代表当前 SOTA；待核实不等于未公开。

## 基本信息

### 简称

The Well

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 全称

The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 基准版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 论文版本

v2；最近论文日期 2025-02-21

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 发布日期

2024-11-30（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 主板块

物理

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.06095v3)（访问 2026-11-07，KST）


### 领域标签

- 多物理场模拟与算子学习

来源：[1](https://arxiv.org/html/2610.06095v3)（访问 2026-11-07，KST）


### 许可与适用范围

代码 BSD-3-Clause；已核验 active_matter 数据卡为 CC-BY-4.0，其他子集需逐一核验。

来源：[1](https://raw.githubusercontent.com/PolymathicAI/the_well/master/LICENSE)（访问 2026-11-07，KST）；[2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md)（访问 2026-11-07，KST）


### 论文

https://arxiv.org/abs/2412.00568

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 代码仓库

https://github.com/PolymathicAI/the_well

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 数据地址

https://huggingface.co/polymathic-ai

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 官方主页

https://polymathic-ai.org/the_well/

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 论文标题

The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 发起与维护

### 机构与发起关系

Polymathic AI；项目页明确说明牵头。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）；[2](https://polymathic-ai.org/the_well/)（访问 2026-11-07，KST）


### 合作机构

Flatiron Institute、Colorado Boulder、Cambridge、NYU、Rutgers、Cornell、Tokyo、Los Alamos、UC Berkeley、Princeton、CEA DAM、Liège等项目合作方；非推定独立出资关系。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）；[2](https://polymathic-ai.org/the_well/)（访问 2026-11-07，KST）


### 作者

- Ohana, Ruben
- McCabe, Michael
- Meyer, Lucas
- Morel, Rudy
- Agocs, Fruzsina J.
- Beneitez, Miguel
- Berger, Marsha
- Burkhart, Blakesley
- Burns, Keaton
- Dalziel, Stuart B.
- Fielding, Drummond B.
- Fortunato, Daniel
- Goldberg, Jared A.
- Hirashima, Keiya
- Jiang, Yan-Fei
- Kerswell, Rich R.
- Maddu, Suryanarayana
- Miller, Jonah
- Mukhopadhyay, Payel
- Nixon, Stefan S.
- Shen, Jeff
- Watteaux, Romain
- Blancard, Bruno Régaldo-Saint
- Rozet, François
- Parker, Liam H.
- Cranmer, Miles
- Ho, Shirley

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 当前维护方

Polymathic AI 项目团队；官方文档列 Ruben Ohana、Michael McCabe 为公开联系方。

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-07，KST）


### 资助方

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 设计目标

### 衡量能力

从历史时空场预测后续物理演化；跨多物理系统的代理模型/神经算子学习及长时滚动稳定性。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 设计背景

常见算子数据只覆盖较少物理行为；此库强调不同维数、边界条件、尺度与非线性机制的多样性。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 构建方式

### 题目或数据来源

领域科学家与数值软件开发者提供真实数值模拟；不是LLM合成问答。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 出题背景

计算物理、流体、天体物理、数值分析与机器学习研究者合作。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 审核流程

论文逐数据集说明控制方程、生成程序、数值方法与物理机制；独立外审数量待核实。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 质量控制

统一HDF5组织、网格/时间元数据及标量、矢量、张量字段；保留各物理系统语义。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 去污染措施

按完整模拟轨迹划分，避免同一轨迹片段随机跨集合；针对预训练语料污染的独立审计待核实。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 数据形式

### 规模

16个数据集，合计15TB（官方口径）；各集约6.9GB至5.1TB。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）；[2](https://polymathic-ai.org/the_well/)（访问 2026-11-07，KST）


### 题型

数值时序回归；单步预测和自回归多步rollout。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 模态

规则网格数值场、时间序列与物理元数据；HDF5/float32接口。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 语言

主体为数值张量与Python接口；不是自然语言选择题。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 难度

不同系统误差差异明显；没有统一题目难度等级。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 数据划分

每个数据集按轨迹约80%训练、10%验证、10%测试；公开可下载。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 评测方法

### 指标

VRMSE（越低越好，预测目标场均值约为1）；另提供NMSE/NRMSE、最大误差、分频谱误差等。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 评分方式

逐物理场计算后平均；单步和不同时间窗rollout分开报告。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 提示与运行设置

非问答提示评测；用 Hydra 配置固定模型、数据、优化器和训练资源。官方示例为 active_matter 上的 FNO。

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-07，KST）


### 评测脚本

https://github.com/PolymathicAI/the_well

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 可比性提醒

不能将不同方程、分辨率、rollout时域或训练算力的误差直接合成总冠军。原论文自称示例基线而非穷尽最优调参。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 最新情况

### 核验日期

2026-11-07 Asia/Seoul

说明：2026H2 引用/使用证据：2026-08，论文表1及参考文献14明确引用 The Well，属于文献引用，不声称重跑整库。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）；[2](https://arxiv.org/abs/2608.22504)（访问 2026-11-07，KST）；[3](https://arxiv.org/abs/2608.22504)（访问 2026-11-07，KST）


### 数据版本与更新

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 论文修订记录

- 2026_H2_evidence：[{'url': 'https://arxiv.org/html/2610.06095v3', 'date': '2026-10-07', 'note': '同一论文 v3 引言将 The Well（Ohana等2024）与 PDEBench 并列为公开算子学习基准；为2026H2具体学术引用。'}]
- evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。
- paper_metadata：{'title': 'The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning', 'authors': ['Ohana, Ruben', 'McCabe, Michael', 'Meyer, Lucas', 'Morel, Rudy', 'Agocs, Fruzsina J.', 'Beneitez, Miguel', 'Berger, Marsha', 'Burkhart, Blakesley', 'Burns, Keaton', 'Dalziel, Stuart B.', 'Fielding, Drummond B.', 'Fortunato, Daniel', 'Goldberg, Jared A.', 'Hirashima, Keiya', 'Jiang, Yan-Fei', 'Kerswell, Rich R.', 'Maddu, Suryanarayana', 'Miller, Jonah', 'Mukhopadhyay, Payel', 'Nixon, Stefan S.', 'Shen, Jeff', 'Watteaux, Romain', 'Blancard, Bruno Régaldo-Saint', 'Rozet, François', 'Parker, Liam H.', 'Cranmer, Miles', 'Ho, Shirley'], 'release': '2024-11-30', 'latest': '2025-02-21', 'version': 'v2'}

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）；[2](https://arxiv.org/html/2610.06095v3)（访问 2026-11-07，KST）


### 饱和程度

不能以一个总分判饱和；长期动力学与分布变化仍有误差。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 争议与已知问题

代理模型拟合数值求解器，不等同于证明真实物理规律；跨轨迹划分不代表跨初值/参数外推均已控制。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 衍生基准

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 榜单快照

### 快照访问日期

2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 官方榜单入口

https://polymathic-ai.org/the_well/

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 第三方入口

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 可核验结果

历史原论文Table 2：viscoelastic_instability单步VRMSE：FNO 0.7212、TFNO 0.7102、U-net 0.4185、CNextU-net 0.2499；模型为论文架构标签，固定训练预算；不是2026实时排名。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 榜单覆盖边界

本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）；[2](https://artificialanalysis.ai/)（访问 2026-11-07，KST）；[3](https://epoch.ai/)（访问 2026-11-07，KST）；[4](https://lmarena.ai/)（访问 2026-11-07，KST）


## 联系方式

### 公开邮箱

- rohana@flatironinstitute.org
- mmccabe@flatironinstitute.org

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-07，KST）


### 公开反馈渠道

https://github.com/PolymathicAI/the_well/issues

来源：[1](https://github.com/PolymathicAI/the_well)（访问 2026-11-07，KST）


### 官方社交账号

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 联系方式原则

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


## 原始文件

### Drive 论文原件

- id：1nF862k2HR4HHw4_5Jo8_3xJE2UgSYJ5l
- webViewLink：https://drive.google.com/file/d/1nF862k2HR4HHw4_5Jo8_3xJE2UgSYJ5l/view

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 原始 PDF 地址

https://arxiv.org/pdf/2412.00568

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 原始文件 SHA-256

050ca3384f117252586c27ff9940781852cc457e2967d7879a7c8a0b30dc8e1f

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-07，KST）


### 原始文件字节数

5375610

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-07，KST）


### Drive 文件夹

- id：1_3NZPzkcaCBep04AYI5UroGFMuDa3jpa
- webViewLink：https://drive.google.com/drive/folders/1_3NZPzkcaCBep04AYI5UroGFMuDa3jpa

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）


### 其他文档

- {"type": "中文介绍 Google Doc", "id": "1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8", "webViewLink": "https://docs.google.com/document/d/1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8/edit"}

来源：[1](https://docs.google.com/document/d/1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8/edit)（访问 2026-11-07，KST）


## 变更记录

- {"date": "2026-11-07", "timezone": "Asia/Seoul", "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"}
- {"date": "2026-11-07", "timezone": "Asia/Seoul", "change": "第1轮深度核验：补官方许可、数据划分、评分及运行协议，复核榜单可读性，并记录2026H2引用证据与冲突；保留无法验证字段。"}

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，KST）

