# MultiChallenge

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: B**。2026-11-07打开Scale官方榜可见新前沿模型及当前结果；仅证明单一创建机构仍维护展示（B），不是11月7日发生新运行的证据。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

## 基本信息

### 简称

MultiChallenge

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 全称

MultiChallenge

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 基准版本

官方榜2026-02-03裁判/题目修订口径

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 论文版本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 发布日期

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 主板块

语言

> 编辑归档，不代表官方分类。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 领域标签

```json
[]
```

> 编辑归档，不代表官方分类。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 许可证

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2501.17399

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 官方代码

https://github.com/ekwinox117/multi-challenge

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 数据地址

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 官方入口

https://labs.scale.com/leaderboard/multichallenge?tab=large

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 论文标题

MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

## 发起与维护

### 发起机构

Scale AI

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 作者

Ved Sirdeshmukh、Kaustubh Deshpande、Johannes Mols、Lifeng Jin、Ed-Yeremai Cardona、Dean Lee、Jeremy Kritz、Willow Primack、Summer Yue、Chen Xing

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 维护方

Scale AI

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

## 设计目标

### 衡量能力

多轮对话中的指令保持、用户信息推断记忆、可靠版本编辑与自洽，联合考察上下文注意及推理。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 设计背景

MT-Bench近饱和；纯格式多轮指令测试未覆盖自然对话中混合推理和约束。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

## 构建方式

### 题目来源

多agent合成候选，再由训练过的标注者审核编辑；仅保留令六个筛选模型中至少三个合理失败的样本。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 出题者背景

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 审核流程

审核定义一致性、自然真实性及失败合理性；初始编辑后另有两层独立复核。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 质量控制

审核定义一致性、自然真实性及失败合理性；初始编辑后另有两层独立复核。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 去污染

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

## 数据形式

### 题量与规模

论文273对话：推断记忆113、指令保持69、版本编辑41、自洽50；每段最多10轮。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 题型

给定对话历史，对最后用户请求生成开放回答。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 模态

```json
[
  "文本"
]
```

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 公开与隐藏划分

论文公开数据及自动评测代码；部分超出可靠裁判能力的困难题明确暂保留私有。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

## 评测方法

### 指标

实例rubric二元通过准确率；官方榜Rank(UB)另依95%CI统计显著关系计算。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 评分

针对最终回答的实例级yes/no rubric，由模型裁判，不要求单一参考文本精确匹配。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 提示与运行设置

官网2026-02-03更新裁判为Gemini 2.5 Pro，54题的评测问题改得更清晰；早期论文实验用GPT-4o等裁判不可直接混用。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 官方评测脚本

https://github.com/ekwinox117/multi-challenge

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 可比性警示

对六个筛选模型存在选择偏差；官网Rank(UB)是1+显著优于它的模型数量，不能把原始分数顺序冒充统计排名。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "官方榜2026-02-03裁判/题目修订口径",
  "trending": "B",
  "heat_evidence": "2026-11-07打开Scale官方榜可见新前沿模型及当前结果；仅证明单一创建机构仍维护展示（B），不是11月7日发生新运行的证据。",
  "evidence_2026_h2": [
    {
      "url": "https://labs.scale.com/leaderboard/multichallenge?tab=large",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 修订历史

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 饱和情况

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 污染与争议

对六个筛选模型存在选择偏差；官网Rank(UB)是1+显著优于它的模型数量，不能把原始分数顺序冒充统计排名。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

### 版本与衍生关系

Large/Small是模型分组，不新建不同benchmark；与IFEval单轮形式约束互补而非同一测试。

[来源](https://arxiv.org/abs/2501.17399)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 官方榜单

https://labs.scale.com/leaderboard/multichallenge?tab=large

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 第三方覆盖

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "gpt 6.1 Sol",
    "score": 81.95,
    "metric": "Scale官方Performance Comparison准确率 (%)；附95%CI",
    "source_url": "https://labs.scale.com/leaderboard/multichallenge?tab=large",
    "source_date": "待核实（榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "分数顺序（非统计Rank UB）",
    "confidence_interval": "±4.16（95%CI）"
  },
  {
    "rank": 2,
    "model": "Gemini 4 Argon",
    "score": 78.7,
    "metric": "Scale官方Performance Comparison准确率 (%)；附95%CI",
    "source_url": "https://labs.scale.com/leaderboard/multichallenge?tab=large",
    "source_date": "待核实（榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "分数顺序（非统计Rank UB）",
    "confidence_interval": "±5.3（95%CI）"
  },
  {
    "rank": 3,
    "model": "Muse Spark",
    "score": 75.52,
    "metric": "Scale官方Performance Comparison准确率 (%)；附95%CI",
    "source_url": "https://labs.scale.com/leaderboard/multichallenge?tab=large",
    "source_date": "待核实（榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "分数顺序（非统计Rank UB）",
    "confidence_interval": "±4.05（95%CI）"
  }
]
```

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 时效与覆盖说明

对六个筛选模型存在选择偏差；官网Rank(UB)是1+显著优于它的模型数量，不能把原始分数顺序冒充统计排名。 榜表自写更新时间：待核实；采集日不等于运行日。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

https://arxiv.org/pdf/2501.17399

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2501.17399)（访问2026-11-07）

### PDF SHA-256

70b688b241c7f4e5ec0b6639f6eaf044ddc19dcf60ee7329d8078ec8a3aa285f

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2501.17399)（访问2026-11-07）

### PDF字节数

2789352

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2501.17399)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://labs.scale.com/leaderboard/multichallenge?tab=large"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2501.17399"
  }
]
```

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。Large/Small是模型分组，不新建不同benchmark；与IFEval单轮形式约束互补而非同一测试。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问2026-11-07）
