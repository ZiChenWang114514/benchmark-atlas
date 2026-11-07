# GDPval (GDPval-AA v2.1)

> 核验：2026-11-07（KST / Asia/Seoul）。官方资料中文改写；待核实不等于未公开。原始数据与第三方实现、历史论文与当前榜单分轨。

编辑状态：研究快照；trending: A；未核实字段保留标记

## 基本信息

### 简称

GDPval (GDPval-AA v2.1)

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 全称

GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 基准版本

原始GDPval；AA实现为GDPval-AA v2.1，分轨记录

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档，不作为官方分类。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 领域标签

- 知识工作
- 金融
- 法律

> 编辑标签

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2510.04374

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 官方代码

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/openai/gdpval

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 官方主页

https://huggingface.co/datasets/openai/gdpval

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 论文标题

GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 发起与维护

### 发起方

OpenAI

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 合作方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 作者

Tejal Patwardhan、Rachel Dias、Elizabeth Proehl等（完整作者见论文）

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 维护方

原始数据：OpenAI；独立实现：Artificial Analysis

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 资助方

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

## 设计目标

### 衡量能力

以真实职业任务衡量经济相关知识工作的交付物质量。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 设计背景

学术短答案测试难以覆盖职业工作中的文件处理、审美与可用性。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 构建方式

### 题目来源

专业从业者实际工作产物，按O*NET工作活动选择9个产业的44个职业。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 出题者背景

专家至少4年职业经验，平均14年；通过面试、背景核查、训练与测验。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 审核流程

自动筛查加通才初审、同行职业专家复审、迭代最终审核。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 质量控制

全体1,320任务平均5轮、至少3轮人工审核。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 去污染

公开gold子集已清理出题者识别信息；不能据此认定完全无训练污染。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 数据形式

### 题量与规模

全量1,320任务；公开gold子集220任务，每职业5题。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 题型

文本请求、参考文件、职业交付物；文件包括文档、表格、幻灯片、CAD及音视频。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 模态

- 文本
- 文档
- 图像
- 音频
- 视频
- 表格

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 语言

公开样例为英语职业任务；多语言覆盖待核实。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 难度

职业长程任务；不等同完整职业可被自动化。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 公开与隐藏划分

220任务gold子集公开；其余全量数据的可获取性待核实。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 评测方法

### 指标

原始轨：模型交付物相对人类专家产物的盲评胜率；AA轨：成对模型交付物Elo。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 评分

原始推荐职业专家成对比较；自动裁判为实验代理而非完全替代专家。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 提示与运行设置

AA使用Stirrup agent循环，提供shell与网页浏览；盲化两份输出由LLM裁判比较。

[来源1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

### 官方评测脚本

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 可比性警示

原始对人类胜率不等于GDPval-AA v2.1 Elo；harness、预算与裁判差异须分轨。

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 当前版本与热度证据

- **version**：原始GDPval；AA实现为GDPval-AA v2.1，分轨记录
- **heat_confidence**：A
- **why_trending**：候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。
- **evidence_2026_h2**：
  - **url**：https://epoch.ai/data/eci-documentation/data
  - **date**：2026-11-07
  - **date_type**：observed_on
  - **organization**：Epoch AI
  - **note**：当前ECI组成明确列出该benchmark；纳入不等于本轮运行。
  - **url**：https://artificialanalysis.ai/evaluations/gdpval-aa
  - **date**：2026-11-07
  - **date_type**：observed_on
  - **organization**：Artificial Analysis
  - **note**：当前v2.1独立评测榜明确展示前沿模型Elo。

[来源1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

### 版本与材料差异

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 污染与争议

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 衍生与版本关系

GDPval数据与AA评测实现同条分轨，不拆成两项；AA v5已移出综合指数但仍单独评测。

> 编辑去重口径；具体版本差异仍以官方材料为准。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 为什么近期热门

候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。

- 2026-11-07（observed_on）：当前ECI组成明确列出该benchmark；纳入不等于本轮运行。 [来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

- 2026-11-07（observed_on）：当前v2.1独立评测榜明确展示前沿模型Elo。 [来源](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 官方榜单

https://huggingface.co/datasets/openai/gdpval

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 独立评测覆盖

https://artificialanalysis.ai/evaluations/gdpval-aa

[来源1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

### 核验结果

- **rank**：1
- **model**：Claude Opus 5.5 (Max, Default Fallback)
- **score**：1866
- **metric**：GDPval-AA v2.1 Elo
- **source_url**：https://artificialanalysis.ai/evaluations/gdpval-aa
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：官方榜单快照
- **rank**：2
- **model**：Kimi K3.1 Pro
- **score**：1858
- **metric**：GDPval-AA v2.1 Elo
- **source_url**：https://artificialanalysis.ai/evaluations/gdpval-aa
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：官方榜单快照
- **rank**：3
- **model**：Muse Wonder Full (Max)
- **score**：1857
- **metric**：GDPval-AA v2.1 Elo
- **source_url**：https://artificialanalysis.ai/evaluations/gdpval-aa
- **source_date**：待核实
- **collected_at**：2026-11-07 KST
- **result_type**：官方榜单快照

[来源1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

### 覆盖与时效说明

AA为独立实现；v2.1锚定DeepSeek V4.1 Flash (max)=1600。榜表模型发行月不是榜单更新时间。

[来源1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

tejal@openai.com（论文公开通讯渠道）

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 官方社交／讨论渠道

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2510.04374

[来源1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### Drive资料文件夹

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### 其他文档

待核实

> 已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

### Drive PDF归档

待核实（本轮未上传）

## 变更记录

### 变更记录

- **date**：2026-11-07
- **timezone**：KST / Asia/Seoul
- **change**：首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。

[来源1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）
