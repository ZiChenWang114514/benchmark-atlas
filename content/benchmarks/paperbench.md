# PaperBench

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk/view?usp=drivesdk)

## 基本信息

### 简称

PaperBench

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 全称

PaperBench

> 保留官方名称，不把论文标题自动扩写为全称。

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 基准版本

原始20篇ICML2024论文套件

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 论文版本

arXiv v3

> 论文修订版本不等同数据集版本。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 发布日期

2025-04-03 00:55:24 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 领域标签

- AI论文复现Agent

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 许可证

MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

[来源1](https://github.com/openai/frontier-evals)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2504.01848

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 官方代码

https://github.com/openai/frontier-evals

> 论文链接openai/preparedness；本次GitHub元数据请求跳转至openai/frontier-evals。仓库根代码许可不自动等同每篇论文及rubric许可。

[来源1](https://github.com/openai/frontier-evals)（访问 2026-11-07）

### 数据地址

https://github.com/openai/frontier-evals/tree/main/project/paperbench/data

> 官方README说明数据由Git-LFS分发；JudgeEval部分材料不可自动再分发。

[来源1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问 2026-11-07）

### 官方入口

https://openai.com/index/paperbench/

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 论文标题

PaperBench: Evaluating AI's Ability to Replicate AI Research

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

OpenAI

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 合作方

被复现ICML论文作者共同制定rubric并签核；不意味着共同维护整个benchmark。

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 作者

- Starace, Giulio

- Jaffe, Oliver

- Sherburn, Dane

- Aung, James

- Chan, Jun Shern

- Maksin, Leon

- Dias, Rachel

- Mays, Evan

- Kinsella, Benjamin

- Thompson, Wyatt

- Heidecke, Johannes

- Glaese, Amelia

- Patwardhan, Tejal

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 当前维护方

OpenAI Preparedness / PaperBench团队

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 设计目标

### 衡量能力

从论文理解贡献、从零开发代码、执行实验并复现现代AI研究。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 设计背景

已有科研代码重跑与孤立ML竞赛不能充分测量端到端从论文重建实验的科研工程能力。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 构建方式

### 题目来源

20篇ICML2024 spotlight/oral论文，覆盖12个主题；另设2篇NeurIPS workshop开发论文和内部holdout。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 出题者背景

OpenAI研究团队与原论文作者共同分解复现目标。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 审核流程

层级rubric与原作者协作，多轮内部审查、澄清addendum，最终作者签核。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 质量控制

8,316个可独立评分叶节点；新VM执行reproduce.sh后裁判评分；另用JudgeEval测裁判。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 去污染

禁止访问原作者仓库与其他复现；论文报告646次尝试中10次违规被取消，不能排除预训练中记忆代码。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 数据形式

### 题量与规模

20篇ICML 2024 Spotlight/Oral论文，共8,316项可独立评分的rubric子任务。

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 题型

长程科研编程与实验执行；提交代码/文件，再按层级rubric检查。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 模态

- 论文文本/图表

- 代码

- 实验数据与输出

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 语言

英语论文与说明；代码语言/框架随论文。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 难度

原论文复现多小时预算；BasicAgent与IterativeAgent、12h/36h条件不同。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 公开与隐藏划分

公开论文、rubric与评测代码，另有开发论文与内部保留集；正式20篇不可和开发集混合。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 评测方法

### 指标

Replication Score：叶节点二元判定后按层级权重聚合，再对论文平均。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 评分

三阶段：agent在容器编写代码；独立带GPU容器复现执行；第三容器按论文rubric评分。Code-Dev跳过复现，只评代码开发要求，不可与完整PaperBench分数直比。

[来源1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问 2026-11-07）

### 提示与运行设置

原论文自动裁判o3-mini-2025-01-31 high；不同agent scaffold、工具和实验预算分别记录。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 官方评测脚本

https://github.com/openai/preparedness

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 可比性警示

BasicAgent21%与IterativeAgent24–26%并非仅模型能力变化；CodeDev、预算、judge版本、标准误和论文子集必须注明。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **版本**：原始20篇ICML2024论文套件
- **2026H2引用／使用证据**：- **来源URL**：https://arxiv.org/html/2609.19134v1
  - **日期**：2026-09-16
  - **说明**：ScienceIDE §4.1及参考文献明确引用 PaperBench，讨论以已有研究结果复现为目标的评价；为H2学术引用。

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

[来源1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 论文修订历史

Submission history From: James Aung [ view email ] [v1] 2025-04-03 00:55:24 KST (4,982 KB) [v2] 2025-04-04 21:44:57 KST (4,982 KB) [v3] 2025-04-07 21:15:49 KST (4,982 KB)

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 污染与争议

官网介绍最佳测试agent为Claude 3.5 Sonnet (New) 21.0%；README同时列出IterativeAgent o1-high 36h的26.0%与24h的24.4%。预算和脚手架不同，保留各自证据，不互相覆盖。

[来源1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问 2026-11-07）；[来源2](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 衍生与版本关系

PaperBench Code-Dev省略运行，是独立口径；JudgeEval评价裁判，不当作更多论文复现题计数。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 官方榜单

https://github.com/openai/frontier-evals/tree/main/project/paperbench

[来源1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问 2026-11-07）

### 独立评测覆盖

待核实

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）

### 核验结果

- **模型 / Agent**：IterativeAgent o1-high
- **分数**：26.0
- **指标**：PaperBench replication score (%)
- **运行次数**：3
- **来源日期**：2025-04-02
- **采集日期**：2026-11-07 KST
- **结果性质**：官方README历史结果（非2026新实验）
- **设置**：36h limit；±0.3

- **模型 / Agent**：IterativeAgent o1-high
- **分数**：24.4
- **指标**：PaperBench replication score (%)
- **运行次数**：3
- **来源日期**：2025-04-02
- **采集日期**：2026-11-07 KST
- **结果性质**：官方README历史结果（非2026新实验）
- **设置**：24h limit；±0.7

- **模型 / Agent**：BasicAgent claude-3.5-sonnet
- **分数**：21.0
- **指标**：PaperBench replication score (%)
- **运行次数**：3
- **来源日期**：2025-04-02
- **采集日期**：2026-11-07 KST
- **结果性质**：官方README历史结果（非2026新实验）
- **设置**：BasicAgent；±0.8

> 官方当前可读榜表的前三行；不同预算/脚手架不作同条件排名。官网介绍最佳21.0%对应当时测得的BasicAgent，不否认README后续列出的26.0%。

[来源1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问 2026-11-07）

### 覆盖与时效说明

所有结果为原论文设置的历史实验，不冒称2026当前SOTA；H2 ScienceIDE引用PaperBench作科学研究复现先行基准，没有在其上实跑。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 公开反馈

https://github.com/openai/frontier-evals/issues

[来源1](https://github.com/openai/frontier-evals)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2504.01848)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2504.01848

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

[来源1](https://arxiv.org/pdf/2504.01848)（访问 2026-11-07）

### 原始PDF SHA-256

2f58f1a6581af9d99432422dccf3cf61f5c263377c1e4550e7333c4a22d7184d

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2504.01848)（访问 2026-11-07）

### 原始PDF字节数

1703363

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2504.01848)（访问 2026-11-07）

### Drive资料文件夹

- **id**：1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c
- **webViewLink**：https://drive.google.com/drive/folders/1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c

[来源1](https://drive.google.com/drive/folders/1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c)（访问 2026-11-07）

### 其他文档

- **type**：中文介绍Google Doc
- **id**：1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE
- **webViewLink**：https://docs.google.com/document/d/1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE/edit?usp=drivesdk

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）；[来源2](https://docs.google.com/document/d/1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk
- **webViewLink**：https://drive.google.com/file/d/1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://openai.com/index/paperbench/)（访问 2026-11-07）
