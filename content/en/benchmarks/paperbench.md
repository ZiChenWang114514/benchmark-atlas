# PaperBench

> Benchmark Constitution, verification 2026-11-08. Unknowns remain "Unverified"; an access date is not an experiment date.

PaperBench requires an agent to start from a research paper, write code, run experiments, and reproduce the target conclusions. The hierarchical rubric is drawn up together with the authors of the original paper. A full reproduction, Code-Dev that does only code development, and different run budgets do not make one and the same leaderboard.

Sources: [Original description](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08); [Results evidence](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08)

## Basic information

### Short name

PaperBench

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### Full name

PaperBench

Note: The official name is retained, and the paper title is not automatically expanded into a full name.

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### Benchmark version

Original suite of 20 ICML2024 papers

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Paper version

arXiv v3

Note: A paper revision is not the same as a dataset version.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Release date

2025-04-03 00:55:24

Note: The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Section

Agent

Note: Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Field tags

- AI paper-reproduction agent

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 许可与适用范围

LICENSE.md at the root of frontier-evals is MIT; the paper, the original ICML text, external data, and JudgeEval files that cannot be redistributed automatically must each be used under their own license, which MIT does not replace.

Sources: [1](https://raw.githubusercontent.com/openai/frontier-evals/main/LICENSE.md) (accessed 2026-11-08); [2](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2504.01848

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Code repository

https://github.com/openai/frontier-evals

Note: The paper links to openai/preparedness; the request for GitHub metadata on this occasion was redirected to openai/frontier-evals. The license of the code at the root of the repository is not automatically the same as the license of each paper and of each rubric.

Sources: [1](https://github.com/openai/frontier-evals) (accessed 2026-11-08)

### 数据地址

https://github.com/openai/frontier-evals/tree/main/project/paperbench/data

Note: The official README states that the data are distributed by Git-LFS; some JudgeEval materials cannot be redistributed automatically.

Sources: [1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md) (accessed 2026-11-07)

### Official homepage

https://openai.com/index/paperbench/

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### Paper title

PaperBench: Evaluating AI's Ability to Replicate AI Research

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

## Origin and maintenance

### 发起与机构归属

OpenAI

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### 合作关系

The authors of the ICML papers being reproduced jointly set the rubric and signed off on it; this does not mean that they jointly maintain the whole benchmark.

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### Authors

- Starace, Giulio
- Jaffe, Oliver
- Sherburn, Dane
- Aung, James
- Chan, Jun Shern
- Maksin, Leon
- Dias, Rachel
- Mays, Evan
- Kinsella, Benjamin
- Thompson, Wyatt
- Heidecke, Johannes
- Glaese, Amelia
- Patwardhan, Tejal

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Current maintainer

The OpenAI Preparedness / PaperBench team.

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### 资助与支持

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

## Design goals

### Abilities measured

Understand the contribution from a paper, develop code from scratch, run experiments, and reproduce modern AI research.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 设计背景与适用边界

Passing a code question is not the same as being able to reproduce a scientific conclusion; PaperBench requires writing from the paper, running the experiment, and checking the actual reproduction against a rubric developed with the authors, whereas Code-Dev evaluates only the code-development portion.

Sources: [1](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08)

## Construction

### 题目或数据来源

20 ICML2024 spotlight and oral papers, covering 12 topics; a further 2 NeurIPS workshop papers are set aside for development, together with an internal holdout.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 构建者背景

The OpenAI research team and the authors of the original paper jointly decomposed the reproduction targets.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Review process

A hierarchical rubric developed in collaboration with the original authors, multiple rounds of internal review, a clarifying addendum, and final author sign-off.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Quality control

8,316 leaf nodes that can be scored independently; a new VM runs reproduce.sh and then a judge scores the result; JudgeEval is also used to test the judge.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 去污染与泄漏边界

Access to the original authors' repository and to other reproductions is prohibited; the paper reports that 10 of 646 attempts were disqualified for violations. Memorization of code during pretraining cannot be ruled out.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

## Data format

### Size

20 ICML 2024 Spotlight and Oral papers, totaling 8,316 rubric subtasks that can be scored independently.

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### 题型与交付物

Long-horizon research programming and experiment execution; code or files are submitted and then checked against a hierarchical rubric.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Modalities

- Paper text/chart
- 代码
- Experimental data and output

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Languages

Papers and descriptions in English; the programming language and framework follow the paper.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Difficulty

The original-paper reproduction uses a budget of multiple hours; the conditions differ for BasicAgent and IterativeAgent, and for 12h/36h.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Public and hidden splits

The paper, the rubric, and the evaluation code are public, and there is also a development paper and an internally held set; the official 20 papers must not be mixed with the development set.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

## Evaluation

### Metrics

Replication Score: after binary judgments at the leaf nodes, results are aggregated by hierarchical weights and then averaged across papers.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### Scoring

Three stages: the agent writes code in a container; an independent container that has a GPU reproduces the execution; a third container scores the result by the rubric in the paper. Code-Dev skips the reproduction and scores only the requirements of code development, and it cannot be compared directly with the full PaperBench score.

Sources: [1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md) (accessed 2026-11-07)

### 提示与运行设置

The original paper's automatic judge is o3-mini-2025-01-31 high; different agent scaffolds, tools, and experiment budgets are recorded separately.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 评测脚本

https://github.com/openai/frontier-evals/tree/main/project/paperbench

Sources: [1](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08); [2](https://github.com/openai/frontier-evals) (accessed 2026-11-08)

### 可比性提醒

BasicAgent21% and IterativeAgent24–26% are not a change in model capability alone; CodeDev, the budget, the judge version, the standard error, and the paper subset must be stated.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 数据版本与更新

```json
{
 "version": "Original suite of 20 ICML2024 papers"
 "evidence_2026_h2": [
 {
 "url": "https://arxiv.org/html/2609.19134v1"
 "date": "2026-09-16"
 "note": "ScienceIDE §4.1 and its references explicitly cite PaperBench and discuss evaluation aimed at reproducing existing research results; this is an H2 academic citation."
 }
 ]
}
```

Note: Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

Sources: [1](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07); [2](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 论文修订记录

Submission history From: James Aung [ view email ] [v1] 2025-04-03 00:55:24 (4,982 KB) [v2] 2025-04-04 21:44:57 (4,982 KB) [v3] 2025-04-07 21:15:49 (4,982 KB)

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 饱和程度

The highest historical full PaperBench listed in the official README is 26.0±0.3% for IterativeAgent o1-high at 36h. The best BasicAgent in the original paper is 21.0% for Claude3.5 Sonnet. Code-Dev43.4% cannot be treated as the full reproduction rate, and current saturation in 2026 cannot be inferred from the old experiment.

Sources: [1](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08); [2](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08)

### 争议与已知问题

The official site presents the best test agent as Claude 3.5 Sonnet (New) at 21.0%; the README also lists IterativeAgent o1-high at 26.0% for 36h and at 24.4% for 24h. The budgets and the scaffolds differ. Each piece of evidence is kept, and neither overwrites the other.

Sources: [1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md) (accessed 2026-11-07); [2](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### 衍生与后续使用

PaperBench Code-Dev omits execution and is an independent definition; JudgeEval evaluates the judge and is not counted as additional paper-reproduction questions.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (date the web page was accessed; dates of historical results are kept separately).

Sources: [1](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08)

### 官方结果入口

https://github.com/openai/frontier-evals/tree/main/project/paperbench

Sources: [1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md) (accessed 2026-11-07)

### 第三方入口

Unverified

Note: Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07)

### 分赛道结果

- {"model": "IterativeAgent o1-high (36h limit)", "score": 26.0, "track": "Official README/full PaperBench/36h", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.3, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 1}
- {"model": "IterativeAgent o1-high (24h limit)", "score": 24.4, "track": "Official README/full PaperBench/24h", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.7, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 1}
- {"model": "BasicAgent claude-3.5-sonnet", "score": 21.0, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.8, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 1}
- {"model": "IterativeAgent claude-3.5-sonnet", "score": 16.1, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.1, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 2}
- {"model": "BasicAgent o1-high", "score": 13.2, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.3, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 3}
- {"model": "IterativeAgent o3-mini-high", "score": 8.5, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.8, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 4}
- {"model": "BasicAgent deepseek-r1", "score": 6.0, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.3, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 5}
- {"model": "BasicAgent gpt-4o", "score": 4.1, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.1, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 6}
- {"model": "BasicAgent gemini-2.0-flash", "score": 3.2, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.2, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 7}
- {"model": "BasicAgent o3-mini-high", "score": 2.6, "track": "Official README/full PaperBench/paper default budget", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.2, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 8}
- {"model": "IterativeAgent o1-high", "score": 43.4, "track": "Official README/Code-Dev/default budget in the paper", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.8, "runs": 3, "source_date": "2025-04-02", "result_type": "Original-paper historical experiment", "rank": 1}

Sources: [1](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08)

### 覆盖边界

Both results tables in the README were copied in full (10 rows of full PaperBench and 1 row of Code-Dev). The ± values, the run counts, and the source date 2025-04-02 are retained. The 36h setting, the 24h setting, and the paper's default configuration, which does not explicitly state a budget, each form a track, and Code-Dev is independent. The 21% on the official site comes from the BasicAgent setting and does not override the IterativeAgent results.

Sources: [1](https://github.com/openai/frontier-evals/tree/main/project/paperbench) (accessed 2026-11-08)

## Contact

### 公开项目邮箱

- giulio.starace@c-openai.com

Sources: [1](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08)

### 公开反馈渠道

https://github.com/openai/frontier-evals/issues

Sources: [1](https://github.com/openai/frontier-evals) (accessed 2026-11-08)

### 官方社交渠道

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)

### 联系方式收录原则

Benchmark Constitution includes only project contact channels that the paper or the official site has made public, and it does not collect private information; this is not a certification of an external site’s privacy policy.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08)

## Original files

### 既存论文原件

### 原始PDF地址

https://arxiv.org/pdf/2504.01848

Note: Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

Sources: [1](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08)

### 下载SHA-256

2f58f1a6581af9d99432422dccf3cf61f5c263377c1e4550e7333c4a22d7184d

Note: Checksum of the bytes downloaded on 2026-11-08. Nothing was overwritten or uploaded, so this does not establish that an existing original is the same version.

Sources: [1](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08)

### 下载字节数

```json
1703363
```

Sources: [1](https://arxiv.org/pdf/2504.01848) (accessed 2026-11-08)

### Other documents

Note: The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [1](https://openai.com/index/paperbench/) (accessed 2026-11-07); [2](

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2504.01848) (accessed 2026-11-08)
