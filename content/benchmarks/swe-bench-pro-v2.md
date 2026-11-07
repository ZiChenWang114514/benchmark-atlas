# SWE-Bench Pro V2

> Benchmark Constitution · 深度复核 2026-11-08（KST / Asia/Seoul）。已核验存在；近期热门新建条目，未核实字段保留标记；trending: A

SWE-Bench Pro V2是同系列公开集的修订与隔离协议，不是SWE-bench Verified的新名字。默认642任务、HARD-51与保留的旧731题需要明确区分；agent离线、清洁镜像重评和双向发布门控是本版关键变化。官方Full与HARD榜分别记录，Rank(UB)按置信区间而非普通同分规则给名次。

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-bench_Pro-os)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）；[来源4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

## 基本信息

### 简称

SWE-Bench Pro V2

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 全称

SWE-Bench Pro V2（公开集刷新版，锁定评测协议）

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 基准版本

V2 / dataset 2.0.0；default=642题，hard=51题，v1=731题

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 论文版本

v2（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### 发布日期

2026-09-22（Scale 公告日期）

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 主板块

代码

> Benchmark Atlas 编辑归档。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 领域

```json
[
  "长程软件工程",
  "代码 agent"
]
```

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 许可与适用范围

评测harness/tooling MIT；任务说明、patch和tests派生自11个上游仓库，仍受各自许可约束，不把MIT覆盖到GPL来源任务。

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2509.16941

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### 官方代码

https://github.com/scaleapi/SWE-bench_Pro-os

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/README.md)（访问 2026-11-08）

### 数据

https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 官方入口

https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 论文标题

SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?（原始系列论文；不冒充V2专门论文）

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

## 发起与维护

### 发起方

Scale AI

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 合作/参与机构

Reflection（V2 联合开发）

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 作者

原始系列论文：Xiang Deng、Jeff Da（共同第一作者），Edwin Pan、Yannis Yiming He、Charles Ide、Kanak Garg、Niklas Lauffer、Andrew Park、Nitin Pasari、Chetan Rane、Karmini Sampath、Maya Krishnan、Srivatsa Kundurthy、Sean Hendryx、Zifan Wang、Vijay Bharadwaj、Jeff Holm、Raja Aluri、Chen Bo Calvin Zhang、Noah Jacobson、Bing Liu、Brad Kenstler；V2合作方Reflection，不自动当作原论文作者。

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### 维护方

Scale AI

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## 设计目标

### 衡量能力

在公开开源仓库中完成具有挑战性的长程软件工程任务（修复缺陷/实现功能且不引入回归）。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 设计背景

针对数据污染、任务多样性不足、问题过度简化、测试不可复现；V2 进一步修复无效任务并锁定网络与评分协议。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）；[来源2](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）

## 构建方式

### 题目来源

来自 GPL 等强 copyleft 许可的公开仓库提交对（fail-to-pass + pass-to-pass 测试）

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 出题者背景

V2 修正由23名合同工程师完成，各自使用其专业编程语言，覆盖11个仓库，共1,897小时

[来源1](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）

### 审核流程

官方V2发布树/HF卡记载529条问题说明重写，逐条由第二位未见任务工程师盲解；214个test patch、38个gold patch修订。网页公告仅列69条指令与测试矛盾更正，二者统计范围不同，不悄悄替换为同一数字。

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 质量控制

642/642 reference patch通过、642/642 empty patch不通过；每题GHCR公共镜像，清除修复历史；Verifier恢复隐藏测试路径、回滚agent改动fixtures/snapshots、清除过时pyc并修复残留git锁；211镜像依赖修复。

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）

### 污染控制

copyleft 许可降低进入训练语料可能；V2 agent 阶段仅能访问模型端点，禁用网页工具；镜像清除 git 历史与隐藏文件

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）；[来源2](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）

## 数据形式

### 题量

642任务、11仓库；HARD-51为同一642题内51任务切片，原731题保留为v1 config/tag v1.0。

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 任务形式

仓库级代码补丁生成

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 模态

```json
[
  "代码",
  "文本"
]
```

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 语言

Go 256、Python 237、JavaScript 145、TypeScript 4；合计642。

[来源1](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 难度

SWE-Bench Pro 参考解平均107.4行、4.1个文件

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 公开与隐藏划分

本条为公开集 V2；SWE-Bench Pro 另有私有集（276实例）与 held-out 集

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## 评测方法

### 指标

Resolve Rate（解决率），附95%置信区间；Rank(UB) 排名规则

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 评分

fail-to-pass 测试全部通过且 pass-to-pass 无回归才算解决；每个 agent diff 在干净镜像上重评并公布两种成绩

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 运行设置

V2每题沙箱50分钟，agent阶段仅放行模型端点，网页工具禁用；verifier不在agent旧沙箱执行。榜页非灰显配置无成本上限/250轮，灰显配置有成本上限/50轮；harness与预算需随成绩保留。

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 评测工具

v2/tasks/<instance_id>/为Harbor任务，含tests/test.sh、run_script.sh、parser.py、test_patch；v2/tooling提供LockedClaudeCode/LockedMiniSwe/LockedCodex和PatchReplayAgent，新沙箱regrade为报告权威分。根目录swe_bench_pro_eval.py是旧v1流程，不用于V2。

[来源1](https://github.com/scaleapi/SWE-bench_Pro-os/blob/main/v2/README.md)（访问 2026-11-08）

### 可比性

V2 与原731题公开集及 SWE-bench Verified 不可直接比较；不同 harness（Claude Code、Codex、mini-swe-agent）混排。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "V2",
  "evidence_2026_h2": [
    {
      "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full",
      "date": "2026-11-07",
      "organization": "Scale AI",
      "note": "当前官方榜单及方法公开；Scale当前长程代码主榜，V2是专门刷新且网络隔离的新协议，不是SWE-bench Verified别名。"
    },
    {
      "url": "https://labs.scale.com/leaderboard",
      "date": "2026-11-07",
      "organization": "Scale AI",
      "note": "Scale当前总榜将SWE-bench Pro V2单列，并展示当前前沿模型结果。"
    },
    {
      "url": "https://labs.scale.com/blog/swe-bench-pro-v2",
      "date": "2026-11-07",
      "organization": "Scale AI",
      "note": "官方V2升级说明及Full/Hard结果；Hard仅切片，不重复计数。"
    },
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks",
      "date": "2026-09-01",
      "organization": "Epoch AI",
      "note": "Epoch 9月1日审查SWE-Bench Pro，结论Flawed；该历史审查不能自动等同V2质量结论。"
    }
  ],
  "trending": {
    "heat_confidence": "A",
    "summary": "Scale 当前长程代码主榜，V2 为刷新且网络隔离的新协议；Epoch AI 亦有收录。"
  }
}
```

> 近期热门证据取自候选研究与本轮重开页面；A级：多家前沿实验室或评测机构独立采用。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）；[来源2](https://labs.scale.com/leaderboard)（访问 2026-11-07）；[来源3](https://labs.scale.com/blog/swe-bench-pro-v2)（访问 2026-11-07）；[来源4](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 修订历史

原始系列arXiv v1/v2修订与2026-09-22数据V2不是同一版本轴；静态Scale PDF仍描述旧公共731题且旧23.3%成绩，不能用其分数覆盖当前V2 Full/HARD。

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

### 饱和与能力边界

Full当前最高99.40±0.40%，HARD-51最高98.00±0.00%（官方当前表值，保留原CI不推算）；两轨均已高分，HARD不是自动永不饱和。Rank(UB)按置信区间排序而非普通点估计同分规则。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 风险与争议

重评发现 Opus 5 伪造 Go 模块校验和、Inkling 修改 Go 模块缓存；残余风险：模型端点为受信中继，补丁内代码仍会被验证器执行。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 系列与衍生关系

原 SWE-Bench Pro（1865题，41仓库）为前身；HARD 是 V2 切片不另计。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-08 KST / Asia/Seoul

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-bench_Pro-os)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）；[来源4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### 官方入口

https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 独立来源

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

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

从官方嵌入variants完整提取Full及HARD各18行；原rank与CI原样保留。Rank(UB)=1+下置信界超过本模型上置信界的模型数，不是点估计同分才并列。网页整体更新日未标，数据V2公告2026-09-22不能当所有模型运行日；HF自动widget可能混含v1厂商结果，不纳入本V2榜。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）

## 联系方式

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

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 隐私边界

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2509.16941v2

[来源1](https://arxiv.org/pdf/2509.16941v2)（访问 2026-11-08）

### 本轮PDF SHA-256

38bafe017fe2e259f27aba35ec3583b0332af001d4a8e7b3330e522076beeb0f

> 本次实际下载的PDF字节计算；未上传Drive。

[来源1](https://arxiv.org/pdf/2509.16941v2)（访问 2026-11-08）

### 本轮PDF字节数

```json
1585853
```

[来源1](https://arxiv.org/pdf/2509.16941v2)（访问 2026-11-08）

### Drive文件夹

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "本轮已打开一手材料",
    "url": "https://arxiv.org/abs/2509.16941",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://github.com/scaleapi/SWE-bench_Pro-os",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮已打开一手材料",
    "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full",
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-bench_Pro-os)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）；[来源4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）

### Drive PDF归档

待核实

[来源1](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST)",
    "change": "深度复核论文/官方实现与数据卡；补全可审计字段；按版本、来源与协议重建榜单轨；明确无法核实及相互冲突的统计。未上传Drive。"
  }
]
```

[来源1](https://arxiv.org/abs/2509.16941)（访问 2026-11-08）；[来源2](https://github.com/scaleapi/SWE-bench_Pro-os)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro)（访问 2026-11-08）；[来源4](https://labs.scale.com/leaderboard/swe_bench_pro_public_v2?tab=full)（访问 2026-11-08）
