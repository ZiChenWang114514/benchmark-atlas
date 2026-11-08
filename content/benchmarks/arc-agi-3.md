# ARC-AGI-3

> 核验日期：2026-11-07。；访问日不是测量日。

无文字规则的交互游戏评测，衡量相对人类行动效率而非普通胜率。真正AI Verified榜在/leaderboard，Standard与Provider Adapter最高分不同，必须分轨。

## 基本信息

### 简称

ARC-AGI-3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 全称

ARC-AGI-3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 基准版本

3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 论文版本

技术报告，2026-04-22

> 报告标题页日期，不冒充benchmark首发日期。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 发布日期

2026-03-25（官方宣布发布的日历日，未给精确时刻；技术报告日期为4月22日）

[来源1](https://arcprize.org/blog/arc-agi-3-launch)（访问 2026-11-07）

### 主板块

推理

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 领域标签

- 交互式推理
- 探索与世界模型
- 行动效率

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 许可证

ARC-AGI Toolkit软件MIT；不据此推断全部游戏内容或私有测试环境也为MIT，后者授权待核实。

> 字段状态：待核实

[来源1](https://github.com/arcprize/arc-agi/blob/main/LICENSE)（访问 2026-11-07）

### 论文

https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 官方代码

https://github.com/arcprize/arc-agi

[来源1](https://docs.arcprize.org/)（访问 2026-11-07）

### 数据地址

https://arcprize.org/tasks?v=3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 官方入口

https://arcprize.org/arc-agi/3

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 论文标题

ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

## 发起与维护

### 发起方

ARC Prize

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 作者

ARC Prize Foundation；环境设计Hunter Henry，工程David Wexler/Derek Smith，基准设计François Chollet；完整开发名单见报告首页。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 维护方

ARC Prize Foundation

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://docs.arcprize.org/)（访问 2026-11-07）

### 资助方

待核实

> 字段状态：待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## 设计目标

### 衡量能力

在新交互环境中探索、获取目标、形成世界模型、跨步骤适应。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 设计背景

静态谜题不足以反映随经验学习与行动效率；交互评测关注学习过程而非最终答案。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## 构建方式

### 题目来源

全新可交互游戏环境。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 出题者背景

基金会内部游戏设计工作室手工设计新环境；不是抽取现成电子游戏关卡，也不是自然语言考试题。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 审核流程

设计→工程实现→结构与平台可靠性测试→人类校准；每环境10名普通参与者初见测试，仅纳入人类可完成环境。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 质量控制

资格检查环境接口/运行可靠性，以可达状态图探索研究随机策略通关概率；人类校准建立upper-median best action baseline。报告接受阈值为随机策略单关通关不高于1/10000，但示例ls20首关图又给1/355，需保留例外，不宣称全部关卡保证一致。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 去污染

公开demo刻意不全面覆盖私有机制；半私有给API模型测试，完全私有用于比赛，力求OOD机制而非公开题微调。官方设计目标不能等同已证明模型训练零污染。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

## 数据形式

### 题量与规模

报告Table1：公开demo25、半私有55、完全私有55个环境；环境下多级游戏，不能把环境数当单关题数。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 题型

无自然语言任务说明的多步游戏探索。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 模态

- 视觉网格
- 离散动作
- 反馈

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 语言

核心游戏无自然语言规则、指令或目标说明；以64×64/16色网格观察及离散动作交互，工具API代码为接口，不是英语理解题。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://github.com/arcprize/arc-agi)（访问 2026-11-07）

### 难度

稀疏反馈下长程规划与技能获取效率。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 公开与隐藏划分

25公开demo较易、偏可玩；55半私有用于frontier API模型测评；55完全私有用于比赛。公开集不是与测试同分布的训练集。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

## 评测方法

### 指标

RHAE（Relative Human Action Efficiency）：对比人类基线行动次数的学习/完成效率，而非简单游戏胜率。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 评分

每关效率min(1.15,(human_actions/agent_actions)^2)，未完成关为0；按关序号线性加权，环境分受完成关权重比例封顶，再对全部环境求平均。每关可到115%，最终总体0–100%。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 运行设置

Standard harness携带模型选择的笔记；Provider Adapter保留推理状态并压缩长对话，两种实现分别列榜。游戏初见、无自然语言任务说明；预算需随具体官方结果保留。

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 官方脚本

https://github.com/arcprize/arc-agi

> 公开Toolkit、scorecard接口及game版本；README的SDK0.9.9不是benchmark v3的新版本号。

[来源1](https://github.com/arcprize/arc-agi)（访问 2026-11-07）；[来源2](https://docs.arcprize.org/)（访问 2026-11-07）

### 可比性警示

Standard与Provider Adapter分轨，不能用99.9% Adapter替代62.7% Standard。/arc-agi/3/leaderboard是人类榜入口，AI verified榜实际在/leaderboard；赛事结束横幅不是AI榜缺失。

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 最新版本与采用证据

```json
{
 "version": "3"
 "heat_confidence": "A"
 "why_trending": "候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。"
 "evidence_2026_h2": [
 {
 "url": "https://openai.com/index/gpt-6-astra/"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "OpenAI"
 "note": "当前发布页实际报告该benchmark分数；厂商自报。"
 }
 {
 "url": "https://arcprize.org/arc-agi/3"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "官方维护方"
 "note": "已打开当前官方方法与榜单；观察日不冒充发布时间。"
 }
 ]
}
```

[来源1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）；[来源2](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 修订历史

官方PDF封面2026-04-22；不是arXiv论文，未见可核验的独立修订版本历史，待核实。

> 字段状态：待核实

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 饱和情况

当前官方表：Standard最高62.7%，Provider Adapter最高99.9%；不同harness结论完全不同，不能单凭Adapter接近100%宣称一般智能已解决。

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）；[来源2](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 污染与争议

公开demo/私有测试刻意OOD；排行榜预览和未完成测试有单独政策。报告的随机通关接受阈值与ls20首关示例不同，描述为设计/校准证据而非所有关卡数学保证。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 版本与衍生关系

ARC-AGI-3在ARC-AGI-1/2静态视觉推理之外增加交互探索；三版本的任务、分数、harness独立呈现。Toolkit0.9.9是运行库版本，不是新增benchmark条目。

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）；[来源2](https://github.com/arcprize/arc-agi)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 官方榜单

https://arcprize.org/leaderboard

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 分轨结果

#### 官方Verified / Standard

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | GPT-6 Astra | 62.7 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 2 | GPT-6.1 Sol | 52.7 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 3 | Gemini 4 Argon | 49.8 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |

> GPT-6 Astra：{"source_date_column": "2026-09-02", "date_column_note": "网页Date/Release date列，不自动解释为实际运行日"}

> GPT-6.1 Sol：{"source_date_column": "2026-09-29", "date_column_note": "网页Date/Release date列，不自动解释为实际运行日"}

> Gemini 4 Argon：{"source_date_column": "2026-10-13", "date_column_note": "网页Date/Release date列，不自动解释为实际运行日"}

#### 官方Verified / Provider Adapter

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | GPT-6 Astra | 99.9 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 2 | Gemini 4 Argon | 97.5 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |
| 3 | GPT-6.1 Sol | 96.4 | ARC-AGI-3 RHAE (%) | [原表](https://arcprize.org/leaderboard)，2026-11-07 |

> GPT-6 Astra：{"source_date_column": "2026-09-02", "date_column_note": "网页Date/Release date列，不自动解释为实际运行日"}

> Gemini 4 Argon：{"source_date_column": "2026-10-13", "date_column_note": "网页Date/Release date列，不自动解释为实际运行日"}

> GPT-6.1 Sol：{"source_date_column": "2026-09-29", "date_column_note": "网页Date/Release date列，不自动解释为实际运行日"}

> 从官方完整表按v3两列分别读取排序；未混入v1/v2列或社区Kaggle分数。

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

### 覆盖说明

首次取得真正AI Verified榜。旧条目只抓人类榜赛事横幅，故误写无法核验；现补Standard/Provider Adapter各前三，数据采集日不等于运行日。

[来源1](https://arcprize.org/leaderboard)（访问 2026-11-07）

## 联系方式

### 公开科研联系邮箱

待核实

> 字段状态：待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 公开反馈

https://github.com/arcprize/arc-agi/issues

[来源1](https://github.com/arcprize/arc-agi)（访问 2026-11-07）

### 官方社交

https://discord.gg/9b77dPAmcA

[来源1](https://docs.arcprize.org/)（访问 2026-11-07）

### 隐私说明/政策

https://arcprize.org/privacy

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### PDF SHA-256

33a19ce7973afb5c15a91566a340e3745f8c9fd6f041f601c0f544cbe982799f

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### PDF字节数

1184316

[来源1](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)（访问 2026-11-07）

### 文件夹

待核实

> 字段状态：待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 其他官方材料

```json
[
 {
 "type": "正式发布文章"
 "url": "https://arcprize.org/blog/arc-agi-3-launch"
 "accessed": "2026-11-07"
 }
 {
 "type": "Toolkit文档"
 "url": "https://docs.arcprize.org/"
 "accessed": "2026-11-07"
 }
 {
 "type": "AI Verified榜"
 "url": "https://arcprize.org/leaderboard"
 "accessed": "2026-11-07"
 }
]
```

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

### 论文副本

待核实

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）

## 变更记录

```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-07"
 最近复核
 }
]
```

[来源1](https://arcprize.org/arc-agi/3)（访问 2026-11-07）
