# TruthfulQA

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/12HuAWYz_OBaC5-Hlk_sLg1mzUbeHUD1k/view?usp=drivesdk)

## 基本信息

### 简称
TruthfulQA
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 全称
TruthfulQA
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 基准版本
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本
arXiv v2
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 发布日期
2021-09-08
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
安全
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "真实性与误解诱发的幻觉"
]
```
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 许可证
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文
https://arxiv.org/abs/2109.07958
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 官方代码
https://github.com/sylinrl/TruthfulQA
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 数据地址
https://github.com/sylinrl/TruthfulQA
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 官方入口
https://github.com/sylinrl/TruthfulQA
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 论文标题
TruthfulQA: Measuring How Models Mimic Human Falsehoods
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
作者 Stephanie Lin、Jacob Hilton、Owain Evans，单位涉及 Oxford 与 OpenAI；此处不推断正式联合发起协议。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Lin, Stephanie",
  "Hilton, Jacob",
  "Evans, Owain"
]
```
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
检验模型是否复述人类常见误解，而非只看回答流畅度。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 既有评测缺口
模仿互联网文本可能学习流行错误；知识问答准确率不直接等于避免误导。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

## 构建方式

### 题目来源
作者编写与常见误解相关的问题；437 道通过 GPT-3 对抗筛选，380 道未筛选。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 出题与标注背景
研究团队撰写问题并核查答案，覆盖多个日常与专业领域。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 审核
区分真实与信息充分，人工检查答案并训练自动裁判。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 质量控制
同时衡量 truthfulness 与 informativeness，避免把无信息拒答误作有用事实回答。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
817 道问题、38 个类别。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 题型
开放生成及多项选择两种评测方式
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 语言
英语
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 难度
专门诱发常见误解；对抗筛选题与未筛选题的分布不同。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 公开与隐藏划分
公开题集及参考正确/错误答案；不得在测试示例上调优后当作原始零样本结果。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

## 评测方法

### 指标
生成式 truthfulness、informativeness及二者同时满足率；选择式MC1/MC2需区分。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 评分
生成任务可用人工或GPT-judge；MC2衡量正确答案集合的归一化概率质量，不是普通单选准确率。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 提示与生成设置
原论文零样本，不用本基准示例调优；greedy生成；提示风格会显著影响回答与拒答。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 脚本
https://github.com/sylinrl/TruthfulQA
[来源1](https://github.com/sylinrl/TruthfulQA)（采集2026-11-07）

### 可比性警告
只答“我不知道”可能被判真实但无信息；truthfulness、true+informative、MC1、MC2不可混比。
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 研究表1–2实际使用 TruthfulQA，并明确区分准确率与MC2等评价口径。

### 数据版本
待核实
[来源1](https://github.com/sylinrl/TruthfulQA)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2021-09-09T02:15:27+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2022-05-08T11:43:02+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 饱和情况
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题
2026-H2 Jev 对比论文混合引用不同历史来源，并对部分 TruthfulQA 分数标明MC2；引用时不可把这些行都当同指标准确率。
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

### 衍生评测
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://arxiv.org/abs/2109.07958
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果
```json
[
  {
    "model": "Gemini 3.8 Flash（研究表2原标签）",
    "score": 97.9,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究；不是基准官方实时榜，也不是AA独立榜；本行未标MC2，不能与表中标MC2的行混比",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Claude Opus 5.5（研究表2原标签）",
    "score": 92.0,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究；不是基准官方实时榜，也不是AA独立榜；本行未标MC2，不能与表中标MC2的行混比",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Jev（研究表2原标签）",
    "score": 87.5,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究；不是基准官方实时榜，也不是AA独立榜；本行未标MC2，不能与表中标MC2的行混比",
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
```json
[
  "sylin07@gmail.com"
]
```
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

### 仓库讨论与Issues
https://github.com/sylinrl/TruthfulQA/issues
[来源1](https://github.com/sylinrl/TruthfulQA)（采集2026-11-07）

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2109.07958)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2109.07958
[来源1](https://arxiv.org/pdf/2109.07958)（采集2026-11-07）

### 原件SHA-256
6e86175861d24d075bbd8fec987cbdabd0d6332700b001a1ccf335fa72f541b2
[来源1](https://arxiv.org/pdf/2109.07958)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
819857
```
[来源1](https://arxiv.org/pdf/2109.07958)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1K67pMyWmwzHPTWfWS6Qbhpuz0ZhyOsLv",
  "webViewLink": "https://drive.google.com/drive/folders/1K67pMyWmwzHPTWfWS6Qbhpuz0ZhyOsLv"
}
```
[来源1](https://drive.google.com/drive/folders/1K67pMyWmwzHPTWfWS6Qbhpuz0ZhyOsLv)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1Gd-3UCMu3Qp3aNooWo3Sq2Ar2Bo1hlC06er3pz1o26E",
    "webViewLink": "https://docs.google.com/document/d/1Gd-3UCMu3Qp3aNooWo3Sq2Ar2Bo1hlC06er3pz1o26E/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/1Gd-3UCMu3Qp3aNooWo3Sq2Ar2Bo1hlC06er3pz1o26E/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2109.07958)（采集2026-11-07） [来源](https://arxiv.org/pdf/2109.07958)（采集2026-11-07）
