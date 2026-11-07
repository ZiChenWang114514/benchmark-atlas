# Surface Evolver Bench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

已核验存在；11节研究快照；note: trending: B；未知字段保留待核实

## 基本信息

### 简称

Surface Evolver Bench

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 全称

Surface Evolver Bench

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 主板块

物理

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 子领域

- 材料
- 流体
- 科学代码

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 许可

Apache-2.0（官网页脚声明；适用范围以原仓库文件为准）

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 论文

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 代码

https://github.com/yhenon/surface-evolver-llm-eval

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 数据

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 官网

https://yhenon.github.io/surface-evolver-llm-eval/

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 论文标题

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 发起与维护

### 发起方

Yann Henon

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 合作方

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 作者

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 维护方

Yann Henon

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 资助

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 设计目标

### 衡量能力

在低资源自定义格式中描述三维液体表面，处理接触角、重力、体积约束、边界积分。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 设计背景

检验可执行计算物理建模，不只测文本物理知识；允许读文档和迭代修复。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 构建方式

### 题目来源

作者为每题编写参考解，模拟收敛液面，预计算体积、面积与能量。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 出题人背景

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 审核流程

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 质量控制

静态检查、隐藏Evolver脚本、与参考物理量的容差比较；不采用LLM裁判。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 去污染

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 数据形式

### 规模

16任务。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 题型

多步读取文档、运行模拟、修复并通过结构化工具提交原始.fe数据文件。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 模态

- 文本
- Surface Evolver .fe文件
- 模拟器反馈

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 语言

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 难度

复杂槽、井、通道液体配置；按任务分数部分给分。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 公开与隐藏划分

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 评测方法

### 指标

平均部分得分与严格pass rate分别记录。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 评分

有效文件、初始几何、约束等可获部分分；严格通过要求全部检查满足。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 提示与运行设置

每任务运行一次agent循环；推理档不同的同一模型独立列项。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 评测脚本

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 可比性警示

Epoch展示mean score不是pass rate；harness文档和反馈环会显著影响成绩。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度B：主要单一机构当前展示或厂商持续自评，不代表行业广泛采纳。

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 当前版本与热门证据

- **version**：待核实
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://epoch.ai/benchmarks/surface-evolver-bench", "date": "2026-11-07", "note": "Epoch当前展示结果和协议；观察日，主要单一机构跟踪。"}, {"url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks", "date": "2026-10-09", "note": "Epoch评审Not enough info；不代表质量合格。"}]

> B：主要单一机构当前评测/厂商采用，不能声称行业广泛采用。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 污染与争议

Epoch评审2026-10-09结论为Not enough info，不能将被收录等同质量认证。

[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 衍生及版本关系

与现有100条slug核对未发现同名旧版；不将评测实现或分项重复计为新benchmark。

> 编辑去重结论；版本关系以下述专门说明为准。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 官方榜单

https://yhenon.github.io/surface-evolver-llm-eval/

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 独立评测入口

https://epoch.ai/benchmarks/surface-evolver-bench

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

### 核验结果

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 覆盖与时效说明

官网有交互图但本轮可读返回没有模型数值；Epoch可读页给协议亦未返回数值，results保留待核实，不猜榜首。

[来源](https://epoch.ai/benchmarks/surface-evolver-bench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Drive资料夹

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方介绍/协议", "url": "https://yhenon.github.io/surface-evolver-llm-eval/"}

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）

### Drive PDF归档

待核实（本任务未上传）

## 变更记录

### changelog

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传Drive。"}

[来源](https://yhenon.github.io/surface-evolver-llm-eval/)（访问 2026-11-07）
