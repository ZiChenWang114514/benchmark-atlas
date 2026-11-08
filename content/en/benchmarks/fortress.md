# Fortress

> Benchmark Constitution, research snapshot 2026-11-07. The collection time is not the time a score was actually run, or the leaderboard update time.

FORTRESS measures robustness of safeguards in dual-use settings of national security and public safety, and at the same time uses benign requests on similar topics to quantify over-refusal. It does not directly measure a “rate of mastery of dangerous knowledge.” The current ARS leaderboard and the scores on the public set in the paper differ. A low risk score still needs to be read together with ORS.

Latest review

## Basic information

### Short name

Fortress

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Full name

Frontier Risk Evaluation for National Security and Public Safety

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Benchmark version

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Paper version

arXiv v2 (a revision of the paper, not a dataset version)

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### Release date

2025-06-18 (time of the first arXiv draft; not the independent release date of the dataset).

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### Section

Safety

Note: Benchmark Constitution editorial filing. It is not an official classification.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Field tags

- 公共安全
- 前沿风险

Note: Editorial tag

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 许可与范围

The license tag on the official HF card is CC BY 4.0. The body of the card also requires that use be limited to safety evaluation and prohibits adversarial training/research. The two statements in the original text are recorded side by side. The tension in the scope of the license is not resolved here.

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2506.14922

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 代码

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Dataset

https://huggingface.co/datasets/ScaleAI/fortress_public

Note: Public HF card revision that was read: 0c096becbc75bb12065c8059a53960c7f0d4d35c; only the state of the public card and of the repository is fixed, and it is not extrapolated to a version of the private test.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）

### Official homepage

https://labs.scale.com/leaderboard/fortress

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Paper title

FORTRESS: Frontier Risk Evaluation for National Security and Public Safety

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

## Origin and maintenance

### 发起/作者单位

Scale AI

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 合作与支持

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Authors

- Christina Q. Knight
- Kaustubh Deshpande
- Ved Sirdeshmukh
- Meher Mankikar
- Scale Red Team
- SEAL Research Team
- Julian Michael

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### Maintainer

Scale Labs

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Funders

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

## Design goals

### Abilities measured

In dual-use scenarios of national security and public safety, the harmful-assistance risk and the benign over-refusal of model safeguards.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Design background

It does not only test dual-use knowledge capability; paired benign prompts are also used to measure the safety-utility tradeoff.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

## Construction

### Question sources

Experts construct adversarial prompts covering CBRNE, political violence/terrorism, and crime/financial illegal activity.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 出题者背景

Experienced human red-team personnel; the appendix of the paper lists multidisciplinary backgrounds, but the Limitations section acknowledges that they may not possess the deep domain knowledge of real malicious actors, and therefore they are not all described as CBRNE domain experts.

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### Review process

Each adversarial prompt is paired with 4–7 binary scoring rubrics and with topically similar benign prompts.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Quality control

Three judges vote by majority on each item; this is not a single coarse-grained keyword check.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 污染控制

The leaderboard includes public and private prompts; the private prompts are used to reduce contamination.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

## Data format

### 题量

The introduction of the current official leaderboard says over 1,010 adversarial prompts, of which 500 are public; the public HF train split has 500 rows, and each row contains an adversarial_prompt, 4–7 rubric items, and a benign_prompt together, so 500 rows are not 1000 independent questions.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）

### 任务形式

Single-turn adversarial requests and paired benign requests.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Modalities

- 文本

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### Languages

The public paper and public prompt examples are in English; additional multilingual coverage is not inferred from that.

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）

### 难度与分层

Built from 3 risk domains, 10 subdomains, and expert adversarial prompts. It does not provide a single difficulty grade that can be compared directly with ordinary knowledge questions; ARS reflects the protective response, not an examination score for domain knowledge.

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### Public and hidden splits

500 public adversarial and benign pairs (the HF split is named train only as a storage name); the current leaderboard also uses private prompts. Results on the public set of 500 in the 2025 paper differ from the current leaderboard, which mixes public and private items.

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）；[一手资料2](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料3](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

## Evaluation

### Metrics

Average Risk Score (ARS) and Over-Refusal Score (ORS); lower is better for both.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 评分

ARS: each rubric is decided by a majority vote of o3, Claude 3.7 Sonnet, and Gemini 2.5 Pro; ORS is refusal detection by GPT-4o-mini.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 提示与运行协议

In the experiments of the original paper, an ordinary model uses temperature=0.7 and a reasoning model uses 1.0. The maximum completion budget and the maximum thinking budget of each model are in Tables 8–9. This holds only for the protocol of the original paper. It is not applied, beyond that protocol, to models that were added later.

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### 评测脚本

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 可比性警示

The ARS in the current Performance Comparison differs from the historical Rankings table in the body text and from the public set of 500 in the original paper. Only the ARS of the current leaderboard is recorded. ORS from the old table is not attached to new models, and ± values that have not been defined are not treated as standard errors.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07 (materials snapshot date)

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 版本与采用证据

- **version**：待核实
- **heat_confidence**：B
- **why_trending**：This is mainly a current presentation by a single organization, or continued self-evaluation by a vendor, and it does not represent broad adoption across the industry.
- **evidence_2026_h2**：- - **url**：https://labs.scale.com/leaderboard/fortress
 - **date**：2026-11-07
 - **date_type**：observed_on
 - **organization**：官方维护方
 - **note**：The current official methods and leaderboard have been opened; the observation date is not presented as the publication date.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 材料沿革

- - **version**：v1
 - **submitted_at**：2025-06-18
- - **version**：v2
 - **submitted_at**：2025-06-25

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### Saturation

The current lowest ARS is 5.78 (lower is better), but these new models do not have a paired ORS, and ARS is the judge’s score on the risk rubric; a low ARS alone cannot be taken to mean that the safety—utility tradeoff is already saturated.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 污染与局限

Public prompts may contaminate training; the current leaderboard uses a private portion to reduce that risk. Limitations stated in the paper include single-turn static prompts, a red team that is not made up entirely of deep domain experts, and a limited number of samples in each subdomain; a low ARS is not the same as having measured real-world harm to be zero.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### 版本/衍生关系

The public data and the private leaderboard extension belong to the same FORTRESS series; benign pairs are used for ORS and are not a second independent benchmark.

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）；[一手资料2](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07 (snapshot date, not the date of the actual run)

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 官方榜

https://labs.scale.com/leaderboard/fortress

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 其他评测入口

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 分轨结果（结构化快照）

```json
[
 {
 "rank": 1
 "model": "claude-opus-5-5-max"
 "score": 5.78
 "metric": "Average Risk Score (ARS), lower is better."
 "displayed_uncertainty": 1.26
 "uncertainty_definition": "Unverified: the current display shows ±, and SE or CI is not inferred from it"
 "scope": "The current Performance Comparison, not the historical Rankings table in the body text"
 "source_url": "https://labs.scale.com/leaderboard/fortress"
 "accessed": "2026-11-07"
 "ORS": "Unverified: these current rows do not give a paired ORS"
 "result_type": "Snapshot of the current official page"
 }
 {
 "rank": 2
 "model": "muse-spark-open"
 "score": 7.64
 "metric": "Average Risk Score (ARS), lower is better."
 "displayed_uncertainty": 1.15
 "uncertainty_definition": "Unverified: the current display shows ±, and SE or CI is not inferred from it"
 "scope": "The current Performance Comparison, not the historical Rankings table in the body text"
 "source_url": "https://labs.scale.com/leaderboard/fortress"
 "accessed": "2026-11-07"
 "ORS": "Unverified: these current rows do not give a paired ORS"
 "result_type": "Snapshot of the current official page"
 }
 {
 "rank": 3
 "model": "gpt-oss-120b"
 "score": 8.24
 "metric": "Average Risk Score (ARS), lower is better."
 "displayed_uncertainty": 1.93
 "uncertainty_definition": "Unverified: the current display shows ±, and SE or CI is not inferred from it"
 "scope": "The current Performance Comparison, not the historical Rankings table in the body text"
 "source_url": "https://labs.scale.com/leaderboard/fortress"
 "accessed": "2026-11-07"
 "ORS": "Unverified: these current rows do not give a paired ORS"
 "result_type": "Snapshot of the current official page"
 }
 {
 "rank": 4
 "model": "Claude Haiku 5.5"
 "score": 9.48
 "metric": "Average Risk Score (ARS), lower is better."
 "displayed_uncertainty": 1.34
 "uncertainty_definition": "Unverified: the current display shows ±, and SE or CI is not inferred from it"
 "scope": "The current Performance Comparison, not the historical Rankings table in the body text"
 "source_url": "https://labs.scale.com/leaderboard/fortress"
 "accessed": "2026-11-07"
 "ORS": "Unverified: these current rows do not give a paired ORS"
 "result_type": "Snapshot of the current official page"
 }
 {
 "rank": 5
 "model": "claude-opus-4-5-20251101-thinking"
 "score": 9.63
 "metric": "Average Risk Score (ARS), lower is better."
 "displayed_uncertainty": 2.11
 "uncertainty_definition": "Unverified: the current display shows ±, and SE or CI is not inferred from it"
 "scope": "The current Performance Comparison, not the historical Rankings table in the body text"
 "source_url": "https://labs.scale.com/leaderboard/fortress"
 "accessed": "2026-11-07"
 "ORS": "Unverified: these current rows do not give a paired ORS"
 "result_type": "Snapshot of the current official page"
 }
]
```

[榜单原始资料](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 覆盖范围

The top five ARS values in the current Performance Comparison have been read: 5.78, 7.64, 8.24, 9.48, and 9.63. Both ARS and ORS are better when lower, but the ORS of the current new models and the definition of ± remain Unverified. The original paper and the historical tables in the body are not mixed into the current paired data, and the date of observation is not treated as the run date.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

## Contact

### 公开研究邮箱

- christina.knight@scale.com

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）

### 问题反馈

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 机构公开渠道

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 隐私政策

https://scale.com/legal/privacy

[一手资料1](https://scale.com/research/fortress)（访问 2026-11-07）

## Original files

### Paper PDF

https://arxiv.org/pdf/2506.14922

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 源站PDF SHA-256

0ad431682c60664c7af8efc9620eff9d384dfa55a0324f304d1a738a8a94edfd

Note: Digest of the PDF bytes downloaded from the source site. This does not claim that a copy was updated.

[一手资料1](https://arxiv.org/pdf/2506.14922)（访问 2026-11-07）

### 源站PDF字节数

4776777

[一手资料1](https://arxiv.org/pdf/2506.14922)（访问 2026-11-07）

### 资料目录

Unverified

状态：待核实。

Note: The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 其他官方资料

- - **type**：Verified official primary sources
 - **url**：https://huggingface.co/datasets/ScaleAI/fortress_public
 - **accessed**：2026-11-07

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）

### PDF归档

Unverified

仅核对源站PDF和已有归档引用，未上传或覆盖文件。

## Changelog

- - **date**：2026-11-07
 - **change**：首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。
- - **date**：2026-11-07
 - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位Official README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
