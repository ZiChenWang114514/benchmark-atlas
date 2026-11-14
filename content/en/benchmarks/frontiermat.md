# FrontierMat

FrontierMat comprises 330 multiple-choice problems from frontier academic and industrial materials R&D; the paper reports that the strongest general-purpose model, GPT-6-Astra, scores 53.7% overall, and that domain adaptation raises open-weight Qwen3.5-35B-A3B from 36.7% to 55.4%.

## Basic information

**Short name**：FrontierMat

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Full name**：FrontierMat: a language-model benchmark for problems at the frontier of materials R&D

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Version**：arXiv:2610.41162v1; 330 multiple-choice problems (98 single-answer, 232 multi-answer)

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Paper version**：arXiv:2610.41162v1 (2026-10-30)

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Release date**：2026-10-30

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Section**：Materials

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Tags**：Frontier materials R&D; Cross-scale reasoning; Composite materials; Multiple-choice evaluation

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**License**：The paper is released on arXiv under the arXiv non-exclusive distribution license. The license for the problem data and any code is unverified. The ethics section states that FrontierMat is intended for research evaluation, but it does not name a dataset or code license.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Paper or report**：https://arxiv.org/abs/2610.41162

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Code**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Dataset**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Homepage**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Paper title**：FrontierMat: Benchmarking Language Models at the Frontier of Materials R&D

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Origin and maintenance

**Initiators**：Nanyang Technological University (affiliations of the corresponding authors)

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Partners**：Peking University, Shanghai Jiao Tong University, Xi'an Jiaotong University, Wuhan University of Technology, Beihang University, Eighth Research Institute of Nuclear Industry, CNNC, Harbin Institute of Technology, Tsinghua University, University of Science and Technology of China, Commercial Aircraft Corporation of China (COMAC), Tongji University, Northwestern Polytechnical University, and Wanhua Chemical Group Co., Ltd. (from the paper affiliations)

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Authors**：Equal-contribution authors Feng Chen, Jianguo Huang, Yushan Xiao, Yue Li, and Bijun Tang; additional authors Xuyu Dong, Xingguo Wang, Feiyang Xie, Jianhui Gu, Bo An, and Zheng Liu; authors from Dongfeng Cao through Xitao Zheng (Dongfeng Cao, Hongda Chen, Yongji Gong, Ruiqi Li, Shuxin Li, Xingji Li, Ruitao Lv, Li Song, Lei Wang, Ye Zhang, Xiaoxu Zhao, and Xitao Zheng) contributed as expert reviewers from academia and industry. Correspondence emails printed on the first page are feng012@e.ntu.edu.sg, boan@ntu.edu.sg, and Z.Liu@ntu.edu.sg.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Maintainer**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Funders**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Design goals

**Capabilities tested**：Tests whether language models can infer a withheld experimental outcome or draw a conclusion from selected evidence about a real materials study, with annotations for functional domain, material system, and the scale of the governing mechanism (micro, meso, macro, or cross-scale).

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Gap in prior benchmarks**：The paper argues that existing materials benchmarks mainly use examinations, textbooks, or model-generated items from existing text, and do not systematically combine problems from active R&D, answers that are research outcomes, and annotations of the mechanisms that link atomic structure to component performance.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Construction

**Question sources**：Problems are drawn from recent work by academic laboratories and industrial R&D teams at the research frontier, including results not yet published, and from experimental studies in specialist journals across aerospace, semiconductors, embodied intelligence, and nuclear fusion. The appendix reports screening 25,182 journal articles published in 2022–2026, retaining 2,186 as sources after title, abstract, and full-text review. Thirteen R&D groups participated (9 academic and 4 industrial or national-laboratory); their identities are withheld for anonymous review. Published sources span 1998–2026.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Author background**：Corresponding authors are affiliated with Nanyang Technological University. Annotators with graduate training in materials science wrote problems under shared guidelines. Leading experimentalists and industry experts reviewed every problem in their field; experts familiar with the originating work reviewed problems drawn from partner research. In the author list, contributors from Dongfeng Cao through Xitao Zheng are marked as expert reviewers from academia and industry.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Review process**：Verification proceeds in two stages: two language models independently check each problem for consistency with its source, then leading experimentalists and industry experts review every problem in their field for relevance, significance of the withheld outcome, and whether distractors represent plausible mistakes by a competent researcher. Experts marked each problem Approve, Revise, or Reject and provided comments. Problems that failed any criterion were revised or removed. The problem set, options, and answers were frozen before any model evaluation.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Quality control**：Annotators record the source evidence for each answer and withhold the answer and its evidence locator from the model. Values read from plots are marked together with the reading resolution, and numerical options differ by more than this resolution. If a source's summary statistic differs from its underlying values, the answer is recomputed from the values given in the prompt and documented. Two language models were used to cross-check problems against their sources.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Decontamination**：Evaluation is closed-book: each model receives only the study setting, candidate options, and required answer format. Answers, sources, and other problems are withheld, and tools are disabled unless stated otherwise. Some problems are grounded in partner research that is not yet published. The paper does not describe a dedicated decontamination procedure against pretraining corpora.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Data format

**Size**：330 multiple-choice problems, of which 98 are single-answer and 232 are multi-answer. By scale there are 200 single-scale problems (88 micro, 24 meso, 88 macro) and 130 cross-scale problems. Table 2 also splits problems into 159 structural (mechanical, protective) and 171 functional (thermal, electrical, electromagnetic, multifunctional trade-off) items. Sources include 13 partner R&D groups (9 academic, 4 industrial or national-laboratory). Mechanical problems form the largest functional domain (the paper states 40%).

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Question types**：All items are multiple choice, either single-answer or multi-answer. Distractors differ from the supported result in direction, magnitude, or mechanism. Some problems require quantitative derivation rather than prediction of an unreported measurement.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Modalities**：Evaluation prompts are English text; the paper does not state whether official items include images. The running example uses a braid schematic to illustrate cross-scale reasoning.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Languages**：English (the appendix states that models receive each problem in English with no few-shot examples)

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Difficulty**：The paper states that half of the problems are solved by at most one model, and that 129 problems are solved by no general-purpose model; 39% of problems were unsolved by any general-purpose model in the analysis. With answer format and construction channel held fixed, cross-scale problems score 8.7 points below single-scale problems.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Public and hidden split**：The paper does not describe a public versus hidden split. The problem set was frozen before model evaluation. Sources include unpublished results, and partner-group identities were withheld during review. Whether the dataset has been publicly released is unverified.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Evaluation

**Metrics**：A response scores 1 if its predicted option set matches the gold set, 0.5 if it is a non-empty proper subset of the gold set, and 0 if it contains any wrong option; single-answer problems are therefore scored 1 or 0. Unparseable outputs score 0. Mean scores are reported as percentages.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Scoring**：The final “Answer:” line is parsed, duplicate letters are removed, and remaining letters are sorted. The paper reports 95% confidence intervals from 10,000 bootstrap resamples of problems and compares models with paired permutation tests; differences that are not significant at p < 0.05 are reported as unresolved. Scores for the official Qwen release and FrontierMat-Model are means over 16 samples per problem.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Prompt settings**：Closed-book evaluation with no few-shot examples and, by default, no tools. Single-answer prompts end with “End with exactly: Answer: <letter>.”; multi-answer prompts ask for all correct letters in alphabetical order. Each model uses the highest reasoning setting it offers: xhigh for GPT-6-Astra and GPT-6-Sol, extended thinking (max) for Claude Opus 5.5, and thinking mode for DeepSeek V4 Pro, GLM-5.3, and both Qwen variants. FrontierMat-Model uses temperature 0.6, top-p 0.95, and at most 32k output tokens, with the same prompts and decoding as official Qwen3.5-35B-A3B.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Official scripts**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Comparability note**：The scores below are author-reported in the paper. No official evaluation scripts or public problem release were found, so the results should not be treated as third-party reproductions. The two Qwen rows are means over 16 samples; the cross-scale and single-scale columns differ in answer format and construction channel, and the controlled comparison is in Section 5.2 of the paper.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Current status

**Checked on**：2026-11-14

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Latest data version**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Paper revisions**：Only arXiv v1 is available; it was submitted on 2026-10-30.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Saturation**：The paper states that the strongest general-purpose model achieves barely half the available score, leaving substantial room for improvement, and that 39% of problems were unsolved by any general-purpose model in the analysis. GPT-6-Astra scores 53.7% overall (95% CI 48.9–58.4).

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Contamination and disputes**：Answers are taken from source studies and may reflect errors in the original findings; some reported values are read from published plots. Problems paraphrase research settings and reproduce a small number of reported values; the paper states that no figures or text are copied. Some sources are unpublished. The paper does not report a pretraining-leakage audit.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Related benchmarks**：The paper introduces FrontierMat-Model, a domain-adapted Qwen3.5-35B-A3B guided by the benchmark; that is a model, not a derived benchmark. Whether any derived benchmarks exist is unverified.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Leaderboard snapshot

**Snapshot date**：2026-11-14

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Official board**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Third-party board**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Results snapshot**：Paper Table 2 (scoring rule in §4.1; scores in percent; the Reasoning column is the highest reasoning setting each model offers). General-purpose models: GPT-6-Astra (xhigh) overall 53.7, micro 51.1, meso 47.9, macro 39.2, cross-scale 66.3, structural 55.1, functional 52.3; GPT-6-Sol (xhigh) overall 51.4, micro 48.3, meso 50.0, macro 34.1, cross-scale 65.4, structural 50.0, functional 52.6; Claude Opus 5.5 (max) overall 47.3, micro 43.2, meso 35.4, macro 27.3, cross-scale 65.8, structural 47.8, functional 46.8; DeepSeek V4 Pro (thinking) overall 47.6, micro 52.3, meso 27.1, macro 27.8, cross-scale 61.5, structural 49.1, functional 46.2; GLM-5.3 (thinking) overall 45.0, micro 43.8, meso 31.2, macro 23.9, cross-scale 62.7, structural 45.3, functional 44.7. Official post-trained Qwen3.5-35B-A3B (thinking; mean over 16 samples) overall 36.7, micro 30.3, meso 22.0, macro 23.8, cross-scale 52.4, structural 35.7, functional 37.6; the authors' domain-adapted FrontierMat-Model overall 55.4, micro 57.5, meso 35.3, macro 41.6, cross-scale 67.1, structural 57.3, functional 53.7, a gain of 18.7 points overall versus the official release. The paper states that the strongest general-purpose model, GPT-6-Astra, scores 53.7% (95% CI 48.9–58.4), significantly ahead of DeepSeek V4 Pro (47.6%) and GLM-5.3 (45.0%); on matched problems, the cross-scale score is 8.7 points below single-scale problems (stratified permutation test, one-sided p = 0.008). Per-domain scores are in Table 8. All of these scores are author-reported in the paper.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Coverage note**：All models are evaluated on the full set of 330 problems. The paper states that application fields and functional domains are unevenly represented, with composites over-represented among material systems, and that results are reported by domain and scale without claiming uniform coverage of the field. Raw cross-scale scores are higher because these problems are more often single-answer and because one construction channel contributes only cross-scale problems, so those columns should not be compared directly with single-scale columns.

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Contact

**Public email**：feng012@e.ntu.edu.sg, boan@ntu.edu.sg, and Z.Liu@ntu.edu.sg (correspondence addresses printed on the paper's first page)

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Code discussion**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Official social accounts**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Privacy policy**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Original files

**Paper PDF**：https://arxiv.org/pdf/2610.41162.pdf

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Checksum**：9ce0d433cf7ddb9f9b35f64afea605b40deedc350791c319ba95d1e4ee832d84

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**File size**：794853

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Folder**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

**Other documents**：Unverified

Sources: [1](https://arxiv.org/abs/2610.41162) [2](https://arxiv.org/pdf/2610.41162.pdf) (accessed 2026-11-14)

## Changelog

2026-11-14: Initial filing.
