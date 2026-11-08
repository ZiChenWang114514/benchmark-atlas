# PostTrainBench

> Benchmark Constitution · 核验 2026-11-08。未知保持“待核实”；访问日不等于实验日。

PostTrainBench评估agent能否在限定GPU与时间内真正改进基础模型，输出后训练权重而非直接回答测试题。当前v1.2的六目标协议、旧七目标题解/轨迹、不同CLI及带模型回退的结果各有边界，不能统一写作一个无条件模型能力分数。

来源：[原始说明](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）；[结果证据](https://posttrainbench.com/scores-v1.2.js)（访问2026-11-08，）；[结果证据](https://posttrainbench.com/config.js)（访问2026-11-08，）

## 基本信息

### 简称

PostTrainBench

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 全称

PostTrainBench

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 基准版本

v1.2

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 论文版本

arXiv v2（2026-03-11 00:55:40 ）；与benchmark v1.2不同。

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 发布日期

论文首投2026-03-10 02:18:00；benchmark v1.2另于2026-09-30发布，不将v1.2日期当基准首次发表。

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）；[2](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 主板块

代码

说明：编辑主板块归档，不据此限制跨学科覆盖。

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 领域标签

[]（源记录为空；不据此认定官方不存在）

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 许可与适用范围

代码仓库LICENSE为MIT；作者组织PostTrainBench-Trajectories HF轨迹数据为Apache-2.0。四基础模型及下游数据仍各自遵守原许可。

来源：[1](https://raw.githubusercontent.com/aisa-group/PostTrainBench/main/LICENSE)（访问2026-11-08，）；[2](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md)（访问2026-11-08，）

### 论文

https://arxiv.org/abs/2603.08640

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 代码仓库

https://github.com/aisa-group/PostTrainBench

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 数据地址

https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories

说明：官方作者组织公开的代理轨迹，不是下游六基准原始测试题的统一重发。

来源：[1](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md)（访问2026-11-08，）

### 官方主页

https://posttrainbench.com/

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 论文标题

PostTrainBench: Can LLM Agents Automate LLM Post-Training?

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

## 发起与维护

### 发起与机构归属

ELLIS Institute Tübingen、MPI for Intelligent Systems、Tübingen AI Center、University of Tübingen、Thoughtful Lab作者团队

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 合作关系

论文作者单位包括ELLIS Institute Tübingen、MPI for Intelligent Systems、Tübingen AI Center、University of Tübingen、Thoughtful Lab；资助与后续外部结果方另列。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

### 作者

- Ben Rank
- Hardik Bhatnagar
- Ameya Prabhu
- Shira Eisenberg
- Karina Nguyen
- Matthias Bethge
- Maksym Andriushchenko

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 当前维护方

PostTrainBench team

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 资助与支持

Thoughtful支持；AP/MB获BMBF FKZ16IS24085B及由Good Ventures Foundation出资的Coefficient Giving支持；MA获Coefficient Giving；HB获Digital Europe OpenEuroLLM101195233；HB/BR获IMPRS-IS支持；Modal for Academics提供compute credits（论文致谢）。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

## 设计目标

### 衡量能力

自主构建数据、训练及实验流程，改善给定小型基础LLM的目标能力。

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 设计背景与适用边界

软件工程能力不能直接代表自主AI研发；基准要求agent在固定硬件/时间内自主选择数据和训练方案，提交真实后训练权重，并审查污染与权重替换。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

## 构建方式

### 题目或数据来源

四基础模型与六目标基准组合（v1.2）：AIME2025、Arena Hard Writing、GPQA Main、GSM8K、HealthBench Easy、HumanEval。HF轨迹卡仍列历史BFCL，不能据此回滚现行六基准协议。

来源：[1](https://github.com/aisa-group/PostTrainBench)（访问2026-11-08，）；[2](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）；[3](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md)（访问2026-11-08，）

### 构建者背景

机器学习/AI安全研究作者团队；通过终端代理自动策划数据与训练实验，基准设计者并不预设每个代理必须采用的后训练策略。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）；[2](https://github.com/aisa-group/PostTrainBench)（访问2026-11-08，）

### 审核流程

独立检查数据污染、API使用、查阅历史PostTrainBench轨迹与模型身份。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 质量控制

v1.2隔离HumanEval评分进程，移除trust-remote-code，污染裁判三次多数票。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 去污染与泄漏边界

禁止从具体测试项衍生训练数据；提供同款n-gram工具；违规运行用基础模型分数。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

## 数据形式

### 规模

4基础模型×6目标基准（v1.2）；旧论文/旧页面的4×7不代表当前协议。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 题型与交付物

提交后训练权重final_model，而非直接提交下游测试答案。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 模态

- 代码
- 训练数据
- 模型权重

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 语言

公开任务指令为英语，提交物是训练脚本、数据处理与模型权重；下游六个基准的语言/任务属性依各自协议，不声称整套只覆盖单一语言。

来源：[1](https://github.com/aisa-group/PostTrainBench)（访问2026-11-08，）；[2](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

### 难度

每运行10小时与单张H100的有限算力自动后训练；4个1.7B–4B级基础模型，面向数学、通识推理、写作、医疗和代码目标。限制的是训练预算，不是选择题难度分档。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）；[2](https://github.com/aisa-group/PostTrainBench)（访问2026-11-08，）；[3](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 公开与隐藏划分

代理不得使用测试项训练；每个下游基准具体公开/隐藏范围依其协议。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

## 评测方法

### 指标

四基础模型上的六基准重加权平均；权重按instruct-base性能差的倒数归一化。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 评分方式

AIME最终评估5种子，GSM8K/GPQA/HumanEval3种子，ArenaHard/HealthBench1种子；违规替换为base得分。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 提示与运行设置

每个运行10小时、一张H100；可使用终端与网络；Reprompted单列。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 评测脚本

aisa-group/PostTrainBench；v1.2增加Harbor adapter。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

### 可比性提醒

v1.1与v1.2维度、HumanEval评分和裁判均变化；Kimi发布文H20和不同CLI不与官方H100榜直接混排。

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 数据版本与更新

```json
{
  "version": "v1.2"
  "evidence_2026_h2": [
    {
      "url": "https://posttrainbench.com/blog/posttrainbench-1-2/"
      "date": "2026-09-30"
      "note": "新版本发布并增加前沿模型。"
    }
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
      "date": "2026-09-09"
      "note": "Epoch将v1.1审查为Verified；不自动扩展为v1.2认证。"
    }
  ]
}
```

来源：[1](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问2026-11-08，）；[2](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07，）

### 论文修订记录

```json
{
  "arxiv": [
    {
      "version": "v1"
      "submitted_at": "2026-03-10 "
    }
    {
      "version": "v2"
      "submitted_at": "2026-03-11 "
    }
  ]
  "benchmark_release_note": "v1.2删除BFCL，修复评分与隔离，增加多种子与多数票；首页仍有七基准描述，以明确v1.2变更和scores-v1.2.js为当前口径。"
}
```

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 饱和程度

当前v1.2官方汇总数据最高已录Fable5.1为44.65（std2.72，n2），含官方注明的Opus5 GPQA fallback；这是加权下游得分而非后训练成功率。不将原论文旧7基准的23.2/51.1直接用作v1.2对照。

来源：[1](https://posttrainbench.com/scores-v1.2.js)（访问2026-11-08，）；[2](https://posttrainbench.com/config.js)（访问2026-11-08，）；[3](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

### 争议与已知问题

已记录测试集训练、替换成现成instruct权重、未经许可API合成数据及查看历史轨迹等违规模式。当前v1.2删除BFCL并强化隔离；HF历史轨迹卡仍列七基准，数据授权Apache2.0也不同于代码MIT。Fable5/5.1 GPQA为混合回退结果，必须显示来源。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）；[2](https://huggingface.co/datasets/aisa-group/PostTrainBench-Trajectories/raw/main/README.md)（访问2026-11-08，）；[3](https://posttrainbench.com/config.js)（访问2026-11-08，）

### 衍生与后续使用

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

## 榜单快照

### 快照访问日期

2026-11-08 （网页访问日期；历史结果日期分别保留）

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 官方结果入口

https://posttrainbench.com/

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 第三方入口

https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks

来源：[1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07，）

### 分赛道结果

- {"model": "Fable 5.1", "score": 44.65, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "fable-5.1", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 2.72, "n": 2, "provenance_note": "官方标注5个GPQA Main单元回退到Opus 5。", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 1}
- {"model": "Opus 5.5", "score": 43.8, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-5.5-max", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 3.0, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 2}
- {"model": "GPT 6 (Astra)", "score": 41.88, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-6-astra", "scaffold": "Codex CLI", "reasoning_effort": "Max", "std": 0.76, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 3}
- {"model": "GPT 6.1 (Sol)", "score": 38.79, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-6.1-sol", "scaffold": "Codex CLI", "reasoning_effort": "Max", "std": 0.36, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 4}
- {"model": "Fable 5", "score": 37.27, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "fable-5", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 1.65, "n": 2, "provenance_note": "官方标注GPQA Main采用Opus4.8 Max回退。", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 5}
- {"model": "GLM 5.3 Flash", "score": 36.79, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "glm-5.3-flash", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 0.11, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 6}
- {"model": "Opus 5", "score": 35.66, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-5", "scaffold": "Claude Code", "reasoning_effort": "官方配置未逐项列明", "std": 2.62, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 7}
- {"model": "GLM 5.3", "score": 34.52, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "glm-5.3", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 3.39, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 8}
- {"model": "Kimi K3", "score": 31.48, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "kimi-k3", "scaffold": "Claude Code", "reasoning_effort": "官方配置未逐项列明", "std": 0.63, "n": 3, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 9}
- {"model": "GPT 5.6 (Sol)", "score": 31.01, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-5.6-sol", "scaffold": "Codex CLI", "reasoning_effort": "Max", "std": 0.2, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 10}
- {"model": "Opus 4.8", "score": 31.0, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-4.8-max", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 3.0, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 11}
- {"model": "Opus 4.8", "score": 30.66, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-4.8", "scaffold": "Claude Code", "reasoning_effort": "High", "std": 3.04, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 12}
- {"model": "GLM 5.2", "score": 30.4, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "glm-5.2", "scaffold": "Claude Code", "reasoning_effort": "Max", "std": 1.46, "n": 3, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 13}
- {"model": "Opus 4.7", "score": 24.34, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "opus-4.7", "scaffold": "Claude Code", "reasoning_effort": "xHigh", "std": 1.63, "n": 3, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 14}
- {"model": "GPT 5.5", "score": 23.87, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-5.5-xhigh", "scaffold": "Codex CLI", "reasoning_effort": "xHigh", "std": 0.48, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 15}
- {"model": "Grok 4.5", "score": 22.62, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "grok-4.5-high", "scaffold": "Cursor CLI", "reasoning_effort": "High", "std": 0.94, "n": 2, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 16}
- {"model": "Gemini 3.1 Pro", "score": 18.11, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gemini-3.1-pro", "scaffold": "OpenCode", "reasoning_effort": "官方配置未逐项列明", "std": 1.68, "n": 3, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 17}
- {"model": "GPT 5.4", "score": 17.76, "track": "官方运行/v1.2/10h-H100", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "gpt-5.4-high", "scaffold": "Codex CLI", "reasoning_effort": "High", "std": 1.8, "n": 3, "provenance_note": "", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 18}
- {"model": "Locus / Opus 5", "score": 41.66, "track": "官方收录/外部运行审阅/v1.2", "metric": "v1.2 weighted average (0–100)", "source_url": "https://posttrainbench.com/scores-v1.2.js", "collected_at": "2026-11-08 ", "agent_id": "locus", "scaffold": "Intology", "reasoning_effort": "配置见官方说明", "std": 0.82, "n": 3, "provenance_note": "Intology运行，PostTrainBench审阅；不是官方团队亲跑。", "result_type": "当前官方JS汇总，未提供统一更新时间", "rank": 1}

来源：[1](https://posttrainbench.com/scores-v1.2.js)（访问2026-11-08，）；[2](https://posttrainbench.com/config.js)（访问2026-11-08，）

### 覆盖边界

完整收录scores-v1.2.js全部19条聚合配置：18条官方运行与1条外部Locus审阅结果分轨，保留std/n、CLI和reasoning effort。Fable5/5.1混合GPQA回退明确标注；不与旧v1/v1.1、厂商H20实验或官方instruct参考混排行。数据资产无统一更新日，仅记录实际访问日。

来源：[1](https://posttrainbench.com/scores-v1.2.js)（访问2026-11-08，）；[2](https://posttrainbench.com/config.js)（访问2026-11-08，）

## 联系方式

### 公开项目邮箱

- maksym.andriushchenko@tue.ellis.eu

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 公开反馈渠道

https://github.com/aisa-group/PostTrainBench/issues

来源：[1](https://github.com/aisa-group/PostTrainBench)（访问2026-11-08，）

### 官方社交渠道

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 联系方式收录原则

Benchmark Constitution仅收录论文/官方站公开的项目联系渠道，不收集私人信息；这不是对外站隐私政策的认证。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-08，）

## 原始文件

### 既存论文原件

待核实

说明：本组仅本地研究，未上传。

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 原始PDF地址

https://arxiv.org/pdf/2603.08640

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）

### 下载SHA-256

823f11de21206c9ba5be0531bee62f1d29d97cfeb5c8e9a6c90a2256f1f948bc

说明：2026-11-08 下载字节的校验；没有覆盖或上传，不能据此认定既存原件同版本。

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

### 下载字节数

```json
366334
```

来源：[1](https://arxiv.org/pdf/2603.08640)（访问2026-11-08，）

### 既存文件夹

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

### 其他文档

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://posttrainbench.com/)（访问2026-11-08，）

## 变更记录

最近复核
最近复核

来源：[1](https://arxiv.org/abs/2603.08640)（访问2026-11-08，）
