# C-Eval

> Benchmark Constitution，深度复核：2026-11-08。官方证据复核完成；2026-H2使用证据已回读；未知字段和文档冲突显式保留

C-Eval以中文原生教育与资格考试背景衡量52个学科的知识和推理，跨初中、高中、大学与专业层级。它不是将英语MMLU简单翻译成中文。读分数必须先问：test还是val、零样本还是五样本、直接作答还是CoT？官方已于2025-07-27公开完整test，旧文档的隐藏标签说法不能继续无条件沿用。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

## 基本信息

### 简称

C-Eval

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 全称

Chinese Evaluation Suite for Foundation Models

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 版本边界

待核实

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本

arXiv v3

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 发布日期

2023-05-15

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 板块

语言

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域

```json
[
  "中文多学科知识"
]
```

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 许可与限制

代码 MIT；数据集 CC BY-NC-SA 4.0，二者不可混用。

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2305.08322

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 官方代码

https://github.com/hkust-nlp/ceval

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 数据入口

https://huggingface.co/datasets/ceval/ceval-exam

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/ceval/ceval-exam/blob/main/README.md)（访问2026-11-08）

### 官方主页

https://cevalbenchmark.com

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 论文题名

C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

## 发起与维护

### 发起方

论文作者单位包括上海交通大学、清华大学、爱丁堡大学、香港科技大学；作者贡献说明由 Junxian He 发起并组织。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 合作机构

待核实

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者

```json
[
  "Huang, Yuzhen"
  "Bai, Yuzhuo"
  "Zhu, Zhihao"
  "Zhang, Junlei"
  "Zhang, Jinghan"
  "Su, Tangjun"
  "Liu, Junteng"
  "Lv, Chuancheng"
  "Zhang, Yikai"
  "Lei, Jiayi"
  "Fu, Yao"
  "Sun, Maosong"
  "He, Junxian"
]
```

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 维护入口

官方公开代码托管于 hkust-nlp；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 资助披露

论文致谢中列出 National Key R&D Program of China 2020AAA0106502、清华大学 Guo Qiang Institute 等作者资助。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

## 设计目标

### 测量对象

衡量基础模型对中文环境中多层次、多学科知识的理解及推理。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 既有评测的缺口

英语中心评测不足以代表中文教育与专业知识掌握；翻译英语题也不能覆盖中文课程背景。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

## 构建方式

### 题源

模拟和地方考试的 PDF/Word、部分大学期末题，以及约 2,000 道获授权的维普题目。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 构建人员

作者组织学科相关学生与研究者搜集、编辑并核验中文考试题。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 审核

文档解析、人工修正格式与 LaTeX，作者交叉验证题干及答案。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 质控

去重并检查格式，尽量避开可能泄漏的全国统一考试题；不等于能保证模型训练无污染。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 去污染及边界

通过题源选择规避部分流行公开试题，并去重；没有证据能保证所有被测模型训练语料完全不含这些题。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

## 数据形式

### 规模与计数口径

共13,948题，52学科，四种难度；验证集1,346题，每科5道开发示例。

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 题型

四选一选择题

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 语言

中文

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 难度

初中、高中、大学及专业资格四层级。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 划分与公开范围

每科 dev 5题、val 用于调参、test 用于评测。README 新闻称2025-07-27完整测试集已公开，但旧 Data 段仍说test标签不公开；存在文档时效冲突，不能继续一概称隐藏测试。

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

## 评测方法

### 指标

准确率；官方论文按学科/类别汇总，需记录平均方式。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 评分

通常从生成内容提取 A/B/C/D；不遵循格式时可比较四选项概率。概率法不适用于CoT；零样本、五样本和CoT分开记录。

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 提示与运行条件

原论文包含 0-shot/5-shot answer-only 与 5-shot CoT；不要混在同一排序。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 官方评测入口

https://github.com/hkust-nlp/ceval

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 可比性边界

C-Eval 的中文原生试题与翻译版 MMLU 不同；隐藏测试、验证集、5-shot、CoT 与平均方式都必须标注。

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

## 最新情况

### 复核时间

2026-11-08

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-08）

### 当前版本

官方 README 新闻记录：2025-07-27完整测试集向社区发布。

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 论文修订与后续使用

```json
{
  "arxiv_revisions_kst": [
    {
      "version": "v1"
      "submitted_at_kst": "2023-05-15"
    }
    {
      "version": "v2"
      "submitted_at_kst": "2023-05-17"
    }
    {
      "version": "v3"
      "submitted_at_kst": "2023-11-06"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-08）

### 饱和情况

待核实

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 风险与冲突

官方README与HF卡2025-07-27公告完整test已公开，旧Data段“标签不公开”是文档时效冲突；公开标签后继续关注污染。题源规避和去重不能证明所有被测模型训练无泄漏。

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/ceval/ceval-exam/blob/main/README.md)（访问2026-11-08）

### 衍生与后续工作

C-Eval Hard：8个数学、物理、化学高推理学科组成的固定子集；不将其与全52学科平均准确率混为一个指标。

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问2026-11-08）

## 榜单快照

### 快照时间

2026-11-08 （实际复核日；批次标签2026-11-07）

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-08）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜入口

https://cevalbenchmark.com/static/leaderboard.html

[来源1](https://cevalbenchmark.com/static/leaderboard.html)（访问2026-11-07）

### 第三方榜入口

待核实

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 逐轨结果

```json
[
  {
    "rank": 1
    "model": "GPT-4"
    "score": 66.4
    "metric": "average accuracy (%)"
    "track": "原版test／0-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 2
    "model": "ChatGPT"
    "score": 51.0
    "metric": "average accuracy (%)"
    "track": "原版test／0-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 3
    "model": "Claude-v1.3"
    "score": 50.5
    "metric": "average accuracy (%)"
    "track": "原版test／0-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": 68.7
    "metric": "average accuracy (%)"
    "track": "原版test／5-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 2
    "model": "ChatGPT"
    "score": 54.4
    "metric": "average accuracy (%)"
    "track": "原版test／5-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 3
    "model": "Claude-v1.3"
    "score": 54.2
    "metric": "average accuracy (%)"
    "track": "原版test／5-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": 69.9
    "metric": "average accuracy (%)"
    "track": "validation／5-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 2
    "model": "Claude-v1.3"
    "score": 55.5
    "metric": "average accuracy (%)"
    "track": "validation／5-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
  {
    "rank": 3
    "model": "ChatGPT"
    "score": 53.5
    "metric": "average accuracy (%)"
    "track": "validation／5-shot answer-only／README历史"
    "source_url": "https://github.com/hkust-nlp/ceval/blob/main/README.md"
    "accessed": "2026-11-08"
    "unit": "%"
    "model_snapshot": "待核实"
    "evaluation_date": "待核实"
  }
]
```

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问2026-11-08）

### 覆盖边界

官方实时榜本次WebFetch返回500，直接HTTPS读取证书验证失败，未绕过证书检查；只更新可直接核验的README历史test零/五样本及val五样本三轨，不能宣称2026实时前三。

[来源1](https://github.com/hkust-nlp/ceval/blob/main/README.md)（访问2026-11-08）；[来源2](https://cevalbenchmark.com/static/leaderboard.html)（访问2026-11-08）

## 联系方式

### 公开研究联系

```json
[
  "ceval.benchmark@gmail.com"
]
```

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

### 项目反馈

https://github.com/hkust-nlp/ceval/issues

[来源1](https://github.com/hkust-nlp/ceval)（访问2026-11-07）

### 官方社交入口

待核实

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 联系信息边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-07）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2305.08322

[来源1](https://arxiv.org/pdf/2305.08322)（访问2026-11-07）

### PDF SHA-256

88bfbd09fe554fc40538cb84fcff09681b86ff5c71398fd4b9beaf177d73acde

[来源1](https://arxiv.org/pdf/2305.08322)（访问2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### PDF字节数

5123072

[来源1](https://arxiv.org/pdf/2305.08322)（访问2026-11-07）

### 目录

```json
{
  "id": "1XiWWm6Qf9bvl231PZpVGtu_Hv4dqxsKM"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
[
  {
    "kind": "中文介绍"
    "id": "1y4w791Z01asAIi1Wr1sXOI5O2ikd4pzprPPrDB2gLHY"
    "webViewLink": "
  }
]
```

[来源1](

### 论文归档

```json
{
  "id": "1srG6OgvEUfLf4iJVtskBpRJCvr3rkoQ0"
  "webViewLink": "
}
```

[来源1](

## 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]
```

[来源1](https://arxiv.org/abs/2305.08322)（访问2026-11-08）；[来源2](https://arxiv.org/pdf/2305.08322)（访问2026-11-08）；[来源3](https://github.com/hkust-nlp/ceval)（访问2026-11-08）
