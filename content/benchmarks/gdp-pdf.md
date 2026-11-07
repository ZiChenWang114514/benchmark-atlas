# GDP.pdf

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: A**。AA 2026-10-27 v5发布文继续以5%权重收录GDP.pdf，当前方法页明确100题×5次；Surge官方榜同时展示新模型。两机构是不同实现，不视为相同分数复核。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）；[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)（访问2026-11-07）

## 基本信息

### 简称

GDP.pdf

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 全称

GDP.pdf

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 基准版本

100题公开版

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 论文版本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 发布日期

2026-04-14（论文§5.1自述基准发布日期；7月论文不是首发日）

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 主板块

语言

> 编辑归档，不代表官方分类。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 领域标签

```json
[
  "长上下文",
  "多模态",
  "专业文档"
]
```

> 编辑归档，不代表官方分类。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 许可证

Apache-2.0（论文Table 2所述公开基准）；第三方PDF保留原始权利。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2607.11192

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 官方代码

https://github.com/surge-ai/gdp-pdf

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 数据地址

https://huggingface.co/datasets/surgeai/GDP.pdf

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 官方入口

https://surgehq.ai/benchmarks/gdp-pdf

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 论文标题

GDP.pdf: Benchmarking Grounded Multimodal Reasoning over Professional PDF Documents

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 发起与维护

### 发起机构

Surge AI

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 作者

Suhaas Garre、Emily Ritchie、Sushant Mehta、Edwin Chen

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 维护方

Surge AI

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 设计目标

### 衡量能力

围绕原始专业PDF完成有证据依据的真实工作问答，同时检验视觉解析、领域语义、跨页引用与无证据时的拒答。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 设计背景

OCR、单表格问答和学科视觉题分别达标，不代表能正确解释实际合同、福利文件、建筑图纸或临床文档。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 构建方式

### 题目来源

十个专业领域的从业者提交实际工作问题及原PDF；仅保留至少两个前沿模型产生实质错误的候选，排除仅靠常识能答或语义含混的题。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 出题者背景

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 审核流程

专家编写参考答案、原子rubric和能力标签；参考答案须通过自己的rubric，故意错误答案须被对应标准拦截；论文的错误分析另行人工核对原文。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 质量控制

专家编写参考答案、原子rubric和能力标签；参考答案须通过自己的rubric，故意错误答案须被对应标准拦截；论文的错误分析另行人工核对原文。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 去污染

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 数据形式

### 题量与规模

100题，十领域均衡分布；AA方法页记4,592页PDF和1,275项评分标准。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 题型

检索、比较、核算、摘要、跨页协调及无支持信息时的拒答；开放回答。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 模态

```json
[
  "PDF原文",
  "文本",
  "图像",
  "表格",
  "图表"
]
```

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 公开与隐藏划分

论文称100题及PDF、提示、rubric、标签全部公开；本次HF数据页返回401，公开性按论文陈述记录，不宣称已下载题库。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 评测方法

### 指标

严格任务通过率（全部rubric成立）与平均rubric得分；榜单采用严格通过率。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 评分

每个标准独立二元评分，任务全部标准通过才计pass；原版以Gemini 3.5 Flash裁判。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 提示与运行设置

原版每模型每题5次，无工具；原PDF通过供应商原生文件输入。AA改用OCR全文和页面图像，裁判GPT-5.6 Luna medium。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 官方评测脚本

https://github.com/surge-ai/gdp-pdf

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 可比性警示

AA与Surge共享题集但PDF输入和裁判不同；原生PDF与预解析OCR两套成绩不能直接互换。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "100题公开版",
  "trending": "A",
  "heat_evidence": "AA 2026-10-27 v5发布文继续以5%权重收录GDP.pdf，当前方法页明确100题×5次；Surge官方榜同时展示新模型。两机构是不同实现，不视为相同分数复核。",
  "evidence_2026_h2": [
    {
      "url": "https://surgehq.ai/benchmarks/gdp-pdf",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    },
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    },
    {
      "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）；[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)（访问2026-11-07）

### 修订历史

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 饱和情况

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 污染与争议

AA与Surge共享题集但PDF输入和裁判不同；原生PDF与预解析OCR两套成绩不能直接互换。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 版本与衍生关系

GDP.pdf不是GDPval，也不是GDP.xlsx：本条只记录专业PDF问答，不合并职业交付物或电子表格任务。

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 官方榜单

https://surgehq.ai/benchmarks/gdp-pdf

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 第三方覆盖

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "GPT 6.1 Sol (Max reasoning)",
    "score": 35,
    "metric": "Surge原版严格通过率 (%)",
    "source_url": "https://surgehq.ai/benchmarks/gdp-pdf",
    "source_date": "待核实（榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 2,
    "model": "GPT 6 Astra (Max reasoning)",
    "score": 34.2,
    "metric": "Surge原版严格通过率 (%)",
    "source_url": "https://surgehq.ai/benchmarks/gdp-pdf",
    "source_date": "待核实（榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 3,
    "model": "Muse Wonder Full (Max reasoning)",
    "score": 33.2,
    "metric": "Surge原版严格通过率 (%)",
    "source_url": "https://surgehq.ai/benchmarks/gdp-pdf",
    "source_date": "待核实（榜表更新时间）",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  }
]
```

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 时效与覆盖说明

AA与Surge共享题集但PDF输入和裁判不同；原生PDF与预解析OCR两套成绩不能直接互换。 榜表自写更新时间：待核实；采集日不等于运行日。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

suhaas@surgehq.ai

[来源](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

https://arxiv.org/pdf/2607.11192

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2607.11192)（访问2026-11-07）

### PDF SHA-256

e139828de98e24caee6ba7f749dd39e9c541ff16c7a6c91ddb18dcd5a8defda4

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2607.11192)（访问2026-11-07）

### PDF字节数

223397

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2607.11192)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://surgehq.ai/benchmarks/gdp-pdf"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2607.11192"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
  }
]
```

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。GDP.pdf不是GDPval，也不是GDP.xlsx：本条只记录专业PDF问答，不合并职业交付物或电子表格任务。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

### 口径补充来源

4,592页、1,275项评分标准及AA的PDF预处理/裁判设置以AA方法页为准。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）
