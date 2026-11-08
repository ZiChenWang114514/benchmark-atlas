# FrontierMath Erdős

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

What it measures is solving unsolved conjectures and giving Lean proofs within a unified budget, not a mathematics contest whose answers are already known. The public registry of solved problems includes the standard evaluation, additional attempts, and external work, and the total in the registry cannot be substituted for a model score.

Latest review

## Basic information

**简称**：FrontierMath Erdős

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**全称**：FrontierMath Erdős

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**基准版本**：A fixed question set of 68 conjectures (constructed in August 2026)

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**论文版本**：arXiv v1（2026-09-06）

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**发布日期**：2026-09-06 19:32:55 (first arXiv version; the question set was built in August 2026)

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 ) ; [2](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**主板块**：数学

核验说明：Benchmark Constitution editorial filing. It is not an official classification.

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**领域标签**：数学

核验说明：编辑标签

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**许可证与授权边界**：The body of the repository is MIT; question files derived from Formal Conjectures separately follow Apache-2.0 and third-party statements, so not all content can be labeled MIT in blanket terms.

Sources: [1](https://github.com/epoch-research/LeanOpenProblems/blob/HEAD/LICENSE) (accessed 2026-11-07 )

**论文或技术报告**：https://arxiv.org/abs/2609.25050

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**官方代码**：https://github.com/epoch-research/LeanOpenProblems

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**数据地址**：https://github.com/epoch-research/LeanOpenProblems

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**官方主页**：https://epoch.ai/benchmarks/frontiermath-erdos

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**论文题名**：FrontierMath Erdős

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

## Origin and maintenance

**发起方**：Epoch AI

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**协作与机构边界**：Thomas F. Bloom (University of Manchester); citing an upstream library is not treated as institutional collaboration.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**作者**：Tom Adamczewski；Thomas F. Bloom

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**维护方**：Epoch AI

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**资助方**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

## Design goals

**测量能力**：Autonomously proves or refutes open mathematical conjectures under a unified budget, and submits Lean formal proofs.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**相对既有评测的缺口**：Avoid reporting only successes, leaving the budget unclear, and leaving human scaffolding opaque; numeric checks are not a substitute for a complete proof.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

## Construction

**题目来源**：Thomas Bloom selects, from erdosproblems.com, unsolved problems that have mathematical significance and difficulty.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**出题与研究背景**：Thomas Bloom is a mathematician and the maintainer of ErdősProblems.com.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**审核流程**：50 conjectures (48 numbered items) are taken from Formal Conjectures; 17 numbered items that had not been formalized yielded 18 conjectures by automatic formalization, and Thomas Bloom reviewed the faithfulness of each one.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**质量控制**：Comparator checks statements against the allowed axioms in a separate container and replays them through the Lean kernel.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**去污染与泄漏边界**：All were unsolved in August 2026; subsequently published proofs may enter training data and should be filtered by the model's knowledge cutoff.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

## Data format

**规模与口径**：68 Lean conjectures, corresponding to 65 ErdősProblems numbers.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**任务类型**：Prove or disprove; output a complete Lean proof.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**模态**：Formal mathematics text；代码

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**语言**：Lean 4 / Mathlib; natural-language descriptions from the literature.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**难度**：Open conjectures at research level; the difficulty of formalization also affects the score.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**公开与隐藏划分**：The Lean statements of the conjectures and the evaluation scaffold are public; this is not standard question answering with hidden answers.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

## Evaluation

**指标**：The proportion of 68 conjectures that passed verification; the error bars are ±1 standard error.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**评分方式**：Only proofs or disproofs that match the trusted statements exactly, add no extra axioms, and can be replayed by the Lean kernel are accepted.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**提示与运行设置**：One attempt per conjecture; 300 US dollars and 72 hours each time; offline Docker, with a shell, an editor, Mathlib, SageMath, and a snapshot of the mathematics literature through 2022.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**官方复现入口**：https://github.com/epoch-research/LeanOpenProblems

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**可比性警告**：Additional high-budget runs or multiple attempts are not counted on the standard leaderboard; the total number of solved problems is not the standard score of any model.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

## Current status

**本次核验**：2026-11-07

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**数据及热度证据**：```json
{
  "version": "A fixed question set of 68 conjectures (constructed in August 2026)"
  "heat_confidence": "A"
  "why_trending": "Candidate heat tier A; the evidence reopened below is labeled, item by item, with the evaluating party and the nature of the evidence, and the number of web pages is not treated as the number of independently adopting organizations."
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/data/benchmarks.csv"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "organization": "Epoch AI"
      "note": "The CSV was read and successful run records were extracted, including 2026H2 runs."
    }
    {
      "url": "https://epoch.ai/benchmarks/frontiermath-erdos"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "organization": "Official maintainer"
      "note": "The current official methods and leaderboard have been opened; the observation date is not presented as the publication date."
    }
  ]
}
```

Sources: [1](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-07 ) ; [2](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**论文与版本历史**：v1: 2026-09-06 19:32:55; the arXiv submission history lists only this version.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**饱和程度**：As of 2026-10-29 the official site lists 17 solved problems (including external research and nonstandard attempts); this does not mean the standard protocol is saturated.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**已知问题与局限**：The cost of formalizing proofs may underestimate mathematical ability; later public solutions bring a risk of contamination.

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**后续与衍生**：The original frontiermath already includes v2 Tier1–4; Erdős is an independently named suite of unsolved problems and is given its own entry.

核验说明：The editorial standard for deduplication; concrete differences among versions still follow the official materials.

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**官方入口**：https://epoch.ai/benchmarks/frontiermath-erdos

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**第三方入口**：https://epoch.ai/data/benchmarks.csv

Sources: [1](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-07 )

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| Unverified (CSV is empty) | 1 | GPT-6.1 Sol (max) | 0.0441176470588235 | mean_score (0–1) | 2026-10-02 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 2 | GPT-6 Astra (max) | 0.0294117647058823 | mean_score (0–1) | 2026-08-29 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 3 | Claude Opus 5.5 (max) | 0.0294 | mean_score (0–1) | 2026-09-24 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 4 | Claude Sonnet 5.5 (max) | 0.029 | mean_score (0–1) | 2026-10-08 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 5 | GPT-6 Sol (max) | 0.0147058823529411 | mean_score (0–1) | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 6 | Gemini 4 Argon (high) | 0.0147058823529411 | mean_score (0–1) | 2026-10-21 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 7 | Grok 4.7 (xhigh) | 0.0 | mean_score (0–1) | 2026-09-22 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| Unverified (CSV is empty) | 8 | Gemini 3.8 Flash (high) | 0.0 | mean_score (0–1) | 2026-09-03 | [原始来源](https://epoch.ai/data/benchmarks.csv) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：The top 8 successful FrontierMath-Erdos records are refreshed. mean_score is kept as the original decimal on 0–1, and 0.0294 is not forcibly rewritten as 2/68. An empty task version in the CSV remains Unverified; the 17 solved items on the page include external or nonstandard attempts and are not the standard score of any one model.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07 ) ; [2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-07 )

## Contact

**公开联系邮箱**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**Issues或讨论入口**：https://github.com/epoch-research/LeanOpenProblems/issues

Sources: [1](https://github.com/epoch-research/LeanOpenProblems) (accessed 2026-11-07 )

**官方社交**：https://x.com/EpochAIResearch

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**隐私政策**：https://epoch.ai/privacy

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

## Original files

**原始PDF**：https://arxiv.org/pdf/2609.25050

Sources: [1](https://arxiv.org/abs/2609.25050) (accessed 2026-11-07 )

**PDF SHA-256**：49a0289087c9378b02e0a85cded14cc0ce9d8b43a814065af2e54895eef6babc

核验说明：Byte count of the original downloaded PDF, not the size displayed on the arXiv page.

Sources: [1](https://arxiv.org/pdf/2609.25050) (accessed 2026-11-07 )

**PDF字节数**：```json
316954
```

核验说明：Actual downloaded byte count; it does not mean the file was uploaded.

Sources: [1](https://arxiv.org/pdf/2609.25050) (accessed 2026-11-07 )

**文件夹**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**其他官方文档**：```json
[
  {
    "type": "The official evaluation scaffold and the Lean questions"
    "url": "https://github.com/epoch-research/LeanOpenProblems"
  }
  {
    "type": "Registry of currently solved problems and methods"
    "url": "https://epoch.ai/benchmarks/frontiermath-erdos"
  }
]
```

Sources: [1](https://github.com/epoch-research/LeanOpenProblems) (accessed 2026-11-07 ) ; [2](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

**论文链接**：待核实

状态：待核实。

核验说明：This group only created a local research entry and did not upload.

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

## Changelog

**及历史变更**：```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-07"
    Latest review
  }
]
```

Sources: [1](https://epoch.ai/benchmarks/frontiermath-erdos) (accessed 2026-11-07 )

