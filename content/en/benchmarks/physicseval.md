# PhysicsEval

> Benchmark Constitution, verification 2026-11-08. Unknowns remain "Unverified"; an access date is not an experiment date.

PhysicsEval provides both a set of worked physics problems drawn from textbooks and experiments on strategy at reasoning time, and it uses the Physics Proficiency Score to judge the quality of the whole solution rather than only checking the answer. The final PPS judge and the verifier at reasoning time are two kinds of role, and their weights also differ; conflicts in the difficulty boundaries and in the normalization wording of the original paper are kept here.

Source: [Original description](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08); [Result evidence](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08)

## Basic information

### Short name

PhysicsEval

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Full name

PhysicsEval

Note: The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Benchmark version

Unverified

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Paper version

arXiv v2

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Release date

2025/07/31

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Section

Physics

Note: Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， )

### Field tags

- 物理

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 许可与适用范围

Data CC-BY-SA-4.0 (as stated on the official dataset card; third-party rights in the original content of the textbooks and the websites require a separate review).

Sources: [1](https://huggingface.co/datasets/IUTVanguard/PhysicsEval/raw/main/README.md) (accessed 2026-11-08， )

### Paper

https://arxiv.org/abs/2508.00079

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Code repository

https://github.com/areebuzair/PhysicsEval

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 数据地址

https://huggingface.co/datasets/IUTVanguard/PhysicsEval

Sources: [1](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

### Official homepage

https://github.com/areebuzair/PhysicsEval

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Paper title

PhysicsEval: Inference-Time Techniques to Improve the Reasoning Proficiency of Large Language Models on Physics Problems

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Origin and maintenance

### 发起与机构归属

Islamic University of Technology, Bangladesh, Systems and Software Lab

Note: Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 合作关系

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Authors

- Siddique, Oshayer
- Alam, J. M Areeb Uzair
- Rafy, Md Jobayer Rahman
- Raiyan, Syed Rifat
- Mahmud, Hasan
- Hasan, Md Kamrul

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Current maintainer

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 资助与支持

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Design goals

### Abilities measured

Compare large models' ability to handle mathematical and descriptive physics problems, and study inference-time computation and multi-agent verification.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 设计背景与适用边界

Checking only the final number makes it hard to judge physical principles, logic, and whether the solution is complete; this work also releases a set of problems and solutions that can be used for training and for evaluation, and it compares several strategies of self-checking at inference time and of external feedback, measuring them by PPS rather than by binary accuracy.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Construction

### 题目或数据来源

The questions come from physics textbooks; the corresponding solutions were collected from physics forums and educational websites.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 构建者背景

The authors are from the Systems and Software Lab in the Department of Computer Science and Engineering at IUT; the questions come from existing physics textbooks and from solutions on expert and education forums. The author team is not described as an independent team of physics experts annotating every question. The PPS weights were consulted with two high-school physics teachers and one scorer of a university entrance examination.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Review process

Human-written questions from textbooks, and solutions from the web, are collected first, and Gemini2.5 Pro, on the authors' own description, is responsible only for arranging spelling, grammar, LaTeX, and the structure of the steps; the category and the topic are extracted. The paper spot-checks some of the scores given by the judge, but it does not claim that every question was verified by two experts.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Quality control

The original content is cleaned, LaTeX is made consistent, Gemini 2.5 Pro Think is used to break the solution into steps, and topic, difficulty, and physical principles are labeled. This process is not the same as an independent expert review of each question.

Sources: [1](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

### 去污染与泄漏边界

A 90/10 split into training and test; the questions and reference solutions come from public textbooks and websites, so memorization from pretraining cannot be ruled out. The paper’s experiments at inference time are not training on the test set; a random split is not treated as completed removal of the test material from the training corpus.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Data format

### Size

19,609 questions; 17,647 for training and 1,962 for test, 19 classes in total.

Sources: [1](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

### 题型与交付物

Open mathematical computation and descriptive physics question answering, with step-by-step reference solutions; 19 categories. It is not multiple-choice accuracy, and the main result uses solution-quality PPS.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， ) ; [2](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

### Modalities

Text and LaTeX formulas, step-by-step solutions, and metadata for category, topic, and difficulty; this release does not build a unified visual track from input images.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， ) ; [2](https://huggingface.co/datasets/IUTVanguard/PhysicsEval/raw/main/README.md) (accessed 2026-11-08， )

### Languages

English (HF dataset card language: en).

Sources: [1](https://huggingface.co/datasets/IUTVanguard/PhysicsEval/raw/main/README.md) (accessed 2026-11-08， )

### Difficulty

Each question is annotated with a difficulty of 1–10; the number of solution steps is also provided, and some questions provide an alternative solution.

Sources: [1](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

### Public and hidden splits

A 90:10 training/test split, 17,647 and 1,962 respectively; the README does not list a separate validation set.

Sources: [1](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

## Evaluation

### Metrics

Physics Proficiency Score (PPS). The paper states that it is normalized to 0–100. Six component scores on a scale of 1–5 are also reported: mathematical accuracy, logical consistency, formulas and principles, completeness, assumptions, and clarity and coherence. It is not a binary accuracy of the final answer.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### Scoring

Gemini2.5 Pro sees the question, the human-source reference solution, and the model-generated solution, and then scores them by the rubric. The final PPS weights (Table 3) are mathematics 0.30, logic 0.25, formulas and principles 0.20, completeness 0.10, assumptions 0.10, and clarity 0.05. They must not be mixed with the verifier weights at reasoning time in §4.1.2. Equation 3 writes only the weighted sum of 1–5 item scores. The text also refers to 0–100, but that equation does not explicitly write a conversion coefficient, and no conversion formula is added.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 提示与运行设置

The four protocols Baseline, Self-Refine, Single-Agent, and Multi-Agent are kept separate. Self-Refine requires a physics professor to check the answer and then answer again. Single-Agent has Qwen3-32B provide a list of errors. Multi-Agent uses three judges, Phi4, DeepSeekR1-14B, and Qwen3-14B, and Qwen3-32B as a meta-judge integrates the feedback. The full prompts are in Appendix A of the paper.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 评测脚本

https://github.com/areebuzair/PhysicsEval

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 可比性提醒

PPS is partial credit assigned by a model judge, and it is not an accuracy. Table 2 for difficulty uses Easy1–4, Medium5–7, and Hard8–10, while Figure 3 marks 1–3, 4–6, and 7–10. The two statements of the ranges conflict, and both are kept. A difference of protocol at reasoning time, a difference of judge version, and a difference of difficulty grouping cannot be ranked across tracks.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， )

### 数据版本与更新

Unverified

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 论文修订记录

Submission history From: Syed Rifat Raiyan [ view email ] [v1] 2025-08-01 03:12:51 (159 KB) [v2] 2025-11-05 16:50:45 (156 KB)

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 饱和程度

In Table 2 of the paper, for the Hard8–10 group: the highest Baseline is o4-mini83.6, and the highest Multi-Agent is Phi-4-reasoning-plus87.6 (PPS, not accuracy). This can state only the measured quality score of that protocol in the original paper, and it is not extrapolated to whether current frontier models are saturated.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 争议与已知问题

Public textbooks and solutions posted on forums carry overlap with training and a risk under third-party copyright; an HF mark of CC-BY-SA-4.0 does not automatically resolve a further license for the original textbooks. The PPS normalization formula omits an explicit coefficient, and the difficulty boundaries in Table 2 and in Figure 3 do not agree; Gemini both arranges the reference solutions and serves as the final judge. The authors say that prompting and manual spot checks reduce the bias, and this is not treated as independent proof that the result is unbiased.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， ) ; [2](https://huggingface.co/datasets/IUTVanguard/PhysicsEval/raw/main/README.md) (accessed 2026-11-08， )

### 衍生与后续使用

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (date the web page was accessed; dates of historical results are kept separately).

Sources: [1](https://arxiv.org/pdf/2508.00079#page=7) (accessed 2026-11-08， )

### 官方结果入口

https://arxiv.org/pdf/2508.00079#page=7

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 第三方入口

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 分赛道结果

- {"model": "QwQ-32B", "score": 93.7, "track": "Original paper v2/Table 2/Easy1–4/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Baseline", "rank": 1}
- {"model": "Llama 4 Maverick", "score": 91.5, "track": "Original paper v2/Table 2/Easy1–4/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Baseline", "rank": 2}
- {"model": "DeepSeek-R1", "score": 90.6, "track": "Original paper v2/Table 2/Easy1–4/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Baseline", "rank": 3}
- {"model": "Gemma 3 27B", "score": 86.9, "track": "Original paper v2/Table 2/Easy1–4/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Baseline", "rank": 4}
- {"model": "o4-mini", "score": 86.7, "track": "Original paper v2/Table 2/Easy1–4/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Baseline", "rank": 5}
- {"model": "Phi-4-reasoning-plus", "score": 84.4, "track": "Original paper v2/Table 2/Easy1–4/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Baseline", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 94.4, "track": "Original paper v2/Table 2/Easy1–4/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Self-Refine", "rank": 1}
- {"model": "QwQ-32B", "score": 94.0, "track": "Original paper v2/Table 2/Easy1–4/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Self-Refine", "rank": 2}
- {"model": "DeepSeek-R1", "score": 92.7, "track": "Original paper v2/Table 2/Easy1–4/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Self-Refine", "rank": 3}
- {"model": "Llama 4 Maverick", "score": 90.5, "track": "Original paper v2/Table 2/Easy1–4/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Self-Refine", "rank": 4}
- {"model": "Gemma 3 27B", "score": 85.7, "track": "Original paper v2/Table 2/Easy1–4/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Self-Refine", "rank": 5}
- {"model": "o4-mini", "score": 82.6, "track": "Original paper v2/Table 2/Easy1–4/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Self-Refine", "rank": 6}
- {"model": "QwQ-32B", "score": 94.2, "track": "Original paper v2/Table 2/Easy1–4/Single-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Single-Agent", "rank": 1}
- {"model": "DeepSeek-R1", "score": 93.3, "track": "Original paper v2/Table 2/Easy1–4/Single-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Single-Agent", "rank": 2}
- {"model": "Phi-4-reasoning-plus", "score": 93.2, "track": "Original paper v2/Table 2/Easy1–4/Single-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Single-Agent", "rank": 3}
- {"model": "Llama 4 Maverick", "score": 92.0, "track": "Original paper v2/Table 2/Easy1–4/Single-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Single-Agent", "rank": 4}
- {"model": "Gemma 3 27B", "score": 86.4, "track": "Original paper v2/Table 2/Easy1–4/Single-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Single-Agent", "rank": 5}
- {"model": "o4-mini", "score": 85.9, "track": "Original paper v2/Table 2/Easy1–4/Single-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Single-Agent", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 94.7, "track": "Original paper v2/Table 2/Easy1–4/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Multi-Agent", "rank": 1}
- {"model": "QwQ-32B", "score": 94.6, "track": "Original paper v2/Table 2/Easy1–4/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Multi-Agent", "rank": 2}
- {"model": "DeepSeek-R1", "score": 94.1, "track": "Original paper v2/Table 2/Easy1–4/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Multi-Agent", "rank": 3}
- {"model": "Llama 4 Maverick", "score": 92.9, "track": "Original paper v2/Table 2/Easy1–4/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Multi-Agent", "rank": 4}
- {"model": "Gemma 3 27B", "score": 87.6, "track": "Original paper v2/Table 2/Easy1–4/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Multi-Agent", "rank": 5}
- {"model": "o4-mini", "score": 86.8, "track": "Original paper v2/Table 2/Easy1–4/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Easy1–4", "inference_method": "Multi-Agent", "rank": 6}
- {"model": "o4-mini", "score": 87.3, "track": "Original paper v2/Table 2/Medium5–7/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Baseline", "rank": 1}
- {"model": "Phi-4-reasoning-plus", "score": 86.9, "track": "Original paper v2/Table 2/Medium5–7/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Baseline", "rank": 2}
- {"model": "Llama 4 Maverick", "score": 83.6, "track": "Original paper v2/Table 2/Medium5–7/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Baseline", "rank": 3}
- {"model": "QwQ-32B", "score": 80.9, "track": "Original paper v2/Table 2/Medium5–7/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Baseline", "rank": 4}
- {"model": "DeepSeek-R1", "score": 80.8, "track": "Original paper v2/Table 2/Medium5–7/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Baseline", "rank": 5}
- {"model": "Gemma 3 27B", "score": 55.8, "track": "Original paper v2/Table 2/Medium5–7/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Baseline", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 92.2, "track": "Original paper v2 / Table 2 / Medium5–7 / Self-Refine.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Self-Refine", "rank": 1}
- {"model": "o4-mini", "score": 86.4, "track": "Original paper v2 / Table 2 / Medium5–7 / Self-Refine.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Self-Refine", "rank": 2}
- {"model": "DeepSeek-R1", "score": 84.4, "track": "Original paper v2 / Table 2 / Medium5–7 / Self-Refine.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Self-Refine", "rank": 3}
- {"model": "Llama 4 Maverick", "score": 82.0, "track": "Original paper v2 / Table 2 / Medium5–7 / Self-Refine.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Self-Refine", "rank": 4}
- {"model": "QwQ-32B", "score": 80.8, "track": "Original paper v2 / Table 2 / Medium5–7 / Self-Refine.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Self-Refine", "rank": 5}
- {"model": "Gemma 3 27B", "score": 56.5, "track": "Original paper v2 / Table 2 / Medium5–7 / Self-Refine.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Self-Refine", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 93.4, "track": "Original paper v2 / Table 2 / Medium5–7 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Single-Agent", "rank": 1}
- {"model": "o4-mini", "score": 87.0, "track": "Original paper v2 / Table 2 / Medium5–7 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Single-Agent", "rank": 2}
- {"model": "DeepSeek-R1", "score": 83.1, "track": "Original paper v2 / Table 2 / Medium5–7 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Single-Agent", "rank": 3}
- {"model": "Llama 4 Maverick", "score": 82.6, "track": "Original paper v2 / Table 2 / Medium5–7 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Single-Agent", "rank": 4}
- {"model": "QwQ-32B", "score": 81.1, "track": "Original paper v2 / Table 2 / Medium5–7 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Single-Agent", "rank": 5}
- {"model": "Gemma 3 27B", "score": 59.4, "track": "Original paper v2 / Table 2 / Medium5–7 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Single-Agent", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 93.9, "track": "Original paper v2 / Table 2 / Medium5–7 / Multi-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Multi-Agent", "rank": 1}
- {"model": "o4-mini", "score": 88.2, "track": "Original paper v2 / Table 2 / Medium5–7 / Multi-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Multi-Agent", "rank": 2}
- {"model": "DeepSeek-R1", "score": 83.4, "track": "Original paper v2 / Table 2 / Medium5–7 / Multi-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Multi-Agent", "rank": 3}
- {"model": "Llama 4 Maverick", "score": 82.4, "track": "Original paper v2 / Table 2 / Medium5–7 / Multi-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Multi-Agent", "rank": 4}
- {"model": "QwQ-32B", "score": 81.9, "track": "Original paper v2 / Table 2 / Medium5–7 / Multi-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Multi-Agent", "rank": 5}
- {"model": "Gemma 3 27B", "score": 59.1, "track": "Original paper v2 / Table 2 / Medium5–7 / Multi-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Medium5–7", "inference_method": "Multi-Agent", "rank": 6}
- {"model": "o4-mini", "score": 83.6, "track": "Original paper v2/Table 2/Hard8–10/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Baseline", "rank": 1}
- {"model": "Phi-4-reasoning-plus", "score": 80.1, "track": "Original paper v2/Table 2/Hard8–10/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Baseline", "rank": 2}
- {"model": "DeepSeek-R1", "score": 72.9, "track": "Original paper v2/Table 2/Hard8–10/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Baseline", "rank": 3}
- {"model": "QwQ-32B", "score": 63.9, "track": "Original paper v2/Table 2/Hard8–10/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Baseline", "rank": 4}
- {"model": "Llama 4 Maverick", "score": 55.2, "track": "Original paper v2/Table 2/Hard8–10/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Baseline", "rank": 5}
- {"model": "Gemma 3 27B", "score": 41.5, "track": "Original paper v2/Table 2/Hard8–10/Baseline", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Baseline", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 83.4, "track": "Original paper v2/Table 2/Hard8–10/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Self-Refine", "rank": 1}
- {"model": "o4-mini", "score": 82.3, "track": "Original paper v2/Table 2/Hard8–10/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Self-Refine", "rank": 2}
- {"model": "DeepSeek-R1", "score": 73.7, "track": "Original paper v2/Table 2/Hard8–10/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Self-Refine", "rank": 3}
- {"model": "QwQ-32B", "score": 68.6, "track": "Original paper v2/Table 2/Hard8–10/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Self-Refine", "rank": 4}
- {"model": "Llama 4 Maverick", "score": 54.0, "track": "Original paper v2/Table 2/Hard8–10/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Self-Refine", "rank": 5}
- {"model": "Gemma 3 27B", "score": 40.4, "track": "Original paper v2/Table 2/Hard8–10/Self-Refine", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Self-Refine", "rank": 6}
- {"model": "o4-mini", "score": 84.1, "track": "Original paper v2 / Table 2 / Hard8–10 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Single-Agent", "rank": 1}
- {"model": "Phi-4-reasoning-plus", "score": 83.8, "track": "Original paper v2 / Table 2 / Hard8–10 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Single-Agent", "rank": 2}
- {"model": "DeepSeek-R1", "score": 74.7, "track": "Original paper v2 / Table 2 / Hard8–10 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Single-Agent", "rank": 3}
- {"model": "QwQ-32B", "score": 63.5, "track": "Original paper v2 / Table 2 / Hard8–10 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Single-Agent", "rank": 4}
- {"model": "Llama 4 Maverick", "score": 57.9, "track": "Original paper v2 / Table 2 / Hard8–10 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Single-Agent", "rank": 5}
- {"model": "Gemma 3 27B", "score": 39.1, "track": "Original paper v2 / Table 2 / Hard8–10 / Single-Agent.", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Single-Agent", "rank": 6}
- {"model": "Phi-4-reasoning-plus", "score": 87.6, "track": "Original paper v2/Table 2/Hard8–10/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Multi-Agent", "rank": 1}
- {"model": "o4-mini", "score": 85.4, "track": "Original paper v2/Table 2/Hard8–10/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Multi-Agent", "rank": 2}
- {"model": "DeepSeek-R1", "score": 72.7, "track": "Original paper v2/Table 2/Hard8–10/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Multi-Agent", "rank": 3}
- {"model": "QwQ-32B", "score": 71.0, "track": "Original paper v2/Table 2/Hard8–10/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Multi-Agent", "rank": 4}
- {"model": "Llama 4 Maverick", "score": 52.1, "track": "Original paper v2/Table 2/Hard8–10/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Multi-Agent", "rank": 5}
- {"model": "Gemma 3 27B", "score": 40.6, "track": "Original paper v2/Table 2/Hard8–10/Multi-Agent", "metric": "PPS (0–100, not accuracy)", "source_url": "https://arxiv.org/pdf/2508.00079", "collected_at": "2026-11-08 ", "result_type": "Original-paper historical results; Table 2 difficulty definition", "difficulty": "Hard8–10", "inference_method": "Multi-Agent", "rank": 6}

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 覆盖边界

The 72 exact PPS scores in Table 2 of the paper, for six models × three difficulty levels × four reasoning strategies, are transcribed in full. Each difficulty level and protocol is kept on its own track. They are not averaged into an overall leaderboard, and PPS is not labeled as accuracy. An independent live official leaderboard has not been verified, and the historical paper is not presented as live SOTA.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

## Contact

### 公开项目邮箱

- rifatraiyan@iut-dhaka.edu

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 公开反馈渠道

https://github.com/areebuzair/PhysicsEval/issues

Sources: [1](https://github.com/areebuzair/PhysicsEval) (accessed 2026-11-08， )

### 官方社交渠道

Unverified

Note: This field has not been verified exactly; that does not mean it is officially Not disclosed.

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 联系方式收录原则

Benchmark Constitution includes only project contact channels that the paper or the official site has made public, and it does not collect private information; this is not a certification of an external site’s privacy policy.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08， )

## Original files

### 既存论文原件

```json
{
  "id": "1xAWaC752N5gbfuKJ8yx0Ua53ndFAwdOy"
  "webViewLink": "
}
```

Sources: [1](

### 原始PDF地址

https://arxiv.org/pdf/2508.00079

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， ) ; [2](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 下载SHA-256

463be2b22a05d41dbf11319c0d11bc34966925ea3f17975b4082b81caa3daea0

Note: Checksum of the bytes downloaded on 2026-11-08. Nothing was overwritten or uploaded, so this does not establish that an existing original is the same version.

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 下载字节数

```json
512745
```

Sources: [1](https://arxiv.org/pdf/2508.00079) (accessed 2026-11-08， )

### 既存文件夹

```json
{
  "id": "14RJrVx0urpr_XOyFXwHYU2-lCkAtLMZ2"
  "webViewLink": "
}
```

Sources: [1](

### Other documents

- {"kind": "Chinese introduction", "id": "1CWGoPSNuvMuZLalgvf-ezAW-3sBwDbq7NDbUFgs1q3M", "webViewLink": "

Sources: [1](

## Changelog

Latest review
Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2508.00079) (accessed 2026-11-08， )
