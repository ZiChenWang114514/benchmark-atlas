# RAG-Safety-Bench

> 第1轮核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。榜单快照与H2使用证据分别记录。

[阅读归档原始论文 PDF](https://drive.google.com/file/d/1XGmcQ4mrUXYV6AjzHXA0P6xrauG_mn3z/view?usp=drivesdk)

## 基本信息

### 简称

RAG-Safety-Bench

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 全称

RAG-Safety-Bench

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 基准版本

v14 frozen release：v14_full_987与v14_balanced_346。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 论文版本

arXiv v1

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 发布日期

2026-09-10

> 原始论文首发日期，不保证等同于数据文件首次公开日。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 主板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 领域标签

- 检索增强系统安全

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 许可证

存在官方材料差异：论文称数据CC BY-SA 4.0；仓库LICENSING.md仍为待作者批准的分拆提案（数据CC BY-SA 4.0、原创代码MIT），批准前不额外授予超出第三方条款的复用许可。

[来源1](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2609.11758

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 官方代码

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 数据地址

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 官方入口

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 论文标题

RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 发起与维护

### 机构与作者单位

University of Ottawa；作者 Adithiyan Rajan Indira Saravanan、Kathleen C. Fraser。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 正式合作机构

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 作者

- Saravanan, Adithiyan Rajan Indira

- Fraser, Kathleen C.

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 当前维护方

官方代码与反馈由 The-Safe-AI-Lab/RAG-Safety-Bench 仓库提供；个人持续维护职责及响应时限未核实。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 资助

NSERC Discovery Grant RGPIN-2026-05716；Compute Ontario 与 Digital Research Alliance of Canada 计算支持。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 设计目标

### 测量能力

控制检索条件，区分RAG引起的安全变化、能力变化和拒答变化。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 既有评测缺口

RAG评测常把答案正确性、有害输出及拒答混合，或没有控制证据中是否真正包含答案。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 构建方式

### 题目来源

使用Wikipedia材料与Claude Sonnet4.5辅助生成，并做自检；构造四种检索条件。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 出题与标注背景

研究团队设计安全子类别及基准；人工资质的逐人清单待核实。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 审核

采用GPT-4.1-mini审计上下文；对balanced样本检查oracle中答案可用性。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 质量控制

分别报告harmfulness、accuracy和refusal，避免把能力差误判为安全好。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 去污染

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 数据形式

### 题量

完整987条query，balanced子集346条，20个子类别；346×4条件得到每模型1,384条实验记录，不是1,384道独立原题。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 题型

开放问答；四条件：无RAG、oracle答案、同主题无答案、随机良性材料

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 难度

安全/不安全知识与不同检索条件的受控比较；不把有害知识准确率直接当安全性。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 公开与隐藏划分

公开frozen输入、provenance manifests与generation配置；原始模型回答、judge traces及unsafe_majority_v2复评分制品刻意不公开，local judge配置仅是实现示例。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

## 评测方法

### 指标

harmfulness、accuracy、refusal分别报告。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 评分

有害性由Llama-Guard-3-8B、ShieldGemma-2B、WildGuard三裁判多数决定；准确性由Claude Opus4.7判定；拒答类别独立分析。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 提示与生成设置

temperature=0.0、top_p=1.0、max_new_tokens=1024；文档使用清洗后的全文前缀，每篇最多12,000字符；论文另注明seed=42。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 脚本

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[来源1](https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench)（访问 2026-11-07）

### 可比性警告

低unsafe accuracy不一定意味着强安全；应同时看harmfulness和refusal；oracle证据仍有部分答案，不能当100%足额证据。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

> 2026-H2实际使用证据：2026-09-10：RAG-Safety-Bench 原始论文H2发布并开展RAG安全实验；其评测协议与基准作为一个条目。

[来源1](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 数据版本

- **版本**：v14：完整987题/3,948条件行；balanced 346题/1,384条件行
- **2026H2引用／使用证据**：- **来源URL**：https://arxiv.org/html/2609.11758v1
  - **日期**：2026-09
  - **说明**：原始论文在H2发布并实际报告五模型四检索条件实验；属于作者首次实验，非独立后续引用。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 论文修订记录

- **版本**：v1
- **submitted_at**：2026-09-11T01:12:25+09:00
- **时区**：Asia/Seoul (KST)

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 污染与已知问题

Oracle可答性并非全为完整答案：balanced中200题yes、146题partial。仓库明确私有v2复评分流程及原始输出未随包发布，local judge示例不能替代论文复评分制品。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 衍生评测

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 榜单快照

### 采集日

2026-11-07

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 官方榜或原始结果入口

https://arxiv.org/abs/2609.11758

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 二级机构榜单

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 可读结果

- **模型 / Agent**：Ministral-3-8B（论文标签）
- **分数**：90.7
- **unit**：%
- **指标**：unsafe-capability accuracy
- **scope**：原始论文 balanced oracle；不是harmfulness/安全分，不能据此认定更安全
- **evaluation_date**：论文2026-09-10；精确运行日期待核实

- **模型 / Agent**：Qwen2.5-7B（论文标签）
- **分数**：82.9
- **unit**：%
- **指标**：unsafe-capability accuracy
- **scope**：同一oracle条件，非安全榜
- **evaluation_date**：论文2026-09-10；精确运行日期待核实

- **模型 / Agent**：Gemma-3-12B（论文标签）
- **分数**：74.9
- **unit**：%
- **指标**：unsafe-capability accuracy
- **scope**：同一oracle条件，非安全榜
- **evaluation_date**：论文2026-09-10；精确运行日期待核实

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 覆盖与时效限制

新基准原始论文基线，不是通用安全排行榜；所列是unsafe-capability答案准确率，不是有害率。本次未核实独立AA/Epoch/LMArena榜。

> 本轮重新打开官方README及H2实证论文；仍未核验到同协议实时全榜，历史论文结果不得称2026当前前三。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

## 联系方式

### 公开研究联系邮箱

- aindi023@uottawa.ca

- kathleen.fraser@uottawa.ca

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 仓库讨论与Issues

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench/issues

> 公开反馈入口；未发送问题。

[来源1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 官方社交渠道

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2609.11758

[来源1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-07）

### 原件SHA-256

0eb8c0582d538136e2ac32fd51bffab170bac16f9173309c9f68870808bdb490

> 原始下载字节SHA-256；未压缩或改写。

[来源1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-07）

### 原件字节数

2137960

[来源1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-07）

### Drive目录

- **id**：1qW8zMCcfafxtK0w_x4SyifexNN8DZ0uh
- **webViewLink**：https://drive.google.com/drive/folders/1qW8zMCcfafxtK0w_x4SyifexNN8DZ0uh

[来源1](https://drive.google.com/drive/folders/1qW8zMCcfafxtK0w_x4SyifexNN8DZ0uh)（访问 2026-11-07）

### 中文介绍

- **kind**：中文介绍 Google Doc
- **id**：1F6zykWwlZb0vzbaaDz6pW4mUcfqD5g4xRsQbwKbVm5o
- **webViewLink**：https://docs.google.com/document/d/1F6zykWwlZb0vzbaaDz6pW4mUcfqD5g4xRsQbwKbVm5o/edit?usp=drivesdk

[来源1](https://docs.google.com/document/d/1F6zykWwlZb0vzbaaDz6pW4mUcfqD5g4xRsQbwKbVm5o/edit?usp=drivesdk)（访问 2026-11-07）

### Drive PDF归档

- **id**：1XGmcQ4mrUXYV6AjzHXA0P6xrauG_mn3z
- **webViewLink**：https://drive.google.com/file/d/1XGmcQ4mrUXYV6AjzHXA0P6xrauG_mn3z/view?usp=drivesdk

## 变更记录

### changelog

- **日期**：2026-11-07
- **时区**：Asia/Seoul
- **变更内容**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。

- **日期**：2026-11-07
- **时区**：KST / Asia/Seoul
- **变更内容**：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。

[来源1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）；[来源2](https://arxiv.org/pdf/2609.11758)（访问 2026-11-07）
