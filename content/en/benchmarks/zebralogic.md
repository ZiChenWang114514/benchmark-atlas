# ZebraLogic

> In-depth review: 2026-11-08. The collection date is not the leaderboard update date; new evidence that has not been obtained does not overwrite an older source date.

ZebraLogic writes entity-attribute relations as constraint puzzles with a unique solution, and observes how a model degrades as the search space and the backtracking complexity grow. Whole-puzzle accuracy, partial cell correctness, and the hardest XL subset cannot be substituted for one another. Taking the best of several attempts is also not the same as a single response.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

## Basic information

### Short name

ZebraLogic

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Full name

ZebraLogic

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Benchmark version

A public set of 1000 questions; first released in 2024, with a 2025 paper version, and no data revision is fixed

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07  ) ; [2](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08 ).

### Paper version

arXiv v2

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Release date

- **paper_first_submission_kst**：2025-02-03
- **date_type**：First submission of the paper; not the same as the first release of the dataset

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Section

Reasoning

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07 ).

### Field tags

- Constrained logical reasoning

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### License

- **evaluation_code**：Apache-2.0（ZeroEval LICENSE）
- **dataset**：Unverified (the WildEval/ZebraLogic dataset card that was opened does not declare a license; a code license does not replace data authorization)

> The code license has been verified; the dataset license remains Unverified. This field is only partly complete and is not counted as the licensing being fully cleared.

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/LICENSE) (accessed 2026-11-08  ) ; [2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md) (accessed 2026-11-08 ).

### Paper

https://arxiv.org/abs/2502.01100

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Code

https://github.com/WildEval/ZeroEval

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07 ).

### 数据地址

https://huggingface.co/datasets/WildEval/ZebraLogic

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07  ) ; [2](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08 ).

### Official entry

https://huggingface.co/spaces/allenai/ZebraLogic

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07  ) ; [2](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08 ).

### Paper title

ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

## Origin and maintenance

### Initiating organizations

University of Washington, Allen Institute for AI, and Stanford University (paper byline)

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### 署名合作机构

- University of Washington
- Allen Institute for AI
- Stanford University

> The institutions named on the first page of the PDF; no further funding partnership is inferred.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08 ).

### Authors

- Lin, Bill Yuchen
- Bras, Ronan Le
- Richardson, Kyle
- Sabharwal, Ashish
- Poovendran, Radha
- Clark, Peter
- Choi, Yejin

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Maintainer

WildEval/ZeroEval maintains the public evaluation and the summary table; the dataset card is at WildEval/ZebraLogic, and the official interactive leaderboard is the allenai/ZebraLogic Space (the configuration also links allenai/ZebraLogicBench).

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md) (accessed 2026-11-08  ) ; [2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md) (accessed 2026-11-08  ) ; [3](https://huggingface.co/spaces/allenai/ZebraLogic/raw/main/README.md) (accessed 2026-11-08 ).

### Funders

Research by Yejin Choi received partial support from NSF DMS-2134012 (paper acknowledgments); it is not inferred that the grant covers every author or the full cost of the project.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08 ).

## Design goals

### Abilities measured

Verifiable zebra logic-grid puzzles are used to evaluate constraint propagation, global consistency, and reasoning ability as it changes with a growing search space.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Design background

Traditional knowledge question answering has difficulty separating memorization from logical search; this set uses CSPs of controllable scale to analyze the scaling limit of reasoning computation.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

## Construction

### 题目与数据来源

The program first samples a complete grid solution, then generates clues and uses a solver to check that the solution is unique; after redundant clues are removed, a natural-language question remains.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### 构建者背景

Researchers in logic and natural-language reasoning designed the templates and the generation programs; the questions are not written by hand one by one.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Review process

Solvability and a unique solution are checked by constraint solving; the paper analyzes how the solver's conflict count corresponds to model difficulty.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Quality control

There are 25 sizes, from 2–6 houses × 2–6 attributes, with 40 questions of each size. A solver guarantees a unique solution and tries, clue by clue, to remove redundant clues, producing a clue set that is minimal with respect to deletion one clue at a time. This is not the same as a globally minimal puzzle statement. Z3 is run 32 times on each question, and the average number of conflicts helps describe the difficulty of the search.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08 ).

### 去污染与泄漏防范

Synthesis and unique-solution verification reduce some data problems, but public sets and templates cannot prove that later models have not seen the test questions.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

## Data format

### Size

The dataset card's grid_mode test set has 1000 puzzles; the mc_mode test set has 3259 multiple-choice questions. The two are different configurations and are not added into a count of independent puzzles.

Sources: [1](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md) (accessed 2026-11-08 ).

### 任务形式

A complete entity-attribute correspondence grid is filled in from natural-language clues, and structured JSON is produced.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Modalities

Plain-text clues and a structured entity-attribute grid; the answer is a JSON table. This is not image-grid recognition or question answering on mathematical formulas.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08  ) ; [2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md) (accessed 2026-11-08 ).

### Languages

Natural-language clues in English, entity attributes, and JSON fields.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08 ).

### 难度与类型

Divided by grid size, search space, Z3 conflicts, and similar factors; the same size does not mean equal difficulty of solution.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### Public and hidden splits

A public evaluation set; the materials do not confirm an independent hidden official test set.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

## Evaluation

### Metrics

Whole-question full-grid correctness is the primary metric; cell correctness is a secondary metric.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### 评分

A complete grid requires every correspondence to be correct; correctness of some cells is not equivalent to passing the whole question.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### 提示和复现设置

Paper §3 uses a one-shot format example and outputs reasoning and JSON. Most models use the same greedy prompt and parsing. o1 is the exception: it is run three times and the best is taken. Mode, N_Mode, and N_Size in the current ZeroEval summary table are recorded as shown in the table. Even where the same model scores 81.0%, the table's single mark and the paper's best-of-3 interpretation are not forcibly unified.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md) (accessed 2026-11-08  ) ; [3](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08 ).

### 官方脚本

ZeroEval: run with -d zebra-grid; scored by src/evaluation/zebra_grid_eval.py, with support for local and API inference.

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md) (accessed 2026-11-08 ).

### 可比性提示

Whole-puzzle Puzzle Acc, Cell Acc, and Small/Medium/Large/XL are kept separate. The paper's one-shot setting and o1 taking the best of three runs, the repository's greedy/single labels, the model provider, and the API checkpoint all need to be retained. The official table includes a Llama-3.1-405B@hyperbolic row of only 16 questions, and it cannot be treated as a full-set rank on 1000 questions.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08 ).

## Current status

### 核验时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md) (accessed 2026-11-08 ).

### 数据版本与当前状态

A public set of 1000 questions; first released in 2024, with a 2025 paper version, and no data revision is fixed

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07  ) ; [2](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08 ).

### 论文修订与H2证据

- **arxiv_version**：arXiv v2
- **history_note**：See the arXiv metadata for the full history; the draft date has been converted, and the paper revision date is not treated as the data version.
- **2026_h2_evidence**：- - **url**：https://arxiv.org/html/2609.27284v1
    - **date**：2026-09-23
    - **note**：Hunyuan-A13B §4.2 Reasoning and Tables 3–4 actually report ZebraLogic; a vendor-self-reported evaluation.
- **revisions**：- - **version**：v1
    - **date_kst**：2025-02-03
  - - **version**：v2
    - **date_kst**：2025-07-15
- **note**：The paper revision time cannot be treated as the data release date. Existing 2026-H2 evidence retains the original collection date.

Sources: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08  ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07 ).

### 饱和程度

The highest full-set Puzzle Acc in the current author table is 92.6% (grok-3-mini-fast-beta-high), and XL on the same row is 76.5%; a high score overall does not mean that a large search space has been solved. o3-mini-high is 91.7% on the full set and XL75.5%, and the figures are read in light of the hard subset and the decoding budget.

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08 ).

### 污染、冲突与限制

Guaranteeing a unique solution at the time of generation does not mean that later models have not seen the public questions. The body of the size classification in the paper uses 10^10 as the boundary between Large and XL, but the header of Table1 writes 10^9, so the thresholds in the source disagree. The explicit list of sizes in the body is recorded first, and the categories are not merged on one's own. The difference between taking the best of three runs in the o1 paper and the single-row label in the repository is also kept; incomplete results on 16 questions are listed on their own.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08 ).

### 后续工作与衍生

It is the zebra-grid task in the ZeroEval evaluation framework; it is not Sudoku, and it is not equivalent to every Einstein puzzle.

Sources: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08  ) ; [2](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07 ).

## Leaderboard snapshot

### 快照采集日

2026-11-08; self-reports by the vendor keep the existing collection date

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08 ).

### Official leaderboard

https://huggingface.co/spaces/allenai/ZebraLogic

Sources: [1](https://github.com/WildEval/ZeroEval) (accessed 2026-11-07  ) ; [2](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07 ).

### 第三方覆盖

Unverified

> No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### Author complete 1000 questions/greedy/single/1

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | grok-3-mini-fast-beta-high | 92.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 98.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 96.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 93.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 76.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 94.63 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 1.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 91.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 99.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 97.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 87.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 75.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 95.7 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 0.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 88.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 99.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 97.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 88.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 60.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 90.41 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 81.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 97.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 92.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 78.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 42.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 78.74 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 80.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 98.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 96.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 77.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 33.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 84.22 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 78.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 98.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 95.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 73.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 28.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 80.54 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 74.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 99.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 91.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 64.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 23.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 72.6 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 1.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 71.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 98.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 88.21 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 59.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 17.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 75.14 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 0.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 70.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 97.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 88.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 55.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 16.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 74.18 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 0.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 59.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 87.5 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 76.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 39.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 12.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 70.32 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 1.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 57.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 94.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 71.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 34.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 4.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 67.73 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 56.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 83.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 76.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 36.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 7.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 69.87 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 1.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 52.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 87.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 67.5 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 24.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 3.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 52.29 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 0.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 42.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 85.62 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 44.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 10.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 1.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 42.04 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 27.9 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 36.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 84.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 28.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 4.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 1.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 54.27 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 33.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 83.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 21.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 3.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 54.34 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 32.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 81.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 22.5 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 1.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 45.8 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 12.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 31.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 80.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 19.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 2.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 0.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 50.34 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 3.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 30.5 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 75.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 20.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 3.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 50.84 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 0.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 30.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 79.06 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 16.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 0.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 39.06 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 24.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 29.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 76.88 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 17.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 1.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 48.83 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 4.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 29.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 75.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 15.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 2.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 47.64 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 1.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 28.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 75.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 15.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 47.9 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 28.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 73.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 16.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 38.72 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 19.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 27.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 71.88 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 13.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 4.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 48.16 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 3.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 27.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 71.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 13.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 2.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 47.43 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 27.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 73.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 12.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 48.91 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 26.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 72.5 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 12.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 40.92 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 11.9 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 26.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 72.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 10.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 43.39 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 6.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 25.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 66.56 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 13.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 48.5 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 25.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 65.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 13.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 2.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 43.56 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 8.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 24.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 67.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 10.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 1.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 27.98 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 43.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 22.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 63.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 8.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 42.46 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 5.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 22.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 62.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 7.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 38.01 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 12.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 21.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 60.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 6.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 38.32 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 10.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 21.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 59.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 7.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 41.58 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 4.9 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 20.5 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 57.5 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 7.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 42.35 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 3.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 20.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 58.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 4.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 41.26 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 19.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 55.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 6.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 31.77 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 22.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 19.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 52.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 9.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 44.59 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 0.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 18.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 53.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 6.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 42.61 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 1.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 18.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 54.37 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 5.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 39.83 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 1.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 18.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 53.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 6.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 43.22 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 18.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 54.06 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 4.29 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 1.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 43.66 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 16.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 48.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 4.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 42.31 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 16.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 48.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 3.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 32.98 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 21.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 16.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 46.56 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 5.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 41.18 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 1.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 14.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 43.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 37.87 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 13.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 40.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 2.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 39.01 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 13.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 39.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 1.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 33.88 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 4.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 12.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 37.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 2.5 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 36.79 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 12.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 39.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 13.68 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 61.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 12.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 36.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 1.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 30.67 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 9.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 11.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 36.88 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 0.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 23.7 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 29.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 11.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 35.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 1.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 34.93 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 1.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 11.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 35.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 0.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 13.5 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 59.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 11.5 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 35.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 32.73 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 4.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 10.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 30.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 33.06 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 9.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 30.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 32.66 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 1.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 9.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 28.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 25.67 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 18.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 9.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 27.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 20.42 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 36.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 8.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 26.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 26.47 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 20.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 8.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 26.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 22.06 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 24.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 7.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 23.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 13.14 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 54.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 6.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 19.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 5.98 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 80.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 4.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 15.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 11.44 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 56.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 4.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 13.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 9.97 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 57.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 2.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 7.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 7.53 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 11.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |

#### Author incomplete subset/greedy/single/1

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Llama-3.1-405B-Inst@hyperbolic | 25.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 50.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 33.33 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 46.62 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 6.25 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |

#### Existing vendor self-report (not refreshed)

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Hunyuan-A13B | 84.7 % | accuracy slow thinking, accuracy on the full set of questions, report Table 3 | 2026-09-23；https://arxiv.org/html/2609.27284v1 |
| — | OpenAI-o1-1217 | 81.0 % | accuracy Column names from the same table; checkpoints recorded as in the report | 2026-09-23；https://arxiv.org/html/2609.27284v1 |

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08  ) ; [2](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07 ).

### Coverage note

All 7 percentage metrics for all 69 rows of the summary table in the current author repository were restored cell by cell, 483 values in total. total_puzzles, mode, n_mode, n_size, and reason length are recorded. The complete set of 1000 questions and the incomplete subset of 16 questions are on separate tracks. A run date that is Not disclosed is not invented. The existing two self-reported Hunyuan rows keep their original dates and sources and are not placed in the official ranking.

Sources: [1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md) (accessed 2026-11-08 ).

## Contact

### 公开联系邮箱

- byuchen@uw.edu
- ronanlb@allenai.org

Sources: [1](https://huggingface.co/spaces/allenai/ZebraLogic) (accessed 2026-11-07  ) ; [2](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08 ).

### 问题反馈

https://github.com/WildEval/ZeroEval/issues

Sources: [1](https://github.com/WildEval/ZeroEval) (accessed 2026-11-07 ).

### 官方讨论渠道

Unverified

> No dedicated official social account has been verified, and personal accounts of the same name are not included

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### 隐私与数据使用

Unverified

> A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2502.01100

Source: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08).

### SHA-256

c252c5c4c6aa7394cb97f81d7e77fd69b3ec8d374ede75c7f0189a1530a3820d

> Original bytes of the PDF downloaded again. The existing copy was not overwritten.

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08 ).

### 字节数

3577291

Sources: [1](https://arxiv.org/pdf/2502.01100) (accessed 2026-11-08 ).

### Folder

- **id**：1zdfv98gUtwSgZInQe0SU-tLvBK_3TWdy
- **webViewLink**：

Sources: [1]( 2026-11-07 ).

### Other documents

- **chinese_intro_doc**：- **id**：125u-jDuDNBy2zes2eY4ZNY425O-LzOhjWowRw-F24vs
  - **webViewLink**：
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/zebralogic.md

Sources: [1]( 2026-11-07 ).

### 原文归档

- **id**：1udO6bEUq9MMLZuhldfpfTxSwt_8H1-uv
- **webViewLink**：

Sources: [1]( 2026-11-07 ).

## Changelog

### 本页修订

- - **date**：2026-11-07
  - **timezone**：
  - **change**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
  - **fields_updated**：- basic_info.license
    - evaluation.official_scripts
    - data_format.size
    - leaderboard.results
    - leaderboard.coverage_note
- - **date**：2026-11-08
  - **timezone**：
  - **round**：2
  - **change**：逐项打开arXiv摘要与PDF全文、Official README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

Sources: [1](https://arxiv.org/abs/2502.01100) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md) (accessed 2026-11-08 ).
