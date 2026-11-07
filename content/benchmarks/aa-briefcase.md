# AA-Briefcase

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

> 尚未找到独立论文PDF；已保留官方方法页HTML原件，不用示例文件或自行导出的页面冒充原始论文。

## 基本信息

### 简称
AA-Briefcase [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 全称
AA-Briefcase [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
v1.1 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 论文版本
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 发布日期
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 主板块
Agent [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "职业知识工作与多交付物"
]
```
 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 许可证
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 论文
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 已核实官方方法页与发布文章；未找到独立原始论文PDF，不能把示例交付物PDF当论文。

### 官方代码
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 数据地址
https://huggingface.co/datasets/ArtificialAnalysis/AA-Briefcase-Lite [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 官方入口
https://artificialanalysis.ai/evaluations/aa-briefcase [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 论文标题
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 官方介绍页是方法/发布文章，独立论文标题尚待核实。

## 发起与维护

### 机构与发起方
Artificial Analysis [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 合作方
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者
Artificial Analysis 团队（方法页署名口径） [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 当前维护方
Artificial Analysis [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 资助
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
数据科学、产品管理、公司战略等专业知识工作的分析、格式化呈现和可用交付物。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 设计背景
只评短答案忽略真实职业流程中的文件分析、跨材料整合和电子表格/演示/备忘录品质。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

## 构建方式

### 题目来源
四个跨数周的专业场景、数千输入文件；每项任务独立运行在预设上下文，不沿用该模型上一次自己的交付物。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 出题者背景
由Artificial Analysis构建知识工作评测；具体专家招募背景待核实。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 审核流程
为交付物设计明确rubric，再结合分析质量与呈现质量的成对比较。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 质量控制
区分客观要求核验与主观质量比较；场景共享背景不意味着模型错误自动连续传递。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 去污染
正式四场景评分材料保留私有；公开第五Lite示例只供体验，不纳入正式榜。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

## 数据形式

### 题量与规模
4个正式多周场景，共91任务、数千输入文件；公开Lite为额外示例场景。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 题型
产出电子表格、演示文稿、备忘录等多种文件交付物。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 模态

```json
[
  "文本",
  "数据文件",
  "表格",
  "演示文稿/视觉呈现"
]
```
 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 语言
英语专业工作任务；文件格式与任务相依。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 难度
多周情境分解为独立任务；不是让模型真实持续运行数周。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 公开与隐藏划分
正式评分材料私有；AA-Briefcase-Lite示例公开，不可将其结果冒充v1.1正式榜。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

## 评测方法

### 指标
复合Elo；另列binary rubric通过率、Analytical Quality与Presentation成对比较。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 评分
rubric结果转换为合成对局并与两类质量对局合成Elo；Elo不是百分正确率。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 提示与运行设置
任务独立在AA运行环境执行；必须记录模型effort、Default Fallback等策略，不把不同配置合并。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 官方评测脚本
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 可比性警示
Elo依对手池和评分协议变化；Presentation、Analytical Quality子指标和headline不可互换。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "v1.1",
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
      "date": "2026-10-28",
      "note": "Artificial Analysis 2026-10-28文章实际报告 AA-Briefcase Elo以及Presentation、Analytical Quality等子维度结果；子维度不另计。"
    }
  ]
}
```
 [来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 饱和情况
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
主观成对判断和复合Elo受裁判、对手池与展示质量影响；正式材料私有降低泄漏但限制完整复现。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 衍生与版本关系
AA-Briefcase-Lite是公开示例，不另计正式benchmark；分析/呈现分项也不拆分。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 官方榜单
https://artificialanalysis.ai/evaluations/aa-briefcase [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 独立评测覆盖
https://artificialanalysis.ai/evaluations/aa-briefcase [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

### 核验结果

```json
[
  {
    "model": "Claude Sonnet 5.5 (Max, Default Fallback)",
    "score": 1813,
    "metric": "Elo",
    "benchmark_version": "v1.1",
    "result_type": "AA官方当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST",
    "ci": "-11 / +12",
    "model_release": "2026-09"
  },
  {
    "model": "Claude Opus 5.5 (Max, Default Fallback)",
    "score": 1800,
    "metric": "Elo",
    "benchmark_version": "v1.1",
    "result_type": "AA官方当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST",
    "ci": "-11 / +12",
    "model_release": "2026-09"
  },
  {
    "model": "Claude Opus 5.5 (Xhigh, Default Fallback)",
    "score": 1760,
    "metric": "Elo",
    "benchmark_version": "v1.1",
    "result_type": "AA官方当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST",
    "ci": "-10 / +11",
    "model_release": "2026-09"
  },
  {
    "model": "Gemini 4 Carbon (High)",
    "score": 1609,
    "metric": "Elo",
    "benchmark_version": "AA-Briefcase",
    "result_type": "AA历史文章",
    "source_date": "2026-10-28",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase) [来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)

### 覆盖与时效说明
AA为基准创建者；不存在把同机构数据称作另一独立复核。前三为11月7日采集页面，模型发行月不是评测运行时间；10月28日文章历史Elo单独保留。 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase) [来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)

## 联系方式

### 公开工作邮箱
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方社交渠道
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 原始PDF SHA-256
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 原始PDF字节数
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### Drive资料文件夹

```json
{
  "id": "1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv",
  "webViewLink": "https://drive.google.com/drive/folders/1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv"
}
```
 [来源3](https://drive.google.com/drive/folders/1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv)

### 其他文档

```json
[
  {
    "type": "官方方法页HTML归档（非论文PDF）",
    "id": "1VG1TTaPBvlUifj4SjEE83SCeWJeFjjiM",
    "webViewLink": "https://drive.google.com/file/d/1VG1TTaPBvlUifj4SjEE83SCeWJeFjjiM/view?usp=drivesdk",
    "source_url": "https://artificialanalysis.ai/evaluations/aa-briefcase",
    "accessed": "2026-11-07",
    "sha256": "ba0e7c1f5b6e70c09d9a33f7ba0cf670630625c0edfde2d374b56fdeef8c0033",
    "bytes": 1813260
  },
  {
    "type": "中文介绍Google Doc",
    "id": "1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I",
    "webViewLink": "https://docs.google.com/document/d/1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I/edit?usp=drivesdk"
  }
]
```
 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase) [来源4](https://docs.google.com/document/d/1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件
待核实 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

> 官方方法页已核实，未找到独立原始论文 PDF；不伪造论文附件。

## 变更记录


```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  }
]
```
 [来源1](https://artificialanalysis.ai/evaluations/aa-briefcase)

## 来源

1. https://artificialanalysis.ai/evaluations/aa-briefcase — 采集：2026-11-07 KST。
2. https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 — 采集：2026-11-07 KST。
3. https://drive.google.com/drive/folders/1-zM1JOXcqsC2u9BxZ5XDL1Z9yhgil7uv — 采集：2026-11-07 KST。
4. https://docs.google.com/document/d/1rmCVNyX0ks68vDaV7L4tHtaWLwzk-M3bzi_4yLeiE2I/edit?usp=drivesdk — 采集：2026-11-07 KST。
