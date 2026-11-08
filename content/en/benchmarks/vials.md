# VIALS

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

VIALS is directed at visual interpretation of the products of everyday experiments in the life sciences, rather than charts already arranged in textbooks. Official direct visual accuracy on 161 questions and AA pass^3 with code tools measure different abilities; data 2.0.0 corrected three questions, and the paper 1.0.0 results should not be relabeled automatically.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-08); [3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08)

## Basic information

### Short name

VIALS

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### Full name

Visual Interpretation of Artifacts in the Life Sciences

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Benchmark version

2.0.0

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Paper version

arXiv v2; submitted at 2026-09-20 00:59:27.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Release date

Data v1.0.0 tag released 2026-09-15; v2.0.0 released 2026-10-30 (the date marked in the dataset-card CHANGELOG); arXiv v1 is separately 2026-08-22 02:59:26, and is not mixed in as the date the data went online.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08); [2](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Section

Multimodal

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### Field tags

- 科学图像
- 物理
- 化学
- 生物与医学
- 材料

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### 许可与适用范围

Data and images are CC BY 4.0 (each image cites the original source in attributions.csv); the evaluation code is separately MIT.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/2608.21357

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Code repository

https://github.com/Handshake-AI-Research/VIALS

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### 数据地址

https://huggingface.co/datasets/Handshake-AI-Research/VIALS

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Official homepage

https://joinhandshake.com/research/benchmarks/vials/

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### Paper title

VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

## Origin and maintenance

### 机构与发起关系

Handshake AI

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Partner organizations

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### Authors

- Elaine Lau
- Thanuka Udumulla
- Lee Izhaki-Tavor
- Francisco Guzmán
- Nicholas Magazine
- Jonas Mueller

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Current maintainer

Handshake AI

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 资助与支持

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

## Design goals

### Abilities measured

Interpretation of real visual evidence in professional life-science workflows, such as gels, flow-cytometry plots, plasmid maps, phylogenetic trees, and molecular structures.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Design background

Emphasizes the everyday visual products of scientific research, rather than textbook examination figures or mere description of natural images, and tests visual localization and domain interpretation.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Unpublished experimental data, artifacts produced by scientific software, and figures from CC-BY open papers; experts write the questions and the reference answers from their own work.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 出题背景

31 professional contributors, 87% with doctoral-level training and 74% with more than 6 years of experience in the life-sciences industry.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Review process

A second domain expert, and often a third, answers blind; the question is kept only when the independent answers agree or review reaches consensus.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Quality control

Image realism, answerability, and task diversity are checked; agreement between the GPT-5-mini judge and 4685 human-annotated responses is 99.9% (reported by the authors).

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 去污染与泄漏

At construction, tasks are checked to confirm that they do not appear online; the dataset card requires that they not enter training corpora. Further tasks developed later in private are not counted in the question total of this version.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

## Data format

### Size

161 tasks; HF test-split parquet.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Question types

One or more images plus a question, an open-ended short answer, including an acceptable numeric range.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Modalities

- 科学图像
- 文本问题
- 短文本答案

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### Languages

- 英语

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/README.md) (accessed 2026-11-08)

### Difficulty

Directed at the daily tasks of professional scientists with relevant training; this does not equal the difficulty of the full research workflow.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

### 数据划分

161 questions are currently public; model input may use only images and question, while answer and the numerical ranges are for scoring only.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS) (accessed 2026-11-07)

## Evaluation

### Metrics

The official direct visual evaluation is the mean accuracy of three independent rollouts; the AA Agent implementation headline is pass^3.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### Scoring

The official procedure extracts the answer after the final ANSWER: and uses GPT-5-mini to judge equivalence of scientific meaning; when a label is ambiguous, the item is reviewed with the figure.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 提示与运行设置

The direct VLM in the paper uses temperature 1.0, 32768 completion tokens, and 3 runs per question; AA uses the Stirrup code tools and image-viewing tools, with no network, and GPT-6 Luna medium as the judge.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 评测脚本

Handshake-AI-Research/VIALS; the data card explicitly states that the code is MIT.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 可比性提醒

Direct vision, official tool assistance, and AA tool assistance must be kept separate; AA pass^3 is not the mean accuracy on the official site, and a higher score cannot be cited as a gain in performance under the same protocol.

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08)

### 数据版本与更新

2.0.0, released on 2026-10-30; after an additional review by experts, 3 tasks were changed: 2 prompts, one reference answer, and one image, and the tasks that are affected must be run again. The results in the paper use 1.0.0, and the scores cannot be upgraded in silence.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08); [2](https://github.com/Handshake-AI-Research/VIALS) (accessed 2026-11-08)

### 论文修订记录

- {"version": "v1", "submitted_at": "2026-08-22 02:59:26 "}
- {"version": "v2", "submitted_at": "2026-09-20 00:59:27 "}

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-08)

### 饱和证据与局限

The highest direct-vision mean accuracy on the official site is 49.9%. The highest tool-assisted headline pass^3 at AA is 64%. The tools and the judges differ, so this cannot be treated as the same protocol rising from 49.9 to 64, and it cannot be inferred that professional vision tasks are saturated.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-08)

### 争议与已知问题

Version 2.0.0 corrects three questions and requires a rerun. The domain text of the data card says nine categories, while the paper and AA use eight. This page keeps the conflict between sources. The paper's self-reported judge agreement of 99.9% on 4685 responses is for v1.0.0, and it is not extrapolated as absolute correctness for every new version.

Sources: [1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08); [2](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/README.md) (accessed 2026-11-08); [3](https://arxiv.org/pdf/2608.21357) (accessed 2026-11-08); [4](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-08)

### 衍生或后继基准

A check against the existing 100 slugs found no older version of the same name; an evaluation implementation or a component score is not counted again as a new benchmark.

Note: The editorial conclusion on deduplication; relations among versions follow the dedicated account below.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-08); [3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08)

### 官方榜单入口

https://joinhandshake.com/research/benchmarks/vials/

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### 第三方入口

https://artificialanalysis.ai/evaluations/vials-aa

Sources: [1](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-07)

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Handshake official site / direct vision | 1 | GPT-6 Astra | 49.9 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 2 | GPT-6.1 Sol | 49.1 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 3 | Gemini 4 Argon | 47.2 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 4 | Claude Sonnet 5.5 | 41.0 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 5 | Claude Opus 5.5 | 40.2 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 6 | Muse Wonder | 31.5 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 7 | Gemini 3.8 Flash | 29.4 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 8 | GPT-5.6 Sol | 26.5 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 9 | Claude Opus 5 | 24.4 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 10 | Muse Spark 1.2 | 22.6 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 11 | Kimi K3 | 20.9 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 12 | Grok 4.7 | 18.2 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 13 | DeepSeek V4.1 Flash | 12.6 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Handshake official site / direct vision | 14 | MiniMax-M3 | 10.8 | average accuracy (%) | The current leaderboard on the official website; the README calls it the leaderboard of the latest version, and the web page does not mark a revision on each row.；Official direct-vision evaluation; not AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 |
| Artificial Analysis / tool-assisted | 1 | Gemini 4 Carbon (High) | 64 | pass^3 (%) | 161 tasks; AA current implementation；Stirrup; Python plus viewing the figure; no network; 3 independent repeats; GPT-6 Luna medium as judge | [Unverified (the webpage does not mark a run time for the results or an update time for the full leaderboard)](https://artificialanalysis.ai/evaluations/vials-aa)；采集2026-11-08 |
| Artificial Analysis / tool-assisted | 2 | GPT-6 Astra (Max) | 63 | pass^3 (%) | 161 tasks; AA current implementation；Stirrup; Python plus viewing the figure; no network; 3 independent repeats; GPT-6 Luna medium as judge | [Unverified (the webpage does not mark a run time for the results or an update time for the full leaderboard)](https://artificialanalysis.ai/evaluations/vials-aa)；采集2026-11-08 |
| Artificial Analysis / tool-assisted | 3 | Claude Opus 5.5 (Max, Default Fallback) | 61 | pass^3 (%) | 161 tasks; AA current implementation；Stirrup; Python plus viewing the figure; no network; 3 independent repeats; GPT-6 Luna medium as judge | [Unverified (the webpage does not mark a run time for the results or an update time for the full leaderboard)](https://artificialanalysis.ai/evaluations/vials-aa)；采集2026-11-08 |

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-08); [3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08)

### 榜单覆盖边界

The 14 rows of mean accuracy for direct vision on the official site, and the top three pass^3 scores that AA lists by name, are kept on separate tracks. The official site does not give a data revision on every row, so it cannot be assumed that every older score has already been rerun as v2. Paper v1.0.0, data v2.0.0, and the independent implementation of the tools at AA are each marked as such.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08); [2](https://artificialanalysis.ai/evaluations/vials-aa) (accessed 2026-11-08); [3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

- elaine.lau@joinhandshake.com
- nicholas.magazine@joinhandshake.com
- jonas.mueller@joinhandshake.com

Sources: [1](https://arxiv.org/abs/2608.21357) (accessed 2026-11-07)

### 公开反馈渠道

https://github.com/Handshake-AI-Research/VIALS/issues

Sources: [1](https://github.com/Handshake-AI-Research/VIALS) (accessed 2026-11-08)

### 官方社交账号

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### 联系方式/隐私原则

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

## Original files

### 原始PDF

https://arxiv.org/pdf/2608.21357

Sources: [1](https://arxiv.org/pdf/2608.21357) (accessed 2026-11-08)

### PDF SHA-256

5d5756cb7d10aa1859a3b8bcbc1155384025a69fbd10efbaaec0e0e80f973f83

Sources: [1](https://arxiv.org/pdf/2608.21357) (accessed 2026-11-08)

### PDF bytes

```json
8757144
```

Sources: [1](https://arxiv.org/pdf/2608.21357) (accessed 2026-11-08)

### Folder

Unverified

Note: The cited official materials have been checked, but precise verification is incomplete; this does not mean the official source has Not disclosed it.

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### Other documents

- {"type": "Official introduction/protocol", "url": "https://joinhandshake.com/research/benchmarks/vials/"}

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

### 论文原件

Unverified

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-07)

## Changelog

Latest review
Latest review

Sources: [1](https://joinhandshake.com/research/benchmarks/vials/) (accessed 2026-11-08)
