# PaperBenchX

Reproduction of key experiments from papers across electromagnetics, photonics, chemistry, materials, biology, and robotics.

## Basic information

**Short name**：PaperBenchX

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Full name**：PaperBenchX: Can AI Reproduce Science Across Disciplines?

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Version**：arXiv:2610.39744, submitted on 29 Oct 2026

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Paper version**：First arXiv version, submitted on 29 Oct 2026

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Release date**：2026-10-29

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Section**：General science

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Tags**：null

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**License**：MIT (code repository)

Sources: [1](https://github.com/UniPat-AI/PaperBenchX) (accessed 2026-11-10)

**Paper or report**：https://arxiv.org/abs/2610.39744

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Code**：https://github.com/UniPat-AI/PaperBenchX

Sources: [1](https://arxiv.org/abs/2610.39744); [2](https://github.com/UniPat-AI/PaperBenchX) (accessed 2026-11-08)

**Dataset**：https://github.com/UniPat-AI/PaperBenchX

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Homepage**：https://arxiv.org/abs/2610.39744

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Paper title**：PaperBenchX: Can AI Reproduce Science Across Disciplines?

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Origin and maintenance

**Initiators**：The paper’s listed affiliations include UniPat AI and Peking University.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Partners**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Authors**：Ruoyu Wu; Zengji Tu; Aolong Sun; Tianyi Ma; Junren Li; Xinbo Xu; Li Fu; Ziyan Zhang; Pinrui Huang; Xiaochen Wang; Chengda Wu; Yutao Zhou; Jianjun Wu; Lin Chang; Baobao Chang; Liang Chen; Kuan Li

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Maintainer**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Funders**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Design goals

**What it measures**：Turn a key experiment from a paper into a runnable workflow, then support the original scientific claim with evidence regenerated in a clean replay.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Gap in earlier benchmarks**：The paper says existing reproduction benchmarks focus mainly on AI and machine learning, where software stacks are relatively homogeneous. Cross-disciplinary reproduction also requires operating the scientific software of each field.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Construction

**Question sources**：93 expert-constructed tasks, each centered on a verifiable scientific claim from a published paper.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Who wrote the tasks**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Review**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Quality control**：Submitted workflows are replayed from scratch in a clean environment, and only regenerated evidence is scored against expert criteria.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Decontamination**：Apart from the representative tasks that are released, the remaining tasks are kept as a hidden evaluation set to reduce test-set contamination.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Data format

**Size**：93 tasks, across 12 research areas and 10 scientific computing environments.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Question types**：An agent must reconstruct the experiment, run and diagnose it, and deliver a runnable workflow.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Modalities**：The paper, a task specification, and a domain-native scientific computing environment.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Languages**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Difficulty**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Public and hidden split**：The paper releases one representative task from each of twelve research areas. Nine include redistributable environments. Three rely on commercially licensed software and release the task specification and scoring details, not the software environment.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Evaluation

**Metrics**：Full reproduction uses a 90% threshold. Mean rubric scores are also reported.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Scoring**：Only evidence regenerated in a clean replay is scored. A merely plausible final answer is not accepted.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Prompt settings**：The paper compares 10 frontier agent configurations.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Official scripts**：https://github.com/UniPat-AI/PaperBenchX

Sources: [1](https://arxiv.org/abs/2610.39744); [2](https://github.com/UniPat-AI/PaperBenchX) (accessed 2026-11-08)

**Comparability**：Both the 14% in the abstract and the 13 tasks in the body come from the paper’s own experiments.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Current status

**Date checked**：2026-11-08

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Latest data version**：The twelve-task public package described in the paper. The repository is UniPat-AI/PaperBenchX.

Sources: [1](https://arxiv.org/abs/2610.39744); [2](https://github.com/UniPat-AI/PaperBenchX) (accessed 2026-11-08)

**Paper revisions**：Only the version submitted on 29 Oct 2026 was checked.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Saturation**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Contamination and disputes**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Later benchmarks**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Leaderboard snapshot

**Snapshot date**：2026-10-29

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Official board**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Snapshot results**：The abstract says the best configuration fully reproduces only 14% of tasks under the 90% threshold, and mean rubric scores range from 27.53% to 59.08%.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Coverage note**：The figures come from the paper’s own experiments, not from an independent live board.

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Contact

**Public email**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Code discussion**：https://github.com/UniPat-AI/PaperBenchX

Sources: [1](https://github.com/UniPat-AI/PaperBenchX) (accessed 2026-11-08)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2610.39744

Sources: [1](https://arxiv.org/pdf/2610.39744) (accessed 2026-11-08)

**File checksum**：b3290184c24169a32b1439121cf800fca648bfde90a8422e34cba136defd1444

Sources: [1](https://arxiv.org/pdf/2610.39744) (accessed 2026-11-10)

**File size**：7384443

Sources: [1](https://arxiv.org/pdf/2610.39744) (accessed 2026-11-10)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

**Other files**：https://github.com/UniPat-AI/PaperBenchX

Sources: [1](https://arxiv.org/abs/2610.39744) (accessed 2026-11-08)

## Changelog

2026-11-08: First filing.
