# MMAU

> Benchmark Constitution, in-depth check 2026-11-08. Facts follow the sources listed and their access dates; an unresolved item is not the same as officially Not disclosed.

## Basic information

MMAU把语音、环境声音和音乐放在同一个音频理解评测框架下，以音频加多选题测试27类任务。当前修订版v05.15.25与原论文首版不同，且test-mini公开答案、完整test保留答案；两者规模与成绩不能混合排名。代码Apache-2.0和数据CC-BY-NC-4.0也应分别记录。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini)（访问 2026-11-07）

### Short name

MMAU

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Full name

Massive Multi-Task Audio Understanding and Reasoning

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Benchmark version

MMAU-v05.15.25

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### Paper version

arXiv v1

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Release date

2024-10-25 (time of the first arXiv draft; not equivalent to an independent dataset first release).

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Section

Multimodal

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. The classification is not claimed to be set by the benchmark's maintainers.

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Field tags

- Speech, sound, and music understanding and reasoning

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 许可证与权利边界

The LICENSE of the code repository is Apache-2.0; the HF test-mini data card is CC-BY-NC-4.0. A license for the code is not a license to reuse the audio, and rights in the upstream audio are observed separately.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/LICENSE)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini/raw/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2410.19168

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Code repository

https://github.com/Sakshi113/MMAU

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini)（访问 2026-11-07）

### Official homepage

https://sakshi113.github.io/mmau_homepage/

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Paper title

MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

## Origin and maintenance

### 发起方与作者单位

Author team from the University of Maryland, College Park, and Adobe.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 合作方

- University of Maryland, College Park
- Adobe

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### Authors

- Sakshi, S
- Tyagi, Utkarsh
- Kumar, Sonal
- Seth, Ashish
- Selvakumar, Ramaneswaran
- Nieto, Oriol
- Duraiswami, Ramani
- Ghosh, Sreyan
- Manocha, Dinesh

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### Maintainer

The MMAU author team. The official README lists S Sakshi, Sonal Kumar, and Sreyan Ghosh as contacts. Test evaluation moved to sonalkum/MMAU-Eval on 2026-01-30.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### Funders

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

## Design goals

### Abilities measured

Expert knowledge, information extraction, and complex reasoning for speech, environmental sound, and music.

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### Design background

Early audio evaluation leaned toward recognition or a single domain, and lacked expert-level complex reasoning across the three major audio domains.

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

## Construction

### Question sources

Starting from 13 audio corpora, with real recordings preferred; experts screened an initial 90 tasks down to 27, wrote the questions and answers, had them screened by independent experts, then expanded the distractor options and reviewed them again.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 出题与审阅者背景

Experts in speech, sound, and music; the authors assisted with selecting audio and with iterative design.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### Review process

Separate teams of experts removed question-answer pairs that were ambiguous, overly complex, or poor in audio quality; the version update of 2025 further revised answers to questions and some of the audio.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### Quality control

v05.15.25, following feedback from the community, revises about 25% of the questions and answers and improves about 5% of the audio. Section C.3 of the original paper requires that the audio not be damaged, that the question be an English question, that the task, difficulty, and dataset labels be present, and that only MCQ items be kept. The copyright guide requires that material from a site which forbids copying and redistribution be left out.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 去污染及其证据边界

Test answers and explanations are not public, and scores are computed through an HF Space; public audio source material may still overlap training corpora, so an absence of contamination cannot be claimed.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

## Data format

### 题量与版本口径

10,000 audio question-answer items and 27 tasks; test-mini 1,000 and test 9,000.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini)（访问 2026-11-07）

### Question types

Audio plus natural-language multiple-choice question answering, covering speech, sound, and music.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### Modalities

Audio+text

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### Languages

- **question_language**：English (Appendix C.3 of the original paper requires that all questions use English).
- **audio_language_distribution**：待核实

> The language of the question and the language of the source audio are strictly distinguished; an English question is not used to infer that all audio is English.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### Difficulty

The original paper has Easy:Medium:Hard = 22%:56%:22%; this cannot be assumed to be the exact distribution after the v05.15.25 revision.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### Public and hidden splits

10,000 questions: test-mini has 1,000 questions with public answers; test has 9,000 questions whose questions are public while the answers and explanations are withheld, and predictions are submitted for evaluation through the official HF Space.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

The official evaluation.py parses model_prediction and computes option accuracy; the three audio domains and the average score are reported separately.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 评分方法

The official evaluation.py parses model_prediction and computes option accuracy; the three audio domains and the average score are reported separately.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 运行与提示设置

Audio preprocessing, output parsing, test-mini/test, and the data version are recorded. The 2026 study of uncertainty places the correct option in each position and then takes the mean, and there is also an open-ended protocol that removes the options.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 官方脚本

https://github.com/Sakshi113/MMAU

[来源](https://github.com/Sakshi113/MMAU)（访问 2026-11-07）

### 可比性警示

The new version v05.15.25 and the old leaderboard cannot be used together; the README and the homepage say 12 extraction tasks plus 15 reasoning tasks, but the body of arXiv v1 says 11 extraction tasks plus 16 reasoning tasks, and both totals are 27, so the breakdown is Unverified.

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

## Current status

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

MMAU-v05.15.25: about 25% of the questions and answers revised, and about 5% of the audio improved; on 2026-01-30 the test evaluation moved from EvalAI to HF Space.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 论文修订及历史证据

- **continued_use_2026h2**：- - **url**：https://arxiv.org/html/2609.28879v1；- **date**：2026-09-24；- **note**：Broadening Uncertainty Estimation for Audio Question Answering actually studies uncertainty estimation, and different question formats, on the MMAU audio question-answering data.；- **date**：2026-09-24

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2609.28879)（访问 2026-11-08）

### Saturation

For the full test of v05.15.25, the current official parsed file peaks at an Avg of 75.98%, below a perfect score; saturation cannot be inferred by mixing test-mini, an older version, or the average result of permutations of the multiple-choice options.

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 污染、争议与限制

The new version v05.15.25 and the old leaderboard cannot be used together; the README and the homepage say 12 extraction tasks plus 15 reasoning tasks, but the body of arXiv v1 says 11 extraction tasks plus 16 reasoning tasks, and both totals are 27, so the breakdown is Unverified.

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

### 衍生与版本关系

MMAU-Pro (official announcement of 2025-08-19); scores are not mixed with the original or revised MMAU.

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### Snapshot date

2026-11-08 (collection date, not the evaluation run date)

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）

### Official entry

https://sakshi113.github.io/mmau_homepage/#leaderboard-v15-parsed

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 第三方覆盖入口

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

[来源](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07）

### 分来源与协议的精确成绩

#### Official v05.15.25 parsed / Test

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Audio-Thinker | 75.98 | accuracy / % |
| Nova 2 Omni | 75.28 | accuracy / % |
| Step-Audio-2 | 73.86 | accuracy / % |
| MiMo-Audio | 72.59 | accuracy / % |
| Audio Flamingo 3 | 72.42 | accuracy / % |
| Qwen2.5-Omni | 71.00 | accuracy / % |
| Step-Audio-2-mini | 70.23 | accuracy / % |
| Gemini 2.5 Pro | 69.36 | accuracy / % |
| Gemini 2.5 Flash | 67.39 | accuracy / % |
| Gemini 2.0 Flash | 67.03 | accuracy / % |
| DeSTA2.5-Audio | 65.21 | accuracy / % |
| Kimi-Audio | 64.40 | accuracy / % |
| Audio Reasoner | 63.78 | accuracy / % |
| Phi-4-multimodal | 62.81 | accuracy / % |
| Gemini 2.5 Flash Lite | 61.61 | accuracy / % |
| Audio Flamingo 2 | 61.06 | accuracy / % |
| GPT-4o Audio | 60.82 | accuracy / % |
| Qwen2-Audio-Instruct | 57.40 | accuracy / % |
| Gemma 3n | 55.20 | accuracy / % |
| Gemma 3n | 52.06 | accuracy / % |
| GPT-4o mini Audio | 51.03 | accuracy / % |
| M2UGen | 39.76 | accuracy / % |
| MusiLingo | 38.29 | accuracy / % |
| SALMONN | 36.23 | accuracy / % |
| MuLLaMa | 25.91 | accuracy / % |
| GAMA-IT | 22.22 | accuracy / % |
| GAMA | 21.68 | accuracy / % |
| LTU | 17.23 | accuracy / % |
| Audio Flamingo Chat | 15.59 | accuracy / % |

- **Audio-Thinker**：- **rank**：1；- **scope**：9000-question test；- **sound**：78.8；- **music**：73.8；- **speech**：75.16；- **model_link**：https://arxiv.org/pdf/2508.08039v1；- **model_size**：8.4B
- **Nova 2 Omni**：- **rank**：2；- **scope**：9000-question test；- **sound**：77.87；- **music**：66.37；- **speech**：81.82；- **model_link**：https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models；- **model_size**：-
- **Step-Audio-2**：- **rank**：3；- **scope**：9000-question test；- **sound**：80.60；- **music**：68.23；- **speech**：72.75；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：-
- **MiMo-Audio**：- **rank**：4；- **scope**：9000-question test；- **sound**：77.2；- **music**：69.73；- **speech**：70.77；- **model_link**：https://github.com/XiaomiMiMo/MiMo-Audio/；- **model_size**：7B
- **Audio Flamingo 3**：- **rank**：5；- **scope**：9000-question test；- **sound**：75.83；- **music**：74.47；- **speech**：66.97；- **model_link**：https://www.arxiv.org/abs/2507.08128；- **model_size**：8.2B
- **Qwen2.5-Omni**：- **rank**：6；- **scope**：9000-question test；- **sound**：76.77；- **music**：67.33；- **speech**：68.90；- **model_link**：https://arxiv.org/abs/2503.20215；- **model_size**：8.2B
- **Step-Audio-2-mini**：- **rank**：7；- **scope**：9000-question test；- **sound**：75.57；- **music**：66.85；- **speech**：66.49；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：8.3B
- **Gemini 2.5 Pro**：- **rank**：8；- **scope**：9000-question test；- **sound**：70.63；- **music**：64.77；- **speech**：72.67；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Gemini 2.5 Flash**：- **rank**：9；- **scope**：9000-question test；- **sound**：69.50；- **music**：69.40；- **speech**：68.27；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Gemini 2.0 Flash**：- **rank**：10；- **scope**：9000-question test；- **sound**：68.93；- **music**：59.30；- **speech**：72.87；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **DeSTA2.5-Audio**：- **rank**：11；- **scope**：9000-question test；- **sound**：66.83；- **music**：57.10；- **speech**：71.94；- **model_link**：https://arxiv.org/abs/2507.02768；- **model_size**：8B
- **Kimi-Audio**：- **rank**：12；- **scope**：9000-question test；- **sound**：70.70；- **music**：65.93；- **speech**：56.57；- **model_link**：https://arxiv.org/abs/2504.18425；- **model_size**：8.2B
- **Audio Reasoner**：- **rank**：13；- **scope**：9000-question test；- **sound**：67.27；- **music**：61.53；- **speech**：62.53；- **model_link**：https://huggingface.co/zhifeixie/Audio-Reasoner/tree/main；- **model_size**：8.2B
- **Phi-4-multimodal**：- **rank**：14；- **scope**：9000-question test；- **sound**：62.67；- **music**：61.97；- **speech**：63.80；- **model_link**：https://huggingface.co/microsoft/phi-4；- **model_size**：5.5B
- **Gemini 2.5 Flash Lite**：- **rank**：15；- **scope**：9000-question test；- **sound**：62.50；- **music**：54.87；- **speech**：67.47；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Audio Flamingo 2**：- **rank**：16；- **scope**：9000-question test；- **sound**：68.13；- **music**：70.20；- **speech**：44.87；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：3B
- **GPT-4o Audio**：- **rank**：17；- **scope**：9000-question test；- **sound**：63.20；- **music**：49.93；- **speech**：69.33；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **Qwen2-Audio-Instruct**：- **rank**：18；- **scope**：9000-question test；- **sound**：61.17；- **music**：55.67；- **speech**：55.37；- **model_link**：https://arxiv.org/abs/2407.10759；- **model_size**：7B
- **Gemma 3n**：- **rank**：19；- **scope**：9000-question test；- **sound**：50.27；- **music**：53.20；- **speech**：62.13；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：4B
- **Gemma 3n**：- **rank**：20；- **scope**：9000-question test；- **sound**：47.47；- **music**：51.63；- **speech**：57.07；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：2B
- **GPT-4o mini Audio**：- **rank**：21；- **scope**：9000-question test；- **sound**：49.67；- **music**：35.97；- **speech**：67.47；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **M2UGen**：- **rank**：22；- **scope**：9000-question test；- **sound**：44.97；- **music**：38.53；- **speech**：35.77；- **model_link**：https://huggingface.co/M2UGen/M2UGen-MusicGen-medium；- **model_size**：7B
- **MusiLingo**：- **rank**：23；- **scope**：9000-question test；- **sound**：41.93；- **music**：41.23；- **speech**：31.70；- **model_link**：https://huggingface.co/m-a-p/MusiLingo-long-v1；- **model_size**：7B
- **SALMONN**：- **rank**：24；- **scope**：9000-question test；- **sound**：42.10；- **music**：37.83；- **speech**：28.77；- **model_link**：https://arxiv.org/pdf/2310.13289；- **model_size**：13B
- **MuLLaMa**：- **rank**：25；- **scope**：9000-question test；- **sound**：30.97；- **music**：29.67；- **speech**：17.10；- **model_link**：https://arxiv.org/pdf/2308.11276；- **model_size**：7B
- **GAMA-IT**：- **rank**：26；- **scope**：9000-question test；- **sound**：32.73；- **music**：22.37；- **speech**：11.57；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA-IT；- **model_size**：7B
- **GAMA**：- **rank**：27；- **scope**：9000-question test；- **sound**：30.73；- **music**：17.33；- **speech**：16.97；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA；- **model_size**：7B
- **LTU**：- **rank**：28；- **scope**：9000-question test；- **sound**：20.67；- **music**：15.68；- **speech**：15.33；- **model_link**：https://openreview.net/pdf?id=nBZBPXdJlC；- **model_size**：7B
- **Audio Flamingo Chat**：- **rank**：29；- **scope**：9000-question test；- **sound**：23.33；- **music**：15.77；- **speech**：7.67；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：1B

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）

#### Official v05.15.25 parsed / Test-mini.

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Nova 2 Omni | 77.8 | accuracy / % |
| Audio-Thinker | 77.7 | accuracy / % |
| Step-Audio-2 | 77.58 | accuracy / % |
| MiMo-Audio | 74.7 | accuracy / % |
| Audio Flamingo 3 | 73.30 | accuracy / % |
| Step-Audio-2-mini | 72.73 | accuracy / % |
| Gemini 2.5 Flash | 71.80 | accuracy / % |
| Gemini 2.5 Pro | 71.60 | accuracy / % |
| Qwen2.5-Omni | 71.50 | accuracy / % |
| Gemini 2.0 Flash | 70.50 | accuracy / % |
| Kimi-Audio | 68.20 | accuracy / % |
| Audio Reasoner | 67.70 | accuracy / % |
| Gemini 2.5 Flash Lite | 66.20 | accuracy / % |
| DeSTA2.5-Audio | 66.00 | accuracy / % |
| Phi-4-multimodal | 65.70 | accuracy / % |
| GPT-4o Audio | 62.50 | accuracy / % |
| Audio Flamingo 2 | 62.40 | accuracy / % |
| Qwen2-Audio-Instruct | 59.60 | accuracy / % |
| Gemma 3n | 58.00 | accuracy / % |
| GPT-4o mini Audio | 53.00 | accuracy / % |
| Gemma 3n | 51.69 | accuracy / % |
| MusiLingo | 38.20 | accuracy / % |
| M2UGen | 37.90 | accuracy / % |
| SALMONN | 34.90 | accuracy / % |
| MuLLaMa | 27.60 | accuracy / % |
| GAMA-IT | 22.83 | accuracy / % |
| GAMA | 20.82 | accuracy / % |
| LTU | 17.44 | accuracy / % |
| Audio Flamingo Chat | 16.60 | accuracy / % |

- **Nova 2 Omni**：- **rank**：1；- **scope**：1000-question test-mini；- **sound**：81.08；- **music**：70.36；- **speech**：81.98；- **model_link**：https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models；- **model_size**：-
- **Audio-Thinker**：- **rank**：2；- **scope**：1000-question test-mini；- **sound**：81.98；- **music**：74.25；- **speech**：76.88；- **model_link**：https://arxiv.org/pdf/2508.08039v1；- **model_size**：8.4B
- **Step-Audio-2**：- **rank**：3；- **scope**：1000-question test-mini；- **sound**：84.04；- **music**：73.56；- **speech**：75.15；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：-
- **MiMo-Audio**：- **rank**：4；- **scope**：1000-question test-mini；- **sound**：81.68；- **music**：74.25；- **speech**：68.17；- **model_link**：https://github.com/XiaomiMiMo/MiMo-Audio/；- **model_size**：7B
- **Audio Flamingo 3**：- **rank**：5；- **scope**：1000-question test-mini；- **sound**：79.58；- **music**：73.95；- **speech**：66.37；- **model_link**：https://www.arxiv.org/abs/2507.08128；- **model_size**：8.2B
- **Step-Audio-2-mini**：- **rank**：6；- **scope**：1000-question test-mini；- **sound**：79.30；- **music**：68.44；- **speech**：68.16；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：8.3B
- **Gemini 2.5 Flash**：- **rank**：7；- **scope**：1000-question test-mini；- **sound**：73.27；- **music**：65.57；- **speech**：76.58；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Gemini 2.5 Pro**：- **rank**：8；- **scope**：1000-question test-mini；- **sound**：75.08；- **music**：68.26；- **speech**：71.47；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Qwen2.5-Omni**：- **rank**：9；- **scope**：1000-question test-mini；- **sound**：78.10；- **music**：65.90；- **speech**：70.60；- **model_link**：https://arxiv.org/abs/2503.20215；- **model_size**：8.2B
- **Gemini 2.0 Flash**：- **rank**：10；- **scope**：1000-question test-mini；- **sound**：71.17；- **music**：65.27；- **speech**：75.08；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Kimi-Audio**：- **rank**：11；- **scope**：1000-question test-mini；- **sound**：75.68；- **music**：66.77；- **speech**：62.16；- **model_link**：https://arxiv.org/abs/2504.18425；- **model_size**：8.2B
- **Audio Reasoner**：- **rank**：12；- **scope**：1000-question test-mini；- **sound**：67.87；- **music**：69.16；- **speech**：66.07；- **model_link**：https://huggingface.co/zhifeixie/Audio-Reasoner/tree/main；- **model_size**：8.2B
- **Gemini 2.5 Flash Lite**：- **rank**：13；- **scope**：1000-question test-mini；- **sound**：63.06；- **music**：63.47；- **speech**：72.07；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **DeSTA2.5-Audio**：- **rank**：14；- **scope**：1000-question test-mini；- **sound**：70.27；- **music**：56.29；- **speech**：71.47；- **model_link**：https://arxiv.org/abs/2507.02768；- **model_size**：8B
- **Phi-4-multimodal**：- **rank**：15；- **scope**：1000-question test-mini；- **sound**：65.47；- **music**：64.37；- **speech**：67.27；- **model_link**：https://huggingface.co/microsoft/phi-4；- **model_size**：5.5B
- **GPT-4o Audio**：- **rank**：16；- **scope**：1000-question test-mini；- **sound**：64.56；- **music**：56.29；- **speech**：66.67；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **Audio Flamingo 2**：- **rank**：17；- **scope**：1000-question test-mini；- **sound**：71.47；- **music**：70.96；- **speech**：44.74；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：3B
- **Qwen2-Audio-Instruct**：- **rank**：18；- **scope**：1000-question test-mini；- **sound**：67.27；- **music**：56.29；- **speech**：55.26；- **model_link**：https://arxiv.org/abs/2407.10759；- **model_size**：7B
- **Gemma 3n**：- **rank**：19；- **scope**：1000-question test-mini；- **sound**：55.86；- **music**：56.89；- **speech**：61.26；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：4B
- **GPT-4o mini Audio**：- **rank**：20；- **scope**：1000-question test-mini；- **sound**：50.75；- **music**：39.22；- **speech**：69.07；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **Gemma 3n**：- **rank**：21；- **scope**：1000-question test-mini；- **sound**：51.35；- **music**：52.10；- **speech**：52.22；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：2B
- **MusiLingo**：- **rank**：22；- **scope**：1000-question test-mini；- **sound**：43.24；- **music**：40.12；- **speech**：31.23；- **model_link**：https://huggingface.co/m-a-p/MusiLingo-long-v1；- **model_size**：7B
- **M2UGen**：- **rank**：23；- **scope**：1000-question test-mini；- **sound**：43.24；- **music**：37.13；- **speech**：33.33；- **model_link**：https://huggingface.co/M2UGen/M2UGen-MusicGen-medium；- **model_size**：7B
- **SALMONN**：- **rank**：24；- **scope**：1000-question test-mini；- **sound**：41.14；- **music**：37.13；- **speech**：26.43；- **model_link**：https://arxiv.org/pdf/2310.13289；- **model_size**：13B
- **MuLLaMa**：- **rank**：25；- **scope**：1000-question test-mini；- **sound**：33.03；- **music**：32.34；- **speech**：17.42；- **model_link**：https://arxiv.org/pdf/2308.11276；- **model_size**：7B
- **GAMA-IT**：- **rank**：26；- **scope**：1000-question test-mini；- **sound**：30.93；- **music**：26.74；- **speech**：10.81；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA-IT；- **model_size**：7B
- **GAMA**：- **rank**：27；- **scope**：1000-question test-mini；- **sound**：31.83；- **music**：17.71；- **speech**：12.91；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA；- **model_size**：7B
- **LTU**：- **rank**：28；- **scope**：1000-question test-mini；- **sound**：20.42；- **music**：15.97；- **speech**：15.92；- **model_link**：https://openreview.net/pdf?id=nBZBPXdJlC；- **model_size**：7B
- **Audio Flamingo Chat**：- **rank**：29；- **scope**：1000-question test-mini；- **sound**：25.23；- **music**：17.66；- **speech**：6.91；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：1B

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）

#### Independent uncertainty study / mean over option permutations on test-mini

| Model / configuration | Raw score | Metric and unit |
|---|---:|---|
| Qwen2.5-Omni-7B | 75.3 | accuracy / % |
| Audio Flamingo 3 | 74.6 | accuracy / % |

- **Qwen2.5-Omni-7B**：- **scope**：MMAU test-mini 1,000, multiple-choice permutation average, Table1；- **date**：2026-09-24；- **provenance**：A retest by independent research authors, not the official standard single-run protocol; the data-revision version is not specified
- **Audio Flamingo 3**：- **scope**：MMAU test-mini 1,000, multiple-choice permutation average, Table1；- **date**：2026-09-24；- **provenance**：A re-evaluation by independent researchers, not a score from the original paper or the official leaderboard

[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

### 覆盖范围与时效

The official parsed JSON was read in full and ranked independently for Test and for Test-mini, and another community/unverified file is not included. The average over option order in the research paper is on a separate track. The original JSON has no submission-time field, the result date is Unverified, and the collection date is not the measurement date.

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

## Contact

### 公开工作邮箱

- ssakshi@umd.edu
- sonalkum@umd.edu
- sreyang@umd.edu

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 公开反馈

https://github.com/Sakshi113/MMAU/issues

[来源](https://github.com/Sakshi113/MMAU)（访问 2026-11-07）

### 官方社交

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 隐私边界

Only officially published project feedback channels are recorded; private contact details are neither collected nor inferred.

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原论文PDF

https://arxiv.org/pdf/2410.19168

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### PDF SHA-256

455dbfa3f7cb020120e3e0d0c624f707324e9596dd3b26b8c82e9b855580d41a

> SHA-256 of the downloaded PDF bytes. This does not claim that the file was uploaded again.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### PDF bytes

8505593

> Byte count of the PDF file downloaded directly.

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

## Changelog

- - **date**：2026-11-07；- **timezone**：；- **change**：核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- - **date**：2026-11-07；- **timezone**：；- **round**：1 / 深度实证复核；- **change**：补机构、维护、英语问句与音频语言的区分、隐藏test协议；重读官方parsed榜单并重核H2。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、Official README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）
