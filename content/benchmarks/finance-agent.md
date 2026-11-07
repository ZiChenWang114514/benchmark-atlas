# Finance Agent

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: B；未知信息保留待核实。

## 基本信息

### 简称

Finance Agent

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### 全称

Finance Agent Benchmark

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### 版本

v2.1

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 发布日期

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### section

Agent

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### subfields

```json
[
  "金融"
]
```

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 许可证

原始论文：公开v1数据CC BY4.0、代码MIT；v2.1公开样本及私有数据许可仍待核实。

[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### 论文链接

https://arxiv.org/abs/2508.00828

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### 官方代码

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 数据集

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 官网

https://www.vals.ai/benchmarks/fabv2-1

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 论文标题

Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

## 发起与维护

### 发起方

Vals AI

[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### partners

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 作者

原始论文：Antoine Bigeard、Rayan Krishnan、Shirley Wu、Langston Nashold；不把旧论文作者名单当v2.1完整人员名单。

[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### 维护方

Vals AI

[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 设计目标

### 衡量能力

初级金融分析师级公开公司文件检索、跨源综合、精确计算与建模。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 设计动机

需实际工具调用和隐含金融惯例，不只静态单文档问答。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 构建方式

### question_sources

公开公司申报与资料；领域专家编写，强调确定答案、跨源综合、行业惯例及脚注精度。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### author_background

问题目标为投行2–3年分析师水平；金融行业专家参与。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### review_process

专家复审问题与rubric，v2.1修正/删除问题并更新检查。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### quality_control

dealbreaker关键事实门控，任一关键项失败整题零分。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### decontamination

测试集持续私有以防过拟合；公开/许可验证样本不进入本榜结果。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 数据形式

### 题量与规模

公开27、许可Private Validation450、私有Test449。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 题型

九类分析师任务，涵盖comparables、precedents、earnings、disclosure、modeling等。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### modalities

```json
[
  "文本",
  "财报",
  "结构化工具返回"
]
```

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### difficulty

跨多文档、更严格数字容差和需要隐含洞察的分析。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 公开与隐藏划分

公开27题；验证450题可许可获取；Test449题明确保持私有，仅此测试集用于榜单。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 评测方法

### 指标

主指标dealbreaker-gated weighted Partial Credit；次指标All-Pass。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 评分方式

关键dealbreaker失败整题零分，否则严重程度加权检查得分；三模型jury评阅。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 提示与运行设置

每任务2小时；六工具edgar_search/web_search/parse_html_page/retrieve_information/calculator/price_history。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 官方评测实现

官方说明公开集与harness位于Finance Agent v2 GitHub仓库，具体仓库URL本轮待核实。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 可比性警告

v2.1与v2不可比较；旧论文537题、50/150/337划分及平衡准确率不代表v2.1。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "v2.1",
  "heat_confidence": "B",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/fabv2-1",
      "date": "2026-11-05",
      "note": "Vals当前37模型榜；热度主要来自单一机构，不称行业广泛采用。"
    }
  ]
}
```

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### paper_revision_history

v2.1更新题目/rubric、替换jury为GPT-6.1 Sol/Gemini3.8 Flash/Claude Sonnet5.5，hedged多候选答案按失败处理。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 为什么近期热门

本轮主要来自单一机构的当前评测或厂商自评，不宣称行业广泛采用。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### official_url

https://www.vals.ai/benchmarks/fabv2-1

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### third_party_url

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "Claude Opus 5.5",
    "score": "67.85%",
    "metric": "v2.1 Partial Credit（表标Accuracy）",
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 2,
    "model": "Gemini 4 Argon",
    "score": "67.66%",
    "metric": "v2.1 Partial Credit（表标Accuracy）",
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 3,
    "model": "Wonder Full",
    "score": "67.58%",
    "metric": "v2.1 Partial Credit（表标Accuracy）",
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 时效与可比性

官方页面结果；采集日期不等于榜单更新时间。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

```json
[
  "contact@vals.ai"
]
```

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2508.00828

> 原始v1论文，不是v2.1的完整新协议。

[来源](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### Drive PDF

待核实

> 本组未上传Drive。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "按官方材料新建中文条目；区分热度、质量和不同版本评分。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）
