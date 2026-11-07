# Berkeley Function Calling Leaderboard (BFCL)

> 第1轮深度复核：2026-11-07（KST / Asia/Seoul）。采集日不等于榜单更新日或评测运行日；“待核实”不等于不存在。

[阅读Drive原始论文PDF](https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk)

## 基本信息

### 简称

Berkeley Function Calling Leaderboard (BFCL)

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 全称

Berkeley Function Calling Leaderboard

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 基准版本

当前BFCL V4；Hunyuan报告为V3

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 论文版本

ICML 2025，PMLR 267，页48371–48392

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 发布日期

BFCL V4发布于2025-07-17；V2为2024-08-19，V3为2024-09-19。首次V1精确发布日期待核实。

来源：[1](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md)（访问 2026-11-07 KST）。

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 领域标签

- 函数调用

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 许可证

官方BFCL README明确榜单统计与用于训练的数据以Apache-2.0发布；第三方工具/API条款须独立遵守。

来源：[1](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md)（访问 2026-11-07 KST）。

### 论文

https://proceedings.mlr.press/v267/patil25a.html

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 官方代码

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 数据地址

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 官方入口

https://gorilla.cs.berkeley.edu/leaderboard.html

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 论文标题

The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

## 发起与维护

### 发起机构

UC Berkeley Gorilla研究团队（机构口径）

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 合作研究机构

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 作者

- Shishir G Patil
- Huanzhi Mao
- Fanjia Yan
- Charlie Cheng-Jie Ji
- Vishnu Suresh
- Ion Stoica
- Joseph E. Gonzalez

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 维护方

Gorilla / BFCL团队

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 资助

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

## 设计目标

### 衡量能力

选择工具、构造合法参数、串并行函数调用、拒绝无关调用及有状态多步Agent决策。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 设计背景

工具调用既需要多样真实函数来源，也需要可扩展地判断不同语法表达是否同样有效。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

## 构建方式

### 题目来源

专家整理函数与用户/企业/开源社区贡献的真实函数和提示；覆盖多编程语言。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 出题者背景

Berkeley研究者与企业/开源工具贡献者。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 审核流程

专家整理与用户贡献结合，使用AST/执行等按类别验证调用。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 质量控制

区分单轮、并行、多轮、相关性与状态；AST验证语义参数而非纯字符串表面。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 去污染

V2加入企业和社区真实贡献数据；V4 Web Search博客发现较新模型可能凭已有知识答对部分题，计划周期更新问题。工具使用表现与预训练记忆不能简单分离，非无污染保证。

来源：[1](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md)（访问 2026-11-07 KST）。

## 数据形式

### 规模

- **scored_entries_v4**：5088
- **scored_categories**：{"agentic": 665, "multi_turn": 800, "live": 1351, "non_live": 1150, "irrelevance": 1122}
- **non_scoring_entries**：5218
- **non_scoring_breakdown**：{"format_sensitivity": 5200, "relevance": 18}
- **agentic_breakdown**：{"web_search": 200, "memory": 465}

> 按官方V4博客score composition口径记录。format sensitivity是26×200组配置，不当作5,200个全新独立问题；不同版本不相加。

来源：[1](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)（访问 2026-11-07 KST）。

### 题型

单/并行函数调用、多轮状态交互、相关性/拒绝调用与agentic任务。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 模态

- 文本
- 结构化函数schema
- 工具调用

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 语言

多种编程语言函数；自然语言分布需按具体版本核实。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 难度与类型

以结构复杂性分层而非统一easy/hard：单/多工具、并行调用、多轮基础/缺函数/缺参数/长上下文，以及web-search和memory。Web Search含多跳链；不估计通用难度比例。

来源：[1](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md)（访问 2026-11-07 KST）。

### 公开与隐藏划分

官方发布数据和评测包；各版本子集与隐藏性需按V4材料确认。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

## 评测方法

### 指标

V4 Overall为固定百分比加权：Agentic 40% + Multi-Turn 30% + Live 10% + Non-Live 10% + Irrelevance/Hallucination 10%。类别内部另按官方规则使用加权或非加权均值。

> 纠正旧条目“Overall是所有子类非加权均值”。官网首页仍有笼统unweighted措辞，与V4博客及CHANGELOG不一致；按更具体的V4定义并列保存冲突。

来源：[1](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md)（访问 2026-11-07 KST）；[3](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 评分

单轮AST匹配与多轮状态+响应检查；2025-04-09 CHANGELOG已退休rest及exec_*旧可执行类别，不能再把它们称当前V4总分构成。Web Search/Memory按agentic规则评估，format-sensitivity和relevance不影响主总分。

来源：[1](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md)（访问 2026-11-07 KST）；[2](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)（访问 2026-11-07 KST）。

### 提示和复现设置

页面当前标示代码commit f7cf7359b7ac615a0b294831c5ba2bc95ee4a000；bfcl-eval==2025.12.17；模型提示和native-FC须一起固定。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 官方脚本

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 可比性提示

V1(AST)、V2(真实贡献函数)、V3(多轮)、V4(agentic)覆盖变化，Hunyuan的BFCLv3不可当作当前V4成绩。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-07 KST / Asia/Seoul

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 最新版本与H2证据

- **version**：当前BFCL V4；Hunyuan报告为V3
- **evidence_2026_h2**：[{"url": "https://arxiv.org/html/2609.27284v1", "date": "2026-09-23", "note": "Hunyuan-A13B §4.2 Agents及表3–4实际报告 Berkeley Function Calling Leaderboard (BFCL)（BFCL为v3），属于厂商自报评测。", "date_kst": "2026-09-23T12:21:24+09:00", "verified_in_round1": "本轮重新打开Hunyuan-A13B §4.2 Agents表格，确认BFCLv3 78.3/65.9是slow/fast-thinking厂商自报，非V4。"}, {"url": "https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference", "date": "2026-08-24", "note": "AA启动文章实际评测BFCL 640任务子集；独立第三方使用证据，不等同BFCL V4全量。"}]

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 KST）；[2](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）；[3](https://arxiv.org/abs/2609.27284)（访问 2026-11-07 KST）；[4](https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference)（访问 2026-11-07 KST）。

### 论文修订与H2使用证据

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

### 饱和程度

官方V4 CHANGELOG明确称单轮趋近饱和，故改为提高多轮/Agentic权重；当前Overall最高77.47%，不能沿用单轮接近饱和的结论到V4全体任务。

来源：[1](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md)（访问 2026-11-07 KST）；[2](https://gorilla.cs.berkeley.edu/data_overall.csv)（访问 2026-11-07 KST）。

### 污染、冲突与限制

AST正确不等于业务任务完成；多轮与记忆带来新评测维度，版本间不可用一个总分追踪。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 后续工作与衍生

BFCL V1–V4为演进版本；本库只计一个函数调用benchmark。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-07 KST / Asia/Seoul

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 官方榜单

https://gorilla.cs.berkeley.edu/leaderboard.html

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 权威第三方覆盖

- **endpoint_accuracy_methodology**：https://artificialanalysis.ai/methodology/endpoint-accuracy-index
- **mobile_subset_launch**：https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference

> AA有500-task offline-only、3 repeats的BFCL v4-500及mobile 640-task子集；都不是官方全量V4，原“无已核实AA覆盖”现纠正。

来源：[1](https://artificialanalysis.ai/methodology/endpoint-accuracy-index)（访问 2026-11-07 KST）；[2](https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference)（访问 2026-11-07 KST）。

### 结果快照

- {"model": "Claude-Opus-4-5-20251101 (FC)", "score": 77.47, "unit": "%", "metric": "V4 weighted overall accuracy", "scope": "BFCL V4 Overall；官方当前data_overall.csv", "date": "待核实", "accessed": "2026-11-07 KST", "source_url": "https://gorilla.cs.berkeley.edu/data_overall.csv", "provenance": "本轮打开官网JavaScript实际加载的CSV，保留FC/Prompt及模型精确快照。", "rank": 1, "benchmark_version": "V4", "leaderboard_updated_at": "2026-04-12", "multi_turn": 68.38, "web_search": 84.5, "memory": 73.76}
- {"model": "Claude-Sonnet-4-5-20250929 (FC)", "score": 73.24, "unit": "%", "metric": "V4 weighted overall accuracy", "scope": "BFCL V4 Overall；官方当前data_overall.csv", "date": "待核实", "accessed": "2026-11-07 KST", "source_url": "https://gorilla.cs.berkeley.edu/data_overall.csv", "provenance": "本轮打开官网JavaScript实际加载的CSV，保留FC/Prompt及模型精确快照。", "rank": 2, "benchmark_version": "V4", "leaderboard_updated_at": "2026-04-12", "multi_turn": 61.37, "web_search": 81.0, "memory": 64.95}
- {"model": "Gemini-3-Pro-Preview (Prompt)", "score": 72.51, "unit": "%", "metric": "V4 weighted overall accuracy", "scope": "BFCL V4 Overall；官方当前data_overall.csv", "date": "待核实", "accessed": "2026-11-07 KST", "source_url": "https://gorilla.cs.berkeley.edu/data_overall.csv", "provenance": "本轮打开官网JavaScript实际加载的CSV，保留FC/Prompt及模型精确快照。", "rank": 3, "benchmark_version": "V4", "leaderboard_updated_at": "2026-04-12", "multi_turn": 60.75, "web_search": 80.0, "memory": 61.72}
- {"model": "GLM-4.6 (FC thinking)", "score": 72.38, "unit": "%", "metric": "V4 weighted overall accuracy", "scope": "BFCL V4 Overall；官方当前data_overall.csv", "date": "待核实", "accessed": "2026-11-07 KST", "source_url": "https://gorilla.cs.berkeley.edu/data_overall.csv", "provenance": "本轮打开官网JavaScript实际加载的CSV，保留FC/Prompt及模型精确快照。", "rank": 4, "benchmark_version": "V4", "leaderboard_updated_at": "2026-04-12", "multi_turn": 68.0, "web_search": 77.5, "memory": 55.7}
- {"model": "Grok-4-1-fast-reasoning (FC)", "score": 69.57, "unit": "%", "metric": "V4 weighted overall accuracy", "scope": "BFCL V4 Overall；官方当前data_overall.csv", "date": "待核实", "accessed": "2026-11-07 KST", "source_url": "https://gorilla.cs.berkeley.edu/data_overall.csv", "provenance": "本轮打开官网JavaScript实际加载的CSV，保留FC/Prompt及模型精确快照。", "rank": 5, "benchmark_version": "V4", "leaderboard_updated_at": "2026-04-12", "multi_turn": 58.87, "web_search": 82.5, "memory": 53.98}
- {"model": "Hunyuan-A13B slow-thinking", "score": 78.3, "metric": "BFCLv3 (%)", "benchmark_version": "V3", "result_type": "厂商技术报告自报", "source_date": "2026-09-23", "collected_at": "2026-11-07 KST"}
- {"model": "Hunyuan-A13B fast-thinking", "score": 65.9, "metric": "BFCLv3 (%)", "benchmark_version": "V3", "result_type": "厂商技术报告自报", "source_date": "2026-09-23", "collected_at": "2026-11-07 KST"}
- {"model": "Qwen3.5 9B (Non-reasoning)", "score": 77, "unit": "%", "metric": "accuracy", "scope": "Artificial Analysis mobile BFCL 640-task subset；量化build，16K context", "date": "2026-08-24", "accessed": "2026-11-07 KST", "source_url": "https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference", "provenance": "AA独立评测的启动文章；不是全量V4总分，不作为2026-11当前第三方排名。"}
- {"model": "Nanbeige4.2-3B", "score": 76, "unit": "%", "metric": "accuracy", "scope": "Artificial Analysis mobile BFCL 640-task subset；量化build，16K context", "date": "2026-08-24", "accessed": "2026-11-07 KST", "source_url": "https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference", "provenance": "AA启动文章明确的BFCL子项分数，非Mobile平均指数；不与全量V4混排。"}

来源：[1](https://gorilla.cs.berkeley.edu/data_overall.csv)（访问 2026-11-07 KST）；[2](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）；[3](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 KST）；[4](https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference)（访问 2026-11-07 KST）。

### 覆盖说明

本轮从index_main.js确认官网读取data_overall.csv后重新采集：V4前三Claude-Opus-4-5-20251101 (FC) 77.47、Claude-Sonnet-4-5-20250929 (FC) 73.24、Gemini-3-Pro-Preview (Prompt) 72.51。官网标Last Updated 2026-04-12；不是2026-11-07新跑分。V3厂商报告和AA子集结果分别标scope，不混为V4排名。

来源：[1](https://gorilla.cs.berkeley.edu/data_overall.csv)（访问 2026-11-07 KST）；[2](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）；[3](https://artificialanalysis.ai/methodology/endpoint-accuracy-index)（访问 2026-11-07 KST）；[4](https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference)（访问 2026-11-07 KST）。

## 联系方式

### 公开联系邮箱

- huanzhimao@berkeley.edu
- shishirpatil@berkeley.edu

> 前者是README联系邮箱；后者为ICML论文公开通讯邮箱。

来源：[1](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)（访问 2026-11-07 KST）。

### 问题反馈

https://github.com/ShishirPatil/gorilla/issues

> 公开仓库反馈入口；未发送问题。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

### 官方讨论渠道

https://discord.gg/grXXvj9Whz

> 官方Discord公开邀请，README指定#leaderboard频道；未加入或发送消息。

来源：[1](https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/README.md)（访问 2026-11-07 KST）。

### 隐私政策

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://proceedings.mlr.press/v267/patil25a.html)（访问 2026-11-07 KST）。

## 原始文件

### 源站论文PDF

https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)（访问 2026-11-07 KST）。

### SHA-256

5248f4770823b2a73fd52e3b12339d94121ff1b359c45163c5a47168edab7a2f

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)（访问 2026-11-07 KST）。

### 字节数

1200643

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)（访问 2026-11-07 KST）。

### Drive文件夹

- **id**：1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT
- **webViewLink**：https://drive.google.com/drive/folders/1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT

来源：[1](https://drive.google.com/drive/folders/1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT)（访问 2026-11-07 KST）。

### 其他文档

- {"type": "中文介绍Google Doc", "id": "1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748", "webViewLink": "https://docs.google.com/document/d/1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748/edit?usp=drivesdk"}

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）；[2](https://docs.google.com/document/d/1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748/edit?usp=drivesdk)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw
- **webViewLink**：https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "round": "1 / 深度实证复核", "change": "读官网真实CSV补V4前五；补5088计分/5218不计分构成；修正V4固定加权而非全子类等权；补AA真实子集覆盖与H2证据。"}

来源：[1](https://gorilla.cs.berkeley.edu/leaderboard.html)（访问 2026-11-07 KST）。

