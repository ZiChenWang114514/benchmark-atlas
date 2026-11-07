# Chess Puzzles (Epoch)

> 核验日期：2026-11-07（Asia/Shanghai，UTC+8）。官方资料中文改写；待核实不等于未公开。

已核实存在；官方资料研究快照，未知保留待核实；trending: A

## 基本信息

### 简称

Chess Puzzles (Epoch)

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 全称

Chess Puzzles (Epoch)

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 基准版本

v2（CSV最新出现2.1.0；分数分版本保存）

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 论文版本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 发布日期

2025-12-10（初始发布）；v2于2026-10-14发布。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 主板块

推理

> 编辑归档；跨领域只计主板块。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 领域标签

```json
[
  "推理"
]
```

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 许可证

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 论文

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 官方代码

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 数据地址

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 官方入口

https://epoch.ai/benchmarks/chess-puzzles

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 论文标题

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Epoch AI

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 合作方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 作者

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 维护方

Epoch AI

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 资助方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 设计目标

### 衡量能力

从文本棋局状态选择唯一最佳下一步，关注空间推理与规划。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 设计背景

低成本程序生成新题，避免直接依赖公开棋谱题库；不是视觉棋盘识别或完整对局水平。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 构建方式

### 题目来源

先随机走6个完整回合，再以随机Elo的Stockfish模拟；全强度Stockfish筛选唯一最佳着且未被模拟玩家选择的局面，排除明显吃子失误。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 出题者背景

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 审核流程

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 质量控制

Stockfish确定唯一最佳着；排除吃无防护子、低值吃高值等明显失误。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 去污染

Epoch程序新生成，不来自已有题库；生成Stockfish具体版本因记录不足无法核实。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 数据形式

### 题量与规模

100个新生成棋局。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 题型

FEN文本输入；submit_answer工具提交起止格四字符走法。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 模态

```json
[
  "文本"
]
```

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 语言

FEN为棋局编码，评测提示为英语。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 难度

作者主观评价从相对直接到较难；5位人类各答约20题的样本测试，不能当完整题集人类基线。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 公开与隐藏划分

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 评测方法

### 指标

最佳走法精确匹配正确率。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 评分

提交后规范大小写、标点与空白，再与标准答案确定性精确匹配。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 运行设置

qa_agent，1,000,000输出token预算；单次模型输出被截断可继续，耗尽总预算时要求立即提交。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 官方脚本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 可比性警示

v2与v1分数并不完全可比；CSV还含2.0.0/2.0.1/2.1.0，不跨版本取最高分当统一榜。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 最新版本与热门证据

```json
{
  "version": "v2（CSV最新出现2.1.0；分数分版本保存）",
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/data/benchmarks.csv",
      "date": "2026-11-06",
      "date_type": "source_calendar_date",
      "note": "最新CSV中Kimi K3.1 Pro(Together,max)实跑2.1.0，45%；开始时间2026-11-06 08:59:23（Asia/Shanghai，UTC+8）；不是引用次数。"
    }
  ]
}
```

> 热度等级沿候选采用；只保留本轮已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 修订历史

2026-10-14 v2发布，改用qa_agent与确定性匹配；CSV已出现2.1.0。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 饱和情况

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 污染与争议

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 版本与已有条目关系

与当前100条目的id、名称、版本字段去重后未收录

> 已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 为什么近期热门

近期实际使用与审查证据如下；不以采集日冒充发布日期。

- 2026-11-06（source_calendar_date）：最新CSV中Kimi K3.1 Pro(Together,max)实跑2.1.0，45%；开始时间2026-11-06 08:59:23（Asia/Shanghai，UTC+8）；不是引用次数。 [来源](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 官方榜单

https://epoch.ai/benchmarks/chess-puzzles

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 第三方覆盖

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 核验结果

```json
[
  {
    "rank": 1,
    "model": "GPT-6 Astra (pro, max)",
    "score": 0.76,
    "metric": "exact-match accuracy (0–1)",
    "stderr": 0.04292346959909278,
    "task_version": "2.0.1",
    "run_started_at": "2026-10-16T00:14:15+08:00",
    "timezone": "Asia/Shanghai (UTC+8)",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "accessed": "2026-11-07"
  },
  {
    "rank": 2,
    "model": "GPT-5.2 (xhigh)",
    "score": 0.48,
    "metric": "exact-match accuracy (0–1)",
    "stderr": 0.05021167315686782,
    "task_version": "2.0.1",
    "run_started_at": "2026-10-15T00:16:30+08:00",
    "timezone": "Asia/Shanghai (UTC+8)",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "accessed": "2026-11-07"
  },
  {
    "rank": 3,
    "model": "DeepSeek V4.1 Flash 1017 (max)",
    "score": 0.46,
    "metric": "exact-match accuracy (0–1)",
    "stderr": 0.05009082659620331,
    "task_version": "2.0.1",
    "run_started_at": "2026-10-20T06:39:00+08:00",
    "timezone": "Asia/Shanghai (UTC+8)",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 覆盖说明

从官方CSV仅筛Success、task=Chess Puzzles、task version=2.0.1后按mean_score取前三运行配置；不是全版本实时榜。最新2.1.0未并入；CSV未给总榜更新时间，逐条记录运行开始时间。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 公开反馈

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 官方社交

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 隐私政策

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### PDF字节数

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### Drive文件夹

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方方法或项目页",
    "url": "https://epoch.ai/benchmarks/chess-puzzles",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai (UTC+8)",
    "change": "首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传Drive。"
  }
]
```

[来源1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

