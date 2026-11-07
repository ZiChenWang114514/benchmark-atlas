# HealthBench

> 核验日期：2026-11-07（Asia/Shanghai，UTC+8）。官方资料中文改写；待核实不等于未公开。

已核实存在；官方资料研究快照，未知保留待核实；trending: A

## 基本信息

### 简称

HealthBench

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 全称

HealthBench

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 基准版本

原始HealthBench（非Professional）

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 论文版本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 发布日期

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 主板块

生物与医学

> 编辑归档；跨领域只计主板块。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 领域标签

```json
[
  "生物与医学"
]
```

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 许可证

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2505.08775

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方代码

https://github.com/openai/simple-evals

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 数据地址

https://github.com/openai/simple-evals

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方入口

https://arxiv.org/abs/2505.08775

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 论文标题

HealthBench: Evaluating Large Language Models Towards Improved Human Health

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

OpenAI

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 合作方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 作者

Rahul K. Arora、Jason Wei、Rebecca Soskin Hicks、Preston Bowman等；完整名单见论文。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 维护方

OpenAI

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 资助方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 设计目标

### 衡量能力

面向普通用户与医护人员的开放式医疗对话质量、安全、上下文意识与沟通能力。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 设计背景

医学选择题和短答案难反映真实医疗交互，也常缺乏与医生判断的一致性验证。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 构建方式

### 题目来源

以合成情境为主，辅以医生红队与HealthSearchQA改写；262名医生参与，执业经历覆盖60国与26专科。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 出题者背景

262名医生，覆盖26专科与60国执业经历；论文列49种医生可贡献语言，不将此自动当成数据集精确语言分布。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 审核流程

医生经付费入门任务筛选；持续自动与人工审查，低质量贡献者注释移除。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 质量控制

共识标准需至少两位且多数医生认可；并通过meta-evaluation比较模型和医生评分一致性。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 去污染

发布canary及避免传播题例的请求，并保留少量同分布私有hold-out；其规模待核实。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 数据形式

### 题量与规模

5,000对话；48,562个唯一rubric标准；Hard为1,000题；Consensus为3,671题且只保留共识标准。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 题型

根据完整单轮或多轮历史回复最后一条用户消息。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 模态

```json
[
  "文本"
]
```

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 语言

多语言医疗对话；精确各语言题量待核实。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 难度

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 公开与隐藏划分

公开主集与少量同分布私有hold-out；hold-out精确题量待核实。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 评测方法

### 指标

整体rubric归一化分、分theme/axis分数、worst-at-k；Hard与Consensus独立报告。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 评分

每项rubric分值-10至10且非零；命中计全分，否则0；总分除正分上限，逐题平均后截断到[0,1]。默认GPT-4.1裁判。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 运行设置

生成最终用户消息的回复；原论文OpenAI模型temperature=1，其他厂商设置见附录H。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方脚本

OpenAI simple-evals中的HealthBench评测、meta-evaluation、Hard/Consensus与绘图工具。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 可比性警示

原始分数与AA长度调整分数不同；Hard、Consensus和525题Professional不是同一个指标；不能把Professional榜搬到本条。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 最新版本与热门证据

```json
{
  "version": "原始HealthBench（非Professional）",
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "AA当前附加评测表明确分别列原始5,000题HealthBench和525题Professional；不把Professional网页排行榜归本条。候选另列10月系统卡，本轮未核实，不能算第二份已核实热度证据。"
    }
  ]
}
```

> 热度等级沿候选采用；只保留本轮已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 修订历史

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 饱和情况

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 污染与争议

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 版本与已有条目关系

与当前100条目的id、名称、版本字段去重后未收录

> 已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 为什么近期热门

近期实际使用与审查证据如下；不以采集日冒充发布日期。

- 2026-11-07（observed_on）：AA当前附加评测表明确分别列原始5,000题HealthBench和525题Professional；不把Professional网页排行榜归本条。候选另列10月系统卡，本轮未核实，不能算第二份已核实热度证据。 [来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方榜单

https://arxiv.org/abs/2505.08775

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 第三方覆盖

https://artificialanalysis.ai/methodology/intelligence-benchmarking

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 核验结果

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 覆盖说明

当前AA /evaluations/healthbench实际呈现Professional的525题榜，不能用于原始5,000题HealthBench。原论文o3=60%是历史结果而非2026当前第一；最新原版榜单数值待核实。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

```json
[
  "karan@openai.com"
]
```

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 公开反馈

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 官方社交

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 隐私政策

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2505.08775

> 官方arXiv原论文PDF入口；本组不下载、不上传Drive。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### PDF字节数

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### Drive文件夹

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方方法或项目页",
    "url": "https://arxiv.org/abs/2505.08775",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai (UTC+8)",
    "change": "首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传Drive。"
  }
]
```

[来源1](https://arxiv.org/abs/2505.08775)（访问 2026-11-07）

