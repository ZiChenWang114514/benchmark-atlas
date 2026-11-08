# SWE-bench Verified

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

SWE-bench Verified 是原始软件修复题经过人工可解性审核后的500题子集，不是新抓取的隐藏测试集。本次找到官网首页内嵌的完整投稿榜，保留系统、agent、release及是否被官方检查；同一模型更换scaffold后的分数不能看成模型本身直接升级。

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）；[2](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-08，）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-08，）

## 基本信息

### 简称

SWE-bench Verified

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 全称

SWE-bench Verified

说明：保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 基准版本

SWE-bench Verified，500题

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 论文版本

arXiv v3；提交于 2024-11-12 08:05:04

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-08，）

### 发布日期

2024-08-13（官方公告日期，未标时间/时区）

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 主板块

代码

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-08，）

### 领域标签

- 仓库级真实软件问题修复

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-08，）

### 许可与适用范围

代码 MIT（当前仓库 LICENSE）；本次原始HF Verified数据卡没有license元数据，数据许可适用范围待核实，不能把代码MIT自动外推到原issue、补丁及第三方软件。

来源：[1](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE)（访问 2026-11-08，）；[2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)（访问 2026-11-08，）

### 论文

https://arxiv.org/abs/2310.06770

说明：2310.06770 是 SWE-bench 母基准论文，Verified 的筛选协议主要见官方公告，不冒称独立 Verified 论文。

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-08，）

### 代码仓库

https://github.com/SWE-bench/SWE-bench

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 数据地址

https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 官方主页

https://www.swebench.com/verified

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 论文标题

SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-08，）

## 发起与维护

### 机构与发起关系

OpenAI 与 SWE-bench 原作者合作发布。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 合作机构

OpenAI（官网明确Verified在人类筛选中与OpenAI合作建立）。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 作者

Verified 公告：Neil Chowdhury、James Aung、Chan Jun Shern、Oliver Jaffe、Dane Sherburn、Giulio Starace 等；母论文作者另见论文元数据。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 当前维护方

SWE-bench 官方团队维护数据与评测框架；OpenAI 提供人工标注和 Verified 公告。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 资助与支持

SWE-bench 官网致谢 Open Philanthropy、AWS、Modal、Andreessen Horowitz、OpenAI、Anthropic 的支持；此列表不是 Verified 专项资金分配表。

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）

## 设计目标

### 衡量能力

理解真实 GitHub issue、定位代码并提交能解决问题且不造成回归的仓库级补丁。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 设计背景

原 SWE-bench 中描述欠明确、测试过窄及环境安装失败可把合理解判错；Verified 筛除这些不公平实例。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

## 构建方式

### 题目或数据来源

来自 12 个开源 Python 仓库的已解决 issue / PR；从原测试集 1,699 个随机标注样本中筛出 500。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 出题背景

93 名具有 Python 经验的专业开发者；先通过 50 道高置信 onboarding 题并获得反馈。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 审核流程

每个样本由 3 名独立标注者评价描述和测试；采用最高严重程度标签，任一严重问题均剔除。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 质量控制

描述/测试严重度 0–3；剔除任一维度 ≥2 或其他重大问题；Docker harness 提高运行稳定性。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 去污染与泄漏

原 issue、仓库与 PR 公开；官方明确承认静态互联网抓取数据可能已进入预训练，人工 Verified 不表示去污染。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

## 数据形式

### 规模

500 题；196 道预估少于 15 分钟的 easy、45 道大于 1 小时的 hard（人工估计，不是模型时限）。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 题型

仓库与问题说明 → 修改文件/代码补丁。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 模态

- 文本
- 代码
- 仓库环境

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 语言

仓库主要为Python；数据卡声明问题文本主要英语，但未按语言过滤或清洗，不保证全部纯英语。

来源：[1](https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified)（访问 2026-11-08，）

### 难度

人工按 <15min、15min–1h、1–4h、>4h 标注；与是否可解筛选分开。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 数据划分

Verified 数据公开；运行时不向 agent 提供 gold patch 和评分测试，公开可得性仍有污染风险。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

## 评测方法

### 指标

Resolved rate：完全解决任务的比例。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 评分方式

补丁可应用且 FAIL_TO_PASS 与 PASS_TO_PASS 两组测试全部通过才算 resolved。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）

### 提示与运行设置

官方Bash Only采用mini-SWE-agent最小ReAct循环。release 1.x支持时temperature=0；2.x及以后不设置temperature；版本记录必须随分数保留。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 评测脚本

当前 v5 CLI：swebench eval verified -p <predictions> --run-id <run_id> -j <workers>；旧 python -m swebench.harness.run_evaluation 仍支持。新补丁复评须使用新 run_id，避免按 run_id/instance_id 缓存旧结果。

来源：[1](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-08，）

### 可比性提醒

完整榜比较任意agent系统，Bash Only才固定mini-SWE-agent；1.x解析输出字符串，2.x用tool calling，官网明确两代结果不一定可比。500题Verified不是完整SWE-bench或SWE-bench Pro。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://www.swebench.com/verified)（访问 2026-11-08，）

### 数据版本与更新

```json
{
  "version": "SWE-bench Verified，500题"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.20804v1"
      "date": "2026-09-17"
      "note": "Harness Design 研究§3.1实际使用500个人工核验GitHub问题，比较不同harness设置；不是同名SWE-Bench Pro Verified。"
    }
  ]
}
```

说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，）；[2](https://www.swebench.com/verified)（访问 2026-11-07，）

### 论文修订记录

- {"version": "v1", "submitted_at": "2023-10-11 01:47:29 ", "timezone": ""}
- {"version": "v2", "submitted_at": "2024-04-06 03:16:29 ", "timezone": ""}
- {"version": "v3", "submitted_at": "2024-11-12 08:05:04 ", "timezone": ""}

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-08，）

### 饱和证据与局限

官网采集快照最高系统结果为79.2%（两条并列）；这是投稿榜可见结果，不是“所有模型已饱和”的证据。

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）

### 争议与已知问题

Verified 是质量筛选而非隐藏新题，且主要覆盖 Python 软件 issue；不能视为一般软件开发或无污染保证。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）；[2](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，）

### 衍生或后继基准

与 SWE-bench Lite、Multimodal、Multilingual 及 SWE-bench Pro 有关系但不同口径，不混排。

来源：[1](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07，）；[2](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）；[2](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-08，）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-08，）

### 官方榜单入口

https://www.swebench.com/?tab=verified

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）

### 第三方入口

待核实

说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| 官方完整系统榜 | 1 | Sonar Foundation Agent + Claude 4.5 Opus | 79.2 | resolved (%) | Verified500；['Model: claude-opus-4-5', 'Org: Sonar', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 1 | live-SWE-agent + Claude 4.5 Opus medium (20251101) | 79.2 | resolved (%) | Verified500；['Model: claude-opus-4-5-20251101', 'Org: UIUC', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 3 | TRAE + Doubao-Seed-Code | 78.8 | resolved (%) | Verified500；['Model: Doubao-Seed-Code', 'Model: Doubao-Seed-1.6', 'Org: ByteDance', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 4 | live-SWE-agent + Gemini 3 Pro Preview (2025-11-18) | 77.4 | resolved (%) | Verified500；['Model: gemini-3-pro-preview', 'Org: UIUC', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 5 | EPAM AI/Run Developer Agent v20250719 + Claude 4 Sonnet | 76.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Org: EPAM Systems, Inc.', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 5 | Atlassian Rovo Dev (2025-09-02) | 76.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Model: gpt-5', 'Org: Atlassian', 'System: Attempts - 2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 1 | Claude 4.5 Opus (high) | 76.8 | resolved (%) | Verified500；['Model: claude-4-5-opus', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 7 | ACoder | 76.4 | resolved (%) | Verified500；['Model: claude-4-sonnet', 'Model: claude-4.1-opus', 'Model: gpt-5-0807-global', 'Model: gemini-2.5-pro-06-17', 'Org: ACoder', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 2 | Gemini 3 Flash (high) | 75.8 | resolved (%) | Verified500；['Model: gemini-3-flash-preview', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 2 | MiniMax M2.5 (high) | 75.8 | resolved (%) | Verified500；['Model: minimax-m2.5', 'Org: Minimax', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 8 | Warp | 75.6 | resolved (%) | Verified500；['Model: gpt-5', 'Model: claude-sonnet-4-20250514', 'Org: Warp', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 4 | Claude 4.6 Opus | 75.6 | resolved (%) | Verified500；['Model: claude-opus-4-6', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 9 | TRAE + Claude Sonnet 4 + Opus 4 + Sonnet 3.7 + Gemini 2.5 Pro | 75.2 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250522', 'Model: claude-4-opus-20250522', 'Model: claude-3-7-sonnet-20250219', 'Model: gemini-2.5-pro-preview-06-05', 'Org: TRAE', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 10 | Harness AI | 74.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Org: Harness', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 10 | Sonar Foundation Agent + Claude 4.5 Sonnet | 74.8 | resolved (%) | Verified500；['Model: claude-sonnet-4-5', 'Org: Sonar', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 12 | Lingxi-v1.5_claude-4-sonnet-20250514 | 74.6 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Lingxi', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 12 | JoyCode + Claude 4 Sonnet + GPT-4.1 | 74.6 | resolved (%) | Verified500；['Model: claude-4-sonnet', 'Model: gpt-4.1', 'Org: JoyCode', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 14 | Refact.ai Agent + Claude 4 Sonnet + o4-mini | 74.4 | resolved (%) | Verified500；['Model: claude-4-sonnet', 'Model: o4-mini', 'Org: Refact.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 14 | Prometheus-v1.2.1 + GPT-5 | 74.4 | resolved (%) | Verified500；['Model: gpt-5-2025-08-07', 'Org: EuniAI', 'Org: Delysium', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.16.0 | 1 | Claude 4.5 Opus (20251101) (medium) | 74.4 | resolved (%) | Verified500；['Model: claude-opus-4-5-20251101', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.16.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.15.0 | 1 | Gemini 3 Pro Preview (2025-11-18) | 74.2 | resolved (%) | Verified500；['Model: gemini-3-pro-preview', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 1.15.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 16 | Salesforce AI Research SAGE (OpenHands) | 73.8 | resolved (%) | Verified500；['Model: claude-sonnet-4.5', 'Model: gpt-5', 'Org: Salesforce AI Research', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 17 | Tools + Claude 4 Opus (2025-05-22) | 73.2 | resolved (%) | Verified500；['Model: claude-4-opus-20250514', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 18 | Salesforce AI Research SAGE (bash-only) | 73.0 | resolved (%) | Verified500；['Model: claude-sonnet-4.5', 'Model: gpt-5', 'Org: Salesforce AI Research', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 5 | GLM 5 (high) | 72.8 | resolved (%) | Verified500；['Model: glm-5', 'Org: Z-AI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 5 | GPT 5.2 (high) | 72.8 | resolved (%) | Verified500；['Model: gpt-5-2', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 5 | GPT 5.2 Codex | 72.8 | resolved (%) | Verified500；['Model: gpt-5-2-codex', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 19 | Tools + Claude 4 Sonnet (2025-05-22) | 72.4 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 20 | OpenHands + GPT-5 | 71.8 | resolved (%) | Verified500；['Model: openai/gpt-5-2025-08-07', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.2 | 1 | GPT 5.2 (2025-12-11) (high) | 71.8 | resolved (%) | Verified500；['Model: gpt-5.2-2025-12-11', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 8 | Claude 4.5 Sonnet (high) | 71.4 | resolved (%) | Verified500；['Model: claude-sonnet-4-5-20250929', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 21 | Bloop | 71.2 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Bloop AI', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 21 | Qodo Command | 71.2 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Model: gpt-4o', 'Org: Qodo', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 21 | Prometheus-v1.2 + GPT-5 | 71.2 | resolved (%) | Verified500；['Model: gpt-5-2025-08-07', 'Org: EuniAI', 'Org: Delysium', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 21 | Lingxi v1.5 x Kimi K2 | 71.2 | resolved (%) | Verified500；['Model: kimi-k2-0905-preview', 'Org: Huawei', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 25 | Warp | 71.0 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Model: claude-3-7-sonnet-20250219', 'Model: gemini-2.5-pro', 'Model: gpt-4.1-2025-04-14', 'Org: Warp', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 26 | Moatless Tools + Claude 4 Sonnet | 70.8 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Moatless AI', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 9 | Kimi K2.5 (high) | 70.8 | resolved (%) | Verified500；['Model: kimi-k2.5', 'Org: Moonshot AI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 27 | TRAE | 70.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.13.3 | 1 | Claude 4.5 Sonnet (20250929) | 70.6 | resolved (%) | Verified500；['Model: claude-sonnet-4-5-20250929', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.13.3'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 28 | Refact.ai Agent | 70.4 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Model: o3', 'Model: o4-mini', 'Org: Refact.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 28 | OpenHands + Claude 4 Sonnet | 70.4 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 28 | Augment Agent v1 | 70.4 | resolved (%) | Verified500；['System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 31 | devlo | 70.2 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Model: o3', 'Model: gemini-2.5-pro', 'Org: devlo', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 32 | Zencoder (2025-04-30) | 70.0 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Model: o4-mini', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 10 | DeepSeek V3.2 (high) | 70.0 | resolved (%) | Verified500；['Model: deepseek-v3.2', 'Org: DeepSeek', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 33 | OpenHands + Qwen3-Coder-480B-A35B-Instruct | 69.6 | resolved (%) | Verified500；['Model: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct', 'Org: Qwen', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 11 | Gemini 3 Pro | 69.6 | resolved (%) | Verified500；['Model: gemini-3-pro-preview', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.2 | 2 | GPT 5.2 (2025-12-11) | 69.0 | resolved (%) | Verified500；['Model: gpt-5.2-2025-12-11', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 34 | Nemotron-CORTEXA | 68.2 | resolved (%) | Verified500；['Model: NV-EmbedCode', 'Model: o3', 'Model: o3-mini', 'Model: o1', 'Model: gpt-4.1', 'Model: gpt-4o-2024-05-13', 'Model: gpt-4-turbo-2024-04-09', 'Model: claude-3-7-sonnet-20250219', 'Model: deepseek-v3', 'Model: Qwen/Qwen2.5-72B-Instruct', 'Model: meta-llama/Llama-3.1-405B-Instruct', 'Model: meta-llama/Llama-3.3-70B-Instruct', 'Org: NVIDIA', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 34 | GLM-4.6 | 68.2 | resolved (%) | Verified500；['Model: https://huggingface.co/zai-org/GLM-4.6', 'Org: Z.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 1 | Claude 4 Opus (20250514) | 67.6 | resolved (%) | Verified500；['Model: claude-4-opus-20250514', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 36 | SWE-agent + Claude 4 Sonnet | 66.6 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 12 | Claude 4.5 Haiku (high) | 66.6 | resolved (%) | Verified500；['Model: claude-haiku-4-5-20251001', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 37 | Aime-coder v1 + Anthopic Claude 3.7 Sonnet | 66.4 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Org: ByteDance DevInfra', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.15.0 | 2 | GPT 5.1 (2025-11-13) (medium) | 66.0 | resolved (%) | Verified500；['Model: gpt-5.1-2025-11-13', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.15.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.16.0 | 2 | GPT 5.1 Codex (medium) | 66.0 | resolved (%) | Verified500；['Model: gpt-5.1-codex', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.16.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 38 | OpenHands | 65.8 | resolved (%) | Verified500；['Org: OpenHands', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 39 | Augment Agent v0 | 65.4 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 39 | Amazon Q Developer Agent (v20250405-dev) | 65.4 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 39 | OpenHands + Kimi K2 | 65.4 | resolved (%) | Verified500；['Model: moonshot/kimi-k2-0711-preview', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.7.0 | 1 | GPT 5 (2025-08-07) (medium) | 65.0 | resolved (%) | Verified500；['Model: gpt-5-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 2 | Claude 4 Sonnet (20250514) | 64.93 | resolved (%) | Verified500；['Model: claude-4-sonnet-20250514', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 42 | W&B Programmer O1 crosscheck5 | 64.6 | resolved (%) | Verified500；['Model: o1-preview', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 42 | PatchPilot-v1.1 | 64.6 | resolved (%) | Verified500；['Model: o4-mini', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 44 | GLM-4.5 | 64.2 | resolved (%) | Verified500；['Model: https://huggingface.co/zai-org/GLM-4.5', 'Org: Z.ai', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 45 | AgentScope | 63.4 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.2 | 3 | Kimi K2 Thinking | 63.4 | resolved (%) | Verified500；['Model: Kimi-K2-Thinking', 'Org: Moonshot AI', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 46 | Tools + Claude 3.7 Sonnet (2025-02-24) | 63.2 | resolved (%) | Verified500；['Org: Anthropic', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 47 | Blackbox AI Agent | 62.8 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 47 | EPAM AI/Run Developer Agent v20250219 + Anthopic Claude 3.5 Sonnet | 62.8 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 49 | SWE-agent + Claude 3.7 Sonnet w/ Review Heavy | 62.4 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Org: SWE-agent', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 50 | CodeStory Midwit Agent + swe-search | 62.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.0 | 1 | MiniMax M2 | 61.0 | resolved (%) | Verified500；['Model: minimax-m2', 'Org: Minimax', 'System: Attempts - 1', 'Mini: 1.17.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 51 | OpenHands + 4x Scaled (2024-02-03) | 60.8 | resolved (%) | Verified500；['Org: OpenHands', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 52 | EntroPO + R2E + Qwen3-Coder-30B-A3B-Instruct | 60.4 | resolved (%) | Verified500；['Model: Qwen3-Coder-30B-A3B-Instruct', 'Org: 42-b3yond-6ug', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 53 | Learn-by-interact | 60.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Google', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.1 | 1 | DeepSeek V3.2 Reasoner | 60.0 | resolved (%) | Verified500；['Model: deepseek-v3.2-reasoner', 'Org: deepseek', 'System: Attempts - 1', 'Mini: 1.17.1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.7.0 | 2 | GPT 5 mini (2025-08-07) (medium) | 59.8 | resolved (%) | Verified500；['Model: gpt-5-mini-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 54 | DeepSWE-Preview + TTS(Bo16) | 58.8 | resolved (%) | Verified500；['Model: https://huggingface.co/agentica-org/DeepSWE-Preview', 'Org: Agentica', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 3 | o3 (2025-04-16) | 58.4 | resolved (%) | Verified500；['Model: o3-20250416', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 55 | devlo | 58.2 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 55 | Nemotron-CORTEXA | 58.2 | resolved (%) | Verified500；['Model: NV-EmbedCode', 'Model: claude-3-5-sonnet-20241022', 'Model: deepseek-v3', 'Model: o3-mini', 'Model: gpt-4o-2024-05-13', 'Model: gpt-4-turbo-2024-04-09', 'Model: Qwen/Qwen2.5-72B-Instruct', 'Model: meta-llama/Llama-3.1-405B-Instruct', 'Model: meta-llama/Llama-3.3-70B-Instruct', 'Org: NVIDIA', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 57 | Emergent E1 (v2024-12-23) | 57.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 58 | Gru(2024-12-08) | 57.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 58 | Artemis Agent v2 (2025-09-24) | 57.0 | resolved (%) | Verified500；['Model: claude-sonnet-4-20250514', 'Org: Turintech', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 60 | SWE-Rizzo | 56.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.2 | 4 | Devstral Small (2512) | 56.4 | resolved (%) | Verified500；['Model: devstral-small-2512', 'Org: mistral', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 2.0.0 | 13 | GPT 5 mini | 56.2 | resolved (%) | Verified500；['Model: gpt-5-mini-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 2.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 61 | EPAM AI/Run Developer Agent v20241212 + Anthopic Claude 3.5 Sonnet | 55.4 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 4 | Qwen3-Coder 480B/A35B Instruct | 55.4 | resolved (%) | Verified500；['Model: Qwen3-Coder-480B-A35B-Instruct', 'Org: Qwen', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.1 | 2 | GLM 4.6 (T=1) | 55.4 | resolved (%) | Verified500；['Model: glm-4.6', 'Org: Z.ai', 'System: Attempts - 1', 'Mini: 1.17.1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 62 | Amazon Q Developer Agent (v20241202-dev) | 55.0 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 63 | devlo | 54.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.9.1 | 1 | GLM 4.5 (2025-08-22) | 54.2 | resolved (%) | Verified500；['Model: GLM-4.5', 'Org: Z.ai', 'System: Attempts - 1', 'Mini: 1.9.1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.17.2 | 5 | Devstral (2512) | 53.8 | resolved (%) | Verified500；['Model: devstral-2512', 'Org: mistral', 'System: Attempts - 1', 'Mini: 1.17.2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 64 | FrogBoss-32B-2510 | 53.6 | resolved (%) | Verified500；['Model: FrogBoss-32B-2510', 'Org: Microsoft', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 5 | Gemini 2.5 Pro (2025-05-06) | 53.6 | resolved (%) | Verified500；['Model: gemini-2.5-pro', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 65 | CodeSweep - SWE-agent - Kimi K2 Instruct | 53.4 | resolved (%) | Verified500；['Model: kimi-k2-instruct', 'Org: CodeSweep Inc.', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 66 | Bracket.sh | 53.2 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 67 | OpenHands + CodeAct v2.1 (claude-3-5-sonnet-20241022) | 53.0 | resolved (%) | Verified500；['Org: OpenHands', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 0.0.0 | 1 | Claude 3.7 Sonnet (20250219) | 52.8 | resolved (%) | Verified500；['Model: claude-3-7-sonnet-20250219', 'Org: Anthropic', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 68 | Google Jules + Gemini 2.0 Flash (v20241212-experimental) | 52.2 | resolved (%) | Verified500；['Org: Google', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 68 | EntroPO + R2E + Qwen3-Coder-30B-A3B-Instruct | 52.2 | resolved (%) | Verified500；['Model: Qwen3-Coder-30B-A3B-Instruct', 'Org: 42-b3yond-6ug', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 70 | Engine Labs (2024-11-25) | 51.8 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Engine Labs', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 71 | AutoCodeRover-v2.1 (Claude-3.5-Sonnet-20241022) | 51.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 71 | OpenHands + Qwen3-Coder-30B-A3B-Instruct | 51.6 | resolved (%) | Verified500；['Model: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct', 'Org: Qwen', 'Org: OpenHands', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 73 | Agentless-1.5 + Claude-3.5 Sonnet (20241022) | 50.8 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: Agentless', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 74 | Solver (2024-10-28) | 50.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 74 | Bytedance MarsCode Agent | 50.0 | resolved (%) | Verified500；['Org: Bytedance', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 76 | nFactorial (2024-11-05) | 49.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 77 | Tools + Claude 3.5 Sonnet (2024-10-22) | 49.0 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: claude-3.5-sonnet-20241022', 'Org: Anthropic', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 78 | Composio SWE-Kit (2024-10-25) | 48.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: o1-mini', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 79 | AppMap Navie v2 | 47.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 80 | Skywork-SWE-32B + TTS(Bo8) | 47.0 | resolved (%) | Verified500；['Model: Qwen2.5-Coder-32B-Instruct', 'Org: Skywork AI', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 81 | OpenHands + DevStral Small 2505 | 46.8 | resolved (%) | Verified500；['Model: mistralai/Devstral-Small-2505', 'Org: OpenHands', 'Org: Mistral', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 82 | Emergent E1 (v2024-10-12) | 46.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 83 | AutoCodeRover-v2.0 (Claude-3.5-Sonnet-20241022) | 46.2 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 84 | PatchPilot + Co-PatcheR | 46.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 85 | Solver (2024-09-12) | 45.4 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 86 | Gru(2024-08-24) | 45.2 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 87 | FrogMini-14B-2510 | 45.0 | resolved (%) | Verified500；['Model: FrogMini-14B-2510', 'Org: Microsoft', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 6 | o4-mini (2025-04-16) | 45.0 | resolved (%) | Verified500；['Model: o4-mini-20250416', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 88 | CodeShellAgent + Gemini 2.0 Flash (Experimental) | 44.2 | resolved (%) | Verified500；['Model: gemini-2.0-flash-exp', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.7.0 | 3 | Kimi K2 Instruct | 43.8 | resolved (%) | Verified500；['Model: Kimi-K2-Instruct', 'Org: Moonshot AI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 89 | Solver (2024-09-12) | 43.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 90 | Agentless Lite + O3 Mini (20250214) | 42.4 | resolved (%) | Verified500；['Model: o3-mini', 'Org: Agentless', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 90 | Amazon Nova Premier 1.0 (2025-04-30) | 42.4 | resolved (%) | Verified500；['Model: amazon.nova-premier-v1:0', 'Org: Amazon Nova', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 92 | DeepSWE-Preview | 42.2 | resolved (%) | Verified500；['Model: https://huggingface.co/agentica-org/DeepSWE-Preview', 'Org: Agentica', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 93 | SWE-Exp | 42.0 | resolved (%) | Verified500；['Model: DeepSeek-V3-0324', 'Org: SWE-Exp', 'System: Attempts - 2'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 94 | nFactorial (2024-10-30) | 41.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: gpt-4o-2024-08-06', 'Model: o1-preview', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 94 | ugaiforge | 41.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 96 | SWE-RL (Llama3-SWE-RL-70B + Agentless Mini) (20250226) | 41.2 | resolved (%) | Verified500；['Model: Llama3-SWE-RL-70B', 'Model_size: 70', 'Org: Agentless', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 97 | Honeycomb | 40.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 97 | Composio SWEkit + Claude 3.5 Sonnet (2024-10-16) | 40.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Model: claude-3.5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 97 | Tools + Claude 3.5 Haiku | 40.6 | resolved (%) | Verified500；['Model: claude-3-haiku-20240307', 'Org: Anthropic', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 97 | Nebius AI Qwen 2.5 72B Generator + LLama 3.1 70B Critic | 40.6 | resolved (%) | Verified500；['Model: Llama 3.1', 'Model: Qwen 2.5', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 101 | SWE-agent + SWE-agent-LM-32B | 40.2 | resolved (%) | Verified500；['Model: Qwen 2.5', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 102 | EPAM AI/Run Developer Agent v20241029 + Anthopic Claude 3.5 Sonnet | 39.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 7 | GPT 4.1 (2025-04-14) | 39.58 | resolved (%) | Verified500；['Model: gpt-4.1-20250414', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 103 | Amazon Q Developer Agent (v20240719-dev) | 38.8 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 103 | Agentless-1.5 + GPT 4o (2024-05-13) | 38.8 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'Org: Agentless', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 105 | AutoCodeRover (v20240620) + GPT 4o (2024-05-13) | 38.4 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 106 | Skywork-SWE-32B | 38.0 | resolved (%) | Verified500；['Model: Qwen2.5-Coder-32B-Instruct', 'Org: Skywork AI', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 106 | SWE-agent + DevStral Small 2507 | 38.0 | resolved (%) | Verified500；['Model: devstral-small-2507', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 108 | Factory Code Droid | 37.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.7.0 | 4 | GPT 5 nano (2025-08-07) (medium) | 34.8 | resolved (%) | Verified500；['Model: gpt-5-nano-2025-08-07', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 109 | SWE-agent + Claude 3.5 Sonnet | 33.6 | resolved (%) | Verified500；['Model: claude-3-5-sonnet-20241022', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 110 | SWE-Fixer (Qwen2.5-7b retriever + Qwen2.5-72b editor) | 32.8 | resolved (%) | Verified500；['Model: Qwen 2.5', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 111 | MASAI + GPT 4o (2024-06-12) | 32.6 | resolved (%) | Verified500；['Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 112 | Artemis Agent v1 (2024-11-20) | 32.0 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 113 | nFactorial (2024-10-07) | 31.6 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 114 | SWE-Fixer (Qwen2.5-7b retriever + Qwen2.5-72b editor) 20241128 | 30.2 | resolved (%) | Verified500；['Model: Qwen 2.5', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 115 | Lingma Agent + Lingma SWE-GPT 72b (v0925) | 28.8 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 8 | Gemini 2.5 Flash (2025-04-17) | 28.73 | resolved (%) | Verified500；['Model: gemini-2.5-flash', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 116 | EPAM AI/Run Developer Agent + GPT4o | 27.0 | resolved (%) | Verified500；['Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 117 | AppMap Navie + GPT 4o (2024-05-13) | 26.2 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.7.0 | 5 | gpt-oss-120b | 26.0 | resolved (%) | Verified500；['Model: gpt-oss-120b', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 1.7.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 118 | nFactorial (2024-10-01) | 25.8 | resolved (%) | Verified500；['System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 119 | Amazon Q Developer Agent (v20240430-dev) | 25.6 | resolved (%) | Verified500；['Org: AWS', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 120 | Lingma Agent + Lingma SWE-GPT 72b (v0918) | 25.0 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 121 | EPAM AI/Run Developer Agent + GPT4o | 24.0 | resolved (%) | Verified500；['Model: gpt-4o-2024-08-06', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 0.0.0 | 2 | GPT 4.1 mini (2025-04-14) | 23.94 | resolved (%) | Verified500；['Model: gpt-4.1-mini-20250414', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 122 | SWE-agent + GPT 4o (2024-05-13) | 23.2 | resolved (%) | Verified500；['Model: gpt-4o-2024-05-13', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 122 | MCTS-Refine-7B | 23.2 | resolved (%) | Verified500；['Model: MCTS-Refine-7B', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 124 | SWE-agent + GPT 4 (1106) | 22.4 | resolved (%) | Verified500；['Model: gpt-4-1106-preview', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 0.0.0 | 3 | GPT 4o (2024-11-20) | 21.62 | resolved (%) | Verified500；['Model: gpt-4o-20241120', 'Org: OpenAI', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 0.0.0 | 4 | Llama 4 Maverick Instruct | 21.04 | resolved (%) | Verified500；['Model: llama-4-maverick-instruct', 'Org: Meta', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 125 | Lingma Agent + Lingma SWE-GPT 7b (v0925) | 18.2 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 126 | SWE-agent + Claude 3 Opus | 15.8 | resolved (%) | Verified500；['Model: claude-3-opus-20240229', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 0.0.0 | 5 | Gemini 2.0 Flash | 13.52 | resolved (%) | Verified500；['Model: gemini-2.0-flash', 'Org: Google DeepMind', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 127 | Lingma Agent + Lingma SWE-GPT 7b (v0918) | 10.2 | resolved (%) | Verified500；['Org: Alibaba', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 0.0.0 | 6 | Llama 4 Scout Instruct | 9.06 | resolved (%) | Verified500；['Model: llama-4-scout-instruct', 'Org: Meta', 'System: Attempts - 1', 'Mini: 0.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方 Bash Only / mini-SWE-agent 1.0.0 | 9 | Qwen2.5-Coder 32B Instruct | 9.0 | resolved (%) | Verified500；['Model: Qwen2.5-Coder-32B-Instruct', 'Org: Qwen', 'System: Attempts - 1', 'Mini: 1.0.0'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 128 | RAG + Claude 3 Opus | 7.0 | resolved (%) | Verified500；['Model: claude-3-opus-20240229', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 129 | RAG + Claude 2 | 4.4 | resolved (%) | Verified500；['Model: claude-2', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 130 | RAG + GPT 4 (1106) | 2.8 | resolved (%) | Verified500；['Model: gpt-4-1106-preview', 'System: Attempts - 2+'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 131 | RAG + SWE-Llama 7B | 1.4 | resolved (%) | Verified500；['Model: SWE-Llama', 'Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 132 | RAG + SWE-Llama 13B | 1.2 | resolved (%) | Verified500；['Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方完整系统榜 | 133 | RAG + ChatGPT 3.5 | 0.4 | resolved (%) | Verified500；['Org: SWE-agent', 'System: Attempts - 1'] | [来源页未列运行日](https://www.swebench.com/)；采集2026-11-08 |
| 官方公告历史基线 | 1 | gpt-4o-2024-05-13 + Agentless | 33.2 | resolved (%) | Verified500； | [2024-08-13](https://openai.com/index/introducing-swe-bench-verified/)；采集2026-11-07 |
| H2 学术实验 | 1 | Nemotron-3 550B / 研究harness | 69.4 | SR (%) | Verified500；T4/128k、planning、bash-only、最多300步、温度0 | [2026-09-17](https://arxiv.org/html/2609.20804v1)；采集2026-11-07 |

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）；[2](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-08，）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-08，）

### 榜单覆盖边界

本次从官网首页公开 leaderboard-data JSON 读取 Verified 全部180条系统结果，而非 /verified 介绍页的空白动态区。按完整系统与 Bash Only release 分轨；checked=false 不等于官方复现实验，不能将投稿系统榜称为固定模型榜。保留两条此前核验的历史实验（沿用原采集日）。

来源：[1](https://www.swebench.com/)（访问 2026-11-08，）；[2](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-08，）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-08，）

## 联系方式

### 官方公开邮箱

- carlosej@princeton.edu
- johnby@stanford.edu

来源：[1](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-08，）

### 公开反馈渠道

https://github.com/SWE-bench/SWE-bench/issues

说明：公开仓库反馈入口；未发送问题。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）

### 官方社交账号

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-07，）

### 联系方式/隐私原则

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2310.06770)（访问 2026-11-07，）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2310.06770

来源：[1](https://arxiv.org/pdf/2310.06770)（访问 2026-11-08，）

### PDF SHA-256

f7e8e1df64129742b8199a21a042734519a823a1dafd6f48f8f3ddcfb48ee296

来源：[1](https://arxiv.org/pdf/2310.06770)（访问 2026-11-08，）

### PDF字节数

```json
4533722
```

来源：[1](https://arxiv.org/pdf/2310.06770)（访问 2026-11-08，）

### 文件夹

```json
{
  "id": "1-YvqNLfMxUXoiTYWqbyPSsbJWrK7H9iL"
  "webViewLink": "
}
```

来源：[1]( 2026-11-07，）

### 其他文档

- {"type": "中文介绍Google Doc", "id": "193rLgS0oSSznAPMtMovoito3n3jfiZIvz4T3WcUxaBQ", "webViewLink": "

说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://www.swebench.com/verified)（访问 2026-11-07，）；[2]( 2026-11-07，）

### 论文原件

```json
{
  "id": "1n47Le3puVRH6y64GwRSgTy41zEGlU32T"
  "webViewLink": "
}
```

来源：[1]( 2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://www.swebench.com/verified)（访问 2026-11-08，）
