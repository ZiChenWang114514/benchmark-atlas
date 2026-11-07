# AgentBench

> 第1轮深度复核：2026-11-07（KST / Asia/Seoul）。采集日不等于榜单更新日或评测运行日；“待核实”不等于不存在。

[阅读Drive原始论文PDF](https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk)

## 基本信息

### 简称

AgentBench

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 全称

AgentBench

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 基准版本

当前仓库为AgentBench FC（2025-10-10发布，5个函数调用环境）；原始8环境仍在v0.1/v0.2分支。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）。

### 论文版本

arXiv v3

> 论文修订版本不等同数据集版本。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 发布日期

2023-08-08 01:08:11 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 领域标签

- 交互式Agent综合能力

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 许可证

Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 论文

https://arxiv.org/abs/2308.03688

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 官方代码

https://github.com/THUDM/AgentBench

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 数据地址

https://github.com/THUDM/AgentBench/tree/main/data

> 官方仓库数据目录；KG另需Freebase，不能将目录视为包含所有第三方环境依赖的一键数据包。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）。

### 官方入口

https://github.com/THUDM/AgentBench

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 论文标题

AgentBench: Evaluating LLMs as Agents

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

## 发起与维护

### 发起机构

Tsinghua University、Ohio State University、UC Berkeley 等作者单位。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 合作研究机构

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

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

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 维护方

THUDM / AgentBench 项目团队

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 资助

论文致谢 Zhipu AI 的 GPU/API 支持及科研项目资助；完整资助清单见原文。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

## 设计目标

### 衡量能力

跨环境长程交互、工具执行、决策、遵循反馈与完成目标的综合Agent能力。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 设计背景

单轮静态语言/知识任务难以评估可行动Agent，不同交互环境的能力差异被单任务掩盖。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

## 构建方式

### 题目来源

8环境：OS、Database、Knowledge Graph、Digital Card Game、Lateral Thinking Puzzles、Household(ALFWorld)、Web Shopping(WebShop)、Web Browsing(Mind2Web)。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 出题者背景

多校研究团队；混合自建环境和既有任务，不是统一专家原创题。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 审核流程

各环境构造任务、交互接口与专用评测；不能把所有环境说成同一审核流程。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 质量控制

统一消息/行动框架，环境特定预算与有效性检查；失败轨迹用于误差分析。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 去污染

包含已公开数据和环境，不能保证完全排除训练重叠；原论文设置不等于隐藏新题。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

## 数据形式

### 规模

原始dev269、test1,014；各环境题量和指标不相同。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 题型

原始版8环境包括OS、DB、KG、DCG、LTP、ALFWorld、WebShop、Mind2Web；当前FC版支持alfworld/dbbench/knowledgegraph/os_interaction/webshop共5环境，函数调用提示并支持Docker Compose。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）。

### 模态

- 文本
- 代码/工具动作
- 模拟环境

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 语言

英语指令为主；含SQL、shell等行动语言。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 难度与类型

依环境和任务变化；不能按一个统一题目难度分布概括。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 公开与隐藏划分

原论文报告dev/test划分，代码与环境公开；split用途不等于永久隐藏测试。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

## 评测方法

### 指标

各环境SR、F1、reward、游戏进度、step SR等；Overall为归一化后的加权环境平均，不是百分准确率。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 评分

环境专用成功判定后再规范化聚合；必须保留单项分数与归一化方式。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 提示和复现设置

原论文简单CoT策略，温度0，无多重重试/集成，约3500-token上下文裁剪，环境各有固定行动预算。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 官方脚本

https://github.com/THUDM/AgentBench

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 可比性提示

FC版五环境pass@1均值，与原始八环境Overall归一化分是不同协议；不能将70.4%与4.01直接比较。需固定分支、容器与Prompt/Function Calling模式。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）；[2](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-07 KST / Asia/Seoul

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 最新版本与H2证据

- **version**：AgentBench FC（2025-10-10），当前main；原始8环境v0.1/v0.2独立保留
- **evidence_2026_h2**：[{"url": "https://arxiv.org/html/2609.19134v1", "date": "2026-09-17", "note": "ScienceIDE §4.2及参考文献明确引用 AgentBench 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。", "date_kst": "2026-09-17T02:55:47+09:00", "verified_in_round1": "本轮重新打开ScienceIDE正文及参考文献，按原始论文ID确认；属于§4.2相关工作引用，非本文实跑。"}]

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）；[2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07 KST）；[3](https://arxiv.org/abs/2609.19134)（访问 2026-11-07 KST）。

### 论文修订与H2使用证据

Submission history From: Xiao Liu [ view email ] [v1] 2023-08-08 01:08:11 KST (20,331 KB) [v2] 2023-10-25 16:41:24 KST (20,908 KB) [v3] 2025-10-04 12:54:18 KST (20,753 KB)

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 饱和程度

当前FC榜单最高五环境AVG pass@1为70.4%；ALFWorld与OS等环境差距明显，不能仅用一个均值称原始八环境或全部Agent能力已饱和。

来源：[1](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问 2026-11-07 KST）。

### 污染、冲突与限制

异质环境与指标聚合可能掩盖不同短板；公开任务污染与上下文/工具失败须和推理能力分开。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 后续工作与衍生

AgentBench FC（5环境函数调用、AgentRL/Docker集成）；VisualAgentBench（2024-08-13，视觉Agent的5个独立环境），不与原始8环境合并排名。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-07 KST / Asia/Seoul

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 官方榜单

https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pubhtml

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）；[2](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问 2026-11-07 KST）。

### 权威第三方覆盖

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 结果快照

- {"model": "AgentRL w/ Qwen2.5-32B-Instruct", "score": 70.4, "unit": "%", "metric": "success rate pass@1，五环境均值", "scope": "AgentBench FC，5环境test；AVG pass@1", "date": "2025-10", "accessed": "2026-11-07 KST", "source_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv", "provenance": "官方当前FC表，非原始八环境论文分数。", "leaderboard_updated_at": "2025-11-18"}
- {"model": "AgentRL w/ Qwen2.5-14B-Instruct", "score": 67.7, "unit": "%", "metric": "success rate pass@1，五环境均值", "scope": "AgentBench FC，5环境test；AVG pass@1", "date": "2025-10", "accessed": "2026-11-07 KST", "source_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv", "provenance": "官方当前FC表，非原始八环境论文分数。", "leaderboard_updated_at": "2025-11-18"}
- {"model": "AgentRL w/ GLM-4-9B-0414", "score": 65.0, "unit": "%", "metric": "success rate pass@1，五环境均值", "scope": "AgentBench FC，5环境test；AVG pass@1", "date": "2025-10", "accessed": "2026-11-07 KST", "source_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv", "provenance": "官方当前FC表，非原始八环境论文分数。", "leaderboard_updated_at": "2025-11-18"}
- {"model": "GPT-4-0613", "score": 4.01, "metric": "Overall归一化分", "benchmark_version": "原始8环境", "result_type": "论文历史基线", "source_date": "论文Table3", "collected_at": "2026-11-07 KST"}
- {"model": "Claude 3 Opus", "score": 3.11, "metric": "Overall归一化分", "benchmark_version": "原始8环境", "result_type": "论文历史基线", "source_date": "论文Table3", "collected_at": "2026-11-07 KST"}
- {"model": "GLM-4", "score": 2.89, "metric": "Overall归一化分", "benchmark_version": "原始8环境", "result_type": "论文历史基线", "source_date": "论文Table3", "collected_at": "2026-11-07 KST"}

来源：[1](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

### 覆盖说明

本轮读取官方FC榜单CSV；公开Sheet标题标updated 2025-11-18，当前前三AVG为70.4/67.7/65.0，Release Date均10/2025。采集日在2026不意味着重新评测；原始8环境基线另列，禁止混排。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）；[2](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pub?output=csv)（访问 2026-11-07 KST）；[3](https://docs.google.com/spreadsheets/d/e/2PACX-1vRR3Wl7wsCgHpwUw1_eUXW_fptAPLL3FkhnW_rua0O1Ji_GIVrpTjY5LaKAhwO-WeARjnY_KNw0SYNJ/pubhtml)（访问 2026-11-07 KST）。

## 联系方式

### 公开联系邮箱

- agentbench_fc@googlegroups.com
- agentbench@googlegroups.com

> FC版结果提交联系前者；仓库原始Google Group入口为后者。

来源：[1](https://raw.githubusercontent.com/THUDM/AgentBench/main/README.md)（访问 2026-11-07 KST）。

### 问题反馈

https://github.com/THUDM/AgentBench/issues

> 公开仓库反馈入口；未发送问题。

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 官方讨论渠道

https://twitter.com/thukeg

> 官方仓库展示的团队账号链接；本轮未访问X内容。

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

### 隐私政策

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2308.03688)（访问 2026-11-07 KST）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2308.03688

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2308.03688)（访问 2026-11-07 KST）。

### SHA-256

9c780e35fc0b2de6c2e21e0572f6aaaadcf7ecdd56d63cfaae2b415bc0dc83c3

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://arxiv.org/pdf/2308.03688)（访问 2026-11-07 KST）。

### 字节数

23017024

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://arxiv.org/pdf/2308.03688)（访问 2026-11-07 KST）。

### Drive文件夹

- **id**：1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6
- **webViewLink**：https://drive.google.com/drive/folders/1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6

来源：[1](https://drive.google.com/drive/folders/1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6)（访问 2026-11-07 KST）。

### 其他文档

- {"type": "中文介绍Google Doc", "id": "1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA", "webViewLink": "https://docs.google.com/document/d/1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA/edit?usp=drivesdk"}

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）；[2](https://docs.google.com/document/d/1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA/edit?usp=drivesdk)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp
- **webViewLink**：https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "round": "1 / 深度实证复核", "change": "纠正当前main已为五环境AgentBench FC，原版八环境留在旧分支；补FC榜单前三和联系；重核H2引用。"}

来源：[1](https://github.com/THUDM/AgentBench)（访问 2026-11-07 KST）。

