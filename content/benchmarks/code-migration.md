# Code Migration v1.1

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: B；未核实保留标记

## 基本信息

### 简称

Code Migration v1.1

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 全称

Code Migration v1.1

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 基准版本

v1.1

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 主板块

代码

> Benchmark Atlas编辑分类。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 领域标签

- 代码

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 论文

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 代码

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 数据集

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 官方主页

https://www.vals.ai/benchmarks/code-migration-v1-1

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 论文标题

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 发起与维护

### 发起方

Vals AI

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 作者

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 维护方

Vals AI

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 设计目标

### 衡量能力

把完整可运行程序迁移到另一语言并忠实复现行为，含遗留COBOL现代化。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 设计背景

短代码翻译不能代表仓库级CLI迁移与有状态遗留业务系统。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 构建方式

### 题目来源

CLI为30个开源仓库；COBOL为10仓库，混合开源程序与为本基准合成的业务系统。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 出题者背景

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 审核

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 质量控制

隐藏行为测试前进行反作弊检查：禁止原程序包装、参考材料复制、硬编码输出，并检查目标语言。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 去污染

隐藏行为测试不向模型公开；源仓库本身公开，不能保证预训练未见。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 数据形式

### 题量与规模

CLI 30源仓库各迁到另外4语言，共120迁移；COBOL→Java另10仓库。headline按40源仓库等权，不是按130任务简单等权。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 题型

提供源程序及指令，提交目标语言实现和Dockerfile。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 模态

- 代码
- 文本
- CLI执行

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 语言

CLI源/目标Python、Java、Kotlin、Rust、C++；另有COBOL→Java。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 难度

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 公开与隐藏划分

开源源仓库；评分隐藏测试，每CLI迁移约100–400行为测试。完整发布范围待核实。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 评测方法

### 指标

Hidden-test pass rate (%)；代码质量另行诊断，不影响主分。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 评分

构建提交Docker镜像运行隐藏测试；CLI先对每源仓库4目标取均值，再40源仓库等权，CLI:COBOL权重3:1。作弊提交0。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 运行设置

v1.1统一Pi agent harness，离线sandbox，给源程序与任务指令。具体token/时限待核实。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 官方脚本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 可比性警示

v1.1从mini-SWE-agent换Pi并修订隐藏测试；任务不变但与v1分数不可直接比较。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：v1.1
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/code-migration-v1-1", "date": "2026-11-07", "date_type": "observed_on", "note": "Vals榜明确更新2026-10-30并列29模型。热度B，主要单一机构当前榜，不称全行业快速增长。"}]

> Vals榜明确更新2026-10-30并列29模型。热度B，主要单一机构当前榜，不称全行业快速增长。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 修订历史

v1.1更换Pi harness并修订隐藏测试；独立论文与修订历史待核实。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 污染、争议与限制

测试通过只表示被测行为；可读性、文档、文件结构和语言习惯是独立review维度，不能将隐藏测试分当代码质量。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 为什么近期热门

Vals榜明确更新2026-10-30并列29模型。热度B，主要单一机构当前榜，不称全行业快速增长。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 官方榜单入口

https://www.vals.ai/benchmarks/code-migration-v1-1

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 第三方覆盖

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | Claude Sonnet 5.5 | 86.88 | Code Migration v1.1 hidden-test pass rate (%) | 2026-10-30 |
| 2 | Claude Opus 5.5 | 81.01 | Code Migration v1.1 hidden-test pass rate (%) | 2026-10-30 |
| 3 | GPT-6 Astra | 80.58 | Code Migration v1.1 hidden-test pass rate (%) | 2026-10-30 |

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

### 覆盖与时效

Vals创建者榜单；三者为Overall而非CLI子集。页面模型effort曲线不等于headline另一个题集。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://www.vals.ai/benchmarks/code-migration-v1-1"}

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问 2026-11-07）
