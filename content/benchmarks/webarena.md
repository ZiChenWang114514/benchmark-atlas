# WebArena

> 深度复核：2026-11-08。采集日不等于榜单更新日；未取得的新证据不覆盖旧来源日期。

WebArena在可重置的自托管网站上验证任务最终状态，允许不同但有效的操作路径。官方Sheet是不同参评者成果的汇总，不是共享模型、输入和harness的一次统一实验；原始812任务与Reddit子集、Infinity成功轨迹不能混用。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 基本信息

### 简称

WebArena

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 全称

WebArena

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 基准版本

canonical WebArena v0.2.0（2023-10-24注释修复后的812任务协议）；AgentLab/BrowserGym属于推荐运行框架。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）。

### 论文版本

arXiv v4

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 发布日期

- **paper_first_submission**：2023-07-26
- **date_type**：论文首次提交，不等同数据集首次上线

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 主板块

Agent

> Benchmark Constitution 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 领域标签

- 网页任务执行

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 许可证

Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

来源：[1](https://github.com/web-arena-x/webarena)（访问 2026-11-07）。

### 论文

https://arxiv.org/abs/2307.13854

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 官方代码

https://github.com/web-arena-x/webarena

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 数据地址

https://github.com/web-arena-x/webarena/blob/main/config_files/test.raw.json

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 官方入口

https://webarena.dev/og/

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 论文标题

WebArena: A Realistic Web Environment for Building Autonomous Agents

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 发起与维护

### 发起机构

Carnegie Mellon University；作者也列Inspired Cognition单位。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 署名合作机构

- Carnegie Mellon University
- Inspired Cognition

> 依论文项目页作者署名机构；与环境中模仿的网站品牌无合作推断。

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 作者

- Zhou, Shuyan
- Xu, Frank F.
- Zhu, Hao
- Zhou, Xuhui
- Lo, Robert
- Sridhar, Abishek
- Cheng, Xianyi
- Ou, Tianyue
- Bisk, Yonatan
- Fried, Daniel
- Alon, Uri
- Neubig, Graham

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 维护方

web-arena-x / WebArena团队维护canonical复现仓库；2024-12-05官方建议新实验使用AgentLab/BrowserGym以改善并行运行、边界处理与统一报告。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）。

### 资助

AFRL FA8750-19-2-0200；AWS AI gift；CAIS compute支持。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 设计目标

### 衡量能力

把高层自然语言意图转成跨网页多步行动，正确改变网页状态或获取信息。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 设计背景

静态网页快照与短步骤任务难评长程规划；单看动作相似度会拒绝不同但正确的路径。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 构建方式

### 题目与数据来源

自托管拟真网站：电商、论坛、协作开发、内容管理四类；作者编写241模板派生812任务，附地图/计算器/wiki等。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 构建者背景

CMU研究者设计意图；网站数据模拟现实分布，不是对真实用户账户操作。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 审核流程

两名标注者生成参考答案，第三人解决分歧。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 质量控制

2023-10-24重新检查全部数据集并修复发现的标注错误；官方将v0.2.0称为相对稳定版本。每个测试任务以程序核查目标信息或网站状态。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）；[2](https://webarena.dev/og/)（访问 2026-11-08）。

### 去污染与泄漏防范

本地环境支持可复现但数据/任务公开；模板相似性和后续训练污染仍需注意。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 数据形式

### 规模

812任务，来自241模板，覆盖4类主要网站。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 任务形式

信息查询、内容创建/修改和多网站联合操作。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 模态

- 网页文本/HTML/可访问性树
- 可选截图
- 工具动作

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 语言

英语指令；网站内容与代码相关语法。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 难度与类型

长程、部分需多网站/外部知识；同模板实例并非完全独立能力点。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 公开与隐藏划分

自托管网站、任务和功能评测代码公开；不等于线上真实网站或隐藏服务。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 评测方法

### 指标

端到端task success rate。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 评分

检查最终或必要中间网站状态；查询答案使用精确、包含或GPT-4-0613模糊比较。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 提示和复现设置

canonical README示例使用accessibility tree、p_cot_id_actree_2s.json两例CoT提示；评测须自部署网站而非演示站，跑完812例后重置环境。模型、最大步数和是否提供not-achievable hint需逐结果固定。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）。

### 官方脚本

https://github.com/web-arena-x/webarena

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 可比性提示

WebArena与VisualWebArena/WebArena-Infinity/Verified变体不同；截图与可访问树观察、外部浏览和步数预算也不同。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 最新情况

### 核验时间

2026-11-08

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）。

### 数据版本与当前状态

- **version**：canonical v0.2.0，812任务；2023-10-24完成全数据复查与标注修复；2024-12-05推荐AgentLab
- **evidence_2026_h2**：- - **url**：https://arxiv.org/html/2609.19134v1
 - **date**：2026-09-17
 - **note**：ScienceIDE §4.2及参考文献明确引用 WebArena 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。
 - **date**：2026-09-17
属于§4.2相关工作引用，非本文实跑。
 - - **url**：
 - **date**：2026-09
 - **note**：官方维护Sheet主榜收录Narada AI Code 86.1，时间列09/2026；是当期榜单收录的参评者成绩，不推断独立复跑。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）；[3](https://arxiv.org/abs/2609.19134)（访问 2026-11-07）；[4]（访问 2026-11-08）。

### 论文修订与H2证据

- **previous_evidence_note**：Submission history From: Shuyan Zhou [ view email ] [v1] 2023-07-26 07:59:32 (9,497 KB) [v2] 2023-10-24 12:19:22 (8,751 KB) [v3] 2023-10-25 10:56:14 (8,751 KB) [v4] 2024-04-17 00:13:18 (9,472 KB)
- **revisions**：- - **version**：v1
 - **date**：2023-07-26
 - - **version**：v2
 - **date**：2023-10-24
 - - **version**：v3
 - **date**：2023-10-25
 - - **version**：v4
 - **date**：2024-04-17
- **note**：论文修订时间已从arXiv的UTC转换为；不能当作数据发布日期。既有2026-H2证据保留原采集日期。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 饱和程度

官方Sheet最高汇总结果86.1%，不等同于统一协议独立评测；原始人类78.24%只在按模板选择的任务上，不应与全量系统结果直接比较。

来源：[1]（访问 2026-11-08）。

### 污染、冲突与限制

固定模板、公开测试和使用LLM模糊裁判会影响泛化解释；网站环境版本需要固定。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 后续工作与衍生

VisualWebArena增加视觉条件；WebArena-Infinity按文档生成新环境及可验证任务。官方HF的webarena-infinity-trajectories为Infinity成功轨迹，不是canonical812任务原始测试卡；不得替代其数据身份。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）；[2](https://huggingface.co/datasets/webarena-x/webarena-infinity-trajectories/raw/main/README.md)（访问 2026-11-08）。

## 榜单快照

### 快照采集日

2026-11-08

来源：[1]（访问 2026-11-08）。

### 官方榜单

待核实

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）；[2]（访问 2026-11-08）。

### 第三方覆盖

待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### 官方Sheet主榜（参评者汇总）

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| 1 | Narada AI Code | 86.1 % | task success rate | 09/2026； |
| 2 | Deepseek v3.2 | 74.3 % | task success rate | 02/2026； |
| 3 | OpAgent | 71.6 % | task success rate | 01/2026； |
| 4 | ColorBrowserAgent | 71.2 % | task success rate | 12/2025； |
| 5 | Claude Code + GBOX MCP | 68.0 % | task success rate | 10/2025； |
| 6 | DeepSky Agent | 66.9 % | task success rate | 09/2025； |
| 7 | Narada AI | 64.2 % | task success rate | 10/2025； |
| 8 | IBM CUGA | 61.7 % | task success rate | 02/2025； |
| 9 | OpenAI Operator | 58.1 % | task success rate | 01/2025； |
| 10 | Jace.AI | 57.1 % | task success rate | 08/2024； |
| 11 | GLM-4-32B + Qwen2.5-VL-7B | 56.3 % | task success rate | 06/2026； |
| 12 | WebOperator + GPT-4o | 54.6 % | task success rate | 12/2025； |
| 13 | ScribeAgent + GPT-4o | 53.0 % | task success rate | 12/2024； |
| 14 | AgentSymbiotic | 52.1 % | task success rate | 01/2025； |
| 15 | Learn-by-Interact | 48.0 % | task success rate | 01/2025； |
| 16 | AgentOccam-Judge | 45.7 % | task success rate | 10/2024； |
| 17 | A3-Qwen3.5-9B | 42.1 % | task success rate | 04/2026； |
| 18 | WebPilot | 37.2 % | task success rate | 08/2024； |
| 19 | GUI-API Hybrid Agent | 35.8 % | task success rate | 10/2024； |
| 20 | Agent Workflow Memory | 35.5 % | task success rate | 09/2024； |
| 21 | SteP | 33.5 % | task success rate | 04/2024； |
| 22 | TTI | 26.1 % | task success rate | 06/2025； |
| 23 | BrowserGym + GPT-4 | 23.5 % | task success rate | 04/2024； |
| 24 | AgentTrek-1.0-32B | 22.4 % | task success rate | 01/2025； |
| 25 | GPT-4 + Auto Eval | 20.2 % | task success rate | 04/2024； |
| 26 | GPT-4o + Tree Search | 19.2 % | task success rate | 06/2024； |
| 27 | AutoWebGLM | 18.2 % | task success rate | 04/2024； |
| 28 | NNetNav | 16.3 % | task success rate | 01/2025； |
| 29 | gpt-4-0613 | 14.9 % | task success rate | 06/2023； |
| 30 | gpt-4o-2024-05-13 | 13.1 % | task success rate | 05/2024； |
| 31 | gpt-4-0613 | 11.7 % | task success rate | 06/2023； |
| 32 | Patel et al + 2024 | 9.36 % | task success rate | 05/2024； |
| 33 | gpt-3.5-turbo-16k-0613 | 8.87 % | task success rate | 03/2023； |
| 34 | Qwen-1.5-chat-72b | 7.14 % | task success rate | 09/2023； |
| 35 | Gemini Pro | 7.12 % | task success rate | 12/2023； |
| 36 | Llama3-chat-70b | 7.02 % | task success rate | 04/2024； |
| 37 | Synatra-CodeLLama7b | 6.28 % | task success rate | 10/2024； |
| 38 | Lemur-chat-70b | 5.3 % | task success rate | 10/2023； |
| 39 | Agent Flan | 4.68 % | task success rate | 03/2024； |
| 40 | CodeLlama-instruct-34b | 4.06 % | task success rate | 08/2023； |
| 41 | AgentLM-70b | 3.81 % | task success rate | 10/2023； |
| 42 | Llama3-chat-8b | 3.32 % | task success rate | 04/2024； |
| 43 | CodeAct Agent | 2.3 % | task success rate | 02/2024； |
| 44 | AgentLM-13b | 1.6 % | task success rate | 10/2023； |
| 45 | Mixtral | 1.39 % | task success rate | 01/2024； |
| 46 | AgentLM-7b | 0.74 % | task success rate | 10/2023； |
| 47 | FireAct | 0.25 % | task success rate | 10/2023； |
| 48 | CodeLlama-instruct-7b | 0.0 % | task success rate | 08/2023； |

#### 官方Sheet/Reddit子集

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | AutoGuide | 43.7 % | task success rate | 03/2024； |
| — | AutoManual | 65.1 % | task success rate | 09/2024； |

#### 官方Sheet/按模板选择的人类子集

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Human | 78.24 % | task success rate | |

#### 原论文v4 Table 2/CoT=True/UA_hint=True/all

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | TEXT-BISON-001 | 5.05 % | task success rate all | https://arxiv.org/pdf/2307.13854 |
| — | GPT-3.5 | 8.75 % | task success rate all | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 11.7 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=True/UA_hint=True/achievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | TEXT-BISON-001 | 4.0 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-3.5 | 6.44 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 8.63 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=True/UA_hint=True/unachievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | TEXT-BISON-001 | 27.78 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-3.5 | 58.33 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 77.78 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=False/UA_hint=True/all

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 6.41 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=False/UA_hint=True/achievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 4.9 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=False/UA_hint=True/unachievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 38.89 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=False/UA_hint=False/all

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 5.1 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=False/UA_hint=False/achievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 4.9 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=False/UA_hint=False/unachievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 8.33 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=True/UA_hint=False/all

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 6.16 % | task success rate all | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 14.41 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=True/UA_hint=False/achievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 6.06 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 13.02 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=True/UA_hint=False/unachievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | GPT-3.5 | 8.33 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |
| — | GPT-4 | 44.44 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=None/UA_hint=True/all

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Human | 78.24 % | task success rate all | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=None/UA_hint=True/achievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Human | 77.3 % | task success rate achievable | https://arxiv.org/pdf/2307.13854 |

#### 原论文v4 Table 2/CoT=None/UA_hint=True/unachievable

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Human | 100.0 % | task success rate unachievable | https://arxiv.org/pdf/2307.13854 |

来源：[1]（访问 2026-11-08）；[2](https://arxiv.org/pdf/2307.13854)（访问 2026-11-08）。

### 覆盖说明

读取官方Sheet全部51行：48主榜、2个Reddit子集、1个人类模板抽样；子集CSV字段错位已按原值复位，保留原source_date月份。追加原论文v4 Table 2全部8配置的all/achievable/unachievable三类成绩。旧档把14.41归为Table 3已纠正为Table 2；Sheet14.9与论文14.41不强行合并。

来源：[1]（访问 2026-11-08）；[2](https://arxiv.org/pdf/2307.13854)（访问 2026-11-08）。

## 联系方式

### 公开联系邮箱

- shuyanzh@cs.cmu.edu
- fangzhex@cs.cmu.edu
- gneubig@cs.cmu.edu

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 问题反馈

https://github.com/web-arena-x/webarena/issues

> 公开仓库反馈入口；未发送问题。

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 官方讨论渠道

待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

### 隐私与数据使用

待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2307.13854

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2307.13854)（访问 2026-11-08）。

### SHA-256

f9731b92bc3d29a2ea7b5f9cb46b48540c76bc3f84a57e0c48fc37ea73107f95

> 重新下载的原始PDF字节；既有副本未覆盖。

来源：[1](https://arxiv.org/pdf/2307.13854)（访问 2026-11-08）。

### 字节数

9128123

来源：[1](https://arxiv.org/pdf/2307.13854)（访问 2026-11-08）。

### 文件夹

来源：。

### 其他文档

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://webarena.dev/og/)（访问 2026-11-08）。

### 原文归档

来源：。

## 变更记录

### 本页修订

- - **date**：2026-11-07
 - **change**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- - **date**：2026-11-07
 - **round**：1 / 深度实证复核
 - **change**：补v0.2.0/AgentLab运行口径，重读官方Sheet当前前三和H2收录；并列论文14.41与Sheet14.9历史差异。
- - **date**：2026-11-08
 - **round**：2
 - **change**：逐项打开arXiv摘要与PDF全文、官方README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-08）。
