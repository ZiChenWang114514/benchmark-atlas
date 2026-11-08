# APEX-Agents

> 核验日期：2026-11-07 （）。未知保留待核实；访问日不是测量日。

已核验存在；11节研究快照；note: trending: A；未知字段保留待核实

职业服务跨应用Agent评测。论文/HF公开480题、AA452题与Mercor当前240题是不同口径；官网静态Score84.2已用页面内嵌数据核实为Pass@1，Mean Score为90.4，二者分轨。

## 基本信息

### 简称

APEX-Agents

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 全称

AI Productivity Index for Agents (APEX–Agents)

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 基准版本

待核实

> 字段状态：待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 论文版本

arXiv v3（2026-02-24 01:49:38 （））

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 发布日期

2026-01-21 02:53:44 （）（arXiv首稿；来源UTC日期为1月20日）

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 主板块

Agent

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 领域标签

- 职业服务
- 跨应用工作流
- 金融
- 公司法
- 管理咨询

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 许可证

数据卡标CC-BY 4.0，同时另写仅限评测、禁止训练/参数拟合及程序化抓取；须核对附加限制，不能只写无条件开放。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2601.14242

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 官方代码

https://github.com/Mercor-Intelligence/archipelago

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 数据地址

https://huggingface.co/datasets/mercor/apex-agents

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 官方入口

https://www.mercor.com/apex/apex-agents-leaderboard/

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 论文标题

APEX–Agents

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

## 发起与维护

### 发起方

Mercor

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 合作方

Mercor当前官网明确与Box及Harvey合作开发；专家雇主名单不自动等同合作机构。

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

### 作者

Bertie Vidgen、Austin Mann、Abby Fennelly、John Wright Stanly 等，完整名单见论文。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 维护方

Mercor

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 资助方

待核实

> 字段状态：待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

## 设计目标

### 衡量能力

长程、跨应用的投资银行、管理咨询与公司法专业服务任务。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 设计背景

以富文件工作世界减少狭窄、人工化agent任务与真实专业工作的差距。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

## 构建方式

### 题目来源

专家用5–10天构建项目世界、材料与专业交付物，再依据世界创建任务和二元rubric及gold outputs。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 出题者背景

256名专业人士，平均12.9年经验；领域为投行、咨询、公司法。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 审核流程

任务与rubric多轮审核；专家检查gold outputs与提示一致性。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 质量控制

96任务由未参与创建/审查者独立完成，发现的问题修正并推广到其余数据。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 去污染

数据只用于评测；关闭网页搜索，世界提供完成任务所需文件。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

## 数据形式

### 题量与规模

原论文v3/HF公开卡：480任务、33 worlds（三职业各160）；当前Mercor官网：240任务、31 worlds；AA独立实现：452任务。三口径并列，不能把网页差异抹平。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）；[来源3](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）；[来源4](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问2026-11-07）

### 题型

单条任务指令、多步跨应用执行；422任务返回文本，58任务创建或修改文件。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 模态

- 文本
- 电子表格
- 文档
- PDF
- 演示文稿
- 邮件/聊天/日历环境

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 语言

英语（官方HF卡Languages: English）。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 难度

专家估计任务平均1.82小时；不是模型实际运行时长。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 公开与隐藏划分

HF卡描述公开480题/全部gold、assets；当前Mercor官网又称完整题集私有、仅开放subset可复现。来源存在时点/版本差异，确切映射待核实；不下载9GB材料来猜测。

> 字段状态：待核实

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

## 评测方法

### 指标

原论文与当前官网均区分Pass@1（全部rubric通过的任务比例）及Mean Score（逐任务criterion通过比例的平均）；原论文另有Pass@8/Pass^8。官网FAQ称Mean Score为主指标，但静态HTML默认显示Pass@1，内嵌数据可核验。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

### 评分

Gemini 3 Flash low逐项独立判Met/Not met，读取提示、输出、文件改动与criterion，不读完整轨迹。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 运行设置

原论文每题8轨迹、250步；AA用452任务、每题3次、Stirrup 200轮，排除投行世界244与246。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 官方脚本

Archipelago提供执行环境、agent运行器与grading系统。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 可比性警示

原论文480题、AA452题与Mercor当前240题三轨不可直接比。官网静态HTML默认Score=84.2对应pass-1，mean-score=90.4，已由内嵌数据键消歧；FAQ仍称Mean Score主排序。n_samples不当作独立题数。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问2026-11-07）；[来源3](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 （）

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 最新版本与采用证据

```json
{
  "version": "待核实"
  "heat_confidence": "A"
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/evaluations/apex-agents-aa"
      "date": "2026-11-07"
      "note": "AA当前独立452题实现与排行榜，观察日。"
    }
  ]
}
```

> A：原始基准与独立评测材料交叉核验；不将仅引用等同独立实跑。

[来源1](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-01-21"
  }
  {
    "version": "v2"
    "submitted_at": "2026-01-28"
  }
  {
    "version": "v3"
    "submitted_at": "2026-02-24"
  }
]
```

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 饱和情况

Mercor当前Loop harness：Pass@1最高84.2%、Mean Score最高90.4%；原论文480题最高Pass@1 24.0与当前240题不是直接进步曲线，不能据不同任务池宣称饱和。

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

### 污染与争议

当前官网与HF卡在题量、worlds、私有/开放策略及主指标上不同；数据卡同时标CC-BY-4.0和禁止训练/参数拟合/自动抓取，须核对这些附加条款，不把其简化成无条件开放。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

### 版本与衍生关系

APEX是同机构基准家族；当前官网并列APEX-Agents/APEX-SWE/APEX-Accounting/APEX-1，不能因此把Agents三个职业分项重复算成独立benchmark。

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 （）

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 官方榜单

https://www.mercor.com/apex/apex-agents-leaderboard/

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）；[来源2](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）

### 第三方覆盖

https://artificialanalysis.ai/evaluations/apex-agents-aa

[来源1](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问2026-11-07）

### 分轨结果

#### Mercor当前240题/31worlds，pass-1

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (high) | 84.2 | Pass@1 (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=pass-1)，2026-11-07 |
| 2 | Gemini 4 Argon (high) | 82.4 | Pass@1 (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=pass-1)，2026-11-07 |
| 3 | Hy4 (high) | 77.6 | Pass@1 (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=pass-1)，2026-11-07 |

> Gemini 4 Carbon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 4.3, "n_samples_source": 960, "sample_count_note": "页面原字段n_samples，不等于独立任务数，不推断重复次数"}

> Gemini 4 Argon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 4.3, "n_samples_source": 954, "sample_count_note": "页面原字段n_samples，不等于独立任务数，不推断重复次数"}

> Hy4 (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 4.5, "n_samples_source": 960, "sample_count_note": "页面原字段n_samples，不等于独立任务数，不推断重复次数"}

#### Mercor当前240题/31worlds，mean-score

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (high) | 90.4 | Mean Score (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=mean-score)，2026-11-07 |
| 2 | Gemini 4 Argon (high) | 87.4 | Mean Score (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=mean-score)，2026-11-07 |
| 3 | Hy4 (high) | 85.1 | Mean Score (%) | [原表](https://www.mercor.com/apex/apex-agents-leaderboard/?pass=mean-score)，2026-11-07 |

> Gemini 4 Carbon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 3.1, "n_samples_source": 960, "sample_count_note": "页面原字段n_samples，不等于独立任务数，不推断重复次数"}

> Gemini 4 Argon (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 3.3, "n_samples_source": 954, "sample_count_note": "页面原字段n_samples，不等于独立任务数，不推断重复次数"}

> Hy4 (high)：{"harness": "loop_truncated_tools_agent", "source_error_plus_minus": 3.6, "n_samples_source": 960, "sample_count_note": "页面原字段n_samples，不等于独立任务数，不推断重复次数"}

#### Artificial Analysis独立452题

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 3.5 Flash (High) | 47.1 | pass@1 (%) | [原表](https://artificialanalysis.ai/evaluations/apex-agents-aa)，2026-11-07 |
| 2 | Qwen3.8 Max (0902) | 42.4 | pass@1 (%) | [原表](https://artificialanalysis.ai/evaluations/apex-agents-aa)，2026-11-07 |
| 3 | Kimi K3 (Max) | 41.3 | pass@1 (%) | [原表](https://artificialanalysis.ai/evaluations/apex-agents-aa)，2026-11-07 |



#### 论文v3/480题历史基线

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 3 Flash (Thinking=High) | 24.0 | Pass@1 (%) | [原表](https://arxiv.org/abs/2601.14242)，2026-11-07 |
| 2 | GPT-5.2 (Thinking=High) | 23.0 | Pass@1 (%) | [原表](https://arxiv.org/abs/2601.14242)，2026-11-07 |
| 3 | Claude Opus 4.5 (Thinking=High) | 18.4 | Pass@1 (%) | [原表](https://arxiv.org/abs/2601.14242)，2026-11-07 |



> 字段状态：待核实

> 读取官方页面内嵌__NEXT_DATA__.props.pageProps.leaderboardData，pass-1与mean-score键明确区分；原HTML默认84.2对应Pass@1，Mean Score为90.4。整体更新时间与实际运行日期待核实。

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问2026-11-07）；[来源3](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### 覆盖说明

Mercor公开页面内嵌70条模型配置，按pass-1/mean-score键及Loop harness逐项排序取前三，未猜测静态Score含义；同时单列AA452题与原论文480题。官网240/31与HF480/33及开放策略仍冲突。

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/apex-agents-aa)（访问2026-11-07）；[来源3](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

apex@mercor.com

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 公开反馈

https://github.com/Mercor-Intelligence/archipelago/issues

[来源1](https://github.com/Mercor-Intelligence/archipelago)（访问2026-11-07）

### 官方社交

待核实

> 字段状态：待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 隐私说明/政策

待核实

> 字段状态：待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2601.14242

[来源1](https://arxiv.org/abs/2601.14242)（访问2026-11-07）

### PDF SHA-256

4f253c14f71cb9a1d17c9204e5b0812f42280f867d1f189f817286029e63594a

> 实际下载字节的SHA-256；不表示已有副本已替换。

[来源1](https://arxiv.org/pdf/2601.14242)（访问2026-11-07）

### PDF字节数

1645464

[来源1](https://arxiv.org/pdf/2601.14242)（访问2026-11-07）

### 文件夹

待核实

> 字段状态：待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方介绍/协议"
    "url": "https://huggingface.co/datasets/mercor/apex-agents"
  }
]
```

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

### 论文副本

待核实

[来源1](https://huggingface.co/datasets/mercor/apex-agents)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": "（）"
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": " ()"
    最近复核
  }
]
```

[来源1](https://www.mercor.com/apex/apex-agents-leaderboard/)（访问2026-11-07）
