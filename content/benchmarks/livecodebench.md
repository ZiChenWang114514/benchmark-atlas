# LiveCodeBench

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk)

## 基本信息

### 简称
LiveCodeBench [来源1](https://livecodebench.github.io/)

### 全称
LiveCodeBench [来源1](https://livecodebench.github.io/)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
持续滚动采题；必须按评测时间窗固定快照 [来源1](https://livecodebench.github.io/)

### 论文版本
arXiv v2 [来源2](https://arxiv.org/abs/2403.07974)

> 论文修订版本不等同数据集版本。

### 发布日期
2024-03-13 02:58:04 KST [来源2](https://arxiv.org/abs/2403.07974)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
代码 [来源2](https://arxiv.org/abs/2403.07974)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "滚动编程竞赛评测"
]
```
 [来源2](https://arxiv.org/abs/2403.07974)

### 许可证
MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源3](https://github.com/LiveCodeBench/LiveCodeBench)

### 论文
https://arxiv.org/abs/2403.07974 [来源2](https://arxiv.org/abs/2403.07974)

### 官方代码
https://github.com/LiveCodeBench/LiveCodeBench [来源1](https://livecodebench.github.io/)

### 数据地址
https://huggingface.co/livecodebench/ [来源1](https://livecodebench.github.io/)

### 官方入口
https://livecodebench.github.io/ [来源1](https://livecodebench.github.io/)

### 论文标题
LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code [来源2](https://arxiv.org/abs/2403.07974)

## 发起与维护

### 机构与发起方
UC Berkeley、MIT、Cornell University 作者团队（单位口径） [来源2](https://arxiv.org/abs/2403.07974)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Jain, Naman",
  "Han, King",
  "Gu, Alex",
  "Li, Wen-Ding",
  "Yan, Fanjia",
  "Zhang, Tianjun",
  "Wang, Sida",
  "Solar-Lezama, Armando",
  "Sen, Koushik",
  "Stoica, Ion"
]
```
 [来源2](https://arxiv.org/abs/2403.07974)

### 当前维护方
LiveCodeBench 项目团队 [来源2](https://arxiv.org/abs/2403.07974)

### 资助
待核实 [来源2](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
代码生成、自修复、代码执行和测试输出预测的综合能力。 [来源2](https://arxiv.org/abs/2403.07974)

### 设计背景
静态题库可能被训练反复接触；仅生成任务无法完整评估代码理解与修复。 [来源2](https://arxiv.org/abs/2403.07974)

## 构建方式

### 题目来源
持续收集 LeetCode、AtCoder、Codeforces 定期竞赛的新题，记录发布时间。 [来源1](https://livecodebench.github.io/)

### 出题者背景
三校程序合成、软件与机器学习研究团队；原题来自竞赛平台。 [来源1](https://livecodebench.github.io/)

### 审核流程
整理问题、测试与场景，官方接受附生成记录的 GitHub PR 并审核后入榜。 [来源1](https://livecodebench.github.io/)

### 质量控制
以可执行测试与发布日期注释支持复查；公布提示和模型生成。 [来源1](https://livecodebench.github.io/)

### 去污染
可选在模型训练截止日期之后发布的题，以降低污染；截止日期不透明、题库公开后再训练仍会影响有效性。 [来源1](https://livecodebench.github.io/)

## 数据形式

### 题量与规模
主页早期快照为 300+ 题（2023-05 至 2024-02）；论文修订/AA 摘要为 500+（至 2024-05）。这些是历史时间窗，不是 2026 总题量。 [来源1](https://livecodebench.github.io/) [来源2](https://arxiv.org/abs/2403.07974)

### 题型
算法程序生成、基于反馈的修复、程序执行、测试输出预测。 [来源1](https://livecodebench.github.io/) [来源2](https://arxiv.org/abs/2403.07974)

### 模态

```json
[
  "文本",
  "代码"
]
```
 [来源1](https://livecodebench.github.io/) [来源2](https://arxiv.org/abs/2403.07974)

### 语言
英语竞赛描述；生成代码支持范围依场景/脚本。 [来源1](https://livecodebench.github.io/) [来源2](https://arxiv.org/abs/2403.07974)

### 难度
保留竞赛题难度差异，按 easy / medium / hard 分析；不能仅据旧 easy 子集判断整体饱和。 [来源1](https://livecodebench.github.io/) [来源2](https://arxiv.org/abs/2403.07974)

### 公开与隐藏划分
题目与评测工具逐批公开；去污染依时间窗，不等同永久私有题库。 [来源1](https://livecodebench.github.io/) [来源2](https://arxiv.org/abs/2403.07974)

## 评测方法

### 指标
各场景执行正确率 / pass@k；生成、修复和输出预测分开。 [来源2](https://arxiv.org/abs/2403.07974)

### 评分
根据竞赛测试或已知输入输出检查生成结果。 [来源2](https://arxiv.org/abs/2403.07974)

### 提示与运行设置
场景、语言、日期窗、采样和修复预算必须固定；本条不假定所有榜单共用一个提示。 [来源2](https://arxiv.org/abs/2403.07974)

### 官方评测脚本
https://github.com/LiveCodeBench/LiveCodeBench [来源1](https://livecodebench.github.io/)

### 可比性警示
不同时窗、题目数量和场景不可直排。AA 当前摘要未给出精确评测窗，保留范围待核实。 [来源2](https://arxiv.org/abs/2403.07974)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://livecodebench.github.io/)

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
 [来源4](https://arxiv.org/html/2609.27284v1) [来源1](https://livecodebench.github.io/)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Naman Jain [ view email ] [v1] 2024-03-13 02:58:04 KST (6,890 KB) [v2] 2024-06-07 02:41:21 KST (7,772 KB) [来源2](https://arxiv.org/abs/2403.07974)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
“Contamination Free”是设计目标/标题；成立范围取决于模型截止日、题目发布时间和后续训练，不能绝对保证。 [来源1](https://livecodebench.github.io/) [来源5](https://artificialanalysis.ai/evaluations/livecodebench)

### 衍生与版本关系
代码生成、self-repair、execution、test-output prediction 为同套件场景，不拆为四条。 [来源1](https://livecodebench.github.io/) [来源5](https://artificialanalysis.ai/evaluations/livecodebench)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://livecodebench.github.io/)

### 官方榜单
https://livecodebench.github.io/ [来源1](https://livecodebench.github.io/)

### 独立评测覆盖
https://artificialanalysis.ai/evaluations/livecodebench [来源5](https://artificialanalysis.ai/evaluations/livecodebench)

### 核验结果

```json
[
  {
    "model": "Gemini 3 Pro Preview (High)",
    "score": 91.7,
    "metric": "AA LiveCodeBench score (%)",
    "benchmark_version": "AA窗口待核实",
    "result_type": "独立第三方当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Gemini 3 Flash Preview (Reasoning)",
    "score": 90.8,
    "metric": "AA LiveCodeBench score (%)",
    "benchmark_version": "AA窗口待核实",
    "result_type": "独立第三方当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "DeepSeek V3.2 Speciale",
    "score": 89.6,
    "metric": "AA LiveCodeBench score (%)",
    "benchmark_version": "AA窗口待核实",
    "result_type": "独立第三方当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
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
 [来源5](https://artificialanalysis.ai/evaluations/livecodebench) [来源4](https://arxiv.org/html/2609.27284v1)

### 覆盖与时效说明
AA 页面确有前三结果，但未从该页面静态正文核实题目日期窗和每个运行日期；采集日不是运行日。官方旧主页图表不是 2026 完整榜，不能与厂商报告跨窗排序。 [来源5](https://artificialanalysis.ai/evaluations/livecodebench) [来源4](https://arxiv.org/html/2609.27284v1)

## 联系方式

### 公开工作邮箱

```json
[
  "naman_jain@berkeley.edu"
]
```
 [来源1](https://livecodebench.github.io/)

### 公开反馈
https://github.com/LiveCodeBench/LiveCodeBench/issues [来源1](https://livecodebench.github.io/)

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2403.07974)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2403.07974 [来源6](https://arxiv.org/pdf/2403.07974)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
a9bd3f7b96ac846ac53506e7b58197d9213919f18f402a27910dcf9fc948b427 [来源6](https://arxiv.org/pdf/2403.07974)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
4960954
```
 [来源6](https://arxiv.org/pdf/2403.07974)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV",
  "webViewLink": "https://drive.google.com/drive/folders/1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV"
}
```
 [来源7](https://drive.google.com/drive/folders/1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV)

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
 [来源1](https://livecodebench.github.io/) [来源8](https://docs.google.com/document/d/1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ",
  "webViewLink": "https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk"
}
```
 [来源9](https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk)

## 变更记录


```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  }
]
```
 [来源1](https://livecodebench.github.io/)

## 来源

1. https://livecodebench.github.io/ — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2403.07974 — 采集：2026-11-07 KST。
3. https://github.com/LiveCodeBench/LiveCodeBench — 采集：2026-11-07 KST。
4. https://arxiv.org/html/2609.27284v1 — 采集：2026-11-07 KST。
5. https://artificialanalysis.ai/evaluations/livecodebench — 采集：2026-11-07 KST。
6. https://arxiv.org/pdf/2403.07974 — 采集：2026-11-07 KST。
7. https://drive.google.com/drive/folders/1z_HNk1FMPnVaJNDIVXUWGGrisPnD3hoV — 采集：2026-11-07 KST。
8. https://docs.google.com/document/d/1iQzZ3B9j7C9CRYuWX6lgKirBvC2894MkhBghQou8p7s/edit?usp=drivesdk — 采集：2026-11-07 KST。
9. https://drive.google.com/file/d/1Z6rekgybFUTEyxblITw5c09XnFgkQ7UZ/view?usp=drivesdk — 采集：2026-11-07 KST。
