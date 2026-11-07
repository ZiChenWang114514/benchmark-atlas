# CyberBench

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: B；未知信息保留待核实。

## 基本信息

### 简称

CyberBench

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 全称

CyberBench

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 版本

v1.1

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 发布日期

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### section

安全

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### subfields

```json
[]
```

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 许可证

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 论文链接

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 官方代码

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 数据集

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 官网

https://www.vals.ai/benchmarks/cyber

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 论文标题

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 发起与维护

### 发起方

Vals AI

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### partners

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 作者

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 维护方

Vals AI

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 设计目标

### 衡量能力

端到端复现真实漏洞并修补，同时保持正常程序行为。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 设计动机

聚焦OSS-Fuzz风格原生代码崩溃，而非把CTF成绩等同通用安全能力。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 构建方式

### question_sources

基于ARVO的OSS-Fuzz回归镜像；任务来自CyberGym原始收集窗口之后。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### author_background

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### review_process

差分oracle和hidden holdout对照维护者修复版本。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### quality_control

v1.1重跑离线沙箱，hardened clean-room grader。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### decontamination

新时间窗口与离线沙箱降低泄漏/外部查询影响；不等于已证明完全无污染。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 数据形式

### 题量与规模

PoC 60任务；Patch 56可靠可评分任务。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 题型

PoC生成触发输入；Patch轨编辑源码修复漏洞。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### modalities

```json
[
  "文本",
  "源码",
  "二进制目标",
  "容器"
]
```

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### difficulty

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 公开与隐藏划分

Patch有隐藏holdout输入；完整任务与数据许可范围待核实。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 评测方法

### 指标

Overall、PoC、Patch准确率；榜首表为Overall。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 评分方式

PoC须使漏洞版崩溃而修复版不崩溃；Patch须编译成功、原PoC不再触发且隐藏行为匹配参考。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 提示与运行设置

统一mini-swe-agent；离线任务沙箱。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 官方评测实现

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 可比性警告

v1.1取代v1，结果不直接可比；拒答算失败，fallback会影响结果，需保留其标记。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "v1.1",
  "heat_confidence": "B",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/cyber",
      "date": "2026-11-05",
      "note": "Vals当前48模型榜；热度主要来自单一评测机构，不能称行业广泛采纳。"
    }
  ]
}
```

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### paper_revision_history

v1.1保留60题PoC、56题Patch并更换离线沙箱和hardened grader；v1不可直接比较。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 为什么近期热门

本轮主要来自单一机构的当前评测或厂商自评，不宣称行业广泛采用。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### official_url

https://www.vals.ai/benchmarks/cyber

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### third_party_url

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "Wonder",
    "score": "80.36%",
    "metric": "Overall Accuracy",
    "source_url": "https://www.vals.ai/benchmarks/cyber",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 2,
    "model": "GPT-6 Sol",
    "score": "77.98%",
    "metric": "Overall Accuracy",
    "source_url": "https://www.vals.ai/benchmarks/cyber",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 3,
    "model": "Gemini 4 Argon",
    "score": "77.86%",
    "metric": "Overall Accuracy",
    "source_url": "https://www.vals.ai/benchmarks/cyber",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### 时效与可比性

官方页面结果；采集日期不等于榜单更新时间。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 候选所列ARVO背景论文不冒充CyberBench自身论文。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）

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

[来源](https://www.vals.ai/benchmarks/cyber)（访问 2026-11-07）
