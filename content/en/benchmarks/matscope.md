# MatScope

A materials-science reasoning benchmark built on aluminium and high-entropy alloys, with 200 unaided tasks, 20 retrieval-agent cases and 20 sequential forecasting pathways, testing whether models can tell similar material states apart and judge from quantitative evidence.

## Basic information

**Short name**：MatScope

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Full name**：MatScope: a benchmark of language models and agents for scientific reasoning in evolving materials laboratories

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Version**：arXiv:2611.12014v1; M1 Core200 tasks, 20 paired M2 cases and 20 MatEvoBench-20 research pathways

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Paper version**：arXiv:2611.12014v1 (2026-11-09)

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Release date**：2026-11-09

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Section**：Materials

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Tags**：Alloy materials reasoning; Quantitative scientific judgement; Retrieval-augmented agents; Sequential forecasting and revision

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**License**：The paper is distributed on arXiv under the arXiv non-exclusive distribution license; no license has been published for the data or code

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Paper or report**：https://arxiv.org/abs/2611.12014

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Code**：The paper says the code is planned for public release at https://github.com/dddxs/MatScope upon publication and is available to editors and reviewers on request during peer review

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Dataset**：The paper says the questions, reference answers and scoring rubrics are in the supplementary files submitted with the manuscript and will be made available at https://github.com/dddxs/MatScope upon publication

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Homepage**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Paper title**：Benchmarking language models and agents for scientific reasoning in evolving materials laboratories

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Origin and maintenance

**Initiators**：School of Materials Science and Engineering at Shanghai Jiao Tong University and Nanyang Technological University, Singapore

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Partners**：NTU School of Materials Science and Engineering and NTU College of Computing and Data Science (per the author affiliations)

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Authors**：Xuyu Dong, Yixuan Li, Jianguo Huang, Feng Chen and Yiyun Zhou; corresponding authors Bo An, Zheng Liu and Da Shu

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Maintainer**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Funders**：Science and Technology Cooperation Program of Shanghai Jiao Tong University in the Inner Mongolia Autonomous Region (grant 2023XYJG0001-01-01); National Research Foundation, Singapore, AI Singapore Programme (AISG2-GC-2023-009); the first author is supported by the China Scholarship Council

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Design goals

**Capabilities tested**：Whether language models and agents can tell closely related material states apart and reason accurately with quantitative evidence, in three parts: M1 for unaided condition-specific reasoning, M2 for tool-assisted transfer of related literature to unresolved questions, and MatEvoBench-20 for initial forecasts and revisions as observations are released

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Gap in prior benchmarks**：The paper argues that existing benchmarks cover domain knowledge, multimodal interpretation and scientific tool use, but do not adequately test the ability to separate similar material states, reason with quantitative evidence and keep judgements reliable as evidence accumulates

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Construction

**Question sources**：Tasks are drawn from a corpus of 28,872 deduplicated works (716,080 text passages), with aluminium alloys and high-entropy alloys as representative systems; sources must have identifiable samples, explicit conditions and quantitative or relational targets, and references come from original measurements and source-supported relationships

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Author background**：The authors are from materials science at Shanghai Jiao Tong University and from materials and computing schools at Nanyang Technological University

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Review process**：Each subquestion has a scientific purpose, a source-supported reference and a target-specific scoring rule; verified extraction and scoring errors are corrected from the saved final answers, and remaining judging concerns and their score effects are reported separately

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Quality control**：Numerical targets use absolute, relative or log-ratio error bands chosen by physical quantity; Python checks numerical errors, unit conversions and ordering; Gemini 3.1 Flash Lite judges explanatory relationships; task scores combine targets by registered weights and dependency rules; intervals come from 2,000 bootstrap resamples of source-connected groups

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Decontamination**：M2 retrieval excludes the source publications used to build the tasks, and a separate permission filter limits the readable passages

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Data format

**Size**：M1: 200 tasks and 1,124 scored targets across 96 source-connected groups and ten research functions; M2: 20 shared-failure cases (64 subquestions, 66 targets); MatEvoBench-20: 20 research pathways with 90 nodes

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Question types**：Open-ended quantitative and relational reasoning, including given-input calculations, conditional numerical predictions, comparisons, mechanism explanations and feasible-route decisions; M2 is a multi-step tool-calling agent task

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Modalities**：Text and numerical records

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Languages**：English

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Difficulty**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Public and hidden split**：Reference answers and scoring rules are kept separate from model inputs during evaluation; the data is planned for release after publication

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Evaluation

**Metrics**：Mean Rubric Score (normalized from a 0 to 5 scale) and complete task success, plus per-function scores, factor errors and MatEvoBench-20 numerical scores at the initial and last hidden checkpoints

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Scoring**：Target-specific rubrics: numerical parts are graded by declared resolution bands and explanatory parts by a model judge; a task score is capped at 20% when none of its claims meets the material-specific discrimination criterion

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Prompt settings**：Each M1 task runs in an independent conversation with the English question and answer requirements, with tools and retrieval disabled; each M2 episode allows up to 3 searches, 8 actions, 10 assistant turns and 6,000 observation tokens, with a 65,536-token generation ceiling and a 30-minute limit

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Official scripts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Comparability note**：Results depend on the specific deployment configuration and answer-generation cost, excluding grading cost; in M2, 12 cases keep the full question and 8 use selected-question projections, so input scope differs

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Current status

**Checked on**：2026-11-12

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Latest data version**：The version described in paper v1

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Paper revisions**：v1 submitted on 2026-11-09

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Saturation**：Not saturated: eleven model deployments reach complete task success of 13.5% to 19.0% on M1

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Contamination and disputes**：The paper records a known semantic-relation judging issue in the zinc-dispersion case as a separate evaluator limitation; two targets with an unspecified local sampling object or ledger operand were removed from the question set

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Related benchmarks**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Leaderboard snapshot

**Snapshot date**：2026-11-12

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Official board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Results snapshot**：Reported in the paper: eleven deployments obtain M1 mean rubric scores of 58.59% to 68.75% and complete success of 13.5% to 19.0%; GPT-6 Astra scores 67.6616% and GPT-6 Sol 67.1955%. On the 20 M2 cases, GPT-6 Astra rises from 17.82% to 19.42% and Claude Fable 5.1 from 15.19% to 19.41%; on 48 shared MatEvoBench-20 endpoints, Astra rises from 32.00% to 37.50% and Fable from 21.42% to 37.67%

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Coverage note**：All results are the authors' own runs; M2 and MatEvoBench-20 evaluate only GPT-6 Astra and Claude Fable 5.1

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Contact

**Public email**：Corresponding-author emails listed in the paper: boan@ntu.edu.sg, z.liu@ntu.edu.sg, dshu@sjtu.edu.cn

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Code discussion**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2611.12014

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Checksum**：e2aab83434018e1e31fa272e7e1eeb79e743ed64e98f95acdb6a6ed7efe5242d

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**File size**：2236271

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

**Other documents**：Unverified

Sources: [1](https://arxiv.org/abs/2611.12014) [2](https://arxiv.org/pdf/2611.12014) (accessed 2026-11-12)

## Changelog

2026-11-12: Initial filing.
