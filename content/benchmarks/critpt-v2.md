# CritPt v2

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: A；未核实保留标记

## 基本信息

### 简称

CritPt v2

[来源](https://critpt.com/)（访问 2026-11-07）

### 全称

Complex Research using Integrated Thinking – Physics Test（CritPt），当前部署v2

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 基准版本

v2

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 主板块

物理

> Benchmark Atlas编辑分类。

[来源](https://critpt.com/)（访问 2026-11-07）

### 领域标签

- 物理

[来源](https://critpt.com/)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2509.26574

> 原始CritPt论文，不能自动视为独立v2论文。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 代码

https://github.com/CritPt-Benchmark/CritPt

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 数据集

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 官方主页

https://critpt.com/

[来源](https://critpt.com/)（访问 2026-11-07）

### 论文标题

Probing the Critical Point (CritPt) of AI Reasoning: a Frontier Physics Research Benchmark

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

## 发起与维护

### 发起方

Argonne National Laboratory、University of Illinois Urbana-Champaign及物理研究者协作

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 作者

Minhui Zhu、Minyang Tian等；完整名单见原始论文。

[来源](https://arxiv.org/abs/2509.26574)（访问2026-11-07）

### 维护方

CritPt团队；Artificial Analysis合作提供评分服务

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 资助

原始论文列Argonne LDRD、美国能源部及NSF算力等支持；v2新增资助待核实。

[来源](https://arxiv.org/abs/2509.26574)（访问2026-11-07）

## 设计目标

### 衡量能力

未发表研究级物理问题的综合推理；从理论、实验或计算条件推导可验证答案。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 设计背景

教材与竞赛题难代表原创研究中的开放式长链推理。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

## 构建方式

### 题目来源

物理专家基于自身研究原创；原始论文的71个挑战包括1个示例，另有190个checkpoint。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 出题者背景

来自30所机构的50余名物理研究人员，包括博士生、博士后及教授（原始版本口径）。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 审核

专家和协调者多轮修订、相近领域同行审核、技术推导复核与科学写作编辑。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 质量控制

标准答案需可机器验证，并为数值、符号与函数输出设置物理相关容差。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 去污染

原创未发表题、抗猜测答案，测试题解保密；不能据此保证完全无污染。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

## 数据形式

### 题量与规模

v2全量70题；AA Hard Subset为其中40题，不另计benchmark。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 题型

开放问答；数值、符号表达式和可执行函数答案。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 模态

- 文本
- 数学表达式
- Python函数

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 语言

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 难度

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 公开与隐藏划分

公开1个示例；原始论文说明另70个测试挑战的答案保留私有。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

## 评测方法

### 指标

全量70题pass@1；指数采用40题Hard Subset的pass@1，均平均5次。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 评分

最终答案按专家金标准验证，复合答案须全部正确；原始论文包含数值容差、SymPy等价与函数测试。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 运行设置

AA：离线Linux sandbox提供代码执行；使用官方评分服务器，5次独立运行。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

### 官方脚本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 可比性警示

不能混用v1无agent结果、v2全70题结果和Hard Subset 40题结果；工具与题集均会改变分数。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://critpt.com/)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：v2
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking", "date": "2026-11-07", "date_type": "observed_on", "note": "AA当前指数以40题Hard Subset计10%权重，且继续跑70题全量；Epoch 2026-10-30专项评审结论为信息不足。"}, {"url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks", "date": "2026-11-07", "date_type": "observed_on", "note": "AA当前指数以40题Hard Subset计10%权重，且继续跑70题全量；Epoch 2026-10-30专项评审结论为信息不足。"}]

> AA当前指数以40题Hard Subset计10%权重，且继续跑70题全量；Epoch 2026-10-30专项评审结论为信息不足。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 饱和情况

AA全量v2最高展示84.0%；不据单个百分比断言已饱和。

[来源](https://artificialanalysis.ai/evaluations/critpt-v2)（访问 2026-11-07）

### 污染、争议与限制

作者修订了欠明确题干、错误和笔误；Epoch于2026-10-30对v2给出Not enough info，而非Verified。

[来源](https://artificialanalysis.ai/evaluations/critpt-v2)（访问 2026-11-07）；[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 衍生与版本关系

当前100项没有CritPt；v2全70题与40题Hard Subset同条记录，不另凑一项。

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://critpt.com/)（访问 2026-11-07）

### 为什么近期热门

AA当前指数以40题Hard Subset计10%权重，且继续跑70题全量；Epoch 2026-10-30专项评审结论为信息不足。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://critpt.com/)（访问 2026-11-07）

### 官方榜单入口

https://critpt.com/

[来源](https://critpt.com/)（访问 2026-11-07）

### 第三方覆盖

https://artificialanalysis.ai/evaluations/critpt-v2

[来源](https://artificialanalysis.ai/evaluations/critpt-v2)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | GPT-6 Astra (Medium) | 84.0 | CritPt v2 全70题 pass@1 (%) | 待核实（页面未明示榜表更新时间） |
| 2 | GPT-6 Astra (High) | 83.7 | CritPt v2 全70题 pass@1 (%) | 待核实（页面未明示榜表更新时间） |
| 3 | GPT-6 Astra (Xhigh) | 83.4 | CritPt v2 全70题 pass@1 (%) | 待核实（页面未明示榜表更新时间） |

[来源](https://artificialanalysis.ai/evaluations/critpt-v2)（访问2026-11-07）

### 覆盖与时效

采用AA当前v2全量页，不从旧CritPt页复制v1分数；同模型不同effort是不同配置。官网另外显示gpt-6-astra 83.1%，保留来源差异，不合并平均。

[来源](https://artificialanalysis.ai/evaluations/critpt-v2)（访问 2026-11-07）；[来源](https://critpt.com/)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- minhui.zhu@anl.gov
- mtian8@illinois.edu

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2509.26574

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2509.26574)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://critpt.com/)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://critpt.com/"}

[来源](https://critpt.com/)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://critpt.com/)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://critpt.com/)（访问 2026-11-07）
