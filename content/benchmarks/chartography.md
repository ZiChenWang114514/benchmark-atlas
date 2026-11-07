# Chartography

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: A；未核实保留标记

## 基本信息

### 简称

Chartography

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 全称

Chartography

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 基准版本

独立基准；语义版本待核实

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 论文版本

待核实

> 论文修订号尚未完成精确核实。

[来源](https://arxiv.org/abs/2608.10677)（访问2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 主板块

多模态

> Benchmark Atlas编辑分类。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 领域标签

- 专业图表

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2608.10677

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 代码

https://github.com/surge-ai/chartography

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/surgeai/chartography

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 官方主页

https://surgehq.ai/benchmarks/chartography

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 论文标题

Chartography: A Benchmark for Professional Chart Understanding

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 发起与维护

### 发起方

Surge AI

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 作者

- Suhaas Garre
- Chris Mutty
- Sushant Mehta
- Edwin Chen

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 维护方

Surge AI

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

## 设计目标

### 衡量能力

专业图表视觉感知、领域解释与多步图形推理，涵盖生存曲线、等高线、Sankey、Bode与金融图形。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 设计背景

此前图表集多偏柱、线、饼图与短链推理，难衡量真实专业决策中的读图。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 构建方式

### 题目来源

81张线上来源图、19张专家创建图；问题由对应领域从业者撰写。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 出题者背景

临床、工程、科学和金融领域专业人士。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 审核

每题由另外3名领域专家独立复核，验证答案、措辞及可接受范围。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 质量控制

两轮pilot改进出题规范；仅保留至少令一种前沿模型出现有意义失败的题。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 去污染

发布全部任务与图像、来源元数据；公开标签长期存在污染风险，未宣称隐藏测试。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 数据形式

### 题量与规模

100个任务–图像记录；98个字节不同的图像文件；12个专业领域标签。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 题型

单图与自由回答问题；数值估计、类别、集合、排序与多部分答案。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 模态

- 图像
- 文本

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 语言

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 难度

专业格式且经过难度筛选；51题有专家范围、25题精确数值、24题类别答案。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 公开与隐藏划分

公开single test split；专家推导过程用于构建审核但不在公开字段中。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 评测方法

### 指标

mean pass@1 (%)；每任务20次，100题共2000次/配置。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 评分

Gemini 3.5 Flash只看问题、标准答案和回答，不看图；专家逐题容差，多部分全对才得分。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 运行设置

单条user消息给问题和原图，无system、few-shot或代码/裁剪/缩放工具。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 官方脚本

Inspect AI评测harness见官方代码仓库。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 可比性警示

论文发布快照与实时榜不同；不把其他图表基准80–90%的分数当本基准结果。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：独立基准；语义版本待核实
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://www.anthropic.com/claude-haiku-5-5", "date": "2026-11-07", "date_type": "observed_on", "note": "Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。"}, {"url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks", "date": "2026-11-07", "date_type": "observed_on", "note": "Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。"}]

> Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。

[来源](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）；[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 污染、争议与限制

Epoch于2026-10-21给出Not enough info；这表示材料不足，不是验证通过或已证明有错。

[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 衍生与版本关系

与已有ChartQA、CharXiv不同的专业图表任务。

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 为什么近期热门

Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。

[来源](https://www.anthropic.com/claude-haiku-5-5)（访问2026-11-07）；[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 官方榜单入口

https://surgehq.ai/benchmarks/chartography

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 第三方覆盖

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | Gemini 4 Argon (High reasoning) | 71.6 | Chartography pass@1 (%) | 待核实（页面未明示榜表更新时间） |
| 2 | GPT 6 Astra (Max reasoning) | 71.0 | Chartography pass@1 (%) | 待核实（页面未明示榜表更新时间） |
| 3 | Claude Opus 5.5 (Adaptive/Max) | 66.3 | Chartography pass@1 (%) | 待核实（页面未明示榜表更新时间） |

> 抓取文本将多行rank显示成1；此处rank按当前Chartography部分分数排序，不读取随后其他基准榜表。

[来源](https://surgehq.ai/benchmarks/chartography)（访问2026-11-07）

### 覆盖与时效

当前官方榜Chartography部分前三；网页后续DAYJOB、sudo、GDP.xlsx榜单均不属于此条。页面未给榜表自写更新日。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- benchmarks@surgehq.ai

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2608.10677

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://surgehq.ai/benchmarks/chartography"}

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）
