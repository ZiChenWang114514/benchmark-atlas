# AdvBench

> Verification date: 2026-11-07. Unknowns are retained as Unverified; the access date is not the measurement date.

Latest review

Experimental data on harmful requests and on string attacks. This is not a live leaderboard that can compress model safety into a general rank. A historical ASR must carry, together, the target model, the attack method, the sample, and the budget.

## Basic information

### Short name

AdvBench

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Full name

AdvBench

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Benchmark version

The original AdvBench paper has two tasks, harmful strings and harmful behaviors; the repository does not define the data version with an independent semantic version number, and reproduction must pin a commit and a CSV.

> Do not write paper v2 as dataset v2.

[来源1](https://github.com/llm-attacks/llm-attacks)（访问 2026-11-07）

### Paper version

arXiv v2

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Release date

2023-07-28 01:49:12 (arXiv first draft; the source UTC date is July 27)

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Section

Safety

> Benchmark Constitution editorial filing. This is not the only field named by the paper.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Field tags

- Harmful requests and jailbreaks

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### License

MIT (software and documentation in the llm-attacks repository; the applicable scope of data and third-party materials must be checked per artifact).

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2307.15043

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Code

https://github.com/llm-attacks/llm-attacks

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 数据地址

https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Official entry

https://llm-attacks.org/

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Paper title

Universal and Transferable Adversarial Attacks on Aligned Language Models

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## Origin and maintenance

### Initiators

The authors are from CMU, the Center for AI Safety, Google DeepMind, the Bosch Center for AI, and other institutions; a formal relationship of who initiated the work is not inferred.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 合作方

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Authors

- Zou, Andy
- Wang, Zifan
- Carlini, Nicholas
- Nasr, Milad
- Kolter, J. Zico
- Fredrikson, Matt

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Maintainer

Official code and feedback are provided by the llm-attacks/llm-attacks repository; individual ongoing maintenance duties and response-time limits have not been verified.

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

### Funders

The acknowledgments of the paper list support that includes DARPA/AFRL FA8750-15-2-0277, Army MURI W911NF-21-1-0317, and NSF CNS1943016.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## Design goals

### Abilities measured

Evaluates the adversarial robustness of aligned language models on harmful behaviors and specified strings.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Design background

Jailbreak exploration by hand alone makes it hard to compare optimizable attacks and transfer across models systematically; unified behaviors and target strings are required.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## Construction

### Question sources

Author-written seed examples are combined with Wizard-Vicuna-30B-Uncensored for generation; the paper distinguishes harmful strings from harmful behaviors.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 出题者背景

The research team provided human seeds and filtered the generated results; not every entry was original work written item by item by safety experts.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Review process

Paper §2.3 builds harmful behaviors and harmful strings separately. Sources of behaviors include initial examples and expansion by an LLM; this is not a third-party certification of model safety. A record of item-by-item external expert review is Unverified.

> 字段状态：待核实

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Quality control

The original paper and the public CSV differ in scale; this entry retains both and pins the sources. Later research notes that looking only at non-refusals may overestimate attack effectiveness.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Decontamination

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## Data format

### 题量与规模

The original paper describes 500 harmful strings and 500 harmful behaviors. On the collection date, the official harmful_behaviors.csv was measured at 520 data rows, excluding the header. These are different versions or artifacts, and they cannot be silently unified as either 500 or 520.

> The CSV is counted with Python csv.DictReader, counting only data rows and excluding the header; the original file was not modified on this occasion.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）；[来源2](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv)（访问 2026-11-07）

### Question types

Requests for harmful behavior and target strings; this introduction does not reproduce specific attack suffixes or harmful steps.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Modalities

Text

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Languages

English

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Difficulty

The evaluation addresses adversarial-attack success and transfer; difficulty depends on the target model and the attack budget.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Public and hidden splits

The repository publishes behavior and string CSVs; an independent hidden-test split has not been verified.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## Evaluation

### Metrics

Attack success rate (ASR); harmful-string matching and behavioral compliance must be defined separately.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 评分

For harmful strings, ASR is computed by exact reproduction of the target string; harmful behaviors require a reasonable attempt, and a human judgment is required on whether the response refused or evaded. Individual numeric differences exist between the tables and the narrative in the paper; this page follows the values explicitly listed in Table1. A non-refusal is not the same as the quality of genuinely harmful assistance.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 运行设置

White-box Table 1 of the original paper: 20 tokens that can be optimized, 500 steps, and GCG with batch512 and top-k256. The single-sample experiment uses the first 100 items. The universal attack is trained on 25 behaviors and then tested on another 100 behaviors, and train and test are reported separately.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 官方脚本

https://github.com/llm-attacks/llm-attacks

[来源1](https://github.com/llm-attacks/llm-attacks)（访问 2026-11-07）

### 可比性警示

ASR evaluates the effect of an attack, and a higher value is more dangerous; the white-box results on the first 100 samples in Table1 of the paper differ from the transfer test of 388 behaviors in Table2, and a string trigger, or a failure to refuse, is not equivalent to human verification that harmful content was completed.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07

[来源1](https://llm-attacks.org/)（访问 2026-11-07）

### 最新版本与采用证据

The official repository path data/advbench releases harmful_behaviors.csv and harmful_strings.csv. Checked against public main and v2 of the original paper, an independent dataset version number is Unverified.

> 字段状态：待核实

[来源1](https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2023-07-28"
 }
 {
 "version": "v2"
 "submitted_at": "2023-12-21"
 }
]
```

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Saturation

This page does not, from an individual attack’s 99% ASR, assert that the benchmark is saturated or that models are generally unsafe; ASR is a conditional result of attack × target model × decision rule × budget.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Contamination and disputes

The conflict in scale is listed side by side: the original paper has 500 rows, and the current official CSV has 520 rows. StrongREJECT points out that a failure to refuse does not mean an effective harmful answer, so results from different ASR judges cannot be compared directly.

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv)（访问 2026-11-07）

### 版本与衍生关系

The official announcement of 2024-08-01 released nanoGCG as a more usable implementation of the GCG algorithm; this is an update to the attack implementation, and it is not a new version of the AdvBench data.

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07

[来源1](https://llm-attacks.org/)（访问 2026-11-07）

### Official leaderboard

https://arxiv.org/abs/2307.15043

> When there is no verified live leaderboard, an entry point to the results in the original paper or the data card is provided; it is not claimed to be a live leaderboard.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 第三方覆盖

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 分轨结果

#### Paper v2 Table1 / the first 100 rows are white-box

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| Not applicable (columns selected within the source, not a global ranking) | Vicuna-7B + GCG | 99.0 | individual Harmful Behavior ASR (%) | [原表](https://arxiv.org/abs/2307.15043)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | LLaMA-2-7B-Chat + GCG | 56.0 | individual Harmful Behavior ASR (%) | [原表](https://arxiv.org/abs/2307.15043)，2026-11-07 |

#### Paper v2 Table1 / general-suffix test

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| Not applicable (columns selected within the source, not a global ranking) | Vicuna-7B + GCG | 98.0 | multiple Harmful Behaviors test ASR (%) | [原表](https://arxiv.org/abs/2307.15043)，2026-11-07 |
| Not applicable (columns selected within the source, not a global ranking) | LLaMA-2-7B-Chat + GCG | 84.0 | multiple Harmful Behaviors test ASR (%) | [原表](https://arxiv.org/abs/2307.15043)，2026-11-07 |

> Original historical experiments, not a 2026 live safety leaderboard; a higher ASR means the attack is more successful, not that the tested model is safer.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### Coverage note

Table1 of the official paper transcribes four historical GCG experiments, kept on separate tracks by attack setting; the README does not link a unified live leaderboard, and the current ranking across models is Unverified; different attacks, judges, and budgets must not be mixed in one ranking.

> 字段状态：待核实

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）；[来源2](https://github.com/llm-attacks/llm-attacks)（访问 2026-11-07）

## Contact

### 公开科研联系邮箱

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 公开反馈

https://github.com/llm-attacks/llm-attacks/issues

> Public feedback entry point; no question was sent.

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问 2026-11-07）

### 官方社交

Unverified

> 字段状态：待核实

> The listed materials have been checked, but this batch has not yet completed exact verification of this field; this does not indicate Not disclosed by the official source.

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### 隐私说明/政策

Only research contact channels made public in the paper, on the official website, or in the official repository are included; private contact details are not collected.

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2307.15043

[来源1](https://arxiv.org/abs/2307.15043)（访问 2026-11-07）

### PDF SHA-256

ab8745c2e3c6dfd939d5a590760bbae4682d92db010947cbb306688ad086bfd1

> SHA-256 of the bytes actually downloaded. It does not mean an existing copy was replaced.

[来源1](https://arxiv.org/pdf/2307.15043)（访问 2026-11-07）

### PDF bytes

4656473

[来源1](https://arxiv.org/pdf/2307.15043)（访问 2026-11-07）

### 论文副本

## Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 }
]
```

[来源1](https://llm-attacks.org/)（访问 2026-11-07）
