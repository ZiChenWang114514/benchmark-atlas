# PostTrainBench

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: A；未知信息保留待核实。

## 基本信息

### 简称

PostTrainBench

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 全称

PostTrainBench

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 版本

v1.2

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 发布日期

2026-09-30（v1.2）

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### section

代码

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### subfields

```json
[]
```

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 许可证

MIT（代码仓库LICENSE；四基础模型及下游数据各自许可另计）

[来源](https://github.com/aisa-group/PostTrainBench/blob/main/LICENSE)（访问 2026-11-07）

### 论文链接

https://arxiv.org/abs/2603.08640

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 官方代码

https://github.com/aisa-group/PostTrainBench

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 数据集

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 官网

https://posttrainbench.com/

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 论文标题

PostTrainBench: Can LLM Agents Automate LLM Post-Training?

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

## 发起与维护

### 发起方

ELLIS Institute Tübingen、MPI for Intelligent Systems、Tübingen AI Center、University of Tübingen、Thoughtful Lab作者团队

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

### partners

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 作者

```json
[
  "Ben Rank",
  "Hardik Bhatnagar",
  "Ameya Prabhu",
  "Shira Eisenberg",
  "Karina Nguyen",
  "Matthias Bethge",
  "Maksym Andriushchenko"
]
```

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

### 维护方

PostTrainBench team

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

## 设计目标

### 衡量能力

自主构建数据、训练及实验流程，改善给定小型基础LLM的目标能力。

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

### 设计动机

直接测端到端LLM后训练，而非仅论文复现或软件修改。

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

## 构建方式

### question_sources

四基础模型与目标基准的组合；v1.2去掉BFCL，保留六目标基准。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### author_background

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### review_process

独立检查数据污染、API使用、查阅历史PostTrainBench轨迹与模型身份。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### quality_control

v1.2隔离HumanEval评分进程，移除trust-remote-code，污染裁判三次多数票。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### decontamination

禁止从具体测试项衍生训练数据；提供同款n-gram工具；违规运行用基础模型分数。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

## 数据形式

### 题量与规模

4基础模型×6目标基准（v1.2）；旧论文/旧页面的4×7不代表当前协议。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 题型

提交后训练权重final_model，而非直接提交下游测试答案。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### modalities

```json
[
  "代码",
  "训练数据",
  "模型权重"
]
```

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### difficulty

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 公开与隐藏划分

代理不得使用测试项训练；每个下游基准具体公开/隐藏范围依其协议。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

## 评测方法

### 指标

四基础模型上的六基准重加权平均；权重按instruct-base性能差的倒数归一化。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 评分方式

AIME最终评估5种子，GSM8K/GPQA/HumanEval3种子，ArenaHard/HealthBench1种子；违规替换为base得分。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 提示与运行设置

每个运行10小时、一张H100；可使用终端与网络；Reprompted单列。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 官方评测实现

aisa-group/PostTrainBench；v1.2增加Harbor adapter。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### 可比性警告

v1.1与v1.2维度、HumanEval评分和裁判均变化；Kimi发布文H20和不同CLI不与官方H100榜直接混排。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "v1.2",
  "evidence_2026_h2": [
    {
      "url": "https://posttrainbench.com/blog/posttrainbench-1-2/",
      "date": "2026-09-30",
      "note": "新版本发布并增加前沿模型。"
    },
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks",
      "date": "2026-09-09",
      "note": "Epoch将v1.1审查为Verified；不自动扩展为v1.2认证。"
    }
  ]
}
```

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）；[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### paper_revision_history

v1.2删除BFCL，修复评分与隔离，增加多种子与多数票；首页仍有七基准描述，以明确v1.2变更和scores-v1.2.js为当前口径。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 污染与争议

存在测试数据训练、模型替换、未经允许API调用及查阅历史轨迹等已记录作弊模式；规则有专门审查。

[来源](https://posttrainbench.com/blog/posttrainbench-1-2/)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### 为什么近期热门

上列2026年后半年发布、当前榜单或独立实跑构成活跃证据；不把热度当成质量背书。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### official_url

https://posttrainbench.com/

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### third_party_url

https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks

[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "Claude Fable 5.1",
    "score": 44.65,
    "metric": "v1.2加权平均(%)",
    "source_url": "https://posttrainbench.com/scores-v1.2.js",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方当前scores-v1.2.js聚合数据，区别9月30日文章四舍五入结果；Fable GPQA含Opus 5 fallback。"
  },
  {
    "rank": 2,
    "model": "Claude Opus 5.5 (Max)",
    "score": 43.8,
    "metric": "v1.2加权平均(%)",
    "source_url": "https://posttrainbench.com/scores-v1.2.js",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方当前scores-v1.2.js聚合数据，区别9月30日文章四舍五入结果；Fable GPQA含Opus 5 fallback。"
  },
  {
    "rank": 3,
    "model": "GPT-6 Astra",
    "score": 41.88,
    "metric": "v1.2加权平均(%)",
    "source_url": "https://posttrainbench.com/scores-v1.2.js",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方当前scores-v1.2.js聚合数据，区别9月30日文章四舍五入结果；Fable GPQA含Opus 5 fallback。"
  }
]
```

[来源](https://posttrainbench.com/scores-v1.2.js)（访问 2026-11-07）

### 时效与可比性

官方当前scores-v1.2.js聚合数据，区别9月30日文章四舍五入结果；Fable GPQA含Opus 5 fallback。

[来源](https://posttrainbench.com/scores-v1.2.js)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

```json
[
  "maksym.andriushchenko@tue.ellis.eu"
]
```

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2603.08640

[来源](https://arxiv.org/abs/2603.08640)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://posttrainbench.com/)（访问 2026-11-07）

### Drive PDF

待核实

> 本组未上传Drive。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "按官方材料新建中文条目；区分热度、质量和不同版本评分。"
  }
]
```

[来源](https://posttrainbench.com/)（访问 2026-11-07）
