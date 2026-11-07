# Mystery Game Puzzles

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: A；未核实保留标记

## 基本信息

### 简称

Mystery Game Puzzles

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 全称

Mystery Game Puzzles

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 基准版本

1.2.1（当前CSV中最新运行版本）

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 发布日期

2026-07（官方BibTeX月份；精确日待核实）

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 主板块

推理

> Benchmark Atlas编辑分类。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 领域标签

- 推理

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 论文

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 代码

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 数据集

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 官方主页

https://epoch.ai/benchmarks/mystery-game-puzzles

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 论文标题

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 发起与维护

### 发起方

Epoch AI

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 作者

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 维护方

Epoch AI

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 设计目标

### 衡量能力

给定某款知名游戏变体的局面，选择唯一最佳下一步。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 设计背景

与Chess Puzzles类似，但隐藏游戏身份以降低针对性预训练或评测准备风险；不是证据充分的“探索隐藏游戏规则”任务。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 构建方式

### 题目来源

程序化随机采样对局，推进到中局并筛选唯一最佳下一步的状态。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 出题者背景

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 审核

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 质量控制

过滤到存在唯一最佳着法的局面；具体验证器与搜索深度待核实。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 去污染

保密游戏身份、提示、例题和轨迹，以降低基准专项准备。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 数据形式

### 题量与规模

100个谜题局面

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 题型

游戏状态文本输入，通过工具提交单一下一步。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 模态

- 文本
- 工具交互

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 语言

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 难度

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 公开与隐藏划分

未公开：游戏身份、提示、示例局面和模型轨迹（官网明确说明）。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 评测方法

### 指标

正确最佳下一步比例

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 评分

提交正规化为游戏记谱并与答案比对；不能提取有效着法为unanswered且无分，非法着法判错。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 运行设置

最小agent scaffold，文本局面输入并使用submission工具。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 官方脚本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 可比性警示

CSV存在1.0.4、1.1.0、1.2.1，不能把不同版本的历史最高直接视为同版榜。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：1.2.1（当前CSV中最新运行版本）
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://epoch.ai/data/benchmarks.csv", "date": "2026-11-07", "date_type": "observed_on", "note": "Epoch CSV最近一条为Kimi K3.1 Pro，2026-11-06 09:59:23 KST开始；ECI当前纳入。主要证据仍来自Epoch自身。"}, {"url": "https://epoch.ai/data/eci-documentation/data", "date": "2026-11-07", "date_type": "observed_on", "note": "Epoch CSV最近一条为Kimi K3.1 Pro，2026-11-06 09:59:23 KST开始；ECI当前纳入。主要证据仍来自Epoch自身。"}]

> Epoch CSV最近一条为Kimi K3.1 Pro，2026-11-06 09:59:23 KST开始；ECI当前纳入。主要证据仍来自Epoch自身。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；[来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 污染、争议与限制

游戏保密有利防专项优化，但公开复核和复现受限；不猜测游戏真实名称。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 为什么近期热门

Epoch CSV最近一条为Kimi K3.1 Pro，2026-11-06 09:59:23 KST开始；ECI当前纳入。主要证据仍来自Epoch自身。

[来源](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）；[来源](https://epoch.ai/data/eci-documentation/data)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 官方榜单入口

https://epoch.ai/benchmarks/mystery-game-puzzles

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 第三方覆盖

https://epoch.ai/data/benchmarks.csv

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | GPT-6.1 Terra (max) | 0.74 | task version 1.2.1 mean_score (0–1) | 待核实（页面未明示榜表更新时间） |
| 2 | Gemini 4 Argon (high) | 0.64 | task version 1.2.1 mean_score (0–1) | 待核实（页面未明示榜表更新时间） |
| 3 | Muse Wonder (max) | 0.51 | task version 1.2.1 mean_score (0–1) | 待核实（页面未明示榜表更新时间） |

- GPT-6.1 Terra (max)：stderr 0.0440844；运行开始2026-10-27 05:00:37 KST

- Gemini 4 Argon (high)：stderr 0.0482418；运行开始2026-10-14 02:14:57 KST

- Muse Wonder (max)：stderr 0.0502418；运行开始2026-10-15 01:17:18 KST

> 仅对CSV中task version=1.2.1记录排序；不是跨版本总榜。

[来源](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

### 覆盖与时效

Epoch自身评测CSV；rank为本次同版筛选结果。CSV于11月6日仍有Kimi K3.1 Pro运行，不把运行次数当引用人数。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://epoch.ai/benchmarks/mystery-game-puzzles"}

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://epoch.ai/benchmarks/mystery-game-puzzles)（访问 2026-11-07）
