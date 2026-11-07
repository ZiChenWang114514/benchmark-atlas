# MMLU-ProX

> 核验：2026-11-07（KST / Asia/Seoul）。基于官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1gohaRGvTuT_OgM7cpG7rgGG4oAjWNDuR/view?usp=drivesdk)

## 基本信息

### 简称

MMLU-ProX

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 全称

MMLU-ProX

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 基准版本

MMLU-ProX：29语言全量版及Lite版；2025-05官方发布记录。

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 论文版本

arXiv v2

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 发布日期

2025-03-13

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块

语言

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签

```json
[
  "多语言高难知识"
]
```

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 许可证

MIT（官方数据集卡声明）

[来源1](https://huggingface.co/datasets/li-lab/MMLU-ProX)（采集2026-11-07）

### 论文

https://arxiv.org/abs/2503.10497

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 官方代码

https://github.com/weihao1115/MMLU-ProX

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 数据地址

https://huggingface.co/datasets/li-lab/MMLU-ProX

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 官方入口

https://mmluprox.github.io/

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 论文标题

MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

## 发起与维护

### 机构与作者单位

论文作者来自 University of Tokyo、Duke-NUS、Waseda 等多所机构；不把作者单位等同于正式合作协议。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 正式合作机构

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者

```json
[
  "Xuan, Weihao",
  "Yang, Rui",
  "Qi, Heli",
  "Zeng, Qingcheng",
  "Xiao, Yunze",
  "Feng, Aosong",
  "Liu, Dairui",
  "Xing, Yun",
  "Wang, Junjue",
  "Gao, Fan",
  "Lu, Jinghui",
  "Jiang, Yuang",
  "Li, Huitao",
  "Li, Xin",
  "Yu, Kunyu",
  "Dong, Ruihai",
  "Gu, Shangding",
  "Li, Yuekang",
  "Xie, Xiaofei",
  "Juefei-Xu, Felix",
  "Khomh, Foutse",
  "Yoshie, Osamu",
  "Chen, Qingyu",
  "Teodoro, Douglas",
  "Liu, Nan",
  "Goebel, Randy",
  "Ma, Lei",
  "Marrese-Taylor, Edison",
  "Lu, Shijian",
  "Iwasawa, Yusuke",
  "Matsuo, Yutaka",
  "Li, Irene"
]
```

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 当前维护方

官方公开代码托管于 weihao1115；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 资助

官网致谢列出 JSPS KAKENHI 24K20832、JST ActX JPMJAX24CU、NVIDIA Academic Grant、Google Gemma Academic Program。

[来源1](https://mmluprox.github.io/)（采集2026-11-07）

## 设计目标

### 测量能力

在相同难题上直接比较多语言知识与推理能力。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 既有评测缺口

英语评测主导，现有多语题集常缺少相互平行、保持推理难度的题目。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

## 构建方式

### 题目来源

以 MMLU-Pro 英语题为基础，采用多个 LLM 翻译后由专家审阅。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 出题与标注背景

多语专家核对术语、概念和文化适配；各语种专家资历以论文附录为准。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 审核

专家检查准确表达、术语一致性与文化相关性。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 质量控制

保持跨语种平行问题，提供 full 与 lite 版本；译文偏差仍可能影响比较。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 去污染

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量

29 种语言，每语种 11,829 道平行题；lite 每语种 658 题。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07） [来源2](https://huggingface.co/datasets/li-lab/MMLU-ProX)（采集2026-11-07）

### 题型

多项选择知识/推理题

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 语言

29种语言（官方README当前描述；不是只统计非英语翻译）

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 难度

继承 MMLU-Pro 的推理导向；高低资源语言之间的分差不是单纯题目难度差。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 公开与隐藏划分

官方数据卡为各语言提供 validation/test；full 与 lite 是不同评测规模。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

## 评测方法

### 指标

各语言选择题准确率及跨语言平均。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 评分

提取最终选项并与标准答案比对，逐语言报告。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 提示与生成设置

通过 lm-evaluation-harness 的 mmlu_prox_<lang> 任务评测；README复现要求 vLLM 0.7.3，Llama3.1-405B例外使用0.6.6。

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 脚本

https://github.com/weihao1115/MMLU-ProX

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 可比性警告

full/lite、语言集合及 CoT 策略不同不能混比；官网模型名称未给 API 日期时不得自行补全。

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 对比研究的表1–2和§3.1实际使用 MMLU-ProX，将其纳入13个多选基准的模型评测。

### 数据版本

README 2025-05记录29语言、Full与Lite；2025-08称正在开发更多语言的第二版，不把计划等同已发布。

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 论文修订记录

```json
[
  {
    "version": "v1",
    "submitted_at": "2025-03-14T00:59:20+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2025-05-27T02:20:21+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 饱和情况

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 衍生评测

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日

2026-11-07

[来源1](https://mmluprox.github.io/)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口

https://mmluprox.github.io/

[来源1](https://mmluprox.github.io/)（采集2026-11-07）

### 二级机构榜单

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果

```json
[
  {
    "model": "DeepSeek-R1（官网标签）",
    "score": 75.5,
    "unit": "%",
    "metric": "跨29语言平均 accuracy",
    "scope": "官网 Performance Results 5-shot CoT；并非实时排名服务",
    "evaluation_date": "待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Qwen3-235B-Think（官网标签）",
    "score": 74.9,
    "unit": "%",
    "metric": "跨29语言平均 accuracy",
    "scope": "官网 5-shot CoT",
    "evaluation_date": "待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "GPT-4.1（官网标签）",
    "score": 72.7,
    "unit": "%",
    "metric": "跨29语言平均 accuracy",
    "scope": "官网 5-shot CoT",
    "evaluation_date": "待核实",
    "snapshot_date": "2026-11-07"
  }
]
```

[来源1](https://mmluprox.github.io/)（采集2026-11-07）

### 覆盖与时效限制

官网提供静态结果表，同时标注独立 Leaderboard Coming Soon；采集日可读不代表 2026 年完成的新评测，模型 API 日期未公开于该表。

[来源1](https://mmluprox.github.io/)（采集2026-11-07） [来源2](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱

```json
[
  "irene.li@weblab.t.u-tokyo.ac.jp",
  "weihaoxuan@g.ecc.u-tokyo.ac.jp"
]
```

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

### 仓库讨论与Issues

https://github.com/weihao1115/MMLU-ProX/issues

[来源1](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

### 官方社交渠道

待核实

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2503.10497

[来源1](https://arxiv.org/pdf/2503.10497)（采集2026-11-07）

### 原件SHA-256

b171ff829bfbb567974812dfebb860a63df7f756daf5662c7a1b659df76833bd

[来源1](https://arxiv.org/pdf/2503.10497)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数

```json
730780
```

[来源1](https://arxiv.org/pdf/2503.10497)（采集2026-11-07）

### Drive目录

```json
{
  "id": "1lkm8WYv2rby8F0gpXf1ZMevpAmGW0vk9",
  "webViewLink": "https://drive.google.com/drive/folders/1lkm8WYv2rby8F0gpXf1ZMevpAmGW0vk9"
}
```

[来源1](https://drive.google.com/drive/folders/1lkm8WYv2rby8F0gpXf1ZMevpAmGW0vk9)（采集2026-11-07）

### 中文介绍

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1iI9qctXi6aYW-mS7lXH46jm9PSI0fUQlkF3-W6KeXBE",
    "webViewLink": "https://docs.google.com/document/d/1iI9qctXi6aYW-mS7lXH46jm9PSI0fUQlkF3-W6KeXBE/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1iI9qctXi6aYW-mS7lXH46jm9PSI0fUQlkF3-W6KeXBE/edit?usp=drivesdk)（采集2026-11-07）

### Drive 原始论文归档

```json
{
  "id": "1gohaRGvTuT_OgM7cpG7rgGG4oAjWNDuR",
  "webViewLink": "https://drive.google.com/file/d/1gohaRGvTuT_OgM7cpG7rgGG4oAjWNDuR/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1gohaRGvTuT_OgM7cpG7rgGG4oAjWNDuR/view?usp=drivesdk)（采集2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "第一轮深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。"
  }
]
```

[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07） [来源2](https://arxiv.org/pdf/2503.10497)（采集2026-11-07） [来源3](https://github.com/weihao1115/MMLU-ProX)（采集2026-11-07）

