# Finance Agent

> Benchmark Constitution · 研究快照 2026-11-07（KST / Asia/Seoul）。采集时间不等于成绩实跑或榜单更新时间。

Finance Agent v2.1要求智能体检索公司申报、整合跨文档事实并遵守金融分析惯例。其关键不是写出听起来合理的金融解释，而是先通过dealbreaker门控，再按rubric取得部分信用；旧v1论文与HF卡不得代替当前v2.1协议。

编辑状态：研究快照；trending: B；未知信息保留待核实。

## 基本信息

### 简称

Finance Agent

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 全称

Finance Agent Benchmark

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 基准版本

v2.1

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 论文版本

arXiv v1（论文修订，不等于数据集版本）

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 发布日期

原始论文初稿 2025-05-21T03:22:10+09:00（KST）；v2.1独立发布日期待核实

状态：待核实。

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 主板块

Agent

说明：编辑主板块归档，不据此限制跨学科覆盖。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 领域标签

- 金融

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 许可与范围

v2 harness仓库LICENSE为MIT；原始v1 HF数据卡CC BY4.0；v2.1榜页Dataset元数据亦列CC BY4.0，但私有题集的访问/再分发条款须按许可另核，不将网页声明当成私有数据开放承诺。

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/LICENSE)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）；[一手资料3](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 论文

https://arxiv.org/abs/2508.00828

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 代码

https://github.com/vals-ai/finance-agent-v2

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）


### 数据入口

- **v2_public_questions**：https://github.com/vals-ai/finance-agent-v2/blob/main/data/public.txt
- **v1_HF**：https://huggingface.co/datasets/vals-ai/finance_agent_benchmark
- **v2_1_test_access**：官方页面：Test私有；Validation需许可

说明：本轮已读取的公开HF卡revision: 1f80cefae847f2e8b6bdf773f789c90f70293f78；只固定公开卡/仓库状态，不外推为私有测试版本。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料3](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）


### 官方主页

https://www.vals.ai/benchmarks/fabv2-1

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 论文标题

Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


## 发起与维护

### 发起/作者单位

Vals AI

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 合作与支持

待核实

状态：待核实。

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 作者

原始论文：Antoine Bigeard、Rayan Krishnan、Shirley Wu、Langston Nashold；不把旧论文作者名单当v2.1完整人员名单。

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 维护方

Vals AI

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 资助

待核实

状态：待核实。

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 设计目标

### 衡量能力

初级金融分析师级公开公司文件检索、跨源综合、精确计算与建模。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 设计背景

需实际工具调用和隐含金融惯例，不只静态单文档问答。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 构建方式

### 题目来源

公开公司申报与资料；领域专家编写，强调确定答案、跨源综合、行业惯例及脚注精度。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 出题者背景

问题目标为投行2–3年分析师水平；金融行业专家参与。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 审核流程

专家复审问题与rubric，v2.1修正/删除问题并更新检查。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 质量控制

dealbreaker关键事实门控，任一关键项失败整题零分。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 污染控制

测试集持续私有以防过拟合；公开/许可验证样本不进入本榜结果。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 数据形式

### 题量

公开27、许可Private Validation450、私有Test449。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 任务形式

九类分析师任务，涵盖comparables、precedents、earnings、disclosure、modeling等。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 模态

- 文本
- 财报
- 结构化工具返回

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 语言

官方README的公开问题与论文示例为英语；完整v2.1私有集的语言分布待核实

状态：待核实。

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 难度与分层

跨多文档、更严格数字容差和需要隐含洞察的分析。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 公开与隐藏划分

公开27题；验证450题可许可获取；Test449题明确保持私有，仅此测试集用于榜单。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 评测方法

### 指标

主指标dealbreaker-gated weighted Partial Credit；次指标All-Pass。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 评分

关键dealbreaker失败整题零分，否则严重程度加权检查得分；三模型jury评阅。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 提示与运行协议

每任务2小时；六工具edgar_search/web_search/parse_html_page/retrieve_information/calculator/price_history。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 评测脚本

https://github.com/vals-ai/finance-agent-v2；finance-agent CLI，默认配置为作者运行配置；需获批Vals平台访问和各数据工具服务。

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 可比性警示

v2.1与v2不可直接比较；旧论文537题及原始平衡准确率不代表v2.1。仓库README目前列五类工具、官网方法列六工具（含calculator），复现必须固定实际工具配置，不把文档列表差异默认为协议一致。

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料3](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul（资料快照日期）

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 版本与采用证据

- **version**：v2.1
- **heat_confidence**：B
- **evidence_2026_h2**：- - **url**：https://www.vals.ai/benchmarks/fabv2-1
    - **date**：2026-11-05
    - **note**：Vals当前37模型榜；热度主要来自单一机构，不称行业广泛采用。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 材料沿革

- **arxiv_history**：- - **version**：v1
    - **submitted_at_kst**：2025-05-21T03:22:10+09:00
    - **timezone**：Asia/Seoul (KST)
- **v2_1_method_changes**：v2.1更新题目/rubric、替换jury为GPT-6.1 Sol/Gemini3.8 Flash/Claude Sonnet5.5，hedged多候选答案按失败处理。

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）；[一手资料2](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 饱和情况

当前v2.1最高Partial Credit为67.85%，不是All-Pass率；仍有大量关键检查未满足，不能以部分信用成绩推断金融研究可自主可靠交付。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 污染与局限

Test449题保持私有以降低过拟合；原v1 HF卡是537题时代说明，不能用它的规模或许可推断当前私有集完整内容。hedged多候选答案按失败，jury与rubric更新使v2/v2.1不可直接比较。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）


### 版本/衍生关系

v1、v1.1、v2和v2.1为同一Finance Agent系列的历史版本；Excel Modeling是相关但不同任务，不并入本题数。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul（快照日，非实跑日）

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 官方榜

https://www.vals.ai/benchmarks/fabv2-1

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 其他评测入口

待核实

状态：待核实。

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 分轨结果（结构化快照）

```json
[
  {
    "rank": 1,
    "model": "Claude Opus 5.5",
    "score": "67.85%",
    "metric": "v2.1 Partial Credit（表标Accuracy）",
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 2,
    "model": "Gemini 4 Argon",
    "score": "67.66%",
    "metric": "v2.1 Partial Credit（表标Accuracy）",
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  },
  {
    "rank": 3,
    "model": "Wonder Full",
    "score": "67.58%",
    "metric": "v2.1 Partial Credit（表标Accuracy）",
    "source_url": "https://www.vals.ai/benchmarks/fabv2-1",
    "source_date": "2026-11-05",
    "collected_at": "2026-11-07 KST",
    "result_type": "官方页面结果；采集日期不等于榜单更新时间。"
  }
]
```

[榜单原始资料](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）

### 覆盖范围

官方页面结果；采集日期不等于榜单更新时间。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 联系方式

### 公开研究邮箱

- contact@vals.ai

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 问题反馈

https://github.com/vals-ai/finance-agent-v2/issues

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）


### 机构公开渠道

https://x.com/ValsAI（维护机构账号）

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 隐私政策

待核实

状态：待核实。

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


## 原始文件

### 论文PDF

https://arxiv.org/pdf/2508.00828

说明：原始v1论文，不是v2.1的完整新协议。

[一手资料1](https://arxiv.org/abs/2508.00828)（访问 2026-11-07）


### 源站PDF SHA-256

bbb021c3a2070c905a6c0fd9a7404aa9a27d2973cf16f621e620d098b4a06740

说明：实际下载的源站PDF字节摘要；不据此声称Drive副本已更新。

[一手资料1](https://arxiv.org/pdf/2508.00828)（访问 2026-11-07）


### 源站PDF字节数

1321074

[一手资料1](https://arxiv.org/pdf/2508.00828)（访问 2026-11-07）


### Drive资料目录

待核实

状态：待核实。

说明：本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[一手资料1](https://www.vals.ai/benchmarks/fabv2-1)（访问 2026-11-07）


### 其他官方资料

- - **type**：本轮核验的官方原始资料
  - **url**：https://github.com/vals-ai/finance-agent-v2/blob/main/README.md
  - **accessed**：2026-11-07
- - **type**：本轮核验的官方原始资料
  - **url**：https://huggingface.co/datasets/vals-ai/finance_agent_benchmark
  - **accessed**：2026-11-07

[一手资料1](https://github.com/vals-ai/finance-agent-v2/blob/main/README.md)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/vals-ai/finance_agent_benchmark)（访问 2026-11-07）


### Drive PDF归档

待核实

本轮仅核对源站PDF和已有归档引用，未上传或覆盖Drive文件。

## 变更记录

- - **date**：2026-11-07
  - **timezone**：KST / Asia/Seoul
  - **change**：按官方材料新建中文条目；区分热度、质量和不同版本评分。
- - **date**：2026-11-07
  - **timezone**：Asia/Seoul (KST)
  - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位官方README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
