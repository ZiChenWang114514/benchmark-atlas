# Robo-bench

> 核验日期：2026-11-08（Asia/Seoul / KST）。访问日期不等于发布或运行日期；无法证实的字段保留待核实。

Robo-bench把机器人控制放进实时MuJoCo闭环：模型不只生成计划，还要自己编写感知、规划和低层控制，并承担思考时物理系统继续运行的后果。24项任务横跨机械臂与人形；分数衡量顺序里程碑，不是完整任务通过比例。

导读来源：[官方材料](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）；具体事实及历史访问日期见各字段。

## 基本信息

### 简称

Robo-bench

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 全称

Robo-bench

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 基准版本

2026-10-13官方榜快照

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 论文版本

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 发布日期

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 主板块

机器人与具身

说明：编辑归档，不代表官方分类。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 领域标签

- 闭环机器人控制
- 运动规划
- 具身感知
- 实时仿真

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 许可与适用范围

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 论文

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 代码仓库

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 数据地址

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 官方主页

https://www.vals.ai/benchmarks/robo_bench

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 论文标题

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 发起与维护

### 机构与发起关系

Vals AI

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 合作机构/署名单位

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 作者

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 当前维护入口

Vals AI

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 资助方

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 设计目标

### 衡量能力

仅以机器人规格、传感器和摄像头，在实时物理环境中自主编写感知、规划及低层控制。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 设计背景

不预装运动规划器或平衡控制器，直接衡量通用agent控制机器人的能力，模型思考延迟计入真实时间。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 构建方式

### 题目或数据来源

MuJoCo中的7自由度Franka Panda机械臂及29自由度Unitree G1人形机器人；24任务涵盖装配、灵巧操作、动力学、移动操作等。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 出题背景

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 审核流程

每个任务参考解须在五个seed全部成功，静止agent不应成功；仿真器位于agent不可读端并签名计分。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 质量控制

每个任务参考解须在五个seed全部成功，静止agent不应成功；仿真器位于agent不可读端并签名计分。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 去污染措施

21个任务保持私有，避免进入训练数据或用于agent/harness针对性调参；3个任务公开。该措施不是对已有模型训练数据的独立审计。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 数据形式

### 规模

24任务：13机械臂、11人形；每模型每任务一次、单seed。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 题型

动作/传感闭环任务；公开天平、积木说明书和忍者路线三例。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 模态

- 摄像头图像
- 深度图
- 状态传感器
- 电机命令
- 代码

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 语言

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 难度

任务覆盖装配、灵巧操作、动力学、推理、堆叠、工具使用及人形多阶段障碍；参考解在五个seed均成功，静止agent不成功。未用统一人工难度等级。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 数据划分

公开3任务，另外21任务保持私有（官网明确）。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 评测方法

### 指标

各任务按顺序里程碑计0–100分，24任务平均；另列机械臂/人形分项和首次动作时间。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 评分方式

里程碑必须顺序达成；任务总分100，仿真端验证；不能将28.33分解释为28.33%任务完整成功。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 提示与运行设置

每episode三分钟真实墙钟、无准备时间；每模型用厂商coding agent最高推理设置，无现成控制器。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 评测脚本

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 可比性提醒

每任务只跑一次；官方说明重复运行总分可变约10分，小差距无显著性保证。不同厂商harness也影响分数。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 最新情况

### 核验日期

2026-11-08 KST / Asia/Seoul

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 数据版本与更新

- **version**：2026-10-13官方榜快照
- **trending**：B
- **heat_evidence**：Vals于2026-10-13更新7模型，主要单一机构专有测试展示（B），不是已证实广泛采用。
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/robo_bench", "date": "2026-11-07", "date_type": "observed_on", "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"}]

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 论文修订记录

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 饱和程度

本次官方七模型中最高平均里程碑分28.33/100；所有模型的人形分项均低于2/100。该快照仍有显著未解决空间，不将平均里程碑分当完整任务成功率。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 争议与已知问题

每任务只跑一次；官方说明重复运行总分可变约10分，小差距无显著性保证。不同厂商harness也影响分数。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 衍生基准

仿真机器人评测，不等于实机部署安全认证；机器人平台分项不另建benchmark。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 榜单快照

### 快照访问日期

2026-11-08 KST / Asia/Seoul（访问日，不是实验运行日）

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 官方榜单入口

https://www.vals.ai/benchmarks/robo_bench

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 第三方入口

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 可核验结果

- {"rank": 1, "model": "GPT-6.1 Sol", "score": 28.33, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$4.97", "time_to_first_move": "79.89s", "source_update_date": "2026-10-13"}
- {"rank": 2, "model": "GPT-6 Astra", "score": 23.33, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$28.48", "time_to_first_move": "74.88s", "source_update_date": "2026-10-13"}
- {"rank": 3, "model": "Claude Opus 5.5", "score": 14.58, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$11.38", "time_to_first_move": "2m07s", "source_update_date": "2026-10-13"}
- {"rank": 4, "model": "Wonder Full", "score": 10.42, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$19.68", "time_to_first_move": "2m14s", "source_update_date": "2026-10-13"}
- {"rank": 5, "model": "Claude Fable 5.1", "score": 5.83, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$20.40", "time_to_first_move": "2m04s", "source_update_date": "2026-10-13"}
- {"rank": 6, "model": "Gemini 4 Argon", "score": 0.83, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$17.33", "time_to_first_move": "2m32s", "source_update_date": "2026-10-13"}
- {"rank": 7, "model": "Grok 4.7", "score": 0.21, "metric": "24任务平均里程碑分（0–100，非完整成功率）", "track": "Vals官方；各厂商最高推理coding agent；单seed/任务；3分钟", "source_url": "https://www.vals.ai/benchmarks/robo_bench", "accessed": "2026-11-08", "collected_at": "2026-11-08 KST", "result_type": "来源表格精确转录；非本库重跑", "estimated_api_cost": "$11.25", "time_to_first_move": "2m31s", "source_update_date": "2026-10-13"}

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 榜单覆盖边界

完整转录官方7模型榜表，不用首页一位小数近似值；页面更新日2026-10-13。单seed重复总分可波动约10分，不能以小差距声称显著排名。纸质论文、代码仓库及HF数据卡入口仍待核实。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 联系方式

### 公开研究联系

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 公开反馈渠道

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 官方社交账号

https://x.com/ValsAI

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 联系方式原则

仅记录项目官方网页公开的研究与反馈入口；不收集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08，KST）

## 原始文件

### Drive论文原件

待核实

说明：本组仅本地建页，未上传Drive，不伪造归档链接。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 原始PDF地址

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 原始文件SHA-256

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 原始文件字节数

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### Drive文件夹

待核实

说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

### 其他文档

- {"type": "已打开官方网页/论文", "url": "https://www.vals.ai/benchmarks/robo_bench"}

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立近期热门中文研究条目。仿真机器人评测，不等于实机部署安全认证；机器人平台分项不另建benchmark。 热度与榜单口径分离，不确定值标记待核实。"}
- {"date": "2026-11-08", "timezone": "Asia/Seoul", "change": "第2轮深度核验：补齐7行官方精确分数；补21项私有题的去污染目的与难度验证，不把28.33解释为任务成功率。"}

来源：[1](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）；[2](https://www.vals.ai/benchmarks/robo_bench)（访问 2026-11-08，KST）
