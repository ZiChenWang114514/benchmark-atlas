# TruthfulQA

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

TruthfulQA tests whether a model repeats misconceptions that are common among people. “Answering truthfully” and “answering informatively” are two different things. The original 817 questions, the current official CSV of 790 questions, and the two-choice setting of 2025 must be separated by version. The probability mass of MC2 is also not the accuracy of an ordinary single choice.

Source: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-08)

## Basic information

### Short name

TruthfulQA

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Full name

TruthfulQA: Measuring How Models Mimic Human Falsehoods

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md) (accessed 2026-11-07， )

### Benchmark version

The official README recommends the two-choice setting updated in January 2025; the original MC1, MC2, and the generation task need to be labeled separately.

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md) (accessed 2026-11-07， )

### Paper version

arXiv v2; submitted at 2022-05-08 11:43:02.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Release date

2021-09-09 02:15:27 (arXiv v1 submission; not the date of the 2025 two-choice revision)

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Section

Safety

Note: Benchmark Constitution editorial filing. This is not the only field named by the paper.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Field tags

- Hallucination induced by truthfulness and misconceptions

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 许可与适用范围

Apache-2.0 (official repository LICENSE; the license for external literature involved in the reference answers is to be checked separately).

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/LICENSE) (accessed 2026-11-07， )

### Paper

https://arxiv.org/abs/2109.07958

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Code repository

https://github.com/sylinrl/TruthfulQA

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 数据地址

https://github.com/sylinrl/TruthfulQA

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Official homepage

https://github.com/sylinrl/TruthfulQA

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Paper title

TruthfulQA: Measuring How Models Mimic Human Falsehoods

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

## Origin and maintenance

### 机构与发起关系

The authors are Stephanie Lin, Jacob Hilton, and Owain Evans, with affiliations involving Oxford and OpenAI; a formal agreement to launch the work jointly is not inferred here.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Partner organizations

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Authors

- Lin, Stephanie
- Hilton, Jacob
- Evans, Owain

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Current maintainer

Official code and feedback are provided by the sylinrl/TruthfulQA repository; individual responsibility for continued maintenance, and response-time limits, have not been verified.

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md) (accessed 2026-11-07， )

### 资助与支持

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

## Design goals

### Abilities measured

Tests whether the model repeats common human misconceptions, rather than looking only at the fluency of the answer.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Design background

Imitating internet text may learn popular errors; accuracy on knowledge question answering is not directly equivalent to avoiding misleading claims.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

## Construction

### 题目或数据来源

The authors wrote questions tied to common misconceptions; 437 items passed GPT-3 adversarial filtering, and 380 items were not filtered.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 出题背景

The research team wrote the questions and checked the answers, covering several everyday and professional domains.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Review process

Distinguishes truthfulness from informativeness; answers are checked by hand and an automatic judge is trained.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Quality control

Truthfulness and informativeness are measured together, so that an uninformative refusal is not mistaken for a useful factual answer.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 去污染与泄漏

The README contains a canary for exclusion from training and states that BIG-bench contains a smaller task from the same source; when the two are used to test each other, the other set must not be added to training. This is a constraint on use, not proof that contamination of model training has already been ruled out.

Sources: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， )

## Data format

### Size

The original paper has 817 questions and 38 categories; the official main/TruthfulQA.csv read this time actually has 790 rows, excluding the header, and includes a Best Incorrect Answer column. The traditional HF card is still 817 rows and belongs to the old protocol. 817 cannot replace the question count of the current CSV.

Sources: [1](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) (accessed 2026-11-08， ) ; [2](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， ) ; [3](https://huggingface.co/datasets/truthfulqa/truthful_qa/raw/main/README.md) (accessed 2026-11-08， ) ; [4](https://arxiv.org/pdf/2109.07958) (accessed 2026-11-08， )

### Question types

Two evaluation modes: open generation and multiple choice

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Modalities

Text

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Languages

English

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### Difficulty

Constructed specifically to elicit common misconceptions; adversarially filtered questions and unfiltered questions follow different distributions.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 数据划分

A public question set and reference correct and incorrect answers; results tuned on the test examples must not be treated as the original zero-shot results.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

## Evaluation

### Metrics

Generative tasks report both truthfulness and informativeness; MC1 is the accuracy of the single correct answer that has the highest answer log-probability, and MC2 is the sum of the normalized probabilities of the correct answers; the 2025 two-choice setting requires the order of the correct and incorrect options to be randomized.

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md) (accessed 2026-11-07， )

### Scoring

Generation tasks may use a human judge or GPT-judge; MC2 measures the normalized probability mass of the set of correct answers, not ordinary single-choice accuracy.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 提示与运行设置

The original paper is zero-shot and does not tune on examples from this benchmark; generation is greedy; prompt style significantly affects answers and refusals.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 评测脚本

https://github.com/sylinrl/TruthfulQA

Sources: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-07， )

### 可比性提醒

Answering only “I don’t know” may be judged true but uninformative; truthfulness, true+informative, MC1, and MC2 cannot be mixed in comparison.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

## Current status

### Date checked

2026-11-08

Sources: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， )

### 数据版本与更新

```json
{
  "version": "The README records a 2-choice update in January 2025; the exact commit is not pinned."
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2610.11978v1"
      "date": "2026-10"
      "note": "Tables 1 and 2 and Appendix A of the Jev study actually use TruthfulQA; MC2 and the accuracy of the selected answer are noted separately."
    }
  ]
}
```

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md) (accessed 2026-11-07， ) ; [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07， )

### 论文修订记录

- {"version": "v1", "submitted_at": "2021-09-09 02:15:27 ", "timezone": ""}
- {"version": "v2", "submitted_at": "2022-05-08 11:43:02 ", "timezone": ""}

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-08， )

### 饱和证据与局限

Different protocols cannot support one judgment of saturation. In the 2026-H2 Jev study, option accuracy for Gemini 3.8 Flash on 817 questions is 97.9%. That is not the score on the 790 two-choice questions of 2025, and it is not the proportion of generation tasks that are both truthful and informative.

Sources: [1](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-08， ) ; [2](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， )

### 争议与已知问题

The update of 2025 removes questions that no longer hold and the category Indexical Error: Time. The official source states explicitly that a full review of the remaining questions and of their sources is not yet finished. The current CSV of 790 items, the traditional HF set of 817 items, and the multiple-choice study in the paper are kept apart. “Truthfulness” is not the same as “being informative enough.”

Sources: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， ) ; [2](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) (accessed 2026-11-08， ) ; [3](https://huggingface.co/datasets/truthfulqa/truthful_qa/raw/main/README.md) (accessed 2026-11-08， )

### 衍生或后继基准

BIG-bench contains smaller tasks from the same source; in January 2025 the official release added a two-choice version, with the correct answer and the best incorrect answer randomly ordered as A/B, recommends the new setting, and keeps MC1 and MC2 valid.

Sources: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， )

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Source: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-08)

### 官方榜单入口

https://arxiv.org/abs/2109.07958

Note: When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-07， )

### 第三方入口

https://arxiv.org/html/2610.11978v1

Sources: [1](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-08， )

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Official README historical baseline / % true | 4 | GPT-3 175B | 20.44 | % true | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % info | 1 | GPT-3 175B | 97.55 | % info | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true (GPT-judge). | 4 | GPT-3 175B | 20.56 | % true (GPT-judge) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEURT | 4 | GPT-3 175B | -0.54 | BLEURT | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / ROUGE | 4 | GPT-3 175B | -17.17 | ROUGE | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEU | 4 | GPT-3 175B | -17.18 | BLEU | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC1 (0–1) | 2 | GPT-3 175B | 0.21 | MC1 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC2 (0–1) | 4 | GPT-3 175B | 0.33 | MC2 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true | 3 | GPT-J 6B | 26.68 | % true | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % info | 2 | GPT-J 6B | 89.96 | % info | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true (GPT-judge). | 3 | GPT-J 6B | 27.54 | % true (GPT-judge) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEURT | 3 | GPT-J 6B | -0.29 | BLEURT | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / ROUGE | 3 | GPT-J 6B | -10.93 | ROUGE | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEU | 3 | GPT-J 6B | -7.48 | BLEU | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC1 (0–1) | 3 | GPT-J 6B | 0.2 | MC1 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC2 (0–1) | 2 | GPT-J 6B | 0.36 | MC2 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true | 2 | GPT-2 1.5B | 29.5 | % true | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % info | 3 | GPT-2 1.5B | 89.84 | % info | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true (GPT-judge). | 2 | GPT-2 1.5B | 30.72 | % true (GPT-judge) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEURT | 2 | GPT-2 1.5B | -0.24 | BLEURT | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / ROUGE | 2 | GPT-2 1.5B | -9.02 | ROUGE | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEU | 2 | GPT-2 1.5B | -4.83 | BLEU | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC1 (0–1) | 1 | GPT-2 1.5B | 0.22 | MC1 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC2 (0–1) | 1 | GPT-2 1.5B | 0.39 | MC2 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true | 1 | UnifiedQA 3B | 53.86 | % true | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % info | 4 | UnifiedQA 3B | 64.5 | % info | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / % true (GPT-judge). | 1 | UnifiedQA 3B | 56.18 | % true (GPT-judge) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEURT | 1 | UnifiedQA 3B | 0.08 | BLEURT | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / ROUGE | 1 | UnifiedQA 3B | 1.92 | ROUGE | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / BLEU | 1 | UnifiedQA 3B | -0.17 | BLEU | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC1 (0–1) | 4 | UnifiedQA 3B | 0.19 | MC1 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Official README historical baseline / MC2 (0–1) | 3 | UnifiedQA 3B | 0.35 | MC2 (0–1) | README Baselines table; not a newly run 2025 two-choice score；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Jev research Table 2 / option accuracy on the original 817 questions | 1 | Gemini 3.8 Flash (original label in research Table 2) | 97.9 | selected-option accuracy (%) | 817-item evaluation; not MC2； | [2026-10-08 (date marked on the paper)](https://arxiv.org/html/2610.11978v1)；采集2026-11-08 |
| Jev research Table 2 / option accuracy on the original 817 questions | 2 | Claude Opus 5.5 (original label in research Table 2) | 92.0 | selected-option accuracy (%) | 817-item evaluation; not MC2； | [2026-10-08 (date marked on the paper)](https://arxiv.org/html/2610.11978v1)；采集2026-11-08 |
| Jev research Table 2 / option accuracy on the original 817 questions | 3 | Jev (original label in research Table 2) | 87.5 | selected-option accuracy (%) | 817-item evaluation; not MC2； | [2026-10-08 (date marked on the paper)](https://arxiv.org/html/2610.11978v1)；采集2026-11-08 |

Source: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-08)

### 榜单覆盖边界

The historical Baselines in the official README are the complete 4 models × 8 metrics, 32 rows, ranked by metric and not mixed together; the 3 option-accuracy entries from Table 2 of the Jev paper are also kept, and Appendix A makes clear that there are 817 questions and that this is not MC2. Questions whose version had not been specified are now filled in. There is no official current model leaderboard, newly verified in this reading, for the 2025 two-choice set of 790 questions.

Source: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

- sylin07@gmail.com

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-07， )

### 公开反馈渠道

https://github.com/sylinrl/TruthfulQA/issues

Note: Public feedback entry point; no question was sent.

Sources: [1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md) (accessed 2026-11-07， )

### 官方社交账号

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2109.07958) (accessed 2026-11-07， )

### 联系方式/隐私原则

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07， )

## Original files

### 原始PDF

https://arxiv.org/pdf/2109.07958

Sources: [1](https://arxiv.org/pdf/2109.07958) (accessed 2026-11-08， )

### PDF SHA-256

6e86175861d24d075bbd8fec987cbdabd0d6332700b001a1ccf335fa72f541b2

Sources: [1](https://arxiv.org/pdf/2109.07958) (accessed 2026-11-08， )

### PDF bytes

```json
819857
```

Sources: [1](https://arxiv.org/pdf/2109.07958) (accessed 2026-11-08， )

### Folder

```json
{
  "id": "1K67pMyWmwzHPTWfWS6Qbhpuz0ZhyOsLv"
  "webViewLink": "
}
```

Sources: [1]( 2026-11-07， )

### Other documents

- {"kind": "Chinese introduction", "id": "1Gd-3UCMu3Qp3aNooWo3Sq2Ar2Bo1hlC06er3pz1o26E", "webViewLink": "

Sources: [1]( 2026-11-07， )

### 论文原件

```json
{
  "id": "12HuAWYz_OBaC5-Hlk_sLg1mzUbeHUD1k"
  "webViewLink": "
}
```

Sources: [1]( 2026-11-07， )

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://github.com/sylinrl/TruthfulQA) (accessed 2026-11-08， )
