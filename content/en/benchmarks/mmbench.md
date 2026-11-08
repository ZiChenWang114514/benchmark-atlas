# MMBench

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MMBench以分层视觉能力而非单一任务组织图文选择题，核心协议是CircularEval：将候选项循环移位，所有轮次均答对才计成功。原README、论文和当前VLMEvalKit包含不同数量与命名版本；V11、EN/CN、dev/test及答案抽取器必须固定，单次准确率并非等价指标。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### Short name

MMBench

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Full name

MMBench

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Benchmark version

The original MMBench EN and CN data and the data named V11 exist side by side; the official VLMEvalKit explicitly provides four configs, DEV/TEST_EN/CN_V11, which are not treated as the same as the old version.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py)（访问 2026-11-08）

### Paper version

arXiv v5

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Release date

2023-07-13 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Section

Multimodal

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. The classification is not claimed to be set by the benchmark's maintainers.

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Field tags

- General image-text capability

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 许可证与权利边界

Apache-2.0 (LICENSE of the official repository); it does not automatically cover third-party rights such as public datasets and original images from the internet.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/LICENSE)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2307.06281

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Code repository

https://github.com/open-compass/MMBench

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 数据集入口

- **repository_download_table**：https://github.com/open-compass/MMBench#dataset
- **current_vlmevalkit_config_source**：https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py
- **hf_mirror**：https://huggingface.co/datasets/opencompass/MMBench

> The HF card has very little content; the protocol rests on the project download table and the official tool definitions.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/opencompass/MMBench/raw/main/README.md)（访问 2026-11-08）

### Official homepage

https://mmbench.opencompass.org.cn/

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Paper title

MMBench: Is Your Multi-modal Model an All-around Player?

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

Developed by the OpenCompass Community; paper author affiliations include Shanghai Artificial Intelligence Laboratory, Nanyang Technological University, The Chinese University of Hong Kong, National University of Singapore, and Zhejiang University.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 合作方

Unverified

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### Authors

- Liu, Yuan
- Duan, Haodong
- Zhang, Yuanhan
- Li, Bo
- Zhang, Songyang
- Zhao, Wangbo
- Yuan, Yike
- Wang, Jiaqi
- He, Conghui
- Liu, Ziwei
- Chen, Kai
- Lin, Dahua

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### Maintainer

The official open-compass repository team (specific individual responsibilities are currently Unverified).

[来源](https://github.com/open-compass/MMBench)（访问 2026-11-07）

### Funders

Unverified

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

## Design goals

### Abilities measured

Fine-grained image-text perception and reasoning, with a diagnosis under a hierarchical ability scheme.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### Design background

Tasks such as VQAv2 and image captioning do not adequately reflect fine-grained ability, pure string matching is hard to reconcile with free responses, and human subjective scoring is hard to scale.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

## Construction

### Question sources

Image-and-text questions collected from public datasets and the internet are organized into a three-level system of capabilities, with 20 fine-grained capabilities; each question has a single correct option.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 出题与审阅者背景

The research team is responsible for the capability framework, data filtering, and quality control; the specific recruitment background of the annotators is Unverified.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### Review process

Appendix B of the paper: GPT-4, Gemini-Pro, and Qwen-Max first run CircularEval on text alone. A question that can be answered correctly with the picture removed is sent to a person for a check. Five VLMs then screen for questions that all five get wrong, and a person checks those questions for ambiguity, for a repeated option, and for a wrong label.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### Quality control

The original paper organizes questions in three layers and 20 capabilities, and Appendix B separately handles text-only shortcut questions and questions that may be wrong; the Chinese translation was then checked by hand. This is not a guarantee of rights in every source image, or of the state of training contamination.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 去污染及其证据边界

Unverified

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

## Data format

### 题量与版本口径

Paper v5 of 2024 has 3,217 questions; the body of the repository README is still at 2,974 questions, and the download table lists dev 1,164 and test 1,784, which also do not add up to 2,974. Each basis is retained, and a single number of questions is not guessed at.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### Question types

Single-choice questions of image + question + options.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### Modalities

Image+text

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### Languages

Chinese and English

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### Difficulty

Difficulty is set by a three-level fine-grained classification of ability, rather than by a single academic grade; CircularEval requires a correct answer on every rotation of the options, and the official README notes that this is harder than a single evaluation.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### Public and hidden splits

The download tables have, for each of EN and CN, 1,164 dev questions and 1,784 test questions. The VLMEvalKit format keeps only one copy of each image. Legacy is N-option CircularEval and keeps N copies. The body text is the same. The number of questions cannot be inferred from the number of image copies.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

CircularEval accuracy: the N options are shifted cyclically N times, and the question counts as solved only when every shift is answered correctly; this is kept separate from accuracy on a single pass.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 评分方法

Options are extracted by rules first, and if that fails ChatGPT matches the answer, with at most 3 attempts; CircularEval shifts every option cyclically, and the original question counts as a success only when all N shifts are correct.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 运行与提示设置

The official VLMEvalKit builds prompts that contain the image, the hint, the question, the candidate answers, and the option instructions; EN/CN and the CircularEval count are retained.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 官方脚本

https://github.com/open-compass/VLMEvalKit

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 可比性警示

The question counts in the README, the paper, and the download table conflict; EN and CN, dev and test, old and new files, and single-pass and CircularEval cannot be compared as a mixture. MMVistaReason uses CompassVerifier and cannot be assumed equivalent to official CircularEval.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

V11 (EN/CN dev/test) is currently visible in VLMEvalKit, while the README of the original project still lists the old download table. A reproduction should record the exact configuration name and the checksum of the file, and should not guess the version from the question count in the README.

[来源](https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py)（访问 2026-11-08）

### 论文修订及历史证据

- **continued_use_2026h2**：- - **url**：https://arxiv.org/html/2610.01352v2；- **date**：2026-10-22；- **note**：MMVistaReason v2 §4.1 and Table 2 actually evaluate MMBench (the EN setting), comparing 4B/9B models and other vision-language models; splits such as mini and val are not counted separately.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### Saturation

Unverified

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 污染、争议与限制

The question counts in the README, the paper, and the download table conflict; EN and CN, dev and test, old and new files, and single-pass and CircularEval cannot be compared as a mixture. MMVistaReason uses CompassVerifier and cannot be assumed equivalent to official CircularEval.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### 衍生与版本关系

The repository also lists CCBench: related to Chinese culture, with 510 dev questions; the announcement of 2023-12-26 deleted noisy samples and updated the leaderboard. CCBench is not the same split as MMBench EN/CN.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### Official entry

https://mmbench.opencompass.org.cn/leaderboard

> The page captured this time has no readable leaderboard rows; the current official ranking is Unverified, and a research paper is not substituted so as to pass for the official ranking.

[来源](https://mmbench.opencompass.org.cn/leaderboard)（访问 2026-11-08）

### 第三方覆盖入口

Unverified

> The AA directory of evaluations was opened in this pass. A separate tracking page for this original benchmark was not confirmed. AA tracking MMMU-Pro is not the same as AA tracking the original MMMU. Preference Elo from LMArena, or a score on another benchmark, is not put in its place. Results from Epoch and from LMArena under the same definition remain Unverified, item by item.

[来源](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07）

### 分来源与协议的精确成绩

#### Original paper v5, Table 3 / EN test / CircularEval.

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| InternLM-XComposer2* | 78.1 | CircularEval Top-1 accuracy / % |
| Qwen-VL-Max | 75.4 | CircularEval Top-1 accuracy / % |
| GPT-4v | 74.3 | CircularEval Top-1 accuracy / % |

- **InternLM-XComposer2***：- **scope**：Historical paper leaderboard, not the current official web-page dynamic leaderboard
- **Qwen-VL-Max**：- **scope**：Historical paper leaderboard, not the current official web-page dynamic leaderboard
- **GPT-4v**：- **scope**：Historical paper leaderboard, not the current official web-page dynamic leaderboard

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

#### MMVistaReason author paper / EN / CompassVerifier

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| MMVistaReason-4B (MVR-4B) | 90.6 | Answer accuracy under the protocol of the paper (CompassVerifier) / % |
| MMVistaReason-9B (MVR-9B) | 92.2 | Answer accuracy under the protocol of the paper (CompassVerifier) / % |

- **MMVistaReason-4B (MVR-4B)**：- **scope**：MMBench-EN; the paper does not list the downloaded version exactly；- **date**：2026-10-22；- **provenance**：Table 2 as reported by the MMVistaReason authors themselves; VLMEvalKit, T=0, max16384; §7.3 replaces traditional string matching with CompassVerifier, and this is not the official leaderboard or an independent evaluation by AA
- **MMVistaReason-9B (MVR-9B)**：- **scope**：MMBench-EN; the paper does not list the downloaded version exactly；- **date**：2026-10-22；- **provenance**：MMVistaReason author self-report Table 2; the same protocol, and not ranked together with other leaderboards without conditions

[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### 覆盖范围与时效

The official leaderboard URL returns only the shell of the front-end application. Dynamic scores were not obtained, and it cannot be claimed that the ranking has been refreshed to the latest. Historical test scores from Table 3 of original paper v5 are added, and the 2026 CompassVerifier research results are placed on another track; different data versions, CN and EN, dev and test, and different scorers must not be ranked together.

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

## Contact

### 公开工作邮箱

Unverified

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 公开反馈

https://github.com/open-compass/MMBench/issues

[来源](https://github.com/open-compass/MMBench)（访问 2026-11-07）

### 官方社交

Unverified

> Precise verification of this field is not yet complete for this batch; this is not the same as Not disclosed by the official source.

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 隐私边界

Only officially published project feedback channels are recorded; private contact details are neither collected nor inferred.

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2307.06281

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### PDF SHA-256

3cd9025569600c548d29a987e1cef6bdac8dc07cdeb6bd49ef04690ae80ebd6b

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### PDF bytes

7311810

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化续核：打开Official README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）
