# HealthBench Professional

> Benchmark Constitution · 核查日期：2026-11-07。未知仍保留待核实；访问日不冒充实验日。

HealthBench Professional聚焦医生工作中的咨询、文书和研究对话，525个公开任务含困难及红队富集，并非自然临床频率样本。论文内部产品评测、参考外部实现及AA裸模型评测需分开；长度校正会奖励短于2,000字符的答案，不只是惩罚长答案。

导读来源：[https://arxiv.org/abs/2604.27470](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 1. 基本信息

### 简称

HealthBench Professional

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 全称

HealthBench Professional

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 数据/协议版本

2026-04论文v1配套公开525例数据包（README未另给数据语义版本）

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）；[2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）

### 论文版本

v1；2026-04-30（；论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 发布日期及口径

2026-04-30（；arXiv初稿提交时间，非推定数据首发日）

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 主板块

生物与医学

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 子领域

- 临床咨询
- 医疗文书
- 医学研究
- 模型裁判与rubric评估

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）

### 许可证

MIT（assets.zip根目录LICENSE，Copyright (c) 2026 OpenAI；README frontmatter同标license: mit）。

来源：[1](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2604.27470

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 代码入口

https://github.com/openai/simple-evals

说明：仅为参考/非官方外部实现；原论文结果用内部实现，不宣称公开代码完全复现原报告。

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）；[2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）

### 数据入口

https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 官方主页

https://arxiv.org/abs/2604.27470

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 论文标题

HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 2. 发起与维护

### 发起团队

OpenAI

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 合作及署名机构

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 作者

Rebecca Soskin Hicks、Mikhail Trofimov、Dominick Lim、Rahul K. Arora 等（完整作者见论文）

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 维护方

OpenAI

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 资助

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 3. 设计目标

### 评测能力

衡量医生与模型真实工作对话中的临床咨询、写作与文档、医学研究能力及安全性。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 设计动机

医学选择题或合成病历不能覆盖常见临床聊天工作；Professional补充而非替代面向患者和医生的HealthBench。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 4. 构建方式

### 材料来源

医生测试ChatGPT for Clinicians所得对话；候选15,079例中按质量、代表性及难度选择525例。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 编制背景

190名医生参与，实践经验跨50国、26个医学专科。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 审核流程

至少3名医生分三阶段撰写、审查、最终裁决；困难任务由独立医生确认错误与现实性。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 质量控制

困难样本相对候选池富集约3.5倍，约三分之一为红队；为全部任务收集不限时、可联网的专科匹配医生基线。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 去污染边界

论文请求不要在线逐题发布数据；使用canary，并保留小型私有held-out集监测训练污染。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 5. 数据形式

### 规模

实际逐行读取公开assets.zip：525例，consult 236、writing 142、research 147；good_faith 334、red_teaming 191；typical 256、difficult 269。这些是公开包计数，不是自然临床发生率。

来源：[1](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）；[2](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）

### 题型

单轮或多轮对话，生成最后用户消息的下一条自由文本答复。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 模态

- 文本对话

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 语言

论文称逐例标注primary language，但公开JSONL实际键中没有该字段；不得声称公开包带语言标签。医生群体熟练使用52种语言，不代表525题含52种语言；准确题目语言分布待核实。

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）；[2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）

### 难度

typical为医生Likert 3–7，difficult为1–2；困难选择针对当时OpenAI模型，非自然临床分布。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 公开及隐藏划分

公开525任务的对话、rubric、use_case、type、difficulty、specialty与医生参考答复；另保留小型私有集，数量待核实。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 6. 评测方法

### 指标

长度调整后的rubric得分；不是临床正确率。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 计分

每题得分为满足rubric权重总和/全部正权重总和；长度校正s_len=s−2.94×10^-5×(字符数−2000)，即每多500字符减1.47个百分点、每少500字符加同量。按题/样本均值后将总体裁剪至[0,1]，不是逐题裁剪。

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）

### 提示与运行设置

论文主要比较每题8样本、最高可用推理档；AA为4次重复，用GPT-5.4 low裁判。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 评测入口

官方论文使用内部实现且明确不发布官方外部实现；HealthBench的simple-evals作为参考，不能称完全同一实现。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 可比性边界

产品harness、裸模型、是否联网与长度调整/裁剪须分开；困难抽样不能解读为现实临床错误率。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 7. 最新情况

### 核查日

2026-11-07（指定采集日期）

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 已核实版本

version：2026-04论文v1配套525例数据包；未另给语义版本；heat_confidence：A；evidence_2026_h2：- url：https://artificialanalysis.ai/evaluations/healthbench-professional；date：2026-11-07；note：Artificial Analysis当前独立评测525任务；日期为观察日。；- url：https://openai.com/index/gpt-6-astra/；date：2026-11-07；note：厂商发布表继续单列Professional；观察日，不冒称首发日。

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）；[2](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2026-04-30；timezone：

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 饱和情况

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 已知问题

Epoch于2026-09-10评审判为Flawed；该目录未说明具体错误，不臆测。另需注意模型裁判、难度富集和长度校正的外推限制。

来源：[1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 衍生关系

Professional是对HealthBench的互补临床工作评测，不是Hard/Consensus切片，也不宣称取代HealthBench。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不代替榜单更新或实验日期）

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 官方结果入口

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 第三方结果入口

https://artificialanalysis.ai/evaluations/healthbench-professional

来源：[1](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Artificial Analysis独立评测 | 1 | GPT-6 Astra (Max) | 66.0 | 长度调整rubric得分 % | [原始来源](https://artificialanalysis.ai/evaluations/healthbench-professional)；采集2026-11-07；待核实（页面未显示测量/更新日） |
| Artificial Analysis独立评测 | 2 | GPT-6.1 Sol (Max) | 65.1 | 长度调整rubric得分 % | [原始来源](https://artificialanalysis.ai/evaluations/healthbench-professional)；采集2026-11-07；待核实（页面未显示测量/更新日） |
| Artificial Analysis独立评测 | 3 | Claude Sonnet 5.5 (Max, Default Fallback) | 63.0 | 长度调整rubric得分 % | [原始来源](https://artificialanalysis.ai/evaluations/healthbench-professional)；采集2026-11-07；待核实（页面未显示测量/更新日） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

仅保留所列来源与协议下的结果；榜单自写更新时间：待核实。访问日期不是评测运行日期。

来源：[1](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）


## 9. 联系方式

### 公开研究联系邮箱

- rebecca.soskinhicks@openai.com
- mtrofimov@openai.com
- karan@openai.com

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 问题反馈

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 官方账号

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 隐私政策

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2604.27470

说明：官方论文正文对应的PDF入口；未下载，故hash与字节数待核实。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### PDF SHA-256

ac61ef9d93b93e827e6543e7449d51381539a4bd37dbfa90e7e48b5fd235a628

说明：下载原始PDF字节的SHA-256；与既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）

### PDF字节数

1171376

来源：[1](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）

### 文件夹

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 其他原始材料

- type：官方公开数据包README及MIT LICENSE；url：https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip
- type：论文与协议；url：https://arxiv.org/abs/2604.27470
- type：非官方外部参考实现；url：https://github.com/openai/simple-evals

来源：[1](https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip)（访问 2026-11-07）；[2](https://arxiv.org/pdf/2604.27470)（访问 2026-11-07）

### PDF

待核实

说明：已检查所引官方材料，未完成精确核验；不代表官方未公开。

来源：[1](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 11. 变更记录

### 本页修订

- date：2026-11-07；timezone：；change：首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）

