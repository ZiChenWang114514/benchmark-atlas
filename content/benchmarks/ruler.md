# RULER

> 核验日期：2026-11-08。访问日期不等于发布或运行日期；无法证实的字段保留待核实。

RULER不是固定题库，而是一套可控制文本长度与任务复杂度的长上下文诊断生成器。它将检索扩展到多键/多值、多跳变量追踪、聚合和问答，核心问题是模型能否真正使用窗口内的信息，而非是否接受那么多token。

导读来源：[官方材料](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）；具体事实及历史访问日期见各字段。

## 基本信息

### 简称

RULER

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 全称

RULER

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 基准版本

原始RULER（13任务配置）；当前仓库另指向v1/v2新pipeline。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）

### 论文版本

v3；最近提交 2024-08-07

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 发布日期

2024-04-10（首个arXiv提交，不推定数据上线日）

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 主板块

语言

说明：Benchmark Constitution编辑归档，不是论文指定的唯一领域。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 领域标签

- 长上下文利用

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 许可与适用范围

代码 Apache-2.0；外部语料应另行遵循各自许可。

来源：[1](https://raw.githubusercontent.com/hsiehjackson/RULER/main/LICENSE)（访问 2026-11-07，）

### 论文

https://arxiv.org/abs/2404.06654

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 代码仓库

https://github.com/hsiehjackson/RULER

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 数据地址

https://github.com/hsiehjackson/RULER

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 官方主页

https://github.com/hsiehjackson/RULER

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 论文标题

RULER: What's the Real Context Size of Your Long-Context Language Models?

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

## 发起与维护

### 机构与发起关系

NVIDIA 研究团队。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 合作机构/署名单位

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 作者

- Hsieh, Cheng-Ping
- Sun, Simeng
- Kriman, Samuel
- Acharya, Shantanu
- Rekesh, Dima
- Jia, Fei
- Zhang, Yang
- Ginsburg, Boris

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 当前维护入口

官方公开代码托管于 hsiehjackson；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）

### 资助方

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

## 设计目标

### 衡量能力

检验模型实际可用上下文长度，而不只看标称窗口。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 设计背景

单一 needle-in-a-haystack 容易被模型攻克，不能代表长上下文中的多跳追踪、聚合与问答。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

## 构建方式

### 题目或数据来源

程序合成检索、多跳变量追踪、聚合与问答任务，可配置长度及复杂度。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 出题背景

研究团队设计可控生成器，不是人工逐题知识考试。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 审核流程

生成器根据任务规则产生可验证标准答案；精确人工逐条审查量待核实。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 质量控制

分任务及长度评测，以多种任务避免只测一种检索模式。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 去污染措施

检索、变量追踪与聚合样本由可控生成器及随机种子合成；问答使用SQuAD/HotpotQA、部分检索背景使用Paul Graham公开文章。新随机实例降低逐题记忆捷径，但公开问答来源不能保证训练无暴露。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2404.06654)（访问 2026-11-08，）

## 数据形式

### 规模

4类任务、13种已评测配置；样本可依随机种子、序列长度和任务复杂度生成，不是固定总题量。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）

### 题型

合成检索、变量追踪、聚合与问答

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 模态

文本

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 语言

英语任务模板；具体语料配置应固定

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 难度

通过长度、目标数量、变量链等控制难度，而非单一固定难度集。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 数据划分

生成代码及任务配置公开，可重新合成；需保存随机种子和配置以复现。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

## 评测方法

### 指标

任务准确率/目标召回，任务平均与按长度汇总的指标；以所用脚本定义为准。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 评分方式

按任务要求比较模型回答中的目标答案，再汇总任务与长度。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 提示与运行设置

原论文使用 greedy decoding、模型聊天模板与答案前缀；需记录 tokenizer、模板及长度设定。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 评测脚本

原始pipeline已deprecated；v1使用NVIDIA/RULER rulerv1-ns，v2使用rulerv2-ns及NeMo-Skills chsieh/ruler2；v2示例temperature=0、tokens_to_generate=16384。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）；[2](https://github.com/NVIDIA/RULER/tree/rulerv2-ns)（访问 2026-11-08，）

### 可比性提醒

不同 token 长度、任务子集、分词器和长度加权分数不能混比；Hunyuan报告的 QA 子任务不是13任务全量。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 数据版本与更新

官方README已将旧pipeline标为deprecated，指向NVIDIA/RULER的rulerv1-ns和rulerv2-ns分支；v1与v2结果不可无标记混合。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）

### 论文修订记录

- {"version": "v1", "submitted_at_kst": "2024-04-10", "timezone": ""}
- {"version": "v2", "submitted_at_kst": "2024-04-12", "timezone": ""}
- {"version": "v3", "submitted_at_kst": "2024-08-07", "timezone": ""}

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 饱和程度

原始13配置是已控制短上下文难度的诊断集合；README历史Avg最高96.0%，但长上下文和更复杂配置仍可能下降。不能将短长度或加权高分外推为全面饱和。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2404.06654)（访问 2026-11-08，）

### 争议与已知问题

标称上下文长度不等于有效窗口；长文本长度、任务复杂度和模板选择可能改变结论。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 衍生基准

官方另提供RULERv2 NeMo-Skills评测分支（rulerv2-ns），旧v1表不代表v2成绩。

来源：[1](https://github.com/NVIDIA/RULER/tree/rulerv2-ns)（访问 2026-11-08，）

## 榜单快照

### 快照访问日期

2026-11-08 （访问日，不是实验运行日）

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）

### 官方榜单入口

https://github.com/hsiehjackson/RULER

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）

### 第三方入口

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 可核验结果

- {"rank": "不设跨协议名次", "model": "Jamba-1.5-large* (94B/398B)", "score": 96.0, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.7, "8K": 96.6, "16K": 96.4, "32K": 96.0, "64K": 95.4, "128K": 95.1}, "claimed_length": "256k", "effective_length": ">128k", "wAvg_increasing": 95.7, "wAvg_decreasing": 96.3}
- {"rank": "不设跨协议名次", "model": "Gemini-1.5-pro", "score": 95.8, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.7, "8K": 95.8, "16K": 96.0, "32K": 95.9, "64K": 95.9, "128K": 94.4}, "claimed_length": "1M", "effective_length": ">128K", "wAvg_increasing": 95.5, "wAvg_decreasing": 96.1}
- {"rank": "不设跨协议名次", "model": "Qwen2.5-14B-Instruct-1M* (14B)", "score": 95.7, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 97.5, "8K": 97.1, "16K": 94.6, "32K": 94.9, "64K": 94.9, "128K": 92.2}, "claimed_length": "1M", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Qwen3-235B-A22B* (235B)", "score": 95.0, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 97.7, "8K": 97.2, "16K": 96.4, "32K": 95.1, "64K": 93.3, "128K": 90.6}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Qwen3-14B* (14B)", "score": 94.6, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 98.0, "8K": 97.8, "16K": 96.4, "32K": 96.1, "64K": 94.0, "128K": 85.1}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Jamba-1.5-mini (12B/52B)", "score": 93.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.6, "8K": 95.6, "16K": 94.8, "32K": 94.6, "64K": 92.8, "128K": 90.0}, "claimed_length": "256K", "effective_length": ">128K", "wAvg_increasing": 93.1, "wAvg_decreasing": 94.8}
- {"rank": "不设跨协议名次", "model": "Qwen3-32B* (32B)", "score": 93.7, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 98.4, "8K": 96.0, "16K": 96.2, "32K": 94.4, "64K": 91.8, "128K": 85.6}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "EXAONE-4.0-32B* (32B)", "score": 93.1, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.3, "8K": 94.9, "16K": 93.9, "32K": 93.6, "64K": 91.7, "128K": 88.2}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Qwen2.5-7B-Instruct-1M* (7B)", "score": 91.8, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.8, "8K": 95.3, "16K": 93.0, "32K": 91.1, "64K": 90.4, "128K": 84.4}, "claimed_length": "1M", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Qwen3-30B-A3B* (30B)", "score": 91.6, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.5, "8K": 97.0, "16K": 95.3, "32K": 92.4, "64K": 89.1, "128K": 79.2}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "GPT-4-1106-preview", "score": 91.6, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.6, "8K": 96.3, "16K": 95.2, "32K": 93.2, "64K": 87.0, "128K": 81.2}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 89.0, "wAvg_decreasing": 94.1}
- {"rank": "不设跨协议名次", "model": "Llama3.1 (70B)", "score": 89.6, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.5, "8K": 95.8, "16K": 95.4, "32K": 94.8, "64K": 88.4, "128K": 66.6}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 85.5, "wAvg_decreasing": 93.7}
- {"rank": "不设跨协议名次", "model": "Qwen3-8B* (8B)", "score": 89.1, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.3, "8K": 96.0, "16K": 91.8, "32K": 91.2, "64K": 82.1, "128K": 77.4}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Mistral-Large-2411 (123B)", "score": 86.0, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.4, "8K": 96.3, "16K": 95.3, "32K": 94.0, "64K": 85.9, "128K": 48.1}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 79.5, "wAvg_decreasing": 92.5}
- {"rank": "不设跨协议名次", "model": "Command-R-plus-0824 (104B)", "score": 87.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.0, "8K": 95.1, "16K": 94.0, "32K": 92.4, "64K": 85.4, "128K": 64.6}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 83.4, "wAvg_decreasing": 92.4}
- {"rank": "不设跨协议名次", "model": "Qwen2 (72B)", "score": 85.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.9, "8K": 96.1, "16K": 94.9, "32K": 94.1, "64K": 79.8, "128K": 53.7}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 79.6, "wAvg_decreasing": 92.3}
- {"rank": "不设跨协议名次", "model": "Command-R-plus (104B)", "score": 87.4, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.6, "8K": 95.2, "16K": 94.2, "32K": 92.0, "64K": 84.3, "128K": 63.1}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 82.7, "wAvg_decreasing": 92.1}
- {"rank": "不设跨协议名次", "model": "Command-R-0824 (32B)", "score": 88.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 94.7, "8K": 93.7, "16K": 93.1, "32K": 90.8, "64K": 86.6, "128K": 74.7}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 86.0, "wAvg_decreasing": 91.9}
- {"rank": "不设跨协议名次", "model": "GLM4 (9B)", "score": 89.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 94.7, "8K": 92.8, "16K": 92.1, "32K": 89.9, "64K": 86.7, "128K": 83.1}, "claimed_length": "1M", "effective_length": "64K", "wAvg_increasing": 88.0, "wAvg_decreasing": 91.7}
- {"rank": "不设跨协议名次", "model": "Llama3.1 (8B)", "score": 88.3, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.5, "8K": 93.8, "16K": 91.6, "32K": 87.4, "64K": 84.7, "128K": 77.0}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 85.4, "wAvg_decreasing": 91.3}
- {"rank": "不设跨协议名次", "model": "ProLong (8B)", "score": 88.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 94.5, "8K": 92.5, "16K": 92.3, "32K": 89.3, "64K": 83.2, "128K": 81.6}, "claimed_length": "512K", "effective_length": "32K", "wAvg_increasing": 86.6, "wAvg_decreasing": 91.2}
- {"rank": "不设跨协议名次", "model": "Command-R (35B)", "score": 88.3, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 93.8, "8K": 93.3, "16K": 92.4, "32K": 89.5, "64K": 84.9, "128K": 76.0}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 85.5, "wAvg_decreasing": 91.1}
- {"rank": "不设跨协议名次", "model": "MegaBeam-Mistral (7B)", "score": 89.1, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 93.8, "8K": 92.5, "16K": 92.0, "32K": 89.2, "64K": 83.7, "128K": 83.7}, "claimed_length": "512K", "effective_length": "32K", "wAvg_increasing": 87.3, "wAvg_decreasing": 91.0}
- {"rank": "不设跨协议名次", "model": "Mistral-Large-2407 (123B)", "score": 80.5, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 96.2, "8K": 96.1, "16K": 95.1, "32K": 93.0, "64K": 78.8, "128K": 23.7}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 70.6, "wAvg_decreasing": 90.4}
- {"rank": "不设跨协议名次", "model": "GradientAI/Llama3 (70B)", "score": 86.5, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.1, "8K": 94.4, "16K": 90.8, "32K": 85.4, "64K": 80.9, "128K": 72.1}, "claimed_length": "1M", "effective_length": "16K", "wAvg_increasing": 82.6, "wAvg_decreasing": 90.3}
- {"rank": "不设跨协议名次", "model": "Mixtral-8x22B (39B/141B)", "score": 81.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.6, "8K": 94.9, "16K": 93.4, "32K": 90.9, "64K": 84.7, "128K": 31.7}, "claimed_length": "64K", "effective_length": "32K", "wAvg_increasing": 73.5, "wAvg_decreasing": 90.3}
- {"rank": "不设跨协议名次", "model": "Yi (34B)", "score": 87.5, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 93.3, "8K": 92.2, "16K": 91.3, "32K": 87.5, "64K": 83.2, "128K": 77.3}, "claimed_length": "200K", "effective_length": "32K", "wAvg_increasing": 84.8, "wAvg_decreasing": 90.1}
- {"rank": "不设跨协议名次", "model": "Qwen3-4B* (4B)", "score": 85.2, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.1, "8K": 93.6, "16K": 91.0, "32K": 87.8, "64K": 77.8, "128K": 66.0}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "EXAONE-4.0-1.2B* (1.2B)", "score": 84.2, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 87.0, "8K": 86.7, "16K": 88.8, "32K": 81.1, "64K": 77.4, "128K": null}, "claimed_length": "64K", "effective_length": "32K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "不设跨协议名次", "model": "Phi3-mini (3.8B)", "score": 84.8, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 92.2, "8K": 91.5, "16K": 90.7, "32K": 87.5, "64K": 80.6, "128K": 66.7}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 80.9, "wAvg_decreasing": 88.7}
- {"rank": "不设跨协议名次", "model": "Phi3-medium (14B)", "score": 81.5, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 93.3, "8K": 93.2, "16K": 91.1, "32K": 86.8, "64K": 78.6, "128K": 46.1}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 74.8, "wAvg_decreasing": 88.3}
- {"rank": "不设跨协议名次", "model": "Mixtral-8x7B (12.9B/46.7B)", "score": 80.4, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 94.9, "8K": 92.1, "16K": 92.5, "32K": 85.9, "64K": 72.4, "128K": 44.5}, "claimed_length": "32K", "effective_length": "32K", "wAvg_increasing": 72.8, "wAvg_decreasing": 87.9}
- {"rank": "不设跨协议名次", "model": "GradientAI/Llama3 (8B)", "score": 82.4, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 92.8, "8K": 90.3, "16K": 85.7, "32K": 79.9, "64K": 76.3, "128K": 69.5}, "claimed_length": "1M", "effective_length": "16K", "wAvg_increasing": 78.5, "wAvg_decreasing": 86.3}
- {"rank": "不设跨协议名次", "model": "FILM-7B* (7B)", "score": 75.5, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；外部作者自报", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 92.8, "8K": 88.2, "16K": 88.1, "32K": 86.9, "64K": 70.1, "128K": 27.1}, "claimed_length": "32K", "effective_length": "32K", "wAvg_increasing": 66.4, "wAvg_decreasing": 84.7}
- {"rank": "不设跨协议名次", "model": "InternLM2.5 (7B)", "score": 80.9, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 88.1, "8K": 85.5, "16K": 84.5, "32K": 82.7, "64K": 75.5, "128K": 68.9}, "claimed_length": "1M", "effective_length": "4K", "wAvg_increasing": 77.8, "wAvg_decreasing": 83.9}
- {"rank": "不设跨协议名次", "model": "Mistral (7B)", "score": 68.4, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 93.6, "8K": 91.2, "16K": 87.2, "32K": 75.4, "64K": 49.0, "128K": 13.8}, "claimed_length": "32K", "effective_length": "16K", "wAvg_increasing": 55.6, "wAvg_decreasing": 81.2}
- {"rank": "不设跨协议名次", "model": "Mistral-Nemo", "score": 66.2, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 87.8, "8K": 87.2, "16K": 87.7, "32K": 69.0, "64K": 46.8, "128K": 19.0}, "claimed_length": "128K", "effective_length": "16K", "wAvg_increasing": 54.7, "wAvg_decreasing": 77.8}
- {"rank": "不设跨协议名次", "model": "GLM3 (6B)", "score": 69.6, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 87.8, "8K": 83.4, "16K": 78.6, "32K": 69.9, "64K": 56.0, "128K": 42.0}, "claimed_length": "128K", "effective_length": "4K", "wAvg_increasing": 62.0, "wAvg_decreasing": 77.2}
- {"rank": "不设跨协议名次", "model": "LWM (7B)", "score": 72.8, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 82.3, "8K": 78.4, "16K": 73.7, "32K": 69.1, "64K": 68.1, "128K": 65.0}, "claimed_length": "1M", "effective_length": "<4K", "wAvg_increasing": 69.9, "wAvg_decreasing": 75.7}
- {"rank": "不设跨协议名次", "model": "DBRX (36B/132B)", "score": 56.3, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 95.1, "8K": 93.8, "16K": 83.6, "32K": 63.1, "64K": 2.4, "128K": 0.0}, "claimed_length": "32K", "effective_length": "8K", "wAvg_increasing": 38.0, "wAvg_decreasing": 74.7}
- {"rank": "不设跨协议名次", "model": "Qwen1.5 (72B)", "score": 55.7, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 94.9, "8K": 93.8, "16K": 78.0, "32K": 67.8, "64K": 0.0, "128K": 0.0}, "claimed_length": "32K", "effective_length": "8K", "wAvg_increasing": 37.5, "wAvg_decreasing": 74.0}
- {"rank": "不设跨协议名次", "model": "Together (7B)", "score": 50.3, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 88.2, "8K": 81.1, "16K": 69.4, "32K": 63.0, "64K": 0.0, "128K": 0.0}, "claimed_length": "32K", "effective_length": "4K", "wAvg_increasing": 33.8, "wAvg_decreasing": 66.7}
- {"rank": "不设跨协议名次", "model": "LongChat (7B)", "score": 49.1, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 84.7, "8K": 79.9, "16K": 70.8, "32K": 59.3, "64K": 0.0, "128K": 0.0}, "claimed_length": "32K", "effective_length": "<4K", "wAvg_increasing": 33.1, "wAvg_decreasing": 65.2}
- {"rank": "不设跨协议名次", "model": "LongAlpaca (13B)", "score": 36.3, "metric": "README Avg（%），按原表保留不重新计算", "track": "RULERv1历史表；项目所列实验", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "来源表格精确转录；非本库重跑", "by_length": {"4K": 60.6, "8K": 57.0, "16K": 56.6, "32K": 43.6, "64K": 0.0, "128K": 0.0}, "claimed_length": " 32K", "effective_length": "<4K", "wAvg_increasing": 24.7, "wAvg_decreasing": 47.9}

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）

### 榜单覆盖边界

完整转录README中44条有Avg的模型记录，保留六长度、两类加权指标与外部自报星号；4K基线Llama2-7B=85.6不具备六长度Avg，未塞入同一平均榜。表格行序不是统一排名，未补未给出的更新时间。

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）

## 联系方式

### 公开研究联系

- chsieh@nvidia.com
- simengs@nvidia.com

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 公开反馈渠道

https://github.com/hsiehjackson/RULER/issues

来源：[1](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）

### 官方社交账号

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）

### 联系方式原则

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07，）

## 原始文件

### 论文原件

- **id**：1jrXqZ9i4OPxWrgbz9D-xEwGusBAFeiiQ
- **webViewLink**：

来源：[1]( 2026-11-07，）

### 原始PDF地址

https://arxiv.org/pdf/2404.06654

来源：[1](https://arxiv.org/pdf/2404.06654)（访问 2026-11-08，）

### 原始文件SHA-256

8a4bc6ca28d84570eec7f42652400c2121f4c8bc361701634e596772e396fc22

说明：实际下载原始PDF字节计算；不据此更改既有文件。

来源：[1](https://arxiv.org/pdf/2404.06654)（访问 2026-11-08，）

### 原始文件字节数

682955

来源：[1](https://arxiv.org/pdf/2404.06654)（访问 2026-11-08，）

### 文件夹

- **id**：1tj6vWFyQX2ASPe0dVeBL5yRrcunkap7I
- **webViewLink**：

来源：[1]( 2026-11-07，）

### 其他文档

- {"kind": "中文介绍", "id": "1BXarcTj97jqzXNsQCTNfsSGu4mnKXyY3yYCp-eiUak4", "webViewLink": "

来源：[1]( 2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://arxiv.org/abs/2404.06654)（访问 2026-11-08，）；[2](https://arxiv.org/pdf/2404.06654)（访问 2026-11-08，）；[3](https://github.com/hsiehjackson/RULER)（访问 2026-11-07，）；[4](https://github.com/hsiehjackson/RULER)（访问 2026-11-08，）
