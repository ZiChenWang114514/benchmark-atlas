# HarmBench

> Benchmark Constitution · 核查日期：2026-11-07（KST / Asia/Seoul）。未知仍保留待核实；访问日不冒充实验日。

HarmBench统一有害行为分类、目标模型回答和成功判定，服务于红队/稳健拒答研究。ASR属于攻击方法、目标模型、行为范围、裁判和预算组成的完整设置，不存在脱离设置的单一安全分数；本页不转载具体有害请求或攻击串。

导读来源：[https://arxiv.org/abs/2402.04249](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

## 1. 基本信息

### 简称

HarmBench

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 全称

HarmBench

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 数据/协议版本

HarmBench 1.0（README 2024-02-26公告）；不能据论文修订号推定新数据版本。

来源：[1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 论文版本

v2；2024-02-27T13:43:08+09:00（KST；论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 发布日期及口径

2024-02-07T03:59:08+09:00（KST；arXiv初稿提交时间，非推定数据首发日）

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 主板块

安全

说明：Benchmark Constitution编辑归档，不是论文指定的唯一领域。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 子领域

- 越狱、拒答与自动红队

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 许可证

MIT（官方仓库LICENSE，2024 centerforaisafety；模型权重及第三方材料须另核条款）。

来源：[1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/LICENSE)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2402.04249

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 代码入口

https://github.com/centerforaisafety/HarmBench

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 数据入口

https://github.com/centerforaisafety/HarmBench

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 官方主页

https://github.com/centerforaisafety/HarmBench

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 论文标题

HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）


## 2. 发起与维护

### 发起团队

作者单位涉及 UIUC、Center for AI Safety、CMU、UC Berkeley、Microsoft 等；不据此推断全部为正式发起方。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 合作及署名机构

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

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

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 维护方

官方代码与反馈由 centerforaisafety/HarmBench 仓库提供；个人持续维护职责及响应时限未核实。

来源：[1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 资助

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）


## 3. 设计目标

### 评测能力

标准化自动红队和稳健拒答评估，比较攻击方法及防御模型。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 设计动机

以往越狱评测在行为集、目标模型、裁判和预算上不统一，容易产生不可复现或夸大的成功率。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）


## 4. 构建方式

### 材料来源

研究团队依据多家提供商安全政策人工整理有害行为，覆盖多种功能场景。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 编制背景

研究者进行安全行为分类与筛选。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 审核流程

去除双重意图/含混行为，关注模型输出相对现有信息带来的差异性危害。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 质量控制

开发专用分类器并进行人类验证；copyright场景另有匹配方法。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 去污染边界

论文要求test行为及test分类器不用于开发攻击或防御，另设validation分类器；这控制评测开发泄漏，不证明目标LLM预训练没有见过公开数据。

来源：[1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）


## 5. 数据形式

### 规模

510 个行为：400 文本、110 多模态；100 验证、410 测试。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 题型

有害行为描述及模型响应评价；本文不转载具体有害请求或攻击串

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 模态

文本及图像条件的多模态行为

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 语言

英语为主，具体子集配置需记录

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 难度

7 个语义类；功能上含200 standard、100 copyright、100 contextual、110 multimodal行为。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 公开及隐藏划分

100 validation用于开发，410 test用于报告；不可优化测试分类器后仍声称独立测试。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）


## 6. 评测方法

### 指标

Attack Success Rate (ASR)，依攻击方法、行为子集、目标模型与预算而定。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 计分

文本/上下文行为用微调Llama-2-13B裁判等专用分类方式；版权类采用相应匹配；不可仅靠非拒答算成功。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 提示与运行设置

原论文目标模型 greedy、最多512输出token；攻击预算和分类器设置也必须固定。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 评测入口

官方scripts/run_pipeline.py及evaluation_pipeline文档；步骤依次为测试用例生成、可选合并、目标模型回答、回答分类。

来源：[1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 可比性边界

没有脱离攻击方法、预算、子集与裁判的“模型安全总分”；ASR越高表示该设置下越易被攻破。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）


## 7. 最新情况

### 核查日

2026-11-07（KST / Asia/Seoul；本轮指定采集日期）

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 已核实版本

version：README最近明确标示HarmBench 1.0，2024-02-26；evidence_2026_h2：- url：https://arxiv.org/html/2609.10594v1；date：2026-09；note：实际比较HarmBench专用分类器与其他越狱裁判，在两个人工标注集上评测。

来源：[1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2024-02-07T03:59:08+09:00；timezone：Asia/Seoul (KST)；- version：v2；submitted_at：2024-02-27T13:43:08+09:00；timezone：Asia/Seoul (KST)

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 饱和情况

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 已知问题

2026-H2 人工标注对照研究专门比较 HarmBench 等裁判可靠性；自动判定不是无偏金标准，需留意误报漏报与攻击家族迁移。

来源：[1](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 衍生关系

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）


## 8. 榜单快照

### 采集日期

2026-11-07（KST / Asia/Seoul；采集日，不代替榜单更新或实验日期）

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 官方结果入口

https://arxiv.org/abs/2402.04249

说明：未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 第三方结果入口

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| 原论文v2表7：test，standard/contextual/copyright，PAIR攻击 | — | Llama 2 7B Chat | 9.4 | ASR %（越低表示该攻击下越稳健） | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07 KST；原始实验日期未单列 |
| 原论文v2表7：test，standard/contextual/copyright，PAIR攻击 | — | GPT-4 0613 | 39.4 | ASR %（越低表示该攻击下越稳健） | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07 KST；原始实验日期未单列 |
| 原论文v2表7：test，standard/contextual/copyright，PAIR攻击 | — | GPT-4 Turbo 1106 | 33.8 | ASR %（越低表示该攻击下越稳健） | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07 KST；原始实验日期未单列 |
| 原论文v2表7：test，standard/contextual/copyright，PAIR攻击 | — | Claude 2 | 4.1 | ASR %（越低表示该攻击下越稳健） | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07 KST；原始实验日期未单列 |
| 原论文v2表7：test，standard/contextual/copyright，PAIR攻击 | — | Claude 2.1 | 2.2 | ASR %（越低表示该攻击下越稳健） | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07 KST；原始实验日期未单列 |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

本轮精确转录同一PAIR攻击、同一test功能类别范围的历史切片；没有给不同攻击预算/模态混合的当前安全总排名。rank=null，不把所列五个模型宣称完整榜单前五。

来源：[1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/centerforaisafety/HarmBench/HEAD/README.md)（访问 2026-11-07）


## 9. 联系方式

### 公开研究联系邮箱

- mantas3@illinois.edu

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 问题反馈

https://github.com/centerforaisafety/HarmBench/issues

说明：公开反馈入口；未发送问题。

来源：[1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md)（访问 2026-11-07）

### 官方账号

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2402.04249)（访问 2026-11-07）

### 隐私政策

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）


## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2402.04249

来源：[1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）

### PDF SHA-256

e6cbcbedbef6aebea3b6fc6c8fd7933546b26cf0a1e65bcf128eea235007c732

说明：本轮下载原始PDF字节的SHA-256；与Drive既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）

### PDF字节数

3233876

来源：[1](https://arxiv.org/pdf/2402.04249)（访问 2026-11-07）

### Drive文件夹

id：1HuxqqbHmEHrlRRRmxfjrOFWFJJfIkNSJ；webViewLink：https://drive.google.com/drive/folders/1HuxqqbHmEHrlRRRmxfjrOFWFJJfIkNSJ

来源：[1](https://drive.google.com/drive/folders/1HuxqqbHmEHrlRRRmxfjrOFWFJJfIkNSJ)（访问 2026-11-07）

### 其他原始材料

- kind：中文介绍 Google Doc；id：10_FfnK2E6j6xSjyxb-1gei2jWsO0PE0gxXPVUoGcbsQ；webViewLink：https://docs.google.com/document/d/10_FfnK2E6j6xSjyxb-1gei2jWsO0PE0gxXPVUoGcbsQ/edit?usp=drivesdk

来源：[1](https://docs.google.com/document/d/10_FfnK2E6j6xSjyxb-1gei2jWsO0PE0gxXPVUoGcbsQ/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF

id：1E8DwWh1UzZ0UNjxcBFNGktI7alwtUFCT；webViewLink：https://drive.google.com/file/d/1E8DwWh1UzZ0UNjxcBFNGktI7alwtUFCT/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1E8DwWh1UzZ0UNjxcBFNGktI7alwtUFCT/view?usp=drivesdk)（访问 2026-11-07）


## 11. 变更记录

### 本页修订

- date：2026-11-07；timezone：Asia/Seoul；change：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- date：2026-11-07；timezone：KST / Asia/Seoul；change：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。
- date：2026-11-07；timezone：Asia/Seoul；change：第二轮q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）

