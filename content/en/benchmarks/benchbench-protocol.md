# BenchBench-Protocol

Recovers 149 protocol-modification tasks from real scientist edits to published protocols across nine wet-lab biology domains; Claude Opus 5 leads at about 59.2% normalized rubric score.

## Basic information

**Short name**：BenchBench-Protocol

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Full name**：BenchBench-Protocol: Evaluating Real-World Wet-Lab Protocol Reasoning and Modification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Version**：149 tasks from 96 source protocols

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Paper version**：arXiv:2608.23898v1 (2026-08-24)

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Release date**：2026-08-24

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Section**：Biology and medicine

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Tags**：wet lab; protocol modification; open-ended response; scoring rubrics

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**License**：Pending verification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Paper or report**：https://arxiv.org/abs/2608.23898

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Code**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Dataset**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Homepage**：https://www.benchling.com/blog/can-llms-work-in-the-wet-lab

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Paper title**：BenchBench-Protocol: Evaluating Real-World Wet-Lab Protocol Reasoning and Modification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Origin and maintenance

**Initiators**：Released by the Benchling team.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Partners**：All listed authors are affiliated with Benchling.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Authors**：Aditya Sivakumar, Ashu Singhal, Nicholas Larus-Stone, and Nithin Parsan (corresponding author and team lead).

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Maintainer**：Benchling

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Funders**：Pending verification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Design goals

**Capabilities tested**：Tests whether models can adapt or extend published wet-lab protocols under real experimental constraints while tracking upstream and downstream dependencies.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Gap in prior benchmarks**：Recent life-science benchmarks often use expert-authored tasks; real protocol edits are constrained by reagents, instruments, and prior results, so the task distribution may differ.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Construction

**Question sources**：Tasks and weighted rubrics are recovered from differences between published protocols and scientist-adapted versions on Benchling, spanning 96 source protocols and nine wet-lab biology domains.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Author background**：Authors are from Benchling; tasks were reviewed by scientists with a PhD in a relevant field and at least three years of bench experience.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Review process**：Each task and rubric was independently reviewed by multiple domain scientists; only highly rated tasks were retained.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Quality control**：Tasks and weighted rubrics are grounded in real modification differences and expert quality control.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Decontamination**：Pending verification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Data format

**Size**：149 expert-reviewed protocol-modification tasks across nine wet-lab biology domains from 96 protocols.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Question types**：Open-ended free-response tasks phrased as a scientist would ask an LLM.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Modalities**：Text protocols and modification prompts.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Languages**：Paper and tasks are primarily in English.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Difficulty**：Among nine models, Claude Opus 5 leads at about 59.2%, with others between about 34.1% and 47.1%; best-of-ten remains unsaturated.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Public and hidden split**：Paper discloses construction and results; a fully public dataset link is pending verification.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Evaluation

**Metrics**：Normalized weighted rubric score.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Scoring**：Open-ended responses are scored with expert-verified weighted rubrics grounded in real modifications.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Prompt settings**：Nine closed and open models are evaluated; best-of-ten attempts remain unsaturated per the paper.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Official scripts**：Pending verification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Comparability note**：Scores come from the authors' paper, not independent third-party reruns; tasks are based on real Benchling platform edits.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Current status

**Checked on**：2026-11-10

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Latest data version**：149 tasks as reported in arXiv:2608.23898v1.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Paper revisions**：arXiv:2608.23898v1, 2026-08-24.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Saturation**：Not saturated. Claude Opus 5 about 59.2%; best-of-ten still unsaturated.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Contamination and disputes**：Pending verification

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Related benchmarks**：Comparable wet-lab protocol benchmarks include AISLE, LAB-Bench, BioProBench, BioBasicsBench, and Gamow LabBench.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Leaderboard snapshot

**Snapshot date**：2026-11-10

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Official board**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Third-party board**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Results snapshot**：Authors evaluate nine models: Claude Opus 5 about 59.2% normalized rubric score; others about 34.1% to 47.1%.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Coverage note**：Summarizes public figures from the paper only; evaluation was not rerun.

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Contact

**Public email**：nithin.parsan@benchling.com

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Code discussion**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Official social accounts**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Privacy policy**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2608.23898

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Checksum**：34c7a9382e4d8690f639194a05c8b8427121f59131665f0347a2f316195efc68

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**File size**：1725774

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Folder**：Not public

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

**Other documents**：https://arxiv.org/abs/2608.23898; https://www.benchling.com/blog/can-llms-work-in-the-wet-lab

Sources: [1](https://arxiv.org/abs/2608.23898) [2](https://www.benchling.com/blog/can-llms-work-in-the-wet-lab) [3](https://arxiv.org/pdf/2608.23898) (accessed 2026-11-10)

## Changelog

2026-11-10: Initial filing.
