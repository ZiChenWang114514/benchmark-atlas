# Terminal-Bench

> 核验：2026-11-07（Asia/Shanghai（UTC+8））。官方材料中文改写；采集日不等于运行日，历史榜单、研究复测与独立评测分别记录。

## 本次热门版本更新（2026-11-07，Asia/Shanghai UTC+8）

4.0从3.0的74题中移除8题，保留66题，重新校准计算/时间预算并改进指令、环境及验证器。2.0与2.1的89题仅作为旧协议，不与66题相混。另：官方4.1.0已发布，66题均有修改但未增删任务，新增63题CPU-only数据集；4.0成绩不能重标为4.1。

Terminal-Bench 4.0（榜单口径）；官方最新tag已为4.1.0，不能称4.0是最新发布版

发布时间：4.0.0：2026-08-26 12:48:12（Asia/Shanghai，UTC+8，官方tag发布时间）；4.1.0：2026-11-04 04:39:05（Asia/Shanghai，UTC+8）

- [https://www.tbench.ai/](https://www.tbench.ai/)（accessed 2026-11-07）
- [https://github.com/harbor-framework/terminal-bench/releases](https://github.com/harbor-framework/terminal-bench/releases)（accessed 2026-11-07）
- [https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（accessed 2026-11-07）
- [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（accessed 2026-11-07）
- [https://cognition.com/blog/frontier-code-2.0](https://cognition.com/blog/frontier-code-2.0)（accessed 2026-11-07）
- [https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（accessed 2026-11-07）

### 为什么近期热门

证据等级：A。2026-08-26官方发布4.0；Cognition 2026-10-27官方FrontierCode 2.0文章将Terminal-Bench 4.0作对照；AA 2026-10-28独立发布Gemini 4 Carbon在4.0上的结果，当前另有66题统一harness榜。多机构材料支持A级，但不将不同agent的64%与65.2%混排。

- [https://www.tbench.ai/](https://www.tbench.ai/)（accessed 2026-11-07）
- [https://github.com/harbor-framework/terminal-bench/releases](https://github.com/harbor-framework/terminal-bench/releases)（accessed 2026-11-07）
- [https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（accessed 2026-11-07）
- [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（accessed 2026-11-07）
- [https://cognition.com/blog/frontier-code-2.0](https://cognition.com/blog/frontier-code-2.0)（accessed 2026-11-07）
- [https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（accessed 2026-11-07）

### 当前榜单快照

当前快照来源：https://artificialanalysis.ai/evaluations/terminalbench-4-0。保留模型配置原名。整体更新时间与各模型实际运行日期待核实。 注意官方tag已到4.1.0，以上榜单明确仍是4.0。

| 名次（同协议） | 模型配置 | 分数 | 版本/范围 |
|---|---|---|---|
| 1 | Kimi K3.1 Pro | 67.2 | 4.0 |
| 2 | Gemini 4 Carbon (High) | 65.2 | 4.0 |
| 3 | Claude Sonnet 5.5 (Max, Default Fallback) | 63.6 | 4.0 |

指标：pass@1 (%)，mini-swe-agent，3 repeats/task；FrontierMath数值如适用均为0–1比例，非百分数。采集：2026-11-07（Asia/Shanghai UTC+8）；采集日不等于评测运行日。

- [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（accessed 2026-11-07）


## 基本信息

### 简称

Terminal-Bench

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 全称

Terminal-Bench

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 基准版本

Terminal-Bench 4.0（榜单口径）；官方最新tag已为4.1.0，不能称4.0是最新发布版

- [https://www.tbench.ai/](https://www.tbench.ai/)（accessed 2026-11-07）
- [https://github.com/harbor-framework/terminal-bench/releases](https://github.com/harbor-framework/terminal-bench/releases)（accessed 2026-11-07）
- [https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（accessed 2026-11-07）
- [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（accessed 2026-11-07）
- [https://cognition.com/blog/frontier-code-2.0](https://cognition.com/blog/frontier-code-2.0)（accessed 2026-11-07）
- [https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（accessed 2026-11-07）

### 论文版本

arXiv v1

> 论文修订版本不等同数据集版本。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 发布日期

4.0.0：2026-08-26 12:48:12（Asia/Shanghai，UTC+8，官方tag发布时间）；4.1.0：2026-11-04 04:39:05（Asia/Shanghai，UTC+8）

历史首发/论文日期：2026-01-17 09:29:30（Asia/Shanghai，UTC+8）

- [https://www.tbench.ai/](https://www.tbench.ai/)（accessed 2026-11-07）
- [https://github.com/harbor-framework/terminal-bench/releases](https://github.com/harbor-framework/terminal-bench/releases)（accessed 2026-11-07）
- [https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（accessed 2026-11-07）
- [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（accessed 2026-11-07）
- [https://cognition.com/blog/frontier-code-2.0](https://cognition.com/blog/frontier-code-2.0)（accessed 2026-11-07）
- [https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（accessed 2026-11-07）
- [https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（accessed 2026-11-07）

### 主板块

代码

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 领域标签

终端环境长程任务

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 许可证

历史terminal-bench-1仓库LICENSE为Apache-2.0；不能自动外推至当前4.0全部任务及第三方软件，4.0具体适用范围待核实。

核验状态：待核实

来源：[https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/LICENSE](https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/LICENSE)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 论文

https://arxiv.org/abs/2601.11868

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 官方代码

https://github.com/harbor-framework/terminal-bench

当前官方仓库；历史terminal-bench-1许可及论文另行保留。

- [https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（accessed 2026-11-07）

### 数据地址

https://hub.harborframework.com/datasets/terminal-bench/terminal-bench/4

4.0版本固定链接；不使用latest替代版本固定。

- [https://github.com/harbor-framework/terminal-bench/releases](https://github.com/harbor-framework/terminal-bench/releases)（accessed 2026-11-07）

### 官方入口

https://www.tbench.ai/

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 论文标题

Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 发起与维护

### 机构与发起方

Laude Institute、Stanford University 研究人员与开源贡献者；作者单位还包括多所大学和机构。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 合作方

论文列出开源任务贡献者及多机构作者；不将所有单位视为联合发起。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 作者

Merrill, Mike A.、Shaw, Alexander G.、Carlini, Nicholas、Li, Boxuan、Raj, Harsh、Bercovich, Ivan、Shi, Lin、Shin, Jeong Yeon、Walshe, Thomas、Buchanan, E. Kelly、Shen, Junhong、Ye, Guanghao、Lin, Haowei、Poulos, Jason、Wang, Maoyu、Nezhurina, Marianna、Jitsev, Jenia、Lu, Di、Mastromichalakis, Orfeas Menis、Xu, Zhiwei、Chen, Zizhao、Liu, Yue、Zhang, Robert、Chen, Leon Liangyu、Kashyap, Anurag、Uslu, Jan-Lucas、Li, Jeffrey、Wu, Jianbo、Yan, Minghao、Bian, Song、Sharma, Vedang、Sun, Ke、Dillmann, Steven、Anand, Akshay、Lanpouthakoun, Andrew、Koopah, Bardia、Hu, Changran、Guha, Etash、Dreiman, Gabriel H. S.、Zhu, Jiacheng、Krauth, Karl、Zhong, Li、Muennighoff, Niklas、Amanfu, Robert、Tan, Shangyin、Pimpalgaonkar, Shreyas、Aggarwal, Tushar、Lin, Xiangning、Lan, Xin、Zhao, Xuandong、Liang, Yiqing、Wang, Yuanli、Wang, Zilong、Zhou, Changzhi、Heineman, David、Liu, Hange、Trivedi, Harsh、Yang, John、Lin, Junhong、Shetty, Manish、Yang, Michael、Omi, Nabil、Raoof, Negin、Li, Shanda、Zhuo, Terry Yue、Lin, Wuwei、Dai, Yiwei、Wang, Yuxin、Chai, Wenhao、Zhou, Shang、Wahdany, Dariush、She, Ziyu、Hu, Jiaming、Dong, Zhikang、Zhu, Yuxuan、Cui, Sasha、Saiyed, Ahson、Kolbeinsson, Arinbjörn、Hu, Jesse、Rytting, Christopher Michael、Marten, Ryan、Wang, Yixin、Dimakis, Alex、Konwinski, Andy、Schmidt, Ludwig

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 当前维护方

Terminal-Bench / Laude Institute 项目团队

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 设计目标

### 衡量能力

在终端中自主完成复杂、长程、可验证的真实技术任务，涵盖软件、系统、科研与安全。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 设计背景

既有评测或不够现实，或难度不足以区分前沿 agent；需要具备环境、任务与可靠终态检验的协议。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 构建方式

### 题目来源

2.0：93 位贡献者创建 229 个任务，按难度与质量选出 89 个；每题含 Docker 环境、说明、测试与人工解。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 出题者背景

开源贡献者和领域技术人员；作者背景跨软件、ML、系统与安全。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 审核流程

2.0 的每题经三位人工审查者验证。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 质量控制

人工参考解、环境可运行性与终态测试；4.0 继续改善说明、环境、verifier 并重新校准预算。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 去污染

公开数据有禁止用于训练的 canary 声明；这是一种管理信号，不保证训练集未见。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 数据形式

### 题量与规模

论文2.0：89题；2026-09研究2.1：89题；AA当前4.0：66题。版本独立记录，不把66题改写成2.1题数。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 题型

给定任务与容器，agent 经 shell / 文件操作完成目标。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 模态

文本、代码、终端/文件环境

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 语言

英语任务说明；解题可用多种编程语言及系统工具。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 难度

面向高技能现实工作，2.0 原论文前沿 agent 仍低于65%（当时结果，非当前上限）。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 公开与隐藏划分

任务和 harness 公开；运行时 verifier 与参考解不可作为 agent 解题资料。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 评测方法

### 指标

pass@1 / task resolution rate。

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 评分

4.0每任务必须通过全部测试才记成功；AA运行66题、mini-swe-agent，每题重复3次后报告平均pass@1。

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 提示与运行设置

AA4.0：mini-swe-agent，66题各运行3次再平均；研究2.1与产品CLI harness另列。

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 官方评测脚本

https://github.com/laude-institute/terminal-bench

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 可比性警示

版本、时限、算力、终端harness和repeat不同会改变结果；AA Coding Agent Index 产品CLI结果不等于同机构 mini-swe-agent 模型榜。

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 最新情况

### 核查日期

2026-11-07 Asia/Shanghai（UTC+8）

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 当前版本与2026年后半年活跃证据

```json
{
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
}
```

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 论文修订历史

Submission history From: Mike A. Merrill [ view email ] [v1] 2026-01-17 09:29:30（Asia/Shanghai，UTC+8） (17,342 KB)

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 污染与争议

版本2.x与4.0的题目、环境与预算改变；旧分数不能搬到新版本。公开任务与参考解接触会破坏评测。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 衍生与版本关系

2.0、2.1、4.0按同一版本化套件计一次；Terminal-Bench-Science 等另有范围，不自动替代主集。

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 历史榜单快照与协议（保留；当前排名见页首更新）

### 快照日期

2026-11-07 Asia/Shanghai（UTC+8）

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 官方榜单

https://www.tbench.ai/

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 独立评测覆盖

https://artificialanalysis.ai/evaluations/terminalbench-4-0

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 核验结果

```json
[
  {
    "model": "Kimi K3.1 Pro",
    "score": 67.2,
    "metric": "pass@1 (%)",
    "benchmark_version": "4.0/66题",
    "result_type": "AA独立当前页面",
    "source_date": "待核实（页面未给出该结果运行/发布日期）",
    "collected_at": "2026-11-07 Asia/Shanghai（UTC+8）",
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
    "collected_at": "2026-11-07 Asia/Shanghai（UTC+8）",
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
    "collected_at": "2026-11-07 Asia/Shanghai（UTC+8）",
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
    "collected_at": "2026-11-07 Asia/Shanghai（UTC+8）",
    "leaderboard_updated_at": "待核实（静态正文未标注整体更新时间）"
  }
]
```

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 覆盖与时效说明

官网当前版本标题核实；AA 页面给出独立模型榜前三。10月28日64%来自不同产品CLI设置，不与65.2%认定为同次更新或错误。实际各次运行日期未公开于摘要。

来源：[https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 公开反馈

https://github.com/laude-institute/terminal-bench/issues

> 公开仓库反馈入口；未发送问题。

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 官方社交渠道

https://discord.gg/6xWPKhGDbA（官方README公开社区渠道）

来源：[https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench-1/main/README.md)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2601.11868

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[https://arxiv.org/pdf/2601.11868](https://arxiv.org/pdf/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 原始PDF SHA-256

4430e04a507b2442bb7b24a88899b750948fa0a6b3bbc33a8d541d6d4debcc1e

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2601.11868](https://arxiv.org/pdf/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 原始PDF字节数

2773926

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2601.11868](https://arxiv.org/pdf/2601.11868)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### Drive资料文件夹

```json
{
  "id": "1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC",
  "webViewLink": "https://drive.google.com/drive/folders/1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC"
}
```

来源：[https://drive.google.com/drive/folders/1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC](https://drive.google.com/drive/folders/1pqVETDnTmA4D-A9xYqF7Vu-lSLuHOdCC)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg",
    "webViewLink": "https://docs.google.com/document/d/13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg/edit?usp=drivesdk"
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））；[https://docs.google.com/document/d/13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg/edit?usp=drivesdk](https://docs.google.com/document/d/13b09PixYeASFWScp_DNwmfXMMNhz0SzdZTGR__1Dowg/edit?usp=drivesdk)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### Drive 原始 PDF

```json
{
  "id": "1xESLe_ARjnszPudgBFEW2yfE62M0tK-p",
  "webViewLink": "https://drive.google.com/file/d/1xESLe_ARjnszPudgBFEW2yfE62M0tK-p/view?usp=drivesdk"
}
```

来源：[https://drive.google.com/file/d/1xESLe_ARjnszPudgBFEW2yfE62M0tK-p/view?usp=drivesdk](https://drive.google.com/file/d/1xESLe_ARjnszPudgBFEW2yfE62M0tK-p/view?usp=drivesdk)（访问 2026-11-07 Asia/Shanghai（UTC+8））

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "第1轮深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。"
  }
]
```

来源：[https://www.tbench.ai/](https://www.tbench.ai/)（访问 2026-11-07 Asia/Shanghai（UTC+8））

### 2026-11-07 热门版本复核

近期热门版本复核：4.0从3.0的74题中移除8题，保留66题，重新校准计算/时间预算并改进指令、环境及验证器。2.0与2.1的89题仅作为旧协议，不与66题相混。另：官方4.1.0已发布，66题均有修改但未增删任务，新增63题CPU-only数据集；4.0成绩不能重标为4.1。 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。

- [https://www.tbench.ai/](https://www.tbench.ai/)（accessed 2026-11-07）
- [https://github.com/harbor-framework/terminal-bench/releases](https://github.com/harbor-framework/terminal-bench/releases)（accessed 2026-11-07）
- [https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md](https://raw.githubusercontent.com/harbor-framework/terminal-bench/main/README.md)（accessed 2026-11-07）
- [https://artificialanalysis.ai/evaluations/terminalbench-4-0](https://artificialanalysis.ai/evaluations/terminalbench-4-0)（accessed 2026-11-07）
- [https://cognition.com/blog/frontier-code-2.0](https://cognition.com/blog/frontier-code-2.0)（accessed 2026-11-07）
- [https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（accessed 2026-11-07）
