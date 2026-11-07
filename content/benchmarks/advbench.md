# AdvBench

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1YwG_SH_yRnyhuf_FPfhBigJl5Y4HfdYq/view?usp=drivesdk)

## 基本信息

### 简称

AdvBench

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 全称

AdvBench

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 论文版本

arXiv v2

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 发布日期

2023-07-27

> 原始论文首发日期，不保证等同于数据文件首次公开日。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 主板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 领域标签

- 有害请求与越狱

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 许可证

MIT（llm-attacks仓库软件与文档；数据/第三方材料适用范围须按制品核查）。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2307.15043

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 官方代码

https://github.com/llm-attacks/llm-attacks

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 数据地址

https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 官方入口

https://llm-attacks.org/

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 论文标题

Universal and Transferable Adversarial Attacks on Aligned Language Models

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## 发起与维护

### 机构与作者单位

作者来自 CMU、Center for AI Safety、Google DeepMind、Bosch Center for AI 等单位；正式发起关系不作推断。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 正式合作机构

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 作者

- Zou, Andy

- Wang, Zifan

- Carlini, Nicholas

- Nasr, Milad

- Kolter, J. Zico

- Fredrikson, Matt

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 当前维护方

官方代码与反馈由 llm-attacks/llm-attacks 仓库提供；个人持续维护职责及响应时限未核实。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

### 资助

论文致谢列出 DARPA/AFRL FA8750-15-2-0277、Army MURI W911NF-21-1-0317、NSF CNS1943016 等支持。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## 设计目标

### 测量能力

评价对齐语言模型在有害行为及指定字符串上的对抗鲁棒性。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 既有评测缺口

仅人工探索越狱难以系统比较可优化攻击及跨模型转移性，需要统一行为与目标字符串。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## 构建方式

### 题目来源

作者人工种子示例配合Wizard-Vicuna-30B-Uncensored生成；论文区分有害字符串与有害行为。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 出题与标注背景

研究团队提供人工种子并筛选生成结果；不是安全专家逐条原创全部条目。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 审核

作者筛选生成请求，统一行为格式；完整逐条审核记录待核实。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 质量控制

原论文与公开CSV规模存在差异，本条保留二者并固定来源；后续研究指出单看非拒答可能高估攻击效果。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 去污染

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## 数据形式

### 题量

原论文描述500条有害字符串、500条有害行为；采集日官方 harmful_behaviors.csv 实测520条数据行（不含表头）。这是不同版本/制品，不能默默统一为500或520。

> CSV使用Python csv.DictReader计数，仅计算数据行，不含表头；本次未修改原文件。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv)（访问 2026-11-07）

### 题型

有害行为请求和目标字符串；此介绍不转载具体攻击后缀或危害步骤

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 难度

评测面向对抗攻击成功与迁移；难度受目标模型及攻击预算影响。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 公开与隐藏划分

仓库公开行为/字符串CSV；未核实独立隐藏测试划分。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## 评测方法

### 指标

攻击成功率（ASR）；有害字符串匹配和行为合规需分别定义。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 评分

指定字符串可用精确匹配；行为评估依原论文及后续裁判选择而变，简单无拒答不保证提供有害帮助。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 提示与生成设置

固定攻击、目标模型快照、提示模板及生成预算；不把不同研究的裁判混作统一协议。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 脚本

https://github.com/llm-attacks/llm-attacks

[来源1](https://github.com/llm-attacks/llm-attacks)（访问 2026-11-07）

### 可比性警告

520行为公开CSV不等于原论文500行为实验；GCG是一种攻击算法，不是AdvBench的别名。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

> 2026-H2实际使用证据：2026-09-16：First Token Matters §2–3明确使用 AdvBench 分析推理模型的拒答与首token安全失效。

[来源1](https://arxiv.org/html/2609.18471v1)（访问 2026-11-07）

### 数据版本

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench)（访问 2026-11-07）

### 论文修订记录

- **版本**：v1
- **submitted_at**：2023-07-28T02:49:12+09:00
- **时区**：Asia/Seoul (KST)

- **版本**：v2
- **submitted_at**：2023-12-21T05:48:57+09:00
- **时区**：Asia/Seoul (KST)

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 污染与已知问题

规模冲突已并列：原论文500行为，官方CSV当前520行。StrongREJECT指出非拒答不代表有效有害回答，因此不同ASR裁判的结果不可直比。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv)（访问 2026-11-07）

### 衍生评测

官方2024-08-01公告发布nanoGCG作为更易用的GCG算法实现；这是攻击实现更新，不等于AdvBench数据新版本。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

## 榜单快照

### 采集日

2026-11-07

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 官方榜或原始结果入口

https://arxiv.org/abs/2307.15043

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 二级机构榜单

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 可读结果

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 覆盖与时效限制

未核实当前统一官方实时榜；H2论文明确使用AdvBench，但协议和裁判各异，本页不把单篇攻击实验冒充通用安全排名。

> 本轮重新打开官方README及H2实证论文；仍未核验到同协议实时全榜，历史论文结果不得称2026当前前三。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.18471v1)（访问 2026-11-07）

## 联系方式

### 公开研究联系邮箱

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 仓库讨论与Issues

https://github.com/llm-attacks/llm-attacks/issues

> 公开反馈入口；未发送问题。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

### 官方社交渠道

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2307.15043

[来源1](https://arxiv.org/pdf/2307.15043)（访问 2026-11-07）

### 原件SHA-256

ab8745c2e3c6dfd939d5a590760bbae4682d92db010947cbb306688ad086bfd1

> 原始下载字节SHA-256；未压缩或改写。

[来源1](https://arxiv.org/pdf/2307.15043)（访问 2026-11-07）

### 原件字节数

4656473

[来源1](https://arxiv.org/pdf/2307.15043)（访问 2026-11-07）

### Drive目录

- **id**：1k-z-nsz7sl4QiHxcjWQM2qSTeFtVv3_x
- **webViewLink**：https://drive.google.com/drive/folders/1k-z-nsz7sl4QiHxcjWQM2qSTeFtVv3_x

[来源1](https://drive.google.com/drive/folders/1k-z-nsz7sl4QiHxcjWQM2qSTeFtVv3_x)（访问 2026-11-07）

### 中文介绍

- **kind**：中文介绍 Google Doc
- **id**：1PyuJWY7qpUtChUoPScosfR0eqX-dPCaFCbHwLi2atC8
- **webViewLink**：https://docs.google.com/document/d/1PyuJWY7qpUtChUoPScosfR0eqX-dPCaFCbHwLi2atC8/edit?usp=drivesdk

[来源1](https://docs.google.com/document/d/1PyuJWY7qpUtChUoPScosfR0eqX-dPCaFCbHwLi2atC8/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1YwG_SH_yRnyhuf_FPfhBigJl5Y4HfdYq
- **webViewLink**：https://drive.google.com/file/d/1YwG_SH_yRnyhuf_FPfhBigJl5Y4HfdYq/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：Asia/Seoul
- **变更内容**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）；[来源2](https://arxiv.org/pdf/2307.15043)（访问 2026-11-07）
