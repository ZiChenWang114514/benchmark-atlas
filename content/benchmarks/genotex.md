# GenoTEX

> 核查日期：2026-11-07（Asia/Seoul）。事实按字段附来源；论文实验不代表当前排名，待核实不等于未公开。

## 1. 基本信息

### 简称

GenoTEX

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 全称

GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 数据版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 论文版本

v3；最近论文日期 2025-04-08

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 发布日期

2024-06-21（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 子领域

基因表达数据分析

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 许可证

数据集为CC BY 4.0（官方README License节）。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2406.15341

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 代码入口

https://github.com/Liu-Hy/GenoTEX

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 数据入口

https://doi.org/10.34740/kaggle/dsv/11309048

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 官方主页

https://github.com/Liu-Hy/GenoTEX

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 论文标题

GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 2. 发起与维护

### 发起团队

UIUC/Novartis署名作者团队；正式共同发起关系待核实。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 合作与署名机构

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 作者

Liu, Haoyang；Chen, Shuyu；Zhang, Ye；Wang, Haohan

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 维护方

Liu-Hy/GenoTEX官方仓库。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 资助

National AI Research Resource（NAIRR），grant 240283。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md)（访问 2026-11-07）

## 3. 设计目标

### 评测能力

从数据选择、预处理至基因—性状关联的自动化表达分析。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 设计动机

一般代码题缺少完整生物数据筛选及质量控制，与真实研究链条脱节。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 4. 构建方式

### 材料来源

GEO、TCGA/UCSC Xena表达数据，OpenTargets/NCBI Gene等辅助资料。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 编制背景

九名受训生物信息学标注者，约20周构建工作。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 审核流程

每个性状两人独立分析，再由资深审核者复查；共享指南迭代。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 质量控制

统一筛选、选择、预处理及关联参考流程；区分可用与成功预处理数据。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 去污染

依赖公开数据与公共文献；人工参考与任务划分不等于排除基础模型训练暴露。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 5. 数据形式

### 规模

1,384个GTA问题：132个无条件、1,252个有条件；911个输入数据集，152,415个样本，237,907行分析代码。README分别给输入数据41.5 GB及完整下载82.0 GB，二者口径不同。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md)（访问 2026-11-07）

### 题型

数据筛选、选择、预处理和基因—性状关联。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 模态与格式

基因表达矩阵、表型/临床元数据、代码与结果表。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 语言

英语任务/数据元信息和生物标识符；数值组学为主。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 难度

端到端与仅给预处理数据难度不同，应分别报告。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 公开与隐藏划分

数据/参考分析公开；全流程任务与预处理后任务为不同协议，不能合并分数。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 6. 评测方法

### 指标

筛选F1、选择accuracy；预处理AJ/SJ/CSC；关联以AUROC为主，另P/R/F1/GSEA。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 评分流程

与专家参考流程及结果比较；基因发现不是因果生物真理证明。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 提示设置

GenoAgent多代理工作流，模型与已有预处理输入条件需在比较时固定。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 评测入口

eval.py：对selection、preprocessing、analysis三类任务评估；预测目录须与output参考目录格式一致，可按gene/clinical/linked子任务选择。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md)（访问 2026-11-07）

### 可比性边界

论文end-to-end与preprocessed任务不同；不能把0.97与0.74 AUROC当同一榜单提升。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 7. 最新情况

### 核查日期

2026-11-07 Asia/Seoul

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 已核实版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 版本历史及后续引用

2026_H2_evidence：url：https://arxiv.org/html/2610.21074v1；date：2026-10-15；note：OmicsBench §2明确引用 GenoTEX（Liu等2025），将其归为给定数据、单次请求的生物分析基准。；evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。；paper_metadata：title：GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis；authors：Liu, Haoyang；Chen, Shuyu；Zhang, Ye；Wang, Haohan；release：2024-06-21；latest：2025-04-08；version：v3

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 饱和情况

端到端结果仍明显落后人工参考；H2引用不是新的模型实跑。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 已知问题

人工分析本身有方法选择与统计不确定性；公开数据可能训练暴露，参考结果不等同因果真值。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 衍生版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 官方榜单入口

https://github.com/Liu-Hy/GenoTEX

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 第三方榜单

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 结果快照

2025 v3论文历史：GenoAgent+o1端到端AUROC0.74/F1 41.39%；人工参考AUROC0.89；预处理后任务可到0.97但协议不同。o1具体API快照待核实；H2仅被引用。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 覆盖边界

本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）；[2](https://artificialanalysis.ai/)（访问 2026-11-07）；[3](https://epoch.ai/)（访问 2026-11-07）；[4](https://lmarena.ai/)（访问 2026-11-07）

## 9. 联系方式

### 公开邮箱

hl57@illinois.edu；shuyu5@illinois.edu；haohanw@illinois.edu；ye-4.zhang@novartis.com

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 问题反馈

https://github.com/Liu-Hy/GenoTEX/issues

来源：[1](https://github.com/Liu-Hy/GenoTEX)（访问 2026-11-07）

### 官方账号

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 隐私政策

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2406.15341

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### PDF SHA-256

a736e1f4af1ac40df8d1727de6722e005292ffdc20ea002a847ac5114d2ce790

来源：[1](https://arxiv.org/pdf/2406.15341)（访问 2026-11-07）

### PDF字节数

1364730

来源：[1](https://arxiv.org/pdf/2406.15341)（访问 2026-11-07）

### Drive文件夹

id：1fUMNCa76uvA8Rrlhv0dnpnOz5L1LD5Di；webViewLink：https://drive.google.com/drive/folders/1fUMNCa76uvA8Rrlhv0dnpnOz5L1LD5Di

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 其他文档

type：中文介绍 Google Doc；id：1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts；webViewLink：https://docs.google.com/document/d/1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts/edit

来源：[1](https://docs.google.com/document/d/1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts/edit)（访问 2026-11-07）

### Drive PDF

id：14eUzgPi0ENwV5ruQZg9wUciFdtwVURCV；webViewLink：https://drive.google.com/file/d/14eUzgPi0ENwV5ruQZg9wUciFdtwVURCV/view

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 11. 变更记录

### 本页修订

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）
