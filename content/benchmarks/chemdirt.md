# ChemDIRT

> Benchmark Constitution · 深度复核：2026-11-08 KST / Asia/Seoul。第1轮实证补全；未确认项保留待核实，论文历史分数与实时榜单分开记录。

ChemDIRT用任务、提示改写和分子表示三个轴诊断化学LLM的稳定性，而不是压成一个总分。论文包含33种任务设置、八类任务；图像到结构、逆合成和性质回归必须保留各自指标。当前README声称4,484题，而HF卡明确4,482行，这个两条记录的差异仍需维护方解释，不能用“4.48k”掩盖。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

## 基本信息

### 简称

ChemDIRT

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 全称

ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 版本边界

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本

v1；最近论文日期 2026-08-21

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 发布日期

2026-08-21（首个arXiv版本日期；非推定数据上线日）

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 板块

化学

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

> 编辑分类沿用入选清单；不代表该基准只测本板块。

### 领域

```json
[
  "指令、表示与任务鲁棒性"
]
```

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 许可与限制

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文

https://arxiv.org/abs/2608.21504

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 官方代码

https://github.com/einae-nd/ChemDIRT

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### 数据入口

https://huggingface.co/datasets/Einae/ChemDIRT

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 官方主页

https://github.com/einae-nd/ChemDIRT

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 论文题名

ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

## 发起与维护

### 发起方

论文作者单位：University of Notre Dame；不据此推断唯一法律所有人。

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 合作机构

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者

```json
[
  "Inae, Eric",
  "Gunn, Tim",
  "Bond, Chris",
  "Jiang, Meng"
]
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 维护入口

einae-nd/ChemDIRT及Einae数据发布账号。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 资助披露

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 设计目标

### 测量对象

对同一化学任务的指令改写与分子表示变化保持可靠；跨八类任务诊断鲁棒性。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 既有评测的缺口

单一提示/表示的成绩容易高估稳定能力，任务平均值掩盖表示及提示敏感性。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

## 构建方式

### 题源

QM9、ZINC、ChEMBL、PubChem分子及MoleculeNet/ChemLLMBench等已有任务；RDKit构建可计算真值。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 构建人员

Eric Inae、Tim Gunn、Chris Bond、Meng Jiang，Notre Dame。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 审核

GPT-5Pro生成十种提示模板并人工核查，实际评测取前四种；清洗继承数据。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 质控

官方提供 bundled data/image 校验脚本；运行结果保存原始预测、任务指标、配置、输入哈希和检查点。

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### 去污染及边界

有继承公开任务与分子库，不能将提示改写视为已去预训练污染；独立模型训练语料审计待核实。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

## 数据形式

### 规模与计数口径

```json
{
  "readme_questions": 4484,
  "readme_molecular_images": 300,
  "hf_card_train_records": 4482,
  "paper_task_settings": 33,
  "warning": "README 4484与当前HF数据卡4482不一致；不四舍五入为一致，也不推断缺失两题的原因。33为任务设置而不是题目数量。"
}
```

[来源1](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/Einae/ChemDIRT/blob/main/README.md)（访问2026-11-08）；[来源3](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）

### 题型

描述、分类、设计、分析、回归、计算、机理、关系任务。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 模态

分子文本表示和分子图像。

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### 语言

英语自然语言；SMILES/IUPAC化学表示。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 难度

指令与表示扰动是主要难度轴；没有统一难度级别。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 划分与公开范围

HF元数据公开单个名为train的split，4,482行；它是发布容器，不证明有独立监督训练流程或隐藏测试集；README本地包声称4,484题，口径冲突保留。

[来源1](https://huggingface.co/datasets/Einae/ChemDIRT/blob/main/README.md)（访问2026-11-08）；[来源2](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）

## 评测方法

### 指标

分类用 accuracy；分子设计报告 exact match 与 MACCS/Morgan/RDK 指纹相似度；数值任务报告 log RMSE、MAE、relative RMSE 和 RMSE。

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 评分

结构先解析再比对；数值任务计算误差；报告四提示下平均和标准差，不混为置信区间。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 提示与运行条件

论文每任务用 GPT-5 Pro 生成 10 个模板并人工校验语义；报告评估取前 4 个通过验证的模板。

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 官方评测入口

src/cli.py 运行推理与评分；scripts/validate_data.py 检查数据及图像。

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### 可比性边界

不同任务指标无通用总分；图像转结构、逆合成与回归成绩不能同排。模型标签与API具体快照需区分。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

## 最新情况

### 复核时间

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）；[来源2](https://arxiv.org/abs/2608.21504)（访问2026-11-08）

### 当前版本

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文修订与后续使用

```json
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.21504v1",
      "date": "2026-08-21",
      "note": "ChemDIRT 原始论文在H2提出并实际评测多指令、多分子表示及八类化学任务的鲁棒性。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation",
    "authors": [
      "Inae, Eric",
      "Gunn, Tim",
      "Bond, Chris",
      "Jiang, Meng"
    ],
    "release": "2026-08-21",
    "latest": "2026-08-21",
    "version": "v1"
  },
  "arxiv_revisions_kst": [
    {
      "version": "v1",
      "submitted_at_kst": "2026-08-22T01:58:30+09:00"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）

### 饱和情况

无有效统一饱和数；Llama3在ClinTox不同提示可从0.095到0.905，说明稳定性问题。

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 风险与冲突

继承公开分子库与任务，提示改写不等于去预训练污染；四提示间总体标准差不是采样置信区间。README题量4,484与HF卡4,482需维护方解释；未找到LICENSE文件，HF卡也未标许可，仍待核实。

[来源1](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/Einae/ChemDIRT/blob/main/README.md)（访问2026-11-08）；[来源3](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）

### 衍生与后续工作

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 榜单快照

### 快照时间

2026-11-08 KST / Asia/Seoul（实际复核日；批次标签2026-11-07）

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）

### 官方榜入口

https://github.com/einae-nd/ChemDIRT

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 第三方榜入口

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 逐轨结果

```json
[
  {
    "rank": null,
    "model": "Claude-Sonnet-5",
    "score": 0.633,
    "metric": "exact match",
    "track": "论文Table V／image→SMILES",
    "source_url": "https://arxiv.org/pdf/2608.21504",
    "accessed": "2026-11-08",
    "std_across_prompts": 0.028,
    "unit": "比例"
  },
  {
    "rank": null,
    "model": "Claude-Sonnet-5",
    "score": 0.687,
    "metric": "exact match",
    "track": "论文Table V／image→IUPAC",
    "source_url": "https://arxiv.org/pdf/2608.21504",
    "accessed": "2026-11-08",
    "std_across_prompts": 0.039,
    "unit": "比例"
  },
  {
    "rank": null,
    "model": "RetroDFM-R",
    "score": 0.685,
    "metric": "exact match",
    "track": "论文Table IV／SMILES retrosynthesis",
    "source_url": "https://arxiv.org/pdf/2608.21504",
    "accessed": "2026-11-08",
    "std_across_prompts": 0.023,
    "unit": "比例"
  }
]
```

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）

### 覆盖边界

三条均锁定v1论文，按image→SMILES、image→IUPAC、SMILES逆合成三轨结构化；rank=null因为不是同一任务的完整排名。±为四种提示的总体标准差，不是置信区间；不宣称当前实时SOTA。

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）；[来源2](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）

## 联系方式

### 公开研究联系

```json
[
  "einae@nd.edu",
  "tgunn2@nd.edu",
  "cbond@nd.edu",
  "mjiang2@nd.edu"
]
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 项目反馈

https://github.com/einae-nd/ChemDIRT/issues

[来源1](https://github.com/einae-nd/ChemDIRT)（访问2026-11-07）

### 官方社交入口

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 联系信息边界

待核实

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

> 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2608.21504

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### PDF SHA-256

70a4ee8128ed69e69bb9a7394b1a823571e1738592986f7fc345603826a12524

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-07）

### PDF字节数

466313

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-07）

### Drive目录

```json
{
  "id": "1Z1arqpVyZtzUnhGEUznM1Oh02lQKFmh5",
  "webViewLink": "https://drive.google.com/drive/folders/1Z1arqpVyZtzUnhGEUznM1Oh02lQKFmh5"
}
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58",
    "webViewLink": "https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit"
  }
]
```

[来源1](https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit)（访问2026-11-07）

### Drive论文归档

```json
{
  "id": "186sLc62vIHc-Ng9ZKqoGmn37H6CvHjjB",
  "webViewLink": "https://drive.google.com/file/d/186sLc62vIHc-Ng9ZKqoGmn37H6CvHjjB/view"
}
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "第1轮：打开官方文档核验许可、数据形式和评测协议；复核2026H2证据，区分历史结果与实时榜单；同步中文介绍。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST)",
    "change": "第2轮q2：重读一级材料、保留版本/许可冲突；榜单按来源与协议分轨，中文介绍重写。"
  }
]
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）
