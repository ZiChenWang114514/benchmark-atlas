# DeepSWE

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: A；未知信息保留待核实。

## 基本信息

### 简称

DeepSWE

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 全称

DeepSWE

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 版本

v1.1

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 发布日期

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### section

代码

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### subfields

```json
[]
```

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 许可证

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 论文链接

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 官方代码

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 数据集

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 官网

https://deepswe.datacurve.ai/

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 论文标题

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 发起与维护

### 发起方

Datacurve

[来源](https://epoch.ai/benchmarks/deepswe/review)（访问 2026-11-07）

### partners

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 作者

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 维护方

Datacurve

[来源](https://epoch.ai/benchmarks/deepswe/review)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 设计目标

### 衡量能力

原创、长程真实软件工程任务的完成能力。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 设计动机

避免已有提交或PR改编，并扩大仓库和语言多样性，区分趋于饱和的代码Agent。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 构建方式

### question_sources

从零编写的任务，覆盖91仓库、5种语言。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### author_background

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### review_process

手工编写behavioral verifier；精确审核人员背景待核实。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### quality_control

官方主张验证行为而非实现细节；Epoch独立发现评分假阴性。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### decontamination

官方称原创任务避免预训练见到解法；这是设计主张，不是无污染证明。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 数据形式

### 题量与规模

113任务、91仓库、5种语言。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 题型

跨文件工程功能实现、修复和长期代码维护。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### modalities

```json
[
  "代码",
  "文本",
  "测试环境"
]
```

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### difficulty

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 公开与隐藏划分

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 评测方法

### 指标

Pass@1；附成本、输出token和Agent步数。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 评分方式

手工行为验证器评测提交改动；具体隐藏测试协议需结合独立审查。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 提示与运行设置

官方榜统一mini-swe-agent；模型reasoning effort按配置列出。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 官方评测实现

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 可比性警告

官网rounded 74%±区间不应与厂商74.1%拼成伪精确同榜；Kimi Code与mini-swe-agent分轨。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "v1.1",
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/benchmarks/deepswe/review",
      "date": "2026-09-07",
      "note": "Epoch独立审查为Flawed。"
    },
    {
      "url": "https://openai.com/index/gpt-6-astra/",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "GPT-6 Astra发布表采用。"
    }
  ]
}
```

[来源](https://epoch.ai/benchmarks/deepswe/review)（访问 2026-11-07）；[来源](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### paper_revision_history

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 污染与争议

Epoch在113任务中至少23题（20.3%以上）发现问题，主要是假阴性；其中18例可能因代理改测试与verifier注入测试冲突。评测热度不等于质量认证。

[来源](https://epoch.ai/benchmarks/deepswe/review)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 为什么近期热门

上列2026年后半年发布、当前榜单或独立实跑构成活跃证据；不把热度当成质量背书。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### official_url

https://deepswe.datacurve.ai/

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### third_party_url

https://epoch.ai/benchmarks/deepswe/review

[来源](https://epoch.ai/benchmarks/deepswe/review)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "gpt-6-astra [xhigh]",
    "score": "74% ±3%",
    "metric": "Pass@1",
    "source_url": "https://deepswe.datacurve.ai/",
    "source_date": "2026-09-22",
    "collected_at": "2026-11-07 KST",
    "result_type": "官网显示顺序；三者显示值相同，误差区间重叠，不据此宣称显著优劣。"
  },
  {
    "rank": 2,
    "model": "gemini-3.8-flash [high]",
    "score": "74% ±1%",
    "metric": "Pass@1",
    "source_url": "https://deepswe.datacurve.ai/",
    "source_date": "2026-09-22",
    "collected_at": "2026-11-07 KST",
    "result_type": "官网显示顺序；三者显示值相同，误差区间重叠，不据此宣称显著优劣。"
  },
  {
    "rank": 3,
    "model": "claude-opus-5 [max]",
    "score": "74% ±4%",
    "metric": "Pass@1",
    "source_url": "https://deepswe.datacurve.ai/",
    "source_date": "2026-09-22",
    "collected_at": "2026-11-07 KST",
    "result_type": "官网显示顺序；三者显示值相同，误差区间重叠，不据此宣称显著优劣。"
  }
]
```

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### 时效与可比性

官网显示顺序；三者显示值相同，误差区间重叠，不据此宣称显著优劣。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）

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

[来源](https://deepswe.datacurve.ai/)（访问 2026-11-07）
