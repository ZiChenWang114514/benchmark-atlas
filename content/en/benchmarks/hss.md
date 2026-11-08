# HSS

> Benchmark Constitution, source-by-source in-depth check: 2026-11-08. The collection date does not represent the experiment date; Unverified is not the same as Not disclosed.

HSS is directed at implicit visual reasoning that an adult can solve by intuition and that a model tends to overthink. There are 522 questions, with answers and rubrics written by hand, including 288 images and 234 videos. The arXiv paper is supplied, together with the revision of the question cards dated 2026-10-08. It is marked that MIT covers the annotations only and does not cover the original media.

Basis of the reading guide: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08); [2](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08); [3](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

## Basic information

### Short name

HSS

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Full name

Humanity’s Sixth Sense

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Benchmark version

A frozen release of 522 questions; the HF update record of 2026-10-08 adds evidence time windows for all 234 videos and revises one question prompt.

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### Paper version

arXiv v2

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

### Release date

2026-10-07 (date of the first arXiv draft; not the separate release date of the dataset).

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

### Section

Multimodal

> Benchmark Constitution editorial filing.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 领域

```json
[
 "Intuitive visual reasoning"
 "Video understanding"
 "Spatial/social reasoning"
]
```

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 许可与使用范围

```json
{
 "annotations": "MIT: prompts, reference answers, rubric, and taxonomy labels"
 "media": "Images and video are not covered by the MIT license above; the rights remain with the original authors. HF states that they are provided only along with the benchmark for non-commercial research and evaluation, and users must follow the original media terms."
}
```

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### 论文入口

https://arxiv.org/abs/2610.08966

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08); [2](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

### Code

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Dataset

https://huggingface.co/datasets/ScaleAI/HSS

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Official homepage

https://labs.scale.com/leaderboard/hss

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Paper title

Humanity’s Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

## Origin and maintenance

### Initiators

Scale AI

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 合作与作者单位

Elorian; there is also a University of California, Santa Cruz author affiliation.

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08); [2](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### Authors

 Xingang Guo¹*, Jing Gu²*, Brian Jang¹*, Renxiong Wang¹, Utkarsh Tyagi¹, Daniel Quigley¹, Steven Li¹, David Yan², Daniel Yue Zhang¹, Darvin Yi¹, Forrest Huang², HiJae Kim¹, Tianyi Zhang², Jared Lichtarge², Jihua Huang², Le Xue², Manan Tomar², Qiuyi Richard Zhang², Ruofei Yu², Seth Neel², Yaning Hu², Marcella Valentine², Xinzhe Jiang², Daniel Evans¹, Chenguang Wang¹·³, Dustin Tran², Tong Zhao¹, Yinfei Yang², Yunzhong He¹ ¹Scale AI, ²Elorian, ³University of California, Santa Cruz，*Equal contribution

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### Maintainer

Scale AI

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 资助与资源支持

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

## Design goals

### 测量能力

Implicit temporal, spatial, social, and abstract structure that a human can infer at a glance (causality, trajectories, power relations, unwritten rules, and similar).

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 与既有基准的差异

Older visual benchmarks often emphasize analysis that requires expert knowledge, or low-level perception, and they lack a measure of the implicit temporal, spatial, social, and causal structure that an adult can grasp at a glance. HSS excludes perception questions that a clear crop alone can solve, and questions that require expert knowledge.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08).

## Construction

### Question sources

Human-written prompts, paired with images or video; the video media come from the public web, and the questions are newly written.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 出题者背景

Original work by trained human annotators; questions and answers must be understandable by adult intuition and must not require professional academic training, and each question has at least three independent reviewers besides the author.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08); [2](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### Review process

3,466 questions were written in total, and 522 were included after three rounds of independent review (a pass rate of 15.1%).

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Quality control

Three rounds of independent unanimous approval; Edit requires review from the start, and Drop removes an item permanently. 3466→1164→559→522 questions; purely perceptual questions, ambiguous questions, and questions on which consensus could not be formed were removed.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08).

### 去污染与泄漏控制

The questions are newly written, but public online media may already be in the training data and cannot be fully excluded

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

## Data format

### 规模与统计口径

522 questions: 4 domains and 11 subdomains; 288 image questions and 234 video questions (17.6 hours of video in total, a median of 76 seconds, and a longest of 28 minutes); 723 scoring criteria

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Question types

Free response, scored by rubric

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Modalities

```json
[
 "图像"
 "Video (no audio track, no subtitles)"
]
```

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Languages

The public prompts and reference answers, and the official prompts, are presented in English; complete language-distribution statistics are Unverified.

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08).

### Difficulty

Human annotators 93.1%; the best model at first release 53.6%, and the median of the models 30.9%.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### Public and hidden splits

HF has only a test split, 522 questions in total; the video-evidence time window is analysis metadata only. Evaluation must take the full video as input and must not be fed only the evidence clip.

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

## Evaluation

### Metrics

Pass@1 (mean of 3 attempts per question), with a 95% clustered bootstrap interval; the rubric score is diagnostic

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 评分规则

Claude-Opus-5 decides each item as an automatic LLM judge

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 提示、采样与工具设置

3 runs per model per question; native video is preferred, otherwise frames are sampled uniformly up to a limit of 500 frames and any stricter provider limit is followed; images keep their original resolution and are downsampled when necessary. The official-site overview states high or maximum output, but current leaderboard rows contain actual settings such as max and xhigh, which are kept per row rather than forcibly rewritten as all high.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08); [2](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08).

### 官方脚本

Official evaluation harness (including model registration, evaluation, and scoring prompts)

> Repository address Unverified.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 可比性警告

Depends on an LLM judge and carries a risk of self-preference; theory-of-mind results represent only agreement with the annotators.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

## Current status

### 核查时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08); [2](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08).

### 最新数据状态

522 questions; the HF record of 2026-10-08 states that all 234 video time windows were added and that the prompt of task 6a7f82ad5cfeb63114fa869b was revised; this is not an increase in the number of questions.

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-10-07"
 }
 {
 "version": "v2"
 "submitted_at": "2026-10-09"
 }
]
```

> The original arXiv UTC time has been converted; this does not constitute a dataset version change.

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

### 饱和度与证据边界

The paper explicitly says that the benchmark is not yet saturated: the best score at first release was 53.6%, and the baseline of 20 human annotators was 93.1%; the current high on the official site is 55.40 ± 4.20, and the count of 25 models at first release cannot be treated as the number of rows on the current leaderboard of 29.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08); [2](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08).

### 污染与已知问题

Limits of the visual channel, dependence on the judge, and the possibility that the media were already seen in training (official Limitations).

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 相关与衍生基准

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not a run date or a leaderboard-update date)

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08).

### 官方结果入口

https://labs.scale.com/leaderboard/hss

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 独立评测入口

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "Gemini-4-Argon (high)"
 "score": "55.40 ± 4.20"
 "metric": "Pass@1"
 "result_type": "Official leaderboard snapshot"
 "source_date": "Unverified (page does not mark a leaderboard update date)"
 "collected_at": "2026-11-08 "
 "source_url": "https://labs.scale.com/leaderboard/hss"
 "track": "The current official set of 522 questions, pass@1; reasoning settings are kept as given on each model row"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "GPT-6-Astra (max)"
 "score": "53.60 ± 4.10"
 "metric": "Pass@1"
 "result_type": "Official leaderboard snapshot"
 "source_date": "Unverified (page does not mark a leaderboard update date)"
 "collected_at": "2026-11-08 "
 "source_url": "https://labs.scale.com/leaderboard/hss"
 "track": "The current official set of 522 questions, pass@1; reasoning settings are kept as given on each model row"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "GPT-6.1-Sol (max)"
 "score": "46.60 ± 3.80"
 "metric": "Pass@1"
 "result_type": "Official leaderboard snapshot"
 "source_date": "Unverified (page does not mark a leaderboard update date)"
 "collected_at": "2026-11-08 "
 "source_url": "https://labs.scale.com/leaderboard/hss"
 "track": "The current official set of 522 questions, pass@1; reasoning settings are kept as given on each model row"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 4
 "model": "Claude-Opus-5.5 (xhigh)"
 "score": "44.60 ± 3.80"
 "metric": "Pass@1"
 "result_type": "Official leaderboard snapshot"
 "source_date": "Unverified (page does not mark a leaderboard update date)"
 "collected_at": "2026-11-08 "
 "source_url": "https://labs.scale.com/leaderboard/hss"
 "track": "The current official set of 522 questions, pass@1; reasoning settings are kept as given on each model row"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 5
 "model": "Muse Wonder 1.0 (max)"
 "score": "43.70 ± 4.20"
 "metric": "Pass@1"
 "result_type": "Official leaderboard snapshot"
 "source_date": "Unverified (page does not mark a leaderboard update date)"
 "collected_at": "2026-11-08 "
 "source_url": "https://labs.scale.com/leaderboard/hss"
 "track": "The current official set of 522 questions, pass@1; reasoning settings are kept as given on each model row"
 "snapshot_date": "2026-11-08 "
 }
]
```

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08).

### 覆盖与局限

29 rows of models can currently be read on the official website, and the 25 models in the summary of the method refer to the paper at first release. The ± is the half-width of a 95% interval from a bootstrap clustered by question, not a standard deviation and not the standard error of three repeats. The current leaderboard on the official website and the results from the first release of the paper cannot be presented as an experiment from the same day.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08).

## Contact

### 官方公开邮箱

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 仓库反馈

Unverified

> The official site mentions an evaluation harness, but the public pages and the paper do not give a verifiable GitHub repository address; no repository is invented.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08); [2](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

### 官方社区

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 隐私与联系边界

A media rights holder may request removal in the HF dataset discussion by providing a task_id or a file path; private contact details are not collected.

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08).

## Original files

### Paper PDF

https://arxiv.org/pdf/2610.08966

Sources: [1](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

### PDF SHA-256

86538d4f2ff2e648a97693fff6bfc2f2c25d99c71f877f4d7797430d4ef283ed

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08).

### PDF bytes

```json
9845488
```

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2610.08966) (accessed 2026-11-08).

### 已有文件夹

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

### 其他官方文档

```json
[
 {
 "type": "Official dataset card/methods entry"
 "url": "https://huggingface.co/datasets/ScaleAI/HSS"
 }
 {
 "type": "Official description"
 "url": "https://labs.scale.com/leaderboard/hss"
 }
]
```

Sources: [1](https://huggingface.co/datasets/ScaleAI/HSS) (accessed 2026-11-08); [2](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08).

### 已有 PDF归档

Unverified

> This group does not upload, as the task requires; the original PDF URL is in original_files.

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07).

## Changelog

### 历次核查

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

Sources: [1](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-07); [2](https://arxiv.org/abs/2610.08966) (accessed 2026-11-08); [3](https://labs.scale.com/leaderboard/hss) (accessed 2026-11-08).
