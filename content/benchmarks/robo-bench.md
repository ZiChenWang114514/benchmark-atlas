# Robo-bench

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: B**。Vals于2026-10-13更新7模型，主要单一机构专有测试展示（B），不是已证实广泛采用。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 基本信息

### 简称

Robo-bench

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 全称

Robo-bench

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 基准版本

2026-10-13官方榜快照

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 论文版本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 发布日期

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 主板块

机器人与具身

> 编辑归档，不代表官方分类。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 领域标签

```json
[]
```

> 编辑归档，不代表官方分类。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 许可证

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 论文

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 官方代码

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 数据地址

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/robo_bench

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 论文标题

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 发起与维护

### 发起机构

Vals AI

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 作者

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 维护方

Vals AI

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 设计目标

### 衡量能力

仅以机器人规格、传感器和摄像头，在实时物理环境中自主编写感知、规划及低层控制。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 设计背景

不预装运动规划器或平衡控制器，直接衡量通用agent控制机器人的能力，模型思考延迟计入真实时间。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 构建方式

### 题目来源

MuJoCo中的7自由度Franka Panda机械臂及29自由度Unitree G1人形机器人；24任务涵盖装配、灵巧操作、动力学、移动操作等。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 出题者背景

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 审核流程

每个任务参考解须在五个seed全部成功，静止agent不应成功；仿真器位于agent不可读端并签名计分。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 质量控制

每个任务参考解须在五个seed全部成功，静止agent不应成功；仿真器位于agent不可读端并签名计分。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 去污染

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 数据形式

### 题量与规模

24任务：13机械臂、11人形；每模型每任务一次、单seed。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 题型

动作/传感闭环任务；公开天平、积木说明书和忍者路线三例。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 模态

```json
[
  "摄像头图像",
  "深度图",
  "状态传感器",
  "电机命令",
  "代码"
]
```

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 公开与隐藏划分

公开3任务，另外21任务保持私有（官网明确）。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 评测方法

### 指标

各任务按顺序里程碑计0–100分，24任务平均；另列机械臂/人形分项和首次动作时间。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 评分

里程碑必须顺序达成；任务总分100，仿真端验证；不能将28.33分解释为28.33%任务完整成功。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 提示与运行设置

每episode三分钟真实墙钟、无准备时间；每模型用厂商coding agent最高推理设置，无现成控制器。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 官方评测脚本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 可比性警示

每任务只跑一次；官方说明重复运行总分可变约10分，小差距无显著性保证。不同厂商harness也影响分数。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "2026-10-13官方榜快照",
  "trending": "B",
  "heat_evidence": "Vals于2026-10-13更新7模型，主要单一机构专有测试展示（B），不是已证实广泛采用。",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/robo_bench",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 修订历史

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 饱和情况

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 污染与争议

每任务只跑一次；官方说明重复运行总分可变约10分，小差距无显著性保证。不同厂商harness也影响分数。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 版本与衍生关系

仿真机器人评测，不等于实机部署安全认证；机器人平台分项不另建benchmark。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 官方榜单

https://www.vals.ai/benchmarks/robo_bench

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 第三方覆盖

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "GPT-6.1 Sol",
    "score": 28.33,
    "metric": "Vals 24任务平均里程碑分 /100",
    "source_url": "https://www.vals.ai/benchmarks/robo_bench",
    "source_date": "2026-10-13",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 2,
    "model": "GPT-6 Astra",
    "score": 23.33,
    "metric": "Vals 24任务平均里程碑分 /100",
    "source_url": "https://www.vals.ai/benchmarks/robo_bench",
    "source_date": "2026-10-13",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 3,
    "model": "Claude Opus 5.5",
    "score": 14.58,
    "metric": "Vals 24任务平均里程碑分 /100",
    "source_url": "https://www.vals.ai/benchmarks/robo_bench",
    "source_date": "2026-10-13",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  }
]
```

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 时效与覆盖说明

每任务只跑一次；官方说明重复运行总分可变约10分，小差距无显著性保证。不同厂商harness也影响分数。 榜表自写更新时间：2026-10-13；采集日不等于运行日。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### PDF SHA-256

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### PDF字节数

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://www.vals.ai/benchmarks/robo_bench"
  }
]
```

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。仿真机器人评测，不等于实机部署安全认证；机器人平台分项不另建benchmark。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/robo_bench)（访问2026-11-07）
