# Multi-step SWE

长程软件工程基准，69项任务各含5至15个相互依赖的工程步骤，每一步都在智能体自己此前写出的代码上继续，九个前沿模型中最高解出率仅18.5%。

## 基本信息

**简称**：Multi-step SWE

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**全称**：Multi-step SWE：编码智能体能否在长程任务中持续基于自己的代码构建

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**基准版本**：arXiv:2611.07166v1；69项任务、574个步骤

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**论文版本**：arXiv:2611.07166v1（2026-11-04）

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**发布日期**：2026-11-04

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**主板块**：代码

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**领域标签**：长程软件工程；编码智能体；多步依赖任务；版本升级与迁移

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**许可证**：代码仓库为 MIT 许可证，附带的上游代码保留各自原许可证；论文在 arXiv 采用 CC BY 4.0

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**论文或技术报告**：https://arxiv.org/abs/2611.07166

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**官方代码**：https://github.com/Klavis-AI/Multi-step-SWE

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**数据地址**：https://github.com/Klavis-AI/Multi-step-SWE（任务以 Harbor 多步格式存放于仓库 tasks 目录，含环境、指令、验证器与参考解）

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**官方主页**：https://multistepswe.com/

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**论文题名**：Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 发起与维护

**发起方**：Klavis AI

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**协作机构**：待核实

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**作者**：Xiangkai Zeng、Zheng Liu、Zihao Lin（同等贡献）

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**当前维护方**：Klavis AI

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**资助方**：待核实

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 设计目标

**要测的能力**：考查编码智能体能否在同一代码库上连续完成5至15个相互依赖的工程请求，每一步都从智能体此前写出的代码出发，早期的设计决策与错误会向后传递

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**现有基准的缺口**：论文指出，无论 SWE-bench 式单一问题修复，还是 Terminal-Bench、DeepSWE、FrontierSWE、ProgramBench 等更长的任务，都是一次性评分的单回合任务，不要求智能体在自己先前的工作上持续构建

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 构建方式

**题目来源**：每一步都以已有的权威依据为基础，例如规范、上游版本发布历史、协议修订、框架迁移路径和手工优化内核，同一依据同时定义指令与验证器；任务既有从零构建，也有基于真实开源代码库的工作

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**出题人背景**：作者均来自 Klavis AI；任务由至少具有五年经验的专业软件工程师审阅

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**审核流程**：每项任务经过两轮专家审阅：初审检查设计、每步是否构成真实进展以及时间预算是否合适；终审逐一对照指令与验证器，确认验证器无法在未完成工作时通过，问题修正后需再次审阅

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**质量控制**：每步在独立验证器容器中评分，隐藏测试与公开检查不同；开发中对验证器做对抗性加固，每个成功的攻击都会新增检查；构建失败、测试数量不足或评分超时均记零分

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**去污染**：论文承认任务源自公开项目，无法排除记忆；多数任务（56项）在作答时仅允许访问模型 API，版本升级任务还使用修改过期望输出的一致性测试，优化任务在评分时生成新输入

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 数据形式

**题量**：69项任务、574个步骤（每项5至15步，中位数8步）；优化18项、功能实现18项、版本升级20项、迁移13项

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**题型**：多步交互式软件工程任务，智能体在容器中修改代码库，每步由隐藏测试验证

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**模态**：代码与文本

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**语言**：9种编程语言：C/C++（38项）、Rust（11）、Java（6）、Go（4）、JavaScript（4）、Python（3）、PHP（2）、Ruby（1）；指令为英语

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**难度**：每步预算2至4小时，每项任务10至60小时（中位数16小时）；38项任务没有任何模型解出

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**公开与隐藏划分**：任务、环境与参考解公开在代码仓库；每步评分的大部分测试对智能体隐藏，并与公开检查不同

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 评测方法

**指标**：任务解出率（所有步骤都获满分才算解出）、Pass@4（四次尝试中至少一次解出的任务比例）与步骤通过率

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**评分方式**：每步在独立验证器容器中按隐藏测试评分；优化步骤以达到参考解加速比为满分门槛

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**提示设置**：每个模型在 Harbor 提供的智能体框架（Claude Code、Codex CLI、mini-swe-agent 或 Grok Build）中以该框架支持的最高推理强度运行，每项任务运行四次

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**官方评测脚本**：通过 Harbor 运行，例如 harbor run --path tasks --n-attempts 4；仓库说明应根据全部步骤奖励计算任务解出率，Harbor 的平均奖励并非任务解出率

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**可比性说明**：结果反映模型与所用智能体框架的组合；优化步骤的满分门槛是参考解的加速比，不一定是可达最优

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 最新情况

**核验日期**：2026-11-12

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**最新数据版本**：论文 v1 与代码仓库所述的69项任务版本

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**论文修订**：v1：2026-11-04 提交

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**饱和情况**：远未饱和：最强模型解出率为18.5%，69项任务中38项无任何模型解出

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**污染与争议**：论文局限部分指出：部分任务仍可能存在含糊要求或验证器误判；语言分布不均，C/C++ 占38项；因源自公开项目，无法排除记忆。对 simdutf 的抽查显示，智能体新增代码与对应上游文件逐行相同的比例中位数为0.2%

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**衍生基准**：待核实

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 榜单快照

**快照日期**：2026-11-12

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**官方榜**：https://multistepswe.com/#leaderboard

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**第三方榜**：待核实

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**结果快照**：论文表5（解出率，%）：Claude Opus 5.5 18.5（Pass@4 31.9，步骤通过率56.8）；Claude Fable 5.1 17.8；Gemini 4 Argon 10.1；GPT-6.1 Sol 10.1；GPT-6 Astra 6.9；DeepSeek V4.1 Flash 6.5；Qwen 3.8 Max 4.0；MiMo 2.6 Pro 2.9；Grok 4.7 1.4

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**覆盖说明**：结果为论文作者自测的九个模型；官方网站榜单为交互式页面

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 联系方式

**公开邮箱**：论文列出的作者邮箱：xiangkaiz@klavis.ai、zhengliu@klavis.ai、zihaolin@klavis.ai

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**代码讨论**：https://github.com/Klavis-AI/Multi-step-SWE/issues

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**官方社交账号**：维护方 Klavis AI 官网列出的账号：X 账号 @Klavis_AI（https://x.com/Klavis_AI）；LinkedIn 公司页 https://www.linkedin.com/company/klavis-ai/

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**隐私政策**：待核实

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 原始文件

**论文PDF**：https://arxiv.org/pdf/2611.07166

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**文件校验**：dc939d8c5de5f1404e1db6e3921e1f92859d41a348fe84d7fec3831891e9ab75

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**文件大小**：422088

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**文件夹**：待核实

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

**其他文件**：https://multistepswe.com/paper.pdf

来源: [1](https://arxiv.org/abs/2611.07166) [2](https://multistepswe.com/) [3](https://github.com/Klavis-AI/Multi-step-SWE) (访问 2026-11-12)

## 变更记录

2026-11-12：初次收录。

2026-11-14：补充维护方公开社交账号。
