# Legal Research Bench

> 核验：2026-11-07（KST / Asia/Seoul）。官方资料中文改写；待核实不等于未公开。原始数据与第三方实现、历史论文与当前榜单分轨。

编辑状态：研究快照；trending: B；未核实字段保留标记

## 基本信息

### 简称

Legal Research Bench

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 全称

Legal Research Bench

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 领域标签

- 法律
- 搜索

> 编辑标签

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2610.00609

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 官方代码

https://github.com/vals-ai/legal-research-bench

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 数据地址

https://github.com/vals-ai/legal-research-bench

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 官方主页

https://www.vals.ai/benchmarks/legal_research

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 论文标题

Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 发起与维护

### 发起方

Vals AI

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 作者

- Katrina Drozdov
- Oliver Chen
- Langston Nashold
- Rayan Krishnan

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 维护方

Vals AI

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 资助方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 设计目标

### 衡量能力

跨美国联邦及州法，检索法律、判例，判断有效性并综合成有权威支持的法律研究答案。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 设计背景

不能把部分正确或仅能检索当作法律工作可靠；遗漏一个必要要点也可能造成错误。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 构建方式

### 题目来源

执业律师原创的真实工作型研究问题，涉及8类法律业务。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 出题者背景

15位执业律师，平均15年经验，承担出题与复核。

[来源1](https://arxiv.org/abs/2610.00609)（访问 2026-11-07）

### 审核流程

同行律师复核。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 质量控制

GPT-5.4裁判对律师多数票rubric标签一致率87.4%。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 去污染

测试集保持私有防止过拟合；公开示例与可许可验证集分开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 数据形式

### 题量与规模

413题：公开5、可许可验证200、私有测试208。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 题型

开放法律研究，含成文法解释、判例规则应用、监管框架、跨来源调和和时间有效性。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 模态

- 文本
- 检索网页与法律材料

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 语言

美国法，英语。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 难度

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 公开与隐藏划分

官方当前网页成绩仅基于208题Test；论文全413题结果不是同一口径。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 评测方法

### 指标

All-Pass为主；另报rubric加权部分分。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 评分

所有必需rubric项及来源核验通过才算正确；GPT-5.4裁判。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 提示与运行设置

共用harness，3小时/题；case-law搜索、web搜索、retrieve_information、parse_html_page与submit_final_result。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 官方评测脚本

https://github.com/vals-ai/legal-research-bench

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 可比性警示

官网208题实时榜与论文413题历史结果分轨；不能以法律测试分数认证无人监督法律执业。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 当前版本与热度证据

- **version**：待核实
- **heat_confidence**：B
- **why_trending**：主要是单一机构当前展示或厂商持续自评，不代表全行业广泛采纳。
- **evidence_2026_h2**：
  - **url**：https://www.vals.ai/benchmarks/legal_research
  - **date**：2026-11-05
  - **date_type**：source_calendar_date
  - **organization**：Vals AI
  - **note**：已打开当前官方方法与榜单；观察日不冒充发布时间。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 版本与材料差异

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 饱和情况

当前严格All-Pass第一55.77%，未达全题可靠。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 污染与争议

时间锚定、裁判与检索工具依赖；流畅回答不等于法律可靠性。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重口径；具体版本差异仍以官方材料为准。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 为什么近期热门

主要是单一机构当前展示或厂商持续自评，不代表全行业广泛采纳。

- 2026-11-05（source_calendar_date）：已打开当前官方方法与榜单；观察日不冒充发布时间。 [来源](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 官方榜单

https://www.vals.ai/benchmarks/legal_research

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 独立评测覆盖

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：Gemini 4 Carbon
- **score**：55.77
- **metric**：All-Pass (%)，208题Test
- **source_url**：https://www.vals.ai/benchmarks/legal_research
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST
- **result_type**：官方榜单快照
- **rank**：2
- **model**：Muse Spark 1.3 Max
- **score**：55.29
- **metric**：All-Pass (%)，208题Test
- **source_url**：https://www.vals.ai/benchmarks/legal_research
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST
- **result_type**：官方榜单快照
- **rank**：3
- **model**：Claude Opus 5
- **score**：55.29
- **metric**：All-Pass (%)，208题Test
- **source_url**：https://www.vals.ai/benchmarks/legal_research
- **source_date**：2026-11-05
- **collected_at**：2026-11-07 KST
- **result_type**：官方榜单快照

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 覆盖与时效说明

采集日不等于榜单自写更新时间；未知更新时间保留待核实。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

contact@vals.ai（访问许可）；katrina@vals.ai（论文通讯作者）

[来源1](https://arxiv.org/abs/2610.00609)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 官方社交／讨论渠道

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2610.00609

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### 其他文档

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）

### Drive PDF归档

待核实（本轮未上传）

## 变更记录

### 变更记录

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。

[来源1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）
