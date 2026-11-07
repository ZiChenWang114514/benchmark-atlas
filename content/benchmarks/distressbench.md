# DistressBench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: B；未核实保留标记

## 基本信息

### 简称

DistressBench

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 全称

DistressBench

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 基准版本

v1

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 主板块

安全

> Benchmark Atlas编辑分类。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 领域标签

- 生物与医学
- 心理健康

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 许可证

公开主数据集卡CC BY 4.0；LH为安全研究受限附录；论文强调评测用途、不用作训练。

[来源](https://huggingface.co/datasets/ScaleAI/DistressBench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2610.12758

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 代码

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/ScaleAI/DistressBench

[来源](https://huggingface.co/datasets/ScaleAI/DistressBench)（访问 2026-11-07）

### 官方主页

https://labs.scale.com/leaderboard/distressbench

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 论文标题

DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

## 发起与维护

### 发起方

Scale AI

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 作者

- Drew Rein
- Patrick Oathout
- Vishal Kumar
- Udari Madhushani Sehwag

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 维护方

Scale Labs

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

## 设计目标

### 衡量能力

心理危机支持中的识别、恰当共情、降级干预和人类援助转介，而非只测拒答。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 设计背景

不输出有害内容不等于给予有效支持；单轮二元拒答指标漏测隐性危机与识别后不行动。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

## 构建方式

### 题目来源

持证临床人员与危机咨询师编写的模拟对话，不是患者聊天或临床记录。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 出题者背景

持证临床人员和危机咨询师；无真实患者信息。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 审核

临床写用户提示及笔记，模型起草rubric/参考回答，经临床人员重写；自动检查与多层人工审核。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 质量控制

75任务、2908临床共识判断校准三裁判面板；多轮连贯性门控。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 去污染

50/50分层公开/私有划分，私有半集用于污染检查。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

## 数据形式

### 题量与规模

718对话、23子类、6901加权原子标准；299单轮，419多轮（3–5用户轮）。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 题型

危机对话回复，按任务专有rubric评价最终assistant轮。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 模态

- 文本对话

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 语言

仅英语；援助资源标准以美国为中心。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 难度

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 公开与隐藏划分

公开359题、私有359题；主榜以全部718题为口径。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

## 评测方法

### 指标

Weighted Rubric Score：每题满足的临床标准权重比例，三次运行均值。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 评分

Opus 4.8、Llama 4 Maverick、Gemini 3.1 Pro独立二元判决后多数票；最终轮权重平均，空回复0；10000次bootstrap区间。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 运行设置

HF：无system prompt，三次独立运行；默认4096 token，部分模型8192/16384，具体以release_metadata.json为准。

[来源](https://huggingface.co/datasets/ScaleAI/DistressBench)（访问 2026-11-07）

### 官方脚本

HF仓库code/grade_public_split.py及code/README.md

[来源](https://huggingface.co/datasets/ScaleAI/DistressBench)（访问 2026-11-07）

### 可比性警示

论文/榜单描述标准helpful system，但当前HF发布说明no system prompt；需固定release_metadata再复现。主榜与公开半集、LH不可混用。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

[发布卡对照](https://huggingface.co/datasets/ScaleAI/DistressBench)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：v1
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://labs.scale.com/leaderboard/distressbench", "date": "2026-11-07", "date_type": "observed_on", "note": "2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。"}, {"url": "https://arxiv.org/abs/2610.12758", "date": "2026-11-07", "date_type": "observed_on", "note": "2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。"}]

> 2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）；[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 饱和情况

主榜最高约88.4%权重满足率不等于完全rubric通过或临床安全；高分不授权心理健康产品部署。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 污染、争议与限制

候选所列2605.13318实际是VERA-MH，非DistressBench论文；已纠正。官网实时表有新增模型但叙述仍为25模型，不能照搬论文前三冒充当前榜。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 衍生与版本关系

DistressBench-LH是20条长时红队附录，不纳入本主榜。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### 为什么近期热门

2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问2026-11-07）；[来源](https://arxiv.org/abs/2610.12758)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 官方榜单入口

https://labs.scale.com/leaderboard/distressbench

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 第三方覆盖

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | muse-spark-1.2 | 88.39 | Weighted Rubric Score (%) | 待核实（页面未明示榜表更新时间） |

- muse-spark-1.2：±0.93；当前网页第一项可核实

> 当前表第二至第四名存在模型名但抽取缺少分数，不填猜测值。论文前三另外有旧静态快照，不能替代缺失实时分数。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问2026-11-07）

### 覆盖与时效

只保存可完整对应的实时榜首。榜表rank与统计band不同，不能称细微差异显著；当前表更新日待核实。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2610.12758

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2610.12758)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://labs.scale.com/leaderboard/distressbench"}

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://labs.scale.com/leaderboard/distressbench)（访问 2026-11-07）
