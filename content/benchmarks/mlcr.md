# MLCR / MLCR-AA

> Benchmark Constitution，深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MLCR关注医疗理赔记录中的长篇综合推理：模型需要重建时间线、临床因果与文档缺失，而非背诵医学考试知识。病例为合成但受现实案例启发；公开较易题与私有难题分开发布。MLCR-AA是Artificial Analysis独立运行的实现，准确性、完整性和联合通过率必须分别解读。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 简称

MLCR / MLCR-AA

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 全称

Medical Long Context Reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 基准版本

MLCR v1.1（2026-08-31）；MLCR-AA是独立实现口径

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 论文版本

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 发布日期

2026-06-18首发；2026-08-31 v1.1

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 主板块

生物与医学

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 领域标签

- 长上下文
- 保险记录

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 许可证与权利边界

HF数据卡明确license: other；具体可再分发条款待核实。官方仓库main/LICENSE请求404，不能由README称open-source推断MIT。

[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset/raw/main/README.md)（访问 2026-11-08）

### 论文入口

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 代码仓库

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 数据集入口

https://huggingface.co/datasets/Wisedocs/mlcr-dataset

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 官方主页

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 论文标题

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

Wisedocs

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 合作方

Artificial Analysis（共同发布MLCR-AA，独立运行其私有评测）

[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 作者

- Denys Linkov（2026-06-18官方技术博客作者）
- Aryan Dhar（2026-08-31 v1.1官方技术博客作者）

> 此处是公开技术材料作者，不冒称完整学术论文作者表。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### 维护方

Wisedocs维护原始MLCR；Artificial Analysis维护MLCR-AA评测。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 资助

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## 设计目标

### 衡量能力

跨长篇、碎片化医疗记录重建时间线、因果、治疗模式及保险理赔相关性。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 设计背景

不仅定位单条事实，还需专家级临床综合与多部分推理。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

## 构建方式

### 题目来源

合成医疗记录，模型上下文可按固定seed确定性插入无关filler；病例、提示、模型、模态、filler比例和thinking levels组成实验矩阵。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 出题与审阅者背景

问题模仿医疗及保险理赔专业人员审阅记录的工作；参考答案由人类验证、以真实案例构成为灵感生成合成病例。具体逐题出题人资历待核实。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）

### 审核流程

专家标注ground truth，三裁判对照原记录与参考答案。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 质量控制

空答案直接失败；多数裁判确认完整且无记录矛盾才通过。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 去污染及其证据边界

官方明确将Tier4–6难题留作私有评测，以降低污染；病例和Tier1–3公开。私有保留是控制措施，不等于已验证所有受测模型从未接触相关材料。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

10个合成病例，每例50–150份医疗摘要、25k–64k tokens；首发博客称250个问题，并公开100+个Tier1–3问题。公开仓库另有131份空表OCR及131份合成填表OCR；AA私有60题×3重复独立计数，不累加到题量。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 题型

单事实检索、跨文档综合、临床因果和多部分问题。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 模态

- 文本
- OCR记录

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 语言

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 难度

原MLCR六层：Easy、Medium、Hard、Expert、Multi-part Compound、Compound Hallucination Check。AA当前页称使用最难两类expert/compound；v1.1博客称three difficult tiers，口径冲突照录，不强行统一。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 公开与隐藏划分

公开Tier1–3及10病例；官方说明Tier4–6私有。HF配置questions、cases_summaries、filler_files均命名train，仅是发布分区标签，不应误称模型训练集。AA另取私有60题、每题3重复。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset/raw/main/README.md)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

## 评测方法

### 指标

主指标pass rate / pass@1；另列accuracy与completeness，不可混用。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 评分方法

三LLM裁判多数票：每部分完整且无任何与原记录矛盾的claim。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 运行与提示设置

每题3重复；默认每部分一段并引用原记录；AA裁判Claude Opus5.5、GPT-6.1 Sol、Grok4.7，medium。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方脚本

Wisedocs官方evaluation harness仓库；AA私有集不能由公开数据直接完全复现。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 可比性警示

公开harness有≤参考答案5倍字符的conciseness gate及旧judge面板；AA当前私有协议和judge已不同。两者结果、模态和filler比例不可混比。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

- **version**：MLCR v1.1；AA私有实现另计
- **evidence_2026_h2**：- - **url**：https://artificialanalysis.ai/evaluations/mlcr-aa；- **date**：2026-11-07；- **date_type**：observed_on；- **note**：AA当前独立评测27模型，属于持续医疗长记录测评，不在Intelligence Index。；- - **url**：https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md；- **date**：2026-08-31；- **note**：Wisedocs README发布v1.1，改进judge校准并与AA共同发布评测。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 论文修订及历史证据

技术材料时间线：2026-06-18首发博客；2026-08-31发布MLCR v1.1，属于裁判校准与参考答案修订。独立arXiv论文版本待核实。

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### 饱和情况

当前AA页面最高联合pass rate为41.7%；accuracy与completeness是独立维度，不能用98.3% accuracy声称整个MLCR-AA已饱和。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 污染、争议与限制

v1.1把accuracy错误与completeness缺漏分开，依据原始记录而不只参考答案，并将长度门槛由3×放宽到5×。v1.1博客的历史64.4%联合通过率与当前AA的41.7%不是同一快照；难题两类/三层表述亦有冲突。HF卡片写Multi-Length Context Retrieval，与官方博客Medical Long Context Reasoning不一致，本条名称以博客及AA为准。

[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset/raw/main/README.md)（访问 2026-11-08）

### 衍生与版本关系

MLCR-AA是Artificial Analysis独立执行的私有难题实现；公开MLCR harness、v1.1博客快照与当前AA榜不混排。

[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（采集日，不是评测运行日）

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 官方入口

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 第三方覆盖入口

https://artificialanalysis.ai/evaluations/mlcr-aa

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### AA当前独立评测 / pass rate

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| GPT-6 Astra (Max) | 41.7 | pass rate / % |
| Claude Sonnet 5.5 (Max, Default Fallback) | 41.7 | pass rate / % |
| GPT-6.1 Sol (Max) | 38.3 | pass rate / % |

- **GPT-6 Astra (Max)**：- **rank**：1；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细
- **Claude Sonnet 5.5 (Max, Default Fallback)**：- **rank**：1；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细
- **GPT-6.1 Sol (Max)**：- **rank**：3；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

#### AA当前独立评测 / completeness

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude Sonnet 5.5 (Max, Default Fallback) | 64.8 | completeness / % |
| Claude Opus 5.5 (Max, Default Fallback) | 63.3 | completeness / % |
| Claude Fable 5.1 (Max, Default Fallback) | 61.1 | completeness / % |

- **Claude Sonnet 5.5 (Max, Default Fallback)**：- **rank**：1；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细
- **Claude Opus 5.5 (Max, Default Fallback)**：- **rank**：2；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细
- **Claude Fable 5.1 (Max, Default Fallback)**：- **rank**：3；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

#### AA当前独立评测 / accuracy

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| GPT-6.1 Terra (Max) | 98.3 | accuracy / % |
| GPT-6.1 Sol (Max) | 96.7 | accuracy / % |
| GPT-6 Astra (Max) | 95.6 | accuracy / % |

- **GPT-6.1 Terra (Max)**：- **rank**：1；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细
- **GPT-6.1 Sol (Max)**：- **rank**：2；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细
- **GPT-6 Astra (Max)**：- **rank**：3；- **scope**：私有60题，每题3重复；仅页面文字列出的前三，不推造其余27模型明细

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）

#### Wisedocs v1.1博客历史快照 / overall

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude Fable 5 | 64.4 | overall pass rate / % |
| Claude Opus 5 | 59.4 | overall pass rate / % |
| Claude Opus 5 | 58.3 | overall pass rate / % |

- **Claude Fable 5**：- **published_date**：2026-08-31；- **configuration**：博客正文未在该数值段给出完整配置，不能映射到当前AA模型行
- **Claude Opus 5**：- **published_date**：2026-08-31；- **configuration**：博客正文未在该数值段给出完整配置，不能映射到当前AA模型行
- **Claude Opus 5**：- **published_date**：2026-08-31；- **configuration**：博客正文未在该数值段给出完整配置，不能映射到当前AA模型行

[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）


[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### 覆盖范围与时效

三个AA指标独立分轨；41.7%为显示精度下并列，不能宣称显著差异。博客历史overall分轨保留，未知精确运行日期待核实；未提取动态完整27模型表。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 公开反馈

https://github.com/Wisedocs-AI/medical-long-context-reasoning/issues

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 官方社交

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 隐私边界

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## 原始文件

### 原论文PDF

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### PDF SHA-256

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### PDF字节数

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 文件夹

待核实

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

### 其他官方材料

- - **title**：Benchmarking LLMs For Medical Document Work；- **url**：https://www.wisedocs.ai/blogs/medical-long-context-reasoning；- **published_date**：2026-06-18
- - **title**：MLCR v1.1: Calibrating LLM Judges for Long-Context Medical Reasoning；- **url**：https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning；- **published_date**：2026-08-31

[来源](https://www.wisedocs.ai/blogs/medical-long-context-reasoning)（访问 2026-11-08）；[来源](https://www.wisedocs.ai/blogs/mlcr-v1-1-calibrating-llm-judges-for-long-context-medical-reasoning)（访问 2026-11-08）

### PDF归档

待核实

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-08）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：按官方材料新建中文条目；区分热度、质量和不同版本评分。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/Wisedocs-AI/medical-long-context-reasoning/main/README.md)（访问 2026-11-08）
