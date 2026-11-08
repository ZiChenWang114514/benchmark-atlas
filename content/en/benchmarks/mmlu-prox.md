# MMLU-ProX

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MMLU-ProX在MMLU-Pro基础上提供29种语言的平行难题。Full的11,829及Lite的658都包含70条validation；实际test分别是11,759和588。翻译质量检查覆盖15种语言的固定抽样，而非所有29语每一道题都人工审校；跨语言差异仍可能混合语言能力、译文与文化因素。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

### Short name

MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Full name

MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Benchmark version

MMLU-ProX: full and Lite editions in 29 languages; official release record of 2025-05.

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### Paper version

arXiv v2

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Release date

2025-03-14 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Section

Language

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Field tags

- Multilingual high-difficulty knowledge

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 许可证与权利边界

MIT (stated on the official dataset card)

[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX)（访问 2026-11-07）

### 论文入口

https://arxiv.org/abs/2503.10497

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Code repository

https://github.com/weihao1115/MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/li-lab/MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Official homepage

https://mmluprox.github.io/

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Paper title

MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

The paper’s authors come from the University of Tokyo, Duke-NUS, Waseda, and other institutions; an author’s affiliation is not equated with a formal collaboration agreement.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 合作方

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Authors

- Xuan, Weihao
- Yang, Rui
- Qi, Heli
- Zeng, Qingcheng
- Xiao, Yunze
- Feng, Aosong
- Liu, Dairui
- Xing, Yun
- Wang, Junjue
- Gao, Fan
- Lu, Jinghui
- Jiang, Yuang
- Li, Huitao
- Li, Xin
- Yu, Kunyu
- Dong, Ruihai
- Gu, Shangding
- Li, Yuekang
- Xie, Xiaofei
- Juefei-Xu, Felix
- Khomh, Foutse
- Yoshie, Osamu
- Chen, Qingyu
- Teodoro, Douglas
- Liu, Nan
- Goebel, Randy
- Ma, Lei
- Marrese-Taylor, Edison
- Lu, Shijian
- Iwasawa, Yusuke
- Matsuo, Yutaka
- Li, Irene

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Maintainer

The official public code is hosted under weihao1115; this records the repository maintenance entry point and is not a basis for inferring institutional legal liability or a commitment to continued maintenance.

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### Funders

The acknowledgments on the official site list JSPS KAKENHI 24K20832, JST ActX JPMJAX24CU, an NVIDIA Academic Grant, and the Google Gemma Academic Program.

[来源](https://mmluprox.github.io/)（访问 2026-11-08）

## Design goals

### Abilities measured

Multilingual knowledge and reasoning ability are compared directly on the same hard questions.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Design background

English-language evaluation predominates, and existing multilingual question sets often lack mutually parallel questions that preserve reasoning difficulty.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## Construction

### Question sources

Based on the English questions of MMLU-Pro, translated by multiple LLMs and then reviewed by experts.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 出题与审阅者背景

English cleaning was done by 4 people from different disciplines; translation quality control selected 15 languages, with 2 professional translators per language who are native speakers of that language and who know English. This is not an expert review, question by question, of every item in all 29 languages.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### Review process

Claude Sonnet3.7 carries out the initial translation, self-reflection, and improvement; o3 checks the low-resource African languages, and GPT-4.1 checks the rest. Humans draw 20 questions from each subject, and the same samples from 14 subjects are checked in 15 languages for accuracy, fluency, and completeness.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### Quality control

Duplicate and partly duplicate questions in MMLU-Pro are removed or merged first, and symbols of grammar are corrected; two human translators score samples in 15 languages on a scale of 1–5, and if for a subject both sides score below 3 on any one metric, the whole subject is translated again; the paper records that Yoruba law triggered this rule.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### 去污染及其证据边界

Paper §3.2 addresses internal duplicates and partial duplicates in the question bank; this is deduplication, not decontamination of the evaluated models' training sets. A model-level audit of training contamination remains Unverified.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

## Data format

### 题量与版本口径

29 languages. Full has 11,829 items per language, equal to validation 70 plus test 11,759. Lite has 658 items per language, equal to validation 70 plus test 588. Total size and the actual number of test questions cannot be substituted for each other.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

### Question types

Multiple-choice knowledge/reasoning questions

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Modalities

Text

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Languages

29 languages (the current description in the official README; this is not a count of non-English translations only).

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### Difficulty

Inherits the reasoning orientation of MMLU-Pro; the score gap between high-resource and low-resource languages is not simply a difference in question difficulty.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Public and hidden splits

Both Full and Lite publish validation and test, together with the standard answers. Full test has 11,759 items, Lite test has 588, and each language has 70 validation items for demonstration. Different scales are evaluated independently.

[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

Multiple-choice accuracy by language and the cross-language mean.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 评分方法

The final choice is extracted and compared with the standard answer, and the result is reported language by language.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 运行与提示设置

Evaluation is through the mmlu_prox_<lang> tasks of lm-evaluation-harness. The README requires vLLM 0.7.3 for reproduction, with the exception that Llama3.1-405B uses 0.6.6.

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 官方脚本

https://github.com/weihao1115/MMLU-ProX

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 可比性警示

full/lite, language sets, and CoT strategies that differ cannot be compared together; when a model name on the official site does not give an API date, the date must not be filled in.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/weihao1115/MMLU-ProX/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

The README of 2025-05 records 29 languages, Full and Lite; the note of 2025-08 says that a second version with more languages is under development. A plan is not equated with a release.

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2025-03-14；- **timezone**：；- - **version**：v2；- **submitted_at**：2025-05-27；- **timezone**：

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### Saturation

In the 5-shot CoT static table on the official site, DeepSeek-R1 averages 75.5% across 29 languages; this is only the historical performance of the models and the protocol that are listed, not the current highest score worldwide or a single criterion of saturation.

[来源](https://mmluprox.github.io/)（访问 2026-11-08）

### 污染、争议与限制

The limitations section of the paper notes that expert verification covers only a sample of 15 languages. Bias in translation and cultural differences may still affect the scores. The Full and Lite totals include 70 validation items, while the tests have only 11,759 and 588 respectively. The totals cannot be written as the number of test questions.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

### 衍生与版本关系

MMLU-ProX-Lite is a subset of the same project, made to reduce the cost of evaluation, and it is not counted as another independent benchmark; the README only announces that more languages for the second version are in development, which is not treated as released.

[来源](https://raw.githubusercontent.com/weihao1115/MMLU-ProX/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### Official entry

https://mmluprox.github.io/

[来源](https://mmluprox.github.io/)（访问 2026-11-08）

### 第三方覆盖入口

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Official paper v2 Table 6 / Full / 5-shot CoT

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| DeepSeek-R1 | 75.5 | 29-language average accuracy / % |
| Qwen3-235B-Think | 74.9 | 29-language average accuracy / % |
| GPT-4.1 | 72.7 | 29-language average accuracy / % |

- **DeepSeek-R1**：- **scope**：Per language, test 11,759; excluding 70 validation.
- **Qwen3-235B-Think**：- **scope**：Per language, test 11,759; excluding 70 validation.
- **GPT-4.1**：- **scope**：Per language, test 11,759; excluding 70 validation.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

#### Static results on the official homepage / 5-shot CoT

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Qwen3-235B-Think | 74.9 | 29-language average accuracy / % |
| DeepSeek-R1 | 75.5 | 29-language average accuracy / % |
| GPT-4.1 | 72.7 | 29-language average accuracy / % |
| DeepSeek-V3 | 70.5 | 29-language average accuracy / % |
| o4-mini | 69.3 | 29-language average accuracy / % |
| Qwen3-235B | 66.7 | 29-language average accuracy / % |
| Qwen3-32B-Think | 66.3 | 29-language average accuracy / % |
| Qwen3-14B-Think | 65.4 | 29-language average accuracy / % |

- **Qwen3-235B-Think**：- **language_scores**：- **EN**：80.7；- **FR**：80.6；- **DE**：80.4；- **ES**：80.7；- **PT**：80.5；- **IT**：80.9；- **HI**：78.7；- **BN**：77.8；- **UR**：76.1；- **TE**：77.9；- **MR**：78.5；- **NE**：78.1；- **ZH**：77.4；- **JA**：77.1；- **KO**：78.3；- **VI**：72.6；- **TH**：77.1；- **ID**：79.9；- **AR**：78.7；- **AF**：80.6；- **SW**：70.8；- **WO**：36.9；- **YO**：49.3；- **ZU**：46.4；- **RU**：77.0；- **UK**：78.8；- **SR**：80.2；- **CS**：80.5；- **HU**：79.8；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **DeepSeek-R1**：- **language_scores**：- **EN**：79.5；- **FR**：81.3；- **DE**：76.7；- **ES**：80.2；- **PT**：78.0；- **IT**：79.9；- **HI**：77.5；- **BN**：66.6；- **UR**：76.2；- **TE**：71.9；- **MR**：70.4；- **NE**：78.9；- **ZH**：78.0；- **JA**：76.9；- **KO**：76.7；- **VI**：76.3；- **TH**：78.7；- **ID**：81.3；- **AR**：76.2；- **AF**：80.9；- **SW**：75.0；- **WO**：58.6；- **YO**：57.0；- **ZU**：67.3；- **RU**：76.4；- **UK**：76.8；- **SR**：80.9；- **CS**：76.8；- **HU**：79.1；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **GPT-4.1**：- **language_scores**：- **EN**：79.8；- **FR**：75.7；- **DE**：76.4；- **ES**：77.8；- **PT**：77.0；- **IT**：78.2；- **HI**：74.5；- **BN**：72.2；- **UR**：68.3；- **TE**：65.9；- **MR**：72.2；- **NE**：74.2；- **ZH**：75.5；- **JA**：75.6；- **KO**：75.4；- **VI**：76.7；- **TH**：75.1；- **ID**：75.6；- **AR**：74.1；- **AF**：77.2；- **SW**：71.9；- **WO**：43.2；- **YO**：53.4；- **ZU**：65.0；- **RU**：71.2；- **UK**：76.4；- **SR**：76.9；- **CS**：77.5；- **HU**：76.6；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **DeepSeek-V3**：- **language_scores**：- **EN**：79.6；- **FR**：76.3；- **DE**：75.1；- **ES**：76.9；- **PT**：75.7；- **IT**：75.9；- **HI**：71.6；- **BN**：69.8；- **UR**：70.3；- **TE**：67.6；- **MR**：69.8；- **NE**：69.3；- **ZH**：73.9；- **JA**：72.9；- **KO**：70.7；- **VI**：75.4；- **TH**：71.2；- **ID**：75.8；- **AR**：72.4；- **AF**：72.9；- **SW**：63.4；- **WO**：47.3；- **YO**：47.7；- **ZU**：53.7；- **RU**：74.9；- **UK**：74.2；- **SR**：72.9；- **CS**：74.7；- **HU**：71.4；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **o4-mini**：- **language_scores**：- **EN**：73.7；- **FR**：72.2；- **DE**：73.5；- **ES**：74.7；- **PT**：74.1；- **IT**：73.9；- **HI**：71.8；- **BN**：70.1；- **UR**：72.0；- **TE**：69.1；- **MR**：70.7；- **NE**：71.5；- **ZH**：72.6；- **JA**：71.5；- **KO**：73.2；- **VI**：73.4；- **TH**：72.0；- **ID**：73.8；- **AR**：72.5；- **AF**：73.5；- **SW**：66.9；- **WO**：24.1；- **YO**：54.9；- **ZU**：61.2；- **RU**：62.0；- **UK**：73.3；- **SR**：72.6；- **CS**：73.5；- **HU**：72.6；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **Qwen3-235B**：- **language_scores**：- **EN**：73.5；- **FR**：72.5；- **DE**：71.3；- **ES**：73.2；- **PT**：73.1；- **IT**：73.7；- **HI**：67.6；- **BN**：67.7；- **UR**：68.7；- **TE**：66.7；- **MR**：67.7；- **NE**：67.8；- **ZH**：70.5；- **JA**：68.8；- **KO**：69.6；- **VI**：71.4；- **TH**：68.8；- **ID**：72.5；- **AR**：70.1；- **AF**：71.1；- **SW**：56.3；- **WO**：26.6；- **YO**：40.2；- **ZU**：46.2；- **RU**：72.9；- **UK**：72.5；- **SR**：71.1；- **CS**：71.8；- **HU**：70.1；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **Qwen3-32B-Think**：- **language_scores**：- **EN**：74.9；- **FR**：72.1；- **DE**：71.7；- **ES**：72.8；- **PT**：72.7；- **IT**：73.5；- **HI**：70.4；- **BN**：66.4；- **UR**：70.8；- **TE**：70.3；- **MR**：70.7；- **NE**：70.7；- **ZH**：68.7；- **JA**：70.2；- **KO**：71.2；- **VI**：72.4；- **TH**：70.4；- **ID**：73.4；- **AR**：70.4；- **AF**：72.4；- **SW**：56.7；- **WO**：26.6；- **YO**：18.8；- **ZU**：35.2；- **RU**：69.1；- **UK**：73.5；- **SR**：72.3；- **CS**：72.8；- **HU**：71.1；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard
- **Qwen3-14B-Think**：- **language_scores**：- **EN**：74.7；- **FR**：72.2；- **DE**：71.4；- **ES**：72.2；- **PT**：71.6；- **IT**：73.0；- **HI**：67.9；- **BN**：66.8；- **UR**：68.0；- **TE**：64.6；- **MR**：66.9；- **NE**：67.3；- **ZH**：66.5；- **JA**：70.8；- **KO**：70.0；- **VI**：71.4；- **TH**：69.8；- **ID**：72.3；- **AR**：69.1；- **AF**：71.3；- **SW**：48.0；- **WO**：28.3；- **YO**：32.5；- **ZU**：32.3；- **RU**：72.2；- **UK**：71.3；- **SR**：71.6；- **CS**：71.1；- **HU**：69.8；- **scope**：Static Performance Results on the official site; a separate Leaderboard Coming Soon, not presented as a live leaderboard

[来源](https://mmluprox.github.io/)（访问 2026-11-08）


[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://mmluprox.github.io/)（访问 2026-11-08）

### 覆盖范围与时效

Table 6 of paper v2 and the static table on the official site are separate tracks; identical numbers are not merged into two independent re-evaluations. The page has no exact run date, so the result date is Unverified; the 2026 collection date is not treated as a new experiment in 2026.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://mmluprox.github.io/)（访问 2026-11-08）

## Contact

### 公开工作邮箱

- irene.li@weblab.t.u-tokyo.ac.jp
- weihaoxuan@g.ecc.u-tokyo.ac.jp

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 公开反馈

https://github.com/weihao1115/MMLU-ProX/issues

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 官方社交

Unverified

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 隐私边界

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2503.10497

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### PDF SHA-256

b171ff829bfbb567974812dfebb860a63df7f756daf5662c7a1b659df76833bd

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### PDF bytes

730780

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### Folder

- **id**：1lkm8WYv2rby8F0gpXf1ZMevpAmGW0vk9
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍；- **id**：1iI9qctXi6aYW-mS7lXH46jm9PSI0fUQlkF3-W6KeXBE；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：1gohaRGvTuT_OgM7cpG7rgGG4oAjWNDuR
- **webViewLink**：

[来源]( 2026-11-07）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/weihao1115/MMLU-ProX/main/README.md)（访问 2026-11-08）
