# ProofBench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: A；未核实保留标记

## 基本信息

### 简称

ProofBench

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 全称

ProofBench（论文名称FormalProofBench）

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 基准版本

v1.1

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文版本

待核实

> 论文修订号尚未完成精确核实。

[来源](https://arxiv.org/abs/2603.26996)（访问2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 主板块

数学

> Benchmark Atlas编辑分类。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 领域标签

- 数学

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2603.26996

[来源](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### 代码

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 数据集

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 官方主页

https://www.vals.ai/benchmarks/proof_bench

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文标题

FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?

[来源](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

## 发起与维护

### 发起方

Vals AI与论文形式化贡献者

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 作者

- Nikil Ravi
- Kexing Ying
- Vasilii Nesterov
- Rayan Krishnan
- Elif Uskuplu
- Bingyu Xia
- Janitha Aswedige
- Langston Nashold

[来源](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### 维护方

Vals AI

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 设计目标

### 衡量能力

高级本科和研究生数学定理的Lean 4机器可验证证明。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 设计背景

自然语言证明可能掩盖逻辑漏洞；需要确定性的形式检查。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 构建方式

### 题目来源

资格考试与标准教材，涵盖概率、测度、分析、代数、代数几何、数论、逻辑。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 出题者背景

Lean 4专家，包括博士生与领域专家。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 审核

题目与Lean形式陈述经过二次人工审核，避免误形式化。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 质量控制

每份接受证明重新编译并检查#print axioms；sorry、admit及新公理不被接受。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 去污染

100道私有测试题用于保留污染抵抗；公开100题用于透明评测。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 数据形式

### 题量与规模

公开100题、私有100题；当前榜以100道private题为口径。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 题型

自然语言题干+Lean 4形式陈述，生成形式证明。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 模态

- 文本
- Lean代码

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 语言

数学自然语言与Lean 4

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 难度

高级本科与研究生数学

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 公开与隐藏划分

公共100题与私有100题；论文早期整体200题的结果不直接套到v1.1。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 评测方法

### 指标

Accuracy (%)：最终提交且通过Lean检查的题目比例。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 评分

每题最多40轮，必须调用submit_proof；无提交或无效证明不给部分分。native_decide现被接受。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 运行设置

普通模型无互联网；lean_loogle查询Mathlib、lean_run_code迭代、submit_proof仅最终一次。普通模型Lean 4.25.2；Aristotle用4.28。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 官方脚本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 可比性警示

v1.1与旧版不可比。Aristotle有自有系统、网页搜索与不同Mathlib；AlephProver也用自有基础设施及不同预算。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：v1.1
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/proof_bench", "date": "2026-11-07", "date_type": "observed_on", "note": "Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。"}, {"url": "https://epoch.ai/data/eci-documentation/data", "date": "2026-11-07", "date_type": "observed_on", "note": "Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。"}]

> Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）；[来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 饱和情况

当前榜4个系统100%；表面已达满分，但不能将此推广为一般数学研究完全解决。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 污染、争议与限制

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 衍生与版本关系

与已有miniF2F不同；v1.1为本条最新版本。

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 为什么近期热门

Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问2026-11-07）；[来源](https://epoch.ai/data/eci-documentation/data)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 官方榜单入口

https://www.vals.ai/benchmarks/proof_bench

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 第三方覆盖

https://epoch.ai/data/eci-documentation/data

[来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | Claude Sonnet 5.5 | 100.0 | ProofBench v1.1 Accuracy (%) | 2026-10-29 |
| 2 | Claude Opus 5.5 | 100.0 | ProofBench v1.1 Accuracy (%) | 2026-10-29 |
| 3 | Claude Fable 5.1 | 100.0 | ProofBench v1.1 Accuracy (%) | 2026-10-29 |
| 4 | AlephProver | 100.0 | ProofBench v1.1 Accuracy (%) | 2026-10-29 |

> 保留官网显示顺序rank 1–4；四者同为100%，不是统计上严格先后。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问2026-11-07）

### 覆盖与时效

Vals为创建者实测；Epoch ECI列入creator-administered，不意味着Epoch重新运行证明。

[来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）；[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2603.26996

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://www.vals.ai/benchmarks/proof_bench"}

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）
