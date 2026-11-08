# Video-MME

> In-depth review: 2026-11-08. The collection date is not the leaderboard update date; new evidence that has not been obtained does not overwrite an older source date.

Video-MME uses real short and long videos as evidence, separating video understanding from the language shortcut of guessing from the question text alone. When results are read, subtitles, the audio track, and the frame-sampling budget matter more than a single “overall score.”

Source: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

## Basic information

### Short name

Video-MME

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Full name

Video-MME

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Benchmark version

The original Video-MME; on 2024-06-15 the official maintainers refreshed broken or potentially invalid video links and reannotated them, without naming a separate numeric version.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### Paper version

arXiv v3

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Release date

- **paper_first_submission**：2024-06-01
- **project_launch_announcement**：2024-06-03
- **note**：The announcement date in the README has no time zone attached, and the date is not shifted.

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### Section

Multimodal

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. The classification is not claimed to be set by the benchmark's maintainers.

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Field tags

- Video understanding and long video

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### License

For academic research only, and commercial use is prohibited; without permission, distributing, publishing, copying, disseminating, or modifying the data is prohibited, and video copyright belongs to the original video owners. Only the paper PDF is archived here, and the restricted videos are not redistributed.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### Paper

https://arxiv.org/abs/2405.21075

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Code

https://github.com/MME-Benchmarks/Video-MME

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### 数据地址

https://huggingface.co/datasets/lmms-lab/Video-MME

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://huggingface.co/datasets/lmms-lab/Video-MME) (accessed 2026-11-07).

### Official entry

https://video-mme.github.io/home_page.html

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Paper title

Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

## Origin and maintenance

### Initiating organizations

Video-MME Team; author affiliations in the paper include Nanjing University, the National Key Laboratory of Cognitive Intelligence, Xiamen University, the University of Hong Kong, Peking University, the Chinese University of Hong Kong, East China Normal University, and the Institute of Automation, Chinese Academy of Sciences.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### 署名合作机构

- Nanjing University
- State Key Laboratory of Cognitive Intelligence
- Xiamen University (XMU)
- The University of Hong Kong (HKU)
- Peking University (PKU)
- The Chinese University of Hong Kong (CUHK)
- East China Normal University (ECNU)
- Institute of Automation, Chinese Academy of Sciences (CASIA)

> Based on the affiliations credited on arXiv v3; organizations of models entered on the leaderboard are not mistaken for initiating partners.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### Authors

- Fu, Chaoyou
- Dai, Yuhan
- Luo, Yongdong
- Li, Lei
- Ren, Shuhuai
- Zhang, Renrui
- Wang, Zihan
- Zhou, Chenyu
- Shen, Yunhang
- Zhang, Mengdan
- Chen, Peixian
- Li, Yanwei
- Lin, Shaohui
- Zhao, Sirui
- Li, Ke
- Xu, Tong
- Zheng, Xiawu
- Chen, Enhong
- Shan, Caifeng
- He, Ran
- Sun, Xing

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08).

### Maintainer

The MME-Benchmarks / Video-MME team. Data-infringement and removal requests are received at videomme2024@gmail.com, and leaderboard submissions are received at bradyfu24@gmail.com.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### Funders

National Natural Science Foundation of China，Grant 62441234。

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

## Design goals

### Abilities measured

Video understanding and long temporal-context ability across domains, durations, and input modalities.

Source: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### Design background

Early multimodal evaluation emphasized static images and could hardly test continuous visual input and long video in a systematic way.

Source: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

## Construction

### 题目与数据来源

Not reused from an existing video dataset; the team collected real videos anew, watched each one in full and repeatedly, and then wrote the question-answer pairs by hand, covering short, medium, and long durations.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### 构建者背景

Annotators are recruited who have strong English ability and research experience in vision-language learning; they are not generically called experts with unspecified qualifications.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### Review process

After watching a video in full, each annotator writes 3 four-choice questions; another annotator checks clarity of expression, answerability, option logic, and the correct answer. Questions that fail are returned for revision.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### Quality control

After manual cross-checking, questions that can be answered without the video were filtered by giving Gemini 1.5 Pro only the question text; the paper reports that accuracy under this text-only setting is below 15%. This checks dependence on the video, and it is not a test for training contamination. On 2024-06-15, unavailable videos were also replaced and the items were labeled again.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 去污染与泄漏防范

YouTube videos were newly collected, and the questions were written by hand. Existing video datasets are not reused. Text-only filtering with Gemini 1.5 Pro reduces language shortcuts. Public videos on the internet, and public question-answer pairs, may still enter later training, so this cannot be used to prove that there is no contamination.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

## Data format

### Size

900 videos, 254 hours, and 2,700 four-choice questions; 900 audio tracks and 744 subtitle files, 3 questions per video, covering 6 major domains, 30 subclasses, and 12 task types.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 任务形式

Four-choice video QA; video frames, subtitles, and audio may be used.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### Modalities

Video frames + text, which may include audio and subtitles

Source: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### Languages

The question text and the options are in English. Video sources include a Multilingual domain, and the language of the question text cannot be equated with the language of the video or the audio track. The full distribution of audio-track languages remains Unverified.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://huggingface.co/datasets/lmms-lab/Video-MME/raw/main/README.md) (accessed 2026-11-08).

### 难度与类型

Short videos are under 2 minutes, medium videos are 4–15 minutes, and long videos are 30–60 minutes; the overall range is 11 seconds to 1 hour. Duration is not an independent difficulty label; the paper analyzes long-range dependence by the length of evidence clips.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### Public and hidden splits

The public evaluation covers 900 videos / 2,700 QA; there are 744 subtitle segments, and every long video has subtitles. The with-subtitles setting uses only the subtitles corresponding to the times of the sampled frames, and does not feed in the complete subtitles unconditionally.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

## Evaluation

### Metrics

Multiple-choice accuracy, also aggregated by video duration, domain, subcategory, and task type; the official evaluation does not call third-party scoring models such as ChatGPT.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 评分

The letter chosen by the model is extracted deterministically and accuracy is computed, without introducing a third-party model judge such as ChatGPT; short/medium/long, domain, subcategory, and task type are reported separately.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 提示和复现设置

Output only A/B/C/D; when subtitles are included, use only the subtitles that correspond to the sampled frames, and the no-subtitle protocol removes the subtitle segment. Frame count, fps, resolution, and audio permission must be recorded.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### 官方脚本

https://github.com/MME-Benchmarks/Video-MME

Sources: [1](https://github.com/MME-Benchmarks/Video-MME) (accessed 2026-11-07).

### 可比性提示

Conditions with subtitles and without them, the budget of video frames, and audio input are kept strictly apart. The abstract of FramePack-U in 2026 writes +9.7 as the gain on long video, but Appendix Table10 shows overall +9.7 and long +12.8. The detailed table is used to record the conflict.

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08); [3](https://arxiv.org/html/2610.16118v1) (accessed 2026-11-07).

## Current status

### 核验时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 数据版本与当前状态

The last repair of the data that the official README lists explicitly is dated 2024-06-15: videos that were damaged, and videos that might no longer be available, were replaced and annotated again; the item of 2025-12-05 is news that Gemini 3 Pro adopted the benchmark, and it is not a new version of the data.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 论文修订与H2证据

- **revisions**：- - **version**：v1
 - **date**：2024-06-01
 - - **version**：v2
 - **date**：2024-06-17
 - - **version**：v3
 - **date**：2025-05-30
- **continued_use_2026h2**：- - **url**：https://arxiv.org/html/2610.16118v1
 - **date**：2026-10-12
 - **note**：The Elephant in the Fridge / FramePack-U study actually uses Video-MME to evaluate long-video understanding and methods of frame packing.
 - **date**：2026-10-12

- **note**：The paper revision time cannot be treated as the data release date. Existing 2026-H2 evidence retains the original collection date.

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.16118v1) (accessed 2026-11-07); [3](https://arxiv.org/abs/2610.16118) (accessed 2026-11-07).

### 饱和程度

The leading entries of the official with-subtitles table are 81.6/81.3/79.6%, and the without-subtitles results are in a separate table; frame budgets, subtitles, and audio inputs are not aligned across models. An overall conclusion of saturation has not been verified under one setting, and a high score is not automatically called saturation.

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 污染、冲突与限制

Conditions with subtitles and without them, the budget of video frames, and audio input are kept strictly apart. The abstract of FramePack-U in 2026 writes +9.7 as the gain on long video, but Appendix Table10 shows overall +9.7 and long +12.8. The detailed table is used to record the conflict.

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08); [3](https://arxiv.org/html/2610.16118v1) (accessed 2026-11-07).

### 后续工作与衍生

The official repository also links MME, MME-RealWorld, and MME-Survey as related work; they are not revised editions of the Video-MME data, and the leaderboard scores of this entry cannot be carried over to them.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

## Leaderboard snapshot

### 快照采集日

2026-11-08; the H2 research retest keeps the earlier collection date

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### Official leaderboard

https://video-mme.github.io/home_page.html#leaderboard

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### 第三方覆盖

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Sources: [1](https://artificialanalysis.ai/evaluations?skill=multimodal) (accessed 2026-11-07).

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### Official table/without subtitles/overall

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 79.7 % | accuracy overall | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 75.0 % | accuracy overall | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 73.5 % | accuracy overall | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 70.6 % | accuracy overall | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 71.2 % | accuracy overall | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 71.9 % | accuracy overall | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 70.6 % | accuracy overall | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 70.3 % | accuracy overall | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 67.3 % | accuracy overall | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 72.1 % | accuracy overall | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 73.0 % | accuracy overall | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 73.0 % | accuracy overall | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 67.5 % | accuracy overall | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 67.6 % | accuracy overall | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 67.0 % | accuracy overall | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 70.3 % | accuracy overall | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 65.6 % | accuracy overall | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 66.2 % | accuracy overall | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 64.1 % | accuracy overall | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 65.9 % | accuracy overall | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 64.2 % | accuracy overall | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 65.3 % | accuracy overall | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 66.3 % | accuracy overall | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 64.8 % | accuracy overall | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 63.9 % | accuracy overall | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 64.6 % | accuracy overall | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 59.3 % | accuracy overall | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 63.9 % | accuracy overall | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 62.4 % | accuracy overall | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 60.9 % | accuracy overall | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 59.9 % | accuracy overall | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 60.0 % | accuracy overall | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 57.3 % | accuracy overall | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 61.2 % | accuracy overall | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 55.5 % | accuracy overall | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 55.8 % | accuracy overall | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 56.1 % | accuracy overall | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 56.0 % | accuracy overall | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 53.2 % | accuracy overall | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 52.9 % | accuracy overall | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 52.6 % | accuracy overall | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 50.7 % | accuracy overall | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 51.3 % | accuracy overall | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 43.2 % | accuracy overall | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 45.3 % | accuracy overall | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 40.6 % | accuracy overall | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 39.5 % | accuracy overall | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 39.9 % | accuracy overall | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 37.9 % | accuracy overall | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 41.1 % | accuracy overall | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 39.9 % | accuracy overall | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/with subtitles/overall

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 81.6 % | accuracy overall | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 81.3 % | accuracy overall | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 79.6 % | accuracy overall | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 79.1 % | accuracy overall | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 77.8 % | accuracy overall | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 77.2 % | accuracy overall | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 76.9 % | accuracy overall | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 75.0 % | accuracy overall | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 74.9 % | accuracy overall | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 74.0 % | accuracy overall | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 74.0 % | accuracy overall | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 73.7 % | accuracy overall | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 73.5 % | accuracy overall | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 72.1 % | accuracy overall | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 72.0 % | accuracy overall | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 71.7 % | accuracy overall | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 71.5 % | accuracy overall | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 70.3 % | accuracy overall | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 70.3 % | accuracy overall | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 70.0 % | accuracy overall | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 70.0 % | accuracy overall | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 69.7 % | accuracy overall | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 69.6 % | accuracy overall | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 68.9 % | accuracy overall | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 68.9 % | accuracy overall | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 68.8 % | accuracy overall | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 68.1 % | accuracy overall | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 67.9 % | accuracy overall | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 64.7 % | accuracy overall | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 63.7 % | accuracy overall | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 63.3 % | accuracy overall | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 62.9 % | accuracy overall | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 62.8 % | accuracy overall | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 62.4 % | accuracy overall | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 61.0 % | accuracy overall | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 59.2 % | accuracy overall | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 58.7 % | accuracy overall | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 57.6 % | accuracy overall | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 57.4 % | accuracy overall | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 57.1 % | accuracy overall | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 54.3 % | accuracy overall | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 52.4 % | accuracy overall | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 51.2 % | accuracy overall | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 47.9 % | accuracy overall | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 47.2 % | accuracy overall | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 45.9 % | accuracy overall | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 43.8 % | accuracy overall | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 43.6 % | accuracy overall | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 42.3 % | accuracy overall | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 41.9 % | accuracy overall | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 41.6 % | accuracy overall | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/without subtitles/short

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 85.0 % | accuracy short | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 81.7 % | accuracy short | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 80.6 % | accuracy short | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 81.6 % | accuracy short | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 80.1 % | accuracy short | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 80.0 % | accuracy short | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 81.4 % | accuracy short | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 78.8 % | accuracy short | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 77.3 % | accuracy short | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 82.8 % | accuracy short | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 81.2 % | accuracy short | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 81.3 % | accuracy short | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 78.9 % | accuracy short | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 76.9 % | accuracy short | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 75.0 % | accuracy short | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 79.0 % | accuracy short | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 76.8 % | accuracy short | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 80.1 % | accuracy short | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 74.8 % | accuracy short | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 77.1 % | accuracy short | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 75.7 % | accuracy short | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 78.0 % | accuracy short | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 76.7 % | accuracy short | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 72.5 % | accuracy short | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 72.8 % | accuracy short | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 74.4 % | accuracy short | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 70.0 % | accuracy short | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 75.4 % | accuracy short | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 69.8 % | accuracy short | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 71.3 % | accuracy short | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 70.5 % | accuracy short | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 71.0 % | accuracy short | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 71.0 % | accuracy short | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 72.0 % | accuracy short | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 64.0 % | accuracy short | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 65.9 % | accuracy short | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 67.0 % | accuracy short | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 66.1 % | accuracy short | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 62.2 % | accuracy short | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 61.9 % | accuracy short | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 61.1 % | accuracy short | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 60.2 % | accuracy short | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 55.8 % | accuracy short | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 49.1 % | accuracy short | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 53.3 % | accuracy short | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 45.7 % | accuracy short | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 48.3 % | accuracy short | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 48.3 % | accuracy short | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 45.7 % | accuracy short | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 46.9 % | accuracy short | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 45.3 % | accuracy short | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/with subtitles/short

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 85.4 % | accuracy short | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 84.5 % | accuracy short | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 82.8 % | accuracy short | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 84.3 % | accuracy short | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 82.2 % | accuracy short | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 82.8 % | accuracy short | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 82.8 % | accuracy short | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 79.8 % | accuracy short | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 80.6 % | accuracy short | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 83.2 % | accuracy short | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 84.0 % | accuracy short | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 83.4 % | accuracy short | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 81.2 % | accuracy short | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 78.3 % | accuracy short | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 77.0 % | accuracy short | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 80.1 % | accuracy short | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 78.7 % | accuracy short | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 80.2 % | accuracy short | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 76.6 % | accuracy short | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 79.0 % | accuracy short | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 77.6 % | accuracy short | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 76.6 % | accuracy short | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 79.3 % | accuracy short | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 74.9 % | accuracy short | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 74.3 % | accuracy short | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 77.1 % | accuracy short | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 72.8 % | accuracy short | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 78.3 % | accuracy short | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 72.0 % | accuracy short | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 73.5 % | accuracy short | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 73.2 % | accuracy short | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 73.5 % | accuracy short | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 75.8 % | accuracy short | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 72.8 % | accuracy short | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 67.4 % | accuracy short | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 70.4 % | accuracy short | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 69.9 % | accuracy short | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 68.0 % | accuracy short | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 66.0 % | accuracy short | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 66.2 % | accuracy short | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 61.6 % | accuracy short | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 61.7 % | accuracy short | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 57.6 % | accuracy short | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 52.8 % | accuracy short | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 55.4 % | accuracy short | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 51.2 % | accuracy short | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 52.8 % | accuracy short | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 53.6 % | accuracy short | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 48.4 % | accuracy short | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 47.3 % | accuracy short | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 46.1 % | accuracy short | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/without subtitles/medium

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 81.7 % | accuracy medium | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 74.3 % | accuracy medium | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 74.9 % | accuracy medium | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 68.6 % | accuracy medium | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 71.3 % | accuracy medium | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 70.3 % | accuracy medium | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 68.9 % | accuracy medium | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 68.8 % | accuracy medium | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 65.3 % | accuracy medium | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 70.9 % | accuracy medium | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 70.7 % | accuracy medium | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 73.6 % | accuracy medium | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 65.8 % | accuracy medium | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 67.0 % | accuracy medium | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 66.0 % | accuracy medium | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 71.6 % | accuracy medium | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 64.6 % | accuracy medium | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 63.7 % | accuracy medium | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 63.9 % | accuracy medium | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 64.9 % | accuracy medium | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 62.2 % | accuracy medium | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 67.8 % | accuracy medium | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 62.2 % | accuracy medium | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 63.1 % | accuracy medium | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 62.9 % | accuracy medium | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 62.9 % | accuracy medium | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 57.7 % | accuracy medium | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 63.9 % | accuracy medium | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 59.9 % | accuracy medium | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 59.4 % | accuracy medium | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 55.8 % | accuracy medium | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 57.4 % | accuracy medium | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 54.4 % | accuracy medium | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 59.1 % | accuracy medium | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 53.2 % | accuracy medium | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 52.9 % | accuracy medium | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 54.2 % | accuracy medium | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 55.3 % | accuracy medium | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 50.6 % | accuracy medium | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 51.4 % | accuracy medium | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 50.4 % | accuracy medium | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 46.4 % | accuracy medium | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 49.2 % | accuracy medium | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 41.3 % | accuracy medium | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 42.7 % | accuracy medium | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 40.3 % | accuracy medium | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 37.0 % | accuracy medium | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 36.3 % | accuracy medium | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 36.8 % | accuracy medium | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 38.7 % | accuracy medium | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 38.0 % | accuracy medium | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/with subtitles/medium

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 83.0 % | accuracy medium | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 81.0 % | accuracy medium | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 79.7 % | accuracy medium | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 76.9 % | accuracy medium | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 76.8 % | accuracy medium | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 76.6 % | accuracy medium | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 75.6 % | accuracy medium | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 74.7 % | accuracy medium | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 74.3 % | accuracy medium | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 74.1 % | accuracy medium | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 71.9 % | accuracy medium | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 74.2 % | accuracy medium | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 71.2 % | accuracy medium | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 71.7 % | accuracy medium | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 73.0 % | accuracy medium | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 68.7 % | accuracy medium | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 69.4 % | accuracy medium | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 69.6 % | accuracy medium | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 70.3 % | accuracy medium | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 68.0 % | accuracy medium | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 69.0 % | accuracy medium | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 63.8 % | accuracy medium | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 66.9 % | accuracy medium | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 68.3 % | accuracy medium | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 69.3 % | accuracy medium | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 69.1 % | accuracy medium | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 66.9 % | accuracy medium | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 69.1 % | accuracy medium | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 63.0 % | accuracy medium | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 61.1 % | accuracy medium | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 59.7 % | accuracy medium | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 60.1 % | accuracy medium | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 60.7 % | accuracy medium | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 61.3 % | accuracy medium | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 60.7 % | accuracy medium | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 56.2 % | accuracy medium | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 55.7 % | accuracy medium | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 55.4 % | accuracy medium | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 56.3 % | accuracy medium | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 54.7 % | accuracy medium | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 53.6 % | accuracy medium | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 49.1 % | accuracy medium | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 48.9 % | accuracy medium | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 47.3 % | accuracy medium | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 44.4 % | accuracy medium | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 44.6 % | accuracy medium | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 39.4 % | accuracy medium | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 39.3 % | accuracy medium | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 41.4 % | accuracy medium | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 40.4 % | accuracy medium | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 40.7 % | accuracy medium | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/without subtitles/long

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 72.3 % | accuracy long | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 67.4 % | accuracy long | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 65.0 % | accuracy long | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 61.6 % | accuracy long | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 62.2 % | accuracy long | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 65.3 % | accuracy long | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 61.5 % | accuracy long | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 61.1 % | accuracy long | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 59.3 % | accuracy long | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 62.6 % | accuracy long | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 67.1 % | accuracy long | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 64.0 % | accuracy long | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 57.8 % | accuracy long | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 58.8 % | accuracy long | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 59.0 % | accuracy long | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 63.2 % | accuracy long | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 55.4 % | accuracy long | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 54.9 % | accuracy long | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 53.7 % | accuracy long | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 55.7 % | accuracy long | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 54.8 % | accuracy long | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 55.6 % | accuracy long | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 60.0 % | accuracy long | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 58.6 % | accuracy long | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 56.0 % | accuracy long | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 56.4 % | accuracy long | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 50.1 % | accuracy long | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 52.2 % | accuracy long | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 57.6 % | accuracy long | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 51.8 % | accuracy long | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 53.5 % | accuracy long | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 51.2 % | accuracy long | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 46.4 % | accuracy long | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 52.6 % | accuracy long | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 49.2 % | accuracy long | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 48.6 % | accuracy long | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 47.1 % | accuracy long | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 46.6 % | accuracy long | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 46.7 % | accuracy long | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 45.4 % | accuracy long | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 46.2 % | accuracy long | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 45.6 % | accuracy long | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 48.9 % | accuracy long | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 39.1 % | accuracy long | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 39.8 % | accuracy long | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 35.8 % | accuracy long | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 33.2 % | accuracy long | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 35.0 % | accuracy long | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 31.3 % | accuracy long | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 37.8 % | accuracy long | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 36.2 % | accuracy long | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### Official table/with subtitles/long

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | video-SALMONN 2+ THU & ByteDance | 76.4 % | accuracy long | 10 fps 6*；2025-09-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Pro Google | 77.4 % | accuracy long | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | AdaReTaKe HIT & Huawei | 76.4 % | accuracy long | 1024；2025-03-04；https://video-mme.github.io/home_page.html |
| — | JT-VL-Chat China Mobile | 76.1 % | accuracy long | 1800；2025-07-24；https://video-mme.github.io/home_page.html |
| — | Qwen2-VL Alibaba | 74.3 % | accuracy long | 768 3*；2024-08-19；https://video-mme.github.io/home_page.html |
| — | GPT-4o OpenAI | 72.1 % | accuracy long | 384 2*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | LLaVA-Video Bytedance & NTU S-Lab | 72.5 % | accuracy long | 64；2024-08-28；https://video-mme.github.io/home_page.html |
| — | Gemini 1.5 Flash Google | 68.8 % | accuracy long | 1/0.5 fps 1*；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Oryx-1.5 THU & Tencent & NTU | 69.9 % | accuracy long | 128；2024-10-21；https://video-mme.github.io/home_page.html |
| — | InternVL2.5 Shanghai AI Lab | 64.8 % | accuracy long | 64；2024-12-13；https://video-mme.github.io/home_page.html |
| — | Keye-VL-1.5 Kwai Keye Team | 66.2 % | accuracy long | 64；2025-08-29；https://video-mme.github.io/home_page.html |
| — | TSPO XJTU & TeleAI & USTB | 63.6 % | accuracy long | 128；2025-09-22；https://video-mme.github.io/home_page.html |
| — | ViLAMP RUC & Ant Group | 68.1 % | accuracy long | 1 fps 4*；2025-04-02；https://video-mme.github.io/home_page.html |
| — | Aria Rhymes AI | 66.3 % | accuracy long | 256；2024-10-11；https://video-mme.github.io/home_page.html |
| — | Long-VITA Tencent & NJU | 66.0 % | accuracy long | 1 fps 7*；2025-07-23；https://video-mme.github.io/home_page.html |
| — | LinVT Meituan Inc | 63.3 % | accuracy long | 120；2025-02-05；https://video-mme.github.io/home_page.html |
| — | TPO Stanford University | 66.4 % | accuracy long | 96；2025-01-26；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 3 Alibaba | 61.0 % | accuracy long | 180；2025-01-24；https://video-mme.github.io/home_page.html |
| — | LiveCC NUS Show Lab & ByteDance | 64.1 % | accuracy long | 2 fps 5*；2025-04-26；https://video-mme.github.io/home_page.html |
| — | QuoTA XMU | 62.9 % | accuracy long | 64；2025-03-04；https://video-mme.github.io/home_page.html |
| — | NVILA NVIDIA | 63.3 % | accuracy long | 1024；2024-11-06；https://video-mme.github.io/home_page.html |
| — | VideoChat-Flash Shanghai AI Lab & NJU | 63.3 % | accuracy long | 512；2025-02-06；https://video-mme.github.io/home_page.html |
| — | LLaVA-OneVision Bytedance & NTU S-Lab | 62.4 % | accuracy long | 32；2024-08-08；https://video-mme.github.io/home_page.html |
| — | GPT-4o mini OpenAI | 63.4 % | accuracy long | 250；2024-07-21；https://video-mme.github.io/home_page.html |
| — | ReTaKe HIT & Huawei | 62.9 % | accuracy long | 1024；2025-02-05；https://video-mme.github.io/home_page.html |
| — | ByteVideoLLM Bytedance | 60.2 % | accuracy long | 100；2024-10-21；https://video-mme.github.io/home_page.html |
| — | mPLUG-Owl3 Alibaba | 64.5 % | accuracy long | 128；2024-11-13；https://video-mme.github.io/home_page.html |
| — | MiniCPM-o 2.6 OpenBMB | 56.3 % | accuracy long | 64；2025-01-16；https://video-mme.github.io/home_page.html |
| — | VideoLLaMA 2 Alibaba | 59.0 % | accuracy long | 32；2024-08-29；https://video-mme.github.io/home_page.html |
| — | MiniCPM-V 2.6 OpenBMB | 56.3 % | accuracy long | 64；2024-08-12；https://video-mme.github.io/home_page.html |
| — | GPT-4V OpenAI | 56.9 % | accuracy long | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Claude 3.5 Sonnet Anthropic | 54.7 % | accuracy long | 20；2024-07-30；https://video-mme.github.io/home_page.html |
| — | TimeMarker Meituan | 51.9 % | accuracy long | 128；2024-11-07；https://video-mme.github.io/home_page.html |
| — | InternVL2 Shanghai AI Lab | 53.0 % | accuracy long | 16；2024-07-18；https://video-mme.github.io/home_page.html |
| — | Video-XL SJTU & BAAI | 54.9 % | accuracy long | 128；2024-10-24；https://video-mme.github.io/home_page.html |
| — | VITA Tencent Youtu Lab & NJU | 50.9 % | accuracy long | 32；2024-09-08；https://video-mme.github.io/home_page.html |
| — | VITA 1.5 Tencent Youtu Lab & NJU | 50.4 % | accuracy long | 16；2025-01-22；https://video-mme.github.io/home_page.html |
| — | Kangaroo Meituan & UCAS | 49.3 % | accuracy long | 64；2024-07-23；https://video-mme.github.io/home_page.html |
| — | Video-CCAM QQMM | 49.9 % | accuracy long | 96；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Long-LLaVA Amazon | 50.3 % | accuracy long | 64；2024-09-09；https://video-mme.github.io/home_page.html |
| — | LongVA NTU S-Lab | 47.6 % | accuracy long | 128；2024-06-25；https://video-mme.github.io/home_page.html |
| — | InternVL-Chat-V1.5 Shanghai AI Lab | 46.6 % | accuracy long | 10；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Max Alibaba | 47.0 % | accuracy long | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGemini XMU | 43.4 % | accuracy long | 64；2024-06-20；https://video-mme.github.io/home_page.html |
| — | SliME CASIA | 41.7 % | accuracy long | 8；2024-07-16；https://video-mme.github.io/home_page.html |
| — | Chat-UniVi-v1.5 PKU | 41.8 % | accuracy long | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | VideoChat2-Mistral Shanghai AI Lab | 39.2 % | accuracy long | 16；2024-06-15；https://video-mme.github.io/home_page.html |
| — | ShareGPT4Video Shanghai AI Lab | 37.9 % | accuracy long | 16；2024-06-17；https://video-mme.github.io/home_page.html |
| — | ST-LLM PKU | 36.9 % | accuracy long | 64；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Qwen-VL-Chat Alibaba | 37.9 % | accuracy long | 4；2024-06-15；https://video-mme.github.io/home_page.html |
| — | Video-LLaVA PKU | 38.1 % | accuracy long | 8；2024-06-15；https://video-mme.github.io/home_page.html |

#### 历史来源

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Qwen3.6-27B + FramePack-U | 76.3 % | accuracy Video-MME overall, 128-frame equivalent budget, d1f16d2f448 | https://arxiv.org/html/2610.16118v1 |

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://arxiv.org/html/2610.16118v1) (accessed 2026-11-07).

### Coverage note

The only results table on the official site was read cell by cell, adding 408 values (overall/short/medium/long × with and without subtitles; missing cells are not filled with zero). The original row order is not a unified budget ranking. The per-row date is the Date in the table, and an overall update date is not inferred. The original 2026-11-07 evidence for the FramePack-U research retest is retained. Its subtitle and audio configuration was not re-verified. This is not an official live leaderboard.

Sources: [1](https://video-mme.github.io/home_page.html) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

## Contact

### 公开联系邮箱

- videomme2024@gmail.com
- bradyfu24@gmail.com

> The former handles data and copyright removal; the latter receives leaderboard results in standard JSON.

Sources: [1](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).

### 问题反馈

https://github.com/MME-Benchmarks/Video-MME/issues

Sources: [1](https://github.com/MME-Benchmarks/Video-MME) (accessed 2026-11-07).

### 官方讨论渠道

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Source: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://video-mme.github.io/home_page.html) (accessed 2026-11-08).

### 隐私与数据使用

Only officially published project feedback channels are recorded; private contact details are neither collected nor inferred.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07).

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2405.21075

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### SHA-256

81272de466da51ca55471ef58522fa5911fb802fba843780d8253d27fc0aeaa2

> Original bytes of the PDF downloaded again. The existing copy was not overwritten.

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### 字节数

4306222

Sources: [1](https://arxiv.org/pdf/2405.21075) (accessed 2026-11-08).

### Other documents

## Changelog

### 本页修订

- - **date**：2026-11-07
 - **change**：核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- - **date**：2026-11-07
 - **round**：1 / 深度实证复核
 - **change**：补版本修订、署名机构、NSFC项目、公开联系、数据更新和评测脚本规则；刷新官方前三，重核H2。
- - **date**：2026-11-08
 - **round**：2
 - **change**：逐项打开arXiv摘要与PDF全文、Official README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

Sources: [1](https://arxiv.org/abs/2405.21075) (accessed 2026-11-08); [2](https://raw.githubusercontent.com/MME-Benchmarks/Video-MME/main/README.md) (accessed 2026-11-08).
