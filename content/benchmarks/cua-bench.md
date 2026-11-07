# CUA-bench

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: B**。Vals于2026-10-13更新9模型的商业游戏结果。热度B，目录与详情同属Vals，不能视为两个独立采纳方。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 基本信息

### 简称

CUA-bench

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 全称

CUA-bench

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 基准版本

2026-10-13官方榜快照

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 论文版本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 发布日期

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 主板块

Agent

> 编辑归档，不代表官方分类。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 领域标签

```json
[
  "游戏",
  "计算机使用"
]
```

> 编辑归档，不代表官方分类。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 许可证

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 论文

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 官方代码

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 数据地址

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/cua_bench

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 论文标题

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 发起与维护

### 发起机构

Vals AI

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 作者

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 维护方

Vals AI

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 设计目标

### 衡量能力

agent仅观察屏幕、使用键盘鼠标，在实时商业游戏中维持长期规划、视觉判断与操作。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 设计背景

多数agent基准提供文本状态、API或DOM，这里只提供像素与键鼠，动作延迟本身影响结果。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 构建方式

### 题目来源

六个商业游戏按三种类型配对：公开Minecraft、SUPERHOT、eFootball，各配一个同类型隐藏游戏。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 出题者背景

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 审核流程

冻结rubric对持久证据事后重评；离线游戏原生状态、在线体育视频扫描及人工疑难复核；录像签名、哈希核验。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 质量控制

冻结rubric对持久证据事后重评；离线游戏原生状态、在线体育视频扫描及人工疑难复核；录像签名、哈希核验。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 去污染

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 数据形式

### 题量与规模

6个游戏，每游戏3小时；每个模型-游戏单次trial。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 题型

屏幕视觉与键鼠交互；里程碑要求按顺序完成。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 模态

```json
[
  "屏幕图像",
  "视频证据",
  "键盘鼠标"
]
```

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 公开与隐藏划分

3个公开游戏；另3个游戏名与里程碑不公开（官网明确），按相同规则计分。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 评测方法

### 指标

六游戏各0–100里程碑分的均值；另报动作延迟和估计API成本。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 评分

每游戏阶梯共100分，后续里程碑不能跳过先决步骤；不足证据为评分失败，不直接计零。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 提示与运行设置

每游戏三小时含读屏、学习控制、失败重试和shell思考；使用厂商harness，通过MCP驱动GPU桌面，不得读取游戏内存或文件。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 官方评测脚本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 可比性警示

分数是里程碑均值，不等于游戏通关率；每cell单trial，公开-私有差距不能自动归因为训练污染。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "2026-10-13官方榜快照",
  "trending": "B",
  "heat_evidence": "Vals于2026-10-13更新9模型的商业游戏结果。热度B，目录与详情同属Vals，不能视为两个独立采纳方。",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/cua_bench",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 修订历史

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 饱和情况

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 污染与争议

分数是里程碑均值，不等于游戏通关率；每cell单trial，公开-私有差距不能自动归因为训练污染。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 版本与衍生关系

CUA-bench只收商业游戏键鼠评测；不能与OSWorld、一般CUA能力或游戏子分项混同。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 官方榜单

https://www.vals.ai/benchmarks/cua_bench

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 第三方覆盖

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "GPT-6 Astra",
    "score": 19.17,
    "metric": "Vals 六游戏平均里程碑分 /100",
    "source_url": "https://www.vals.ai/benchmarks/cua_bench",
    "source_date": "2026-10-13",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 2,
    "model": "Claude Opus 5.5",
    "score": 14.0,
    "metric": "Vals 六游戏平均里程碑分 /100",
    "source_url": "https://www.vals.ai/benchmarks/cua_bench",
    "source_date": "2026-10-13",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 3,
    "model": "Claude Fable 5.1",
    "score": 13.17,
    "metric": "Vals 六游戏平均里程碑分 /100",
    "source_url": "https://www.vals.ai/benchmarks/cua_bench",
    "source_date": "2026-10-13",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  }
]
```

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 时效与覆盖说明

分数是里程碑均值，不等于游戏通关率；每cell单trial，公开-私有差距不能自动归因为训练污染。 榜表自写更新时间：2026-10-13；采集日不等于运行日。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### PDF SHA-256

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### PDF字节数

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://www.vals.ai/benchmarks/cua_bench"
  }
]
```

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。CUA-bench只收商业游戏键鼠评测；不能与OSWorld、一般CUA能力或游戏子分项混同。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/cua_bench)（访问2026-11-07）
