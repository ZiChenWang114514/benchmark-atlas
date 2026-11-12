# AutomationBench-AA

> 核查：2026-11-07。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

AutomationBench-AA

来源：[1]

### 全称

AutomationBench-AA（Artificial Analysis 对 Zapier AutomationBench 的实现）

来源：[1]

### 数据/软件版本

AA使用AutomationBench数据集1.0.6的私有657任务划分；AA评分协议独立。

来源：[2]

### 论文版本

arXiv v1

来源：[3]

说明：论文修订版本不等同数据集版本。

### 发布日期

2026-04-21 08:14:59（Zapier母论文arXiv v1提交，不冒称AA实现首发时刻）

来源：[3]

### 主板块

Agent

来源：[3]

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

### 学科标签

长程自动化任务

来源：[3]

### 许可证与范围

母仓库Zapier原创部分为MIT；LICENSE对第三方API结构表示不主张原创版权，且不授予第三方IP权；AA私有657题的独立数据许可待核实。

来源：[4][5]

状态：待核实（本字段尚有未能确认的部分）。

### 论文入口

https://arxiv.org/abs/2604.18934

来源：[3]

说明：2604.18934是Zapier母协议论文，不把AA的657题部分得分口径归给母论文。

### 论文标题

AutomationBench

来源：[3]

### 官方代码

https://github.com/zapier/AutomationBench

来源：[1]

### 数据入口

未公开（AA使用的657任务held-out测试集）；母项目公开任务另见https://github.com/zapier/AutomationBench。

来源：[2][1]

### 官方主页

https://artificialanalysis.ai/evaluations/automationbench-aa

来源：[1]

## 2. 发起与维护

### 发起团队

母基准：Zapier；AA实现与独立评测：Artificial Analysis。

来源：[1][3]

### 署名/合作机构

母论文致谢Prime Intellect等早期反馈；不意味着这些机构共同维护AA私有集。

来源：[1][3]

### 作者

Daniel Shepard；Robin Salimans

来源：[1][3]

### 维护入口

AutomationBench母项目由Zapier维护；AA运行与榜单由Artificial Analysis维护。

来源：[1][3]

### 资助与计算资源

待核实

来源：[3]

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

状态：待核实（本字段尚有未能确认的部分）。

## 3. 设计目标

AA实现和Zapier母基准共享任务形态却不共享主分数：AA对无guardrail违规任务给予目标完成比例，Zapier严格要求全断言成功。77.8%不能与母论文9.9%直接作同协议时间进步曲线。
来源：[1][3][1][3]

### 测量能力

跨SaaS应用自主发现API、处理数据、遵守分层业务规则并完成多步工作流。

来源：[1][3]

### 为何需要这个基准

很多工具基准只测单应用/函数选择，缺少跨应用协调、端点发现和业务政策组合。

来源：[1][3]

## 4. 构建方式

### 材料来源

根据Zapier客户工作流形状合成，未使用PII/客户机密；涵盖6领域、约500端点与47模拟应用。

来源：[3]

### 命题/编制背景

Zapier研究/工程团队；Opus4.6、GPT5.3Codex、Gemini3参与生成，再做审查。

来源：[3]

### 审核流程

多轮现实性/难度迭代、抽样人工审计；通过不含实际参数的提示模式验证可解性。

来源：[3]

### 质量控制

每题要求可观察状态修改、确定性检查与负断言防止撒网行为；RL试验识别奖励漏洞。

来源：[3]

### 去污染与证据边界

母协议公开600题，至少同规模私有题；AA保留657评测题，公开示例不是官方完整评分集。

来源：[3]

## 5. 数据形式

### 规模与分母

AA实现：657任务，6领域（Finance/HR/Marketing/Operations/Sales/Support）；母论文公开600及600+私有不是同一精确分母。

来源：[1]

### 题型

一次任务指令后自主多步API检索/调用，最后核对多个应用状态。

来源：[1]

### 模态与字段

文本；结构化API与数据库；模拟SaaS应用

来源：[1]

### 语言

英语业务指令与API schema。

来源：[1]

### 难度定位

分层政策、噪声和相似记录造成困难；不等于真实生产SaaS连通性或凭证权限测试。

来源：[1]

### 公开、隐藏与划分

AA评分题保留私有，部分样例公开；母项目公开题可研究，不能作为AA分数完全复现集。

来源：[1]

## 6. 评测方法

### 指标

headline为每题objective完成比例，经guardrail门控后平均；另有严格整题成功率。

来源：[1]

### 评分流程

每个任务先检查终态程序断言：任一guardrail违规或任务出错记0；否则取该任务objectives完成比例，再对任务等权平均。没有独立LLM裁判；网页无guardrail门控的Objectives Completed仅为诊断指标，不是headline。

来源：[5][1]

### 运行与提示

私有657题来自AutomationBench 1.0.6；Finance/HR/Marketing/Operations/Sales/Support六域；每题运行一次，最多50轮，以结构化工具发现并调用REST API。各域互斥；一题可涉及多个app，因此应用分项不互斥。

来源：[5]

### 评测实现

https://github.com/zapier/AutomationBench

来源：[1]

### 不能混比的设置

AA对无guardrail违规任务按目标完成比例给分，违规或执行错误记0；Zapier主榜按所有断言全通过的任务比例评分。公开600任务、AA私有657任务、另200条simple任务不能混用。

来源：[2][6]

## 7. 最新情况

### 核查日期

2026-11-07（采集日，不是实验日）

来源：[3]

### 当前发布

version：AutomationBench 1.0.6；AA私有657任务；evidence_2026_h2：- url：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1；date：2026-10-28；note：Artificial Analysis 2026-10-28文章明确列出 AutomationBench-AA 为 Intelligence Index v5 的评测组成并报告模型领先表现。

来源：[2][7]

### 版本脉络

mother_paper：arXiv:2604.18934v1；submitted_at：2026-04-21；boundary：Zapier论文首发不是AA私有集上线日。

来源：[3]

### 分数上限与饱和度

AA网页当前前三77.8/77.6/77.5%，尚有明显未完成目标或guardrail错误，不能宣布完全饱和。母论文最高9.9%是2026-04历史严格整题成功率；公开600题README当前最高50.3%，两者不与AA部分得分混比。

来源：[1][6][8]

### 争议与局限

合成任务与模拟API可能偏离真实业务；仅终态评分不完整检查行为过程，guardrail口径影响解读。

来源：[3][1]

### 衍生版本

AutomationBench-AA为AA实现；母协议600公开题与657私有评测不拆计两条，应用/领域子项不另计。

来源：[3][1]

## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不是实验日）

来源：[3]

### 官方入口

https://artificialanalysis.ai/evaluations/automationbench-aa

来源：[1]

### 第三方/补充实验

https://artificialanalysis.ai/evaluations/automationbench-aa

来源：[1]

### 分轨成绩

#### AA官方现榜：657私有任务 / guardrail-gated objective credit

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Gemini 4 Carbon (High) | 77.8 | AutomationBench-AA Score (%) |
| 2 | Gemini 4 Carbon (Medium) | 77.6 | AutomationBench-AA Score (%) |
| 3 | Gemini 4 Argon (High) | 77.5 | AutomationBench-AA Score (%) |

- Gemini 4 Carbon (High)：source_url：https://artificialanalysis.ai/evaluations/automationbench-aa；accessed：2026-11-07；benchmark_version：AutomationBench 1.0.6 / AA private 657；source_type：AA实施方独立评测网页快照；source_date：待核实（网页未注明逐模型运行/榜表更新日期）
- Gemini 4 Carbon (Medium)：source_url：https://artificialanalysis.ai/evaluations/automationbench-aa；accessed：2026-11-07；benchmark_version：AutomationBench 1.0.6 / AA private 657；source_type：AA实施方独立评测网页快照；source_date：待核实（网页未注明逐模型运行/榜表更新日期）
- Gemini 4 Argon (High)：source_url：https://artificialanalysis.ai/evaluations/automationbench-aa；accessed：2026-11-07；benchmark_version：AutomationBench 1.0.6 / AA private 657；source_type：AA实施方独立评测网页快照；source_date：待核实（网页未注明逐模型运行/榜表更新日期）

#### Zapier官方README：600公开任务 / strict all-assertions pass

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Claude Opus 5 (max) | 50.3 | strict task pass rate (%) |
| 2 | Kimi K3 (max) | 46.67 | strict task pass rate (%) |
| 3 | Claude Fable 5 (max) | 46.17 | strict task pass rate (%) |
| 4 | GPT-5.6 Sol (max) | 45.83 | strict task pass rate (%) |
| 5 | Gemini 3.6 Flash (high) | 45.0 | strict task pass rate (%) |

- Claude Opus 5 (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：母项目公开集README保存成绩；非657题AA榜/非Zapier私有主榜；n_tasks：600；protocol：六域各100任务；各模型最高可用reasoning effort；Fable5为2026-07更严格classifier后成绩
- Kimi K3 (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：母项目公开集README保存成绩；非657题AA榜/非Zapier私有主榜；n_tasks：600；protocol：六域各100任务；各模型最高可用reasoning effort；Fable5为2026-07更严格classifier后成绩
- Claude Fable 5 (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：母项目公开集README保存成绩；非657题AA榜/非Zapier私有主榜；n_tasks：600；protocol：六域各100任务；各模型最高可用reasoning effort；Fable5为2026-07更严格classifier后成绩
- GPT-5.6 Sol (max)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：母项目公开集README保存成绩；非657题AA榜/非Zapier私有主榜；n_tasks：600；protocol：六域各100任务；各模型最高可用reasoning effort；Fable5为2026-07更严格classifier后成绩
- Gemini 3.6 Flash (high)：source_url：https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md；accessed：2026-11-07；source_type：母项目公开集README保存成绩；非657题AA榜/非Zapier私有主榜；n_tasks：600；protocol：六域各100任务；各模型最高可用reasoning effort；Fable5为2026-07更严格classifier后成绩

来源：[1][6]

### 覆盖边界

AA既是本实现维护方，也是相对Zapier母项目的独立评测方；同一AA URL不算两份独立证据。另列Zapier README公开600题严格通过率，不当作AA657题或Zapier更难私有集的成绩。AA网页前三Objectives Completed另为94/94/93，不得替换77.8/77.6/77.5 headline。

来源：[1][6][5]

## 9. 联系方式

### 公开作者工作邮箱

daniel.shepard@zapier.com；robin.salimans@zapier.com

来源：[3]

### 公开反馈

https://github.com/zapier/AutomationBench/issues

来源：[1]

说明：公开仓库反馈入口；未发送问题。

### 官方账号

待核实

来源：[3]

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

状态：待核实（本字段尚有未能确认的部分）。

### 隐私信息

待核实

来源：[3]

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

状态：待核实（本字段尚有未能确认的部分）。

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2604.18934

来源：[8]

说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 下载源文件SHA-256

348360cd2ccefc52d1a8ea65e0a334cb3363fab85e66f71e09f6f5935233cbc5

来源：[8]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

684375

来源：[8]

### 既有文件夹

来源：[9]

### 其他材料

来源：[1][10]

说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### 既有 PDF链接

来源：[11]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- 2026-11-07：深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。
- 2026-11-07：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[1]

### 来源索引

[1]: https://artificialanalysis.ai/evaluations/automationbench-aa "访问 2026-11-07"
[2]: https://artificialanalysis.ai/methodology/intelligence-benchmarking "访问 2026-11-07"
[3]: https://arxiv.org/abs/2604.18934 "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/zapier/AutomationBench/main/LICENSE "访问 2026-11-07"
[5]: https://artificialanalysis.ai/methodology/intelligence-benchmarking#automation-bench-aa "访问 2026-11-07"
[6]: https://raw.githubusercontent.com/zapier/AutomationBench/main/README.md "访问 2026-11-07"
[7]: https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 "访问 2026-11-07"
[8]: https://arxiv.org/pdf/2604.18934 "访问 2026-11-07"
[9]: "访问 2026-11-07"
[10]: "访问 2026-11-07"
[11]: "访问 2026-11-07"
