# DrugDiscoveryBench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: B；未核实保留标记

## 基本信息

### 简称

DrugDiscoveryBench

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 全称

DrugDiscoveryBench

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 主板块

化学

> Benchmark Atlas编辑分类。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 领域标签

- 生物与医学
- 药物发现

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 许可证

Preview数据：CC BY 4.0；完整集及代码许可不可据此外推。

[来源](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview)（访问 2026-11-07）

### 论文

https://labs.scale.com/papers/drugdiscoverybench

[来源](https://labs.scale.com/papers/drugdiscoverybench)（访问 2026-11-07）

### 代码

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview

[来源](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview)（访问 2026-11-07）

### 官方主页

https://labs.scale.com/leaderboard/drugdiscoverybench

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 论文标题

DrugDiscoveryBench: Can Coding Agents Assist Early-Stage Drug Discovery?

[来源](https://labs.scale.com/papers/drugdiscoverybench)（访问 2026-11-07）

## 发起与维护

### 发起方

Scale Labs与Phylo

[来源](https://labs.scale.com/papers/drugdiscoverybench)（访问 2026-11-07）

### 合作方

Phylo

[来源](https://labs.scale.com/papers/drugdiscoverybench)（访问 2026-11-07）

### 作者

Afra Feyza Akyürek、Xinming Tu（共同一作），Alec Gutmanstein、Jason Qin等；完整作者表见官方论文页。

[来源](https://labs.scale.com/papers/drugdiscoverybench)（访问 2026-11-07）

### 维护方

Scale Labs

[来源](https://labs.scale.com/papers/drugdiscoverybench)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

## 设计目标

### 衡量能力

早期药物发现的多步检索、计算和生物医学工具工作流：靶标、命中发现、构效分析和先导优化。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 设计背景

仅通用编码或知识问答难测制药真实流水线中的约束保持与科学规划。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

## 构建方式

### 题目来源

制药科学家与生物医学研究者根据真实PDB、专利、论文、数据库记录写作。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 出题者背景

药物与生物医学领域专家。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 审核

专家出题→第二专家复核→BenchGuard自动检查→作者方法可解性审核→修订→独立QC签署。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 质量控制

每题单一可验证终点；同时提供结果rubric与过程rubric，过程不进入主要分数。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 去污染

Preview含canary，明确不用于训练；完整金标准/rubric需访问审核。

[来源](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview)（访问 2026-11-07）

## 数据形式

### 题量与规模

82任务、7能力类别、4早期药物发现阶段，920条rubric标准。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 题型

3–12个人工定义步骤的工作流，最终输出整数、浮点、SMILES/InChIKey、排序或短表。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 模态

- 文本
- 代码
- 结构与数据库文件

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 语言

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 难度

专家多步任务；不覆盖候选药确定之后DMPK、毒理、制剂和临床。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 公开与隐藏划分

公开Preview为82条任务提示与元数据，不含金标准和评分rubric；完整集需人工审核访问，不等于完全未公开。

[来源](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview)（访问 2026-11-07）

## 评测方法

### 指标

Pass rate (%)；全任务三次平均；另有mean outcome score供论文分析。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 评分

GPT-5.4按专家加权rubric评最终answer.md；结果得100才算任务解决，拒答/超时/缺失均0；过程标准不计主分。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 运行设置

Scale-Biomni提供226函数、22领域、76文件数据湖和117科学包；Harbor格式；每次120分钟；原生harness或mini-SWE-agent。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 官方脚本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 可比性警示

模型、effort、harness共同构成配置。论文/页面旧key takeaways与实时表数值不同，不能混用。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：待核实
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://labs.scale.com/leaderboard/drugdiscoverybench", "date": "2026-11-07", "date_type": "observed_on", "note": "2026-11-07 KST观察Scale现行模型配置比较和官方Preview；热度B，主要是单一评测机构当前使用，不能宣称行业广泛采纳。"}, {"url": "https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview", "date": "2026-11-07", "date_type": "observed_on", "note": "2026-11-07 KST观察Scale现行模型配置比较和官方Preview；热度B，主要是单一评测机构当前使用，不能宣称行业广泛采纳。"}]

> 2026-11-07 KST观察Scale现行模型配置比较和官方Preview；热度B，主要是单一评测机构当前使用，不能宣称行业广泛采纳。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 污染、争议与限制

日期标定的在线数据库任务可能随时间漂移。论文页专家方法恢复说80/82，榜单方法段说76/82，保留冲突不择高数。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 为什么近期热门

2026-11-07 KST观察Scale现行模型配置比较和官方Preview；热度B，主要是单一评测机构当前使用，不能宣称行业广泛采纳。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问2026-11-07）；[来源](https://huggingface.co/datasets/ScaleAI/DrugDiscoveryBench-Preview)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 官方榜单入口

https://labs.scale.com/leaderboard/drugdiscoverybench

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 第三方覆盖

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | GPT 6 Astra (mini-SWE-agent) max | 68.7 | Pass rate (%) | 待核实（页面未明示榜表更新时间） |
| 2 | GPT 6 Astra (Codex) max | 65.4 | Pass rate (%) | 待核实（页面未明示榜表更新时间） |
| 3 | Gemini 4 Argon (mini-swe-agent) high | 65.4 | Pass rate (%) | 待核实（页面未明示榜表更新时间） |

- GPT 6 Astra (mini-SWE-agent) max：±2.50（页面表）

- GPT 6 Astra (Codex) max：±1.90（页面表）

- Gemini 4 Argon (mini-swe-agent) high：±2.90（页面表）

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问2026-11-07）

### 覆盖与时效

只提取Performance Comparison前三；key takeaways仍使用早期GPT-5.5等结果，不能当最新榜。模型×effort设置数正文出现12与16，而表更长，因此不填当前总模型数。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://labs.scale.com/leaderboard/drugdiscoverybench"}

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://labs.scale.com/leaderboard/drugdiscoverybench)（访问 2026-11-07）
