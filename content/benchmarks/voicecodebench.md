# VoiceCodeBench

> 深度复核：2026-11-08。采集日不等于榜单更新日；未取得的新证据不覆盖旧来源日期。

VoiceCodeBench测的不是“转写是否通顺”，而是下游软件依赖的结构值是否能完整恢复。作者仓库、原论文与Vals不是同一模型集，本页按来源和版本分轨，避免把WER改版与端点差异混为一谈。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

## 基本信息

### 简称

VoiceCodeBench

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 全称

VoiceCodeBench

> 沿用官方名称；不将论文标题臆造为全称。

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 基准版本

公开test-only集合；由HF仓库commit/dataset revision标识发布，metadata schema version 1。论文v2改变WER和基线系统集，不改变录音、标注、CTEM/TSR定义。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）；[2](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 发布日期

- **paper_first_submission_kst**：2026-08-29
- **date_type**：论文首次提交，不等同数据集首次上线

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 主板块

语音

> Benchmark Constitution编辑分类。

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 领域标签

- 语音

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 许可证

非音频材料MIT；音频附加禁止声音克隆限制，须阅读完整LICENSE。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07 ）。

### 论文

https://arxiv.org/abs/2608.28916

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 官方代码

https://huggingface.co/datasets/besimple-ai/voice-code-bench

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 数据地址

https://huggingface.co/datasets/besimple-ai/voice-code-bench

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 官方入口

https://www.vals.ai/benchmarks/voice-code-bench

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 论文标题

VoiceCodeBench: Evaluating Exact Structured-Token Recovery in Automatic Speech Recognition

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

## 发起与维护

### 发起机构

Besimple AI

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 署名合作机构

Vals AI提供外部实现与榜单；不据此推断共同创建数据。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 作者

- Tyler Baumgartner
- Brandon Tai
- Lisa Kaelin-Martin
- Candice Fan
- Luc Debaupte
- Bill Wang
- Yi Zhong

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 维护方

Besimple AI维护数据；Vals AI维护其评测实现

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 资助

Besimple, Inc.

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

## 设计目标

### 衡量能力

英语工作语音中精确恢复电话、标识符、路径、URL、命令与单位等结构值。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 设计背景

WER相近的转写可能在关键值上不同，流畅文本未必可供软件正确执行。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

## 构建方式

### 题目与数据来源

先选实体类型、数量与难度，再用合成值构建工作场景和脚本；人类录音。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 构建者背景

85位付费、同意数据发布的录音贡献者；研究团队审核实体。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 审核流程

LLM辅助脚本生成，经人工自然性、唯一性、实体一致性与可恢复性审核；录音质量差则重录。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 质量控制

1,482实体经审计；每份录音检查朗读错误和严重音质问题，拒收后重录。200条分层verifier判决人工审计完全一致，但只覆盖原12系统，不能证明23系统上裁判零误差。

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）。

### 去污染与泄漏防范

public test-only，不提供训练集；公开标签意味着可被适配，需披露任何benchmark特化。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

## 数据形式

### 规模

300 WAV录音，5.587小时、85说话者、1482实体、26类型、8工作流领域。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07 ）。

### 任务形式

音频转写；template/acoustic/canonical三层文本与实体标注。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 模态

- 音频
- 文本

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 语言

英语

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 难度与类型

light 30段、standard 114段、dense 93段、stress 63段；随文本长度、实体数与干扰增加。人为配额是诊断覆盖，不是生产发生率；datasheet的目标字数区间与论文实际字数范围分开看。

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）。

### 公开与隐藏划分

300录音单一公开test split，无训练语料或隐藏榜单。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

## 评测方法

### 指标

TSR=全部目标实体都正确的录音比例；CTEM=正确实体比例；WER/WAcc作辅助。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 评分

版本化LLM verifier判断canonical值是否可唯一恢复；无害格式变化允许，错符号、数字或单位不允许；TSR不给部分分。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 提示和复现设置

raw-audio-only，不给领域、实体提示、词表、语法约束或转写后修正。流式仅评分final transcript。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 官方脚本

HF中scripts及评分/reproduce_release.sh；Vals移植到Valkyrie。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07 ）。

### 可比性提示

作者当前CSV23配置、v2论文19配置、冻结paper_results.csv12配置、Vals20配置分赛道。v2与当前实现均用format-invariant WER；不可把Vals与v2的差异归因于v1的WER定义。模型/端点/流式设置不同；实时总延迟包含按语速播放，TTFP另报。

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）；[3](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[4](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv)（访问 2026-11-08 ）；[5](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

## 最新情况

### 核验时间

2026-11-08

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）。

### 数据版本与当前状态

- **version**：按HF仓库revision管理；metadata schema 1
- **current_baselines**：23
- **paper_v2_configurations**：19
- **frozen_paper_results_csv_rows**：12
- **note**：README/当前CSV、v2论文、冻结paper_results.csv及datasheet(13)不是同一模型集；不把模型集变化当成新增录音。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）；[3](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[4](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[5](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv)（访问 2026-11-08 ）。

### 论文修订与H2证据

- **revisions**：- - **version**：v1
    - **date_kst**：2026-08-29
  - - **version**：v2
    - **date_kst**：2026-09-12
- **note**：论文修订时间已从arXiv的UTC转换为；不能当作数据发布日期。既有2026-H2证据保留原采集日期。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）；[2](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 饱和程度

当前作者CSV最高TSR为0.6866666666666666，README展示为68.7%；仍有录音存在至少一个关键实体恢复失败。整段TSR未饱和，不以某些数值类实体的高分推断整个ASR能力已解决。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）；[3](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）。

### 污染、冲突与限制

公开标签不支持隐藏榜单，训练或定制适配会破坏测试有效性。v1为12配置、普通acoustic-reference WER；v2为19配置、format-invariant WER，相关系数从−0.73/−0.73更正为−0.28/−0.22。当前README/CSV为23系统，而冻结paper_results.csv仍12行、datasheet写13；分别记录，不掩盖文档滞后。Vals方法页仍以“论文12基线/严格WER”描述历史论文，不能用来解释v2的19配置结果。

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）；[3](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）；[4](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[5](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv)（访问 2026-11-08 ）；[6](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 后续工作与衍生

该项目把精确值恢复作为通用WER的补充；官方数据卡与论文讨论ContextASR-Bench等相关工作，不把它们当本集合版本。Vals/Valkyrie是外部评测移植，不是新增数据集。

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[2](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）；[3](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）。

## 榜单快照

### 快照采集日

2026-11-08

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[2](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 官方榜单

https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）。

### 第三方覆盖

https://www.vals.ai/benchmarks/voice-code-bench

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### 作者当前CSV

|名次|模型|数值|指标/范围|设置与日期|
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

#### 作者冻结paper_results.csv（12配置，非v2表5）

|名次|模型|数值|指标/范围|设置与日期|
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

#### Vals独立实现

|名次|模型|数值|指标/范围|设置与日期|
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

#### Vals独立实现/图表一位小数

|名次|模型|数值|指标/范围|设置与日期|
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

#### 原论文v2 Table 5（19配置）

|名次|模型|数值|指标/范围|设置与日期|
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

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv)（访问 2026-11-08 ）；[3](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）；[4](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）。

### 覆盖说明

四个来源赛道共222个结构化指标值：当前作者CSV23配置、冻结CSV12配置、v2论文19配置及Vals20模型及其CTEM/WAcc图表；保留原精度、流式标记与来源日期。Vals页面更新时间2026-09-24并非作者CSV更新时间。每个赛道内排名不能跨赛道解释。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/results.csv)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/baselines/paper_results.csv)（访问 2026-11-08 ）；[3](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）；[4](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

## 联系方式

### 公开联系邮箱

- tyler@besimple.ai
- yi@besimple.ai

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### 问题反馈

https://huggingface.co/datasets/besimple-ai/voice-code-bench/discussions

> 项目代码托管HF，不冒称GitHub Issues；官方数据卡要求通过issues/PR提供复现信息。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）。

### 官方讨论渠道

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 隐私与数据使用

录音者付费参与并同意发布，仅公开匿名ID及粗粒度属性；声纹仍可能识别个人。禁止克隆声音，且不适用于身份识别、生物特征建模、人口画像或尝试重识别。脚本值为合成/保留范围，不是私人账户记录。

来源：[1](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/DATASET_CARD.md)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/LICENSE)（访问 2026-11-08 ）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2608.28916

> 原始论文PDF入口；未下载或上传，哈希与字节数待核实。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）。

### SHA-256

80f42d91580ff561e9cff6ac999e9130020642fc63bd1f43f8e53342579cfddb

> 重新下载的原始PDF字节；既有副本未覆盖。

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）。

### 字节数

454778

来源：[1](https://arxiv.org/pdf/2608.28916)（访问 2026-11-08 ）。

### 文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 其他文档

- - **type**：官方网页方法与榜单（非PDF）
  - **url**：https://www.vals.ai/benchmarks/voice-code-bench

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

### 原文归档

待核实

> 按本批范围不上传；不是官方未公开。

来源：[1](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-08 ）。

## 变更记录

### 本页修订

- - **date**：2026-11-07
  - **timezone**：
  - **change**：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。
- - **date**：2026-11-08
  - **timezone**：
  - **round**：2
  - **change**：逐项打开arXiv摘要与PDF全文、官方README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

来源：[1](https://arxiv.org/abs/2608.28916)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/besimple-ai/voice-code-bench/raw/main/README.md)（访问 2026-11-08 ）。
