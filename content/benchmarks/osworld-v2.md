# OSWorld 2.1

> Benchmark Constitution · 本轮核验 2026-11-08 KST（Asia/Seoul）。未知保持“待核实”；访问日不等于实验日。

OSWorld2.x测量在虚拟桌面和自托管网站中完成长程真实工作流的能力，重点是跨应用约束和状态恢复，而非孤立GUI点击。本页明确区分论文2.0、推荐环境2.1、全集/离线集及二元/部分完成指标。

来源：[原始说明](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）；[结果证据](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10)（访问2026-11-08，KST）；[结果证据](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07，KST）

## 基本信息

### 简称

OSWorld 2.1

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 全称

OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks（当前推荐发布 osworld-v2.1）

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）；[2](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 基准版本

osworld-v2.1（2026-09-16 发布的 bug-fix 版本，官方推荐）；历史发布 osworld-v2-2026.08.08、osworld-v2-2026.06.24 仍为 Active

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 论文版本

arXiv v2（2026-07-13修订；与osworld-v2.1环境版本不同）

来源：[1](https://arxiv.org/abs/2606.29537)（访问2026-11-08，KST）

### 发布日期

2026-06-26（论文、环境与 osworld-v2-2026.06.24 首发）；osworld-v2.1 于 2026-09-16 发布

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 主板块

Agent

说明：Benchmark Constitution 编辑归档。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 领域标签

- 计算机使用
- 长程桌面工作流

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 许可与适用范围

Apache-2.0（代码仓库）

说明：任务类与完整资产经 Hugging Face gated 数据集分发，数据许可另行待核实。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 论文

https://arxiv.org/abs/2606.29537

来源：[1](https://arxiv.org/abs/2606.29537)（访问2026-11-08，KST）；[2](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 代码仓库

https://github.com/xlang-ai/OSWorld-V2

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 数据地址

https://huggingface.co/datasets/xlangai/osworld_v2_tasks

说明：gated；完整资产 xlangai/osworld_v2_assets_gated。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 官方主页

https://osworld-v2.xlang.ai

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）；[2](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 论文标题

OSWorld 2.0: Benchmarking Computer-Use Agents on Long-Horizon Real-World Tasks

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

## 发起与维护

### 发起与机构归属

XLANG Lab, University of Hong Kong

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 合作关系

UCSD、Columbia、UCSB、Mila、Uniphore、Snorkel AI、UW-Madison、Alibaba Qwen、Ohio State、Simular、NeoCognition（作者单位）

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 作者

Mengqi Yuan、Zilong Zhou、Xinzhuang Xiong（共同一作）等，通讯/末位含 Tianbao Xie、Tao Yu

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 当前维护方

xlang-ai（GitHub 组织）

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 资助与支持

Google Research gift fund提供支持；Snorkel AI为论文致谢列出的research & data partner。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

## 设计目标

### 衡量能力

真实端到端长程计算机使用：跨来源推理、视觉空间精度、隐式状态推断、多项状态追踪、冲突消歧、多模态编辑、教程跟随等。

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 设计背景与适用边界

OSWorld1.0等短程桌面动作评测不足以测量跨应用状态、任务中途新信息、隐含约束和最终交付验证；2.x把完整长期工作流而非孤立点击设为评价单位。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

## 构建方式

### 题目或数据来源

基于真实输入材料构建工作流，并与有状态的用户档案数据交叉引用；使用31个自托管模拟网站及自托管 GitLab。

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 构建者背景

XLANG与合作团队共同设计；论文附录A列Mengqi Yuan负责设计/标注，Zilong Zhou和Xinzhuang Xiong参与任务复核，Tao Yu发起并指导。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

### 审核流程

编码agent先生成rubric单元测试；两位独立人类标注员端到端完成并互查可解性和权重；多种前沿agent轨迹检查遗漏。各阶段有分歧就修订，无法消除歧义或不可行的任务删除。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

### 质量控制

手工、对抗测试及轨迹审计同时检查reward hacking和正确答案误扣分；模型裁判仅占总分11.53%，每题不超过50%，用标注正确/混淆错误状态验证。发布时锁定代码、任务、资产、网站与VM镜像。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）；[2](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 去污染与泄漏边界

官方任务类通过 gated HF 数据集分发而不放在公开 GitHub，以减少泄漏、防止被评 agent 在线查到答案或评估器细节。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

## 数据形式

### 规模

108 个长程任务，覆盖7个专业领域、21个子类；平均27.25个评分检查点；69.6%任务人类耗时超过1小时

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 题型与交付物

交互式桌面/网页工作流任务（agent 在虚拟机中操作）

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 模态

- 屏幕图像
- 文本
- 文件/多媒体

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 语言

公开论文的任务说明/示例为英语，涉及多种应用与原始文件；不据此声称所有文件仅为单一语言。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

### 难度

人类中位约1.6小时；平均 agent 步数 >250

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 公开与隐藏划分

另有 Offline set（官网图表区分 Full set / Offline set）；任务类为 gated 公开（自动审批）

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）；[2](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

## 评测方法

### 指标

主指标为 500 步内的二元完成率（Binary reward），并报告部分得分（Partial reward）

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 评分方式

每任务多检查点评分（平均27.25个），二元完成要求全部满足。

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 提示与运行设置

官方图表以500步为默认预算，记录reasoning effort及batch/single tool设置；历史100/300/500步实验分开。按推荐2.1 release同时锁定网站、任务、资产、镜像；不是统一通用CoT提示。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）；[2](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10)（访问2026-11-08，KST）；[3](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）；[4](https://raw.githubusercontent.com/xlang-ai/OSWorld-V2/main/docs/PUBLIC_EVALUATION_GUIDELINE_v2.1.md)（访问2026-11-08，KST）

### 评测脚本

仓库提供 run.py / main.py / show_result.py 等运行与汇总脚本，以及 setup-osworld skill

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 可比性提醒

2.0/2.1 与 OSWorld 1.0 不可直接比较；Full 与 Offline 子集不可混比；厂商报告的“offline subset”分数不同于全集；须同一发布版本。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）；[2](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07，KST）

## 最新情况

### 核验日期

2026-11-08 KST（Asia/Seoul）

来源：[1](https://arxiv.org/abs/2606.29537)（访问2026-11-08，KST）

### 数据版本与更新

```json
{
  "version": "osworld-v2.1（2026-09-16 发布的 bug-fix 版本，官方推荐）；历史发布 osworld-v2-2026.08.08、osworld-v2-2026.06.24 仍为 Active",
  "evidence_2026_h2": [
    {
      "url": "https://openai.com/index/introducing-gpt-6-1-terra/",
      "date": "2026-11-07",
      "organization": "OpenAI",
      "note": "GPT-6.1 Terra发布文用OSWorld 2.1比较多步骤桌面操作。"
    },
    {
      "url": "https://www.anthropic.com/claude-haiku-5-5",
      "date": "2026-10-07",
      "organization": "Anthropic",
      "note": "10月7日Haiku发布表和成本图报告OSWorld 2.1 offline subset。"
    },
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks",
      "date": "2026-09-28",
      "organization": "Epoch AI",
      "note": "Epoch 9月28日评审OSWorld 2.1为Flawed。"
    }
  ],
  "trending": {
    "heat_confidence": "A",
    "summary": "9月发布的长程桌面任务同时出现在 OpenAI 与 Anthropic 10–11 月模型发布比较中，Epoch AI 亦有评审。"
  }
}
```

说明：近期热门证据取自候选研究与本轮重开页面；A级：多家前沿实验室或评测机构独立采用。

来源：[1](https://openai.com/index/introducing-gpt-6-1-terra/)（访问2026-11-07，KST）；[2](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07，KST）；[3](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07，KST）

### 论文修订记录

```json
{
  "arxiv": [
    {
      "version": "v1",
      "submitted_at": "2026-06-29T02:59:17+09:00 KST"
    },
    {
      "version": "v2",
      "submitted_at": "2026-07-13T19:30:17+09:00 KST"
    }
  ],
  "benchmark_release_note": "论文首投与v2修订见arXiv:2606.29537；环境发布另为2026-06-26首发、2026-08-08更新、2026-09-16 osworld-v2.1。论文版本不能替代环境版本。"
}
```

来源：[1](https://arxiv.org/abs/2606.29537)（访问2026-11-08，KST）

### 饱和程度

官方数据v2.1/full/500步/e2e最高已录配置为Claude Opus 5（max，batch tool）44.33%；不能用offline厂商高分宣称全集饱和。

来源：[1](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10)（访问2026-11-08，KST）

### 争议与已知问题

Epoch AI 2026-09-28 将 OSWorld 2.1 评为 Flawed（据候选研究证据）；具体缺陷描述待核实。

来源：[1](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07，KST）

### 衍生与后续使用

前身 OSWorld 1.0（xlang-ai/OSWorld）；本条目只记录 2.x 系列。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

## 榜单快照

### 快照访问日期

2026-11-08 KST（网页访问日期；历史结果日期分别保留）

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 官方结果入口

https://osworld-v2.xlang.ai

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 第三方入口

https://www.anthropic.com/claude-haiku-5-5

来源：[1](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07，KST）

### 分赛道结果

- {"model": "Claude Opus 5", "score": 44.33, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "MuseSpark 1.3", "score": 39.25, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.3-1015-merged-106tasks.zip", "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 36.89, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 33.33, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 33.01, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 18.81, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "MuseSpark 1.2", "score": 15.84, "track": "官方图表/v2.1/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.2-1015-merged-105tasks.zip", "binary_success_threshold": null, "rank": 7}
- {"model": "Claude Opus 5", "score": 77.67, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 73.11, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "MuseSpark 1.3", "score": 69.56, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.3-1015-merged-106tasks.zip", "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 68.92, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 64.85, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 59.09, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "MuseSpark 1.2", "score": 44.08, "track": "官方图表/v2.1/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/xlangai/osworld2.0-trajectory/blob/main/v2.1-muse_spark_1.2-1015-merged-105tasks.zip", "binary_success_threshold": null, "rank": 7}
- {"model": "Claude Opus 5", "score": 48.65, "track": "官方图表/v2.1/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 39.74, "track": "官方图表/v2.1/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 37.18, "track": "官方图表/v2.1/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 34.67, "track": "官方图表/v2.1/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 22.08, "track": "官方图表/v2.1/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 79.2, "track": "官方图表/v2.1/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 72.03, "track": "官方图表/v2.1/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 70.55, "track": "官方图表/v2.1/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 5", "score": 66.25, "track": "官方图表/v2.1/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 60.34, "track": "官方图表/v2.1/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 31.43, "track": "官方图表/v2026.08.08/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 30.21, "track": "官方图表/v2026.08.08/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 28.98, "track": "官方图表/v2026.08.08/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 27.34, "track": "官方图表/v2026.08.08/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 25.33, "track": "官方图表/v2026.08.08/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 22.32, "track": "官方图表/v2026.08.08/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 5", "score": 68.31, "track": "官方图表/v2026.08.08/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 67.67, "track": "官方图表/v2026.08.08/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 63.79, "track": "官方图表/v2026.08.08/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 62.72, "track": "官方图表/v2026.08.08/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 60.49, "track": "官方图表/v2026.08.08/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 54.89, "track": "官方图表/v2026.08.08/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 5", "score": 34.72, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 33.38, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 32.69, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 28.1, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 5", "score": 27.13, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "GPT-5.6 Sol", "score": 24.63, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 5", "score": 24.61, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "GPT-5.6 Sol", "score": 20, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "GPT-5.6 Sol", "score": 17.56, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 9}
- {"model": "GPT-5.6 Sol", "score": 7.32, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "GPT-5.6 Sol", "score": 3.41, "track": "官方图表/v2026.08.08/offline/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "none", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 11}
- {"model": "Claude Opus 5", "score": 70.19, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 5", "score": 70.14, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 5", "score": 65.92, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "GPT-5.6 Sol", "score": 64.13, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "max", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "GPT-5.6 Sol", "score": 60.6, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Opus 5", "score": 60.26, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "GPT-5.6 Sol", "score": 56.03, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "high", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "Claude Opus 5", "score": 55.22, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "GPT-5.6 Sol", "score": 49.01, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "medium", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 9}
- {"model": "GPT-5.6 Sol", "score": 29.63, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "low", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "GPT-5.6 Sol", "score": 16.43, "track": "官方图表/v2026.08.08/offline/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "offline", "step_budget": 500, "reasoning": "none", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 11}
- {"model": "Claude Opus 4.8", "score": 20.6, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.8", "score": 18.52, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 4.7", "score": 18.2, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 4.7", "score": 13.9, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "GPT-5.5", "score": 13.0, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Sonnet 4.6", "score": 9.3, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Sonnet 4.6", "score": 8.3, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "MiniMax M3", "score": 4.6, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "Kimi 2.6", "score": 4.6, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "Qwen 3.7-Plus", "score": 2.8, "track": "官方图表/v2026.06.24/full/500步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "thinking", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "Claude Opus 4.8", "score": 54.8, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "GPT-5.5", "score": 49.5, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Opus 4.8", "score": 49.33, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Opus 4.7", "score": 49.1, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Claude Opus 4.7", "score": 48.91, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "batched tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Claude Sonnet 4.6", "score": 41.5, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Sonnet 4.6", "score": 33.9, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "medium", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "MiniMax M3", "score": 22.3, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 8}
- {"model": "Kimi 2.6", "score": 22.1, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 9}
- {"model": "Qwen 3.7-Plus", "score": 21.5, "track": "官方图表/v2026.06.24/full/500步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 500, "reasoning": "thinking", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 10}
- {"model": "GPT-5.5", "score": 13.0, "track": "官方图表/v2026.06.24/full/150步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.7", "score": 4.6, "track": "官方图表/v2026.06.24/full/150步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 4.6, "track": "官方图表/v2026.06.24/full/150步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "medium", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 4.6, "track": "官方图表/v2026.06.24/full/150步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "MiniMax M3", "score": 1.9, "track": "官方图表/v2026.06.24/full/150步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Kimi 2.6", "score": 1.9, "track": "官方图表/v2026.06.24/full/150步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "GPT-5.5", "score": 46.7, "track": "官方图表/v2026.06.24/full/150步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.7", "score": 20.3, "track": "官方图表/v2026.06.24/full/150步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 20.0, "track": "官方图表/v2026.06.24/full/150步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Sonnet 4.6", "score": 14.2, "track": "官方图表/v2026.06.24/full/150步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "medium", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "MiniMax M3", "score": 8.2, "track": "官方图表/v2026.06.24/full/150步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Kimi 2.6", "score": 7.1, "track": "官方图表/v2026.06.24/full/150步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 150, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Claude Opus 4.7", "score": 13.0, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "GPT-5.5", "score": 13.0, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Sonnet 4.6", "score": 8.3, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "medium", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Sonnet 4.6", "score": 6.5, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Kimi 2.6", "score": 4.6, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "MiniMax M3", "score": 3.7, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 6}
- {"model": "Qwen 3.7-Plus", "score": 1.9, "track": "官方图表/v2026.06.24/full/300步/e2e/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "thinking", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "GPT-5.5", "score": 49.5, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "xhigh", "tool_setting": "batch tool", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 1}
- {"model": "Claude Opus 4.7", "score": 39.8, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 2}
- {"model": "Claude Sonnet 4.6", "score": 35.8, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "max", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 3}
- {"model": "Claude Sonnet 4.6", "score": 29.4, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "medium", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 4}
- {"model": "Qwen 3.7-Plus", "score": 16.6, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "thinking", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "MiniMax M3", "score": 16.6, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 5}
- {"model": "Kimi 2.6", "score": 14.4, "track": "官方图表/v2026.06.24/full/300步/e2e/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.06.24", "dataset_scope": "full", "step_budget": 300, "reasoning": "enabled", "tool_setting": "standard", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "e2e", "official_flag": true, "trajectory_url": null, "binary_success_threshold": null, "rank": 7}
- {"model": "Sai w/ Claude Opus 5", "score": 41.67, "track": "官方图表/v2.1/full/500步/agent/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/simular-ai/sai-osworld-v21-reference-runs", "binary_success_threshold": null, "rank": 1}
- {"model": "Sai w/ Claude Opus 5", "score": 79.38, "track": "官方图表/v2.1/full/500步/agent/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 500, "reasoning": "max", "tool_setting": "", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/simular-ai/sai-osworld-v21-reference-runs", "binary_success_threshold": null, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 37.65, "track": "官方图表/v2026.08.08/full/450步/agent/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v0808_20260915", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 66.62, "track": "官方图表/v2026.08.08/full/450步/agent/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2026.08.08", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v0808_20260915", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 44.44, "track": "官方图表/v2.1/full/450步/agent/Binary accuracy (%)", "metric": "Binary accuracy (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v21_20261012", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Darwinx w/ Claude Opus 4.8", "score": 75.97, "track": "官方图表/v2.1/full/450步/agent/Partial score (%)", "metric": "Partial score (%)", "source_url": "https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10", "collected_at": "2026-11-08 KST", "release": "v2.1", "dataset_scope": "full", "step_budget": 450, "reasoning": "max (thinking disabled)", "tool_setting": "", "result_type": "官方图表数据；不与厂商自报混排", "source_date": "2026-10-15", "model_type": "agent", "official_flag": null, "trajectory_url": "https://huggingface.co/datasets/LoyoTheNerd/darwinx_v21_20261012", "binary_success_threshold": 0.99, "rank": 1}
- {"model": "Claude Sonnet 5.5", "score": 83.9, "metric": "OSWorld 2.1 offline subset accuracy（厂商自报）", "result_type": "厂商发布页自报（非官方榜）", "source_date": "2026-10-07", "collected_at": "2026-11-07 KST（历史已存证据；本轮未重开）", "track": "Anthropic厂商自报/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 1}
- {"model": "Claude Haiku 5.5", "score": 72.4, "metric": "OSWorld 2.1 offline subset accuracy（厂商自报）", "result_type": "厂商发布页自报（非官方榜）", "source_date": "2026-10-07", "collected_at": "2026-11-07 KST（历史已存证据；本轮未重开）", "track": "Anthropic厂商自报/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 2}
- {"model": "GPT-6 Luna", "score": 48.9, "metric": "OSWorld 2.1 offline subset accuracy（厂商自报）", "result_type": "厂商发布页自报（非官方榜）", "source_date": "2026-10-07", "collected_at": "2026-11-07 KST（历史已存证据；本轮未重开）", "track": "Anthropic厂商自报/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 3}
- {"model": "Claude Haiku 4.5", "score": 15.7, "metric": "OSWorld 2.1 offline subset accuracy（厂商自报）", "result_type": "厂商发布页自报（非官方榜）", "source_date": "2026-10-07", "collected_at": "2026-11-07 KST（历史已存证据；本轮未重开）", "track": "Anthropic厂商自报/OSWorld2.1/offline subset", "source_url": "https://www.anthropic.com/claude-haiku-5-5", "rank": 4}

来源：[1](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10)（访问2026-11-08，KST）；[2](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07，KST）

### 覆盖边界

本轮从官网脚本找到公开official-results.json（updatedAt=2026-10-15），完整收录所有结果并按release、full/offline、步数、agent类别及binary/partial指标分赛道。JSON未显式release/scope的行仅使用文件声明的默认值；名次按同赛道公布点值计算。保留前轮Anthropic自报作为单独历史来源，访问日期不冒改。

来源：[1](https://osworld-v2.xlang.ai/static/data/leaderboard/official-results.json?v=leaderboard-musespark-v10)（访问2026-11-08，KST）

## 联系方式

### 公开项目邮箱

- yuanmengqi732@gmail.com
- zzl0712@connect.hku.hk

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 公开反馈渠道

https://github.com/xlang-ai/OSWorld-V2/issues

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 官方社交渠道

- https://x.com/XLangNLP/status/2070517498974253269
- https://discord.com/invite/4Gnw7eTEZR

来源：[1](https://osworld-v2.xlang.ai)（访问2026-11-08，KST）

### 联系方式收录原则

Benchmark Constitution仅收录论文/官方站公开的项目联系渠道，不收集私人信息；这不是对外站隐私政策的认证。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-08，KST）

## 原始文件

### 既存Drive论文原件

待核实

说明：本组按任务要求不上传Drive；原始PDF URL见original_files。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 原始PDF地址

https://arxiv.org/pdf/2606.29537

来源：[1](https://arxiv.org/abs/2606.29537)（访问2026-11-08，KST）

### 本轮下载SHA-256

a1e4d52bbf3a5fae8e3153835adcfd5f314efc45bbc8e9e73b19bcbf20d3fefc

说明：2026-11-08 KST本轮下载字节的校验；没有覆盖或上传Drive，不能据此认定既存Drive原件同版本。

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

### 本轮下载字节数

```json
25962973
```

来源：[1](https://arxiv.org/pdf/2606.29537)（访问2026-11-08，KST）

### 既存Drive文件夹

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

### 其他文档

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://github.com/xlang-ai/OSWorld-V2)（访问2026-11-08，KST）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。"}
- {"date": "2026-11-08", "timezone": "Asia/Seoul", "change": "第2轮逐档深核：重开原论文/官方README、许可和数据卡，细化构建与评测边界，补可读官方结果分轨；保留未知、冲突及历史来源日期。"}

来源：[1](https://arxiv.org/abs/2606.29537)（访问2026-11-08，KST）
