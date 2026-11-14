# Multi-step SWE

A long-horizon software engineering benchmark of 69 tasks, each a chain of 5 to 15 dependent engineering steps that build on the agent's own earlier code; the best of nine frontier models solves only 18.5%.

## Basic information

**Short name**：Multi-step SWE

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Full name**：Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Version**：arXiv:2611.07166v1; 69 tasks and 574 steps

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Paper version**：arXiv:2611.07166v1 (2026-11-04)

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Release date**：2026-11-04

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Section**：Code

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Tags**：Long-horizon software engineering; Coding agents; Multi-step dependent tasks; Version upgrades and migrations

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**License**：The repository is MIT-licensed, with bundled upstream code keeping its original licenses; the paper is CC BY 4.0 on arXiv

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Paper or report**：https://arxiv.org/abs/2611.07166

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Code**：https://github.com/Klavis-AI/Multi-step-SWE

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Dataset**：https://github.com/Klavis-AI/Multi-step-SWE (tasks are stored in Harbor's multi-step format under the tasks directory, with environments, instructions, verifiers and reference solutions)

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Homepage**：https://multistepswe.com/

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Paper title**：Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Origin and maintenance

**Initiators**：Klavis AI

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Partners**：Unverified

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Authors**：Xiangkai Zeng, Zheng Liu and Zihao Lin (equal contribution)

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Maintainer**：Klavis AI

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Funders**：Unverified

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Design goals

**Capabilities tested**：Whether coding agents can complete 5 to 15 dependent engineering requests in a row on one codebase, where each step starts from the code the agent itself wrote earlier, so early design decisions and errors carry forward

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Gap in prior benchmarks**：The paper notes that both single-issue benchmarks like SWE-bench and longer tasks such as Terminal-Bench, DeepSWE, FrontierSWE and ProgramBench are single episodes graded once, so none requires an agent to keep building on its own earlier work

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Construction

**Question sources**：Every step is grounded in an existing source of truth, such as specifications, upstream release histories, protocol revisions, framework migration paths and hand-optimized kernels, which defines both the instruction and the verifier; tasks include from-scratch builds and work on real open-source codebases

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Author background**：All authors are from Klavis AI; tasks were reviewed by professional software engineers with at least five years of experience

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Review process**：Each task passed two rounds of expert review: the first checks the design, whether each step is real progress and whether it fits its time budget; the final round compares every instruction with its verifier and confirms the verifier cannot be passed without doing the work, with fixes re-reviewed

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Quality control**：Each step is graded in a separate verifier container with hidden tests that differ from the public checks; verifiers were adversarially hardened, with each successful attack leading to a new check; a failed build, too few test cases or a grading timeout earns zero

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Decontamination**：The paper acknowledges that tasks derive from public projects, so memorization cannot be ruled out; most tasks (56) allow only model API access during agent work, version-upgrade tasks also grade modified conformance tests with changed expected outputs, and optimization tasks generate fresh inputs at grading time

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Data format

**Size**：69 tasks and 574 steps (5 to 15 per task, median 8): 18 optimization, 18 feature implementation, 20 version upgrade and 13 migration tasks

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Question types**：Multi-step interactive software engineering, where the agent edits a codebase in a container and each step is checked by hidden tests

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Modalities**：Code and text

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Languages**：Nine programming languages: C/C++ (38 tasks), Rust (11), Java (6), Go (4), JavaScript (4), Python (3), PHP (2), Ruby (1); instructions are in English

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Difficulty**：Each step has a 2 to 4 hour budget and each task 10 to 60 hours (median 16); 38 tasks are not solved by any model

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Public and hidden split**：Tasks, environments and reference solutions are public in the repository; most graded tests for each step are hidden from the agent and differ from the public checks

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Evaluation

**Metrics**：Task solve rate (a task counts only if every step gets full credit), Pass@4 (share of tasks solved in at least one of four attempts) and share of steps passed

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Scoring**：Each step is graded by hidden tests in a separate verifier container; for optimization steps, full credit requires reaching the reference solution's speedup

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Prompt settings**：Each model runs in a Harbor-provided harness (Claude Code, Codex CLI, mini-swe-agent or Grok Build) at the highest reasoning effort that harness supports, four times per task

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Official scripts**：Run with Harbor, for example harbor run --path tasks --n-attempts 4; the repository notes that the task solve rate must be computed from all step rewards, since Harbor's mean reward is not the solve rate

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Comparability note**：Results reflect each model combined with its harness; the full-credit threshold for optimization steps is the reference solution's speedup, which need not be the best achievable

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Current status

**Checked on**：2026-11-12

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Latest data version**：The 69-task version described in paper v1 and the repository

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Paper revisions**：v1 submitted on 2026-11-04

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Saturation**：Far from saturated: the strongest model solves 18.5% of rollouts, and 38 of 69 tasks are unsolved by any model

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Contamination and disputes**：The limitations section notes that some tasks may still contain ambiguous requirements or verifier errors, that language coverage is uneven with C/C++ in 38 tasks, and that memorization cannot be ruled out because tasks derive from public projects. A check on simdutf found a median of 0.2% of added lines matching the corresponding upstream file verbatim

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Related benchmarks**：Unverified

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Leaderboard snapshot

**Snapshot date**：2026-11-12

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Official board**：https://multistepswe.com/#leaderboard

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Results snapshot**：Paper Table 5 (solve rate, %): Claude Opus 5.5 18.5 (Pass@4 31.9, steps passed 56.8); Claude Fable 5.1 17.8; Gemini 4 Argon 10.1; GPT-6.1 Sol 10.1; GPT-6 Astra 6.9; DeepSeek V4.1 Flash 6.5; Qwen 3.8 Max 4.0; MiMo 2.6 Pro 2.9; Grok 4.7 1.4

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Coverage note**：Results are the authors' own runs on nine models; the official website leaderboard is interactive

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Contact

**Public email**：Author emails listed in the paper: xiangkaiz@klavis.ai, zhengliu@klavis.ai, zihaolin@klavis.ai

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Code discussion**：https://github.com/Klavis-AI/Multi-step-SWE/issues

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Official social accounts**：Accounts listed on the maintainer Klavis AI website: X account @Klavis_AI (https://x.com/Klavis_AI); LinkedIn company page https://www.linkedin.com/company/klavis-ai/

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2611.07166

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Checksum**：dc939d8c5de5f1404e1db6e3921e1f92859d41a348fe84d7fec3831891e9ab75

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**File size**：422088

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

**Other documents**：https://multistepswe.com/paper.pdf

Sources: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (accessed 2026-11-12)

## Changelog

2026-11-12: Initial filing.

2026-11-14: Added the maintainer’s public social accounts.
