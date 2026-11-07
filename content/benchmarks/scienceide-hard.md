# ScienceIDE-Hard

> 第1轮实证优化｜2026-11-07（KST / Asia/Seoul）。待核实不等于未公开；历史论文结果不等于实时榜单。

## 基本信息

### 简称

ScienceIDE-Hard

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 名称

ScienceIDE-Hard

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 基准版本

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 论文版本

v1；最近论文日期 2026-09-16

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 发布日期

2026-09-16（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 主板块

物理

> 编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）

### 领域标签

- 科学软件执行（以计算物理和地学为主）

来源：[1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）

### 许可与使用范围

自有代码及任务元数据的许可证尚待完整发布时宣布；上游科学代码各自保留许可证，不能把上游 MIT/Apache 许可外推给整个基准。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2609.19134

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 官方代码

https://github.com/aitofound/ScienceIDE

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 数据入口

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 官方主页

https://aitonomy.org/projects/scienceide

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 论文标题

ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 发起与维护

### 机构与作者单位

PhAI-Labs、Qwen（论文页项目标识）；多机构作者合作。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 合作机构

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 作者

- Geng, Hejia
- Huang, Zesen
- Li, Haoyang
- Li, Wenbin
- Wu, Koutian
- Zhou, Zihan
- Pang, Yuanbo
- Liu, Weihao
- Xu, Zigong
- Li, Zhiping
- Zhang, Zongzheng
- Dong, Chuanfei
- Sun, Jiankai
- Zheng, Tianzhe
- Xie, Fengyu
- Ma, Yue
- Shi, Yueheng
- Xie, Tong
- Di, Zonglin
- Liu, Xianrong
- Gao, Qucheng
- Liu, Yimin
- Pan, Jiaming
- Huang, Sheng
- Ma, Xiao-Han
- Yuan, Lanqing
- Zhu, Zhenlin
- Liu, Ziang
- Xu, Ziyang
- Wang, Junkai
- Liang, Kangkai
- Xian, Jiayi
- Zhao, Zehong
- Xu, Liuwei
- Xie, Jingxu
- Zhang, Peijin
- Gao, Qiang
- Xing, Chengyi
- Zhao, Zhe
- Wang, Xi
- Xing, Yaopeng
- Meng, Xing
- Yin, Zhenfei
- Wu, Yingcheng
- Yang, Ling

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 维护方

AItonomy/aitofound ScienceIDE项目仓库。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 资助方

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 设计目标

### 测量能力

在真实科学软件中修复和实现算法，并满足领域数值与物理契约；多文件修改及约定忠实重建。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 针对的不足

代码单元测试和通用程序修复不能充分测科学数值等价、守恒不变量与复杂领域约定。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 构建方式

### 材料来源

从科学代码库及官方测试构建执行环境，以可运行科学检查合成修复/实现任务；Hard子集来自五个仓库家族。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 出题背景

科学计算与模型训练团队；环境来源覆盖流体、等离子体、海洋大气等领域。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 审核流程

先提出候选，再通过执行建立有效性；每个准入任务有known-valid witness、空交付基线和有缺陷起点。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 质量控制

每个公开任务均经执行验证：官方修复在评分容器得到 1.0，未修复构建留有奖励空间，agent 镜像不含答案材料。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 去污染措施

固定85个相同任务标识供全体模型；训练/验证任务标识不交叉；源代码公开不等于无训练暴露。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 数据形式

### 规模与统计口径

ScienceIDE-Hard 共 85 项任务；仓库预览公开其中 30 项，另外 55 项仅列名并保留。整体基础设施有 64 个环境，不等于 85 项任务。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 任务与题型

多步工具调用、科学代码修复与实现，交付可运行修改。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 模态

科学源代码、命令行、数值输出与文本说明。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 语言

多科学代码库语言与英语交互；逐环境语言见来源附录。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 难度

以未修复得分、编辑位置数量、验证开销和实测通过率描述难度，而不是手工赋予单一难度标签。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 公开与保留划分

Hard85：30 项公开、55 项保留；环境集：15 个公开、49 个保留。两种统计单位不可混淆。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

## 评测方法

### 指标

严格科学任务成功率；运行时间、输出token及历史估算成本辅助分析。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 评分方式

reward 为物理案例评分均值；reward_repair=max(0,(reward−floor)/(1−floor))，其中 floor 为未修复构建的得分。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 提示与运行设定

15个模型—harness组合，固定85题，单任务1小时预算；多次重复及within-task bootstrap，Fable仅单次。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 官方评测入口

https://github.com/aitofound/ScienceIDE/tree/main/hard85

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 可比性提醒

模型与harness/工具预算耦合；Fable单测，Opus与Astra置信区间重叠。时间截断曲线为事后完成分布，不是新预算重跑。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 最新情况

### 本次核验

2026-11-07 Asia/Seoul

> 2026H2 活跃性复核：2026-09-16 技术报告及官方仓库包含训练/评估使用；这是发布与自评证据，不是独立外部引用。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）；[2](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 版本与发布状态

官方 README 标记为 preview/work in progress；完整环境、任务库和出题管线仍待后续发布。

来源：[1](https://raw.githubusercontent.com/aitofound/ScienceIDE/main/README.md)（访问 2026-11-07）

### 论文修订

2026_H2_evidence：- url：https://arxiv.org/html/2609.19134v1；date：2026-09-16；note：ScienceIDE §3在85项 hard 科学代码任务上实际评测15个模型—harness组合；任务含天体流体、等离子体、海洋大气与粒子模拟。；evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。；paper_metadata：title：ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments；authors：- Geng, Hejia
- Huang, Zesen
- Li, Haoyang
- Li, Wenbin
- Wu, Koutian
- Zhou, Zihan
- Pang, Yuanbo
- Liu, Weihao
- Xu, Zigong
- Li, Zhiping
- Zhang, Zongzheng
- Dong, Chuanfei
- Sun, Jiankai
- Zheng, Tianzhe
- Xie, Fengyu
- Ma, Yue
- Shi, Yueheng
- Xie, Tong
- Di, Zonglin
- Liu, Xianrong
- Gao, Qucheng
- Liu, Yimin
- Pan, Jiaming
- Huang, Sheng
- Ma, Xiao-Han
- Yuan, Lanqing
- Zhu, Zhenlin
- Liu, Ziang
- Xu, Ziyang
- Wang, Junkai
- Liang, Kangkai
- Xian, Jiayi
- Zhao, Zehong
- Xu, Liuwei
- Xie, Jingxu
- Zhang, Peijin
- Gao, Qiang
- Xing, Chengyi
- Zhao, Zhe
- Wang, Xi
- Xing, Yaopeng
- Meng, Xing
- Yin, Zhenfei
- Wu, Yingcheng
- Yang, Ling；release：2026-09-16；latest：2026-09-16；version：v1

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）

### 饱和情况

历史最佳仍约三分之一未解决；不能从头部点估计做显著性排名。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 争议与局限

已知有效解并不保证通用科学验证完备；公开仓库预训练暴露与策略筛选依赖需单独审计。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 衍生资源

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 榜单快照

### 采集日期

2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 官方榜单入口

https://aitonomy.org/projects/scienceide

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 第三方榜单

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 已核验结果

原论文2026-09 Figure7历史：Fable5.1 67.1%、Opus5 64.6%、Astra63.1%、Sol55.0%；均为85题1小时严格成功率。名称按论文标签，完整API版本/执行日期待核实；不宣称实时SOTA。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 覆盖与时效说明

本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）；[2](https://artificialanalysis.ai/)（访问 2026-11-07）；[3](https://epoch.ai/)（访问 2026-11-07）；[4](https://lmarena.ai/)（访问 2026-11-07）

## 联系方式

### 公开联系邮箱

- team@aitonomy.org
- yang@phai-labs.com

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### Issues

https://github.com/aitofound/ScienceIDE/issues

来源：[1](https://github.com/aitofound/ScienceIDE)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 隐私原则

待核实

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 原始文件

### 原文 PDF

https://arxiv.org/pdf/2609.19134

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 原件 SHA-256

1e7b6acfba2328ab5beec566914b4d72c2ee71d89a420fa8a65a0b5a123485cb

来源：[1](https://arxiv.org/pdf/2609.19134)（访问 2026-11-07）

### 原件字节数

1276454

来源：[1](https://arxiv.org/pdf/2609.19134)（访问 2026-11-07）

### Drive 文件夹

id：1M4oZUj7501UWir_irDTwM567TEAuDbnD；webViewLink：https://drive.google.com/drive/folders/1M4oZUj7501UWir_irDTwM567TEAuDbnD

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 其他官方文档

- type：中文介绍 Google Doc；id：1aU1-Mpk_6kiKpPRV9nlUrXdHW1rYZ2134s98tTsnsvo；webViewLink：https://docs.google.com/document/d/1aU1-Mpk_6kiKpPRV9nlUrXdHW1rYZ2134s98tTsnsvo/edit

来源：[1](https://docs.google.com/document/d/1aU1-Mpk_6kiKpPRV9nlUrXdHW1rYZ2134s98tTsnsvo/edit)（访问 2026-11-07）

### Drive PDF

id：10Ctq-Va8GHSTojWWiXGYcZGSYJpVTiGN；webViewLink：https://drive.google.com/file/d/10Ctq-Va8GHSTojWWiXGYcZGSYJpVTiGN/view

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

## 变更记录

### 变更记录

- date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- date：2026-11-07；timezone：Asia/Seoul；change：第1轮：打开官方文档核验许可、数据形式和评测协议；复核2026H2证据，区分历史结果与实时榜单；同步中文介绍。

来源：[1](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）
