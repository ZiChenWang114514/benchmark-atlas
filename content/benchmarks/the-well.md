# The Well

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

The Well不是科学选择题，而是16个物理模拟数据集组成的15TB时空场预测资源。基线任务用四步历史预测下一步，并测试自回归误差；不同系统与时间窗不可合成未经定义的总冠军。旧黏弹不稳定性数据因处理错误被弃用，必须区分修正版。

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）；[2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md)（访问 2026-11-08，）；[3](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）

## 基本信息

### 简称

The Well

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 全称

The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 基准版本

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 论文版本

arXiv v2；提交于 2025-02-22 04:24:16

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 发布日期

2024-12-01 04:42:14 （arXiv v1提交；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 主板块

物理

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.06095v3)（访问 2026-11-07，）

### 领域标签

- 多物理场模拟与算子学习

来源：[1](https://arxiv.org/html/2610.06095v3)（访问 2026-11-07，）

### 许可与适用范围

代码BSD-3-Clause（当前仓库LICENSE）；论文Datasheet Q43明确整套数据CC-BY-4.0，active_matter数据卡同样标CC-BY-4.0。部分生成程序为专有代码，不推定可重分发。

来源：[1](https://github.com/PolymathicAI/the_well/blob/master/LICENSE)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）；[3](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md)（访问 2026-11-08，）

### 论文

https://arxiv.org/abs/2412.00568

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 代码仓库

https://github.com/PolymathicAI/the_well

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 数据地址

https://huggingface.co/polymathic-ai

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 官方主页

https://polymathic-ai.org/the_well/

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 论文标题

The Well: a Large-Scale Collection of Diverse Physics Simulations for Machine Learning

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

## 发起与维护

### 机构与发起关系

Polymathic AI；项目页明确说明牵头。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）；[2](https://polymathic-ai.org/the_well/)（访问 2026-11-07，）

### 合作机构

Flatiron Institute、Colorado Boulder、Cambridge、NYU、Rutgers、Cornell、Tokyo、Los Alamos、UC Berkeley、Princeton、CEA DAM、Liège等项目合作方；非推定独立出资关系。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）；[2](https://polymathic-ai.org/the_well/)（访问 2026-11-07，）

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

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 当前维护方

Polymathic AI 项目团队；官方文档列 Ruben Ohana、Michael McCabe 为公开联系方。

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-07，）

### 资助与支持

Polymathic AI获Simons Foundation与Schmidt Sciences资助，NVIDIA捐赠DGX Cloud节点时数；论文还逐贡献数据说明EPSRC、NASA、LANL、DOE、CEA等支持，不能合并成单一总经费。

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

## 设计目标

### 衡量能力

从历史时空场预测后续物理演化；跨多物理系统的代理模型/神经算子学习及长时滚动稳定性。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 设计背景

常见算子数据只覆盖较少物理行为；此库强调不同维数、边界条件、尺度与非线性机制的多样性。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

## 构建方式

### 题目或数据来源

领域科学家与数值软件开发者提供真实数值模拟；不是LLM合成问答。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 出题背景

计算物理、流体、天体物理、数值分析与机器学习研究者合作。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 审核流程

论文逐数据集说明控制方程、生成程序、数值方法与物理机制；独立外审数量待核实。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 质量控制

各领域专家给出方程、数值方法、边界条件与参数；统一HDF5及张量元数据；当前仓库明确viscoelastic_instability因处理错误弃用，viscoelastic_instability_v2为相同数据的修正版。

来源：[1](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

### 去污染与泄漏

默认按每组模拟参数的初始条件做80/10/10划分；模拟数量不足的子集改用不重叠时间块，不能声称所有子集都完整按轨迹切分。独立预训练语料污染审计待核实。

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

## 数据形式

### 规模

16个数据集，合计15TB（官方口径）；各集约6.9GB至5.1TB。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）；[2](https://polymathic-ai.org/the_well/)（访问 2026-11-07，）

### 题型

数值时序回归；单步预测和自回归多步rollout。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 模态

规则网格数值场、时间序列与物理元数据；HDF5/float32接口。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 语言

主体为数值张量与Python接口；不是自然语言选择题。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 难度

不同系统误差差异明显；没有统一题目难度等级。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 数据划分

公开train/valid/test；通常按初始条件80/10/10，轨迹不足时按不重叠时间块同比分割，时间块不保证严格按时间先后排列（论文Datasheet Q12）。

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

## 评测方法

### 指标

VRMSE（越低越好，预测目标场均值约为1）；另提供NMSE/NRMSE、最大误差、分频谱误差等。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 评分方式

逐物理场计算后平均；单步和不同时间窗rollout分开报告。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 提示与运行设置

非问答提示评测；用 Hydra 配置固定模型、数据、优化器和训练资源。官方示例为 active_matter 上的 FNO。

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-07，）

### 评测脚本

https://github.com/PolymathicAI/the_well

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 可比性提醒

不能将不同方程、分辨率、rollout时域或训练算力的误差直接合成总冠军。原论文自称示例基线而非穷尽最优调参。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-08，）

### 数据版本与更新

当前官方仓库提供viscoelastic_instability_v2并弃用旧viscoelastic_instability（仅保留向后比较）；整套数据统一语义版本号待核实，软件包版本不能代替数据版本。

来源：[1](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-12-01 04:42:14 ", "timezone": ""}
- {"version": "v2", "submitted_at": "2025-02-22 04:24:16 ", "timezone": ""}

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-08，）

### 饱和证据与局限

官方明确原论文是单张H100、12小时预算的示例基线，不是SOTA；单步与rollout性能差距大，不能从单步低误差认定全部物理动力学已饱和。

来源：[1](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

### 争议与已知问题

viscoelastic_instability旧版因处理错误被弃用，需换v2；论文基线中的旧版结果只作历史。部分数据时间块切分仍共享同一模拟的物理参数，不应宣称严格跨轨迹外推。

来源：[1](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

### 衍生或后继基准

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）；[2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md)（访问 2026-11-08，）；[3](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）

### 官方榜单入口

https://polymathic-ai.org/the_well/

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

### 第三方入口

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| 论文v2表2 / acoustic_scattering (maze) | 4 | FNO | 0.5062 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / acoustic_scattering (maze) | 3 | TFNO | 0.5057 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / acoustic_scattering (maze) | 2 | U-net | 0.0351 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / acoustic_scattering (maze) | 1 | CNextU-net | 0.0153 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / active_matter | 4 | FNO | 0.3691 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / active_matter | 3 | TFNO | 0.3598 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / active_matter | 2 | U-net | 0.2489 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / active_matter | 1 | CNextU-net | 0.1034 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / convective_envelope_rsg | 1 | FNO | 0.0269 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / convective_envelope_rsg | 2 | TFNO | 0.0283 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / convective_envelope_rsg | 3 | U-net | 0.0555 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / convective_envelope_rsg | 4 | CNextU-net | 0.0799 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / euler_multi_quadrants (periodic b.c.) | 3 | FNO | 0.4081 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / euler_multi_quadrants (periodic b.c.) | 4 | TFNO | 0.4163 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / euler_multi_quadrants (periodic b.c.) | 2 | U-net | 0.1834 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / euler_multi_quadrants (periodic b.c.) | 1 | CNextU-net | 0.1531 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / gray_scott_reaction_diffusion | 1 | FNO | 0.1365 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / gray_scott_reaction_diffusion | 4 | TFNO | 0.3633 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / gray_scott_reaction_diffusion | 3 | U-net | 0.2252 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / gray_scott_reaction_diffusion | 2 | CNextU-net | 0.1761 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / helmholtz_staircase | 1 | FNO | 0.00046 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / helmholtz_staircase | 2 | TFNO | 0.00346 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / helmholtz_staircase | 3 | U-net | 0.01931 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / helmholtz_staircase | 4 | CNextU-net | 0.02758 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / MHD_64 | 4 | FNO | 0.3605 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / MHD_64 | 3 | TFNO | 0.3561 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / MHD_64 | 2 | U-net | 0.1798 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / MHD_64 | 1 | CNextU-net | 0.1633 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / planetswe | 2 | FNO | 0.1727 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / planetswe | 1 | TFNO | 0.0853 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / planetswe | 3 | U-net | 0.362 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / planetswe | 4 | CNextU-net | 0.3724 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / post_neutron_star_merger | 2 | FNO | 0.3866 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / post_neutron_star_merger | 1 | TFNO | 0.3793 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_benard | 3 | FNO | 0.8395 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_benard | 1 | TFNO | 0.6566 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_benard | 4 | U-net | 1.486 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_benard | 2 | CNextU-net | 0.6699 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_taylor_instability (At = 0.25) | — | FNO | >10 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_taylor_instability (At = 0.25) | — | TFNO | >10 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_taylor_instability (At = 0.25) | — | U-net | >10 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / rayleigh_taylor_instability (At = 0.25) | — | CNextU-net | >10 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / shear_flow | 2 | FNO | 1.189 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / shear_flow | 3 | TFNO | 1.472 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / shear_flow | 4 | U-net | 3.447 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / shear_flow | 1 | CNextU-net | 0.808 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / supernova_explosion_64 | 3 | FNO | 0.3783 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / supernova_explosion_64 | 4 | TFNO | 0.3785 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / supernova_explosion_64 | 1 | U-net | 0.3063 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / supernova_explosion_64 | 2 | CNextU-net | 0.3181 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulence_gravity_cooling | 2 | FNO | 0.2429 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulence_gravity_cooling | 3 | TFNO | 0.2673 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulence_gravity_cooling | 4 | U-net | 0.6753 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulence_gravity_cooling | 1 | CNextU-net | 0.2096 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_2D | 3 | FNO | 0.5001 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_2D | 4 | TFNO | 0.5016 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_2D | 2 | U-net | 0.2418 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_2D | 1 | CNextU-net | 0.1956 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_3D | 4 | FNO | 0.5278 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_3D | 3 | TFNO | 0.5187 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_3D | 2 | U-net | 0.3728 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / turbulent_radiative_layer_3D | 1 | CNextU-net | 0.3667 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / viscoelastic_instability | 4 | FNO | 0.7212 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / viscoelastic_instability | 3 | TFNO | 0.7102 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / viscoelastic_instability | 2 | U-net | 0.4185 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表2 / viscoelastic_instability | 1 | CNextU-net | 0.2499 | one-step VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；4步历史预测下一步；单H100 / 12h预算 | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 6:12 | 3 | FNO | 1.06 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 13:30 | 4 | FNO | 1.72 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 6:12 | 4 | TFNO | 1.13 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 13:30 | 3 | TFNO | 1.23 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 6:12 | 1 | U-net | 0.56 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 13:30 | 1 | U-net | 0.92 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 6:12 | 2 | CNextU-net | 0.78 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / acoustic_scattering (maze) / 13:30 | 2 | CNextU-net | 1.13 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 6:12 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 13:30 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 6:12 | 3 | TFNO | 7.52 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 13:30 | 3 | TFNO | 4.72 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 6:12 | 2 | U-net | 2.53 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 13:30 | 1 | U-net | 2.62 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 6:12 | 1 | CNextU-net | 2.11 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / active_matter / 13:30 | 2 | CNextU-net | 2.71 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 6:12 | 1 | FNO | 0.28 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 13:30 | 1 | FNO | 0.47 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 6:12 | 2 | TFNO | 0.32 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 13:30 | 2 | TFNO | 0.65 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 6:12 | 3 | U-net | 0.76 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 13:30 | 4 | U-net | 2.16 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 6:12 | 4 | CNextU-net | 1.15 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / convective_envelope_rsg / 13:30 | 3 | CNextU-net | 1.59 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 6:12 | 2 | FNO | 1.13 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 13:30 | 1 | FNO | 1.37 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 6:12 | 3 | TFNO | 1.23 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 13:30 | 2 | TFNO | 1.52 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 6:12 | 1 | U-net | 1.02 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 13:30 | 3 | U-net | 1.63 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 6:12 | 4 | CNextU-net | 4.98 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / euler_multi_quadrants / 13:30 | — | CNextU-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 6:12 | 3 | FNO | 0.89 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 13:30 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 6:12 | 4 | TFNO | 1.54 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 6:12 | 2 | U-net | 0.57 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 13:30 | — | U-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 6:12 | 1 | CNextU-net | 0.29 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / gray_scott_reaction_diffusion / 13:30 | 1 | CNextU-net | 7.62 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 6:12 | 1 | FNO | 0.002 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 13:30 | 1 | FNO | 0.003 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 6:12 | 2 | TFNO | 0.011 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 13:30 | 2 | TFNO | 0.019 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 6:12 | 3 | U-net | 0.057 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 13:30 | 3 | U-net | 0.097 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 6:12 | 4 | CNextU-net | 0.11 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / helmholtz_staircase / 13:30 | 4 | CNextU-net | 0.194 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 6:12 | 1 | FNO | 1.24 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 13:30 | 1 | FNO | 1.61 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 6:12 | 2 | TFNO | 1.25 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 13:30 | 2 | TFNO | 1.81 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 6:12 | 4 | U-net | 1.65 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 13:30 | 4 | U-net | 4.66 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 6:12 | 3 | CNextU-net | 1.3 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / MHD_64 / 13:30 | 3 | CNextU-net | 2.23 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 6:12 | 3 | FNO | 0.81 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 13:30 | 4 | FNO | 2.96 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 6:12 | 1 | TFNO | 0.29 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 13:30 | 2 | TFNO | 0.55 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 6:12 | 4 | U-net | 1.18 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 13:30 | 3 | U-net | 1.92 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 6:12 | 2 | CNextU-net | 0.42 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / planetswe / 13:30 | 1 | CNextU-net | 0.52 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / post_neutron_star_merger / 6:12 | 2 | FNO | 0.76 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / post_neutron_star_merger / 13:30 | 1 | FNO | 1.05 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / post_neutron_star_merger / 6:12 | 1 | TFNO | 0.7 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / post_neutron_star_merger / 13:30 | 1 | TFNO | 1.05 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 6:12 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 13:30 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 6:12 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 6:12 | — | U-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 13:30 | — | U-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 6:12 | — | CNextU-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_benard / 13:30 | — | CNextU-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 6:12 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 13:30 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 6:12 | 1 | TFNO | 6.72 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 6:12 | — | U-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 13:30 | 1 | U-net | 2.84 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 6:12 | — | CNextU-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / rayleigh_taylor_instability / 13:30 | 2 | CNextU-net | 7.43 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 6:12 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 13:30 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 6:12 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 6:12 | — | U-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 13:30 | — | U-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 6:12 | 1 | CNextU-net | 2.33 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / shear_flow / 13:30 | — | CNextU-net | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 6:12 | 4 | FNO | 2.41 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 13:30 | — | FNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 6:12 | 3 | TFNO | 1.86 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 6:12 | 1 | U-net | 0.94 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 13:30 | 1 | U-net | 1.69 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 6:12 | 2 | CNextU-net | 1.12 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / supernova_explosion_64 / 13:30 | 2 | CNextU-net | 4.55 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 6:12 | 2 | FNO | 3.55 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 13:30 | 3 | FNO | 5.63 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 6:12 | 3 | TFNO | 4.49 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 13:30 | 4 | TFNO | 6.95 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 6:12 | 4 | U-net | 7.14 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 13:30 | 2 | U-net | 4.15 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 6:12 | 1 | CNextU-net | 1.3 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulence_gravity_cooling / 13:30 | 1 | CNextU-net | 2.09 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 6:12 | 3 | FNO | 1.79 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 13:30 | 3 | FNO | 3.54 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 6:12 | 4 | TFNO | 6.01 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 6:12 | 2 | U-net | 0.66 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 13:30 | 2 | U-net | 1.04 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 6:12 | 1 | CNextU-net | 0.54 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_2D / 13:30 | 1 | CNextU-net | 1.01 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 6:12 | 2 | FNO | 0.81 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 13:30 | 2 | FNO | 0.94 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 6:12 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 13:30 | — | TFNO | >10 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 6:12 | 3 | U-net | 0.95 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 13:30 | 3 | U-net | 1.09 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 6:12 | 1 | CNextU-net | 0.77 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / turbulent_radiative_layer_3D / 13:30 | 1 | CNextU-net | 0.86 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / viscoelastic_instability / 6:12 | 4 | FNO | 4.11 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / viscoelastic_instability / 6:12 | 3 | TFNO | 0.93 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / viscoelastic_instability / 6:12 | 2 | U-net | 0.89 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |
| 论文v2表3 / viscoelastic_instability / 6:12 | 1 | CNextU-net | 0.52 | time-averaged VRMSE（越低越好） | 原论文数据；viscoelastic_instability为已弃用旧版；从轨迹开始自回归；不同于滑窗one-step | [来源页未列运行日](https://arxiv.org/pdf/2412.00568)；采集2026-11-08 |

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）；[2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md)（访问 2026-11-08，）；[3](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）

### 榜单覆盖边界

恢复论文v2表2单步与表3两个rollout窗口所有非缺失值；按数据子集、窗口分轨，VRMSE越低越好。>10保留为大于10的下界标签，—不转0；viscoelastic_instability成绩明确旧版，不能重标修正版v2。此为论文基线，不宣称当前SOTA。

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）；[2](https://huggingface.co/datasets/polymathic-ai/active_matter/raw/main/README.md)（访问 2026-11-08，）；[3](https://github.com/PolymathicAI/the_well)（访问 2026-11-08，）

## 联系方式

### 官方公开邮箱

- rohana@flatironinstitute.org
- mmccabe@flatironinstitute.org

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-07，）

### 公开反馈渠道

https://github.com/PolymathicAI/the_well/issues

来源：[1](https://github.com/PolymathicAI/the_well)（访问 2026-11-07，）

### 官方社交账号

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

### 联系方式/隐私原则

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2412.00568

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

### PDF SHA-256

050ca3384f117252586c27ff9940781852cc457e2967d7879a7c8a0b30dc8e1f

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

### PDF字节数

```json
5375610
```

来源：[1](https://arxiv.org/pdf/2412.00568)（访问 2026-11-08，）

### 文件夹

```json
{
  "id": "1_3NZPzkcaCBep04AYI5UroGFMuDa3jpa"
  "webViewLink": "
}
```

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

### 其他文档

- {"type": "中文介绍", "id": "1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8", "webViewLink": "https://docs.google.com/document/d/1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8/edit"}

来源：[1](https://docs.google.com/document/d/1dEIuyVWpFSkApyB1YcrbQgAJlK0IAAvyoMRF7mYGDN8/edit)（访问 2026-11-07，）

### 论文原件

```json
{
  "id": "1nF862k2HR4HHw4_5Jo8_3xJE2UgSYJ5l"
  "webViewLink": "
}
```

来源：[1](https://arxiv.org/abs/2412.00568)（访问 2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://polymathic-ai.org/the_well/)（访问 2026-11-08，）
