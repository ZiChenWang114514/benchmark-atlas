# MMLU-Pro

> Benchmark Constitution，深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MMLU-Pro通过剔除简单和含糊题、增加推理题及干扰选项来扩展原始MMLU，标准主实验采用5-shot CoT。它不是每题都严格十个选项，也不是所有题都由研究生专家原创。官方Space混合实验室实测与外部自报，本页已读取公开底表并按Data Source分轨，不再只给旧Mini-Leaderboard。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 简称

MMLU-Pro

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 全称

MMLU-Pro

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 基准版本

MMLU-Pro（数据卡未以统一语义版本号命名；需固定数据修订以复现）

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 论文版本

arXiv v6

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 发布日期

2024-06-04（arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 主板块

语言

> Benchmark Constitution编辑归档，不是论文指定的唯一领域。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 领域标签

- 高难多学科知识与推理

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 许可证与权利边界

数据集MIT（论文附录A.5及HF卡片）；代码仓库LICENSE为Apache-2.0。应按下载的工件分别遵守，不能统一称MIT。

[来源](https://arxiv.org/pdf/2406.01574)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/raw/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/TIGER-AI-Lab/MMLU-Pro/main/LICENSE)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2406.01574

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 代码仓库

https://github.com/TIGER-AI-Lab/MMLU-Pro

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 官方主页

https://github.com/TIGER-AI-Lab/MMLU-Pro

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 论文标题

MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

论文作者来自 University of Waterloo、University of Toronto、Carnegie Mellon University 等；作者单位不等同于唯一发起方。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 合作方

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 作者

- Wang, Yubo
- Ma, Xueguang
- Zhang, Ge
- Ni, Yuansheng
- Chandra, Abhranil
- Guo, Shiguang
- Ren, Weiming
- Arulraj, Aaran
- He, Xuan
- Jiang, Ziyan
- Li, Tianle
- Ku, Max
- Wang, Kai
- Zhuang, Alex
- Fan, Rongqi
- Yue, Xiang
- Chen, Wenhu

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 维护方

官方公开代码托管于 TIGER-AI-Lab；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源](https://github.com/TIGER-AI-Lab/MMLU-Pro)（访问 2026-11-08）

### 资助

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

## 设计目标

### 衡量能力

在多学科知识问答中提高推理强度、难度与提示稳健性。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 设计背景

原始 MMLU 存在过易题、噪声及提示敏感问题；增加候选项和推理题以继续区分强模型。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

## 构建方式

### 题目来源

筛选原始 MMLU，并补充 STEM 网站、TheoremQA 与 SciBench 等来源的题目；使用 GPT-4-Turbo 辅助生成干扰选项。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 出题与审阅者背景

作者组织专业背景审阅者进行学科审核；具体每位出题人的资历需以论文附录为准。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 审核流程

GPT-4 扩充干扰项后，由十余名专家审核问题和选项；初筛排除原 MMLU 中简单或含糊的问题。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 质量控制

当前HF记录2025-04-06修正15个医学答案、2025-10-25 Health分类修订、2026-01-18修复STEM选项前导空格捷径；复现必须固定数据修订。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/raw/main/README.md)（访问 2026-11-08）

### 去污染及其证据边界

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

测试集 12,032 题；validation 70 题；14 学科。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 题型

通常为十选一；人工复核时少数题删去不合理选项，不能假定每题严格十个选项。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 模态

文本

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 语言

英语

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 难度

更强调推理并减少原始 MMLU 的简单题；不能把所有题都称为研究生级专家原创题。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 公开与隐藏划分

HF公开test12,032题、validation70题，字段含answer与answer_index；这不是隐藏答案测试集。validation用于少样本提示，不并入test成绩。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/raw/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

选择题准确率；可按学科查看。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 评分方法

从生成回答中抽取答案选项，官方提供多种答案抽取策略；原论文脚本无法匹配答案时使用随机回退，复现需记录实现。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 运行与提示设置

原论文主设置为 5-shot CoT；直接回答与 CoT 分开报告。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 官方脚本

https://github.com/TIGER-AI-Lab/MMLU-Pro

[来源](https://github.com/TIGER-AI-Lab/MMLU-Pro)（访问 2026-11-08）

### 可比性警示

必须区分5-shot CoT、0-shot、直接回答、错题重试，以及数据修订。官方Space汇总TIGER-Lab实测与Self-Reported/社区提交；前沿行不自动代表统一设置的独立验证。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/raw/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/TIGER-AI-Lab/MMLU-Pro/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro/raw/main/utils.py)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/TIGER-AI-Lab/MMLU-Pro/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

官方数据卡记录2026-01-18修正答案选项前导空格；2026-03-11新增榜单模型。未据此宣称之后没有更新。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 论文修订及历史证据

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 饱和情况

当前官方Space底表中TIGER-Lab来源最高Gemini-3.1-Pro Overall=0.9116；有明显剩余空间，但不能跨提示/数据版本和Self-Reported行得出统一饱和阈值。

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）

### 污染、争议与限制

公开静态题集仍可能污染；2026-01-18官方修复选项前导空格可能构成捷径。仓库API示例含--retry_wrong 2（错题重试），若使用需另报协议，不得当作标准pass@1。

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/raw/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/TIGER-AI-Lab/MMLU-Pro/main/README.md)（访问 2026-11-08）

### 衍生与版本关系

- MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（采集日，不是评测运行日）

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）

### 官方入口

https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro

[来源](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（访问 2026-11-07）

### 第三方覆盖入口

https://artificialanalysis.ai/evaluations/mmlu-pro

[来源](https://artificialanalysis.ai/evaluations/mmlu-pro)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### 官方Space底表 / TIGER-Lab

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Gemini-3.1-Pro | 0.9116 | Overall accuracy / proportion (0–1) |
| Gemini-2.5-Pro-Exp-03-25 | 0.8452 | Overall accuracy / proportion (0–1) |
| Gemini-2.0-Flash-exp | 0.7624 | Overall accuracy / proportion (0–1) |
| Claude-3.5-Sonnet (2024-06-20) | 0.7612 | Overall accuracy / proportion (0–1) |
| GPT-4o (2024-08-06) | 0.7468 | Overall accuracy / proportion (0–1) |
| GPT-oss-20B(medium) | 0.7314 | Overall accuracy / proportion (0–1) |
| Athene-V2-Chat (0-shot) | 0.7311 | Overall accuracy / proportion (0–1) |
| GPT-4o (2024-05-13) | 0.7255 | Overall accuracy / proportion (0–1) |
| Gemini-1.5-Pro-002 | 0.7025 | Overall accuracy / proportion (0–1) |
| Athene-V2-Chat | 0.7021 | Overall accuracy / proportion (0–1) |
| QwQ-32B | 0.6907 | Overall accuracy / proportion (0–1) |
| Claude-3-Opus | 0.6845 | Overall accuracy / proportion (0–1) |
| Mistral-Large-Instruct-2411 | 0.6794 | Overall accuracy / proportion (0–1) |
| Llama-3.3-70B-Instruct | 0.6592 | Overall accuracy / proportion (0–1) |
| Mistral-Large-Instruct-2407 | 0.6591 | Overall accuracy / proportion (0–1) |
| DeepSeek-Chat-V2_5 | 0.6583 | Overall accuracy / proportion (0–1) |
| Qwen2-72B-Chat | 0.6438 | Overall accuracy / proportion (0–1) |
| Gemini-1.5-Flash-002 | 0.6409 | Overall accuracy / proportion (0–1) |
| magnum-72b-v1 | 0.6393 | Overall accuracy / proportion (0–1) |
| GPT-4-Turbo | 0.6371 | Overall accuracy / proportion (0–1) |
| DeepSeek-Coder-V2-Instruct | 0.6363 | Overall accuracy / proportion (0–1) |
| GPT-4o-mini | 0.6309 | Overall accuracy / proportion (0–1) |
| Llama-3.1-70B-Instruct | 0.6284 | Overall accuracy / proportion (0–1) |
| Llama-3.1-Nemotron-70B-Instruct-HF | 0.6278 | Overall accuracy / proportion (0–1) |
| Yi-Lightning | 0.6238 | Overall accuracy / proportion (0–1) |
| Claude-3-5-Haiku-20241022 | 0.6212 | Overall accuracy / proportion (0–1) |
| Reflection-Llama-3.1-70B | 0.6035 | Overall accuracy / proportion (0–1) |
| Gemini-1.5-Flash | 0.5912 | Overall accuracy / proportion (0–1) |
| EXAONE-3.5-32B-Instruct | 0.5891 | Overall accuracy / proportion (0–1) |
| Yi-large | 0.5809 | Overall accuracy / proportion (0–1) |
| Claude-3-Sonnet | 0.568 | Overall accuracy / proportion (0–1) |
| Gemma-2-27B-it | 0.5654 | Overall accuracy / proportion (0–1) |
| Mixtral-8x22B-Instruct-v0.1 | 0.5633 | Overall accuracy / proportion (0–1) |
| Llama-3-70B-Instruct | 0.562 | Overall accuracy / proportion (0–1) |
| Phi3-medium-4k | 0.5570 | Overall accuracy / proportion (0–1) |
| Qwen2-72B-32k | 0.5559 | Overall accuracy / proportion (0–1) |
| Deepseek-V2-Chat | 0.5481 | Overall accuracy / proportion (0–1) |
| Llama-3-70B | 0.5278 | Overall accuracy / proportion (0–1) |
| Qwen1.5-72B-Chat | 0.5264 | Overall accuracy / proportion (0–1) |
| Llama-3.1-70B | 0.5247 | Overall accuracy / proportion (0–1) |
| Yi-1.5-34B-Chat | 0.5229 | Overall accuracy / proportion (0–1) |
| Gemma-2-9B-it | 0.5208 | Overall accuracy / proportion (0–1) |
| Phi3-medium-128k | 0.5191 | Overall accuracy / proportion (0–1) |
| MAmmoTH2-8x7B-Plus | 0.504 | Overall accuracy / proportion (0–1) |
| Qwen1.5-110B | 0.4993 | Overall accuracy / proportion (0–1) |
| Jamba-1.5-Large | 0.4946 | Overall accuracy / proportion (0–1) |
| Mistral-Small-Instruct-2409 | 0.4840 | Overall accuracy / proportion (0–1) |
| GLM-4-9B-Chat | 0.4801 | Overall accuracy / proportion (0–1) |
| GLM-4-9B | 0.4792 | Overall accuracy / proportion (0–1) |
| Phi-3.5-mini-instruct | 0.4787 | Overall accuracy / proportion (0–1) |
| Qwen2-7B-Instruct | 0.4724 | Overall accuracy / proportion (0–1) |
| EXAONE-3.5-7.8B-Instruct | 0.4624 | Overall accuracy / proportion (0–1) |
| Yi-1.5-9B-Chat | 0.4595 | Overall accuracy / proportion (0–1) |
| Phi3-mini-4k | 0.4566 | Overall accuracy / proportion (0–1) |
| Aya-Expanse-32B | 0.4541 | Overall accuracy / proportion (0–1) |
| Gemma-2-9B | 0.4510 | Overall accuracy / proportion (0–1) |
| Mistral-Nemo-Instruct-2407 | 0.4481 | Overall accuracy / proportion (0–1) |
| Llama-3.1-8B-Instruct | 0.4425 | Overall accuracy / proportion (0–1) |
| Phi3-mini-128k | 0.4386 | Overall accuracy / proportion (0–1) |
| MAmmoTH2-8B-Plus | 0.4335 | Overall accuracy / proportion (0–1) |
| Mixtral-8x7B-Instruct-v0.1 | 0.4327 | Overall accuracy / proportion (0–1) |
| Yi-34B | 0.4303 | Overall accuracy / proportion (0–1) |
| Claude-3-Haiku-20240307 | 0.4229 | Overall accuracy / proportion (0–1) |
| Mathstral-7B-v0.1 | 0.4200 | Overall accuracy / proportion (0–1) |
| DeepSeek-Coder-V2-Lite-Instruct | 0.4157 | Overall accuracy / proportion (0–1) |
| Mixtral-8x7B-v0.1 | 0.4103 | Overall accuracy / proportion (0–1) |
| Granite-3.1-8B-Instruct | 0.4103 | Overall accuracy / proportion (0–1) |
| Llama-3-8B-Instruct | 0.4098 | Overall accuracy / proportion (0–1) |
| MAmmoTH2-7B-Plus | 0.4085 | Overall accuracy / proportion (0–1) |
| Qwen2-7B | 0.4073 | Overall accuracy / proportion (0–1) |
| Mistral-Nemo-Base-2407 | 0.3977 | Overall accuracy / proportion (0–1) |
| WizardLM-2-8x22B | 0.3924 | Overall accuracy / proportion (0–1) |
| EXAONE-3.5-2.4B-Instruct | 0.3910 | Overall accuracy / proportion (0–1) |
| Yi-1.5-6B-Chat | 0.3823 | Overall accuracy / proportion (0–1) |
| Qwen1.5-14B-Chat | 0.3802 | Overall accuracy / proportion (0–1) |
| Ministral-8B-Instruct-2410 | 0.3793 | Overall accuracy / proportion (0–1) |
| c4ai-command-r-v01 | 0.379 | Overall accuracy / proportion (0–1) |
| Staring-7B | 0.3790 | Overall accuracy / proportion (0–1) |
| Llama-2-70B | 0.3753 | Overall accuracy / proportion (0–1) |
| OpenChat-3.5-8B | 0.3724 | Overall accuracy / proportion (0–1) |
| InternMath-20B-Plus | 0.3710 | Overall accuracy / proportion (0–1) |
| Llama3-Smaug-8B | 0.3693 | Overall accuracy / proportion (0–1) |
| Llama-3.1-8B | 0.3660 | Overall accuracy / proportion (0–1) |
| Llama-3-8B | 0.3536 | Overall accuracy / proportion (0–1) |
| DeepseekMath-7B-Instruct | 0.353 | Overall accuracy / proportion (0–1) |
| DeepSeek-Coder-V2-Lite-Base | 0.3437 | Overall accuracy / proportion (0–1) |
| Aya-Expanse-8B | 0.3374 | Overall accuracy / proportion (0–1) |
| Gemma-7B | 0.3373 | Overall accuracy / proportion (0–1) |
| InternMath-7B-Plus | 0.335 | Overall accuracy / proportion (0–1) |
| Granite-3.1-8B-Base | 0.3308 | Overall accuracy / proportion (0–1) |
| Zephyr-7B-Beta | 0.3297 | Overall accuracy / proportion (0–1) |
| Granite-3.1-2B-Instruct | 0.3197 | Overall accuracy / proportion (0–1) |
| Granite-3.0-8B-Base | 0.3103 | Overall accuracy / proportion (0–1) |
| Mistral-7B-v0.1 | 0.3088 | Overall accuracy / proportion (0–1) |
| Mistral-7B-Instruct-v0.2 | 0.3084 | Overall accuracy / proportion (0–1) |
| Mistral-7B-v0.2 | 0.3043 | Overall accuracy / proportion (0–1) |
| Qwen1.5-7B-Chat | 0.2906 | Overall accuracy / proportion (0–1) |
| Yi-6B-Chat | 0.2884 | Overall accuracy / proportion (0–1) |
| Neo-7B-Instruct | 0.2874 | Overall accuracy / proportion (0–1) |
| Yi-6B | 0.2651 | Overall accuracy / proportion (0–1) |
| Neo-7B | 0.2585 | Overall accuracy / proportion (0–1) |
| Mistral-7B-Instruct-v0.1 | 0.2575 | Overall accuracy / proportion (0–1) |
| Granite-3.1-3B-A800M-Instruct | 0.2542 | Overall accuracy / proportion (0–1) |
| Llama-2-13B | 0.2534 | Overall accuracy / proportion (0–1) |
| Granite-3.1-2B-Base | 0.2389 | Overall accuracy / proportion (0–1) |
| Llemma-7B | 0.2345 | Overall accuracy / proportion (0–1) |
| Qwen2-1.5B-Instruct | 0.2262 | Overall accuracy / proportion (0–1) |
| Qwen2-1.5B | 0.2256 | Overall accuracy / proportion (0–1) |
| Llama-3.2-3B | 0.2217 | Overall accuracy / proportion (0–1) |
| Granite-3.0-2B-Base | 0.2172 | Overall accuracy / proportion (0–1) |
| Granite-3.1-3B-A800M-Base | 0.2039 | Overall accuracy / proportion (0–1) |
| Llama-2-7B | 0.2032 | Overall accuracy / proportion (0–1) |
| SmolLM2-1.7B | 0.1831 | Overall accuracy / proportion (0–1) |
| Qwen2-0.5B-Instruct | 0.1593 | Overall accuracy / proportion (0–1) |
| Gemma-2B | 0.1585 | Overall accuracy / proportion (0–1) |
| Qwen2-0.5B | 0.1497 | Overall accuracy / proportion (0–1) |
| Granite-3.1-1B-A400M-Instruct | 0.1327 | Overall accuracy / proportion (0–1) |
| Granite-3.1-1B-A400M-Base | 0.1234 | Overall accuracy / proportion (0–1) |
| Llama-3.2-1B | 0.1195 | Overall accuracy / proportion (0–1) |
| SmolLM-1.7B | 0.1193 | Overall accuracy / proportion (0–1) |
| SmolLM2-360M | 0.1138 | Overall accuracy / proportion (0–1) |
| SmolLM-135M | 0.1122 | Overall accuracy / proportion (0–1) |
| SmolLM-360M | 0.1095 | Overall accuracy / proportion (0–1) |
| SmolLM2-135M | 0.1085 | Overall accuracy / proportion (0–1) |

- **Gemini-3.1-Pro**：- **rank**：1；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.9582；- **Business**：0.9328；- **Chemistry**：0.9214；- **Computer Science**：0.9366；- **Economics**：0.9336；- **Engineering**：0.8733；- **Health**：0.8619；- **History**：0.8556；- **Law**：0.8564；- **Math**：0.9548；- **Philosophy**：0.9038；- **Physics**：0.9320；- **Psychology**：0.9185；- **Other**：0.8929；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-2.5-Pro-Exp-03-25**：- **rank**：2；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.9299；- **Business**：0.893；- **Chemistry**：0.8741；- **Computer Science**：0.8556；- **Economics**：0.8829；- **Engineering**：0.7358；- **Health**：0.817；- **History**：0.7553；- **Law**：0.7244；- **Math**：0.8884；- **Philosophy**：0.8327；- **Physics**：0.8831；- **Psychology**：0.8726；- **Other**：0.8295；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-2.0-Flash-exp**：- **rank**：3；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8836；- **Business**：0.7985；- **Chemistry**：0.8004；- **Computer Science**：0.799；- **Economics**：0.8169；- **Engineering**：0.6155；- **Health**：0.7442；- **History**：0.7008；- **Law**：0.5647；- **Math**：0.8638；- **Philosophy**：0.6994；- **Physics**：0.8127；- **Psychology**：0.7905；- **Other**：0.7476；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3.5-Sonnet (2024-06-20)**：- **rank**：4；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8856；- **Business**：0.8023；- **Chemistry**：0.773；- **Computer Science**：0.7976；- **Economics**：0.8246；- **Engineering**：0.6153；- **Health**：0.7531；- **History**：0.7585；- **Law**：0.6385；- **Math**：0.7683；- **Philosophy**：0.7475；- **Physics**：0.7667；- **Psychology**：0.8221；- **Other**：0.7846；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4o (2024-08-06)**：- **rank**：5；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8926；- **Business**：0.801；- **Chemistry**：0.727；- **Computer Science**：0.7829；- **Economics**：0.8164；- **Engineering**：0.5531；- **Health**：0.7604；- **History**：0.7323；- **Law**：0.5895；- **Math**：0.7942；- **Philosophy**：0.7034；- **Physics**：0.7506；- **Psychology**：0.8271；- **Other**：0.7955；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-oss-20B(medium)**：- **rank**：6；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：20；- **Biology**：0.8536；- **Business**：0.7997；- **Chemistry**：0.8083；- **Computer Science**：0.8244；- **Economics**：0.8057；- **Engineering**：0.5635；- **Health**：0.7347；- **History**：0.5958；- **Law**：0.3978；- **Math**：0.9149；- **Philosophy**：0.5992；- **Physics**：0.8306；- **Psychology**：0.7368；- **Other**：0.6602；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Athene-V2-Chat (0-shot)**：- **rank**：7；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.8689；- **Business**：0.7921；- **Chemistry**：0.7473；- **Computer Science**：0.7463；- **Economics**：0.8081；- **Engineering**：0.5996；- **Health**：0.7164；- **History**：0.6404；- **Law**：0.5095；- **Math**：0.8364；- **Philosophy**：0.6293；- **Physics**：0.7737；- **Psychology**：0.7857；- **Other**：0.7219；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4o (2024-05-13)**：- **rank**：8；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8675；- **Business**：0.7858；- **Chemistry**：0.7393；- **Computer Science**：0.7829；- **Economics**：0.808；- **Engineering**：0.55；- **Health**：0.7212；- **History**：0.7007；- **Law**：0.5104；- **Math**：0.7609；- **Philosophy**：0.7014；- **Physics**：0.7467；- **Psychology**：0.7919；- **Other**：0.7748；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-1.5-Pro-002**：- **rank**：9；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8645；- **Business**：0.8094；- **Chemistry**：0.6221；- **Computer Science**：0.7122；- **Economics**：0.8171；- **Engineering**：0.5899；- **Health**：0.7479；- **History**：0.7008；- **Law**：0.5522；- **Math**：0.5174；- **Philosophy**：0.7234；- **Physics**：0.8072；- **Psychology**：0.8294；- **Other**：0.7359；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Athene-V2-Chat**：- **rank**：10；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.8243；- **Business**：0.7351；- **Chemistry**：0.7208；- **Computer Science**：0.7341；- **Economics**：0.8045；- **Engineering**：0.5470；- **Health**：0.6834；- **History**：0.6273；- **Law**：0.4832；- **Math**：0.8061；- **Philosophy**：0.6273；- **Physics**：0.7336；- **Psychology**：0.7694；- **Other**：0.7056；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **QwQ-32B**：- **rank**：11；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：0.8410；- **Business**：0.7668；- **Chemistry**：0.7041；- **Computer Science**：0.7366；- **Economics**：0.7832；- **Engineering**：0.4871；- **Health**：0.7066；- **History**：0.6325；- **Law**：0.4777；- **Math**：0.7876；- **Philosophy**：0.6713；- **Physics**：0.7028；- **Psychology**：0.7632；- **Other**：0.6537；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3-Opus**：- **rank**：12；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8507；- **Business**：0.7338；- **Chemistry**：0.693；- **Computer Science**：0.6902；- **Economics**：0.798；- **Engineering**：0.484；- **Health**：0.6845；- **History**：0.6141；- **Law**：0.5349；- **Math**：0.6957；- **Philosophy**：0.6352；- **Physics**：0.6966；- **Psychology**：0.7631；- **Other**：0.6991；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Large-Instruct-2411**：- **rank**：13；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：123；- **Biology**：0.8368；- **Business**：0.7186；- **Chemistry**：0.6290；- **Computer Science**：0.7683；- **Economics**：0.7642；- **Engineering**：0.5119；- **Health**：0.7457；- **History**：0.6640；- **Law**：0.5041；- **Math**：0.7091；- **Philosophy**：0.6533；- **Physics**：0.6605；- **Psychology**：0.7845；- **Other**：0.7067；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.3-70B-Instruct**：- **rank**：14；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.8187；- **Business**：0.6857；- **Chemistry**：0.6246；- **Computer Science**：0.7073；- **Economics**：0.7784；- **Engineering**：0.4665；- **Health**：0.7115；- **History**：0.6614；- **Law**：0.4796；- **Math**：0.6891；- **Philosophy**：0.6353；- **Physics**：0.6428；- **Psychology**：0.7794；- **Other**：0.6818；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Large-Instruct-2407**：- **rank**：15；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：123；- **Biology**：0.8271；- **Business**：0.6198；- **Chemistry**：0.6307；- **Computer Science**：0.7024；- **Economics**：0.7571；- **Engineering**：0.4396；- **Health**：0.7152；- **History**：0.6299；- **Law**：0.4823；- **Math**：0.7128；- **Philosophy**：0.6453；- **Physics**：0.6913；- **Psychology**：0.7707；- **Other**：0.6786；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-Chat-V2_5**：- **rank**：16；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：236；- **Biology**：0.8271；- **Business**：0.7364；- **Chemistry**：0.6979；- **Computer Science**：0.7098；- **Economics**：0.7678；- **Engineering**：0.517；- **Health**：0.6247；- **History**：0.5564；- **Law**：0.3715；- **Math**：0.7535；- **Philosophy**：0.5631；- **Physics**：0.7052；- **Psychology**：0.7268；- **Other**：0.6385；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-72B-Chat**：- **rank**：17；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.8107；- **Business**：0.6996；- **Chemistry**：0.5989；- **Computer Science**：0.6488；- **Economics**：0.7589；- **Engineering**：0.6724；- **Health**：0.4603；- **History**：0.6781；- **Law**：0.4587；- **Math**：0.7098；- **Philosophy**：0.5892；- **Physics**：0.6089；- **Psychology**：0.7669；- **Other**：0.6652；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-1.5-Flash-002**：- **rank**：18；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8368；- **Business**：0.7145；- **Chemistry**：0.6708；- **Computer Science**：0.6341；- **Economics**：0.7628；- **Engineering**：0.407；- **Health**：0.6284；- **History**：0.5932；- **Law**：0.4286；- **Math**：0.6255；- **Philosophy**：0.6052；- **Physics**：0.7141；- **Psychology**：0.7623；- **Other**：0.6453；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **magnum-72b-v1**：- **rank**：19；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.8219；- **Business**：0.6339；- **Chemistry**：0.5967；- **Computer Science**：0.7116；- **Economics**：0.7497；- **Engineering**：0.4847；- **Health**：0.6626；- **History**：0.6706；- **Law**：0.4378；- **Math**：0.6737；- **Philosophy**：0.6017；- **Physics**：0.6020；- **Psychology**：0.7657；- **Other**：0.6692；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4-Turbo**：- **rank**：20；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8243；- **Business**：0.673；- **Chemistry**：0.5592；- **Computer Science**：0.6854；- **Economics**：0.7476；- **Engineering**：0.3591；- **Health**：0.7078；- **History**：0.6772；- **Law**：0.5123；- **Math**：0.6277；- **Philosophy**：0.6433；- **Physics**：0.6097；- **Psychology**：0.7832；- **Other**：0.7186；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-Coder-V2-Instruct**：- **rank**：21；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：236；- **Biology**：0.7657；- **Business**：0.7326；- **Chemistry**：0.6686；- **Computer Science**：0.6878；- **Economics**：0.7464；- **Engineering**：0.5175；- **Health**：0.6112；- **History**：0.5184；- **Law**：0.3506；- **Math**：0.6342；- **Philosophy**：0.5621；- **Physics**：0.6813；- **Psychology**：0.7206；- **Other**：0.6537；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4o-mini**：- **rank**：22；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.802；- **Business**：0.706；- **Chemistry**：0.6299；- **Computer Science**：0.6707；- **Economics**：0.7334；- **Engineering**：0.3942；- **Health**：0.676；- **History**：0.5879；- **Law**：0.3724；- **Math**：0.7232；- **Philosophy**：0.5591；- **Physics**：0.6366；- **Psychology**：0.7381；- **Other**：0.6613；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-70B-Instruct**：- **rank**：23；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.8117；- **Business**：0.6641；- **Chemistry**：0.5910；- **Computer Science**：0.6634；- **Economics**：0.7524；- **Engineering**：0.4582；- **Health**：0.6846；- **History**：0.6614；- **Law**：0.4696；- **Math**：0.6047；- **Philosophy**：0.6172；- **Physics**：0.5912；- **Psychology**：0.7556；- **Other**：0.6602；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-Nemotron-70B-Instruct-HF**：- **rank**：24；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.7992；- **Business**：0.6793；- **Chemistry**：0.5963；- **Computer Science**：0.6829；- **Economics**：0.7642；- **Engineering**：0.4045；- **Health**：0.6797；- **History**：0.6352；- **Law**：0.4687；- **Math**：0.6306；- **Philosophy**：0.6012；- **Physics**：0.5989；- **Psychology**：0.7268；- **Other**：0.6807；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-Lightning**：- **rank**：25；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.7964；- **Business**：0.6907；- **Chemistry**：0.6193；- **Computer Science**：0.6439；- **Economics**：0.731；- **Engineering**：0.4221；- **Health**：0.6553；- **History**：0.5748；- **Law**：0.3751；- **Math**：0.6913；- **Philosophy**：0.5711；- **Physics**：0.6251；- **Psychology**：0.7293；- **Other**：0.6677；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3-5-Haiku-20241022**：- **rank**：26；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8075；- **Business**：0.6857；- **Chemistry**：0.5936；- **Computer Science**：0.6463；- **Economics**：0.7287；- **Engineering**：0.4231；- **Health**：0.6614；- **History**：0.622；- **Law**：0.4668；- **Math**：0.6173；- **Philosophy**：0.5852；- **Physics**：0.5835；- **Psychology**：0.7544；- **Other**：0.6645；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Reflection-Llama-3.1-70B**：- **rank**：27；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.7950；- **Business**：0.6324；- **Chemistry**：0.5433；- **Computer Science**：0.6268；- **Economics**：0.7370；- **Engineering**：0.4396；- **Health**：0.6907；- **History**：0.6194；- **Law**：0.4242；- **Math**：0.6136；- **Philosophy**：0.5772；- **Physics**：0.5327；- **Psychology**：0.7444；- **Other**：0.6504；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-1.5-Flash**：- **rank**：28；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8131；- **Business**：0.667；- **Chemistry**：0.613；- **Computer Science**：0.5951；- **Economics**：0.6943；- **Engineering**：0.4416；- **Health**：0.6039；- **History**：0.538；- **Law**：0.3732；- **Math**：0.5958；- **Philosophy**：0.4949；- **Physics**：0.612；- **Psychology**：0.7005；- **Other**：0.58；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **EXAONE-3.5-32B-Instruct**：- **rank**：29；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：0.7573；- **Business**：0.6502；- **Chemistry**：0.5830；- **Computer Science**：0.6634；- **Economics**：0.6908；- **Engineering**：0.4654；- **Health**：0.6002；- **History**：0.5328；- **Law**：0.4005；- **Math**：0.6691；- **Philosophy**：0.5371；- **Physics**：0.5350；- **Psychology**：0.6830；- **Other**：0.5617；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-large**：- **rank**：30；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：150；- **Biology**：0.6987；- **Business**：0.6413；- **Chemistry**：0.6166；- **Computer Science**：0.6341；- **Economics**：0.6813；- **Engineering**：0.4541；- **Health**：0.6443；- **History**：0.4961；- **Law**：0.3624；- **Math**：0.6481；- **Philosophy**：0.5531；- **Physics**：0.5704；- **Psychology**：0.5063；- **Other**：0.6472；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3-Sonnet**：- **rank**：31；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.768；- **Business**：0.657；- **Chemistry**：0.5291；- **Computer Science**：0.59；- **Economics**：0.709；- **Engineering**：0.4045；- **Health**：0.6332；- **History**：0.5721；- **Law**：0.427；- **Math**：0.49；- **Philosophy**：0.513；- **Physics**：0.5311；- **Psychology**：0.7218；- **Other**：0.594；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-2-27B-it**：- **rank**：32；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：27；- **Biology**：0.7796；- **Business**：0.6008；- **Chemistry**：0.5371；- **Computer Science**：0.5683；- **Economics**：0.6979；- **Engineering**：0.3488；- **Health**：0.6186；- **History**：0.5722；- **Law**：0.3951；- **Math**：0.5611；- **Philosophy**：0.5230；- **Physics**：0.5296；- **Psychology**：0.7155；- **Other**：0.6115；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mixtral-8x22B-Instruct-v0.1**：- **rank**：33；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：176；- **Biology**：0.7517；- **Business**：0.6033；- **Chemistry**：0.4885；- **Computer Science**：0.6415；- **Economics**：0.6742；- **Engineering**：0.4324；- **Health**：0.6149；- **History**：0.5643；- **Law**：0.3878；- **Math**：0.5655；- **Philosophy**：0.5491；- **Physics**：0.5089；- **Psychology**：0.7030；- **Other**：0.5996；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3-70B-Instruct**：- **rank**：34；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.7812；- **Business**：0.6018；- **Chemistry**：0.4681；- **Computer Science**：0.6053；- **Economics**：0.6841；- **Engineering**：0.4362；- **Health**：0.6533；- **History**：0.5692；- **Law**：0.3991；- **Math**：0.5402；- **Philosophy**：0.5499；- **Physics**：0.4962；- **Psychology**：0.7017；- **Other**：0.5924；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi3-medium-4k**：- **rank**：35；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：0.7587；- **Business**：0.6160；- **Chemistry**：0.4991；- **Computer Science**：0.5415；- **Economics**：0.7038；- **Engineering**：0.3787；- **Health**：0.6357；- **History**：0.5722；- **Law**：0.3833；- **Math**：0.5218；- **Philosophy**：0.5511；- **Physics**：0.4935；- **Psychology**：0.7343；- **Other**：0.6028；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-72B-32k**：- **rank**：36；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.7866；- **Business**：0.5615；- **Chemistry**：0.4337；- **Computer Science**：0.6146；- **Economics**：0.7097；- **Engineering**：0.3942；- **Health**：0.6271；- **History**：0.5801；- **Law**：0.3451；- **Math**：0.567；- **Philosophy**：0.5731；- **Physics**：0.5081；- **Psychology**：0.7206；- **Other**：0.6017；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Deepseek-V2-Chat**：- **rank**：37；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：236；- **Biology**：0.6625；- **Business**：0.6375；- **Chemistry**：0.5415；- **Computer Science**：0.5171；- **Economics**：0.6363；- **Engineering**：0.3189；- **Health**：0.5825；- **History**：0.4528；- **Law**：0.4064；- **Math**：0.5366；- **Philosophy**：0.5492；- **Physics**：0.5396；- **Psychology**：0.6621；- **Other**：0.6299；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3-70B**：- **rank**：38；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.749；- **Business**：0.4994；- **Chemistry**：0.417；- **Computer Science**：0.5512；- **Economics**：0.6528；- **Engineering**：0.3498；- **Health**：0.6174；- **History**：0.5774；- **Law**：0.3497；- **Math**：0.4967；- **Philosophy**：0.5691；- **Physics**：0.4981；- **Psychology**：0.7143；- **Other**：0.5942；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen1.5-72B-Chat**：- **rank**：39；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.7280；- **Business**：0.5792；- **Chemistry**：0.4196；- **Computer Science**：0.5683；- **Economics**：0.6540；- **Engineering**：0.3664；- **Health**：0.5954；- **History**：0.5591；- **Law**：0.3851；- **Math**：0.5233；- **Philosophy**：0.5150；- **Physics**：0.4419；- **Psychology**：0.6767；- **Other**：0.5823；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-70B**：- **rank**：40；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.7462；- **Business**：0.4880；- **Chemistry**：0.4496；- **Computer Science**：0.5195；- **Economics**：0.6209；- **Engineering**：0.3777；- **Health**：0.6015；- **History**：0.5827；- **Law**：0.3224；- **Math**：0.5056；- **Philosophy**：0.5691；- **Physics**：0.4896；- **Psychology**：0.7143；- **Other**：0.5833；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-1.5-34B-Chat**：- **rank**：41；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：34；- **Biology**：0.7141；- **Business**：0.5843；- **Chemistry**：0.4753；- **Computer Science**：0.539；- **Economics**：0.6457；- **Engineering**：0.3437；- **Health**：0.5819；- **History**：0.5276；- **Law**：0.3479；- **Math**：0.5618；- **Philosophy**：0.4629；- **Physics**：0.4935；- **Psychology**：0.6429；- **Other**：0.5162；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-2-9B-it**：- **rank**：42；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：0.7587；- **Business**：0.5539；- **Chemistry**：0.4664；- **Computer Science**：0.5073；- **Economics**：0.6552；- **Engineering**：0.3622；- **Health**：0.5844；- **History**：0.5354；- **Law**：0.3579；- **Math**：0.4944；- **Philosophy**：0.4950；- **Physics**：0.4758；- **Psychology**：0.6617；- **Other**：0.5498；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi3-medium-128k**：- **rank**：43；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：0.7336；- **Business**：0.5640；- **Chemistry**：0.4382；- **Computer Science**：0.5171；- **Economics**：0.6647；- **Engineering**：0.3437；- **Health**：0.5856；- **History**：0.5381；- **Law**：0.3597；- **Math**：0.4989；- **Philosophy**：0.4910；- **Physics**：0.4519；- **Psychology**：0.7093；- **Other**：0.5639；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MAmmoTH2-8x7B-Plus**：- **rank**：44；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：56；- **Biology**：0.7183；- **Business**：0.5615；- **Chemistry**：0.4205；- **Computer Science**：0.4854；- **Economics**：0.6398；- **Engineering**：0.3395；- **Health**：0.5538；- **History**：0.5092；- **Law**：0.3551；- **Math**：0.5026；- **Philosophy**：0.481；- **Physics**：0.4565；- **Psychology**：0.6378；- **Other**：0.5444；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen1.5-110B**：- **rank**：45；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：110；- **Biology**：0.7476；- **Business**：0.4664；- **Chemistry**：0.3746；- **Computer Science**：0.5122；- **Economics**：0.6185；- **Engineering**：0.3529；- **Health**：0.5868；- **History**：0.5407；- **Law**：0.3506；- **Math**：0.5041；- **Philosophy**：0.5311；- **Physics**：0.4142；- **Psychology**：0.6629；- **Other**：0.5639；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Jamba-1.5-Large**：- **rank**：46；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：399；- **Biology**：0.7713；- **Business**：0.5792；- **Chemistry**：0.2995；- **Computer Science**：0.5463；- **Economics**：0.6635；- **Engineering**：0.3344；- **Health**：0.6064；- **History**：0.5564；- **Law**：0.4405；- **Math**：0.3205；- **Philosophy**：0.5731；- **Physics**：0.338；- **Psychology**：0.7306；- **Other**：0.6061；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Small-Instruct-2409**：- **rank**：47；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：22；- **Biology**：0.7169；- **Business**：0.5272；- **Chemistry**：0.3684；- **Computer Science**：0.5366；- **Economics**：0.6007；- **Engineering**：0.3055；- **Health**：0.5379；- **History**：0.5013；- **Law**：0.3197；- **Math**：0.5085；- **Philosophy**：0.4810；- **Physics**：0.4034；- **Psychology**：0.6391；- **Other**：0.5509；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GLM-4-9B-Chat**：- **rank**：48；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：0.7015；- **Business**：0.5070；- **Chemistry**：0.4117；- **Computer Science**：0.4976；- **Economics**：0.6232；- **Engineering**：0.3106；- **Health**：0.5379；- **History**：0.5223；- **Law**：0.3006；- **Math**：0.5107；- **Philosophy**：0.4429；- **Physics**：0.4042；- **Psychology**：0.6165；- **Other**：0.5173；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GLM-4-9B**：- **rank**：49；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：0.7099；- **Business**：0.4778；- **Chemistry**：0.3719；- **Computer Science**：0.4927；- **Economics**：0.6552；- **Engineering**：0.3323；- **Health**：0.5440；- **History**：0.5381；- **Law**：0.3551；- **Math**：0.4323；- **Philosophy**：0.4709；- **Physics**：0.3865；- **Psychology**：0.6541；- **Other**：0.5390；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi-3.5-mini-instruct**：- **rank**：50；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：3.8；- **Biology**：0.7057；- **Business**：0.5349；- **Chemistry**：0.4125；- **Computer Science**：0.5195；- **Economics**：0.6386；- **Engineering**：0.3075；- **Health**：0.5244；- **History**：0.4252；- **Law**：0.2943；- **Math**：0.4900；- **Philosophy**：0.5000；- **Physics**：0.4509；- **Psychology**：0.4188；- **Other**：0.6353；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-7B-Instruct**：- **rank**：51；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.6625；- **Business**：0.5412；- **Chemistry**：0.3772；- **Computer Science**：0.4634；- **Economics**：0.5995；- **Engineering**：0.3540；- **Health**：0.4645；- **History**：0.4331；- **Law**：0.2934；- **Math**：0.5803；- **Philosophy**：0.4509；- **Physics**：0.3972；- **Psychology**：0.6128；- **Other**：0.4697；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **EXAONE-3.5-7.8B-Instruct**：- **rank**：52；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7.8；- **Biology**：0.7308；- **Business**：0.4740；- **Chemistry**：0.3719；- **Computer Science**：0.5537；- **Economics**：0.6066；- **Engineering**：0.3767；- **Health**：0.4707；- **History**：0.4514；- **Law**：0.2870；- **Math**：0.4996；- **Philosophy**：0.4248；- **Physics**：0.3818；- **Psychology**：0.5965；- **Other**：0.4426；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-1.5-9B-Chat**：- **rank**：53；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：0.6667；- **Business**：0.5425；- **Chemistry**：0.3949；- **Computer Science**：0.5；- **Economics**：0.6019；- **Engineering**：0.3323；- **Health**：0.4352；- **History**：0.4094；- **Law**：0.2661；- **Math**：0.5248；- **Philosophy**：0.4008；- **Physics**：0.4142；- **Psychology**：0.594；- **Other**：0.4491；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi3-mini-4k**：- **rank**：54；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：3.8；- **Biology**：0.7015；- **Business**：0.5044；- **Chemistry**：0.3896；- **Computer Science**：0.4463；- **Economics**：0.6055；- **Engineering**：0.2869；- **Health**：0.5024；- **History**：0.4147；- **Law**：0.2852；- **Math**：0.4182；- **Philosophy**：0.4449；- **Physics**：0.4095；- **Psychology**：0.6516；- **Other**：0.4957；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Aya-Expanse-32B**：- **rank**：55；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：0.6165；- **Business**：0.4804；- **Chemistry**：0.3481；- **Computer Science**：0.5122；- **Economics**：0.5829；- **Engineering**：0.2838；- **Health**：0.5428；- **History**：0.4961；- **Law**：0.3415；- **Math**：0.4152；- **Philosophy**：0.4609；- **Physics**：0.3949；- **Psychology**：0.6103；- **Other**：0.5108；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-2-9B**：- **rank**：56；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：0.6457；- **Business**：0.4284；- **Chemistry**：0.3746；- **Computer Science**：0.4122；- **Economics**：0.5486；- **Engineering**：0.3075；- **Health**：0.5232；- **History**：0.4987；- **Law**：0.2843；- **Math**：0.4041；- **Philosophy**：0.4850；- **Physics**：0.4296；- **Psychology**：0.6353；- **Other**：0.5271；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Nemo-Instruct-2407**：- **rank**：57；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：12；- **Biology**：0.6583；- **Business**：0.4715；- **Chemistry**：0.3445；- **Computer Science**：0.4463；- **Economics**：0.5806；- **Engineering**：0.3148；- **Health**：0.5281；- **History**：0.4829；- **Law**：0.3106；- **Math**：0.4241；- **Philosophy**：0.4529；- **Physics**：0.3695；- **Psychology**：0.6165；- **Other**：0.4881；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-8B-Instruct**：- **rank**：58；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.6304；- **Business**：0.4930；- **Chemistry**：0.3763；- **Computer Science**：0.4829；- **Economics**：0.5509；- **Engineering**：0.2972；- **Health**：0.5073；- **History**：0.4226；- **Law**：0.2725；- **Math**：0.4382；- **Philosophy**：0.4449；- **Physics**：0.4026；- **Psychology**：0.6003；- **Other**：0.4481；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi3-mini-128k**：- **rank**：59；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：3.8；- **Biology**：0.6695；- **Business**：0.4892；- **Chemistry**：0.3763；- **Computer Science**：0.4146；- **Economics**：0.5960；- **Engineering**：0.2570；- **Health**：0.4804；- **History**：0.4094；- **Law**：0.2698；- **Math**：0.4145；- **Philosophy**：0.4529；- **Physics**：0.3803；- **Psychology**：0.6491；- **Other**：0.4535；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MAmmoTH2-8B-Plus**：- **rank**：60；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.6429；- **Business**：0.4765；- **Chemistry**：0.3904；- **Computer Science**：0.4317；- **Economics**：0.5734；- **Engineering**：0.2631；- **Health**：0.4132；- **History**：0.4461；- **Law**：0.2479；- **Math**：0.4766；- **Philosophy**：0.4208；- **Physics**：0.398；- **Psychology**：0.5563；- **Other**：0.461；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mixtral-8x7B-Instruct-v0.1**：- **rank**：61；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：56；- **Biology**：0.6764；- **Business**：0.4119；- **Chemistry**：0.2756；- **Computer Science**：0.4439；- **Economics**：0.5581；- **Engineering**：0.2921；- **Health**：0.5049；- **History**：0.4462；- **Law**：0.3206；- **Math**：0.3634；- **Philosophy**：0.4729；- **Physics**：0.3988；- **Psychology**：0.6341；- **Other**：0.4989；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-34B**：- **rank**：62；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：34；- **Biology**：0.6527；- **Business**：0.4005；- **Chemistry**：0.2650；- **Computer Science**：0.4366；- **Economics**：0.5569；- **Engineering**：0.3261；- **Health**：0.5379；- **History**：0.5197；- **Law**：0.3270；- **Math**：0.3175；- **Philosophy**：0.4770；- **Physics**：0.3503；- **Psychology**：0.6253；- **Other**：0.5509；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3-Haiku-20240307**：- **rank**：63；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.7099；- **Business**：0.3663；- **Chemistry**：0.2739；- **Computer Science**：0.4049；- **Economics**：0.5723；- **Engineering**：0.3209；- **Health**：0.5306；- **History**：0.4357；- **Law**：0.3397；- **Math**：0.3397；- **Philosophy**：0.4629；- **Physics**：0.3226；- **Psychology**：0.6466；- **Other**：0.4556；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mathstral-7B-v0.1**：- **rank**：64；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.6346；- **Business**：0.4208；- **Chemistry**：0.3878；- **Computer Science**：0.4561；- **Economics**：0.5178；- **Engineering**：0.3839；- **Health**：0.3924；- **History**：0.3596；- **Law**：0.2243；- **Math**：0.4767；- **Philosophy**：0.3828；- **Physics**：0.3803；- **Psychology**：0.5263；- **Other**：0.4091；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-Coder-V2-Lite-Instruct**：- **rank**：65；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：16；- **Biology**：0.5007；- **Business**：0.5463；- **Chemistry**：0.4293；- **Computer Science**：0.4756；- **Economics**：0.5344；- **Engineering**：0.3437；- **Health**：0.2995；- **History**：0.3123；- **Law**：0.1880；- **Math**：0.5263；- **Philosophy**：0.3006；- **Physics**：0.4473；- **Psychology**：0.4687；- **Other**：0.3896；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mixtral-8x7B-v0.1**：- **rank**：66；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：56；- **Biology**：0.6206；- **Business**：0.3752；- **Chemistry**：0.288；- **Computer Science**：0.4683；- **Economics**：0.5071；- **Engineering**：0.2786；- **Health**：0.467；- **History**：0.4751；- **Law**：0.2707；- **Math**：0.3412；- **Philosophy**：0.4629；- **Physics**：0.3718；- **Psychology**：0.6103；- **Other**：0.4946；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-8B-Instruct**：- **rank**：67；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.5746；- **Business**：0.4563；- **Chemistry**：0.3145；- **Computer Science**：0.4244；- **Economics**：0.5047；- **Engineering**：0.2910；- **Health**：0.4707；- **History**：0.4121；- **Law**：0.2607；- **Math**：0.4189；- **Philosophy**：0.4329；- **Physics**：0.3472；- **Psychology**：0.5739；- **Other**：0.4405；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3-8B-Instruct**：- **rank**：68；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.6653；- **Business**：0.4043；- **Chemistry**：0.28；- **Computer Science**：0.4244；- **Economics**：0.5355；- **Engineering**：0.3127；- **Health**：0.4902；- **History**：0.4226；- **Law**：0.2652；- **Math**：0.3605；- **Philosophy**：0.4048；- **Physics**：0.3441；- **Psychology**：0.594；- **Other**：0.46；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MAmmoTH2-7B-Plus**：- **rank**：69；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.615；- **Business**：0.4588；- **Chemistry**：0.3604；- **Computer Science**：0.3805；- **Economics**：0.5722；- **Engineering**：0.2363；- **Health**：0.4009；- **History**：0.3674；- **Law**：0.2298；- **Math**：0.4574；- **Philosophy**：0.3346；- **Physics**：0.396；- **Psychology**：0.5513；- **Other**：0.408；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-7B**：- **rank**：70；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.6011；- **Business**：0.4423；- **Chemistry**：0.2977；- **Computer Science**：0.4317；- **Economics**：0.5213；- **Engineering**：0.2982；- **Health**：0.4108；- **History**：0.3832；- **Law**：0.2380；- **Math**：0.4752；- **Philosophy**：0.4269；- **Physics**：0.3410；- **Psychology**：0.5464；- **Other**：0.4329；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Nemo-Base-2407**：- **rank**：71；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：12；- **Biology**：0.6011；- **Business**：0.3866；- **Chemistry**：0.3127；- **Computer Science**：0.3805；- **Economics**：0.4775；- **Engineering**：0.3013；- **Health**：0.4866；- **History**：0.4383；- **Law**：0.2343；- **Math**：0.3257；- **Philosophy**：0.4810；- **Physics**：0.3464；- **Psychology**：0.5890；- **Other**：0.4556；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **WizardLM-2-8x22B**：- **rank**：72；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：176；- **Biology**：0.6234；- **Business**：0.5488；- **Chemistry**：0.3772；- **Computer Science**：0.5045；- **Economics**：0.5908；- **Engineering**：0.1498；- **Health**：0.4854；- **History**：0.4831；- **Law**：0.2852；- **Math**：0.1972；- **Philosophy**：0.5374；- **Physics**：0.2602；- **Psychology**：0.4825；- **Other**：0.4245；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **EXAONE-3.5-2.4B-Instruct**：- **rank**：73；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：2.4；- **Biology**：0.6541；- **Business**：0.3942；- **Chemistry**：0.3171；- **Computer Science**：0.4415；- **Economics**：0.5261；- **Engineering**：0.3168；- **Health**：0.3851；- **History**：0.3727；- **Law**：0.2498；- **Math**：0.4323；- **Philosophy**：0.3026；- **Physics**：0.3472；- **Psychology**：0.5038；- **Other**：0.3387；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-1.5-6B-Chat**：- **rank**：74；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：6；- **Biology**：0.5746；- **Business**：0.4766；- **Chemistry**：0.3074；- **Computer Science**：0.4366；- **Economics**：0.5273；- **Engineering**：0.2683；- **Health**：0.3362；- **History**：0.3176；- **Law**：0.2198；- **Math**：0.4145；- **Philosophy**：0.3327；- **Physics**：0.3564；- **Psychology**：0.5013；- **Other**：0.382；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen1.5-14B-Chat**：- **rank**：75；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：0.6151；- **Business**：0.3942；- **Chemistry**：0.2615；- **Computer Science**：0.3683；- **Economics**：0.5142；- **Engineering**：0.2817；- **Health**：0.4218；- **History**：0.3753；- **Law**：0.2489；- **Math**：0.3886；- **Philosophy**：0.3527；- **Physics**：0.3156；- **Psychology**：0.5251；- **Other**：0.4069；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Ministral-8B-Instruct-2410**：- **rank**：76；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.5900；- **Business**：0.3942；- **Chemistry**：0.2641；- **Computer Science**：0.4488；- **Economics**：0.4929；- **Engineering**：0.2312；- **Health**：0.4328；- **History**：0.4383；- **Law**：0.2598；- **Math**：0.4115；- **Philosophy**：0.3647；- **Physics**：0.2918；- **Psychology**：0.5163；- **Other**：0.4015；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **c4ai-command-r-v01**：- **rank**：77；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：35；- **Biology**：0.5509；- **Business**：0.3739；- **Chemistry**：0.2226；- **Computer Science**：0.3829；- **Economics**：0.5118；- **Engineering**：0.2477；- **Health**：0.4878；- **History**：0.4751；- **Law**：0.3397；- **Math**：0.2628；- **Philosophy**：0.4289；- **Physics**：0.2833；- **Psychology**：0.5852；- **Other**：0.4665；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Staring-7B**：- **rank**：78；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.5871；- **Business**：0.3688；- **Chemistry**：0.2676；- **Computer Science**：0.4048；- **Economics**：0.4810；- **Engineering**：0.2703；- **Health**：0.4425；- **History**：0.4356；- **Law**：0.2470；- **Math**：0.3486；- **Philosophy**：0.4231；- **Physics**：0.3847；- **Psychology**：0.3248；- **Other**：0.5463；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-2-70B**：- **rank**：79；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.5802；- **Business**：0.3853；- **Chemistry**：0.2217；- **Computer Science**：0.4098；- **Economics**：0.5059；- **Engineering**：0.2353；- **Health**：0.4352；- **History**：0.4593；- **Law**：0.2861；- **Math**：0.2679；- **Philosophy**：0.4629；- **Physics**：0.2818；- **Psychology**：0.5902；- **Other**：0.4827；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **OpenChat-3.5-8B**：- **rank**：80；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.5578；- **Business**：0.415；- **Chemistry**：0.2464；- **Computer Science**：0.4048；- **Economics**：0.4869；- **Engineering**：0.2693；- **Health**：0.4132；- **History**：0.3989；- **Law**：0.2461；- **Math**：0.3619；- **Philosophy**：0.3847；- **Physics**：0.3048；- **Psychology**：0.5451；- **Other**：0.3928；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **InternMath-20B-Plus**：- **rank**：81；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：20；- **Biology**：0.5216；- **Business**：0.4752；- **Chemistry**：0.4028；- **Computer Science**：0.446；- **Economics**：0.4312；- **Engineering**：0.3044；- **Health**：0.2334；- **History**：0.2047；- **Law**：0.1516；- **Math**：0.5610；- **Philosophy**：0.2683；- **Physics**：0.2404；- **Psychology**：0.4234；- **Other**：0.3834；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama3-Smaug-8B**：- **rank**：82；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.6220；- **Business**：0.3738；- **Chemistry**：0.2305；- **Computer Science**：0.3658；- **Economics**：0.4917；- **Engineering**：0.1981；- **Health**：0.4327；- **History**：0.4199；- **Law**：0.2652；- **Math**：0.3316；- **Philosophy**：0.4502；- **Physics**：0.3727；- **Psychology**：0.2856；- **Other**：0.5739；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-8B**：- **rank**：83；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.5635；- **Business**：0.3308；- **Chemistry**：0.2588；- **Computer Science**：0.3732；- **Economics**：0.4491；- **Engineering**：0.2859；- **Health**：0.4450；- **History**：0.4173；- **Law**：0.2107；- **Math**：0.3323；- **Philosophy**：0.4028；- **Physics**：0.3118；- **Psychology**：0.5313；- **Other**：0.4361；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3-8B**：- **rank**：84；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.5649；- **Business**：0.3207；- **Chemistry**：0.2482；- **Computer Science**：0.3366；- **Economics**：0.4668；- **Engineering**：0.2549；- **Health**：0.4328；- **History**：0.3622；- **Law**：0.1962；- **Math**：0.3042；- **Philosophy**：0.4048；- **Physics**：0.3141；- **Psychology**：0.5326；- **Other**：0.4145；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepseekMath-7B-Instruct**：- **rank**：85；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.46；- **Business**：0.4233；- **Chemistry**：0.4108；- **Computer Science**：0.3902；- **Economics**：0.4822；- **Engineering**：0.3364；- **Health**：0.2506；- **History**：0.1522；- **Law**：0.1571；- **Math**：0.4278；- **Philosophy**：0.2705；- **Physics**：0.3918；- **Psychology**：0.3947；- **Other**：0.2803；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-Coder-V2-Lite-Base**：- **rank**：86；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：16；- **Biology**：0.4114；- **Business**：0.3777；- **Chemistry**：0.3366；- **Computer Science**：0.3780；- **Economics**：0.4727；- **Engineering**：0.3127；- **Health**：0.2848；- **History**：0.2572；- **Law**：0.1589；- **Math**：0.4086；- **Philosophy**：0.2725；- **Physics**：0.3811；- **Psychology**：0.3997；- **Other**：0.3214；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Aya-Expanse-8B**：- **rank**：87；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.5579；- **Business**：0.3739；- **Chemistry**：0.2217；- **Computer Science**：0.3585；- **Economics**：0.4336；- **Engineering**：0.2497；- **Health**：0.3741；- **History**：0.3255；- **Law**：0.2307；- **Math**：0.3605；- **Philosophy**：0.2966；- **Physics**：0.2671；- **Psychology**：0.4599；- **Other**：0.3517；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-7B**：- **rank**：88；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.5649；- **Business**：0.3333；- **Chemistry**：0.2624；- **Computer Science**：0.3659；- **Economics**：0.4242；- **Engineering**：0.227；- **Health**：0.3716；- **History**：0.3675；- **Law**：0.2171；- **Math**：0.2509；- **Philosophy**：0.3908；- **Physics**：0.2756；- **Psychology**：0.5175；- **Other**：0.4091；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **InternMath-7B-Plus**：- **rank**：89；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.4714；- **Business**：0.3751；- **Chemistry**：0.3436；- **Computer Science**：0.3975；- **Economics**：0.4135；- **Engineering**：0.2817；- **Health**：0.2628；- **History**：0.1916；- **Law**：0.1444；- **Math**：0.4826；- **Philosophy**：0.2435；- **Physics**：0.2284；- **Psychology**：0.3826；- **Other**：0.3634；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-8B-Base**：- **rank**：90；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.4979；- **Business**：0.3181；- **Chemistry**：0.2403；- **Computer Science**：0.3390；- **Economics**：0.4372；- **Engineering**：0.2425；- **Health**：0.3716；- **History**：0.3412；- **Law**：0.2044；- **Math**：0.3249；- **Philosophy**：0.3567；- **Physics**：0.2748；- **Psychology**：0.4862；- **Other**：0.3636；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Zephyr-7B-Beta**：- **rank**：91；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.5509；- **Business**：0.2775；- **Chemistry**：0.2367；- **Computer Science**：0.3756；- **Economics**：0.4573；- **Engineering**：0.2394；- **Health**：0.396；- **History**：0.3202；- **Law**：0.2198；- **Math**：0.2361；- **Philosophy**：0.3896；- **Physics**：0.3567；- **Psychology**：0.2817；- **Other**：0.5050；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-2B-Instruct**：- **rank**：92；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：2；- **Biology**：0.5007；- **Business**：0.3308；- **Chemistry**：0.2412；- **Computer Science**：0.3707；- **Economics**：0.4111；- **Engineering**：0.2528；- **Health**：0.3056；- **History**：0.3045；- **Law**：0.2180；- **Math**：0.3442；- **Philosophy**：0.2846；- **Physics**：0.2648；- **Psychology**：0.4411；- **Other**：0.3258；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.0-8B-Base**：- **rank**：93；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：0.4728；- **Business**：0.3080；- **Chemistry**：0.2217；- **Computer Science**：0.3268；- **Economics**：0.4135；- **Engineering**：0.2136；- **Health**：0.3863；- **History**：0.3307；- **Law**：0.2316；- **Math**：0.2805；- **Philosophy**：0.3467；- **Physics**：0.2494；- **Psychology**：0.4336；- **Other**：0.3149；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-7B-v0.1**：- **rank**：94；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.4965；- **Business**：0.2852；- **Chemistry**：0.1846；- **Computer Science**：0.339；- **Economics**：0.4028；- **Engineering**：0.2239；- **Health**：0.3863；- **History**：0.3255；- **Law**：0.2071；- **Math**：0.2354；- **Philosophy**：0.3687；- **Physics**：0.2479；- **Psychology**：0.4887；- **Other**：0.3755；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-7B-Instruct-v0.2**：- **rank**：95；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.4533；- **Business**：0.289；- **Chemistry**：0.1767；- **Computer Science**：0.3195；- **Economics**：0.4633；- **Engineering**：0.1971；- **Health**：0.3875；- **History**：0.3438；- **Law**：0.218；- **Math**：0.2243；- **Philosophy**：0.3387；- **Physics**：0.2548；- **Psychology**：0.51；- **Other**：0.3755；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-7B-v0.2**：- **rank**：96；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.484；- **Business**：0.2611；- **Chemistry**：0.1829；- **Computer Science**：0.3073；- **Economics**：0.3791；- **Engineering**：0.2415；- **Health**：0.3704；- **History**：0.3228；- **Law**：0.1989；- **Math**：0.2287；- **Philosophy**：0.3547；- **Physics**：0.254；- **Psychology**：0.4937；- **Other**：0.3961；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen1.5-7B-Chat**：- **rank**：97；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.4561；- **Business**：0.2953；- **Chemistry**：0.1943；- **Computer Science**：0.3195；- **Economics**：0.41；- **Engineering**：0.1878；- **Health**：0.2714；- **History**：0.3018；- **Law**：0.198；- **Math**：0.3064；- **Philosophy**：0.2826；- **Physics**：0.2148；- **Psychology**：0.4524；- **Other**：0.3323；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-6B-Chat**：- **rank**：98；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：6；- **Biology**：0.477；- **Business**：0.2826；- **Chemistry**：0.1661；- **Computer Science**：0.2659；- **Economics**：0.3969；- **Engineering**：0.1899；- **Health**：0.3521；- **History**：0.315；- **Law**：0.2162；- **Math**：0.2124；- **Philosophy**：0.3367；- **Physics**：0.2094；- **Psychology**：0.4912；- **Other**：0.3506；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Neo-7B-Instruct**：- **rank**：99；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.5097；- **Business**：0.3229；- **Chemistry**：0.2266；- **Computer Science**：0.2919；- **Economics**：0.3577；- **Engineering**：0.1914；- **Health**：0.2509；- **History**：0.2821；- **Law**：0.1795；- **Math**：0.3545；- **Philosophy**：0.2603；- **Physics**：0.2370；- **Psychology**：0.3619；- **Other**：0.2803；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Yi-6B**：- **rank**：100；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：6；- **Biology**：0.4226；- **Business**：0.2864；- **Chemistry**：0.1484；- **Computer Science**：0.2732；- **Economics**：0.3578；- **Engineering**：0.1796；- **Health**：0.3166；- **History**：0.2940；- **Law**：0.1953；- **Math**：0.1902；- **Philosophy**：0.3186；- **Physics**：0.1832；- **Psychology**：0.4286；- **Other**：0.3496；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Neo-7B**：- **rank**：101；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.4253；- **Business**：0.2547；- **Chemistry**：0.1819；- **Computer Science**：0.2414；- **Economics**：0.3578；- **Engineering**：0.2136；- **Health**：0.2652；- **History**：0.2519；- **Law**：0.1589；- **Math**：0.2509；- **Philosophy**：0.2694；- **Physics**：0.2585；- **Psychology**：0.2347；- **Other**：0.3521；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-7B-Instruct-v0.1**：- **rank**：102；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.4993；- **Business**：0.1914；- **Chemistry**：0.1687；- **Computer Science**：0.3049；- **Economics**：0.3412；- **Engineering**：0.1651；- **Health**：0.2885；- **History**：0.2835；- **Law**：0.1753；- **Math**：0.1821；- **Philosophy**：0.2705；- **Physics**：0.2163；- **Psychology**：0.4336；- **Other**：0.303；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-3B-A800M-Instruct**：- **rank**：103；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：3；- **Biology**：0.3431；- **Business**：0.2725；- **Chemistry**：0.1608；- **Computer Science**：0.2829；- **Economics**：0.3626；- **Engineering**：0.1744；- **Health**：0.2641；- **History**：0.2415；- **Law**：0.1708；- **Math**：0.2754；- **Philosophy**：0.2806；- **Physics**：0.2017；- **Psychology**：0.3810；- **Other**：0.2706；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-2-13B**：- **rank**：104；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：13；- **Biology**：0.4045；- **Business**：0.2484；- **Chemistry**：0.1519；- **Computer Science**：0.2293；- **Economics**：0.3353；- **Engineering**：0.2023；- **Health**：0.3081；- **History**：0.2835；- **Law**：0.1599；- **Math**：0.1651；- **Philosophy**：0.3046；- **Physics**：0.1986；- **Psychology**：0.4261；- **Other**：0.3344；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-2B-Base**：- **rank**：105；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：2；- **Biology**：0.3752；- **Business**：0.2560；- **Chemistry**：0.1696；- **Computer Science**：0.2439；- **Economics**：0.3092；- **Engineering**：0.1930；- **Health**：0.2604；- **History**：0.2178；- **Law**：0.1253；- **Math**：0.2487；- **Philosophy**：0.2525；- **Physics**：0.1986；- **Psychology**：0.3421；- **Other**：0.2565；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llemma-7B**：- **rank**：106；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.3724；- **Business**：0.251；- **Chemistry**：0.1829；- **Computer Science**：0.2659；- **Economics**：0.3009；- **Engineering**：0.2384；- **Health**：0.2139；- **History**：0.1522；- **Law**：0.148；- **Math**：0.2161；- **Philosophy**：0.1964；- **Physics**：0.2571；- **Psychology**：0.2957；- **Other**：0.2165；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-1.5B-Instruct**：- **rank**：107；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1.5；- **Biology**：0.3612；- **Business**：0.2104；- **Chemistry**：0.1449；- **Computer Science**：0.2220；- **Economics**：0.3128；- **Engineering**：0.1600；- **Health**：0.2347；- **History**：0.2126；- **Law**：0.1653；- **Math**：0.2420；- **Philosophy**：0.2365；- **Physics**：0.1740；- **Psychology**：0.3321；- **Other**：0.2511；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-1.5B**：- **rank**：108；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1.5；- **Biology**：0.3515；- **Business**：0.1952；- **Chemistry**：0.1466；- **Computer Science**：0.2829；- **Economics**：0.2974；- **Engineering**：0.1486；- **Health**：0.2311；- **History**：0.1969；- **Law**：0.1589；- **Math**：0.2376；- **Philosophy**：0.2485；- **Physics**：0.1778；- **Psychology**：0.3283；- **Other**：0.2749；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.2-3B**：- **rank**：109；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：3；- **Biology**：0.3919；- **Business**：0.2041；- **Chemistry**：0.1458；- **Computer Science**：0.2049；- **Economics**：0.3258；- **Engineering**：0.1538；- **Health**：0.2518；- **History**：0.2782；- **Law**：0.1626；- **Math**：0.2021；- **Philosophy**：0.2365；- **Physics**：0.1493；- **Psychology**：0.3033；- **Other**：0.2543；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.0-2B-Base**：- **rank**：110；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：2；- **Biology**：0.3445；- **Business**：0.1977；- **Chemistry**：0.1564；- **Computer Science**：0.2659；- **Economics**：0.3033；- **Engineering**：0.1465；- **Health**：0.2298；- **History**：0.1837；- **Law**：0.1653；- **Math**：0.2058；- **Philosophy**：0.2385；- **Physics**：0.1640；- **Psychology**：0.3271；- **Other**：0.2327；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-3B-A800M-Base**：- **rank**：111；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：3；- **Biology**：0.2957；- **Business**：0.1762；- **Chemistry**：0.1405；- **Computer Science**：0.2268；- **Economics**：0.2737；- **Engineering**：0.1527；- **Health**：0.2286；- **History**：0.1995；- **Law**：0.1444；- **Math**：0.2198；- **Philosophy**：0.2305；- **Physics**：0.1640；- **Psychology**：0.3083；- **Other**：0.1926；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-2-7B**：- **rank**：112；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：0.325；- **Business**：0.1876；- **Chemistry**：0.1511；- **Computer Science**：0.1829；- **Economics**：0.3164；- **Engineering**：0.1496；- **Health**：0.2298；- **History**：0.1942；- **Law**：0.1662；- **Math**：0.1332；- **Philosophy**：0.2204；- **Physics**：0.1694；- **Psychology**：0.317；- **Other**：0.2143；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SmolLM2-1.7B**：- **rank**：113；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1.7；- **Biology**：0.1925；- **Business**：0.1762；- **Chemistry**：0.1422；- **Computer Science**：0.1634；- **Economics**：0.2536；- **Engineering**：0.1373；- **Health**：0.2054；- **History**：0.1575；- **Law**：0.1444；- **Math**：0.1673；- **Philosophy**：0.2144；- **Physics**：0.1655；- **Psychology**：0.2845；- **Other**：0.2045；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-0.5B-Instruct**：- **rank**：114；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：0.5；- **Biology**：0.2538；- **Business**：0.1432；- **Chemistry**：0.1254；- **Computer Science**：0.1585；- **Economics**：0.1991；- **Engineering**：0.1414；- **Health**：0.1553；- **History**：0.1706；- **Law**：0.1580；- **Math**：0.1384；- **Philosophy**：0.1323；- **Physics**：0.1386；- **Psychology**：0.2180；- **Other**：0.1483；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-2B**：- **rank**：115；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：2；- **Biology**：0.2482；- **Business**：0.1457；- **Chemistry**：0.1378；- **Computer Science**：0.1414；- **Economics**：0.1753；- **Engineering**：0.1269；- **Health**：0.177；- **History**：0.154；- **Law**：0.123；- **Math**：0.163；- **Philosophy**：0.1482；- **Physics**：0.1563；- **Psychology**：0.1608；- **Other**：0.1817；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2-0.5B**：- **rank**：116；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：0.5；- **Biology**：0.1855；- **Business**：0.1420；- **Chemistry**：0.1069；- **Computer Science**：0.1488；- **Economics**：0.2062；- **Engineering**：0.1135；- **Health**：0.1491；- **History**：0.1732；- **Law**：0.1599；- **Math**：0.1488；- **Philosophy**：0.1523；- **Physics**：0.1255；- **Psychology**：0.1992；- **Other**：0.1374；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-1B-A400M-Instruct**：- **rank**：117；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1；- **Biology**：0.1437；- **Business**：0.1267；- **Chemistry**：0.1148；- **Computer Science**：0.1610；- **Economics**：0.1576；- **Engineering**：0.1125；- **Health**：0.1638；- **History**：0.1129；- **Law**：0.1253；- **Math**：0.1303；- **Philosophy**：0.1202；- **Physics**：0.1209；- **Psychology**：0.1617；- **Other**：0.1288；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Granite-3.1-1B-A400M-Base**：- **rank**：118；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1；- **Biology**：0.1353；- **Business**：0.1153；- **Chemistry**：0.1246；- **Computer Science**：0.1415；- **Economics**：0.1422；- **Engineering**：0.0980；- **Health**：0.1308；- **History**：0.1234；- **Law**：0.1126；- **Math**：0.1310；- **Philosophy**：0.1683；- **Physics**：0.1124；- **Psychology**：0.1078；- **Other**：0.1212；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.2-1B**：- **rank**：119；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1；- **Biology**：0.1325；- **Business**：0.1077；- **Chemistry**：0.1095；- **Computer Science**：0.1122；- **Economics**：0.1256；- **Engineering**：0.1342；- **Health**：0.1247；- **History**：0.0892；- **Law**：0.1317；- **Math**：0.1021；- **Philosophy**：0.1323；- **Physics**：0.1147；- **Psychology**：0.1253；- **Other**：0.1277；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SmolLM-1.7B**：- **rank**：120；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：1.7；- **Biology**：0.1046；- **Business**：0.1052；- **Chemistry**：0.1069；- **Computer Science**：0.1268；- **Economics**：0.1197；- **Engineering**：0.1259；- **Health**：0.1467；- **History**：0.1181；- **Law**：0.1371；- **Math**：0.1110；- **Philosophy**：0.1423；- **Physics**：0.1132；- **Psychology**：0.1115；- **Other**：0.1169；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SmolLM2-360M**：- **rank**：121；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：0.36；- **Biology**：0.1269；- **Business**：0.1242；- **Chemistry**：0.1131；- **Computer Science**：0.1024；- **Economics**：0.1209；- **Engineering**：0.1135；- **Health**：0.1112；- **History**：0.1155；- **Law**：0.1299；- **Math**：0.1088；- **Philosophy**：0.1202；- **Physics**：0.0993；- **Psychology**：0.1015；- **Other**：0.1115；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SmolLM-135M**：- **rank**：122；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：0.135；- **Biology**：0.1227；- **Business**：0.1191；- **Chemistry**：0.1051；- **Computer Science**：0.1073；- **Economics**：0.1173；- **Engineering**：0.0939；- **Health**：0.1247；- **History**：0.0945；- **Law**：0.1153；- **Math**：0.1140；- **Philosophy**：0.1563；- **Physics**：0.0970；- **Psychology**：0.1090；- **Other**：0.1136；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SmolLM-360M**：- **rank**：123；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：0.36；- **Biology**：0.1116；- **Business**：0.0989；- **Chemistry**：0.1007；- **Computer Science**：0.1098；- **Economics**：0.1209；- **Engineering**：0.0877；- **Health**：0.1259；- **History**：0.1129；- **Law**：0.1117；- **Math**：0.1044；- **Philosophy**：0.1303；- **Physics**：0.1001；- **Psychology**：0.1266；- **Other**：0.1169；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SmolLM2-135M**：- **rank**：124；- **data_source**：TIGER-Lab；- **per_subject_and_size**：- **Model Size(B)**：0.135；- **Biology**：0.1185；- **Business**：0.1179；- **Chemistry**：0.0945；- **Computer Science**：0.0927；- **Economics**：0.1209；- **Engineering**：0.0815；- **Health**：0.1186；- **History**：0.1024；- **Law**：0.1199；- **Math**：0.1192；- **Philosophy**：0.1182；- **Physics**：0.1032；- **Psychology**：0.1140；- **Other**：0.0952；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）

#### 官方Space底表 / Self-Reported

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Gemini-3-Pro(11/25) | 0.901 | Overall accuracy / proportion (0–1) |
| GPT-o1 | 0.893 | Overall accuracy / proportion (0–1) |
| Claude-4.6-Opus(Thinking) | 0.891 | Overall accuracy / proportion (0–1) |
| Gemini-3-Flash(12/25) | 0.886 | Overall accuracy / proportion (0–1) |
| MiniMax-M2.1 | 0.880 | Overall accuracy / proportion (0–1) |
| Qwen3.5-397B-A17B | 0.878 | Overall accuracy / proportion (0–1) |
| Seed2.0-Lite | 0.877 | Overall accuracy / proportion (0–1) |
| GPT-5.4 | 0.875 | Overall accuracy / proportion (0–1) |
| GPT-5.2 | 0.874 | Overall accuracy / proportion (0–1) |
| Claude-4.5-Sonnet(Thinking) | 0.874 | Overall accuracy / proportion (0–1) |
| Claude-4-Opus-Thinking | 0.873 | Overall accuracy / proportion (0–1) |
| Claude-4.5-Opus(Thinking) | 0.873 | Overall accuracy / proportion (0–1) |
| Claude-4.6-Sonnet(Thinking) | 0.873 | Overall accuracy / proportion (0–1) |
| Hunyuan-T1 | 0.872 | Overall accuracy / proportion (0–1) |
| GPT-5(high) | 0.871 | Overall accuracy / proportion (0–1) |
| K2.5-1T-A32B | 0.871 | Overall accuracy / proportion (0–1) |
| Seed-Thinking-v1.5 | 0.870 | Overall accuracy / proportion (0–1) |
| Grok-4 | 0.870 | Overall accuracy / proportion (0–1) |
| Seed2.0-Pro | 0.870 | Overall accuracy / proportion (0–1) |
| Qwen3.5-122B-A10B | 0.867 | Overall accuracy / proportion (0–1) |
| Seed1.6-Thinking | 0.866 | Overall accuracy / proportion (0–1) |
| Seed1.6-Base | 0.866 | Overall accuracy / proportion (0–1) |
| Seed1.6-Ada-Thinking | 0.864 | Overall accuracy / proportion (0–1) |
| GPT-5.1 | 0.864 | Overall accuracy / proportion (0–1) |
| Gemini-3.1-Flash-Lite-Preview | 0.862 | Overall accuracy / proportion (0–1) |
| GPT-4.5 | 0.861 | Overall accuracy / proportion (0–1) |
| Qwen3.5-27B | 0.861 | Overall accuracy / proportion (0–1) |
| Gemini-2.5-Pro | 0.860 | Overall accuracy / proportion (0–1) |
| GLM-5 | 0.860 | Overall accuracy / proportion (0–1) |
| Qwen3-Max-Thinking | 0.857 | Overall accuracy / proportion (0–1) |
| Qwen3.5-35B-A3B | 0.853 | Overall accuracy / proportion (0–1) |
| GPT-o3-high | 0.850 | Overall accuracy / proportion (0–1) |
| DeepSeek-V3.2-Thinking | 0.850 | Overall accuracy / proportion (0–1) |
| DeepSeek-V3.1-Thinking | 0.848 | Overall accuracy / proportion (0–1) |
| GLM-4.5 | 0.846 | Overall accuracy / proportion (0–1) |
| Qwen3-235B-A22B-Thinking-2507 | 0.845 | Overall accuracy / proportion (0–1) |
| Grok-4.1-Fast(Reasoning) | 0.842 | Overall accuracy / proportion (0–1) |
| DeepSeek-R1 | 0.840 | Overall accuracy / proportion (0–1) |
| Claude-3.7-Sonnet-Thinking | 0.840 | Overall accuracy / proportion (0–1) |
| Claude-4-Sonnet | 0.837 | Overall accuracy / proportion (0–1) |
| DeepSeek-V3.1-NonThinking | 0.837 | Overall accuracy / proportion (0–1) |
| Seed2.0-Mini | 0.836 | Overall accuracy / proportion (0–1) |
| Intern-S1 | 0.835 | Overall accuracy / proportion (0–1) |
| DeepSeek-R1-0528 | 0.834 | Overall accuracy / proportion (0–1) |
| Grok-3-mini | 0.830 | Overall accuracy / proportion (0–1) |
| GPT-4-mini (high) | 0.830 | Overall accuracy / proportion (0–1) |
| Qwen3-235B-A22B-Instruct-2507 | 0.830 | Overall accuracy / proportion (0–1) |
| Llama4-Behemoth | 0.828 | Overall accuracy / proportion (0–1) |
| Seed-OSS-36B-Instruct | 0.827 | Overall accuracy / proportion (0–1) |
| LongCat-Flash-Chat | 0.827 | Overall accuracy / proportion (0–1) |
| Qwen3.5-9B | 0.825 | Overall accuracy / proportion (0–1) |
| MiniMax-M2 | 0.820 | Overall accuracy / proportion (0–1) |
| GPT-4.1 | 0.818 | Overall accuracy / proportion (0–1) |
| GLM-4.5-Air | 0.814 | Overall accuracy / proportion (0–1) |
| Deepseek-V3-0324 | 0.813 | Overall accuracy / proportion (0–1) |
| MiniMax-M1 | 0.811 | Overall accuracy / proportion (0–1) |
| Kimi-K2-Instruct | 0.810 | Overall accuracy / proportion (0–1) |
| Qwen3-30B-A3B-Thinking-2507 | 0.809 | Overall accuracy / proportion (0–1) |
| GPT-oss-120B(high) | 0.808 | Overall accuracy / proportion (0–1) |
| Llama4-Maverick | 0.805 | Overall accuracy / proportion (0–1) |
| GPT-o1-mini | 0.803 | Overall accuracy / proportion (0–1) |
| Doubao-1.5-Pro | 0.801 | Overall accuracy / proportion (0–1) |
| MiniMax-M2.5 | 0.801 | Overall accuracy / proportion (0–1) |
| Grok3-Beta | 0.799 | Overall accuracy / proportion (0–1) |
| GPT-o3-mini | 0.794 | Overall accuracy / proportion (0–1) |
| Gemini-2.0-Pro | 0.791 | Overall accuracy / proportion (0–1) |
| Qwen3.5-4B | 0.791 | Overall accuracy / proportion (0–1) |
| HunyuanTurboS | 0.790 | Overall accuracy / proportion (0–1) |
| Grok3-mini-Beta | 0.789 | Overall accuracy / proportion (0–1) |
| Qwen3-30B-A3B-Thinking | 0.785 | Overall accuracy / proportion (0–1) |
| ERNIE-4.5-300B-A47B | 0.784 | Overall accuracy / proportion (0–1) |
| Nemotron-3-Nano-30B-A3B(BF16) | 0.783 | Overall accuracy / proportion (0–1) |
| Nemotron-3-Nano-30B-A3B(FP8) | 0.781 | Overall accuracy / proportion (0–1) |
| Claude-3.5-Sonnet (2024-10-22) | 0.780 | Overall accuracy / proportion (0–1) |
| GPT-4o (2024-11-20) | 0.779 | Overall accuracy / proportion (0–1) |
| Gemini-2.0-Flash | 0.776 | Overall accuracy / proportion (0–1) |
| Qwen2.5-Max | 0.761 | Overall accuracy / proportion (0–1) |
| Phi-4-reasoning-plus | 0.760 | Overall accuracy / proportion (0–1) |
| Deepseek-V3 | 0.7587 | Overall accuracy / proportion (0–1) |
| MiniMax-Text-01 | 0.757 | Overall accuracy / proportion (0–1) |
| Grok-2 | 0.7546 | Overall accuracy / proportion (0–1) |
| Grok-4.1-Fast(Non-Reasoning) | 0.752 | Overall accuracy / proportion (0–1) |
| Llama4-Scout | 0.743 | Overall accuracy / proportion (0–1) |
| Phi-4-reasoning | 0.743 | Overall accuracy / proportion (0–1) |
| GPT-oss-20B(high) | 0.736 | Overall accuracy / proportion (0–1) |
| Llama-3.1-405B-Instruct | 0.733 | Overall accuracy / proportion (0–1) |
| Grok-2-mini | 0.7185 | Overall accuracy / proportion (0–1) |
| Gemini-2.0-Flash-Lite | 0.716 | Overall accuracy / proportion (0–1) |
| Qwen2.5-72B | 0.7159 | Overall accuracy / proportion (0–1) |
| ECHO_Ego_v2_14B | 0.7124 | Overall accuracy / proportion (0–1) |
| QwQ-32B-Preview | 0.7097 | Overall accuracy / proportion (0–1) |
| Phi-4 | 0.704 | Overall accuracy / proportion (0–1) |
| ERNIE-4.5-300B-A47B-Base | 0.695 | Overall accuracy / proportion (0–1) |
| Qwen2.5-32B | 0.6923 | Overall accuracy / proportion (0–1) |
| SkyThought-T1 | 0.692 | Overall accuracy / proportion (0–1) |
| Gemini-1.5-Pro | 0.6903 | Overall accuracy / proportion (0–1) |
| Qwen3-235B-A22B | 0.6818 | Overall accuracy / proportion (0–1) |
| Gemma-3-27B-it | 0.675 | Overall accuracy / proportion (0–1) |
| Hunyuan-A13B | 0.673 | Overall accuracy / proportion (0–1) |
| General-Reasoner-14B | 0.666 | Overall accuracy / proportion (0–1) |
| Mistral-Small-instruct | 0.663 | Overall accuracy / proportion (0–1) |
| Seed-OSS-36B-Base(w/ syn.) | 0.651 | Overall accuracy / proportion (0–1) |
| Nemotron-3-Nano-30B-A3B-Base | 0.651 | Overall accuracy / proportion (0–1) |
| Reka 3 | 0.650 | Overall accuracy / proportion (0–1) |
| Qwen2.5-14B | 0.6369 | Overall accuracy / proportion (0–1) |
| Higgs-Llama-3-70B | 0.6316 | Overall accuracy / proportion (0–1) |
| azerogpt | 0.6307 | Overall accuracy / proportion (0–1) |
| RRD2.5-9B | 0.6184 | Overall accuracy / proportion (0–1) |
| Qwen3-30B-A3B-Base | 0.617 | Overall accuracy / proportion (0–1) |
| Llama-3.1-405B | 0.616 | Overall accuracy / proportion (0–1) |
| Gemma-3-12B-it | 0.606 | Overall accuracy / proportion (0–1) |
| Nemotron-H-56B-Base | 0.605 | Overall accuracy / proportion (0–1) |
| Seed-OSS-36B-Base(w/o syn.) | 0.604 | Overall accuracy / proportion (0–1) |
| Hunyuan-Large | 0.602 | Overall accuracy / proportion (0–1) |
| General-Reasoner-7B | 0.589 | Overall accuracy / proportion (0–1) |
| Mimo-7B-RL | 0.586 | Overall accuracy / proportion (0–1) |
| NewenAI/Phi4-sft | 0.577 | Overall accuracy / proportion (0–1) |
| Internlm3-8B-Instruct | 0.576 | Overall accuracy / proportion (0–1) |
| ERNIE-4.5-21B-A3B-Base | 0.567 | Overall accuracy / proportion (0–1) |
| Qwen2.5-Turbo | 0.556 | Overall accuracy / proportion (0–1) |
| Qwen3.5-2B | 0.553 | Overall accuracy / proportion (0–1) |
| Mistral-Small-base | 0.544 | Overall accuracy / proportion (0–1) |
| Phi-4-mini | 0.528 | Overall accuracy / proportion (0–1) |
| Cohere-Aya-Vision | 0.472 | Overall accuracy / proportion (0–1) |
| Qwen2.5-7B | 0.450 | Overall accuracy / proportion (0–1) |
| Nemotron-H-8B-Base | 0.440 | Overall accuracy / proportion (0–1) |
| Qwen2.5-3B | 0.4373 | Overall accuracy / proportion (0–1) |
| Gemma-3-4B-it | 0.436 | Overall accuracy / proportion (0–1) |
| Mimo-7B-base | 0.419 | Overall accuracy / proportion (0–1) |
| LLaDA | 0.370 | Overall accuracy / proportion (0–1) |
| LLaDA | 0.370 | Overall accuracy / proportion (0–1) |
| Qwen2.5-1.5B | 0.3210 | Overall accuracy / proportion (0–1) |
| Qwen3.5-0.8B | 0.297 | Overall accuracy / proportion (0–1) |
| Gemma-2-2B-it | 0.156 | Overall accuracy / proportion (0–1) |
| Qwen2.5-0.5B | 0.1492 | Overall accuracy / proportion (0–1) |
| Gemma-3-1B-it | 0.147 | Overall accuracy / proportion (0–1) |

- **Gemini-3-Pro(11/25)**：- **rank**：1；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-o1**：- **rank**：2；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-4.6-Opus(Thinking)**：- **rank**：3；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-3-Flash(12/25)**：- **rank**：4；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MiniMax-M2.1**：- **rank**：5；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：229；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-397B-A17B**：- **rank**：6；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：397；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed2.0-Lite**：- **rank**：7；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-5.4**：- **rank**：8；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-5.2**：- **rank**：9；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-4.5-Sonnet(Thinking)**：- **rank**：10；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-4-Opus-Thinking**：- **rank**：11；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-4.5-Opus(Thinking)**：- **rank**：12；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-4.6-Sonnet(Thinking)**：- **rank**：13；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Hunyuan-T1**：- **rank**：14；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：389；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-5(high)**：- **rank**：15；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **K2.5-1T-A32B**：- **rank**：16；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：1000；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed-Thinking-v1.5**：- **rank**：17；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：200；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok-4**：- **rank**：18；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed2.0-Pro**：- **rank**：19；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-122B-A10B**：- **rank**：20；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：122；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed1.6-Thinking**：- **rank**：21；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：200；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed1.6-Base**：- **rank**：22；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：200；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed1.6-Ada-Thinking**：- **rank**：23；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：200；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-5.1**：- **rank**：24；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-3.1-Flash-Lite-Preview**：- **rank**：25；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4.5**：- **rank**：26；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-27B**：- **rank**：27；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：27；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-2.5-Pro**：- **rank**：28；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GLM-5**：- **rank**：29；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：754；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-Max-Thinking**：- **rank**：30；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-35B-A3B**：- **rank**：31；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：35；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-o3-high**：- **rank**：32；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-V3.2-Thinking**：- **rank**：33；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：685；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-V3.1-Thinking**：- **rank**：34；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：681；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GLM-4.5**：- **rank**：35；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：355；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-235B-A22B-Thinking-2507**：- **rank**：36；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：235；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok-4.1-Fast(Reasoning)**：- **rank**：37；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-R1**：- **rank**：38；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：671；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3.7-Sonnet-Thinking**：- **rank**：39；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-4-Sonnet**：- **rank**：40；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-V3.1-NonThinking**：- **rank**：41；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：671；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed2.0-Mini**：- **rank**：42；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Intern-S1**：- **rank**：43；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：235；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **DeepSeek-R1-0528**：- **rank**：44；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：671；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok-3-mini**：- **rank**：45；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4-mini (high)**：- **rank**：46；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-235B-A22B-Instruct-2507**：- **rank**：47；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：235；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama4-Behemoth**：- **rank**：48；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：2000；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed-OSS-36B-Instruct**：- **rank**：49；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：36；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **LongCat-Flash-Chat**：- **rank**：50；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：560；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-9B**：- **rank**：51；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MiniMax-M2**：- **rank**：52；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：229；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4.1**：- **rank**：53；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GLM-4.5-Air**：- **rank**：54；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：106；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Deepseek-V3-0324**：- **rank**：55；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：671；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MiniMax-M1**：- **rank**：56；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：456；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Kimi-K2-Instruct**：- **rank**：57；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：1000；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-30B-A3B-Thinking-2507**：- **rank**：58；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：30；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-oss-120B(high)**：- **rank**：59；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：120；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama4-Maverick**：- **rank**：60；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：400；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-o1-mini**：- **rank**：61；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Doubao-1.5-Pro**：- **rank**：62；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MiniMax-M2.5**：- **rank**：63；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：229；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok3-Beta**：- **rank**：64；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-o3-mini**：- **rank**：65；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-2.0-Pro**：- **rank**：66；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-4B**：- **rank**：67；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：4；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **HunyuanTurboS**：- **rank**：68；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：560；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok3-mini-Beta**：- **rank**：69；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-30B-A3B-Thinking**：- **rank**：70；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：30；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **ERNIE-4.5-300B-A47B**：- **rank**：71；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：300；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Nemotron-3-Nano-30B-A3B(BF16)**：- **rank**：72；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：30；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Nemotron-3-Nano-30B-A3B(FP8)**：- **rank**：73；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：30；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Claude-3.5-Sonnet (2024-10-22)**：- **rank**：74；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-4o (2024-11-20)**：- **rank**：75；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-2.0-Flash**：- **rank**：76；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-Max**：- **rank**：77；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi-4-reasoning-plus**：- **rank**：78；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Deepseek-V3**：- **rank**：79；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：671；- **Biology**：0.8689；- **Business**：0.8099；- **Chemistry**：0.7951；- **Computer Science**：0.7951；- **Economics**：0.8175；- **Engineering**：0.6223；- **Health**：0.7372；- **History**：0.6824；- **Law**：0.5477；- **Math**：0.8616；- **Philosophy**：0.7154；- **Physics**：0.7898；- **Psychology**：0.7882；- **Other**：0.7641；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **MiniMax-Text-01**：- **rank**：80；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：456；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok-2**：- **rank**：81；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8842；- **Business**：0.7896；- **Chemistry**：0.7703；- **Computer Science**：0.7585；- **Economics**：0.8187；- **Engineering**：0.6078；- **Health**：0.7592；- **History**：0.6982；- **Law**：0.6167；- **Math**：0.7927；- **Philosophy**：0.7234；- **Physics**：0.7729；- **Psychology**：0.8133；- **Other**：0.7662；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok-4.1-Fast(Non-Reasoning)**：- **rank**：82；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama4-Scout**：- **rank**：83；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：109；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi-4-reasoning**：- **rank**：84；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **GPT-oss-20B(high)**：- **rank**：85；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：20；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-405B-Instruct**：- **rank**：86；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：405；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Grok-2-mini**：- **rank**：87；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8465；- **Business**：0.7566；- **Chemistry**：0.7429；- **Computer Science**：0.7317；- **Economics**：0.8092；- **Engineering**：0.5624；- **Health**：0.7518；- **History**：0.6719；- **Law**：0.5367；- **Math**：0.7609；- **Philosophy**：0.6553；- **Physics**：0.7328；- **Psychology**：0.7994；- **Other**：0.7197；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-2.0-Flash-Lite**：- **rank**：88；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-72B**：- **rank**：89；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：72；- **Biology**：0.8326；- **Business**：0.7693；- **Chemistry**：0.7314；- **Computer Science**：0.7488；- **Economics**：0.8104；- **Engineering**：0.5645；- **Health**：0.6956；- **History**：0.6745；- **Law**：0.4914；- **Math**：0.8120；- **Philosophy**：0.6473；- **Physics**：0.7498；- **Psychology**：0.7857；- **Other**：0.7100；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **ECHO_Ego_v2_14B**：- **rank**：90；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：0.8396；- **Business**：0.7807；- **Chemistry**：0.7624；- **Computer Science**：0.739；- **Economics**：0.7642；- **Engineering**：0.5641；- **Health**：0.6993；- **History**：0.6063；- **Law**：0.4069；- **Math**：0.8764；- **Philosophy**：0.6152；- **Physics**：0.8014；- **Psychology**：0.7419；- **Other**：0.671；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **QwQ-32B-Preview**：- **rank**：91；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：0.8490；- **Business**：0.7506；- **Chemistry**：0.7429；- **Computer Science**：0.4571；- **Economics**：0.5469；- **Engineering**：0.6569；- **Health**：0.7784；- **History**：0.7506；- **Law**：0.7605；- **Math**：0.6916；- **Philosophy**：0.8494；- **Physics**：0.6573；- **Psychology**：0.7732；- **Other**：None；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi-4**：- **rank**：92；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **ERNIE-4.5-300B-A47B-Base**：- **rank**：93；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：300；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-32B**：- **rank**：94；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：0.8396；- **Business**：0.7567；- **Chemistry**：0.7032；- **Computer Science**：0.7390；- **Economics**：0.7725；- **Engineering**：0.5480；- **Health**：0.6932；- **History**：0.5932；- **Law**：0.4541；- **Math**：0.8053；- **Philosophy**：0.6152；- **Physics**：0.7259；- **Psychology**：0.7569；- **Other**：0.6645；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **SkyThought-T1**：- **rank**：95；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemini-1.5-Pro**：- **rank**：96；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8466；- **Business**：0.7288；- **Chemistry**：0.7032；- **Computer Science**：0.7293；- **Economics**：0.7844；- **Engineering**：0.4871；- **Health**：0.7274；- **History**：0.6562；- **Law**：0.5077；- **Math**：0.7276；- **Philosophy**：0.6172；- **Physics**：0.7036；- **Psychology**：0.7720；- **Other**：0.7251；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-235B-A22B**：- **rank**：97；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：235；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-3-27B-it**：- **rank**：98；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：27；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Hunyuan-A13B**：- **rank**：99；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：80；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **General-Reasoner-14B**：- **rank**：100；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Small-instruct**：- **rank**：101；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：24；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed-OSS-36B-Base(w/ syn.)**：- **rank**：102；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：36；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Nemotron-3-Nano-30B-A3B-Base**：- **rank**：103；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：30；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Reka 3**：- **rank**：104；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：21；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-14B**：- **rank**：105；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：0.7978；- **Business**：0.7085；- **Chemistry**：0.6873；- **Computer Science**：0.6707；- **Economics**：0.7310；- **Engineering**：0.4954；- **Health**：0.6222；- **History**：0.5774；- **Law**：0.3660；- **Math**：0.6788；- **Philosophy**：0.5711；- **Physics**：0.6844；- **Psychology**：0.7243；- **Other**：0.6288；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Higgs-Llama-3-70B**：- **rank**：106；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：70；- **Biology**：0.8354；- **Business**：0.6743；- **Chemistry**：0.6034；- **Computer Science**：0.6902；- **Economics**：0.7512；- **Engineering**：0.4737；- **Health**：0.6687；- **History**：0.6404；- **Law**：0.4432；- **Math**：0.6321；- **Philosophy**：0.5591；- **Physics**：0.5989；- **Psychology**：0.7619；- **Other**：0.6613；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **azerogpt**：- **rank**：107；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8215；- **Business**：0.6667；- **Chemistry**：0.508；- **Computer Science**：0.6683；- **Economics**：0.7393；- **Engineering**：0.4828；- **Health**：0.665；- **History**：0.6693；- **Law**：0.4587；- **Math**：0.6329；- **Philosophy**：0.6212；- **Physics**：0.5751；- **Psychology**：0.7506；- **Other**：0.6591；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **RRD2.5-9B**：- **rank**：108；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：9；- **Biology**：0.7824；- **Business**：0.6820；- **Chemistry**：0.6078；- **Computer Science**：0.6561；- **Economics**：0.7204；- **Engineering**：0.4857；- **Health**：0.6198；- **History**：0.5381；- **Law**：0.3733；- **Math**：0.7365；- **Philosophy**：0.5471；- **Physics**：0.6020；- **Psychology**：0.7118；- **Other**：0.6082；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3-30B-A3B-Base**：- **rank**：109；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：30；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Llama-3.1-405B**：- **rank**：110；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：405；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-3-12B-it**：- **rank**：111；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：12；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Nemotron-H-56B-Base**：- **rank**：112；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：56；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Seed-OSS-36B-Base(w/o syn.)**：- **rank**：113；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：36；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Hunyuan-Large**：- **rank**：114；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：389；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **General-Reasoner-7B**：- **rank**：115；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mimo-7B-RL**：- **rank**：116；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **NewenAI/Phi4-sft**：- **rank**：117；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：14；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Internlm3-8B-Instruct**：- **rank**：118；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **ERNIE-4.5-21B-A3B-Base**：- **rank**：119；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：21；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-Turbo**：- **rank**：120；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-2B**：- **rank**：121；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：2；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mistral-Small-base**：- **rank**：122；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：24；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Phi-4-mini**：- **rank**：123；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：5.6；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Cohere-Aya-Vision**：- **rank**：124；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：32；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-7B**：- **rank**：125；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Nemotron-H-8B-Base**：- **rank**：126；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-3B**：- **rank**：127；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：3；- **Biology**：0.5453；- **Business**：0.5412；- **Chemistry**：0.4072；- **Computer Science**：0.4317；- **Economics**：0.5296；- **Engineering**：0.2921；- **Health**：0.4401；- **History**：0.3911；- **Law**：0.2234；- **Math**：0.5455；- **Philosophy**：0.3707；- **Physics**：0.4403；- **Psychology**：0.5551；- **Other**：0.4145；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-3-4B-it**：- **rank**：128；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：4；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Mimo-7B-base**：- **rank**：129；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：7；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **LLaDA**：- **rank**：130；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **LLaDA**：- **rank**：131；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：8；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-1.5B**：- **rank**：132；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：1.5；- **Biology**：0.4351；- **Business**：0.3739；- **Chemistry**：0.2562；- **Computer Science**：0.3512；- **Economics**：0.3886；- **Engineering**：0.1899；- **Health**：0.3362；- **History**：0.2782；- **Law**：0.1480；- **Math**：0.4301；- **Philosophy**：0.2786；- **Physics**：0.2856；- **Psychology**：0.4687；- **Other**：0.3247；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen3.5-0.8B**：- **rank**：133；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：0.8；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-2-2B-it**：- **rank**：134；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：2；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Qwen2.5-0.5B**：- **rank**：135；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：0.5；- **Biology**：0.2078；- **Business**：0.1458；- **Chemistry**：0.1157；- **Computer Science**：0.1366；- **Economics**：0.2251；- **Engineering**：0.1104；- **Health**：0.1687；- **History**：0.1312；- **Law**：0.1335；- **Math**：0.1325；- **Philosophy**：0.1323；- **Physics**：0.1224；- **Psychology**：0.2118；- **Other**：0.1504；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造
- **Gemma-3-1B-it**：- **rank**：136；- **data_source**：Self-Reported；- **per_subject_and_size**：- **Model Size(B)**：1；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）

#### 官方Space底表 / TIGER-LAb

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude-3.5-Sonnet (2024-10-22) | 0.7764 | Overall accuracy / proportion (0–1) |

- **Claude-3.5-Sonnet (2024-10-22)**：- **rank**：1；- **data_source**：TIGER-LAb；- **per_subject_and_size**：- **Model Size(B)**：unk；- **Biology**：0.8856；- **Business**：0.8137；- **Chemistry**：0.7853；- **Computer Science**：0.8244；- **Economics**：0.859；- **Engineering**：0.613；- **Health**：0.7689；- **History**：0.7375；- **Law**：0.6458；- **Math**：0.8105；- **Philosophy**：0.7675；- **Physics**：0.7729；- **Psychology**：0.8459；- **Other**：0.8019；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）

#### 官方Space底表 / Sefl-Reported

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Mistral-3.1-Small | 0.668 | Overall accuracy / proportion (0–1) |

- **Mistral-3.1-Small**：- **rank**：1；- **data_source**：Sefl-Reported；- **per_subject_and_size**：- **Model Size(B)**：24；- **Biology**：-；- **Business**：-；- **Chemistry**：-；- **Computer Science**：-；- **Economics**：-；- **Engineering**：-；- **Health**：-；- **History**：-；- **Law**：-；- **Math**：-；- **Philosophy**：-；- **Physics**：-；- **Psychology**：-；- **Other**：-；- **protocol**：该行未给出完整shot/CoT/checkpoint/运行日期，不能补造

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）

> 完整转录当前官方Space公开CSV，按Data Source分轨，保留原始小数；不把模型简称扩写成API日期。

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）；[来源](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro/raw/main/utils.py)（访问 2026-11-08）

### 覆盖范围与时效

通过公开Space app.py→utils.py确认底表为TIGER-Lab/mmlu_pro_leaderboard_submission/results.csv，已全量读取。TIGER-Lab实测与Self-Reported分轨，README mini榜不再冒充最新榜。AA页面打开，但可读正文没有具体模型分数，不补造AA排名。

[来源](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv)（访问 2026-11-08）；[来源](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro/raw/main/utils.py)（访问 2026-11-08）；[来源](https://artificialanalysis.ai/evaluations/mmlu-pro)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

- y726wang@uwaterloo.ca
- x93ma@uwaterloo.ca
- wenhuchen@uwaterloo.ca

[来源](https://github.com/TIGER-AI-Lab/MMLU-Pro)（访问 2026-11-08）

### 公开反馈

https://github.com/TIGER-AI-Lab/MMLU-Pro/issues

[来源](https://github.com/TIGER-AI-Lab/MMLU-Pro)（访问 2026-11-08）

### 官方社交

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2406.01574)（访问 2026-11-08）

### 隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2406.01574

[来源](https://arxiv.org/pdf/2406.01574)（访问 2026-11-08）

### PDF SHA-256

e8f695db151fc8820f20c2864e6f6e27769fd94a307b7e60e211912cc9a3ef59

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2406.01574)（访问 2026-11-08）

### PDF字节数

959520

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2406.01574)（访问 2026-11-08）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/TIGER-AI-Lab/MMLU-Pro/main/README.md)（访问 2026-11-08）
