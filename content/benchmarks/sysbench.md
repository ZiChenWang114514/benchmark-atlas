# SysBench

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

SysBench把“遵守系统消息”拆成约束满足、单条用户指令满足与五轮会话稳定三个层次。数据来自实际系统消息的清洗与人工改写，而不是500道互不相关单轮问答；表中最高CSR不等于最高SSR。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

## 基本信息

### 简称

SysBench

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 全称

SysBench

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 基准版本

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 论文版本

arXiv v2；提交于 2024-10-23 00:07:35

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 发布日期

2024-08-21 00:33:16 （arXiv v1提交；论文日期标示8月20日不含时区）

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 主板块

语言

说明：Benchmark Constitution编辑归档，不是论文指定的唯一领域。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 领域标签

- 系统指令遵循

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 许可与适用范围

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2408.10943

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 代码仓库

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 数据地址

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 官方主页

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 论文标题

SysBench: Can Large Language Models Follow System Messages?

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

## 发起与维护

### 机构与发起关系

论文作者来自北京大学与百川智能等单位；作者单位记录不等于唯一发起机构。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 合作机构

作者单位为北京大学、百川智能；论文列出的单位关系不等于另有未声明的资助或法律合作协议。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 作者

- Qin, Yanzhao
- Zhang, Tao
- Zhang, Tao
- Shen, Yanjun
- Luo, Wenjing
- Sun, Haoze
- Zhang, Yan
- Qiao, Yujing
- Chen, Weipeng
- Zhou, Zenan
- Zhang, Wentao
- Cui, Bin

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 当前维护方

官方公开代码托管于 PKU-Baichuan-MLSystemLab；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-07）

### 资助与支持

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

## 设计目标

### 衡量能力

评估模型遵守系统消息约束，以及多轮交互中的持续性。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 设计背景

常见指令评测主要针对用户消息，无法充分衡量系统指令优先级、多轮依赖和稳定性。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

## 构建方式

### 题目或数据来源

从真实线上日志收集数千条系统消息，经启发式规则与聚类去噪去重；21名经训练标注者选出500条并人工改写。用户对话来自收集与GPT-4o辅助生成，每条保留5轮并按专家指南改写。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 出题背景

21名经训练的数据标注者，专家制定标注指南并进行独立多轮核查。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 审核流程

每个用户指令标注相关约束的checklist；多名专家独立进行多轮检查；GPT-4o按完整系统消息、历史对话及checklist判断各约束是否满足。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 质量控制

论文报告验证器与人工评估一致率超过94%；采用CSR、ISR、SSR三层指标，区分局部满足与五轮整体稳定性。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 去污染与泄漏

构建阶段以启发式规则及聚类去除重复和噪声；这属于库内去重，独立的预训练语料污染审计仍待核实。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

## 数据形式

### 规模

500个含系统消息的对话，每个包含5轮对话；不是500个独立单轮问题。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-07）

### 题型

带系统指令的多轮文本对话

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 模态

文本

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 语言

公开数据包含中文系统消息与中文多轮对话，并含翻译等跨语言要求；论文附录说明展示例为从中文翻译成英语，不能因论文模型分组称English/Chinese就把数据视为完整中英平行版。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench/blob/main/datas/system_benchmark_eval_datas.json)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 难度

约束违反、指令误判、多轮不稳定三个问题，包含依赖或平行对话设置。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 数据划分

公开文件 datas/system_benchmark_eval_datas.json；包含system_prompt、messages与逐轮prompt_infos（alignment和criteria）。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-07）

## 评测方法

### 指标

Constraint Satisfaction Rate (CSR)、Instruction Satisfaction Rate (ISR)、Session Stability Rate (SSR)。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 评分方式

GPT-4o按人工checklist逐项判定：CSR统计约束满足比例，ISR要求同一回复所有相关约束满足，SSR衡量多轮稳定；官方README的指标命令写eval_output，但当前根目录无该文件，复现入口与文档一致性仍需留意。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 提示与运行设置

系统消息与用户轮次必须保持原角色和顺序，记录被测模型的 system-role 支持和模板。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 评测脚本

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-07）

### 可比性提醒

CSR、ISR、SSR 粒度不同；不能将厂商报告中未指定指标的 SysBench 分数默认为三者之一。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-08）

### 数据版本与更新

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-07）

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-08-21 00:33:16 "}
- {"version": "v2", "submitted_at": "2024-10-23 00:07:35 "}

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-08）

### 饱和证据与局限

原论文v2的最高SSR为54.4%（GPT4o），最高CSR为87.1%；指标不同，不能以厂商自报单一SysBench值推断五轮已饱和。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 争议与已知问题

日志来源、GPT-4o生成辅助及GPT-4o验证器可能带来分布与裁判依赖；CSR/ISR/SSR必须分开；README提到的eval_output命令与当前仓库根目录文件存在不一致。

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 衍生或后继基准

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-07）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

### 官方榜单入口

https://arxiv.org/abs/2408.10943

说明：未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-07）

### 第三方入口

https://arxiv.org/html/2609.27284v1

来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| 原论文v2表2 / CSR | 1 | GPT4o | 87.1 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 2 | GPT4o | 76.4 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 1 | GPT4o | 54.4 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 2 | GPT4-Turbo-20240409 | 86.5 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 1 | GPT4-Turbo-20240409 | 76.6 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 2 | GPT4-Turbo-20240409 | 53.2 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 3 | Claude-3-Opus | 85.0 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 3 | Claude-3-Opus | 74.1 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 3 | Claude-3-Opus | 51.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 7 | Llama3.1-70B-Instruct | 76.6 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 8 | Llama3.1-70B-Instruct | 60.3 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 8 | Llama3.1-70B-Instruct | 36.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 10 | Llama3.1-8B-Instruct | 66.5 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 10 | Llama3.1-8B-Instruct | 46.9 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 11 | Llama3.1-8B-Instruct | 24.9 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 12 | Mixtral-8x22B-Instruct | 63.6 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 11 | Mixtral-8x22B-Instruct | 44.4 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 12 | Mixtral-8x22B-Instruct | 22.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 13 | GPT3.5-Turbo-20231106 | 61.6 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 13 | GPT3.5-Turbo-20231106 | 43.2 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 13 | GPT3.5-Turbo-20231106 | 20.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 14 | Mixtral-8x7B-Instruct | 56.5 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 14 | Mixtral-8x7B-Instruct | 37.6 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 15 | Mixtral-8x7B-Instruct | 19.1 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 4 | Qwen2.5-72B-Instruct | 80.4 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 4 | Qwen2.5-72B-Instruct | 66.2 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 4 | Qwen2.5-72B-Instruct | 42.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 6 | GLM-4-0520 | 78.9 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 5 | GLM-4-0520 | 65.5 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 5 | GLM-4-0520 | 41.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 5 | Qwen2-72B-Instruct | 79.0 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 6 | Qwen2-72B-Instruct | 64.1 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 5 | Qwen2-72B-Instruct | 41.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 8 | DeepSeek-V2-0628 | 76.1 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 7 | DeepSeek-V2-0628 | 61.7 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 7 | DeepSeek-V2-0628 | 39.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 9 | Moonshot-V1-8K | 70.3 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 9 | Moonshot-V1-8K | 52.3 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 9 | Moonshot-V1-8K | 30.0 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 11 | GLM-4-9B-Chat | 64.2 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 12 | GLM-4-9B-Chat | 44.0 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 10 | GLM-4-9B-Chat | 25.9 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 15 | ERNIE-4-8K-0613 | 50.7 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 15 | ERNIE-4-8K-0613 | 33.8 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 14 | ERNIE-4-8K-0613 | 20.0 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / CSR | 16 | Qwen2-7B-Instruct | 47.0 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / ISR | 16 | Qwen2-7B-Instruct | 26.9 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 原论文v2表2 / SSR | 16 | Qwen2-7B-Instruct | 15.0 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 （v2提交日，非运行日）](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| 厂商报告表3 / slow-thinking | 1 | Hunyuan-Large-1116 | 82.5 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表3 / slow-thinking | 2 | Qwen2.5-72B-instruct | 77.7 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表3 / slow-thinking | 4 | Qwen3-A22B | 74.2 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表3 / slow-thinking | 3 | Hunyuan-A13B | 76.1 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表4 / fast-thinking | 4 | Hunyuan-Large-1116 | 57.6 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表4 / fast-thinking | 2 | Qwen2.5-72B-instruct | 70.4 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表4 / fast-thinking | 1 | Qwen3-A22B | 72.1 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| 厂商报告表4 / fast-thinking | 3 | Hunyuan-A13B | 70.2 | SysBench（报告原标签，未指定CSR/ISR/SSR） |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

### 榜单覆盖边界

恢复原论文v2表2全部16模型×CSR/ISR/SSR共48行；另列Hunyuan报告表3慢思考与表4快思考8行，自报未注明指标，不混排至CSR、ISR或SSR。官方仓库以论文复现表为主，并非持续更新的实时总榜。

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

## 联系方式

### 官方公开邮箱

- qinyanzhao123@pku.edu.cn

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-07）

### 公开反馈渠道

https://github.com/PKU-Baichuan-MLSystemLab/SysBench/issues

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-07）

### 官方社交账号

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2408.10943)（访问 2026-11-07）

### 联系方式/隐私原则

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2408.10943

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### PDF SHA-256

192a6383d66f9075c26bff148774396da331daad4c69e1dafea9222fc20c10ed

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### PDF字节数

```json
788584
```

来源：[1](https://arxiv.org/pdf/2408.10943)（访问 2026-11-08）

### 文件夹

来源：[1]( 2026-11-07，）

### 其他文档

来源：[1]( 2026-11-07，）

### 论文原件

来源：[1]( 2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（访问 2026-11-08）
