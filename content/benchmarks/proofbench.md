# ProofBench

> 深度核验：2026-11-08。访问日不等于发布日期或实验运行日；未知保留，不推定“未公开”。

ProofBench（论文名FormalProofBench）让模型提交由Lean 4检验的数学证明，而非让裁判读自然语言解答。当前v1.1在100道私有题评测，已与原始200题论文协议分离。形式检查规则、Lean/Mathlib版本、是否联网、能否添加辅助引理和预算差异都会改变可比性；native_decide获准也不等于所有证明仅依赖kernel。

最近复核

## 1. 基本信息

### 简称

ProofBench

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 全称

ProofBench（论文名称FormalProofBench）

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 数据版本

v1.1

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文版本

arXiv:2603.26996v1；ICLR 2026 Workshop VerifAI-2论文。

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 发布时间

论文首发：2026-03-28 06:14:53 （源站2026-03-27 21:14:53 UTC）；不是当前v1.1榜单更新时间。

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 板块

数学

> Benchmark Atlas编辑分类。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 子领域

```json
[
 "数学"
]
```

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 许可

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2603.26996

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### 代码

https://github.com/vals-ai/proof-bench

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### 数据集

https://github.com/vals-ai/proof-bench/tree/main/problems

> 仓库明确仅提供sample problems，不冒称已下载网页所述全部100题public split。未找到由官方材料确认的HF发布入口。

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### 官方主页

https://www.vals.ai/benchmarks/proof_bench

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文题名

FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

## 2. 发起与维护

### 发起方

Vals AI与论文形式化贡献者

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 合作单位

```json
[
 "EPFL"
 "Moscow Institute of Physics and Technology"
 "Indiana University Bloomington"
 "独立研究者（依论文作者单位）"
]
```

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 作者

```json
[
 "Nikil Ravi"
 "Kexing Ying"
 "Vasilii Nesterov"
 "Rayan Krishnan"
 "Elif Uskuplu"
 "Bingyu Xia"
 "Janitha Aswedige"
 "Langston Nashold"
]
```

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### 维护方

Vals AI

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 3. 设计目标

### 目标能力

高级本科和研究生数学定理的Lean 4机器可验证证明。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 相对既有评测的缺口

自然语言证明可能掩盖逻辑漏洞；需要确定性的形式检查。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 4. 构建方式

### 题目与标签来源

资格考试与标准教材，涵盖概率、测度、分析、代数、代数几何、数论、逻辑。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 出题/标注背景

Lean 4专家，包括博士生与领域专家。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 审核流程

题目与Lean形式陈述经过二次人工审核，避免误形式化。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 质量控制

每份接受证明重新编译并检查#print axioms；sorry、admit及新公理不被接受。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 去污染与隔离

原始论文为防训练污染保密200题；当前v1.1改为public 100/private 100，私有100题用于榜单。教材/资格考试本身可公开，隐藏形式化并不保证模型未见过自然语言定理。

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

## 5. 数据形式

### 规模

公开100题、私有100题；当前榜以100道private题为口径。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 题型

自然语言题干+Lean 4形式陈述，生成形式证明。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 模态

```json
[
 "文本"
 "Lean代码"
]
```

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 语言

数学自然语言与Lean 4

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 难度

高级本科与研究生数学

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 公开/隐藏划分

存在版本与可下载性差异：原始v1论文200题保密、只放示例；当前v1.1网页称public 100/private 100，当前榜以private 100题评估；仓库README仍称仅含sample problems。不能宣称已验证完整public 100题可下载。

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）；[2](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

## 6. 评测方法

### 指标

Accuracy (%)：最终提交且通过Lean检查的题目比例。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 判分

每题最多40轮，必须submit_proof且编译通过；无提交不得分。每份证明检查#print axioms，拒绝sorry/admit及新增公理。native_decide现被接受：它依赖Lean.ofReduceBool与Lean.trustCompiler，并非只由kernel逐步归约证明。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 提示/推理设置

普通模型无互联网；lean_loogle查询Mathlib、lean_run_code迭代、submit_proof仅最终一次。普通模型Lean 4.25.2；Aristotle用4.28。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 官方实现

https://github.com/vals-ai/proof-bench；main.py、proof_bench/agent.py、tools.py、prover.py等。README命令的--k 3属于复现实验参数，不自动当当前榜单重复次数。

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### 可比性边界

v1.1与旧版不可比。Aristotle有自有系统、网页搜索与不同Mathlib；AlephProver也用自有基础设施及不同预算。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 7. 最新情况

### 核验日

2026-11-08

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 本次版本快照

```json
{
 "version": "v1.1"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://www.vals.ai/benchmarks/proof_bench"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。"
 }
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。"
 }
 ]
}
```

> Vals榜明确更新2026-10-29；Epoch ECI纳入ProofBench，但标明由创建者实施，不把指数收录误写为独立实跑。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）；[2](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 论文修订

```json
[
 {
 "version": "v1"
 "submitted_at": "2026-03-28"
 }
]
```

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 饱和情况

当前榜4个系统100%；表面已达满分，但不能将此推广为一般数学研究完全解决。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 污染/限制/争议

v1.1与旧版不可直接比较。native_decide先拒后接受，影响7个模型在2道题中的单题分数。Aristotle可联网、使用Lean 4.28及整文件辅助引理；语言模型无网络、Lean 4.25.2、仅提交证明体。AlephProver可辅助引理、禁网络，用4.25.2；预算$500/24h获得100，首轮$75/90min为99。这些系统和预算不能当作同一受控配置。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 衍生与相关版本

与已有miniF2F不同；v1.1为本条最新版本。

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-08 （采集日，不是实验运行日）

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）

### 官方结果入口

https://www.vals.ai/benchmarks/proof_bench

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 第三方入口

https://epoch.ai/data/eci-documentation/data

[1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| 官方当前v1.1 / private 100 | 1 | [Claude Sonnet 5.5](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 2 | [Claude Opus 5.5](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 3 | [Claude Fable 5.1](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 4 | [AlephProver](https://www.vals.ai/benchmarks/proof_bench) | 100.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 5 | [GPT-6.1 Sol](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 6 | [GPT-6 Astra](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 7 | [Gemini 4 Argon](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 8 | [Claude Opus 5](https://www.vals.ai/benchmarks/proof_bench) | 99.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 9 | [Claude Fable 5](https://www.vals.ai/benchmarks/proof_bench) | 95.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 10 | [Wonder Full](https://www.vals.ai/benchmarks/proof_bench) | 94.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 11 | [Kimi K3.1 Pro](https://www.vals.ai/benchmarks/proof_bench) | 91.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 12 | [Claude Haiku 5.5](https://www.vals.ai/benchmarks/proof_bench) | 89.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 13 | [Kimi K3](https://www.vals.ai/benchmarks/proof_bench) | 87.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 14 | [Aristotle](https://www.vals.ai/benchmarks/proof_bench) | 86.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 15 | [Wonder](https://www.vals.ai/benchmarks/proof_bench) | 84.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 16 | [GPT-6 Sol](https://www.vals.ai/benchmarks/proof_bench) | 83.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 17 | [GPT-5.6 Sol](https://www.vals.ai/benchmarks/proof_bench) | 83.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 18 | [Claude Sonnet 5](https://www.vals.ai/benchmarks/proof_bench) | 77.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 19 | [Hy4 Preview](https://www.vals.ai/benchmarks/proof_bench) | 75.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 20 | [GPT-5.6 Terra](https://www.vals.ai/benchmarks/proof_bench) | 74.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 21 | [MiMo V2.6 Pro](https://www.vals.ai/benchmarks/proof_bench) | 70.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 22 | [GPT-6 Luna](https://www.vals.ai/benchmarks/proof_bench) | 64.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 23 | [MiMo V2.6 Flash](https://www.vals.ai/benchmarks/proof_bench) | 63.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 24 | [Ember-1](https://www.vals.ai/benchmarks/proof_bench) | 61.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 25 | [GPT-5.6 Luna](https://www.vals.ai/benchmarks/proof_bench) | 60.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 26 | [Gemini 3.7 Flash](https://www.vals.ai/benchmarks/proof_bench) | 58.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 27 | [Muse Spark 1.3 Max](https://www.vals.ai/benchmarks/proof_bench) | 58.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 28 | [Qwen 3.8 Max](https://www.vals.ai/benchmarks/proof_bench) | 58.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 29 | [DeepSeek V4 Flash 0731](https://www.vals.ai/benchmarks/proof_bench) | 56.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 30 | [Muse Spark 1.3](https://www.vals.ai/benchmarks/proof_bench) | 55.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 31 | [DeepSeek V4.1 Flash](https://www.vals.ai/benchmarks/proof_bench) | 54.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 32 | [Grok 4.6](https://www.vals.ai/benchmarks/proof_bench) | 51.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 33 | [DeepSeek V4 Pro 0813](https://www.vals.ai/benchmarks/proof_bench) | 50.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 34 | [GLM 5.3](https://www.vals.ai/benchmarks/proof_bench) | 49.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 35 | [Gemini 3.8 Flash](https://www.vals.ai/benchmarks/proof_bench) | 48.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 36 | [Muse Spark 1.2](https://www.vals.ai/benchmarks/proof_bench) | 43.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 37 | [Step 5 Preview](https://www.vals.ai/benchmarks/proof_bench) | 42.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 38 | [Gemini 3.5 Flash](https://www.vals.ai/benchmarks/proof_bench) | 31.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 39 | [Grok 4.5](https://www.vals.ai/benchmarks/proof_bench) | 31.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 40 | [Grok 4.7](https://www.vals.ai/benchmarks/proof_bench) | 26.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 41 | [Gemini 3.1 Pro Preview (02/26)](https://www.vals.ai/benchmarks/proof_bench) | 26.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 42 | [MiMo V2.5 Pro](https://www.vals.ai/benchmarks/proof_bench) | 22.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 43 | [GLM 5.3 Flash](https://www.vals.ai/benchmarks/proof_bench) | 21.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 44 | [Beam 1.0](https://www.vals.ai/benchmarks/proof_bench) | 18.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 45 | [MiniMax-M3](https://www.vals.ai/benchmarks/proof_bench) | 18.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 46 | [DeepSeek V4](https://www.vals.ai/benchmarks/proof_bench) | 16.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 47 | [MiMo V2.5](https://www.vals.ai/benchmarks/proof_bench) | 16.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 48 | [Qwen 3.8 27B](https://www.vals.ai/benchmarks/proof_bench) | 16.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 49 | [Mistral Large 4 Preview](https://www.vals.ai/benchmarks/proof_bench) | 10.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 50 | [Mistral Medium 3.5](https://www.vals.ai/benchmarks/proof_bench) | 9.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 51 | [Inkling Small](https://www.vals.ai/benchmarks/proof_bench) | 6.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 52 | [Mercury 2.5](https://www.vals.ai/benchmarks/proof_bench) | 3.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 53 | [Inkling](https://www.vals.ai/benchmarks/proof_bench) | 0.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 官方当前v1.1 / private 100 | 54 | [Nemotron 3.5 Lightning](https://www.vals.ai/benchmarks/proof_bench) | 0.0 | ProofBench v1.1 private-100 Accuracy (%) | 2026-10-29 |
| 论文v1 Table 2 / 历史200题 | 1 | [Claude Opus 4.5 (Thinking)](https://arxiv.org/pdf/2603.26996) | 33.5 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 2 | [Gemini 3 Pro (11/25)](https://arxiv.org/pdf/2603.26996) | 18.5 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 3 | [Claude Sonnet 4.5 (Thinking)](https://arxiv.org/pdf/2603.26996) | 18 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 4 | [GPT 5](https://arxiv.org/pdf/2603.26996) | 17 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 5 | [Gemini 3 Flash (12/25)](https://arxiv.org/pdf/2603.26996) | 15 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 6 | [GPT 5.2](https://arxiv.org/pdf/2603.26996) | 13.5 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 7 | [GPT 5 Nano](https://arxiv.org/pdf/2603.26996) | 12.5 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 8 | [GPT 5.1 Codex Max](https://arxiv.org/pdf/2603.26996) | 12 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 9 | [DeepSeek V3.2 (Nonthinking)](https://arxiv.org/pdf/2603.26996) | 8 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 10 | [GPT 5 Mini](https://arxiv.org/pdf/2603.26996) | 7 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 11 | [GLM 4.7](https://arxiv.org/pdf/2603.26996) | 4.5 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 12 | [Grok 4.1 Fast (Reasoning)](https://arxiv.org/pdf/2603.26996) | 4 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |
| 论文v1 Table 2 / 历史200题 | 13 | [DeepSeek V3.2 (Thinking)](https://arxiv.org/pdf/2603.26996) | 3 | FormalProofBench旧版200题 Accuracy (%) | 2026-03-28 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 覆盖与限制

收录v1.1官网54行及论文v1 Table 2全部13行，版本分轨。当前网页前4项显示100%；保留原显示行号但不把同分写成真实性能差距。Epoch ECI只是聚合创建者结果，未据此新增“Epoch独立实跑”成绩。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

## 9. 联系方式

### 项目公开邮箱

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### GitHub反馈

https://github.com/vals-ai/proof-bench/issues

[1](https://raw.githubusercontent.com/vals-ai/proof-bench/main/README.md)（访问 2026-11-08）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 隐私边界

只列官方项目反馈渠道；不推断作者私人邮箱。

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-08）

## 10. 原始文件

### 原始PDF

https://arxiv.org/pdf/2603.26996

> 原始论文PDF入口；未下载或上传，哈希与字节数待核实。

[1](https://arxiv.org/abs/2603.26996)（访问 2026-11-07）

### SHA-256

e5f3a7973c389484b6114050274665dc2fb2525edc0e48f8908adfb44119b9ac

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### PDF字节数

818681

[1](https://arxiv.org/pdf/2603.26996)（访问 2026-11-08）

### 文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "官方网页方法与榜单（非PDF）"
 "url": "https://www.vals.ai/benchmarks/proof_bench"
 }
]
```

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

### 论文PDF

待核实

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-07）

## 11. 变更记录

[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-08"
 最近复核
 }
]

[1](https://www.vals.ai/benchmarks/proof_bench)（访问 2026-11-08）
