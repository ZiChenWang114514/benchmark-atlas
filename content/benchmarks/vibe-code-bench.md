# Vibe Code Bench v1.1

> 核验日期：2026-11-07（Asia/Shanghai，UTC+8）。官方资料中文改写；待核实不等于未公开。

已核实存在；官方资料研究快照，未知保留待核实；trending: B

## 基本信息

### 简称

Vibe Code Bench v1.1

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 全称

Vibe Code Bench v1.1

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 基准版本

v1.1

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文版本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 发布日期

2026-02-24（v1.1）

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 主板块

代码

> 编辑归档；跨领域只计主板块。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 领域标签

```json
[
  "代码"
]
```

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 许可证

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2603.04601

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 官方代码

https://github.com/vals-ai/VibeCodeBench-Openhands-Scaffold

[来源1](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### 数据地址

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/vibe-code

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 论文标题

Vibe Code Bench: Evaluating AI Models on End-to-End Web Application Development

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Vals AI

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 合作方

作者隶属Vals AI及MIT；不据作者隶属推断正式合作协议。

[来源1](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### 作者

Hung Tran、Langston Nashold、Rayan Krishnan、Antoine Bigeard、Alex Gu

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### 维护方

Vals AI

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 资助方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 设计目标

### 衡量能力

从自然语言规格零到一构建可部署网页应用，完成认证、数据、支付、邮件等用户流程。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 设计背景

函数生成或已有仓库修bug不足以检验完整应用交付、部署与服务集成。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 构建方式

### 题目来源

LLM生成初稿，PM与软件工程师多轮审查，规格与测试对齐，测试经人工检查。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 出题者背景

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 审核流程

产品经理与软件工程师多轮审核应用规格与测试；人工检查需求是否足以支持验证步骤。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 质量控制

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 去污染

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 数据形式

### 题量与规模

论文：100应用规格，50验证/50测试；964浏览器工作流、10,131子步骤。当前网页另称每规格20–60测试，与论文6–23工作流口径不一致。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### 题型

完整应用规格输入；输出可部署应用，浏览器逐步验证。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 模态

```json
[
  "文本",
  "代码",
  "网页视觉交互"
]
```

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 语言

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 难度

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 公开与隐藏划分

论文摘要称50私有验证/50隐藏测试，表3写Validation(public)；公开性互相矛盾，待确认，不能擅称完整开放。

[来源1](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

## 评测方法

### 指标

工作流通过率，按应用平均，误差条±1标准误。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 评分

浏览器agent执行预写用户工作流；至少90%子步骤成功则该工作流通过；按应用工作流通过比例再对应用平均。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 运行设置

OpenHands改造容器环境，最多5小时或1,000轮；终端、浏览器、自托管Supabase、Stripe测试模式、MailHog。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 官方脚本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 可比性警示

网页与论文对技术栈约束、测试数量及验证集公开性描述有冲突，分来源记录；当前v1.1榜单不等于论文早期16模型结果。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 最新版本与热门证据

```json
{
  "version": "v1.1",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/vibe-code",
      "date": "2026-11-05",
      "date_type": "source_calendar_date",
      "note": "Vals AI当前方法与榜单实际评测多模型；主要单一机构当前展示，不代表行业广泛采纳。"
    }
  ]
}
```

> 热度等级沿候选采用；只保留本轮已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 修订历史

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 饱和情况

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 污染与争议

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 版本与已有条目关系

与当前100条目的id、名称、版本字段去重后未收录

> 已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 为什么近期热门

主要单一机构当前展示或持续评测，不能称为行业广泛采纳。

- 2026-11-05（source_calendar_date）：Vals AI当前方法与榜单实际评测多模型；主要单一机构当前展示，不代表行业广泛采纳。 [来源](https://www.vals.ai/benchmarks/vibe-code)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 官方榜单

https://www.vals.ai/benchmarks/vibe-code

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 第三方覆盖

https://www.vals.ai/benchmarks/vibe-code

> Vals自建基准与独立运行外部基准性质不同；同机构多URL不等于独立复核。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 核验结果

```json
[
  {
    "rank": 1,
    "model": "Claude Sonnet 5.5 (OpenHands)",
    "score": 92.39,
    "metric": "Accuracy (%)",
    "source_url": "https://www.vals.ai/benchmarks/vibe-code",
    "accessed": "2026-11-07",
    "source_date": "2026-11-05"
  },
  {
    "rank": 2,
    "model": "Gemini 4 Argon (OpenHands)",
    "score": 91.91,
    "metric": "Accuracy (%)",
    "source_url": "https://www.vals.ai/benchmarks/vibe-code",
    "accessed": "2026-11-07",
    "source_date": "2026-11-05"
  },
  {
    "rank": 3,
    "model": "Claude Haiku 5.5 (OpenHands)",
    "score": 90.44,
    "metric": "Accuracy (%)",
    "source_url": "https://www.vals.ai/benchmarks/vibe-code",
    "accessed": "2026-11-07",
    "source_date": "2026-11-05"
  }
]
```

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 覆盖说明

仅记录已打开页面可读的当前分数；表内模型配置保留，不将不同harness当裸模型对比。榜表更新时间：2026-11-05

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

```json
[
  "hung@vals.ai",
  "langston@vals.ai",
  "rayan@vals.ai"
]
```

[来源1](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### 公开反馈

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 官方社交

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 隐私政策

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2603.04601

> 官方arXiv原论文PDF入口；本组不下载、不上传Drive。

[来源1](https://arxiv.org/abs/2603.04601)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### PDF字节数

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### Drive文件夹

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方方法或项目页",
    "url": "https://www.vals.ai/benchmarks/vibe-code",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

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

[来源1](https://www.vals.ai/benchmarks/vibe-code)（访问 2026-11-07）

