# OmicsBench

> Benchmark Constitution，核验 2026-11-08。未知保持“待核实”；访问日不等于实验日。

OmicsBench把组学研究中的分析依赖拆成多轮DAG任务，观察agent是否能沿前序结果推进并利用反馈纠错。带门限反馈的gated协议不是无反馈single-pass能力的替代，本页将14个模型/脚手架组合的两套论文成绩分开。

来源：[原始说明](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）；[结果证据](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

## 基本信息

### 简称

OmicsBench

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 全称

OmicsBench

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 基准版本

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 论文版本

v1；最近论文日期 2026-10-15

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 发布日期

2026-10-15（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 主板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 领域标签

- 研究规模组学多轮分析

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 许可与适用范围

Runner及全部grader为MIT；三个公开任务及答案为CC BY 4.0；所附生物数据和标识符数据库仍遵守各原始来源许可证。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）；[2](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 论文

https://arxiv.org/abs/2610.21074

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 代码仓库

https://huggingface.co/datasets/gideonshaked/OmicsBench

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 数据地址

https://huggingface.co/datasets/gideonshaked/OmicsBench

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 官方主页

https://huggingface.co/datasets/gideonshaked/OmicsBench

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 论文标题

OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

## 发起与维护

### 发起与机构归属

作者Gideon Shaked、Siddharth Nagisetty同时署名University of Michigan计算医学与生物信息学系和AfterQuery；依据作者单位归属，不推定单一发起法人。

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 合作关系

- University of Michigan, Department of Computational Medicine and Bioinformatics
- AfterQuery

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 作者

- Shaked, Gideon
- Nagisetty, Siddharth

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 当前维护方

gideonshaked/OmicsBench与grader-databases发布账号。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 资助与支持

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

## 设计目标

### 衡量能力

研究规模、长时多轮组学工作流，跨依赖子任务产出可自动检查的生物学分析。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 设计背景与适用边界

单次提示难以反映真实组学研究中逐轮委托、前序结果依赖和收到反馈后的恢复能力；本基准把研究工作流拆成DAG依赖的多轮子任务。

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

## 构建方式

### 题目或数据来源

已发表生物研究与对应公开数据集，按研究工作流拆成任务DAG。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 构建者背景

计算生物学研究生专家策划；writer/reviewer代理辅助后由人工编辑。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 审核流程

受过研究生层次计算生物学训练的人类专家选论文及数据；writer agent起草，reviewer agent审核支持性及泄漏，最多三轮修订；自动格式检查后人类复核编辑或拒绝。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 质量控制

58类确定性生物grader与实体同义词参考库；分步依赖DAG检查。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 去污染与泄漏边界

94私有任务控制答案访问，3公开任务作示例；源论文公开及grader反馈可能使记忆/奖励投机仍存在。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

## 数据形式

### 规模

97任务、662子任务、58确定性生物评分器；3公开、94私有。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 题型与交付物

长时多轮组学数据分析；有向无环依赖子任务。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 模态

组学矩阵、表格、代码、分析产物与文字结果。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 语言

任务示例和runner文档为英语，分析工具含Python/R与生物实体标识符；不推断多语覆盖率。

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）；[2](https://huggingface.co/datasets/gideonshaked/OmicsBench/raw/main/omicsbench_runner/README.md)（访问2026-11-08，）

### 难度

研究规模而非短题；依赖链及迭代分析是难点。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 公开与隐藏划分

97项任务、662个子任务；公开3项任务及答案，94项为私有测试集，需联系作者申请评测。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

## 评测方法

### 指标

任务/子任务生物grader得分；single-pass与gated两协议分开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 评分方式

58类确定性grader先给答案字段0—1分；子任务取字段均值，任务取子任务均值。single-pass无反馈；gated阈值0.7、最多3次，每轮1800秒；两种模式均记录最佳尝试。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 提示与运行设置

每轮1800秒；Docker无网络、4核、12GB内存、20GB盘；支持时reasoning high。12模型、3harness、14组合。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 评测脚本

官方HF仓库omicsbench_runner/包含runner与全部grader；安装与运行说明见omicsbench_runner/README.md。

来源：[1](https://huggingface.co/datasets/gideonshaked/OmicsBench)（访问2026-11-08，）

### 可比性提醒

模型与harness混杂；gated反馈可能导致reward hacking，因此提升可作为上界而非独立能力提升。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 数据版本与更新

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 论文修订记录

```json
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.21074v1"
      "date": "2026-10-15"
      "note": "OmicsBench 原始论文于H2发布并评测研究规模、多轮组学数据分析Agent。"
    }
  ]
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。"
  "paper_metadata": {
    "title": "OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics"
    "authors": [
      "Shaked, Gideon"
      "Nagisetty, Siddharth"
    ]
    "release": "2026-10-15"
    "latest": "2026-10-15"
    "version": "v1"
  }
}
```

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）；[2](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 饱和程度

原论文12个模型、3种harness的实验中，最佳Opus 5/OpenCode为single-pass 0.57、gated 0.67；作者认为未饱和。这是论文判断，不是实时榜单结论。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 争议与已知问题

94项私有测试防止公开答案暴露；gated反馈允许猜测或调整阈值造成reward hacking，增益是反馈作用的上界；模型与harness效果未完全解耦；失败分析judge未与人工标注验证。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07，）

### 衍生与后续使用

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

## 榜单快照

### 快照访问日期

2026-11-08 （网页访问日期；历史结果日期分别保留）

来源：[1](https://huggingface.co/datasets/gideonshaked/OmicsBench)（访问2026-11-08，）

### 官方结果入口

https://huggingface.co/datasets/gideonshaked/OmicsBench

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 第三方入口

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 分赛道结果

- {"model": "Opus 5", "score": 0.57, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.56, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 2}
- {"model": "Grok 4.6", "score": 0.55, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 3}
- {"model": "Muse-Spark 1.1", "score": 0.54, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 4}
- {"model": "Kimi K3", "score": 0.49, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 5}
- {"model": "GLM-5.2", "score": 0.48, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 6}
- {"model": "Qwen3.8-Max", "score": 0.48, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 6}
- {"model": "Gemini 3.1 Pro", "score": 0.47, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 8}
- {"model": "MiniMax-M3", "score": 0.46, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 9}
- {"model": "DeepSeek-V4-Pro", "score": 0.45, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 10}
- {"model": "Qwen3.7-Max", "score": 0.44, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 11}
- {"model": "Grok 4.3", "score": 0.43, "track": "原论文v1/OpenCode/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 12}
- {"model": "Opus 5", "score": 0.67, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.66, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 2}
- {"model": "Grok 4.6", "score": 0.66, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 2}
- {"model": "Muse-Spark 1.1", "score": 0.63, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 4}
- {"model": "Kimi K3", "score": 0.59, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 5}
- {"model": "GLM-5.2", "score": 0.59, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 5}
- {"model": "Qwen3.8-Max", "score": 0.59, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 5}
- {"model": "Gemini 3.1 Pro", "score": 0.58, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 8}
- {"model": "MiniMax-M3", "score": 0.58, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 8}
- {"model": "DeepSeek-V4-Pro", "score": 0.58, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 8}
- {"model": "Qwen3.7-Max", "score": 0.56, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 11}
- {"model": "Grok 4.3", "score": 0.54, "track": "原论文v1/OpenCode/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "OpenCode", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 12}
- {"model": "Opus 5", "score": 0.56, "track": "原论文v1/Claude Code/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Claude Code", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 1}
- {"model": "Opus 5", "score": 0.66, "track": "原论文v1/Claude Code/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Claude Code", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.55, "track": "原论文v1/Codex/single-pass", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Codex", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 1}
- {"model": "GPT-5.6 Sol", "score": 0.67, "track": "原论文v1/Codex/gated", "metric": "Mean task score (0–1)", "source_url": "https://arxiv.org/pdf/2610.21074", "collected_at": "2026-11-08 ", "harness": "Codex", "runs_per_task": 3, "result_type": "论文Figure4A标出的精确两位小数；已逐数视觉核对，未从柱高估值", "rank": 1}

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 覆盖边界

完整转录论文Figure4A的14个model/harness组合×两协议=28个公布数字，PDF图中文字逐项视觉校核，不从柱高估计。OpenCode/ClaudeCode/Codex和single-pass/gated分别成轨，原论文12模型14组合；无独立动态现榜，所有分数是论文历史结果。

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

## 联系方式

### 公开项目邮箱

- gshaked@umich.edu

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 公开反馈渠道

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 官方社交渠道

待核实

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 联系方式收录原则

Benchmark Constitution仅收录论文/官方站公开的项目联系渠道，不收集私人信息；这不是对外站隐私政策的认证。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-08，）

## 原始文件

### 既存论文原件

```json
{
  "id": "1MBjoelJtmqKWsHEhAC4vwW6VbwC4iX6G"
  "webViewLink": "
}
```

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 原始PDF地址

https://arxiv.org/pdf/2610.21074

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 下载SHA-256

34555d4ef285b66a95fc368bc903980f44d436e0de2987992bc3729a7f4f0171

说明：2026-11-08 下载字节的校验；没有覆盖或上传，不能据此认定既存原件同版本。

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 下载字节数

```json
1891438
```

来源：[1](https://arxiv.org/pdf/2610.21074)（访问2026-11-08，）

### 既存文件夹

```json
{
  "id": "1xJuAwVBG1yPF04Nbzc7zU3ba0C80UKaf"
  "webViewLink": "
}
```

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）

### 其他文档

- {"type": "中文介绍", "id": "1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto", "webViewLink": "https://docs.google.com/document/d/1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto/edit"}

来源：[1](https://docs.google.com/document/d/1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto/edit)（访问2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://arxiv.org/abs/2610.21074)（访问2026-11-08，）
