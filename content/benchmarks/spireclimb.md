# SpireClimb

> Benchmark Constitution · 深度复核 2026-11-08。官方存在性已核验；字段级研究快照；note: trending: A

SpireClimb让模型通过截图和鼠标键盘完成两款Slay the Spire最高难度整局游戏，测量长程决策和计算机操作可靠性。两游戏胜率等权，不能直接按135局混算；2026-11-05修复开局Neow奖励改变了一代游戏的测试设置。StS2冻结版本是v0.107.1，网页后面的脚注1并非版本后缀。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

## 基本信息

### 简称

SpireClimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 全称

SpireClimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 基准版本

StS2冻结v0.107.1；StS1 A20 Heart与StS2 A10双轨

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 论文版本

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 发布日期

2026-10-14 （官方首发分析页date元数据：2026-10-14；不是评测运行日）

[来源1](https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel)（访问 2026-11-08）

### 主板块

Agent

> Benchmark Atlas 编辑分类。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 领域

```json
[
  "游戏"
]
```

> 编辑标签；空列表表示尚未补充细分标签。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 许可与适用范围

评测代码许可待核实；游戏内容有版权，Epoch说明仅为研究与评论使用，不分发游戏本体。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 论文

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方代码

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 数据

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方入口

https://epoch.ai/benchmarks/spireclimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 论文标题

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 发起与维护

### 发起方

Epoch AI

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 合作/参与机构

评测由Epoch独立于Mega Crit Games开展，官方明确不分发或出售游戏版权内容；Mega Crit不能据此列为合作研发方。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 作者

```json
[
  "Benjamin Ou"
  "Simon Chen"
]
```

> 官方首发分析署名；不冒充尚未确认的独立学术论文作者表。

[来源1](https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel)（访问 2026-11-08）

### 维护方

Epoch AI

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 资助

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 设计目标

### 衡量能力

计算机使用、长程推理、战术决策与跨完整游戏流程的可靠性。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 设计背景

用最高难度真实游戏端到端胜率，而非短回合局部动作或孤立推理题。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 构建方式

### 题目来源

Slay the Spire 1和2，分别采用最高难度，所有内容解锁；每角色固定15随机种子供所有模型共用。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 出题者背景

首发分析作者Benjamin Ou与Simon Chen；文章作者简介称Ou为Epoch benchmarking researcher、UC Berkeley物理与计算机科学本科背景。

[来源1](https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel)（访问 2026-11-08）

### 审核流程

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 质量控制

固定StS2游戏版本；发现save scumming样本排除后重跑。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 污染控制

官方承认流行游戏可能成为训练目标；冻结版本改善可解释性但不声称无污染。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 数据形式

### 题量

StS1：4角色×15=60局；StS2：5角色×15=75局。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 任务形式

通过截图、鼠标键盘完成完整游戏流程。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 模态

```json
[
  "截图"
  "鼠标键盘动作"
  "文字笔记"
  "限定wiki搜索"
]
```

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 语言

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 难度

StS1 Ascension 20 Heart Kill；StS2 Ascension 10。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 公开与隐藏划分

每角色15个固定任意选定种子，所有模型使用相同种子；运行配置全部内容解锁。官网没有给出完整种子清单或独立隐藏集说明，相关细节待核实。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## 评测方法

### 指标

两款游戏各自胜率，再对两游戏等权平均（不是135局直接混合胜率）。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 评分

StS1需击杀Heart、StS2需通过3幕；成功局比例；两轨必须保持版本一致。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 运行设置

Inspect ReAct computer-use harness；模型最大推理档，300,000 tokens压缩阈值且笔记保留；仅可检索Slay the Spire wiki；StS1截图1280×720、StS2 1280×800。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 评测工具

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 可比性

2026-11-05修复StS1开局Neow奖励缺失后重新评分；旧版不可直接作为同协议当前榜；不与后续StS2公众更新版本混比。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "StS2 v0.107.1"
  "method_update": "2026-11-05 Neow奖励修复"
  "note": "网页v0.107.1后的上标1为脚注，不是第四段游戏版本号。"
}
```

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 修订历史

2026-11-05方法修复Neow奖励：GPT-6 Astra StS1 16.7%→33.3%，GPT-6.1 Sol 20%→18.3%，不是两游戏合成分数。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 饱和与能力边界

官方认为热门游戏可能被针对性训练并较快饱和，但本次CSV总体最高0.33999999999999997，并非满分；不能把最低难度的高胜率写成最高难度成绩。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

### 风险与争议

训练针对热门游戏的风险、版本固定后偏离玩家最新策略的风险；save scumming靠行为检查排除而非机械禁止。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 系列与衍生关系

Slay the Spire 1与2是同一基准的两个组成轨；最高难度总体为两游戏胜率等权平均，不拆分成两条新增benchmark。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 官方入口

https://epoch.ai/benchmarks/spireclimb

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 独立来源

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 分来源与协议结果

#### SpireClimb / CSV未标合成task version

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.33999999999999997 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-cd6cd8bb290a7ae3+steambench-sts2-a10-cdf1c9fa85cb6300","run_started_at_kst":"2026-11-05","stderr":"0.04131325151634216"} |
| 2 | GPT-6.1 Sol (max) | 0.23833333333333334 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-e795fd781f73bd66+steambench-sts2-a10-9a23c8dea53b6755","run_started_at_kst":"2026-11-05","stderr":"0.03653377199465138"} |
| 3 | GPT-6.1 Terra (max) | 0.22333333333333333 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-263bd0e64b156075+steambench-sts2-a10-1102b0b9cf1785f6","run_started_at_kst":"2026-11-05","stderr":"0.03386031744341088"} |
| 4 | GPT-6 Sol (max) | 0.09166666666666667 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-831fe00153e0f0b1+steambench-sts2-a10-edacf7bb0ae31edf","run_started_at_kst":"2026-11-06","stderr":"0.024324094573715753"} |
| 5 | Claude Opus 5.5 (max) | 0.058333333333333334 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-789f946c67a789f5+steambench-sts2-a10-ef454c368767b2a0","run_started_at_kst":"2026-11-05","stderr":"0.020285004230980282"} |
| 6 | Claude Fable 5.1 (max) | 0.02 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-2057a494867d184c+steambench-sts2-a10-413d1cc930f6d4c6","run_started_at_kst":"2026-11-06","stderr":"0.011389895949029987"} |
| 7 | Claude Sonnet 5.5 (max) | 0.013333333333333334 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-e8f930bf4d4f1a14+steambench-sts2-a10-5db0e95e99f6b21c","run_started_at_kst":"2026-11-06","stderr":"0.009364170421755878"} |
| 8 | GPT-6 Luna (max) | 0.0 | equal-weight two-game win rate (0–1) | {"run_id":"steambench-sts1-a20h-f7325d71b8b16f57+steambench-sts2-a10-0e148062f8e47c4a","run_started_at_kst":"2026-11-06","stderr":"0.0"} |

#### SpireClimb (Slay the Spire 1, Ascension 20 Heart) / 0.3.3_cd56aef

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.3333333333333333 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-cd6cd8bb290a7ae3","run_started_at_kst":"2026-11-05","stderr":"0.06137164119322156","task_version":"0.3.3_cd56aef"} |
| 2 | GPT-6.1 Sol (max) | 0.18333333333333332 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-e795fd781f73bd66","run_started_at_kst":"2026-11-05","stderr":"0.05037523978531015","task_version":"0.3.3_cd56aef"} |
| 3 | GPT-6.1 Terra (max) | 0.1 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-263bd0e64b156075","run_started_at_kst":"2026-11-05","stderr":"0.039056673294247155","task_version":"0.3.3_cd56aef"} |
| 4 | GPT-6 Sol (max) | 0.05 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-831fe00153e0f0b1","run_started_at_kst":"2026-11-06","stderr":"0.028374015326751195","task_version":"0.3.3_cd56aef"} |
| 4 | Claude Opus 5.5 (max) | 0.05 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-789f946c67a789f5","run_started_at_kst":"2026-11-05","stderr":"0.028374015326751195","task_version":"0.3.3_cd56aef"} |
| 6 | Claude Fable 5.1 (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-2057a494867d184c","run_started_at_kst":"2026-11-06","stderr":"0.0","task_version":"0.3.3_cd56aef"} |
| 6 | Claude Sonnet 5.5 (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-e8f930bf4d4f1a14","run_started_at_kst":"2026-11-06","stderr":"0.0","task_version":"0.3.3_cd56aef"} |
| 6 | GPT-6 Luna (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts1-a20h-f7325d71b8b16f57","run_started_at_kst":"2026-11-06","stderr":"0.0","task_version":"0.3.3_cd56aef"} |

#### SpireClimb (Slay the Spire 2, Ascension 10) / 0.3.3_447ebe2

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6.1 Terra (max) | 0.3466666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-1102b0b9cf1785f6","run_started_at_kst":"2026-11-04","stderr":"0.055323237980623115","task_version":"0.3.3_447ebe2"} |

#### SpireClimb (Slay the Spire 2, Ascension 10) / 0.3.3_e52e280

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.3466666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-cdf1c9fa85cb6300","run_started_at_kst":"2026-09-23","stderr":"0.055323237980623115","task_version":"0.3.3_e52e280"} |
| 2 | GPT-6.1 Sol (max) | 0.29333333333333333 | win rate (0–1) | {"run_id":"steambench-sts2-a10-9a23c8dea53b6755","run_started_at_kst":"2026-09-30","stderr":"0.052926375288708374","task_version":"0.3.3_e52e280"} |
| 3 | GPT-6 Sol (max) | 0.13333333333333333 | win rate (0–1) | {"run_id":"steambench-sts2-a10-edacf7bb0ae31edf","run_started_at_kst":"2026-09-23","stderr":"0.03951659855758794","task_version":"0.3.3_e52e280"} |
| 4 | Claude Opus 5.5 (max) | 0.06666666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-ef454c368767b2a0","run_started_at_kst":"2026-09-23","stderr":"0.028997255746722662","task_version":"0.3.3_e52e280"} |
| 5 | Claude Fable 5.1 (max) | 0.04 | win rate (0–1) | {"run_id":"steambench-sts2-a10-413d1cc930f6d4c6","run_started_at_kst":"2026-09-25","stderr":"0.022779791898059974","task_version":"0.3.3_e52e280"} |
| 6 | Claude Sonnet 5.5 (max) | 0.02666666666666667 | win rate (0–1) | {"run_id":"steambench-sts2-a10-5db0e95e99f6b21c","run_started_at_kst":"2026-09-30","stderr":"0.018728340843511757","task_version":"0.3.3_e52e280"} |
| 7 | GPT-6 Luna (max) | 0.0 | win rate (0–1) | {"run_id":"steambench-sts2-a10-0e148062f8e47c4a","run_started_at_kst":"2026-09-29","stderr":"0.0","task_version":"0.3.3_e52e280"} |

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖与时效

完整提取CSV当前24行SpireClimb记录，按task+task_version+精确model配置取最新成功run；总体8行与两游戏16行分轨，StS2两个task版本也分开。总体mean_score直接取源值，不重新近似合成；CSV没有全榜更新时间，started_at只作为运行开始时间且已转。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源2](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

```json
[
  "benchmarks@epoch.ai"
]
```

[来源1](https://epoch.ai/benchmarks)（访问 2026-11-07）

### 官方反馈

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 公开社区

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 隐私边界

仅记录Epoch公开的benchmark工作联系渠道，不收集游戏玩家或第三方个人信息。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）

## 原始文件

### 源站PDF

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### PDF字节数

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 文件夹

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "官方方法/介绍网页（不是论文PDF）"
    "url": "https://epoch.ai/benchmarks/spireclimb"
  }
  {
    "type": "已打开一手材料"
    "url": "https://epoch.ai/data/benchmarks.csv"
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### PDF归档

待核实

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

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

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）
