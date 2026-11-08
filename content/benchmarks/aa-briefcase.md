# AA-Briefcase

> 核验日期：2026-11-07 （UTC+8）。未知保留待核实；访问日不是测量日。

已核验存在；研究快照，未核实字段保留标记

评测四个私有多周工作场景的专业交付物，但每任务独立运行。公开Lite只是额外示例；v1.1改变Crowd-BT拟合，不是换了一套题。

## 基本信息

### 简称

AA-Briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 全称

AA-Briefcase

> 保留官方名称，不把论文标题自动扩写为全称。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 基准版本

v1.1

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 论文版本

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 发布日期

2026-06-18（官方首发文章日期；v1.1具体上线日待核实）

[来源1](https://artificialanalysis.ai/articles/aa-briefcase)（访问2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 领域标签

- 职业知识工作与多交付物

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 许可证

公开Lite为Apache-2.0、Stirrup框架为MIT；正式私有四场景数据许可待核实。

> 字段状态：待核实

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)（访问2026-11-07）；[来源2](https://github.com/ArtificialAnalysis/Stirrup/blob/main/LICENSE)（访问2026-11-07）

### 论文

待核实

> 字段状态：待核实

> 已核实官方方法页与发布文章；未找到独立原始论文PDF，不能把示例交付物PDF当论文。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 官方代码

https://github.com/ArtificialAnalysis/Stirrup

> 这是运行agent的公开harness，不代表私有题集和完整评分代码开源。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

### 数据地址

https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 官方入口

https://artificialanalysis.ai/evaluations/aa-briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 论文标题

待核实

> 字段状态：待核实

> 官方介绍页是方法/发布文章，独立论文标题尚待核实。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 发起与维护

### 发起方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 作者

Artificial Analysis 团队（方法页署名口径）

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 维护方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 资助方

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 设计目标

### 衡量能力

数据科学、产品管理、公司战略等专业知识工作的分析、格式化呈现和可用交付物。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 设计背景

只评短答案忽略真实职业流程中的文件分析、跨材料整合和电子表格/演示/备忘录品质。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 构建方式

### 题目来源

场景源文件混合真实、增强与合成材料，含Slack导出、邮件、表格、访谈和市场研究；后续周任务可提供全模型相同的标准参考产物。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

### 出题者背景

由行业专家历时数月构建，背景覆盖数据科学、产品管理、企业战略，官方举例包括Google、McKinsey & Company、Boston Consulting Group；不据从业背景推断机构合作。

[来源1](https://artificialanalysis.ai/articles/aa-briefcase)（访问2026-11-07）

### 审核流程

为交付物设计明确rubric，再结合分析质量与呈现质量的成对比较。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 质量控制

正式任务独立运行，不继承模型先前提交；后续周可提供全模型相同的base-case文件。按rubric客观条件与分析/呈现成对质量分开评分；公开Lite提供source_graph和traceability证据链。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)（访问2026-11-07）

### 去污染

正式四场景评分材料保留私有；公开第五Lite示例只供体验，不纳入正式榜。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 数据形式

### 题量与规模

4个正式多周场景，共91任务、数千输入文件；公开Lite为额外示例场景。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 题型

产出电子表格、演示文稿、备忘录等多种文件交付物。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 模态

- 文本
- 数据文件
- 表格
- 演示文稿/视觉呈现

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 语言

英语专业工作任务；文件格式与任务相依。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 难度

多周情境分解为独立任务；不是让模型真实持续运行数周。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 公开与隐藏划分

正式4场景91任务私有；公开Lite为第5场景的一周，4个任务、63项checks、67个来源/147文件，不计入正式榜。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 评测方法

### 指标

复合Elo；另列binary rubric通过率、Analytical Quality与Presentation成对比较。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 评分

rubric二元通过率转换为合成对局，与分析质量、呈现质量对局合成headline Elo；v1.1在各scope用Crowd-BT拟合评审质量。rubric与pairwise各用三模型panel，每项由均衡抽样的一个judge判定，而非三票多数。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase)（访问2026-11-07）

### 运行设置

每任务独立运行，无此前任务的自生成产物继承；Stirrup/E2B离线sandbox，最多500轮，代码执行、finish、放弃工具，支持视觉的模型可查看图像；正式任务1次运行。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

### 官方脚本

https://github.com/ArtificialAnalysis/Stirrup

> Lite公开prompts、grader/rubric、源文件与示例提交；正式私有全套实现不能由此推定已开放。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase)（访问2026-11-07）

### 可比性警示

v1.1仅改变Elo拟合，不改变题目；Elo取决于对手池、裁判与拟合，不能按百分正确率解释，也不能与v1 Elo直接作增减。每任务独立运行，不是模型持续工作数周。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 （UTC+8）

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 最新版本与采用证据

```json
{
  "version": "v1.1"
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1"
      "date": "2026-10-28"
      "note": "Artificial Analysis 2026-10-28文章实际报告 AA-Briefcase Elo以及Presentation、Analytical Quality等子维度结果；子维度不另计。"
    }
  ]
}
```

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

[来源1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 修订历史

v1.1仅改变Elo拟合：各scope采用Crowd-BT；不改变任务数量。论文修订历史待核实。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

### 饱和情况

headline是无固定100%上限的相对Elo，不能由1813判断接近饱和；应另看rubric通过率及任务失败类型。

> 方法论层面的解释，不主张已完成独立饱和度测量。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-briefcase)（访问2026-11-07）

### 污染与争议

主观成对判断和复合Elo受裁判、对手池与展示质量影响；正式材料私有降低泄漏但限制完整复现。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 版本与衍生关系

AA-Briefcase-Lite是公开示例，不另计正式benchmark；分析/呈现分项也不拆分。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 （UTC+8）

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 官方榜单

https://artificialanalysis.ai/evaluations/aa-briefcase

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 原值与官方榜完全相同，已纠正；不把AA自评标成独立复评。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 分轨结果

#### 官方当前v1.1

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Claude Sonnet 5.5 (Max, Default Fallback) | 1813 | AA-Briefcase v1.1 Elo | [原表](https://artificialanalysis.ai/evaluations/aa-briefcase) · 2026-11-07 |
| 2 | Claude Opus 5.5 (Max, Default Fallback) | 1800 | AA-Briefcase v1.1 Elo | [原表](https://artificialanalysis.ai/evaluations/aa-briefcase) · 2026-11-07 |
| 3 | Claude Opus 5.5 (Xhigh, Default Fallback) | 1760 | AA-Briefcase v1.1 Elo | [原表](https://artificialanalysis.ai/evaluations/aa-briefcase) · 2026-11-07 |

> Claude Sonnet 5.5 (Max, Default Fallback)：{"confidence_interval_95": "-11 / +12"}

> Claude Opus 5.5 (Max, Default Fallback)：{"confidence_interval_95": "-11 / +12"}

> Claude Opus 5.5 (Xhigh, Default Fallback)：{"confidence_interval_95": "-10 / +11"}

> 字段状态：待核实

> 来源表Release Date为模型发行月，不是评测日期；整体更新时间待核实。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 覆盖说明

AA为基准创建者；不存在把同机构数据称作另一独立复核。前三为11月7日采集页面，模型发行月不是评测运行时间；10月28日文章历史Elo单独保留。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 公开反馈

https://github.com/ArtificialAnalysis/Stirrup/issues

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 官方社交

- https://x.com/ArtificialAnlys
- https://www.linkedin.com/company/artificial-analysis/

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 隐私说明/政策

https://artificialanalysis.ai/privacy-policy

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 检查官方评测页、首发文章和方法页及PDF检索，未定位原始论文PDF。网页方法材料不冒充原始PDF；drive_pdf维持缺失。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-briefcase)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

### PDF SHA-256

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### PDF字节数

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

### 文件夹

```json
{
  "id": "1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
[
  {
    "type": "官方方法页HTML归档（非论文PDF）"
    "id": "1VG1TTaPBvlUifj4SjEE83SCeWJeFjjiM"
    "webViewLink": "
    "source_url": "https://artificialanalysis.ai/evaluations/aa-briefcase"
    "accessed": "2026-11-07"
    "sha256": "ba0e7c1f5b6e70c09d9a33f7ba0cf670630625c0edfde2d374b56fdeef8c0033"
    "bytes": 1813260
  }
  {
    "type": "中文介绍Google Doc"
    "id": "1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I"
    "webViewLink": "
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）；[来源2](

### 论文副本

待核实

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": "（UTC+8）"
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": "（UTC+8）"
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": " (UTC+8)"
    最近复核
  }
]
```

[来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)（访问2026-11-07）
