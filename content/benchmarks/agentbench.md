# AgentBench

> 核验日期：2026-11-07。；访问日不是测量日。

已重新检索官方材料；历史榜单/当前快照/厂商自报分离；未实证字段保留待核实

原始八环境与当前五环境FC版是两套聚合口径。本页同时保存FC官方CSV和原论文基线，但不将百分成功率与归一化Overall分混排。

## 基本信息

### 简称

AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 全称

AgentBench

> 保留官方名称，不把论文标题自动扩写为全称。

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 基准版本

当前仓库为AgentBench FC（2025-10-10发布，5个函数调用环境）；原始8环境仍在v0.1/v0.2分支。

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）

### 论文版本

arXiv v3

> 论文修订版本不等同数据集版本。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 发布日期

2023-08-08 00:08:11（arXiv首稿）

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 领域标签

- 交互式Agent综合能力

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 许可证

Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2308.03688

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 官方代码

https://github.com/THUDM/AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 数据地址

https://github.com/THUDM/AgentBench/tree/main/data

> 官方仓库数据目录；KG另需Freebase，不能将目录视为包含所有第三方环境依赖的一键数据包。

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）

### 官方入口

https://github.com/THUDM/AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 论文标题

AgentBench: Evaluating LLMs as Agents

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

## 发起与维护

### 发起方

Tsinghua University、Ohio State University、UC Berkeley 等作者单位。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 作者

- Liu, Xiao
- Yu, Hao
- Zhang, Hanchen
- Xu, Yifan
- Lei, Xuanyu
- Lai, Hanyu
- Gu, Yu
- Ding, Hangliang
- Men, Kaiwen
- Yang, Kejuan
- Zhang, Shudan
- Deng, Xiang
- Zeng, Aohan
- Du, Zhengxiao
- Zhang, Chenhui
- Shen, Sheng
- Zhang, Tianjun
- Su, Yu
- Sun, Huan
- Huang, Minlie
- Dong, Yuxiao
- Tang, Jie

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 维护方

THUDM / AgentBench 项目团队

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 资助方

论文致谢 Zhipu AI 的 GPU/API 支持及科研项目资助；完整资助清单见原文。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

## 设计目标

### 衡量能力

跨环境长程交互、工具执行、决策、遵循反馈与完成目标的综合Agent能力。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 设计背景

单轮静态语言/知识任务难以评估可行动Agent，不同交互环境的能力差异被单任务掩盖。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

## 构建方式

### 题目来源

8环境：OS、Database、Knowledge Graph、Digital Card Game、Lateral Thinking Puzzles、Household(ALFWorld)、Web Shopping(WebShop)、Web Browsing(Mind2Web)。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 出题者背景

多校研究团队；混合自建环境和既有任务，不是统一专家原创题。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 审核流程

各环境构造任务、交互接口与专用评测；不能把所有环境说成同一审核流程。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 质量控制

统一消息/行动框架，环境特定预算与有效性检查；失败轨迹用于误差分析。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 去污染

包含已公开数据和环境，不能保证完全排除训练重叠；原论文设置不等于隐藏新题。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

## 数据形式

### 题量与规模

原始dev269、test1,014；各环境题量和指标不相同。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 题型

原始版8环境包括OS、DB、KG、DCG、LTP、ALFWorld、WebShop、Mind2Web；当前FC版支持alfworld/dbbench/knowledgegraph/os_interaction/webshop共5环境，函数调用提示并支持Docker Compose。

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）

### 模态

- 文本
- 代码/工具动作
- 模拟环境

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 语言

英语指令为主；含SQL、shell等行动语言。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 难度

依环境和任务变化；不能按一个统一题目难度分布概括。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 公开与隐藏划分

原论文报告dev/test划分，代码与环境公开；split用途不等于永久隐藏测试。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

## 评测方法

### 指标

各环境SR、F1、reward、游戏进度、step SR等；Overall为归一化后的加权环境平均，不是百分准确率。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 评分

环境专用成功判定后再规范化聚合；必须保留单项分数与归一化方式。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 运行设置

原论文简单CoT策略，温度0，无多重重试/集成，约3500-token上下文裁剪，环境各有固定行动预算。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 官方脚本

https://github.com/THUDM/AgentBench

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 可比性警示

FC版五环境pass@1均值，与原始八环境Overall归一化分是不同协议；不能将70.4%与4.01直接比较。需固定分支、容器与Prompt/Function Calling模式。

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）；[来源2]（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 最新版本与采用证据

```json
{
 "version": "AgentBench FC（2025-10-10），当前main；原始8环境v0.1/v0.2独立保留"
 "evidence_2026_h2": [
 {
 "url": "https://arxiv.org/html/2609.19134v1"
 "date": "2026-09-17"
 "note": "ScienceIDE §4.2及参考文献明确引用 AgentBench 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。"
 "date_shanghai": "2026-09-17"

 }
 ]
}
```

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2023-08-08"
 }
 {
 "version": "v2"
 "submitted_at": "2023-10-25"
 }
 {
 "version": "v3"
 "submitted_at": "2025-10-04"
 }
]
```

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 饱和情况

当前FC榜单最高五环境AVG pass@1为70.4%；ALFWorld与OS等环境差距明显，不能仅用一个均值称原始八环境或全部Agent能力已饱和。

### 污染与争议

异质环境与指标聚合可能掩盖不同短板；公开任务污染与上下文/工具失败须和推理能力分开。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 版本与衍生关系

AgentBench FC（5环境函数调用、AgentRL/Docker集成）；VisualAgentBench（2024-08-13，视觉Agent的5个独立环境），不与原始8环境合并排名。

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 官方榜单

待核实

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）；[来源2]（访问 2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 分轨结果

#### AgentBench FC官方Sheet

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | AgentRL w/ Qwen2.5-32B-Instruct | 70.4 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 2 | AgentRL w/ Qwen2.5-14B-Instruct | 67.7 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 3 | AgentRL w/ GLM-4-9B-0414 | 65.0 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 4 | AgentRL w/ Qwen2.5-7B-Instruct | 62.0 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 5 | AgentRL w/ Qwen2.5-3B-Instruct | 60.0 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 6 | Claude Sonnet 4.5 (2025-09-29) | 58.9 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 7 | Claude Sonnet 4.5 Thinking (2025-09-29) | 58.3 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 8 | Claude Sonnet 4 Thinking (2025-05-14) | 58.2 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 9 | Claude Sonnet 4 (2025-05-14) | 57.4 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 10 | Claude Sonnet 3.7 (2025-02-19) | 53.2 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 11 | GPT-5 (2025-08-07) | 52.2 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 12 | AgentLM-70B | 51.4 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 13 | Claude Sonnet 3.7 Thinking (2025-02-19) | 50.0 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 14 | DeepSeek-R1 (2025-05-28) | 49.3 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 15 | AgentLM-13B | 45.1 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 16 | AgentLM-7B | 42.7 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 17 | o3-mini (2025-01-31) | 40.9 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 18 | Qwen2.5-72B-Instruct | 40.8 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 19 | o4-mini (2025-04-16) | 39.7 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 20 | GPT-4o (2024-11-20) | 39.6 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 21 | Qwen2.5-32B-Instruct | 37.2 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 22 | Hephaestus-8B-IFT | 36.3 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 23 | DeepSeek-V3 (2025-03-24) | 36.1 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 24 | Hephaestus-8B-Base | 31.9 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |
| 25 | Qwen2.5-14B-Instruct | 27.2 | 五环境AVG pass@1 (%) | [原表]，2026-11-07 |

> AgentRL w/ Qwen2.5-32B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 94.5, "DB": 70.4, "KG": 77.0, "OS": 51.7, "WebShop": 58.6}}

> AgentRL w/ Qwen2.5-14B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 91.5, "DB": 72.2, "KG": 72.8, "OS": 43.6, "WebShop": 58.5}}

> AgentRL w/ GLM-4-9B-0414：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 93.3, "DB": 66.9, "KG": 75.7, "OS": 33.2, "WebShop": 55.9}}

> AgentRL w/ Qwen2.5-7B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 91.5, "DB": 63.7, "KG": 57.8, "OS": 40.8, "WebShop": 56.1}}

> AgentRL w/ Qwen2.5-3B-Instruct：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 92.4, "DB": 60.0, "KG": 55.0, "OS": 40.5, "WebShop": 52.1}}

> Claude Sonnet 4.5 (2025-09-29)：{"model_organization": "Anthropic", "result_source": "-", "source_release_month": "11/2025", "subscores": {"ALFWorld": 82.5, "DB": 71.2, "KG": 64.1, "OS": 38.0, "WebShop": 38.6}}

> Claude Sonnet 4.5 Thinking (2025-09-29)：{"model_organization": "Anthropic", "result_source": "-", "source_release_month": "11/2025", "subscores": {"ALFWorld": 80.7, "DB": 70.3, "KG": 62.7, "OS": 39.4, "WebShop": 38.2}}

> Claude Sonnet 4 Thinking (2025-05-14)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 69.0, "DB": 68.4, "KG": 64.4, "OS": 51.0, "WebShop": 38.3}}

> Claude Sonnet 4 (2025-05-14)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 73.6, "DB": 70.1, "KG": 63.4, "OS": 45.3, "WebShop": 34.6}}

> Claude Sonnet 3.7 (2025-02-19)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 61.1, "DB": 68.5, "KG": 59.8, "OS": 36.5, "WebShop": 40.1}}

> GPT-5 (2025-08-07)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 65.4, "DB": 63.2, "KG": 64.1, "OS": 34.5, "WebShop": 33.7}}

> AgentLM-70B：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 86.0, "DB": 37.7, "KG": 47.0, "OS": 21.5, "WebShop": 64.9}}

> Claude Sonnet 3.7 Thinking (2025-02-19)：{"model_organization": "Anthropic", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 54.1, "DB": 68.4, "KG": 38.2, "OS": 53.1, "WebShop": 36.0}}

> DeepSeek-R1 (2025-05-28)：{"model_organization": "DeepSeek", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 51.4, "DB": 60.4, "KG": 50.2, "OS": 53.6, "WebShop": 31.0}}

> AgentLM-13B：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 76.0, "DB": 33.7, "KG": 26.8, "OS": 18.1, "WebShop": 70.8}}

> AgentLM-7B：{"model_organization": "Z.ai", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 84.0, "DB": 30.6, "KG": 18.1, "OS": 17.4, "WebShop": 63.6}}

> o3-mini (2025-01-31)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 28.4, "DB": 56.5, "KG": 51.8, "OS": 35.1, "WebShop": 32.7}}

> Qwen2.5-72B-Instruct：{"model_organization": "Alibaba", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 47.5, "DB": 45.3, "KG": 26.5, "OS": 49.5, "WebShop": 35.4}}

> o4-mini (2025-04-16)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 32.6, "DB": 63.4, "KG": 32.4, "OS": 41.8, "WebShop": 28.5}}

> GPT-4o (2024-11-20)：{"model_organization": "OpenAI", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 28.3, "DB": 54.3, "KG": 49.3, "OS": 38.5, "WebShop": 27.8}}

> Qwen2.5-32B-Instruct：{"model_organization": "Alibaba", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 32.1, "DB": 55.8, "KG": 33.8, "OS": 37.0, "WebShop": 27.5}}

> Hephaestus-8B-IFT：{"model_organization": "Amazon", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 46.0, "DB": 29.7, "KG": 21.2, "OS": 20.8, "WebShop": 63.9}}

> DeepSeek-V3 (2025-03-24)：{"model_organization": "DeepSeek", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 31.9, "DB": 58.4, "KG": 14.0, "OS": 53.0, "WebShop": 23.4}}

> Hephaestus-8B-Base：{"model_organization": "Amazon", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 30.0, "DB": 32.3, "KG": 16.0, "OS": 20.8, "WebShop": 60.5}}

> Qwen2.5-14B-Instruct：{"model_organization": "Alibaba", "result_source": "AgentRL", "source_release_month": "10/2025", "subscores": {"ALFWorld": 8.7, "DB": 48.4, "KG": 35.3, "OS": 26.0, "WebShop": 17.6}}

#### 原始8环境/论文历史Table3

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 不适用（来源内选列，非全局排名） | GPT-4-0613 | 4.01 | Overall归一化分 | [原表](https://arxiv.org/abs/2308.03688)，2026-11-07 |
| 不适用（来源内选列，非全局排名） | Claude 3 Opus | 3.11 | Overall归一化分 | [原表](https://arxiv.org/abs/2308.03688)，2026-11-07 |
| 不适用（来源内选列，非全局排名） | GLM-4 | 2.89 | Overall归一化分 | [原表](https://arxiv.org/abs/2308.03688)，2026-11-07 |

> FC结果来自实际下载官方CSV；Release Date列按来源原名保存，不冒充实验运行时间。

[来源1]（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### 覆盖说明

官方CSV共25行FC模型，另列原始8环境历史三行。FC前三为70.4/67.7/65.0；前三Release Date为10/2025，其余有11/2025，不冒充实际运行日。原始Overall归一化分与FC百分均值不能混排。

## 联系方式

### 公开科研联系邮箱

- agentbench_fc@googlegroups.com
- agentbench@googlegroups.com

> FC版结果提交联系前者；仓库原始Google Group入口为后者。

[来源1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07）

### 公开反馈

https://github.com/THUDM/AgentBench/issues

> 公开仓库反馈入口；未发送问题。

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 官方社交

https://twitter.com/thukeg

> 官方仓库展示的团队账号链接；未访问X内容。

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）

### 隐私说明/政策

待核实

> 字段状态：待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2308.03688

[来源1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07）

### PDF SHA-256

9c780e35fc0b2de6c2e21e0572f6aaaadcf7ecdd56d63cfaae2b415bc0dc83c3

> 实际下载字节的SHA-256；不表示已有副本已替换。

[来源1](https://arxiv.org/pdf/2308.03688)（访问 2026-11-07）

### PDF字节数

23017024

[来源1](https://arxiv.org/pdf/2308.03688)（访问 2026-11-07）

### 论文副本

## 变更记录

```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-07"
 "round": "1 / 深度实证复核"
 最近复核
 }
 {
 "date": "2026-11-07"
 最近复核
 }
]
```

[来源1](https://github.com/THUDM/AgentBench)（访问 2026-11-07）
