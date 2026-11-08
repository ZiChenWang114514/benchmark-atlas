# IFEval

> Benchmark Constitution｜逐源深度核查：2026-11-08。采集日期不代表实验日期；待核实不等于未公开。

IFEval把长度、关键词、格式等指令转成确定性验证程序。它有prompt/instruction和strict/loose四套不同准确率；恢复四套原作者基线，避免用未说明指标的厂商总分掩盖差异。

导读依据：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）；[2](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（访问 2026-11-08）；[3](https://huggingface.co/datasets/google/IFEval)（访问 2026-11-08）。

## 基本信息

### 简称

IFEval

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 全称

Instruction-Following Evaluation

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 基准版本

原论文541提示、25种可验证指令；Google官方HF数据卡对应train split（评测用途，不代表建议把测试提示用于训练）。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）；[2](https://huggingface.co/datasets/google/IFEval)（访问 2026-11-08）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）。

### 发布日期

2023-11-14（arXiv初稿日期，不是数据集的单独发布日）

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）。

### 主板块

语言

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 领域

```json
[
 "可验证指令遵循"
]
```

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 许可与使用范围

google-research仓库Apache-2.0；Google官方HF数据卡另标apache-2.0。

来源：[1](https://github.com/google-research/google-research/blob/master/LICENSE)（访问 2026-11-08）；[2](https://huggingface.co/datasets/google/IFEval)（访问 2026-11-08）。

### 论文入口

https://arxiv.org/abs/2311.07911

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 官方代码

https://github.com/google-research/google-research/tree/master/instruction_following_eval

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 数据入口

https://huggingface.co/datasets/google/IFEval

> Google官方HF发布入口；原始代码与JSONL仍在google-research/instruction_following_eval。

来源：[1](https://huggingface.co/datasets/google/IFEval)（访问 2026-11-08）。

### 官方主页

https://github.com/google-research/google-research/tree/master/instruction_following_eval

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 论文标题

Instruction-Following Evaluation for Large Language Models

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

## 发起与维护

### 发起方

Google Research 研究团队；Jeffrey Zhou 的研究实习与 Yale 背景在论文说明。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 合作与作者单位

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 作者

```json
[
 "Zhou, Jeffrey"
 "Lu, Tianjian"
 "Mishra, Swaroop"
 "Brahma, Siddhartha"
 "Basu, Sujoy"
 "Luan, Yi"
 "Zhou, Denny"
 "Hou, Le"
]
```

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 维护方

官方公开代码托管于 google-research；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

来源：[1](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（访问 2026-11-07）。

### 资助与资源支持

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

## 设计目标

### 测量能力

通过可程序验证的约束客观评估指令遵循。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 与既有基准的差异

人工评测昂贵，模型裁判可能受偏差影响；需要可重复、确定性检查的指令。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

## 构建方式

### 题目来源

合成基础提示并添加 1–3 个可验证约束，再移除不合理组合及重写提示。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 出题者背景

研究团队设计约束与提示；不依赖领域知识考试出题。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 审核流程

人工检查全部提示，修正不自然或冲突约束。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 质量控制

同时报告严格和宽松判定；宽松版本处理格式等变换，但可能增加假阳性。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 去污染与泄漏控制

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

## 数据形式

### 规模与统计口径

541 条提示，25 类可验证指令。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 题型

带输出长度、关键词、格式等约束的开放文本生成

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 模态

文本

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 语言

英语

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 难度

约束类型及同一提示中的组合增加难度；不是学科知识难度分层。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 公开与隐藏划分

官方公开提示数据和验证程序；未核实独立隐藏测试集。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

## 评测方法

### 指标

prompt-level strict/loose accuracy 与 instruction-level strict/loose accuracy。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 评分规则

官方主程序分别调用 strict 与 loose 校验，输出两套JSONL；prompt级准确率为全部指令均通过的回答比例，不应与单条指令通过率混淆。

来源：[1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/evaluation_main.py)（访问 2026-11-07）。

### 提示、采样与工具设置

按原提示生成回答后调用官方检查器；不要把评分用文本清洗当作模型真正满足原格式。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 官方脚本

google-research/instruction_following_eval/evaluation_main.py；输入原始指令JSONL及含prompt、response的模型响应JSONL。

来源：[1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/README.md)（访问 2026-11-07）。

### 可比性警告

prompt-level 与 instruction-level、strict 与 loose 是四种不同指标，分数必须指明；宽松清洗也有假阳性风险。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

## 最新情况

### 核查时间

2026-11-08

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）；[2](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（访问 2026-11-08）。

### 最新数据状态

Google官方HF卡显示541行，25种指令以原论文为准；未编造语义版本号。

来源：[1](https://huggingface.co/datasets/google/IFEval)（访问 2026-11-08）；[2](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）。

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2023-11-14"
 }
]
```

> arXiv原始UTC时间已转换为；不等于数据集版本变更。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）。

### 饱和度与证据边界

原论文GPT-4 prompt-strict为76.89%；后续IFBench论文表3的定向IF-RLVR训练可达到IFEval 92.2（该文prompt-loose口径）。高分与可验证任务训练的泛化局限需分开，不能宣称所有指令能力已饱和。

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### 污染与已知问题

可程序验证的约束只覆盖部分真实指令能力；严格/宽松结果不等价，不能把格式容错理解为全面遵循。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 相关与衍生基准

IFBench是独立的58种OOD约束基准，扩展IFEval验证思路而非同一题集新版本；IFBench当前软件包兼容25种经典IFEval验证器。

来源：[1](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）。

## 榜单快照

### 采集日期

2026-11-08 （采集日，不是运行或榜单更新日）

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）。

### 官方结果入口

https://arxiv.org/abs/2311.07911

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 独立评测入口

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "GPT-4"
 "score": "76.89"
 "metric": "prompt-level strict accuracy (%)"
 "track": "作者论文表3 / prompt-level strict"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "PaLM 2 S"
 "score": "43.07"
 "metric": "prompt-level strict accuracy (%)"
 "track": "作者论文表3 / prompt-level strict"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "83.57"
 "metric": "instruction-level strict accuracy (%)"
 "track": "作者论文表3 / instruction-level strict"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "PaLM 2 S"
 "score": "55.76"
 "metric": "instruction-level strict accuracy (%)"
 "track": "作者论文表3 / instruction-level strict"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "79.30"
 "metric": "prompt-level loose accuracy (%)"
 "track": "作者论文表3 / prompt-level loose"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "PaLM 2 S"
 "score": "46.95"
 "metric": "prompt-level loose accuracy (%)"
 "track": "作者论文表3 / prompt-level loose"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "85.37"
 "metric": "instruction-level loose accuracy (%)"
 "track": "作者论文表3 / instruction-level loose"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "PaLM 2 S"
 "score": "59.11"
 "metric": "instruction-level loose accuracy (%)"
 "track": "作者论文表3 / instruction-level loose"
 "source_url": "https://arxiv.org/pdf/2311.07911"
 "result_type": "历史API基线；GPT-4 2023年11月、PaLM 2 S 2023年8月，具体checkpoint未列明"
 "snapshot_date": "2026-11-08 "
 }
 {
 "model": "Hunyuan-A13B（报告命名）"
 "score": 84.7
 "unit": "%"
 "metric": "IF-Eval，报告表3原标签"
 "scope": "Hunyuan-A13B 技术报告，slow-thinking；厂商自报，未明确对应本条四指标中的哪一个，不能与论文 prompt-strict 直接混比"
 "evaluation_date": "报告日期2026-09-23；精确运行日期待核实"
 "snapshot_date": "2026-11-07 （保留历史证据；未复开厂商报告）"
 "track": "Hunyuan-A13B厂商技术报告（四指标映射未知）"
 "rank": null
 }
]
```

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）。

### 覆盖与局限

补回原作者论文四套精确指标基线，不用一个未说明strict/loose的厂商IF-Eval数字替代它们。原项目README是评测程序入口，不是实时SOTA排行榜；保留旧厂商报告但不跨轨排名。

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-08）；[2](https://github.com/google-research/google-research/tree/master/instruction_following_eval/README.md)（访问 2026-11-08）。

## 联系方式

### 官方公开邮箱

```json
[
 "lehou@google.com"
]
```

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 仓库反馈

https://github.com/google-research/google-research/issues

来源：[1](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（访问 2026-11-07）。

### 官方社区

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）。

### 隐私与联系边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）。

## 原始文件

### 论文PDF

https://arxiv.org/pdf/2311.07911

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-07）。

### PDF SHA-256

5d7cedfd762af6d9ad13d8768de64fa65895b8ebc3f5e454454c5ffbd48124f2

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-08）。

### PDF字节数

```json
464152
```

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2311.07911)（访问 2026-11-08）。

### 已有文件夹

来源：。

### 其他官方文档

来源：。

### 已有 PDF归档

来源：。

## 变更记录

### 历次核查

```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-08"
 最近复核
 }
]
```

来源：[1](https://arxiv.org/abs/2311.07911)（访问 2026-11-07）；[2](https://arxiv.org/pdf/2311.07911)（访问 2026-11-07）；[3](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（访问 2026-11-07）；[4](https://arxiv.org/abs/2311.07911)（访问 2026-11-08）；[5](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（访问 2026-11-08）。
