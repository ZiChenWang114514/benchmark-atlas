# CORE-Bench

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8/view?usp=drivesdk)

## 基本信息

### 简称
CORE-Bench [来源1](https://github.com/siegelz/core-bench)

### 全称
CORE-Bench [来源1](https://github.com/siegelz/core-bench)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
原始90篇论文×3级=270任务 [来源2](https://arxiv.org/abs/2409.11363)

### 论文版本
arXiv v2 [来源2](https://arxiv.org/abs/2409.11363)

> 论文修订版本不等同数据集版本。

### 发布日期
2024-09-18 02:13:19 KST [来源2](https://arxiv.org/abs/2409.11363)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2409.11363)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "科学计算结果复现Agent"
]
```
 [来源2](https://arxiv.org/abs/2409.11363)

### 许可证
MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源1](https://github.com/siegelz/core-bench)

### 论文
https://arxiv.org/abs/2409.11363 [来源2](https://arxiv.org/abs/2409.11363)

### 官方代码
https://github.com/siegelz/core-bench [来源1](https://github.com/siegelz/core-bench)

### 数据地址
待核实 [来源2](https://arxiv.org/abs/2409.11363)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方入口
https://github.com/siegelz/core-bench [来源1](https://github.com/siegelz/core-bench)

### 论文标题
CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark [来源2](https://arxiv.org/abs/2409.11363)

## 发起与维护

### 机构与发起方
Princeton University 作者团队 [来源2](https://arxiv.org/abs/2409.11363)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2409.11363)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Zachary S. Siegel",
  "Sayash Kapoor",
  "Nitya Nadgir",
  "Benedikt Stroebl",
  "Arvind Narayanan"
]
```
 [来源2](https://arxiv.org/abs/2409.11363)

### 当前维护方
siegelz / CORE-Bench项目团队 [来源2](https://arxiv.org/abs/2409.11363)

### 资助
Princeton CSML compute；OpenAI researcher access支持。 [来源2](https://arxiv.org/abs/2409.11363)

## 设计目标

### 衡量能力
通过已有研究代码与环境重新执行实验、读取输出并回答科学结果问题。 [来源2](https://arxiv.org/abs/2409.11363)

### 设计背景
计算可复现性既是研究可信度问题，也是需要工具、软件环境与结果解释的Agent综合任务。 [来源2](https://arxiv.org/abs/2409.11363)

## 构建方式

### 题目来源
Code Ocean上的90篇计算机科学、社会科学和医学论文的代码capsule。 [来源2](https://arxiv.org/abs/2409.11363)

### 出题者背景
Princeton研究团队人工整理可复现问题。 [来源2](https://arxiv.org/abs/2409.11363)

### 审核流程
每个capsule人工运行3次，验证问题可答与输出稳定性。 [来源2](https://arxiv.org/abs/2409.11363)

### 质量控制
确定性输出精确答案；非确定性数值用重复运行构造95%预测区间。 [来源2](https://arxiv.org/abs/2409.11363)

### 去污染
评测禁止访问Code Ocean网站以免直接取回现成输出；公开论文/代码的训练泄漏仍无法完全排除。 [来源2](https://arxiv.org/abs/2409.11363)

## 数据形式

### 题量与规模
90论文、270任务（每篇3难度）；45论文train/45test；181个独特问题被复用于各难度，不等于270篇论文。 [来源2](https://arxiv.org/abs/2409.11363)

### 题型
运行科研代码、检查产物，回答关于实验/图表的短问题。 [来源2](https://arxiv.org/abs/2409.11363)

### 模态

```json
[
  "论文/README文本",
  "代码",
  "实验数据/结果文件"
]
```
 [来源2](https://arxiv.org/abs/2409.11363)

### 语言
Python / R科研代码；英语问题与文档。 [来源2](https://arxiv.org/abs/2409.11363)

### 难度
Easy给出输出；Medium给Dockerfile+README；Hard只有README，需自行配置执行。 [来源2](https://arxiv.org/abs/2409.11363)

### 公开与隐藏划分
按论文分45/45 train/test以避免同篇跨split；研究材料/脚本公开。 [来源2](https://arxiv.org/abs/2409.11363)

## 评测方法

### 指标
任务全问题正确率；按Easy/Medium/Hard分别报告。 [来源2](https://arxiv.org/abs/2409.11363)

### 评分
一项任务内全部问题都正确才通过，数值允许按官方区间检查。 [来源2](https://arxiv.org/abs/2409.11363)

### 提示与运行设置
CORE-Agent / AutoGPT等harness与模型快照、环境信息权限必须注明；禁止浏览Code Ocean找输出。 [来源2](https://arxiv.org/abs/2409.11363)

### 官方评测脚本
https://github.com/siegelz/core-bench [来源1](https://github.com/siegelz/core-bench)

### 可比性警示
不同难度提供信息不同；270任务存在同篇与同问题复用，不能解释为270独立科学研究复现。 [来源2](https://arxiv.org/abs/2409.11363)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/siegelz/core-bench)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始90篇论文×3级=270任务",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §4.1及参考文献明确引用 CORE-Bench，讨论以已有研究结果复现为目标的评价；为H2学术引用。"
    }
  ]
}
```
 [来源3](https://arxiv.org/html/2609.19134v1) [来源2](https://arxiv.org/abs/2409.11363)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Zachary Siegel [ view email ] [v1] 2024-09-18 02:13:19 KST (2,912 KB) [v2] 2026-06-23 07:36:12 KST (2,906 KB) [来源2](https://arxiv.org/abs/2409.11363)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2409.11363)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
非确定性实验、依赖安装和数据下载会影响复现；论文Easy结果存在60.00/60.60文本冲突，保留而不擅自修正。 [来源2](https://arxiv.org/abs/2409.11363)

### 衍生与版本关系
Easy/Medium/Hard为同一套件信息权限级别，计一个benchmark；与从头复写论文的PaperBench不同。 [来源2](https://arxiv.org/abs/2409.11363)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/siegelz/core-bench)

### 官方榜单
https://github.com/siegelz/core-bench [来源1](https://github.com/siegelz/core-bench)

### 独立评测覆盖
待核实 [来源1](https://github.com/siegelz/core-bench)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "CORE-Agent + gpt-4o-2024-05-13",
    "score": 21.48,
    "metric": "Hard任务成功率 (%)",
    "benchmark_version": "原始Hard",
    "result_type": "论文历史基线",
    "source_date": "论文Table1",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "CORE-Agent + gpt-4o-mini-2024-07-18",
    "score": 16.3,
    "metric": "Hard任务成功率 (%)",
    "benchmark_version": "原始Hard",
    "result_type": "论文历史基线",
    "source_date": "论文Table1",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "AutoGPT + gpt-4o-2024-05-13",
    "score": 6.67,
    "metric": "Hard任务成功率 (%)",
    "benchmark_version": "原始Hard",
    "result_type": "论文历史基线",
    "source_date": "论文Table1",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源2](https://arxiv.org/abs/2409.11363)

### 覆盖与时效说明
均为论文历史Hard基线，不是11月7日最新榜。论文Easy主表60.00与正文/附录60.60有不一致，暂不在结果表采用该冲突数字。H2 ScienceIDE仅引用本benchmark。 [来源2](https://arxiv.org/abs/2409.11363)

## 联系方式

### 公开工作邮箱

```json
[
  "zachary@siegel.com",
  "sayashk@princeton.edu",
  "nn7887@princeton.edu",
  "stroebl@princeton.edu",
  "arvindn@cs.princeton.edu"
]
```
 [来源2](https://arxiv.org/abs/2409.11363)

### 公开反馈
https://github.com/siegelz/core-bench/issues [来源1](https://github.com/siegelz/core-bench)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2409.11363)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2409.11363)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2409.11363 [来源4](https://arxiv.org/pdf/2409.11363)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
1d1fbe8a3cf472fc468495e6a3bcd6b90224ba1eae3dac8d8174f98d666c3d76 [来源4](https://arxiv.org/pdf/2409.11363)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
2885202
```
 [来源4](https://arxiv.org/pdf/2409.11363)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl",
  "webViewLink": "https://drive.google.com/drive/folders/1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl"
}
```
 [来源5](https://drive.google.com/drive/folders/1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA",
    "webViewLink": "https://docs.google.com/document/d/1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA/edit?usp=drivesdk"
  }
]
```
 [来源1](https://github.com/siegelz/core-bench) [来源6](https://docs.google.com/document/d/1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8",
  "webViewLink": "https://drive.google.com/file/d/1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8/view?usp=drivesdk"
}
```
 [来源7](https://drive.google.com/file/d/1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8/view?usp=drivesdk)

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
 [来源1](https://github.com/siegelz/core-bench)

## 来源

1. https://github.com/siegelz/core-bench — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2409.11363 — 采集：2026-11-07 KST。
3. https://arxiv.org/html/2609.19134v1 — 采集：2026-11-07 KST。
4. https://arxiv.org/pdf/2409.11363 — 采集：2026-11-07 KST。
5. https://drive.google.com/drive/folders/1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl — 采集：2026-11-07 KST。
6. https://docs.google.com/document/d/1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA/edit?usp=drivesdk — 采集：2026-11-07 KST。
7. https://drive.google.com/file/d/1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8/view?usp=drivesdk — 采集：2026-11-07 KST。
