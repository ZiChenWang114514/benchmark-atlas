# MedCode

> Benchmark Constitution｜2026-11-08 KST（Asia/Seoul）深度复核。访问日期不等于实验运行日期；历史来源日期保持原记录。

MedCode关注住院医疗计费所需的诊断编码，而不是医学常识问答。Vals AI与Protege整理2,755例去标识住院记录，要求模型在出院总结、进展与会诊材料中识别主要和次要诊断并映射CMS ICD-10-CM。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）；[https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works)（访问2026-11-08 KST）

## 基本信息

### 简称

MedCode

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 全称

MedCode

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 版本与作用域

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 论文/报告版本

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 首次公开日期

最迟于2026-02-23已发布（当日官方博客称recently released）；精确首次上线日期待核实。

核验状态：待核实

来源：[https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works)（访问2026-11-08 KST）

### 主板块

生物与医学

说明：编辑主板块归档，不据此限制跨学科覆盖。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 子领域

```json
[
  "医疗编码"
]
```

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 许可与权利边界

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 论文/报告入口

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 官方代码

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 数据入口

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 官方主页

https://www.vals.ai/benchmarks/medcode

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 论文/报告标题

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 发起与维护

### 研究发起团队

Vals AI

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 合作研究机构与顾问

Protege提供经整理的去标识医疗数据；Harvard Medical School的Pranav Rajpurkar提供顾问意见，不据个人顾问身份推断哈佛为法律共同发起机构。

来源：[https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works)（访问2026-11-08 KST）；[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 作者

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 维护方

Vals AI

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 资助方

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 设计目标

### 测量能力

从完整住院记录输出ICD-10-CM主要及次要诊断编码。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 设计动机

模拟真实医疗计费文档约束，而非只测临床选择题。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 构建方式

### 材料来源

2755例去标识患者记录，出院总结、进展记录与会诊记录。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 命题与标注背景

每例两名certified professional coders独立标注。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 审核流程

可用Codify查验但禁用AI；分歧协作解决。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 质量控制

保留所需人口与区域信息，ZIP前三位映射辖区；O类分娩编码因混淆不可靠而排除。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 去污染与留出

官方发布文明确采用patient-level holdouts；Vals通用方法规定专有基准发布成绩只用始终私有的test set，以降低训练泄漏。去标识化是隐私措施而非单独的污染证明，私有留出也不等于证实所有训练无重叠。

来源：[https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works)（访问2026-11-08 KST）；[https://www.vals.ai/methodology](https://www.vals.ai/methodology)（访问2026-11-08 KST）

## 数据形式

### 规模与统计对象

2755例去标识住院记录。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 题型与字段

生成CMS ICD-10-CM主要/次要诊断编码。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 模态

```json
[
  "文本医疗记录"
]
```

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 语言

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 难度与覆盖

覆盖整个住院过程的主要与次要诊断编码；需结合出院总结、进展与会诊记录以及人口/地域信息执行CMS ICD-10-CM编码规则。官方按章节、诊断主次及码精度分析错误，不提供统一易/中/难分档。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 公开/私有与数据划分

官方发布成绩来自私有test set（Vals专有基准通用方法明确保持私有）；该条目具体公共验证集下载地址、train/validation人数及分割比例待核实，不能从通用的most benchmarks有公共验证集推断此条一定公开。

核验状态：待核实

来源：[https://www.vals.ai/methodology](https://www.vals.ai/methodology)（访问2026-11-08 KST）；[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 评测方法

### 指标

官方主表Accuracy(%)；另报主要/次要诊断、ICD章节和编码精度分项。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 评分与聚合

按参考诊断编码rubric评测；精确匹配/部分分数聚合公式待核实。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 提示与推理预算

temperature=1，最多30000 tokens。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 官方实现

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 可比性边界

医疗编码成绩不代表诊断能力或临床可部署性；章节、码粒度和主要/次要诊断分项不能混比。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 最新情况

### 本轮核验时间

2026-11-08 KST / Asia/Seoul

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 当前数据与协议

```json
{
  "version": "MedCode（榜单更新2026-10-29；数据语义版本号待核实）",
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

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 论文修订与延续使用证据

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 饱和判断边界

当前官方最高Accuracy为63.57%；官方分析表明主要诊断优于次要诊断，漏掉参考诊断比主次标签混淆更常见。保留明显提升空间，不将63.57%解释为完整住院记录全部编码正确的比例。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 污染、冲突与复现风险

官方声明患者级留出与专有test私有；缺少逐题开放数据与可复现脚本，第三方无法只凭榜单审计全部重叠与评分。模型名是来源原样标签，不补写API快照。

来源：[https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works)（访问2026-11-08 KST）；[https://www.vals.ai/methodology](https://www.vals.ai/methodology)（访问2026-11-08 KST）；[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 衍生实现

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 榜单快照

### 访问快照日期

2026-11-08 KST / Asia/Seoul（本轮访问；各来源运行/提交日期另列）

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 官方榜单入口

https://www.vals.ai/benchmarks/medcode

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 第三方评测入口

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 分来源、分协议结果

```json
[
  {
    "rank": 1,
    "model": "Claude Opus 5",
    "score": 63.57,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 2,
    "model": "Gemini 3.1 Pro Preview (02/26)",
    "score": 59.06,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 3,
    "model": "Gemini 4 Argon",
    "score": 58.8,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 4,
    "model": "Claude Fable 5",
    "score": 56.07,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 5,
    "model": "Gemini 3 Flash (12/25)",
    "score": 55.92,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 6,
    "model": "Gemini 3.5 Flash",
    "score": 55.83,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 7,
    "model": "Claude Opus 4.7",
    "score": 54.86,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 8,
    "model": "Claude Fable 5.1",
    "score": 53.51,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 9,
    "model": "Gemini 3.7 Flash",
    "score": 53.39,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  },
  {
    "rank": 10,
    "model": "Claude Opus 4.8",
    "score": 53.22,
    "unit": "%",
    "metric": "Accuracy",
    "track": "Vals官方 / MedCode / 2026-10-29页面快照",
    "source_url": "https://www.vals.ai/benchmarks/medcode",
    "accessed": "2026-11-08",
    "source_date": "2026-10-29",
    "result_type": "基准维护方统一评测；非厂商自报",
    "settings": "temperature1；最多30k输出tokens"
  }
]
```

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 快照覆盖说明

本轮逐项重读官方榜前10，页面自写Updated 2026-10-29；访问2026-11-08 KST。模型行数不是题数，最新访问也不等于当日重跑。该任务由Vals维护，Vals榜为一级官方来源而非另一独立采纳机构。

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 联系方式

### 官方公开联系邮箱

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 项目反馈入口

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 公开社交渠道

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 联系信息原则

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 原始文件

### 原始论文/技术报告PDF

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 本轮PDF SHA-256

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### PDF原始字节数

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### Drive资料夹

待核实

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

### 其他官方资料

```json
[
  {
    "title": "Measuring Healthcare AI Where It Actually Works",
    "url": "https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works",
    "source_date": "2026-02-23",
    "byline": "Rayan Krishnan"
  },
  {
    "title": "Vals AI Evaluation Methodology",
    "url": "https://www.vals.ai/methodology"
  }
]
```

来源：[https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works)（访问2026-11-08 KST）；[https://www.vals.ai/methodology](https://www.vals.ai/methodology)（访问2026-11-08 KST）

### Drive已存PDF

待核实

说明：本组仅本地研究，未上传Drive。

核验状态：待核实

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）

## 变更记录

### 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "按官方材料新建中文条目；区分热度、质量和不同版本评分。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul",
    "change": "补2026-02-23发布证据、患者级留出、私有test边界和顾问信息；官方前10复核。"
  }
]
```

来源：[https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode)（访问2026-11-08 KST）
