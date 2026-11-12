# AudioMultiChallenge

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Checked item by item against the evidence: the paper PDF, the official release materials, and the leaderboards for each protocol; items not confirmed are kept

## Basic information

### Short name

AudioMultiChallenge

### Full name

Audio MultiChallenge

### 数据/软件版本

Original Audio MultiChallenge; identifier Unverified

### Paper version

arXiv:2512.14865v1；2025-12-17 03:26:44

### Release date

2025-12-17 (arXiv v1 submitted at 03:26:44; the Scale research page separately marks 12/17/2025, with no timezone timestamp)

### Section

Speech

Note: Editorial filing. Only the main section is counted.

### 学科标签

多模态；多轮对话

### 许可证与范围

MIT (ScaleAI/audiomc official dataset-card YAML)

### 论文入口

https://arxiv.org/abs/2512.14865

### Paper title

Audio MultiChallenge: A Multi-Turn Evaluation of Spoken Dialogue Systems on Natural Human Interaction

### Code

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

### Dataset

https://huggingface.co/datasets/ScaleAI/audiomc

### Official homepage

https://labs.scale.com/leaderboard/audiomc

## Origin and maintenance

### 发起团队

Scale AI

### 署名/合作机构

The 11 authors on the first page of the paper are all affiliated with Scale AI; this records the institution named in the public paper and does not infer that speakers or uncredited contributors are collaborating institutions.

### Authors

Advait Gosai；Tyler Vuong；Utkarsh Tyagi；Steven Li；Wenjia You；Miheer Bavare；Arda Uçar；Zhongwang Fang；Brian Jang；Bing Liu；Yunzhong He

### 维护入口

Scale AI

### 资助与计算资源

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

## Design goals

固定历史测试只让受测模型生成最后一轮，重点是对自然音频中的约束、记忆和修订保持。Text与Audio是不同输出模式；Audio轨评分仍看输出文本流，不等于语音自然度或音色质量。

### 测量能力

Inferential memory, instruction retention, self-consistency, and spoken revision in natural human-voice multi-turn dialogue.

### 为何需要这个基准

ASR/TTS or single-turn synthetic-speech tests have difficulty measuring robustness to hesitation, interruption, ambient sound, and multi-turn revision.

## Construction

### 材料来源

Multiple agents first use TTS to explore strategies that fail and distill them into a blueprint; humans then improvise and record natural dialogue from the blueprint and write atomic rubrics.

### 命题/编制背景

The paper describes them as highly trained core contributors. 47 speakers recorded natural improvisations from an adversarial blueprint. Specialist reviewers, an independent quality-control team, and an internal research team reviewed the recordings again. TTS audio does not itself serve as the final test set of human voices.

### Review process

Dedicated reviewers, an independent QC team, and an internal research team review, in three stages, naturalness, whether failures are valid, the audio, and the rubric.

### Quality control

Three stages of review check naturalness, whether a failure is a real one, diversity of the prompts, quality of the audio, and the rubric. The methods page on the official site reports that, on 1712 judgments of the rubric, Cohen κ between o4-mini and people is about 0.87 and Macro F1 is about 0.94. Those are approximate values reported by the authors, not values computed by this catalog.

### 去污染与证据边界

Newly collected spoken adversarial dialogues, and a final-turn rubric written for the particular instance, can reduce direct reuse of existing question-answer pairs, but the public HF card contains transcripts and history; the paper does not contain evidence of an item-by-item audit that removed duplicates from the training corpus, so the absence of contamination cannot be claimed.

## Data format

### 规模与分母

452 conversations, 1,712 rubric items, and 47 speakers; 14.99 hours of user audio at 48kHz; 3–8 turns per conversation.

### Question types

A fixed dialogue history is provided, and only the final assistant reply is evaluated; user turns are audio, and historical assistant turns are text.

### 模态与字段

音频；文本

### Languages

English

### 难度定位

A fixed context of 3–8 turns: Inference Memory, Instruction Retention, Self Coherence, and Voice Editing; 42 questions require an audio cue such as background sound or a paralinguistic signal. The difficulty is state across turns and revision that is spoken, rather than only increasing the number of turns or measuring the quality of pronunciation.

### 公开、隐藏与划分

The official HF release publishes 452 dialogues and the rubric data. Each user's audio turns, transcripts, and historical assistant text are used to fix the historical input. The last assistant reply is newly generated by the model under test. A historical assistant answer cannot be treated as that model's trajectory of free interaction. An independent training split and a hidden test split have not been verified.

Status: Unverified (part of this field is still unconfirmed).

## Evaluation

### Metrics

APR is the full-pass rate on the primary task, and ARS is a diagnostic metric for partial passes on the rubric.

### 评分流程

o4-mini makes a binary judgment on each item; APR requires every rubric on the same task to pass, and ARS is the per-task proportion of rubrics passed, then averaged.

### 运行与提示

History is fixed, user turns are audio and assistant turns are text, and only the last turn is generated and scored; Text Output and Audio Output are configured separately.

### 评测实现

The official HF dataset card publishes directly the system prompt of the o4-mini judge and the Python function build_grading_conversation_history: it follows the historical text of the dataset and replaces only the last assistant turn with the output of the model under test. It is public code for constructing a score, not a complete runner that covers every model API in one step.

Note: The address of a separate, complete code repository remains Unverified at basic_info.code_url; finding only a fragment is not a basis for claiming that a runner for the full pipeline has been released.

### 不能混比的设置

Text and Audio outputs are tracked separately; Audio mode still evaluates the text stream the model outputs and does not directly evaluate sound quality. It is not an upgraded version of MMAU.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

version：Original Audio MultiChallenge; identifier Unverified；evidence_2026_h2：- url：https://labs.scale.com/leaderboard/audiomc；date：2026-11-07；date_type：observed_on；note：Scale's current multi-turn speech leaderboard retains measured results; it is mainly a display by a single organization, and multiple Scale links are not counted as multiple independent adopters.

Note: The heat grade is adopted from the candidate; only evidence that has been opened and can be verified is retained. A does not guarantee that every version received independent reruns by multiple institutions.

### 版本脉络

v1：2025-12-17；arxiv_id：2512.14865；paper_reported_best：model：Gemini 3 Pro Preview (Thinking)；APR：54.65；output：Text；boundary：Historical experiments in the paper and the continuously updated official Text/Audio leaderboards are shown separately.

### 分数上限与饱和度

The head of the official Text leaderboard is 60.40% APR, and the head of the Audio leaderboard is 48.45% APR; both are clearly short of a perfect score, but these two different output protocols are not merged directly into a single ranking.

### 争议与局限

The question counts on the four axes of the official site write Self-Coherence/Voice Editing as 83/117, while Table 1 of the paper writes 117/83; the total of 452 agrees, and the conflict over which axis the two counts belong to remains Unverified. The Audio track scores only the output text stream and does not check the naturalness or the timbre of the original audio; the score cannot be read as speech quality in full.

Status: Unverified (part of this field is still unconfirmed).

### 衍生版本

This is not a new version of the existing mmau. MMAU focuses on audio-understanding question answering, and this entry is natural multi-turn spoken dialogue; the Text/Audio output subtracks are not created again as new entries.

Note: Already deduplicated against the existing_slugs list; relations among versions are based on the methods pages that are listed, and a different task domain is not treated as an update of the same questions.

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

https://labs.scale.com/leaderboard/audiomc

### 第三方/补充实验

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### Official current leaderboard: Text Output

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | gemini-3.8-flash (high) | 60.4 | APR (%) |
| 2 | salesforce-launa-omni-1 | 59.69 | APR (%) |
| 3 | gemini-4-argon (high) | 58.41 | APR (%) |
| 4 | Inkling (Thinking) | 56.64 | APR (%) |
| 5 | Inkling-small | 54.87 | APR (%) |

- gemini-3.8-flash (high)：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.49
- salesforce-launa-omni-1：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.13
- gemini-4-argon (high)：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.53
- Inkling (Thinking)：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale official-site snapshot；displayed_ci_plus_minus：2.7
- Inkling-small：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.57

#### Current official leaderboard: Audio Output

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | gpt-realtime-2 (xHigh) | 48.45 | APR (%) |
| 2 | tml-interaction-small | 43.36 | APR (%) |
| 3 | gpt-realtime-2 | 37.61 | APR (%) |
| 4 | gemini-3.1-flash-live-preview (Thinking) | 36.06 | APR (%) |
| 5 | gpt-realtime-1.5 | 34.73 | APR (%) |

- gpt-realtime-2 (xHigh)：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.59
- tml-interaction-small：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.55
- gpt-realtime-2：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.45
- gemini-3.1-flash-live-preview (Thinking)：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.41
- gpt-realtime-1.5：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale official-site snapshot；displayed_ci_plus_minus：4.38

#### Original paper v1 Table 2: Text Output (historical)

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Gemini 3 Pro Preview (Thinking) | 54.65 | APR (%) |
| 2 | Gemini 2.5 Pro (Thinking) | 46.9 | APR (%) |
| 3 | Gemini 2.5 Flash (Thinking) | 40.04 | APR (%) |

- Gemini 3 Pro Preview (Thinking)：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：text；source_type：Paper-fixed experiment
- Gemini 2.5 Pro (Thinking)：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：text；source_type：Paper-fixed experiment
- Gemini 2.5 Flash (Thinking)：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：text；source_type：Paper-fixed experiment

#### Original paper v1 Table 2: Audio Output (historical)

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | Qwen 3 Omni | 24.34 | APR (%) |
| 2 | GPT 4o Audio Preview | 23.23 | APR (%) |
| 3 | GPT Realtime | 20.35 | APR (%) |

- Qwen 3 Omni：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：audio；source_type：Paper-fixed experiment
- GPT 4o Audio Preview：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：audio；source_type：Paper-fixed experiment
- GPT Realtime：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：audio；source_type：Paper-fixed experiment

### 覆盖边界

The Text Output and Audio Output dedicated leaderboards were each opened, and the output mode of the top three on the combined page is no longer left blank. rank is the order currently displayed on each page, and a statistically significant ranking is not computed separately. The page also defines Rank(UB). The Inkling confidence interval is ±4.55 on the combined page and ±2.70 on the Text page. The value from the corresponding dedicated page is used, and the conflict is recorded. Per-model run dates and the leaderboard update time remain Unverified.

## Contact

### 公开作者工作邮箱

advait.gosai@scale.com

### 公开反馈

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

### 官方账号

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://arxiv.org/pdf/2512.14865

Note: Entry point for the official arXiv PDF of the original paper; this group does not download or upload it.

### 下载源文件SHA-256

d724dd047b476408bef588fac478984c0237e76a84c7e9096ff64f330d145e57

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

2393184

### 既有文件夹

Unverified

Note: The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

Status: Unverified (part of this field is still unconfirmed).

### 其他材料

- type：Official methods or project page；url：https://labs.scale.com/leaderboard/audiomc；accessed：2026-11-07

### 既有 PDF链接

Unverified

Note: This group only created a staging entry and did not upload.

Status: Unverified (part of this field is still unconfirmed).

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传。
- 2026-11-07：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

### 来源索引

[1]: https://labs.scale.com/leaderboard/audiomc "访问 2026-11-07"
[2]: https://arxiv.org/abs/2512.14865 "访问 2026-11-07"
[3]: https://huggingface.co/datasets/ScaleAI/audiomc/raw/main/README.md "访问 2026-11-07"
[4]: https://scale.com/research/audiomc "访问 2026-11-07"
[5]: https://arxiv.org/pdf/2512.14865 "访问 2026-11-07"
[6]: https://labs.scale.com/leaderboard/audiomc-text "访问 2026-11-07"
[7]: https://huggingface.co/datasets/ScaleAI/audiomc "访问 2026-11-07"
[8]: https://labs.scale.com/leaderboard/audiomc-audio "访问 2026-11-07"
