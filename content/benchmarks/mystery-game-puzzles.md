# Mystery Game Puzzles

> 核验日期：2026-11-08。未知不补造；来源访问日不等于实验运行日。

Epoch AI提供100个来自保密游戏变体的中局状态，每题选择唯一最优下一步，不是整局胜率或猜测游戏名称。官方主动不发布提示、例题和轨迹以降低专项准备风险。本次读到144条成功运行，分属1.0.4、1.1.0、1.2.0、1.2.1四个任务版本；不同版本的历史最高不能合成同版排行榜。
[本页导读依据](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

[补充导读依据](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

## 基本信息

### 简称

Mystery Game Puzzles

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 全称

Mystery Game Puzzles

> 沿用官方名称；不将论文标题臆造为全称。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 数据/基准版本

1.2.1（当前CSV中最新运行版本）

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 论文版本

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 发布日期

2026-07（官方BibTeX月份；精确日待核实）

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 主板块

推理

> Benchmark Atlas编辑分类。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 子领域

推理

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 许可边界

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 论文入口

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 代码入口

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 数据入口

未公开：官网明确目前不发布提示、示例局面或模型轨迹，以保持游戏身份保密。公开CSV是模型成绩，不是题库。

> 状态：未公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 官方主页

https://epoch.ai/benchmarks/mystery-game-puzzles

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 论文标题

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 发起与维护

### 发起方

Epoch AI

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 合作机构

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 作者

Epoch AI（官方BibTeX为机构作者，未据此补造个人作者名单）

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 当前维护方

Epoch AI

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 资助

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 设计目标

### 衡量能力

给定某款知名游戏变体的局面，选择唯一最佳下一步。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 设计动机

与Chess Puzzles类似，但隐藏游戏身份以降低针对性预训练或评测准备风险；不是证据充分的“探索隐藏游戏规则”任务。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 构建方式

### 题目来源

程序化随机采样对局，推进到中局并筛选唯一最佳下一步的状态。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 出题/构建者背景

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 审核流程

程序化筛选到唯一最佳着法；是否还有独立人工审校、游戏引擎版本及搜索深度待核实。

> 状态：待核实。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 质量控制

过滤到存在唯一最佳着法的局面；具体验证器与搜索深度待核实。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 去污染/泄漏控制

保密游戏身份、提示、例题和轨迹，以降低基准专项准备。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 数据形式

### 精确规模与统计口径

100个谜题局面

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 题型

100个中局状态，选择唯一最优下一步；不是整局胜率，也不是要求模型发现保密游戏名称的任务。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 模态

文本；工具交互

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 语言/代码语种

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 难度结构

程序采样随机对局并推进至中局，只保留有唯一最优下一步的状态；官方未给公开分级表，不凭模型分数推定跨游戏难度。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 公开与隐藏划分

未公开：游戏身份、提示、示例局面和模型轨迹（官网明确说明）。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 评测方法

### 指标

正确最佳下一步比例

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 评分规则

提交正规化为游戏记谱并与答案比对；不能提取有效着法为unanswered且无分，非法着法判错。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 运行与提示设置

最小agent scaffold，文本局面输入并使用submission工具。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 官方评测脚本

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 可比性警示

CSV存在1.0.4、1.1.0、1.2.1，不能把不同版本的历史最高直接视为同版榜。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 最新情况

### 核验日期

2026-11-08

> 本次源站访问日期；时区；不等于榜单运行日期。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
 "version": "1.2.1（当前CSV中最新运行版本）"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/benchmarks.csv"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Epoch CSV最近一条为Kimi K3.1 Pro，2026-11-06 09:59:23 开始；ECI当前纳入。主要证据仍来自Epoch自身。"
 }
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Epoch CSV最近一条为Kimi K3.1 Pro，2026-11-06 09:59:23 开始；ECI当前纳入。主要证据仍来自Epoch自身。"
 }
 ]
 "csv_versions": {
 "1.2.1": 6
 "1.2.0": 1
 "1.1.0": 5
 "1.0.4": 132
 }
 "observed_on": "2026-11-08"
}
```

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 论文/数据修订历史

官方网页BibTeX列2026年7月；CSV现有任务版本1.0.4、1.1.0、1.2.0、1.2.1。各版本技术变更及独立论文修订史待核实，不能把模型运行日期当benchmark发布日期。

> 状态：待核实。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 饱和性证据

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 污染与已知争议

官方不发布游戏身份、提示、例题和轨迹以减轻专项准备风险，因此公开可复核性受限；不能猜游戏名称。当前CSV含四种任务版本，v1.0.4的最高0.84不能与v1.2.1最高0.74混成同版排名。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 衍生与条目关系

方法上与Epoch Chess Puzzles相似，但保密游戏身份；它不是MysteryMechanism科学机制发现，也不将每个task version计作独立benchmark。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mysterymechanism)（访问 2026-11-08）

## 榜单快照

### 本次榜单采集日

2026-11-08

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 官方榜源

https://epoch.ai/benchmarks/mystery-game-puzzles

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 第三方覆盖

待核实

> 状态：待核实。

> epoch.ai/data/benchmarks.csv是创建者Epoch自身成绩源，不是独立第三方；本次纠正原先的误归类。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Epoch官方CSV / task version 1.2.1

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | GPT-6.1 Terra (max) | 0.74；stderr 0.04408440022768081 0–1 | mean_score | 2026-10-27 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 2 | Gemini 4 Argon (high) | 0.64；stderr 0.048241815132442176 0–1 | mean_score | 2026-10-14 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | Muse Wonder (max) | 0.51；stderr 0.05024183937956913 0–1 | mean_score | 2026-10-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 4 | DeepSeek V4.1 Flash 1017 (max) | 0.49；stderr 0.05024183937956914 0–1 | mean_score | 2026-10-20 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | Kimi K3.1 Pro (Together, max) | 0.42；stderr 0.04960449637488583 0–1 | mean_score | 2026-11-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 6 | Mistral Large 4 (high) | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-11-02 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- 本次同版本score排序，保留重复模型运行，不跨版本合并最高值

- 创建者自身评测；不同配置/运行ID独立保留

#### Epoch官方CSV / task version 1.2.0

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Mistral Large 4 Preview (high) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-10-14 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- 本次同版本score排序，保留重复模型运行，不跨版本合并最高值

- 创建者自身评测；不同配置/运行ID独立保留

#### Epoch官方CSV / task version 1.1.0

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | GPT-6.1 Sol (max) | 0.8；stderr 0.04020151261036849 0–1 | mean_score | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 2 | Claude Opus 5.5 (max) | 0.71；stderr 0.04560480215720687 0–1 | mean_score | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | Claude Sonnet 5.5 (max) | 0.65；stderr 0.04793724854411022 0–1 | mean_score | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 4 | DeepSeek V4.1 Flash (max) | 0.43；stderr 0.0497569851956243 0–1 | mean_score | 2026-10-09 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | Claude Haiku 5.5 (max) | 0.3；stderr 0.04605661864718382 0–1 | mean_score | 2026-10-08 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- 本次同版本score排序，保留重复模型运行，不跨版本合并最高值

- 创建者自身评测；不同配置/运行ID独立保留

#### Epoch官方CSV / task version 1.0.4

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | GPT-6 Astra (max) | 0.84；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-30 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 2 | Claude Opus 5 (max) | 0.59；stderr 0.04943110704237103 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | Claude Fable 5.1 (max) | 0.58；stderr 0.04960449637488583 0–1 | mean_score | 2026-09-02 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 3 | GPT-5.6 Sol (max) | 0.58；stderr 0.04960449637488583 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | GPT-6 Sol (max) | 0.56；stderr 0.049888765156985884 0–1 | mean_score | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 5 | GPT-5.5 (xhigh) | 0.56；stderr 0.049888765156985884 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 7 | Claude Fable 5 (max) | 0.52；stderr 0.05021167315686782 0–1 | mean_score | 2026-08-01 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 7 | GPT-5.5 (high) | 0.52；stderr 0.05021167315686782 0–1 | mean_score | 2026-07-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 9 | Gemini 3.8 Flash (high) | 0.47；stderr 0.05016135580465918 0–1 | mean_score | 2026-09-03 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 10 | DeepSeek V4 Pro 0813 (max) | 0.43；stderr 0.0497569851956243 0–1 | mean_score | 2026-08-20 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 11 | Qwen3.8 Max (xhigh) | 0.38；stderr 0.048783173121456344 0–1 | mean_score | 2026-08-05 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 12 | Gemini 3.7 Flash (high) | 0.37；stderr 0.048523658709390974 0–1 | mean_score | 2026-08-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 12 | Claude Opus 5 | 0.37；stderr 0.048523658709390974 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 12 | GPT-5.4 (xhigh) | 0.37；stderr 0.048523658709390974 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 15 | Claude Opus 4.8 | 0.36；stderr 0.04824181513244218 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 16 | Claude Sonnet 5 (max) | 0.35；stderr 0.04793724854411023 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 16 | GPT-5.6 Terra (max) | 0.35；stderr 0.047937248544110224 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 18 | Grok 4.6 (xhigh) | 0.34；stderr 0.04760952285695234 0–1 | mean_score | 2026-08-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 18 | DeepSeek V4 Flash 0731 (max) | 0.34；stderr 0.04760952285695233 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 18 | Gemini 3.1 Pro Preview | 0.34；stderr 0.04760952285695234 0–1 | mean_score | 2026-07-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 21 | GLM-5.3 (max) | 0.33；stderr 0.04725815626252608 0–1 | mean_score | 2026-08-31 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 21 | GPT-5.6 Sol (none) | 0.33；stderr 0.04725815626252608 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 23 | Gemini 3.1 Pro Preview | 0.32；stderr 0.04688261722621506 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 23 | Qwen3.7 Max | 0.32；stderr 0.04688261722621506 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 23 | Gemini 3.5 Flash | 0.32；stderr 0.04688261722621506 0–1 | mean_score | 2026-07-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 26 | Claude Opus 4.8 | 0.31；stderr 0.04648231987117317 0–1 | mean_score | 2026-07-27 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 27 | Gemini 3.6 Flash | 0.3；stderr 0.04605661864718382 0–1 | mean_score | 2026-08-05 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 28 | Grok 4.7 (xhigh) | 0.29；stderr 0.045604802157206865 0–1 | mean_score | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 28 | o3 (high) | 0.29；stderr 0.04560480215720687 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 28 | Gemini 3.1 Pro Preview | 0.29；stderr 0.04560480215720687 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | GPT-5.5 (low) | 0.28；stderr 0.045126085985421296 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | GPT-5.4 (medium) | 0.28；stderr 0.04512608598542129 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | Gemini 3.5 Flash | 0.28；stderr 0.045126085985421296 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 31 | Claude Opus 4.7 (max) | 0.28；stderr 0.04512608598542129 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | GPT-5.6 Sol (low) | 0.26；stderr 0.04408440022768081 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | qwen3.7-max_none | 0.26；stderr 0.0440844002276808 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | Gemini 3 Flash Preview | 0.26；stderr 0.0440844002276808 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 35 | Kimi K3 (max) | 0.26；stderr 0.0440844002276808 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Muse Spark 1.3 (max) | 0.25；stderr 0.044640484731156636 0–1 | mean_score | 2026-09-19 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Gemini 3.6 Flash | 0.25；stderr 0.04351941398892446 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Gemini 3 Flash Preview | 0.25；stderr 0.04351941398892446 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 39 | Claude Opus 4.6 (max) | 0.25；stderr 0.04351941398892446 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | o3 (medium) | 0.23；stderr 0.04229525846816507 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | GPT-5.2 (high) | 0.23；stderr 0.04229525846816508 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | Gemini 3.6 Flash | 0.23；stderr 0.04229525846816508 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 43 | GPT-5 (high) | 0.23；stderr 0.04229525846816508 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 47 | GPT-5.2 (medium) | 0.22；stderr 0.041633319989322654 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 47 | Qwen3.6 35B-A3B | 0.22；stderr 0.041633319989322654 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 47 | Claude Opus 4.5 (48k thinking) | 0.22；stderr 0.04163331998932266 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 50 | GPT-5.6 Luna (max) | 0.21；stderr 0.040936018074033236 0–1 | mean_score | 2026-07-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 50 | claude-opus-4-1-20250805_24K | 0.21；stderr 0.040936018074033236 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | GPT-5.6 Luna (none) | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-31 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | Qwen3.5 Flash | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | nemotron-3-ultra | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 52 | Gemini 3 Flash Preview | 0.2；stderr 0.04020151261036849 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | Qwen 3.6 Max (Preview) | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | GPT-5.6 Terra (low) | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | GPT-5.1 (low) | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | GLM-5.2 | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 56 | Gemini 3.5 Flash-Lite | 0.19；stderr 0.039427724440366255 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | Qwen3.5 397B-A17B | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | Qwen 3.6 Flash (2026-04-16) | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | GPT-5.5 (no thinking) | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | glm-5.2_minimal | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | GLM-5.2 | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 61 | Kimi K2.6 | 0.18；stderr 0.03861229196653691 0–1 | mean_score | 2026-07-18 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Qwen3.7 Plus | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | GPT-5.4 (low) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | qwen3.5-122b-a10b_none | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Qwen3.5 Plus | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | GPT-5.6 Luna (low) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Qwen3.7 Plus | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | DeepSeek v4 Pro (unknown thinking) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 67 | Claude Sonnet 4.5 (48k thinking) | 0.17；stderr 0.03775251680686369 0–1 | mean_score | 2026-07-25 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | GPT-5.4 (none) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-31 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | GPT-5.1 (medium) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | GPT-5 (low) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Qwen3.5 Flash | 0.16；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Claude Sonnet 4.6 (low) | 0.16；stderr 0.03684529491774706 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Claude Sonnet 5 (no thinking) | 0.16；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 75 | Qwen3.5 Plus | 0.16；stderr 0.036845294917747066 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | Qwen3.7 Flash | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | GPT-5 (medium) | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | GLM-5.2 | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | GPT-5.1 (no thinking) | 0.15；stderr 0.03588702812826368 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 82 | Claude Opus 4.6 (no thinking) | 0.15；stderr 0.03588702812826367 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 87 | Muse Spark 1.3 (xhigh) | 0.1414141414141414；stderr 0.03519858850692775 0–1 | mean_score | 2026-09-17 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | Qwen3.7 Flash | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | GPT-5.2 (none) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | GPT-5.6 Terra (none) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | GPT-5 (minimal) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 88 | Claude Sonnet 4.6 (no thinking) | 0.14；stderr 0.0348735088019777 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 93 | Claude Opus 4.7 (no thinking) | 0.13；stderr 0.033799766898963114 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Kimi K3 (low) | 0.12；stderr 0.032659863237109045 0–1 | mean_score | 2026-08-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | kimi-k2.6_none | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-29 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | GPT-4 (Jun 2023) | 0.12；stderr 0.032659863237109045 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Qwen 3.6 Flash (2026-04-16) | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | GPT-5.6 Luna (medium) | 0.12；stderr 0.032659863237109045 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Qwen 3.6 Plus (2026-04-02) | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | gpt-4o-mini-2024-07-18 | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 94 | Gemini 3.5 Flash-Lite | 0.12；stderr 0.03265986323710904 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 102 | GPT-5.4 mini (none) | 0.11；stderr 0.03144660377352201 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 103 | GPT-5.6 Terra (medium) | 0.1；stderr 0.03015113445777636 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 103 | GPT-5.2 (low) | 0.1；stderr 0.03015113445777636 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 103 | GPT-5 mini (minimal) | 0.1；stderr 0.03015113445777636 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | GPT-5 nano (medium) | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | Qwen3-235B-A22B-Thinking-2507 | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | GPT-5 nano (low) | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 106 | GPT-5.4 nano (no thinking) | 0.09；stderr 0.028762349126466143 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | GLM-5.3-Flash (max) | 0.08；stderr 0.027265992434429072 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | GPT-5.4 mini (low) | 0.08；stderr 0.027265992434429072 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | MiniMax-M3_none | 0.08；stderr 0.027265992434429075 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 110 | GPT-5 nano (high) | 0.08；stderr 0.027265992434429075 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | GPT-6 Luna (max) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | MiniMax-M3 | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | o3-mini (high) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | Qwen3.6 27B | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | GPT-5.4 mini (medium) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | GPT-4.1 mini | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 114 | Claude Opus 4.6 (low) | 0.07；stderr 0.02564323999762428 0–1 | mean_score | 2026-08-06 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 121 | GPT-5.4 nano (medium) | 0.06；stderr 0.0238683256575942 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 121 | Inkling Small (xhigh) | 0.06；stderr 0.023868325657594204 0–1 | mean_score | 2026-08-15 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | o4-mini (high) | 0.05；stderr 0.02190429135575903 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | GPT-5 mini (high) | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | GPT-5.4 nano (high) | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | Qwen3-Max-Instruct | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 123 | GPT-5 nano (minimal) | 0.05；stderr 0.021904291355759033 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 128 | GPT-5 mini (medium) | 0.04；stderr 0.019694638556693237 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 129 | GPT-5.4 nano (low) | 0.03；stderr 0.01714466079977653 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 129 | GPT-3.5 Turbo (Jan 2024) | 0.03；stderr 0.01714466079977653 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 131 | gpt-oss-120b_medium | 0.02；stderr 0.014070529413628966 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |
| 132 | gpt-oss-120b_high | 0.0；stderr 0.0 0–1 | mean_score | 2026-08-28 | [原始来源](https://epoch.ai/data/benchmarks.csv)（2026-11-08） |

- 本次同版本score排序，保留重复模型运行，不跨版本合并最高值

- 创建者自身评测；不同配置/运行ID独立保留

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖范围与限制

完整收录本次CSV的144条成功运行；按1.0.4/1.1.0/1.2.0/1.2.1四赛道分隔，并保留原始stderr精度、模型配置和run_id。最新一条Kimi K3.1 Pro (Together, max)于2026-11-06 09:59:23 开始。CSV是Epoch自身评测，不算独立第三方；不假定不同版本分数完全可比。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

## 联系方式

### 公开研究邮箱

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 项目反馈入口

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 官方公开社交入口

https://www.linkedin.com/company/epochai（官网页脚官方链接）

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 公开渠道/隐私边界

https://epoch.ai/privacy（官网页脚隐私政策入口）

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

## 原始文件

### 源站PDF

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### PDF SHA-256

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### PDF字节数

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）

### 文件夹

待核实

> 状态：待核实。

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 其他官方文档

```json
[
 {
 "type": "官方方法网页（非独立论文PDF）"
 "url": "https://epoch.ai/benchmarks/mystery-game-puzzles"
 "accessed": "2026-11-08"
 }
 {
 "type": "官方原始运行成绩CSV（非题库）"
 "url": "https://epoch.ai/data/benchmarks.csv"
 "accessed": "2026-11-08"
 }
 {
 "type": "打开核验的官方/研究来源"
 "url": "https://www.vals.ai/benchmarks/mysterymechanism"
 "accessed": "2026-11-08"
 }
]
```

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）；[来源2](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源3](https://www.vals.ai/benchmarks/mysterymechanism)（访问 2026-11-08）

### 原始PDF

待核实

> 状态：待核实。

> 按本批范围不上传；不是官方未公开。

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 变更记录

### 变更记录

```json
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
```

[来源1](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-08）
