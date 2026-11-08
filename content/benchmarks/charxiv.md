# CharXiv

> Benchmark Constitution，深度复核：2026-11-08。已重新检索官方材料；历史榜单/当前快照/厂商自报分离；未实证字段保留待核实

CharXiv从科研论文中挑选自然复杂图表，分别考查描述性元素识别和跨视觉元素推理。每图四道描述题、一道人类审核的推理题；推理题可从GPT-4V候选中选改，不是所有初稿都纯人工原创。官网CSV有两列Overall，分别对应reasoning与descriptive，必须拆为两条榜；公开val与隐藏test答案也不能混用。

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

## 基本信息

### 简称

CharXiv

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 全称

CharXiv

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 版本边界

v1.0

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 论文版本

arXiv v1

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 发布日期

2024-06-27 02:50:11 （arXiv v1；原站日历日期2024-06-26）

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-08）

### 板块

多模态

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

> Benchmark Atlas编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

### 领域

```json
[
  "真实科研图表理解"
]
```

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 许可与限制

原创问答CC BY-SA 4.0，代码Apache-2.0；图表版权属原作者。官方HF卡另声明仅用于评测，不允许用于训练，需同时审阅这些使用限制。

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2406.18521

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 官方代码

https://github.com/princeton-nlp/CharXiv

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 数据入口

https://huggingface.co/datasets/princeton-nlp/CharXiv

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/princeton-nlp/CharXiv)（访问2026-11-07）

### 官方主页

https://charxiv.github.io/

[来源1](https://charxiv.github.io/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 论文题名

CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

## 发起与维护

### 发起方

Princeton Language and Intelligence（普林斯顿大学）主导作者团队，合作作者单位含威斯康星大学麦迪逊分校、香港大学。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### 合作机构

```json
[
  "Princeton Language and Intelligence (PLI), Princeton University"
  "University of Wisconsin–Madison"
  "The University of Hong Kong"
]
```

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### 作者

```json
[
  "Wang, Zirui"
  "Xia, Mengzhou"
  "He, Luxi"
  "Chen, Howard"
  "Liu, Yitao"
  "Zhu, Richard"
  "Liang, Kaiqu"
  "Wu, Xindi"
  "Liu, Haotian"
  "Malladi, Sadhika"
  "Chevalier, Alexis"
  "Arora, Sanjeev"
  "Chen, Danqi"
]
```

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）

### 维护入口

princeton-nlp / CharXiv作者团队；官方README欢迎Issue/PR，并由Zirui Wang接收数据构建脚本咨询。

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 资助披露

Microsoft Accelerate Foundation Models Academic Research Initiative；作者个人支持另含Apple Scholars in AIML Fellowship、Gordon Wu Fellowship。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

## 设计目标

### 测量对象

真实科研图表的基础元素识别与跨复杂视觉元素的综合推理。

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### 既有评测的缺口

同质化图表和模板问题会高估模型能力；科研原生图表包含更丰富的结构与视觉变化。

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

## 构建方式

### 题源

从arXiv八大学科论文中人工挑选图表，设计描述型与推理型问题；部分推理题为GPT生成或启发后经人工筛选与验证，非全部纯人工初稿。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### 构建人员

推理题标注员为研究生；每图先看GPT-4V生成的10组候选QA，再选取、编辑或自行撰题；不把所有初稿称为纯人工专家原创。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-08）

### 审核

所有图表、问题经人类专家挑选、整理、验证；描述题聚焦基本元素，推理题需整合图内信息。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 质控

所有图表、问题经人类专家挑选、整理、验证；描述题聚焦基本元素，推理题需整合图内信息。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源3](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

> HF数据卡另有公开Erratum：0.jpg推理答案错误；不能因为专家人工审核就宣称零标注错误。

### 去污染及边界

test答案刻意设为null而不公开，避免测试答案泄漏；论文datasheet同时承认图表可能与SciCap、SciGraphQA、Multimodal Arxiv有重叠，不能保证图像未进入预训练。

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

## 数据形式

### 规模与计数口径

```json
{
  "charts": 2323
  "descriptive_questions": 9292
  "reasoning_questions": 2323
  "validation_charts": 1000
  "test_charts": 1323
  "documentation_conflict": "README导览另写2333 images，与论文Table 2和README主体2323不一致，保留冲突。"
}
```

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-08）；[来源2](https://github.com/princeton-nlp/CharXiv)（访问2026-11-08）

### 题型

descriptive与reasoning开放问答；验证集1,000图表、5,000问题。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 模态

图像+文本

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

### 语言

English（官方HF数据卡language: en）；这是官方语言标注，不推断图中所有原论文文本的语言比例。

[来源1](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

### 难度

来自八大学科的自然复杂图表；无本批核实的统一易中难分布。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 划分与公开范围

按图表随机分为val 1000与test 1323；val公开完整5,000个QA，test答案在公开JSON置null。以图表为划分单位，不将1,323写成测试问题总量。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-08）；[来源2](https://github.com/princeton-nlp/CharXiv)（访问2026-11-08）

## 评测方法

### 指标

GPT-4o判定答案，聚合描述与推理正确率；两种分数不混并。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 评分

GPT-4o判定答案，聚合描述与推理正确率；两种分数不混并。

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 提示与运行条件

zero-shot，按问题类别自然指令；官方脚本分别生成、评分、汇总，需记录grader模型快照。

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### 官方评测入口

https://github.com/princeton-nlp/CharXiv

[来源1](https://github.com/princeton-nlp/CharXiv)（访问2026-11-07）

### 可比性边界

官方CSV与README榜单都可能为历史结果；MMVistaReason的CharXiv reas.是另一研究的CompassVerifier协议，不是官方榜单刷新。

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源3](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）

## 最新情况

### 复核时间

2026-11-08

[来源1](https://charxiv.github.io/)（访问2026-11-08）

### 当前版本

v1.0

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

### 论文修订与后续使用

```json
{
  "revisions": [
    {
      "version": "v1"
      "date_kst": "2024-06-27"
    }
  ]
  "continued_use_2026h2": [
    {
      "url": "https://arxiv.org/html/2610.01352v2"
      "date": "2026-10-23"
      "note": "MMVistaReason v2 §4.1及表2实际评测 CharXiv（reasoning设置），比较4B/9B及其他视觉语言模型；不把mini/val等划分另计。"
      "date_kst": "2026-10-23"
      "verified_in_round1": "重新打开arXiv v2正文§4.1/Table2与abs提交历史，确认实际评测；源站v2为2026-10-22 16:54:37 UTC。"
    }
  ]
  "verification": "已打开并复核证据原文的实际评测章节及表格，不只按参考文献或网页存活判断。"
  "arxiv_revisions_kst": [
    {
      "version": "v1"
      "submitted_at_kst": "2024-06-27"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-08）

### 饱和情况

官方val reasoning前三为78.6%、72.0%、64.2%；Human为80.5%，但描述题指标独立且隐藏test不等于val。这里只记录接近程度，不把接近历史人类参照宣称为全任务饱和。

[来源1](https://charxiv.github.io/data/val_result.csv)（访问2026-11-07）

### 风险与冲突

官网CSV与README静态榜单更新不同，当前快照优先使用官网CSV。2,323 charts与README导览2,333 images冲突并列保留；test答案隐藏不代表图像无污染。MMVistaReason的CompassVerifier协议不能与官方GPT裁判结果混排。 官方HF Erratum明确0.jpg的reasoning参考答案有误（社区#2发现）；数据卡表示未来版本会修正，不自行改写答案。

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）；[来源2](https://charxiv.github.io/data/val_result.csv)（访问2026-11-07）；[来源3](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）；[来源4](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）；[来源5](https://huggingface.co/datasets/princeton-nlp/CharXiv/raw/main/README.md)（访问2026-11-07）

### 衍生与后续工作

待核实

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://charxiv.github.io/)（访问2026-11-07）

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

## 榜单快照

### 快照时间

2026-11-08 （实际复核日；批次标签2026-11-07）

[来源1](https://charxiv.github.io/)（访问2026-11-08）

### 官方榜入口

https://charxiv.github.io/#leaderboard

[来源1](https://charxiv.github.io/)（访问2026-11-07）

### 第三方榜入口

待核实

[来源1](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问2026-11-07）

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

### 逐轨结果

```json
[
  {
    "rank": 1
    "model": "o3 (high)"
    "score": 78.6
    "metric": "accuracy (%)"
    "track": "官网CSV／val／reasoning overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 2
    "model": "o4 mini (high)"
    "score": 72.0
    "metric": "accuracy (%)"
    "track": "官网CSV／val／reasoning overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 3
    "model": "Claude 3.7 Sonnet"
    "score": 64.2
    "metric": "accuracy (%)"
    "track": "官网CSV／val／reasoning overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 1
    "model": "o3 (high)"
    "score": 95.0
    "metric": "accuracy (%)"
    "track": "官网CSV／val／descriptive overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 2
    "model": "o4 mini (high)"
    "score": 94.3
    "metric": "accuracy (%)"
    "track": "官网CSV／val／descriptive overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "rank": 3
    "model": "GPT 4.5"
    "score": 90.0
    "metric": "accuracy (%)"
    "track": "官网CSV／val／descriptive overall"
    "source_url": "https://charxiv.github.io/data/val_result.csv"
    "accessed": "2026-11-08"
    "unit": "%"
    "evaluation_date": "待核实"
    "model_snapshot": "待核实"
  }
  {
    "model": "MMVistaReason-4B (MVR-4B)"
    "score": 66.9
    "unit": "%"
    "metric": "论文协议答案正确率（CompassVerifier）"
    "scope": "CharXiv reasoning"
    "date": "2026-10-23"
    "accessed": "2026-11-08"
    "source_url": "https://arxiv.org/html/2610.01352v2"
    "provenance": "MMVistaReason作者自报表2；VLMEvalKit，T=0，max16384；§7.3用CompassVerifier替代传统字符串匹配，不是官方榜单/AA独立评测"
    "date_basis": "arXiv v2提交时间换算；不是未公开的评测运行日期。"
    "track": "MMVistaReason v2／reasoning／CompassVerifier／作者自报"
    "rank": null
  }
  {
    "model": "MMVistaReason-9B (MVR-9B)"
    "score": 68.8
    "unit": "%"
    "metric": "论文协议答案正确率（CompassVerifier）"
    "scope": "CharXiv reasoning"
    "date": "2026-10-23"
    "accessed": "2026-11-08"
    "source_url": "https://arxiv.org/html/2610.01352v2"
    "provenance": "MMVistaReason作者自报表2；同上协议，不与其他榜单无条件混排"
    "date_basis": "arXiv v2提交时间换算；不是未公开的评测运行日期。"
    "track": "MMVistaReason v2／reasoning／CompassVerifier／作者自报"
    "rank": null
  }
]
```

[来源1](https://charxiv.github.io/data/val_result.csv)（访问2026-11-08）；[来源2](https://arxiv.org/html/2610.01352v2)（访问2026-11-08）

### 覆盖边界

重新读取官网CSV，reasoning与descriptive两列各自排序，排除Human与Random基线；CSV缺失的API快照和运行日期仍待核实。MMVistaReason使用另一裁判协议单列，绝不跨轨排名。

[来源1](https://charxiv.github.io/data/val_result.csv)（访问2026-11-08）；[来源2](https://arxiv.org/html/2610.01352v2)（访问2026-11-08）

## 联系方式

### 公开研究联系

```json
[
  "zw1300@cs.princeton.edu"
]
```

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

> 使用README明确提供的咨询邮箱；论文署名邮箱可能不同，不认定旧地址已失效。

### 项目反馈

https://github.com/princeton-nlp/CharXiv/issues

[来源1](https://github.com/princeton-nlp/CharXiv)（访问2026-11-07）

### 官方社交入口

https://x.com/zwcolin/status/1816948825036071196

[来源1](https://raw.githubusercontent.com/princeton-nlp/CharXiv/main/README.md)（访问2026-11-07）

> 官方README引用的项目讨论链接；未访问X内容或发送消息。

### 联系信息边界

仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-07）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2406.18521

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### PDF SHA-256

696ad9488b3d5f6d842fd1278d5be0fa2263676740d65bf1469bdd618af8a36c

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

> 下载原始字节校验，未压缩、未改写。

### PDF字节数

12563743

[来源1](https://arxiv.org/pdf/2406.18521)（访问2026-11-07）

### 目录

```json
{
  "id": "1pSe5r0MWe3eNJElkRmQkwLD06Lmy7nLh"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
[
  {
    "kind": "中文介绍"
    "id": "1TenxIC3WJjBkQ8biE0hfhDWmbMFdwrml9zIJH1UlYf4"
    "webViewLink": "
  }
]
```

[来源1](

### 论文归档

```json
{
  "id": "18fClV3CX6-yQ6K_VIjCX64Rbe-IFRP8J"
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
    "round": "1 / 深度实证复核"
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]
```

[来源1](https://arxiv.org/abs/2406.18521)（访问2026-11-08）；[来源2](https://charxiv.github.io/)（访问2026-11-08）
