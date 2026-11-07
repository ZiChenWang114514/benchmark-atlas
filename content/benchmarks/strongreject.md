# StrongREJECT

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1qVDkFDcnFVOGYrw9wE7T7e6myH6wJoor/view?usp=drivesdk)

## 基本信息

### 简称

StrongREJECT

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 全称

StrongREJECT

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 论文版本

arXiv v2

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 发布日期

2024-02-15

> 原始论文首发日期，不保证等同于数据文件首次公开日。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 主板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 领域标签

- 有害请求完成度与拒答评价

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 许可证

MIT（本项目代码）；汇编数据继承来源约束：README注明部分来源无许可，不能把MIT直接套用全部数据。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2402.10260

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方代码

https://github.com/dsbowen/strong_reject

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 数据地址

https://github.com/dsbowen/strong_reject

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方入口

https://strong-reject.readthedocs.io/

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 论文标题

A StrongREJECT for Empty Jailbreaks

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 发起与维护

### 机构与作者单位

UC Berkeley / Center for Human-Compatible AI 相关作者团队。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 正式合作机构

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 作者

- Souly, Alexandra

- Lu, Qingyuan

- Bowen, Dillon

- Trinh, Tu

- Hsieh, Elvis

- Pandey, Sana

- Abbeel, Pieter

- Svegliato, Justin

- Emmons, Scott

- Watkins, Olivia

- Toyer, Sam

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 当前维护方

官方代码与反馈由 dsbowen/strong_reject 仓库提供；个人持续维护职责及响应时限未核实。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 设计目标

### 测量能力

判定越狱输出是否真正提供具体、可信的有害帮助，而不只判断是否拒答。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 既有评测缺口

简单非拒答指标会把空泛、无用或不可信回答错误计为越狱成功。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 构建方式

### 题目来源

从既有越狱数据与系统卡中筛选整理，包括AdvBench、DAN、MasterKey、MaliciousInstruct、HarmfulQ及GPT-4 System Card；按6类危害组织。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 出题与标注背景

研究团队结合人工、GPT-4与pplx-70b-online辅助编写及核实。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 审核

语义去重，检查拒答、回答可能性与提示质量，并人工复核。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 质量控制

以人类标注验证结构化rubric与微调评估器。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 去污染

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 数据形式

### 题量

313 个禁止请求，6 大类别。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 题型

禁止请求与回答完成度评价；不在本页复现危害操作内容

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 难度

关注回答的具体性和说服力，而非仅统计拒答词是否出现。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 公开与隐藏划分

公开提示与评估器；模型裁判验证集与实际目标模型攻击测试不是相同对象。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 评测方法

### 指标

拒答、具体性、说服力的组合分，归一化到0–1；另有评估器与人类的一致性指标。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 评分

拒答时记零；否则结合具体性、说服力；提供rubric评估器与Gemma-2B微调评估器。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 提示与生成设置

按官方评价提示对有害请求及目标回答打分，必须记录裁判模型版本。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 脚本

strong_reject包提供evaluate_dataset；rubric-based LLM evaluator和fine-tuned Gemma 2B evaluator是两个不同实现，报告需明确选择。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 可比性警告

rubric评分、微调评估器分数和二值ASR不同；评估器MAE也不是目标模型的安全分。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

> 2026-H2实际使用证据：2026-09-07：同一H2越狱评估器研究实际研究 StrongREJECT 评分及其可靠性。；2026-09-16：First Token Matters 也明确使用 StrongReject 数据集分析推理模型安全崩塌。

[来源1](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.18471v1)（访问 2026-11-07）

### 数据版本

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://github.com/dsbowen/strong_reject)（访问 2026-11-07）

### 论文修订记录

- **版本**：v1
- **submitted_at**：2024-02-16T03:58:09+09:00
- **时区**：Asia/Seoul (KST)

- **版本**：v2
- **submitted_at**：2024-08-27T12:32:47+09:00
- **时区**：Asia/Seoul (KST)

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 污染与已知问题

README列明若干源数据无license；项目MIT不自动补足来源授权。H2裁判比较使用共享Qwen3.8-27B-Uncensored backbone的rubric版，不能视为原生微调评分器验证。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 衍生评测

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 榜单快照

### 采集日

2026-11-07

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方榜或原始结果入口

https://arxiv.org/abs/2402.10260

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 二级机构榜单

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 可读结果

- **模型 / Agent**：StrongREJECT rubric evaluator
- **分数**：0.077
- **指标**：相对人类标签MAE
- **scope**：原始论文评估器验证，非目标模型安全榜
- **evaluation_date**：2024年原论文，精确日期待核实

- **模型 / Agent**：StrongREJECT finetuned evaluator
- **分数**：0.084
- **指标**：相对人类标签MAE
- **scope**：原始论文评估器验证，非目标模型安全榜
- **evaluation_date**：2024年原论文，精确日期待核实

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 覆盖与时效限制

此处只列原始评估器校验，不能据此排序被攻击模型；未核实当前统一官方实时安全榜。

> 本轮重新打开官方README及H2实证论文；仍未核验到同协议实时全榜，历史论文结果不得称2026当前前三。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）；[来源3](https://arxiv.org/html/2609.18471v1)（访问 2026-11-07）

## 联系方式

### 公开研究联系邮箱

- alexandrasouly@gmail.com

- sdt@berkeley.edu

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 仓库讨论与Issues

https://github.com/dsbowen/strong_reject/issues

> 公开反馈入口；未发送问题。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 官方社交渠道

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2402.10260

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-07）

### 原件SHA-256

10caab98ed5a75b019ef3c8a6697527f83edda067516996d2cb612f02ff746bc

> 原始下载字节SHA-256；未压缩或改写。

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-07）

### 原件字节数

600542

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-07）

### Drive目录

- **id**：1Rjik34iUFEZBTeLqjtMXs8us5Ea3NsvV
- **webViewLink**：https://drive.google.com/drive/folders/1Rjik34iUFEZBTeLqjtMXs8us5Ea3NsvV

[来源1](https://drive.google.com/drive/folders/1Rjik34iUFEZBTeLqjtMXs8us5Ea3NsvV)（访问 2026-11-07）

### 中文介绍

- **kind**：中文介绍 Google Doc
- **id**：15uyExEs5PXDPaRliDItqwcrgvzhdto9GUXOBBbZueIE
- **webViewLink**：https://docs.google.com/document/d/15uyExEs5PXDPaRliDItqwcrgvzhdto9GUXOBBbZueIE/edit?usp=drivesdk

[来源1](https://docs.google.com/document/d/15uyExEs5PXDPaRliDItqwcrgvzhdto9GUXOBBbZueIE/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1qVDkFDcnFVOGYrw9wE7T7e6myH6wJoor
- **webViewLink**：https://drive.google.com/file/d/1qVDkFDcnFVOGYrw9wE7T7e6myH6wJoor/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：Asia/Seoul
- **变更内容**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）；[来源2](https://arxiv.org/pdf/2402.10260)（访问 2026-11-07）
