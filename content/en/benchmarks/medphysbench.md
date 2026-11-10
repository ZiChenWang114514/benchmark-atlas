# MedPhysBench

A medical physics benchmark of calculations and peer checks graded against protocol code, spanning radiotherapy, imaging, nuclear medicine and radiation protection.

## Basic information

**Short name**：MedPhysBench

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Full name**：MedPhysBench

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Version**：v1.0 (Prime Intellect Environments Hub environment omar/medphysbench 1.0.1)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Paper version**：arXiv:2611.05340v1 (2026-11-03)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Release date**：2026-11-03

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Section**：Physics

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Tags**：Medical physics; Radiation therapy; Dose calculation; Error detection

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**License**：MIT for the code repository

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Paper or report**：https://arxiv.org/abs/2611.05340

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Code**：https://github.com/onusrat/medphysbench

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Dataset**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Homepage**：https://github.com/onusrat/medphysbench

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Paper title**：MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Origin and maintenance

**Initiators**：Omar Nusrat (Department of Physics, Toronto Metropolitan University; iBEST, St. Michael's Hospital)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Partners**：Prime Intellect (hosts the environment and provided the inference and evaluation platform)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Authors**：Omar Nusrat

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Maintainer**：Omar Nusrat

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Funders**：Prime Intellect provided platform credits and compute through its RL Residency

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Design goals

**Capabilities tested**：Tests whether language models can perform medical physics calculations and check a colleague's calculation for errors, across radiation therapy, diagnostic imaging, nuclear medicine and radiation protection

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Gap in prior benchmarks**：The paper notes that prior evaluations in the field mostly use multiple-choice exams or open-ended ratings, and none grade a computed quantity with its unit or a peer check

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Construction

**Question sources**：Ten seeded generators produce items from protocols such as TG-51, TG-71, TG-43U1 and NCRP 151, with reference answers computed by code implementing each protocol

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Author background**：Medical physics researcher

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Review process**：Before freezing, every solver was cross-checked against an independent second implementation and a development-split pilot on four models was traced by hand; the author states a blinded review by external medical physicists is planned

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Quality control**：The two implementations agreed within a relative difference of 1.3×10⁻¹⁵ on 60,000 items; tolerance bands come from an empirical sensitivity analysis; after the runs the code was compared with published worked examples and the shielding items were read against NCRP Report 151

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Decontamination**：Test seeds are derived from an unpublished key via HMAC-SHA256, every item carries a canary string, and a hash commitment to the test parameters is published

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Data format

**Size**：Test split of 1,200 items (600 calculation, 300 worksheet-check and 300 result-check items); public development split of 600 items

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Question types**：Numerical calculations with units; worksheet checks (verdict and first wrong step); result checks

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Modalities**：Text only

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Languages**：English

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Difficulty**：Three levels, with level 3 being complete clinical hand calculations such as a TG-51 calibration worksheet and an isocentric MU calculation

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Public and hidden split**：The development split is public; the test split can only be generated with the key and is scored by the author on request

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Evaluation

**Metrics**：Share of calculations within tolerance; detection rate, false-alarm rate and Youden's J for checking items

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Scoring**：Deterministic grading with no model judge: the last boxed answer is parsed, converted with pint, and accepted within a relative band of 0.5% to 2%

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Prompt settings**：Provider default temperature and reasoning settings, no tools, up to 32,768 output tokens, one answer per item

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Official scripts**：https://github.com/onusrat/medphysbench

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Comparability note**：Some models answered only a pre-specified stratified half of the test split; the paper discloses two issues in the NCRP 151 items that affect a small number of level-3 shielding items

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Current status

**Checked on**：2026-11-10

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Latest data version**：v1.0 (environment version 1.0.1)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Paper revisions**：v1 (2026-11-03)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Saturation**：The calculation task is near saturation for the top four models (99.3% to 100.0%)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Contamination and disputes**：The paper self-reports that the NCRP 151 shielding items depart from the report on the two-source rule and the patient-scatter use factor, to be corrected in version 1.1; seven result-check items also changed which quantity is reported and remain in the main analysis

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Related benchmarks**：The author's earlier multiple-choice benchmark omar/medphysbench-kq (no shared items)

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Leaderboard snapshot

**Snapshot date**：2026-11-10

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Official board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Results snapshot**：Paper Table 2 calculation accuracy: GPT-6 Astra 100.0% (half split), GPT-6.1 Sol 99.7%, Gemini 4 Argon 99.5%, Claude Opus 5.5 99.3%, Claude Sonnet 5.5 93.7%, Gemma 3 27B 33.3%

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Coverage note**：Results from the paper, covering 12 models

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Contact

**Public email**：omar.nusrat@torontomu.ca

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Code discussion**：https://github.com/onusrat/medphysbench/issues

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2611.05340v1

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Checksum**：dfdd0079dc599d9c4d71e0b2d9ef52d02661eabcef118cc3f8d31c4592f90456

Sources: [1](https://arxiv.org/pdf/2611.05340v1) (accessed 2026-11-10)

**File size**：1129352

Sources: [1](https://arxiv.org/pdf/2611.05340v1) (accessed 2026-11-10)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

**Other documents**：Unverified

Sources: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (accessed 2026-11-10)

## Changelog

2026-11-10: Initial filing.
