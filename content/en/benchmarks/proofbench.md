# ProofBench

> In-depth verification: 2026-11-08. The access date is not the publication date or the experiment run date; unknowns are retained, and "Not disclosed" is not inferred.

ProofBench (paper name FormalProofBench) has the model submit a mathematical proof checked by Lean 4, rather than having a judge read a natural-language solution. The current v1.1 evaluates 100 private questions and has been separated from the original paper's protocol of 200 questions. Differences in the formal-check rules, the Lean and Mathlib versions, whether the network is available, whether auxiliary lemmas may be added, and the budget all change comparability. Permission for native_decide also does not mean that every proof depends only on the kernel.

Latest review

## Basic information

### Short name

ProofBench

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Full name

ProofBench (the name in the paper is FormalProofBench).

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Dataset version

v1.1

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Paper version

arXiv:2603.26996v1; an ICLR 2026 Workshop VerifAI-2 paper.

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 发布时间

First release of the paper: 2026-03-28 06:14:53 (source site 2026-03-27 21:14:53 UTC); this is not the update time of the current v1.1 leaderboard.

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 板块

Mathematics

> Benchmark Constitution editorial classification.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Subfields

```json
[
  "数学"
]
```

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### License

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Paper

https://arxiv.org/abs/2603.26996

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### 代码

https://github.com/vals-ai/proof-bench

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### Dataset

https://github.com/vals-ai/proof-bench/tree/main/problems

> The repository explicitly provides only sample problems and does not claim that the entire public split of 100 questions described on the web page has been downloaded. No HF release entry confirmed by official materials was found.

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### Official homepage

https://www.vals.ai/benchmarks/proof_bench

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文题名

FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Vals AI and the paper's formalization contributors

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 合作单位

```json
[
  "EPFL"
  "Moscow Institute of Physics and Technology"
  "Indiana University Bloomington"
  "Independent researchers (according to paper author affiliations)"
]
```

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### Authors

```json
[
  "Nikil Ravi"
  "Kexing Ying"
  "Vasilii Nesterov"
  "Rayan Krishnan"
  "Elif Uskuplu"
  "Bingyu Xia"
  "Janitha Aswedige"
  "Langston Nashold"
]
```

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### Maintainer

Vals AI

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Funders

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## Design goals

### 目标能力

Machine-verifiable Lean 4 proofs of advanced undergraduate and graduate mathematics theorems.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 相对既有评测的缺口

A proof in natural language can conceal logical gaps; deterministic formal checking is required.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## Construction

### 题目与标签来源

Qualifying examinations and standard textbooks, covering probability, measure, analysis, algebra, algebraic geometry, number theory, and logic.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 出题/标注背景

Lean 4 experts, including doctoral students and specialists in the field.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Review process

Questions and Lean formal statements received a second human review, to avoid incorrect formalization.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Quality control

Each accepted proof is recompiled and checked for #print axioms; sorry, admit, and new axioms are not accepted.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 去污染与隔离

The original paper withheld 200 questions in order to prevent training contamination. Current v1.1 changes this to 100 public and 100 private, and the private 100 are used for the leaderboard. Textbooks and qualification examinations can themselves be public. Hiding the formalization does not guarantee that a model has never seen the theorem in natural language.

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

## Data format

### Size

100 public questions and 100 private questions; the current leaderboard takes the 100 private questions as its reporting basis.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Question types

A stem in natural language plus a formal statement in Lean 4, from which a formal proof is generated.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Modalities

```json
[
  "文本"
  "Lean code"
]
```

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Languages

Mathematical natural language and Lean 4

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Difficulty

Advanced undergraduate and graduate mathematics

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 公开/隐藏划分

Versions differ, and so does what can be downloaded: the original v1 paper keeps 200 questions confidential and releases only examples; the current v1.1 web page says public 100 and private 100, and the current leaderboard evaluates the private 100 questions; the repository README still says that it contains only sample problems. It cannot be claimed that download of the complete public 100 questions has been verified.

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

Accuracy (%): the proportion of questions that are finally submitted and that pass the Lean check.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 判分

At most 40 turns per question. submit_proof is required, and compilation must pass. No submission scores zero. Each proof is checked with #print axioms. sorry, admit, and newly added axioms are rejected. native_decide is now accepted: it depends on Lean.ofReduceBool and Lean.trustCompiler, and it is not a proof reduced step by step by the kernel alone.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 提示/推理设置

Ordinary models have no internet. lean_loogle queries Mathlib, lean_run_code iterates, and submit_proof is allowed only once, at the end. Ordinary models use Lean 4.25.2. Aristotle uses 4.28.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 官方实现

https://github.com/vals-ai/proof-bench; main.py, proof_bench/agent.py, tools.py, prover.py, and others. The --k 3 in the README command is a parameter of the reproduction experiment, and it is not automatically taken as the number of repeats on the current leaderboard.

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### 可比性边界

v1.1 is not comparable with the older version. Aristotle has its own system, web search, and a different Mathlib; AlephProver also uses its own infrastructure and a different budget.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## Current status

### 核验日

2026-11-08

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 本次版本快照

```json
{
  "version": "v1.1"
  "heat_confidence": "A"
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/proof_bench"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "The Vals leaderboard states an update of 2026-10-29; the Epoch ECI includes ProofBench, but it marks the evaluation as carried out by the creator. Inclusion in the index is not written down as an independent actual run."
    }
    {
      "url": "https://epoch.ai/data/eci-documentation/data"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "The Vals leaderboard states an update of 2026-10-29; the Epoch ECI includes ProofBench, but it marks the evaluation as carried out by the creator. Inclusion in the index is not written down as an independent actual run."
    }
  ]
}
```

> The Vals leaderboard states an update of 2026-10-29; the Epoch ECI includes ProofBench, but it marks the evaluation as carried out by the creator. Inclusion in the index is not written down as an independent actual run.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）；[2](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### Paper revisions

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-03-28"
    "timezone": ""
  }
]
```

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### Saturation

4 systems on the current leaderboard score 100%; the surface result is a full score, but this cannot be generalized to general mathematical research being fully solved.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 污染/限制/争议

v1.1 cannot be compared directly with the older version. native_decide was rejected first and accepted later, which affects the per-question scores of 7 models on 2 questions. Aristotle may use the network, uses Lean 4.28, and may use auxiliary lemmas for the whole file. The language models have no network, use Lean 4.25.2, and submit only the proof body. AlephProver may use auxiliary lemmas, is barred from the network, and uses 4.25.2. A budget of $500/24h scored 100, and the first round at $75/90min scored 99. These systems and budgets cannot be treated as one controlled configuration.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 衍生与相关版本

Distinct from the existing miniF2F; v1.1 is the latest version of this entry.

> Editorial note on deduplication; the same benchmark subset, metric, or version is not counted more than once.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not the experiment run date)

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 官方结果入口

https://www.vals.ai/benchmarks/proof_bench

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 第三方入口

https://epoch.ai/data/eci-documentation/data

[1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| Current official v1.1 / private 100 | 1 | [Claude Sonnet 5.5](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 2 | [Claude Opus 5.5](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 3 | [Claude Fable 5.1](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 4 | [AlephProver](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 5 | [GPT-6.1 Sol](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 6 | [GPT-6 Astra](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 7 | [Gemini 4 Argon](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 8 | [Claude Opus 5](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 9 | [Claude Fable 5](https://www.vals.ai/benchmarks/proof_bench) | 95.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 10 | [Wonder Full](https://www.vals.ai/benchmarks/proof_bench) | 94.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 11 | [Kimi K3.1 Pro](https://www.vals.ai/benchmarks/proof_bench) | 91.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 12 | [Claude Haiku 5.5](https://www.vals.ai/benchmarks/proof_bench) | 89.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 13 | [Kimi K3](https://www.vals.ai/benchmarks/proof_bench) | 87.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 14 | [Aristotle](https://www.vals.ai/benchmarks/proof_bench) | 86.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 15 | [Wonder](https://www.vals.ai/benchmarks/proof_bench) | 84.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 16 | [GPT-6 Sol](https://www.vals.ai/benchmarks/proof_bench) | 83.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 17 | [GPT-5.6 Sol](https://www.vals.ai/benchmarks/proof_bench) | 83.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 18 | [Claude Sonnet 5](https://www.vals.ai/benchmarks/proof_bench) | 77.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 19 | [Hy4 Preview](https://www.vals.ai/benchmarks/proof_bench) | 75.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 20 | [GPT-5.6 Terra](https://www.vals.ai/benchmarks/proof_bench) | 74.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 21 | [MiMo V2.6 Pro](https://www.vals.ai/benchmarks/proof_bench) | 70.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 22 | [GPT-6 Luna](https://www.vals.ai/benchmarks/proof_bench) | 64.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 23 | [MiMo V2.6 Flash](https://www.vals.ai/benchmarks/proof_bench) | 63.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 24 | [Ember-1](https://www.vals.ai/benchmarks/proof_bench) | 61.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 25 | [GPT-5.6 Luna](https://www.vals.ai/benchmarks/proof_bench) | 60.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 26 | [Gemini 3.7 Flash](https://www.vals.ai/benchmarks/proof_bench) | 58.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 27 | [Muse Spark 1.3 Max](https://www.vals.ai/benchmarks/proof_bench) | 58.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 28 | [Qwen 3.8 Max](https://www.vals.ai/benchmarks/proof_bench) | 58.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 29 | [DeepSeek V4 Flash 0731](https://www.vals.ai/benchmarks/proof_bench) | 56.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 30 | [Muse Spark 1.3](https://www.vals.ai/benchmarks/proof_bench) | 55.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 31 | [DeepSeek V4.1 Flash](https://www.vals.ai/benchmarks/proof_bench) | 54.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 32 | [Grok 4.6](https://www.vals.ai/benchmarks/proof_bench) | 51.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 33 | [DeepSeek V4 Pro 0813](https://www.vals.ai/benchmarks/proof_bench) | 50.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 34 | [GLM 5.3](https://www.vals.ai/benchmarks/proof_bench) | 49.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 35 | [Gemini 3.8 Flash](https://www.vals.ai/benchmarks/proof_bench) | 48.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 36 | [Muse Spark 1.2](https://www.vals.ai/benchmarks/proof_bench) | 43.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 37 | [Step 5 Preview](https://www.vals.ai/benchmarks/proof_bench) | 42.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 38 | [Gemini 3.5 Flash](https://www.vals.ai/benchmarks/proof_bench) | 31.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 39 | [Grok 4.5](https://www.vals.ai/benchmarks/proof_bench) | 31.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 40 | [Grok 4.7](https://www.vals.ai/benchmarks/proof_bench) | 26.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 41 | [Gemini 3.1 Pro Preview (02/26)](https://www.vals.ai/benchmarks/proof_bench) | 26.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 42 | [MiMo V2.5 Pro](https://www.vals.ai/benchmarks/proof_bench) | 22.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 43 | [GLM 5.3 Flash](https://www.vals.ai/benchmarks/proof_bench) | 21.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 44 | [Beam 1.0](https://www.vals.ai/benchmarks/proof_bench) | 18.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 45 | [MiniMax-M3](https://www.vals.ai/benchmarks/proof_bench) | 18.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 46 | [DeepSeek V4](https://www.vals.ai/benchmarks/proof_bench) | 16.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 47 | [MiMo V2.5](https://www.vals.ai/benchmarks/proof_bench) | 16.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 48 | [Qwen 3.8 27B](https://www.vals.ai/benchmarks/proof_bench) | 16.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 49 | [Mistral Large 4 Preview](https://www.vals.ai/benchmarks/proof_bench) | 10.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 50 | [Mistral Medium 3.5](https://www.vals.ai/benchmarks/proof_bench) | 9.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 51 | [Inkling Small](https://www.vals.ai/benchmarks/proof_bench) | 6.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 52 | [Mercury 2.5](https://www.vals.ai/benchmarks/proof_bench) | 3.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 53 | [Inkling](https://www.vals.ai/benchmarks/proof_bench) | 0.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Current official v1.1 / private 100 | 54 | [Nemotron 3.5 Lightning](https://www.vals.ai/benchmarks/proof_bench) | 0.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| Paper v1 Table 2 / historical 200 questions | 1 | [Claude Opus 4.5 (Thinking)](https://arxiv.org/pdf/2603.26996) | 33.5 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 2 | [Gemini 3 Pro (11/25)](https://arxiv.org/pdf/2603.26996) | 18.5 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 3 | [Claude Sonnet 4.5 (Thinking)](https://arxiv.org/pdf/2603.26996) | 18 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 4 | [GPT 5](https://arxiv.org/pdf/2603.26996) | 17 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 5 | [Gemini 3 Flash (12/25)](https://arxiv.org/pdf/2603.26996) | 15 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 6 | [GPT 5.2](https://arxiv.org/pdf/2603.26996) | 13.5 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 7 | [GPT 5 Nano](https://arxiv.org/pdf/2603.26996) | 12.5 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 8 | [GPT 5.1 Codex Max](https://arxiv.org/pdf/2603.26996) | 12 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 9 | [DeepSeek V3.2 (Nonthinking)](https://arxiv.org/pdf/2603.26996) | 8 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 10 | [GPT 5 Mini](https://arxiv.org/pdf/2603.26996) | 7 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 11 | [GLM 4.7](https://arxiv.org/pdf/2603.26996) | 4.5 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 12 | [Grok 4.1 Fast (Reasoning)](https://arxiv.org/pdf/2603.26996) | 4 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |
| Paper v1 Table 2 / historical 200 questions | 13 | [DeepSeek V3.2 (Thinking)](https://arxiv.org/pdf/2603.26996) | 3 | Accuracy (%) on the legacy 200 questions of FormalProofBench. | 2026-03-28 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 覆盖与限制

The 54 rows on the v1.1 official site and all 13 rows of Table 2 in paper v1 are included, with versions on separate tracks. The first 4 entries on the current web page display 100%; the original displayed row numbers are kept, and tied scores are not written as a real performance gap. Epoch ECI only aggregates the creators' results, and no score labeled “independent Epoch run” is added on that basis.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

## Contact

### 项目公开邮箱

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### GitHub反馈

https://github.com/vals-ai/proof-bench/issues

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### 官方社交

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 隐私边界

Only official channels for project feedback are listed; private email addresses of the authors are not inferred.

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08）

## Original files

### 原始PDF

https://arxiv.org/pdf/2603.26996

> Entry point for the original paper PDF; not downloaded or uploaded; hash and byte count Unverified.

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### SHA-256

e5f3a7973c389484b6114050274665dc2fb2525edc0e48f8908adfb44119b9ac

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### PDF bytes

818681

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### Folder

Unverified

> The listed materials have been checked, but this field has not yet been precisely verified; this does not mean the official source has not published it.

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Official web-page methods and leaderboard (not a PDF)"
    "url": "https://www.vals.ai/benchmarks/proof_bench"
  }
]
```

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Paper PDF

Unverified

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## Changelog

[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）
