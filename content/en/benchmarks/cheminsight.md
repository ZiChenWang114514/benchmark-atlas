# ChemInsight

A diagnostic chemistry reasoning benchmark focused on organic chemistry, with 203 free-form questions in 50 bundles plus 50 single-step diagnosis questions, using scope and depth scores to separate coverage from multi-step completeness.

## Basic information

**Short name**：ChemInsight

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Full name**：ChemInsight: A Comprehensive Benchmark for Evaluating and Diagnosing Chemistry Understanding and Reasoning in Large Language Models

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Version**：arXiv:2611.11794v1; a 203-question benchmark set in 50 bundles plus a 50-question diagnosis set

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Paper version**：arXiv:2611.11794v1 (2026-11-09)

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Release date**：2026-11-09

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Section**：Chemistry

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Tags**：Organic chemistry reasoning; SMILES structure understanding; Multi-step reasoning; Diagnostic evaluation

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**License**：The paper is distributed on arXiv under the arXiv non-exclusive distribution license; no license has been published for the question data

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Paper or report**：https://arxiv.org/abs/2611.11794

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Code**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Dataset**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Homepage**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Paper title**：ChemInsight: A Comprehensive Benchmark for Evaluating and Diagnosing Chemistry Understanding and Reasoning in Large Language Models

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Origin and maintenance

**Initiators**：Ant Group and Peking University

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Partners**：University of Electronic Science and Technology of China, Westlake University and Peking University Health Science Center (per the author affiliations)

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Authors**：Equal-contribution authors Changyu Hu, Yiming Zou and Xin Tang; other authors Yiru Pan, Zicheng Huang, Deng Zhao and Qing Cui; corresponding authors Zhenduo Zhang, Wang Ren and Xiao Li

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Maintainer**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Funders**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Design goals

**Capabilities tested**：Chemistry tasks that need multi-step reasoning and structured chemical understanding, across six ability dimensions: reaction-type recognition, structure generation in context, calculation and counting, structure-property reasoning, selectivity prediction, and spatial and three-dimensional thinking

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Gap in prior benchmarks**：The paper argues that existing chemistry benchmarks usually report a single score, which hides the specific bottlenecks behind weak model performance and gives little guidance for targeted improvement

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Construction

**Question sources**：The benchmark set consists of original, search-resistant questions focused mainly on organic chemistry. The design standard requires questions to challenge chemistry majors and to have answers that cannot be retrieved directly from chemistry databases such as SciFinder or Reaxys or from search engines

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Author background**：The paper defines domain experts as chemistry majors at top-ranked universities; the three equal-contribution authors did this work during internships at Ant Group

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Review process**：Both the benchmark set and the diagnosis set were created independently and cross-validated by domain experts for correctness, clarity and appropriate difficulty

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Quality control**：SMILES answers are canonicalized with RDKit and checked for exact matches; short answers are graded by an LLM judge with a structured prompt that first enforces special rules and keyword matching, then applies a three-level rubric (full, partial, zero credit) with an anti-hallucination constraint

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Decontamination**：The paper does not describe a dedicated decontamination procedure; the design requires that answers cannot be retrieved directly from chemistry databases or search engines

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Data format

**Size**：The benchmark set has 203 questions in 50 bundles worth 262 points, of which 23 are essence bundles with linked questions of increasing difficulty. The diagnosis set has 50 single-step questions: 30 on structure recognition and 20 on structure-property reasoning

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Question types**：All free-form answers with no multiple-choice items; answer formats are natural-language text, chemical formulas and SMILES structures

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Modalities**：Text and symbolic notations such as SMILES (no images)

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Languages**：English (per the appendix examples in the paper)

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Difficulty**：Questions carry expert-assigned easy, medium and hard labels; Figure 3 of the paper shows scores falling as difficulty rises

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Public and hidden split**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Evaluation

**Metrics**：A scope score (share of benchmark-set points, normalized by 262) and a depth score (rewarding fully solved essence bundles, normalized by 524), plus per-dimension scores and diagnosis-set accuracy

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Scoring**：Hybrid scoring: SMILES questions are matched exactly after RDKit canonicalization and short answers are graded by an LLM judge; each question score is the mean of eight independent samples

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Prompt settings**：A task-specific structured prompt (full text in Appendix B); eight independent samples per question per model; eight models run in thinking mode, while Ling-1T and DeepSeek-V3.1 run in non-thinking mode

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Official scripts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Comparability note**：LLM-judge grading of open-ended answers is uncertain, and correct reasoning that departs from the reference may be misgraded; scope and depth use different normalizers, and their sum is not capped at 100

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Current status

**Checked on**：2026-11-12

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Latest data version**：The version described in paper v1: 203 benchmark-set questions and 50 diagnosis-set questions

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Paper revisions**：v1 submitted on 2026-11-09

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Saturation**：Far from saturated: the paper reports scope scores of 11.6% to 27.8% and depth scores of 2.3% to 10.7% across ten models, against a human-expert scope score of 36.3%

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Contamination and disputes**：The limitations section notes that the benchmark covers only text and symbolic modalities, leaving out visual tasks such as NMR spectrum reading, and that LLM-judge grading carries uncertainty

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Related benchmarks**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Leaderboard snapshot

**Snapshot date**：2026-11-12

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Official board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Results snapshot**：Paper Table 1 (mean of eight runs): Gemini 3 Pro scope 0.278, depth 0.107; GPT-5 scope 0.215, depth 0.069; Gemini 2.5 Pro scope 0.212, depth 0.059; DeepSeek-V3.2-Speciale scope 0.208, depth 0.067; DeepSeek-V3.2 scope 0.181, depth 0.047; DeepSeek-V3.1 (non-thinking) scope 0.116, depth 0.024; human experts scope 36.3%

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Coverage note**：All results are the authors' own runs on ten models. On the diagnosis set, reasoning models reach about 90% on property prediction, common-name-to-SMILES accuracy ranges from 29.4% to 56.6%, and variation on SMILES questions explains about 82% of the variance in the overall score

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Contact

**Public email**：Corresponding-author emails listed in the paper: zhenduo.zzd@antgroup.com, renwang.rw@antgroup.com, xiaoli@pku.edu.cn

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Code discussion**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2611.11794

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Checksum**：5ff70b40e7eec1907cb9c4a06dde7b9bc6f0182076701965907ae0d330ca4a11

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**File size**：1580645

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

**Other documents**：Unverified

Sources: [1](https://arxiv.org/abs/2611.11794) [2](https://arxiv.org/pdf/2611.11794) (accessed 2026-11-12)

## Changelog

2026-11-12: Initial filing.
