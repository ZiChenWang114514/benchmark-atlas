# SWE-bench Multimodal

> 核验日期：2026-11-07（Asia/Shanghai，UTC+8）。官方资料中文改写；待核实不等于未公开。

已核实存在；官方资料研究快照，未知保留待核实；trending: B

## 基本信息

### 简称

SWE-bench Multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 全称

SWE-bench Multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 基准版本

Multimodal v2

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 论文版本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 发布日期

2026-09-01（Multimodal v2）

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 主板块

代码

> 编辑归档；跨领域只计主板块。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 领域标签

```json
[
  "多模态"
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 许可证

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2410.03859

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 官方代码

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 数据地址

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 官方入口

https://www.swebench.com/multimodal.html

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 论文标题

SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Stanford University与Princeton University研究团队

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 合作方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 作者

John Yang、Carlos E. Jimenez、Alex L. Zhang、Kilian Lieret等

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 维护方

Stanford University与Princeton University研究团队

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 资助方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 设计目标

### 衡量能力

利用截图或短录屏理解真实JavaScript仓库问题，定位并修复代码。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 设计背景

纯文本SWE-bench不能覆盖图表、界面、语法高亮等视觉证据决定需求的场景。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 构建方式

### 题目来源

从真实仓库视觉issue扩展SWE-bench；v2移除已知不稳定或不可评分测试，重建Docker环境与视觉资产处理。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 出题者背景

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 审核流程

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 质量控制

v2剔除flaky/ungradeable测试并重建环境，解决依赖和browser drift。

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 去污染

实例id包含上游修复PR号，有联网查答案风险；Vals全程禁网络并提前下载视觉素材。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 数据形式

### 题量与规模

v2测试集480任务、11仓库；原始发布517视觉issue，不与旧题量混用。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 题型

issue文本与图像输入，输出代码diff。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 模态

```json
[
  "文本",
  "图像",
  "代码"
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 语言

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 难度

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 公开与隐藏划分

v2完整480题test split与评测工具开源；具体数据下载位置待核实。

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

## 评测方法

### 指标

测试判定issue解决正确率（Accuracy）。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 评分

Vals以mini-swe-agent单次运行，预下载截图附到首条消息；上游harness按仓库自身测试判定修复成功。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 运行设置

mini-swe-agent；issue文本、首轮附截图、shell与独立sandbox；每模型每题运行一次，误差条为二项标准误。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 官方脚本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 可比性警示

与已有swe-bench-verified是同系列不同任务域/模态，不是Verified同题新版；Vals关闭网络，不能与能查官方补丁的联网结果比较。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 最新版本与热门证据

```json
{
  "version": "Multimodal v2",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/swebench-multimodal",
      "date": "2026-11-05",
      "date_type": "source_calendar_date",
      "note": "Vals AI当前方法与榜单实际评测多模型；主要单一机构当前展示，不代表行业广泛采纳。"
    }
  ]
}
```

> 热度等级沿候选采用；只保留本轮已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 修订历史

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 饱和情况

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 污染与争议

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 版本与已有条目关系

与已有swe-bench-verified属于同系列但输入模态和任务域不同，独立收Multimodal v2；原始517题现保留480可复现题。

> 已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 为什么近期热门

主要单一机构当前展示或持续评测，不能称为行业广泛采纳。

- 2026-11-05（source_calendar_date）：Vals AI当前方法与榜单实际评测多模型；主要单一机构当前展示，不代表行业广泛采纳。 [来源](https://www.vals.ai/benchmarks/swebench-multimodal)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 官方榜单

https://www.vals.ai/benchmarks/swebench-multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 第三方覆盖

https://www.vals.ai/benchmarks/swebench-multimodal

> Vals自建基准与独立运行外部基准性质不同；同机构多URL不等于独立复核。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 核验结果

```json
[
  {
    "rank": 1,
    "model": "Claude Opus 5.5",
    "score": 70.21,
    "metric": "Accuracy (%)",
    "source_url": "https://www.vals.ai/benchmarks/swebench-multimodal",
    "accessed": "2026-11-07",
    "source_date": "2026-11-05"
  },
  {
    "rank": 2,
    "model": "Claude Fable 5.1",
    "score": 61.25,
    "metric": "Accuracy (%)",
    "source_url": "https://www.vals.ai/benchmarks/swebench-multimodal",
    "accessed": "2026-11-07",
    "source_date": "2026-11-05"
  },
  {
    "rank": 3,
    "model": "Claude Sonnet 5.5",
    "score": 58.33,
    "metric": "Accuracy (%)",
    "source_url": "https://www.vals.ai/benchmarks/swebench-multimodal",
    "accessed": "2026-11-07",
    "source_date": "2026-11-05"
  }
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 覆盖说明

仅记录已打开页面可读的当前分数；表内模型配置保留，不将不同harness当裸模型对比。榜表更新时间：2026-11-05

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

```json
[
  "johnby@stanford.edu",
  "carlosej@cs.princeton.edu"
]
```

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 公开反馈

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 官方社交

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 隐私政策

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### PDF字节数

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Drive文件夹

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方方法或项目页",
    "url": "https://www.vals.ai/benchmarks/swebench-multimodal",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

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

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

