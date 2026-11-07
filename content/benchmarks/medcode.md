# MedCode

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: B；未知信息保留待核实。

## 基本信息

### 简称

MedCode

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 全称

MedCode

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 版本

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 发布日期

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### section

生物与医学

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### subfields

```json
[
  "医疗编码"
]
```

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 许可证

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 论文链接

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 官方代码

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 数据集

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 官网

https://www.vals.ai/benchmarks/medcode

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 论文标题

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 发起与维护

### 发起方

Vals AI

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### partners

Protege

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 作者

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 维护方

Vals AI

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 设计目标

### 衡量能力

从完整住院记录输出ICD-10-CM主要及次要诊断编码。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 设计动机

模拟真实医疗计费文档约束，而非只测临床选择题。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 构建方式

### question_sources

2755例去标识患者记录，出院总结、进展记录与会诊记录。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### author_background

每例两名certified professional coders独立标注。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### review_process

可用Codify查验但禁用AI；分歧协作解决。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### quality_control

保留所需人口与区域信息，ZIP前三位映射辖区；O类分娩编码因混淆不可靠而排除。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### decontamination

去标识不等于防训练污染；完整污染检查待核实。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 数据形式

### 题量与规模

2755例去标识住院记录。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 题型

生成CMS ICD-10-CM主要/次要诊断编码。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### modalities

```json
[
  "文本医疗记录"
]
```

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### difficulty

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 公开与隐藏划分

正式训练/验证/测试划分与公开数据许可待核实。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 评测方法

### 指标

官方主表Accuracy(%)；另报主要/次要诊断、ICD章节和编码精度分项。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 评分方式

按参考诊断编码rubric评测；精确匹配/部分分数聚合公式待核实。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 提示与运行设置

temperature=1，最多30000 tokens。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 官方评测实现

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 可比性警告

医疗编码成绩不代表诊断能力或临床可部署性；章节、码粒度和主要/次要诊断分项不能混比。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "MedCode；编号待核实",
  "heat_confidence": "B",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/medcode",
      "date": "2026-10-29",
      "note": "Vals当前107模型榜；热度主要来自单一评测机构，不称广泛采纳。"
    }
  ]
}
```

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### paper_revision_history

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 为什么近期热门

本轮主要来自单一机构的当前评测或厂商自评，不宣称行业广泛采用。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### official_url

https://www.vals.ai/benchmarks/medcode

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### third_party_url

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "Claude Opus 5",
    "score": "63.57%",
    "metric": "Accuracy",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "source_date": "2026-10-29",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 2,
    "model": "Gemini 3.1 Pro Preview (02/26)",
    "score": "59.06%",
    "metric": "Accuracy",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "source_date": "2026-10-29",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 3,
    "model": "Gemini 4 Argon",
    "score": "58.80%",
    "metric": "Accuracy",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "source_date": "2026-10-29",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### 时效与可比性

官方页面结果；采集日期不等于榜单更新时间。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）

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

[来源](https://www.vals.ai/benchmarks/medcode)（访问 2026-11-07）
