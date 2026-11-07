# Furniture Assembly Benchmark

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: A；未知信息保留待核实。

## 基本信息

### 简称

Furniture Assembly Benchmark

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 全称

Furniture Assembly Benchmark

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 版本

运行CSV中见1.0.0与1.0.1；本轮榜单限1.0.0分轨

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 发布日期

2026-09（官方BibTeX月；精确日待核实）

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### section

多模态

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### subfields

```json
[
  "空间推理"
]
```

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 许可证

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 论文链接

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 官方代码

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 数据集

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 官网

https://epoch.ai/benchmarks/furniture-assembly

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 论文标题

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 发起与维护

### 发起方

Epoch AI

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### partners

研究独立于IKEA，不据使用产品及说明书推断合作。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 作者

Epoch AI

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 维护方

Epoch AI

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 设计目标

### 衡量能力

将真实装配照片与技术图示连接，识别错误并定位产生错误的步骤。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 设计动机

衡量物理构建的空间及多步推理，而非仅抽象视觉题。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 构建方式

### question_sources

研究人员购买三件IKEA家具并拍摄装配过程，故意制造可见错误后可继续安装。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### author_background

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### review_process

有错样本先核对步骤，再由GPT-5.6 Sol宽松评阅错误描述。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### quality_control

正确构建正确识别直接通过；有错样本必须正确定位并大致描述。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### decontamination

官方不分发或出售底层受版权保护图片和说明书；不由此推断完整数据开放。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 数据形式

### 题量与规模

60张照片：Ställ鞋柜14、Tonstad床架25、Gullaberg斗柜21。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 题型

判断安装正确性；识别错误步骤与原因；正确时指出下一步。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### modalities

```json
[
  "照片",
  "PDF装配手册",
  "文本"
]
```

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### languages

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### difficulty

三产品按复杂度选择，错误可发生于较早而非最后一步。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 公开与隐藏划分

未公开：官方声明不分发/出售底层受版权保护材料；其他划分待核实。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 评测方法

### 指标

60照片准确率，误差条为±标准误。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 评分方式

错题先匹配步骤，再LLM判描述；人类基线仅判步骤，任务略容易。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 提示与运行设置

提供产品名、当前完成步骤、照片、PDF手册、zoom与Python；80步budget；最高支持reasoning effort。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 官方评测实现

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 可比性警告

不能把人类84%最佳组合称单人全卷成绩；运行CSV有不同任务版本，须分轨。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "CSV最新运行见1.0.1",
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/data/benchmarks.csv",
      "date": "2026-11-06",
      "note": "Kimi K3.1 Pro，运行2026-11-06 20:34:34 KST，id UNKjzcpUBaxGsrr7zZZZWC；持续实跑证据。"
    }
  ]
}
```

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### paper_revision_history

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 为什么近期热门

上列2026年后半年发布、当前榜单或独立实跑构成活跃证据；不把热度当成质量背书。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### official_url

https://epoch.ai/benchmarks/furniture-assembly

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### third_party_url

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "Claude Opus 5.5 (max)",
    "score": 0.8333333333333334,
    "metric": "accuracy (0–1), task version 1.0.0",
    "stderr": "0.047040472216649226",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "source_date": "2026-09-23T01:51:00+09:00 KST",
    "run_id": "4QrkRM7KEDCQvg4wvfhz7N",
    "collected_at": "2026-11-07 KST"
  },
  {
    "rank": 2,
    "model": "GPT-6.1 Sol (max)",
    "score": 0.8,
    "metric": "accuracy (0–1), task version 1.0.0",
    "stderr": "0.04928872620664329",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "source_date": "2026-09-30T03:29:32+09:00 KST",
    "run_id": "R4vjsSfDrDo6ECQWGTUdWe",
    "collected_at": "2026-11-07 KST"
  },
  {
    "rank": 3,
    "model": "GPT-6 Astra (max)",
    "score": 0.8,
    "metric": "accuracy (0–1), task version 1.0.0",
    "stderr": "0.04928872620664329",
    "source_url": "https://epoch.ai/data/benchmarks.csv",
    "source_date": "2026-09-11T05:22:39+09:00 KST",
    "run_id": "BSzNeBCFhFUnZswSqHtAed",
    "collected_at": "2026-11-07 KST"
  }
]
```

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 时效与可比性

官方CSV按1.0.0轨运行均分排序的前三记录；未合并1.0.1，也未将同模型不同配置去重。来源日期为各自运行时间，非整榜更新时间。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）

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

[来源](https://epoch.ai/benchmarks/furniture-assembly)（访问 2026-11-07）
