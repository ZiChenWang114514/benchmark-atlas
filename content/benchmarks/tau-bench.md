# τ-bench

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ/view?usp=drivesdk)

## 基本信息

### 简称

τ-bench

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 全称

τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 基准版本

原始retail / airline协议；不与τ²混合

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 论文版本

arXiv v1

> 论文修订版本不等同数据集版本。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 发布日期

2024-06-18 04:33:08 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 领域标签

- 工具—Agent—用户交互

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 许可证

MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2406.12045

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 官方代码

https://github.com/sierra-research/tau-bench

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 数据地址

https://github.com/sierra-research/tau-bench

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 官方入口

https://github.com/sierra-research/tau-bench

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 论文标题

$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Sierra

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 合作方

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 作者

- Shunyu Yao

- Noah Shinn

- Pedram Razavi

- Karthik Narasimhan

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 当前维护方

Sierra Research / tau-bench团队

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 设计目标

### 衡量能力

与用户多轮交流、调用数据库工具并遵守业务政策，稳定完成现实服务任务。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 设计背景

单轮工具调用或固定计划不能测清楚持续用户交互、政策遵循与重复运行可靠性。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 构建方式

### 题目来源

人工设计零售/航空业务政策、Python工具API和JSON数据库；模型辅助生成数据库内容，人工写任务场景。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 出题者背景

Sierra研究团队；用户由语言模型模拟，不能称为真实客户对话。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 审核流程

人工场景与多次agent运行迭代验证任务可行性。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 质量控制

以目标数据库终态及必要用户回复子串判断成功，检查无关/禁止变更。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 去污染

公开环境与任务可能被后续训练接触；模拟用户随机性不能替代去污染。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 数据形式

### 题量与规模

原始retail测试115题、airline测试50题。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 题型

工具—Agent—用户多轮业务交互。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 模态

- 文本对话

- 结构化数据库

- 函数调用

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 语言

英语对话与Markdown政策；Python工具/JSON状态。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 难度

跨政策、用户信息收集与多动作；原论文按领域报告，不假定统一难度配比。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 公开与隐藏划分

原始数据、工具、政策与评测代码公开；用户目标和金标准终态不展示给agent。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 评测方法

### 指标

pass^k（重复k次全成功），也报告平均成功率；与pass@k至少一次成功定义相反。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 评分

终态数据库与金标准对比，加所需回复内容检查；不完整审计所有中间行为。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 提示与运行设置

当前README默认模拟用户为gpt-4o，可通过user-model及llm/react/verify/reflection策略切换；复现实验应另行固定模拟器和agent策略，不能将当前默认值当作原论文设置。

> 保留原记录所述论文设置作为历史线索：agent温度0、user温度1、gpt-4-0613用户；本轮未重新核验该组论文参数。

[来源1](https://raw.githubusercontent.com/sierra-research/tau-bench/main/README.md)（访问 2026-11-07）

### 官方评测脚本

https://github.com/sierra-research/tau-bench

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 可比性警示

领域平均与按任务加权均值不同；user模型、次数、pass^k/pass@k及τ²/τ³版本必须区分。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **版本**：原始retail / airline协议；不与τ²混合
- **2026H2引用／使用证据**：- **来源URL**：https://arxiv.org/html/2609.27284v1
  - **日期**：2026-09-23
  - **说明**：Hunyuan-A13B §4.2 Agents及表3–4实际报告 τ-bench（BFCL为v3），属于厂商自报评测。

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 论文修订历史

Submission history From: Karthik Narasimhan [ view email ] [v1] 2024-06-18 04:33:08 KST (647 KB)

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 污染与争议

原论文终态奖励不能检查全部中间政策行为；当前官方README另明确原airline/retail任务过时，应迁移至τ³修正版。历史结果和修正版不得直接合并。

[来源1](https://raw.githubusercontent.com/sierra-research/tau-bench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 衍生与版本关系

官方已将τ²仓库升级为τ³：新增banking、voice，并修复airline和retail任务；原τ-bench仓库警告任务已过时且不再更新。本条保留原始协议，不把τ³分数并入。

[来源1](https://raw.githubusercontent.com/sierra-research/tau-bench/main/README.md)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 官方榜单

https://github.com/sierra-research/tau-bench

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 独立评测覆盖

待核实

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 核验结果

- **模型 / Agent**：claude-3-5-sonnet-20241022
- **分数**：0.46
- **指标**：Pass^1（0–1）
- **基准版本**：原始τ-bench Airline
- **设置**：TC / tool-calling
- **结果性质**：采集日官方README历史榜表
- **来源日期**：待核实（榜表未注明更新日期）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：gpt-4o
- **分数**：0.42
- **指标**：Pass^1（0–1）
- **基准版本**：原始τ-bench Airline
- **设置**：TC / tool-calling
- **结果性质**：采集日官方README历史榜表
- **来源日期**：待核实（榜表未注明更新日期）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：claude-3-5-sonnet-20240620
- **分数**：0.36
- **指标**：Pass^1（0–1）
- **基准版本**：原始τ-bench Airline
- **设置**：TC / tool-calling
- **结果性质**：采集日官方README历史榜表
- **来源日期**：待核实（榜表未注明更新日期）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：claude-3-5-sonnet-20241022
- **分数**：0.692
- **指标**：Pass^1（0–1）
- **基准版本**：原始τ-bench Retail
- **设置**：TC / tool-calling
- **结果性质**：采集日官方README历史榜表
- **来源日期**：待核实（榜表未注明更新日期）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：claude-3-5-sonnet-20240620
- **分数**：0.626
- **指标**：Pass^1（0–1）
- **基准版本**：原始τ-bench Retail
- **设置**：TC / tool-calling
- **结果性质**：采集日官方README历史榜表
- **来源日期**：待核实（榜表未注明更新日期）
- **采集日期**：2026-11-07 KST

- **模型 / Agent**：gpt-4o
- **分数**：0.604
- **指标**：Pass^1（0–1）
- **基准版本**：原始τ-bench Retail
- **设置**：TC / tool-calling
- **结果性质**：采集日官方README历史榜表
- **来源日期**：待核实（榜表未注明更新日期）
- **采集日期**：2026-11-07 KST

> 按领域分别摘录前三；榜单行顺序并非始终按分数排序，本条按Pass^1排列。不是τ³当前全榜。此前Hunyuan自报54.7%见H2证据，不能混作同口径排名。

[来源1](https://raw.githubusercontent.com/sierra-research/tau-bench/main/README.md)（访问 2026-11-07）

### 覆盖与时效说明

官方README仍提供原始两个领域历史榜；已核验Hunyuan-A13B报告表3的54.7%，但其聚合口径待核实，故不混入此领域榜快照。

[来源1](https://raw.githubusercontent.com/sierra-research/tau-bench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 公开反馈

https://github.com/sierra-research/tau-bench/issues

> 公开仓库反馈入口；未发送问题。

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2406.12045

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

[来源1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-07）

### 原始PDF SHA-256

0ce66a1763d698c61bb311c3c874bf593d1e9a5bfff11bb35f6f72b981f6da56

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-07）

### 原始PDF字节数

663224

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-07）

### Drive资料文件夹

- **id**：1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2
- **webViewLink**：https://drive.google.com/drive/folders/1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2

[来源1](https://drive.google.com/drive/folders/1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2)（访问 2026-11-07）

### 其他文档

- **type**：中文介绍Google Doc
- **id**：1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ
- **webViewLink**：https://docs.google.com/document/d/1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ/edit?usp=drivesdk

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）；[来源2](https://docs.google.com/document/d/1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ
- **webViewLink**：https://drive.google.com/file/d/1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）
