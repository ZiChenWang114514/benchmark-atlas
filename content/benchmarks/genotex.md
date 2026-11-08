# GenoTEX

> Benchmark Constitution，核查日期：2026-11-07。未知仍保留待核实；访问日不冒充实验日。

GenoTEX把基因表达分析拆成数据选择、预处理和基因—性状关联，核心考察从原始数据执行完整分析，而非只回答生物知识题。阅读结果时首先区分端到端输入和专家预处理输入：两者的AUROC不能合并为同一榜单。

导读来源：[https://arxiv.org/abs/2406.15341](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

## 1. 基本信息

### 简称

GenoTEX

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 全称

GenoTEX: An LLM Agent Benchmark for Automated Gene Expression Data Analysis

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 数据/协议版本

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 论文版本

v3；2025-04-09（论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 发布日期及口径

2024-06-22（arXiv初稿提交时间，非推定数据首发日）

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 主板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 子领域

- 基因表达数据分析

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

https://huggingface.co/datasets/Liu-Hy/GenoTEX

说明：官方README同时提供Kaggle DOI；HF为完整代码+数据捆绑分发，非新增benchmark。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/HEAD/README.md)（访问 2026-11-07）；[2](https://huggingface.co/datasets/Liu-Hy/GenoTEX/raw/main/README.md)（访问 2026-11-07）

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

### 合作及署名机构

论文署名单位为University of Illinois Urbana-Champaign与Novartis；仅记录作者单位，不推定正式合作合同或共同所有权。

来源：[1](https://arxiv.org/pdf/2406.15341)（访问 2026-11-07）

### 作者

- Liu, Haoyang
- Chen, Shuyu
- Zhang, Ye
- Wang, Haohan

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

### 去污染边界

依赖公开数据与公共文献；人工参考与任务划分不等于排除基础模型训练暴露。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）


## 5. 数据形式

### 规模

1,384个GTA问题：132个无条件、1,252个有条件；911个输入数据集，152,415个样本，237,907行分析代码。README分别给输入数据41.5 GB及完整下载82.0 GB，二者口径不同。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md)（访问 2026-11-07）

### 题型

数据筛选、选择、预处理和基因—性状关联。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 模态

基因表达矩阵、表型/临床元数据、代码与结果表。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 语言

英语任务/数据元信息和生物标识符；数值组学为主。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 难度

端到端与仅给预处理数据难度不同，应分别报告。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 公开及隐藏划分

数据/参考分析公开；全流程任务与预处理后任务为不同协议，不能合并分数。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）


## 6. 评测方法

### 指标

筛选F1、选择accuracy；预处理AJ/SJ/CSC；关联以AUROC为主，另P/R/F1/GSEA。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 计分

与专家参考流程及结果比较；基因发现不是因果生物真理证明。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 提示与运行设置

GenoAgent多代理工作流，模型与已有预处理输入条件需在比较时固定。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 评测入口

eval.py：对selection、preprocessing、analysis三类任务评估；预测目录须与output参考目录格式一致，可按gene/clinical/linked子任务选择。

来源：[1](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/main/README.md)（访问 2026-11-07）

### 可比性边界

论文end-to-end与preprocessed任务不同；不能把0.97与0.74 AUROC当同一榜单提升。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）


## 7. 最新情况

### 核查日

2026-11-07（指定采集日期）

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 已核实版本

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2024-06-22；timezone：；- version：v2；submitted_at：2025-03-28；timezone：；- version：v3；submitted_at：2025-04-09；timezone：；2026_H2_evidence：- url：https://arxiv.org/html/2610.21074v1；date：2026-10-15；note：OmicsBench §2明确引用 GenoTEX（Liu等2025），将其归为给定数据、单次请求的生物分析基准。；evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 饱和情况

端到端结果仍明显落后人工参考；H2引用不是新的模型实跑。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 已知问题

人工分析本身有方法选择与统计不确定性；公开数据可能训练暴露，参考结果不等同因果真值。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 衍生关系

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）


## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不代替榜单更新或实验日期）

来源：[1](https://github.com/Liu-Hy/GenoTEX)（访问 2026-11-07）

### 官方结果入口

https://github.com/Liu-Hy/GenoTEX

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 第三方结果入口

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| 论文v3表2：端到端，从原始数据开始 | — | GenoAgent + OpenAI o1 | 0.74 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表2：端到端，从原始数据开始 | — | GenoAgent + Claude 3.5 Sonnet | 0.71 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表2：端到端，从原始数据开始 | — | GenoAgent + OpenAI o3-mini | 0.7 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表2：端到端，从原始数据开始 | — | GenoAgent + DeepSeek R1 | 0.7 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表3：给定专家预处理数据 | — | GenoAgent | 0.97 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表3：给定专家预处理数据 | — | Data Interpreter | 0.95 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表3：给定专家预处理数据 | — | MetaGPT | 0.95 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |
| 论文v3表3：给定专家预处理数据 | — | CodeAct | 0.92 | GTA AUROC | [原始来源](https://arxiv.org/pdf/2406.15341)；采集2026-11-07；2025-04-09 （论文修订） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

表2与表3为不同输入条件的历史实验；已复核PDF全部所列行，但未得到可核验实时总榜。rank=null表示未给跨模型实时名次；模型API快照仍待核实。

来源：[1](https://arxiv.org/pdf/2406.15341)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/Liu-Hy/GenoTEX/HEAD/README.md)（访问 2026-11-07）


## 9. 联系方式

### 公开研究联系邮箱

- hl57@illinois.edu
- shuyu5@illinois.edu
- haohanw@illinois.edu
- ye-4.zhang@novartis.com

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 问题反馈

https://github.com/Liu-Hy/GenoTEX/issues

来源：[1](https://github.com/Liu-Hy/GenoTEX)（访问 2026-11-07）

### 官方账号

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 隐私政策

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）


## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2406.15341

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### PDF SHA-256

a736e1f4af1ac40df8d1727de6722e005292ffdc20ea002a847ac5114d2ce790

说明：下载原始PDF字节的SHA-256；与既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/2406.15341)（访问 2026-11-07）

### PDF字节数

1364730

来源：[1](https://arxiv.org/pdf/2406.15341)（访问 2026-11-07）

### 文件夹

id：1fUMNCa76uvA8Rrlhv0dnpnOz5L1LD5Di；webViewLink：

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）

### 其他原始材料

- type：中文介绍；id：1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts；webViewLink：https://docs.google.com/document/d/1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts/edit

来源：[1](https://docs.google.com/document/d/1ytmVpfPLMKgIITCThNPm9Th1b0Pmak9cbUuReO3Kyts/edit)（访问 2026-11-07）

### PDF

id：14eUzgPi0ENwV5ruQZg9wUciFdtwVURCV；webViewLink：

来源：[1](https://arxiv.org/abs/2406.15341)（访问 2026-11-07）


## 11. 变更记录

### 本页修订

- date：2026-11-07；timezone：；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- date：2026-11-07；timezone：；change：深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）

