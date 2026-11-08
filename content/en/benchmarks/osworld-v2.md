# OSWorld 2.1

> Benchmark Constitution, verification 2026-11-08. Unknowns remain "Unverified"; an access date is not an experiment date.

OSWorld2.x measures the ability to complete long-horizon real workflows on a virtual desktop and on self-hosted websites. The emphasis is constraints that cross applications, and recovery of state, rather than an isolated GUI click. This page distinguishes paper 2.0, recommended environment 2.1, the full set and the offline set, and binary completion from partial completion.

Sources: [Original description](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08); [Results evidence](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10) (accessed 2026-11-08); [Results evidence](https://www.anthropic.com/claude-haiku-5-5) (accessed 2026-11-07)

## Basic information

### Short name

OSWorld 2.1

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Full name

OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks (the release recommended at present is osworld-v2.1)

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08); [2](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Benchmark version

osworld-v2.1 (the bug-fix release of 2026-09-16, which the official source recommends). The earlier releases osworld-v2-2026.08.08 and osworld-v2-2026.06.24 are still Active.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Paper version

arXiv v2 (revised 2026-07-13; different from the osworld-v2.1 environment version)

Sources: [1](https://arxiv.org/abs/2606.29537) (accessed 2026-11-08)

### Release date

2026-06-26 (first release of the paper, the environment, and osworld-v2-2026.06.24); osworld-v2.1 was released on 2026-09-16

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Section

Agent

Note: Benchmark Constitution editorial filing.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Field tags

- 计算机使用
- Long-horizon desktop workflow

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 许可与适用范围

Apache-2.0 (code repository)

Note: Task classes and the complete assets are distributed as a gated dataset on Hugging Face, and the data license is separately Unverified.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Paper

https://arxiv.org/abs/2606.29537

Sources: [1](https://arxiv.org/abs/2606.29537) (accessed 2026-11-08); [2](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Code repository

https://github.com/xlang-ai/OSWorld-V2

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 数据地址

https://huggingface.co/datasets/xlangai/osworld_v2_tasks

Note: gated; complete assets at xlangai/osworld_v2_assets_gated.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Official homepage

https://osworld-v2.xlang.ai

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08); [2](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Paper title

OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

## Origin and maintenance

### 发起与机构归属

XLANG Lab, University of Hong Kong

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 合作关系

UCSD, Columbia, UCSB, Mila, Uniphore, Snorkel AI, UW-Madison, Alibaba Qwen, Ohio State, Simular, and NeoCognition (author affiliations).

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Authors

Mengqi Yuan, Zilong Zhou, and Xinzhuang Xiong (co-first authors), among others; corresponding and last authors include Tianbao Xie and Tao Yu

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Current maintainer

xlang-ai (GitHub organization)

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 资助与支持

A Google Research gift fund provided support; Snorkel AI is the research & data partner listed in the paper’s acknowledgements.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

## Design goals

### Abilities measured

Real end-to-end long-horizon computer use: cross-source reasoning, visual-spatial precision, implicit-state inference, tracking of multiple states, conflict disambiguation, multimodal editing, tutorial following, and related demands.

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 设计背景与适用边界

Short-horizon evaluations of desktop actions, such as OSWorld1.0, are not enough to measure state that crosses applications, new information arising in the middle of a task, implicit constraints, and verification of the final deliverable; 2.x takes the complete long-horizon workflow, rather than an isolated click, as the unit of evaluation.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

## Construction

### 题目或数据来源

Workflows are built from real input materials and cross-referenced with stateful user-profile data; 31 self-hosted simulated websites and a self-hosted GitLab are used.

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 构建者背景

Designed jointly by XLANG and the collaborating teams; Appendix A of the paper lists Mengqi Yuan as responsible for design and annotation, Zilong Zhou and Xinzhuang Xiong as taking part in the review of the tasks, and Tao Yu as the person who initiated the work and directed it.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

### Review process

A coding agent first generates the unit tests of the rubric; two independent human annotators complete the task from end to end and check each other's work for whether it can be solved and for the weights; trajectories from several frontier agents are checked for omissions. Wherever a stage has a disagreement it is revised, and a task is deleted if the ambiguity cannot be removed or if the task is not feasible.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

### Quality control

Review by hand, adversarial testing, and an audit of trajectories check at the same time for reward hacking and for points taken off a correct answer by mistake. The model judge accounts for only 11.53% of the total score, and for no more than 50% of any one question, and it is checked on labeled states of a correct answer and of a confusable error. At the time of release, the code, the tasks, the assets, the website, and the VM images are locked.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08); [2](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 去污染与泄漏边界

Official task classes are distributed through a gated HF dataset and are not placed on public GitHub, in order to reduce leakage and to keep an agent under evaluation from looking up, online, the answers or the details of the evaluator.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

## Data format

### Size

108 long-horizon tasks, covering 7 professional domains and 21 subcategories; 27.25 scoring checkpoints on average; humans take more than 1 hour on 69.6% of the tasks

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 题型与交付物

Interactive desktop/web workflow tasks (the agent operates in a virtual machine)

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Modalities

- 屏幕图像
- 文本
- File/multimedia

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Languages

The task descriptions and examples in the public paper are in English and involve several applications and original files; this is not a basis for claiming that every file is in a single language only.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

### Difficulty

Human median about 1.6 hours; mean agent steps >250

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Public and hidden splits

There is also an Offline set (the chart on the official site distinguishes Full set / Offline set); the task class is gated public (automatic approval)

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08); [2](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

## Evaluation

### Metrics

The primary metric is the binary completion rate within 500 steps (Binary reward), and partial scores are also reported (Partial reward)

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### Scoring

Multiple checkpoints are scored for each task (27.25 on average), and binary completion requires that all of them be met.

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 提示与运行设置

The official charts use 500 steps as the default budget and record reasoning effort and the batch or single tool setting; historical experiments at 100, 300, and 500 steps are kept separate. Under the recommended 2.1 release, the website, the tasks, the assets, and the images are locked together. This is not one general CoT prompt.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08); [2](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10) (accessed 2026-11-08); [3](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08); [4](https://raw.githubusercontent.com/xlang-ai/OSWorld-V2/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md) (accessed 2026-11-08)

### 评测脚本

The repository provides run and aggregation scripts such as run.py / main.py / show_result.py, and the setup-osworld skill

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 可比性提醒

2.0/2.1 cannot be compared directly with OSWorld 1.0; the Full subset and the Offline subset cannot be mixed in one comparison; an “offline subset” score reported by a vendor differs from the score on the full set; the same release version is required.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08); [2](https://www.anthropic.com/claude-haiku-5-5) (accessed 2026-11-07)

## Current status

### Date checked

2026-11-08

Sources: [1](https://arxiv.org/abs/2606.29537) (accessed 2026-11-08)

### 数据版本与更新

```json
{
 "version": "osworld-v2.1 (the bug-fix release of 2026-09-16, which the official source recommends). The earlier releases osworld-v2-2026.08.08 and osworld-v2-2026.06.24 are still Active."
 "evidence_2026_h2": [
 {
 "url": "https://openai.com/index/introducing-gpt-6-1-terra/"
 "date": "2026-11-07"
 "organization": "OpenAI"
 "note": "The GPT-6.1 Terra release post uses OSWorld 2.1 to compare multi-step desktop operations."
 }
 {
 "url": "https://www.anthropic.com/claude-haiku-5-5"
 "date": "2026-10-07"
 "organization": "Anthropic"
 "note": "The Haiku release table and cost chart of October 7 report the OSWorld 2.1 offline subset."
 }
 {
 "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
 "date": "2026-09-28"
 "organization": "Epoch AI"
 "note": "On September 28, Epoch reviewed OSWorld 2.1 as Flawed."
 }
 ]
 "trending": {
 "heat_confidence": "A"
 "summary": "The long-horizon desktop tasks released in September appear both in the OpenAI model-release comparisons and in the Anthropic model-release comparisons of October–November, and Epoch AI also has a review."
 }
}
```

Note: Recent popularity evidence is taken from candidate studies and reopened pages; grade A: adopted independently by multiple frontier laboratories or evaluation organizations.

Sources: [1](https://openai.com/index/introducing-gpt-6-1-terra/) (accessed 2026-11-07); [2](https://www.anthropic.com/claude-haiku-5-5) (accessed 2026-11-07); [3](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks) (accessed 2026-11-07)

### 论文修订记录

```json
{
 "arxiv": [
 {
 "version": "v1"
 "submitted_at": "2026-06-29 "
 }
 {
 "version": "v2"
 "submitted_at": "2026-07-13 "
 }
 ]
 "benchmark_release_note": "The first submission of the paper and the v2 revision are at arXiv:2606.29537. The environment release is separate: first released on 2026-06-26, updated on 2026-08-08, and osworld-v2.1 on 2026-09-16. The paper version cannot stand in for the environment version."
}
```

Sources: [1](https://arxiv.org/abs/2606.29537) (accessed 2026-11-08)

### 饱和程度

The highest configuration already recorded for the official data at v2.1/full/500 steps/e2e is Claude Opus 5 (max, batch tool) at 44.33%; a high offline score from a vendor cannot be used to claim that the full set is saturated.

Sources: [1](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10) (accessed 2026-11-08)

### 争议与已知问题

On 2026-09-28, Epoch AI rated OSWorld 2.1 Flawed (on the basis of candidate research evidence); the description of the specific defect is Unverified.

Sources: [1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks) (accessed 2026-11-07)

### 衍生与后续使用

The predecessor is OSWorld 1.0 (xlang-ai/OSWorld); this entry records only the 2.x series.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (date the web page was accessed; dates of historical results are kept separately).

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 官方结果入口

https://osworld-v2.xlang.ai

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 第三方入口

https://www.anthropic.com/claude-haiku-5-5

Sources: [1](https://www.anthropic.com/claude-haiku-5-5) (accessed 2026-11-07)

### 分赛道结果

- {"model": "Claude Opus 5", "score": 44.33, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "MuseSpark 1.3", "score": 39.25, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.3-1015-merged-106tasks.zip", "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 36.89, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 33.33, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 33.01, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 18.81, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "MuseSpark 1.2", "score": 15.84, "track": "Official chart/v2.1/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.2-1015-merged-105tasks.zip", "binary_success_threshold": null, "rank": 7}
- {"model": "Claude Opus 5", "score": 77.67, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 73.11, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "MuseSpark 1.3", "score": 69.56, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.3-1015-merged-106tasks.zip", "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 68.92, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 64.85, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 59.09, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "MuseSpark 1.2", "score": 44.08, "track": "Official chart/v2.1/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.2-1015-merged-105tasks.zip", "binary_success_threshold": null, "rank": 7}
- {"model": "Claude Opus 5", "score": 48.65, "track": "Official chart/v2.1/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 39.74, "track": "Official chart/v2.1/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 37.18, "track": "Official chart/v2.1/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 34.67, "track": "Official chart/v2.1/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 22.08, "track": "Official chart/v2.1/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 79.2, "track": "Official chart/v2.1/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 72.03, "track": "Official chart/v2.1/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 70.55, "track": "Official chart/v2.1/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 66.25, "track": "Official chart/v2.1/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 60.34, "track": "Official chart/v2.1/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 31.43, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 30.21, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 28.98, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 27.34, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 25.33, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 22.32, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 5", "score": 68.31, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 67.67, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 63.79, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 62.72, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 60.49, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 54.89, "track": "Official chart/v2026.08.08/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 5", "score": 34.72, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 33.38, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 32.69, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 28.1, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 27.13, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "GPT-5.6 Sol", "score": 24.63, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 5", "score": 24.61, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "GPT-5.6 Sol", "score": 20, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "GPT-5.6 Sol", "score": 17.56, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 9}
- {"model": "GPT-5.6 Sol", "score": 7.32, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "GPT-5.6 Sol", "score": 3.41, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "none", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 11}
- {"model": "Claude Opus 5", "score": 70.19, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 70.14, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 65.92, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 64.13, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "GPT-5.6 Sol", "score": 60.6, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 60.26, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "GPT-5.6 Sol", "score": 56.03, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "Claude Opus 5", "score": 55.22, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "GPT-5.6 Sol", "score": 49.01, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 9}
- {"model": "GPT-5.6 Sol", "score": 29.63, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "GPT-5.6 Sol", "score": 16.43, "track": "Official chart/v2026.08.08/offline/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "none", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 11}
- {"model": "Claude Opus 4.8", "score": 20.6, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.8", "score": 18.52, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 4.7", "score": 18.2, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 4.7", "score": 13.9, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "GPT-5.5", "score": 13.0, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Sonnet 4.6", "score": 9.3, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Sonnet 4.6", "score": 8.3, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "MiniMax M3", "score": 4.6, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "Kimi 2.6", "score": 4.6, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "Qwen 3.7-Plus", "score": 2.8, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "thinking", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "Claude Opus 4.8", "score": 54.8, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "GPT-5.5", "score": 49.5, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 4.8", "score": 49.33, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 4.7", "score": 49.1, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 4.7", "score": 48.91, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Sonnet 4.6", "score": 41.5, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Sonnet 4.6", "score": 33.9, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "MiniMax M3", "score": 22.3, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "Kimi 2.6", "score": 22.1, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 9}
- {"model": "Qwen 3.7-Plus", "score": 21.5, "track": "Official chart/v2026.06.24/full/500 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "thinking", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "GPT-5.5", "score": 13.0, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.7", "score": 4.6, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 4.6, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "medium", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 4.6, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "MiniMax M3", "score": 1.9, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Kimi 2.6", "score": 1.9, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "GPT-5.5", "score": 46.7, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.7", "score": 20.3, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 20.0, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Sonnet 4.6", "score": 14.2, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "medium", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "MiniMax M3", "score": 8.2, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Kimi 2.6", "score": 7.1, "track": "Official chart/v2026.06.24/full/150 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 4.7", "score": 13.0, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "GPT-5.5", "score": 13.0, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Sonnet 4.6", "score": 8.3, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "medium", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Sonnet 4.6", "score": 6.5, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Kimi 2.6", "score": 4.6, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "MiniMax M3", "score": 3.7, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Qwen 3.7-Plus", "score": 1.9, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "thinking", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "GPT-5.5", "score": 49.5, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.7", "score": 39.8, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 35.8, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Sonnet 4.6", "score": 29.4, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "medium", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Qwen 3.7-Plus", "score": 16.6, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "thinking", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "MiniMax M3", "score": 16.6, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Kimi 2.6", "score": 14.4, "track": "Official chart/v2026.06.24/full/300 steps/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "Sai w/ Claude Opus 5", "score": 41.67, "track": "Official chart/v2.1/full/500 steps/agent/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/simular-ai/sai-osworld-v21-reference-runs", "binary_success_threshold": null, "rank": 1}
- {"model": "Sai w/ Claude Opus 5", "score": 79.38, "track": "Official chart/v2.1/full/500 steps/agent/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/simular-ai/sai-osworld-v21-reference-runs", "binary_success_threshold": null, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 37.65, "track": "Official chart/v2026.08.08/full/450 steps/agent/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v0808_20260915", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 66.62, "track": "Official chart/v2026.08.08/full/450 steps/agent/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v0808_20260915", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 44.44, "track": "Official chart/v2.1/full/450 steps/agent/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v21_20261012", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 75.97, "track": "Official chart/v2.1/full/450 steps/agent/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 ", "release": "v2.1", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "Official chart data; not ranked together with vendor self-reports", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v21_20261012", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Claude Sonnet 5.5", "score": 83.9, "metric": "OSWorld 2.1 offline subset accuracy (vendor self-report)", "result_type": "Vendor release-page self-report (not an official leaderboard)", "source_date": "2026-10-07", "collected_at": "2026-11-07 (historical evidence already on file; not reopened)", "track": "Anthropic vendor self-report/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 1}
- {"model": "Claude Haiku 5.5", "score": 72.4, "metric": "OSWorld 2.1 offline subset accuracy (vendor self-report)", "result_type": "Vendor release-page self-report (not an official leaderboard)", "source_date": "2026-10-07", "collected_at": "2026-11-07 (historical evidence already on file; not reopened)", "track": "Anthropic vendor self-report/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 2}
- {"model": "GPT-6 Luna", "score": 48.9, "metric": "OSWorld 2.1 offline subset accuracy (vendor self-report)", "result_type": "Vendor release-page self-report (not an official leaderboard)", "source_date": "2026-10-07", "collected_at": "2026-11-07 (historical evidence already on file; not reopened)", "track": "Anthropic vendor self-report/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 3}
- {"model": "Claude Haiku 4.5", "score": 15.7, "metric": "OSWorld 2.1 offline subset accuracy (vendor self-report)", "result_type": "Vendor release-page self-report (not an official leaderboard)", "source_date": "2026-10-07", "collected_at": "2026-11-07 (historical evidence already on file; not reopened)", "track": "Anthropic vendor self-report/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 4}

Sources: [1](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10) (accessed 2026-11-08); [2](https://www.anthropic.com/claude-haiku-5-5) (accessed 2026-11-07)

### 覆盖边界

The public official-results.json was found from the official site's script (updatedAt=2026-10-15). All results are included in full and split into tracks by release, full/offline, step count, agent category, and binary/partial metrics. Rows whose JSON does not state release or scope explicitly use only the default declared in the file. Rank is computed from the published point values within the same track. A previously recorded Anthropic self-report is retained as a separate historical source, and the access date is not altered.

Sources: [1](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10) (accessed 2026-11-08)

## Contact

### 公开项目邮箱

- yuanmengqi732@gmail.com
- zzl0712@connect.hku.hk

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 公开反馈渠道

https://github.com/xlang-ai/OSWorld-V2/issues

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 官方社交渠道

- https://x.com/XLangNLP/status/2070517498974253269
- https://discord.com/invite/4Gnw7eTEZR

Sources: [1](https://osworld-v2.xlang.ai) (accessed 2026-11-08)

### 联系方式收录原则

Benchmark Constitution includes only project contact channels that the paper or the official site has made public, and it does not collect private information; this is not a certification of an external site’s privacy policy.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08)

## Original files

### 既存论文原件

Unverified

Note: This group does not upload, as the task requires; the original PDF URL is in original_files.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### 原始PDF地址

https://arxiv.org/pdf/2606.29537

Sources: [1](https://arxiv.org/abs/2606.29537) (accessed 2026-11-08)

### 下载SHA-256

a1e4d52bbf3a5fae8e3153835adcfd5f314efc45bbc8e9e73b19bcbf20d3fefc

Note: Checksum of the bytes downloaded on 2026-11-08. Nothing was overwritten or uploaded, so this does not establish that an existing original is the same version.

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

### 下载字节数

```json
25962973
```

Sources: [1](https://arxiv.org/pdf/2606.29537) (accessed 2026-11-08)

### 既存文件夹

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

### Other documents

Unverified

Note: The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://github.com/xlang-ai/OSWorld-V2) (accessed 2026-11-08)

## Changelog

Latest review
Latest review

Sources: [1](https://arxiv.org/abs/2606.29537) (accessed 2026-11-08)
