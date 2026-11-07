# SpireClimb

> 核验日期：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未知不等于未公开。热度与成绩快照分开记录。

编辑状态：官方存在性已核验；字段级研究快照；note: trending: A

## 基本信息

### 简称

SpireClimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 全称

SpireClimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 基准版本

StS2冻结v0.107.1.1；StS1 A20 Heart与StS2 A10双轨

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 论文版本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 发布日期

2026-10（官方BibTeX月份；具体日待核实）

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑分类。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 领域标签

- 游戏

> 编辑标签；空列表表示尚未补充细分标签。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 许可证

评测代码许可待核实；游戏内容有版权，Epoch说明仅为研究与评论使用，不分发游戏本体。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 论文入口

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方代码

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 数据地址

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方入口

https://epoch.ai/benchmarks/spireclimb

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 论文标题

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 发起与维护

### 发起机构

Epoch AI

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 合作方

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 作者

Epoch AI（官方建议引用署名）

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 维护方

Epoch AI

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 资助

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

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

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 审核流程

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 质量控制

固定StS2游戏版本；发现save scumming样本排除后重跑。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 去污染

官方承认流行游戏可能成为训练目标；冻结版本改善可解释性但不声称无污染。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 数据形式

### 题量与规模

StS1：4角色×15=60局；StS2：5角色×15=75局。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 题型

通过截图、鼠标键盘完成完整游戏流程。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 模态

- 截图
- 鼠标键盘动作
- 文字笔记
- 限定wiki搜索

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 语言

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 难度

StS1 Ascension 20 Heart Kill；StS2 Ascension 10。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 公开与隐藏划分

固定共享种子；种子清单及隐藏划分细节待核实。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 评测方法

### 指标

两款游戏各自胜率，再对两游戏等权平均（不是135局直接混合胜率）。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 评分方式

StS1需击杀Heart、StS2需通过3幕；成功局比例；两轨必须保持版本一致。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 提示与运行设置

Inspect ReAct computer-use harness；模型最大推理档，300,000 tokens压缩阈值且笔记保留；仅可检索Slay the Spire wiki；StS1截图1280×720、StS2 1280×800。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方评测脚本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 可比性警示

2026-11-05修复StS1开局Neow奖励缺失后重新评分；旧版不可直接作为同协议当前榜；不与后续StS2公众更新版本混比。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度A沿用候选分级；证据性质逐项标明，多URL不自动等于多个独立采纳方，也不把当前可见当作近期首发。

- Epoch公布Neow奖励修复并重新评分。 [来源](https://epoch.ai/benchmarks/spireclimb)（证据日期 2026-11-05；访问 2026-11-07）
- 当前ECI纳入SpireClimb。 [来源](https://epoch.ai/data/eci-documentation/data)（证据日期 2026-11-07；访问 2026-11-07）

### 核验日期

2026-11-07 KST / Asia/Seoul

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 当前版本与2026H2使用证据

- **version**：StS2冻结v0.107.1.1；StS1 A20 Heart与StS2 A10双轨
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://epoch.ai/benchmarks/spireclimb", "date": "2026-11-05", "date_type": "source_calendar_date", "note": "Epoch公布Neow奖励修复并重新评分。"}, {"url": "https://epoch.ai/data/eci-documentation/data", "date": "2026-11-07", "date_type": "observed_on", "note": "当前ECI纳入SpireClimb。"}]

> 热度A沿用候选分级；证据性质逐项标明，多URL不自动等于多个独立采纳方，也不把当前可见当作近期首发。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）；[来源2](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 修订历史

2026-11-05方法修复Neow奖励：GPT-6 Astra StS1 16.7%→33.3%，GPT-6.1 Sol 20%→18.3%，不是两游戏合成分数。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 饱和情况

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 污染与争议

训练针对热门游戏的风险、版本固定后偏离玩家最新策略的风险；save scumming靠行为检查排除而非机械禁止。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 衍生与版本关系

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方榜单入口

https://epoch.ai/benchmarks/spireclimb

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 第三方评测入口

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "GPT-6 Astra (max)", "score": 0.33999999999999997, "metric": "equal-weight two-game win rate (0–1)", "stderr": 0.04131325151634216, "source_url": "https://epoch.ai/data/benchmarks.csv", "source_date": "待核实（CSV不提供整体榜单更新日）", "run_started_at": "2026-11-05T03:35:57.934000+09:00 KST", "run_id": "steambench-sts1-a20h-cd6cd8bb290a7ae3+steambench-sts2-a10-cdf1c9fa85cb6300", "task_version": "待核实", "collected_at": "2026-11-07 KST"}
- {"rank": 2, "model": "GPT-6.1 Sol (max)", "score": 0.23833333333333334, "metric": "equal-weight two-game win rate (0–1)", "stderr": 0.03653377199465138, "source_url": "https://epoch.ai/data/benchmarks.csv", "source_date": "待核实（CSV不提供整体榜单更新日）", "run_started_at": "2026-11-05T03:36:01.058000+09:00 KST", "run_id": "steambench-sts1-a20h-e795fd781f73bd66+steambench-sts2-a10-9a23c8dea53b6755", "task_version": "待核实", "collected_at": "2026-11-07 KST"}
- {"rank": 3, "model": "GPT-6.1 Terra (max)", "score": 0.22333333333333333, "metric": "equal-weight two-game win rate (0–1)", "stderr": 0.03386031744341088, "source_url": "https://epoch.ai/data/benchmarks.csv", "source_date": "待核实（CSV不提供整体榜单更新日）", "run_started_at": "2026-11-05T03:35:54.875000+09:00 KST", "run_id": "steambench-sts1-a20h-263bd0e64b156075+steambench-sts2-a10-1102b0b9cf1785f6", "task_version": "待核实", "collected_at": "2026-11-07 KST"}

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 覆盖与时效说明

由官方CSV构建可审计快照：每个精确model配置先取最新成功run，再按mean_score降序；rank为该最新run集合中的点估计名次，同分并列。不是Epoch网页平滑或聚合榜；不以旧run最佳成绩挑分。CSV整体更新日待核实，run开始时间已转换KST。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- benchmarks@epoch.ai

[来源1](https://epoch.ai/benchmarks)（访问 2026-11-07）

### 公开反馈渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 隐私政策

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Drive资料目录

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方方法/介绍网页（不是论文PDF）", "url": "https://epoch.ai/benchmarks/spireclimb"}

[来源1](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组只建立本地研究文件，不上传或声明已有Drive PDF。

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "新建近期热门中文研究条目；区分当前榜单与历史结果；缺项逐字段标记。"}

[来源](https://epoch.ai/benchmarks/spireclimb)（访问 2026-11-07）
