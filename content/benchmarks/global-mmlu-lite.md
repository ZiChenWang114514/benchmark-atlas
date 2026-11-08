# Global-MMLU-Lite

> Benchmark Constitution，核查日期：2026-11-07。未知仍保留待核实；访问日不冒充实验日。

Global-MMLU-Lite用人工翻译或后编辑的MMLU子集评估多语言能力，并将文化敏感性与模型表现分开分析。当前3.0数据卡的23语言范围不同于原论文15语言实验和AA实现覆盖，不应只凭同名将三者合并。

导读来源：[https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）; [https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）; [https://arxiv.org/abs/2412.03304](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

## 1. 基本信息

### 简称

Global-MMLU-Lite

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 全称

Global-MMLU-Lite

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 数据/协议版本

3.0

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 论文版本

v2；2025-02-19（论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 发布日期及口径

2024-12首发；3.0于2026-05更新（数据卡仅给月份）

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 主板块

语言

说明：Benchmark Constitution 编辑分类。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 子领域

- 多语言

说明：编辑标签；空列表表示尚未补充细分标签。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 许可证

Apache 2.0（数据集）

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2412.03304

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 代码入口

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 数据入口

https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 官方主页

https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 论文标题

Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）


## 2. 发起与维护

### 发起团队

Cohere Labs

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 合作及署名机构

Cohere For AI社区及付费语言专家共同完成文化标注和译校；本字段只陈述贡献，不把所有作者单位视为正式合作机构。

来源：[1](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 作者

Shivalika Singh、Angelika Romanou、Clémentine Fourrier、David I. Adelani等；全量作者以论文为准。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 维护方

Cohere Labs与Open Science社区

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 资助

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）


## 3. 设计目标

### 评测能力

多语言知识与推理，并独立分析文化敏感CS和文化无关CA题表现。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 设计动机

单纯机器翻译英文MMLU既有翻译伪影也保留西方知识偏差；人工译校与文化标注使评估更可解释。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）


## 4. 构建方式

### 材料来源

从MMLU选题，每语言200文化敏感CS与200文化无关CA。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 编制背景

专业标注员和Cohere Labs社区贡献者。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 审核流程

Lite题目全部人工翻译或人工后编辑；文化标注以多位标注员票数记录。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 质量控制

CS/CA均衡；保留country、region、culture、time_sensitive等元信息。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 去污染边界

沿用公开MMLU题源，人工翻译与文化标注改进译质和解释性，但不构成消除预训练接触的保证；专项训练污染审计待核实。

来源：[1](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）


## 5. 数据形式

### 规模

test 9,200条（23语言，每语言400）；dev 4,655条（22语言）。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 题型

四选一A/B/C/D，含sample_id、subject、question、options、answer和文化标注字段。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 模态

- 文本

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 语言

23语言（3.0数据卡）；原论文15语言与AA支持子集另列，不等同当前全部23语言。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 难度

沿用MMLU学科问题，不另设Lite统一难度等级；CS/CA是文化敏感性标签，不是简单/困难标签。

来源：[1](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 公开及隐藏划分

公开test与dev；不要把数据查看器总行数14,000当作精确测试题量。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）


## 6. 评测方法

### 指标

准确率/pass@1；宜分语言与CS/CA报告。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 计分

AA使用正则提取四选一答案，pass@1，各题1次，无工具。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 提示与运行设置

AA标准zero-shot指令；约400题/语言。原论文5-shot实验不能不加说明与AA混排。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 评测入口

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 可比性边界

全量Global-MMLU是42语言而非Lite 23语言；AA方法页仍写约6,000题并列16个支持语言，语言计数与约数之间需复核，不能据此声称覆盖全部3.0。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[3](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）


## 7. 最新情况

### 核查日

2026-11-07（指定采集日期）

来源：[1](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 已核实版本

version：3.0；heat_confidence：B；evidence_2026_h2：- url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；date_type：observed_on；note：AA当前Multilingual Index基于该测试，另有独立评测页。

说明：热度B：近期热度主要由单一评测机构持续运行/展示支持，不表示行业广泛采纳。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2024-12-04；timezone：；- version：v2；submitted_at：2025-02-19；timezone：

来源：[1](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### 饱和情况

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 已知问题

标注文化敏感不等于已解决文化包容性；社区贡献分布不均、方言覆盖有限。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 衍生关系

同族Global-MMLU全量不再拆条；与OpenAI MMMLU存在部分翻译源重叠，但不是同一题集。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）；[2](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）


## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不代替榜单更新或实验日期）

来源：[1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

### 官方结果入口

https://artificialanalysis.ai/evaluations/global-mmlu-lite

来源：[1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

### 第三方结果入口

https://artificialanalysis.ai/evaluations/global-mmlu-lite

来源：[1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Artificial Analysis独立评测 | 1 | Gemini 3.1 Pro Preview | 93.2 | accuracy % | [原始来源](https://artificialanalysis.ai/evaluations/global-mmlu-lite)；采集2026-11-07；待核实（页面未显示测量/更新日） |
| Artificial Analysis独立评测 | 2 | Gemini 3 Flash Preview (Non-reasoning) | 92.7 | accuracy % | [原始来源](https://artificialanalysis.ai/evaluations/global-mmlu-lite)；采集2026-11-07；待核实（页面未显示测量/更新日） |
| Artificial Analysis独立评测 | 3 | Gemini 3 Pro Preview (High) | 92.2 | accuracy % | [原始来源](https://artificialanalysis.ai/evaluations/global-mmlu-lite)；采集2026-11-07；待核实（页面未显示测量/更新日） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

当前网页可见结果；页面未标明榜单更新日，不能以采集日代替更新日。

来源：[1](https://artificialanalysis.ai/evaluations/global-mmlu-lite)（访问 2026-11-07）


## 9. 联系方式

### 公开研究联系邮箱

- shivalika@cohere.com
- beyza@cohere.com
- sarahooker@cohere.com

来源：[1](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）

### 问题反馈

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 官方账号

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 隐私政策

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）


## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2412.03304

说明：同族原始论文，不冒称3.0独立论文。

来源：[1](https://arxiv.org/abs/2412.03304)（访问 2026-11-07）

### PDF SHA-256

33355d08932663acd0631ad63c0d35977fd6944c22f28cc802abdba5c91baa8e

说明：下载原始PDF字节的SHA-256；与既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）

### PDF字节数

7733572

来源：[1](https://arxiv.org/pdf/2412.03304)（访问 2026-11-07）

### 文件夹

待核实

说明：已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### 其他原始材料

- type：官方方法/介绍网页（不是论文PDF）；url：https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）

### PDF

待核实

说明：本组只建立本地研究文件，不上传或声明已有 PDF。

来源：[1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite)（访问 2026-11-07）


## 11. 变更记录

### 本页修订

- date：2026-11-07；timezone：；change：新建近期热门中文研究条目；区分当前榜单与历史结果；缺项逐字段标记。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）

