# PaperBench

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk/view?usp=drivesdk)

## 基本信息

### 简称
PaperBench [来源1](https://openai.com/index/paperbench/)

### 全称
PaperBench [来源1](https://openai.com/index/paperbench/)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
原始20篇ICML2024论文套件 [来源2](https://arxiv.org/abs/2504.01848)

### 论文版本
arXiv v3 [来源2](https://arxiv.org/abs/2504.01848)

> 论文修订版本不等同数据集版本。

### 发布日期
2025-04-03 00:55:24 KST [来源2](https://arxiv.org/abs/2504.01848)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2504.01848)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "AI论文复现Agent"
]
```
 [来源2](https://arxiv.org/abs/2504.01848)

### 许可证
MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源3](https://github.com/openai/frontier-evals)

### 论文
https://arxiv.org/abs/2504.01848 [来源2](https://arxiv.org/abs/2504.01848)

### 官方代码
https://github.com/openai/frontier-evals [来源3](https://github.com/openai/frontier-evals)

> 论文链接openai/preparedness；本次GitHub元数据请求跳转至openai/frontier-evals。仓库根代码许可不自动等同每篇论文及rubric许可。

### 数据地址
待核实 [来源2](https://arxiv.org/abs/2504.01848)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方入口
https://openai.com/index/paperbench/ [来源1](https://openai.com/index/paperbench/)

### 论文标题
PaperBench: Evaluating AI's Ability to Replicate AI Research [来源2](https://arxiv.org/abs/2504.01848)

## 发起与维护

### 机构与发起方
OpenAI [来源1](https://openai.com/index/paperbench/)

### 合作方
被复现ICML论文作者共同制定rubric并签核；不意味着共同维护整个benchmark。 [来源1](https://openai.com/index/paperbench/)

### 作者

```json
[
  "Starace, Giulio",
  "Jaffe, Oliver",
  "Sherburn, Dane",
  "Aung, James",
  "Chan, Jun Shern",
  "Maksin, Leon",
  "Dias, Rachel",
  "Mays, Evan",
  "Kinsella, Benjamin",
  "Thompson, Wyatt",
  "Heidecke, Johannes",
  "Glaese, Amelia",
  "Patwardhan, Tejal"
]
```
 [来源2](https://arxiv.org/abs/2504.01848)

### 当前维护方
OpenAI Preparedness / PaperBench团队 [来源1](https://openai.com/index/paperbench/)

### 资助
待核实 [来源2](https://arxiv.org/abs/2504.01848)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
从论文理解贡献、从零开发代码、执行实验并复现现代AI研究。 [来源2](https://arxiv.org/abs/2504.01848)

### 设计背景
已有科研代码重跑与孤立ML竞赛不能充分测量端到端从论文重建实验的科研工程能力。 [来源2](https://arxiv.org/abs/2504.01848)

## 构建方式

### 题目来源
20篇ICML2024 spotlight/oral论文，覆盖12个主题；另设2篇NeurIPS workshop开发论文和内部holdout。 [来源2](https://arxiv.org/abs/2504.01848)

### 出题者背景
OpenAI研究团队与原论文作者共同分解复现目标。 [来源2](https://arxiv.org/abs/2504.01848)

### 审核流程
层级rubric与原作者协作，多轮内部审查、澄清addendum，最终作者签核。 [来源2](https://arxiv.org/abs/2504.01848)

### 质量控制
8,316个可独立评分叶节点；新VM执行reproduce.sh后裁判评分；另用JudgeEval测裁判。 [来源2](https://arxiv.org/abs/2504.01848)

### 去污染
禁止访问原作者仓库与其他复现；论文报告646次尝试中10次违规被取消，不能排除预训练中记忆代码。 [来源2](https://arxiv.org/abs/2504.01848)

## 数据形式

### 题量与规模
20篇正式论文、8,316个评分叶节点；叶节点不是8,316个独立论文复现任务。 [来源2](https://arxiv.org/abs/2504.01848)

### 题型
长程科研编程与实验执行；提交代码/文件，再按层级rubric检查。 [来源2](https://arxiv.org/abs/2504.01848)

### 模态

```json
[
  "论文文本/图表",
  "代码",
  "实验数据与输出"
]
```
 [来源2](https://arxiv.org/abs/2504.01848)

### 语言
英语论文与说明；代码语言/框架随论文。 [来源2](https://arxiv.org/abs/2504.01848)

### 难度
原论文复现多小时预算；BasicAgent与IterativeAgent、12h/36h条件不同。 [来源2](https://arxiv.org/abs/2504.01848)

### 公开与隐藏划分
公开论文、rubric与评测代码，另有开发论文与内部保留集；正式20篇不可和开发集混合。 [来源2](https://arxiv.org/abs/2504.01848)

## 评测方法

### 指标
Replication Score：叶节点二元判定后按层级权重聚合，再对论文平均。 [来源2](https://arxiv.org/abs/2504.01848)

### 评分
先在fresh VM运行reproduce.sh，裁判据执行结果与代码核验；Code-Dev跳过运行，不能替代完整Replication。 [来源2](https://arxiv.org/abs/2504.01848)

### 提示与运行设置
原论文自动裁判o3-mini-2025-01-31 high；不同agent scaffold、工具和实验预算分别记录。 [来源2](https://arxiv.org/abs/2504.01848)

### 官方评测脚本
https://github.com/openai/preparedness [来源1](https://openai.com/index/paperbench/)

### 可比性警示
BasicAgent21%与IterativeAgent24–26%并非仅模型能力变化；CodeDev、预算、judge版本、标准误和论文子集必须注明。 [来源2](https://arxiv.org/abs/2504.01848)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://openai.com/index/paperbench/)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始20篇ICML2024论文套件",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §4.1及参考文献明确引用 PaperBench，讨论以已有研究结果复现为目标的评价；为H2学术引用。"
    }
  ]
}
```
 [来源4](https://arxiv.org/html/2609.19134v1) [来源2](https://arxiv.org/abs/2504.01848)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: James Aung [ view email ] [v1] 2025-04-03 00:55:24 KST (4,982 KB) [v2] 2025-04-04 21:44:57 KST (4,982 KB) [v3] 2025-04-07 21:15:49 KST (4,982 KB) [来源2](https://arxiv.org/abs/2504.01848)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2504.01848)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
自动裁判不完美且非确定；原论文JudgeEval F1约0.83。公开论文/禁用仓库可能仍在预训练中；禁止检索不等于排除记忆。 [来源2](https://arxiv.org/abs/2504.01848)

### 衍生与版本关系
PaperBench Code-Dev省略运行，是独立口径；JudgeEval评价裁判，不当作更多论文复现题计数。 [来源2](https://arxiv.org/abs/2504.01848)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://openai.com/index/paperbench/)

### 官方榜单
https://openai.com/index/paperbench/ [来源1](https://openai.com/index/paperbench/)

### 独立评测覆盖
待核实 [来源1](https://openai.com/index/paperbench/)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "BasicAgent + Claude 3.5 Sonnet 20241022",
    "score": 21,
    "metric": "Replication Score (%)",
    "benchmark_version": "20论文",
    "result_type": "论文历史基线",
    "source_date": "2025-04",
    "collected_at": "2026-11-07 KST",
    "uncertainty": "±0.8百分点"
  },
  {
    "model": "BasicAgent + o1-2024-12-17 high",
    "score": 13.2,
    "metric": "Replication Score (%)",
    "benchmark_version": "20论文",
    "result_type": "论文历史基线",
    "source_date": "2025-04",
    "collected_at": "2026-11-07 KST",
    "uncertainty": "±0.3百分点"
  },
  {
    "model": "IterativeAgent + o1-2024-12-17 high",
    "score": 24.4,
    "metric": "Replication Score (%)",
    "benchmark_version": "20论文/12小时",
    "result_type": "论文历史基线",
    "source_date": "2025-04",
    "collected_at": "2026-11-07 KST",
    "uncertainty": "±0.7百分点"
  },
  {
    "model": "IterativeAgent + o1-2024-12-17 high",
    "score": 26,
    "metric": "Replication Score (%)",
    "benchmark_version": "20论文/36小时",
    "result_type": "论文历史基线",
    "source_date": "2025-04",
    "collected_at": "2026-11-07 KST",
    "uncertainty": "±0.3百分点"
  }
]
```
 [来源2](https://arxiv.org/abs/2504.01848)

### 覆盖与时效说明
所有结果为原论文设置的历史实验，不冒称2026当前SOTA；H2 ScienceIDE引用PaperBench作科学研究复现先行基准，没有在其上实跑。 [来源2](https://arxiv.org/abs/2504.01848)

## 联系方式

### 公开工作邮箱
待核实 [来源2](https://arxiv.org/abs/2504.01848)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
https://github.com/openai/frontier-evals/issues [来源3](https://github.com/openai/frontier-evals)

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2504.01848)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2504.01848)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2504.01848 [来源5](https://arxiv.org/pdf/2504.01848)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
2f58f1a6581af9d99432422dccf3cf61f5c263377c1e4550e7333c4a22d7184d [来源5](https://arxiv.org/pdf/2504.01848)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
1703363
```
 [来源5](https://arxiv.org/pdf/2504.01848)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c",
  "webViewLink": "https://drive.google.com/drive/folders/1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c"
}
```
 [来源6](https://drive.google.com/drive/folders/1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE",
    "webViewLink": "https://docs.google.com/document/d/1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE/edit?usp=drivesdk"
  }
]
```
 [来源1](https://openai.com/index/paperbench/) [来源7](https://docs.google.com/document/d/1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk",
  "webViewLink": "https://drive.google.com/file/d/1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk/view?usp=drivesdk)

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
 [来源1](https://openai.com/index/paperbench/)

## 来源

1. https://openai.com/index/paperbench/ — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2504.01848 — 采集：2026-11-07 KST。
3. https://github.com/openai/frontier-evals — 采集：2026-11-07 KST。
4. https://arxiv.org/html/2609.19134v1 — 采集：2026-11-07 KST。
5. https://arxiv.org/pdf/2504.01848 — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk/view?usp=drivesdk — 采集：2026-11-07 KST。
