# RoboDojo

42个仿真任务与18个真机任务组成的通用机器人操作基准，已被前沿模型发布页用于评测机器人控制。

## 基本信息

**简称**：RoboDojo

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**全称**：RoboDojo：面向通用机器人操作策略的统一仿真与真机基准

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**基准版本**：42个仿真任务与18个真机任务；榜单评测协议版本2026.11.03

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**论文版本**：arXiv:2607.04434v3（v1 2026-07-05，v3 2026-07-08）

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**发布日期**：2026-07-05

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**主板块**：机器人与具身

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**领域标签**：机器人操作；双臂操作；仿真与真机评测；视觉-语言-动作策略

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**许可证**：代码仓库为 MIT；Hugging Face 数据集标注为 Apache-2.0

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**论文或技术报告**：https://arxiv.org/abs/2607.04434

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**官方代码**：https://github.com/RoboDojo-Benchmark/RoboDojo

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**数据地址**：https://huggingface.co/datasets/RoboDojo-Benchmark/RoboDojo

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**官方主页**：https://robodojo-benchmark.com/

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**论文题名**：RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 发起与维护

**发起方**：香港大学 MMLab、加州大学伯克利分校、清华大学、北京大学等

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**协作机构**：斯坦福、MIT、北卡罗来纳大学、普林斯顿、卡内基梅隆等共18家学术机构；官方评测由全球学术合作机构支持，无商业参与

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**作者**：Tianxing Chen、Yue Chen（共同项目负责人）等；通讯作者 Mingyu Ding、Wenbo Ding、Masayoshi Tomizuka、Ping Luo

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**当前维护方**：RoboDojo 团队

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**资助方**：待核实

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 设计目标

**要测的能力**：在仿真中按泛化、记忆、精度、长程执行与开放指令五个维度诊断通用操作策略，并在三种真机平台上检验部署能力

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**现有基准的缺口**：论文指出现有基准多为简单、短程或技能单一的任务，且多只在仿真或只在真机中评测，难以兼顾效率与部署可信度

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 构建方式

**题目来源**：研究团队基于 Isaac Sim 在 ARX X5 双臂平台上设计42个仿真任务，并在 ARX X5、Piper、Piper X 三种平台上设计18个真机任务

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**出题人背景**：来自18家学术机构的机器人与具身智能研究者

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**审核流程**：真机试次由三名评分者在双盲协议下独立打分；官方榜发布需通过隐藏布局验证并公开模型与复现代码

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**质量控制**：仿真跨 GPU 复测成功率标准差不超过1.1个百分点；真机三轮重复评测总体成功率标准差不超过1.3个百分点；保留申诉机制

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**去污染**：官方评测在公开布局之外加测隐藏验证布局，以减少对公开布局的过拟合与刷榜

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 数据形式

**题量**：42个仿真任务（每任务50回合，共2,100回合）与18个真机任务（每任务10次试验）；仿真训练数据3,500条轨迹，真机训练数据1,800条轨迹

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**题型**：机器人操作任务（成功率与分步得分）

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**模态**：RGB 图像、机器人状态与语言指令

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**语言**：英语（语言指令）

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**难度**：论文冻结榜中最佳策略仿真平均成功率8.80%，人类遥操作专家为76.03%；开放维度接近零分

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**公开与隐藏划分**：公开布局用于主榜；官方评测另设隐藏验证布局

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 评测方法

**指标**：成功率与平均得分（含部分进度）

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**评分方式**：总体成绩取五个能力维度的平均，避免任务多的维度主导；真机得分为三名评分者的平均

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**提示设置**：不适用（策略评测）；智能体类模型单列于智能体榜且不参与主榜排名

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**官方评测脚本**：https://github.com/RoboDojo-Benchmark/RoboDojo

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**可比性说明**：官方榜将智能体类方法与 VLA 类策略分开展示；Claude Fable 5.2 发布页的 RoboDojo Sim 分数为 Anthropic 内部运行，与官方核验榜不直接可比

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 最新情况

**核验日期**：2026-11-10

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**最新数据版本**：评测协议2026.11.03

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**论文修订**：v1（2026-07-05）；v3（2026-07-08）

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**饱和情况**：未饱和：官方榜主榜最高平均得分42.59，智能体榜最高74.20，均低于论文报告的人类专家水平

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**污染与争议**：未见公开争议

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**衍生基准**：待核实

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 榜单快照

**快照日期**：2026-11-10

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**官方榜**：https://robodojo-benchmark.com/leaderboard

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**第三方榜**：https://www.anthropic.com/claude-fable-and-mythos-5-2

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**结果快照**：官方仿真主榜（2026-11-03更新）：WALL-OSS-1.0-lite 平均得分42.59、成功率34.97%，VPP2 39.26/32.26%，Awomo-0.5 35.34/29.64%；智能体榜 Q0-Preview 74.20/68.87%，GPT-6-Astra 28.97/22.48%

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**覆盖说明**：官方仿真榜共42个条目；Anthropic 报告 Claude Fable 5.2 在 RoboDojo Sim 内部运行中平均成功率64.9%

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 联系方式

**公开邮箱**：待核实

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**代码讨论**：https://github.com/RoboDojo-Benchmark/RoboDojo/issues

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**官方社交账号**：待核实

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**隐私政策**：待核实

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 原始文件

**论文PDF**：https://arxiv.org/pdf/2607.04434v3

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**文件校验**：e07c215f30169dde6a792c34b046b1f54818d09331763988732dcf9ead89a9d4

来源: [1](https://arxiv.org/pdf/2607.04434v3) (访问 2026-11-10)

**文件大小**：27334326

来源: [1](https://arxiv.org/pdf/2607.04434v3) (访问 2026-11-10)

**文件夹**：待核实

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

**其他文件**：https://xpolicylab.github.io

来源: [1](https://arxiv.org/abs/2607.04434) [2](https://robodojo-benchmark.com/) [3](https://robodojo-benchmark.com/leaderboard) (访问 2026-11-10)

## 变更记录

2026-11-10：初次收录。
