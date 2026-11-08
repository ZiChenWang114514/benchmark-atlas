# VoiceCodeBench

> In-depth review: 2026-11-08. The collection date is not the leaderboard update date; new evidence that has not been obtained does not overwrite an older source date.

What VoiceCodeBench measures is not “whether the transcription reads smoothly,” but whether structural values that downstream software depends on can be recovered in full. The authors' repository, the original paper, and Vals are not the same set of models. This page keeps them on separate tracks by source and by version, so that a change in the WER definition and a difference of endpoints are not treated as the same thing.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

## Basic information

### Short name

VoiceCodeBench

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### Full name

VoiceCodeBench

> The official name is kept; the paper title is not fabricated as a full name.

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### Benchmark version

A public test-only set; the release is identified by the HF repository commit and dataset revision, metadata schema version 1. Paper v2 changes WER and the set of baseline systems, and does not change the recordings, the annotations, or the definitions of CTEM and TSR.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08).

### Paper version

arXiv v2

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Release date

- **paper_first_submission**：2026-08-29
- **date_type**：First submission of the paper; not the same as the first release of the dataset

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Section

Speech

> Benchmark Constitution editorial classification.

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### Field tags

- 语音

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### License

Non-audio materials are MIT; the audio adds a prohibition on voice cloning, and the full LICENSE must be read.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench) (accessed 2026-11-07).

### Paper

https://arxiv.org/abs/2608.28916

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Code

https://huggingface.co/datasets/besimple-ai/voice-code-bench

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 数据地址

https://huggingface.co/datasets/besimple-ai/voice-code-bench

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Official entry

https://www.vals.ai/benchmarks/voice-code-bench

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### Paper title

VoiceCodeBench: Evaluating Exact Structured-Token Recovery in Automatic Speech Recognition

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

## Origin and maintenance

### Initiating organizations

Besimple AI

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 署名合作机构

Vals AI provides an external implementation and a leaderboard; joint creation of the data is not inferred from that.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Authors

- Tyler Baumgartner
- Brandon Tai
- Lisa Kaelin-Martin
- Candice Fan
- Luc Debaupte
- Bill Wang
- Yi Zhong

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Maintainer

Besimple AI maintains the data; Vals AI maintains its evaluation implementation.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Funders

Besimple, Inc.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

## Design goals

### Abilities measured

Exactly recovers structured values such as telephone numbers, identifiers, paths, URLs, commands, and units in English workplace speech.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Design background

Transcriptions with similar WER may differ on critical values, and fluent text is not necessarily executable correctly by software.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

## Construction

### 题目与数据来源

Entity type, count, and difficulty are chosen first, and synthetic values are then used to build work scenarios and scripts; the recordings are human.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 构建者背景

85 paid recording contributors who consented to data release; the research team reviewed the entities.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Review process

Scripts are generated with LLM assistance and reviewed by hand for naturalness, uniqueness, entity consistency, and recoverability; a recording of poor quality is made again.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Quality control

1,482 entities were audited; each recording is checked for errors of reading aloud and for serious problems of audio quality, and a recording that is rejected is made again. Human audit agreed completely with 200 verifier decisions on a stratified sample, but the audit covers only the original 12 systems and cannot prove that the judge has zero error on 23 systems.

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08).

### 去污染与泄漏防范

Public test-only, with no training set provided; public labels mean the set can be adapted to, and any benchmark-specific specialization must be disclosed.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

## Data format

### Size

300 WAV recordings, 5.587 hours, 85 speakers, 1482 entities, 26 types, and 8 workflow domains.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench) (accessed 2026-11-07).

### 任务形式

Audio transcription; three text layers, template/acoustic/canonical, and entity annotation.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Modalities

- 音频
- 文本

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### Languages

English

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 难度与类型

light has 30 segments, standard 114 segments, dense 93 segments, and stress 63 segments; they increase with text length, entity count, and interference. The artificial quotas are diagnostic coverage, not production incidence; the target word-count interval in the datasheet and the actual word-count range in the paper are read separately.

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08).

### Public and hidden splits

300 recordings in a single public test split, with no training corpus and no hidden leaderboard.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

## Evaluation

### Metrics

TSR=the proportion of recordings in which every target entity is correct; CTEM=the proportion of correct entities; WER/WAcc are auxiliary.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 评分

A versioned LLM verifier judges whether the canonical value can be recovered uniquely; a harmless change of format is allowed, and a wrong symbol, digit, or unit is not. TSR gives no partial credit.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 提示和复现设置

raw-audio-only, with no domain, no entity prompt, no vocabulary, no grammar constraint, and no correction after transcription. Streaming scores only the final transcript.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 官方脚本

scripts and scoring/reproduce_release.sh on HF; Vals ported them to Valkyrie.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench) (accessed 2026-11-07).

### 可比性提示

The author's current CSV with 23 configurations, the v2 paper with 19 configurations, the frozen paper_results.csv with 12 configurations, and Vals with 20 configurations are on separate tracks. Both v2 and the current implementation use format-invariant WER. The difference between Vals and v2 cannot be attributed to the WER definition in v1. Model, endpoint, and streaming settings differ. Real-time total latency includes playback at speaking rate, and TTFP is reported separately.

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08); [3](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [4](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv) (accessed 2026-11-08); [5](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

## Current status

### 核验时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08).

### 数据版本与当前状态

- **version**：Managed by HF repository revision; metadata schema 1.
- **current_baselines**：23
- **paper_v2_configurations**：19
- **frozen_paper_results_csv_rows**：12
- **note**：The README and the current CSV, the v2 paper, the frozen paper_results.csv, and datasheet(13) are not the same set of models; a change in the set of models is not treated as newly added recordings.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08); [3](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [4](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [5](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv) (accessed 2026-11-08).

### 论文修订与H2证据

- **revisions**：- - **version**：v1
 - **date**：2026-08-29
 - - **version**：v2
 - **date**：2026-09-12
- **note**：The paper revision time cannot be treated as the data release date. Existing 2026-H2 evidence retains the original collection date.

Sources: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### 饱和程度

The highest TSR in the authors' current CSV is 0.6866666666666666, which the README displays as 68.7%. There are still recordings on which at least one key entity fails to be recovered. TSR over a whole passage is not saturated. A high score on some numeric kind of entity is not used to infer that ASR ability as a whole has been solved.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08); [3](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08).

### 污染、冲突与限制

Public labels do not support a hidden leaderboard. Training or custom adaptation would break the validity of the test. v1 has 12 configurations and ordinary acoustic-reference WER. v2 has 19 configurations and format-invariant WER, and the correlation coefficients were corrected from −0.73/−0.73 to −0.28/−0.22. The current README and CSV have 23 systems, while the frozen paper_results.csv still has 12 rows and the datasheet writes 13. They are recorded separately, and the lag in the documentation is not concealed. The Vals methods page still describes the historical paper as "12 paper baselines / strict WER," and that description cannot be used to interpret the 19-configuration results of v2.

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08); [3](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08); [4](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [5](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv) (accessed 2026-11-08); [6](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### 后续工作与衍生

This project treats recovery of exact values as a supplement to general WER. The official data card and the paper discuss related work such as ContextASR-Bench, and they do not treat that work as a version of this collection. Vals/Valkyrie is an external evaluation port, not a newly added dataset.

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08); [3](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08).

## Leaderboard snapshot

### 快照采集日

2026-11-08

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### Official leaderboard

https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08).

### 第三方覆盖

https://www.vals.ai/benchmarks/voice-code-bench

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### Author's current CSV

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| 1 | deepgram_nova3 | 0.6866666666666666 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 3 | deepgram_nova3 | 0.9089068825910931 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 16 | deepgram_nova3 | 0.08155390369774158 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 6 | openai_gpt_transcribe | 0.61 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 5 | openai_gpt_transcribe | 0.8927125506072875 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 8 | openai_gpt_transcribe | 0.061431750390606506 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 14 | assemblyai_universal_3_5_pro | 0.5166666666666667 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 12 | assemblyai_universal_3_5_pro | 0.865047233468286 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 1 | assemblyai_universal_3_5_pro | 0.03823209128355665 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 7 | google_cloud_chirp_3 | 0.6033333333333334 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 7 | google_cloud_chirp_3 | 0.8879892037786775 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 6 | google_cloud_chirp_3 | 0.05840159083376734 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 3 | elevenlabs_scribe_v2 | 0.6766666666666666 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 2 | elevenlabs_scribe_v2 | 0.9156545209176788 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 12 | elevenlabs_scribe_v2 | 0.06872307182425075 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 12 | whisper_large_v3 | 0.5433333333333333 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 8 | whisper_large_v3 | 0.8758434547908233 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 5 | whisper_large_v3 | 0.058164859618389284 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 16 | modal_inkling | 0.49666666666666665 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 16 | modal_inkling | 0.8427800269905533 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 2 | modal_inkling | 0.04860091851711567 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 20 | modal_nvidia_parakeet_tdt_0_6b_v3 | 0.37333333333333335 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 20 | modal_nvidia_parakeet_tdt_0_6b_v3 | 0.7860998650472335 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 20 | modal_nvidia_parakeet_tdt_0_6b_v3 | 0.09317740637280432 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 21 | amazon_transcribe_streaming | 0.33666666666666667 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 22 | amazon_transcribe_streaming | 0.752361673414305 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 22 | amazon_transcribe_streaming | 0.10295440556791818 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 4 | cartesia_ink_2_streaming | 0.6366666666666667 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 4 | cartesia_ink_2_streaming | 0.9014844804318488 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 19 | cartesia_ink_2_streaming | 0.09282230954973723 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 5 | deepgram_nova3_streaming | 0.6166666666666667 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 6 | deepgram_nova3_streaming | 0.8893387314439946 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 18 | deepgram_nova3_streaming | 0.0927512901851238 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 1 | openai_gpt_live_transcribe_streaming | 0.6866666666666666 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 1 | openai_gpt_live_transcribe_streaming | 0.9176788124156545 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 7 | openai_gpt_live_transcribe_streaming | 0.05854362956299418 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 22 | assemblyai_universal_3_6_pro_streaming | 0.27666666666666667 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 21 | assemblyai_universal_3_6_pro_streaming | 0.7685560053981106 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 3 | assemblyai_universal_3_6_pro_streaming | 0.05080251882013162 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 15 | google_cloud_chirp_3_streaming | 0.5033333333333333 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 13 | google_cloud_chirp_3_streaming | 0.8609986504723347 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 10 | google_cloud_chirp_3_streaming | 0.06685289522276408 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 18 | elevenlabs_scribe_v2_realtime_streaming | 0.4633333333333333 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 17 | elevenlabs_scribe_v2_realtime_streaming | 0.840080971659919 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 11 | elevenlabs_scribe_v2_realtime_streaming | 0.0681312437858056 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 19 | inworld_stt_1 | 0.44 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 18 | inworld_stt_1 | 0.8373819163292847 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 21 | inworld_stt_1 | 0.09672837460347522 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 23 | inworld_stt_1_streaming | 0.06333333333333334 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 23 | inworld_stt_1_streaming | 0.33873144399460187 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 23 | inworld_stt_1_streaming | 0.5732683111595095 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 11 | meta_muse_voice_transcribe_1_0 | 0.5533333333333333 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 8 | meta_muse_voice_transcribe_1_0 | 0.8758434547908233 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 14 | meta_muse_voice_transcribe_1_0 | 0.07459400596562663 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 9 | meta_muse_voice_transcribe_1_0_streaming | 0.5566666666666666 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 11 | meta_muse_voice_transcribe_1_0_streaming | 0.8677462887989204 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 13 | meta_muse_voice_transcribe_1_0_streaming | 0.07388381231949245 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 9 | xai_grok_voice_transcribe_2_0 | 0.5566666666666666 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 13 | xai_grok_voice_transcribe_2_0 | 0.8609986504723347 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 15 | xai_grok_voice_transcribe_2_0 | 0.07710335684863406 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 8 | xai_grok_voice_transcribe_2_0_streaming | 0.56 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 15 | xai_grok_voice_transcribe_2_0_streaming | 0.8582995951417004 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 17 | xai_grok_voice_transcribe_2_0_streaming | 0.08706974101605038 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 13 | mistral_voxtral_mini_transcribe_2 | 0.5233333333333333 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 10 | mistral_voxtral_mini_transcribe_2 | 0.8690958164642375 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 4 | mistral_voxtral_mini_transcribe_2 | 0.054968988210785476 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 17 | mistral_voxtral_mini_transcribe_realtime_streaming | 0.48 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 18 | mistral_voxtral_mini_transcribe_realtime_streaming | 0.8373819163292847 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |
| 9 | mistral_voxtral_mini_transcribe_realtime_streaming | 0.06647412527815917 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv |

#### The authors froze paper_results.csv (12 configurations, not v2 Table 5).

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| 1 | deepgram_nova3 | 0.6866666666666666 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 2 | deepgram_nova3 | 0.9089068825910931 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 9 | deepgram_nova3 | 0.08155390369774158 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 6 | openai_gpt_4o_transcribe | 0.5566666666666666 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 7 | openai_gpt_4o_transcribe | 0.8738191632928475 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 2 | openai_gpt_4o_transcribe | 0.044245064154159366 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 8 | assemblyai_universal_3_pro | 0.5033333333333333 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 9 | assemblyai_universal_3_pro | 0.8454790823211876 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 1 | assemblyai_universal_3_pro | 0.043227119928033714 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 4 | google_cloud_chirp_3 | 0.6033333333333334 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 4 | google_cloud_chirp_3 | 0.8879892037786775 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 4 | google_cloud_chirp_3 | 0.05840159083376734 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 2 | elevenlabs_scribe_v2 | 0.6766666666666666 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 1 | elevenlabs_scribe_v2 | 0.9156545209176788 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 8 | elevenlabs_scribe_v2 | 0.06872307182425075 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 7 | whisper_large_v3 | 0.5433333333333333 fraction | TSR 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 6 | whisper_large_v3 | 0.8758434547908233 fraction | CTEM 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 3 | whisper_large_v3 | 0.058164859618389284 fraction | WER 300 recordings；1482 target entities | batch；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 11 | amazon_transcribe_streaming | 0.33666666666666667 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 12 | amazon_transcribe_streaming | 0.752361673414305 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 12 | amazon_transcribe_streaming | 0.10295440556791818 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 3 | deepgram_nova3_streaming | 0.6166666666666667 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 3 | deepgram_nova3_streaming | 0.8893387314439946 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 11 | deepgram_nova3_streaming | 0.0927512901851238 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 5 | openai_gpt_realtime_whisper_streaming | 0.5933333333333334 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 5 | openai_gpt_realtime_whisper_streaming | 0.8873144399460189 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 10 | openai_gpt_realtime_whisper_streaming | 0.08593343118223569 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 12 | assemblyai_universal_3_pro_streaming | 0.33 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 11 | assemblyai_universal_3_pro_streaming | 0.7827260458839406 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 5 | assemblyai_universal_3_pro_streaming | 0.06074522986601013 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 8 | google_cloud_chirp_3_streaming | 0.5033333333333333 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 8 | google_cloud_chirp_3_streaming | 0.8609986504723347 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 6 | google_cloud_chirp_3_streaming | 0.06685289522276408 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 10 | elevenlabs_scribe_v2_realtime_streaming | 0.4633333333333333 fraction | TSR 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 10 | elevenlabs_scribe_v2_realtime_streaming | 0.840080971659919 fraction | CTEM 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |
| 7 | elevenlabs_scribe_v2_realtime_streaming | 0.0681312437858056 fraction | WER 300 recordings；1482 target entities | streaming；https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv |

#### Vals independent implementation

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| 1 | GPT Live Transcribe | 67.67 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 2 | Grok Voice Transcribe 2.0 | 65.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 3 | Cartesia Ink 2 | 62.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 4 | GPT 4o Transcribe | 59.67 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 5 | Deepgram Nova-3 (Streaming) | 59.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 6 | Reson8 Resonant-1 | 59.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 7 | Inworld STT 1 | 57.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 8 | Whisper Large-v3 Turbo | 57.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 9 | Muse Voice Transcribe | 57.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 10 | Deepgram Flux General English | 55.67 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 11 | Google Cloud Chirp 3 | 55.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 12 | ElevenLabs Scribe v2 Realtime | 55.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 13 | Whisper Large-v3 | 54.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 14 | Voxtral Mini Transcribe 2 | 53.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 15 | Grok Voice Transcribe 1.0 | 52.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 16 | GPT 4o Mini Transcribe (Streaming) | 51.67 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 17 | Voxtral Mini Transcribe Realtime 2602 | 46.0 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 18 | Cohere Transcribe | 44.67 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 19 | Azure Speech Universal Language Model | 37.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| 20 | AssemblyAI Universal-3.5 Pro | 30.33 % | TSR | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |

#### Vals independent implementation/chart to one decimal place

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT Live Transcribe | 91.4 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | GPT Live Transcribe | 94.1 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Grok Voice Transcribe 2.0 | 90.6 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Grok Voice Transcribe 2.0 | 89.5 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Cartesia Ink 2 | 89.5 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Cartesia Ink 2 | 90.8 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | GPT 4o Transcribe | 88.7 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | GPT 4o Transcribe | 96.0 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Deepgram Nova-3 (Streaming) | 88.0 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Deepgram Nova-3 (Streaming) | 90.5 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Reson8 Resonant-1 | 88.7 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Reson8 Resonant-1 | 93.6 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Inworld STT 1 | 88.0 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Inworld STT 1 | 91.9 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Whisper Large-v3 Turbo | 87.6 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Whisper Large-v3 Turbo | 93.3 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Muse Voice Transcribe | 87.9 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Muse Voice Transcribe | 92.4 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Deepgram Flux General English | 86.6 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Deepgram Flux General English | 90.6 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Google Cloud Chirp 3 | 86.8 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Google Cloud Chirp 3 | 93.4 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | ElevenLabs Scribe v2 Realtime | 86.8 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | ElevenLabs Scribe v2 Realtime | 94.9 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Whisper Large-v3 | 87.2 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Whisper Large-v3 | 94.2 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Voxtral Mini Transcribe 2 | 87.0 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Voxtral Mini Transcribe 2 | 94.5 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Grok Voice Transcribe 1.0 | 84.7 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Grok Voice Transcribe 1.0 | 91.0 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | GPT 4o Mini Transcribe (Streaming) | 86.6 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | GPT 4o Mini Transcribe (Streaming) | 95.2 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Voxtral Mini Transcribe Realtime 2602 | 83.3 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Voxtral Mini Transcribe Realtime 2602 | 93.4 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Cohere Transcribe | 83.9 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Cohere Transcribe | 93.0 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Azure Speech Universal Language Model | 80.7 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | Azure Speech Universal Language Model | 89.6 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | AssemblyAI Universal-3.5 Pro | 77.1 % | CTEM | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |
| — | AssemblyAI Universal-3.5 Pro | 94.5 % | WAcc | 2026-09-24；https://www.vals.ai/benchmarks/voice-code-bench |

#### Original paper v2 Table 5 (19 configurations)

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | ElevenLabs Scribe v2 | 6.9 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | ElevenLabs Scribe v2 | 91.6 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | ElevenLabs Scribe v2 | 67.7 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Deepgram Nova-3 | 8.2 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Deepgram Nova-3 | 90.9 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Deepgram Nova-3 | 68.7 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | OpenAI gpt-transcribe | 6.1 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | OpenAI gpt-transcribe | 89.3 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | OpenAI gpt-transcribe | 61.0 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Google Cloud Chirp 3 | 5.8 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Google Cloud Chirp 3 | 88.8 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Google Cloud Chirp 3 | 60.3 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Whisper large-v3 | 5.8 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Whisper large-v3 | 87.6 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Whisper large-v3 | 54.3 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Meta Muse Voice Transcribe 1.0 | 7.5 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Meta Muse Voice Transcribe 1.0 | 87.6 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Meta Muse Voice Transcribe 1.0 | 55.3 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | AssemblyAI Universal-3 Pro | 4.3 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | AssemblyAI Universal-3 Pro | 84.5 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | AssemblyAI Universal-3 Pro | 50.3 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inkling-NVFP4 via Modal | 4.9 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inkling-NVFP4 via Modal | 84.3 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inkling-NVFP4 via Modal | 49.7 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inworld STT 1 | 9.7 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inworld STT 1 | 83.7 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inworld STT 1 | 44.0 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | NVIDIA Parakeet TDT 0.6B v3 | 9.3 % | WER | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | NVIDIA Parakeet TDT 0.6B v3 | 78.6 % | CTEM | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | NVIDIA Parakeet TDT 0.6B v3 | 37.3 % | TSR | batch；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | OpenAI gpt-live-transcribe | 5.9 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | OpenAI gpt-live-transcribe | 91.8 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | OpenAI gpt-live-transcribe | 68.7 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Cartesia Ink 2 | 9.3 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Cartesia Ink 2 | 90.1 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Cartesia Ink 2 | 63.7 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Deepgram Nova-3 | 9.3 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Deepgram Nova-3 | 88.9 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Deepgram Nova-3 | 61.7 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Meta Muse Voice Transcribe 1.0 | 7.4 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Meta Muse Voice Transcribe 1.0 | 86.8 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Meta Muse Voice Transcribe 1.0 | 55.7 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Google Cloud Chirp 3 | 6.7 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Google Cloud Chirp 3 | 86.1 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Google Cloud Chirp 3 | 50.3 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | ElevenLabs Scribe v2 Realtime | 6.8 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | ElevenLabs Scribe v2 Realtime | 84.0 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | ElevenLabs Scribe v2 Realtime | 46.3 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | AssemblyAI Universal-3 Pro | 6.1 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | AssemblyAI Universal-3 Pro | 78.3 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | AssemblyAI Universal-3 Pro | 33.0 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Amazon Transcribe | 10.3 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Amazon Transcribe | 75.2 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Amazon Transcribe | 33.7 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inworld STT 1 | 57.3 % | WER | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inworld STT 1 | 33.9 % | CTEM | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |
| — | Inworld STT 1 | 6.3 % | TSR | streaming；2026-09-12；https://arxiv.org/pdf/2608.28916 |

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv) (accessed 2026-11-08); [3](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08); [4](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08).

### Coverage note

Four source tracks contain 222 structured metric values in total: 23 configurations in the current author CSV, 12 in the frozen CSV, 19 in the v2 paper, and 20 models on Vals together with their CTEM and WAcc charts. The original precision, the streaming marks, and the source dates are kept. The update time of the Vals page, 2026-09-24, is not the update time of the author CSV. A rank inside one track cannot be interpreted across tracks.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv) (accessed 2026-11-08); [3](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08); [4](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

## Contact

### 公开联系邮箱

- tyler@besimple.ai
- yi@besimple.ai

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### 问题反馈

https://huggingface.co/datasets/besimple-ai/voice-code-bench/discussions

> The project code is hosted on HF and is not claimed to be GitHub Issues; the official dataset card requires reproduction information to be provided through issues and PRs.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08).

### 官方讨论渠道

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### 隐私与数据使用

People who made the recordings took part for pay and consented to publication. Only anonymous IDs and coarse-grained attributes are made public. A voiceprint may still identify a person. Cloning a voice is prohibited, and the material is not to be used for identity recognition, biometric modeling, demographic profiling, or an attempt at re-identification. Script values are synthetic or retained ranges, not records of a private account.

Sources: [1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/LICENSE) (accessed 2026-11-08).

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2608.28916

> Entry point for the original paper PDF; not downloaded or uploaded; hash and byte count Unverified.

Source: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08).

### SHA-256

80f42d91580ff561e9cff6ac999e9130020642fc63bd1f43f8e53342579cfddb

> Original bytes of the PDF downloaded again. The existing copy was not overwritten.

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08).

### 字节数

454778

Sources: [1](https://arxiv.org/pdf/2608.28916) (accessed 2026-11-08).

### Folder

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### Other documents

- - **type**：Official web-page methods and leaderboard (not a PDF)
 - **url**：https://www.vals.ai/benchmarks/voice-code-bench

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

### 原文归档

Unverified

> Not uploaded within the scope of this batch; this is not an official Not disclosed.

Sources: [1](https://www.vals.ai/benchmarks/voice-code-bench) (accessed 2026-11-08).

## Changelog

### 本页修订

- - **date**：2026-11-07
 - **change**：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。
- - **date**：2026-11-08
 - **round**：2
 - **change**：逐项打开arXiv摘要与PDF全文、Official README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

Sources: [1](https://arxiv.org/abs/2608.28916) (accessed 2026-11-08); [2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md) (accessed 2026-11-08).
