# Terminal-Bench

> 本页中文整理与本轮复核：2026-11-08（KST / Asia/Seoul）。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

Terminal-Bench以可执行终端任务评估长期行动与工具使用。当前数据release已到4.1.0，但官网与AA本次可见榜仍是4.0；题量同为66也不能忽略验证器修订，另63题CPU-only是不同运行集合。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-08，KST）

## 基本信息

### 简称

Terminal-Bench

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）

### 全称

Terminal-Bench

说明：保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）

### 基准版本

Terminal-Bench 4.0（榜单口径）；官方最新tag已为4.1.0，不能称4.0是最新发布版

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）；[2](https://github.com/harbor-framework/terminal-bench/releases)（访问 2026-11-07，KST）；[3](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（访问 2026-11-07，KST）；[4](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[5](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07，KST）；[6](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07，KST）

### 论文版本

arXiv v1；提交于 2026-01-17 10:29:30 KST

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 发布日期

4.0.0：2026-08-26 13:48:12 KST；4.1.0：2026-11-04 05:39:05 KST（GitHub published_at，Asia/Seoul）

来源：[1](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.1.0)（访问 2026-11-08，KST）；[2](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.0.0)（访问 2026-11-08，KST）

### 主板块

代码

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 领域标签

- 终端环境长程任务

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 许可与适用范围

当前harbor-framework/terminal-bench仓库LICENSE为Apache-2.0；包含的第三方软件、原始数据及依赖须分别遵守相应许可，不自动推导为全任务素材同许可。

来源：[1](https://github.com/harbor-framework/terminal-bench/blob/main/LICENSE)（访问 2026-11-08，KST）

### 论文

https://arxiv.org/abs/2601.11868

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 代码仓库

https://github.com/harbor-framework/terminal-bench

说明：当前官方仓库；历史terminal-bench-1许可及论文另行保留。

来源：[1](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（访问 2026-11-07，KST）

### 数据地址

https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4

说明：4.0版本固定链接；不使用latest替代版本固定。

来源：[1](https://github.com/harbor-framework/terminal-bench/releases)（访问 2026-11-07，KST）

### 官方主页

https://www.tbench.ai/

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）

### 论文标题

Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

## 发起与维护

### 机构与发起关系

Laude Institute、Stanford University 研究人员与开源贡献者；作者单位还包括多所大学和机构。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 合作机构

论文列出开源任务贡献者及多机构作者；不将所有单位视为联合发起。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 作者

- Merrill, Mike A.
- Shaw, Alexander G.
- Carlini, Nicholas
- Li, Boxuan
- Raj, Harsh
- Bercovich, Ivan
- Shi, Lin
- Shin, Jeong Yeon
- Walshe, Thomas
- Buchanan, E. Kelly
- Shen, Junhong
- Ye, Guanghao
- Lin, Haowei
- Poulos, Jason
- Wang, Maoyu
- Nezhurina, Marianna
- Jitsev, Jenia
- Lu, Di
- Mastromichalakis, Orfeas Menis
- Xu, Zhiwei
- Chen, Zizhao
- Liu, Yue
- Zhang, Robert
- Chen, Leon Liangyu
- Kashyap, Anurag
- Uslu, Jan-Lucas
- Li, Jeffrey
- Wu, Jianbo
- Yan, Minghao
- Bian, Song
- Sharma, Vedang
- Sun, Ke
- Dillmann, Steven
- Anand, Akshay
- Lanpouthakoun, Andrew
- Koopah, Bardia
- Hu, Changran
- Guha, Etash
- Dreiman, Gabriel H. S.
- Zhu, Jiacheng
- Krauth, Karl
- Zhong, Li
- Muennighoff, Niklas
- Amanfu, Robert
- Tan, Shangyin
- Pimpalgaonkar, Shreyas
- Aggarwal, Tushar
- Lin, Xiangning
- Lan, Xin
- Zhao, Xuandong
- Liang, Yiqing
- Wang, Yuanli
- Wang, Zilong
- Zhou, Changzhi
- Heineman, David
- Liu, Hange
- Trivedi, Harsh
- Yang, John
- Lin, Junhong
- Shetty, Manish
- Yang, Michael
- Omi, Nabil
- Raoof, Negin
- Li, Shanda
- Zhuo, Terry Yue
- Lin, Wuwei
- Dai, Yiwei
- Wang, Yuxin
- Chai, Wenhao
- Zhou, Shang
- Wahdany, Dariush
- She, Ziyu
- Hu, Jiaming
- Dong, Zhikang
- Zhu, Yuxuan
- Cui, Sasha
- Saiyed, Ahson
- Kolbeinsson, Arinbjörn
- Hu, Jesse
- Rytting, Christopher Michael
- Marten, Ryan
- Wang, Yixin
- Dimakis, Alex
- Konwinski, Andy
- Schmidt, Ludwig

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 当前维护方

Terminal-Bench / Laude Institute 项目团队

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 资助与支持

当前README列算力支持Modal、Anthropic、OpenAI、Google；由Harbor与Laude Institute托管；数据伙伴与算力赞助不等同。

来源：[1](https://github.com/harbor-framework/terminal-bench)（访问 2026-11-08，KST）

## 设计目标

### 衡量能力

在终端中自主完成复杂、长程、可验证的真实技术任务，涵盖软件、系统、科研与安全。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 设计背景

既有评测或不够现实，或难度不足以区分前沿 agent；需要具备环境、任务与可靠终态检验的协议。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

## 构建方式

### 题目或数据来源

2.0：93 位贡献者创建 229 个任务，按难度与质量选出 89 个；每题含 Docker 环境、说明、测试与人工解。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 出题背景

开源贡献者和领域技术人员；作者背景跨软件、ML、系统与安全。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 审核流程

2.0 的每题经三位人工审查者验证。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 质量控制

人工参考解、环境可运行性与终态测试；4.0 继续改善说明、环境、verifier 并重新校准预算。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 去污染与泄漏

公开数据有禁止用于训练的 canary 声明；这是一种管理信号，不保证训练集未见。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

## 数据形式

### 规模

论文2.0：89题；2026-09研究2.1：89题；AA当前4.0：66题。版本独立记录，不把66题改写成2.1题数。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

### 题型

给定任务与容器，agent 经 shell / 文件操作完成目标。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

### 模态

- 文本
- 代码
- 终端/文件环境

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

### 语言

英语任务说明；解题可用多种编程语言及系统工具。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

### 难度

面向高技能现实工作，2.0 原论文前沿 agent 仍低于65%（当时结果，非当前上限）。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

### 数据划分

任务和 harness 公开；运行时 verifier 与参考解不可作为 agent 解题资料。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

## 评测方法

### 指标

pass@1 / task resolution rate。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）

### 评分方式

4.0每任务必须通过全部测试才记成功；AA运行66题、mini-swe-agent，每题重复3次后报告平均pass@1。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）

### 提示与运行设置

AA4.0：mini-swe-agent，66题各运行3次再平均；研究2.1与产品CLI harness另列。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）

### 评测脚本

https://github.com/laude-institute/terminal-bench

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）

### 可比性提醒

版本、时限、算力、终端harness和repeat不同会改变结果；AA Coding Agent Index 产品CLI结果不等于同机构 mini-swe-agent 模型榜。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）

## 最新情况

### 核验日期

2026-11-08 KST / Asia/Seoul

来源：[1](https://www.tbench.ai/)（访问 2026-11-08，KST）

### 数据版本与更新

```json
{
  "current_version": "4.1.0（最新发布）；官网/AA可见榜仍4.0",
  "release_date": "4.0.0：2026-08-26 13:48:12 KST；4.1.0：2026-11-04 05:39:05 KST（GitHub published_at，Asia/Seoul）",
  "version_changes": "4.0从3.0的74题中移除8题，保留66题，重新校准计算/时间预算并改进指令、环境及验证器。2.0与2.1的89题仅作为旧协议，不与66题相混。另：官方4.1.0已发布，66题均有修改但未增删任务，新增63题CPU-only数据集；4.0成绩不能重标为4.1。",
  "trending": "A",
  "why_trending": "2026-08-26官方发布4.0；Cognition 2026-10-27官方FrontierCode 2.0文章将Terminal-Bench 4.0作对照；AA 2026-10-28独立发布Gemini 4 Carbon在4.0上的结果，当前另有66题统一harness榜。多机构材料支持A级，但不将不同agent的64%与65.2%混排。",
  "history": {
    "previous_version_field": {
      "value": "当前官网 / AA 为 4.0；保留论文2.0与H2研究2.1",
      "sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0",
          "accessed": "2026-11-07"
        }
      ]
    },
    "previous_release_date_field": {
      "value": "2026-01-17 10:29:30 KST",
      "sources": [
        {
          "url": "https://arxiv.org/abs/2601.11868",
          "accessed": "2026-11-07"
        }
      ],
      "note": "首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。"
    },
    "previous_status_field": {
      "value": {
        "version": "当前官网 / AA 为 4.0；保留论文2.0与H2研究2.1",
        "evidence_2026_h2": [
          {
            "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
            "date": "2026-10-28",
            "note": "Artificial Analysis 2026-10-28明确报告 Terminal-Bench 4.0 的评测结果；作为版本化套件只计一次。"
          },
          {
            "url": "https://arxiv.org/html/2609.20804v1",
            "date": "2026-09-17",
            "note": "H2 harness研究同时在 Terminal-Bench 2.1 的89个端到端CLI任务上实际开展实验，显示版本差异必须保留。"
          }
        ]
      },
      "sources": [
        {
          "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
          "accessed": "2026-11-07"
        },
        {
          "url": "https://arxiv.org/html/2609.20804v1",
          "accessed": "2026-11-07"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0",
          "accessed": "2026-11-07"
        }
      ],
      "note": "H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。"
    },
    "previous_results_field": {
      "value": [
        {
          "model": "Kimi K3.1 Pro",
          "score": 67.2,
          "metric": "pass@1 (%)",
          "benchmark_version": "4.0/66题",
          "result_type": "AA独立当前页面",
          "source_date": "待核实（页面未给出该结果运行/发布日期）",
          "collected_at": "2026-11-07 KST",
          "harness": "mini-swe-agent；3 repeats",
          "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
        },
        {
          "model": "Gemini 4 Carbon (High)",
          "score": 65.2,
          "metric": "pass@1 (%)",
          "benchmark_version": "4.0/66题",
          "result_type": "AA独立当前页面",
          "source_date": "待核实（页面未给出该结果运行/发布日期）",
          "collected_at": "2026-11-07 KST",
          "harness": "mini-swe-agent；3 repeats",
          "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
        },
        {
          "model": "Claude Sonnet 5.5 (Max, Default Fallback)",
          "score": 63.6,
          "metric": "pass@1 (%)",
          "benchmark_version": "4.0/66题",
          "result_type": "AA独立当前页面",
          "source_date": "待核实（页面未给出该结果运行/发布日期）",
          "collected_at": "2026-11-07 KST",
          "harness": "mini-swe-agent；3 repeats",
          "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
        },
        {
          "model": "Gemini 4 Carbon (High) + Antigravity CLI",
          "score": 64,
          "metric": "Terminal-Bench score (%)",
          "benchmark_version": "4.0",
          "result_type": "AA历史产品agent评测",
          "source_date": "待核实（页面未给出该结果运行/发布日期）",
          "collected_at": "2026-11-07 KST",
          "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
        }
      ],
      "sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0",
          "accessed": "2026-11-07"
        },
        {
          "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
          "accessed": "2026-11-07"
        }
      ]
    }
  },
  "dataset_url_4_1": "https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/5"
}
```

来源：[1](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.1.0)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-08，KST）

### 论文修订记录

- {"version": "v1", "submitted_at": "2026-01-17 10:29:30 KST", "timezone": "Asia/Seoul"}

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-08，KST）

### 饱和证据与局限

本次AA统一mini-swe-agent的4.0最高为67.2%，仍有未解决任务；4.1更改验证器与防reward hacking，4.0结果不能当作4.1饱和证据。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-08，KST）；[2](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.1.0)（访问 2026-11-08，KST）

### 争议与已知问题

4.1官方发布说明：验证器修复、可复现性改进与防reward hacking；66题均修改、无新增删除，另有63题CPU-only。题目相同数量不意味着评分口径相同。

来源：[1](https://github.com/harbor-framework/terminal-bench/releases/tag/v4.1.0)（访问 2026-11-08，KST）

### 衍生或后继基准

2.0、2.1、4.0按同一版本化套件计一次；Terminal-Bench-Science 等另有范围，不自动替代主集。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-07，KST）；[2](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）；[3](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07，KST）

## 榜单快照

### 快照访问日期

2026-11-08 KST / Asia/Seoul

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-08，KST）

### 官方榜单入口

https://www.tbench.ai/

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）

### 第三方入口

https://artificialanalysis.ai/evaluations/terminalbench-4-0

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07，KST）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| AA统一harness / 4.0 | 1 | Kimi K3.1 Pro | 67.2 | pass@1 (%) | 4.0 / 66 tasks；mini-swe-agent；3 repeats/task | [待核实（页面未标各次运行或榜单整体更新时间）](https://artificialanalysis.ai/evaluations/terminalbench-4-0)；采集2026-11-08 KST / Asia/Seoul |
| AA统一harness / 4.0 | 2 | Gemini 4 Carbon (High) | 65.2 | pass@1 (%) | 4.0 / 66 tasks；mini-swe-agent；3 repeats/task | [待核实（页面未标各次运行或榜单整体更新时间）](https://artificialanalysis.ai/evaluations/terminalbench-4-0)；采集2026-11-08 KST / Asia/Seoul |
| AA统一harness / 4.0 | 3 | Claude Sonnet 5.5 (Max, Default Fallback) | 63.6 | pass@1 (%) | 4.0 / 66 tasks；mini-swe-agent；3 repeats/task | [待核实（页面未标各次运行或榜单整体更新时间）](https://artificialanalysis.ai/evaluations/terminalbench-4-0)；采集2026-11-08 KST / Asia/Seoul |

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-08，KST）

### 榜单覆盖边界

本次重新打开官网及AA；官网首屏未输出系统榜数值，保留AA当前页明确写出的前三名，非完整244模型榜。官方最新发布4.1.0，所列仍严格为4.0 / 66题 / mini-swe-agent / 三次重复，不重标4.1。

来源：[1](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-08，KST）

## 联系方式

### 官方公开邮箱

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-07，KST）

### 公开反馈渠道

https://github.com/laude-institute/terminal-bench/issues

说明：公开仓库反馈入口；未发送问题。

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）

### 官方社交账号

https://discord.gg/6xWPKhGDbA（官方README公开社区渠道）

来源：[1](https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/README.md)（访问 2026-11-07，KST）

### 联系方式/隐私原则

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2601.11868)（访问 2026-11-07，KST）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2601.11868

来源：[1](https://arxiv.org/pdf/2601.11868)（访问 2026-11-08，KST）

### PDF SHA-256

4430e04a507b2442bb7b24a88899b750948fa0a6b3bbc33a8d541d6d4debcc1e

来源：[1](https://arxiv.org/pdf/2601.11868)（访问 2026-11-08，KST）

### PDF字节数

```json
2773926
```

来源：[1](https://arxiv.org/pdf/2601.11868)（访问 2026-11-08，KST）

### Drive文件夹

```json
{
  "id": "1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC",
  "webViewLink": "https://drive.google.com/drive/folders/1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC"
}
```

来源：[1](https://drive.google.com/drive/folders/1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC)（访问 2026-11-07，KST）

### 其他文档

- {"type": "中文介绍Google Doc", "id": "13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg", "webViewLink": "https://docs.google.com/document/d/13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg/edit?usp=drivesdk"}

说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://www.tbench.ai/)（访问 2026-11-07，KST）；[2](https://docs.google.com/document/d/13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg/edit?usp=drivesdk)（访问 2026-11-07，KST）

### Drive论文原件

```json
{
  "id": "1xESLe_ARjnszPudgBFEW2yfE62M0tK-p",
  "webViewLink": "https://drive.google.com/file/d/1xESLe_ARjnszPudgBFEW2yfE62M0tK-p/view?usp=drivesdk"
}
```

来源：[1](https://drive.google.com/file/d/1xESLe_ARjnszPudgBFEW2yfE62M0tK-p/view?usp=drivesdk)（访问 2026-11-07，KST）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "第1轮深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。"}
- {"date": "2026-11-07", "timezone": "Asia/Shanghai", "change": "近期热门版本复核：4.0从3.0的74题中移除8题，保留66题，重新校准计算/时间预算并改进指令、环境及验证器。2.0与2.1的89题仅作为旧协议，不与66题相混。另：官方4.1.0已发布，66题均有修改但未增删任务，新增63题CPU-only数据集；4.0成绩不能重标为4.1。 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。", "sources": [{"url": "https://www.tbench.ai/", "accessed": "2026-11-07"}, {"url": "https://github.com/harbor-framework/terminal-bench/releases", "accessed": "2026-11-07"}, {"url": "https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md", "accessed": "2026-11-07"}, {"url": "https://artificialanalysis.ai/evaluations/terminalbench-4-0", "accessed": "2026-11-07"}, {"url": "https://cognition.com/blog/frontier-code-2.0", "accessed": "2026-11-07"}, {"url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1", "accessed": "2026-11-07"}]}
- {"date": "2026-11-08", "timezone": "Asia/Seoul", "change": "第2轮逐源深核：直接核实当前仓库Apache-2.0，不再仅依旧terminal-bench-1仓库。；官方4.1发布日期转KST，66题修改与63题CPU-only分开；AA4.0重新核验且不重标4.1。"}

来源：[1](https://www.tbench.ai/)（访问 2026-11-08，KST）
