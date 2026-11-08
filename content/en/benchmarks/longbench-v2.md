# LongBench v2
> Verification: 2026-11-08. Review of the official evidence is complete; the 2026-H2 usage evidence has been reread; unknown fields and document conflicts are retained explicitly

LongBench v2 uses four-choice questions on real long documents. The emphasis is deep understanding and reasoning, rather than retrieval alone. The unit of length is words; although the 503 questions are named train on HF, they are in fact public evaluation questions. Direct answering and CoT are two independent protocols, and the data license on the official site should also be kept separate from the software license.

Overview basis: [S1](https://arxiv.org/abs/2412.15204)

## Basic information

**简称**：LongBench v2 [S1](https://arxiv.org/abs/2412.15204)

**全称**：LongBench v2 [S1](https://arxiv.org/abs/2412.15204)

**版本口径**：LongBench v2 (distinguished from the older LongBench v1). [S2](https://github.com/THUDM/LongBench)

**论文修订**：arXiv v2 [S3](https://arxiv.org/abs/2412.15204)

**发布时间**：2024-12-20 [S2](https://github.com/THUDM/LongBench)

> The date of the release announcement in the official README, kept distinct from the date the paper was first released.

**主板块**：语言 [S1](https://arxiv.org/abs/2412.15204)

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

**领域**：Long-context understanding [S1](https://arxiv.org/abs/2412.15204)

**许可与权利边界**：The data card for LongBench-v2 is Apache-2.0. The LICENSE at the root of the THUDM/LongBench repository is MIT (2023 THU-KEG & Zhipu AI). The license for the data and the license for the software in the repository are recorded separately and are not written as one. [S4](https://huggingface.co/datasets/THUDM/LongBench-v2) [S5](https://github.com/THUDM/LongBench/blob/main/LICENSE)

**论文**：https://arxiv.org/abs/2412.15204 [S1](https://arxiv.org/abs/2412.15204)

**代码入口**：https://github.com/THUDM/LongBench [S1](https://arxiv.org/abs/2412.15204)

**数据入口**：https://huggingface.co/datasets/THUDM/LongBench-v2 [S1](https://arxiv.org/abs/2412.15204)

**官网**：https://longbench2.github.io/ [S1](https://arxiv.org/abs/2412.15204)

**论文标题**：LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks [S1](https://arxiv.org/abs/2412.15204)

## Origin and maintenance

**发起方**：Author affiliations in the paper include Tsinghua University and Zhipu; Yushi Bai is the first author. [S1](https://arxiv.org/abs/2412.15204)

**署名与合作**：The first page of the paper explicitly gives the author affiliations as Tsinghua University and Zhipu.AI; the 24 reviewers were selected from 97 annotators and are not 24 fully independent question writers recruited in addition. [S6](https://arxiv.org/pdf/2412.15204)

**作者**：Bai, Yushi；Tu, Shangqing；Zhang, Jiajie；Peng, Hao；Wang, Xiaozhi；Lv, Xin；Cao, Shulin；Xu, Jiazheng；Hou, Lei；Dong, Yuxiao；Tang, Jie；Li, Juanzi [S1](https://arxiv.org/abs/2412.15204)

**维护入口**：The official public code is hosted under THUDM; this records the maintenance entry point of the repository and is not a basis for inferring institutional legal liability or a commitment of continued maintenance. [S2](https://github.com/THUDM/LongBench)

**资助**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

## Design goals

**衡量能力**：Tests deep understanding and reasoning in real long contexts, beyond a simple needle-in-a-haystack. [S1](https://arxiv.org/abs/2412.15204)

**设计动机**：Retrieving only a fixed needle, or easier short question answering, is not enough to measure understanding of long documents, multiple documents, code repositories, and structured data. [S1](https://arxiv.org/abs/2412.15204)

## Construction

**题目/样本来源**：Annotators submit academic, legal, fiction, code, and tabular materials they have actually encountered, and questions are then written from those materials. [S1](https://arxiv.org/abs/2412.15204)

**构建者背景**：97 annotators with higher education and 24 expert reviewers. [S1](https://arxiv.org/abs/2412.15204)

**审查流程**：Difficulty screening by 3 models, human review, and rework; only entries that pass review receive a reward. [S1](https://arxiv.org/abs/2412.15204)

**质量控制**：Multiple-choice questions are used to improve scoring consistency, while timed answers by experts estimate difficulty. [S1](https://arxiv.org/abs/2412.15204)

**去污染与防泄漏**：KG reasoning anonymizes entities in order to limit memorization; the annotation guide requires that common classic literature be avoided or that the questions be obscure, rejects questions that can be answered without the materials, and checks documents for duplication. These are mitigations, not a guarantee that the full training set has no overlap. [S6](https://arxiv.org/pdf/2412.15204)

## Data format

**规模**：503 four-choice questions, 6 major task categories and 20 subtasks; context of 8k–2M words (words, not tokens). [S1](https://arxiv.org/abs/2412.15204)

**任务形式**：Four-option multiple-choice questions based on long context [S1](https://arxiv.org/abs/2412.15204)

**模态**：文本 [S1](https://arxiv.org/abs/2412.15204)

**语言**：英语 [S1](https://arxiv.org/abs/2412.15204)

**难度与覆盖**：There are 192 easy questions and 311 hard questions. By length, short is under 32k words and has 180 questions, medium is 32k–128k words and has 215 questions, and long is over 128k words and has 108 questions. With experts limited to 15 minutes, the result is 53.7%. That is not a ceiling on human ability when time is not limited. [S6](https://arxiv.org/pdf/2412.15204)

**公开与测试划分**：The official HF load uses split=train for 503 evaluation questions, and the answers are public; train here is the name of a file split and does not mean the split is suitable for training. [S2](https://github.com/THUDM/LongBench)

## Evaluation

**指标**：Overall accuracy, and accuracy by the easy/hard grouping and the short/medium/long grouping. [S1](https://arxiv.org/abs/2412.15204)

**评分**：The final choice is extracted from the model output and compared with the gold standard. [S1](https://arxiv.org/abs/2412.15204)

**提示/训练/运行设置**：The zero-shot setting in the original paper uses temperature=0.1 and max_new_tokens=128; CoT first uses 1024 tokens and then a second call of 128 tokens to take the final answer. The code also supports --cot, --no_context, and --rag N; the settings of models added on the web page cannot be assumed to equal the paper. [S6](https://arxiv.org/pdf/2412.15204) [S7](https://github.com/THUDM/LongBench)

**官方脚本**：https://github.com/THUDM/LongBench [S2](https://github.com/THUDM/LongBench)

**可比性警示**：words are not equal to tokens. Context truncation, CoT, thinking budget, and YaRN affect the results. A footnote on the official site states that the Qwen results use YaRN factor4, which cannot be copied as the setting for every model in the original paper. [S1](https://arxiv.org/abs/2412.15204)

## Current status

**核查日**：2026-11-08 [S8](https://longbench2.github.io/)

**数据版本与持续使用**：v2 [S9](https://huggingface.co/datasets/THUDM/LongBench-v2)

**论文版本与证据历史**：v1 2024-12-20；v2 2025-01-03。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S3](https://arxiv.org/abs/2412.15204)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The highest readable overall w/CoT on the official site is 63.3%, which is not enough to declare from that figure that every long-context task is saturated; the update time of that static table also calls for caution. [S10](https://longbench2.github.io/)

**已知问题与争议**：The human score in the body of the paper and on the official website is 53.7%; 50.1% once appeared in the conclusion of the paper, and that figure is also the historical score of GPT-4o under direct answering. This entry adopts the human score of 53.7% from the body and from the official website, and it retains a statement of the conflict. [S1](https://arxiv.org/abs/2412.15204)

**版本/衍生关系**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

## Leaderboard snapshot

**快照日**：2026-11-08 [S11](https://longbench2.github.io/#leaderboard)

**官方榜入口**：https://longbench2.github.io/#leaderboard [S10](https://longbench2.github.io/)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

### Official: direct answer

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Human | 53.7% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 2 | MiniMax-Text-01 MiniMax | 52.9% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 3 | GPT-4o OpenAI | 50.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 4 | Gemini-Exp-1206 Google | 49.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 5 | Gemini-2.0-Flash Google | 47.4% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 6 | Qwen3-235B-A22B-Instruct-2507 Alibaba | 46.7% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 7 | GPT-4o OpenAI | 46.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 8 | Kimi-K2-Instruct Moonshot AI | 44.9% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 9 | GLM-4-Plus Z.ai & Tsinghua | 44.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 10 | Qwen2.5-72B Alibaba | 42.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 11 | Claude 3.5 Sonnet Anthropic | 41.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 12 | Qwen3-235B-A22B | 40.4% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 13 | Qwen3-32B | 38.8% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 14 | o1-mini OpenAI | 37.8% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 15 | Mistral Large 24.11 Mistral AI | 34.4% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 16 | Qwen3-30B-A3B | 32.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 17 | Llama 3.1 70B Meta | 31.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 18 | Nemotron 70B Nvidia | 31.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 19 | NExtLong 8B CAS | 30.8% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 20 | GLM-4-9B Z.ai & Tsinghua | 30.2% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 21 | Qwen2.5-7B Alibaba | 30.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 22 | Llama 3.1 8B Meta | 30.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 23 | Llama 3.3 70B Meta | 29.8% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 24 | GPT-4o mini OpenAI | 29.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 25 | Command R+ Cohere | 27.8% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 26 | Mistral Large 2 Mistral AI | 26.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 27 | Random | 25.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |

### Official: w/ CoT

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Gemini-2.5-Pro | 63.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 2 | Gemini-2.5-Flash | 62.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 3 | Qwen3-235B-A22B-Thinking-2507 | 60.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 4 | DeepSeek-R1 | 58.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 5 | Qwen3-235B-A22B-Instruct-2507 Alibaba | 58.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 6 | o1-preview | 57.7% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 7 | DeepSeek-R1-0528 | 56.7% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 8 | MiniMax-Text-01 MiniMax | 56.5% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 9 | Gemini-2.0-Flash-Thinking | 56.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 10 | Human | 53.7% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 11 | Gemini-Exp-1206 Google | 52.5% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 12 | GPT-4o OpenAI | 51.4% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 13 | GPT-4o OpenAI | 51.2% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 14 | Gemini-2.0-Flash Google | 51.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 15 | GLM-4.5 | 50.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 16 | Qwen3-30B-A3B-Thinking-2507 | 50.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 17 | Qwen3-235B-A22B | 50.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 18 | Qwen3-32B | 49.2% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 19 | QwQ-32B | 48.9% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 20 | GLM-4.5-Air | 48.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 21 | Claude 3.5 Sonnet Anthropic | 46.7% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 22 | GLM-4-Plus Z.ai & Tsinghua | 46.1% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 23 | Kimi-K2-Instruct Moonshot AI | 44.3% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 24 | Qwen2.5-72B Alibaba | 43.5% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 25 | Qwen3-30B-A3B | 42.5% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 26 | Mistral Large 24.11 Mistral AI | 39.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 27 | o1-mini OpenAI | 38.9% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 28 | Llama 3.1 70B Meta | 36.2% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 29 | Llama 3.3 70B Meta | 36.2% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 30 | Qwen2.5-7B Alibaba | 35.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 31 | Nemotron 70B Nvidia | 35.2% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 32 | Mistral Large 2 Mistral AI | 33.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 33 | GPT-4o mini OpenAI | 32.4% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 34 | NExtLong 8B CAS | 32.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 35 | Command R+ Cohere | 31.6% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 36 | GLM-4-9B Z.ai & Tsinghua | 30.8% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 37 | Llama 3.1 8B Meta | 30.4% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |
| 38 | Random | 25.0% | Overall accuracy | [来源](https://longbench2.github.io/)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S8](https://longbench2.github.io/)

**覆盖与时效**：Every readable cell for a direct answer and for CoT in the official table is transcribed, and the two are ranked separately. A cell marked “-” is not filled with 0. Model names, context lengths, and the original Date are kept. The footer of the webpage says Last Update 2025-05-06, but the table contains rows dated 2025-07. The contradiction in the dates is kept. [S8](https://longbench2.github.io/)

## Contact

**公开研究邮箱**：待核实 [S1](https://arxiv.org/abs/2412.15204)

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

**问题反馈**：https://github.com/THUDM/LongBench/issues [S2](https://github.com/THUDM/LongBench)

**官方发布渠道**：https://x.com/realYushiBai/status/1869946577349132766 [S7](https://github.com/THUDM/LongBench)

> The project release Thread linked from the official README; X content is not being read.

**隐私口径**：Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected. [S12](urn:benchmark-atlas:constitution:v0.1)

## Original files

**源站PDF**：https://arxiv.org/pdf/2412.15204 [S13](https://arxiv.org/pdf/2412.15204)

**PDF SHA-256**：35e7e66bb3323d8da0a6dde553a9f5fc9be97ed3232d87a24be89f5a8f9024d5 [S6](https://arxiv.org/pdf/2412.15204)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：9951437 [S6](https://arxiv.org/pdf/2412.15204)

**原有文件夹**：{"id": "1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE", "webViewLink": " [S14](

**其他材料**：[{"kind": "Chinese introduction", "id": "17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8", "webViewLink": " [S15](

**原有 PDF**：{"id": "1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx", "webViewLink": " [S16](

## Changelog

- 2026-11-07，首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- 2026-11-07，深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S1](https://arxiv.org/abs/2412.15204) [S13](https://arxiv.org/pdf/2412.15204) [S2](https://github.com/THUDM/LongBench) [S8](https://longbench2.github.io/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2412.15204](https://arxiv.org/abs/2412.15204)，访问 2026-11-07
- S2，[https://github.com/THUDM/LongBench](https://github.com/THUDM/LongBench)，访问 2026-11-07
- S3，[https://arxiv.org/abs/2412.15204](https://arxiv.org/abs/2412.15204)，访问 2026-11-08
- S4，[https://huggingface.co/datasets/THUDM/LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2)，访问 2026-11-08
- S5，[https://github.com/THUDM/LongBench/blob/main/LICENSE](https://github.com/THUDM/LongBench/blob/main/LICENSE)，访问 2026-11-08
- S6，[https://arxiv.org/pdf/2412.15204](https://arxiv.org/pdf/2412.15204)，访问 2026-11-08
- S7，[https://github.com/THUDM/LongBench](https://github.com/THUDM/LongBench)，访问 2026-11-08
- S8，[https://longbench2.github.io/](https://longbench2.github.io/)，访问 2026-11-08
- S9，[https://huggingface.co/datasets/THUDM/LongBench-v2](https://huggingface.co/datasets/THUDM/LongBench-v2)，访问 2026-11-07
- S10，[https://longbench2.github.io/](https://longbench2.github.io/)，访问 2026-11-07
- S11，[https://longbench2.github.io/#leaderboard](https://longbench2.github.io/#leaderboard)，访问 2026-11-08
- S12，[urn:benchmark-atlas:constitution:v0.1](urn:benchmark-atlas:constitution:v0.1)，访问 2026-11-07
- S13，[https://arxiv.org/pdf/2412.15204](https://arxiv.org/pdf/2412.15204)，访问 2026-11-07
- S14，[，访问 2026-11-07
- S15，[，访问 2026-11-07
- S16，[，访问 2026-11-07
