# MLCR / MLCR-AA

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: A；未知信息保留待核实。

## 基本信息

### 简称

MLCR / MLCR-AA

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 全称

Medical Long Context Reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 版本

MLCR v1.1（2026-08-31）；MLCR-AA是独立实现口径

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 发布日期

2026-06-18首发；2026-08-31 v1.1

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### section

生物与医学

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### subfields

```json
[
  "长上下文",
  "保险记录"
]
```

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 许可证

HF数据卡license: other；精确条款待核实，不能当作MIT或Apache。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 论文链接

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 官方代码

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/Wisedocs/mlcr-dataset

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 官网

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 论文标题

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

## 发起与维护

### 发起方

Wisedocs

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### partners

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 作者

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 维护方

Wisedocs维护原始MLCR；Artificial Analysis维护MLCR-AA评测。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

## 设计目标

### 衡量能力

跨长篇、碎片化医疗记录重建时间线、因果、治疗模式及保险理赔相关性。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### 设计动机

不仅定位单条事实，还需专家级临床综合与多部分推理。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

## 构建方式

### question_sources

合成医疗记录，模型上下文可按固定seed确定性插入无关filler；病例、提示、模型、模态、filler比例和thinking levels组成实验矩阵。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### author_background

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### review_process

专家标注ground truth，三裁判对照原记录与参考答案。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### quality_control

空答案直接失败；多数裁判确认完整且无记录矛盾才通过。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### decontamination

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

## 数据形式

### 题量与规模

公开数据：10病例目录（Tier1–3），131空白表格OCR文件和131生成表格OCR文件；AA私有60题×3重复，不能相加成题量。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### 题型

单事实检索、跨文档综合、临床因果和多部分问题。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### modalities

```json
[
  "文本",
  "OCR记录"
]
```

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### difficulty

原MLCR六层；AA只取expert和compound两层。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/Wisedocs/mlcr-dataset)（访问 2026-11-07）

### 公开与隐藏划分

公开下载仅text，含questions/cases_summaries/filler_files，不含图片；仓库支持图片模式不等于已发布图片。AA独立私有最难两层60题另计。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

## 评测方法

### 指标

主指标pass rate / pass@1；另列accuracy与completeness，不可混用。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 评分方式

三LLM裁判多数票：每部分完整且无任何与原记录矛盾的claim。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 提示与运行设置

每题3重复；默认每部分一段并引用原记录；AA裁判Claude Opus5.5、GPT-6.1 Sol、Grok4.7，medium。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方评测实现

Wisedocs官方evaluation harness仓库；AA私有集不能由公开数据直接完全复现。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 可比性警告

公开harness有≤参考答案5倍字符的conciseness gate及旧judge面板；AA当前私有协议和judge已不同。两者结果、模态和filler比例不可混比。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "MLCR v1.1；AA私有实现另计",
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/evaluations/mlcr-aa",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "AA当前独立评测27模型，属于持续医疗长记录测评，不在Intelligence Index。"
    },
    {
      "url": "https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md",
      "date": "2026-08-31",
      "note": "Wisedocs README发布v1.1，改进judge校准并与AA共同发布评测。"
    }
  ]
}
```

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）；[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning/blob/main/README.md)（访问 2026-11-07）

### paper_revision_history

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### 为什么近期热门

上列2026年后半年发布、当前榜单或独立实跑构成活跃证据；不把热度当成质量背书。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### official_url

https://github.com/Wisedocs-AI/medical-long-context-reasoning

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### third_party_url

https://artificialanalysis.ai/evaluations/mlcr-aa

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "GPT-6 Astra (Max)",
    "score": "41.7%",
    "metric": "MLCR-AA pass rate",
    "source_url": "https://artificialanalysis.ai/evaluations/mlcr-aa",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "AA当前页面文字报告；前两显示分相同，不表示显著优劣；不是accuracy榜。"
  },
  {
    "rank": 2,
    "model": "Claude Sonnet 5.5 (Max, Default Fallback)",
    "score": "41.7%",
    "metric": "MLCR-AA pass rate",
    "source_url": "https://artificialanalysis.ai/evaluations/mlcr-aa",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "AA当前页面文字报告；前两显示分相同，不表示显著优劣；不是accuracy榜。"
  },
  {
    "rank": 3,
    "model": "GPT-6.1 Sol (Max)",
    "score": "38.3%",
    "metric": "MLCR-AA pass rate",
    "source_url": "https://artificialanalysis.ai/evaluations/mlcr-aa",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "AA当前页面文字报告；前两显示分相同，不表示显著优劣；不是accuracy榜。"
  }
]
```

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

### 时效与可比性

AA当前页面文字报告；前两显示分相同，不表示显著优劣；不是accuracy榜。

[来源](https://artificialanalysis.ai/evaluations/mlcr-aa)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### github_issues

https://github.com/Wisedocs-AI/medical-long-context-reasoning/issues

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）

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

[来源](https://github.com/Wisedocs-AI/medical-long-context-reasoning)（访问 2026-11-07）
