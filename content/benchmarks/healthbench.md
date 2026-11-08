# HealthBench

> Benchmark Constitution，核查日期：2026-11-07。未知仍保留待核实；访问日不冒充实验日。

原版HealthBench用医生撰写的rubric评价5,000段医疗对话的最后一条回复；Hard与Consensus是其切片。它不等于525例HealthBench Professional，后者的长度调整榜不能当作原版更新成绩，也不能将rubric得分当作临床正确率。

导读来源：[https://arxiv.org/abs/2505.08775](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 1. 基本信息

### 简称

HealthBench

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 全称

HealthBench

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 数据/协议版本

原始HealthBench（非Professional）

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 论文版本

v1；2025-05-14（论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 发布日期及口径

2025-05-14（arXiv初稿提交时间，非推定数据首发日）

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 主板块

生物与医学

说明：编辑归档；跨领域只计主板块。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 子领域

- 生物与医学

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 许可证

MIT；官方simple-evals README的HealthBench条目明确链接本仓库MIT LICENSE，已读许可证全文。

来源：[1](https://raw.githubusercontent.com/openai/simple-evals/HEAD/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/openai/simple-evals/HEAD/LICENSE)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2505.08775

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 代码入口

https://github.com/openai/simple-evals

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 数据入口

https://github.com/openai/simple-evals

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方主页

https://arxiv.org/abs/2505.08775

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 论文标题

HealthBench: Evaluating Large Language Models Towards Improved Human Health

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 2. 发起与维护

### 发起团队

OpenAI

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 合作及署名机构

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 作者

Rahul K. Arora、Jason Wei、Rebecca Soskin Hicks、Preston Bowman等；完整名单见论文。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 维护方

OpenAI

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 资助

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 3. 设计目标

### 评测能力

面向普通用户与医护人员的开放式医疗对话质量、安全、上下文意识与沟通能力。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 设计动机

医学选择题和短答案难反映真实医疗交互，也常缺乏与医生判断的一致性验证。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 4. 构建方式

### 材料来源

以合成情境为主，辅以医生红队与HealthSearchQA改写；262名医生参与，执业经历覆盖60国与26专科。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 编制背景

262名医生，覆盖26专科与60国执业经历；论文列49种医生可贡献语言，不将此自动当成数据集精确语言分布。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 审核流程

医生经付费入门任务筛选；持续自动与人工审查，低质量贡献者注释移除。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 质量控制

共识标准需至少两位且多数医生认可；并通过meta-evaluation比较模型和医生评分一致性。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 去污染边界

发布canary及避免传播题例的请求，并保留少量同分布私有hold-out；其规模待核实。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 5. 数据形式

### 规模

5,000对话；48,562个唯一rubric标准；Hard为1,000题；Consensus为3,671题且只保留共识标准。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 题型

根据完整单轮或多轮历史回复最后一条用户消息。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 模态

- 文本

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 语言

多语言医疗对话；精确各语言题量待核实。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 难度

Hard为1,000个困难样本：先对o3、Grok 3、Gemini 2.5 Pro、Claude 3.7 Sonnet与Llama 4 Maverick逐题计分，剔除所有模型均未取得正分的题，再按五模型平均分选最低1,000题；不是自然医疗分布的随机抽样。

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）

### 公开及隐藏划分

公开主集与少量同分布私有hold-out；hold-out精确题量待核实。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 6. 评测方法

### 指标

整体rubric归一化分、分theme/axis分数、worst-at-k；Hard与Consensus独立报告。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 计分

每条rubric权重为-10至10且不为0；满足计该条全部分，否则0；每题除以正权重总和，再对所有题平均，最后将总体分数裁剪至[0,1]。单题可为负，不应逐题先裁剪。默认GPT-4.1裁判。

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）

### 提示与运行设置

生成最终用户消息的回复；原论文OpenAI模型temperature=1，其他厂商设置见附录H。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 评测入口

OpenAI simple-evals中的HealthBench评测、meta-evaluation、Hard/Consensus与绘图工具。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 可比性边界

原始分数与AA长度调整分数不同；Hard、Consensus和525题Professional不是同一个指标；不能把Professional榜搬到本条。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 7. 最新情况

### 核查日

2026-11-07（指定采集日期）

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 已核实版本

version：原始HealthBench（非Professional）；evidence_2026_h2：- url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；date_type：observed_on；note：AA当前附加评测表明确分别列原始5,000题HealthBench和525题Professional；不把Professional网页排行榜归本条。候选另列10月系统卡，未核实，不能算第二份已核实热度证据。

说明：热度等级沿候选采用；只保留已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2025-05-14；timezone：

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 饱和情况

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 已知问题

作者用canary和私有同分布集检查训练污染风险；公开集不可据此宣称无污染。论文讨论医生对rubric解释和容错偏好存在分歧；模型裁判得分不是临床真实获益或患者安全的直接证明。

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）

### 衍生关系

HealthBench Hard与Consensus为原版衍生切片；HealthBench Professional是另一个525例临床工作对话基准，本库单独建档，不把其榜归入本条。

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）；[2](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）


## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不代替榜单更新或实验日期）

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方结果入口

https://arxiv.org/abs/2505.08775

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 第三方结果入口

https://artificialanalysis.ai/methodology/intelligence-benchmarking

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| 原论文表7：原版5,000题，16次运行均值，无长度调整 | — | o3 | 0.599 ± 0.0016 | HealthBench归一化rubric得分（0–1） | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 （论文提交） |
| 原论文表7：原版5,000题，16次运行均值，无长度调整 | — | GPT-4.1 | 0.4778 ± 0.0022 | HealthBench归一化rubric得分（0–1） | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 （论文提交） |
| 原论文表7：原版5,000题，16次运行均值，无长度调整 | — | o1 | 0.42 ± 0.0022 | HealthBench归一化rubric得分（0–1） | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 （论文提交） |
| 原论文表7：原版5,000题，16次运行均值，无长度调整 | — | GPT-4o (Aug 2024) | 0.3233 ± 0.002 | HealthBench归一化rubric得分（0–1） | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 （论文提交） |
| 原论文表7：原版5,000题，16次运行均值，无长度调整 | — | GPT-3.5 Turbo | 0.1554 ± 0.0029 | HealthBench归一化rubric得分（0–1） | [原始来源](https://arxiv.org/pdf/2505.08775)；采集2026-11-07；2025-05-14 （论文提交） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

从原论文表7恢复16次运行的精确均值/标准差，不以摘要四舍五入60%代替0.5990，不将此历史切片称当前SOTA。Professional 525题AA现榜在独立条目，不能迁入本条。

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）


## 9. 联系方式

### 公开研究联系邮箱

- karan@openai.com

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 问题反馈

https://github.com/openai/simple-evals/issues

来源：[1](https://raw.githubusercontent.com/openai/simple-evals/HEAD/README.md)（访问 2026-11-07）

### 官方账号

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 隐私政策

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2505.08775

说明：官方arXiv原论文PDF入口；本组不下载、不上传。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### PDF SHA-256

f61c53f6bde84a3964531efe04a75389f9bba9e70a35b4012c871c9ec0b512f3

说明：下载原始PDF字节的SHA-256；与既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）

### PDF字节数

8359760

来源：[1](https://arxiv.org/pdf/2505.08775)（访问 2026-11-07）

### 文件夹

待核实

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 其他原始材料

- type：官方方法或项目页；url：https://arxiv.org/abs/2505.08775；accessed：2026-11-07

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### PDF

待核实

说明：本组只建立暂存条目，未上传。

来源：[1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）


## 11. 变更记录

### 本页修订

- date：2026-11-07；timezone： ()；change：首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传。
- date：2026-11-07；timezone：；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）

