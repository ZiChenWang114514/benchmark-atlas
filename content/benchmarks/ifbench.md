# IFBench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: B；未核实保留标记

## 基本信息

### 简称

IFBench

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 全称

IFBench

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 论文版本

待核实

> 论文修订号尚未完成精确核实。

[来源](https://arxiv.org/abs/2507.02833)（访问2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 主板块

语言

> Benchmark Atlas编辑分类。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 领域标签

- 语言

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2507.02833

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 代码

https://github.com/allenai/IFBench

[来源](https://arxiv.org/abs/2507.02833)（访问2026-11-07）

### 数据集

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 官方主页

https://github.com/allenai/IFBench

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 论文标题

Generalizing Verifiable Instruction Following

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

## 发起与维护

### 发起方

Allen Institute for Artificial Intelligence、University of Washington

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 作者

- Valentina Pyatkin
- Saumya Malik
- Victoria Graf
- Hamish Ivison
- Shengyi Huang
- Pradeep Dasigi
- Nathan Lambert
- Hannaneh Hajishirzi

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 维护方

AllenAI IFBench项目

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 资助

NSF IIS-2044660

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

## 设计目标

### 衡量能力

对58种新颖可程序验证的域外输出约束泛化，包括计数、比例、单词、句子、格式、自定义与复制。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 设计背景

IFEval的25种约束可能被过拟合；IFBench不是IFEval别名或新版本。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

## 构建方式

### 题目来源

人工收集用户反馈及核心技能需求设计约束，组合未发布的WildChat留出提示。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 出题者背景

指令遵循与后训练研究者；兼容性标注者具体资历待核实。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 审核

每实例人工检查提示与约束兼容，防止无法同时满足。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 质量控制

为约束编写Python验证函数；排除训练/测试约束重合。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 去污染

测试58种新约束与IFTrain 29种训练约束分开，原始WildChat提示留出；公开后仍需防泄漏。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

## 数据形式

### 题量与规模

原始IFBench 300提示，每个含1或2约束；AA评294题。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 题型

开放文本输出，单轮任务+约束；多轮先回答原任务后按约束改写。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 模态

- 文本

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 语言

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 难度

旨在测未见约束泛化，不以IFEval得分推断能力。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 公开与隐藏划分

IFBench评测300提示；IFTrain 29约束与训练提示为独立材料，不混成测试规模。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

## 评测方法

### 指标

strict/loose accuracy；论文报告prompt-level loose accuracy，AA采用规则评分pass@1。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 评分

strict直接验证，loose允许删首末行和部分字体标记后再检验；题级与约束级口径不可混用。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 运行设置

原论文通常temperature 0，思考模型调整token并移除思维链；DeepSeek R1用0.6/top_p .95，o3温度1。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 官方脚本

AllenAI/IFBench含约束验证代码；本轮GitHub页仅返回摘要，不据此填许可证。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 可比性警示

AA 294题×5次不同于原始300提示；单/多轮与strict/loose差异须保留。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：待核实
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking", "date": "2026-11-07", "date_type": "observed_on", "note": "AA当前仍将IFBench列为额外评测，294题×5次；不是当前v5指数成分。热度B主要来自单一第三方持续评测。"}, {"url": "https://artificialanalysis.ai/evaluations/ifbench", "date": "2026-11-07", "date_type": "observed_on", "note": "AA当前仍将IFBench列为额外评测，294题×5次；不是当前v5指数成分。热度B主要来自单一第三方持续评测。"}]

> AA当前仍将IFBench列为额外评测，294题×5次；不是当前v5指数成分。热度B主要来自单一第三方持续评测。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[来源](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 污染、争议与限制

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 衍生与版本关系

与已收录ifeval不同：IFBench测试域外约束泛化，不能当IFEval新名字。

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 为什么近期热门

AA当前仍将IFBench列为额外评测，294题×5次；不是当前v5指数成分。热度B主要来自单一第三方持续评测。

[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源](https://artificialanalysis.ai/evaluations/ifbench)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 官方榜单入口

https://github.com/allenai/IFBench

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 第三方覆盖

https://artificialanalysis.ai/evaluations/ifbench

[来源](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | Grok 4.3 (Medium) | 83.3 | AA IFBench pass@1 (%) | 待核实（页面未明示榜表更新时间） |
| 2 | Grok 4.20 0309 (Reasoning) | 82.9 | AA IFBench pass@1 (%) | 待核实（页面未明示榜表更新时间） |
| 3 | MiniMax-M3 | 82.9 | AA IFBench pass@1 (%) | 待核实（页面未明示榜表更新时间） |

[来源](https://artificialanalysis.ai/evaluations/ifbench)（访问2026-11-07）

### 覆盖与时效

AA独立运行；第二、三相同展示精度，不声称显著优劣。无页面自写更新日，模型发布日期不替代评测时间。

[来源](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- valentinap@allenai.org

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### 公开反馈

https://github.com/allenai/IFBench/issues

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2507.02833

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://github.com/allenai/IFBench"}

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://github.com/allenai/IFBench)（访问 2026-11-07）
