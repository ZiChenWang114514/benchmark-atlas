# FRAMES

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/12q4xCRz_D8WiC27veCZz7ZOgQsMshCzq/view?usp=drivesdk)

## 基本信息

### 简称
FRAMES
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 全称
Factuality, Retrieval, And reasoning MEasurement Set
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 基准版本
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本
arXiv v3
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 发布日期
2024-09-19
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "检索增强多跳事实问答"
]
```
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 许可证
Apache-2.0（官方数据卡）；数据卡另有异常自动元数据，规模以正文及论文824题为准。
[来源1](https://huggingface.co/datasets/google/frames-benchmark)（采集2026-11-07）

### 论文
https://arxiv.org/abs/2409.12941
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 官方代码
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 数据地址
https://huggingface.co/datasets/google/frames-benchmark
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 官方入口
https://huggingface.co/datasets/google/frames-benchmark
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 论文标题
Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
Google/Google DeepMind 与 Harvard 相关作者团队；以论文作者单位为准，不推断唯一发起方。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Krishna, Satyapriya",
  "Krishna, Kalpesh",
  "Mohananey, Anhad",
  "Schwarcz, Steven",
  "Stambler, Adam",
  "Upadhyay, Shyam",
  "Faruqui, Manaal"
]
```
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
统一评估 RAG 系统的事实性、检索和多跳推理能力。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 既有评测缺口
既有数据常把检索、事实性与推理拆开，不能充分测量端到端多来源整合。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

## 构建方式

### 题目来源
依据多个 Wikipedia 页面编写需要多跳整合的问题，提供金答案及相关页面。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 出题与标注背景
论文描述的数据构建标注者及研究团队；逐人资质尚待核实。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 审核
问题要能关联所列来源，并标注推理类型；精确逐轮复核协议应参照论文。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 质量控制
提供 gold answers 和来源页面，区分 oracle 与实际检索设置。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
824 个问题，每题需整合 2–15 篇 Wikipedia 文章。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07） [来源2](https://huggingface.co/datasets/google/frames-benchmark)（采集2026-11-07）

### 题型
开放式、多跳检索问答
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 语言
英语
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 难度
数值、表格、多约束、时间、后处理等推理类型；文章数不同。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 公开与隐藏划分
官方公开问题、答案、相关 Wikipedia 文章；本次未核实额外隐藏集。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

## 评测方法

### 指标
最终回答准确率；检索配置须单独标注。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 评分
对最终答案评判，论文比较无检索、BM25、oracle 和多轮检索推理；不能将 oracle 分当作端到端检索分。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 提示与生成设置
原论文包含 naive、BM25 top4、oracle、多步检索推理等不同管线；保持模型快照与检索协议一致。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 脚本
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可比性警告
模型得分依赖索引、网页版本、检索器、检索轮数和上下文；oracle已给证据，不等价于真实搜索。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-09-23：Hunyuan-A13B §4.2–4.3实际使用 FRAMES 并报告结果；厂商自报，需保留各基准的提示/上下文条件。

### 数据版本
待核实
[来源1](https://huggingface.co/datasets/google/frames-benchmark)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2024-09-20T02:52:07+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2024-10-19T06:37:34+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2025-01-25T04:23:15+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 饱和情况
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题
官方数据卡 YAML 存在与正文不一致的 pretty_name/size_categories 等元数据；本条规模采用论文与正文的824题，不采信异常自动标签。
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 衍生评测
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://huggingface.co/datasets/google/frames-benchmark)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://arxiv.org/abs/2409.12941
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果
```json
[
  {
    "model": "Gemini-Pro-1.5-0514",
    "score": 72.9,
    "unit": "%",
    "metric": "answer accuracy",
    "scope": "原始官方数据卡历史 baseline，oracle检索",
    "evaluation_date": "2024年原论文；精确运行日期待核实"
  },
  {
    "model": "Gemini-Pro-1.5-0514",
    "score": 66.0,
    "unit": "%",
    "metric": "answer accuracy",
    "scope": "同一历史baseline，多步检索与推理",
    "evaluation_date": "2024年原论文；精确运行日期待核实"
  }
]
```
[来源1](https://huggingface.co/datasets/google/frames-benchmark)（采集2026-11-07）

### 覆盖与时效限制
只列官方数据卡清楚定义的历史管线。H2 Hunyuan报告自报81.1%，是另一评测管线，未合并排序。未核实统一实时榜。
[来源1](https://huggingface.co/datasets/google/frames-benchmark)（采集2026-11-07） [来源2](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
```json
[
  "skrishna@g.harvard.edu"
]
```
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

### 仓库讨论与Issues
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2409.12941)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2409.12941
[来源1](https://arxiv.org/pdf/2409.12941)（采集2026-11-07）

### 原件SHA-256
4f4f33ebd7be7ccb97af2be83fa123940fc38bc8256ecbdf2afde749481a091c
[来源1](https://arxiv.org/pdf/2409.12941)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
1163381
```
[来源1](https://arxiv.org/pdf/2409.12941)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1zSYlUJaUCjrqhUwIsS3H7UhyVBCD-7GD",
  "webViewLink": "https://drive.google.com/drive/folders/1zSYlUJaUCjrqhUwIsS3H7UhyVBCD-7GD"
}
```
[来源1](https://drive.google.com/drive/folders/1zSYlUJaUCjrqhUwIsS3H7UhyVBCD-7GD)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "10JG8gXXEf2Ztv2XsbMxIHl5xlk91cQX1b9nmf8-aGD0",
    "webViewLink": "https://docs.google.com/document/d/10JG8gXXEf2Ztv2XsbMxIHl5xlk91cQX1b9nmf8-aGD0/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/10JG8gXXEf2Ztv2XsbMxIHl5xlk91cQX1b9nmf8-aGD0/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2409.12941)（采集2026-11-07） [来源](https://arxiv.org/pdf/2409.12941)（采集2026-11-07）
