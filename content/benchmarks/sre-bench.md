# SRE Bench（SRE-Bench）

> Benchmark Constitution，深度复核 2026-11-08。已核验存在；近期热门新建条目，未核实字段保留标记；trending: A

SRE-Bench评测从未知二进制恢复程序语义的能力，不是站点可靠性工程。19个私有程序被构建为262个二进制实例，每实例6个可确定验证任务。最关键的阅读门槛是分母：论文只对gradable runs计算条件成绩，Vals把全部262实例纳入；内部关闭护栏的多尝试成绩又是第三套条件。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

## 基本信息

### 简称

SRE Bench（SRE-Bench）

> 此处 SRE 指软件逆向工程，不是站点可靠性工程。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 全称

The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 基准版本

论文v2所定义262实例/1,572任务；无单独数据集语义版本号

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 论文版本

v2（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 发布日期

2026-08-11（arXiv v1 提交）

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 主板块

代码

> Benchmark Atlas 编辑归档；Vals 归入 Cyber。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 领域

```json
[
  "二进制逆向工程"
  "网络安全"
]
```

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 许可与适用范围

待核实

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2608.11469

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 官方代码

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 数据

未公开

> 论文说明19个程序为 private。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/srebench

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 论文标题

The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

## 发起与维护

### 发起方

Columbia University等论文作者团队，Vals AI参与共建及托管；包括UC Berkeley、UCLA、Tufts以及产业研究作者。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 合作/参与机构

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 作者

Jeremy Spence、Nicholas Assaderaghi、Feng Xiao、Jinhao Zhu、Nikil Ravi、Xiangyu Qi、Matthew Jagielski、Raluca Ada Popa、Eric Wallace、Guannan Wei、Yangruibo Ding、Zhuo Zhang

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 维护方

Vals AI（当前榜单维护）

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 设计目标

### 衡量能力

在没有源代码的情况下理解真实规模、带反分析保护的二进制程序（协议、固件、游戏、文件格式恢复、恶意软件）。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）

### 设计背景

现有 RE 相关基准依赖已有 CTF 或玩具程序，易被记忆污染且规模与保护不真实。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 构建方式

### 题目来源

RE 专家从零构建19个内部程序（平均约16.9K行代码），配合44种自研反分析机制（27K行代码的保护套件）。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 出题者背景

逆向工程专家平均6年经验，总投入超过5,000专家小时；19程序分别从私有设计规范独立实现，不共享代码且不基于公开项目。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 审核流程

每程序私有参考解必须得6/6作为可解性及回归门；用Opus 4.8与GPT-6-Astra进行对抗性reward-hacking审计，发现可读隐藏行为字符串后移除并加入构建回归检查。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 质量控制

目标、评分基础设施及保护套件全部内部构建；评分代码、参考解和开发产物从agent容器移除，运行中不提供评分反馈；域级任务通过确定性server、回放或沙箱验证。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 污染控制

全部从零 clean-room 构建、程序私有，以避免出现在训练数据中

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 数据形式

### 题量

19个程序 → 262个二进制实例 → 1,572个确定性评分任务（每实例6个）

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 任务形式

shell 环境中的 agent 逆向任务，确定性验证

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 模态

```json
[
  "二进制文件"
  "文本/命令行"
]
```

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 语言

目标程序实现语言：C、C++、Rust、Go；固件不含Go。交互/问题自然语言完整分布待核实。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 难度

19程序平均16,915.8行代码，44保护原语组成8预设；262二进制实例，每实例6确定性子任务。论文公共API评测中最佳149/181已评分实例全解，并非149/262的条件成功率。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 公开与隐藏划分

私有（Vals 标注 Proprietary）

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 评测方法

### 指标

Fully Solved：每实例6项全对才算解决；Capability Score：每实例完成6项的比例。论文Table 4只平均可评分实例；Vals Accuracy把全部262实例纳入且失败计0。总任务库存为262×6=1,572，不是论文条件平均的固定分母。

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

### 评分

论文Table 4的Score、Solved与Zeros只对gradable runs计算，拒答及上下文失败不入分母；Vals方法则明确以全部262实例为分母，失败记零。两套百分比不可直接比较。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 运行设置

论文公共设置：mini-SWE-agent、最高推理档、最多500模型steps和6小时，标准RE工具箱；内部unconstrained设置：Codex/Claude Code、关闭cyber safeguards且无预算上限。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 评测工具

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 可比性

论文gradable-run条件成绩与Vals全262实例成绩分母明确不同；内部关闭安全护栏、无预算上限、多尝试Codex/Claude Code又是独立协议，不能混排。

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

## 最新情况

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "待核实"
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/srebench"
      "date": "2026-11-05"
      "organization": "Vals AI"
      "note": "当前方法与榜单页展示多家前沿模型的实测结果；11月5日更新、37模型二进制逆向理解测试；不能误译为站点可靠性工程基准。"
    }
    {
      "url": "https://www.vals.ai/benchmarks"
      "date": "2026-11-05"
      "organization": "Vals AI"
      "note": "目录卡片：Cyber Proprietary SRE Bench Updated: 11/5/2026 Models Tested: 37 Can AI agents work out what a real-world binary does without its source code? Top Models 1 GPT-6 Astra 2 GPT-6.1 Sol 3 Gemini 4 Argon View Details"
    }
    {
      "url": "https://openai.com/index/gpt-6-astra/"
      "date": "2026-11-07"
      "organization": "OpenAI"
      "note": "GPT-6 Astra正式发布评测表明确报告SRE Bench，作为近期厂商采用证据。"
    }
  ]
  "trending": {
    "heat_confidence": "A"
    "summary": "8月发布的二进制逆向评测已进入 GPT-6 Astra 正式发布表，Vals 11月仍更新37模型榜。"
  }
}
```

> 近期热门证据取自候选研究与重开页面；A级：多家前沿实验室或评测机构独立采用。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）；[来源2](https://www.vals.ai/benchmarks)（访问 2026-11-07）；[来源3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-08-12"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2026-10-01"
    "timezone": ""
  }
]
```

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 饱和与能力边界

Vals当前最高Accuracy为56.87%；论文内部无约束配置GPT-6-Astra Max达到88.0% pass@1和99.2% pass@4（4尝试）。后者不衡量无私有grader的正确候选选择能力，也不意味着公共API单次评测饱和。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

### 风险与争议

论文明确不公开二进制与任务实例以维持污染抵抗，提供受控评测服务；19程序的覆盖面有限且平均规模仍小于大型真实软件。“contamination-free”是作者设计主张，不等于独立审计已证明所有未来训练均无泄漏。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 系列与衍生关系

SRE表示二进制逆向评测，不是Site Reliability Engineering。与ProgramBench的行为重实现不同，后者提供已知公开程序及文档。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

### 官方入口

https://www.vals.ai/benchmarks/srebench

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 独立来源

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 分来源与协议结果

#### Vals current / denominator 262

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra | 56.87 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 2 | GPT-6.1 Sol | 50.76 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 3 | Gemini 4 Argon | 44.27 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 4 | Claude Opus 5.5 | 33.59 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 5 | Daybreak Blue | 31.68 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 6 | GPT-5.6 Sol | 30.53 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 7 | GPT-6 Sol | 30.53 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 8 | Claude Sonnet 5.5 | 30.15 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 9 | Kimi K3.1 Pro | 27.1 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 10 | Claude Fable 5.1 | 22.9 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 11 | Claude Opus 5.5 (CVP) | 21.76 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 12 | Claude Opus 5 | 12.21 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 13 | Wonder Full | 11.83 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 14 | Gemini 3.8 Flash | 11.07 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 15 | GPT-5.6 Terra | 9.54 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 16 | GLM 5.3 | 9.16 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 17 | Claude Haiku 5.5 | 5.72 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 18 | Gemini 3.7 Flash | 4.58 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 19 | MiMo V2.6 Flash | 4.2 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 20 | Grok 4.7 | 3.82 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 21 | GPT 5.5 | 3.82 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 22 | Muse Spark 1.3 Max | 3.82 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 23 | MiMo V2.6 Pro | 3.05 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 24 | GPT-6 Luna | 2.67 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 25 | Hy4 Preview | 2.29 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 26 | DeepSeek V4 Pro 0813 | 1.91 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 27 | Inkling 2 Small | 1.91 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 28 | GPT-5.6 Luna | 1.53 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 29 | DeepSeek V4.1 Flash | 0.76 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 30 | GLM 5.3 Flash | 0.76 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 31 | Grok 4.5 | 0.76 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 32 | Claude Sonnet 5 | 0.38 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 33 | Step 5 Preview | 0.38 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 34 | GLM 5.2 | 0.0 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 35 | Muse Spark 1.2 | 0.0 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 36 | Gemini 3.1 Pro Preview (02/26) | 0.0 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |
| 37 | Inkling | 0.0 | Accuracy (%)；全262实例 | {"source_date":"2026-11-05"} |

#### paper v2 Table 4 public / graded-only

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | gpt-6-astra | 5.55 | mean successful tasks per graded binary (0–6) | {"n_graded":181,"total_instances":262,"fully_solved_percent_of_graded":82.3} |
| — | gpt-5.6-sol | 3.69 | mean successful tasks per graded binary (0–6) | {"n_graded":254,"total_instances":262,"fully_solved_percent_of_graded":31.5} |
| — | claude-fable-5.1 | 2.58 | mean successful tasks per graded binary (0–6) | {"n_graded":223,"total_instances":262,"fully_solved_percent_of_graded":26.9} |
| — | claude-opus-5 | 1.91 | mean successful tasks per graded binary (0–6) | {"n_graded":256,"total_instances":262,"fully_solved_percent_of_graded":12.5} |
| — | gpt-5.5 | 1.02 | mean successful tasks per graded binary (0–6) | {"n_graded":262,"total_instances":262,"fully_solved_percent_of_graded":3.8} |
| — | deepseek-v4.1-flash | 0.85 | mean successful tasks per graded binary (0–6) | {"n_graded":262,"total_instances":262,"fully_solved_percent_of_graded":0.8} |
| — | grok-4.5 | 0.45 | mean successful tasks per graded binary (0–6) | {"n_graded":218,"total_instances":262,"fully_solved_percent_of_graded":0.9} |
| — | glm-5.2 | 0.21 | mean successful tasks per graded binary (0–6) | {"n_graded":262,"total_instances":262,"fully_solved_percent_of_graded":0.0} |

#### paper v2 Table 11 internal unconstrained Max / pass@1

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | GPT-5.6 Sol | 55.8 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-5.6 Cyber | 56.8 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-6-Astra | 88.0 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | Opus 5.5 | 82.1 | pass@1 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |

#### paper v2 Table 11 internal unconstrained Max / pass@4

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | GPT-5.6 Sol | 68.7 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-5.6 Cyber | 72.5 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | GPT-6-Astra | 99.2 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |
| — | Opus 5.5 | 98.1 | pass@4 (%) | {"reasoning_effort":"Max","safety_guards":"disabled","attempts_per_instance":4} |

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

### 覆盖与时效

Vals全部37模型Accuracy按262实例分母单独成轨；论文Table 4的8模型分别记录条件Score与条件Solved，明确n_graded；Table 11 Max内部pass@1/pass@4另轨，不混作公开API榜。官网BibTeX称forthcoming、但arXiv v2已实际打开，以arXiv完整署名和修订史为准。

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

```json
[
  "js6721@columbia.edu"
  "41zz@cs.columbia.edu"
]
```

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）

### 官方反馈

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 公开社区

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 隐私边界

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2608.11469

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）

### PDF SHA-256

04416ad347e07e0cb2d4eda5e80fba82bcb3e296ed9ef16b38edbc1a4e5d2905

> 本次实际下载的PDF字节计算；未上传。

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）

### PDF字节数

```json
692156
```

[来源1](https://arxiv.org/pdf/2608.11469)（访问 2026-11-08）

### 文件夹

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "已打开一手材料"
    "url": "https://arxiv.org/abs/2608.11469"
    "accessed": "2026-11-08"
  }
  {
    "type": "已打开一手材料"
    "url": "https://www.vals.ai/benchmarks/srebench"
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）

### PDF归档

待核实

[来源1](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]
```

[来源1](https://arxiv.org/abs/2608.11469)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/srebench)（访问 2026-11-08）
