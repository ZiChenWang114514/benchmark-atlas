# AA-Omniscience

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1x28FX-LyGRAjXuPwOHCqqhubxSLh7OJj/view?usp=drivesdk)

## 基本信息

### 简称
AA-Omniscience
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 全称
AA-Omniscience
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 基准版本
v1.1
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 论文版本
arXiv v1
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

### 发布日期
2025-11-17
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "知识准确性、幻觉与校准"
]
```
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 许可证
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文
https://arxiv.org/abs/2511.13029
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

### 官方代码
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 数据地址
https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 官方入口
https://artificialanalysis.ai/evaluations/omniscience
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 论文标题
AA-Omniscience: Evaluating Cross-Domain Knowledge Reliability in Large Language Models
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
Artificial Analysis。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Jackson, Declan",
  "Keating, William",
  "Cameron, George",
  "Hill-Smith, Micah"
]
```
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

### 当前维护方
Artificial Analysis
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 资助
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
测量跨领域事实知识与知道何时不作答的知识校准，惩罚错误猜测。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 既有评测缺口
一般能力分数不能代表可靠事实输出，也不体现模型是否承认知识缺口。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

## 构建方式

### 题目来源
LLM 问题生成 agent 从权威学术与行业材料生成问题。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 出题与标注背景
Artificial Analysis 研究团队设计自动生成与评测流程。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 审核
题目代理以权威材料为依据，方法强调可判定性和事实精度；具体 v1.1 的逐题人工审查量待核实。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 质量控制
v1.1 移除已饱和问题，官网同时展示公开/私有题的表现一致性分析。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 去污染
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
v1.1 共 3,000 题、6 大领域；原论文 v1 为 6,000 题、42 个主题，不能当成 v1.1 规模。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 题型
开放式事实问答，允许放弃作答
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 模态
文本
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 语言
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 难度
v1.1 删除饱和题；分数降低可以来自题库变化，不能直接断言模型退步。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 公开与隐藏划分
官方公开 Public-v1.1 子集，并展示 private questions 对比；公开/私有精确题数本次待核实。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

## 评测方法

### 指标
Net Score（-100至100）、accuracy、hallucination rate；三者不同。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 评分
v1.1 Net Score 奖励正确、惩罚错误、不惩罚拒答；accuracy以全部问题为分母。官网当前hallucination rate定义为 incorrect/(incorrect+partial+not attempted)，不得自行换成常见的“错误/已作答”。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 提示与生成设置
应以 AA-Omniscience v1.1 methodology 为准；各模型 reasoning effort 标签需要保留。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 脚本
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可比性警告
v1 与 v1.1 题库和分数不可直接混比；当前页仍保留 v1 论文摘要的 Claude4.1Opus 4.8 分，那不是当前榜首。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-28：Artificial Analysis 2026-10-28 评测文章明确报告 AA-Omniscience v1.1 的分数、准确率及幻觉率；独立评测机构结果。

### 数据版本
v1.1
[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（采集2026-11-07）

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2025-11-17T15:27:16+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2511.13029)（采集2026-11-07）

### 饱和情况
官方说明 v1.1 移除了饱和题；这说明题库发生筛选，不代表整个知识任务已饱和。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 污染与已知问题
同页含 v1 论文摘要和 v1.1 当前方法，题量、最高分与分数含义必须按版本区分；当前幻觉率分母使用官网给出的定义，不按惯例改写。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 衍生评测
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://artificialanalysis.ai/evaluations/omniscience
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 二级机构榜单
https://artificialanalysis.ai/evaluations/omniscience
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 可读结果
```json
[
  {
    "model": "Gemini 4 Carbon (High)",
    "score": 54,
    "unit": "points",
    "metric": "v1.1 Net Score",
    "scope": "AA独立评测官网可读前列",
    "snapshot_date": "2026-11-07",
    "model_release_date": "2026-10-28"
  },
  {
    "model": "Claude Opus 5.5 (Max, Default Fallback)",
    "score": 48,
    "unit": "points",
    "metric": "v1.1 Net Score",
    "scope": "AA独立评测官网可读前列",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Gemini 4 Carbon (Medium)",
    "score": 47,
    "unit": "points",
    "metric": "v1.1 Net Score",
    "scope": "AA独立评测官网可读前列",
    "snapshot_date": "2026-11-07"
  }
]
```
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

### 覆盖与时效限制
采集日官网明确可读的 Net Score 前三名；同页accuracy榜首68%、hallucination rate最低4%属于不同模型/配置和指标，未揉成统一安全排名。原始 PDF 是v1论文，当前方法为v1.1。
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07） [来源2](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 仓库讨论与Issues
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 官方社交渠道
待核实
[来源1](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2511.13029
[来源1](https://arxiv.org/pdf/2511.13029)（采集2026-11-07）

### 原件SHA-256
abedc69e8235329cbfe0fe49cc33928a5b1732bc054637328c00b07f588b5dfa
[来源1](https://arxiv.org/pdf/2511.13029)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
3786016
```
[来源1](https://arxiv.org/pdf/2511.13029)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1Mrrp24vyM98TfiB-wQ0QON4zu8XdEJWO",
  "webViewLink": "https://drive.google.com/drive/folders/1Mrrp24vyM98TfiB-wQ0QON4zu8XdEJWO"
}
```
[来源1](https://drive.google.com/drive/folders/1Mrrp24vyM98TfiB-wQ0QON4zu8XdEJWO)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1Suli8iNzIoHvLMfAxHiSjWdZaSYSX22WFU-Wznw_V1k",
    "webViewLink": "https://docs.google.com/document/d/1Suli8iNzIoHvLMfAxHiSjWdZaSYSX22WFU-Wznw_V1k/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/1Suli8iNzIoHvLMfAxHiSjWdZaSYSX22WFU-Wznw_V1k/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://artificialanalysis.ai/evaluations/omniscience)（采集2026-11-07） [来源](https://arxiv.org/pdf/2511.13029)（采集2026-11-07）
