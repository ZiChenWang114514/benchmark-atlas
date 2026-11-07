# HarmBench

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1E8DwWh1UzZ0UNjxcBFNGktI7alwtUFCT/view?usp=drivesdk)

## 基本信息

### 简称

HarmBench

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 全称

HarmBench

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 基准版本

HarmBench 1.0（README 2024-02-26公告）；不能据论文修订号推定新数据版本。

[来源1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 论文版本

arXiv v2

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 发布日期

2024-02-06

> 原始论文首发日期，不保证等同于数据文件首次公开日。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 主板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 领域标签

- 越狱、拒答与自动红队

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 许可证

MIT（官方仓库LICENSE，2024 centerforaisafety；模型权重及第三方材料须另核条款）。

[来源1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/LICENSE)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2402.04249

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 官方代码

https://github.com/centerforaisafety/HarmBench

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 数据地址

https://github.com/centerforaisafety/HarmBench

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 官方入口

https://github.com/centerforaisafety/HarmBench

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 论文标题

HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 发起与维护

### 机构与作者单位

作者单位涉及 UIUC、Center for AI Safety、CMU、UC Berkeley、Microsoft 等；不据此推断全部为正式发起方。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 正式合作机构

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 作者

- Mazeika, Mantas

- Phan, Long

- Yin, Xuwang

- Zou, Andy

- Wang, Zifan

- Mu, Norman

- Sakhaee, Elham

- Li, Nathaniel

- Basart, Steven

- Li, Bo

- Forsyth, David

- Hendrycks, Dan

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 当前维护方

官方代码与反馈由 centerforaisafety/HarmBench 仓库提供；个人持续维护职责及响应时限未核实。

[来源1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 设计目标

### 测量能力

标准化自动红队和稳健拒答评估，比较攻击方法及防御模型。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 既有评测缺口

以往越狱评测在行为集、目标模型、裁判和预算上不统一，容易产生不可复现或夸大的成功率。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 构建方式

### 题目来源

研究团队依据多家提供商安全政策人工整理有害行为，覆盖多种功能场景。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 出题与标注背景

研究者进行安全行为分类与筛选。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 审核

去除双重意图/含混行为，关注模型输出相对现有信息带来的差异性危害。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 质量控制

开发专用分类器并进行人类验证；copyright场景另有匹配方法。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 去污染

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 数据形式

### 题量

510 个行为：400 文本、110 多模态；100 验证、410 测试。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 题型

有害行为描述及模型响应评价；本文不转载具体有害请求或攻击串

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 模态

文本及图像条件的多模态行为

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 语言

英语为主，具体子集配置需记录

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 难度

7 个语义类；功能上含200 standard、100 copyright、100 contextual、110 multimodal行为。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 公开与隐藏划分

100 validation用于开发，410 test用于报告；不可优化测试分类器后仍声称独立测试。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 评测方法

### 指标

Attack Success Rate (ASR)，依攻击方法、行为子集、目标模型与预算而定。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 评分

文本/上下文行为用微调Llama-2-13B裁判等专用分类方式；版权类采用相应匹配；不可仅靠非拒答算成功。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 提示与生成设置

原论文目标模型 greedy、最多512输出token；攻击预算和分类器设置也必须固定。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 脚本

官方scripts/run_pipeline.py及evaluation_pipeline文档；步骤依次为测试用例生成、可选合并、目标模型回答、回答分类。

[来源1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 可比性警告

没有脱离攻击方法、预算、子集与裁判的“模型安全总分”；ASR越高表示该设置下越易被攻破。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

> 2026-H2实际使用证据：2026-09-07：An Empirical Measurement of Jailbreaking Evaluators 实际比较 HarmBench 等越狱评估器的行为及可靠性。

[来源1](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 数据版本

- **版本**：README最近明确标示HarmBench 1.0，2024-02-26
- **2026H2引用／使用证据**：- **来源URL**：https://arxiv.org/html/2609.10594v1
  - **日期**：2026-09
  - **说明**：实际比较HarmBench专用分类器与其他越狱裁判，在两个人工标注集上评测。

[来源1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 论文修订记录

- **版本**：v1
- **submitted_at**：2024-02-07T03:59:08+09:00
- **时区**：Asia/Seoul (KST)

- **版本**：v2
- **submitted_at**：2024-02-27T13:43:08+09:00
- **时区**：Asia/Seoul (KST)

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 污染与已知问题

2026-H2 人工标注对照研究专门比较 HarmBench 等裁判可靠性；自动判定不是无偏金标准，需留意误报漏报与攻击家族迁移。

[来源1](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 衍生评测

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 榜单快照

### 采集日

2026-11-07

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 官方榜或原始结果入口

https://arxiv.org/abs/2402.04249

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 二级机构榜单

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 可读结果

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 覆盖与时效限制

未核实当前统一官方实时榜；原始论文的攻击×目标模型矩阵不能压成单一当前模型排名，故不编造榜首。

> 本轮重新打开官方README及H2实证论文；仍未核验到同协议实时全榜，历史论文结果不得称2026当前前三。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

## 联系方式

### 公开研究联系邮箱

- mantas3@illinois.edu

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 仓库讨论与Issues

https://github.com/centerforaisafety/HarmBench/issues

> 公开反馈入口；未发送问题。

[来源1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 官方社交渠道

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2402.04249

[来源1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）

### 原件SHA-256

e6cbcbedbef6aebea3b6fc6c8fd7933546b26cf0a1e65bcf128eea235007c732

> 原始下载字节SHA-256；未压缩或改写。

[来源1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）

### 原件字节数

3233876

[来源1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）

### Drive目录

- **id**：1HuxqqbHmEHrlRRRmxfjrOFWFJJfIkNSJ
- **webViewLink**：https://drive.google.com/drive/folders/1HuxqqbHmEHrlRRRmxfjrOFWFJJfIkNSJ

[来源1](https://drive.google.com/drive/folders/1HuxqqbHmEHrlRRRmxfjrOFWFJJfIkNSJ)（访问 2026-11-07）

### 中文介绍

- **kind**：中文介绍 Google Doc
- **id**：10_FfnK2E6j6xSjyxb-1gei2jWsO0PE0gxXPVUoGcbsQ
- **webViewLink**：https://docs.google.com/document/d/10_FfnK2E6j6xSjyxb-1gei2jWsO0PE0gxXPVUoGcbsQ/edit?usp=drivesdk

[来源1](https://docs.google.com/document/d/10_FfnK2E6j6xSjyxb-1gei2jWsO0PE0gxXPVUoGcbsQ/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1E8DwWh1UzZ0UNjxcBFNGktI7alwtUFCT
- **webViewLink**：https://drive.google.com/file/d/1E8DwWh1UzZ0UNjxcBFNGktI7alwtUFCT/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：Asia/Seoul
- **变更内容**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）；[来源2](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）
