# RULER

> Verification date: 2026-11-08. The access date is not the publication date or the run date; a field that cannot be confirmed remains Unverified.

RULER is not a fixed bank of questions. It is a generator of long-context diagnostics whose length of text and complexity of task can be controlled. It extends retrieval to several keys and several values, to tracking a variable across several hops, to aggregation, and to question answering. The question at the center is whether the model can actually use the information inside the window, rather than whether it will accept that many tokens.

Guide source: [Official materials](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08); specific facts and historical access dates are given in the individual fields.

## Basic information

### Short name

RULER

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Full name

RULER

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Benchmark version

Original RULER (13-task configuration); the current repository also points to a new v1/v2 pipeline.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07)

### Paper version

v3; latest submission 2024-08-07

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Release date

2024-04-10 (first arXiv submission; the date the data went online is not inferred).

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Section

Language

Note: Benchmark Constitution editorial filing. This is not the only field named by the paper.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Field tags

- Long-context utilization

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 许可与适用范围

Code under Apache-2.0; external corpora should follow their own licenses separately.

Sources: [1](https://raw.githubusercontent.com/hsiehjackson/RULER/main/LICENSE) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/2404.06654

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Code repository

https://github.com/hsiehjackson/RULER

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 数据地址

https://github.com/hsiehjackson/RULER

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Official homepage

https://github.com/hsiehjackson/RULER

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Paper title

RULER: What's the Real Context Size of Your Long-Context Language Models?

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

## Origin and maintenance

### 机构与发起关系

NVIDIA research team.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 合作机构/署名单位

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Authors

- Hsieh, Cheng-Ping
- Sun, Simeng
- Kriman, Samuel
- Acharya, Shantanu
- Rekesh, Dima
- Jia, Fei
- Zhang, Yang
- Ginsburg, Boris

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 当前维护入口

Official public code is hosted at hsiehjackson; this records the repository maintenance entry point and is not used to infer institutional legal liability or an ongoing maintenance commitment.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07)

### Funders

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

## Design goals

### Abilities measured

Tests the context length a model can actually use, not only the nominal window.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Design background

A single needle-in-a-haystack is easy for models to solve and cannot represent multi-hop tracking, aggregation, and question answering in long context.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Program-synthesis retrieval, multi-hop variable tracking, aggregation, and question-answering tasks, with configurable length and complexity.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 出题背景

The research team designed a controllable generator; this is not a knowledge examination written by hand, question by question.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Review process

The generator produces verifiable reference answers according to the task rules; the exact volume of item-by-item human review is Unverified.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Quality control

Evaluated by task and by length, using several tasks so that the evaluation is not limited to one retrieval pattern.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 去污染措施

Samples for retrieval, for tracking of variables, and for aggregation are synthesized by a controllable generator and by random seeds. Question answering uses SQuAD and HotpotQA, and some of the background for retrieval uses public essays by Paul Graham. A new random instance reduces the shortcut of memorizing one particular question, but a public source of questions and answers cannot guarantee that training was never exposed to it.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2404.06654) (accessed 2026-11-08)

## Data format

### Size

4 task types and 13 configurations already evaluated; samples can be generated from a random seed, a sequence length, and task complexity, and there is no fixed total number of questions.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07)

### Question types

Synthetic retrieval, variable tracking, aggregation, and question answering

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Modalities

Text

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Languages

English task templates; the specific corpus configuration should be fixed

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Difficulty

Difficulty is controlled through length, number of targets, variable chains, and similar factors, rather than through one fixed difficulty set.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 数据划分

The generation code and the task configuration are public and can be synthesized again; the random seed and the configuration must be saved in order to reproduce the result.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

## Evaluation

### Metrics

Task accuracy and target recall, with task-average metrics and metrics aggregated by length; the definition in the script that is used is authoritative.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Scoring

The target answer in a model response is compared as the task requires, then aggregated by task and by length.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 提示与运行设置

The original paper uses greedy decoding, the model chat template, and an answer prefix; the tokenizer, template, and length settings must be recorded.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 评测脚本

The original pipeline is deprecated; v1 uses NVIDIA/RULER rulerv1-ns, and v2 uses rulerv2-ns and NeMo-Skills chsieh/ruler2; the v2 example uses temperature=0 and tokens_to_generate=16384.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08); [2](https://github.com/NVIDIA/RULER/tree/rulerv2-ns) (accessed 2026-11-08)

### 可比性提醒

Different token lengths, task subsets, tokenizers, and length-weighted scores cannot be compared together; the QA subtask reported by Hunyuan is not the full set of 13 tasks.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 数据版本与更新

The official README has marked the old pipeline as deprecated and points to the rulerv1-ns and rulerv2-ns branches of NVIDIA/RULER; results from v1 and from v2 cannot be mixed without a label.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07)

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-04-10"}
- {"version": "v2", "submitted_at": "2024-04-12"}
- {"version": "v3", "submitted_at": "2024-08-07"}

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 饱和程度

The original 13 configurations are a diagnostic set in which the difficulty of the short context has already been controlled; the historical Avg in the README peaks at 96.0%, but the long context and more complex configurations may still score lower. A short length, or a high weighted score, cannot be extrapolated to saturation across the board.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2404.06654) (accessed 2026-11-08)

### 争议与已知问题

A nominal context length is not the effective window; the length of the long text, task complexity, and the choice of template may change the conclusion.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### Derivative benchmarks

The official source also provides the RULERv2 NeMo-Skills evaluation branch (rulerv2-ns); the old v1 table does not represent v2 scores.

Sources: [1](https://github.com/NVIDIA/RULER/tree/rulerv2-ns) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (access date, not the experiment run date)

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08)

### 官方榜单入口

https://github.com/hsiehjackson/RULER

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07)

### 第三方入口

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 可核验结果

- {"rank": "No cross-protocol rank", "model": "Jamba-1.5-large* (94B/398B)", "score": 96.0, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.7, "8K": 96.6, "16K": 96.4, "32K": 96.0, "64K": 95.4, "128K": 95.1}, "claimed_length": "256k", "effective_length": ">128k", "wAvg_increasing": 95.7, "wAvg_decreasing": 96.3}
- {"rank": "No cross-protocol rank", "model": "Gemini-1.5-pro", "score": 95.8, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.7, "8K": 95.8, "16K": 96.0, "32K": 95.9, "64K": 95.9, "128K": 94.4}, "claimed_length": "1M", "effective_length": ">128K", "wAvg_increasing": 95.5, "wAvg_decreasing": 96.1}
- {"rank": "No cross-protocol rank", "model": "Qwen2.5-14B-Instruct-1M* (14B)", "score": 95.7, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 97.5, "8K": 97.1, "16K": 94.6, "32K": 94.9, "64K": 94.9, "128K": 92.2}, "claimed_length": "1M", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Qwen3-235B-A22B* (235B)", "score": 95.0, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 97.7, "8K": 97.2, "16K": 96.4, "32K": 95.1, "64K": 93.3, "128K": 90.6}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Qwen3-14B* (14B)", "score": 94.6, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 98.0, "8K": 97.8, "16K": 96.4, "32K": 96.1, "64K": 94.0, "128K": 85.1}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Jamba-1.5-mini (12B/52B)", "score": 93.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.6, "8K": 95.6, "16K": 94.8, "32K": 94.6, "64K": 92.8, "128K": 90.0}, "claimed_length": "256K", "effective_length": ">128K", "wAvg_increasing": 93.1, "wAvg_decreasing": 94.8}
- {"rank": "No cross-protocol rank", "model": "Qwen3-32B* (32B)", "score": 93.7, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 98.4, "8K": 96.0, "16K": 96.2, "32K": 94.4, "64K": 91.8, "128K": 85.6}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "EXAONE-4.0-32B* (32B)", "score": 93.1, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.3, "8K": 94.9, "16K": 93.9, "32K": 93.6, "64K": 91.7, "128K": 88.2}, "claimed_length": "128K", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Qwen2.5-7B-Instruct-1M* (7B)", "score": 91.8, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.8, "8K": 95.3, "16K": 93.0, "32K": 91.1, "64K": 90.4, "128K": 84.4}, "claimed_length": "1M", "effective_length": ">128K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Qwen3-30B-A3B* (30B)", "score": 91.6, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.5, "8K": 97.0, "16K": 95.3, "32K": 92.4, "64K": 89.1, "128K": 79.2}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "GPT-4-1106-preview", "score": 91.6, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.6, "8K": 96.3, "16K": 95.2, "32K": 93.2, "64K": 87.0, "128K": 81.2}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 89.0, "wAvg_decreasing": 94.1}
- {"rank": "No cross-protocol rank", "model": "Llama3.1 (70B)", "score": 89.6, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.5, "8K": 95.8, "16K": 95.4, "32K": 94.8, "64K": 88.4, "128K": 66.6}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 85.5, "wAvg_decreasing": 93.7}
- {"rank": "No cross-protocol rank", "model": "Qwen3-8B* (8B)", "score": 89.1, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.3, "8K": 96.0, "16K": 91.8, "32K": 91.2, "64K": 82.1, "128K": 77.4}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Mistral-Large-2411 (123B)", "score": 86.0, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.4, "8K": 96.3, "16K": 95.3, "32K": 94.0, "64K": 85.9, "128K": 48.1}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 79.5, "wAvg_decreasing": 92.5}
- {"rank": "No cross-protocol rank", "model": "Command-R-plus-0824 (104B)", "score": 87.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.0, "8K": 95.1, "16K": 94.0, "32K": 92.4, "64K": 85.4, "128K": 64.6}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 83.4, "wAvg_decreasing": 92.4}
- {"rank": "No cross-protocol rank", "model": "Qwen2 (72B)", "score": 85.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.9, "8K": 96.1, "16K": 94.9, "32K": 94.1, "64K": 79.8, "128K": 53.7}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 79.6, "wAvg_decreasing": 92.3}
- {"rank": "No cross-protocol rank", "model": "Command-R-plus (104B)", "score": 87.4, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.6, "8K": 95.2, "16K": 94.2, "32K": 92.0, "64K": 84.3, "128K": 63.1}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 82.7, "wAvg_decreasing": 92.1}
- {"rank": "No cross-protocol rank", "model": "Command-R-0824 (32B)", "score": 88.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 94.7, "8K": 93.7, "16K": 93.1, "32K": 90.8, "64K": 86.6, "128K": 74.7}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": 86.0, "wAvg_decreasing": 91.9}
- {"rank": "No cross-protocol rank", "model": "GLM4 (9B)", "score": 89.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 94.7, "8K": 92.8, "16K": 92.1, "32K": 89.9, "64K": 86.7, "128K": 83.1}, "claimed_length": "1M", "effective_length": "64K", "wAvg_increasing": 88.0, "wAvg_decreasing": 91.7}
- {"rank": "No cross-protocol rank", "model": "Llama3.1 (8B)", "score": 88.3, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.5, "8K": 93.8, "16K": 91.6, "32K": 87.4, "64K": 84.7, "128K": 77.0}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 85.4, "wAvg_decreasing": 91.3}
- {"rank": "No cross-protocol rank", "model": "ProLong (8B)", "score": 88.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 94.5, "8K": 92.5, "16K": 92.3, "32K": 89.3, "64K": 83.2, "128K": 81.6}, "claimed_length": "512K", "effective_length": "32K", "wAvg_increasing": 86.6, "wAvg_decreasing": 91.2}
- {"rank": "No cross-protocol rank", "model": "Command-R (35B)", "score": 88.3, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 93.8, "8K": 93.3, "16K": 92.4, "32K": 89.5, "64K": 84.9, "128K": 76.0}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 85.5, "wAvg_decreasing": 91.1}
- {"rank": "No cross-protocol rank", "model": "MegaBeam-Mistral (7B)", "score": 89.1, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 93.8, "8K": 92.5, "16K": 92.0, "32K": 89.2, "64K": 83.7, "128K": 83.7}, "claimed_length": "512K", "effective_length": "32K", "wAvg_increasing": 87.3, "wAvg_decreasing": 91.0}
- {"rank": "No cross-protocol rank", "model": "Mistral-Large-2407 (123B)", "score": 80.5, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 96.2, "8K": 96.1, "16K": 95.1, "32K": 93.0, "64K": 78.8, "128K": 23.7}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 70.6, "wAvg_decreasing": 90.4}
- {"rank": "No cross-protocol rank", "model": "GradientAI/Llama3 (70B)", "score": 86.5, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.1, "8K": 94.4, "16K": 90.8, "32K": 85.4, "64K": 80.9, "128K": 72.1}, "claimed_length": "1M", "effective_length": "16K", "wAvg_increasing": 82.6, "wAvg_decreasing": 90.3}
- {"rank": "No cross-protocol rank", "model": "Mixtral-8x22B (39B/141B)", "score": 81.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.6, "8K": 94.9, "16K": 93.4, "32K": 90.9, "64K": 84.7, "128K": 31.7}, "claimed_length": "64K", "effective_length": "32K", "wAvg_increasing": 73.5, "wAvg_decreasing": 90.3}
- {"rank": "No cross-protocol rank", "model": "Yi (34B)", "score": 87.5, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 93.3, "8K": 92.2, "16K": 91.3, "32K": 87.5, "64K": 83.2, "128K": 77.3}, "claimed_length": "200K", "effective_length": "32K", "wAvg_increasing": 84.8, "wAvg_decreasing": 90.1}
- {"rank": "No cross-protocol rank", "model": "Qwen3-4B* (4B)", "score": 85.2, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.1, "8K": 93.6, "16K": 91.0, "32K": 87.8, "64K": 77.8, "128K": 66.0}, "claimed_length": "128K", "effective_length": "64K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "EXAONE-4.0-1.2B* (1.2B)", "score": 84.2, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 87.0, "8K": 86.7, "16K": 88.8, "32K": 81.1, "64K": 77.4, "128K": null}, "claimed_length": "64K", "effective_length": "32K", "wAvg_increasing": null, "wAvg_decreasing": null}
- {"rank": "No cross-protocol rank", "model": "Phi3-mini (3.8B)", "score": 84.8, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 92.2, "8K": 91.5, "16K": 90.7, "32K": 87.5, "64K": 80.6, "128K": 66.7}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 80.9, "wAvg_decreasing": 88.7}
- {"rank": "No cross-protocol rank", "model": "Phi3-medium (14B)", "score": 81.5, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 93.3, "8K": 93.2, "16K": 91.1, "32K": 86.8, "64K": 78.6, "128K": 46.1}, "claimed_length": "128K", "effective_length": "32K", "wAvg_increasing": 74.8, "wAvg_decreasing": 88.3}
- {"rank": "No cross-protocol rank", "model": "Mixtral-8x7B (12.9B/46.7B)", "score": 80.4, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 94.9, "8K": 92.1, "16K": 92.5, "32K": 85.9, "64K": 72.4, "128K": 44.5}, "claimed_length": "32K", "effective_length": "32K", "wAvg_increasing": 72.8, "wAvg_decreasing": 87.9}
- {"rank": "No cross-protocol rank", "model": "GradientAI/Llama3 (8B)", "score": 82.4, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 92.8, "8K": 90.3, "16K": 85.7, "32K": 79.9, "64K": 76.3, "128K": 69.5}, "claimed_length": "1M", "effective_length": "16K", "wAvg_increasing": 78.5, "wAvg_decreasing": 86.3}
- {"rank": "No cross-protocol rank", "model": "FILM-7B* (7B)", "score": 75.5, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; self-reported by external authors", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 92.8, "8K": 88.2, "16K": 88.1, "32K": 86.9, "64K": 70.1, "128K": 27.1}, "claimed_length": "32K", "effective_length": "32K", "wAvg_increasing": 66.4, "wAvg_decreasing": 84.7}
- {"rank": "No cross-protocol rank", "model": "InternLM2.5 (7B)", "score": 80.9, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 88.1, "8K": 85.5, "16K": 84.5, "32K": 82.7, "64K": 75.5, "128K": 68.9}, "claimed_length": "1M", "effective_length": "4K", "wAvg_increasing": 77.8, "wAvg_decreasing": 83.9}
- {"rank": "No cross-protocol rank", "model": "Mistral (7B)", "score": 68.4, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 93.6, "8K": 91.2, "16K": 87.2, "32K": 75.4, "64K": 49.0, "128K": 13.8}, "claimed_length": "32K", "effective_length": "16K", "wAvg_increasing": 55.6, "wAvg_decreasing": 81.2}
- {"rank": "No cross-protocol rank", "model": "Mistral-Nemo", "score": 66.2, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 87.8, "8K": 87.2, "16K": 87.7, "32K": 69.0, "64K": 46.8, "128K": 19.0}, "claimed_length": "128K", "effective_length": "16K", "wAvg_increasing": 54.7, "wAvg_decreasing": 77.8}
- {"rank": "No cross-protocol rank", "model": "GLM3 (6B)", "score": 69.6, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 87.8, "8K": 83.4, "16K": 78.6, "32K": 69.9, "64K": 56.0, "128K": 42.0}, "claimed_length": "128K", "effective_length": "4K", "wAvg_increasing": 62.0, "wAvg_decreasing": 77.2}
- {"rank": "No cross-protocol rank", "model": "LWM (7B)", "score": 72.8, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 82.3, "8K": 78.4, "16K": 73.7, "32K": 69.1, "64K": 68.1, "128K": 65.0}, "claimed_length": "1M", "effective_length": "<4K", "wAvg_increasing": 69.9, "wAvg_decreasing": 75.7}
- {"rank": "No cross-protocol rank", "model": "DBRX (36B/132B)", "score": 56.3, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 95.1, "8K": 93.8, "16K": 83.6, "32K": 63.1, "64K": 2.4, "128K": 0.0}, "claimed_length": "32K", "effective_length": "8K", "wAvg_increasing": 38.0, "wAvg_decreasing": 74.7}
- {"rank": "No cross-protocol rank", "model": "Qwen1.5 (72B)", "score": 55.7, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 94.9, "8K": 93.8, "16K": 78.0, "32K": 67.8, "64K": 0.0, "128K": 0.0}, "claimed_length": "32K", "effective_length": "8K", "wAvg_increasing": 37.5, "wAvg_decreasing": 74.0}
- {"rank": "No cross-protocol rank", "model": "Together (7B)", "score": 50.3, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 88.2, "8K": 81.1, "16K": 69.4, "32K": 63.0, "64K": 0.0, "128K": 0.0}, "claimed_length": "32K", "effective_length": "4K", "wAvg_increasing": 33.8, "wAvg_decreasing": 66.7}
- {"rank": "No cross-protocol rank", "model": "LongChat (7B)", "score": 49.1, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 84.7, "8K": 79.9, "16K": 70.8, "32K": 59.3, "64K": 0.0, "128K": 0.0}, "claimed_length": "32K", "effective_length": "<4K", "wAvg_increasing": 33.1, "wAvg_decreasing": 65.2}
- {"rank": "No cross-protocol rank", "model": "LongAlpaca (13B)", "score": 36.3, "metric": "README Avg (%), kept as in the original table and not recalculated", "track": "RULERv1 historical table; experiments listed by the project", "source_url": "https://github.com/hsiehjackson/RULER", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "by_length": {"4K": 60.6, "8K": 57.0, "16K": 56.6, "32K": 43.6, "64K": 0.0, "128K": 0.0}, "claimed_length": " 32K", "effective_length": "<4K", "wAvg_increasing": 24.7, "wAvg_decreasing": 47.9}

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08)

### 榜单覆盖边界

Every one of the 44 model records in the README that has an Avg is transcribed in full. The six lengths, both kinds of weighted metric, and the asterisks that mark an outside self-report are kept. The 4K baseline Llama2-7B=85.6 has no Avg over the six lengths, and it was not placed on the same leaderboard of averages. The order of the rows is not one ranking. An update time that the source does not give is not filled in.

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08)

## Contact

### 公开研究联系

- chsieh@nvidia.com
- simengs@nvidia.com

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 公开反馈渠道

https://github.com/hsiehjackson/RULER/issues

Sources: [1](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07)

### 官方社交账号

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08)

### 联系方式原则

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07)

## Original files

### 论文原件

### 原始PDF地址

https://arxiv.org/pdf/2404.06654

Sources: [1](https://arxiv.org/pdf/2404.06654) (accessed 2026-11-08)

### 原始文件SHA-256

8a4bc6ca28d84570eec7f42652400c2121f4c8bc361701634e596772e396fc22

Note: Byte count of the original PDF actually downloaded. The existing file is not changed on that basis.

Sources: [1](https://arxiv.org/pdf/2404.06654) (accessed 2026-11-08)

### 原始文件字节数

682955

Sources: [1](https://arxiv.org/pdf/2404.06654) (accessed 2026-11-08)

### Other documents

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2404.06654) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2404.06654) (accessed 2026-11-08); [3](https://github.com/hsiehjackson/RULER) (accessed 2026-11-07); [4](https://github.com/hsiehjackson/RULER) (accessed 2026-11-08)
