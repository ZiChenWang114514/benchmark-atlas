# IFEval

> 核验：2026-11-07（KST / Asia/Seoul）。基于官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1Nsrlsk4-LLFXvYCvPbWzRa7hHw_ZdJlM/view?usp=drivesdk)

## 基本信息

### 简称

IFEval

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 全称

Instruction-Following Evaluation

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 基准版本

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本

arXiv v1

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 发布日期

2023-11-14

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块

语言

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签

```json
[
  "可验证指令遵循"
]
```

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 许可证

评测源码 Apache-2.0；数据再分发权利不由代码文件头单独证明。

[来源1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/evaluation_main.py)（采集2026-11-07）

### 论文

https://arxiv.org/abs/2311.07911

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 官方代码

https://github.com/google-research/google-research/tree/master/instruction_following_eval

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 数据地址

https://github.com/google-research/google-research/tree/master/instruction_following_eval

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 官方入口

https://github.com/google-research/google-research/tree/master/instruction_following_eval

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 论文标题

Instruction-Following Evaluation for Large Language Models

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

## 发起与维护

### 机构与作者单位

Google Research 研究团队；Jeffrey Zhou 的研究实习与 Yale 背景在论文说明。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 正式合作机构

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者

```json
[
  "Zhou, Jeffrey",
  "Lu, Tianjian",
  "Mishra, Swaroop",
  "Brahma, Siddhartha",
  "Basu, Sujoy",
  "Luan, Yi",
  "Zhou, Denny",
  "Hou, Le"
]
```

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 当前维护方

官方公开代码托管于 google-research；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源1](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（采集2026-11-07）

### 资助

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力

通过可程序验证的约束客观评估指令遵循。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 既有评测缺口

人工评测昂贵，模型裁判可能受偏差影响；需要可重复、确定性检查的指令。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

## 构建方式

### 题目来源

合成基础提示并添加 1–3 个可验证约束，再移除不合理组合及重写提示。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 出题与标注背景

研究团队设计约束与提示；不依赖领域知识考试出题。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 审核

人工检查全部提示，修正不自然或冲突约束。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 质量控制

同时报告严格和宽松判定；宽松版本处理格式等变换，但可能增加假阳性。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 去污染

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量

541 条提示，25 类可验证指令。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 题型

带输出长度、关键词、格式等约束的开放文本生成

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 难度

约束类型及同一提示中的组合增加难度；不是学科知识难度分层。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 公开与隐藏划分

官方公开提示数据和验证程序；未核实独立隐藏测试集。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

## 评测方法

### 指标

prompt-level strict/loose accuracy 与 instruction-level strict/loose accuracy。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 评分

官方主程序分别调用 strict 与 loose 校验，输出两套JSONL；prompt级准确率为全部指令均通过的回答比例，不应与单条指令通过率混淆。

[来源1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/evaluation_main.py)（采集2026-11-07）

### 提示与生成设置

按原提示生成回答后调用官方检查器；不要把评分用文本清洗当作模型真正满足原格式。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 脚本

google-research/instruction_following_eval/evaluation_main.py；输入原始指令JSONL及含prompt、response的模型响应JSONL。

[来源1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/README.md)（采集2026-11-07）

### 可比性警告

prompt-level 与 instruction-level、strict 与 loose 是四种不同指标，分数必须指明；宽松清洗也有假阳性风险。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-09-23：Hunyuan-A13B §4.2–4.3实际使用 IFEval 并报告结果；厂商自报，需保留各基准的提示/上下文条件。

### 数据版本

待核实

[来源1](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录

```json
[
  {
    "version": "v1",
    "submitted_at": "2023-11-14T14:13:55+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 饱和情况

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题

可程序验证的约束只覆盖部分真实指令能力；严格/宽松结果不等价，不能把格式容错理解为全面遵循。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 衍生评测

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日

2026-11-07

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口

https://arxiv.org/abs/2311.07911

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果

```json
[
  {
    "model": "Hunyuan-A13B（报告命名）",
    "score": 84.7,
    "unit": "%",
    "metric": "IF-Eval，报告表3原标签",
    "scope": "Hunyuan-A13B 技术报告，slow-thinking；厂商自报，未明确对应本条四指标中的哪一个，不能与论文 prompt-strict 直接混比",
    "evaluation_date": "报告日期2026-09-23；精确运行日期待核实",
    "snapshot_date": "2026-11-07"
  }
]
```

[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

### 覆盖与时效限制

仅收录H2技术报告中明确可读的厂商自报成绩；模型标签按报告保留，未核实其精确API运行日期。不能把这些成绩冒充独立机构当前排行榜。

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07） [来源2](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱

```json
[
  "lehou@google.com"
]
```

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

### 仓库讨论与Issues

https://github.com/google-research/google-research/issues

[来源1](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（采集2026-11-07）

### 官方社交渠道

待核实

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2311.07911

[来源1](https://arxiv.org/pdf/2311.07911)（采集2026-11-07）

### 原件SHA-256

5d7cedfd762af6d9ad13d8768de64fa65895b8ebc3f5e454454c5ffbd48124f2

[来源1](https://arxiv.org/pdf/2311.07911)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数

```json
464152
```

[来源1](https://arxiv.org/pdf/2311.07911)（采集2026-11-07）

### Drive目录

```json
{
  "id": "1USyTVejz1q3o4ZVbGwBQVt4QDHXw0PJZ",
  "webViewLink": "https://drive.google.com/drive/folders/1USyTVejz1q3o4ZVbGwBQVt4QDHXw0PJZ"
}
```

[来源1](https://drive.google.com/drive/folders/1USyTVejz1q3o4ZVbGwBQVt4QDHXw0PJZ)（采集2026-11-07）

### 中文介绍

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1EXunkoRqRKfRFViKuCIvLaQwApjkiWauYh-NTkz-9iU",
    "webViewLink": "https://docs.google.com/document/d/1EXunkoRqRKfRFViKuCIvLaQwApjkiWauYh-NTkz-9iU/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1EXunkoRqRKfRFViKuCIvLaQwApjkiWauYh-NTkz-9iU/edit?usp=drivesdk)（采集2026-11-07）

### Drive 原始论文归档

```json
{
  "id": "1Nsrlsk4-LLFXvYCvPbWzRa7hHw_ZdJlM",
  "webViewLink": "https://drive.google.com/file/d/1Nsrlsk4-LLFXvYCvPbWzRa7hHw_ZdJlM/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1Nsrlsk4-LLFXvYCvPbWzRa7hHw_ZdJlM/view?usp=drivesdk)（采集2026-11-07）

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

[来源1](https://arxiv.org/abs/2311.07911)（采集2026-11-07） [来源2](https://arxiv.org/pdf/2311.07911)（采集2026-11-07） [来源3](https://github.com/google-research/google-research/tree/master/instruction_following_eval)（采集2026-11-07）

