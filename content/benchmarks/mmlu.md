# MMLU

> 核验：2026-11-07（KST / Asia/Seoul）。基于官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1_7QVvJvbgngMAfsCYTyOLG7QjAa1NbO9/view?usp=drivesdk)

## 基本信息

### 简称

MMLU

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 全称

Massive Multitask Language Understanding

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 基准版本

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本

arXiv v3

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 发布日期

2020-09-07

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块

语言

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签

```json
[
  "多学科知识"
]
```

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 许可证

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文

https://arxiv.org/abs/2009.03300

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 官方代码

https://github.com/hendrycks/test

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 数据地址

https://github.com/hendrycks/test

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 官方入口

https://github.com/hendrycks/test

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 论文标题

Measuring Massive Multitask Language Understanding

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

## 发起与维护

### 机构与作者单位

论文作者单位包括 UC Berkeley、Columbia University、University of Chicago、UIUC；此处记录作者单位，不推断正式机构发起关系。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 正式合作机构

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者

```json
[
  "Hendrycks, Dan",
  "Burns, Collin",
  "Basart, Steven",
  "Zou, Andy",
  "Mazeika, Mantas",
  "Song, Dawn",
  "Steinhardt, Jacob"
]
```

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 当前维护方

官方公开代码托管于 hendrycks；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

### 资助

论文致谢列出 NSF Graduate Research Fellowship、Open Philanthropy AI Fellowship 与 NSF Frontier Award 1804794 等支持。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

## 设计目标

### 测量能力

衡量语言模型在广泛学科中的知识与问题求解能力，而非只在单一任务上训练后评测。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 既有评测缺口

以往语言理解数据集往往狭窄、容易被任务微调或模式匹配攻克；本基准采用跨学科、零样本或少样本测试。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

## 构建方式

### 题目来源

学生贡献者人工搜集网上可自由获取的考试、教材与练习题，覆盖人文、社会科学、STEM 和专业知识。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 出题与标注背景

论文说明题目主要由本科生搜集，并非所有题目均为领域专家原创。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 审核

作者整理各科选择题并形成开发、验证、测试划分；精确的逐题复核职责分配待进一步核实。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 质量控制

各题采用统一的四选一格式；后续 MMLU-Redux 研究仍发现歧义、标注和题目错误，不能视为已完全纠错。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 去污染

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量

共 15,908 题，57 个学科；测试集 14,079 题，验证集 1,540 题，每科 5 道开发示例。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 题型

四选一选择题

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 难度

从基础教育知识到大学及专业资格难度；学科间难度不同。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 公开与隐藏划分

开发示例、验证集、测试集均公开；不要把各划分混合评测。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

## 评测方法

### 指标

选择题准确率，按任务汇总。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 评分

原始实验比较 A、B、C、D 选项的模型概率，取概率最高的选项。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 提示与生成设置

原始论文报告零样本、少样本等设置；标准少样本使用每科 5 道开发题。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 脚本

https://github.com/hendrycks/test

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

### 可比性警告

零样本、5-shot、CoT、学科宏平均与题目微平均不可不加标记地混比；MMLU 与其纠错/扩展/翻译版本也不同。

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 对比研究的表1–2和§3.1实际使用 MMLU，将其纳入13个多选基准的模型评测。

### 数据版本

待核实

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录

```json
[
  {
    "version": "v1",
    "submitted_at": "2020-09-08T02:59:25+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2020-09-21T14:06:57+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2021-01-13T03:57:11+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

### 饱和情况

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题

MMLU-Pro 与 MMLU-Redux 的原始研究分别指出简单题、噪声与标签错误；错误率随学科变化，不应把局部抽样错误率外推到全部题目。

[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 衍生评测

```json
[
  "MMLU-Pro",
  "MMLU-Redux",
  "MMMLU"
]
```

[来源1](https://arxiv.org/abs/2610.11978)（采集2026-11-07）

## 榜单快照

### 采集日

2026-11-07

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口

https://github.com/hendrycks/test#test-leaderboard

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

### 二级机构榜单

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果

```json
[
  {
    "model": "Chinchilla",
    "score": 67.5,
    "unit": "%",
    "metric": "Average accuracy",
    "scope": "官方 README 当前可读历史榜；不是2026最新模型实力排名",
    "model_setting": "70B few-shot",
    "leaderboard_updated_at": "待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Gopher",
    "score": 60.0,
    "unit": "%",
    "metric": "Average accuracy",
    "scope": "官方 README 当前可读历史榜；不是2026最新模型实力排名",
    "model_setting": "280B few-shot",
    "leaderboard_updated_at": "待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "GPT-3",
    "score": 53.9,
    "unit": "%",
    "metric": "Average accuracy",
    "scope": "官方 README 当前可读历史榜；不是2026最新模型实力排名",
    "model_setting": "175B fine-tuned",
    "leaderboard_updated_at": "待核实",
    "snapshot_date": "2026-11-07"
  }
]
```

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

### 覆盖与时效限制

以官方 README 可读表替代非官方研究比较表作为本栏快照；榜单未给统一更新日期，模型年代和提示协议不同，禁止视为2026前沿排名。

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 仓库讨论与Issues

https://github.com/hendrycks/test/issues

[来源1](https://github.com/hendrycks/test)（采集2026-11-07）

### 官方社交渠道

待核实

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2009.03300

[来源1](https://arxiv.org/pdf/2009.03300)（采集2026-11-07）

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
  "id": "16jdkBY7vMWPeny-ZoCn5i4limN90OF26",
  "webViewLink": "https://drive.google.com/drive/folders/16jdkBY7vMWPeny-ZoCn5i4limN90OF26"
}
```

[来源1](https://drive.google.com/drive/folders/16jdkBY7vMWPeny-ZoCn5i4limN90OF26)（采集2026-11-07）

### 中文介绍

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "10X_jNgeT4GCIeP3q17ZGinf7YmmYmD1g4wxlM6aLIOc",
    "webViewLink": "https://docs.google.com/document/d/10X_jNgeT4GCIeP3q17ZGinf7YmmYmD1g4wxlM6aLIOc/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/10X_jNgeT4GCIeP3q17ZGinf7YmmYmD1g4wxlM6aLIOc/edit?usp=drivesdk)（采集2026-11-07）

### Drive 原始论文归档

```json
{
  "id": "1_7QVvJvbgngMAfsCYTyOLG7QjAa1NbO9",
  "webViewLink": "https://drive.google.com/file/d/1_7QVvJvbgngMAfsCYTyOLG7QjAa1NbO9/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1_7QVvJvbgngMAfsCYTyOLG7QjAa1NbO9/view?usp=drivesdk)（采集2026-11-07）

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

[来源1](https://arxiv.org/abs/2009.03300)（采集2026-11-07） [来源2](https://arxiv.org/pdf/2009.03300)（采集2026-11-07） [来源3](https://github.com/hendrycks/test)（采集2026-11-07）

