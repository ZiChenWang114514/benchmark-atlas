# Chartography

> Benchmark Constitution，深度复核：2026-11-08。

Chartography聚焦专业人士真正用于判断的图形：生存曲线、等高线、Sankey、Bode和金融图等，不局限于常规柱线饼图。100题由从业者编写并经另外三名专家验证。原论文固定July 2026快照与当前官网已明显不同；论文每题20次、README榜单示例10次的差异也需保留，不能将45%历史上限当成当前能力边界。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 基本信息

### 简称

Chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 全称

Chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 沿用官方名称；不将论文标题臆造为全称。

### 版本边界

独立基准；语义版本待核实

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 论文版本

arXiv v1（2026-08-11）

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-08）

### 发布日期

2026-08-11 17:57:25 （arXiv首次提交；非推定项目首次上线日）

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-08）

### 板块

多模态

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> Benchmark Atlas编辑分类。

### 领域

```json
[
 "专业图表"
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 许可与限制

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

### 论文

https://arxiv.org/abs/2608.10677

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 官方代码

https://github.com/surge-ai/chartography

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 数据入口

https://huggingface.co/datasets/surgeai/chartography

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 官方主页

https://surgehq.ai/benchmarks/chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 论文题名

Chartography: A Benchmark for Professional Chart Understanding

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 发起与维护

### 发起方

Surge AI

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 合作机构

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

### 作者

```json
[
 "Suhaas Garre"
 "Chris Mutty"
 "Sushant Mehta"
 "Edwin Chen"
]
```

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 维护入口

Surge AI

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 资助披露

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

## 设计目标

### 测量对象

专业图表视觉感知、领域解释与多步图形推理，涵盖生存曲线、等高线、Sankey、Bode与金融图形。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 既有评测的缺口

此前图表集多偏柱、线、饼图与短链推理，难衡量真实专业决策中的读图。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 构建方式

### 题源

81张线上来源图、19张专家创建图；问题由对应领域从业者撰写。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 构建人员

临床、工程、科学和金融领域专业人士。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 审核

每题由另外3名领域专家独立复核，验证答案、措辞及可接受范围。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 质控

两轮pilot改进出题规范；仅保留至少令一种前沿模型出现有意义失败的题。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 去污染及边界

发布全部任务与图像、来源元数据；公开标签长期存在污染风险，未宣称隐藏测试。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 数据形式

### 规模与计数口径

100个任务–图像记录；98个字节不同的图像文件；12个专业领域标签。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 题型

单图与自由回答问题；数值估计、类别、集合、排序与多部分答案。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 模态

```json
[
 "图像"
 "文本"
]
```

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 语言

公开论文和README任务提示使用英语；HF卡本次401无法读取，完整数据语言元数据仍待核实。

[来源1](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）；[来源2](https://github.com/surge-ai/chartography)（访问 2026-11-08）

### 难度

专业格式且经过难度筛选；51题有专家范围、25题精确数值、24题类别答案。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 划分与公开范围

公开single test split；专家推导过程用于构建审核但不在公开字段中。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 评测方法

### 指标

mean pass@1 (%)。论文固定July 2026快照每题20次、100题每配置2000次；当前README复现榜单示例为每题10次，必须注明二者版本差异。pass@K与pass^K另列，不互换。

[来源1](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）；[来源2](https://github.com/surge-ai/chartography/blob/main/README.md)（访问 2026-11-08）

### 评分

Gemini 3.5 Flash只看问题、标准答案和回答，不看图；专家逐题容差，多部分全对才得分。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 提示与运行条件

单条user消息给问题和原图，无system、few-shot或代码/裁剪/缩放工具。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 官方评测入口

Inspect AI评测harness见官方代码仓库。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 可比性边界

论文发布快照与实时榜不同；不把其他图表基准80–90%的分数当本基准结果。

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

## 最新情况

### 复核时间

2026-11-08

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）

### 当前版本

```json
{
 "version": "独立基准；语义版本待核实"
 "heat_confidence": "A"
 "evidence_2026_h2": [
 {
 "url": "https://www.anthropic.com/claude-haiku-5-5"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。"
 }
 {
 "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "note": "Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。"
 }
 ]
}
```

[来源1](https://www.anthropic.com/claude-haiku-5-5)（访问 2026-11-07）；[来源2](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

> Anthropic在2026-10-07 Haiku 5.5发布表实际报告Chartography；Epoch 2026-10-21进行评审，结论信息不足。

### 论文修订与后续使用

```json
{
 "arxiv_revisions": [
 {
 "version": "v1"
 "submitted_at": "2026-08-11"
 }
 ]
}
```

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-08）

### 饱和情况

论文启动快照最高45.0%，当前官网最高71.6%；这说明分数有进步，不足以单独认定专业图表任务已饱和，且运行次数/配置需对齐。

[来源1](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）；[来源2](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）

### 风险与冲突

论文July 2026启动快照最高45.0%，当前官网前三71.6/71.0/66.3，README仍写“没有模型超过45%”，不能将旧断言用于当前榜。README榜单配置10次与论文20次不同。HF返回401，未声称读到其许可；仓库根目录未发现LICENSE文件，许可待核实。

[来源1](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）；[来源2](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）；[来源3](https://github.com/surge-ai/chartography/blob/main/README.md)（访问 2026-11-08）

### 衍生与后续工作

与已有ChartQA、CharXiv不同的专业图表任务。

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

## 榜单快照

### 快照时间

2026-11-08 （实际复核日；批次标签2026-11-07）

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）

### 官方榜入口

https://surgehq.ai/benchmarks/chartography

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 第三方榜入口

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

### 逐轨结果

```json
[
 {
 "rank": 1
 "model": "Gemini 4 Argon (High reasoning)"
 "score": 71.6
 "metric": "Chartography pass@1 (%)"
 "source_url": "https://surgehq.ai/benchmarks/chartography"
 "source_date": "待核实（页面未明示榜表更新时间）"
 "collected_at": "2026-11-07 "
 "track": "官网当前Chartography榜／配置如模型名"
 "unit": "%"
 "accessed": "2026-11-08"
 }
 {
 "rank": 2
 "model": "GPT 6 Astra (Max reasoning)"
 "score": 71.0
 "metric": "Chartography pass@1 (%)"
 "source_url": "https://surgehq.ai/benchmarks/chartography"
 "source_date": "待核实（页面未明示榜表更新时间）"
 "collected_at": "2026-11-07 "
 "track": "官网当前Chartography榜／配置如模型名"
 "unit": "%"
 "accessed": "2026-11-08"
 }
 {
 "rank": 3
 "model": "Claude Opus 5.5 (Adaptive/Max)"
 "score": 66.3
 "metric": "Chartography pass@1 (%)"
 "source_url": "https://surgehq.ai/benchmarks/chartography"
 "source_date": "待核实（页面未明示榜表更新时间）"
 "collected_at": "2026-11-07 "
 "track": "官网当前Chartography榜／配置如模型名"
 "unit": "%"
 "accessed": "2026-11-08"
 }
 {
 "rank": 1
 "model": "GPT-5.6 Sol (Max reasoning)"
 "score": 45.0
 "metric": "mean pass@1 (%)"
 "track": "论文Table 3／July 2026／20 trials no tools"
 "source_url": "https://arxiv.org/pdf/2608.10677"
 "accessed": "2026-11-08"
 "unit": "%"
 "source_context": "冻结启动快照，不与当前网页榜混排"
 "ci95_half_width_pp": 1.1
 }
 {
 "rank": 2
 "model": "GPT-5.6 Sol (default)"
 "score": 39.5
 "metric": "mean pass@1 (%)"
 "track": "论文Table 3／July 2026／20 trials no tools"
 "source_url": "https://arxiv.org/pdf/2608.10677"
 "accessed": "2026-11-08"
 "unit": "%"
 "ci95_half_width_pp": 1.2
 }
 {
 "rank": 3
 "model": "Gemini 3.5 Flash"
 "score": 35.9
 "metric": "mean pass@1 (%)"
 "track": "论文Table 3／July 2026／20 trials no tools"
 "source_url": "https://arxiv.org/pdf/2608.10677"
 "accessed": "2026-11-08"
 "unit": "%"
 "ci95_half_width_pp": 1.3
 }
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）

### 覆盖边界

当前官网前三已重新读取，另列论文July 2026历史首名；网页表未给可核实逐行运行日期。HF访问401、根目录无LICENSE，不能由公开可见推定许可。

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）；[来源3](https://github.com/surge-ai/chartography)（访问 2026-11-08）

## 联系方式

### 公开研究联系

```json
[
 "benchmarks@surgehq.ai"
]
```

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

### 项目反馈

https://github.com/surge-ai/chartography/issues

[来源1](https://github.com/surge-ai/chartography)（访问 2026-11-08）

### 官方社交入口

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

### 联系信息边界

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2608.10677

[来源1](https://arxiv.org/abs/2608.10677)（访问 2026-11-07）

> 原始论文PDF入口；未下载或上传，哈希与字节数待核实。

### PDF SHA-256

77ef3accf5fe10db02baaa5ae6a7e8f9783cea449a1b8c2f9b8ea3bc803990fb

[来源1](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）

> 下载PDF字节的SHA-256；不表示已上传。

### PDF字节数

1575099

[来源1](https://arxiv.org/pdf/2608.10677)（访问 2026-11-08）

> 下载PDF字节数；归档仍待核实。

### 目录

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

### 其他官方材料

```json
[
 {
 "type": "官方网页方法与榜单（非PDF）"
 "url": "https://surgehq.ai/benchmarks/chartography"
 }
]
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

### 论文归档

待核实

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-07）

## 变更记录

```json
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
```

[来源1](https://surgehq.ai/benchmarks/chartography)（访问 2026-11-08）
