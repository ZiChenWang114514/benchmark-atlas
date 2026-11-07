# MMMLU

> 核验：2026-11-07（KST / Asia/Seoul）。基于官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/10nTX-hZcL0fXPaatAK5f_f47-_-daG2g/view?usp=drivesdk)

## 基本信息

### 简称

MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 全称

Multilingual Massive Multitask Language Understanding

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 基准版本

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 发布日期

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 主板块

语言

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签

```json
[
  "多语言多学科知识"
]
```

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 许可证

MIT（OpenAI 官方数据集卡声明）

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 论文

https://arxiv.org/abs/2009.03300

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07） [来源2](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 所附为数据卡引用的 MMLU 原始论文，非 MMMLU 独立论文。

### 官方代码

https://github.com/openai/simple-evals

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 数据地址

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 官方入口

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 论文标题

Measuring Massive Multitask Language Understanding

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 所附为数据卡引用的 MMLU 原始论文，非 MMMLU 独立论文。

## 发起与维护

### 机构与作者单位

OpenAI 官方数据集。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 正式合作机构

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> MMMLU数据卡未核实个人作者；不能把MMLU原始论文作者当成翻译数据集作者。

### 当前维护方

OpenAI（官方数据发布命名空间 openai/MMMLU）

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 资助

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力

通过专业人工翻译检验多语言的一般知识能力，尤其关注低资源语言翻译质量。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 既有评测缺口

只测英语无法反映跨语言表现；机器翻译题的质量可能影响低资源语种测评。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

## 构建方式

### 题目来源

原始 MMLU 测试集的14种语言专业人工翻译，覆盖原MMLU的57学科。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 出题与标注背景

由专业人工译者翻译 MMLU 测试集，不是机器翻译版本。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 审核

通过专业人工翻译提高题目语义准确性；完整逐题复审分工待核实。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 质量控制

跨语种基于同一 MMLU 测试题集，适合比较知识迁移；不能消除原始 MMLU 题目错误。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 去污染

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量

14 个翻译语种、57 类学科；独立题目精确数量本次待核实，不能把数据查看器的合并/重复行数当成原题数。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 题型

四选一知识题

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 模态

文本

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 语言

```json
[
  "阿拉伯语",
  "孟加拉语",
  "德语",
  "西班牙语",
  "法语",
  "印地语",
  "印度尼西亚语",
  "意大利语",
  "日语",
  "韩语",
  "巴西葡萄牙语",
  "斯瓦希里语",
  "约鲁巴语",
  "简体中文"
]
```

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 难度

沿用 MMLU，从基础到专业学科；翻译不是新难度等级。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 公开与隐藏划分

官方卡列出14个语言配置，均为公开test/*.csv测试文件；不将这些test文件当训练集。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

## 评测方法

### 指标

选择题准确率，需标明语言与跨语种汇总方法。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 评分

官方链接 OpenAI simple-evals；具体采样与答案抽取版本应固定到代码提交。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 提示与生成设置

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 脚本

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（采集2026-11-07）

### 可比性警告

MMMLU 是 OpenAI 对 MMLU 的专业人工翻译数据集，不是 MMLU-ProX；14 个翻译语种不应被误写为包含原英语的14语种。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 对比研究的表1–2和§3.1实际使用 MMMLU，将其纳入13个多选基准的模型评测。

### 数据版本

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 饱和情况

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题

数据卡只链接 MMLU 原始论文，尚未确认 MMMLU 独立论文。本目录 PDF 明确标注为 MMLU 原始论文，不能把其作者、首发日期和实验成绩写作 MMMLU 的。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

### 衍生评测

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日

2026-11-07

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果

```json
[
  {
    "model": "Gemini 3.8 Flash（研究表2原标签）",
    "score": 92.6,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Qwen3.8-Max（研究表2原标签）",
    "score": 90.3,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "DeepSeek-V4.1-Flash（研究表2原标签）",
    "score": 88.8,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  }
]
```

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

### 覆盖与时效限制

H2对比研究可读结果；保留论文模型标签，未核实精确API日期，不将混合提示或历史引用成绩都视为同协议。未核实当前官方统一实时榜和AA/Epoch/LMArena对应独立单项榜。

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07） [来源2](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 仓库讨论与Issues

https://github.com/openai/simple-evals/issues

[来源1](https://github.com/openai/simple-evals)（采集2026-11-07）

### 官方社交渠道

待核实

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2009.03300

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07） [来源2](https://arxiv.org/pdf/2009.03300)（采集2026-11-07）

> 所附为数据卡引用的 MMLU 原始论文，非 MMMLU 独立论文。

### 原件SHA-256

d3a7b0f8589f5365ebfd34a3876a9a8b3fde83e0adb9ed19ccf8f0034bb48fc1

[来源1](https://arxiv.org/pdf/2009.03300)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数

```json
2074939
```

[来源1](https://arxiv.org/pdf/2009.03300)（采集2026-11-07）

### Drive目录

```json
{
  "id": "1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC",
  "webViewLink": "https://drive.google.com/drive/folders/1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC"
}
```

[来源1](https://drive.google.com/drive/folders/1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC)（采集2026-11-07）

### 中文介绍

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g",
    "webViewLink": "https://docs.google.com/document/d/1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g/edit?usp=drivesdk)（采集2026-11-07）

### Drive 原始论文归档

```json
{
  "id": "10nTX-hZcL0fXPaatAK5f_f47-_-daG2g",
  "webViewLink": "https://drive.google.com/file/d/10nTX-hZcL0fXPaatAK5f_f47-_-daG2g/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/10nTX-hZcL0fXPaatAK5f_f47-_-daG2g/view?usp=drivesdk)（采集2026-11-07）

> 所附为数据卡引用的 MMLU 原始论文，非 MMMLU 独立论文。

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

[来源1](https://huggingface.co/datasets/openai/MMMLU)（采集2026-11-07） [来源2](https://arxiv.org/pdf/2009.03300)（采集2026-11-07） [来源3](https://github.com/openai/simple-evals)（采集2026-11-07）

