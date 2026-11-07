# C-Eval

> 核验：2026-11-07（KST / Asia/Seoul）。基于官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1srG6OgvEUfLf4iJVtskBpRJCvr3rkoQ0/view?usp=drivesdk)

## 基本信息

### 简称

C-Eval

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 全称

Chinese Evaluation Suite for Foundation Models

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 基准版本

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本

arXiv v3

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 发布日期

2023-05-15

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块

语言

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签

```json
[
  "中文多学科知识"
]
```

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 许可证

代码 MIT；数据集 CC BY-NC-SA 4.0，二者不可混用。

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 论文

https://arxiv.org/abs/2305.08322

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 官方代码

https://github.com/hkust-nlp/ceval

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 数据地址

https://github.com/hkust-nlp/ceval

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 官方入口

https://cevalbenchmark.com

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 论文标题

C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

## 发起与维护

### 机构与作者单位

论文作者单位包括上海交通大学、清华大学、爱丁堡大学、香港科技大学；作者贡献说明由 Junxian He 发起并组织。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 正式合作机构

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者

```json
[
  "Huang, Yuzhen",
  "Bai, Yuzhuo",
  "Zhu, Zhihao",
  "Zhang, Junlei",
  "Zhang, Jinghan",
  "Su, Tangjun",
  "Liu, Junteng",
  "Lv, Chuancheng",
  "Zhang, Yikai",
  "Lei, Jiayi",
  "Fu, Yao",
  "Sun, Maosong",
  "He, Junxian"
]
```

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 当前维护方

官方公开代码托管于 hkust-nlp；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 资助

论文致谢中列出 National Key R&D Program of China 2020AAA0106502、清华大学 Guo Qiang Institute 等作者资助。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

## 设计目标

### 测量能力

衡量基础模型对中文环境中多层次、多学科知识的理解及推理。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 既有评测缺口

英语中心评测不足以代表中文教育与专业知识掌握；翻译英语题也不能覆盖中文课程背景。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

## 构建方式

### 题目来源

模拟和地方考试的 PDF/Word、部分大学期末题，以及约 2,000 道获授权的维普题目。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 出题与标注背景

作者组织学科相关学生与研究者搜集、编辑并核验中文考试题。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 审核

文档解析、人工修正格式与 LaTeX，作者交叉验证题干及答案。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 质量控制

去重并检查格式，尽量避开可能泄漏的全国统一考试题；不等于能保证模型训练无污染。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 去污染

通过题源选择规避部分流行公开试题，并去重；没有证据能保证所有被测模型训练语料完全不含这些题。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

## 数据形式

### 题量

共13,948题，52学科，四种难度；验证集1,346题，每科5道开发示例。

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 题型

四选一选择题

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 语言

中文

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 难度

初中、高中、大学及专业资格四层级。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 公开与隐藏划分

每科 dev 5题、val 用于调参、test 用于评测。README 新闻称2025-07-27完整测试集已公开，但旧 Data 段仍说test标签不公开；存在文档时效冲突，不能继续一概称隐藏测试。

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

## 评测方法

### 指标

准确率；官方论文按学科/类别汇总，需记录平均方式。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 评分

通常从生成内容提取 A/B/C/D；不遵循格式时可比较四选项概率。概率法不适用于CoT；零样本、五样本和CoT分开记录。

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 提示与生成设置

原论文包含 0-shot/5-shot answer-only 与 5-shot CoT；不要混在同一排序。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 脚本

https://github.com/hkust-nlp/ceval

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 可比性警告

C-Eval 的中文原生试题与翻译版 MMLU 不同；隐藏测试、验证集、5-shot、CoT 与平均方式都必须标注。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据

2026-11-07

[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 对比研究的表1–2和§3.1实际使用 C-Eval，将其纳入13个多选基准的模型评测。

### 数据版本

官方 README 新闻记录：2025-07-27完整测试集向社区发布。

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 论文修订记录

```json
[
  {
    "version": "v1",
    "submitted_at": "2023-05-15T12:20:19+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2023-05-17T10:11:35+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2023-11-06T22:24:16+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 饱和情况

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 衍生评测

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日

2026-11-07

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口

https://cevalbenchmark.com/static/leaderboard.html

[来源1](https://cevalbenchmark.com/static/leaderboard.html)（采集2026-11-07）

### 二级机构榜单

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果

```json
[
  {
    "model": "GPT-4（原论文标签）",
    "score": 68.7,
    "unit": "%",
    "metric": "accuracy",
    "scope": "原论文历史 5-shot answer-only；精确 API 快照待核实",
    "evaluation_date": "2023年原论文实验，精确日期待核实"
  }
]
```

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 覆盖与时效限制

官方榜单地址已确认，但本次 HTTPS 证书过期且网页抓取返回错误，未声称取得当前榜首；只列清楚标记的论文历史结果。

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07） [来源2](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱

```json
[
  "ceval.benchmark@gmail.com"
]
```

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

### 仓库讨论与Issues

https://github.com/hkust-nlp/ceval/issues

[来源1](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

### 官方社交渠道

待核实

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF

https://arxiv.org/pdf/2305.08322

[来源1](https://arxiv.org/pdf/2305.08322)（采集2026-11-07）

### 原件SHA-256

88bfbd09fe554fc40538cb84fcff09681b86ff5c71398fd4b9beaf177d73acde

[来源1](https://arxiv.org/pdf/2305.08322)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数

```json
5123072
```

[来源1](https://arxiv.org/pdf/2305.08322)（采集2026-11-07）

### Drive目录

```json
{
  "id": "1XiWWm6Qf9bvl231PZpVGtu_Hv4dqxsKM",
  "webViewLink": "https://drive.google.com/drive/folders/1XiWWm6Qf9bvl231PZpVGtu_Hv4dqxsKM"
}
```

[来源1](https://drive.google.com/drive/folders/1XiWWm6Qf9bvl231PZpVGtu_Hv4dqxsKM)（采集2026-11-07）

### 中文介绍

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1y4w791Z01asAIi1Wr1sXOI5O2ikd4pzprPPrDB2gLHY",
    "webViewLink": "https://docs.google.com/document/d/1y4w791Z01asAIi1Wr1sXOI5O2ikd4pzprPPrDB2gLHY/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1y4w791Z01asAIi1Wr1sXOI5O2ikd4pzprPPrDB2gLHY/edit?usp=drivesdk)（采集2026-11-07）

### Drive 原始论文归档

```json
{
  "id": "1srG6OgvEUfLf4iJVtskBpRJCvr3rkoQ0",
  "webViewLink": "https://drive.google.com/file/d/1srG6OgvEUfLf4iJVtskBpRJCvr3rkoQ0/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1srG6OgvEUfLf4iJVtskBpRJCvr3rkoQ0/view?usp=drivesdk)（采集2026-11-07）

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

[来源1](https://arxiv.org/abs/2305.08322)（采集2026-11-07） [来源2](https://arxiv.org/pdf/2305.08322)（采集2026-11-07） [来源3](https://github.com/hkust-nlp/ceval)（采集2026-11-07）

