# HLE-Diamond

> 核验日期：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未知不等于未公开。热度与成绩快照分开记录。

编辑状态：官方存在性已核验；字段级研究快照；note: trending: A

## 基本信息

### 简称

HLE-Diamond

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 全称

Humanity’s Last Exam: Diamond

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 基准版本

HLE-Diamond（命名版本）

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 论文版本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 发布日期

2026-09-22（官方发布文章日期）

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 主板块

推理

> Benchmark Atlas 编辑分类。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 领域标签

- 多模态
- 跨学科科学

> 编辑标签；空列表表示尚未补充细分标签。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 许可证

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 论文入口

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 官方代码

https://github.com/centerforaisafety/hle

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/cais/hle-diamond

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 官方入口

https://lastexam.ai/blog/hle-diamond

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 论文标题

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

## 发起与维护

### 发起机构

- Center for AI Safety
- Scale AI

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 合作方

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 作者

Center for AI Safety、Scale AI 与 HLE Contributors Consortium；Diamond清洗工作感谢研究社区与题目贡献者。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 维护方

Center for AI Safety / Scale AI

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 资助

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

## 设计目标

### 衡量能力

闭卷专家知识与跨学科推理；包含图像题，分别报告知识与推理分区。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 设计背景

针对原HLE问题质量，经研究社区反馈清洗与精炼，建立可持续比较的新版子集。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

## 构建方式

### 题目来源

从原HLE题目集合清洗、精炼而来。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 出题者背景

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 审核流程

历时一年的清洗与精炼，结合研究社区及HLE-Rolling反馈。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 质量控制

知识与推理各500题；不把原HLE总分直接当Diamond分数。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 去污染

数据卡加入canary字符串供训练数据过滤，并明确要求基准数据不进入训练语料。

[来源1](https://huggingface.co/datasets/cais/hle-diamond)（访问 2026-11-07）

## 数据形式

### 题量与规模

1,000题：500推理、500知识。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/cais/hle-diamond)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 题型

沿用HLE字段格式；AA以开放答案与等价检查裁判评分。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/cais/hle-diamond)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 模态

- 文本
- 图像（272题）

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 语言

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 难度

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 公开与隐藏划分

公开test split；partition列区分reasoning与knowledge。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/cais/hle-diamond)（访问 2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

## 评测方法

### 指标

pass@1 / 准确率；另报reasoning和knowledge。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 评分方式

AA遵循官方HLE裁判提示与格式，GPT-5.6 Luna (medium)判答案正确性。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 提示与运行设置

AA：1,000题各1次，无工具；官方HLE系统提示要求解释、答案及置信度。有视觉输入的模型接收图像，否则仅接收题文，仍在全部1,000题计分。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方评测脚本

https://github.com/centerforaisafety/hle

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 可比性警示

官方文章high推理、max推理及工具轨不同；AA使用自有裁判实现。原HLE的2,158纯文本题结果不可与Diamond 1,000题直接比较。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度A沿用候选分级；证据性质逐项标明，多URL不自动等于多个独立采纳方，也不把当前可见当作近期首发。

- AA v5用HLE-Diamond替换原HLE，指数权重10%。 [来源](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)（证据日期 2026-10-27；访问 2026-11-07）

### 核验日期

2026-11-07 KST / Asia/Seoul

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 当前版本与2026H2使用证据

- **version**：HLE-Diamond（命名版本）
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5", "date": "2026-10-27", "date_type": "source_calendar_date", "note": "AA v5用HLE-Diamond替换原HLE，指数权重10%。"}]

> 热度A沿用候选分级；证据性质逐项标明，多URL不自动等于多个独立采纳方，也不把当前可见当作近期首发。

[来源1](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)（访问 2026-11-07）

### 修订历史

Diamond为2026-09-22命名发布；官网引用原HLE论文，不能把该论文的首发日写成Diamond发布日期。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 饱和情况

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 衍生与版本关系

与已收录hle为同族新版子集；保留两者关系，不把知识/推理/工具轨重复计数。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 官方榜单入口

https://lastexam.ai/blog/hle-diamond

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 第三方评测入口

https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "GPT-6 Astra", "score": 59.9, "metric": "HLE-Diamond accuracy %; reasoning high; no tools", "source_url": "https://lastexam.ai/blog/hle-diamond", "source_date": "待核实", "collected_at": "2026-11-07 KST"}
- {"rank": 2, "model": "Gemini 4 Argon", "score": 56.9, "metric": "HLE-Diamond accuracy %; reasoning high; no tools", "source_url": "https://lastexam.ai/blog/hle-diamond", "source_date": "待核实", "collected_at": "2026-11-07 KST"}
- {"rank": 3, "model": "Claude Opus 5.5", "score": 54.6, "metric": "HLE-Diamond accuracy %; reasoning high; no tools", "source_url": "https://lastexam.ai/blog/hle-diamond", "source_date": "待核实", "collected_at": "2026-11-07 KST"}

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 覆盖与时效说明

官网发布文章内嵌当前模型结果，文章日期为2026-09-22但榜表独立更新日待核实；AA 2026-10-27报告max档Opus 5.5 68%、Astra 64%、Fable 5.1 60%，与这里high档分轨保留。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- agibenchmark@safe.ai

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 公开反馈渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 隐私政策

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### Drive资料目录

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方方法/介绍网页（不是论文PDF）", "url": "https://lastexam.ai/blog/hle-diamond"}

[来源1](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组只建立本地研究文件，不上传或声明已有Drive PDF。

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "新建近期热门中文研究条目；区分当前榜单与历史结果；缺项逐字段标记。"}

[来源](https://lastexam.ai/blog/hle-diamond)（访问 2026-11-07）
