# MCP Atlas

> Benchmark Constitution, in-depth review 2026-11-08. The access date is not the date the experiment was run; dates from historical sources keep their original record.

MCP-Atlas requires an Agent to discover tools from a tool menu that contains distractors, to complete tasks across real MCP servers, and to give a final answer supported by evidence. It is not a test of a single function call against a simulated API: each of the 1,000 tasks has its own claim rubric, 500 questions are public, and 500 questions are held private.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md](https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md) (accessed 2026-11-08)

## Basic information

### Short name

MCP Atlas

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### Full name

MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 版本与作用域

The data remain the original 1,000 tasks, of which 500 are public. The CHANGELOG of the current public harness marks v2.0.0, and the environment-image README uses 1.2.7. The leaderboard evaluation protocol of April 2026 is listed separately. The three are not the same.

Sources: [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/CHANGELOG.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/CHANGELOG.md) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md](https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 论文/报告版本

arXiv v3（2026-05-20 08:26:22 ）

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### 首次公开日期

2026-02-01 08:19:39 (arXiv v1; the original site's UTC calendar date is 2026-01-31)

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### Section

Agent

Note: Benchmark Constitution editorial classification.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### Subfields

```json
[]
```

Note: Editorial tags; an empty list means finer-grained tags have not yet been added.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 许可与权利边界

The dataset card explicitly states CC BY 4.0. The code license has a source conflict: the LICENSE at the root of the current repository is MIT, while Appendix C.4 of paper v3 still describes the harness and the claims evaluator as Apache 2.0. For the current repository snapshot, the actual MIT file is authoritative, and the historical grant stated in the paper is retained alongside it. Upstream MCP services and tool outputs are separately bound by their own terms.

Sources: [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/LICENSE](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/LICENSE) (accessed 2026-11-08); [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md](https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md) (accessed 2026-11-08)

### 论文/报告入口

https://arxiv.org/abs/2602.00933

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### Code

https://github.com/scaleapi/mcp-atlas

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### Dataset

https://huggingface.co/datasets/ScaleAI/MCP-Atlas

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### Official homepage

https://labs.scale.com/leaderboard/mcp_atlas

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 论文/报告标题

MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

## Origin and maintenance

### 研究发起团队

Scale AI

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 合作研究机构与顾问

National University of Singapore (the named affiliation of co-first author Chaithanya Bandi); the remaining authors are affiliated with Scale AI.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

### Authors

```json
[
 "Chaithanya Bandi"
 "Razvan-Gabriel Dumitru"
 "Ben Hertzberg"
 "Divyansh Agarwal"
 "Geobio Boo"
 "Tejas Polakam"
 "Sami Hassaan"
 "Jeff Da"
 "HiJae Kim"
 "Vipul Gupta"
 "Manasi Sharma"
 "Andrew Park"
 "Martin Dimakis"
 "Ernesto Gabriel Hernández Montoya"
 "Dan Rambado"
 "Ivan Salazar"
 "Rafael Cruz"
 "MohammadHossein Rezaei"
 "Chetan Rane"
 "Ben Levin"
 "Daniel Yue Zhang"
 "Brad Kenstler"
 "Bing Liu"
]
```

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08)

### Maintainer

Scale Research

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### Funders

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

## Design goals

### 测量能力

Tool discovery, construction of parameters, orchestration across MCP servers, error recovery, and synthesis of the final evidence.

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### 设计动机

Avoid testing only simple function calls, simulated APIs, a small pool of tools, or matching of trajectories; score real multi-step workflows and the claims in the answer.

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

## Construction

### 材料来源

Natural-language tasks written and checked by humans; the prompt does not directly name the server, the tools, or the parameters.

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### 命题与标注背景

Written and reviewed by domain experts.

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### Review process

A five-layer quality process: execution of reference trajectories, domain review, prompt-leakage checks, LLM-claims consistency checks, and random human audit.

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### Quality control

Five layers of checks: experts actually run the reference trajectories; domain review; a second review for leakage of prompt-tool names and server names; an LLM check of the completeness of claims and of consistency with the trajectory; and a random human audit. The environment fixes the data and the container version. Final success rests on the claims, rather than on an exact match to the trajectory.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

### 去污染与留出

A random split of 500 public/500 private; the public-private score gap is only an exposure-audit signal, not direct evidence of contamination.

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

## Data format

### 规模与统计对象

Paper v3 and the HF benchmark definition: 1,000 tasks, 36 real MCP servers, and 220 tools, with 500 of the tasks public. The complete list of services linked from the current README instead says 307 tools. The total number of tools available in a running environment is not substituted for the benchmark's actual coverage of 220 tools.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md](https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08)

### 题型与字段

A single-turn instruction in natural language, with multiple tool calls; the fields are TASK, ENABLED_TOOLS, PROMPT, GTFA_CLAIMS, and TRAJECTORY.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07)

### Modalities

```json
[
 "文本"
 "Structured tool inputs and outputs"
]
```

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07)

### Languages

English; non-English tool use is outside the scope of the original paper.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07)

### 难度与覆盖

Most items have cross-server and multi-hop dependencies; the web overview is 3–6 calls per task, while the paper’s statistics are 6–37 tools exposed and 2–8 tools required, a different scope from the web overview of 10–25 exposed tools.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07)

### 公开/私有与数据划分

500 tasks in a public Parquet file; 500 tasks held out as private.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas](https://huggingface.co/datasets/ScaleAI/MCP-Atlas) (accessed 2026-11-07)

## Evaluation

### Metrics

Pass Rate (the proportion of tasks with coverage≥0.75); Mean Coverage is reported separately.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### 评分与聚合

Each claim scores 0/0.5/1. Task coverage takes the mean. coverage ≥ 0.75 counts as a pass, and Pass Rate is the average over tasks. The primary judge in paper v3 is Gemini 3.1 Pro Preview, with GPT-5.4/Claude Opus 4.6 sensitivity experiments listed alongside. The current public code defaults to the same Gemini 3.1 Pro Preview. An older methods section on the web page still writes Gemini-2.5-Pro/temperature0, and it cannot be silently mixed in as the same protocol.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 提示与推理预算

In April 2026 the web page was updated to 100 tool calls per task, and the limit is no longer 20 turns. The current public README defaults to max-turns256, max-tool-calls100, a timeout of 1800 seconds, and no added system prompt; these defaults of the public implementation do not automatically equal every historical submission configuration on the web page.

Sources: [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 官方实现

https://github.com/scaleapi/mcp-atlas

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### 可比性边界

The public subset of 500 and the full set of 1,000 cannot be placed in one ranking; 100-turn and 100-tool-call are not the same budget either. Rank(UB) on the web leaderboard is determined by the confidence interval and does not guarantee an order by the point estimate; the conflict over the version of the judge has been retained.

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

## Current status

### 核验时间

2026-11-08

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 当前数据与协议

```json
{
 "version": "The data remain the original 1,000 tasks, of which 500 are public. The CHANGELOG of the current public harness marks v2.0.0, and the environment-image README uses 1.2.7. The leaderboard evaluation protocol of April 2026 is listed separately. The three are not the same."
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Scale current tool-use leaderboard."
 }
 {
 "url": "https://www.kimi.com/blog/kimi-k3"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "The vendor release page that is visible now self-reports use of the public subset of 500, a 100-turn limit, and a Gemini 3.1 Pro judge; the body corresponds to the July release and cannot be treated as a new adoption event after August."
 }
 ]
}
```

Sources: [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/CHANGELOG.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/CHANGELOG.md) (accessed 2026-11-08); [https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md](https://huggingface.co/datasets/ScaleAI/MCP-Atlas/raw/main/README.md) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 论文修订与延续使用证据

```json
[
 {
 "version": "v1"
 "date": "2026-02-01"
 }
 {
 "version": "v2"
 "date": "2026-05-04"
 }
 {
 "version": "v3"
 "date": "2026-05-20"
 }
]
```

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08)

### 饱和判断边界

The paper peaks at 82.2%; the current web page has higher point estimates, but some of the leading rows show only a place and no number. The 83.6% at the head of the page and the 62.3% in an older section disagree with the dynamic table, so the number at the head of the page is not used as the leading score, and no judgment that the benchmark is saturated is made.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 污染、冲突与复现风险

The score gap between public and private tasks is a signal for monitoring exposure, not a conclusion about contamination. Live API drift, claim noise, and judge differences limit reproduction. The paper's main judge, the current public implementation, and the old methods section on the webpage are not fully consistent, and the code license also conflicts. All of these are listed explicitly and separately.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/README.md) (accessed 2026-11-08); [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/LICENSE](https://raw.githubusercontent.com/scaleapi/mcp-atlas/main/LICENSE) (accessed 2026-11-08)

### 衍生实现

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

## Leaderboard snapshot

### 访问快照日期

2026-11-08 (access; run and submission dates of each source are listed separately)

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 官方榜单入口

https://labs.scale.com/leaderboard/mcp_atlas

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 第三方评测入口

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 分来源、分协议结果

```json
[
 {
 "rank": 1
 "model": "Gemini-4-Argon"
 "score": "Unverified (web page has no numeric values)"
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": null
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 2
 "model": "Muse Spark 1.1"
 "score": 88.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": 1.95
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 3
 "model": "Fable 5.1"
 "score": 87.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": 2.05
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 4
 "model": "Opus 5.5"
 "score": "Unverified (web page has no numeric values)"
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": null
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 5
 "model": "Gemini 3.5 Flash (high)"
 "score": 83.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": 2.3
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 6
 "model": "Qwen3.8-2.4T-A95B (xHigh)"
 "score": 84.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": 2.25
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 7
 "model": "GLM 5.3"
 "score": 84.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": 2.15
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 8
 "model": "claude-opus-5 (xhigh)"
 "score": 85.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Official web page Performance Comparison / All1000 / Rank(UB)"
 "source_url": "https://labs.scale.com/leaderboard/mcp_atlas"
 "accessed": "2026-11-08"
 "reported_plus_minus": 2.1
 "rank_definition": "1 + the number of models whose lower CI exceeds the upper CI of this model."
 "source_date": "The page is marked Updated April 8, 2026; this is not the measured date of each row."
 }
 {
 "rank": 1
 "model": "Muse Spark"
 "score": 82.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 1
 "model": "Muse Spark"
 "score": 79.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 1
 "model": "Muse Spark"
 "score": 79.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 2
 "model": "Claude Opus 4.7"
 "score": 79.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 3
 "model": "Claude Opus 4.7"
 "score": 75.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 5
 "model": "Claude Opus 4.7"
 "score": 74.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 3
 "model": "Gemini 3.1 Pro Preview"
 "score": 78.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 2
 "model": "Gemini 3.1 Pro Preview"
 "score": 75.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 2
 "model": "Gemini 3.1 Pro Preview"
 "score": 76.4
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 4
 "model": "Claude Opus 4.6"
 "score": 76.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 4
 "model": "Claude Opus 4.6"
 "score": 73.3
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 4
 "model": "Claude Opus 4.6"
 "score": 74.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 5
 "model": "GLM-5.1"
 "score": 75.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 5
 "model": "GLM-5.1"
 "score": 72.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 3
 "model": "GLM-5.1"
 "score": 75.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 6
 "model": "GPT-5.5"
 "score": 75.3
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 6
 "model": "GPT-5.5"
 "score": 72.0
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 6
 "model": "GPT-5.5"
 "score": 71.9
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 7
 "model": "GPT-5.4"
 "score": 70.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 7
 "model": "GPT-5.4"
 "score": 68.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 7
 "model": "GPT-5.4"
 "score": 69.9
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 8
 "model": "Gemini 3 Pro Preview"
 "score": 70.3
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 8
 "model": "Gemini 3 Pro Preview"
 "score": 68.0
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 8
 "model": "Gemini 3 Pro Preview"
 "score": 68.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 9
 "model": "Claude Opus 4.5"
 "score": 69.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 10
 "model": "Claude Opus 4.5"
 "score": 66.3
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 9
 "model": "Claude Opus 4.5"
 "score": 68.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 10
 "model": "Claude Sonnet 4.6"
 "score": 69.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 9
 "model": "Claude Sonnet 4.6"
 "score": 66.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 10
 "model": "Claude Sonnet 4.6"
 "score": 67.4
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 11
 "model": "GPT-5.2"
 "score": 67.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 11
 "model": "GPT-5.2"
 "score": 65.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 11
 "model": "GPT-5.2"
 "score": 66.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 12
 "model": "Kimi K2.5"
 "score": 64.4
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 12
 "model": "Kimi K2.5"
 "score": 59.9
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 12
 "model": "Kimi K2.5"
 "score": 63.0
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 13
 "model": "Gemini 3 Flash Preview"
 "score": 62.0
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 13
 "model": "Gemini 3 Flash Preview"
 "score": 57.4
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 13
 "model": "Gemini 3 Flash Preview"
 "score": 59.4
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 14
 "model": "Claude Sonnet 4.5"
 "score": 59.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 14
 "model": "Claude Sonnet 4.5"
 "score": 56.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 14
 "model": "Claude Sonnet 4.5"
 "score": 59.0
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 15
 "model": "GLM-4.7"
 "score": 58.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 16
 "model": "GLM-4.7"
 "score": 54.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 17
 "model": "GLM-4.7"
 "score": 55.7
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 16
 "model": "Gemini 3.1 Flash Lite Preview"
 "score": 57.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 17
 "model": "Gemini 3.1 Flash Lite Preview"
 "score": 54.3
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 16
 "model": "Gemini 3.1 Flash Lite Preview"
 "score": 56.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 17
 "model": "GPT-5.4 Mini"
 "score": 56.7
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 15
 "model": "GPT-5.4 Mini"
 "score": 54.9
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 15
 "model": "GPT-5.4 Mini"
 "score": 57.7
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 18
 "model": "GPT-5.1"
 "score": 50.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 18
 "model": "GPT-5.1"
 "score": 47.9
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 18
 "model": "GPT-5.1"
 "score": 50.8
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 19
 "model": "o3 Pro"
 "score": 44.5
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 19
 "model": "o3 Pro"
 "score": 41.3
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 19
 "model": "o3 Pro"
 "score": 43.6
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 20
 "model": "Claude Haiku 4.5"
 "score": 40.2
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Gemini 3.1 Pro Preview"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 20
 "model": "Claude Haiku 4.5"
 "score": 37.1
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3, Table 7 / All1000 / judge=GPT-5.4."
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
 {
 "rank": 20
 "model": "Claude Haiku 4.5"
 "score": 38.7
 "unit": "%"
 "metric": "Pass Rate (coverage≥0.75)"
 "track": "Paper v3 Table 7 / All1000 / judge=Claude Opus 4.6"
 "source_url": "https://arxiv.org/pdf/2602.00933"
 "accessed": "2026-11-08"
 "result_type": "Historical paper experiments; an independent track per judge"
 }
]
```

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

### 快照覆盖说明

The original Rank(UB) of the top 8 in the dynamic table on the current web page, and the 20 models × 3 judges in Table 7 of paper v3, are recorded independently. The missing values for first place and for fourth place on the web page remain Unverified, and they are not filled from an old table in the body or from the 83.6% headline. The dynamic table cannot be renumbered from point estimates, and the Updated date on the page is not guaranteed to equal the run date of a newly added model.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08); [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

## Contact

### 官方公开联系邮箱

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 项目反馈入口

https://github.com/scaleapi/mcp-atlas/issues

Note: GitHub API has_issues=true

Sources: [https://api.github.com/repos/scaleapi/mcp-atlas](https://api.github.com/repos/scaleapi/mcp-atlas) (accessed 2026-11-07)

### 公开社交渠道

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 联系信息原则

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

## Original files

### 原始论文/技术报告PDF

https://arxiv.org/pdf/2602.00933

Sources: [https://arxiv.org/abs/2602.00933](https://arxiv.org/abs/2602.00933) (accessed 2026-11-08); [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

### PDF SHA-256

2cd00f60d5ac0324ee9edd8693a4a3be61dc3a06c550209310fbf7581917315d

Note: Original bytes downloaded from arXiv. This does not mean an older file was replaced.

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

### PDF原始字节数

571240

Sources: [https://arxiv.org/pdf/2602.00933](https://arxiv.org/pdf/2602.00933) (accessed 2026-11-08)

### 资料夹

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 其他官方资料

```json
[
 {
 "type": "Official methods and introduction page (not the paper PDF)"
 "url": "https://labs.scale.com/leaderboard/mcp_atlas"
 }
]
```

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

### 已存PDF

Unverified

Note: This group only creates local research files and does not upload a PDF or claim that one already exists.

核验状态：待核实

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)

## Changelog

### Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

Sources: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) (accessed 2026-11-08)
