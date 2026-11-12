# Berkeley Function Calling Leaderboard (BFCL)

> 核查：2026-11-07。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

Berkeley Function Calling Leaderboard (BFCL)

来源：[1]

### 全称

Berkeley Function Calling Leaderboard

来源：[2]

### 数据/软件版本

BFCL V4；V1–V3为历史协议

来源：[1][3][4][5][6][7]

### 论文版本

ICML 2025，PMLR 267，页48371–48392

来源：[2]

### 发布日期

V1：2024-02-26；V4 Agentic：2025-07-17（官方数据README明确Original/Latest Release Date，无时刻）；论文ICML2025与数据首发日期分开。

来源：[8][2]

### 主板块

Agent

来源：[2]

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

### 学科标签

函数调用

来源：[2]

### 许可证与范围

官方BFCL README明确榜单统计与用于训练的数据以Apache-2.0发布；第三方工具/API条款须独立遵守。

来源：[9]

### 论文入口

https://proceedings.mlr.press/v267/patil25a.html

来源：[2]

### 论文标题

The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models

来源：[2]

### 官方代码

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

来源：[1]

### 数据入口

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

来源：[1]

### 官方主页

https://gorilla.cs.berkeley.edu/leaderboard.html

来源：[1]

## 2. 发起与维护

### 发起团队

UC Berkeley Gorilla研究团队（机构口径）

来源：[2]

### 署名/合作机构

待核实

来源：[2]

说明：已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

状态：待核实（本字段尚有未能确认的部分）。

### 作者

Shishir G Patil；Huanzhi Mao；Fanjia Yan；Charlie Cheng-Jie Ji；Vishnu Suresh；Ion Stoica；Joseph E. Gonzalez

来源：[2]

### 维护入口

Gorilla / BFCL团队

来源：[2]

### 资助与计算资源

待核实

来源：[2]

说明：已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

状态：待核实（本字段尚有未能确认的部分）。

## 3. 设计目标

函数调用正确性不等于整个业务任务成功。BFCL不断把重点从单轮AST转向多轮状态与Agentic记忆；必须固定V4权重、代码/数据版本和FC或Prompt配置，V3高分不能置换V4总分。
来源：[2][2]

### 测量能力

选择工具、构造合法参数、串并行函数调用、拒绝无关调用及有状态多步Agent决策。

来源：[2]

### 为何需要这个基准

工具调用既需要多样真实函数来源，也需要可扩展地判断不同语法表达是否同样有效。

来源：[2]

## 4. 构建方式

### 材料来源

专家整理函数与用户/企业/开源社区贡献的真实函数和提示；覆盖多编程语言。

来源：[2]

### 命题/编制背景

Berkeley研究者与企业/开源工具贡献者。

来源：[2]

### 审核流程

专家整理与用户贡献结合，使用AST/执行等按类别验证调用。

来源：[2]

### 质量控制

区分单轮、并行、多轮、相关性与状态；AST验证语义参数而非纯字符串表面。

来源：[2]

### 去污染与证据边界

V2加入企业和社区真实贡献数据；V4 Web Search博客发现较新模型可能凭已有知识答对部分题，计划周期更新问题。工具使用表现与预训练记忆不能简单分离，非无污染保证。

来源：[4][5]

## 5. 数据形式

### 规模与分母

scored_entries_v4：5088；scored_categories：agentic：665；multi_turn：800；live：1351；non_live：1150；irrelevance：1122；non_scoring_entries：5218；non_scoring_breakdown：format_sensitivity：5200；relevance：18；agentic_breakdown：web_search：200；memory：465

来源：[4]

说明：按官方V4博客score composition口径记录。format sensitivity是26×200组配置，不当作5,200个全新独立问题；不同版本不相加。

### 题型

单/并行函数调用、多轮状态交互、相关性/拒绝调用与agentic任务。

来源：[1]

### 模态与字段

文本；结构化函数schema；工具调用

来源：[1]

### 语言

官方数据README标记自然语言en；函数覆盖Python、Java、JavaScript等。多语言函数不等同于自然语言题面多语。

来源：[8][9]

### 难度定位

以结构复杂性分层而非统一easy/hard：单/多工具、并行调用、多轮基础/缺函数/缺参数/长上下文，以及web-search和memory。Web Search含多跳链；不估计通用难度比例。

来源：[4][9]

### 公开、隐藏与划分

官方GitHub按类别发布JSONL问题、function schema与对应评测文件；HF卡仍写2024-09-22旧版，不应拿其V3描述替代GitHub V4清单。各类别以官方脚本选择，非重新训练/测试随机划分。

来源：[8][10][9]

## 6. 评测方法

### 指标

V4 Overall为固定百分比加权：Agentic 40% + Multi-Turn 30% + Live 10% + Non-Live 10% + Irrelevance/Hallucination 10%。类别内部另按官方规则使用加权或非加权均值。

来源：[4][5][1]

说明：纠正旧条目“Overall是所有子类非加权均值”。官网首页仍有笼统unweighted措辞，与V4博客及CHANGELOG不一致；按更具体的V4定义并列保存冲突。

### 评分流程

单轮AST匹配与多轮状态+响应检查；2025-04-09 CHANGELOG已退休rest及exec_*旧可执行类别，不能再把它们称当前V4总分构成。Web Search/Memory按agentic规则评估，format-sensitivity和relevance不影响主总分。

来源：[5][4]

### 运行与提示

页面当前标示代码commit f7cf7359b7ac615a0b294831c5ba2bc95ee4a000；bfcl-eval==2025.12.17；模型提示和native-FC须一起固定。

来源：[1]

### 评测实现

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

来源：[1]

### 不能混比的设置

V1(AST)、V2(真实贡献函数)、V3(多轮)、V4(agentic)覆盖变化，Hunyuan的BFCLv3不可当作当前V4成绩。

来源：[1]

## 7. 最新情况

### 核查日期

2026-11-07（采集日，不是实验日）

来源：[2]

### 当前发布

current_version：BFCL V4；V1–V3为历史协议；release_date：V1 2024-02-26；V4 2025-07-17（官方数据README）；version_changes：V1引入AST单轮，V2引入企业/社区贡献，V3引入多轮；V4新增Web Search、Memory与Format Sensitivity。总分权重为Agentic40%、Multi-Turn30%、Live10%、Non-Live10%、Hallucination10%；Format Sensitivity不计总分。以官方V4方法博客为准；官网概述“unweighted average of all sub-categories”不应覆盖明细的固定权重定义。；trending：B；why_trending：AA于2026-08-24在移动端评测中实际使用BFCL 640任务子集；Qwen官方模型卡当前列BFCL-V4，但未确认该卡评测发布日期。官网V4榜最后更新时间仍是2026-04-12，不能称其为H2新跑分；近期明确带日期证据主要是AA子集，暂列B。V4全量在2026-08后的新增采用日期仍待核实。；history_note：history保留既有旧版字段与旧快照原样；其中旧待核实是历史记录，不据此覆盖当前核实结论。

来源：[8][4][5][1]

### 版本脉络

paper：ICML2025/PMLR267:48371–48392正式论文；dataset_original_release：2024-02-26；V4_release：2025-07-17；leaderboard_updated：2026-04-12；changes_source：https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md；paper_source：以官方ICML/PMLR论文为准，不推测未核实的arXiv编号。

来源：[2][8][5]

### 分数上限与饱和度

官方V4 CHANGELOG明确称单轮趋近饱和，故改为提高多轮/Agentic权重；当前Overall最高77.47%，不能沿用单轮接近饱和的结论到V4全体任务。

来源：[5][3]

### 争议与局限

AST正确不等于业务任务完成；多轮与记忆带来新评测维度，版本间不可用一个总分追踪。

来源：[1]

### 衍生版本

BFCL V1–V4为演进版本；本库只计一个函数调用benchmark。

来源：[1]

## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不是实验日）

来源：[2]

### 官方入口

https://gorilla.cs.berkeley.edu/leaderboard.html

来源：[1]

### 第三方/补充实验

endpoint_accuracy_methodology：https://artificialanalysis.ai/methodology/endpoint-accuracy-index；mobile_subset_launch：https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference

来源：[11][6]

说明：AA有500-task offline-only、3 repeats的BFCL v4-500及mobile 640-task子集；都不是官方全量V4，原“无已核实AA覆盖”现纠正。

### 分轨成绩

#### 官方V4 Overall（FC/Prompt配置按原名）

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Claude-Opus-4-5-20251101 (FC) | 77.47 | V4 fixed-weight overall accuracy (%) |
| 2 | Claude-Sonnet-4-5-20250929 (FC) | 73.24 | V4 fixed-weight overall accuracy (%) |
| 3 | Gemini-3-Pro-Preview (Prompt) | 72.51 | V4 fixed-weight overall accuracy (%) |
| 4 | GLM-4.6 (FC thinking) | 72.38 | V4 fixed-weight overall accuracy (%) |
| 5 | Grok-4-1-fast-reasoning (FC) | 69.57 | V4 fixed-weight overall accuracy (%) |
| 6 | Claude-Haiku-4-5-20251001 (FC) | 68.7 | V4 fixed-weight overall accuracy (%) |
| 7 | Gemini-3-Pro-Preview (FC) | 68.14 | V4 fixed-weight overall accuracy (%) |
| 8 | o3-2025-04-16 (Prompt) | 63.05 | V4 fixed-weight overall accuracy (%) |
| 9 | Grok-4-0709 (Prompt) | 62.97 | V4 fixed-weight overall accuracy (%) |
| 10 | Grok-4-0709 (FC) | 61.38 | V4 fixed-weight overall accuracy (%) |

- Claude-Opus-4-5-20251101 (FC)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：68.38；web_search：84.5；memory：73.76
- Claude-Sonnet-4-5-20250929 (FC)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：61.37；web_search：81.0；memory：64.95
- Gemini-3-Pro-Preview (Prompt)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：60.75；web_search：80.0；memory：61.72
- GLM-4.6 (FC thinking)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：68.0；web_search：77.5；memory：55.7
- Grok-4-1-fast-reasoning (FC)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：58.87；web_search：82.5；memory：53.98
- Claude-Haiku-4-5-20251001 (FC)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：53.62；web_search：83.5；memory：54.41
- Gemini-3-Pro-Preview (FC)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：63.12；web_search：68.5；memory：54.84
- o3-2025-04-16 (Prompt)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：62.25；web_search：50.5；memory：51.83
- Grok-4-0709 (Prompt)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：47.0；web_search：74.0；memory：50.54
- Grok-4-0709 (FC)：benchmark_version：V4；source_url：https://gorilla.cs.berkeley.edu/data_overall.csv；accessed：2026-11-07；leaderboard_updated_at：2026-04-12；multi_turn：33.88；web_search：82.0；memory：55.91

来源：[3]

### 覆盖边界

重新打开官方CSV，精确转录前10且保留native FC/Prompt/thinking配置。官网Last Updated=2026-04-12，非新运行。V4按博客固定权重而非官网概述unweighted文字；HF卡是2024旧发布描述，不用它更新V4规模。

来源：[3][4][10][1]

## 9. 联系方式

### 公开作者工作邮箱

huanzhimao@berkeley.edu；shishirpatil@berkeley.edu

来源：[9][12]

说明：前者是README联系邮箱；后者为ICML论文公开通讯邮箱。

### 公开反馈

https://github.com/ShishirPatil/gorilla/issues

来源：[1]

说明：公开仓库反馈入口；未发送问题。

### 官方账号

https://discord.gg/grXXvj9Whz

来源：[9]

说明：官方Discord公开邀请，README指定#leaderboard频道；未加入或发送消息。

### 隐私信息

待核实

来源：[2]

说明：已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

状态：待核实（本字段尚有未能确认的部分）。

## 10. 原始文件

### 原文PDF

https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf

来源：[12]

说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 下载源文件SHA-256

5248f4770823b2a73fd52e3b12339d94121ff1b359c45163c5a47168edab7a2f

来源：[12]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

1200643

来源：[12]

### 既有文件夹

来源：[13]

### 其他材料

来源：[1][14]

说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### 既有 PDF链接

来源：[15]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- 2026-11-07：读官网真实CSV补V4前五；补5088计分/5218不计分构成；修正V4固定加权而非全子类等权；补AA真实子集覆盖与H2证据。
- 2026-11-07：近期热门版本复核：V1引入AST单轮，V2引入企业/社区贡献，V3引入多轮；V4新增Web Search、Memory与Format Sensitivity。总分权重为Agentic40%、Multi-Turn30%、Live10%、Non-Live10%、Hallucination10%；Format Sensitivity不计总分。以官方V4方法博客为准；官网概述“unweighted average of all sub-categories”不应覆盖明细的固定权重定义。 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。
- 2026-11-07：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[1][3][4][5][6][7]

### 来源索引

[1]: https://gorilla.cs.berkeley.edu/leaderboard.html "访问 2026-11-07"
[2]: https://proceedings.mlr.press/v267/patil25a.html "访问 2026-11-07"
[3]: https://gorilla.cs.berkeley.edu/data_overall.csv "访问 2026-11-07"
[4]: https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html "访问 2026-11-07"
[5]: https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md "访问 2026-11-07"
[6]: https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference "访问 2026-11-07"
[7]: https://huggingface.co/Qwen/Qwen3.5-4B "访问 2026-11-07"
[8]: https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/bfcl_eval/data/README.md "访问 2026-11-07"
[9]: https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md "访问 2026-11-07"
[10]: https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard "访问 2026-11-07"
[11]: https://artificialanalysis.ai/methodology/endpoint-accuracy-index "访问 2026-11-07"
[12]: https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf "访问 2026-11-07"
[13]: "访问 2026-11-07"
[14]: "访问 2026-11-07"
[15]: "访问 2026-11-07"
