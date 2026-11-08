# SysBench

> Chinese compilation and review of this page: 2026-11-08. Historical results, different data versions, scaffolds, and scoring protocols are recorded separately; Unverified is not the same as Not disclosed.

SysBench splits “following the system message” into three levels: satisfaction of constraints, satisfaction of a single user instruction, and stability across a session of five turns. The data come from cleaning and hand rewriting of real system messages, rather than from 500 unrelated single-turn questions and answers. The highest CSR in the table does not equal the highest SSR.

Source: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08); [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08)

## Basic information

### Short name

SysBench

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Full name

SysBench

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Benchmark version

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Paper version

arXiv v2; submitted at 2024-10-23 00:07:35.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Release date

2024-08-21 00:33:16 (arXiv v1 submission; the paper date is marked August 20, with no timezone)

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Section

Language

Note: Benchmark Constitution editorial filing. This is not the only field named by the paper.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Field tags

- System-instruction following

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### 许可与适用范围

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2408.10943

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Code repository

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### 数据地址

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Official homepage

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Paper title

SysBench: Can Large Language Models Follow System Messages?

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

## Origin and maintenance

### 机构与发起关系

The authors of the paper come from Peking University, Baichuan Intelligence, and other institutions; a record of author affiliations is not the same as the sole initiating organization.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Partner organizations

The author affiliations are Peking University and Baichuan Intelligence; an affiliation listed in the paper is not the same as a further undeclared funding source or a legal collaboration agreement.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### Authors

- Qin, Yanzhao
- Zhang, Tao
- Zhang, Tao
- Shen, Yanjun
- Luo, Wenjing
- Sun, Haoze
- Zhang, Yan
- Qiao, Yujing
- Chen, Weipeng
- Zhou, Zenan
- Zhang, Wentao
- Cui, Bin

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Current maintainer

The official public code is hosted at PKU-Baichuan-MLSystemLab; what is recorded here is the maintenance entry of the repository. Institutional legal liability, or a commitment of continued maintenance, is not inferred from it.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-07)

### 资助与支持

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

## Design goals

### Abilities measured

Evaluates whether the model follows constraints in the system message, and whether that holds across multiple turns.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Design background

Common instruction evaluations mainly target the user message and cannot adequately measure the priority of system instructions, dependence across turns, and stability.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Several thousand system messages were collected from real online logs and were denoised and deduplicated by heuristic rules and by clustering; 21 annotators who had been trained selected 500 of them and rewrote them by hand. The user dialogues come from collection and from generation assisted by GPT-4o; each dialogue keeps 5 turns and is rewritten according to the expert guidelines.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### 出题背景

21 trained data annotators; experts set the annotation guidelines and carry out independent checks over multiple rounds.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### Review process

Each user instruction is annotated with a checklist of the relevant constraints; several experts independently carry out more than one round of checking; GPT-4o judges, from the complete system message, the dialogue history, and the checklist, whether each constraint is satisfied.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### Quality control

The paper reports agreement above 94% between the verifier and human evaluation; it uses the three-level metrics CSR, ISR, and SSR to distinguish local satisfaction from overall stability across five rounds.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### 去污染与泄漏

During construction, heuristic rules and clustering remove duplicates and noise; this is deduplication inside the collection, and an independent audit of contamination in pretraining corpora remains Unverified.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

## Data format

### Size

500 conversations that contain a system message, each with 5 turns; not 500 independent single-turn questions.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-07)

### Question types

Multi-turn text dialogue with a system instruction

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Modalities

Text

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Languages

The public data contain Chinese system messages and Chinese multi-turn dialogues, and they include cross-lingual requirements such as translation. The paper appendix states that the displayed examples are translated from Chinese into English. The data cannot be treated as a complete Chinese-English parallel edition merely because the paper's model groups are labeled English/Chinese.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench/blob/main/datas/system_benchmark_eval_datas.json) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### Difficulty

3 problems: constraint violation, misjudgment of instructions, and multi-turn instability, including dependent or parallel dialogue settings.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### 数据划分

The public file is datas/system_benchmark_eval_datas.json. It contains system_prompt, messages, and, for each turn, prompt_infos, with alignment and criteria.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-07)

## Evaluation

### Metrics

Constraint Satisfaction Rate (CSR)、Instruction Satisfaction Rate (ISR)、Session Stability Rate (SSR)。

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### Scoring

GPT-4o judges each item against a human checklist: CSR is the proportion of constraints satisfied, ISR requires every relevant constraint in the same response to be satisfied, and SSR measures stability across turns. The metric command in the official README is written as eval_output, but that file is absent from the current root directory, and consistency between the reproduction entry point and the documentation still needs attention.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### 提示与运行设置

System messages and user turns must keep their original roles and their order, and the evaluated model's support for system-role, together with its template, is recorded.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### 评测脚本

https://github.com/PKU-Baichuan-MLSystemLab/SysBench

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-07)

### 可比性提醒

CSR, ISR, and SSR differ in granularity; a SysBench score in a vendor report that does not name the metric cannot be defaulted to any one of the three.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-08)

### 数据版本与更新

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-07)

### 论文修订记录

- {"version": "v1", "submitted_at": "2024-08-21 00:33:16 "}
- {"version": "v2", "submitted_at": "2024-10-23 00:07:35 "}

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-08)

### 饱和证据与局限

The highest SSR in original paper v2 is 54.4% (GPT4o), and the highest CSR is 87.1%; the metrics differ, so a single vendor-self-reported SysBench value cannot be used to infer that five rounds are saturated.

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### 争议与已知问题

Log sources, assistance from GPT-4o generation, and the GPT-4o verifier may introduce dependence on the distribution and on the judge. CSR, ISR, and SSR must be kept separate. The eval_output command mentioned in the README is inconsistent with the files in the current repository root.

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### 衍生或后继基准

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-07)

## Leaderboard snapshot

### 快照访问日期

2026-11-08

Source: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08); [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08)

### 官方榜单入口

https://arxiv.org/abs/2408.10943

Note: When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-07)

### 第三方入口

https://arxiv.org/html/2609.27284v1

Sources: [1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08)

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Original paper v2 Table 2 / CSR | 1 | GPT4o | 87.1 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 2 | GPT4o | 76.4 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 1 | GPT4o | 54.4 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 2 | GPT4-Turbo-20240409 | 86.5 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 1 | GPT4-Turbo-20240409 | 76.6 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 2 | GPT4-Turbo-20240409 | 53.2 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 3 | Claude-3-Opus | 85.0 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 3 | Claude-3-Opus | 74.1 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 3 | Claude-3-Opus | 51.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 7 | Llama3.1-70B-Instruct | 76.6 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 8 | Llama3.1-70B-Instruct | 60.3 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 8 | Llama3.1-70B-Instruct | 36.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 10 | Llama3.1-8B-Instruct | 66.5 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 10 | Llama3.1-8B-Instruct | 46.9 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 11 | Llama3.1-8B-Instruct | 24.9 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 12 | Mixtral-8x22B-Instruct | 63.6 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 11 | Mixtral-8x22B-Instruct | 44.4 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 12 | Mixtral-8x22B-Instruct | 22.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 13 | GPT3.5-Turbo-20231106 | 61.6 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 13 | GPT3.5-Turbo-20231106 | 43.2 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 13 | GPT3.5-Turbo-20231106 | 20.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 14 | Mixtral-8x7B-Instruct | 56.5 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 14 | Mixtral-8x7B-Instruct | 37.6 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 15 | Mixtral-8x7B-Instruct | 19.1 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 4 | Qwen2.5-72B-Instruct | 80.4 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 4 | Qwen2.5-72B-Instruct | 66.2 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 4 | Qwen2.5-72B-Instruct | 42.8 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 6 | GLM-4-0520 | 78.9 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 5 | GLM-4-0520 | 65.5 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 5 | GLM-4-0520 | 41.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 5 | Qwen2-72B-Instruct | 79.0 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 6 | Qwen2-72B-Instruct | 64.1 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 5 | Qwen2-72B-Instruct | 41.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 8 | DeepSeek-V2-0628 | 76.1 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 7 | DeepSeek-V2-0628 | 61.7 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 7 | DeepSeek-V2-0628 | 39.6 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 9 | Moonshot-V1-8K | 70.3 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 9 | Moonshot-V1-8K | 52.3 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 9 | Moonshot-V1-8K | 30.0 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 11 | GLM-4-9B-Chat | 64.2 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 12 | GLM-4-9B-Chat | 44.0 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 10 | GLM-4-9B-Chat | 25.9 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 15 | ERNIE-4-8K-0613 | 50.7 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 15 | ERNIE-4-8K-0613 | 33.8 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 14 | ERNIE-4-8K-0613 | 20.0 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / CSR | 16 | Qwen2-7B-Instruct | 47.0 | CSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / ISR | 16 | Qwen2-7B-Instruct | 26.9 | ISR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Original paper v2 Table 2 / SSR | 16 | Qwen2-7B-Instruct | 15.0 | SSR (%) | 500 sessions × 5 turns； | [2024-10-23 (v2 submission date, not the run date)](https://arxiv.org/pdf/2408.10943)；采集2026-11-08 |
| Vendor report Table 3 / slow-thinking | 1 | Hunyuan-Large-1116 | 82.5 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 3 / slow-thinking | 2 | Qwen2.5-72B-instruct | 77.7 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 3 / slow-thinking | 4 | Qwen3-A22B | 74.2 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 3 / slow-thinking | 3 | Hunyuan-A13B | 76.1 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；slow-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 4 / fast-thinking | 4 | Hunyuan-Large-1116 | 57.6 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 4 / fast-thinking | 2 | Qwen2.5-72B-instruct | 70.4 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 4 / fast-thinking | 1 | Qwen3-A22B | 72.1 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |
| Vendor report Table 4 / fast-thinking | 3 | Hunyuan-A13B | 70.2 | SysBench (the original label in the report; CSR/ISR/SSR are not specified). |；fast-thinking | [来源页未列运行日](https://arxiv.org/html/2609.27284v1)；采集2026-11-08 |

Source: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08); [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08)

### 榜单覆盖边界

All 16 models × CSR/ISR/SSR in Table 2 of original paper v2 are restored, 48 rows in total; the Hunyuan report separately lists 8 rows for slow thinking in Table 3 and fast thinking in Table 4. The self-report does not name the metric and is not ranked with CSR, ISR, or SSR. The official repository is centered on the paper reproduction tables and is not a continuously updated real-time overall leaderboard.

Source: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08); [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-08)

## Contact

### 官方公开邮箱

- qinyanzhao123@pku.edu.cn

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-07)

### 公开反馈渠道

https://github.com/PKU-Baichuan-MLSystemLab/SysBench/issues

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-07)

### 官方社交账号

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2408.10943) (accessed 2026-11-07)

### 联系方式/隐私原则

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07)

## Original files

### 原始PDF

https://arxiv.org/pdf/2408.10943

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### PDF SHA-256

192a6383d66f9075c26bff148774396da331daad4c69e1dafea9222fc20c10ed

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### PDF bytes

```json
788584
```

Sources: [1](https://arxiv.org/pdf/2408.10943) (accessed 2026-11-08)

### Other documents

### 论文原件

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench) (accessed 2026-11-08)
