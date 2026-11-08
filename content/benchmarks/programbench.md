# ProgramBench

> 深度核验：2026-11-08。访问日不等于发布日期或实验运行日；未知保留，不推定“未公开”。

ProgramBench要求Agent只凭可执行程序及文档，从零构建行为匹配的软件项目。受评Agent不能看原源码、不能联网或反编译；构建测试的Agent却可参考源码和现有测试，两个阶段的权限必须区分。主指标是全部隐藏测试通过的任务比例，平均测试通过率和95%阈值只是辅助诊断。

最近复核

## 1. 基本信息

### 简称

ProgramBench

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 全称

ProgramBench

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 数据版本

公开200任务发布集，代码与生成测试分开发布；以任务目录的仓库短commit固定原程序，而非自拟v1。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 论文版本

arXiv:2605.03546v1；abs当前仅列v1。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 发布时间

论文首发：2026-05-05 18:17:02；PDF封面另标May 6, 2026，日期口径分开。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 板块

代码

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 子领域

```json
[
 "从零程序重建"
 "软件架构"
 "行为等价测试"
 "代码Agent"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 许可

评测仓库MIT；HF卡元数据标MIT，但任务内附原仓库LICENSE与ATTRIBUTION。生成测试可能借鉴原测试，GPL/LGPL/MPL等衍生部分仍受原许可约束，不能笼统称所有任务无条件MIT。

[1](https://raw.githubusercontent.com/facebookresearch/ProgramBench/main/LICENSE)（访问 2026-11-08）；[2](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2605.03546

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 代码

https://github.com/facebookresearch/ProgramBench

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/programbench/ProgramBench-Tests

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/facebookresearch/ProgramBench/main/README.md)（访问 2026-11-08）

### 官方主页

https://programbench.com

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 论文题名

ProgramBench: Can Language Models Rebuild Programs From Scratch?

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## 2. 发起与维护

### 发起方

```json
[
 "Meta Superintelligence Labs"
 "Stanford University"
 "Harvard University"
]
```

[1](https://programbench.com)（访问 2026-11-07）

### 合作单位

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 作者

```json
[
 "John Yang"
 "Kilian Lieret"
 "Jeffrey Ma"
 "Parth Thakkar"
 "Dmitrii Pedchenko"
 "Sten Sootla"
 "Emily McMilin"
 "Pengcheng Yin"
 "Rui Hou"
 "Gabriel Synnaeve"
 "Diyi Yang"
 "Ofir Press"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 维护方

facebookresearch/ProgramBench团队；HF公开维护联系人John Yang、Kilian Lieret。

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/facebookresearch/ProgramBench/main/README.md)（访问 2026-11-08）

### 资助

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 3. 设计目标

### 目标能力

仅给可执行程序与文档，自行设计架构、选择语言并从零实现行为等价程序。

[1](https://programbench.com)（访问 2026-11-07）

### 相对既有评测的缺口

不提供函数签名、类骨架或预设目录，区别于局部bug修复及填空式整仓生成。

[1](https://programbench.com)（访问 2026-11-07）

## 4. 构建方式

### 题目与标签来源

200个开源项目的可执行程序及文档。必须区分阶段：构建测试的agent能参考原源码和现有测试；接受评测的重建agent不能访问这些源码/测试。

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 出题/标注背景

作者来自Meta Superintelligence Labs、Stanford与Harvard；测试由agent驱动生成，不是200题均由人工逐题原创。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 审核流程

agent探索原程序，覆盖率引导fuzz生成行为断言，收集现有行为测试。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 质量控制

静态linter筛弱断言；删除不能稳定通过原程序或能通过dummy程序的测试。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 去污染与隔离

离线沙箱、原二进制仅可执行，不允许反编译、源码检索或包装原程序；原仓库公开带来潜在记忆风险。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## 5. 数据形式

### 规模

200任务；论文版本共248,853测试函数。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 题型

完整源码项目与build脚本生成，行为测试比较标准输出/错误、退出码与文件副作用。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 模态

```json
[
 "程序二进制"
 "文档"
 "源代码"
 "终端交互"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 语言

参考程序：Rust 107、Go 46、C 33、C++ 12、Haskell 1、Java 1；HF卡标英语。重建模型可自选实现语言。

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 难度

HF卡：27 easy、120 medium、18 hard、35 unrated；这是任务元数据，不是按本次模型得分重分桶。

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 公开/隐藏划分

200任务与AI生成行为测试公开发布；测试在一次受评agent运行中隐藏。公开发布不代表可在推理时查看断言。

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

## 6. 评测方法

### 指标

Fully Resolved/Resolved：全部隐藏行为测试通过；Almost Resolved：至少95%测试通过；Raw Pass Rate：任务内测试通过率平均。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 判分

编译提交实现后用行为测试比较原程序，不靠LLM主观评分；有限测试不能证明所有输入等价。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 提示/推理设置

mini-SWE-agent、1000步、6小时，离线cleanroom；Vals统一bash工具与沙箱。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 官方实现

官方代码入口为facebookresearch/ProgramBench，论文提供数据构建和评测流程。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 可比性边界

官网2026-10-22与Vals 2026-11-05的样本/运行结果分开；Fully Resolved不是Raw Pass Rate，也不是95%测试阈值。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 7. 最新情况

### 核验日

2026-11-08

[1](https://programbench.com)（访问 2026-11-08）

### 本次版本快照

```json
{
 "version": "公开200任务及ProgramBench-Tests（访问日快照，未自拟语义版本）"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://programbench.com"
 "date": "2026-10-22"
 "note": "官方榜单自写更新日。"
 }
 {
 "url": "https://www.vals.ai/benchmarks/programbench"
 "date": "2026-11-05"
 "note": "Vals独立评测榜单自写更新日。"
 }
 ]
}
```

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）；[2](https://programbench.com)（访问 2026-11-08）

### 论文修订

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-05-05"
 }
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 饱和情况

官网2026-10-22最高Fully Resolved 18.5%，Almost Resolved 70.5%；Vals 2026-11-05最高Fully Resolved 18.50%。全部测试通过仍是严格主指标，不能把较高Raw Pass Rate当作完全解决。

[1](https://programbench.com)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

### 污染/限制/争议

原仓库公开，存在记忆风险；官网报告跨语言实现消融并继续监测。断网、execute-only权限与禁反编译用于阻止源码复制，不能证明训练语料从未见过项目。有限测试无法证明所有输入行为等价；测试可能受原仓库copyleft条款约束。

[1](https://programbench.com)（访问 2026-11-08）；[2](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 衍生与相关版本

官网交叉推荐SWE-sweep，但未据此把它认定为ProgramBench新版或把单项任务拆为独立benchmark。

[1](https://programbench.com)（访问 2026-11-08）

## 8. 榜单快照

### 采集日期

2026-11-08 （采集日，不是实验运行日）

[1](https://programbench.com)（访问 2026-11-08）

### 官方结果入口

https://programbench.com

[1](https://programbench.com)（访问 2026-11-07）

### 第三方入口

https://www.vals.ai/benchmarks/programbench

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| 官方 / 200任务 / mini-SWE-agent | 1 | [Claude Opus 5.5 (xhigh)](https://programbench.com) | 18.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 2 | [Claude Fable 5.1 (xhigh)](https://programbench.com) | 9.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 3 | [Muse Wonder Full](https://programbench.com) | 8.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 4 | [Muse Wonder (xhigh)](https://programbench.com) | 5.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 5 | [GPT 6 Astra (max)](https://programbench.com) | 5.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 6 | [Claude Opus 5 (xhigh)](https://programbench.com) | 4.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 7 | [Muse Spark 1.3 (max)](https://programbench.com) | 2.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 8 | [Muse Spark 1.3 (xhigh)](https://programbench.com) | 1.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 9 | [GPT-5.6 Sol (xhigh)](https://programbench.com) | 1.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 10 | [GPT 5.5 (xhigh)](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 11 | [GPT 5.5 (high)](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 12 | [Gemini 3.6 Flash](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 13 | [GPT-5.6 Sol](https://programbench.com) | 0.5 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 14 | [Claude Opus 4.8 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 15 | [GLM-5.2](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 16 | [Gemini 3.7 Flash](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 17 | [Muse Spark 1.2 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 18 | [Claude Opus 4.7 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 19 | [Muse Spark 1.1 (xhigh)](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 20 | [Gemini 3.5 Flash](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 21 | [Claude Opus 4.7](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 22 | [Claude Opus 4.6](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 23 | [GPT 5.5](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 24 | [Claude Sonnet 4.6](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 25 | [GPT 5.4](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 26 | [Gemini 3.1 Pro](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 27 | [Gemini 3 Flash](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 28 | [Claude Haiku 4.5](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 29 | [GPT 5.4 mini](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| 官方 / 200任务 / mini-SWE-agent | 30 | [GPT 5 mini](https://programbench.com) | 0.0 | Fully Resolved (%) | 2026-10-22 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 1 | [Claude Opus 5.5](https://www.vals.ai/benchmarks/programbench) | 18.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 2 | [Claude Fable 5.1](https://www.vals.ai/benchmarks/programbench) | 7.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 3 | [Claude Sonnet 5.5](https://www.vals.ai/benchmarks/programbench) | 6.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 4 | [GPT-6 Astra](https://www.vals.ai/benchmarks/programbench) | 5.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 5 | [GPT-6.1 Sol](https://www.vals.ai/benchmarks/programbench) | 3.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 6 | [Claude Opus 5](https://www.vals.ai/benchmarks/programbench) | 3.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 7 | [Gemini 4 Argon](https://www.vals.ai/benchmarks/programbench) | 2.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 8 | [Claude Haiku 5.5](https://www.vals.ai/benchmarks/programbench) | 2.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 9 | [Muse Spark 1.3 Max](https://www.vals.ai/benchmarks/programbench) | 2.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 10 | [Claude Fable 5](https://www.vals.ai/benchmarks/programbench) | 2.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 11 | [GPT-6 Sol](https://www.vals.ai/benchmarks/programbench) | 2.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 12 | [Kimi K3](https://www.vals.ai/benchmarks/programbench) | 2.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 13 | [GPT-5.6 Sol](https://www.vals.ai/benchmarks/programbench) | 1.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 14 | [GLM 5.3](https://www.vals.ai/benchmarks/programbench) | 1.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 15 | [Grok 4.6](https://www.vals.ai/benchmarks/programbench) | 1.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 16 | [Claude Opus 4.8](https://www.vals.ai/benchmarks/programbench) | 1.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 17 | [Gemini 3.8 Flash](https://www.vals.ai/benchmarks/programbench) | 1.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 18 | [Grok 4.7](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 19 | [MiMo V2.6 Flash](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 20 | [DeepSeek V4.1 Flash](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 21 | [GPT-5.6 Terra](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 22 | [Muse Spark 1.3](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 23 | [MiMo V2.6 Pro](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 24 | [Inkling 2 Small](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 25 | [GPT 5.5](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 26 | [GLM 5.2](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 27 | [GPT-6 Luna](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 28 | [Wonder Full](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 29 | [GPT 5.4 (high)](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 30 | [Muse Spark 1.2](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 31 | [Claude Sonnet 4.6](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 32 | [Inkling Small](https://www.vals.ai/benchmarks/programbench) | 0.5 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 33 | [Hy4 Preview](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 34 | [DeepSeek V4 Pro 0813](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 35 | [Claude Sonnet 5](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 36 | [Qwen 3.8 Max](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 37 | [Gemini 3.7 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 38 | [Claude Opus 4.7](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 39 | [GPT-5.6 Luna](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 40 | [DeepSeek V4 Flash 0731](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 41 | [GPT 5.4 (xhigh)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 42 | [GLM 5.3 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 43 | [Grok 4.5](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 44 | [GPT 5.4 Mini](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 45 | [Gemini 3.6 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 46 | [Muse Spark 1.1](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 47 | [Gemini 3.5 Flash](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 48 | [GLM 5.1](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 49 | [Gemini 3.1 Pro Preview (02/26)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 50 | [Qwen 3.6 Plus](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 51 | [Qwen 3.8 27B](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 52 | [Kimi K2.7 Code](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 53 | [Kimi K2.6](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 54 | [Nemotron 3 Ultra](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 55 | [DeepSeek V4](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 56 | [Gemini 3 Flash (12/25)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 57 | [Gemini 3.5 Flash Lite](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 58 | [Claude Haiku 4.5 (Thinking)](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 59 | [Grok 4.3](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 60 | [Nemotron 3.5 Lightning](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 61 | [Laguna XS.2](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 62 | [Inkling](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 63 | [Laguna M.1](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 64 | [Gemini 3.1 Flash Lite Preview](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals独立复测 / 200任务 / mini-SWE-agent | 65 | [MiniMax-M2.7](https://www.vals.ai/benchmarks/programbench) | 0.0 | Fully Resolved (%) | 2026-11-05 |
| Vals原始测试通过率诊断表 | — | [Claude Opus 5.5](https://www.vals.ai/benchmarks/programbench) | 87.0 | Raw Pass Rate (%) | 2026-11-05 |
| Vals原始测试通过率诊断表 | — | [GPT-6 Astra](https://www.vals.ai/benchmarks/programbench) | 85.4 | Raw Pass Rate (%) | 2026-11-05 |
| Vals原始测试通过率诊断表 | — | [GPT-6.1 Sol](https://www.vals.ai/benchmarks/programbench) | 85.3 | Raw Pass Rate (%) | 2026-11-05 |
| Vals原始测试通过率诊断表 | — | [Gemini 4 Argon](https://www.vals.ai/benchmarks/programbench) | 83.7 | Raw Pass Rate (%) | 2026-11-05 |
| Vals原始测试通过率诊断表 | — | [Claude Fable 5.1](https://www.vals.ai/benchmarks/programbench) | 82.7 | Raw Pass Rate (%) | 2026-11-05 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://programbench.com)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

### 覆盖与限制

官网31行中30条有数字名次，Vals全榜65行，另收录5行Raw Pass Rate诊断表。独立榜分开，不以相同18.5%断言同一运行。官网Almost Resolved是比例；Vals诊断表的130/37等是任务数，不是130%/37%。

[1](https://programbench.com)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-08）

## 9. 联系方式

### 项目公开邮箱

```json
[
 "johnby@meta.com"
 "klieret@meta.com"
]
```

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### GitHub反馈

https://github.com/facebookresearch/ProgramBench/issues

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

### 官方社交

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 隐私边界

仅记录HF卡和论文公开的项目邮箱及Issues，不推测私人联系方式。

[1](https://huggingface.co/datasets/programbench/ProgramBench-Tests/raw/main/README.md)（访问 2026-11-08）

## 10. 原始文件

### 原始PDF

https://arxiv.org/pdf/2605.03546

> 官方论文正文对应的PDF入口；未下载，故hash与字节数待核实。

[1](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### SHA-256

87c67873f06f48044ef3a1bcd5bed21be2c90d92090bfb3b73b6ca7b9b13781c

[1](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### PDF字节数

2568568

[1](https://arxiv.org/pdf/2605.03546)（访问 2026-11-08）

### 文件夹

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "官方介绍/协议"
 "url": "https://www.vals.ai/benchmarks/programbench"
 }
]
```

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 论文PDF

待核实

[1](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 11. 变更记录

[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-08"
 最近复核
 }
]

[1](https://programbench.com)（访问 2026-11-08）
