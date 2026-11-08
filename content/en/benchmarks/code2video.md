# Code2Video Bench

> Benchmark Constitution, in-depth verification snapshot 2026-11-07. Unverified is not the same as Not disclosed; the collection date is not the leaderboard update time.

Code2Video Bench evaluates “writing code that generates a good video,” and it does not only check whether the code can run. The original HeyGen version has 168 human reference clips and briefs and a preference judge trained by the authors; AA is an independent implementation with 114 briefs and a Gemini judge. The two Elo figures depend on different question sets, judges, and pools of opponents, and they must be shown on separate tracks.

Basis of the reading guide: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07); [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07); [1](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07)

## Basic information

**简称**：Code2Video Bench

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**全称**：Code2Video Benchmark（Benchmarking Code-to-Video: Evaluating AI Agents on the Art of Motion Design）

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**基准版本**：The HeyGen web report of 2026-09-18: 168 items; the independent AA edition, Code2Video-AA: 114 items. These are not one semantic version of the same question set.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**论文版本**：An official web technical report dated 2026-09-18; it is not presented as an arXiv paper on that basis.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**发布日期**：2026-09-18 (date of the HeyGen technical report)

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**主板块**：多模态

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：Benchmark Constitution editorial filing. Artificial Analysis places it under Coding.

**领域**：代码生成；Motion graphics/video design

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**许可与范围**：The HyperFrames rendering framework is Apache-2.0; independent licenses for the 168 benchmark assets, the reference videos, and the judge API are Unverified.

Sources: [1](https://raw.githubusercontent.com/heygen-com/hyperframes/main/LICENSE) (accessed 2026-11-07 ) ; [2](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**论文/技术报告**：https://www.heygen.com/research/introducing-code2video-benchmark

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**代码**：https://github.com/heygen-com/hyperframes

Sources: [1](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

核验说明：The HyperFrames rendering framework, not the evaluation code itself.

**数据**：https://www.kaggle.com/benchmarks/heygen/code2video

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**主页**：https://www.heygen.com/research/introducing-code2video-benchmark

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**论文标题**：Benchmarking Code-to-Video: Evaluating AI Agents on the Art of Motion Design

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

## Origin and maintenance

**发起/作者单位**：HeyGen

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**合作关系**：Kaggle (jointly releases the full benchmark); Artificial Analysis (independent implementation Code2Video-AA)

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

**作者**：Abhay Zala, Miao Yang, Wenbo Zhu, Bin Liu, and the Kaggle Team

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**维护方**：HeyGen

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**资助**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Design goals

**测量能力**：From a design brief, write code that can be deterministically rendered as video (HTML/GSAP), measuring the quality of motion design and not only whether the code runs.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

**针对的不足**：Model leaderboards mostly test questions with checkable answers; creative and video categories lack quantitative evaluation.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

## Construction

**材料来源**：HeyGen design briefs and human-reference composite works

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**出题背景**：Human reference motion-design works and design briefs are created by people; preference annotators first receive basic training in motion design and are screened. The report authors are HeyGen researchers and the Kaggle Team.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**审核**：Paired human preferences are collected along each design axis, and annotators take part in the evaluation after training and screening; the report uses the retained sample pairs to test agreement between the judge and humans.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**质控**：Preference annotators are trained and then screened; the authors report that the judge scores 82% on the 1,464 samples of a human-alignment evaluation, and a general-purpose VLM scores 75%. This is an evaluation by the authors, not the correctness rate on the video task; when VLMs are compared, the order of the videos is swapped in order to control position bias.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**去污染边界**：The report shows held-out sample pairs that were not used to train the judge; this supports only a test of judge generalization, and it is not proof of pretraining decontamination for the generative model under test.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

## Data format

**规模与统计口径**：The original HeyGen version has 168 human-created motion-reference videos and briefs, covering 8 types of product-launch clips; the independent AA version has 114 briefs. The two are not added together to pad the question count.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**任务形式**：Code generation → rendered video → pairwise comparison

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**模态**：Text brief；HTML/JS code；视频

Sources: [1](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

**语言**：The report and the public example briefs are in English; the output is HTML/CSS/JavaScript motion-graphics code. This is not a basis for claiming that only one language of rendered text is used.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**难度**：Coverage includes Hook, Problem, Product intro, Key feature, Benefits, Social proof, Call to action, and Brand outro; the difficulty is timing, composition, and craft, rather than whether the syntax can run, and no single examination difficulty level is set.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**公开/保留划分**：HeyGen says that it released, with Kaggle, all references, briefs, and the judge API; a static fetch of the Kaggle page this time obtained only the title, and the file list was not verified independently. The AA page separately marks Private Dataset and at the same time displays 3 tasks from a public split; the two release states cannot be written as one.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

## Evaluation

**指标**：Elo (pairwise comparison); AA is the mean of five-axis Elo, anchored at GPT-5.5 (xhigh)=1000

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

**评分**：Five axes: appeal, fit to intent, composition, temporal consistency, and craft; HeyGen uses a self-trained judge model, and AA uses Gemini 4 Argon for blind judging

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

**提示与运行设定**：HeyGen gives the model under test a HyperFrames skill, runs 168 prompts, and renders them, pairing them round-robin with human references and with other models; AA generates one HyperFrames HTML/GSAP work for each brief. The specific run budget has not been verified, and it is not conjectured.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**脚本/运行入口**：Rendering framework and skill: https://github.com/heygen-com/hyperframes; HeyGen says that Kaggle runs Harbor-compatible data and a custom harness, and the renderer cannot be treated as the complete scoring code of the benchmark.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**可比性**：The original HeyGen version and the AA implementation differ in the number of questions and in the judge, so their Elo scores cannot be compared with each other; Elo depends on the opponent pool.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

## Current status

**本次核验**：2026-11-07

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**当前版本证据**：version：The HeyGen web report of 2026-09-18: 168 items; the independent AA edition, Code2Video-AA: 114 items. These are not one semantic version of the same question set.；evidence_2026_h2：url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；organization：Artificial Analysis；note：The current methods page lists Code2Video Bench as an evaluation currently being carried out and discloses the task or scoring protocol.；url：https://artificialanalysis.ai/evaluations；date：2026-11-07；organization：Artificial Analysis；note：The current public evaluation catalog lists Code2Video Bench on its own; this is not a mention in the news.；url：https://www.heygen.com/research/introducing-code2video-benchmark；date：2026-11-07；organization：HeyGen；note：The official HeyGen introduction of the original benchmark and the independent AA implementation are both present.；trending：heat_confidence：A；summary：The HeyGen video-generation code evaluation is marked New in the AA catalog and is implemented independently.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**修订历史**：The verified web technical report is dated 2026-09-18; no verifiable arXiv revision sequence was found.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**饱和**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**争议与局限**：Elo changes with the pool of opponents and with the judge; HeyGen’s self-trained judge and AA’s Gemini 4 Argon are not the same scorer. The confidence intervals reported for the top 4 overlap, so a significant win cannot be decided from the point estimate alone.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**派生/去重**：Code2Video-AA is an independent implementation by AA, with 114 items and a five-axis Gemini judge; it is recorded on a separate track from HeyGen’s 168 items and self-trained judge, and scores are not merged or counted twice.

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

## Leaderboard snapshot

**快照日**：2026-11-07

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**官方榜**：https://www.kaggle.com/benchmarks/heygen/code2video

Sources: [1](https://www.kaggle.com/benchmarks/heygen/code2video) (accessed 2026-11-07 ) ; [2](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

**独立评测**：https://artificialanalysis.ai/evaluations/code2video-aa

Sources: [1](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 )

### 分轨结果（不合并来源/题集/协议）

**AA / Code2Video-AA / 114 briefs**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | Claude Opus 5.5 (Max, Default Fallback) | 1536 | five-axis mean Elo |
| 2 | Claude Sonnet 5.5 (Max, Default Fallback) | 1443 | five-axis mean Elo |
| 3 | GPT-6 Astra (Max) | 1427 | five-axis mean Elo |
| 4 | GPT-6.1 Sol (Max) | 1369 | five-axis mean Elo |
| 5 | Claude Fable 5.1 (Max, Default Fallback) | 1325 | five-axis mean Elo |
| 6 | Gemini 4 Argon (High) | 1259 | five-axis mean Elo |
| 7 | Claude Haiku 5.5 (Max) | 1192 | five-axis mean Elo |
| 8 | Grok 4.7 (Xhigh) | 1127 | five-axis mean Elo |
| 9 | DeepSeek V4.1 Flash (Max) | 1053 | five-axis mean Elo |
| 10 | MiMo-V2.6-Flash | 1052 | five-axis mean Elo |
| 11 | MiMo-V2.6-Pro | 1052 | five-axis mean Elo |
| 12 | Kimi K3 (Max) | 1041 | five-axis mean Elo |
| 13 | GLM-5.3 (Max) | 1034 | five-axis mean Elo |
| 14 | GPT-6 Luna (Max) | 1030 | five-axis mean Elo |
| 15 | Qwen3.8 Max (0902) | 1021 | five-axis mean Elo |
| 16 | Inkling 2 Small | 1020 | five-axis mean Elo |
| 17 | Muse Spark 1.3 (Max) | 1019 | five-axis mean Elo |
| 18 | GPT-5.5 (Xhigh) | 1000 | five-axis mean Elo |
| 19 | Muse Wonder (Max) | 997 | five-axis mean Elo |
| 20 | GLM-5.3-Flash | 975 | five-axis mean Elo |
| 21 | Qwen3.8 27B (Xhigh) | 949 | five-axis mean Elo |
| 22 | Mistral Large 4 Preview | 931 | five-axis mean Elo |
| 23 | Gemini 3.8 Flash (High) | 899 | five-axis mean Elo |
| 24 | Step 5 Preview | 821 | five-axis mean Elo |
| 25 | MiniMax-M3 | 724 | five-axis mean Elo |
| 26 | Beam 1.0 | 675 | five-axis mean Elo |
| 27 | Inkling (Xhigh) | 467 | five-axis mean Elo |
| 28 | Nemotron 3 Ultra 550B A55B (Reasoning) | 304 | five-axis mean Elo |

Sources: [https://artificialanalysis.ai/evaluations/code2video-aa](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; 其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Engagement**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-5.5 | 1578 | Elo |
| 2 | gpt-6-astra | 1576 | Elo |
| 3 | claude-opus-5 | 1571 | Elo |

scope：Reports the within-axis rank among the overall top5, not an axis leaderboard of all models

Sources: [https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; 其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Prompt-Intent**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-6-astra | 1577 | Elo |
| 2 | gpt-5.5 | 1575 | Elo |
| 3 | claude-opus-5 | 1570 | Elo |

scope：Reports the within-axis rank among the overall top5, not an axis leaderboard of all models

Sources: [https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; 其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Composition**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-5.5 | 1585 | Elo |
| 1 | gpt-6-astra | 1585 | Elo |
| 3 | claude-opus-5 | 1576 | Elo |

scope：Reports the within-axis rank among the overall top5, not an axis leaderboard of all models

Sources: [https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; 其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Temporal**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-5.5 | 1579 | Elo |
| 2 | gpt-6-astra | 1578 | Elo |
| 3 | gpt-5.6-sol | 1568 | Elo |

scope：Reports the within-axis rank among the overall top5, not an axis leaderboard of all models

Sources: [https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; 其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Craft**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-6-astra | 1586 | Elo |
| 2 | gpt-5.5 | 1585 | Elo |
| 3 | claude-opus-5 | 1574 | Elo |

scope：Reports the within-axis rank among the overall top5, not an axis leaderboard of all models

Sources: [https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; 其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：All 28 configurations in the AA table were entered (the chart separately writes 27 of 28, and the display difference is retained). The full model names for Max and Default Fallback are retained. HeyGen includes only the five-axis top3 values that can be verified verbatim, with no estimates read off the overall figure. The two sources are on separate tracks. Elo is not merged and is not averaged. A static Kaggle capture yielded only the title, and it cannot be called a verified live leaderboard.

Sources: [1](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [2](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [3](https://www.kaggle.com/benchmarks/heygen/code2video) (accessed 2026-11-07 )

## Contact

**公开研究邮箱**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**Issues**：https://github.com/heygen-com/hyperframes/issues

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**公开社区**：Community linked from the official HyperFrames README: https://discord.gg/fzbdWyjphr

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

**隐私原则**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

## Original files

**PDF**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**原件SHA-256**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**PDF字节数**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**目录**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

**其他文档**：type：Official web-page technical report；url：https://www.heygen.com/research/introducing-code2video-benchmark；type：Kaggle official benchmark entry；url：https://www.kaggle.com/benchmarks/heygen/code2video；type：AA independent evaluation；url：https://artificialanalysis.ai/evaluations/code2video-aa

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/evaluations/code2video-aa) (accessed 2026-11-07 ) ; [3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) (accessed 2026-11-07 )

** PDF**：待核实

Sources: [1](https://www.heygen.com/research/introducing-code2video-benchmark) (accessed 2026-11-07 )

## Changelog

- date：2026-11-07；timezone：；change：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。
- date：2026-11-07；timezone：；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
