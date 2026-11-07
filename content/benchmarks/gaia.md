# GAIA

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk)

## 基本信息

### 简称
GAIA [来源1](https://huggingface.co/gaia-benchmark)

### 全称
GAIA: a benchmark for General AI Assistants [来源2](https://arxiv.org/abs/2311.12983)

### 基准版本
GAIA 原始466题；2023数据发布 [来源2](https://arxiv.org/abs/2311.12983)

### 论文版本
arXiv v1 [来源2](https://arxiv.org/abs/2311.12983)

> 论文修订版本不等同数据集版本。

### 发布日期
2023-11-22 05:34:47 KST [来源2](https://arxiv.org/abs/2311.12983)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2311.12983)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "通用助理与工具使用"
]
```
 [来源2](https://arxiv.org/abs/2311.12983)

### 许可证
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 论文
https://arxiv.org/abs/2311.12983 [来源2](https://arxiv.org/abs/2311.12983)

### 官方代码
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 数据地址
https://huggingface.co/gaia-benchmark [来源2](https://arxiv.org/abs/2311.12983)

### 官方入口
https://huggingface.co/gaia-benchmark [来源1](https://huggingface.co/gaia-benchmark)

### 论文标题
GAIA: a benchmark for General AI Assistants [来源2](https://arxiv.org/abs/2311.12983)

## 发起与维护

### 机构与发起方
Meta FAIR / GenAI、Hugging Face 与 AutoGPT 作者团队（单位/项目口径） [来源2](https://arxiv.org/abs/2311.12983)

### 合作方
Surge AI 提供有偿人工标注。 [来源2](https://arxiv.org/abs/2311.12983)

### 作者

```json
[
  "Mialon, Grégoire",
  "Fourrier, Clémentine",
  "Swift, Craig",
  "Wolf, Thomas",
  "LeCun, Yann",
  "Scialom, Thomas"
]
```
 [来源2](https://arxiv.org/abs/2311.12983)

### 当前维护方
gaia-benchmark 官方 Hugging Face 组织 [来源2](https://arxiv.org/abs/2311.12983)

### 资助
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
现实信息查找、多模态理解、网页访问、工具与多步推理结合的通用助理能力。 [来源2](https://arxiv.org/abs/2311.12983)

### 设计背景
人类容易完成但需要组合工具的任务，可能比孤立专业知识题更能揭示助理系统不足。 [来源2](https://arxiv.org/abs/2311.12983)

## 构建方式

### 题目来源
人工设计可验证现实问题，答案通常短且明确，部分含附件。 [来源2](https://arxiv.org/abs/2311.12983)

### 出题者背景
研究作者与经付费招募的 Surge AI 标注者；不把所有出题人称专家。 [来源2](https://arxiv.org/abs/2311.12983)

### 审核流程
创建者之外两名独立验证者复核，不一致时修改或丢弃。 [来源2](https://arxiv.org/abs/2311.12983)

### 质量控制
力求唯一/稳定答案、可由人完成；按推理步数与工具复杂度设三档。 [来源2](https://arxiv.org/abs/2311.12983)

### 去污染
避免答案可直接在网上纯文本检索到，隐藏测试答案；问题公开后仍可能进入后续训练。 [来源2](https://arxiv.org/abs/2311.12983)

## 数据形式

### 题量与规模
466道人工问题；166道development公开答案，300道test答案隐藏。 [来源2](https://arxiv.org/abs/2311.12983)

### 题型
短答案的开放问题，可能需网页、文件、视觉和计算。 [来源2](https://arxiv.org/abs/2311.12983)

### 模态

```json
[
  "文本",
  "图像及文件附件（视题）",
  "工具/网页"
]
```
 [来源2](https://arxiv.org/abs/2311.12983)

### 语言
英语为主。 [来源2](https://arxiv.org/abs/2311.12983)

### 难度
Level 1 / 2 / 3，依据步骤、工具数量与复杂性划分。 [来源2](https://arxiv.org/abs/2311.12983)

### 公开与隐藏划分
development166答案公开；test300问题可访问但答案不公开，用官方提交评测。 [来源2](https://arxiv.org/abs/2311.12983)

## 评测方法

### 指标
准确率，按Level和总体报告。 [来源2](https://arxiv.org/abs/2311.12983)

### 评分
按答案类型规范化的准精确匹配；不以一般LLM长文评分代替。 [来源2](https://arxiv.org/abs/2311.12983)

### 提示与运行设置
原协议zero-shot；完整助理系统可以使用工具，必须报告工具、预算与附件处理。 [来源2](https://arxiv.org/abs/2311.12983)

### 官方评测脚本
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 可比性警示
validation与test、总体与各Level、多模态权限不同不可混排；不要把仅LLM和完整Agent系统分数等同。 [来源2](https://arxiv.org/abs/2311.12983)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://huggingface.co/gaia-benchmark)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "GAIA 原始466题；2023数据发布",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §4.2及参考文献明确引用 GAIA 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。"
    }
  ]
}
```
 [来源3](https://arxiv.org/html/2609.19134v1) [来源2](https://arxiv.org/abs/2311.12983)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Grégoire Mialon [ view email ] [v1] 2023-11-22 05:34:47 KST (3,688 KB) [来源2](https://arxiv.org/abs/2311.12983)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
网页内容与在线工具随时间变化、公开问题后续污染、答案规范化都会影响复现；原论文成绩不能当作当前能力上限。 [来源2](https://arxiv.org/abs/2311.12983)

### 衍生与版本关系
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://huggingface.co/gaia-benchmark)

### 官方榜单
https://huggingface.co/spaces/gaia-benchmark/leaderboard [来源4](https://huggingface.co/spaces/gaia-benchmark/leaderboard)

### 独立评测覆盖
待核实 [来源1](https://huggingface.co/gaia-benchmark)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果
待核实 [来源4](https://huggingface.co/spaces/gaia-benchmark/leaderboard)

> 官方Space已核实存在，但当前读取停在“Fetching metadata / Refreshing”，未得到可核验动态榜单行；不借历史数值冒称最新前三。

### 覆盖与时效说明
H2 ScienceIDE仅在相关工作引用GAIA，不声称实际运行；官方动态排行榜结果待核实，尚未核实AA/Epoch/LMArena同口径覆盖。 [来源4](https://huggingface.co/spaces/gaia-benchmark/leaderboard) [来源3](https://arxiv.org/html/2609.19134v1)

## 联系方式

### 公开工作邮箱

```json
[
  "gmialon@meta.com",
  "tscialom@meta.com",
  "clementine@huggingface.co"
]
```
 [来源2](https://arxiv.org/abs/2311.12983)

### 公开反馈
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2311.12983)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2311.12983 [来源5](https://arxiv.org/pdf/2311.12983)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
5bf6f968d4f5cd20acdfca6e81e3c9f5277bb66061fad7a02e35442dff812ba0 [来源5](https://arxiv.org/pdf/2311.12983)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
4254059
```
 [来源5](https://arxiv.org/pdf/2311.12983)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1XQ-wCiSOFqEob12_--TjaruKGF7D99rG",
  "webViewLink": "https://drive.google.com/drive/folders/1XQ-wCiSOFqEob12_--TjaruKGF7D99rG"
}
```
 [来源6](https://drive.google.com/drive/folders/1XQ-wCiSOFqEob12_--TjaruKGF7D99rG)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE",
    "webViewLink": "https://docs.google.com/document/d/1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE/edit?usp=drivesdk"
  }
]
```
 [来源1](https://huggingface.co/gaia-benchmark) [来源7](https://docs.google.com/document/d/1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf",
  "webViewLink": "https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk)

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
 [来源1](https://huggingface.co/gaia-benchmark)

## 来源

1. https://huggingface.co/gaia-benchmark — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2311.12983 — 采集：2026-11-07 KST。
3. https://arxiv.org/html/2609.19134v1 — 采集：2026-11-07 KST。
4. https://huggingface.co/spaces/gaia-benchmark/leaderboard — 采集：2026-11-07 KST。
5. https://arxiv.org/pdf/2311.12983 — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1XQ-wCiSOFqEob12_--TjaruKGF7D99rG — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/1UDgxrXAUff4QGR8MENwmAhxmXVNbEod1s-ePTkpfQSE/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1cvZ5wCwGoHF0mlc_2fEjkje0l1OGegpf/view?usp=drivesdk — 采集：2026-11-07 KST。
