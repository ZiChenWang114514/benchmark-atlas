# IFEval

> Benchmark Constitution, source-by-source in-depth check: 2026-11-08. The collection date does not represent the experiment date; Unverified is not the same as Not disclosed.

IFEval turns instructions such as length, keywords, and format into deterministic verification programs. It has four different accuracies: prompt-level and instruction-level, and strict and loose. The four baselines from the original authors are restored, so that a vendor total whose metric is not stated does not hide the differences.

Basis of the reading guide: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08); [2](https://github.com/google-research/google-research/tree/master/instruction_following_eval) (accessed 2026-11-08); [3](https://huggingface.co/datasets/google/IFEval) (accessed 2026-11-08).

## Basic information

### Short name

IFEval

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Full name

Instruction-Following Evaluation

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Benchmark version

The original paper has 541 prompts and 25 types of verifiable instruction; the official Google HF data card corresponds to the train split (for use in evaluation, and it does not represent advice to use the test prompts for training).

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08 ) ; [2](https://huggingface.co/datasets/google/IFEval) (accessed 2026-11-08).

### Paper version

arXiv v1

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08).

### Release date

2023-11-14 (date of the first arXiv draft; not the separate release date of the dataset).

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08).

### Section

Language

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 领域

```json
[
  "Verifiable instruction following"
]
```

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 许可与使用范围

The google-research repository is Apache-2.0; the official Google HF dataset card separately labels apache-2.0.

Sources: [1](https://github.com/google-research/google-research/blob/master/LICENSE) (accessed 2026-11-08 ) ; [2](https://huggingface.co/datasets/google/IFEval) (accessed 2026-11-08).

### 论文入口

https://arxiv.org/abs/2311.07911

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Code

https://github.com/google-research/google-research/tree/master/instruction_following_eval

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Dataset

https://huggingface.co/datasets/google/IFEval

> Google’s official HF release entry; the original code and JSONL remain in google-research/instruction_following_eval.

Sources: [1](https://huggingface.co/datasets/google/IFEval) (accessed 2026-11-08).

### Official homepage

https://github.com/google-research/google-research/tree/master/instruction_following_eval

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Paper title

Instruction-Following Evaluation for Large Language Models

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

## Origin and maintenance

### Initiators

The Google Research team; Jeffrey Zhou's research internship and Yale background are stated in the paper.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 合作与作者单位

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Authors

```json
[
  "Zhou, Jeffrey"
  "Lu, Tianjian"
  "Mishra, Swaroop"
  "Brahma, Siddhartha"
  "Basu, Sujoy"
  "Luan, Yi"
  "Zhou, Denny"
  "Hou, Le"
]
```

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Maintainer

Official public code is hosted at google-research; this records the repository maintenance entry point and is not used to infer institutional legal liability or an ongoing maintenance commitment.

Sources: [1](https://github.com/google-research/google-research/tree/master/instruction_following_eval) (accessed 2026-11-07).

### 资助与资源支持

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

## Design goals

### 测量能力

Instruction following is evaluated objectively through constraints that a program can check.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 与既有基准的差异

Human evaluation is expensive, and a model judge may be affected by bias; instructions that can be checked repeatably and deterministically are needed.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

## Construction

### Question sources

Base prompts are synthesized and 1–3 verifiable constraints are added, then unreasonable combinations are removed and the prompts are rewritten.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 出题者背景

The research team designed the constraints and the prompts; the questions do not depend on a domain-knowledge examination.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Review process

Every prompt is checked by hand, and unnatural or conflicting constraints are corrected.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Quality control

Strict and lenient judgments are both reported; the lenient version handles transformations such as format, but it may increase false positives.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 去污染与泄漏控制

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

## Data format

### 规模与统计口径

541 prompts and 25 classes of verifiable instructions.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Question types

Open-ended text generation under constraints such as output length, keywords, and format

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Modalities

Text

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Languages

English

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Difficulty

Constraint types, and their combination within the same prompt, increase difficulty; this is not a stratification of subject-knowledge difficulty.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### Public and hidden splits

Public official prompt data and a validation program; an independent hidden test set has not been verified.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

## Evaluation

### Metrics

prompt-level strict/loose accuracy and instruction-level strict/loose accuracy.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 评分规则

The official main program calls the strict check and the loose check separately and writes two JSONL files; prompt-level accuracy is the proportion of responses in which every instruction passes, and it should not be confused with the pass rate of a single instruction.

Sources: [1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/evaluation_main.py) (accessed 2026-11-07).

### 提示、采样与工具设置

Generate the response from the original prompt, then call the official checker; do not treat text cleaning used for scoring as the model truly meeting the original format.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 官方脚本

google-research/instruction_following_eval/evaluation_main.py. The inputs are the JSONL of the original instructions and a JSONL of model responses that contains prompt and response.

Sources: [1](https://raw.githubusercontent.com/google-research/google-research/master/instruction_following_eval/README.md) (accessed 2026-11-07).

### 可比性警告

prompt-level and instruction-level, and strict and loose, are four different metrics, and a score must say which one it is; loose cleaning also carries a risk of false positives.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

## Current status

### 核查时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08 ) ; [2](https://github.com/google-research/google-research/tree/master/instruction_following_eval) (accessed 2026-11-08).

### 最新数据状态

The official Google HF card shows 541 rows, and the 25 instruction types follow the original paper; no semantic version number was invented.

Sources: [1](https://huggingface.co/datasets/google/IFEval) (accessed 2026-11-08 ) ; [2](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08).

### 论文修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2023-11-14"
    "timezone": ""
  }
]
```

> The original arXiv UTC time has been converted; this does not constitute a dataset version change.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08).

### 饱和度与证据边界

In the original paper, GPT-4 prompt-strict is 76.89%; targeted IF-RLVR training in Table 3 of the later IFBench paper can reach IFEval 92.2 (the prompt-loose accounting of that paper). A high score and the limits on generalization from training on verifiable tasks need to be kept separate, and it cannot be claimed that every instruction-following ability is saturated.

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-08 ) ; [2](https://arxiv.org/pdf/2507.02833) (accessed 2026-11-08).

### 污染与已知问题

Constraints that a program can check cover only part of real ability to follow instructions; strict and loose results are not equivalent, and tolerance of format cannot be read as compliance in full.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 相关与衍生基准

IFBench is an independent benchmark of 58 OOD constraints. It extends the verification approach of IFEval rather than being a new version of the same question set; the current IFBench package is compatible with 25 classic IFEval verifiers.

Sources: [1](https://github.com/allenai/IFBench/blob/main/README.md) (accessed 2026-11-08).

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not a run date or a leaderboard-update date)

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-08 ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08).

### 官方结果入口

https://arxiv.org/abs/2311.07911

> When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 独立评测入口

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 结构化结果

```json
[
  {
    "rank": 1
    "model": "GPT-4"
    "score": "76.89"
    "metric": "prompt-level strict accuracy (%)"
    "track": "Author paper Table 3 / prompt-level strict"
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "PaLM 2 S"
    "score": "43.07"
    "metric": "prompt-level strict accuracy (%)"
    "track": "Author paper Table 3 / prompt-level strict"
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "83.57"
    "metric": "instruction-level strict accuracy (%)"
    "track": "Authors paper, Table 3 / instruction-level strict."
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "PaLM 2 S"
    "score": "55.76"
    "metric": "instruction-level strict accuracy (%)"
    "track": "Authors paper, Table 3 / instruction-level strict."
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "79.30"
    "metric": "prompt-level loose accuracy (%)"
    "track": "Author paper Table 3 / prompt-level loose"
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "PaLM 2 S"
    "score": "46.95"
    "metric": "prompt-level loose accuracy (%)"
    "track": "Author paper Table 3 / prompt-level loose"
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "85.37"
    "metric": "instruction-level loose accuracy (%)"
    "track": "Paper by the authors, Table 3 / instruction-level loose."
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "PaLM 2 S"
    "score": "59.11"
    "metric": "instruction-level loose accuracy (%)"
    "track": "Paper by the authors, Table 3 / instruction-level loose."
    "source_url": "https://arxiv.org/pdf/2311.07911"
    "result_type": "Historical API baseline; GPT-4 in November 2023 and PaLM 2 S in August 2023, with the specific checkpoint not stated"
    "snapshot_date": "2026-11-08 "
  }
  {
    "model": "Hunyuan-A13B (the name used in the report)"
    "score": 84.7
    "unit": "%"
    "metric": "IF-Eval, original label in report Table 3"
    "scope": "Hunyuan-A13B technical report, slow-thinking; vendor-self-reported, and it does not state which of the four metrics in this entry it corresponds to, so it cannot be compared directly with prompt-strict in the paper."
    "evaluation_date": "Report date 2026-09-23; the exact run date is Unverified"
    "snapshot_date": "2026-11-07 (historical evidence retained; vendor reports were not reopened)"
    "track": "Hunyuan-A13B vendor technical report (mapping of the four metrics is unknown)"
    "rank": null
  }
]
```

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-08 ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08).

### 覆盖与局限

The exact metric baselines for the four sets in the original authors' paper are restored. They are not replaced by one vendor IF-Eval number whose strict or loose setting is not stated. The README of the original project is the entry point of the evaluation program, not a live SOTA leaderboard. Older vendor reports are kept, but they are not ranked across tracks.

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-08 ) ; [2](https://github.com/google-research/google-research/tree/master/instruction_following_eval/README.md) (accessed 2026-11-08).

## Contact

### 官方公开邮箱

```json
[
  "lehou@google.com"
]
```

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 仓库反馈

https://github.com/google-research/google-research/issues

Sources: [1](https://github.com/google-research/google-research/tree/master/instruction_following_eval) (accessed 2026-11-07).

### 官方社区

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07).

### 隐私与联系边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07).

## Original files

### Paper PDF

https://arxiv.org/pdf/2311.07911

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-07).

### PDF SHA-256

5d7cedfd762af6d9ad13d8768de64fa65895b8ebc3f5e454454c5ffbd48124f2

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-08).

### PDF bytes

```json
464152
```

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-08).

### 已有文件夹

```json
{
  "id": "1USyTVejz1q3o4ZVbGwBQVt4QDHXw0PJZ"
  "webViewLink": "
}
```

Sources: [1]( 2026-11-07).

### 其他官方文档

```json
[
  {
    "kind": "Chinese introduction"
    "id": "1EXunkoRqRKfRFViKuCIvLaQwApjkiWauYh-NTkz-9iU"
    "webViewLink": "
  }
]
```

Sources: [1]( 2026-11-07).

### 已有 PDF归档

```json
{
  "id": "1Nsrlsk4-LLFXvYCvPbWzRa7hHw_ZdJlM"
  "webViewLink": "
}
```

Sources: [1]( 2026-11-07).

## Changelog

### 历次核查

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

Sources: [1](https://arxiv.org/abs/2311.07911) (accessed 2026-11-07 ) ; [2](https://arxiv.org/pdf/2311.07911) (accessed 2026-11-07 ) ; [3](https://github.com/google-research/google-research/tree/master/instruction_following_eval) (accessed 2026-11-07 ) ; [4](https://arxiv.org/abs/2311.07911) (accessed 2026-11-08 ) ; [5](https://github.com/google-research/google-research/tree/master/instruction_following_eval) (accessed 2026-11-08).

