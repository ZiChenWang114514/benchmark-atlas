# ToolTurns

A multi-turn tool-use dialogue benchmark of 2,620 problems spanning 1,827 tools and 11,004 API endpoints, each with an intentionally underspecified first request and two context-dependent follow-ups. The paper reports that the best of nine agents, Claude Opus 4.8, resolves 69.6% of individual requests but completes only 39.8% of full dialogues.

## Basic information

**Short name**：ToolTurns

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Full name**：ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Version**：arXiv:2611.14925v1; a benchmark of 2,620 problems (1,827 tools, 11,004 API endpoints, 47 categories)

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Paper version**：arXiv:2611.14925v1 (2026-11-11)

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Release date**：2026-11-11

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Section**：Agent

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Tags**：Tool use; Multi-turn dialogue; User simulation; Agent evaluation

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**License**：The paper is released on arXiv under Creative Commons Attribution 4.0 International. The official repository states that original code, prompts, configuration, and documentation are under Apache License 2.0, and that original benchmark questions, withheld contexts, anonymized research labels, and derived scores are under CC BY 4.0. Embedded upstream material such as ToolBench tool schemas retains its original licenses (ToolBench and StableToolBench Apache-2.0; API-Bank-derived data under the upstream MIT declaration); the StableToolBench cache is not redistributed.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Paper or report**：https://arxiv.org/abs/2611.14925

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Code**：https://github.com/milad621/ToolTurns

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Dataset**：https://github.com/milad621/ToolTurns

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Homepage**：https://github.com/milad621/ToolTurns

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Paper title**：ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Origin and maintenance

**Initiators**：University of California, Santa Cruz

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Partners**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Authors**：Milad Gholami, Brendan King, and Jeffrey Flanigan (the paper does not mark equal contribution or a corresponding author)

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Maintainer**：Unverified. The repository license scope names the three authors as copyright holders and does not list a separate maintainer role.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Funders**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Design goals

**Capabilities tested**：Tests whether tool-using agents can clarify an intentionally underspecified initial request, call tools, and retain conversational context across two context-dependent follow-ups. Each problem exposes a fixed subset of endpoints (26.5 on average). A user simulator answers clarification questions from withheld context and generates follow-ups from the user-visible conversation. Evaluation along each agent’s own trajectory reports request-level task success, full-dialogue completion, and a five-aspect dialogue-quality rubric.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Gap in prior benchmarks**：The paper argues that most large-scale tool-use benchmarks focus on isolated requests. ToolBench and similar resources provide broad API coverage but not adaptive multi-turn user dialogue, while interactive benchmarks such as tau-bench and ToolSandbox evaluate agents mainly in stateful application environments. This work targets the combination of broad API coverage and adaptive, end-to-end dialogue evaluation: whether agents can clarify underspecified requests and resolve related follow-ups across diverse tool sets.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Construction

**Question sources**：The tool catalogue is the RapidAPI collection released with ToolBench, executed through a StableToolBench-based cache or LLM-simulated layer. After tool sets are sampled from ToolBench’s three retrieval groups and expanded to all endpoints of the referenced tools, GPT-4o-mini generates, from a fixed template, queries that deliberately omit needed details together with two to four context keywords. Initial queries and withheld context are model-generated, not written by people. The official repository’s complete evaluation input is the 2,620-record file final_queries_march_27_2026.json.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Author background**：All three authors are listed in the paper and citation file as affiliated with the University of California, Santa Cruz. Further personal biographies are unverified.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Review process**：The paper is a preprint. The official repository describes it as an ICLR 2027 submission or preprint, but the paper text itself does not report a review decision. Problems are model-generated. User turns may pass through a checker–fixer pipeline, and 120 revised pairs received blind human preference annotation. Agreement between human annotators and the LLM judges was measured for both task success and dialogue-quality aspects.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Quality control**：An optional checker–fixer pipeline evaluates each simulated user turn against eleven violation types plus deterministic rules, and a fixer rewrites flagged turns while preserving intent. The paper reports that the pipeline rewrote 536 of 1,272 candidate user turns and reduced rule-detected defects by 41.2% among rewritten turns; blind human annotators preferred the revised turn in 63.3% of 120 pairs. Task success uses a deterministic hard-fail gate (applied to only 20 of 70,740 subtasks) before an LLM judge decides whether that subtask’s information need was fully met. Human–LLM agreement was Cohen’s kappa 0.68 for binary task success and quadratic-weighted kappa 0.53 across the five dialogue-quality aspects. The repository redacts credential-like example fields from upstream tool metadata.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Decontamination**：The paper does not describe a decontamination procedure against model pretraining corpora. Problems are newly generated from tool schemas, and the generation prompt requires queries not to mention tool or API names.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Data format

**Size**：The evaluation set has 2,620 problems spanning 1,827 distinct tools, 11,004 distinct API endpoints, and 47 RapidAPI categories. Of these, 1,032 (39.4%) are single-tool, 1,588 (60.6%) are multi-tool, and 1,023 are cross-category multi-tool problems (64.4% of multi-tool problems). Tools per problem are 3.4 mean / 3.0 median, and endpoints per problem are 26.5 / 15.0. Each dialogue has an initial request and two follow-ups, producing 7,860 separately scored subtasks per agent. The official repository notes that runtime name normalization merges five aliases, yielding 10,999 normalized triples, distinct from the paper’s count of 11,004 raw triples.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Question types**：Multi-turn tool-use dialogues. Each problem is a triple of an initial natural-language query, a fixed set of callable endpoints and their schemas, and a user goal represented as slot–value constraints. The agent may invoke a tool, send a message to the user for clarification, or complete the current request with a final answer.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Modalities**：Text dialogue together with structured tool schemas, tool calls, and tool responses; no images or speech.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Languages**：English, based on the paper’s example problems, prompts, and evaluation protocol.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Difficulty**：The paper describes the benchmark as hard: pooled subtask pass rates across nine models fall in a 55–70% band and no model reaches 70%; requiring all three subtasks of a dialogue to succeed drops every model below 40%, with a best rate of 39.8%. Under the existing protocol, every evaluated model scores lower on both follow-ups than on the initial request, with drops from 2.1 to 16.2 percentage points.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Public and hidden split**：The paper uses the 2,620 problems as a shared evaluation set, and the official repository releases the complete questions and sanitized saved scores. Neither the paper nor the repository describes a separate hidden test set.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Evaluation

**Metrics**：Task success includes the pooled subtask pass rate and the stricter all-three-subtasks-pass dialogue completion rate; a dialogue’s task-success score is the fraction of its subtasks that succeed. Dialogue quality is scored on consistency, relevance, efficiency, correctness, and adaptability, each on a five-level scale of 0, 0.25, 0.5, 0.75, and 1.0. The weighted aggregate uses weights 0.30 for correctness; 0.20 each for consistency, relevance, and efficiency; and 0.10 for adaptability. Dialogues and subtasks for which the judge returned an error are excluded.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Scoring**：Task success uses a hybrid evaluator: a deterministic gate fails the subtask if every substantive tool observation is documentation-placeholder prose rather than data-shaped output; otherwise an LLM judge returns, via structured function calling, whether the user’s information need for that query was fully met. Each dialogue-quality aspect uses one LLM call. In the main experiments, rubric and task-success judges use gpt-oss at temperature 0.2 with a fixed prompt set across agents. A Table 3 footnote states that GPT-OSS is also the judge model, so its scores are not judge-independent.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Prompt settings**：In the main experiments the user simulator is Qwen3-32B-AWQ with the checker–fixer pipeline enabled; the same model also supplies API responses missing from the StableToolBench cache. Within a turn, the agent’s tool-using search loop is capped at 15 messages, followed by one final synthesis call if the budget is exhausted. All five open-weight agents have reasoning enabled by default, and the authors did not disable it. Judge prompts are given in Appendix G and held fixed across agents. The repository provides offline commands and experiment configurations.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Official scripts**：The official repository https://github.com/milad621/ToolTurns provides the commands toolturns offline, validate, and tables after installation, plus experiment and reproduction documentation. The paper points to release v1.0.0 of that repository for the benchmark, code, configurations, and sanitized saved scores. The repository’s current software version is 1.0.1, and it states that the paper’s availability link remains pinned to v1.0.0.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Comparability note**：The scores in paper Tables 3 and 4 are the authors’ own runs. The official release states that all 72 main-table cells reproduce under the historical aggregation rules, including judge-error exclusions, but it does not claim an end-to-end rerun of the reported experiments, and some auxiliary results are not independently reproduced. The task-success judge sees only the current subtask’s tool evidence, which may affect follow-up scores; the paper states that the effect on rankings has not been quantified. Evaluation trajectories are shaped by a simulated user, and tool observations come from a cache or an LLM simulation rather than live provider calls. GPT-OSS scores are not judge-independent because that model is also the judge.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Current status

**Checked on**：2026-11-14

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Latest data version**：The paper’s availability link is pinned to repository release v1.0.0. The repository’s current version is 1.0.1, which states that the software fix does not change the preserved paper values. The evaluation input is the 2,620-problem file final_queries_march_27_2026.json.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Paper revisions**：v1 submitted on 2026-11-11

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Saturation**：Far from saturated. The paper reports a highest subtask success rate of 69.6% and a highest full-dialogue completion rate of only 39.8% among nine models, and states that no agent is scored as completing even two dialogues in five.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Contamination and disputes**：The limitations section notes that measured difficulty mixes the agent with a simulated user’s choices; tool observations are not live provider calls; initial queries and withheld context are generated rather than written by people; and both the dialogue-quality rubric and the task-success evaluator are LLM judges. The task-success judge does not include prior-subtask tool evidence. The repository further records that some historical auxiliary inputs are no longer available, that construction logs and historical random choices were not recovered, and that current generator defaults would produce 2,600 requests and cannot by themselves reconstruct the released 2,620-record snapshot. In 56.1% of its dialogues, GPT-OSS returns an answer as plain text instead of calling finish, leaving the subtask open as protocol non-compliance.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Related benchmarks**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Leaderboard snapshot

**Snapshot date**：2026-11-14

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Official board**：https://github.com/milad621/ToolTurns

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Results snapshot**：All figures are author-reported from paper Tables 3 and 4, on nine models and a shared set of 2,620 problems, excluding dialogues and subtasks for which the judge returned an error. Claude Opus 4.8 has the highest task success and full-dialogue completion, at 69.6% and 39.8%. GPT-5.4-mini has the highest weighted dialogue-quality score, 0.817, but only 56.3% task success. Other task-success rates are Gemma 4-31B-IT 67.5%, GLM-5.2-744B 67.9%, GPT-4.1-mini 64.5%, Qwen3.6-27B 61.0%, Qwen3.5-397B-A17B 60.9%, GPT-4o-mini 57.0%, and GPT-OSS-120B 55.2%. The paper reports that task-success and dialogue-quality rankings correlate at only Spearman rho = 0.23. Table 4 shows that every model scores lower on both follow-ups than on the initial request, with drops of 2.1 to 16.2 points from the initial request to the second follow-up. The checker–fixer pipeline reduces detected defects by 41.2% on the 536 turns it rewrites, and blind human annotation prefers the revised turn in 76 of 120 pairs.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Coverage note**：Official results cover four proprietary models (GPT-4o-mini, GPT-4.1-mini, GPT-5.4-mini, and Claude Opus 4.8) and five open-weight models (Qwen3.5-397B-A17B, Qwen3.6-27B, Gemma 4-31B-IT, GPT-OSS-120B, and GLM-5.2-744B). The user simulator is Qwen3-32B-AWQ. Auxiliary experiments include simulator ablations, a comparison with human-written API-Bank dialogues, and human agreement checks for the judges; those are not the nine-model main table.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Contact

**Public email**：Author emails listed in the paper: mgholami@ucsc.edu, bking2@ucsc.edu, jmflanig@ucsc.edu

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Code discussion**：Issue tracker of the official code repository: https://github.com/milad621/ToolTurns/issues

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2611.14925.pdf

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Checksum**：ed949696bfef2967af35c5f4f98951409058d34e242ac3a5b5e5cd110103b51b

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**File size**：368510

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

**Other documents**：The experimental arXiv HTML version at https://arxiv.org/html/2611.14925v1; official repository files on license scope, third-party notices, data, reproduction, and verification, plus release notes for v1.0.0 and v1.0.1.

Sources: [1](https://arxiv.org/abs/2611.14925) [2](https://arxiv.org/pdf/2611.14925.pdf) [3](https://github.com/milad621/ToolTurns) (accessed 2026-11-14)

## Changelog

2026-11-14: Initial filing.
