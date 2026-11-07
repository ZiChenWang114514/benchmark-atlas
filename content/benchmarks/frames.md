# FRAMES

> Benchmark Constitution · 研究快照 2026-11-07（KST / Asia/Seoul）。采集时间不等于成绩实跑或榜单更新时间。

FRAMES把检索、事实性与多来源推理放在同一端到端任务中。最终824题是人工构建而非原始LLM合成结果；oracle提供相关文章，因此72.9%与真实多步检索的66.0%不能当作不同模型的统一排名。

编辑状态：已核实存在与2026-H2实际使用；已建内容，待核实字段显式保留

## 基本信息

### 简称

FRAMES

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 全称

Factuality, Retrieval, And reasoning MEasurement Set

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 基准版本

官方HF公开快照 revision 58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef；数据卡无独立语义版本标签

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/blob/58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef/README.md)（访问 2026-11-07）


### 论文版本

arXiv v3（论文修订，不等于数据集版本）

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 发布日期

2024-09-20T02:52:07+09:00（KST；arXiv初稿时间，不冒充数据集独立发布日期）

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 主板块

语言

说明：Benchmark Constitution编辑归档，不是论文指定的唯一领域。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 领域标签

- 检索增强多跳事实问答

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 许可与范围

Apache-2.0（官方数据卡）；数据卡另有异常自动元数据，规模以正文及论文824题为准。

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）


### 论文

https://arxiv.org/abs/2409.12941

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 代码

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 数据入口

https://huggingface.co/datasets/google/frames-benchmark

说明：本轮已读取的公开HF卡revision: 58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef；只固定公开卡/仓库状态，不外推为私有测试版本。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 官方主页

https://huggingface.co/datasets/google/frames-benchmark

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 论文标题

Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 发起与维护

### 发起/作者单位

论文作者单位为Harvard University、Google DeepMind、Meta；不把作者的现单位自动等同法律发起方或正式合作协议。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 合作与支持

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 作者

- Krishna, Satyapriya
- Krishna, Kalpesh
- Mohananey, Anhad
- Schwarcz, Steven
- Stambler, Adam
- Upadhyay, Shyam
- Faruqui, Manaal

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 维护方

Google HF组织下的google/frames-benchmark发布账户；学术联系为论文通讯作者Satyapriya Krishna，不推断个别员工当前仍维护。

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 资助

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 设计目标

### 衡量能力

统一评估 RAG 系统的事实性、检索和多跳推理能力。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 设计背景

既有数据常把检索、事实性与推理拆开，不能充分测量端到端多来源整合。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 构建方式

### 题目来源

先试验LLM合成，但>30%出现幻觉且难稳定要求超过4篇文章；最终824题由人工编写，利用多篇Wikipedia页面、金答案和来源链接，不能称作纯合成题库。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 出题者背景

经过筛选、具有问题编写和复杂推理任务经验的人工标注专家；这是论文对团队资质的描述，不外推每位标注员的学历/学科身份。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 审核流程

人工重新标注核对答案与所列Wikipedia页面是否一致；补充时间截止语境消除时效歧义；删除yes/no问题以减少猜测；每题标注可重叠的推理类型。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 质量控制

题目与答案重新核对来源、补明确日期以免答案随时间变化、移除二元答案扩大输出空间，并标注五类推理以便解释。Wikipedia页面数不直接等于严格推理hop数。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 污染控制

以需要跨来源推理和额外运算的问题减少直接事实记忆的收益；论文Limitations仍明确承认Wikipedia可能进入预训练，未证明无污染。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 数据形式

### 题量

824道多跳问题，每题需关联2–15篇Wikipedia文章；正文为题量权威口径，不采用卡片异常的n>1T自动元数据。

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/raw/main/README.md)（访问 2026-11-07）


### 任务形式

多跳开放问答；附gold answer及相关文章，标注数值、表格、多重约束、时间与后处理等推理类型。

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/raw/main/README.md)（访问 2026-11-07）


### 模态

文本

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 语言

英语（数据卡language: en）

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/raw/main/README.md)（访问 2026-11-07）


### 难度与分层

数值、表格、多约束、时间、后处理等推理类型；文章数不同。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 公开与隐藏划分

官方公开问题、答案、相关 Wikipedia 文章；本次未核实额外隐藏集。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 评测方法

### 指标

最终回答准确率；检索配置须单独标注。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 评分

对最终答案评判，论文比较无检索、BM25、oracle 和多轮检索推理；不能将 oracle 分当作端到端检索分。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 提示与运行协议

原论文包含 naive、BM25 top4、oracle、多步检索推理等不同管线；保持模型快照与检索协议一致。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 评测脚本

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 可比性警示

模型得分依赖索引、网页版本、检索器、检索轮数和上下文；oracle已给证据，不等价于真实搜索。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul（资料快照日期）

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）


### 版本与采用证据

- **public_dataset_revision**：58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef
- **size**：824
- **source**：官方HF主分支本轮resolve响应的x-repo-commit；不当作论文版本

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/blob/58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef/README.md)（访问 2026-11-07）


### 材料沿革

- - **version**：v1
  - **submitted_at_kst**：2024-09-20T02:52:07+09:00
  - **timezone**：Asia/Seoul (KST)
- - **version**：v2
  - **submitted_at_kst**：2024-10-19T06:37:34+09:00
  - **timezone**：Asia/Seoul (KST)
- - **version**：v3
  - **submitted_at_kst**：2025-01-25T04:23:15+09:00
  - **timezone**：Asia/Seoul (KST)

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 饱和情况

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 污染与局限

论文明确承认预训练数据污染可能抬高分数；公开金答案及Wikipedia素材不能充当隐藏无污染测试。HF YAML还有异常pretty_name/size_categories，规模按论文及正文824题而非n>1T。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）


### 版本/衍生关系

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul（快照日，非实跑日）

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 官方榜

https://arxiv.org/abs/2409.12941

说明：未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 其他评测入口

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 分轨结果（结构化快照）

```json
[
  {
    "rank": null,
    "model": "Gemini-Pro-1.5-0514",
    "score": 40.8,
    "unit": "%",
    "metric": "answer accuracy",
    "settings": "naive prompting",
    "scope": "官方数据卡2024原论文历史baseline；设置不同不作模型排名",
    "source_url": "https://huggingface.co/datasets/google/frames-benchmark",
    "accessed": "2026-11-07",
    "evaluation_date": "待核实：卡片未列精确实验日"
  },
  {
    "rank": null,
    "model": "Gemini-Pro-1.5-0514",
    "score": 47.4,
    "unit": "%",
    "metric": "answer accuracy",
    "settings": "BM25, top4 docs",
    "scope": "官方数据卡2024原论文历史baseline；设置不同不作模型排名",
    "source_url": "https://huggingface.co/datasets/google/frames-benchmark",
    "accessed": "2026-11-07",
    "evaluation_date": "待核实：卡片未列精确实验日"
  },
  {
    "rank": null,
    "model": "Gemini-Pro-1.5-0514",
    "score": 72.9,
    "unit": "%",
    "metric": "answer accuracy",
    "settings": "oracle retrieval",
    "scope": "官方数据卡2024原论文历史baseline；设置不同不作模型排名",
    "source_url": "https://huggingface.co/datasets/google/frames-benchmark",
    "accessed": "2026-11-07",
    "evaluation_date": "待核实：卡片未列精确实验日"
  },
  {
    "rank": null,
    "model": "Gemini-Pro-1.5-0514",
    "score": 66.0,
    "unit": "%",
    "metric": "answer accuracy",
    "settings": "multi-step retrieval & reasoning",
    "scope": "官方数据卡2024原论文历史baseline；设置不同不作模型排名",
    "source_url": "https://huggingface.co/datasets/google/frames-benchmark",
    "accessed": "2026-11-07",
    "evaluation_date": "待核实：卡片未列精确实验日"
  }
]
```

[榜单原始资料](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）；[榜单原始资料](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 覆盖范围

重读官方HF卡列全四个历史baseline；72.9是oracle给定相关文章，66.0是实际多步检索推理，不同管线不混排。未发现该官方卡维护独立实时排行榜；Hunyuan自报81.1%不据此宣称官方新纪录。

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


## 联系方式

### 公开研究邮箱

- skrishna@g.harvard.edu

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 问题反馈

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 机构公开渠道

待核实

状态：待核实。

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）


### 隐私政策

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[一手资料1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）


## 原始文件

### 论文PDF

https://arxiv.org/pdf/2409.12941

[一手资料1](https://arxiv.org/pdf/2409.12941)（访问 2026-11-07）


### 源站PDF SHA-256

4f4f33ebd7be7ccb97af2be83fa123940fc38bc8256ecbdf2afde749481a091c

说明：实际下载的源站PDF字节摘要；不据此声称Drive副本已更新。

[一手资料1](https://arxiv.org/pdf/2409.12941)（访问 2026-11-07）


### 源站PDF字节数

1163381

[一手资料1](https://arxiv.org/pdf/2409.12941)（访问 2026-11-07）


### Drive资料目录

- **id**：1zSYlUJaUCjrqhUwIsS3H7UhyVBCD-7GD
- **webViewLink**：https://drive.google.com/drive/folders/1zSYlUJaUCjrqhUwIsS3H7UhyVBCD-7GD

[一手资料1](https://drive.google.com/drive/folders/1zSYlUJaUCjrqhUwIsS3H7UhyVBCD-7GD)（访问 2026-11-07）


### 其他官方资料

- - **kind**：中文介绍 Google Doc
  - **id**：10JG8gXXEf2Ztv2XsbMxIHl5xlk91cQX1b9nmf8-aGD0
  - **webViewLink**：https://docs.google.com/document/d/10JG8gXXEf2Ztv2XsbMxIHl5xlk91cQX1b9nmf8-aGD0/edit?usp=drivesdk
- - **type**：本轮核验的官方原始资料
  - **url**：https://huggingface.co/datasets/google/frames-benchmark
  - **accessed**：2026-11-07

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）


### Drive PDF归档

- **id**：12q4xCRz_D8WiC27veCZz7ZOgQsMshCzq
- **webViewLink**：https://drive.google.com/file/d/12q4xCRz_D8WiC27veCZz7ZOgQsMshCzq/view?usp=drivesdk

本轮仅核对源站PDF和已有归档引用，未上传或覆盖Drive文件。

## 变更记录

- - **date**：2026-11-07
  - **timezone**：Asia/Seoul
  - **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07
  - **timezone**：Asia/Seoul
  - **change**：第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
  - **fields_updated**：- data_format.size
    - data_format.languages
    - data_format.question_types
- - **date**：2026-11-07
  - **timezone**：Asia/Seoul (KST)
  - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位官方README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
