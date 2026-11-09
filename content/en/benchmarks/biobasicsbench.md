# BioBasicsBench

Measures whether agents can interpret raw data from routine wet-lab work, identify errors, and recognize when the evidence cannot support a conclusion.

## Basic information

**Short name**：BioBasicsBench

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Full name**：BioBasicsBench

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Version**：The version described on the official page dated 6 Nov 2026

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Paper version**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Release date**：2026-11-06

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Section**：Biology and medicine

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Tags**：null

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**License**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Paper or report**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Code**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Dataset**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Homepage**：https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Paper title**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Origin and maintenance

**Initiators**：OpenAI and Ligo. The page describes Ligo as a biotechnology company focused on enzyme design.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Partners**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Authors**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Maintainer**：OpenAI

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Funders**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Design goals

**What it measures**：Interpret raw experimental data, identify errors, and judge whether the evidence can support a conclusion.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Gap in earlier benchmarks**：The page says benchmarks built from charts and images selected for papers can miss failed experiments, ambiguous images, and conflicting observations in wet-lab work.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Construction

**Question sources**：Scientists created the tasks from data in their own experiments and wrote grading criteria for each question.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Who wrote the tasks**：The tasks were written by scientists. External review was done by a PhD-level scientist working in a wet lab.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Review**：Each task had an internal review by a Ligo scientist who had not written it, an external review by a PhD-level wet-lab scientist, and a final internal review.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Quality control**：Reviewers checked the prompt, the experimental evidence, the rubric, the author notes, and a graded model attempt.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Decontamination**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Data format

**Size**：100 tasks, in protein methods, imaging and cytometry, quantification and assays, nucleic acid methods, and molecular cloning.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Question types**：Agents return a structured answer with the requested conclusion, measurement, or recommendation, and supporting reasoning where required.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Modalities**：Raw evidence such as gel and blot images, plate photographs, microscopy stacks, sequencing reads, plate-reader exports, and videos of bench work.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Languages**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Difficulty**：Tasks range from reading the molecular weight of a DNA sample in a gel to detailed assay analysis. The page says all of them are routine work a wet-lab scientist should be able to complete reliably.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Public and hidden split**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Evaluation

**Metrics**：Mean reward, the average task score as a percentage of the available credit.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Scoring**：Credit is assigned against individual rubric criteria, so a correct conclusion can be distinguished from a partly correct analysis.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Prompt settings**：The page reports seven models and 37 model and reasoning-effort settings, with five attempts on each of the 100 tasks per setting.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Official scripts**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Comparability**：The scores on the page are reported by OpenAI, not by an independent re-evaluation.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Current status

**Date checked**：2026-11-08

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Latest data version**：The version described on the official page dated 6 Nov 2026

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Paper revisions**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Saturation**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Contamination and disputes**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Later benchmarks**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Leaderboard snapshot

**Snapshot date**：2026-11-06

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Official board**：https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Third-party board**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Snapshot results**：In the xhigh table on the page, GPT-6 Astra has a mean reward of 66.7% and GPT-5.6 Sol has 43.8%.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Coverage note**：These are results the vendor reports on its own page.

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Contact

**Public email**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Code discussion**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Official social accounts**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Privacy policy**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Original files

**Paper PDF**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**File checksum**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**File size**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Folder**：Unverified

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

**Other files**：https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

Sources: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (accessed 2026-11-08)

## Changelog

2026-11-08: First filing.
