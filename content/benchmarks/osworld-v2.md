# OSWorld 2.1

> 近期热门批次核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未核实不等于官方未公开。已核验存在；近期热门新建条目，未核实字段保留标记；trending: A

原始论文 PDF：https://github.com/xlang-ai/OSWorld-V2/raw/main/OSWorld2.0.pdf

## 为什么近期热门

OSWorld 2.x 是 2026 下半年前沿模型发布中最常见的计算机使用指标之一，OpenAI、Anthropic 发布页均直接报告，Epoch AI 也做了独立评审。

- 2026-11-07 · OpenAI：GPT-6.1 Terra发布文用OSWorld 2.1比较多步骤桌面操作。（[链接](https://openai.com/index/introducing-gpt-6-1-terra/)）
- 2026-10-07 · Anthropic：10月7日Haiku发布表和成本图报告OSWorld 2.1 offline subset。（[链接](https://www.anthropic.com/claude-haiku-5-5)）
- 2026-09-28 · Epoch AI：Epoch 9月28日评审OSWorld 2.1为Flawed。（[链接](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)）

热度等级：**trending: A**。

## 基本信息

### 简称

OSWorld 2.1

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 全称

OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks（当前推荐发布 osworld-v2.1）

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）；[来源2](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 基准版本

osworld-v2.1（2026-09-16 发布的 bug-fix 版本，官方推荐）；历史发布 osworld-v2-2026.08.08、osworld-v2-2026.06.24 仍为 Active

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 论文版本

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 发布日期

2026-06-26（论文、环境与 osworld-v2-2026.06.24 首发）；osworld-v2.1 于 2026-09-16 发布

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 领域标签

- 计算机使用
- 长程桌面工作流

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 许可证

Apache-2.0（代码仓库）

> 任务类与完整资产经 Hugging Face gated 数据集分发，数据许可另行待核实。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 论文

https://github.com/xlang-ai/OSWorld-V2/blob/main/OSWorld2.0.pdf

> 仓库根目录含 OSWorld2.0.pdf 与 paper.pdf；arXiv 编号待核实。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 官方代码

https://github.com/xlang-ai/OSWorld-V2

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/xlangai/osworld_v2_tasks

> gated；完整资产 xlangai/osworld_v2_assets_gated。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 官方入口

https://osworld-v2.xlang.ai

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）；[来源2](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 论文标题

OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

XLANG Lab, University of Hong Kong

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 合作方

UCSD、Columbia、UCSB、Mila、Uniphore、Snorkel AI、UW-Madison、Alibaba Qwen、Ohio State、Simular、NeoCognition（作者单位）

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 作者

Mengqi Yuan、Zilong Zhou、Xinzhuang Xiong（共同一作）等，通讯/末位含 Tianbao Xie、Tao Yu

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 当前维护方

xlang-ai（GitHub 组织）

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

## 设计目标

### 衡量能力

真实端到端长程计算机使用：跨来源推理、视觉空间精度、隐式状态推断、多项状态追踪、冲突消歧、多模态编辑、教程跟随等。

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 设计背景

现有计算机使用基准缺乏真实性、复杂度和长程性；OSWorld 2.0 单任务人类中位约1.6小时，Claude Opus 4.7 平均需318次工具调用，而 OSWorld 1.0 约30次。

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

## 构建方式

### 题目来源

基于真实输入材料构建工作流，并与有状态的用户档案数据交叉引用；使用31个自托管模拟网站及自托管 GitLab。

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 出题者背景

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 审核流程

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 质量控制

以发布版本固定代码、任务文件、资产、网站与镜像，禁止混用版本；另附安全报告审计安全敏感执行。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）；[来源2](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 去污染

官方任务类通过 gated HF 数据集分发而不放在公开 GitHub，以减少泄漏、防止被评 agent 在线查到答案或评估器细节。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

## 数据形式

### 题量与规模

108 个长程任务，覆盖7个专业领域、21个子类；平均27.25个评分检查点；69.6%任务人类耗时超过1小时

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 题型

交互式桌面/网页工作流任务（agent 在虚拟机中操作）

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 模态

- 屏幕图像
- 文本
- 文件/多媒体

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 语言

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 难度

人类中位约1.6小时；平均 agent 步数 >250

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 公开与隐藏划分

另有 Offline set（官网图表区分 Full set / Offline set）；任务类为 gated 公开（自动审批）

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）；[来源2](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

## 评测方法

### 指标

主指标为 500 步内的二元完成率（Binary reward），并报告部分得分（Partial reward）

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 评分

每任务多检查点评分（平均27.25个），二元完成要求全部满足。

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 提示与运行设置

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 官方评测脚本

仓库提供 run.py / main.py / show_result.py 等运行与汇总脚本，以及 setup-osworld skill

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 可比性警示

2.0/2.1 与 OSWorld 1.0 不可直接比较；Full 与 Offline 子集不可混比；厂商报告的“offline subset”分数不同于全集；须同一发布版本。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）；[来源2](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 当前版本与2026年后半年活跃证据

- **version**：osworld-v2.1（2026-09-16 发布的 bug-fix 版本，官方推荐）；历史发布 osworld-v2-2026.08.08、osworld-v2-2026.06.24 仍为 Active
- **evidence_2026_h2**：- **url**：https://openai.com/index/introducing-gpt-6-1-terra/
- **date**：2026-11-07
- **organization**：OpenAI
- **note**：GPT-6.1 Terra发布文用OSWorld 2.1比较多步骤桌面操作。

- **url**：https://www.anthropic.com/claude-haiku-5-5
- **date**：2026-10-07
- **organization**：Anthropic
- **note**：10月7日Haiku发布表和成本图报告OSWorld 2.1 offline subset。

- **url**：https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks
- **date**：2026-09-28
- **organization**：Epoch AI
- **note**：Epoch 9月28日评审OSWorld 2.1为Flawed。
- **trending**：- **heat_confidence**：A
- **summary**：9月发布的长程桌面任务同时出现在 OpenAI 与 Anthropic 10–11 月模型发布比较中，Epoch AI 亦有评审。

> 近期热门证据取自候选研究与本轮重开页面；A级：多家前沿实验室或评测机构独立采用。

[来源1](https://openai.com/index/introducing-gpt-6-1-terra/)（访问 2026-11-07）；[来源2](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）；[来源3](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 论文修订历史

2026-06-26 首发 → 2026-08-08 发布 → 2026-09-16 osworld-v2.1；2026-09-08 起不再托管 06.24 版网站

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 污染与争议

Epoch AI 2026-09-28 将 OSWorld 2.1 评为 Flawed（据候选研究证据）；具体缺陷描述待核实。

[来源1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 衍生与版本关系

前身 OSWorld 1.0（xlang-ai/OSWorld）；本条目只记录 2.x 系列。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 官方榜单

https://osworld-v2.xlang.ai

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 独立评测覆盖

https://www.anthropic.com/claude-haiku-5-5

[来源1](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：Claude Sonnet 5.5
- **score**：83.9%
- **metric**：OSWorld 2.1 offline subset accuracy（厂商自报）
- **result_type**：厂商发布页自报（非官方榜）
- **source_date**：2026-10-07
- **collected_at**：2026-11-07 KST

- **rank**：2
- **model**：Claude Haiku 5.5
- **score**：72.4%
- **metric**：OSWorld 2.1 offline subset accuracy（厂商自报）
- **result_type**：厂商发布页自报（非官方榜）
- **source_date**：2026-10-07
- **collected_at**：2026-11-07 KST

- **rank**：3
- **model**：GPT-6 Luna
- **score**：48.9%
- **metric**：OSWorld 2.1 offline subset accuracy（厂商自报）
- **result_type**：厂商发布页自报（非官方榜）
- **source_date**：2026-10-07
- **collected_at**：2026-11-07 KST

- **rank**：4
- **model**：Claude Haiku 4.5
- **score**：15.7%
- **metric**：OSWorld 2.1 offline subset accuracy（厂商自报）
- **result_type**：厂商发布页自报（非官方榜）
- **source_date**：2026-10-07
- **collected_at**：2026-11-07 KST

> 仅为 Anthropic 发布表中列出的4个模型，rank 为本表内排序，不代表全局名次。

[来源1](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）

### 覆盖与时效说明

官网榜单为动态图表，本轮未抓到结构化名次；下列为 Anthropic 2026-10-07 发布页自报的 offline subset 数据，属厂商自报，不是官方全集榜。论文首发时 Claude Opus 4.8 二元完成率20.6%、部分得分54.8%。

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）；[来源2](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 公开反馈

https://github.com/xlang-ai/OSWorld-V2/issues

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 官方社交渠道

官网链接 Twitter 与 Discord（具体账号待核实）

[来源1](https://osworld-v2.xlang.ai)（访问 2026-11-07）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://github.com/xlang-ai/OSWorld-V2/raw/main/OSWorld2.0.pdf

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### 其他文档

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组按任务要求不上传Drive；原始PDF URL见original_files。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

## 变更记录

### changelog

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。

[来源1](https://github.com/xlang-ai/OSWorld-V2)（访问 2026-11-07）

