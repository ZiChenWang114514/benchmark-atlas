# MMMLU

> Verification date: 2026-11-08. Unknowns are not filled in; the date on which the source was accessed is not the experiment run date.

OpenAI extended the MMLU test questions to 14 non-English languages by professional human translation. The core use is to compare the cross-language availability of the same kind of subject knowledge, not to write a new and harder MMLU question bank. All 14 CSVs were downloaded at a fixed HF commit: 14042 rows and 57 subjects per language, 196588 translated items in total. The HF viewer's aggregate count of 393176 repeats the default configuration and each language configuration, and it cannot be treated as an independent question count.
[Guide basis for this page](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md) (accessed 2026-11-08)

[Supplementary reading basis](https://huggingface.co/datasets/openai/MMMLU) (accessed 2026-11-08)

## Basic information

### Short name

MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Full name

Multilingual Massive Multitask Language Understanding

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 数据/基准版本

```json
{
  "release_name": "MMMLU (semantic version number not listed separately)"
  "hf_revision": "325a01dc3e173cac1578df94120499aaca2e2504"
}
```

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### Paper version

What is linked is the MMLU source-question paper, arXiv v3 (2021-01-13 03:57:11); an independent MMMLU paper and its version are Unverified.

> 状态：待核实。

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### Release date

The HF repository was created at 2024-09-14 01:37:19; this is not a confirmed official first-release time for MMMLU, and the official release date is Unverified.

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Section

Language

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### Subfields

Multilingual multidisciplinary knowledge

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 许可边界

MIT (as stated on the official OpenAI dataset card)

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2009.03300

> This is a link to the parent MMLU paper and does not prove that an independent MMMLU paper exists.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 代码入口

https://github.com/openai/simple-evals

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Dataset

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Official homepage

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Paper title

Parent-item paper: Measuring Massive Multitask Language Understanding; an independent MMMLU paper is Unverified.

> 状态：待核实。

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## Origin and maintenance

### Initiators

OpenAI official dataset.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Partner organizations

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Authors

The data release is signed by OpenAI; the dataset card does not list the individual translators or the authors of an independent MMMLU paper, and the list of individuals is Unverified.

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### Current maintainer

OpenAI (the official data-release namespace openai/MMMLU).

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Funders

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## Design goals

### Abilities measured

Tests multilingual general-knowledge ability through professional human translation, with particular attention to translation quality for low-resource languages.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 设计动机

Testing only English cannot reflect cross-language performance; the quality of machine-translated questions may affect evaluation of low-resource languages.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## Construction

### Question sources

Professional human translation of the original MMLU test set into 14 languages, covering the 57 subjects of the original MMLU.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 出题/构建者背景

The MMLU test set was translated by professional human translators, not by machine translation.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Review process

Professional human translation, which the official source says can raise confidence in translation accuracy for low-resource languages; review of each item and the double-blind proofreading process are Unverified.

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### Quality control

The human translations cover the same MMLU test tasks; this check of the files finds 14042 rows and 57 subjects for every language. An unnamed index column repeats within each subject and cannot serve as a global question ID; the subject order and the index order of SW-KE, YO-NG, and AR-XY are not fully the same, and the original question must be checked before items are paired, rather than joining directly by row number.

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv)（访问 2026-11-08）；[来源4](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv)（访问 2026-11-08）

### 去污染/泄漏控制

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## Data format

### 精确规模与统计口径

```json
{
  "base_test_items_per_locale": 14042
  "translated_locales": 14
  "total_translation_rows": 196588
  "subjects_per_locale": 57
  "hf_viewer_aggregate_rows": 393176
  "count_method": "The 14 CSVs of one HF revision were downloaded one by one, and csv.DictReader and pandas.read_csv were each used as a check. The default configuration sums every language, and the viewer then counts each language configuration again. The figure 393176 is not a count of independent questions."
}
```

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv)（访问 2026-11-08）；[来源4](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_BN-BD.csv)（访问 2026-11-08）；[来源5](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_DE-DE.csv)（访问 2026-11-08）；[来源6](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ES-LA.csv)（访问 2026-11-08）；[来源7](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_FR-FR.csv)（访问 2026-11-08）；[来源8](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_HI-IN.csv)（访问 2026-11-08）；[来源9](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ID-ID.csv)（访问 2026-11-08）；[来源10](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_IT-IT.csv)（访问 2026-11-08）；[来源11](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_JA-JP.csv)（访问 2026-11-08）；[来源12](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_KO-KR.csv)（访问 2026-11-08）；[来源13](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_PT-BR.csv)（访问 2026-11-08）；[来源14](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv)（访问 2026-11-08）；[来源15](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv)（访问 2026-11-08）；[来源16](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ZH-CN.csv)（访问 2026-11-08）

### Question types

Four-option knowledge question

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Modalities

Text

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 语言/代码语种

阿拉伯语；孟加拉语；德语；西班牙语；法语；印地语；Indonesian；意大利语；日语；韩语；Brazilian Portuguese；斯瓦希里语；约鲁巴语；简体中文

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 难度结构

Follows MMLU, from foundational to professional subjects; translation is not a new difficulty level.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### Public and hidden splits

The official card lists 14 language configurations, all of them public test/*.csv test files; these test files are not treated as a training set.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## Evaluation

### Metrics

Accuracy on multiple-choice questions; the language and the method of aggregating across languages must be stated.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 评分规则

After answers are normalized, a regular expression over multilingual answers extracts the letter. A match to the Answer column scores 1, and otherwise 0; within one language, scores are aggregated at the sample level. Any further pooling across languages must be declared separately.

[来源1](https://github.com/openai/simple-evals/blob/main/mmlu_eval.py)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/common.py)（访问 2026-11-08）

### 运行与提示设置

The official MMLUEval(language=...) loads the CSV of the corresponding language; each question is zero-shot CoT, and the last line is required to be Answer: A/B/C/D; language defaults to EN-US, and a run on a translated set must name the language explicitly. Sampling for num_examples uses Random(0).

[来源1](https://github.com/openai/simple-evals/blob/main/mmlu_eval.py)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/common.py)（访问 2026-11-08）；[来源3](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）

### Official evaluation scripts

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### 可比性警示

MMMLU is OpenAI’s dataset of MMLU in professional human translation, not MMLU-ProX; the 14 translated languages should not be miswritten as 14 languages that include the original English.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## Current status

### Date checked

2026-11-08

> Access date of the source site for this visit; not the leaderboard run date.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "hf_revision": "325a01dc3e173cac1578df94120499aaca2e2504"
  "last_modified_kst": "2024-10-17"
  "scope": "A public HF translation of MMMLU, not a new version of MMLU"
}
```

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "scope": "A revision of the paper for the MMLU parent questions; it is not presented as an independent MMMLU paper"
  "revisions": [
    {
      "version": "v1"
      "date_kst": "2020-09-08"
    }
    {
      "version": "v2"
      "date_kst": "2020-09-21"
    }
    {
      "version": "v3"
      "date_kst": "2021-01-13"
    }
  ]
  "mmmlu_repository_last_modified_kst": "2024-10-17"
}
```

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 饱和性证据

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 污染与已知争议

Human translation is not the same as decontamination of the original questions. The figure 393176 shown on the HF card is an aggregate count across configurations and cannot be treated as the original question count. simple-evals stopped updating new models and new scores in July 2025. Its English MMLU table cannot be treated as a multilingual MMMLU leaderboard.

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）

### 衍生与条目关系

MMMLU is a release of MMLU in human translation across 14 languages; it is not treated as the same version as MMLU-ProX, Global-MMLU, or English MMLU.

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### 本次榜单采集日

2026-11-08

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 官方榜源

https://huggingface.co/datasets/openai/MMMLU

> When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 第三方覆盖

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Jev research Table 2: retest group in this study / MMMLU in 14 languages

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Gemini 3.8 Flash | 92.6 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 2 | Qwen3.8-Max | 90.3 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 3 | DeepSeek-V4.1-Flash | 88.8 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 4 | Qwen3.8-Flash | 88.3 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 5 | Claude Opus 5.5 | 87.2 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 6 | GPT-5.6 Sol | 85.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 6 | Jev | 85.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |

- A finite set of answer choices; one run per model; model labels are kept as in the original paper

- A third-party research re-evaluation; not the official unified OpenAI leaderboard

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 覆盖范围与限制

Jev Table 2 was reread and expanded to the 7 entries actually measured in this study. The representative-model and small-model portions cite historical scores under different protocols and are not merged into this track. The official HF card does not give a unified live leaderboard. English MMLU scores in simple-evals are not moved over as MMMLU.

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源3](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）

## Contact

### 公开研究邮箱

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 项目反馈入口

https://github.com/openai/simple-evals/issues

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### 官方公开社交入口

Unverified

> 状态：待核实。

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 公开渠道/隐私边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2009.03300

> The PDF was downloaded again, read, and verified to have a matching hash; this archive is the paper of the MMLU parent items and is not labeled as an independent MMMLU paper.

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF SHA-256

d3a7b0f8589f5365ebfd34a3876a9a8b3fde83e0adb9ed19ccf8f0034bb48fc1

> SHA-256 of the originally downloaded bytes. They were not compressed or rewritten.

[来源1](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF bytes

2074939

[来源1](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### Folder

```json
{
  "id": "1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

### 其他官方文档

```json
[
  {
    "kind": "Chinese introduction"
    "id": "1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g"
    "webViewLink": "
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/abs/2009.03300"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/html/2610.11978v1"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/pdf/2009.03300"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://github.com/openai/simple-evals/blob/main/README.md"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://github.com/openai/simple-evals/blob/main/common.py"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://github.com/openai/simple-evals/blob/main/mmlu_eval.py"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_BN-BD.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_DE-DE.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ES-LA.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_FR-FR.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_HI-IN.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ID-ID.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_IT-IT.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_JA-JP.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_KO-KR.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_PT-BR.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ZH-CN.csv"
    "accessed": "2026-11-08"
  }
]
```

[来源1]( 2026-11-07）；[来源2](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源3](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源5](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）；[来源6](https://github.com/openai/simple-evals/blob/main/common.py)（访问 2026-11-08）；[来源7](https://github.com/openai/simple-evals/blob/main/mmlu_eval.py)（访问 2026-11-08）；[来源8](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源9](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源10](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源11](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv)（访问 2026-11-08）；[来源12](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_BN-BD.csv)（访问 2026-11-08）；[来源13](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_DE-DE.csv)（访问 2026-11-08）；[来源14](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ES-LA.csv)（访问 2026-11-08）；[来源15](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_FR-FR.csv)（访问 2026-11-08）；[来源16](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_HI-IN.csv)（访问 2026-11-08）；[来源17](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ID-ID.csv)（访问 2026-11-08）；[来源18](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_IT-IT.csv)（访问 2026-11-08）；[来源19](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_JA-JP.csv)（访问 2026-11-08）；[来源20](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_KO-KR.csv)（访问 2026-11-08）；[来源21](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_PT-BR.csv)（访问 2026-11-08）；[来源22](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv)（访问 2026-11-08）；[来源23](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv)（访问 2026-11-08）；[来源24](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ZH-CN.csv)（访问 2026-11-08）

### 原始PDF

```json
{
  "id": "10nTX-hZcL0fXPaatAK5f_f47-_-daG2g"
  "webViewLink": "
}
```

> What is attached is the original MMLU paper cited by the data card, not a standalone MMMLU paper.

[来源1]( 2026-11-07）

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
    "timezone": " (, UTC+9)"
    Latest review
  }
]
```

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）
