# EBR-bench

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: A**。官方2026-09-22更新v4并在10月审计回应中报告新模型学习结果；本次重读Epoch CSV可见11月2日Mistral Large 4运行。A为候选分级，不据此声称多个独立创建机构。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 基本信息

### 简称

EBR-bench

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 全称

EBR-bench

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 基准版本

v4 methodology（2026-09-22）

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 论文版本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 发布日期

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 主板块

Agent

> 编辑归档，不代表官方分类。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 领域标签

```json
[
  "持续学习",
  "游戏"
]
```

> 编辑归档，不代表官方分类。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 许可证

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 论文

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 官方代码

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 数据地址

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 官方入口

https://epoch.ai/benchmarks/ebr-bench

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 论文标题

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 发起与维护

### 发起机构

Epoch AI

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 作者

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 维护方

Epoch AI

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 设计目标

### 衡量能力

通过反复游玩陌生复杂桌游Earthborne Rangers，衡量记笔记、长期策略与从经验中学习的能力。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 设计背景

不只检查首次答题，而是在同一任务连续尝试后是否改善；表现分和学习增益必须区分。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 构建方式

### 题目来源

独立数字化游戏初始五个游戏日；从任务、奖励及重要事件定义21个可得目标。游戏版权属于Earthborne Games，不代表其参与基准开发。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 出题者背景

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 审核流程

Generality Labs受Epoch委托于2026年7月审核v1；肯定游戏设计，同时质疑持续学习诱发与上下文整理；8月27日修复一个引擎bug。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 质量控制

Generality Labs受Epoch委托于2026年7月审核v1；肯定游戏设计，同时质疑持续学习诱发与上下文整理；8月27日修复一个引擎bug。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 去污染

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 数据形式

### 题量与规模

每run 10次游玩：8次学习、最后2次评分；每模型通常5个独立样本，旧实验10个；每次最多21目标。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 题型

卡牌查阅、路线规划、笔记管理和多步游戏决策。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 模态

```json
[
  "文本",
  "地图图像",
  "工具调用"
]
```

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 公开与隐藏划分

Epoch明确不分发或出售底层受版权保护游戏材料；公开的是方法与成绩，完整游戏及评测数据许可待核实。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 评测方法

### 指标

Topline：每run最后两次得分取较高，再跨样本汇总；得分为21目标比例；另研究消融学习增益。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 评分

以完成目标计分，不把游戏高分直接视为持续学习增益；学习增益需与仅两次游玩的消融对照。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 提示与运行设置

默认单agent、禁用特定卡牌，250k token压缩阈值；Fable系列用标称上下文90%；ReAct与Deep Agent多agent分开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 官方评测脚本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 可比性警示

v1/v2计分变更、v3压缩阈值取优、v4禁卡和采样量更改导致历史不完全可比；默认单agent不混多agent。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "v4 methodology（2026-09-22）",
  "trending": "A",
  "heat_evidence": "官方2026-09-22更新v4并在10月审计回应中报告新模型学习结果；本次重读Epoch CSV可见11月2日Mistral Large 4运行。A为候选分级，不据此声称多个独立创建机构。",
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/benchmarks/ebr-bench",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 修订历史

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 饱和情况

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 污染与争议

v1/v2计分变更、v3压缩阈值取优、v4禁卡和采样量更改导致历史不完全可比；默认单agent不混多agent。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 版本与衍生关系

Earthborne Rangers为游戏名，EBR-bench为Epoch研究基准；与游戏本体版权及作者关系区分。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 官方榜单

https://epoch.ai/benchmarks/ebr-bench

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 第三方覆盖

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "GPT-6.1 Terra (max)",
    "score": 0.780952380952381,
    "metric": "CSV mean_score（0–1，21目标比例）",
    "stderr": "0.05128728387747146",
    "run_id": "65SHyNJX5oxVADzzjkssFK",
    "started_at_kst": "2026-10-27T05:01:15+09:00 KST",
    "source_date": "待核实（CSV榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "note": "按CSV均值排序；可能跨历史协议，不作为统一v4严格排名。"
  },
  {
    "rank": 2,
    "model": "GPT-6 Astra (max)",
    "score": 0.7619047619047619,
    "metric": "CSV mean_score（0–1，21目标比例）",
    "stderr": "0.08384198505551908",
    "run_id": "GhVYxWxttDxZ7akiJQPYsE",
    "started_at_kst": "2026-08-31T00:38:49+09:00 KST",
    "source_date": "待核实（CSV榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "note": "按CSV均值排序；可能跨历史协议，不作为统一v4严格排名。"
  },
  {
    "rank": 3,
    "model": "Claude Opus 5.5 (max)",
    "score": 0.7142857142857142,
    "metric": "CSV mean_score（0–1，21目标比例）",
    "stderr": "0.07063046178186345",
    "run_id": "iKWWUmcuzRjqisoshKVEpL",
    "started_at_kst": "2026-09-23T06:38:58+09:00 KST",
    "source_date": "待核实（CSV榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "note": "按CSV均值排序；可能跨历史协议，不作为统一v4严格排名。"
  }
]
```

[来源](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

### 时效与覆盖说明

v1/v2计分变更、v3压缩阈值取优、v4禁卡和采样量更改导致历史不完全可比；默认单agent不混多agent。 榜表自写更新时间：待核实；采集日不等于运行日。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### PDF SHA-256

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### PDF字节数

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://epoch.ai/benchmarks/ebr-bench"
  }
]
```

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。Earthborne Rangers为游戏名，EBR-bench为Epoch研究基准；与游戏本体版权及作者关系区分。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://epoch.ai/benchmarks/ebr-bench)（访问2026-11-07）
