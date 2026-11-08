# Surface Evolver Bench

> Benchmark Constitution · 深度复核 2026-11-08。已核验存在；11节研究快照；note: trending: B；未知字段保留待核实

Surface Evolver Bench要求模型提交能被物理模拟器执行的.fe文件：几何、方向、接触角、体积和能量必须相互一致。评分不是模型裁判，而是确定性静态检查、隐藏模拟和数值容差。本次直接取得官方聚合JSON，区分95%的部分得分与87.5%的严格通过率，不再因交互图难读而留空。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval)（访问 2026-11-08）；[来源2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

## 基本信息

### 简称

Surface Evolver Bench

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 全称

Surface Evolver Bench

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 主板块

物理

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 领域

```json
[
  "材料"
  "流体"
  "科学代码"
]
```

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 许可与适用范围

Apache-2.0（已打开官方LICENSE）；Surface Evolver及其他依赖仍按其自身授权。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 论文

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 官方代码

https://github.com/yhenon/surface-evolver-llm-eval

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 数据

https://github.com/yhenon/surface-evolver-llm-eval/tree/main/tasks_public

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 官方入口

https://yhenon.github.io/surface-evolver-llm-eval/

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 论文标题

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 发起与维护

### 发起方

Yann Henon

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 合作/参与机构

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 作者

Yann Henon（官方项目作者；不是已找到独立论文的作者表）

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 维护方

Yann Henon

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 资助

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 设计目标

### 衡量能力

在低资源自定义格式中描述三维液体表面，处理接触角、重力、体积约束、边界积分。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 设计背景

检验可执行计算物理建模，不只测文本物理知识；允许读文档和迭代修复。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 构建方式

### 题目来源

作者为每题编写参考解，模拟收敛液面，预计算体积、面积与能量。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 出题者背景

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 审核流程

作者手写参考解并求收敛液面；静态与隐藏模拟器验收共同核查；独立多专家人工审稿流程待核实。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 质量控制

静态检查、隐藏Evolver脚本、与参考物理量的容差比较；不采用LLM裁判。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 污染控制

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 数据形式

### 题量

16任务；官方aggregate共448模型-任务运行、28配置，每配置16任务。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）；[来源2](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-08）

### 任务形式

多步读取文档、运行模拟、修复并通过结构化工具提交原始.fe数据文件。

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 模态

```json
[
  "文本"
  "Surface Evolver .fe文件"
  "模拟器反馈"
]
```

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 语言

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 难度

复杂槽、井、通道液体配置；按任务分数部分给分。

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 公开与隐藏划分

仓库区分tasks_public/与tasks_private/，默认运行private任务目录；agent只见prompt、可读文档与公开运行反馈，最终由hidden_command_script和隐藏物理量阈值验收。目录名称private不等于文件必然不可下载。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

平均部分得分与严格pass rate分别记录。

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 评分

加权部分分：静态检查0.3、隐藏Surface Evolver运行0.3、隐藏物理量容差检查0.4；passed要求静态和全部动态检查都通过。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 运行设置

工具为get_evolver_doc、run_surface_evolver、submit_fe_file；可迭代修复到max-rounds上限；原始.fe必须经结构化工具提交。推理档与API provider作为运行配置保留。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 评测工具

se_eval.run_eval（generate/grade）、se_eval.run_matrix、se_eval.rescore_results；任务JSON提供static_checks和dynamic_checks.evolver_metrics。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 可比性

Epoch展示mean score不是pass rate；harness文档和反馈环会显著影响成绩。

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08

[来源1](https://github.com/yhenon/surface-evolver-llm-eval)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "待核实"
  "heat_confidence": "B"
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/benchmarks/surface-evolver-bench"
      "date": "2026-11-07"
      "note": "Epoch当前展示结果和协议；观察日，主要单一机构跟踪。"
    }
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
      "date": "2026-10-09"
      "note": "Epoch评审Not enough info；不代表质量合格。"
    }
  ]
}
```

> B：主要单一机构当前评测/厂商采用，不能声称行业广泛采用。

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 饱和与能力边界

官方aggregate最高mean_score=0.95（claude-fable-5 high及kimi-k3），两者严格pass_rate均0.875（14/16）；部分给分接近满分不等于所有物理检查均已解决。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

### 风险与争议

低资源领域不等于无污染。作者称早期无文档或弱反馈harness成绩很低，工具、文档与反馈环显著影响结果；小型16题、一次运行不支持把微小名次差当统计显著差。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 系列与衍生关系

Surface Evolver是底层求解器，本评测是其16任务的LLM建模harness；平均部分得分与严格通过率是同任务两指标，不是两个独立benchmark。

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08

[来源1](https://github.com/yhenon/surface-evolver-llm-eval)（访问 2026-11-08）；[来源2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

### 官方入口

https://yhenon.github.io/surface-evolver-llm-eval/

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 独立来源

https://epoch.ai/benchmarks/surface-evolver-bench

[来源1](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 分来源与协议结果

#### official aggregate / mean score

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | claude-fable-5 (high) | 0.95 | mean partial-credit score (0–1) | {"runs":16,"passed":14,"pass_rate":0.875} |
| 1 | kimi-k3 | 0.95 | mean partial-credit score (0–1) | {"runs":16,"passed":14,"pass_rate":0.875} |
| 3 | gpt-5.6-sol (xhigh) | 0.93125 | mean partial-credit score (0–1) | {"runs":16,"passed":14,"pass_rate":0.875} |
| 4 | gpt-5.5 (high) | 0.88125 | mean partial-credit score (0–1) | {"runs":16,"passed":12,"pass_rate":0.75} |
| 5 | claude-opus-4.8 (high) | 0.875 | mean partial-credit score (0–1) | {"runs":16,"passed":11,"pass_rate":0.6875} |
| 6 | gpt-5.6-terra (xhigh) | 0.8375 | mean partial-credit score (0–1) | {"runs":16,"passed":11,"pass_rate":0.6875} |
| 7 | gpt-5.5 (medium) | 0.8125 | mean partial-credit score (0–1) | {"runs":16,"passed":10,"pass_rate":0.625} |
| 8 | gemini-3.8-flash (high) | 0.76875 | mean partial-credit score (0–1) | {"runs":16,"passed":9,"pass_rate":0.5625} |
| 9 | grok-4.5 (high) | 0.74375 | mean partial-credit score (0–1) | {"runs":16,"passed":8,"pass_rate":0.5} |
| 10 | claude-opus-4.8 (none) | 0.68125 | mean partial-credit score (0–1) | {"runs":16,"passed":4,"pass_rate":0.25} |
| 11 | gpt-5.6-luna (medium) | 0.61875 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 12 | claude-sonnet-5 (medium) | 0.6 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 13 | gemini-3.5-flash (medium) | 0.58125 | mean partial-credit score (0–1) | {"runs":16,"passed":6,"pass_rate":0.375} |
| 14 | glm-5.2 (high) | 0.55625 | mean partial-credit score (0–1) | {"runs":16,"passed":5,"pass_rate":0.3125} |
| 15 | minimax-m3 | 0.5499999999999999 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 16 | muse-spark-1.1 (high) | 0.525 | mean partial-credit score (0–1) | {"runs":16,"passed":6,"pass_rate":0.375} |
| 16 | glm-5.3-flash (max) | 0.525 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 18 | kimi-k2.7-code | 0.4875 | mean partial-credit score (0–1) | {"runs":16,"passed":6,"pass_rate":0.375} |
| 19 | deepseek-v4.1-flash (high) | 0.4625 | mean partial-credit score (0–1) | {"runs":16,"passed":5,"pass_rate":0.3125} |
| 20 | qwen3.8-27b (xhigh) | 0.45 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 21 | qwen3.6-35b-a3b | 0.44375 | mean partial-credit score (0–1) | {"runs":16,"passed":2,"pass_rate":0.125} |
| 22 | deepseek-v4-pro (high) | 0.4 | mean partial-credit score (0–1) | {"runs":16,"passed":4,"pass_rate":0.25} |
| 23 | gemma-4-31b-it (none) | 0.30624999999999997 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 24 | mistral-large-4-0 | 0.28125 | mean partial-credit score (0–1) | {"runs":16,"passed":3,"pass_rate":0.1875} |
| 25 | mistral-medium-3-5 (high) | 0.26875 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 26 | gpt-oss-120b | 0.25 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 27 | laguna-m.1 | 0.15625 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |
| 27 | trinity-large-thinking | 0.15625 | mean partial-credit score (0–1) | {"runs":16,"passed":1,"pass_rate":0.0625} |

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

### 覆盖与时效

直接解析官方发布data/aggregates.json，完整保留28配置的原始mean_score、pass_rate、passed与runs，按mean_score同分并列；不从图表估读，不将Epoch转载当独立重测。源文件没有全榜更新时间。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 官方反馈

https://github.com/yhenon/surface-evolver-llm-eval/issues

[来源1](https://github.com/yhenon/surface-evolver-llm-eval/blob/main/README.md)（访问 2026-11-08）

### 公开社区

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 隐私边界

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 原始文件

### 源站PDF

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 文件夹

待核实

> 已检查所引官方材料，未完成精确核验；不代表官方未公开。

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "官方介绍/协议"
    "url": "https://yhenon.github.io/surface-evolver-llm-eval/"
  }
  {
    "type": "已打开一手材料"
    "url": "https://github.com/yhenon/surface-evolver-llm-eval"
    "accessed": "2026-11-08"
  }
  {
    "type": "已打开一手材料"
    "url": "https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json"
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://github.com/yhenon/surface-evolver-llm-eval)（访问 2026-11-08）；[来源2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）

### PDF归档

待核实

[来源1](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 变更记录

```json
[
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

[来源1](https://github.com/yhenon/surface-evolver-llm-eval)（访问 2026-11-08）；[来源2](https://yhenon.github.io/surface-evolver-llm-eval/data/aggregates.json)（访问 2026-11-08）
