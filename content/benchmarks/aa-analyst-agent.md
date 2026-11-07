# AA-AnalystAgent

> 核验日期：2026-11-07 Asia/Shanghai（UTC+8）。未知保留待核实；访问日不是测量日。

已核验存在；近期热门新建条目，未核实字段保留标记；trending: B

核心不是单次算对，而是同一道真实分析题独立做五遍都可靠。80题按领域和工作流分布；pass^5、pass@1与pass@5必须分开阅读。

## 基本信息

### 简称

AA-AnalystAgent

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 全称

AA-AnalystAgent Benchmark

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 基准版本

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 论文版本

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 发布日期

2026-08-10（官方首发文章日；页面未提供精确时刻）

[来源1](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）

### 主板块

Agent

> Benchmark Atlas 编辑归档。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 领域标签

- 数据分析
- 表格与文档定量分析

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 许可证

Stirrup运行框架MIT；题目、参考答案与输入文件明确不公开；正式评测数据许可待核实，不能将框架许可外推。

> 字段状态：待核实

[来源1](https://github.com/ArtificialAnalysis/Stirrup/blob/main/LICENSE)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 论文

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 官方代码

https://github.com/ArtificialAnalysis/Stirrup

> agent harness，非题集。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 数据地址

未公开：官方明确题目、参考答案和源文件不对外发布；主页仅展示示例。

> 字段状态：未公开

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 官方入口

https://artificialanalysis.ai/evaluations/aa-analyst-agent

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 论文标题

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

## 发起与维护

### 发起方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 作者

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 维护方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 资助方

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 设计目标

### 衡量能力

基于真实表格与文档，像业务/数据分析师那样完成端到端定量分析，包括解读来源、判断例外与方法选择。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 设计背景

分析师工作不仅是算术正确，还要选对来源、解释例外并稳定重复得出答案；用5次全对而非偶然成功衡量可托付程度。

[来源1](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）

## 构建方式

### 题目来源

真实表格与文档，包括医疗支出、贸易与商品统计、水文天气、财政拨款、能源成本、财务模型与项目排期；80题跨14业务及科学领域。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 出题者背景

Artificial Analysis团队组织并人工编写参考答案；具体命题者职业资历待核实。

> 字段状态：待核实

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 审核流程

人工撰写参考答案，由Artificial Analysis独立验证；参考答案不提供给作答agent。

> 官方仅披露参考答案验证，不据此声称有双盲外部专家逐题审查。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 质量控制

每题5次独立运行；数值等价预检查仅能覆盖确定正确的答案，其他情况保留LLM裁判判决；格式、单位和所要求精度均纳入判分。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 去污染

题目与参考答案私有以降低污染风险

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 数据形式

### 题量与规模

80 题、14 个业务与科学领域，每题绑定一组源表格与文档

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 题型

定量问答（数值答案）

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 模态

- 表格
- 文档
- 文本

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 语言

公开示例题与运行/评分提示为英语；完整私有题库语种分布待核实。

> 字段状态：待核实

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 难度

不以学历分级；覆盖来源查找诊断、筛选汇总、比率/趋势/敏感性、损益模型、现金/资产负债表/估值五种工作流。

[来源1](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）

### 公开与隐藏划分

私有，示例题公开（如加州 Medicaid 支出报告题）

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 评测方法

### 指标

主指标 pass^5（5次全对比例），并报告 pass@1、pass@5

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 评分

逐次二元判分：每个答案均交Gemini 3 Flash (Reasoning)裁判；确定性数值等价预检查可将符合单位与精度的答案覆盖为通过，不能覆盖为失败。pass^5为80题中五次均正确的比例；pass@1为所有尝试平均正确率；pass@5为至少一次正确的题目比例。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 运行设置

Stirrup；每题5次独立运行，每次最多100轮；隔离Linux/Python3.12，提供题目源文件、代码执行、URL抓取、图像查看（视觉模型）和最终答案提交；只提交数值或标签，不附解释。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 官方脚本

https://github.com/ArtificialAnalysis/Stirrup

> 公开通用harness及完整提示模板；不是已公开80题完整评测实现。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 可比性警示

独立榜，不计入 AA Intelligence Index；pass^5 与 pass@1 排名差异显著。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 Asia/Shanghai（UTC+8）

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 最新版本与采用证据

```json
{
  "version": "待核实",
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
      "date": "2026-11-07",
      "organization": "Artificial Analysis",
      "note": "当前方法页将AA-AnalystAgent列为正在实施的评测，披露任务或评分协议。"
    },
    {
      "url": "https://artificialanalysis.ai/evaluations",
      "date": "2026-11-07",
      "organization": "Artificial Analysis",
      "note": "当前公开评测目录单列AA-AnalystAgent，不是新闻提及。"
    }
  ],
  "trending": {
    "heat_confidence": "B",
    "summary": "AA 当前独立80题数据分析榜，用 pass^5 强调稳定性。"
  }
}
```

> 近期热门证据取自候选研究与本轮重开页面；B级：主要为单一机构在用，不代表行业广泛采纳。

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/evaluations)（访问2026-11-07）

### 修订历史

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 饱和情况

本轮官网pass^5最高60.0%，pass@1最高71.3%、pass@5最高86.3%；不同指标榜首不同，不把一次答对视为稳定解决。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 污染与争议

题目、答案与源文件私有降低直接泄漏风险，但也限制第三方重跑；首发失败分析57%是过早锚定错误解释（1567条失败轨迹、多标签分类），不是全体任务57%错误。

[来源1](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### 版本与衍生关系

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 Asia/Shanghai（UTC+8）

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 官方榜单

https://artificialanalysis.ai/evaluations/aa-analyst-agent

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 分轨结果

#### pass^5

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 3.7 Flash (High) | 60.0 | 五次全对任务比例 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |
| 2 | Claude Sonnet 5.5 (Max, Default Fallback) | 57.5 | 五次全对任务比例 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |
| 2 | Claude Fable 5.1 (Max, Default Fallback) | 57.5 | 五次全对任务比例 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |



#### pass@1

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Inkling 2 Small | 71.3 | 平均尝试正确率 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |
| 2 | Gemini 3.7 Flash (High) | 70.5 | 平均尝试正确率 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |
| 3 | Claude Sonnet 5.5 (Max, Default Fallback) | 69.5 | 平均尝试正确率 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |



#### pass@5

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Inkling 2 Small | 86.3 | 至少一次正确任务比例 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |
| 2 | GPT-6 Luna (Max) | 85.0 | 至少一次正确任务比例 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |
| 3 | Claude Haiku 5.5 (Max) | 83.8 | 至少一次正确任务比例 (%) | [原表](https://artificialanalysis.ai/evaluations/aa-analyst-agent) · 2026-11-07 |



> 字段状态：待核实

> 已重读公开HTML摘要确认三个分轨；各模型实际运行时间及榜单整体更新时间待核实。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 覆盖说明

AA 为基准创建者，无独立复测；采集日2026-11-07，27/52模型展示。pass@1 第一为 Inkling 2 Small 71.3%。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 公开反馈

https://github.com/ArtificialAnalysis/Stirrup/issues

> 仅通用harness问题入口；不是私有题库的专属问题单。

[来源1](https://github.com/ArtificialAnalysis/Stirrup)（访问2026-11-07）

### 官方社交

- https://x.com/ArtificialAnlys
- https://www.linkedin.com/company/artificial-analysis/

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 隐私说明/政策

https://artificialanalysis.ai/privacy-policy

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### PDF SHA-256

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### PDF字节数

待核实

> 字段状态：待核实

> 本轮实际阅读评测页、首发文章与方法页；所读材料未链接独立原始论文，不由此断言论文不存在。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）；[来源2](https://artificialanalysis.ai/articles/aa-analyst-agent)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### Drive文件夹

待核实

> 字段状态：待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "首发文章",
    "url": "https://artificialanalysis.ai/articles/aa-analyst-agent",
    "accessed": "2026-11-07"
  },
  {
    "type": "完整运行与评分提示",
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://artificialanalysis.ai/methodology/intelligence-benchmarking#aa-analyst-agent)（访问2026-11-07）

### Drive论文副本

待核实

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai (UTC+8)",
    "change": "Round2 q0：实际重读原始论文PDF、官方README/LICENSE、可用HF卡与排行榜；补方法、版本/样本/指标冲突及分轨结果，保留未核实信息。"
  }
]
```

[来源1](https://artificialanalysis.ai/evaluations/aa-analyst-agent)（访问2026-11-07）
