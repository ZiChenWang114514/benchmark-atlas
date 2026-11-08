# MBPP

> Benchmark Constitution, in-depth review 2026-11-08. The access date is not the date the experiment was run; dates from historical sources keep their original record.

MBPP measures the ability to generate an executable Python function from a short English requirement. The original 974 questions and the manually cleaned sanitized version are not two independent benchmarks; the full test has 500 questions, and the sanitized test has 257 questions. Passing three assertions is only a limited check of functional correctness and cannot be equated with the reliability of production software.

Sources: [https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md](https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md) (accessed 2026-11-08); [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08)

## Basic information

### Short name

MBPP

Sources: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp) (accessed 2026-11-07  )

### Full name

Mostly Basic Programming Problems

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 版本与作用域

The original 974 questions; the sanitized subset must be noted separately

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 论文/报告版本

arXiv v1

Note: A paper revision is not the same as a dataset version.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 首次公开日期

2021-08-16 12:57:30

Note: The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Section

Code

Note: Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Subfields

```json
[
  "Basic Python programming"
]
```

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 许可与权利边界

The root LICENSE of the Google Research code repository is Apache-2.0; the MBPP dataset card hosted by Google Research Datasets is marked explicitly as CC BY 4.0. The two record the code license and the data license separately, and the data license is no longer left blank as a whole; the grant is not extended to any externally cited material.

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/LICENSE](https://raw.githubusercontent.com/google-research/google-research/master/LICENSE) (accessed 2026-11-08  ) ; [https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md](https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md) (accessed 2026-11-08  )

### 论文/报告入口

https://arxiv.org/abs/2108.07732

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Code

https://github.com/google-research/google-research/tree/master/mbpp

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Dataset

https://huggingface.co/datasets/google-research-datasets/mbpp

Sources: [https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md](https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md) (accessed 2026-11-08  ) ; [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  )

### Official homepage

https://github.com/google-research/google-research/tree/master/mbpp

Sources: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp) (accessed 2026-11-07  )

### 论文/报告标题

Program Synthesis with Large Language Models

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Origin and maintenance

### 研究发起团队

Google Research; some authors participated at MIT or in the capacity of interns.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 合作研究机构与顾问

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

核验状态：待核实

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Authors

```json
[
  "Austin, Jacob"
  "Odena, Augustus"
  "Nye, Maxwell"
  "Bosma, Maarten"
  "Michalewski, Henryk"
  "Dohan, David"
  "Jiang, Ellen"
  "Cai, Carrie"
  "Terry, Michael"
  "Le, Quoc"
  "Sutton, Charles"
]
```

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Maintainer

Google Research official mbpp data directory

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Funders

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

核验状态：待核实

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Design goals

### 测量能力

Generate basic Python programs from short natural-language requirements, and check functionality with execution results.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 设计动机

Studying program synthesis, prompting, and fine-tuning in pretrained models of different scales requires introductory tasks that are diverse and executable.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Construction

### 材料来源

Crowdsourced tasks; each question has a text description, Python reference code, and 3 assertion tests.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 命题与标注背景

Internal crowd workers with basic Python, who may use internet resources.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Review process

Internal crowd workers write the problem statement, a reference function, and three tests; the authors manually check, edit, and trim some problems, standardize function signatures, remove ambiguity, and align the tests with the description.

Sources: [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  )

### Quality control

After manual revision in §2.1 of the original paper there are 426 questions; the current HF sanitized set has 427 questions (120+257+43+7). All reference code passes its tests under Python3.6; passing only three tests does not guarantee semantic correctness for every input. The count in the paper and the count in the hosted snapshot are listed side by side and are not rewritten as one version.

Sources: [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  ) ; [https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md](https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md) (accessed 2026-11-08  )

### 去污染与留出

The original paper found that 32 of 974 questions matched pretrained samples on more than half of their lines of code; this was an overlap check for the models of that time, not a proof of cleanliness today.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Data format

### 规模与统计对象

As read from the official files: the original mbpp.jsonl has 974 questions, and sanitized-mbpp.json has 427 questions; they are not two independent benchmarks.

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/mbpp.jsonl](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/mbpp.jsonl) (accessed 2026-11-07  ) ; [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/sanitized-mbpp.json](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/sanitized-mbpp.json) (accessed 2026-11-07  )

### 题型与字段

Text to a Python function, with assertion tests and a reference program.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Modalities

```json
[
  "文本"
  "代码"
]
```

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### Languages

Python (the execution environment in the original paper is Python 3.6); the tasks are in English.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 难度与覆盖

Intended for basic programming; not contest programming or repository-level software engineering.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 公开/私有与数据划分

full: train374, test500, validation90, and prompt10. sanitized: train120, test257, validation43, and prompt7. The original README uses ID11–510 as test, 1–10 as prompts, 511–600 as validation, and 601–974 as training. sanitized inherits the ID grouping. An example left in the HF body text calls both the full package 974/427 test, which is not the same as the actual split metadata.

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  ) ; [https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md](https://huggingface.co/datasets/google-research-datasets/mbpp/raw/main/README.md) (accessed 2026-11-08  )

## Evaluation

### Metrics

Functional correctness; the per-sample pass proportion must be distinguished from solving at least once among multiple samples.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 评分与聚合

The generated program is run and the assertions are checked; the original tests are few and cannot replace the strengthened tests of MBPP+.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 提示与推理预算

The three example IDs in the original paper are 2, 3, and 4; the code is delimited by [BEGIN]/[DONE], temperature=0.5, and 80 program segments are sampled per question. The rate at which a task is solved and the correctness rate of a single sample are reported separately.

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  ) ; [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  )

### 官方实现

https://github.com/google-research/google-research/tree/master/mbpp

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 可比性边界

The original 974, test 500, sanitized 427, and EvalPlus evaluation 399 have different denominators; they cannot be ranked side by side.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Current status

### 核验时间

2026-11-08

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  )

### 当前数据与协议

```json
{
  "version": "The original 974 questions; the sanitized subset must be noted separately"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1"
      "date": "2026-09-23"
      "note": "Hunyuan-A13B §4.1/§4.2 and Tables 2–4 actually report MBPP; CRUX-I/O is kept as the same CRUXEval entry and is not split for counting."
    }
  ]
}
```

Note: Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

Sources: [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08  ) ; [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 论文修订与延续使用证据

Submission history From: Augustus Odena [ view email ] [v1] 2021-08-16 12:57:30 (2,247 KB)

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 饱和判断边界

Saturation is not declared from heterogeneous results: the 59.6% in the original paper is the proportion, among 500 questions, for which at least one success occurs in 80 samples, and it cannot be treated as pass@1; the later 83.86% comes from a vendor report at 3-shot, and the identifiers of the split are still insufficient.

Sources: [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08  )

### 污染、冲突与复现风险

A public and widely used basic question bank carries a risk of training overlap; the original small test set is limited by missed errors.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 衍生实现

MBPP sanitized and MBPP+ are subset or augmented derivatives and do not replace the original definition of MBPP.

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Leaderboard snapshot

### 访问快照日期

2026-11-08 (access; run and submission dates of each source are listed separately)

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  )

### 官方榜单入口

https://github.com/google-research/google-research/tree/master/mbpp

Sources: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp) (accessed 2026-11-07  )

### 第三方评测入口

Unverified

Note: Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

核验状态：待核实

Sources: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp) (accessed 2026-11-07  )

### 分来源、分协议结果

```json
[
  {
    "rank": null
    "model": "137B decoder-only Transformer (the largest model in the original paper)"
    "score": 59.6
    "unit": "%"
    "metric": "Proportion of tasks for which any of 80 samples passes all tests"
    "track": "Original paper / full test500 / 3-shot / 80 samples"
    "source_url": "https://arxiv.org/pdf/2108.07732"
    "accessed": "2026-11-08"
    "settings": "temperature 0.5; not pass@1"
    "result_type": "Historical original-paper result"
  }
  {
    "rank": null
    "model": "Hunyuan-Large-1116"
    "score": 72.6
    "unit": "%"
    "metric": "Accuracy"
    "track": "Hunyuan-A13B technical report Table 2 / MBPP / base model 3-shot"
    "source_url": "https://arxiv.org/html/2609.27284v1"
    "accessed": "2026-11-08"
    "benchmark_version": "The exact full/sanitized split is Unverified"
    "result_type": "Values self-reported or used for comparison by the authors of the report; not the official live MBPP leaderboard"
  }
  {
    "rank": null
    "model": "Qwen2.5-72B"
    "score": 76.0
    "unit": "%"
    "metric": "Accuracy"
    "track": "Hunyuan-A13B technical report Table 2 / MBPP / base model 3-shot"
    "source_url": "https://arxiv.org/html/2609.27284v1"
    "accessed": "2026-11-08"
    "benchmark_version": "The exact full/sanitized split is Unverified"
    "result_type": "Values self-reported or used for comparison by the authors of the report; not the official live MBPP leaderboard"
  }
  {
    "rank": null
    "model": "Qwen3-A22B"
    "score": 81.4
    "unit": "%"
    "metric": "Accuracy"
    "track": "Hunyuan-A13B technical report Table 2 / MBPP / base model 3-shot"
    "source_url": "https://arxiv.org/html/2609.27284v1"
    "accessed": "2026-11-08"
    "benchmark_version": "The exact full/sanitized split is Unverified"
    "result_type": "Values self-reported or used for comparison by the authors of the report; not the official live MBPP leaderboard"
  }
  {
    "rank": null
    "model": "Hunyuan-A13B"
    "score": 83.86
    "unit": "%"
    "metric": "Accuracy"
    "track": "Hunyuan-A13B technical report Table 2 / MBPP / base model 3-shot"
    "source_url": "https://arxiv.org/html/2609.27284v1"
    "accessed": "2026-11-08"
    "benchmark_version": "The exact full/sanitized split is Unverified"
    "result_type": "Values self-reported or used for comparison by the authors of the report; not the official live MBPP leaderboard"
  }
]
```

核验状态：待核实

Sources: [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08  )

### 快照覆盖说明

The original repository provides the data and the paper. It is not presented as a continuously maintained official overall score leaderboard. The original paper's 80-sample results and the full-row MBPP comparisons from the 2026 report are newly added, and they are tracked separately by source and sampling protocol. The exact test split of every Hunyuan report value remains Unverified.

核验状态：待核实

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  ) ; [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08  )

## Contact

### 官方公开联系邮箱

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

核验状态：待核实

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 项目反馈入口

https://github.com/google-research/google-research/issues

Note: Public repository feedback entry point; no question was sent.

Sources: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp) (accessed 2026-11-07  )

### 公开社交渠道

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

核验状态：待核实

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

### 联系信息原则

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

核验状态：待核实

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  )

## Original files

### 原始论文/技术报告PDF

https://arxiv.org/pdf/2108.07732

Sources: [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732) (accessed 2026-11-08  ) ; [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  )

### PDF SHA-256

820a8de4a9fe8aef947a40d5da13db0d660baf3658b4a9cebf6d30ac5ba351ab

Note: Original bytes downloaded from arXiv. This does not mean an older file was replaced.

Sources: [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  )

### PDF原始字节数

1540169

Sources: [https://arxiv.org/pdf/2108.07732](https://arxiv.org/pdf/2108.07732) (accessed 2026-11-08  )

### 资料夹

```json
{
  "id": "1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB"
  "webViewLink": "
}
```

Sources: [  )

### 其他官方资料

```json
[
  {
    "type": "Chinese-language introductory Google Doc"
    "id": "18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw"
    "webViewLink": "
  }
]
```

Note: The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp) (accessed 2026-11-07  ) ; [  )

### 已存PDF

```json
{
  "id": "1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P"
  "webViewLink": "
}
```

Sources: [  )

## Changelog

### Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]
```

核验状态：待核实

Sources: [https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md) (accessed 2026-11-08  )
