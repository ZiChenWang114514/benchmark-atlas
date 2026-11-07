# HealthBench Professional

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

已核验存在；11节研究快照；note: trending: A；未知字段保留待核实

## 基本信息

### 简称

HealthBench Professional

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 全称

HealthBench Professional

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 论文版本

v1（本轮返回正文版本）

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 主板块

生物与医学

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 子领域



[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 许可

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2604.27470

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 代码

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 数据

https://openaipublic.blob.core.windows.net/simple-evals/healthbench_professional/assets.zip

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 官网

https://arxiv.org/abs/2604.27470

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 论文标题

HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 发起与维护

### 发起方

OpenAI

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 合作方

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 作者

Rebecca Soskin Hicks、Mikhail Trofimov、Dominick Lim、Rahul K. Arora 等（完整作者见论文）

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 维护方

OpenAI

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 资助

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 设计目标

### 衡量能力

衡量医生与模型真实工作对话中的临床咨询、写作与文档、医学研究能力及安全性。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 设计背景

医学选择题或合成病历不能覆盖常见临床聊天工作；Professional补充而非替代面向患者和医生的HealthBench。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 构建方式

### 题目来源

医生测试ChatGPT for Clinicians所得对话；候选15,079例中按质量、代表性及难度选择525例。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 出题人背景

190名医生参与，实践经验跨50国、26个医学专科。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 审核流程

至少3名医生分三阶段撰写、审查、最终裁决；困难任务由独立医生确认错误与现实性。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 质量控制

困难样本相对候选池富集约3.5倍，约三分之一为红队；为全部任务收集不限时、可联网的专科匹配医生基线。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 去污染

论文请求不要在线逐题发布数据；使用canary，并保留小型私有held-out集监测训练污染。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 数据形式

### 规模

525例：care consult 236、writing and documentation 142、medical research 147。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 题型

单轮或多轮对话，生成最后用户消息的下一条自由文本答复。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 模态

- 文本对话

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 语言

每例有primary language标签；完整语言计数待核实。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 难度

typical为医生Likert 3–7，difficult为1–2；困难选择针对当时OpenAI模型，非自然临床分布。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 公开与隐藏划分

公开525任务的对话、rubric、use_case、type、difficulty、specialty与医生参考答复；另保留小型私有集，数量待核实。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 评测方法

### 指标

长度调整后的rubric得分；不是临床正确率。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 评分

每项非零权重在-10至10，满足计全部点数，否则0；除以正权重总和；每超过2000字符500字扣1.47个百分点；论文均值裁剪至[0,1]。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 提示与运行设置

论文主要比较每题8样本、最高可用推理档；AA为4次重复，用GPT-5.4 low裁判。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 评测脚本

官方论文使用内部实现且明确不发布官方外部实现；HealthBench的simple-evals作为参考，不能称完全同一实现。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 可比性警示

产品harness、裸模型、是否联网与长度调整/裁剪须分开；困难抽样不能解读为现实临床错误率。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度A：有当前独立评测或多来源采用证据；按下列日期类型解读。

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 当前版本与热门证据

- **version**：待核实
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://artificialanalysis.ai/evaluations/healthbench-professional", "date": "2026-11-07", "note": "Artificial Analysis当前独立评测525任务；日期为观察日。"}, {"url": "https://openai.com/index/gpt-6-astra/", "date": "2026-11-07", "note": "厂商发布表继续单列Professional；观察日，不冒称首发日。"}]

> A：原始基准与独立评测材料交叉核验；不将仅引用等同独立实跑。

[来源](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 污染与争议

Epoch于2026-09-10评审判为Flawed；该目录未说明具体错误，不臆测。另需注意模型裁判、难度富集和长度校正的外推限制。

[来源](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问 2026-11-07）

### 衍生及版本关系

Professional是对HealthBench的互补临床工作评测，不是Hard/Consensus切片，也不宣称取代HealthBench。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 官方榜单

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 独立评测入口

https://artificialanalysis.ai/evaluations/healthbench-professional

[来源](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "GPT-6 Astra (Max)", "score": "66.0%", "metric": "AA长度调整rubric得分", "source_url": "https://artificialanalysis.ai/evaluations/healthbench-professional", "source_date": "待核实", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}
- {"rank": 2, "model": "GPT-6.1 Sol (Max)", "score": "65.1%", "metric": "AA长度调整rubric得分", "source_url": "https://artificialanalysis.ai/evaluations/healthbench-professional", "source_date": "待核实", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}
- {"rank": 3, "model": "Claude Sonnet 5.5 (Max, Default Fallback)", "score": "63.0%", "metric": "AA长度调整rubric得分", "source_url": "https://artificialanalysis.ai/evaluations/healthbench-professional", "source_date": "待核实", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}

[来源](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）

### 覆盖与时效说明

仅保留所列来源与协议下的结果；榜单自写更新时间：待核实。访问日期不是评测运行日期。

[来源](https://artificialanalysis.ai/evaluations/healthbench-professional)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- rebecca.soskinhicks@openai.com
- mtrofimov@openai.com
- karan@openai.com

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2604.27470

> 官方论文正文对应的PDF入口；本轮未下载，故hash与字节数待核实。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### Drive资料夹

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方介绍/协议", "url": "https://arxiv.org/abs/2604.27470"}

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）

### Drive PDF归档

待核实（本任务未上传）

## 变更记录

### changelog

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传Drive。"}

[来源](https://arxiv.org/abs/2604.27470)（访问 2026-11-07）
