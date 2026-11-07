# SkillsBench

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: B**。Vals于2026-10-29更新With Skills/No Skills配对结果，榜表35行配置；热度B，主要同一评测机构当前展示，不把目录和详情当两家采纳。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

## 基本信息

### 简称

SkillsBench

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 全称

SkillsBench

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 基准版本

论文当前87题库存；Vals 2026-10-29实现快照

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 论文版本

v4（本次arXiv正文资源标识）

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 发布日期

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 主板块

Agent

> 编辑归档，不代表官方分类。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 领域标签

```json
[
  "代码",
  "技能"
]
```

> 编辑归档，不代表官方分类。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 许可证

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2602.12670

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 官方代码

https://github.com/benchflow-ai/skillsbench

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 数据地址

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/skillsbench

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 论文标题

SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

## 发起与维护

### 发起机构

BenchFlow（原始benchmark）；Vals AI（独立实现）

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 作者

Xiangyi Li、Yimin Liu、Wenbo Chen等；完整作者名单见论文，Vals引用作者表与当前论文修订名单不同。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 维护方

BenchFlow（原始benchmark）；Vals AI（独立实现）

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

## 设计目标

### 衡量能力

配对比较同一模型及harness在有无可复用技能包时的表现，测量技能增强收益。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 设计背景

传统agent得分混合基础模型、工具架构与增强效果；本基准把技能作为独立实验因素。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

## 构建方式

### 题目来源

142位贡献者提交400候选任务，经结构、oracle执行、指令来源和技能泄漏门控及人工审查，当前保留87任务。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 出题者背景

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 审核流程

人工真实工作指令、固定容器、参考解及确定性验证器；技能不能包含实例答案、硬编码路径或魔数。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 质量控制

人工真实工作指令、固定容器、参考解及确定性验证器；技能不能包含实例答案、硬编码路径或魔数。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 去污染

技能与任务答案解耦，扫描实例文件名、魔数、原样oracle命令或预期输出泄漏；不能保证完全排除预训练污染。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

## 数据形式

### 题量与规模

论文当前87任务、8领域；18个模型-harness配置。Vals方法页未在本次可读正文明确其任务清单commit，不能自动认定与论文修订库存完全相同。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 题型

终端与文件产物任务；包含自然科学、数学优化、安全、工程、金融、办公及软件等。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 模态

```json
[
  "文本",
  "代码",
  "数据文件"
]
```

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 公开与隐藏划分

论文公开任务定义；oracle、验证器和标签在agent运行时隔离；这不等于网站完全不公开它们。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

## 评测方法

### 指标

任务宏平均通过率、Skills绝对增益与归一化增益。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 评分

确定性脚本/pytest验证；Vals每模型每条件3次，先题内平均再跨题平均。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 提示与运行设置

Vals默认OpenHands-CLI固定commit 3ca17446c5d9c1e35e054803478a3501ec251ecf；同GPT-5.5另列Codex；With/No Skills为分轨。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 官方评测脚本

https://github.com/benchflow-ai/skillsbench

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 可比性警示

论文与Vals的库存、harness及运行时间不同；论文87题结果不可替代Vals当前榜；要按同模型同harness计算技能增益。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "论文当前87题库存；Vals 2026-10-29实现快照",
  "trending": "B",
  "heat_evidence": "Vals于2026-10-29更新With Skills/No Skills配对结果，榜表35行配置；热度B，主要同一评测机构当前展示，不把目录和详情当两家采纳。",
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/skillsbench",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 修订历史

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 饱和情况

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 污染与争议

论文与Vals的库存、harness及运行时间不同；论文87题结果不可替代Vals当前榜；要按同模型同harness计算技能增益。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 版本与衍生关系

SkillsBench不是AgentBench；With Skills和No Skills是同一条目的实验条件，不重复新增。

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 官方榜单

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 第三方覆盖

https://www.vals.ai/benchmarks/skillsbench

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "DeepSeek V4.1 Flash",
    "score": 69.8,
    "metric": "Vals With Skills 准确率 (%)；OpenHands",
    "source_url": "https://www.vals.ai/benchmarks/skillsbench",
    "source_date": "2026-10-29",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序",
    "harness": "OpenHands",
    "condition": "With Skills"
  },
  {
    "rank": 2,
    "model": "Grok 4.5",
    "score": 66.03,
    "metric": "Vals With Skills 准确率 (%)；OpenHands",
    "source_url": "https://www.vals.ai/benchmarks/skillsbench",
    "source_date": "2026-10-29",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序",
    "harness": "OpenHands",
    "condition": "With Skills"
  },
  {
    "rank": 3,
    "model": "Gemini 3.7 Flash",
    "score": 65.89,
    "metric": "Vals With Skills 准确率 (%)；OpenHands",
    "source_url": "https://www.vals.ai/benchmarks/skillsbench",
    "source_date": "2026-10-29",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序",
    "harness": "OpenHands",
    "condition": "With Skills"
  }
]
```

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 时效与覆盖说明

论文与Vals的库存、harness及运行时间不同；论文87题结果不可替代Vals当前榜；要按同模型同harness计算技能增益。 榜表自写更新时间：2026-10-29；采集日不等于运行日。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

xiangyi@benchflow.ai

[来源](https://arxiv.org/abs/2602.12670)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

https://arxiv.org/pdf/2602.12670

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2602.12670)（访问2026-11-07）

### PDF SHA-256

e987ebc3f0084a1ffc8acbca58259e33120b95fcef3876abfad060e169cf210b

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2602.12670)（访问2026-11-07）

### PDF字节数

1769852

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2602.12670)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://www.vals.ai/benchmarks/skillsbench"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2602.12670"
  }
]
```

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。SkillsBench不是AgentBench；With Skills和No Skills是同一条目的实验条件，不重复新增。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://www.vals.ai/benchmarks/skillsbench)（访问2026-11-07）
