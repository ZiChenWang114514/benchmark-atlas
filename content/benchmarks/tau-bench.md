# τ-bench

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

τ-bench要求agent在模拟用户、业务政策和数据库工具之间完成服务流程；它的pass^k衡量重复全部成功，不是至少一次成功的pass@k。原仓库现已明确警告任务过时，本页保留原始航空/零售协议历史榜，不偷换成τ³结果。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

## 基本信息

### 简称

τ-bench

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 全称

τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 基准版本

原始retail / airline协议；不与τ²混合

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 论文版本

arXiv v1；提交于 2024-06-18 04:33:08

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 发布日期

2024-06-18 04:33:08

说明：首次 arXiv 论文提交时间，已转；不自动视为数据集首发时间。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 主板块

Agent

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 领域标签

- 工具—Agent—用户交互

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 许可与适用范围

MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2406.12045

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 代码仓库

https://github.com/sierra-research/tau-bench

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 数据地址

https://github.com/sierra-research/tau-bench

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 官方主页

https://github.com/sierra-research/tau-bench

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 论文标题

$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

## 发起与维护

### 机构与发起关系

Sierra

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 合作机构

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 作者

- Shunyu Yao
- Noah Shinn
- Pedram Razavi
- Karthik Narasimhan

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 当前维护方

Sierra Research / tau-bench团队

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 资助与支持

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

## 设计目标

### 衡量能力

与用户多轮交流、调用数据库工具并遵守业务政策，稳定完成现实服务任务。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 设计背景

单轮工具调用或固定计划不能测清楚持续用户交互、政策遵循与重复运行可靠性。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

## 构建方式

### 题目或数据来源

人工设计零售/航空业务政策、Python工具API和JSON数据库；模型辅助生成数据库内容，人工写任务场景。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 出题背景

Sierra研究团队；用户由语言模型模拟，不能称为真实客户对话。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 审核流程

人工场景与多次agent运行迭代验证任务可行性。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 质量控制

以目标数据库终态及必要用户回复子串判断成功，检查无关/禁止变更。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 去污染与泄漏

公开环境与任务可能被后续训练接触；模拟用户随机性不能替代去污染。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

## 数据形式

### 规模

原始retail测试115题、airline测试50题。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 题型

工具—Agent—用户多轮业务交互。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 模态

- 文本对话
- 结构化数据库
- 函数调用

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 语言

英语对话与Markdown政策；Python工具/JSON状态。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 难度

跨政策、用户信息收集与多动作；原论文按领域报告，不假定统一难度配比。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 数据划分

原始数据、工具、政策与评测代码公开；用户目标和金标准终态不展示给agent。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

## 评测方法

### 指标

pass^k（重复k次全成功），也报告平均成功率；与pass@k至少一次成功定义相反。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 评分方式

终态数据库与金标准对比，加所需回复内容检查；不完整审计所有中间行为。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 提示与运行设置

原论文每任务最多30次agent动作；主要结果至少3次试验，agent温度0.0、用户温度1.0。当前README默认gpt-4o用户模拟器，可更换模型及llm/react/verify/reflection策略；二者不得混作同一设置。

来源：[1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-08）；[2](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

### 评测脚本

https://github.com/sierra-research/tau-bench

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 可比性提醒

领域平均与按任务加权均值不同；user模型、次数、pass^k/pass@k及τ²/τ³版本必须区分。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

### 数据版本与更新

本条保留原始τ-bench retail/airline协议。官方README明确警告任务已过时，建议迁移τ³-bench；τ³新增banking与voice并修复retail/airline，不能把其分数改标为原版。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-06-18 04:33:08 "}

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-08）

### 饱和证据与局限

旧仓库可见最高Pass^1为airline 0.460、retail 0.692；最高Pass^4分别0.225、0.462，说明同一系统单次表现与多次可靠性差距明显；旧题已过时，不据此评断τ³能力。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

### 争议与已知问题

官方明确写原仓库任务不再更新且已过时；对外比较须固定旧版commit或使用τ³修订任务，并分开记录。终态一致不保证每个中间行为都遵守政策。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2406.12045)（访问 2026-11-08）

### 衍生或后继基准

τ²-bench后继仓库现已升级为τ³-bench；新增banking领域、voice模态及旧领域修复。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

### 官方榜单入口

https://github.com/sierra-research/tau-bench

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 第三方入口

待核实

说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| 官方README旧版 Airline / Pass^1 | 1 | claude-3-5-sonnet-20241022 | 0.46 | Pass^1 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^2 | 1 | claude-3-5-sonnet-20241022 | 0.326 | Pass^2 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^3 | 1 | claude-3-5-sonnet-20241022 | 0.263 | Pass^3 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^4 | 1 | claude-3-5-sonnet-20241022 | 0.225 | Pass^4 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^1 | 2 | gpt-4o | 0.42 | Pass^1 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^2 | 2 | gpt-4o | 0.273 | Pass^2 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^3 | 2 | gpt-4o | 0.22 | Pass^3 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^4 | 2 | gpt-4o | 0.2 | Pass^4 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^1 | 4 | claude-3-5-sonnet-20240620 | 0.36 | Pass^1 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^2 | 4 | claude-3-5-sonnet-20240620 | 0.224 | Pass^2 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^3 | 4 | claude-3-5-sonnet-20240620 | 0.169 | Pass^3 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^4 | 5 | claude-3-5-sonnet-20240620 | 0.139 | Pass^4 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^1 | 6 | gpt-4o-mini | 0.225 | Pass^1 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^2 | 6 | gpt-4o-mini | 0.14 | Pass^2 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^3 | 6 | gpt-4o-mini | 0.11 | Pass^3 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^4 | 6 | gpt-4o-mini | 0.1 | Pass^4 (0–1) | 原始τ-bench / Airline；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^1 | 3 | gpt-4o | 0.365 | Pass^1 (0–1) | 原始τ-bench / Airline；Act | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^2 | 5 | gpt-4o | 0.217 | Pass^2 (0–1) | 原始τ-bench / Airline；Act | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^3 | 5 | gpt-4o | 0.16 | Pass^3 (0–1) | 原始τ-bench / Airline；Act | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^4 | 4 | gpt-4o | 0.14 | Pass^4 (0–1) | 原始τ-bench / Airline；Act | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^1 | 5 | gpt-4o | 0.325 | Pass^1 (0–1) | 原始τ-bench / Airline；ReAct | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^2 | 3 | gpt-4o | 0.233 | Pass^2 (0–1) | 原始τ-bench / Airline；ReAct | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^3 | 3 | gpt-4o | 0.185 | Pass^3 (0–1) | 原始τ-bench / Airline；ReAct | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Airline / Pass^4 | 3 | gpt-4o | 0.16 | Pass^4 (0–1) | 原始τ-bench / Airline；ReAct | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^1 | 1 | claude-3-5-sonnet-20241022 | 0.692 | Pass^1 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^2 | 1 | claude-3-5-sonnet-20241022 | 0.576 | Pass^2 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^3 | 1 | claude-3-5-sonnet-20241022 | 0.509 | Pass^3 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^4 | 1 | claude-3-5-sonnet-20241022 | 0.462 | Pass^4 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^1 | 3 | gpt-4o | 0.604 | Pass^1 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^2 | 3 | gpt-4o | 0.491 | Pass^2 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^3 | 3 | gpt-4o | 0.43 | Pass^3 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^4 | 3 | gpt-4o | 0.383 | Pass^4 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^1 | 2 | claude-3-5-sonnet-20240620 | 0.626 | Pass^1 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^2 | 2 | claude-3-5-sonnet-20240620 | 0.506 | Pass^2 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^3 | 2 | claude-3-5-sonnet-20240620 | 0.435 | Pass^3 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |
| 官方README旧版 Retail / Pass^4 | 2 | claude-3-5-sonnet-20240620 | 0.387 | Pass^4 (0–1) | 原始τ-bench / Retail；TC | [待核实（README未标该表更新时间）](https://github.com/sierra-research/tau-bench)；采集2026-11-08 |

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

### 榜单覆盖边界

完整转录README所有有数值的9组系统×4个Pass^k共36行；??明确为未知，不补零。各领域和k分轨，策略保留；原版已被官方标记过时，此表不是τ³最新榜。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）

## 联系方式

### 官方公开邮箱

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 公开反馈渠道

https://github.com/sierra-research/tau-bench/issues

说明：公开仓库反馈入口；未发送问题。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）

### 官方社交账号

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

### 联系方式/隐私原则

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2406.12045)（访问 2026-11-07）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2406.12045

来源：[1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-08）

### PDF SHA-256

0ce66a1763d698c61bb311c3c874bf593d1e9a5bfff11bb35f6f72b981f6da56

来源：[1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-08）

### PDF字节数

```json
663224
```

来源：[1](https://arxiv.org/pdf/2406.12045)（访问 2026-11-08）

### 文件夹

来源：[1]( 2026-11-07，）

### 其他文档

说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-07）；[2]( 2026-11-07，）

### 论文原件

来源：[1]( 2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://github.com/sierra-research/tau-bench)（访问 2026-11-08）
