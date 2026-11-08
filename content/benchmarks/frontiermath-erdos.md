# FrontierMath Erdős

> Benchmark Constitution｜深度核验：2026-11-07。访问日沿固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

它测的是在统一预算内解决未解猜想并给出Lean证明，不是已知答案的数学竞赛。公开已解问题登记包含标准评测、额外尝试及外部工作，不能拿登记总数替代模型得分。

最近复核

## 基本信息

**简称**：FrontierMath Erdős

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**全称**：FrontierMath Erdős

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**基准版本**：68猜想固定题集（2026年8月构建）

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**论文版本**：arXiv v1（2026-09-06）

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**发布日期**：2026-09-06 19:32:55 （arXiv首版；题集于2026年8月构建）

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**主板块**：数学

核验说明：Benchmark Constitution 编辑归档，不作为官方分类。

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**领域标签**：数学

核验说明：编辑标签

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**许可证与授权边界**：仓库主体MIT；其中Formal Conjectures衍生的题目文件另遵Apache-2.0及第三方声明，不能把所有内容笼统标为MIT。

来源：[1](https://github.com/epoch-research/LeanOpenProblems/blob/HEAD/LICENSE)（访问2026-11-07）

**论文或技术报告**：https://arxiv.org/abs/2609.25050

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**官方代码**：https://github.com/epoch-research/LeanOpenProblems

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**数据地址**：https://github.com/epoch-research/LeanOpenProblems

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**官方主页**：https://epoch.ai/benchmarks/frontiermath-erdos

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**论文题名**：FrontierMath Erdős

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

## 发起与维护

**发起方**：Epoch AI

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**协作与机构边界**：Thomas F. Bloom（University of Manchester）；不将引用上游库等同机构合作。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**作者**：Tom Adamczewski；Thomas F. Bloom

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**维护方**：Epoch AI

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

## 设计目标

**测量能力**：在统一预算下自主证明或推翻开放数学猜想，并提交Lean形式化证明。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**相对既有评测的缺口**：避免只报道成功案例、预算不明和人工脚手架不透明；不用数值验证代替完整证明。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

## 构建方式

**题目来源**：Thomas Bloom从erdosproblems.com选取有数学意义与难度的未解问题。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**出题与研究背景**：Thomas Bloom为数学家及ErdősProblems.com维护者。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**审核流程**：50条猜想（48个编号）取自Formal Conjectures；17个未形式化编号经自动形式化得到18条猜想，Thomas Bloom逐条审核其忠实性。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**质量控制**：Comparator在独立容器中核对陈述与允许公理，并通过Lean内核重放。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**去污染与泄漏边界**：2026年8月均未解；后续已发表证明可能进入训练数据，应按模型知识截止时间过滤。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

## 数据形式

**规模与口径**：68条Lean猜想，对应65个ErdősProblems编号。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**任务类型**：证明或否证；输出完整Lean证明。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**模态**：形式化数学文本；代码

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**语言**：Lean 4 / Mathlib；自然语言文献说明。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**难度**：研究级开放猜想，形式化难度亦影响成绩。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**公开与隐藏划分**：猜想Lean陈述与评测scaffold公开；不是隐藏答案标准问答。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

## 评测方法

**指标**：68条猜想中通过核验的比例；误差条为±1标准误。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**评分方式**：仅接受与可信陈述完全一致、无额外公理、可由Lean内核重放的证明或否证。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**提示与运行设置**：每猜想一次尝试；每次300美元及72小时；离线Docker，shell、编辑器、Mathlib、SageMath及截至2022年的数学文献快照。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**官方复现入口**：https://github.com/epoch-research/LeanOpenProblems

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**可比性警告**：额外高预算或多次尝试不计入标准榜；已解问题总数不是任一模型标准分数。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**数据及热度证据**：```json
{
  "version": "68猜想固定题集（2026年8月构建）"
  "heat_confidence": "A"
  "why_trending": "候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。"
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/data/benchmarks.csv"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "organization": "Epoch AI"
      "note": "本次读取CSV并提取成功运行记录，含2026H2运行。"
    }
    {
      "url": "https://epoch.ai/benchmarks/frontiermath-erdos"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "organization": "官方维护方"
      "note": "已打开当前官方方法与榜单；观察日不冒充发布时间。"
    }
  ]
}
```

来源：[1](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**论文与版本历史**：v1：2026-09-06 19:32:55；arXiv提交历史只列这一版。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**饱和程度**：官网截至2026-10-29列出17个已解问题（包含外部研究及非标准尝试），不代表标准协议饱和。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**已知问题与局限**：证明形式化成本可能低估数学能力；后续公开解答带来污染风险。

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**后续与衍生**：原frontiermath已包含v2的Tier1–4；Erdős为独立命名未解问题套件，单独建条目。

核验说明：编辑去重口径；具体版本差异仍以官方材料为准。

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

## 榜单快照

**快照日期**：2026-11-07

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**官方入口**：https://epoch.ai/benchmarks/frontiermath-erdos

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**第三方入口**：https://epoch.ai/data/benchmarks.csv

来源：[1](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 待核实（CSV为空） | 1 | GPT-6.1 Sol (max) | 0.0441176470588235 | mean_score (0–1) | 2026-10-02 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 2 | GPT-6 Astra (max) | 0.0294117647058823 | mean_score (0–1) | 2026-08-29 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 3 | Claude Opus 5.5 (max) | 0.0294 | mean_score (0–1) | 2026-09-24 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 4 | Claude Sonnet 5.5 (max) | 0.029 | mean_score (0–1) | 2026-10-08 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 5 | GPT-6 Sol (max) | 0.0147058823529411 | mean_score (0–1) | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 6 | Gemini 4 Argon (high) | 0.0147058823529411 | mean_score (0–1) | 2026-10-21 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 7 | Grok 4.7 (xhigh) | 0.0 | mean_score (0–1) | 2026-09-22 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 待核实（CSV为空） | 8 | Gemini 3.8 Flash (high) | 0.0 | mean_score (0–1) | 2026-09-03 | [原始来源](https://epoch.ai/data/benchmarks.csv) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：刷新FrontierMath-Erdos成功记录前8，保持mean_score原始0–1小数，不将0.0294强制改成2/68。CSV task version空值仍待核实；页面17个已解包含外部/非标准尝试，不是任一模型标准分数。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

## 联系方式

**公开联系邮箱**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**Issues或讨论入口**：https://github.com/epoch-research/LeanOpenProblems/issues

来源：[1](https://github.com/epoch-research/LeanOpenProblems)（访问2026-11-07）

**官方社交**：https://x.com/EpochAIResearch

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**隐私政策**：https://epoch.ai/privacy

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

## 原始文件

**原始PDF**：https://arxiv.org/pdf/2609.25050

来源：[1](https://arxiv.org/abs/2609.25050)（访问2026-11-07）

**PDF SHA-256**：49a0289087c9378b02e0a85cded14cc0ce9d8b43a814065af2e54895eef6babc

核验说明：下载原始PDF字节计算，非arXiv网页显示大小。

来源：[1](https://arxiv.org/pdf/2609.25050)（访问2026-11-07）

**PDF字节数**：```json
316954
```

核验说明：实际下载字节数；不代表已上传。

来源：[1](https://arxiv.org/pdf/2609.25050)（访问2026-11-07）

**文件夹**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**其他官方文档**：```json
[
  {
    "type": "官方评测scaffold与Lean题目"
    "url": "https://github.com/epoch-research/LeanOpenProblems"
  }
  {
    "type": "当前已解问题登记及方法"
    "url": "https://epoch.ai/benchmarks/frontiermath-erdos"
  }
]
```

来源：[1](https://github.com/epoch-research/LeanOpenProblems)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

**论文链接**：待核实

状态：待核实。

核验说明：本组仅建立本地研究条目，未上传。

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

## 变更记录

**及历史变更**：```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    最近复核
  }
]
```

来源：[1](https://epoch.ai/benchmarks/frontiermath-erdos)（访问2026-11-07）

