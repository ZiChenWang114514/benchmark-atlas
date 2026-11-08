# FRAMES

> Benchmark Constitution, research snapshot 2026-11-07. The collection time is not the time a score was actually run, or the leaderboard update time.

FRAMES places retrieval, factuality, and reasoning from more than one source in the same end-to-end task. The final 824 questions were built by people, rather than being the result originally synthesized by an LLM. The oracle supplies the relevant articles, so 72.9% and the 66.0% from real multi-step retrieval cannot be treated as one ranking of different models.

Latest review

## Basic information

### Short name

FRAMES

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Full name

Factuality, Retrieval, And reasoning MEasurement Set

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Benchmark version

Official public HF snapshot, revision 58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef; the data card has no separate semantic-version label

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/blob/58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef/README.md)（访问 2026-11-07）

### Paper version

arXiv v3 (a revision of the paper, not a dataset version)

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Release date

2024-09-20 (time of the first arXiv draft; not the independent release date of the dataset).

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Section

Language

Note: Benchmark Constitution editorial filing. This is not the only field named by the paper.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Field tags

- Retrieval-augmented multi-hop factual question answering

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 许可与范围

Apache-2.0 (official dataset card); the dataset card also has anomalous automatic metadata, and the scale follows the body text and the 824 questions in the paper.

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2409.12941

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 代码

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Dataset

https://huggingface.co/datasets/google/frames-benchmark

Note: Public HF card revision that was read: 58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef; only the state of the public card and of the repository is fixed, and it is not extrapolated to a version of the private test.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Official homepage

https://huggingface.co/datasets/google/frames-benchmark

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Paper title

Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Origin and maintenance

### 发起/作者单位

Paper author affiliations are Harvard University, Google DeepMind, and Meta; an author’s current affiliation is not automatically treated as the legal sponsor or as a formal collaboration agreement.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 合作与支持

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Authors

- Krishna, Satyapriya
- Krishna, Kalpesh
- Mohananey, Anhad
- Schwarcz, Steven
- Stambler, Adam
- Upadhyay, Shyam
- Faruqui, Manaal

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Maintainer

The release account google/frames-benchmark under the Google organization on HF; the academic contact is Satyapriya Krishna, the corresponding author of the paper, and it is not inferred that any particular employee still maintains the release.

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Funders

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Design goals

### Abilities measured

A uniform evaluation of factuality, retrieval, and multi-hop reasoning in RAG systems.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Design background

Existing data often separate retrieval, factuality, and reasoning, and cannot adequately measure end-to-end integration across multiple sources.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Construction

### Question sources

LLM synthesis was tried first, but >30% contained hallucinations and it was hard to require more than 4 articles in a stable way; the final 824 questions were written by humans, using multiple Wikipedia pages, gold answers, and source links, and the bank cannot be called a purely synthetic question bank.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 出题者背景

Human annotation experts who were screened and who have experience writing questions and complex reasoning tasks; this is the paper's description of the team's qualifications and is not extended to each annotator's degree or field.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Review process

Human re-annotation checks whether the answer agrees with the listed Wikipedia page; a cutoff-in-time context is added to remove ambiguity about what was current; yes/no questions are removed to reduce guessing; each question is labeled with reasoning types, which may overlap.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Quality control

Questions and answers were checked again against their sources, explicit dates were added so that answers would not change with time, binary answers were removed in order to enlarge the output space, and five types of reasoning were labeled in order to support explanation. The number of Wikipedia pages does not directly equal the number of strict reasoning hops.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 污染控制

Questions that require reasoning across sources and additional computation reduce the benefit of direct factual memorization; the paper’s Limitations still explicitly acknowledge that Wikipedia may enter pretraining, and the absence of contamination is not proved.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Data format

### 题量

824 multi-hop questions, each requiring 2–15 Wikipedia articles; the body text is the authoritative definition of the question count, and the card's anomalous automatic metadata of n>1T is not used.

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/raw/main/README.md)（访问 2026-11-07）

### 任务形式

Multi-hop open question answering; a gold answer and related articles are attached, and reasoning types such as numerical, table, multiple constraints, temporal, and post-processing are labeled.

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/raw/main/README.md)（访问 2026-11-07）

### Modalities

Text

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Languages

English (dataset card language: en)

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/raw/main/README.md)（访问 2026-11-07）

### 难度与分层

Reasoning types such as numeric, table, multi-constraint, temporal, and post-processing; the number of articles differs.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Public and hidden splits

The official release makes the questions, answers, and related Wikipedia articles public; no additional hidden set was verified this time.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Evaluation

### Metrics

Final-answer accuracy; the retrieval configuration must be labeled separately.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 评分

For judging the final answer, the paper compares no retrieval, BM25, oracle, and multi-turn retrieval reasoning; an oracle score cannot be treated as an end-to-end retrieval score.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 提示与运行协议

The original paper includes different pipelines, among them naive, BM25 top4, oracle, and multi-step retrieval reasoning; the model snapshot and the retrieval protocol must be kept consistent.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 评测脚本

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 可比性警示

A model's score depends on the index, the version of the web page, the retriever, the number of retrieval rounds, and the context; the oracle already supplies the evidence and is not equivalent to a real search.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07 (materials snapshot date)

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）

### 版本与采用证据

- **public_dataset_revision**：58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef
- **size**：824
- **source**：The x-repo-commit from the resolve response of the official HF main branch; not treated as the paper version

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark/blob/58d9fb6330f3ab1316d1eca12e5e8ef23dcc22ef/README.md)（访问 2026-11-07）

### 材料沿革

- - **version**：v1
 - **submitted_at**：2024-09-20
- - **version**：v2
 - **submitted_at**：2024-10-19
- - **version**：v3
 - **submitted_at**：2025-01-25

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### Saturation

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 污染与局限

The paper explicitly acknowledges that contamination from pretraining data may raise scores; public gold answers and Wikipedia material cannot serve as a hidden uncontaminated test. The HF YAML also has anomalous pretty_name and size_categories. The scale follows the paper and the body text, 824 questions, rather than n>1T.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）

### 版本/衍生关系

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07 (snapshot date, not the date of the actual run)

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 官方榜

https://arxiv.org/abs/2409.12941

Note: When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 其他评测入口

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 分轨结果（结构化快照）

```json
[
 {
 "rank": null
 "model": "Gemini-Pro-1.5-0514"
 "score": 40.8
 "unit": "%"
 "metric": "answer accuracy"
 "settings": "naive prompting"
 "scope": "Historical baseline from the 2024 original paper on the official data card; differing settings are not used to rank models."
 "source_url": "https://huggingface.co/datasets/google/frames-benchmark"
 "accessed": "2026-11-07"
 "evaluation_date": "Unverified: the card does not list an exact experiment date"
 }
 {
 "rank": null
 "model": "Gemini-Pro-1.5-0514"
 "score": 47.4
 "unit": "%"
 "metric": "answer accuracy"
 "settings": "BM25, top4 docs"
 "scope": "Historical baseline from the 2024 original paper on the official data card; differing settings are not used to rank models."
 "source_url": "https://huggingface.co/datasets/google/frames-benchmark"
 "accessed": "2026-11-07"
 "evaluation_date": "Unverified: the card does not list an exact experiment date"
 }
 {
 "rank": null
 "model": "Gemini-Pro-1.5-0514"
 "score": 72.9
 "unit": "%"
 "metric": "answer accuracy"
 "settings": "oracle retrieval"
 "scope": "Historical baseline from the 2024 original paper on the official data card; differing settings are not used to rank models."
 "source_url": "https://huggingface.co/datasets/google/frames-benchmark"
 "accessed": "2026-11-07"
 "evaluation_date": "Unverified: the card does not list an exact experiment date"
 }
 {
 "rank": null
 "model": "Gemini-Pro-1.5-0514"
 "score": 66.0
 "unit": "%"
 "metric": "answer accuracy"
 "settings": "multi-step retrieval & reasoning"
 "scope": "Historical baseline from the 2024 original paper on the official data card; differing settings are not used to rank models."
 "source_url": "https://huggingface.co/datasets/google/frames-benchmark"
 "accessed": "2026-11-07"
 "evaluation_date": "Unverified: the card does not list an exact experiment date"
 }
]
```

[榜单原始资料](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）；[榜单原始资料](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 覆盖范围

The official HF card was read again, and all four historical baselines are listed. The figure 72.9 is the oracle result when the relevant articles are given, and 66.0 is the result of retrieval and reasoning over several real steps. Different pipelines are not placed on one ranking. That official card was not found to maintain an independent live leaderboard. The self-reported 81.1% from Hunyuan is not the basis for claiming a new official record.

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

## Contact

### 公开研究邮箱

- skrishna@g.harvard.edu

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 问题反馈

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 机构公开渠道

Unverified

状态：待核实。

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[一手资料1](https://arxiv.org/abs/2409.12941)（访问 2026-11-07）

### 隐私政策

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[一手资料1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### Paper PDF

https://arxiv.org/pdf/2409.12941

[一手资料1](https://arxiv.org/pdf/2409.12941)（访问 2026-11-07）

### 源站PDF SHA-256

4f4f33ebd7be7ccb97af2be83fa123940fc38bc8256ecbdf2afde749481a091c

Note: Digest of the PDF bytes downloaded from the source site. This does not claim that a copy was updated.

[一手资料1](https://arxiv.org/pdf/2409.12941)（访问 2026-11-07）

### 源站PDF字节数

1163381

[一手资料1](https://arxiv.org/pdf/2409.12941)（访问 2026-11-07）

### 其他官方资料

- - **type**：Verified official primary sources
 - **url**：https://huggingface.co/datasets/google/frames-benchmark
 - **accessed**：2026-11-07

[一手资料1](https://huggingface.co/datasets/google/frames-benchmark)（访问 2026-11-07）

### PDF归档

仅核对源站PDF和已有归档引用，未上传或覆盖文件。

## Changelog

- - **date**：2026-11-07
 - **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07
 - **change**：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
 - **fields_updated**：- data_format.size
 - data_format.languages
 - data_format.question_types
- - **date**：2026-11-07
 - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位Official README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
