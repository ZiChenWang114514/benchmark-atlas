# FrontierCode

> Benchmark Constitution, research snapshot 2026-11-07. The collection time is not the time a score was actually run, or the leaderboard update time.

FrontierCode takes, as its standard, whether a maintainer would be willing to merge the change, and it includes functionality, discipline of scope, tests, and the conventions of the repository in a weighted score. Version 2.0 is rebuilt as 132 questions; this page distinguishes the official Cognition leaderboard from the Stirrup reproduction by Artificial Analysis, and scores from the two harnesses cannot be joined into one ranking.

Latest review

## Basic information

### Short name

FrontierCode

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Full name

FrontierCode

Note: The official name is retained, and the paper title is not automatically expanded into a full name.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Benchmark version

FrontierCode 2.0; 1.0 and 1.1 are retained as historical versions.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### Paper version

Unverified

状态：待核实。

Note: The official method and leaderboard pages were opened, and the corresponding paper or public code asset was not located in the primary sources that were read. The field remains Unverified, and failure to locate it is not written as officially Not disclosed.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Release date

2.0: 2026-10-27 (the official article gives only the date).

Note: Release dates of the original paper and of older versions are kept in the historical material of the latest status; when a source gives only a date, no time zone is inferred.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### Section

Code

Note: Benchmark Constitution editorial filing. Only the main section is counted.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Field tags

- Frontier code-agent capability

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 许可与范围

Unverified

状态：待核实。

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Paper

Unverified

状态：待核实。

Note: The official method and leaderboard pages were opened, and the corresponding paper or public code asset was not located in the primary sources that were read. The field remains Unverified, and failure to locate it is not written as officially Not disclosed.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 代码

Unverified

状态：待核实。

Note: The official method and leaderboard pages were opened, and the corresponding paper or public code asset was not located in the primary sources that were read. The field remains Unverified, and failure to locate it is not written as officially Not disclosed.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Dataset

https://cognition.com/frontiercode#methodology (the official description of the private 132 questions and a partial display of tasks, not a complete public download)

Note: The official method states explicitly that the tasks remain private; no HF dataset or full release repository was fabricated.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Official homepage

https://cognition.com/frontiercode

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Paper title

Unverified

状态：待核实。

Note: The official method and leaderboard pages were opened, and the corresponding paper or public code asset was not located in the primary sources that were read. The field remains Unverified, and failure to locate it is not written as officially Not disclosed.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

## Origin and maintenance

### 发起/作者单位

Cognition

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 合作与支持

More than 20 leading maintainers of open-source projects took part in building the 2.0 tasks.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### Authors

The Cognition Team (byline of the official methods article)

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### Maintainer

Cognition; Artificial Analysis independently runs its evaluation implementation.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### Funders

Unverified

状态：待核实。

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

## Design goals

### Abilities measured

Whether code can be submitted that maintainers are willing to merge: functionally correct, attentive to implicit requirements, consistent with the existing abstractions and compatibility, and without excessive rewriting.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### Design background

A detailed specification and unit tests alone easily miss unstated constraints, maintainability, and merge quality in real development.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

## Construction

### Question sources

Tasks are designed from real repositories that the open-source maintainers maintain themselves; each maintainer spends more than 40 hours on each question; 2.0 adds more security and performance tasks.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 出题者背景

More than 20 world-class open-source developers, not only general annotators.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### Review process

For each question, the maintainers of the repository write the task and the scoring rubric, which then undergoes adversarial testing, calibration, and multi-stage human and automatic review, and each question is reviewed by hand by a Cognition researcher; 80% of the reference solutions in 2.0 differ from the upstream PR.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）；[一手资料2](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### Quality control

More than 20 open-source developers spent more than 40 hours on each question, with review in several stages, both human and automatic. In 2.0, 80% of the reference solutions differ from the upstream PR (60% in 1.0); these are QC statistics stated by the official side, not an independent audit.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 污染控制

The questions stay private; if a scan of the trajectory finds a lookup of a ready-made solution, the score is recorded as 0. Pretraining exposure to the repository itself cannot be ruled out.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

## Data format

### 题量

2.0: 132 tasks; 1.1 Main is 100 questions out of 150 tasks, and the denominators must not be mixed.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 任务形式

Real-repository code edits, comprehensive tests, and a maintainer-scoring rubric.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### Modalities

- 文本
- 源代码
- 仓库环境

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### Languages

The official public examples cover JavaScript (Mock Service Worker) and Kotlin (PostHog Android SDK). The full language distribution is Unverified, and coverage of the full suite is not extrapolated from the examples.

状态：待核实。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 难度与分层

Emphasizes implicit constraints, complete repairs, and a standard of mergeability; 2.0 is not a simple increase in the number of the same questions.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### Public and hidden splits

The scoring tasks are private; the official source and AA make public some example questions and methods, rather than the complete dataset.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

## Evaluation

### Metrics

A weighted rubric score (%) in which tasks have equal weight.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 评分

If any blocking check fails, or a looked-up solution is flagged by trajectory scanning, the entire attempt scores 0; otherwise the items are summed by their weights.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 提示与运行协议

The independent AA implementation uses all 132 questions, repeats each question 3 times, uses the Stirrup harness, and allows at most 500 turns. GPT-6 Luna (medium) is the LLM judge. This setting is not the same as the experiments released officially by Cognition.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 评测脚本

Unverified

状态：待核实。

Note: The official method and leaderboard pages were opened, and the corresponding paper or public code asset was not located in the primary sources that were read. The field remains Unverified, and failure to locate it is not written as officially Not disclosed.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 可比性警示

The official Cognition harness and the independent AA implementation with Stirrup differ; 1.1 and 2.0 differ; the score is not a simple rate of tasks that are entirely correct, and an increase in reasoning effort may also lower the score because the scope has changed.

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

## Current status

### 核查日期

2026-11-07 (materials snapshot date)

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 版本与采用证据

- **current_version**：FrontierCode 2.0; 1.0 and 1.1 are retained as historical versions.
- **release_date**：2.0: 2026-10-27 (the official article gives only the date).
- **version_changes**：2.0 has 132 private tasks. Relative to 1.0, the repositories covered are 55% more and the blocking criteria are 43% more. Relative to 1.1, the reference solution modifies 67% more files and 89% more lines, and the codebase is 25% larger. Implicit correctness and thoroughness, audit tasks, and security tasks are strengthened, while some scope criteria are relaxed. The comparison baseline differs across these figures, and they cannot be mixed.
- **trending**：A
- **why_trending**：On 2026-10-27 Cognition released 2.0 and published a cross-model comparison. AA now independently runs the full 132 questions, 3 times per question, and the current AA Intelligence Index v5.0.1 includes FrontierCode 2.0. Both the publisher and the independent evaluator have in fact adopted it, and it is listed as grade A. The 1.1 scores still reported on October 28 are not mistaken for 2.0.
- **history**：- **previous_version_field**：- **value**：2.0; 1.1 retained as a historical snapshot
 - **sources**：- - **url**：https://cognition.com/blog/frontier-code-2.0
 - **accessed**：2026-11-07
 - **previous_release_date_field**：- **value**：2.0: 2026-10-27 (date of the official article).
 - **sources**：- - **url**：https://cognition.com/blog/frontier-code-2.0
 - **accessed**：2026-11-07
 - **previous_status_field**：- **value**：- **version**：2.0; 1.1 retained as a historical snapshot
 - **evidence_2026_h2**：- - **url**：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
 - **date**：2026-10-28
 - **note**：The Artificial Analysis article of 2026-10-28 explicitly reports results for FrontierCode v1.1 and includes them in the Coding Agent Index. This is an evaluation by an independent organization.
 - **sources**：- - **url**：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
 - **accessed**：2026-11-07
 - - **url**：https://cognition.com/blog/frontier-code-2.0
 - **accessed**：2026-11-07
 - **note**：Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.
 - **previous_results_field**：- **value**：- - **model**：Claude Opus 5.5 (Max, Default Fallback)
 - **score**：46.4
 - **metric**：weighted score (%)
 - **benchmark_version**：2.0/132 questions
 - **result_type**：AA independent current page
 - **source_date**：Unverified (the page does not give a run date or a release date for this result)
 - **collected_at**：2026-11-07
 - **leaderboard_updated_at**：Unverified (the static body text does not mark an overall update time)
 - - **model**：Claude Opus 5.5 (Xhigh, Default Fallback)
 - **score**：43.8
 - **metric**：weighted score (%)
 - **benchmark_version**：2.0/132 questions
 - **result_type**：AA independent current page
 - **source_date**：Unverified (the page does not give a run date or a release date for this result)
 - **collected_at**：2026-11-07
 - **leaderboard_updated_at**：Unverified (the static body text does not mark an overall update time)
 - - **model**：GPT-6 Astra (Max)
 - **score**：42.4
 - **metric**：weighted score (%)
 - **benchmark_version**：2.0/132 questions
 - **result_type**：AA independent current page
 - **source_date**：Unverified (the page does not give a run date or a release date for this result)
 - **collected_at**：2026-11-07
 - **leaderboard_updated_at**：Unverified (the static body text does not mark an overall update time)
 - - **model**：Claude Opus 5.5 (best effort)
 - **score**：45.5
 - **metric**：weighted score (%)
 - **benchmark_version**：2.0
 - **result_type**：Cognition official release experiments
 - **source_date**：2026-10-27
 - **collected_at**：2026-11-07
 - **sources**：- - **url**：https://artificialanalysis.ai/evaluations/frontiercode-2-0
 - **accessed**：2026-11-07
 - - **url**：https://cognition.com/blog/frontier-code-2.0
 - **accessed**：2026-11-07

Note: Historical fields are kept as they were; an old snapshot is not a new ranking. Heat grades are a grading of editorial evidence, not an official certification.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）；[一手资料3](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）

### 材料沿革

History of the official method document: 1.0 was introduced on 2026-06-08, 1.1 was revised on 2026-07-07, and 2.0 rebuilt 132 questions on 2026-10-27. What is recorded here is the method article, not an invented revision number for a paper.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### Saturation

In the official 2.0 release experiments the best result is about 45%, and the official judgment is that it is far from saturated; this is not an absolute conclusion about all future systems.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 污染与局限

Private tasks reduce direct leakage of questions; scope constraints and unstated requirements affect interpretation, and the scope criteria were officially audited and adjusted in 2.0.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 版本/衍生关系

1.0, 1.1, and 2.0 are suite versions, and this repository counts them together as one benchmark.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-07 (snapshot date, not the date of the actual run)

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 官方榜

https://cognition.com/frontiercode

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 其他评测入口

https://artificialanalysis.ai/evaluations/frontiercode-2-0

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 分轨结果（结构化快照）

```json
[
 {
 "rank": 1
 "model": "Claude Opus 5.5"
 "score": 45.5
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 2
 "model": "GPT-6 Astra"
 "score": 42.8
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 3
 "model": "Claude Sonnet 5.5"
 "score": 41.0
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 4
 "model": "Gemini 4 Carbon"
 "score": 40.0
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 5
 "model": "GPT-6.1 Sol"
 "score": 39.0
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 6
 "model": "GPT-6 Sol"
 "score": 34.3
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 7
 "model": "Claude Fable 5.1"
 "score": 32.4
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 8
 "model": "Grok 4.7"
 "score": 28.6
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 9
 "model": "Claude Haiku 5.5"
 "score": 27.7
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 10
 "model": "GPT-5.6 Sol"
 "score": 27.6
 "metric": "weighted rubric score (%)"
 "benchmark_version": "2.0 / 132 tasks"
 "scope": "Cognition official leaderboard JSON-LD ItemList; not the AA Stirrup implementation"
 "source_url": "https://cognition.com/frontiercode"
 "accessed": "2026-11-07"
 "page_changelog_latest": "2026-11-05 (record on the web page of the latest model addition, not the run date of every entry)"
 "settings": "The specific effort and harness of each configuration are Unverified; this structured leaderboard does not list the complete configuration."
 }
 {
 "rank": 1
 "model": "Claude Opus 5.5 (Max, Default Fallback)"
 "score": 46.4
 "metric": "weighted rubric score (%)，Stirrup，3 attempts/task"
 "benchmark_version": "2.0"
 "source_url": "https://artificialanalysis.ai/evaluations/frontiercode-2-0"
 "accessed": "2026-11-07"
 "collected_at": "2026-11-07"
 "leaderboard_updated_at": "Unverified (the current page does not state an overall update time for the leaderboard)"
 "scope": "An independent AA Stirrup implementation, on a separate track from the official leaderboard"
 }
 {
 "rank": 2
 "model": "Claude Opus 5.5 (Xhigh, Default Fallback)"
 "score": 43.8
 "metric": "weighted rubric score (%)，Stirrup，3 attempts/task"
 "benchmark_version": "2.0"
 "source_url": "https://artificialanalysis.ai/evaluations/frontiercode-2-0"
 "accessed": "2026-11-07"
 "collected_at": "2026-11-07"
 "leaderboard_updated_at": "Unverified (the current page does not state an overall update time for the leaderboard)"
 "scope": "An independent AA Stirrup implementation, on a separate track from the official leaderboard"
 }
 {
 "rank": 3
 "model": "GPT-6 Astra (Max)"
 "score": 42.4
 "metric": "weighted rubric score (%)，Stirrup，3 attempts/task"
 "benchmark_version": "2.0"
 "source_url": "https://artificialanalysis.ai/evaluations/frontiercode-2-0"
 "accessed": "2026-11-07"
 "collected_at": "2026-11-07"
 "leaderboard_updated_at": "Unverified (the current page does not state an overall update time for the leaderboard)"
 "scope": "An independent AA Stirrup implementation, on a separate track from the official leaderboard"
 }
]
```

[榜单原始资料](https://cognition.com/frontiercode)（访问 2026-11-07）；[榜单原始资料](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 覆盖范围

Added the top 10 from JSON-LD on the current official Cognition page: 45.5, 42.8, 41.0, and others. AA's 46.4, 43.8, and 42.4 are listed separately. The two are not the same harness, and rank is valid only within each track. The official site has a record of the latest model additions on November 5, and that record is not treated as the run date of each entry. JSON-LD does not carry the complete effort, and the configuration gap is retained.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

## Contact

### 公开研究邮箱

Unverified

状态：待核实。

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 问题反馈

Unverified

状态：待核实。

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 机构公开渠道

https://x.com/cognition (official organization account; sameAs metadata and footer on the official site)

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 隐私政策

https://cognition.com/legal/privacy-policy

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

## Original files

### Paper PDF

Unverified

状态：待核实。

Note: The official method and leaderboard pages were opened, and the corresponding paper or public code asset was not located in the primary sources that were read. The field remains Unverified, and failure to locate it is not written as officially Not disclosed.

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）

### 源站PDF SHA-256

Unverified

状态：待核实。

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 源站PDF字节数

Unverified

状态：待核实。

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### 其他官方资料

- - **type**：An HTML archive of the official methods page (not the paper PDF)
 - **source_url**：https://cognition.com/blog/frontier-code-2.0
 - **accessed**：2026-11-07
 - **sha256**：c0073b17387e29534db8ca821b92b524ba178cdbe36331b6873fdcdc7b49dedb
 - **bytes**：226414
- - **type**：Verified official primary sources
 - **url**：https://cognition.com/frontiercode
 - **accessed**：2026-11-07

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）

### PDF归档

Unverified

仅核对源站PDF和已有归档引用，未上传或覆盖文件。

## Changelog

- - **date**：2026-11-07
 - **change**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- - **date**：2026-11-07
 - **change**：深度优化续核：打开Official README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- - **date**：2026-11-07
 - **change**：近期热门版本复核：2.0 has 132 private tasks. Relative to 1.0, the repositories covered are 55% more and the blocking criteria are 43% more. Relative to 1.1, the reference solution modifies 67% more files and 89% more lines, and the codebase is 25% larger. Implicit correctness and thoroughness, audit tasks, and security tasks are strengthened, while some scope criteria are relaxed. The comparison baseline differs across these figures, and they cannot be mixed. 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。
 - **sources**：- - **url**：https://cognition.com/blog/frontier-code-2.0
 - **accessed**：2026-11-07
 - - **url**：https://artificialanalysis.ai/evaluations/frontiercode-2-0
 - **accessed**：2026-11-07
- - **date**：2026-11-07
 - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位Official README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
