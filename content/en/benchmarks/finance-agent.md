# Finance Agent

> Benchmark Constitution, research snapshot 2026-11-07. The collection time is not the time a score was actually run, or the leaderboard update time.

Finance Agent v2.1 requires an agent to retrieve company filings, to bring together facts across documents, and to follow the conventions of financial analysis. The point is not to write a financial explanation that sounds plausible. The agent must first pass the dealbreaker gate and then receive partial credit under the rubric; the old v1 paper and the HF card must not stand in for the current v2.1 protocol.

Latest review

## Basic information

### Short name

Finance Agent

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### Full name

Finance Agent Benchmark

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### Benchmark version

v2.1

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### Paper version

arXiv v1 (a revision of the paper, not a dataset version)

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### Release date

The first draft of the original paper is dated 2025-05-21; the independent release date of v2.1 is Unverified.

状态：待核实。

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Section

Agent

Note: Filed under one main section. That filing does not limit coverage of other disciplines.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Field tags

- 金融

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 许可与范围

The LICENSE of the v2 harness repository is MIT; the original v1 HF dataset card is CC BY4.0; the Dataset metadata on the v2.1 leaderboard page also lists CC BY4.0. The access and redistribution terms of the private question set must be checked separately against the license, and a statement on the web page is not taken as a commitment that the private data are open.

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/LICENSE)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）；[一手资料3](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Paper

https://arxiv.org/abs/2508.00828

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 代码

https://github.com/vals-ai/finance-agent-v2

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）


### Dataset

- **v2_public_questions**：https://github.com/vals-ai/finance-agent-v2/blob/main/data/public.txt
- **v1_HF**：https://huggingface.co/datasets/vals-ai/finance_agent_benchmark
- **v2_1_test_access**：Official page: Test is private; Validation requires permission

Note: Public HF card revision that was read: 1f80cefae847f2e8b6bdf773f789c90f70293f78; only the state of the public card and of the repository is fixed, and it is not extrapolated to a version of the private test.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料3](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）


### Official homepage

https://www.vals.ai/benchmarks/fabv2-1

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Paper title

Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


## Origin and maintenance

### 发起/作者单位

Vals AI

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 合作与支持

Unverified

状态：待核实。

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Authors

The original paper: Antoine Bigeard, Rayan Krishnan, Shirley Wu, and Langston Nashold; the list of authors of the old paper is not treated as the complete list of personnel for v2.1.

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### Maintainer

Vals AI

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### Funders

Unverified

状态：待核实。

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Design goals

### Abilities measured

Retrieval over public company documents, cross-source synthesis, precise calculation, and modeling, at junior financial-analyst level.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Design background

Requires actual tool calls and implicit financial conventions, not only static question answering over a single document.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Construction

### Question sources

Public company filings and materials; written by domain experts, with emphasis on determinate answers, synthesis across sources, industry practice, and precision of footnotes.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 出题者背景

The questions are aimed at the level of an investment-banking analyst with 2–3 years of experience; experts from the financial industry took part.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Review process

Experts re-review the questions and the rubrics; v2.1 corrects or deletes questions and updates the checks.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Quality control

dealbreaker gating on key facts: if any key item fails, the whole question scores zero.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 污染控制

The test set remains private to prevent overfitting; public or licensed validation samples do not enter the results of this leaderboard.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Data format

### 题量

27 public, licensed Private Validation 450, and private Test 449.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 任务形式

Nine classes of analyst task, covering comparables, precedents, earnings, disclosure, modeling, and others.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Modalities

- 文本
- 财报
- Structured tool return

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Languages

The public questions in the official README and the examples in the paper are in English; the language distribution of the complete private v2.1 set is Unverified

状态：待核实。

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 难度与分层

Analyses that span multiple documents, apply a stricter numerical tolerance, and require implicit insight.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Public and hidden splits

27 questions are public; 450 validation questions can be obtained under a license; Test449 questions are explicitly kept private, and only this test set is used for the leaderboard.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Evaluation

### Metrics

The primary metric is dealbreaker-gated weighted Partial Credit; the secondary metric is All-Pass.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 评分

Failure on a critical dealbreaker scores the whole question at zero; otherwise the score is a severity-weighted check. A jury of three models grades the item.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 提示与运行协议

2 hours per task. Six tools: edgar_search, web_search, parse_html_page, retrieve_information, calculator, and price_history.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 评测脚本

https://github.com/vals-ai/finance-agent-v2. The finance-agent CLI, with the default configuration being the configuration the authors ran. Approved access to the Vals platform and to each data-tool service is required.

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 可比性警示

v2.1 cannot be compared directly with v2. The 537 questions of the older paper, and the original balanced accuracy, do not represent v2.1. The README of the repository currently lists five categories of tools, while the methods page on the official site lists six tools, calculator among them. A reproduction has to fix the tool configuration that was actually used. A difference between those lists is not taken to mean that the protocols are the same.

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料3](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


## Current status

### 核查日期

2026-11-07 (materials snapshot date)

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 版本与采用证据

- **version**：v2.1
- **heat_confidence**：B
- **evidence_2026_h2**：- - **url**：https://www.vals.ai/benchmarks/fabv2-1
    - **date**：2026-11-05
    - **note**：The current Vals leaderboard of 37 models; attention comes mainly from a single organization, and it is not described as broad adoption by the industry.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 材料沿革

- **arxiv_history**：- - **version**：v1
    - **submitted_at_kst**：2025-05-21
    - **timezone**：
- **v2_1_method_changes**：v2.1 updates the questions and the rubrics and replaces the jury with GPT-6.1 Sol, Gemini3.8 Flash, and Claude Sonnet5.5; a hedged answer that offers several candidates is treated as a failure.

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### Saturation

The highest Partial Credit in the current v2.1 is 67.85%, which is not the All-Pass rate; a large number of critical checks are still unmet, and a partial-credit score cannot be used to infer that financial research can be delivered autonomously and reliably.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 污染与局限

The 449 questions of the test are kept private in order to reduce overfitting. The HF card of the original v1 is the description from the period of 537 questions. Its scale, or its license, cannot be used to infer the full contents of the private set in use now. An answer that hedges across several candidates counts as a failure. Updates of the jury and of the rubric make v2 and v2.1 impossible to compare directly.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）


### 版本/衍生关系

v1, v1.1, v2, and v2.1 are historical versions of the same Finance Agent series; Excel Modeling is a related but different task and is not included in this question count.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Leaderboard snapshot

### Snapshot date

2026-11-07 (snapshot date, not the date of the actual run)

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 官方榜

https://www.vals.ai/benchmarks/fabv2-1

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 其他评测入口

Unverified

状态：待核实。

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 分轨结果（结构化快照）

```json
[
  {
    "rank": 1
    "model": "Claude Opus 5.5"
    "score": "67.85%"
    "metric": "v2.1 Partial Credit (labeled Accuracy in the table)."
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-07 "
    "result_type": "Results on the official page; the collection date is not the time at which the leaderboard was updated."
  }
  {
    "rank": 2
    "model": "Gemini 4 Argon"
    "score": "67.66%"
    "metric": "v2.1 Partial Credit (labeled Accuracy in the table)."
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-07 "
    "result_type": "Results on the official page; the collection date is not the time at which the leaderboard was updated."
  }
  {
    "rank": 3
    "model": "Wonder Full"
    "score": "67.58%"
    "metric": "v2.1 Partial Credit (labeled Accuracy in the table)."
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-07 "
    "result_type": "Results on the official page; the collection date is not the time at which the leaderboard was updated."
  }
]
```

[榜单原始资料](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 覆盖范围

Results on the official page; the collection date is not the time at which the leaderboard was updated.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Contact

### 公开研究邮箱

- contact@vals.ai

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 问题反馈

https://github.com/vals-ai/finance-agent-v2/issues

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）


### 机构公开渠道

https://x.com/ValsAI (account of the maintaining organization)

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 隐私政策

Unverified

状态：待核实。

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## Original files

### Paper PDF

https://arxiv.org/pdf/2508.00828

Note: The original v1 paper, not the complete new protocol of v2.1.

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 源站PDF SHA-256

bbb021c3a2070c905a6c0fd9a7404aa9a27d2973cf16f621e620d098b4a06740

Note: Digest of the PDF bytes downloaded from the source site. This does not claim that a copy was updated.

[一手资料1](https://arxiv.org/pdf/2508.00828)（访问 2026-11-07）


### 源站PDF字节数

1321074

[一手资料1](https://arxiv.org/pdf/2508.00828)（访问 2026-11-07）


### 资料目录

Unverified

状态：待核实。

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 其他官方资料

- - **type**：Verified official primary sources
  - **url**：https://github.com/vals-ai/finance-agent-v2/blob/main/README.md
  - **accessed**：2026-11-07
- - **type**：Verified official primary sources
  - **url**：https://huggingface.co/datasets/vals-ai/finance_agent_benchmark
  - **accessed**：2026-11-07

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）


### PDF归档

Unverified

仅核对源站PDF和已有归档引用，未上传或覆盖文件。

## Changelog

- - **date**：2026-11-07
  - **timezone**：
  - **change**：按官方材料新建中文条目；区分热度、质量和不同版本评分。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位Official README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
