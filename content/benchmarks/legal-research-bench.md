# Legal Research Bench

> Benchmark Constitution｜逐源深度核查：2026-11-08。采集日期不代表实验日期；待核实不等于未公开。

Legal Research Bench要求agent完成美国法开放式检索，并同时满足全部必需rubric及来源核验。官网208题test榜与论文413题历史实验分轨；代码MIT不意味着Proprietary完整题集开放，也不代表达到可无人监督执业的可靠性。

导读依据：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）；[3](https://github.com/vals-ai/legal-research-bench)（访问 2026-11-08）。

## 基本信息

### 简称

Legal Research Bench

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 全称

Legal Research Bench

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 基准版本

LRB：413题语料；官方当前网页只在208题test评测。公开5题、许可验证200题、隐藏test208题分开。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）。

### 发布日期

2026-10-01（arXiv初稿日期，不冒充数据集单独首发日）

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）。

### 主板块

Agent

> Benchmark Atlas 编辑归档，不作为官方分类。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 领域

```json
[
  "法律"
  "搜索"
]
```

> 编辑标签

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 许可与使用范围

```json
{
  "harness": "MIT，Copyright 2026 Vals AI, Inc."
  "dataset": "官网标Proprietary；5题公开样例、其余访问另需批准/许可，不能以代码MIT推断完整题集开放。"
}
```

来源：[1](https://github.com/vals-ai/legal-research-bench/blob/main/LICENSE)（访问 2026-11-08）；[2](https://github.com/vals-ai/legal-research-bench/blob/main/README.md)（访问 2026-11-08）；[3](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）。

### 论文入口

https://arxiv.org/abs/2610.00609

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 官方代码

https://github.com/vals-ai/legal-research-bench

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 数据入口

https://github.com/vals-ai/legal-research-bench

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 官方主页

https://www.vals.ai/benchmarks/legal_research

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 论文标题

Legal Research Bench: Measuring End-to-End Reliability in Long-Horizon Legal Research Agents

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 发起与维护

### 发起方

Vals AI

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 合作与作者单位

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 作者

```json
[
  "Katrina Drozdov"
  "Oliver Chen"
  "Langston Nashold"
  "Rayan Krishnan"
]
```

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 维护方

Vals AI

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 资助与资源支持

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 设计目标

### 测量能力

跨美国联邦及州法，检索法律、判例，判断有效性并综合成有权威支持的法律研究答案。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 与既有基准的差异

不能把部分正确或仅能检索当作法律工作可靠；遗漏一个必要要点也可能造成错误。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 构建方式

### 题目来源

执业律师原创的真实工作型研究问题，涉及8类法律业务。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 出题者背景

15位执业律师，平均15年经验，承担出题与复核。

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-07）。

### 审核流程

每题至少一位额外执业律师独立复核；15位律师平均15年经验，约4律师工时/题；gold材料除轻度copyediting外不借助AI生成。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

### 质量控制

GPT-5.4裁判对律师多数票rubric标签一致率87.4%。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 去污染与泄漏控制

测试集保持私有防止过拟合；公开示例与可许可验证集分开。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 数据形式

### 规模与统计口径

413题：公开5、可许可验证200、私有测试208。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 题型

开放法律研究，含成文法解释、判例规则应用、监管框架、跨来源调和和时间有效性。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 模态

```json
[
  "文本"
  "检索网页与法律材料"
]
```

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 语言

美国法，英语。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 难度

多标签难度属性：Reconciliation 116题、Temporal Validity 66题（论文全413题口径）；两者可重叠，不应当互斥难度分层。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

### 公开与隐藏划分

官方当前网页成绩仅基于208题Test；论文全413题结果不是同一口径。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 评测方法

### 指标

All-Pass为主；另报rubric加权部分分。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 评分规则

所有必需rubric项及来源核验通过才算正确；GPT-5.4裁判。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 提示、采样与工具设置

共用harness，3小时/题；case-law搜索、web搜索、retrieve_information、parse_html_page与submit_final_result。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 官方脚本

https://github.com/vals-ai/legal-research-bench

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 可比性警告

官网208题实时榜与论文413题历史结果分轨；不能以法律测试分数认证无人监督法律执业。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 最新情况

### 核查时间

2026-11-08

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）。

### 最新数据状态

```json
{
  "version": "413题LRB原论文语料；当前官网208题test轨"
  "official_page_updated": "2026-11-05"
  "public": 5
  "validation": 200
  "test": 208
}
```

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）。

### 论文修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-10-01"
    "timezone": ""
  }
]
```

> arXiv原始UTC时间已转换为；不等于数据集版本变更。

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）。

### 饱和度与证据边界

当前严格All-Pass第一55.77%，未达全题可靠。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 污染与已知问题

时间锚定、裁判与检索工具依赖；流畅回答不等于法律可靠性。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 相关与衍生基准

相关但不同：LegalBench、LegalBench-RAG测静态法律推理/检索；Harvey Legal Agent Benchmark使用限定matter文档，LRB开放检索美国法律权威资料。不是这些基准的别名或新版本。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

## 榜单快照

### 采集日期

2026-11-08 （采集日，不是运行或榜单更新日）

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

### 官方结果入口

https://www.vals.ai/benchmarks/legal_research

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 独立评测入口

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 结构化结果

```json
[
  {
    "rank": 1
    "model": "Gemini 4 Carbon"
    "score": 55.77
    "metric": "All-Pass (%)，208题Test"
    "source_url": "https://www.vals.ai/benchmarks/legal_research"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-08 "
    "result_type": "官方榜单快照"
    "track": "官方当前208题test / All-Pass"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "Muse Spark 1.3 Max"
    "score": 55.29
    "metric": "All-Pass (%)，208题Test"
    "source_url": "https://www.vals.ai/benchmarks/legal_research"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-08 "
    "result_type": "官方榜单快照"
    "track": "官方当前208题test / All-Pass"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "Claude Opus 5"
    "score": 55.29
    "metric": "All-Pass (%)，208题Test"
    "source_url": "https://www.vals.ai/benchmarks/legal_research"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-08 "
    "result_type": "官方榜单快照"
    "track": "官方当前208题test / All-Pass"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "Claude Opus 4.8"
    "score": "42.9"
    "metric": "All-Pass (%)"
    "track": "原论文413题全量 / 历史作者实验"
    "source_url": "https://arxiv.org/pdf/2610.00609"
    "result_type": "论文摘要历史结果，非208题当前官网榜"
    "snapshot_date": "2026-11-08 "
  }
]
```

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

### 覆盖与局限

官网明确Updated 11/5/2026；它是页面更新日，不必然是每模型运行日。保留208题test当前榜，并另列论文413题历史42.9%；两者不能按同一排名比较。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

## 联系方式

### 官方公开邮箱

contact@vals.ai（访问许可）；katrina@vals.ai（论文通讯作者）

来源：[1](https://arxiv.org/abs/2610.00609)（访问 2026-11-07）。

### 仓库反馈

https://github.com/vals-ai/legal-research-bench/issues

> 公开仓库问题入口；访问许可仍应联系Vals。

来源：[1](https://github.com/vals-ai/legal-research-bench/blob/main/README.md)（访问 2026-11-08）。

### 官方社区

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 隐私与联系边界

论文声明题目为原创假设事实场景，无真实客户信息、个人可识别信息或特权/机密材料；参与律师获报酬并同意使用。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

## 原始文件

### 论文PDF

https://arxiv.org/pdf/2610.00609

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### PDF SHA-256

a7f99b089bb1ff218471ecab84557f79af3dbb607b1eb6fbb30e926133658876

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

### PDF字节数

```json
467211
```

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2610.00609)（访问 2026-11-08）。

### 已有文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

### 其他官方文档

```json
[
  {
    "type": "官方数据卡/方法入口"
    "url": "https://github.com/vals-ai/legal-research-bench"
  }
  {
    "type": "公开代码文档"
    "url": "https://github.com/vals-ai/legal-research-bench"
  }
]
```

来源：[1](https://github.com/vals-ai/legal-research-bench)（访问 2026-11-08）；[2](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）。

### 已有 PDF归档

待核实

> 本组仅建立本地研究条目，未上传。

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）。

## 变更记录

### 历次核查

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]
```

来源：[1](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-07）；[2](https://arxiv.org/abs/2610.00609)（访问 2026-11-08）；[3](https://www.vals.ai/benchmarks/legal_research)（访问 2026-11-08）。

