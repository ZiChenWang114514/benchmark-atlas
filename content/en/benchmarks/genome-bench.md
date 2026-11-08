# Genome-Bench

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

Genome-Bench is a text question-answering set that researchers at Princeton and Stanford converted from long-running CRISPR expert discussion, and it is entirely different from OpenAI's GeneBench and GeneBench-Pro. The routing-system scores in the paper come from multiple RL experts and cannot be treated as the independent score of a single small model.

Latest review

## Basic information

**简称**：Genome-Bench

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**全称**：Genome-Bench (genomics question answering accompanying RL4GenomeBench)

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**基准版本**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**论文版本**：v2; latest paper date 2025-06-02

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**发布日期**：2025-05-26 (date of the first arXiv version; not an inferred date on which the data went online).

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**主板块**：生物与医学

核验说明：The editorial section follows the selection list. It does not mean the benchmark measures only that section.

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07 )

**领域标签**：Genomics capability

Sources: [1](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07 )

**许可证与授权边界**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**论文或技术报告**：https://arxiv.org/abs/2505.19501

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**官方代码**：https://github.com/mingyin0312/RL4GenomeBench

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**数据地址**：https://huggingface.co/datasets/Mingyin0312/Genome-Bench

Sources: [1](https://raw.githubusercontent.com/mingyin0312/RL4GenomeBench/main/README.md) (accessed 2026-11-07 )

**官方主页**：https://github.com/mingyin0312/RL4GenomeBench

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**论文题名**：Toward Scientific Reasoning in LLMs: Training from Expert Discussions via Reinforcement Learning

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Origin and maintenance

**发起方**：A collaboration of paper authors at Princeton and Stanford.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**协作与机构边界**：Authors are jointly affiliated with Princeton University and Stanford University; the public README mentions the use of TRL, and the organization of a dependency library is not treated as a collaborating institution.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 ) ; [2](https://github.com/mingyin0312/RL4GenomeBench) (accessed 2026-11-07 )

**作者**：Ming Yin；Yuanhao Qu；Ling Yang；Le Cong；Mengdi Wang

核验说明：Surname and given-name inversions and spellings from an earlier author parse are corrected from the PDF title page.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**维护方**：The official mingyin0312/RL4GenomeBench repository.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**资助方**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Design goals

**测量能力**：Scientific reasoning and question answering on CRISPR and genome experiments, based on expert discussion; tool-free MCQ.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**相对既有评测的缺口**：Factual question answering from textbooks is not enough to reflect experimental design, fault diagnosis, and experiential knowledge in the expert community.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Construction

**题目来源**：Expert discussions and forum threads related to CRISPR; the official dataset_pipeline can parse .mbox mail archives and convert them to standard MCQ and QA formats.

Sources: [1](https://raw.githubusercontent.com/mingyin0312/RL4GenomeBench/main/README.md) (accessed 2026-11-07 )

**出题与研究背景**：The original community questions come from participants in experiments and genomics; the authors of the paper extract and clean the QA.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**审核流程**：GPT-4Turbo extracts QA/context, GPT-4o rewrites the items and builds distractors, and humans check them.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**质量控制**：Deduplication, removal of unanswered or off-topic content, randomized option order, and human quality checks.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**去污染与泄漏边界**：The source discussion is public; separating questions and answers does not guarantee that pretraining had no exposure, or that discussion of the same topic was fully isolated.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Data format

**规模与口径**：3,332 question-answer pairs, drawn from 11 years of discussion of genome-editing research; HF fixes train at 2,671 and test at 661, which must not be confused with the 103 and 129 questions of GeneBench.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 ) ; [2](https://huggingface.co/datasets/Mingyin0312/Genome-Bench/blob/main/README.md) (accessed 2026-11-07 )

**任务类型**：English 5-choose-1 science and experimental reasoning; this is not gene-sequence prediction or execution-based omics analysis.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**模态**：Plain-text questions, context, five options, and answers.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**语言**：英语。

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**难度**：Adapted from expert discussion; the original paper uses a seven-category task scope; a unified difficulty label is not fabricated.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**公开与隐藏划分**：Public train/test 2671/661, with fixed test accuracy.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Evaluation

**指标**：661-question test accuracy.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**评分方式**：The structured final-answer label is extracted and compared with the standard option.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**提示与运行设置**：The paper compares base/CoT/RL-Router, and the same prompt and routing/multi-expert settings must be retained.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**官方复现入口**：evaluation/genome-bench_eval.py (the test-set evaluation entry point in the official README).

Sources: [1](https://raw.githubusercontent.com/mingyin0312/RL4GenomeBench/main/README.md) (accessed 2026-11-07 )

**可比性警告**：The four-expert system of RL-Router differs from a single 7B model; this is not an overall leaderboard of general biological-analysis agent capability.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Current status

**本次核验**：2026-11-07

Sources: [1](https://github.com/mingyin0312/RL4GenomeBench) (accessed 2026-11-07 )

**数据及热度证据**：Public train/test snapshots under the default configuration (2671/661); the official HF card does not mark a semantic version number, and reproduction should pin the revision.

Sources: [1](https://huggingface.co/datasets/Mingyin0312/Genome-Bench/blob/main/README.md) (accessed 2026-11-07 )

**论文与版本历史**：```json
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.21074v1"
      "date": "2026-10-15"
      "note": "OmicsBench §2 explicitly lists Genome-Bench (Yin et al. 2025) as a prior benchmark for evaluating local biological ability; this is an H2 academic citation."
    }
  ]
  "evidence_boundary": "A citation is not a rerun; this page keeps the historical experiments in the paper separate from the current leaderboard."
  "paper_metadata": {
    "title": "Toward Scientific Reasoning in LLMs: Training from Expert Discussions via Reinforcement Learning"
    "authors": [
      "Yin, Ming"
      "Qu, Yuanhao"
      "Yang, Ling"
      "Cong, Le"
      "Wang, Mengdi"
    ]
    "release": "2025-05-26"
    "latest": "2025-06-02"
    "version": "v2"
  }
}
```

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 ) ; [2](https://arxiv.org/html/2610.21074v1) (accessed 2026-11-07 )

**饱和程度**：The historical best is 81.07%, and it is not the current upper bound for 2026; an updated live leaderboard has not been verified.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**已知问题与局限**：The source discussion and the question bank are public, and rewriting the answers does not remove semantic memorization; the sample size of 661 questions requires that error be considered.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**后续与衍生**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Leaderboard snapshot

**快照日期**：2026-11-07 (web-page collection date; not equal to the model experiment date)

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**官方入口**：https://github.com/mingyin0312/RL4GenomeBench

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**第三方入口**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| arXiv v2 Table 2 historical experiments | 1 | RL-Router (Qwen2.5-7B + four RL experts) | 81.07 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2 historical experiments | 2 | DeepSeek-R1 01-20-25 | 78.97 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2 historical experiments | 3 | Gemini-2.5-Pro exp-03-25 | 77.46 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2 historical experiments | 4 | Qwen2.5-7B RL-tuned | 76.85 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2 historical experiments | 5 | Claude-3.7-Sonnet 02-19-25 | 76.4 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：Tables 1 and 2 of the v2 PDF were read again to check the versions and the scores, and the original strings were changed into structured results. RL-Router is a routing system with four experts, and it cannot be treated as a single 7B model. The official README does not provide an updated unified live leaderboard, and SOTA for 2026 is not claimed.

Sources: [1](https://arxiv.org/abs/2505.19501v2) (accessed 2026-11-07 ) ; [2](https://github.com/mingyin0312/RL4GenomeBench) (accessed 2026-11-07 )

## Contact

**公开联系邮箱**：my0049@princeton.edu；yhqu@stanford.edu

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**Issues或讨论入口**：https://github.com/mingyin0312/RL4GenomeBench/issues

Sources: [1](https://github.com/mingyin0312/RL4GenomeBench) (accessed 2026-11-07 )

**官方社交**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**隐私政策**：待核实

状态：待核实。

核验说明：The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Original files

**原始PDF**：https://arxiv.org/pdf/2505.19501

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**PDF SHA-256**：ea37fbd1578b8906f5d975c28a63898f9139e3fcd4177bacc5d99f67dec2d9b3

核验说明：Byte count of the original downloaded PDF, not the size displayed on the arXiv page.

Sources: [1](https://arxiv.org/pdf/2505.19501) (accessed 2026-11-07 )

**PDF字节数**：```json
24536967
```

核验说明：Actual downloaded byte count; it does not mean the file was uploaded.

Sources: [1](https://arxiv.org/pdf/2505.19501) (accessed 2026-11-07 )

**文件夹**：```json
{
  "id": "1Ujb8zb_jipEtvQBq_eUglTPU4MJXlI04"
  "webViewLink": "
}
```

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

**其他官方文档**：```json
[
  {
    "type": "Chinese introduction"
    "id": "1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8"
    "webViewLink": "https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit"
  }
]
```

Sources: [1](https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit) (accessed 2026-11-07 )

**论文链接**：```json
{
  "id": "1zvsJcz5mzrqjItFIVfStqXqZHd-Kt_0r"
  "webViewLink": "
}
```

Sources: [1](https://arxiv.org/abs/2505.19501) (accessed 2026-11-07 )

## Changelog

**及历史变更**：```json
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
    "date": "2026-11-07"
    Latest review
  }
]
```

Sources: [1](https://github.com/mingyin0312/RL4GenomeBench) (accessed 2026-11-07 )

