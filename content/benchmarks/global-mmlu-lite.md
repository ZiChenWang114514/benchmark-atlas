# Global-MMLU-Lite

> 核验日期：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未知不等于未公开。热度与成绩快照分开记录。

编辑状态：官方存在性已核验；字段级研究快照；note: trending: B

## 基本信息

### 简称

Global-MMLU-Lite

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 全称

Global-MMLU-Lite

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 基准版本

3.0

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 论文版本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 发布日期

2024-12首发；3.0于2026-05更新（数据卡仅给月份）

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 主板块

语言

> Benchmark Atlas 编辑分类。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 领域标签

- 多语言

> 编辑标签；空列表表示尚未补充细分标签。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 许可证

Apache 2.0（数据集）

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 论文入口

https://arxiv.org/abs/2412.03304

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 官方代码

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 官方入口

https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 论文标题

Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

## 发起与维护

### 发起机构

Cohere Labs

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 合作方

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 作者

Shivalika Singh、Angelika Romanou、Clémentine Fourrier、David I. Adelani等；全量作者以论文为准。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 维护方

Cohere Labs与Open Science社区

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 资助

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

## 设计目标

### 衡量能力

多语言知识与推理，并独立分析文化敏感CS和文化无关CA题表现。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 设计背景

单纯机器翻译英文MMLU既有翻译伪影也保留西方知识偏差；人工译校与文化标注使评估更可解释。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

## 构建方式

### 题目来源

从MMLU选题，每语言200文化敏感CS与200文化无关CA。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 出题者背景

专业标注员和Cohere Labs社区贡献者。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 审核流程

Lite题目全部人工翻译或人工后编辑；文化标注以多位标注员票数记录。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 质量控制

CS/CA均衡；保留country、region、culture、time_sensitive等元信息。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 去污染

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

## 数据形式

### 题量与规模

test 9,200条（23语言，每语言400）；dev 4,655条（22语言）。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 题型

四选一A/B/C/D，含sample_id、subject、question、options、answer和文化标注字段。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 模态

- 文本

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 语言

23语言（3.0数据卡）；原论文15语言与AA支持子集另列，不等同当前全部23语言。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 难度

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 公开与隐藏划分

公开test与dev；不要把数据查看器总行数14,000当作精确测试题量。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

## 评测方法

### 指标

准确率/pass@1；宜分语言与CS/CA报告。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 评分方式

AA使用正则提取四选一答案，pass@1，各题1次，无工具。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 提示与运行设置

AA标准zero-shot指令；约400题/语言。原论文5-shot实验不能不加说明与AA混排。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 官方评测脚本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 可比性警示

全量Global-MMLU是42语言而非Lite 23语言；AA方法页仍写约6,000题并列16个支持语言，语言计数与约数之间需复核，不能据此声称覆盖全部3.0。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度B：本轮近期热度主要由单一评测机构持续运行/展示支持，不表示行业广泛采纳。

- AA当前Multilingual Index基于该测试，另有独立评测页。 [来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（证据日期 2026-11-07；访问 2026-11-07）

### 核验日期

2026-11-07 KST / Asia/Seoul

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 当前版本与2026H2使用证据

- **version**：3.0
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking", "date": "2026-11-07", "date_type": "observed_on", "note": "AA当前Multilingual Index基于该测试，另有独立评测页。"}]

> 热度B：本轮近期热度主要由单一评测机构持续运行/展示支持，不表示行业广泛采纳。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 修订历史

Lite 1.0：2024-12，15语言；2.0：2025-12加入Albanian/Burmese/Welsh；3.0：2026-05扩展至23语言。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 饱和情况

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 污染与争议

标注文化敏感不等于已解决文化包容性；社区贡献分布不均、方言覆盖有限。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 衍生与版本关系

同族Global-MMLU全量不再拆条；与OpenAI MMMLU存在部分翻译源重叠，但不是同一题集。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 官方榜单入口

https://artificialanalysis.ai/evaluations/global-mmlu-lite

[来源1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

### 第三方评测入口

https://artificialanalysis.ai/evaluations/global-mmlu-lite

[来源1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "Gemini 3.1 Pro Preview", "score": 93.2, "metric": "AA Global-MMLU-Lite accuracy %", "source_url": "https://artificialanalysis.ai/evaluations/global-mmlu-lite", "source_date": "待核实", "collected_at": "2026-11-07 KST"}
- {"rank": 2, "model": "Gemini 3 Flash Preview (Non-reasoning)", "score": 92.7, "metric": "AA Global-MMLU-Lite accuracy %", "source_url": "https://artificialanalysis.ai/evaluations/global-mmlu-lite", "source_date": "待核实", "collected_at": "2026-11-07 KST"}
- {"rank": 3, "model": "Gemini 3 Pro Preview (High)", "score": 92.2, "metric": "AA Global-MMLU-Lite accuracy %", "source_url": "https://artificialanalysis.ai/evaluations/global-mmlu-lite", "source_date": "待核实", "collected_at": "2026-11-07 KST"}

[来源1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

### 覆盖与时效说明

当前网页可见结果；页面未标明榜单更新日，不能以采集日代替更新日。

[来源1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 公开反馈渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 隐私政策

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2412.03304

> 同族原始论文，不冒称3.0独立论文。

[来源1](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 原始PDF SHA-256

33355d08932663acd0631ad63c0d35977fd6944c22f28cc802abdba5c91baa8e

> 本轮实际获取源站PDF字节并计算；未上传Drive。

[来源](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）

### 原始PDF字节数

7733572

> 本轮实际获取源站PDF字节并计算；未上传Drive。

[来源](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）

### Drive资料目录

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方方法/介绍网页（不是论文PDF）", "url": "https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite"}

[来源1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组只建立本地研究文件，不上传或声明已有Drive PDF。

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "新建近期热门中文研究条目；区分当前榜单与历史结果；缺项逐字段标记。"}

[来源](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）
