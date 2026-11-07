# GAIA

> 第1轮深度复核：2026-11-07（KST / Asia/Seoul）。采集日不等于榜单更新日或评测运行日；“待核实”不等于不存在。

[阅读Drive原始论文PDF](https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk)

## 基本信息

### 简称

GAIA

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）。

### 全称

GAIA: a benchmark for General AI Assistants

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 基准版本

GAIA 原始466题；2023数据发布

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 论文版本

arXiv v1

> 论文修订版本不等同数据集版本。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 发布日期

2023-11-22 05:34:47 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 领域标签

- 通用助理与工具使用

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 许可证

官方GAIA leaderboard Space代码：Apache-2.0（Space README元数据）；GAIA数据集独立许可证待核实，数据卡要求门控且不得公开再分发。

> 官方数据卡与本轮公开metadata均未给出可核实的数据license字段，不把Space代码许可扩展到数据。

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/README.md)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/gaia-benchmark/GAIA)（访问 2026-11-07 KST）；[3](https://huggingface.co/api/datasets/gaia-benchmark/GAIA)（访问 2026-11-07 KST）。

### 论文

https://arxiv.org/abs/2311.12983

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 官方代码

https://huggingface.co/spaces/gaia-benchmark/leaderboard/tree/main

> 官方评测Space源代码，包括app.py与scorer.py；不是推断出来的第三方GitHub仓库。

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）；[2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/README.md)（访问 2026-11-07 KST）。

### 数据地址

https://huggingface.co/gaia-benchmark

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 官方入口

https://huggingface.co/gaia-benchmark

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）。

### 论文标题

GAIA: a benchmark for General AI Assistants

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 发起与维护

### 发起机构

Meta FAIR / GenAI、Hugging Face 与 AutoGPT 作者团队（单位/项目口径）

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 合作研究机构

Surge AI 提供有偿人工标注。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 作者

- Mialon, Grégoire
- Fourrier, Clémentine
- Swift, Craig
- Wolf, Thomas
- LeCun, Yann
- Scialom, Thomas

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 维护方

gaia-benchmark 官方 Hugging Face 组织

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 资助

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 设计目标

### 衡量能力

现实信息查找、多模态理解、网页访问、工具与多步推理结合的通用助理能力。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 设计背景

人类容易完成但需要组合工具的任务，可能比孤立专业知识题更能揭示助理系统不足。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 构建方式

### 题目来源

人工设计可验证现实问题，答案通常短且明确，部分含附件。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 出题者背景

研究作者与经付费招募的 Surge AI 标注者；不把所有出题人称专家。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 审核流程

创建者之外两名独立验证者复核，不一致时修改或丢弃。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 质量控制

力求唯一/稳定答案、可由人完成；按推理步数与工具复杂度设三档。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 去污染

避免答案可直接在网上纯文本检索到，隐藏测试答案；问题公开后仍可能进入后续训练。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 数据形式

### 规模

466道人工问题；166道development公开答案，300道test答案隐藏。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 题型

短答案的开放问题，可能需网页、文件、视觉和计算。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 模态

- 文本
- 图像及文件附件（视题）
- 工具/网页

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 语言

英语为主。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 难度与类型

Level 1 / 2 / 3，依据步骤、工具数量与复杂性划分。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 公开与隐藏划分

2023版共466题：validation 165（L1 53/L2 86/L3 26），test 301（L1 93/L2 159/L3 49）。官方app当前仅显示test榜；数据集门控，不下载或公开传播隐藏数据。

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/gaia-benchmark/GAIA)（访问 2026-11-07 KST）。

## 评测方法

### 指标

准确率，按Level和总体报告。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 评分

官方scorer.py：数字移除$、%、逗号后转float严格相等；列表按逗号/分号分项，要求长度与顺序相等；字符串去空格、默认去标点并转小写后精确匹配。无LLM裁判。

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/scorer.py)（访问 2026-11-07 KST）。

### 提示和复现设置

原协议zero-shot；完整助理系统可以使用工具，必须报告工具、预算与附件处理。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 官方脚本

https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/scorer.py

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/raw/main/scorer.py)（访问 2026-11-07 KST）；[2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）。

### 可比性提示

validation与test、总体与各Level、多模态权限不同不可混排；不要把仅LLM和完整Agent系统分数等同。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-07 KST / Asia/Seoul

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）。

### 最新版本与H2证据

- **version**：GAIA 原始466题；2023数据发布
- **evidence_2026_h2**：[{"url": "https://arxiv.org/html/2609.19134v1", "date": "2026-09-17", "note": "ScienceIDE §4.2及参考文献明确引用 GAIA 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。", "date_kst": "2026-09-17T02:55:47+09:00", "verified_in_round1": "本轮重新打开ScienceIDE正文及参考文献，按原始论文ID确认；属于§4.2相关工作引用，非本文实跑。"}, {"url": "https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet", "date": "2026-11-03", "note": "官方HF榜单公开结果集2023/test中Keen AgenticOS V1.1提交记录，score 0.9435215946843853；为官方评分提交证据。"}]
- **format_update**：2025-10：HF数据集改为Parquet分片（metadata.parquet及各level分片），列名不变；数据集已加访问门控。

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）；[3](https://huggingface.co/datasets/gaia-benchmark/GAIA)（访问 2026-11-07 KST）；[4](https://arxiv.org/abs/2609.19134)（访问 2026-11-07 KST）；[5](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet)（访问 2026-11-07 KST）；[6](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）。

### 论文修订与H2使用证据

Submission history From: Grégoire Mialon [ view email ] [v1] 2023-11-22 05:34:47 KST (3,688 KB)

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 饱和程度

官方test提交榜最高94.35%；这反映提交系统通过隐藏答案自动评分的结果，不是独立审计重跑，也不足证明人类广泛能力饱和。原始论文92%人类参照不能不加条件与当前系统混比。

来源：[1](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet)（访问 2026-11-07 KST）；[2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）；[3](https://arxiv.org/pdf/2311.12983)（访问 2026-11-07 KST）。

### 污染、冲突与限制

网页内容与在线工具随时间变化、公开问题后续污染、答案规范化都会影响复现；原论文成绩不能当作当前能力上限。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 后续工作与衍生

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-07 KST / Asia/Seoul

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）。

### 官方榜单

https://huggingface.co/spaces/gaia-benchmark/leaderboard

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard)（访问 2026-11-07 KST）。

### 权威第三方覆盖

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）。

### 结果快照

- {"model": "Keen AgenticOS V1.1", "score": 94.35, "unit": "%", "metric": "Average score (%)", "scope": "GAIA 2023 test 301；官方HF Space同源results_public", "date": "2026-11-03", "accessed": "2026-11-07 KST", "source_url": "https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet", "provenance": "官方Space app.py指定的公开结果集；参评者提交由官方scorer评分，不等同独立重跑Agent。", "model_family": "Deepseek，Kimi，Claude", "level1": 97.85, "level2": 93.71, "level3": 89.8, "leaderboard_updated_at": "待核实"}
- {"model": "Shadow Harness V8.01", "score": 94.02, "unit": "%", "metric": "Average score (%)", "scope": "GAIA 2023 test 301；官方HF Space同源results_public", "date": "2026-10-12", "accessed": "2026-11-07 KST", "source_url": "https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet", "provenance": "官方Space app.py指定的公开结果集；参评者提交由官方scorer评分，不等同独立重跑Agent。", "model_family": "GPT  Claude  Grok  Gemini  DeepSeek", "level1": 98.92, "level2": 91.82, "level3": 91.84, "leaderboard_updated_at": "待核实"}
- {"model": "Keen AgenticOS  V1.0", "score": 94.02, "unit": "%", "metric": "Average score (%)", "scope": "GAIA 2023 test 301；官方HF Space同源results_public", "date": "2026-10-29", "accessed": "2026-11-07 KST", "source_url": "https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet", "provenance": "官方Space app.py指定的公开结果集；参评者提交由官方scorer评分，不等同独立重跑Agent。", "model_family": "Deepseek，Kimi，Claude", "level1": 96.77, "level2": 93.71, "level3": 89.8, "leaderboard_updated_at": "待核实"}

> Space外壳未直接渲染表格，但公开app.py可读且明确从gaia-benchmark/results_public的2023/test读取；本轮仅下载公开榜单结果Parquet，不触及门控GAIA题库或内部提交/联系数据。

来源：[1](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet)（访问 2026-11-07 KST）；[2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）。

### 覆盖说明

本轮从官方HF Space公开app.py追踪到results_public，按score降序并乘100、保留2位小数，与app展示转换一致。前三Keen AgenticOS V1.1 94.35、Shadow Harness V8.01 94.02、Keen AgenticOS V1.0 94.02；后两名同分不强行分胜负。记录各提交日，不把采集日当榜单整体更新日。

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/gaia-benchmark/results_public/resolve/main/2023/test-00000-of-00001.parquet)（访问 2026-11-07 KST）。

## 联系方式

### 公开联系邮箱

- gmialon@meta.com
- tscialom@meta.com
- clementine@huggingface.co

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 问题反馈

https://huggingface.co/spaces/gaia-benchmark/leaderboard/discussions

> 官方HF Space社区反馈，不伪造不存在的GitHub Issues。

来源：[1](https://huggingface.co/spaces/gaia-benchmark/leaderboard)（访问 2026-11-07 KST）；[2](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/app.py)（访问 2026-11-07 KST）。

### 官方讨论渠道

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

### 隐私政策

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2311.12983)（访问 2026-11-07 KST）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2311.12983

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2311.12983)（访问 2026-11-07 KST）。

### SHA-256

5bf6f968d4f5cd20acdfca6e81e3c9f5277bb66061fad7a02e35442dff812ba0

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://arxiv.org/pdf/2311.12983)（访问 2026-11-07 KST）。

### 字节数

4254059

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://arxiv.org/pdf/2311.12983)（访问 2026-11-07 KST）。

### Drive文件夹

- **id**：1XQ-wCiSOFqEob12_--TjaruKGF7D99rG
- **webViewLink**：https://drive.google.com/drive/folders/1XQ-wCiSOFqEob12_--TjaruKGF7D99rG

来源：[1](https://drive.google.com/drive/folders/1XQ-wCiSOFqEob12_--TjaruKGF7D99rG)（访问 2026-11-07 KST）。

### 其他文档

- {"type": "中文介绍Google Doc", "id": "1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE", "webViewLink": "https://docs.google.com/document/d/1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE/edit?usp=drivesdk"}

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）；[2](https://docs.google.com/document/d/1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE/edit?usp=drivesdk)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf
- **webViewLink**：https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "round": "1 / 深度实证复核", "change": "补官方Space代码与Apache代码许可，数据许可仍待核实；读取公开results_public得test前三与11月提交证据，补官方scorer。"}

来源：[1](https://huggingface.co/gaia-benchmark)（访问 2026-11-07 KST）。

