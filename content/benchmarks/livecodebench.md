# LiveCodeBench

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；采集日不等于运行日，历史榜单、研究复测与独立评测分别记录。

## 基本信息

### 简称

LiveCodeBench

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 全称

LiveCodeBench

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 基准版本

README列举到release_v6；默认release_latest是可变别名，复现须锁定release_version和题目日期窗。

来源：[https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)（访问 2026-11-07 KST）

### 论文版本

arXiv v2

> 论文修订版本不等同数据集版本。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 发布日期

2024-03-13 02:58:04 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 主板块

代码

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 领域标签

滚动编程竞赛评测

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 许可证

MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

来源：[https://github.com/LiveCodeBench/LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench)（访问 2026-11-07 KST）

### 论文

https://arxiv.org/abs/2403.07974

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 官方代码

https://github.com/LiveCodeBench/LiveCodeBench

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 数据地址

https://huggingface.co/livecodebench/

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 官方入口

https://livecodebench.github.io/

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 论文标题

LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

## 发起与维护

### 机构与发起方

UC Berkeley、MIT、Cornell University 作者团队（单位口径）

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 合作方

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 作者

Jain, Naman、Han, King、Gu, Alex、Li, Wen-Ding、Yan, Fanjia、Zhang, Tianjun、Wang, Sida、Solar-Lezama, Armando、Sen, Koushik、Stoica, Ion

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 当前维护方

LiveCodeBench 项目团队

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

## 设计目标

### 衡量能力

代码生成、自修复、代码执行和测试输出预测的综合能力。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 设计背景

静态题库可能被训练反复接触；仅生成任务无法完整评估代码理解与修复。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

## 构建方式

### 题目来源

持续收集 LeetCode、AtCoder、Codeforces 定期竞赛的新题，记录发布时间。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 出题者背景

三校程序合成、软件与机器学习研究团队；原题来自竞赛平台。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 审核流程

整理问题、测试与场景，官方接受附生成记录的 GitHub PR 并审核后入榜。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 质量控制

ERRATA追踪错误测试及不适合自动评分的问题；code_generation_lite删减测试以加速，原始集需--not_fast。官方提示超时可造成小于0.5点分数变化。

来源：[https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)（访问 2026-11-07 KST）

### 去污染

可选在模型训练截止日期之后发布的题，以降低污染；截止日期不透明、题库公开后再训练仍会影响有效性。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

## 数据形式

### 题量与规模

README明确列出 release_v1 400、v2 511、v3 612、v4 713、v5 880、v6 1,055题；v6覆盖2023-05至2025-04。主页300+与论文500+属历史窗口，不能当作当前总量。

来源：[https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)（访问 2026-11-07 KST）

### 题型

算法程序生成、基于反馈的修复、程序执行、测试输出预测。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 模态

文本、代码

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 语言

英语竞赛描述；生成代码支持范围依场景/脚本。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 难度

保留竞赛题难度差异，按 easy / medium / hard 分析；不能仅据旧 easy 子集判断整体饱和。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 公开与隐藏划分

题目与评测工具逐批公开；去污染依时间窗，不等同永久私有题库。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

## 评测方法

### 指标

各场景执行正确率 / pass@k；生成、修复和输出预测分开。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 评分

根据竞赛测试或已知输入输出检查生成结果。

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 提示与运行设置

官方代码生成示例n=10、temperature=0.2；按模型设置提示；生成计算pass@1/pass@5。必须固定release_version、start_date/end_date、lite或原始测试。

来源：[https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md](https://raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md)（访问 2026-11-07 KST）

### 官方评测脚本

https://github.com/LiveCodeBench/LiveCodeBench

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 可比性警示

不同时窗、题目数量和场景不可直排。AA 当前摘要未给出精确评测窗，保留范围待核实。

核验状态：待核实

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "持续滚动采题；必须按评测时间窗固定快照",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1/§4.2及表2–4实际报告 LiveCodeBench；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。"
    }
  ]
}
```

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 KST）；[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 论文修订历史

Submission history From: Naman Jain [ view email ] [v1] 2024-03-13 02:58:04 KST (6,890 KB) [v2] 2024-06-07 02:41:21 KST (7,772 KB)

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 污染与争议

“Contamination Free”是设计目标/标题；成立范围取决于模型截止日、题目发布时间和后续训练，不能绝对保证。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)（访问 2026-11-07 KST）

### 衍生与版本关系

代码生成、self-repair、execution、test-output prediction 为同套件场景，不拆为四条。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)（访问 2026-11-07 KST）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 官方榜单

https://livecodebench.github.io/

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 独立评测覆盖

https://artificialanalysis.ai/evaluations/livecodebench

来源：[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)（访问 2026-11-07 KST）

### 核验结果

```json
[
  {
    "model": "Gemini 3 Pro Preview (High)",
    "score": 91.7,
    "metric": "AA LiveCodeBench score (%)",
    "benchmark_version": "AA窗口待核实",
    "result_type": "独立第三方当前页面",
    "source_date": "待核实（页面未给出该结果运行/发布日期）",
    "collected_at": "2026-11-07 KST",
    "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
  },
  {
    "model": "Gemini 3 Flash Preview (Reasoning)",
    "score": 90.8,
    "metric": "AA LiveCodeBench score (%)",
    "benchmark_version": "AA窗口待核实",
    "result_type": "独立第三方当前页面",
    "source_date": "待核实（页面未给出该结果运行/发布日期）",
    "collected_at": "2026-11-07 KST",
    "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
  },
  {
    "model": "DeepSeek V3.2 Speciale",
    "score": 89.6,
    "metric": "AA LiveCodeBench score (%)",
    "benchmark_version": "AA窗口待核实",
    "result_type": "独立第三方当前页面",
    "source_date": "待核实（页面未给出该结果运行/发布日期）",
    "collected_at": "2026-11-07 KST",
    "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
  },
  {
    "model": "Hunyuan-A13B slow-thinking",
    "score": 63.9,
    "metric": "报告中的 LiveCodeBench (%)",
    "benchmark_version": "日期窗待核实",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST"
  }
]
```

核验状态：待核实

来源：[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)（访问 2026-11-07 KST）；[https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 KST）

### 覆盖与时效说明

AA 页面确有前三结果，但未从该页面静态正文核实题目日期窗和每个运行日期；采集日不是运行日。官方旧主页图表不是 2026 完整榜，不能与厂商报告跨窗排序。

来源：[https://artificialanalysis.ai/evaluations/livecodebench](https://artificialanalysis.ai/evaluations/livecodebench)（访问 2026-11-07 KST）；[https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 KST）

## 联系方式

### 公开工作邮箱

naman_jain@berkeley.edu

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 公开反馈

https://github.com/LiveCodeBench/LiveCodeBench/issues

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)（访问 2026-11-07 KST）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2403.07974

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)（访问 2026-11-07 KST）

### 原始PDF SHA-256

a9bd3f7b96ac846ac53506e7b58197d9213919f18f402a27910dcf9fc948b427

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)（访问 2026-11-07 KST）

### 原始PDF字节数

4960954

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2403.07974](https://arxiv.org/pdf/2403.07974)（访问 2026-11-07 KST）

### Drive资料文件夹

```json
{
  "id": "1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV",
  "webViewLink": "https://drive.google.com/drive/folders/1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV"
}
```

来源：[https://drive.google.com/drive/folders/1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV](https://drive.google.com/drive/folders/1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV)（访问 2026-11-07 KST）

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s",
    "webViewLink": "https://docs.google.com/document/d/1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s/edit?usp=drivesdk"
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）；[https://docs.google.com/document/d/1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s/edit?usp=drivesdk](https://docs.google.com/document/d/1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s/edit?usp=drivesdk)（访问 2026-11-07 KST）

### Drive 原始 PDF

```json
{
  "id": "1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ",
  "webViewLink": "https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk"
}
```

来源：[https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk](https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk)（访问 2026-11-07 KST）

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  },
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "第1轮深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。"
  }
]
```

来源：[https://livecodebench.github.io/](https://livecodebench.github.io/)（访问 2026-11-07 KST）
