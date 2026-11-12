# HarmBench

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

HarmBench unifies categories of harmful behavior, target-model responses, and success judgments, for red-team and robust-refusal research. ASR belongs to a complete setting made up of the attack method, the target model, the behavior scope, the judge, and the budget. There is no single safety score detached from that setting. This page does not reproduce specific harmful requests or attack strings.

Guide source: [https://arxiv.org/abs/2402.04249](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Basic information

### Short name

HarmBench

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Full name

HarmBench

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Dataset version

HarmBench 1.0 (README announcement of 2024-02-26); a new data version cannot be inferred from the paper revision number.

Sources: [1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md) (accessed 2026-11-07)

### Paper version

v2; 2024-02-27 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Release date

2024-02-07 (submission time of the first arXiv draft; not an inferred data first-release date).

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Section

Safety

Note: Benchmark Constitution editorial filing. This is not the only field named by the paper.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Subfields

- Jailbreaks, refusals, and automated red-teaming

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### License

MIT (official repository LICENSE, 2024 centerforaisafety; model weights and third-party materials require a separate check of terms).

Sources: [1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/LICENSE) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/2402.04249

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 代码入口

https://github.com/centerforaisafety/HarmBench

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Dataset

https://github.com/centerforaisafety/HarmBench

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Official homepage

https://github.com/centerforaisafety/HarmBench

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Paper title

HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Origin and maintenance

### 发起团队

Author affiliations involve UIUC, the Center for AI Safety, CMU, UC Berkeley, Microsoft, and others; it is not inferred from this that all of them are formal sponsors.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 合作及署名机构

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Authors

- Mazeika, Mantas
- Phan, Long
- Yin, Xuwang
- Zou, Andy
- Wang, Zifan
- Mu, Norman
- Sakhaee, Elham
- Li, Nathaniel
- Basart, Steven
- Li, Bo
- Forsyth, David
- Hendrycks, Dan

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Maintainer

Official code and feedback are provided by the centerforaisafety/HarmBench repository; individual ongoing maintenance duties and response-time limits have not been verified.

Sources: [1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md) (accessed 2026-11-07)

### Funders

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Design goals

### 评测能力

Standardized automated red-teaming and robust-refusal evaluation, comparing attack methods and defense models.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 设计动机

Earlier jailbreak evaluations are not uniform in behavior sets, target models, judges, and budgets, and readily produce success rates that cannot be reproduced or that are inflated.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Construction

### 材料来源

The research team manually compiled harmful behaviors from the safety policies of multiple providers, covering multiple functional scenarios.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 编制背景

Researchers perform safety-behavior classification and filtering.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Review process

Dual intent and ambiguous behavior are removed, and the focus is the differential harm that model output introduces relative to existing information.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Quality control

A dedicated classifier is developed and human verification is performed; copyright scenarios have a separate matching method.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 去污染边界

The paper requires that test behavior and the test classifier not be used to develop attacks or defenses, and it sets up a validation classifier separately; this controls leakage while the evaluation is being developed, and it does not prove that pretraining of the target LLM never saw the public data.

Sources: [1](https://arxiv.org/pdf/2402.04249) (accessed 2026-11-07)

## Data format

### Size

510 behaviors: 400 text and 110 multimodal; 100 validation and 410 test.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Question types

Descriptions of harmful behavior and evaluation of model responses; this article does not reproduce specific harmful requests or attack strings.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Modalities

Multimodal behavior conditioned on text and images

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Languages

Primarily English; the specific subset configuration needs to be recorded

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Difficulty

7 semantic classes; functionally, 200 standard, 100 copyright, 100 contextual, and 110 multimodal behaviors.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 公开及隐藏划分

100 validation items are used for development and 410 test items for reporting; one must not optimize a classifier on the test set and still claim an independent test.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Evaluation

### Metrics

Attack Success Rate (ASR), which depends on the attack method, the behavior subset, the target model, and the budget.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 计分

Text and contextual behavior use specialized classifiers such as a fine-tuned Llama-2-13B judge; copyright categories use the corresponding matching; success cannot be counted from non-refusal alone.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 提示与运行设置

The target models in the original paper are greedy, with at most 512 output tokens; the attack budget and the classifier settings must also be held fixed.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 评测入口

The official scripts/run_pipeline.py and the evaluation_pipeline documentation; the steps, in order, are generation of test cases, optional merging, answers from the target model, and classification of the answers.

Sources: [1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md) (accessed 2026-11-07)

### 可比性边界

There is no "model safety total score" detached from the attack method, the budget, the subset, and the judge; a higher ASR means that, under that setting, the model is easier to break.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 已核实版本

version：The README most recently marks HarmBench 1.0 explicitly, 2024-02-26；evidence_2026_h2：- url：https://arxiv.org/html/2609.10594v1；date：2026-09；note：It actually compares the HarmBench-specific classifier with other jailbreak judges, evaluated on two manually annotated sets.

Sources: [1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md) (accessed 2026-11-07); [2](https://arxiv.org/html/2609.10594v1) (accessed 2026-11-07)

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2024-02-07；- version：v2；submitted_at：2024-02-27；Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### Saturation

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 已知问题

A human-annotation comparison study in 2026-H2 specifically compares the reliability of judges, including HarmBench; automatic judgment is not an unbiased gold standard, and false positives, false negatives, and transfer across families of attacks need attention.

Sources: [1](https://arxiv.org/html/2609.10594v1) (accessed 2026-11-07)

### 衍生关系

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 官方结果入口

https://arxiv.org/abs/2402.04249

Note: When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 第三方结果入口

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Original paper v2 Table 7: test, standard/contextual/copyright, PAIR attack | — | Llama 2 7B Chat | 9.4 | ASR % (lower means more robust under that attack) | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07；原始实验日期未单列 |
| Original paper v2 Table 7: test, standard/contextual/copyright, PAIR attack | — | GPT-4 0613 | 39.4 | ASR % (lower means more robust under that attack) | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07；原始实验日期未单列 |
| Original paper v2 Table 7: test, standard/contextual/copyright, PAIR attack | — | GPT-4 Turbo 1106 | 33.8 | ASR % (lower means more robust under that attack) | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07；原始实验日期未单列 |
| Original paper v2 Table 7: test, standard/contextual/copyright, PAIR attack | — | Claude 2 | 4.1 | ASR % (lower means more robust under that attack) | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07；原始实验日期未单列 |
| Original paper v2 Table 7: test, standard/contextual/copyright, PAIR attack | — | Claude 2.1 | 2.2 | ASR % (lower means more robust under that attack) | [原始来源](https://arxiv.org/pdf/2402.04249)；采集2026-11-07；原始实验日期未单列 |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

A historical slice of the same PAIR attack and of the same range of test functional categories is transcribed exactly; no current overall safety ranking is given that mixes different attack budgets or modalities. rank=null, and the five models listed are not declared to be the top five of a complete leaderboard.

Sources: [1](https://arxiv.org/pdf/2402.04249) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/centerforaisafety/HarmBench/HEAD/README.md) (accessed 2026-11-07)

## Contact

### 公开研究联系邮箱

- mantas3@illinois.edu

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 问题反馈

https://github.com/centerforaisafety/HarmBench/issues

Note: Public feedback entry point; no question was sent.

Sources: [1](https://raw.githubusercontent.com/centerforaisafety/HarmBench/main/README.md) (accessed 2026-11-07)

### 官方账号

Unverified

Note: The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

Sources: [1](https://arxiv.org/abs/2402.04249) (accessed 2026-11-07)

### 隐私政策

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07)

## Original files

### 原文PDF

https://arxiv.org/pdf/2402.04249

Sources: [1](https://arxiv.org/pdf/2402.04249) (accessed 2026-11-07)

### PDF SHA-256

e6cbcbedbef6aebea3b6fc6c8fd7933546b26cf0a1e65bcf128eea235007c732

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/2402.04249) (accessed 2026-11-07)

### PDF bytes

3233876

Sources: [1](https://arxiv.org/pdf/2402.04249) (accessed 2026-11-07)

## Changelog

### 本页修订

- date：2026-11-07；change：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- date：2026-11-07；change：深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。
- date：2026-11-07；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07)
