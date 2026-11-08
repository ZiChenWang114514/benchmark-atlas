# SWE-Bench Pro V2

> Benchmark Constitution, in-depth review 2026-11-08.

SWE-Bench Pro V2 is a revision and isolation protocol for the public set in the same series. It is not a new name for SWE-bench Verified. The default 642 tasks, HARD-51, and the retained older 731 questions need to be clearly distinguished. An offline agent, re-evaluation on clean images, and two-way release gating are the key changes in this version. The official Full and HARD leaderboards are recorded separately. Rank(UB) assigns rank by confidence interval rather than by the ordinary rule for tied scores.

[Source 1](https://arxiv.org/abs/2509.16941) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-bench_Pro-os) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) (accessed 2026-11-08); [Source 4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) (accessed 2026-11-08)

## Basic information

### Short name

SWE-Bench Pro V2

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Full name

SWE-Bench Pro V2 (a refreshed edition of the public set, with the evaluation protocol locked).

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Benchmark version

V2 / dataset 2.0.0; default=642 questions, hard=51 questions, v1=731 questions

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### Paper version

v2 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### Release date

2026-09-22 (Scale announcement date)

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Section

Code

> Benchmark Constitution editorial filing.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 领域

```json
[
 "Long-horizon software engineering"
 "Code agent"
]
```

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 许可与适用范围

The evaluation harness and tooling are MIT; task descriptions, patches, and tests are derived from 11 upstream repositories and remain under their own licenses, so MIT is not extended to tasks whose source is GPL.

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2509.16941

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### Code

https://github.com/scaleapi/SWE-bench_Pro-os

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/README.md)（访问 2026-11-08）

### 数据

https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### Official entry

https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Paper title

SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (a paper of the original series; it is not presented as a paper devoted to V2)

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

## Origin and maintenance

### Initiators

Scale AI

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 合作/参与机构

Reflection (joint development of V2)

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Authors

Original series paper: Xiang Deng and Jeff Da (joint first authors), Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean Hendryx, Zifan Wang, Vijay Bharadwaj, Jeff Holm, Raja Aluri, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, and Brad Kenstler. The V2 collaborator Reflection is not automatically treated as an author of the original paper.

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### Maintainer

Scale AI

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Funders

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## Design goals

### Abilities measured

Challenging long-horizon software-engineering tasks are completed in public open-source repositories (fixing defects/implementing features without introducing regressions).

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Design background

Addressed to data contamination, insufficient task diversity, oversimplified questions, and tests that cannot be reproduced; V2 further repairs invalid tasks and locks the network and scoring protocol.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）；[来源2](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）

## Construction

### Question sources

Commit pairs from public repositories under strong copyleft licenses such as the GPL (fail-to-pass + pass-to-pass tests)

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 出题者背景

The V2 corrections were completed by 23 contract engineers, each using the programming language of their own specialty, covering 11 repositories, for 1,897 hours in total

[来源1](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）

### Review process

The official V2 release tree and the HF card record that 529 problem statements were rewritten, each solved blind by a second engineer who had not seen the task; 214 test patches and 38 gold patches were revised. The web-page announcement lists only 69 corrections of contradictions between instructions and tests. The two counts have different scopes and are not quietly replaced by one and the same number.

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### Quality control

642/642 reference patches pass, and 642/642 empty patches fail. Each question uses a public GHCR image, and the fix history is cleared. The Verifier restores hidden test paths, rolls back agent changes to fixtures/snapshots, clears stale pyc files, and repairs leftover git locks. 211 image dependencies were fixed.

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）

### 污染控制

A copyleft license lowers the chance of entering a training corpus; in the V2 agent stage only the model endpoint can be accessed, and web tools are disabled; the mirror removes the git history and hidden files

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）；[来源2](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）

## Data format

### 题量

642 tasks and 11 repositories; HARD-51 is a slice of 51 tasks within the same 642 questions, and the original 731 questions are retained as v1 config/tag v1.0.

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 任务形式

Repository-level code-patch generation

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Modalities

```json
[
 "代码"
 "文本"
]
```

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Languages

Go 256, Python 237, JavaScript 145, TypeScript 4; 642 in total.

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### Difficulty

SWE-Bench Pro reference solutions average 107.4 lines and 4.1 files.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### Public and hidden splits

This entry is the public set V2; SWE-Bench Pro also has a private set (276 instances) and a held-out set.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## Evaluation

### Metrics

Resolve Rate (solve rate), with a 95% confidence interval; Rank(UB) ranking rule

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 评分

A task counts as solved only when every fail-to-pass test passes and pass-to-pass has no regression; each agent diff is scored again on a clean image, and both scores are published

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 运行设置

In V2, the sandbox for each question lasts 50 minutes. During the agent stage only the model endpoint is let through, and web tools are disabled. The verifier does not execute inside the sandbox the agent has already used. A configuration on the leaderboard page that is not shown in gray has no cap on cost and has 250 turns. A configuration shown in gray has a cap on cost and has 50 turns. The harness and the budget have to be kept with the score.

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 评测工具

v2/tasks/<instance_id>/ is a Harbor task, containing tests/test.sh, run_script.sh, parser.py, and test_patch. v2/tooling provides LockedClaudeCode, LockedMiniSwe, LockedCodex, and PatchReplayAgent. Regrade in the new sandbox is the authoritative reported score. swe_bench_pro_eval.py in the root directory is the old v1 flow and is not used for V2.

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）

### Comparability

V2 cannot be compared directly with the original public set of 731 questions or with SWE-bench Verified; different harnesses (Claude Code, Codex, and mini-swe-agent) are placed in one ranking.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
 "version": "V2"
 "evidence_2026_h2": [
 {
 "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
 "date": "2026-11-07"
 "organization": "Scale AI"
 "note": "The current official leaderboard and the methods are public; this is Scale’s current main leaderboard for long-horizon code. V2 is a new protocol, refreshed for the purpose and isolated from the network. It is not an alias of SWE-bench Verified."
 }
 {
 "url": "https://labs.scale.com/leaderboard"
 "date": "2026-11-07"
 "organization": "Scale AI"
 "note": "Scale's current overall leaderboard lists SWE-bench Pro V2 separately and shows current frontier-model results."
 }
 {
 "url": "https://labs.scale.com/blog/swe-bench-pro-v2"
 "date": "2026-11-07"
 "organization": "Scale AI"
 "note": "The official V2 upgrade notes and the Full and Hard results; Hard is only a slice and is not counted again."
 }
 {
 "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
 "date": "2026-09-01"
 "organization": "Epoch AI"
 "note": "On September 1, Epoch reviewed SWE-Bench Pro and concluded Flawed; that historical review cannot automatically be equated with a quality conclusion for V2."
 }
 ]
 "trending": {
 "heat_confidence": "A"
 "summary": "The current main leaderboard at Scale for long-horizon code; V2 is a refreshed protocol that is isolated from the network. Epoch AI also lists it."
 }
}
```

> Recent popularity evidence is taken from candidate studies and reopened pages; grade A: adopted independently by multiple frontier laboratories or evaluation organizations.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）；[来源2](https://labs.scale.com/leaderboard)（访问 2026-11-07）；[来源3](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）；[来源4](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 修订历史

Revisions v1 and v2 of the original-series arXiv paper, and data V2 dated 2026-09-22, are not the same version axis. The static Scale PDF still describes the old public set of 731 questions and the old score of 23.3%. Its scores cannot be used to overwrite the current V2 Full and HARD.

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 饱和与能力边界

The current highest score on Full is 99.40±0.40%, and the highest on HARD-51 is 98.00±0.00% (the values in the current official table; the original confidence interval is kept and is not recomputed). Both tracks are already high, and HARD is not thereby a track that can never saturate. Rank(UB) orders results by the confidence interval, rather than by the ordinary rule for a tie on the point estimate.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 风险与争议

Re-evaluation found that Opus 5 forged Go module checksums and that Inkling modified the Go module cache; residual risk: the model endpoint is a trusted relay, and code inside a patch is still executed by the verifier.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 系列与衍生关系

The original SWE-Bench Pro (1865 questions, 41 repositories) is the predecessor; HARD is a slice of V2 and is not counted separately.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2509.16941) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-bench_Pro-os) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) (accessed 2026-11-08); [Source 4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) (accessed 2026-11-08)

### Official entry

https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 独立来源

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 分来源与协议结果

#### Scale V2 / full

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5 (Claude Code) xhigh | 99.4 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0.4,"dataset_size":642,"deprecated":false} |
| 2 | Gemini 4 Argon (mini-swe-agent) high | 99.22 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0.45,"dataset_size":642,"deprecated":false} |
| 2 | Fable 5.1 (Claude Code) high | 99.1 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0.5,"dataset_size":642,"deprecated":false} |
| 3 | Kimi-K3 (mini-swe-agent) max | 97.7 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0.9,"dataset_size":642,"deprecated":false} |
| 4 | Inkling Small 2 | 97.66 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.46,"dataset_size":642,"deprecated":false} |
| 5 | GPT-6-Astra (Codex) high | 96.9 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.1,"dataset_size":642,"deprecated":false} |
| 5 | Muse Wonder 1.0 (mini-swe-agent) xhigh | 96.73 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.12,"dataset_size":642,"deprecated":false} |
| 6 | Minimax M3p1 Flash (mini-swe-agent) xhigh | 96.57 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.16,"dataset_size":642,"deprecated":false} |
| 6 | GPT-6.1-Sol (mini-swe-agent) xhigh | 96.11 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.24,"dataset_size":642,"deprecated":false} |
| 7 | Sonnet 5.5 (mini-swe-agent) xhigh | 95.79 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.3,"dataset_size":642,"deprecated":false} |
| 7 | GLM-5.3 (mini-swe-agent) max | 95.6 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.3,"dataset_size":642,"deprecated":false} |
| 8 | GPT-5.6-sol (Codex) xhigh | 95.5 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.4,"dataset_size":642,"deprecated":false} |
| 8 | Muse Spark Open (mini-swe-agent) xhigh | 95.02 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.43,"dataset_size":642,"deprecated":false} |
| 9 | Gemini 3.8 Flash (mini-swe-agent) high | 94.86 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.46,"dataset_size":642,"deprecated":false} |
| 10 | Sonnet 5 (Claude Code) xhigh | 93.15 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.71,"dataset_size":642,"deprecated":false} |
| 11 | GPT-5.6-Terra (Codex) xhigh | 92.37 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":1.81,"dataset_size":642,"deprecated":false} |
| 12 | Inkling (mini-swe-agent) xhigh | 89.88 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":2.1,"dataset_size":642,"deprecated":false} |
| 13 | Haiku 5.5 (mini-swe-agent) high | 87.23 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":2.36,"dataset_size":642,"deprecated":false} |

#### Scale V2 / hard

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Opus 5 (Claude Code) xhigh | 98 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 2 | Fable 5.1 (Claude Code) high | 92.2 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 3 | Gemini 4 Argon (mini-swe-agent) high | 92.16 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 4 | GPT-6 Astra (Codex) high | 90.2 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 4 | Muse Wonder 1.0 (mini-swe-agent) xhigh | 90.2 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 6 | Kimi-K3 (mini-swe-agent) max | 88.2 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 6 | Sonnet 5 (Claude Code) xhigh | 88.2 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 8 | GPT-5.6 Terra (Codex) xhigh | 86.3 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 8 | Inkling Small 2 | 86.27 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 9 | Minimax M3p1 Flash (mini-swe-agent) xhigh | 84.31 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 10 | GLM-5.3 (mini-swe-agent) max | 84.3 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 11 | GPT-5.6 Sol (Codex) xhigh | 82.4 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 12 | Muse Spark Open (mini-swe-agent) xhigh | 82.35 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 13 | Sonnet 5.5 (mini-swe-agent) xhigh | 70.59 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 14 | Gemini 3.8 Flash (mini-swe-agent) high | 58.8 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 15 | Inkling (mini-swe-agent) xhigh | 56.9 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |
| 16 | Haiku 5.5 (mini-swe-agent) high | 52.94 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":13.01,"dataset_size":51,"deprecated":false} |
| 17 | Haiku 4.5 (Claude Code) xhigh | 25.5 | Resolve Rate (%) | {"rank_type":"official Rank(UB)","ci_plus_minus":0,"dataset_size":51,"deprecated":false} |

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 覆盖与时效

All 18 Full rows and all 18 HARD rows were extracted in full from the official embedded variants. The original rank and CI are retained as they are. Rank(UB)=1+ the number of models whose lower confidence bound exceeds this model's upper confidence bound. It is not a tie only when the point estimates are equal. The web page does not mark an overall update date. The data V2 announcement of 2026-09-22 cannot be treated as the run date of every model. The automatic HF widget may mix in v1 vendor results and is not included in this V2 leaderboard.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

## Contact

### 公开工作邮箱

```json
[
 "jeffrey.da@scale.com"
]
```

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### 官方反馈

https://github.com/scaleapi/SWE-bench_Pro-os/issues

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/README.md)（访问 2026-11-08）

### 公开社区

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 隐私边界

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2509.16941v2

[来源1](https://arxiv.org/pdf/2509.16941v2)（访问 2026-11-08）

### PDF SHA-256

38bafe017fe2e259f27aba35ec3583b0332af001d4a8e7b3330e522076beeb0f

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2509.16941v2)（访问 2026-11-08）

### PDF bytes

```json
1585853
```

[来源1](https://arxiv.org/pdf/2509.16941v2)（访问 2026-11-08）

### Folder

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "Opened primary material"
 "url": "https://arxiv.org/abs/2509.16941"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://github.com/scaleapi/SWE-bench_Pro-os"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"
 "accessed": "2026-11-08"
 }
 {
 "type": "Opened primary material"
 "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full"
 "accessed": "2026-11-08"
 }
]
```

[Source 1](https://arxiv.org/abs/2509.16941) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-bench_Pro-os) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) (accessed 2026-11-08); [Source 4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

[Source 1](https://arxiv.org/abs/2509.16941) (accessed 2026-11-08); [Source 2](https://github.com/scaleapi/SWE-bench_Pro-os) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) (accessed 2026-11-08); [Source 4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full) (accessed 2026-11-08)
