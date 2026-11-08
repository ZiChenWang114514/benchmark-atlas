# Robo-bench

> Verification date: 2026-11-08. The access date is not the publication date or the run date; a field that cannot be confirmed remains Unverified.

Robo-bench places robot control in a real-time MuJoCo closed loop: the model does not only generate a plan. It must itself write perception, planning, and low-level control, and it bears the consequences of the physical system continuing to run while it thinks. The 24 tasks span robot arms and humanoids; the score measures ordered milestones, not the proportion of complete tasks passed.

Guide source: [Official materials](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08); specific facts and historical access dates are given in the individual fields.

## Basic information

### Short name

Robo-bench

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Full name

Robo-bench

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Benchmark version

2026-10-13 official leaderboard snapshot

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Paper version

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Release date

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Section

机器人与具身

Note: Editorial filing. It does not represent an official classification.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Field tags

- Closed-loop robot control
- 运动规划
- 具身感知
- 实时仿真

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 许可与适用范围

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Paper

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Code repository

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 数据地址

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Official homepage

https://www.vals.ai/benchmarks/robo_bench

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Paper title

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Origin and maintenance

### 机构与发起关系

Vals AI

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 合作机构/署名单位

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Authors

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 当前维护入口

Vals AI

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Funders

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Design goals

### Abilities measured

Using only the robot specification, sensors, and cameras, it autonomously writes perception, planning, and low-level control in a real-time physical environment.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Design background

No motion planner or balance controller is preinstalled; it directly measures a general agent's ability to control a robot, and model thinking latency is counted in real time.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Construction

### 题目或数据来源

A 7-degree-of-freedom Franka Panda arm and a 29-degree-of-freedom Unitree G1 humanoid in MuJoCo; 24 tasks cover assembly, dexterous manipulation, dynamics, mobile manipulation, and other skills.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 出题背景

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Review process

The reference solution for each task must succeed on all five seeds, and a stationary agent should not succeed; the simulator sits on a side the agent cannot read and signs the score.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Quality control

The reference solution for each task must succeed on all five seeds, and a stationary agent should not succeed; the simulator sits on a side the agent cannot read and signs the score.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 去污染措施

21 tasks are kept private, so that they do not enter training data and are not used for targeted tuning of an agent or a harness; 3 tasks are public. This measure is not an independent audit of the training data of models that already exist.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Data format

### Size

24 tasks: 13 robot arms and 11 humanoids; once per model per task, with a single seed.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Question types

Closed-loop action and sensing tasks; three public examples: a balance scale, block-assembly instructions, and a ninja route.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Modalities

- 摄像头图像
- 深度图
- 状态传感器
- 电机命令
- 代码

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Languages

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Difficulty

The tasks cover assembly, dexterous manipulation, dynamics, reasoning, stacking, tool use, and humanoid multi-stage obstacles; the reference solution succeeds on all five seeds, and a stationary agent does not. No single human difficulty scale is used.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 数据划分

3 tasks are public, and another 21 tasks remain private (stated explicitly on the official site).

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Evaluation

### Metrics

Each task is scored 0–100 by sequential milestones and the 24 tasks are averaged; robot-arm/humanoid breakdowns and time to first action are also listed.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Scoring

Milestones must be achieved in order; the task total is 100 and is verified on the simulation side. A score of 28.33 cannot be interpreted as 28.33% of tasks completely succeeding.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 提示与运行设置

Each episode is three minutes of real wall-clock time, with no preparation time; each model uses the vendor coding agent's highest reasoning setting, and there is no ready-made controller.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 评测脚本

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 可比性提醒

Each task is run only once; the official note says that on repeated runs the total score can vary by about 10 points, and small gaps carry no guarantee of significance. Harnesses from different vendors also affect the score.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Current status

### Date checked

2026-11-08

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 数据版本与更新

- **version**：2026-10-13 official leaderboard snapshot
- **trending**：B
- **heat_evidence**：On 2026-10-13 Vals updated 7 models, mainly a showcase of a proprietary test from a single organization (B), not wide adoption that has been demonstrated.
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/robo_bench", "date": "2026-11-07", "date_type": "observed_on", "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."}]

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 论文修订记录

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 饱和程度

Among the seven official models in this set, the highest average milestone score is 28.33/100; the humanoid component of every model is below 2/100. This snapshot still leaves a substantial share unsolved, and the average milestone score is not treated as the success rate on the complete task.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 争议与已知问题

Each task is run only once; the official note says that on repeated runs the total score can vary by about 10 points, and small gaps carry no guarantee of significance. Harnesses from different vendors also affect the score.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Derivative benchmarks

A simulated-robot evaluation, which is not a safety certification for deployment on a physical robot; robot-platform breakdowns are not established as a separate benchmark.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Leaderboard snapshot

### 快照访问日期

2026-11-08 (access date, not the experiment run date)

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 官方榜单入口

https://www.vals.ai/benchmarks/robo_bench

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 第三方入口

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 可核验结果

- {"rank": 1, "model": "GPT-6.1 Sol", "score": 28.33, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$4.97", "time_to_first_move": "79.89s", "source_update_date": "2026-10-13"}
- {"rank": 2, "model": "GPT-6 Astra", "score": 23.33, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$28.48", "time_to_first_move": "74.88s", "source_update_date": "2026-10-13"}
- {"rank": 3, "model": "Claude Opus 5.5", "score": 14.58, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$11.38", "time_to_first_move": "2m07s", "source_update_date": "2026-10-13"}
- {"rank": 4, "model": "Wonder Full", "score": 10.42, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$19.68", "time_to_first_move": "2m14s", "source_update_date": "2026-10-13"}
- {"rank": 5, "model": "Claude Fable 5.1", "score": 5.83, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$20.40", "time_to_first_move": "2m04s", "source_update_date": "2026-10-13"}
- {"rank": 6, "model": "Gemini 4 Argon", "score": 0.83, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$17.33", "time_to_first_move": "2m32s", "source_update_date": "2026-10-13"}
- {"rank": 7, "model": "Grok 4.7", "score": 0.21, "metric": "Mean milestone score over 24 tasks (0–100, not the rate of complete success)", "track": "Vals official; each vendor's highest-reasoning coding agent; one seed/task; 3 minutes", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 ", "result_type": "Exact transcription of the source table; not a rerun by this repository", "estimated_api_cost": "$11.25", "time_to_first_move": "2m31s", "source_update_date": "2026-10-13"}

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 榜单覆盖边界

The official leaderboard table of 7 models is transcribed in full, without using the one-decimal approximations on the homepage. The page update date is 2026-10-13. The total score from repeated runs of a single seed can fluctuate by about 10 points, so a small gap cannot be claimed as a significant ranking. Entry points for the paper document, the code repository, and the HF data card remain Unverified.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Contact

### 公开研究联系

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 公开反馈渠道

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 官方社交账号

https://x.com/ValsAI

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 联系方式原则

Only research and feedback entry points made public on the official project web page are recorded; private contact details are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-08)

## Original files

### 论文原件

Unverified

Note: The page for this group was built only locally and was not uploaded; no archive link is fabricated.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 原始PDF地址

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 原始文件SHA-256

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### 原始文件字节数

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Folder

Unverified

Note: The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

### Other documents

- {"type": "Official web page/paper opened", "url": "https://www.vals.ai/benchmarks/robo_bench"}

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)

## Changelog

Latest review
Latest review

Sources: [1](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08); [2](https://www.vals.ai/benchmarks/robo_bench) (accessed 2026-11-08)
