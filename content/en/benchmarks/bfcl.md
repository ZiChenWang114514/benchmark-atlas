# Berkeley Function Calling Leaderboard (BFCL)

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Checked item by item against the evidence: the paper PDF, the official release materials, and the leaderboards for each protocol; items not confirmed are kept

## Basic information

### Short name

Berkeley Function Calling Leaderboard (BFCL)

### Full name

Berkeley Function Calling Leaderboard

### 数据/软件版本

BFCL V4; V1–V3 are historical protocols

### Paper version

ICML 2025, PMLR 267, pages 48371–48392.

### Release date

V1: 2024-02-26. V4 Agentic: 2025-07-17 (the official data README states Original and Latest Release Date explicitly, and gives no time of day). ICML2025 for the paper, and the date on which the data were first released, are kept apart.

### Section

Agent

Note: Benchmark Constitution editorial filing. Only the main section is counted.

### 学科标签

Function calling

### 许可证与范围

The official BFCL README states that the leaderboard statistics and the data used for training are released under Apache-2.0; third-party tool and API terms must be followed separately.

### 论文入口

https://proceedings.mlr.press/v267/patil25a.html

### Paper title

The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models

### Code

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

### Dataset

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

### Official homepage

https://gorilla.cs.berkeley.edu/leaderboard.html

## Origin and maintenance

### 发起团队

UC Berkeley Gorilla research team (institutional scope)

### 署名/合作机构

Unverified

Note: The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Status: Unverified (part of this field is still unconfirmed).

### Authors

Shishir G Patil；Huanzhi Mao；Fanjia Yan；Charlie Cheng-Jie Ji；Vishnu Suresh；Ion Stoica；Joseph E. Gonzalez

### 维护入口

Gorilla / BFCL team

### 资助与计算资源

Unverified

Note: The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Status: Unverified (part of this field is still unconfirmed).

## Design goals

函数调用正确性不等于整个业务任务成功。BFCL不断把重点从单轮AST转向多轮状态与Agentic记忆；必须固定V4权重、代码/数据版本和FC或Prompt配置，V3高分不能置换V4总分。

### 测量能力

Tool selection, construction of valid parameters, serial and parallel function calls, rejection of irrelevant calls, and stateful multi-step agent decisions.

### 为何需要这个基准

Tool calling requires both diverse sources of real functions and a scalable way to judge whether different syntactic expressions are equally valid.

## Construction

### 材料来源

Functions curated by experts, together with real functions and prompts contributed by users, companies, and the open-source community; multiple programming languages are covered.

### 命题/编制背景

Berkeley researchers and contributors from industry and open-source tools.

### Review process

Expert curation is combined with user contributions, and calls are verified by category using AST, execution, and similar checks.

### Quality control

Distinguishes single-turn, parallel, multi-turn, relevance, and state; AST checks semantic parameters rather than the surface of a bare string.

### 去污染与证据边界

V2 adds real contribution data from enterprises and from the community; the V4 Web Search blog finds that a newer model may answer some questions correctly from knowledge it already has, and it plans to update the questions on a cycle. Performance when tools are used, and memory from pretraining, cannot be separated in a simple way, and this is not a guarantee that there is no contamination.

## Data format

### 规模与分母

scored_entries_v4：5088；scored_categories：agentic：665；multi_turn：800；live：1351；non_live：1150；irrelevance：1122；non_scoring_entries：5218；non_scoring_breakdown：format_sensitivity：5200；relevance：18；agentic_breakdown：web_search：200；memory：465

Note: Recorded on the score-composition basis of the official V4 blog. Format sensitivity consists of 26×200 groups of configurations and is not treated as 5,200 entirely new independent questions; different versions are not added together.

### Question types

Single and parallel function calls, multi-turn stateful interaction, relevance and refusal calls, and agentic tasks.

### 模态与字段

文本；Structured function schema；工具调用

### Languages

The official data README marks the natural language as en; the functions cover Python, Java, JavaScript, and others. A function in more than one language is not the same thing as a question surface in more than one natural language.

### 难度定位

Stratified by structural complexity rather than by a uniform easy or hard label: single tool and multiple tools, parallel calls, multi-turn basic, missing function, missing parameter, and long context, together with web-search and memory. Web Search includes multi-hop chains. A general proportion of difficulty is not estimated.

### 公开、隐藏与划分

The official GitHub releases JSONL questions, function schemas, and the corresponding evaluation files by category; the HF card still describes the old version dated 2024-09-22, and its V3 description should not replace the GitHub V4 inventory. Each category is selected by the official script, not by a new random train/test split.

## Evaluation

### Metrics

V4 Overall is a fixed percentage weighting: Agentic 40% + Multi-Turn 30% + Live 10% + Non-Live 10% + Irrelevance/Hallucination 10%. Inside a category, a weighted or an unweighted mean is used according to the official rules.

Note: Corrects the old entry that said “Overall is the unweighted mean of all subclasses.” The homepage of the official website still uses loose wording about an unweighted mean, which disagrees with the V4 blog and the CHANGELOG; the conflict is kept side by side under the more specific definition in V4.

### 评分流程

Single-turn AST matching and multi-turn state-plus-response checks. The CHANGELOG of 2025-04-09 retired the old executable categories rest and exec_*, and they can no longer be called constituents of the current V4 total score. Web Search and Memory are evaluated under agentic rules. format-sensitivity and relevance do not affect the primary total score.

### 运行与提示

The page currently marks code commit f7cf7359b7ac615a0b294831c5ba2bc95ee4a000 and bfcl-eval==2025.12.17. The model prompt and native-FC must be fixed together.

### 评测实现

https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

### 不能混比的设置

Coverage changes across V1 (AST), V2 (real contributed functions), V3 (multi-turn), and V4 (agentic). Hunyuan’s BFCLv3 cannot be treated as a current V4 result.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

current_version：BFCL V4; V1–V3 are historical protocols；release_date：V1 2024-02-26; V4 2025-07-17 (official data README)；version_changes：V1 introduced single-turn AST, V2 introduced enterprise and community contributions, and V3 introduced multi-turn. V4 adds Web Search, Memory, and Format Sensitivity. The total-score weights are Agentic40%, Multi-Turn30%, Live10%, Non-Live10%, and Hallucination10%. Format Sensitivity is not counted in the total score. The official V4 methods blog is authoritative. The official-site overview's "unweighted average of all sub-categories" should not override the fixed-weight definition in the detailed specification.；trending：B；why_trending：On 2026-08-24, AA actually used a 640-task subset of BFCL in a mobile evaluation. The official Qwen model card currently lists BFCL-V4, but the evaluation release date of that card has not been confirmed. The last update time of the official V4 leaderboard is still 2026-04-12, so it cannot be called a new H2 score. Recent evidence that clearly carries a date is mainly the AA subset, provisionally listed as B. The date of new adoption of the full V4 set after 2026-08 remains Unverified.；history_note：history keeps the existing fields of older versions and the older snapshots as they are; an older Unverified among them is a historical record and is not used to overwrite the current conclusion of verification.

### 版本脉络

paper：The official paper, ICML2025/PMLR267:48371–48392.；dataset_original_release：2024-02-26；V4_release：2025-07-17；leaderboard_updated：2026-04-12；changes_source：https://raw.githubusercontent.com/ShishirPatil/gorilla/main/berkeley-function-call-leaderboard/CHANGELOG.md；paper_source：The official ICML/PMLR paper is taken as the authority; an arXiv identifier that has not been verified is not conjectured.

### 分数上限与饱和度

The official V4 CHANGELOG states explicitly that the single-turn setting is nearing saturation, and for that reason the weights of the multi-turn and Agentic settings were raised; the current Overall peaks at 77.47%, and the conclusion that the single-turn setting is near saturation cannot be carried over to every task in V4.

### 争议与局限

A correct AST is not completion of the business task; multiple turns and memory add new evaluation dimensions, and a single total score cannot track across versions.

### 衍生版本

BFCL V1–V4 are successive versions; this repository counts only one function-calling benchmark.

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

https://gorilla.cs.berkeley.edu/leaderboard.html

### 第三方/补充实验

endpoint_accuracy_methodology：https://artificialanalysis.ai/methodology/endpoint-accuracy-index；mobile_subset_launch：https://artificialanalysis.ai/articles/mobile-phone-intelligence-inference

Note: AA has a 500-task offline-only BFCL v4-500 with 3 repeats, and a mobile subset of 640 tasks. Neither is the official full V4. The earlier claim of “no verified AA coverage” is now corrected.

### 分轨成绩

#### Official V4 Overall (FC/Prompt configurations kept under their original names)

| Source order / track index | Model / system | Score | Metric |
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

### 覆盖边界

The official CSV was opened again, and the top 10 were transcribed exactly, with the native FC, Prompt, and thinking configuration kept. Last Updated on the official site is 2026-04-12, and this is not a new run. V4 follows the fixed weights in the blog rather than the word unweighted in the overview on the official site; the HF card is a description of the old 2024 release, and it is not used to update the scale of V4.

## Contact

### 公开作者工作邮箱

huanzhimao@berkeley.edu；shishirpatil@berkeley.edu

Note: The former is the contact email in the README; the latter is the public correspondence email in the ICML paper.

### 公开反馈

https://github.com/ShishirPatil/gorilla/issues

Note: Public repository feedback entry point; no question was sent.

### 官方账号

https://discord.gg/grXXvj9Whz

Note: The official Discord invite is public, and the README designates the #leaderboard channel; the channel was not joined and no message was sent.

### 隐私信息

Unverified

Note: The official README, the project page, and the readable papers were checked again; this field still lacks a sufficiently explicit official statement. It remains Unverified and is not inferred to be Not disclosed or to be nonexistent.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf

Note: Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

### 下载源文件SHA-256

5248f4770823b2a73fd52e3b12339d94121ff1b359c45163c5a47168edab7a2f

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

1200643

### 其他材料

Note: The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

### 既有 PDF链接

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- 2026-11-07：读官网真实CSV补V4前五；补5088计分/5218不计分构成；修正V4固定加权而非全子类等权；补AA真实子集覆盖与H2证据。
- 2026-11-07：近期热门版本复核：V1 introduced single-turn AST, V2 introduced enterprise and community contributions, and V3 introduced multi-turn. V4 adds Web Search, Memory, and Format Sensitivity. The total-score weights are Agentic40%, Multi-Turn30%, Live10%, Non-Live10%, and Hallucination10%. Format Sensitivity is not counted in the total score. The official V4 methods blog is authoritative. The official-site overview's "unweighted average of all sub-categories" should not override the fixed-weight definition in the detailed specification. 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。
- 2026-11-07（）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

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
