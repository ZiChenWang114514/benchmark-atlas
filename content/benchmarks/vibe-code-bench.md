# Vibe Code Bench v1.1

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

Vibe Code Bench要求从自然语言规格构建可部署Web应用，用浏览器工作流核验功能而非只测代码片段。本次完整记录125条官网配置；它不测安全与代码质量，也不是从已有应用连续改需求的VCB 1–100。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

## 基本信息

### 简称

Vibe Code Bench v1.1

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 全称

Vibe Code Bench v1.1

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 基准版本

v1.1

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文版本

arXiv v3；提交于 2026-05-14 08:00:10

来源：[1](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

### 发布日期

2026-02-24（v1.1）

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 主板块

代码

说明：编辑归档；跨领域只计主板块。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 领域标签

- 代码

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 许可与适用范围

公开OpenHands scaffold除enterprise/目录外为MIT，enterprise/按其独立许可；官网将benchmark标为Proprietary，测试集许可待核实，不把scaffold MIT外推至题库。

来源：[1](https://github.com/vals-ai/VibeCodeBench-Openhands-Scaffold/blob/main/LICENSE)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2603.04601

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 代码仓库

https://github.com/vals-ai/VibeCodeBench-Openhands-Scaffold

来源：[1](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

### 数据地址

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 官方主页

https://www.vals.ai/benchmarks/vibe-code

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文标题

Vibe Code Bench: Evaluating AI Models on End-to-End Web Application Development

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 发起与维护

### 机构与发起关系

Vals AI

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 合作机构

作者隶属Vals AI及MIT；不据作者隶属推断正式合作协议。

来源：[1](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

### 作者

Hung Tran、Langston Nashold、Rayan Krishnan、Antoine Bigeard、Alex Gu

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）；[2](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

### 当前维护方

Vals AI

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 资助与支持

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 设计目标

### 衡量能力

从自然语言规格零到一构建可部署网页应用，完成认证、数据、支付、邮件等用户流程。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 设计背景

函数生成或已有仓库修bug不足以检验完整应用交付、部署与服务集成。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 构建方式

### 题目或数据来源

LLM生成初稿，PM与软件工程师多轮审查，规格与测试对齐，测试经人工检查。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 出题背景

专业产品经理与软件工程师审查规格；题目初稿由LLM生成，灵感来自咨询案例、自由职业开发任务及创业应用模式。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### 审核流程

产品经理与软件工程师多轮审核应用规格与测试；人工检查需求是否足以支持验证步骤。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 质量控制

每规格多轮PM/工程师审阅；官网称每测试由专业工程师三重验证。论文另做人类对齐研究，模型裁判间子步骤一致率31.8–93.6%，评分器选择影响结果；可用性不等于设计、代码质量或安全审计。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### 去污染与泄漏

验证/测试应用任务互不重叠，运行隔离新浏览器会话并使用唯一账户/数据防工作流状态泄漏；这是评测状态隔离，预训练数据污染审计仍待核实。

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

## 数据形式

### 规模

论文：100应用规格，50验证/50测试；964浏览器工作流、10,131子步骤。当前网页另称每规格20–60测试，与论文6–23工作流口径不一致。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）；[2](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

### 题型

完整应用规格输入；输出可部署应用，浏览器逐步验证。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 模态

- 文本
- 代码
- 网页视觉交互

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 语言

英文自然语言应用规格与UI工作流；生成物涉及Web代码、终端及浏览器视觉交互，不能解读为固定编程语言单元测试。

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### 难度

论文按16模型平均通过率后验分为Easy23、Medium19、Hard8（测试50题）；不是先验专家固定难度标签，新增模型不应重写历史分组。

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### 数据划分

论文摘要称50私有验证/50隐藏测试，表3写Validation(public)；公开性互相矛盾，待确认，不能擅称完整开放。

来源：[1](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

## 评测方法

### 指标

工作流通过率，按应用平均，误差条±1标准误。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 评分方式

浏览器agent执行预写用户工作流；至少90%子步骤成功则该工作流通过；按应用工作流通过比例再对应用平均。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 提示与运行设置

OpenHands改造容器环境，最多5小时或1,000轮；终端、浏览器、自托管Supabase、Stripe测试模式、MailHog。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 评测脚本

https://github.com/vals-ai/VibeCodeBench-Openhands-Scaffold

说明：本地址是公开改造OpenHands scaffold；并不保证私有规格、测试和评分服务全部公开。

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 可比性提醒

网页与论文对技术栈约束、测试数量及验证集公开性描述有冲突，分来源记录；当前v1.1榜单不等于论文早期16模型结果。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 数据版本与更新

```json
{
 "version": "v1.1"
 "evidence_2026_h2": [
 {
 "url": "https://www.vals.ai/benchmarks/vibe-code"
 "date": "2026-11-05"
 "date_type": "source_calendar_date"
 "note": "Vals AI当前方法与榜单实际评测多模型；主要单一机构当前展示，不代表行业广泛采纳。"
 }
 ]
}
```

说明：热度等级沿候选采用；只保留已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文修订记录

- {"version": "v1", "submitted_at": "2026-03-05 06:00:33 "}
- {"version": "v2", "submitted_at": "2026-05-05 12:37:49 "}
- {"version": "v3", "submitted_at": "2026-05-14 08:00:10 "}

来源：[1](https://arxiv.org/abs/2603.04601)（访问 2026-11-08）

### 饱和证据与局限

官网2026-11-05更新的v1.1榜最高92.39%，但逐应用仍有低通过率异常；工作流通过率高不证明完整应用、代码质量、安全全部合格。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 争议与已知问题

arXiv v3摘要/正文称50 private validation，表3又标Validation(public)；公开性矛盾保留。官网v1.1已经125个系统配置，论文16模型为历史，不混为同次实验。

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 衍生或后继基准

VCB 1–100从v1.1已通过应用出发，连续最多10轮需求变更；有50测试/50验证场景，测演进与回归，不是本页从零建应用的替代分数。

来源：[1](https://www.vals.ai/benchmarks/vcb-1-100)（访问 2026-11-08）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 官方榜单入口

https://www.vals.ai/benchmarks/vibe-code

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 第三方入口

https://www.vals.ai/benchmarks/vibe-code

说明：Vals自建基准与独立运行外部基准性质不同；同机构多URL不等于独立复核。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Vals官网v1.1 / OpenHands | 1 | Claude Sonnet 5.5 | 92.39 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 2 | Gemini 4 Argon | 91.91 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 3 | Claude Haiku 5.5 | 90.44 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 4 | Claude Fable 5 | 90.35 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 5 | Claude Opus 5.5 | 90.29 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 6 | Claude Fable 5.1 | 90.26 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 7 | GPT-6 Astra | 89.59 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 8 | Gemini 4 Carbon | 89.06 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 9 | GPT-6.1 Sol | 88.93 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 10 | Claude Opus 5 | 88.4 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 11 | GPT-6 Sol | 87.82 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 12 | DeepSeek V4.1 Flash 1017 | 87.73 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 13 | Grok 4.7 | 86.17 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 14 | Wonder Full | 86.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 15 | Muse Spark 1.3 Max | 85.86 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 16 | MiMo V2.6 Pro | 85.22 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 17 | Kimi K3 | 84.97 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 18 | Kimi K3.1 Pro | 84.89 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 19 | DeepSeek V4.1 Flash | 84.74 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 20 | GPT-6.1 Terra | 84.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 21 | Ember-1 | 83.87 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 22 | Wonder | 83.09 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 23 | Muse Spark 1.3 | 82.86 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 24 | Claude Opus 4.8 | 82.72 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 25 | DeepSeek V4 Pro 0813 | 82.3 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 26 | GPT-6 Luna | 81.65 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 27 | Mistral Large 4 | 81.56 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 28 | Inkling 2 Small | 81.55 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 29 | Claude Sonnet 5 | 81.33 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 30 | Hy4 | 81.01 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 31 | GPT-5.6 Sol | 80.5 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 32 | Muse Spark 1.2 | 79.1 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 33 | MiMo V2.6 Flash | 78.96 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 34 | Gemini 3.8 Flash | 78.65 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 35 | Mistral Large 4 Preview | 78.4 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 36 | GLM 5.3 | 78.13 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Claude Code | 1 | Claude Opus 4.8 | 77.48 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 37 | Hy4 Preview | 77.48 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 38 | Qwen 3.8 Max 0902 | 77.14 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 39 | GPT-5.6 Luna | 77.06 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 40 | Grok 4.6 | 76.24 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 41 | Muse Spark Open | 76.19 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 42 | DeepSeek V4 Flash 0731 | 74.74 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 43 | GPT-5.6 Terra | 74.59 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 44 | MiniMax-M3.1-Flash | 73.94 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 45 | Muse Spark 1.1 | 72.16 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 46 | Claude Opus 4.7 | 71.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 47 | Step 5 Preview | 70.4 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 48 | Gemini 3.7 Flash | 70.39 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 49 | GPT 5.5 | 69.85 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 50 | Grok 4.5 | 69.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 51 | GPT 5.4 (xhigh) | 67.42 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Factory | 1 | GPT 5.5 | 67.39 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 52 | Beam 1.0 | 66.44 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 53 | Qwen 3.8 27B | 64.85 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 54 | Qwen 3.8 Max | 64.7 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 55 | Gemini 3.6 Flash | 64.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 56 | GLM 5.2 | 63.96 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 57 | GPT 5.3 Codex | 61.77 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 58 | Mercury 3 | 60.93 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Codex | 1 | GPT 5.5 | 58.19 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 59 | Claude Opus 4.6 (Nonthinking) | 57.57 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Claude Code | 2 | Claude Sonnet 4.6 | 55.77 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 60 | GPT 5.2 | 53.5 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 60 | Claude Opus 4.6 (Thinking) | 53.5 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 62 | Claude Sonnet 4.6 | 51.48 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 63 | DeepSeek V4 | 49.93 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Cursor CLI | 1 | Composer 2.5 | 49.61 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 64 | Gemini 3.5 Flash | 48.68 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Codex | 2 | GPT 5.4 | 48.47 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 65 | GPT 5.4 Mini | 47.97 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 66 | Qwen 3.7 Max | 47.67 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 67 | MiniMax-M3 | 47.57 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 68 | Kimi K2.7 Code | 47.21 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 69 | Qwen 3.7 Plus | 46.39 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 70 | MiMo V2.5 | 42.17 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 71 | GPT 5.2 Codex | 37.91 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 72 | Kimi K2.6 | 37.89 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 73 | Gemini 3.5 Flash Lite | 37.16 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 74 | MiMo V2.5 Pro | 34.11 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 75 | Gemini 3.1 Pro Preview (02/26) | 32.03 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 76 | GLM 5.1 | 31.46 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 77 | GLM 5.3 Flash | 30.76 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 78 | GPT 5.4 Nano | 26.1 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 79 | Qwen 3.6 Plus | 25.57 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 80 | GPT 5.1 | 24.61 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 81 | GLM 5 | 23.36 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 82 | Claude Sonnet 4.5 (Thinking) | 22.62 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 83 | GPT 5.1 Codex Max | 22.17 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 84 | Claude Opus 4.5 (Thinking) | 20.63 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 85 | Gemini 3 Flash (12/25) | 20.2 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 86 | GPT 5 | 20.09 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 87 | Muse Spark | 19.67 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 88 | Grok 4.3 | 19.4 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 89 | Inkling | 19.21 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 90 | Inkling Small | 19.05 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 91 | Kimi K2.5 | 17.54 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 92 | Qwen 3.5 Plus | 15.74 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 93 | MiniMax-M2.5 | 14.85 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 94 | Gemini 3 Pro (11/25) | 14.3 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 95 | GPT 5 Mini | 14.17 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Grok Build | 1 | Grok Build 0.1 | 13.35 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 96 | GPT 5.1 Codex | 13.12 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 97 | Qwen 3.6 27B | 11.94 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 98 | MiniMax-M2.7 | 11.93 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 99 | Claude Haiku 4.5 (Thinking) | 11.39 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 100 | Laguna M.1 | 11.04 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 101 | Nemotron 3 Ultra | 7.64 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / Devin CLI | 1 | SWE-1.6 Fast | 7.22 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 102 | Laguna XS.2 | 5.21 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 103 | DeepSeek V3.2 (Thinking) | 5.11 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 104 | Grok 4.20 (Reasoning) | 4.06 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 105 | Nemotron 3.5 Super VL | 3.71 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 106 | Mercury 2.5 | 3.68 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 107 | Qwen 3 Max | 3.51 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 108 | Ling 3.0 Flash Fin | 3.4 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 109 | GLM 4.6 | 3.09 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 110 | Ling 3.0 Flash | 2.91 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 111 | Mistral Medium 3.5 | 2.89 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 112 | Grok 4.1 Fast (Reasoning) | 1.2 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 113 | Gemini 2.5 Pro | 0.4 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 114 | Gemini 3.1 Flash Lite Preview | 0.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 114 | Nemotron 3.5 Lightning | 0.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 114 | Grok 4 Fast (Reasoning) | 0.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |
| Vals官网v1.1 / OpenHands | 114 | Mistral Small 4 | 0.0 | workflow accuracy (%) | v1.1 / canonical test set； | [2026-11-05（网页Updated）](https://www.vals.ai/benchmarks/vibe-code)；采集2026-11-08 |

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

### 榜单覆盖边界

完整转录官网125条模型×harness配置，保留原表全榜rank；本页rank按harness分轨重算，不能将不同scaffold当同一基础模型配置。11月5日为网页更新时间，不冒充精确评测运行日期；不混入VCB 1–100的33.98%等后继任务结果。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）

## 联系方式

### 官方公开邮箱

- hung@vals.ai
- langston@vals.ai
- rayan@vals.ai

来源：[1](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### 公开反馈渠道

https://github.com/vals-ai/VibeCodeBench-Openhands-Scaffold/issues

来源：[1](https://github.com/vals-ai/VibeCodeBench-Openhands-Scaffold)（访问 2026-11-08）

### 官方社交账号

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 联系方式/隐私原则

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2603.04601

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### PDF SHA-256

1933eb3da0f6f6b6905903c1c6952238d0347ec6c2f5526f02e5346cac0fbf5f

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### PDF字节数

```json
2556686
```

来源：[1](https://arxiv.org/pdf/2603.04601)（访问 2026-11-08）

### 文件夹

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 其他文档

- {"type": "官方方法或项目页", "url": "https://www.vals.ai/benchmarks/vibe-code", "accessed": "2026-11-07"}

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文原件

待核实

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 变更记录

最近复核
最近复核

来源：[1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-08）
