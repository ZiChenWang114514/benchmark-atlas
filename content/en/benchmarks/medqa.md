# MedQA

> Benchmark Constitution, in-depth review 2026-11-08. The access date is not the date the experiment was run; dates from historical sources keep their original record.

MedQA organizes medical licensing examination questions from the United States, mainland China, and Taiwan into question answering in English, Simplified Chinese, and Traditional Chinese, and it provides textbook retrieval corpora. The original trilingual test and later implementations that use four USMLE options, sampling, or bias injection must be described separately. Any one high score cannot be generalized directly to an ability to provide clinical care.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08); [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08)

## Basic information

### Short name

MedQA

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Full name

MedQA

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 版本与作用域

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

核验状态：待核实

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 论文/报告版本

arXiv v1（2020-09-28 14:07:51 ）

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 首次公开日期

2020-09-28 14:07:51 (arXiv v1; not an inferred first data-release time)

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Section

Biology and medicine

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

Sources: [https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1) (accessed 2026-11-08  )

### Subfields

```json
[
  "Medical-licensing-exam-style clinical reasoning"
]
```

Sources: [https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1) (accessed 2026-11-08  )

### 许可与权利边界

The LICENSE at the root of the repository is MIT (2022 Di Jin), but it does not cover every upstream right in the medical textbooks; §3.2 of the original paper states that the textbooks are released only under a research-use-only agreement. The BigBio mirror on HF lists the data license as unknown. The three scopes are set side by side, and MIT is not reduced to a claim that the whole package of textbooks may be used commercially at will.

Sources: [https://raw.githubusercontent.com/jind11/MedQA/master/LICENSE](https://raw.githubusercontent.com/jind11/MedQA/master/LICENSE) (accessed 2026-11-08  ) ; [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  ) ; [https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md](https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md) (accessed 2026-11-08  )

### 论文/报告入口

https://arxiv.org/abs/2009.13081

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Code

https://github.com/jind11/MedQA

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Dataset

https://github.com/jind11/MedQA

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Official homepage

https://github.com/jind11/MedQA

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 论文/报告标题

What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

## Origin and maintenance

### 研究发起团队

Research team on the paper: jointly signed by MIT CSAIL and Tongji Medical College, Huazhong University of Science and Technology; an institutional legal agreement to initiate the work is not inferred.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### 合作研究机构与顾问

```json
[
  "MIT CSAIL"
  "Tongji Medical College, Huazhong University of Science and Technology"
]
```

Note: Only jointly credited affiliations are treated as collaborating research institutions.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### Authors

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

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Maintainer

jind11/MedQA official repository.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### Funders

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

核验状态：待核实

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

## Design goals

### 测量能力

Multiple choice in the style of a medical licensing examination, combining clinical knowledge, case reasoning, and retrieval of external evidence.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 设计动机

Reading comprehension that extracts an answer from a given short passage can hardly stand for open-domain question answering that must retrieve multiple medical sources.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

## Construction

### 材料来源

Medical qualification examination questions from the United States, mainland China, and Taiwan, and related corpora of medical textbooks and documents.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 命题与标注背景

The paper is joint work by MIT computer researchers and authors from Tongji Medical College; the data are professional medical licensing examinations and practice questions. The paper additionally uses two physicians to review retrieved evidence, and they are not mistaken for the setters of all the original questions.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### Review process

Duplicate questions are removed, and questions are randomly split 80%/10%/10% into train, dev, and test; for USMLE and MCMLE the options are shuffled and one incorrect option is deleted at random to obtain a four-option version. The two physicians in the paper review whether the evidence is sufficient in the top 25 retrieved passages of 100 random dev questions, not a dual medical review of the full data.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### Quality control

Multilingual data with a fixed split; the paper analyzes retrieval noise and failures of multi-evidence reasoning.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 去污染与留出

Public examinations and the GitHub test set carry a risk of training exposure; the original split from 2020 cannot prove that models in 2026 are free of contamination.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

## Data format

### 规模与统计对象

English 12,723, Simplified Chinese 34,251, and Traditional Chinese 14,123 questions; the three languages total 61,097 (summed from the itemized counts in the original paper).

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 题型与字段

Multiple choice on cases or medical knowledge; the original version and the processed 4-option versions for the US and the mainland must be kept separate.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  ) ; [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA) (accessed 2026-11-07  )

### Modalities

Text stems, options, and answers; QA is saved line by line as JSONL, and each line is one dict; English and Simplified Chinese textbook retrieval corpora are attached.

Sources: [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08  )

### Languages

```json
[
  "英语"
  "Simplified Chinese"
  "Traditional Chinese"
]
```

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 难度与覆盖

A professional medical examination; not equivalent to a real clinical workflow or to a validation of safety.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 公开/私有与数据划分

Table 3 of the original paper: USMLE train10,178/dev1,272/test1,273; MCMLE train27,400/dev3,425/test3,426; TWMLE train11,298/dev1,412/test1,413. Both the original data and the 4_options processed version must be marked. The trilingual splits are public. This is not a unified hidden medical test.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08); [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08)

## Evaluation

### Metrics

Accuracy: the selected answer matches the standard answer.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 评分与聚合

The original paper combines a retriever and a reader, and closed-book selection is also possible; retrieval and open-book are kept separate from closed-book.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 提示与推理预算

The original paper does not use one unified modern LLM prompt; later models must state 4/5 options, CoT, shot, retrieval, and the test subset.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 官方实现

https://github.com/jind11/MedQA

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 可比性边界

The three languages, the number of options, the tools, and the subsets must be consistent; a high score on a medical examination does not mean clinical effectiveness or safety.

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

## Current status

### 核验时间

2026-11-08

Sources: [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08  )

### 当前数据与协议

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

核验状态：待核实

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 论文修订与延续使用证据

```json
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.19029v1"
      "date": "2026-08-19"
      "note": "Adaptive Memory and Reflection Multi-Agent System actually evaluates medical question answering on MedQA."
    }
  ]
  "evidence_boundary": "A citation is not a rerun; this page keeps the historical experiments in the paper separate from the current leaderboard."
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

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1) (accessed 2026-11-08  )

### 饱和判断边界

Vals archives it explicitly on the ground that scores are saturated under that institution's protocol of sampling a 2000-question USMLE source and of injecting bias, and it stops the evaluation of new models. The page was updated on 2026-04-16. That conclusion applies only to its evaluation. It does not mean that every test in the original trilingual MedQA has been solved under the same protocol.

Sources: [https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa) (accessed 2026-11-08  )

### 污染、冲突与复现风险

The original question set has been public since 2020, and Vals notes explicitly that it may have been used for model pretraining; the bias-injection questions are not public. The scopes must be distinguished: textbooks in the original paper are limited to research use, the BigBio license is unknown, and the repository is MIT. The AMR narrative gives feedback question by question, but the experiment says that retrieval is frozen and that test feedback is not written back. Only the authors' self-reported results are kept, and they are not made into a unified SOTA.

Sources: [https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa) (accessed 2026-11-08  ) ; [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  ) ; [https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md](https://huggingface.co/datasets/bigbio/med_qa/raw/main/README.md) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1) (accessed 2026-11-08  )

### 衍生实现

The official release also provides a processed 4_options version for the United States and mainland China; it must not be ranked together or compared directly with the original-option version.

Sources: [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08  )

## Leaderboard snapshot

### 访问快照日期

2026-11-08 (access; run and submission dates of each source are listed separately)

Sources: [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08  )

### 官方榜单入口

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

核验状态：待核实

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 第三方评测入口

https://www.vals.ai/benchmarks/medqa

Note: A 2000-question evaluation drawn from the USMLE, run independently by Vals and now archived; it is not the original official test of 1273 questions.

Sources: [https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa) (accessed 2026-11-08  )

### 分来源、分协议结果

```json
[
  {
    "rank": null
    "model": "BioBERT-Large"
    "score": 36.7
    "unit": "%"
    "metric": "Accuracy"
    "track": "Original paper Table 7/8 / USMLE test1273 / English"
    "source_url": "https://arxiv.org/pdf/2009.13081"
    "accessed": "2026-11-08"
    "result_type": "Original historical baseline; textbook retrieval + reader"
  }
  {
    "rank": null
    "model": "BioBERT-Large"
    "score": 42.0
    "unit": "%"
    "metric": "Accuracy"
    "track": "Original paper, Tables 7/8 / TWMLE test1413 / Traditional Chinese translated into English."
    "source_url": "https://arxiv.org/pdf/2009.13081"
    "accessed": "2026-11-08"
    "result_type": "Original historical baseline; textbook retrieval + reader"
  }
  {
    "rank": null
    "model": "RoBERTa-Large-WWM-ext"
    "score": 70.1
    "unit": "%"
    "metric": "Accuracy"
    "track": "Original paper Table 7/8 / MCMLE test3426 / Simplified Chinese"
    "source_url": "https://arxiv.org/pdf/2009.13081"
    "accessed": "2026-11-08"
    "result_type": "Original historical baseline; textbook retrieval + reader"
  }
  {
    "rank": 1
    "model": "o1"
    "score": 96.52
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 2
    "model": "GPT 5.1"
    "score": 96.38
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 3
    "model": "Gemini 3.1 Pro Preview (02/26)"
    "score": 96.37
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 4
    "model": "GPT 5"
    "score": 96.32
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 5
    "model": "GPT 5.4 (xhigh)"
    "score": 96.09
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 6
    "model": "o3"
    "score": 96.06
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 7
    "model": "GPT 5 Mini"
    "score": 96.06
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 8
    "model": "Gemini 3 Pro (11/25)"
    "score": 96.03
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 9
    "model": "o4 Mini"
    "score": 96.02
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": 10
    "model": "Claude Opus 4.5 (Thinking)"
    "score": 95.88
    "unit": "%"
    "metric": "Accuracy"
    "track": "Vals archived evaluation / a sample of 2000 questions from USMLE sources, and a bias study."
    "source_url": "https://www.vals.ai/benchmarks/medqa"
    "accessed": "2026-11-08"
    "source_date": "2026-04-16"
    "result_type": "An evaluation by an independent organization; which table rows correspond to the unbiased and the biased aggregation is Unverified"
  }
  {
    "rank": null
    "model": "AMR (GPT-4o)"
    "score": 93.2
    "unit": "%"
    "metric": "Accuracy"
    "track": "AMR paper / official USMLE test / train retrieval frozen."
    "source_url": "https://arxiv.org/html/2608.19029v1"
    "accessed": "2026-11-08"
    "source_date": "2026-08-19"
    "settings": "The specific GPT-4o API snapshot and the complete sample list are Unverified"
    "result_type": "Self-reported by paper authors"
  }
]
```

核验状态：待核实

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  ) ; [https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1) (accessed 2026-11-08  )

### 快照覆盖说明

Three sources that are not mixed: the trilingual historical baselines in the original paper, the top 10 of the archived Vals leaderboard, and self-reports in the AMR paper. The Vals methods description states a sample of 2000 questions and injection of five types of bias, which differs from the original USMLE test1273. Whether a table row corresponds to the unbiased baseline or to aggregation across multiple groups remains Unverified, so the source's original Accuracy label and that boundary are retained. The Vals archive cannot be treated as a continuously live official leaderboard.

核验状态：待核实

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  ) ; [https://www.vals.ai/benchmarks/medqa](https://www.vals.ai/benchmarks/medqa) (accessed 2026-11-08  ) ; [https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1) (accessed 2026-11-08  )

## Contact

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

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 项目反馈入口

https://github.com/jind11/MedQA/issues

Sources: [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA) (accessed 2026-11-07  )

### 公开社交渠道

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

核验状态：待核实

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 联系信息原则

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

核验状态：待核实

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

## Original files

### 原始论文/技术报告PDF

https://arxiv.org/pdf/2009.13081

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  ) ; [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### PDF SHA-256

5e19522f21c0ab5c24cc0dacd3feaa5d4b7057391520075f2e521a271d062ee6

Note: Original bytes downloaded from arXiv. This does not mean an older file was replaced.

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### PDF原始字节数

189006

Sources: [https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081) (accessed 2026-11-08  )

### 资料夹

```json
{
  "id": "1AYwJpnQXewH8Hk2KHLsemGjydd3Fvco0"
  "webViewLink": "
}
```

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

### 其他官方资料

```json
[
  {
    "type": "Chinese introduction"
    "id": "1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE"
    "webViewLink": "https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit"
  }
]
```

Sources: [https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit](https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit) (accessed 2026-11-07  )

### 已存PDF

```json
{
  "id": "1zmvFZ0lC8HCOh62LXlOrjcHf25kzF4gZ"
  "webViewLink": "
}
```

Sources: [https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081) (accessed 2026-11-08  )

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

Sources: [https://raw.githubusercontent.com/jind11/MedQA/master/README.md](https://raw.githubusercontent.com/jind11/MedQA/master/README.md) (accessed 2026-11-08  )
