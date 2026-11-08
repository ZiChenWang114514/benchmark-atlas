# WinoGrande

> In-depth review: 2026-11-08. The collection date is not the leaderboard update date; new evidence that has not been obtained does not overwrite an older source date.

WinoGrande reduces lexical shortcuts through crowdsourced paired sentences and AFLite, but “debiasing” does not mean that training contamination of modern models has already been ruled out. The full training set, the debiased development and test sets, the five supervised training scales, and modern zero-shot and few-shot testing must be distinguished.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

## Basic information

### Short name

WinoGrande

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Full name

WinoGrande

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Benchmark version

1.1 (official repository README)

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### Paper version

arXiv v2

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Release date

- **paper_first_submission**：2019-07-25
- **date_type**：First submission of the paper; not the same as the first release of the dataset

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Section

Reasoning

Sources: [1](http://winogrande.allenai.org) (accessed 2026-11-07).

### Field tags

- Commonsense coreference reasoning

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### License

- **code**：Apache-2.0
- **dataset**：CC-BY (the README does not state a specific minor version)

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### Paper

https://arxiv.org/abs/1907.10641

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Code

https://github.com/allenai/winogrande

Sources: [1](http://winogrande.allenai.org) (accessed 2026-11-07).

### 数据地址

https://github.com/allenai/winogrande

Sources: [1](http://winogrande.allenai.org) (accessed 2026-11-07); [2](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Official entry

http://winogrande.allenai.org

Sources: [1](http://winogrande.allenai.org) (accessed 2026-11-07); [2](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Paper title

WinoGrande: An Adversarial Winograd Schema Challenge at Scale

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

## Origin and maintenance

### Initiating organizations

Allen Institute for AI、University of Washington

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 署名合作机构

- Allen Institute for Artificial Intelligence
- University of Washington

> Author affiliations: all authors are credited to AI2, and Yejin Choi is also credited to UW; no additional commercial partners are inferred.

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08).

### Authors

- Sakaguchi, Keisuke
- Bras, Ronan Le
- Bhagavatula, Chandra
- Choi, Yejin

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Maintainer

The official code is allenai/winogrande, and data distribution and question answering are provided by the AI2 team; the README specifies GitHub Issues and the WinoGrande Google Group, and the public contact is Keisuke Sakaguchi.

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08); [2](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08).

### Funders

NSF IIS-1524371 and IIS-1714566. DARPA CwC through ARO W911NF-15-1-0543. DARPA MCS through NIWC Pacific N66001-19-2-4031.

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08).

## Design goals

### Abilities measured

Evaluates the resolution of pronoun and coreference ambiguity by common sense and context, rather than by lexical association alone.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Design background

The original Winograd Schema set is small and may be affected by surface data bias, so a larger set that has been adversarially debiased is needed.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

## Construction

### 题目与数据来源

Crowd workers wrote pairs of sentences that are close in meaning but differ in the answer, using WikiHow words as anchors, and the pairs were then filtered with AFLite.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 构建者背景

Crowdsourced question writing and independent verification; the researchers designed AFLite and the collection constraints.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Review process

Each question is checked by more than one person; AFLite uses representations and a simple classifier to identify samples that bias would allow one to guess.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Quality control

3 human validators are combined with automatic debiasing; different training scales are provided in order to measure data efficiency.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 去污染与泄漏防范

AFLite targets learnable bias within the set; it is not deduplication of the training corpora of modern LLMs.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

## Data format

### Size

The full set has 43,972 questions: train_xl 40,938, validation 1,267, and test 1,767. The debiased train has 9,248 (12,282 together with the same dev/test). The training scales XS/S/M/L/XL are 160/640/2,558/10,234/40,938 respectively. HF lists each as a config, and they are not added together.

Sources: [1](https://huggingface.co/datasets/allenai/winogrande/raw/main/README.md) (accessed 2026-11-08); [2](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08).

### 任务形式

One sentence containing a blank and 2 fill-in options.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Modalities

Plain text: an English sentence containing a blank, two candidate noun phrases, and a 1/2 answer; it is not a mathematics problem and contains no image/video.

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08); [2](https://huggingface.co/datasets/allenai/winogrande/raw/main/README.md) (accessed 2026-11-08).

### Languages

English; official HF dataset card language: en.

Sources: [1](https://huggingface.co/datasets/allenai/winogrande/raw/main/README.md) (accessed 2026-11-08).

### 难度与类型

Commonsense coreference disambiguation; XS/S/M/L/XL are training scales, not difficulty levels.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### Public and hidden splits

train has five scales, xs/s/m/l/xl, with separate labels; dev includes labels, and test does not disclose the labels. Each line of the prediction file has five columns, corresponding in order to the five training scales.

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

## Evaluation

### Metrics

Accuracy; the official challenge also requires predictions in the five columns XS/S/M/L/XL, in order to examine data efficiency and the learning curve. Modern zero-shot and few-shot validation accuracy is not the same track as the official test protocol with five training scales.

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### 评分

Output 1 or 2 and compare with the answer; an official submission may include prediction columns for 5 training scales.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 提示和复现设置

The original paper uses supervised fine-tuning; modern zero/few-shot generative evaluation is not the same as the official learning-curve setting.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 官方脚本

The official README directs the use of eval.py to evaluate dev, with the output metrics.json; test should be submitted to the official leaderboard as predictions.lst.

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### 可比性提示

The debiased and XL training sets, dev and test, and single-point accuracy and learning curves must be kept distinct.

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07).

## Current status

### 核验时间

2026-11-08

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### 数据版本与当前状态

1.1 (the version listed in the README; recent open-source activity or the latest commit is not inferred from it).

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### 论文修订与H2证据

- **arxiv_version**：arXiv v2
- **history_note**：See the arXiv metadata for the full history; the draft date has been converted, and the paper revision date is not treated as the data version.
- **2026_h2_evidence**：- - **url**：https://arxiv.org/html/2610.11978v1
 - **date**：2026-10-08
 - **note**：Jev research Tables 1–2 and §3.1 actually compare multiple classes of models on WinoGrande and do not count ARC-Easy or other subsets separately.
- **revisions**：- - **version**：v1
 - **date**：2019-07-25
 - - **version**：v2
 - **date**：2019-11-22
- **note**：The paper revision time cannot be treated as the data release date. Existing 2026-H2 evidence retains the original collection date.

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07).

### 饱和程度

Unverified

> Whether it is saturated depends on the specific split, the tools, and the protocol; the scores below are only a snapshot from a limited source and are not a judgment of overall saturation or of SOTA

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07).

### 污染、冲突与限制

The public development set, templates, and vocabulary may all be absorbed into training; debiasing does not mean an absence of contamination.

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](http://winogrande.allenai.org) (accessed 2026-11-07).

### 后续工作与衍生

Extended from the Winograd Schema; it is not a synonym of WSC273 or of all Winograd data.

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](http://winogrande.allenai.org) (accessed 2026-11-07).

## Leaderboard snapshot

### 快照采集日

2026-11-08; only the paper historical table was refreshed; the official live leaderboard failed

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### Official leaderboard

https://leaderboard.allenai.org/winogrande/submissions/public

Sources: [1](https://github.com/allenai/winogrande) (accessed 2026-11-07); [2](https://leaderboard.allenai.org/winogrande/submissions/public) (accessed 2026-11-07).

### 第三方覆盖

Unverified

> No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### Existing 2026-H2 research experiments (not refreshed)

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Gemini 3.8 Flash | 97.1 % | accuracy Jev Table 2; the checkpoint date is not listed | 2026-10-08；https://arxiv.org/html/2610.11978v1 |
| — | Qwen3.8 Flash | 94.4 % | accuracy Jev Table 2; model display name | 2026-10-08；https://arxiv.org/html/2610.11978v1 |
| — | Claude Opus 5.5 | 92.7 % | accuracy Jev Table 2; model display name | 2026-10-08；https://arxiv.org/html/2610.11978v1 |

#### Original paper v2 Table 3/dev

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | WKH | 49.4 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | Ensemble LMs | 53.0 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | BERT | 65.8 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa | 79.3 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | BERT (local context) | 52.5 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa (local context) | 52.1 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | BERT-DPR (zero-shot) | 50.2 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa-DPR (zero-shot) | 59.4 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | Human | 94.1 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 3/test

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | WKH | 49.6 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | Ensemble LMs | 50.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | BERT | 64.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa | 79.1 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | BERT (local context) | 51.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa (local context) | 50.0 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | BERT-DPR (zero-shot) | 51.0 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa-DPR (zero-shot) | 58.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | Human | 94.0 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/XS/dev

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 51.5 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/XS/test

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 50.4 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/S/dev

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 58.6 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/S/test

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 58.6 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/M/dev

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 66.9 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/M/test

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 67.6 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/L/dev

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 75.8 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/L/test

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 74.7 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/XL/dev

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 79.3 % | accuracy | https://arxiv.org/pdf/1907.10641 |

#### Original paper v2 Table 4/XL/test

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | RoBERTa | 79.1 % | accuracy | https://arxiv.org/pdf/1907.10641 |

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.11978v1) (accessed 2026-11-07).

### Coverage note

Requests to the official AI2 leaderboard met a TLS EOF, and WebFetch returned 500. A live leaderboard was not obtained, and the latest SOTA is not claimed. The 9 models × dev/test in Table3 of original paper v2, and the five training scales × dev/test in Table4, were restored value by value. The existing three rows of 2026-H2 research keep the old collection date and are kept separate from the official test and the learning curve.

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

## Contact

### 公开联系邮箱

- keisukes@allenai.org

Sources: [1](http://winogrande.allenai.org) (accessed 2026-11-07); [2](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### 问题反馈

https://github.com/allenai/winogrande/issues

Sources: [1](https://github.com/allenai/winogrande) (accessed 2026-11-07).

### 官方讨论渠道

https://groups.google.com/a/allenai.org/forum/#!forum/winogrande

> The question-answering Google Group specified in the official README; it is not a personal social account.

Sources: [1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).

### 隐私与数据使用

Unverified

> A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

## Original files

### 源站论文PDF

https://arxiv.org/pdf/1907.10641

Source: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08).

### SHA-256

780b26e4c9dd38c61f2f9e7b99a3e3dfec94fd19bb13bc06338770ca3733e67a

> Original bytes of the PDF downloaded again. The existing copy was not overwritten.

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08).

### 字节数

1098857

Sources: [1](https://arxiv.org/pdf/1907.10641) (accessed 2026-11-08).

### Other documents

## Changelog

### 本页修订

- - **date**：2026-11-07
 - **change**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- - **date**：2026-11-07
 - **change**：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
 - **fields_updated**：- basic_info.version
 - latest_status.latest_dataset_version
 - evaluation.official_scripts
 - data_format.public_hidden_split
- - **date**：2026-11-08
 - **round**：2
 - **change**：逐项打开arXiv摘要与PDF全文、Official README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

Sources: [1](https://arxiv.org/abs/1907.10641) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md) (accessed 2026-11-08).
