# HumanEvalFix

> Benchmark Constitution｜逐源深度核查：2026-11-08。采集日期不代表实验日期；待核实不等于未公开。

HumanEvalFix在HumanEvalPack六种语言参考程序上人工加入功能错误，要求通过测试修复。相同164个原题跨语言改写不能视为984个独立知识问题；补回原论文按语言的FixTests精确基线，与FixDocs及后续相对提升实验分开。

导读依据：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-08）；[2](https://github.com/bigcode-project/octopack)（访问 2026-11-08）；[3](https://huggingface.co/datasets/bigcode/humanevalpack)（访问 2026-11-08）。

## 基本信息

### 简称

HumanEvalFix

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 全称

HumanEvalFix

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 基准版本

HumanEvalPack 中的 HumanEvalFix；6语言×164题

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-08）。

### 发布日期

2023-08-14（arXiv初稿日期，不是数据集的单独发布日）

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-08）。

### 主板块

代码

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 领域

```json
[
  "代码修复"
]
```

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 许可与使用范围

MIT；OctoPack官方明确将HumanEvalPack和全部代码纳入本仓库MIT许可，而非只标代码。CommitPack/CommitPackFT样本另有原仓库许可，不应混用。

来源：[1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07）。

### 论文入口

https://arxiv.org/abs/2308.07124

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 官方代码

https://github.com/bigcode-project/octopack

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 数据入口

https://huggingface.co/datasets/bigcode/humanevalpack

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 官方主页

https://github.com/bigcode-project/octopack

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 论文标题

OctoPack: Instruction Tuning Code Large Language Models

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

## 发起与维护

### 发起方

BigCode / OctoPack 作者团队

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 合作与作者单位

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 作者

```json
[
  "Muennighoff, Niklas"
  "Liu, Qian"
  "Zebaze, Armel"
  "Zheng, Qinkai"
  "Hui, Binyuan"
  "Zhuo, Terry Yue"
  "Singh, Swayam"
  "Tang, Xiangru"
  "von Werra, Leandro"
  "Longpre, Shayne"
]
```

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 维护方

BigCode octopack 项目

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 资助与资源支持

论文致谢Hugging Face提供计算实例；这证明算力支持，不推断未列明的现金资助金额。

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）。

## 设计目标

### 测量能力

根据任务规范和已有带错误的程序修复功能错误；测量指令微调代码模型。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 与既有基准的差异

代码补全只覆盖合成，缺少跨语言指令驱动修复与解释任务。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

## 构建方式

### 题目来源

在每种语言的 164 个 HumanEval 参考函数中人工加入一个 bug，跨语言尽量保持同类错误。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 出题者背景

论文团队人工设计 bug，而非由模型自动判定修复真值。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 审核流程

从HumanEval-X各语言解答JSON开始，人工并行向各语言引入bug；修正HumanEval-X问题并记录，转为带bug解答、instruction及元数据的JSONL上传HumanEvalPack。

来源：[1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07）。

### 质量控制

六种语言使用相近 bug 以支持可比性；附录给出类别与实例。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 去污染与泄漏控制

源自公开 HumanEval；添加人工错误不消除模型记忆原始正确实现的可能性。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

## 数据形式

### 规模与统计口径

每语言 164 个问题，6 语言共 984 个 bug；不等于 984 个互不相关原题。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 题型

自然语言+错误代码 → 修复代码；tests 与 docstring 提示有不同变体。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 模态

```json
[
  "文本"
  "源代码"
]
```

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 语言

```json
[
  "Python"
  "JavaScript"
  "Java"
  "Go"
  "C++"
  "Rust"
]
```

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 难度

细微功能 bug；文档提示的较易变体与只给测试的变体须区分。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 公开与隐藏划分

通过 HumanEvalPack 公开；Fix、Explain、Synthesize 是同套件不同任务。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

## 评测方法

### 指标

执行测试的 pass@1 等；按语言分别报告。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 评分规则

修复代码必须通过参考测试，不以自然语言解释质量代替功能正确。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 提示、采样与工具设置

区分humanevalfixtests（给测试、不含docstring，论文主设置）与humanevalfixdocs（给docstring）；官方示例temperature=0.2、n_samples=20、batch_size=5、max_length_generation=2048。

来源：[1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07）。

### 官方脚本

https://github.com/bigcode-project/octopack

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 可比性警告

必须分语言及fixdocs/fixtests协议比较；官方说明Python版本和batch_size影响随机性，论文使用Python3.9.13、batch_size=5；执行不可信生成代码应隔离。

来源：[1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07）。

## 最新情况

### 核查时间

2026-11-08

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-08）；[2](https://github.com/bigcode-project/octopack)（访问 2026-11-08）。

### 最新数据状态

```json
{
  "version": "HumanEvalPack 中的 HumanEvalFix；6语言×164题"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1"
      "date": "2026-09-16"
      "note": "ScienceIDE §3.3、附录11.1实际用 HumanEvalFix JavaScript 等代码修复任务评测科学轨迹训练迁移。"
    }
  ]
}
```

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07）；[2](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 论文修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2023-08-14"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2024-02-18"
    "timezone": ""
  }
]
```

> arXiv原始UTC时间已转换为；不等于数据集版本变更。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-08）。

### 饱和度与证据边界

原论文表2六语言平均pass@1：GPT-4 47.8%、OctoCoder 27.0%；这是2023/2024历史基线，不能据此判定2026年当前饱和程度。

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）。

### 污染与已知问题

HumanEval 改编造成原题记忆与修复能力混合，跨语言一致 bug 也不是完全独立样本。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 相关与衍生基准

HumanEvalExplain 与 HumanEvalSynthesize 是 HumanEvalPack 兄弟任务；本条仅收 HumanEvalFix。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

## 榜单快照

### 采集日期

2026-11-08 （采集日，不是运行或榜单更新日）

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-08）。

### 官方结果入口

https://github.com/bigcode-project/octopack

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 独立评测入口

待核实

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 结构化结果

```json
[
  {
    "rank": 1
    "model": "GPT-4"
    "score": "47.0"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Python"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "WizardCoder"
    "score": "31.8"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Python"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "OctoCoder"
    "score": "30.4"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Python"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "48.2"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / JavaScript"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "WizardCoder"
    "score": "29.5"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / JavaScript"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "OctoCoder"
    "score": "28.4"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / JavaScript"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "50.0"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Java"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "WizardCoder"
    "score": "30.7"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Java"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "OctoCoder"
    "score": "30.6"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Java"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "50.6"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Go"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "WizardCoder"
    "score": "30.4"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Go"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "OctoCoder"
    "score": "30.2"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Go"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "47.6"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / C++"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "OctoCoder"
    "score": "26.1"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / C++"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "WizardCoder"
    "score": "18.7"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / C++"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "GPT-4"
    "score": "43.3"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Rust"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "OctoCoder"
    "score": "16.5"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Rust"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "WizardCoder"
    "score": "13.0"
    "metric": "zero-shot pass@1 (%)"
    "track": "原论文表2 HumanEvalFixTests / Rust"
    "source_url": "https://arxiv.org/pdf/2308.07124"
    "result_type": "作者论文历史基线；列出的三模型子集内排序，非当前全榜"
    "source_date": "论文v2；实际API运行日待核实"
    "snapshot_date": "2026-11-08 "
  }
  {
    "model": "ScienceIDE 4B SFT 训练设置（精确检查点待核实）"
    "result": "HumanEvalFix JavaScript 相对提升 10.98 个百分点"
    "metric": "论文报告相对改善，不是绝对得分"
    "benchmark_version": "HumanEvalFix JS"
    "result_type": "H2 学术实验"
    "source_date": "2026-09-16"
    "collected_at": "2026-11-07 "
    "track": "ScienceIDE H2学术实验（相对改善，非绝对榜分）"
    "snapshot_date": "2026-11-07 （历史证据保留，未复开此文）"
    "rank": null
  }
]
```

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）；[2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-08）。

### 覆盖与局限

补入原作者论文表2的精确分语言FixTests基线；未找到独立实时官方总榜。ScienceIDE相对改善保留旧采集日并单列，不转换为绝对pass@1；FixDocs不得混入本轨。

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）；[2](https://github.com/bigcode-project/octopack/blob/main/README.md)（访问 2026-11-08）。

## 联系方式

### 官方公开邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 仓库反馈

https://github.com/bigcode-project/octopack/issues

> 公开仓库反馈入口；未发送问题。

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）。

### 官方社区

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

### 隐私与联系边界

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2308.07124)（访问 2026-11-07）。

## 原始文件

### 论文PDF

https://arxiv.org/pdf/2308.07124

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-07）。

### PDF SHA-256

c03f04d06e000e4a251bea07c8b654721a97dbf23009ba45909439c7d814502a

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）。

### PDF字节数

```json
2618401
```

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2308.07124)（访问 2026-11-08）。

### 已有文件夹

```json
{
  "id": "1xXVcvs2QJOirQEtIZUomvCncd0wm0nkK"
  "webViewLink": "
}
```

来源：[1]( 2026-11-07）。

### 其他官方文档

```json
[
  {
    "type": "中文介绍Google Doc"
    "id": "1VdSi5h_gTRKSEqG_HYOcUmV6YHox8eeex48YUrwHtUY"
    "webViewLink": "
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）；[2]( 2026-11-07）。

### 已有 PDF归档

```json
{
  "id": "10-4Bu_ewHurkjd6393FPJH4XwOO8jXtn"
  "webViewLink": "
}
```

来源：[1]( 2026-11-07）。

## 变更记录

### 历次核查

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]
```

来源：[1](https://github.com/bigcode-project/octopack)（访问 2026-11-07）；[2](https://arxiv.org/abs/2308.07124)（访问 2026-11-08）；[3](https://github.com/bigcode-project/octopack)（访问 2026-11-08）。

