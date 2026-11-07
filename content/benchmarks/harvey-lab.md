# Harvey LAB（Legal Agent Benchmark）

> Benchmark Constitution · 核查日期：2026-11-07（KST / Asia/Seoul）。未知仍保留待核实；访问日不冒充实验日。

Harvey LAB要求agent处理案卷并交付可审核的法律文件，测的是长程工作完成而非孤立法律选择题。公开任务库现已大于首发规模，但AA与Vals榜仍各用120个私有任务；双裁判all-pass与AA幻觉门控是独立赛道。

导读来源：[https://artificialanalysis.ai/evaluations/harvey-lab-aa](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）; [https://www.vals.ai/benchmarks/hlab](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

## 1. 基本信息

### 简称

Harvey LAB（Legal Agent Benchmark）

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 全称

Harvey's Legal Agent Benchmark (LAB)

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 数据/协议版本

开源仓库 lab-core v1.3.0；AA 实现为 Harvey LAB-AA v1.1；Vals 实现为 HLAB-Vals-1.1

说明：三处“v1.1”分属不同实现，彼此不可比。

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[3](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 论文版本

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 发布日期及口径

2026-05-06（Harvey 官方博客）

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 主板块

Agent

说明：Benchmark Constitution 编辑归档。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 子领域

- 法律
- 专业知识工作

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 许可证

MIT（harvey-labs 仓库）

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 论文

待核实

说明：官方以博客发布，未见独立论文。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 代码入口

https://github.com/harveyai/harvey-labs

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 数据入口

https://github.com/harveyai/harvey-labs

说明：开源任务集在仓库 tasks/ 目录。

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 官方主页

https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 论文标题

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 2. 发起与维护

### 发起团队

Harvey

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 合作及署名机构

Artificial Analysis（v1.1 联合开发 AA 实现）；Vals AI（行业合作评测）

来源：[1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 作者

Niko Grupen、Gabe Pereyra、Julio Pereyra（博客署名）

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 维护方

Harvey（harveyai/harvey-labs）

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 资助

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 3. 设计目标

### 评测能力

像律所分派工作那样：给出指令与客户案卷材料，要求 agent 产出可审阅的法律工作成果（文档、表格、演示）。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）；[2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 设计动机

LegalBench、CUAD、LEXam、BigLaw Bench 等只评短程推理，缺少长程法律 agent 基准。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 4. 构建方式

### 材料来源

从各执业领域律师经办的真实客户事项出发，拆分为可分派给associate的具体任务；给定指令、案卷及交付物要求。来源并未逐项证明公开材料的脱敏或授权细节，相关流程待核实。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 编制背景

执业律师参与任务来源，rubric由领域专家撰写；首发称75,000+标准，不能把该历史数当作本轮实测条数。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 审核流程

将合伙人/客户会审核的事实、结论、引用、风险等级和交付格式拆成二元标准，并将每条标准绑定具体输出文件；公开集允许法律专业人员审查任务并审核rubric。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md)（访问 2026-11-07）

### 质量控制

Vals v1.1披露移除17条不可完成标准、替换1份错配源文件，hold-out仍120任务；官方2026-11-05变更让裁判看到DOCX修订和评论，带修订输出与旧评分不可直接比较。

来源：[1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md)（访问 2026-11-07）

### 去污染边界

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 5. 数据形式

### 规模

当前README徽章为2,010任务；评测文档写2,010任务、27执业领域，README仍写24+contracting（分类口径未统一）。首发博客为1,200+任务、24领域、75,000+专家rubric，属于首版而非当前总量。AA与Vals各使用120个私有hold-out任务，不能以2,010作为榜单分母。

来源：[1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md)（访问 2026-11-07）；[3](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）；[4](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[5](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 题型

长程 agent 任务，产出 docx/xlsx/pptx 等交付物

来源：[1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 模态

- 文本
- 办公文档

来源：[1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 语言

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 难度

长程专业法律交付物；all-pass要求一位裁判判定全部标准通过，不能用criteria pass rate代替任务解决率。AA另加实质性幻觉门控。

来源：[1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[3](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 公开及隐藏划分

有公开集与 held-out 测试集；Vals 结果来自 held-out 集；AA 使用私有数据集

来源：[1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）


## 6. 评测方法

### 指标

AA：Hallucination-Gated All-Pass Rate（全部标准满足且无实质性幻觉）；Vals：Task Pass Rate 及 Criteria Pass Rate

来源：[1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 计分

开源标准双裁判claude-sonnet-4-6与gpt-5.5：逐裁判计算任务all-pass，再取平均；一题可为0、0.5或1，严格双裁判都通过另列。AA v1.1使用三裁判并有实质性幻觉门控；Vals为两裁判任务pass率均值。

来源：[1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[3](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 提示与运行设置

Vals：Read/Edit/Write File、Glob、Bash、Grep 六工具与 docx/pptx/xlsx 技能；AA：Stirrup harness

来源：[1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 评测入口

https://github.com/harveyai/harvey-labs

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 可比性边界

AA v1.1 与 v1.0 不可比；Vals HLAB-Vals-1.1 与 AA LAB-AA 不可比（Vals 页面明确说明）。

来源：[1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）


## 7. 最新情况

### 核查日

2026-11-07（KST / Asia/Seoul；本轮指定采集日期）

来源：[1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/README.md)（访问 2026-11-07）

### 已核实版本

version：开源仓库 lab-core v1.3.0；AA 实现为 Harvey LAB-AA v1.1；Vals 实现为 HLAB-Vals-1.1；evidence_2026_h2：- url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；organization：Artificial Analysis；note：当前方法页将Harvey Legal Agent Benchmark (LAB v1.1)列为正在实施的评测，披露任务或评分协议。；- url：https://artificialanalysis.ai/evaluations；date：2026-11-07；organization：Artificial Analysis；note：当前公开评测目录单列Harvey Legal Agent Benchmark (LAB v1.1)，不是新闻提及。；- url：https://www.vals.ai/benchmarks/hlab；date：2026-11-05；organization：Vals AI；note：Vals 11月5日更新HLAB-Vals-1.1专业法律交付物榜；与AA设置分开记录。；trending：heat_confidence：A；summary：AA 目录标 Updated，已与 Harvey 联合升级为幻觉门控评测；Vals 也独立评 HLAB-Vals-1.1。

说明：近期热门证据取自候选研究与本轮重开页面；A级：多家前沿实验室或评测机构独立采用。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations)（访问 2026-11-07）；[3](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 论文历史及后续证据

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 饱和情况

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 已知问题

公开任务可用于研究和训练，不能视为无污染。当前开源评分受harness、SDK及DOCX修订解析变更影响；11月5日以前/以后的修订文档任务结果应分版。AA/Vals private hold-out与公开全集不是同一数据范围。

来源：[1](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md)（访问 2026-11-07）；[3](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[4](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 衍生关系

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 8. 榜单快照

### 采集日期

2026-11-07（KST / Asia/Seoul；采集日，不代替榜单更新或实验日期）

来源：[1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 官方结果入口

https://artificialanalysis.ai/evaluations/harvey-lab-aa

说明：Harvey 本身无官方榜；AA 为与 Harvey 合作的实现。

来源：[1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）

### 第三方结果入口

https://www.vals.ai/benchmarks/hlab

来源：[1](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| AA LAB-AA v1.1；120私有任务；Stirrup；三裁判 | 1 | Muse Wonder Full (Max) | 13.1 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07 KST；待核实（页面未标明更新日） |
| AA LAB-AA v1.1；120私有任务；Stirrup；三裁判 | 2 | Muse Wonder (Max) | 10.0 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07 KST；待核实（页面未标明更新日） |
| AA LAB-AA v1.1；120私有任务；Stirrup；三裁判 | 3 | Grok 4.7 (Xhigh) | 9.4 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07 KST；待核实（页面未标明更新日） |
| AA LAB-AA v1.1；120私有任务；Stirrup；三裁判 | 4 | Muse Spark 1.3 (Max) | 8.9 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07 KST；待核实（页面未标明更新日） |
| AA LAB-AA v1.1；120私有任务；Stirrup；三裁判 | 5 | GPT-6 Astra (Max) | 8.6 | Hallucination-Gated All-Pass Rate % | [原始来源](https://artificialanalysis.ai/evaluations/harvey-lab-aa)；采集2026-11-07 KST；待核实（页面未标明更新日） |
| HLAB-Vals-1.1；120私有任务；Harvey/Valkyrie；双裁判 | 1 | Gemini 4 Argon | 27.08 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07 KST；2026-11-05（页面自报更新日期，未给时区） |
| HLAB-Vals-1.1；120私有任务；Harvey/Valkyrie；双裁判 | 2 | Muse Spark Open | 25.0 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07 KST；2026-11-05（页面自报更新日期，未给时区） |
| HLAB-Vals-1.1；120私有任务；Harvey/Valkyrie；双裁判 | 3 | Wonder | 23.75 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07 KST；2026-11-05（页面自报更新日期，未给时区） |
| HLAB-Vals-1.1；120私有任务；Harvey/Valkyrie；双裁判 | 4 | Wonder Full | 23.33 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07 KST；2026-11-05（页面自报更新日期，未给时区） |
| HLAB-Vals-1.1；120私有任务；Harvey/Valkyrie；双裁判 | 5 | Inkling 2 Small | 21.67 | Task Pass Rate % | [原始来源](https://www.vals.ai/benchmarks/hlab)；采集2026-11-07 KST；2026-11-05（页面自报更新日期，未给时区） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

分别转录AA v1.1与Vals v1.1各前五；两个榜的harness、裁判、幻觉门控和修复版本不同，绝不互相比名次。AA未显示榜单更新日；Vals页面明确Updated 11/5/2026。

来源：[1](https://artificialanalysis.ai/evaluations/harvey-lab-aa)（访问 2026-11-07）；[2](https://www.vals.ai/benchmarks/hlab)（访问 2026-11-07）


## 9. 联系方式

### 公开研究联系邮箱

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 问题反馈

https://github.com/harveyai/harvey-labs/issues

来源：[1](https://github.com/harveyai/harvey-labs)（访问 2026-11-07）

### 官方账号

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 隐私政策

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 10. 原始文件

### 原文PDF

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### PDF SHA-256

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### PDF字节数

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### Drive文件夹

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）

### 其他原始材料

- type：官方首发博客（非论文）；url：https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- type：评分方法；url：https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md
- type：影响分数的版本日志；url：https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/docs/eval-strategies.md)（访问 2026-11-07）；[3](https://raw.githubusercontent.com/harveyai/harvey-labs/HEAD/CHANGELOG.md)（访问 2026-11-07）

### Drive PDF

待核实

说明：本组按任务要求不上传Drive；原始PDF URL见original_files。

来源：[1](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)（访问 2026-11-07）


## 11. 变更记录

### 本页修订

- date：2026-11-07；timezone：KST / Asia/Seoul；change：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。
- date：2026-11-07；timezone：Asia/Seoul；change：第二轮q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）

