# WebArena

> In-depth review: 2026-11-08. The collection date is not the leaderboard update date; new evidence that has not been obtained does not overwrite an older source date.

WebArena checks the final state of a task on self-hosted websites that can be reset, and it allows action paths that differ and are still valid. The official Sheet is a collection of results from different entrants, not one unified experiment that shares the model, the inputs, and the harness; the original 812 tasks, the Reddit subset, and the Infinity success trajectories cannot be used interchangeably.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Basic information

### Short name

WebArena

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### Full name

WebArena

> The official name is retained, and the paper title is not automatically expanded into a full name.

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### Benchmark version

Canonical WebArena v0.2.0 (the protocol of 812 tasks after the comment fix of 2023-10-24); AgentLab/BrowserGym belongs to the recommended frameworks for running it.

Sources: [1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08 ).

### Paper version

arXiv v4

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Release date

- **paper_first_submission_kst**：2023-07-26
- **date_type**：First submission of the paper; not the same as the first release of the dataset

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Section

Agent

> Benchmark Constitution editorial filing. Only the main section is counted.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Field tags

- Web task execution

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### License

Apache-2.0 (the marking on the code of the GitHub repository; it does not automatically cover the original questions, third-party materials, or private test data)

Sources: [1](https://github.com/web-arena-x/webarena) (accessed 2026-11-07 ).

### Paper

https://arxiv.org/abs/2307.13854

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Code

https://github.com/web-arena-x/webarena

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### 数据地址

https://github.com/web-arena-x/webarena/blob/main/config_files/test.raw.json

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### Official entry

https://webarena.dev/og/

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### Paper title

WebArena: A Realistic Web Environment for Building Autonomous Agents

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Origin and maintenance

### Initiating organizations

Carnegie Mellon University; the authors also list an Inspired Cognition affiliation.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 署名合作机构

- Carnegie Mellon University
- Inspired Cognition

> According to the institutions in the author byline on the project page of the paper; no collaboration is inferred with website brands imitated in the environment.

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### Authors

- Zhou, Shuyan
- Xu, Frank F.
- Zhu, Hao
- Zhou, Xuhui
- Lo, Robert
- Sridhar, Abishek
- Cheng, Xianyi
- Ou, Tianyue
- Bisk, Yonatan
- Fried, Daniel
- Alon, Uri
- Neubig, Graham

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Maintainer

web-arena-x and the WebArena team maintain the canonical reproduction repository. On 2024-12-05, the official recommendation was that new experiments use AgentLab/BrowserGym, in order to improve parallel runs, boundary handling, and unified reporting.

Sources: [1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08 ).

### Funders

AFRL FA8750-19-2-0200; AWS AI gift; CAIS compute support.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Design goals

### Abilities measured

Turns high-level natural-language intent into multi-step actions across web pages, correctly changing web-page state or obtaining information.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Design background

Static web-page snapshots and short-step tasks make long-horizon planning hard to evaluate; looking only at similarity of actions rejects paths that differ but are correct.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Construction

### 题目与数据来源

Self-hosted realistic websites in four categories: e-commerce, forums, collaborative development, and content management. The authors wrote 241 templates that yield 812 tasks, with a map, a calculator, a wiki, and similar tools attached.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 构建者背景

Intents designed by CMU researchers; the website data simulate real-world distributions and are not operations on real user accounts.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Review process

Two annotators produce the reference answer, and a third person resolves disagreements.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Quality control

On 2023-10-24 the full dataset was rechecked and annotation errors that were found were fixed; the official release calls v0.2.0 a relatively stable version. Each test task uses a program to check the target information or the website state.

Sources: [1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08  ) ; [2](https://webarena.dev/og/) (accessed 2026-11-08 ).

### 去污染与泄漏防范

The local environment supports reproduction, but the data and tasks are public; template similarity and later training contamination still require attention.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Data format

### Size

812 tasks, from 241 templates, covering 4 main categories of websites.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 任务形式

Information lookup, creation and editing of content, and joint operations across several websites.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Modalities

- Web-page text/HTML/accessibility tree
- 可选截图
- 工具动作

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Languages

English instructions; website content and code-related syntax.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 难度与类型

Long-horizon, and some require multiple websites or external knowledge; instances from the same template are not fully independent points of capability.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### Public and hidden splits

Self-hosted websites, tasks, and functional-evaluation code are public; this is not equivalent to live real websites or hidden services.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Evaluation

### Metrics

End-to-end task success rate.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 评分

The final or necessary intermediate website state is checked; query answers use exact match, contains, or GPT-4-0613 fuzzy comparison.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 提示和复现设置

The example in the canonical README uses an accessibility tree and two CoT prompts in p_cot_id_actree_2s.json; evaluation must deploy the websites itself rather than use the demonstration site, and the environment is reset after all 812 examples have been run. The model, the maximum number of steps, and whether a not-achievable hint is provided must be fixed for each result.

Sources: [1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08 ).

### 官方脚本

https://github.com/web-arena-x/webarena

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### 可比性提示

WebArena differs from the VisualWebArena, WebArena-Infinity, and Verified variants; observation by screenshot and by the accessibility tree, external browsing, and the step budget also differ.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Current status

### 核验时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08 ).

### 数据版本与当前状态

- **version**：canonical v0.2.0, 812 tasks; a full recheck of the data and a repair of the annotations were completed on 2023-10-24; AgentLab was recommended on 2024-12-05
- **evidence_2026_h2**：- - **url**：https://arxiv.org/html/2609.19134v1
    - **date**：2026-09-17
    - **note**：ScienceIDE §4.2 and the references explicitly cite WebArena as a prior benchmark for language-model agents and interactive environments; this is an H2 academic citation, and it does not claim that this paper ran the benchmark.
    - **date_kst**：2026-09-17
    - **verified_in_round1**：The ScienceIDE text and references were reopened and confirmed by the original paper ID; it belongs to the related-work citations in §4.2 and is not an actual run in this paper.
  - - **url**：https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv
    - **date**：2026-09
    - **note**：The main leaderboard on the officially maintained Sheet includes Narada AI Code at 86.1, with the time column 09/2026; this is a participant’s score included on the leaderboard of that period, and an independent rerun is not inferred.

Sources: [1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08  ) ; [2](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07  ) ; [3](https://arxiv.org/abs/2609.19134) (accessed 2026-11-07  ) ; [4](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv) (accessed 2026-11-08 ).

### 论文修订与H2证据

- **previous_evidence_note**：Submission history From: Shuyan Zhou [ view email ] [v1] 2023-07-26 07:59:32 (9,497 KB) [v2] 2023-10-24 12:19:22 (8,751 KB) [v3] 2023-10-25 10:56:14 (8,751 KB) [v4] 2024-04-17 00:13:18 (9,472 KB)
- **revisions**：- - **version**：v1
    - **date_kst**：2023-07-26
  - - **version**：v2
    - **date_kst**：2023-10-24
  - - **version**：v3
    - **date_kst**：2023-10-25
  - - **version**：v4
    - **date_kst**：2024-04-17
- **note**：The paper revision time cannot be treated as the data release date. Existing 2026-H2 evidence retains the original collection date.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 饱和程度

The highest aggregate result on the official Sheet is 86.1%, which is not the same as an independent evaluation under one protocol; the original human figure of 78.24% is only on tasks selected by a template, and it should not be compared directly with system results on the full set.

Sources: [1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv) (accessed 2026-11-08 ).

### 污染、冲突与限制

Fixed templates, public tests, and fuzzy judging by an LLM affect how generalization is interpreted; the version of the website environment needs to be fixed.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 后续工作与衍生

VisualWebArena adds visual conditions; WebArena-Infinity generates new environments and verifiable tasks from documents. The official HF set webarena-infinity-trajectories contains successful Infinity trajectories, and it is not the original test card of the canonical812 tasks; it must not take the place of that data identity.

Sources: [1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08  ) ; [2](https://huggingface.co/datasets/webarena-x/webarena-infinity-trajectories/raw/main/README.md) (accessed 2026-11-08 ).

## Leaderboard snapshot

### 快照采集日

2026-11-08

Sources: [1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv) (accessed 2026-11-08 ).

### Official leaderboard

https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/edit

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08  ) ; [2](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv) (accessed 2026-11-08 ).

### 第三方覆盖

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### Official Sheet main leaderboard (participant aggregate)

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| 1 | Narada AI Code | 86.1 % | task success rate | 09/2026；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 2 | Deepseek v3.2 | 74.3 % | task success rate | 02/2026；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 3 | OpAgent | 71.6 % | task success rate | 01/2026；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 4 | ColorBrowserAgent | 71.2 % | task success rate | 12/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 5 | Claude Code + GBOX MCP | 68.0 % | task success rate | 10/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 6 | DeepSky Agent | 66.9 % | task success rate | 09/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 7 | Narada AI | 64.2 % | task success rate | 10/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 8 | IBM CUGA | 61.7 % | task success rate | 02/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 9 | OpenAI Operator | 58.1 % | task success rate | 01/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 10 | Jace.AI | 57.1 % | task success rate | 08/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 11 | GLM-4-32B + Qwen2.5-VL-7B | 56.3 % | task success rate | 06/2026；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 12 | WebOperator + GPT-4o | 54.6 % | task success rate | 12/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 13 | ScribeAgent + GPT-4o | 53.0 % | task success rate | 12/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 14 | AgentSymbiotic | 52.1 % | task success rate | 01/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 15 | Learn-by-Interact | 48.0 % | task success rate | 01/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 16 | AgentOccam-Judge | 45.7 % | task success rate | 10/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 17 | A3-Qwen3.5-9B | 42.1 % | task success rate | 04/2026；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 18 | WebPilot | 37.2 % | task success rate | 08/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 19 | GUI-API Hybrid Agent | 35.8 % | task success rate | 10/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 20 | Agent Workflow Memory | 35.5 % | task success rate | 09/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 21 | SteP | 33.5 % | task success rate | 04/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 22 | TTI | 26.1 % | task success rate | 06/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 23 | BrowserGym + GPT-4 | 23.5 % | task success rate | 04/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 24 | AgentTrek-1.0-32B | 22.4 % | task success rate | 01/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 25 | GPT-4 + Auto Eval | 20.2 % | task success rate | 04/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 26 | GPT-4o + Tree Search | 19.2 % | task success rate | 06/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 27 | AutoWebGLM | 18.2 % | task success rate | 04/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 28 | NNetNav | 16.3 % | task success rate | 01/2025；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 29 | gpt-4-0613 | 14.9 % | task success rate | 06/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 30 | gpt-4o-2024-05-13 | 13.1 % | task success rate | 05/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 31 | gpt-4-0613 | 11.7 % | task success rate | 06/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 32 | Patel et al + 2024 | 9.36 % | task success rate | 05/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 33 | gpt-3.5-turbo-16k-0613 | 8.87 % | task success rate | 03/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 34 | Qwen-1.5-chat-72b | 7.14 % | task success rate | 09/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 35 | Gemini Pro | 7.12 % | task success rate | 12/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 36 | Llama3-chat-70b | 7.02 % | task success rate | 04/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 37 | Synatra-CodeLLama7b | 6.28 % | task success rate | 10/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 38 | Lemur-chat-70b | 5.3 % | task success rate | 10/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 39 | Agent Flan | 4.68 % | task success rate | 03/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 40 | CodeLlama-instruct-34b | 4.06 % | task success rate | 08/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 41 | AgentLM-70b | 3.81 % | task success rate | 10/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 42 | Llama3-chat-8b | 3.32 % | task success rate | 04/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 43 | CodeAct Agent | 2.3 % | task success rate | 02/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 44 | AgentLM-13b | 1.6 % | task success rate | 10/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 45 | Mixtral | 1.39 % | task success rate | 01/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 46 | AgentLM-7b | 0.74 % | task success rate | 10/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 47 | FireAct | 0.25 % | task success rate | 10/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| 48 | CodeLlama-instruct-7b | 0.0 % | task success rate | 08/2023；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |

#### Official Sheet/Reddit subset

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | AutoGuide | 43.7 % | task success rate | 03/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |
| — | AutoManual | 65.1 % | task success rate | 09/2024；https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |

#### Official Sheet / the human subset selected by template

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Human | 78.24 % | task success rate | https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv |

#### Original paper v4 Table 2/CoT=True/UA_hint=True/all

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | TEXT-BISON-001 | 5.05 % | task success rate all | https://arxiv.org/pdf/2307.13854 |
| — | GPT-3.5 | 8.75 % | task success rate all | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 11.7 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=True/UA_hint=True/achievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | TEXT-BISON-001 | 4.0 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-3.5 | 6.44 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 8.63 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=True/UA_hint=True/unachievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | TEXT-BISON-001 | 27.78 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-3.5 | 58.33 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 77.78 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=False/UA_hint=True/all

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 6.41 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=False/UA_hint=True/achievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 4.9 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=False/UA_hint=True/unachievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 38.89 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=False/UA_hint=False/all

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 5.1 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=False/UA_hint=False/achievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 4.9 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=False/UA_hint=False/unachievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 8.33 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=True/UA_hint=False/all

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 6.16 % | task success rate all | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 14.41 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=True/UA_hint=False/achievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 6.06 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 13.02 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=True/UA_hint=False/unachievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | GPT-3.5 | 8.33 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 44.44 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=None/UA_hint=True/all

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Human | 78.24 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=None/UA_hint=True/achievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Human | 77.3 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### Original paper v4 Table 2/CoT=None/UA_hint=True/unachievable

| Rank | Model | Value | Metric / scope | Settings and date |
|---|---|---|---|---|
| — | Human | 100.0 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

Sources: [1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv) (accessed 2026-11-08  ) ; [2](https://arxiv.org/pdf/2307.13854) (accessed 2026-11-08 ).

### Coverage note

All 51 rows of the official Sheet were read: 48 on the main leaderboard, 2 Reddit subsets, and 1 human-template sample. Misaligned fields in the subset CSV were restored to the original values, and the original source_date month is retained. All 8 configurations from Table 2 of original paper v4 were appended, with scores in the three classes all, achievable, and unachievable. 14.41 belongs to Table 2, not to Table 3. Sheet14.9 and the paper's 14.41 are not forcibly merged.

Sources: [1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv) (accessed 2026-11-08  ) ; [2](https://arxiv.org/pdf/2307.13854) (accessed 2026-11-08 ).

## Contact

### 公开联系邮箱

- shuyanzh@cs.cmu.edu
- fangzhex@cs.cmu.edu
- gneubig@cs.cmu.edu

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### 问题反馈

https://github.com/web-arena-x/webarena/issues

> Public repository feedback entry point; no question was sent.

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08 ).

### 官方讨论渠道

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

### 隐私与数据使用

Unverified

> The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Source: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08).

## Original files

### 源站论文PDF

https://arxiv.org/pdf/2307.13854

> Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

Sources: [1](https://arxiv.org/pdf/2307.13854) (accessed 2026-11-08 ).

### SHA-256

f9731b92bc3d29a2ea7b5f9cb46b48540c76bc3f84a57e0c48fc37ea73107f95

> Original bytes of the PDF downloaded again. The existing copy was not overwritten.

Sources: [1](https://arxiv.org/pdf/2307.13854) (accessed 2026-11-08 ).

### 字节数

9128123

Sources: [1](https://arxiv.org/pdf/2307.13854) (accessed 2026-11-08 ).

### Folder

- **id**：1nFh380aqu7esGjwpLfEm0xF85brhlOzU
- **webViewLink**：

Sources: [1]( 2026-11-07 ).

### Other documents

- - **type**：Chinese-language introductory Google Doc
  - **id**：1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4
  - **webViewLink**：

> The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [1](https://webarena.dev/og/) (accessed 2026-11-08  ) ; [2]( 2026-11-07 ).

### 原文归档

- **id**：1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L
- **webViewLink**：

Sources: [1]( 2026-11-07 ).

## Changelog

### 本页修订

- - **date**：2026-11-07
  - **timezone**：
  - **change**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- - **date**：2026-11-07
  - **timezone**：
  - **round**：1 / 深度实证复核
  - **change**：补v0.2.0/AgentLab运行口径，重读官方Sheet当前前三和H2收录；并列论文14.41与Sheet14.9历史差异。
- - **date**：2026-11-08
  - **timezone**：
  - **round**：2
  - **change**：逐项打开arXiv摘要与PDF全文、Official README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

Sources: [1](https://arxiv.org/abs/2307.13854) (accessed 2026-11-08  ) ; [2](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md) (accessed 2026-11-08 ).
