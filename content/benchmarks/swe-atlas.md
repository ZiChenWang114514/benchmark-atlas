# SWE Atlas

> Benchmark Constitution · 深度复核 2026-11-08（KST / Asia/Seoul）。研究快照；trending: B；未核实字段保留标记

SWE Atlas针对补bug以外的软件工程工作：代码库运行时理解、测试编写和行为保持重构。284题分成124/90/70三类，评分同时看程序行为与专家rubric；新judge下的v1.1不能和原论文旧judge结果直接做增长对比。完整任务与运行工具已经公开，本档补上其仓库而非继续把它当仅有私有榜单的项目。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-Atlas)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

## 基本信息

### 简称

SWE Atlas

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 全称

SWE Atlas

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 基准版本

v1.1（2026年11月更新）

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 论文版本

v1（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 发布日期

2026-05-09 KST（arXiv v1提交2026-05-09T03:21:44+09:00）；v1.1官网公告2026-11，仅精确到月。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### 主板块

代码

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 领域

```json
[
  "代码"
]
```

> 编辑标签

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 许可与适用范围

Apache-2.0（官方LICENSE）；QnA第三方措辞须保留NOTICE，上游代码各守原许可。

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2605.08366

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 官方代码

https://github.com/scaleapi/SWE-Atlas

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 数据

https://github.com/scaleapi/SWE-Atlas/tree/main/data

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 官方入口

https://labs.scale.com/leaderboard/swe-atlas?tab=overall

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 论文标题

SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 发起与维护

### 发起方

Scale AI

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 合作/参与机构

v1.1致谢Artificial Analysis与Inductive ML的评分措辞及奖励投机反馈贡献。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 作者

```json
[
  "Mohit Raghavendra",
  "Soham Dan",
  "Miguel Romero Calvo",
  "Yannis Yiming He",
  "Johannes Baptist Mols",
  "Gautam Anand",
  "Cole McCollum",
  "Edgar Arakelyan",
  "Vijay Bharadwaj",
  "Andrew Park",
  "Jeff Da",
  "MohammadHossein Rezaei",
  "Bing Liu",
  "Brad Kenstler",
  "Yunzhong He"
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://static.scale.com/uploads/6691558a94899f2f65a87a75/Coding_Agent_Eval%20(5).pdf)（访问 2026-11-08）

### 维护方

Scale Labs

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 资助

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 设计目标

### 衡量能力

代码库理解、测试编写与重构。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 设计背景

补足只关注issue resolution的软件工程评测。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 构建方式

### 题目来源

专业软件工程工作；当前方法页称来自15个生产仓库、6种语言。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 出题者背景

有多年实际软件工程经验的专业工程师编题，另有独立QC团队及三位可信专家审计；附录说明合同报酬符合或超过当地工资要求，不使用无偿志愿劳动。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 审核流程

参考解须通过全部检查；独立QC复核；再由三位专家独立核对指令、验证与rubric，至少两位认为无效、过度规定实现或含糊的rubric被剔除。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 质量控制

v1.1重新运行所有模型，更新裁判、评分条件并限制网络访问。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 污染控制

Test Writing/Refactoring对passing agent补丁与gold补丁作Jaccard与sequence similarity记忆筛查，未见明显逐字复现；这不证明无污染。容器删除并重新初始化git历史，v1.1进一步限制网络。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

## 数据形式

### 题量

284任务：Codebase QnA 124、Test Writing 90、Refactoring 70；论文v1称18仓库，当前v1.1官网称15仓库，同为284题但来源仓库口径存在差异，未强行统一。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### 任务形式

每任务单轮目标提示，agent可在仓库Docker中构建、运行与测试。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 模态

```json
[
  "代码",
  "文本"
]
```

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 语言

Go、Python、TypeScript、C、C++、JavaScript

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 难度

论文Refactoring参考修改35–2,073行，要求多文件协调和行为保持；QnA强调运行时证据，Test Writing必须能在真实实现通过、被替换为stub后失败。

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 公开与隐藏划分

三类完整284任务、reference solution、grader、rubric、judge prompt及digest-pinned公共镜像公开；agent只能见instruction与运行仓库，评分材料由验证阶段使用。

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

v1.1总体index及三类子榜；每trial reward为0/1，跨3次尝试求均值为pass@1。论文Pass 3是三次全部成功，Pass@3是至少一次成功，不可混淆。

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 评分

QnA：全部必需rubric通过；TW：manifest+mutation+必需rubric同时通过；RF：行为保持/回归测试+必需rubric通过。v1.1以GPT-6.1 Sol high作judge，3票多数；拒答/空答/无法评分为0，基础设施错误须重跑而非计0。

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 运行设置

v1.1配置中Claude Code 2.1.293与Codex 0.142.1，effort max，每任务3次；禁WebSearch/WebFetch、网络allowlist只允许模型端点；judge gpt-6.1-sol high，多数票3次。

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 评测工具

Harbor run.sh入口，configs/保存oracle、nop和Anthropic/OpenAI榜单运行配置；data/qa、data/tw、data/rf分别有测试与评分器。

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 可比性

v1.1与v1.0裁判与环境不同，分数不能直接比较。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "v1.1（2026年11月更新）",
  "heat_confidence": "B",
  "why_trending": "主要是单一机构当前展示或厂商持续自评，不代表全行业广泛采纳。",
  "evidence_2026_h2": [
    {
      "url": "https://labs.scale.com/leaderboard/swe-atlas?tab=overall",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "organization": "官方维护方",
      "note": "已打开当前官方方法与榜单；观察日不冒充发布时间。"
    }
  ]
}
```

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1",
    "submitted_at": "2026-05-09T03:21:44+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 饱和与能力边界

当前v1.1总体最高77.40±5.00；不同工作流与harness有差异，尚不是全任务接近满分。原论文43.49等旧judge分数不能与77.40直接解释为同协议增量。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 风险与争议

v1.1回应reward hacking反馈并强化环境，公开上游代码仍有训练污染风险。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 系列与衍生关系

与SWE-bench不同；QnA/Test Writing/Refactoring是此条子榜不单独凑数。

> 编辑去重口径；具体版本差异仍以官方材料为准。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-Atlas)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### 官方入口

https://labs.scale.com/leaderboard/swe-atlas?tab=overall

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 独立来源

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 分来源与协议结果

#### Scale v1.1 / overall

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5.5 | 77.4 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5,"source_month":"2026-11"} |
| 2 | Fable 5.1 | 74.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.3,"source_month":"2026-11"} |
| 3 | Gemini 4 Argon | 70.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.5,"source_month":"2026-11"} |
| 4 | GPT-6 Astra | 69.4 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.6,"source_month":"2026-11"} |
| 5 | Sonnet 5.5 | 67.5 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.7,"source_month":"2026-11"} |
| 6 | GPT-6.1 Sol | 65.9 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.7,"source_month":"2026-11"} |
| 7 | Muse Wonder 1.0 | 64.8 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 8 | Grok 4.7 | 62.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 9 | DeepSeek V4.1 Flash | 62.1 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 10 | Inkling 2 Small | 61.9 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 11 | Kimi K3 | 61 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |
| 12 | Haiku 5.5 | 59.4 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |
| 13 | GPT-6.1 Terra | 57.7 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |
| 14 | Gemini 3.8 Flash | 57.3 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.8,"source_month":"2026-11"} |
| 15 | GPT-6 Luna | 50.8 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":6,"source_month":"2026-11"} |
| 16 | Muse Spark Open | 42.3 | SWE Atlas v1.1 index (%) | {"ci_plus_minus":5.9,"source_month":"2026-11"} |

#### Scale v1.1 / qna

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5.5 | 77.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.5,"source_month":"2026-11"} |
| 2 | Inkling 2 Small | 74.2 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.8,"source_month":"2026-11"} |
| 3 | Fable 5.1 | 73.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.9,"source_month":"2026-11"} |
| 4 | Muse Wonder 1.0 | 73.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.9,"source_month":"2026-11"} |
| 5 | Grok 4.7 | 73.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":7.9,"source_month":"2026-11"} |
| 6 | Sonnet 5.5 | 71.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8,"source_month":"2026-11"} |
| 7 | GPT-6.1 Sol | 71 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.1,"source_month":"2026-11"} |
| 8 | DeepSeek V4.1 Flash | 71 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.1,"source_month":"2026-11"} |
| 9 | GPT-6 Astra | 70.2 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.2,"source_month":"2026-11"} |
| 10 | Gemini 4 Argon | 65.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.5,"source_month":"2026-11"} |
| 11 | Kimi K3 | 65.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.5,"source_month":"2026-11"} |
| 12 | Haiku 5.5 | 62.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.7,"source_month":"2026-11"} |
| 13 | GPT-6.1 Terra | 54 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |
| 14 | GPT-6 Luna | 50.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |
| 15 | Muse Spark Open | 50 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |
| 16 | Gemini 3.8 Flash | 45.2 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.9,"source_month":"2026-11"} |

#### Scale v1.1 / testwriting

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Fable 5.1 | 78.9 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.6,"source_month":"2026-11"} |
| 2 | Opus 5.5 | 77.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.8,"source_month":"2026-11"} |
| 3 | Gemini 4 Argon | 77.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":8.8,"source_month":"2026-11"} |
| 4 | Gemini 3.8 Flash | 71.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.5,"source_month":"2026-11"} |
| 5 | Sonnet 5.5 | 67.8 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.8,"source_month":"2026-11"} |
| 6 | GPT-6 Astra | 66.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.9,"source_month":"2026-11"} |
| 7 | GPT-6.1 Sol | 66.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":9.9,"source_month":"2026-11"} |
| 8 | Grok 4.7 | 64.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 9 | Kimi K3 | 63.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 10 | Haiku 5.5 | 63.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 11 | GPT-6.1 Terra | 63.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 12 | Muse Wonder 1.0 | 61.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.3,"source_month":"2026-11"} |
| 13 | DeepSeek V4.1 Flash | 61.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.3,"source_month":"2026-11"} |
| 14 | Inkling 2 Small | 58.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.4,"source_month":"2026-11"} |
| 15 | GPT-6 Luna | 54.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.5,"source_month":"2026-11"} |
| 16 | Muse Spark Open | 41.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.4,"source_month":"2026-11"} |

#### Scale v1.1 / refactoring

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5.5 | 77.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.1,"source_month":"2026-11"} |
| 2 | GPT-6 Astra | 71.4 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":10.8,"source_month":"2026-11"} |
| 3 | Fable 5.1 | 70 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11,"source_month":"2026-11"} |
| 4 | Gemini 4 Argon | 67.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.3,"source_month":"2026-11"} |
| 5 | Sonnet 5.5 | 62.9 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.6,"source_month":"2026-11"} |
| 6 | GPT-6.1 Sol | 60 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.8,"source_month":"2026-11"} |
| 7 | Muse Wonder 1.0 | 60 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.8,"source_month":"2026-11"} |
| 8 | GPT-6.1 Terra | 55.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.9,"source_month":"2026-11"} |
| 9 | Gemini 3.8 Flash | 55.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.9,"source_month":"2026-11"} |
| 10 | DeepSeek V4.1 Flash | 54.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 11 | Kimi K3 | 54.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 12 | Inkling 2 Small | 53.3 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 13 | Haiku 5.5 | 52.9 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 14 | Grok 4.7 | 48.6 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 15 | GPT-6 Luna | 47.1 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":12,"source_month":"2026-11"} |
| 16 | Muse Spark Open | 35.7 | SWE Atlas v1.1 category score (%) | {"ci_plus_minus":11.5,"source_month":"2026-11"} |

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### 覆盖与时效

从官方页面嵌入的variants逐项提取总体、QnA、Test Writing、Refactoring四轨各16行，共64行，保留原rank及CI。createdAt是条目元数据，不冒充运行或榜单更新日期；官网更新仅精确到2026年11月。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

```json
[
  "mohit.raghavendra@scale.com"
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）

### 官方反馈

https://github.com/scaleapi/SWE-Atlas/issues

[来源1](https://github.com/scaleapi/SWE-Atlas/blob/main/README.md)（访问 2026-11-08）

### 公开社区

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 隐私边界

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2605.08366v1

[来源1](https://arxiv.org/pdf/2605.08366v1)（访问 2026-11-08）

### 本轮PDF SHA-256

af39ccd39558020ce2229788542294d61342d791ef5e01547b78f160bf4dd5a7

> 本次实际下载的PDF字节计算；未上传Drive。

[来源1](https://arxiv.org/pdf/2605.08366v1)（访问 2026-11-08）

### 本轮PDF字节数

```json
2118311
```

[来源1](https://arxiv.org/pdf/2605.08366v1)（访问 2026-11-08）

### Drive文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "本轮已打开一手材料",
    "url": "https://arxiv.org/abs/2605.08366",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://github.com/scaleapi/SWE-Atlas",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://labs.scale.com/leaderboard/swe-atlas?tab=overall",
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-Atlas)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）

### Drive PDF归档

待核实

[来源1](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST)",
    "change": "深度复核论文/官方实现与数据卡；补全可审计字段；按版本、来源与协议重建榜单轨；明确无法核实及相互冲突的统计。未上传Drive。"
  }
]
```

[来源1](https://arxiv.org/abs/2605.08366)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-Atlas)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/swe-atlas?tab=overall)（访问 2026-11-08）
