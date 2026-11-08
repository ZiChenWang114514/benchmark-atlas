# QMOF

> 深度核验：2026-11-08。访问日不等于发布日期或实验运行日；未知保留，不推定“未公开”。

QMOF是金属有机框架与配位聚合物的DFT量子化学数据库，不是由一个名称就能确定统一测试集的排行榜。带隙预测只是其下游任务之一，必须连同数据库版本、DFT层级、结构划分与训练配置读取MAE。维护方v13表、NIST固定任务和2026模型论文三个来源分轨，不能合并排成所谓全局SOTA。

最近复核

## 1. 基本信息

### 简称

QMOF

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 全称

Quantum MOF (QMOF) Database

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 数据版本

官方updates.md最新列出 Figshare v18（加入初步 QMOF Thermo Database）；仓库版本日志不等于本次已核实Figshare全部最新发布。

[1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)（访问 2026-11-07）

### 论文版本

Matter 4,1578–1597 (2021)；20k+版同时引用2022 npj Computational Materials扩展论文。

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 发布时间

官方版本日志：初次数据发布v1为2020-10-28；ChemRxiv页面版本日期2020-10-29。Matter正式发表为2021年，不能把2021误作数据库首次发布年。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/updates.md)（访问 2026-11-08）；[2](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）

### 板块

材料

> 编辑分类沿用入选清单；不代表该基准只测本板块。

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 子领域

```json
[
  "金属有机框架带隙预测"
]
```

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 许可

数据库数据CC BY 4.0；仓库软件LICENSE为MIT。数据与代码授权范围区分。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/LICENSE)（访问 2026-11-08）

### 论文

https://doi.org/10.1016/j.matt.2021.02.015

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 代码

https://github.com/Andrew-S-Rosen/QMOF

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### 数据集

https://doi.org/10.6084/m9.figshare.13147324

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### 官方主页

https://github.com/Andrew-S-Rosen/QMOF

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 论文题名

Machine learning the quantum-chemical properties of metal–organic frameworks for accelerated materials discovery

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

## 2. 发起与维护

### 发起方

Rosen等QMOF研究团队；原始论文作者与作者单位见ChemRxiv/正式文献，数据库长期由Andrew-S-Rosen/QMOF维护。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）；[2](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）

### 合作单位

待核实

> 已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 作者

```json
[
  "Andrew S. Rosen"
  "Shaelyn M. Iyer"
  "Debmalya Ray"
  "Zhenpeng Yao"
  "Alán Aspuru-Guzik"
  "Laura Gagliardi"
  "Justin M. Notestein"
  "Randall Q. Snurr"
]
```

[1](https://www.osti.gov/pages/biblio/1774653)（访问 2026-11-07）

### 维护方

Andrew-S-Rosen/QMOF；Materials Project MOF Explorer为数据浏览入口。

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 资助

原始论文ChemRxiv页面列National Defense Science and Engineering Graduate Fellowship、Nanoporous Materials Genome Center（DE-FG02-17ER16362）；OSTI另列NSF及DOE/BES支持。来源列表不冒充资助比例。

[1](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）；[2](https://www.osti.gov/pages/biblio/1774653)（访问 2026-11-08）

## 3. 设计目标

### 目标能力

从MOF结构预测量子化学性质，本文收录的明确评测任务为固定划分的带隙回归，而非把数据库当统一Agent基准。

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 相对既有评测的缺口

大规模MOF电子结构DFT成本高，需图模型代理进行材料筛选；不同DFT泛函应分开评估。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

## 4. 构建方式

### 题目与标签来源

实验MOF/配位聚合物结构经高通量周期DFT计算产生性质标签；无自然语言命题。

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 出题/标注背景

量子化学、MOF、DFT及图神经网络研究者合作；2022作者机构含Berkeley/LBNL、Northwestern、ORNL、Minnesota。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 审核流程

统一DFT工作流、结构及电子态分析；不是专家逐题审阅考试题。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 质量控制

v9使用pymatgen StructureMatcher移除重复结构并修正186个EDIFF设置；v12移除带错误键合/缺氢问题的部分结构。属于版本化清理，不代表数据无误。

[1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)（访问 2026-11-07）

### 去污染与隔离

H2固定train/val/test评估预测误差；结构重叠与多保真泄漏需单独审计。2022多保真允许同结构不同泛函跨划分，不同于结构外推。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

## 5. 数据形式

### 规模

官方当前概述20,000+结构；H2固定带隙任务16,340训练、2,042验证、2,042测试。初版规模与后续数据库版不同，不能混用。

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 题型

结构→带隙连续值回归；数据库也含其他量子化学性质，但未逐属性拆成独立条目。

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 模态

MOF/配位聚合物原子结构及周期DFT量化学性质；官方FAQ明确不提供轨迹。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### 语言

数值及结构数据；英语说明，无自然语言考试语言。

[1](https://github.com/Andrew-S-Rosen/QMOF)（访问 2026-11-07）

### 难度

电子开壳层过渡金属与不同泛函的带隙差异较难；并无统一题目难度标签。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### 公开/隐藏划分

数据公开；H2 16340/2042/2042固定划分，2022原论文则80/5/15随机划分，两种协议不同。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

## 6. 评测方法

### 指标

带隙MAE，单位eV，越低越好；报告对应DFT层级。

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 判分

对测试结构预测带隙与DFT参考值计算绝对误差平均。

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 提示/推理设置

不是LLM问答提示。ALIGNN 2.0论文Table 2在JARVIS协议下比较固定16340/2042/2042划分；0.202 eV来自improved训练设置，radius消融为0.208 eV，不能统称未改动的base kNN。

[1](https://arxiv.org/pdf/2609.19487)（访问 2026-11-08）

### 官方实现

https://github.com/Andrew-S-Rosen/QMOF

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 可比性边界

QMOF是数据库+下游协议，不存在由数据库名唯一决定的全局榜。PBE带隙不等于实验光学带隙；不同结构/泛函划分不可混排。

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

## 7. 最新情况

### 核验日

2026-11-08

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）

### 本次版本快照

仓库更新日志列至v18；v15—v17各移除一个结构，v18加入初步热力学数据库。发布日期待核实。

[1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)（访问 2026-11-07）

### 论文修订

2026H2 使用证据：ALIGNN 2.0（2026-09-16）表2报告QMOF带隙任务，16,340训练/2042验证/2042测试，ALIGNN 2.0与原ALIGNN的MAE均0.202 eV。

[1](https://arxiv.org/abs/2609.19487)（访问 2026-11-07）

### 饱和情况

H2同协议MAE未改善不代表所有MOF电子性质饱和，也不证明结构外推已解决。

[1](https://arxiv.org/html/2609.19487v1)（访问 2026-11-07）

### 污染/限制/争议

需区分QMOF版本、训练/测试结构及DFT泛函；维护方v13对比和NIST协议不能默认相同。原始2021论文PDFCell/化学预印本下载仍受403限制；仅重开ChemRxiv摘要、仓库、NIST及2026下游论文，未以其他论文冒充原始PDF。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）；[2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）；[4](https://chemrxiv.org/engage/chemrxiv/article-details/60c75162469df46822f449f8)（访问 2026-11-08）

### 衍生与相关版本

v18加入初步QMOF Thermo Database；属于原数据库扩展，本库不据此把每属性重复计作独立benchmark。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/updates.md)（访问 2026-11-08）

## 8. 榜单快照

### 采集日期

2026-11-08 （采集日，不是实验运行日）

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）

### 官方结果入口

https://github.com/Andrew-S-Rosen/QMOF/blob/main/benchmarks.md

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）

### 第三方入口

https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/

[1](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| ALIGNN 2.0作者论文v1 Table 2 / 固定16340-2042-2042 | — | [ALIGNN 2.0 (improved recipe)](https://arxiv.org/pdf/2609.19487) | 0.202 | bandgap test MAE (eV), lower is better | 2026-09-17 |
| ALIGNN 2.0作者论文v1 Table 2 / 固定16340-2042-2042 | — | [ALIGNN (pre-2.0)](https://arxiv.org/pdf/2609.19487) | 0.202 | bandgap test MAE (eV), lower is better | 2026-09-17 |
| ALIGNN 2.0作者论文补充Table S2 / radius消融 | — | [ALIGNN 2.0 (radius graph)](https://arxiv.org/pdf/2609.19487) | 0.208 | bandgap test MAE (eV), lower is better | 2026-09-17 |
| QMOF维护方 / v13 / 80%训练 | — | [Mean of Dataset](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.94 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF维护方 / v13 / 80%训练 | — | [Sine Matrix Eigenspectrum](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.539 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF维护方 / v13 / 80%训练 | — | [Stoichiometric-45](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.459 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF维护方 / v13 / 80%训练 | — | [Stoichiometric-120](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.454 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF维护方 / v13 / 80%训练 | — | [Orbital Field Matrix](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.41 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF维护方 / v13 / 80%训练 | — | [Average SOAP kernel](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.344 | bandgap MAE (eV), lower is better | 未标注 |
| QMOF维护方 / v13 / 80%训练 | — | [CGCNN](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md) | 0.27 | bandgap MAE (eV), lower is better | 未标注 |
| NIST JARVIS / qmof_bandgap / 20424样本 | — | [alignn_model](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/) | 0.2019 | bandgap MAE (eV), lower is better | 01-14-2023 |
| NIST JARVIS / qmof_bandgap / 20424样本 | — | [matminer_rf](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/) | 0.3618 | bandgap MAE (eV), lower is better | 05-22-2023 |
| NIST JARVIS / qmof_bandgap / 20424样本 | — | [matminer_xgboost](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/) | 0.3421 | bandgap MAE (eV), lower is better | 05-22-2023 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://arxiv.org/pdf/2609.19487)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）；[3](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）

### 覆盖与限制

三个独立协议：维护方v13/80%训练7行；NIST JARVIS qmof_bandgap全部3行（MAE精确0.2019、0.3618、0.3421）；2026 ALIGNN 2.0论文主表与消融3行。NIST页面列名虽为ACC，说明明确是带隙MAE，越低越好。不同版本、划分、报告精度不混排；0.2019不得反向改写论文0.202。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/benchmarks.md)（访问 2026-11-08）；[2](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/)（访问 2026-11-08）；[3](https://arxiv.org/pdf/2609.19487)（访问 2026-11-08）

## 9. 联系方式

### 项目公开邮箱

```json
[
  "rosen@u.northwestern.edu"
]
```

[1](https://www.nature.com/articles/s41524-022-00796-6)（访问 2026-11-07）

### GitHub反馈

https://github.com/Andrew-S-Rosen/QMOF/issues

> 官方公开仓库的问题反馈入口；未发送消息。

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-07）

### 官方社交

待核实

> 已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 隐私边界

仅记录官方项目材料明确公开的研究联络方式与Issues，不收集或推断私人资料。

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08）

## 10. 原始文件

### 原始PDF

待核实

> 已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### SHA-256

待核实

> 已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### PDF字节数

待核实

> 已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 文件夹

```json
{
  "id": "16710civVuRQy4imv33HqI4LGvAE8rIGF"
  "webViewLink": "
}
```

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "中文介绍 Google Doc"
    "id": "16w8iieykbWu2_oUxwzSuqlAGEVLfYBHs-ssbWCx-igA"
    "webViewLink": "https://docs.google.com/document/d/16w8iieykbWu2_oUxwzSuqlAGEVLfYBHs-ssbWCx-igA/edit"
  }
]
```

[1](https://docs.google.com/document/d/16w8iieykbWu2_oUxwzSuqlAGEVLfYBHs-ssbWCx-igA/edit)（访问 2026-11-07）

### 论文PDF

待核实

[1](https://doi.org/10.1016/j.matt.2021.02.015)（访问 2026-11-07）

## 11. 变更记录

[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]

[1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)（访问 2026-11-08）
