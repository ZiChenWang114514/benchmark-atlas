# ScienceQA

> 第1轮深度复核：2026-11-07（KST / Asia/Seoul）。采集日不等于榜单更新日或评测运行日；“待核实”不等于不存在。

[阅读Drive原始论文PDF](https://drive.google.com/file/d/1DbMOVlQF4L3yu_htLns-S1ladvipIuxm/view?usp=drivesdk)

## 基本信息

### 简称

ScienceQA

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 全称

Science Question Answering

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 基准版本

NeurIPS 2022 原始21,208题发布协议；本轮固定官方problems.json，未发现官方另命名的数字版本。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/data/scienceqa/problems.json)（访问 2026-11-07 KST）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 发布日期

2022-09-20

> arXiv元数据首发日期原值；不是推测数据集首次上线时间。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 主板块

多模态

> Benchmark Atlas编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 领域标签

- 多模态科学问答

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 许可证

数据CC BY-NC-SA 4.0，原课程资源版权属于IXL；代码许可与数据许可分开。

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### 论文

https://arxiv.org/abs/2209.09513

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 官方代码

https://github.com/lupantech/ScienceQA

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 数据地址

https://huggingface.co/datasets/derek-thomas/ScienceQA

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/derek-thomas/ScienceQA)（访问 2026-11-07 KST）。

### 官方入口

https://scienceqa.github.io/

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 论文标题

Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

## 发起与维护

### 发起机构

论文作者单位：UCLA、亚利桑那州立大学、Allen Institute for AI。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

### 合作研究机构

- University of California, Los Angeles
- Arizona State University
- Allen Institute for AI

> 按论文作者署名机构记录合作研究背景，不把课程来源IXL误写为合作机构。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### 作者

- Lu, Pan
- Mishra, Swaroop
- Xia, Tony
- Qiu, Liang
- Chang, Kai-Wei
- Zhu, Song-Chun
- Tafjord, Oyvind
- Clark, Peter
- Kalyan, Ashwin

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）。

### 维护方

Pan Lu / ScienceQA 官方仓库；README明确由Pan Lu接收问题与榜单反馈。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 资助

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

## 设计目标

### 衡量能力

多模态科学选择题与可解释的多步推理，联合学习答案、lecture和explanation。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

### 设计背景

既有科学QA往往仅文本、规模小、学科少或缺少答案解释。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

## 构建方式

### 题目来源

从IXL小学与中学课程资源收集问题、图像/文本上下文、答案、背景lecture与具体explanation。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

### 出题者背景

原课程内容来自教育网站IXL；本批未核实所有原题作者资质。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### 审核流程

整理多模态上下文和分层主题标签；质量审查及人类评估细则见论文附录，本批未逐条复现。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 质量控制

整理多模态上下文和分层主题标签；质量审查及人类评估细则见论文附录，本批未逐条复现。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 去污染

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

## 数据形式

### 规模

21,208题；10,332题有图，10,220题有文本上下文，6,532题两者都有；26主题、127类别、379技能。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/derek-thomas/ScienceQA)（访问 2026-11-07 KST）。

### 题型

多项选择；部分无图或无上下文，不能把全量集视为纯图像问答。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 模态

图像+文本（部分样本或版本仅文本）

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

### 语言

英文（本次公开问题/官方说明；完整语言分布待核实）

来源：[1](https://huggingface.co/datasets/derek-thomas/ScienceQA)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 难度与类型

- **proxy**：grade是课程年级，不等同于经校准的题目难度。
- **grades_1_to_12_counts**：{"grade1": 95, "grade2": 1678, "grade3": 3032, "grade4": 3544, "grade5": 3086, "grade6": 2450, "grade7": 2749, "grade8": 2546, "grade9": 491, "grade10": 558, "grade11": 539, "grade12": 440}
- **leaderboard_groups**：["G1-6", "G7-12"]

> 本轮逐条统计官方problems.json，共21,208条；不估计额外难度等级。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/data/scienceqa/problems.json)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 公开与隐藏划分

官方公开train 12,726、val 4,241、test 4,241及答案；60:20:20随机划分。榜单另有mini 1,000，必须标明全量/mini与IMG等子集。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/data/scienceqa/problems.json)（访问 2026-11-07 KST）；[2](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[3](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

## 评测方法

### 指标

选项准确率；另按自然/社会/语言学科、图像/文本上下文、年级分组报告。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 评分

选项准确率；另按自然/社会/语言学科、图像/文本上下文、年级分组报告。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 提示和复现设置

论文比较few-shot GPT-3与微调UnifiedQA；Q/C/M/A/lecture/explanation的输入输出组合要记录，带参考解释输入属于不同协议。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）；[2](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### 官方脚本

https://github.com/lupantech/ScienceQA

来源：[1](https://github.com/lupantech/ScienceQA)（访问 2026-11-07 KST）。

### 可比性提示

官方榜单由论文人工整理，官方提醒可能有错误、歧义和缺失；zero-shot/few-shot/fine-tune、全量与IMG子集、4,241与mini 1,000不能混比。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）；[3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-07 KST / Asia/Seoul

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

### 最新版本与H2证据

当前官方仓库仍提供21,208题原始协议与JSON；README最近列出的主要榜单更新为2023-12-29，交互榜单数据另含2024-01-23 KAM-CoT记录。不存在由访问日期推导出的2026新数据版本。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/javascript/leaderboard-data.js)（访问 2026-11-07 KST）；[3](https://raw.githubusercontent.com/lupantech/ScienceQA/main/data/scienceqa/problems.json)（访问 2026-11-07 KST）。

### 论文修订与H2使用证据

- **revisions**：[{"version": "v1", "date_kst": "2022-09-20T16:04:24+09:00"}, {"version": "v2", "date_kst": "2022-10-17T16:46:47+09:00"}]
- **continued_use_2026h2**：[{"url": "https://arxiv.org/html/2610.01352v2", "date": "2026-10-23", "note": "MMVistaReason v2 §4.1及表2实际评测 ScienceQA（ScienceQA设置），比较4B/9B及其他视觉语言模型；不把mini/val等划分另计。", "date_kst": "2026-10-23T01:54:37+09:00", "verified_in_round1": "本轮重新打开arXiv v2正文§4.1/Table2与abs提交历史，确认实际评测；源站v2为2026-10-22 16:54:37 UTC。"}]
- **verification**：已打开并复核证据原文的实际评测章节及表格，不只按参考文献或网页存活判断。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）；[3](https://arxiv.org/abs/2610.01352)（访问 2026-11-07 KST）。

### 饱和程度

本轮官方榜单数据最高Avg为96.18%（Fine-tune），但榜单混列训练设置且非持续独立复测。可说明该设置高分，不能据此断言所有设置或整个基准已饱和。

来源：[1](https://scienceqa.github.io/javascript/leaderboard-data.js)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 污染、冲突与限制

官方榜单由论文人工整理，官方提醒可能有错误、歧义和缺失；zero-shot/few-shot/fine-tune、全量与IMG子集、4,241与mini 1,000不能混比。

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）；[3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

### 后续工作与衍生

官方榜单提供mini 1,000与IMG/NAT/SOC/LAN、G1-6/G7-12等报告切片；它们是同一基准的子集，不作为新benchmark计数。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-07

来源：[1](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

### 官方榜单

https://scienceqa.github.io/leaderboard.html

来源：[1](https://scienceqa.github.io/leaderboard.html)（访问 2026-11-07 KST）。

### 权威第三方覆盖

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07 KST）。

### 结果快照

- {"model": "Mutimodal-T-SciQ_Large", "score": 96.18, "unit": "%", "metric": "accuracy", "scope": "官方全量test 4,241；Fine-tune；Avg", "date": "2023-05-05", "accessed": "2026-11-07 KST", "source_url": "https://scienceqa.github.io/javascript/leaderboard-data.js", "provenance": "本轮重新打开官方网页实际使用的leaderboard-data.js；人工摘录论文结果，不是2026重新跑分。", "leaderboard_updated_at": "待核实"}
- {"model": "MC-CoT_F-Large", "score": 94.88, "unit": "%", "metric": "accuracy", "scope": "官方全量test 4,241；Fine-tune；Avg", "date": "2023-11-23", "accessed": "2026-11-07 KST", "source_url": "https://scienceqa.github.io/javascript/leaderboard-data.js", "provenance": "本轮重新打开官方网页实际使用的leaderboard-data.js；人工摘录论文结果，不是2026重新跑分。", "leaderboard_updated_at": "待核实"}
- {"model": "Honeybee (Vicuna-13B)", "score": 94.39, "unit": "%", "metric": "accuracy", "scope": "官方全量test 4,241；Fine-tune；Avg", "date": "2023-12-11", "accessed": "2026-11-07 KST", "source_url": "https://scienceqa.github.io/javascript/leaderboard-data.js", "provenance": "本轮重新打开官方网页实际使用的leaderboard-data.js；人工摘录论文结果，不是2026重新跑分。", "leaderboard_updated_at": "待核实"}
- {"model": "MMVistaReason-4B (MVR-4B)", "score": 96.8, "unit": "%", "metric": "论文协议答案正确率（CompassVerifier）", "scope": "ScienceQA，论文此表未区分全量/IMG口径", "date": "2026-10-23", "accessed": "2026-11-07", "source_url": "https://arxiv.org/html/2610.01352v2", "provenance": "MMVistaReason作者自报表2；VLMEvalKit，T=0，max16384；§7.3用CompassVerifier替代传统字符串匹配，不是官方榜单/AA独立评测", "date_basis": "arXiv v2提交时间换算KST；不是未公开的评测运行日期。"}
- {"model": "MMVistaReason-9B (MVR-9B)", "score": 97.4, "unit": "%", "metric": "论文协议答案正确率（CompassVerifier）", "scope": "ScienceQA，论文此表未区分全量/IMG口径", "date": "2026-10-23", "accessed": "2026-11-07", "source_url": "https://arxiv.org/html/2610.01352v2", "provenance": "MMVistaReason作者自报表2；同上协议，不与其他榜单无条件混排", "date_basis": "arXiv v2提交时间换算KST；不是未公开的评测运行日期。"}

来源：[1](https://scienceqa.github.io/javascript/leaderboard-data.js)（访问 2026-11-07 KST）；[2](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

### 覆盖说明

2026-11-07 KST重新读取交互榜单实际数据源；前三为可见历史汇总，未提供统一榜单更新日期。保留2026-H2研究复测于不同scope，不混排或称当前全球SOTA。官方提示人工整理可能有错误和缺失。

来源：[1](https://scienceqa.github.io/javascript/leaderboard-data.js)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）；[3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

## 联系方式

### 公开联系邮箱

- lupantech@gmail.com

> 项目官方公开联系/榜单提交或版权反馈邮箱；未发送任何邮件。

来源：[1](https://scienceqa.github.io/leaderboard.html)（访问 2026-11-07 KST）。

### 问题反馈

https://github.com/lupantech/ScienceQA/issues

来源：[1](https://github.com/lupantech/ScienceQA)（访问 2026-11-07 KST）。

### 官方讨论渠道

https://twitter.com/lupantech/status/1570828580346802178

> 官方README提供的公开讨论入口；本轮未访问X内容、未发送消息。

来源：[1](https://raw.githubusercontent.com/lupantech/ScienceQA/main/README.md)（访问 2026-11-07 KST）。

### 隐私政策

仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07 KST）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2209.09513

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### SHA-256

046aa5207a78594b84fddac6a750354b8afc0d37f6bdef6730ef3aae691abee5

> 下载原始字节校验，未压缩、未改写。

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### 字节数

8065121

来源：[1](https://arxiv.org/pdf/2209.09513)（访问 2026-11-07 KST）。

### Drive文件夹

- **id**：1_wNk_5SUO3RJJZ_YQeDGPVT_QepWLNu9
- **webViewLink**：https://drive.google.com/drive/folders/1_wNk_5SUO3RJJZ_YQeDGPVT_QepWLNu9

来源：[1](https://drive.google.com/drive/folders/1_wNk_5SUO3RJJZ_YQeDGPVT_QepWLNu9)（访问 2026-11-07 KST）。

### 其他文档

- {"kind": "中文介绍 Google Doc", "id": "1x5f5zGPYo6PjLVTHT6IDBzCJo0SQkXF0UzNmWmcNxkQ", "webViewLink": "https://docs.google.com/document/d/1x5f5zGPYo6PjLVTHT6IDBzCJo0SQkXF0UzNmWmcNxkQ/edit?usp=drivesdk"}

来源：[1](https://docs.google.com/document/d/1x5f5zGPYo6PjLVTHT6IDBzCJo0SQkXF0UzNmWmcNxkQ/edit?usp=drivesdk)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：1DbMOVlQF4L3yu_htLns-S1ladvipIuxm
- **webViewLink**：https://drive.google.com/file/d/1DbMOVlQF4L3yu_htLns-S1ladvipIuxm/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1DbMOVlQF4L3yu_htLns-S1ladvipIuxm/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- {"date": "2026-11-07", "timezone": "Asia/Seoul", "change": "核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "round": "1 / 深度实证复核", "change": "重读官方论文/JSON，补合作机构、维护和社交入口、精确年级分布；刷新官网JS榜单前三；重新核实H2实跑并修正v2日期为KST。"}

来源：[1](https://arxiv.org/abs/2209.09513)（访问 2026-11-07 KST）；[2](https://scienceqa.github.io/)（访问 2026-11-07 KST）。

