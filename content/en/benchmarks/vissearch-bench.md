# VisSearch-Bench

Tests how multimodal agents organize and connect visual evidence during long-horizon open-web search.

## Basic information

**Short name**：VisSearch-Bench

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Full name**：VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Version**：arXiv:2611.04894, submitted on 3 Nov 2026

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Paper version**：First arXiv version, submitted on 3 Nov 2026

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Release date**：2026-11-03

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Section**：Multimodal

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Tags**：null

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**License**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Paper or report**：https://arxiv.org/abs/2611.04894

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Code**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Dataset**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Homepage**：https://arxiv.org/abs/2611.04894

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Paper title**：VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Origin and maintenance

**Initiators**：The paper lists Tsinghua University, Ant Group, and Renmin University of China.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Partners**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Authors**：ZhengXian Wu; Qianhao Nie; Zhuohong Chen; Junjie Gao; Yuyao Zhang; Yunyao Yu; Hangrui Xu; Cheng Cheng; Guiyu Ma; Jin Zhang; Xingzhong Xu; Kai Yang; Haoqian Wang

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Maintainer**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Funders**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Design goals

**What it measures**：Organize visual information during long-horizon open-web search, and connect images, objects, and later search steps.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Gap in earlier benchmarks**：The paper says some search tasks use an image mainly to identify an initial entity and then rely on text retrieval, so they do not show how an agent connects evidence across images.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Construction

**Question sources**：People wrote the tasks from public, searchable sources. They gathered images, entity relationships, and facts, then wrote a reference answer and the supporting evidence.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Who wrote the tasks**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Review**：Automated checks and human review examine whether sources are accessible, whether answers are consistent, and whether a shortcut bypasses the intended visual requirements.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Quality control**：Each task has a reference answer, traceable evidence, and scoring rules.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Decontamination**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Data format

**Size**：204 human-written tasks, across 7 main domains and 25 subdomains.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Question types**：Set-wise visual search, sequential visual search, hybrid wide-deep search, competitive visual disambiguation, and visual-structure-guided search.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Modalities**：Images and open-web search.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Languages**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Difficulty**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Public and hidden split**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Evaluation

**Metrics**：Accuracy measures whether the full answer meets the task. Process Score measures individual results and subquestion answers.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Scoring**：Accuracy measures complete task success.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Prompt settings**：The paper compares 16 multimodal models, including direct answering and the use of search tools.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Official scripts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Comparability**：The figure of 26.47% comes from the paper’s own experiments, not from an independent live board.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Current status

**Date checked**：2026-11-08

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Latest data version**：arXiv:2611.04894, submitted on 3 Nov 2026

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Paper revisions**：Only the version submitted on 3 Nov 2026 was checked.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Saturation**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Contamination and disputes**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Later benchmarks**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Leaderboard snapshot

**Snapshot date**：2026-11-03

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Official board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Snapshot results**：The paper reports that the best system fully solves only 26.47% of the tasks, even with search tools.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Coverage note**：The figure comes from the paper’s own experiments, not from an independent live board.

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Contact

**Public email**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Code discussion**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2611.04894

Sources: [1](https://arxiv.org/pdf/2611.04894) (accessed 2026-11-08)

**File checksum**：Unverified

Sources: [1](https://arxiv.org/pdf/2611.04894) (accessed 2026-11-08)

**File size**：Unverified

Sources: [1](https://arxiv.org/pdf/2611.04894) (accessed 2026-11-08)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

**Other files**：Unverified

Sources: [1](https://arxiv.org/abs/2611.04894) (accessed 2026-11-08)

## Changelog

2026-11-08: First filing.
