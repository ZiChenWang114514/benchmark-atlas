# SkillsBench

> Benchmark Constitution · 深度复核 2026-11-08（KST / Asia/Seoul）。已核验存在；研究快照；note: trending: B；未核实字段保留标记

SkillsBench把“技能是否真的有用”变成配对实验：同一模型与同一agent，在有技能和无技能两条件下完成专家任务。默认v1.1含87题，额外14题不能并入默认库存。官方87题发布、HF审计导出和Vals独立实现有不同配置与时间快照，本档不将它们拼成统一裸模型榜。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）；[来源2](https://github.com/benchflow-ai/skillsbench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源4](https://www.skillsbench.ai)（访问 2026-11-08）

## 基本信息

### 简称

SkillsBench

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 全称

SkillsBench

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 基准版本

SkillsBench v1.1（87默认任务；14个tasks-extra不计入默认集）

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### 论文版本

v4（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### 发布日期

2026-02-13 KST（arXiv v1 2026-02-13T16:06:06+09:00；不是v1.1 tag的发布日期）

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### 主板块

Agent

> 编辑归档，不代表官方分类。

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 领域

```json
[
  "代码",
  "技能"
]
```

> 编辑归档，不代表官方分类。

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 许可与适用范围

Apache-2.0（官方仓库LICENSE及README）；任务依赖的外部资产仍须遵循各自授权。

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2602.12670

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 官方代码

https://github.com/benchflow-ai/skillsbench

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 数据

https://huggingface.co/datasets/benchflow/skillsbench

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### 官方入口

https://www.skillsbench.ai

[来源1](https://github.com/benchflow-ai/skillsbench)（访问 2026-11-08）；[来源2](https://www.skillsbench.ai)（访问 2026-11-08）

### 论文标题

SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## 发起与维护

### 发起方

BenchFlow（原始benchmark）；Vals AI（独立实现）

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 合作/参与机构

贡献者来自BenchFlow、OSU、Amazon、UC Berkeley等机构及独立研究者；Vals明确与BenchFlow合作集成到Valkyrie。

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

### 作者

Xiangyi Li、Yimin Liu、Wenbo Chen等；完整作者名单见论文，Vals引用作者表与当前论文修订名单不同。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 维护方

BenchFlow（原始benchmark）；Vals AI（独立实现）

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 资助

论文致谢模型厂商提供模型访问/API支持，Google Cloud Platform与Amazon Bedrock提供基础设施，Lambda提供GPU、Daytona提供credits；这是资源支持清单，不把它冒充现金资助金额。

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

## 设计目标

### 衡量能力

配对比较同一模型及harness在有无可复用技能包时的表现，测量技能增强收益。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 设计背景

传统agent得分混合基础模型、工具架构与增强效果；本基准把技能作为独立实验因素。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## 构建方式

### 题目来源

142位贡献者提交400候选任务，经结构、oracle执行、指令来源和技能泄漏门控及人工审查，当前保留87任务。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 出题者背景

142位贡献者提交任务，论文署名包括BenchFlow及多所大学、企业和独立研究者；Amazon署名作者注明工作在其本职之外完成。

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### 审核流程

人工真实工作指令、固定容器、参考解及确定性验证器；技能不能包含实例答案、硬编码路径或魔数。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 质量控制

人工真实工作指令、固定容器、参考解及确定性验证器；技能不能包含实例答案、硬编码路径或魔数。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 污染控制

技能与任务答案解耦，扫描实例文件名、魔数、原样oracle命令或预期输出泄漏；不能保证完全排除预训练污染。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## 数据形式

### 题量

v1.1：87默认任务、8领域；另14个需要凭据或与集成不兼容的任务包明确排除。官网当前25 model–harness配置（24配对+1仅With）；论文v4为18配置，HF卡与export为24配置，分别保留来源快照。

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### 任务形式

终端与文件产物任务；包含自然科学、数学优化、安全、工程、金融、办公及软件等。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 模态

```json
[
  "文本",
  "代码",
  "数据文件"
]
```

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 难度

专家工作流、需组合技能；官方目标为2个以上技能组合，但目标不是已证实所有模型成绩低于50%的结论。

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### 公开与隐藏划分

87个任务定义、oracle、verifier和技能包公开；运行时agent不能读取oracle/验证器。tasks-extra的14题不属于默认评测集。

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

## 评测方法

### 指标

任务宏平均通过率、Skills绝对增益与归一化增益。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 评分

确定性脚本/pytest验证；Vals每模型每条件3次，先题内平均再跨题平均。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 运行设置

官方v1.1通过BenchFlow按同模型、同agent配对with-skill/no-skill；HF导出只计reviewed non-timeout trials并保留partial coverage。Vals独立实现默认OpenHands-CLI commit 3ca17446c5d9c1e35e054803478a3501ec251ecf；GPT 5.5另列Codex，每条件3次、先题内再跨题平均。

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

### 评测工具

https://github.com/benchflow-ai/skillsbench

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 可比性

论文与Vals的库存、harness及运行时间不同；论文87题结果不可替代Vals当前榜；要按同模型同harness计算技能增益。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "v1.1",
  "source_commit": "27738384b1df694ea2ae466e416f476e94d8fab9",
  "active_tasks": 87,
  "excluded_tasks": 14,
  "source_snapshots": "官网25配置/2026-07-16；HF归档24配置/卡称2026-06-16；Vals独立35行/2026-10-29，不能强行合并。"
}
```

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）

### 修订历史

```json
[
  {
    "version": "v1",
    "submitted_at": "2026-02-13T16:06:06+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2026-03-07T09:51:15+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2026-03-13T16:33:01+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v4",
    "submitted_at": "2026-06-15T06:21:07+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）

### 饱和与能力边界

官方官网当前With Skills最高67.3%；Vals独立榜最高69.80%。不同harness/库存/运行时间不能合成单一饱和度，尚无本轮证据支持完全饱和。

[来源1](https://www.skillsbench.ai)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

### 风险与争议

论文与Vals的库存、harness及运行时间不同；论文87题结果不可替代Vals当前榜；要按同模型同harness计算技能增益。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 系列与衍生关系

SkillsBench不是AgentBench；With Skills和No Skills是同一条目的实验条件，不重复新增。

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）；[来源2](https://github.com/benchflow-ai/skillsbench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源4](https://www.skillsbench.ai)（访问 2026-11-08）

### 官方入口

https://www.skillsbench.ai

[来源1](https://www.skillsbench.ai)（访问 2026-11-08）

### 独立来源

https://www.vals.ai/benchmarks/skillsbench

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 分来源与协议结果

#### official v1.1 export / With Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-5.5 | 67.3 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":15.8,"selected_trials":261} |
| 2 | GPT-5.5 | 66.5 | resolution rate (%) | {"condition":"With Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19.7,"selected_trials":261} |
| 3 | Opus 4.7 | 61.2 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.2,"selected_trials":261} |
| 4 | Gemini 3.1 Pro | 60.8 | resolution rate (%) | {"condition":"With Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":24.8,"selected_trials":261} |
| 5 | GLM 5.1 | 58.4 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":25.7,"selected_trials":261} |
| 6 | Gemini 3 Flash | 54.6068 | resolution rate (%) | {"condition":"With Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":20.3884,"selected_trials":261} |
| 7 | Opus 4.8 | 54.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":8.4,"selected_trials":261} |
| 8 | Kimi K2.6 | 54 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":20.6,"selected_trials":261} |
| 9 | Opus 4.7 | 53.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.1,"selected_trials":261} |
| 10 | MiniMax M3 | 53 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.3,"selected_trials":261} |
| 11 | Gemini 3.1 Pro | 52.8 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19,"selected_trials":261} |
| 12 | GPT-5.2 | 51.7046 | resolution rate (%) | {"condition":"With Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":22.0068,"selected_trials":261} |
| 13 | Opus 4.6 | 50.2241 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":16.5479,"selected_trials":259} |
| 14 | DeepSeek V4 Pro | 50.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.2,"selected_trials":261} |
| 15 | Opus 4.5 | 49.0395 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":25.223,"selected_trials":257} |
| 16 | Gemini 3.5 Flash | 48.2 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":7.1,"selected_trials":261} |
| 17 | Sonnet 4.6 | 47.2 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":13.6,"selected_trials":261} |
| 18 | DeepSeek V4 Flash | 44.7 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":17.2,"selected_trials":261} |
| 19 | Grok 4.3 | 41.7 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.8,"selected_trials":261} |
| 20 | GPT-5.4 Mini | 41.4 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.5,"selected_trials":261} |
| 21 | Sonnet 4.5 | 36.1723 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":19.4519,"selected_trials":260} |
| 22 | MiniMax M2.7 | 34.9 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":16.8,"selected_trials":261} |
| 23 | Haiku 4.5 | 30.0831 | resolution rate (%) | {"condition":"With Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":21.2897,"selected_trials":261} |
| 24 | Gemini 3.1 Flash Lite | 20.1 | resolution rate (%) | {"condition":"With Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":4.1,"selected_trials":261} |

#### official v1.1 export / Without Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-5.5 | 51.5 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":15.8,"selected_trials":261} |
| 2 | GPT-5.5 | 46.8 | resolution rate (%) | {"condition":"Without Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19.7,"selected_trials":261} |
| 4 | Opus 4.7 | 43 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.2,"selected_trials":261} |
| 7 | Gemini 3.1 Pro | 36 | resolution rate (%) | {"condition":"Without Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":24.8,"selected_trials":261} |
| 13 | GLM 5.1 | 32.7 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":25.7,"selected_trials":261} |
| 8 | Gemini 3 Flash | 34.2184 | resolution rate (%) | {"condition":"Without Skills","agent":"gemini-cli","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":20.3884,"selected_trials":261} |
| 3 | Opus 4.8 | 45.7 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":8.4,"selected_trials":261} |
| 12 | Kimi K2.6 | 33.4 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":20.6,"selected_trials":261} |
| 5 | Opus 4.7 | 42.1 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.1,"selected_trials":261} |
| 15 | MiniMax M3 | 29.7 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.3,"selected_trials":261} |
| 9 | Gemini 3.1 Pro | 33.8 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":19,"selected_trials":261} |
| 16 | GPT-5.2 | 29.6978 | resolution rate (%) | {"condition":"Without Skills","agent":"codex","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":22.0068,"selected_trials":261} |
| 10 | Opus 4.6 | 33.6762 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":16.5479,"selected_trials":258} |
| 18 | DeepSeek V4 Pro | 26.9 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":23.2,"selected_trials":261} |
| 19 | Opus 4.5 | 23.8165 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":25.223,"selected_trials":261} |
| 6 | Gemini 3.5 Flash | 41.1 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":7.1,"selected_trials":261} |
| 11 | Sonnet 4.6 | 33.5 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":13.6,"selected_trials":261} |
| 17 | DeepSeek V4 Flash | 27.5 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":17.2,"selected_trials":261} |
| 20 | Grok 4.3 | 22.8 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":18.8,"selected_trials":261} |
| 14 | GPT-5.4 Mini | 29.9 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":11.5,"selected_trials":261} |
| 22 | Sonnet 4.5 | 16.7204 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"partial","source_recomputed_date":null,"skill_lift":19.4519,"selected_trials":261} |
| 21 | MiniMax M2.7 | 18.1 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":16.8,"selected_trials":261} |
| 24 | Haiku 4.5 | 8.7935 | resolution rate (%) | {"condition":"Without Skills","agent":"claude-code","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":null,"skill_lift":21.2897,"selected_trials":261} |
| 23 | Gemini 3.1 Flash Lite | 16 | resolution rate (%) | {"condition":"Without Skills","agent":"openhands","harness":"benchflow","task_version":"v1.1","coverage_status":"full","source_recomputed_date":"2026-06-11","skill_lift":4.1,"selected_trials":261} |

#### Vals With Skills / OpenHands

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | DeepSeek V4.1 Flash | 69.8 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 2 | Grok 4.5 | 66.03 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 3 | Gemini 3.7 Flash | 65.89 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 5 | GPT 5.5 | 62.21 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 6 | Claude Fable 5.1 | 61.55 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 7 | GPT-5.6 Luna | 60.45 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 8 | Claude Opus 5 | 60.44 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 9 | Claude Opus 4.8 | 59.23 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 10 | Muse Spark 1.1 | 59.19 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 11 | GPT-5.6 Terra | 58.9 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 12 | Gemini 3.8 Flash | 57.98 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 13 | Grok 4.6 | 55.77 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 14 | Qwen 3.7 Plus | 54.3 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 15 | GPT-5.6 Sol | 54.1 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 16 | DeepSeek V4 Pro 0813 | 53.83 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 17 | Muse Spark 1.2 | 53.04 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 18 | Gemini 3.5 Flash | 52.74 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 19 | GPT 5.4 (xhigh) | 51.71 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 20 | MiniMax-M3 | 51.5 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 21 | DeepSeek V4 | 51.27 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 22 | DeepSeek V4 Flash 0731 | 50.67 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 23 | Kimi K2.7 Code | 50.04 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 24 | Claude Sonnet 4.6 | 49.05 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 25 | GLM 5.3 | 47.51 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 26 | Claude Sonnet 5 | 46.48 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 27 | GLM 5.2 | 45.08 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 28 | Qwen 3.8 Max | 42.01 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 29 | Grok 4.3 | 40.64 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 30 | GLM 5.3 Flash | 40.16 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 31 | Qwen 3.8 27B | 38.11 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 32 | Inkling Small | 33.58 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 33 | Ling 3.0 Flash | 27.95 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 34 | Inkling | 26.09 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |
| 35 | Mercury 2.5 | 18.06 | Accuracy (%) | {"harness":"OpenHands","condition":"With Skills","source_date":"2026-10-29"} |

#### Vals With Skills / Codex

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 4 | GPT 5.5 | 62.55 | Accuracy (%) | {"harness":"Codex","condition":"With Skills","source_date":"2026-10-29"} |

#### official website 2026-07-16 / Without Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | OpenAI GPT-5.5 OpenHands | 51.5 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 15.8"} |
| 2 | OpenAI GPT-5.5 Codex | 46.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.7"} |
| 4 | Claude Opus 4.7 Claude Code | 43.0 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.2"} |
| 7 | Gemini Gemini 3.1 Pro Gemini CLI | 36.0 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 24.8"} |
| 13 | Z.ai GLM 5.1 OpenHands | 32.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.7"} |
| 8 | Gemini Gemini 3 Flash Gemini CLI | 34.2 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.4"} |
| 3 | Claude Opus 4.8 OpenHands | 45.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 8.4"} |
| 12 | MoonshotAI Kimi K2.6 OpenHands | 33.4 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.6"} |
| 5 | Claude Opus 4.7 OpenHands | 42.1 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.1"} |
| 15 | Minimax MiniMax M3 OpenHands | 29.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.3"} |
| 9 | Gemini Gemini 3.1 Pro OpenHands | 33.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.0"} |
| 15 | OpenAI GPT-5.2 Codex | 29.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 22.0"} |
| 10 | Claude Opus 4.6 Claude Code | 33.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.5"} |
| 18 | DeepSeek DeepSeek V4 Pro OpenHands | 26.9 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.2"} |
| 19 | Claude Opus 4.5 Claude Code | 23.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.2"} |
| 6 | Gemini Gemini 3.5 Flash OpenHands | 41.1 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 7.1"} |
| 11 | Claude Sonnet 4.6 OpenHands | 33.5 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 13.6"} |
| 17 | DeepSeek DeepSeek V4 Flash OpenHands | 27.5 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 17.2"} |
| 20 | Grok Grok 4.3 OpenHands | 22.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.8"} |
| 14 | OpenAI GPT-5.4 Mini OpenHands | 29.9 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.5"} |
| 22 | Claude Sonnet 4.5 Claude Code | 16.7 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.5"} |
| 21 | Minimax MiniMax M2.7 OpenHands | 18.1 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.8"} |
| 24 | Claude Haiku 4.5 Claude Code | 8.8 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 21.3"} |
| 23 | Gemini Gemini 3.1 Flash Lite OpenHands | 16.0 | resolution rate (%) | {"condition":"Without Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 4.1"} |

#### official website 2026-07-16 / With Skills

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | OpenAI GPT-5.5 OpenHands | 67.3 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 15.8"} |
| 2 | OpenAI GPT-5.5 Codex | 66.5 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.7"} |
| 3 | Claude Opus 4.7 Claude Code | 61.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.2"} |
| 4 | Gemini Gemini 3.1 Pro Gemini CLI | 60.8 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 24.8"} |
| 5 | Z.ai GLM 5.1 OpenHands | 58.4 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.7"} |
| 6 | Hunyuan HY3 Claude Code | 55.9 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"—"} |
| 7 | Gemini Gemini 3 Flash Gemini CLI | 54.6 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.4"} |
| 8 | Claude Opus 4.8 OpenHands | 54.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 8.4"} |
| 9 | MoonshotAI Kimi K2.6 OpenHands | 54.0 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 20.6"} |
| 10 | Claude Opus 4.7 OpenHands | 53.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.1"} |
| 11 | Minimax MiniMax M3 OpenHands | 53.0 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.3"} |
| 12 | Gemini Gemini 3.1 Pro OpenHands | 52.8 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.0"} |
| 13 | OpenAI GPT-5.2 Codex | 51.7 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 22.0"} |
| 14 | Claude Opus 4.6 Claude Code | 50.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.5"} |
| 15 | DeepSeek DeepSeek V4 Pro OpenHands | 50.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 23.2"} |
| 16 | Claude Opus 4.5 Claude Code | 49.0 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 25.2"} |
| 17 | Gemini Gemini 3.5 Flash OpenHands | 48.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 7.1"} |
| 18 | Claude Sonnet 4.6 OpenHands | 47.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 13.6"} |
| 19 | DeepSeek DeepSeek V4 Flash OpenHands | 44.7 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 17.2"} |
| 20 | Grok Grok 4.3 OpenHands | 41.7 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 18.8"} |
| 21 | OpenAI GPT-5.4 Mini OpenHands | 41.4 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 11.5"} |
| 22 | Claude Sonnet 4.5 Claude Code | 36.2 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 19.5"} |
| 23 | Minimax MiniMax M2.7 OpenHands | 34.9 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 16.8"} |
| 24 | Claude Haiku 4.5 Claude Code | 30.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 21.3"} |
| 25 | Gemini Gemini 3.1 Flash Lite OpenHands | 20.1 | resolution rate (%) | {"condition":"With Skills","source_recomputed_date":"2026-07-16","published_delta":"+ 4.1"} |

[来源1](https://huggingface.co/datasets/benchflow/skillsbench-leaderboard/resolve/main/leaderboard/skillsbench/v1.1/official.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）；[来源3](https://www.skillsbench.ai)（访问 2026-11-08）

### 覆盖与时效

HF机器导出24配置×2条件=48行为独立可审计轨，每条件原数值原样保留；官网25配置的24配对+HY3仅With共49行单独成轨，保留其公开小数精度。HF卡称2026-06-16、官网称2026-07-16、每行recomputed_date又不同，分别记录，不把访问日冒充重算日。Vals可读With Skills表35配置另成轨；该页配对图只有舍入值，未反推更精确No Skills榜。

[来源1](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源2](https://www.skillsbench.ai)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/benchflow/skillsbench-leaderboard/resolve/main/leaderboard/skillsbench/v1.1/official.json)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

xiangyi@benchflow.ai

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-07）

### 官方反馈

https://github.com/benchflow-ai/skillsbench/issues

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### 公开社区

https://discord.gg/G9dg3EfSva

[来源1](https://github.com/benchflow-ai/skillsbench/blob/main/README.md)（访问 2026-11-08）

### 隐私边界

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2602.12670

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### 本轮PDF SHA-256

e987ebc3f0084a1ffc8acbca58259e33120b95fcef3876abfad060e169cf210b

> 本次实际下载的PDF字节计算；未上传Drive。

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### 本轮PDF字节数

```json
1769852
```

[来源1](https://arxiv.org/pdf/2602.12670)（访问 2026-11-08）

### Drive文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://www.vals.ai/benchmarks/skillsbench"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2602.12670"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://github.com/benchflow-ai/skillsbench",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://huggingface.co/datasets/benchflow/skillsbench",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://www.skillsbench.ai",
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）；[来源2](https://github.com/benchflow-ai/skillsbench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源4](https://www.skillsbench.ai)（访问 2026-11-08）

### Drive PDF归档

待核实

[来源1](https://www.vals.ai/benchmarks/skillsbench)（访问 2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。SkillsBench不是AgentBench；With Skills和No Skills是同一条目的实验条件，不重复新增。 热度与榜单口径分离，不确定值标记待核实。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST)",
    "change": "深度复核论文/官方实现与数据卡；补全可审计字段；按版本、来源与协议重建榜单轨；明确无法核实及相互冲突的统计。未上传Drive。"
  }
]
```

[来源1](https://arxiv.org/abs/2602.12670)（访问 2026-11-08）；[来源2](https://github.com/benchflow-ai/skillsbench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/benchflow/skillsbench)（访问 2026-11-08）；[来源4](https://www.skillsbench.ai)（访问 2026-11-08）
