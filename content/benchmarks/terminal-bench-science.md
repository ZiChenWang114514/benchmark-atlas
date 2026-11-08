# Terminal-Bench-Science

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

Terminal-Bench-Science围绕研究者真实工作构建可验证终端流程，覆盖生命、物理、地球、数学与工程。本页严格以已发布0.1.0的70题解释AA分数，main开发中的86题与筹备2.0不改变历史分母。

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

## 基本信息

### 简称

Terminal-Bench-Science

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 全称

Terminal-Bench-Science

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 基准版本

0.1.0（AA明确的release；官网简写0.1）

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 论文版本

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 发布日期

v0.1.0：2026-08-26 19:24:33 （GitHub published_at）；公告日另为2026-08-27，不混为同一事件。

来源：[1](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)（访问 2026-11-08，）

### 主板块

物理

说明：编辑主板块归档，不据此限制跨学科覆盖。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 领域标签

- 跨学科科学
- 化学
- 生物与医学
- 地球与天文
- 数学
- 工程

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 许可与适用范围

Apache-2.0（当前仓库LICENSE与README软件引用）；各任务所含第三方数据仍应单独核对。

来源：[1](https://github.com/harbor-framework/terminal-bench-science/blob/main/LICENSE)（访问 2026-11-08，）

### 论文

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 代码仓库

https://github.com/harbor-framework/terminal-bench-science

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 数据地址

https://hub.harborframework.com/datasets/terminal-bench-science/terminal-bench-science/latest?tab=tasks

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 官方主页

https://terminal-bench-science.ai/

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 论文标题

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

## 发起与维护

### 机构与发起关系

Stanford University研究人员与Terminal-Bench / Harbor团队

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 合作机构

- Laude Institute
- SAIL
- HAI
- AIMS
- IFML
- Allen Institute
- Ai2

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 作者

Terminal-Bench-Science Team；发布文章署名Steven Dillmann

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 当前维护方

Terminal-Bench / Harbor团队及科学贡献者社区

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 资助与支持

Laude Slingshots、Snorkel AI Open Benchmarks Grants等；API credits与科研合作身份分开理解。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

## 设计目标

### 衡量能力

在终端完成真实科学研究工作流，产出分析、仿真、证明、代码与数据产品。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 设计背景

用执业科学家贡献的研究任务而非教材回忆题衡量可验证科研执行能力。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

## 构建方式

### 题目或数据来源

科学研究人员从自身工作提出任务，经GitHub提案与PR公开构建。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 出题背景

跨生命、物理、地球、数学与工程科学的研究人员。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 审核流程

提案审核后实施；领域审查、技术审查与最终bar-raiser质量检查。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 质量控制

提案→实现→审查；自动检查、并行领域与技术审查、最终bar-raiser批准。包括oracle通过/no-op失败、对抗作弊检查；官方建议在目标沙箱先跑5次oracle确认环境稳定。

来源：[1](https://github.com/harbor-framework/terminal-bench-science)（访问 2026-11-08，）

### 去污染与泄漏

官方页面带禁止将基准数据纳入训练语料的canary声明；不能把声明理解为已证明无污染。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

## 数据形式

### 规模

固定v0.1.0发布70题：生命19、物理17、数学17、工程9、地球8；当前main README统计86题属于开发状态，不得给0.1.0榜改分母。

来源：[1](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)（访问 2026-11-08，）；[2](https://github.com/harbor-framework/terminal-bench-science)（访问 2026-11-08，）；[3](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

### 题型

科学数据分析、统计推断、模拟、优化、证明、图像重建、信号处理等终端工作流。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

### 模态

- 文本
- 代码
- 科学数据/计算产物

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

### 语言

官方公开任务说明及AA示例采用英语；工作流还包含Python/命令行和领域数据文件，不是纯语言问答集。

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

### 难度

由领域专家提出真实研究工作流、要求可客观验证且对前沿agent有挑战；没有由官方公开的统一难度分级量表。

来源：[1](https://github.com/harbor-framework/terminal-bench-science)（访问 2026-11-08，）

### 数据划分

0.1.0任务公开；正式训练/验证/隐藏测试划分待核实。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

## 评测方法

### 指标

测试套件通过率 / resolution rate，pass@1。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

### 评分方式

每个任务必须通过全部测试；AA使用独立verifier容器。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

### 提示与运行设置

AA：70任务×3重复，mini-swe-agent，最多1000步；官网首发使用各厂商CLI，需分轨。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

### 评测脚本

Harbor运行框架与官方任务仓库；可在Modal或其他Harbor支持的环境运行。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

### 可比性提醒

官网发布结果、AA统一harness结果及厂商自报结果不可当成同一榜；Science Index综合分不是本单项分。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-08，）

### 数据版本与更新

最新可见正式release为v0.1.0，70题；main已有86题，2.0征稿尚在进行。开发分支题量不能当成已发布2.0。

来源：[1](https://github.com/harbor-framework/terminal-bench-science/releases/tag/v0.1.0)（访问 2026-11-08，）；[2](https://github.com/harbor-framework/terminal-bench-science)（访问 2026-11-08，）

### 论文修订记录

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 饱和证据与局限

AA固定0.1.0 / 70题最高64.8%；此为统一mini-swe-agent平均单次成功率，不能与官网不同CLI系统或main86题混比。

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

### 争议与已知问题

官方要求公开任务携带canary，并欢迎报告直接取答案、歧义指令、验证器误判及oracle不稳定；有防污染标记不等于已经证实无污染。

来源：[1](https://github.com/harbor-framework/terminal-bench-science)（访问 2026-11-08，）

### 衍生或后继基准

独立科学工作流套件，不是Terminal-Bench 4.0的别名；0.2开发已在首发公告提及，但不据此断言正式发布。

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

### 官方榜单入口

https://terminal-bench-science.ai/

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 第三方入口

https://artificialanalysis.ai/evaluations/terminal-bench-science

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-07，）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| AA统一harness / 0.1.0 | 1 | Gemini 4 Carbon (High) | 64.8 | pass@1 (%) | 0.1.0 / 70 tasks；mini-swe-agent；3 repeats/task | [待核实（网页未标各结果运行日期）](https://artificialanalysis.ai/evaluations/terminal-bench-science)；采集2026-11-08 |
| AA统一harness / 0.1.0 | 2 | GPT-6 Astra (Max) | 63.3 | pass@1 (%) | 0.1.0 / 70 tasks；mini-swe-agent；3 repeats/task | [待核实（网页未标各结果运行日期）](https://artificialanalysis.ai/evaluations/terminal-bench-science)；采集2026-11-08 |
| AA统一harness / 0.1.0 | 3 | Gemini 4 Carbon (Medium) | 62.4 | pass@1 (%) | 0.1.0 / 70 tasks；mini-swe-agent；3 repeats/task | [待核实（网页未标各结果运行日期）](https://artificialanalysis.ai/evaluations/terminal-bench-science)；采集2026-11-08 |

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

### 榜单覆盖边界

AA页面明确报出的前三名；官网首屏未返回CLI系统分数。固定0.1.0的70题，main86题与筹备中的2.0不参与本快照；未发现官方链接的独立arXiv论文，软件DOI不冒充论文PDF。

来源：[1](https://artificialanalysis.ai/evaluations/terminal-bench-science)（访问 2026-11-08，）

## 联系方式

### 官方公开邮箱

- stevendi@stanford.edu

来源：[1](https://terminal-bench-science.ai/run)（访问 2026-11-07，）

### 公开反馈渠道

https://github.com/harbor-framework/terminal-bench-science/issues

来源：[1](https://github.com/harbor-framework/terminal-bench-science)（访问 2026-11-08，）

### 官方社交账号

https://discord.com/invite/2Pe5uWGcV3

来源：[1](https://terminal-bench-science.ai/run)（访问 2026-11-07，）

### 联系方式/隐私原则

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

## 原始文件

### 原始PDF

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### PDF SHA-256

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### PDF字节数

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 文件夹

待核实

说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

### 其他文档

- {"type": "官方软件发布引用（非论文PDF）", "url": "https://doi.org/10.5281/zenodo.22110253"}

来源：[1](https://terminal-bench-science.ai/announcement)（访问 2026-11-07，）

### 论文原件

待核实

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-07，）

## 变更记录

最近复核
最近复核

来源：[1](https://terminal-bench-science.ai/)（访问 2026-11-08，）
