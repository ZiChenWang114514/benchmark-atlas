# MedQA

> Benchmark Constitution｜2026-11-08 深度复核。访问日期不等于实验运行日期；历史来源日期保持原记录。

MedQA把美国、中国大陆及台湾的医学执照考试题整理为英语、简体中文与繁体中文问答，并提供教材检索语料。原始三语test与后续USMLE四选项、抽样或偏见注入实现必须分别说明，不能把任何一个高分直接推广为临床诊疗能力。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）；[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）

## 基本信息

### 简称

MedQA

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 全称

MedQA

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 版本与作用域

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 论文/报告版本

arXiv v1（2020-09-28 14:07:51 ）

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 首次公开日期

2020-09-28 14:07:51 （arXiv v1；非推定数据首发时间）

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 主板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（访问2026-11-08 ）

### 子领域

```json
[
  "医学执照考试式临床推理"
]
```

来源：[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（访问2026-11-08 ）

### 许可与权利边界

仓库根LICENSE为MIT（2022 Di Jin），但不覆盖所有上游医学教材权利；原论文§3.2明确教材仅按research-use-only协议释放。BigBio HF镜像将数据license列unknown。三种作用域并列，不将MIT简化为整包教材可任意商用。

来源：[https://raw.githubusercontent.com/jind11/MedQA/master/LICENSE](https://raw.githubusercontent.com/jind11/MedQA/master/LICENSE)（访问2026-11-08 ）；[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）；[https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md](https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md)（访问2026-11-08 ）

### 论文/报告入口

https://arxiv.org/abs/2009.13081

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 官方代码

https://github.com/jind11/MedQA

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 数据入口

https://github.com/jind11/MedQA

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 官方主页

https://github.com/jind11/MedQA

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 论文/报告标题

What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 发起与维护

### 研究发起团队

论文研究团队：MIT CSAIL与华中科技大学同济医学院共同署名；不推断机构法律发起协议。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### 合作研究机构与顾问

```json
[
  "MIT CSAIL"
  "Tongji Medical College, Huazhong University of Science and Technology"
]
```

说明：仅以共同署名单位为合作研究机构。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### 作者

```json
[
  "Jin, Di"
  "Pan, Eileen"
  "Oufattole, Nassim"
  "Weng, Wei-Hung"
  "Fang, Hanyi"
  "Szolovits, Peter"
]
```

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 维护方

jind11/MedQA官方仓库。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 资助方

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 设计目标

### 测量能力

医学执照考试式多项选择，结合临床知识、病例推理与外部证据检索。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 设计动机

给定短文抽取答案的阅读理解难以代表需检索多个医学来源的开放域问答。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 构建方式

### 材料来源

美国、中国大陆、台湾医学资格考试题及相关医学教科书/文档语料。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 命题与标注背景

论文为MIT计算机研究者与同济医学院作者共同工作；数据为专业医学执照考试及模拟题。论文另外使用两名医学医生审核检索证据，不把他们误作全部原题命题者。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### 审核流程

删除重复题，按问题随机80%/10%/10%分train/dev/test；USMLE与MCMLE打乱选项并随机删一个错误项得到四选项版。论文两名医生审核的是dev随机100题top25检索段落的证据充分性，不是全数据医学双审。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### 质量控制

多语言数据与固定划分，论文分析检索噪声和多证据推理失败。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 去污染与留出

公开考试及GitHub测试集存在训练暴露风险；2020原始划分不能证明2026模型无污染。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 数据形式

### 规模与统计对象

英语12,723、简体中文34,251、繁体中文14,123题；三语合计61,097（由原论文分项相加）。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 题型与字段

病例或医学知识的多项选择；原版与US/大陆4选项处理版须分开。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）；[https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)（访问2026-11-07 ）

### 模态

文本题干、选项、答案；QA逐行保存为JSONL，每行是一个dict；附英语与简体中文教材检索语料。

来源：[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）

### 语言

```json
[
  "英语"
  "简体中文"
  "繁体中文"
]
```

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 难度与覆盖

专业医学考试；不等同真实临床工作流或安全性验证。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 公开/私有与数据划分

原论文表3：USMLE train10,178/dev1,272/test1,273；MCMLE train27,400/dev3,425/test3,426；TWMLE train11,298/dev1,412/test1,413。原数据与4_options处理版均需标记；三语分割公开，不是统一的隐藏医疗测试。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）；[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）

## 评测方法

### 指标

Accuracy：选择答案匹配标准答案。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 评分与聚合

原论文结合检索器与阅读器，也可闭卷选择；检索/开卷与闭卷分开。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 提示与推理预算

原论文非统一现代LLM提示；后续模型需注明4/5选项、CoT、shot、检索和测试子集。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 官方实现

https://github.com/jind11/MedQA

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 可比性边界

三语、选项数量、工具与子集必须一致；医学考试高分不代表临床有效或安全。

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 最新情况

### 核验时间

2026-11-08

来源：[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）

### 当前数据与协议

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 论文修订与延续使用证据

```json
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.19029v1"
      "date": "2026-08-19"
      "note": "Adaptive Memory and Reflection Multi-Agent System 实际在 MedQA 上评测医学问答。"
    }
  ]
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。"
  "paper_metadata": {
    "title": "What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams"
    "authors": [
      "Jin, Di"
      "Pan, Eileen"
      "Oufattole, Nassim"
      "Weng, Wei-Hung"
      "Fang, Hanyi"
      "Szolovits, Peter"
    ]
    "release": "2020-09-28"
    "latest": "2020-09-28"
    "version": "v1"
  }
}
```

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（访问2026-11-08 ）

### 饱和判断边界

Vals明确以该机构2000题USMLE来源抽样/偏见注入协议的分数已饱和为由归档，停止新模型评测（页面更新2026-04-16）；该结论只适用于其评测，不等于三语MedQA原始全部测试同协议均已解决。

来源：[https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa)（访问2026-11-08 ）

### 污染、冲突与复现风险

原始题集自2020年公开，Vals明确指出可能用于模型预训练；其偏见注入题不公开。原论文教材限研究使用、BigBio许可unknown与仓库MIT的作用域须区分。AMR叙述逐题反馈但实验称冻结检索、不写回test反馈，仅保留作者自报结果不作统一SOTA。

来源：[https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa)（访问2026-11-08 ）；[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）；[https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md](https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md)（访问2026-11-08 ）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（访问2026-11-08 ）

### 衍生实现

官方另提供美国和中国大陆4_options处理版；不得与原选项版直接混排比较。

来源：[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）

## 榜单快照

### 访问快照日期

2026-11-08 （访问；各来源运行/提交日期另列）

来源：[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）

### 官方榜单入口

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 第三方评测入口

https://www.vals.ai/benchmarks/medqa

说明：Vals独立执行的2000题USMLE来源评测，已归档；不是原始官方1273题test。

来源：[https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa)（访问2026-11-08 ）

### 分来源、分协议结果

```json
[
  {
    "rank": null
    "model": "BioBERT-Large"
    "score": 36.7
    "unit": "%"
    "metric": "Accuracy"
    "track": "原论文表7/8 / USMLE test1273 / 英文"
    "source_url": "https://arxiv.org/pdf/2009.13081"
    "accessed": "2026-11-08"
    "result_type": "原始历史基线；教材检索+reader"
  }
  {
    "rank": null
    "model": "BioBERT-Large"
    "score": 42.0
    "unit": "%"
    "metric": "Accuracy"
    "track": "原论文表7/8 / TWMLE test1413 / 繁中翻译英语"
    "source_url": "https://arxiv.org/pdf/2009.13081"
    "accessed": "2026-11-08"
    "result_type": "原始历史基线；教材检索+reader"
  }
  {
    "rank": null
    "model": "RoBERTa-Large-WWM-ext"
    "score": 70.1
    "unit": "%"
    "metric": "Accuracy"
    "track": "原论文表7/8 / MCMLE test3426 / 简中"
    "source_url": "https://arxiv.org/pdf/2009.13081"
    "accessed": "2026-11-08"
    "result_type": "原始历史基线；教材检索+reader"
  }
  {
    "rank": 1
    "model": "o1"
    "score": 96.52
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 2
    "model": "GPT 5.1"
    "score": 96.38
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 3
    "model": "Gemini 3.1 Pro Preview (02/26)"
    "score": 96.37
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 4
    "model": "GPT 5"
    "score": 96.32
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 5
    "model": "GPT 5.4 (xhigh)"
    "score": 96.09
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 6
    "model": "o3"
    "score": 96.06
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 7
    "model": "GPT 5 Mini"
    "score": 96.06
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 8
    "model": "Gemini 3 Pro (11/25)"
    "score": 96.03
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 9
    "model": "o4 Mini"
    "score": 96.02
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": 10
    "model": "Claude Opus 4.5 (Thinking)"
    "score": 95.88
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals归档评测 / USMLE来源2000题抽样及偏见研究"
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "独立机构评测；具体表行对应无偏/偏见聚合口径待核实"
  }
  {
    "rank": null
    "model": "AMR (GPT-4o)"
    "score": 93.2
    "unit": "%"
    "metric": "Accuracy"
    "track": "AMR论文 / 官方USMLE test / train检索冻结"
    "source_url": "https://arxiv.org/html/2608.19029v1"
    "accessed": "2026-11-08"
    "source_date": "2026-08-19"
    "settings": "GPT-4o具体API快照、完整样本清单待核实"
    "result_type": "论文作者自报"
  }
]
```

核验状态：待核实

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）；[https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa)（访问2026-11-08 ）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（访问2026-11-08 ）

### 快照覆盖说明

三条互不混排来源：原论文三语历史基线、Vals归档榜前10、AMR论文自报。Vals方法说明2000题抽样及五类偏见注入，和原USMLE test1273不同；表行究竟对应无偏基线还是多组聚合尚待核实，因此保留来源原Accuracy标签与该边界。不能把Vals归档当持续实时官方榜。

核验状态：待核实

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）；[https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa)（访问2026-11-08 ）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（访问2026-11-08 ）

## 联系方式

### 官方公开联系邮箱

```json
[
  "jindi15@mit.edu"
  "eileenp@mit.edu"
  "nassim@mit.edu"
  "ckbjimmy@mit.edu"
  "psz@mit.edu"
  "fanghanyi@hust.edu.cn"
]
```

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 项目反馈入口

https://github.com/jind11/MedQA/issues

来源：[https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)（访问2026-11-07 ）

### 公开社交渠道

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 联系信息原则

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 原始文件

### 原始论文/技术报告PDF

https://arxiv.org/pdf/2009.13081

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）；[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### PDF SHA-256

5e19522f21c0ab5c24cc0dacd3feaa5d4b7057391520075f2e521a271d062ee6

说明：下载的arXiv原始字节；不表示已替换中的旧文件。

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### PDF原始字节数

189006

来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（访问2026-11-08 ）

### 资料夹

```json
{
  "id": "1AYwJpnQXewH8Hk2KHLsemGjydd3Fvco0"
  "webViewLink": "
}
```

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

### 其他官方资料

```json
[
  {
    "type": "中文介绍 Google Doc"
    "id": "1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE"
    "webViewLink": "https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit"
  }
]
```

来源：[https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit](https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit)（访问2026-11-07 ）

### 已存PDF

```json
{
  "id": "1zmvFZ0lC8HCOh62LXlOrjcHf25kzF4gZ"
  "webViewLink": "
}
```

来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（访问2026-11-08 ）

## 变更记录

### 变更记录

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

来源：[https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问2026-11-08 ）
