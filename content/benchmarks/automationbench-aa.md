# AutomationBench-AA

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE/view?usp=drivesdk)

## 基本信息

### 简称
AutomationBench-AA [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 全称
AutomationBench-AA（Artificial Analysis 对 Zapier AutomationBench 的实现） [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 基准版本
AA独立实现657任务；母协议AutomationBench [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 论文版本
arXiv v1 [来源2](https://arxiv.org/abs/2604.18934)

> 论文修订版本不等同数据集版本。

### 发布日期
2026-04-21 09:14:59 KST [来源2](https://arxiv.org/abs/2604.18934)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2604.18934)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "长程自动化任务"
]
```
 [来源2](https://arxiv.org/abs/2604.18934)

### 许可证
母仓库Zapier原创部分为MIT；第三方API结构表示不主张原创版权，也不授予第三方IP权；AA私有集使用权另行核实。 [来源3](https://github.com/zapier/AutomationBench/blob/main/LICENSE)

### 论文
https://arxiv.org/abs/2604.18934 [来源2](https://arxiv.org/abs/2604.18934)

> 2604.18934是Zapier母协议论文，不把AA的657题部分得分口径归给母论文。

### 官方代码
https://github.com/zapier/AutomationBench [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 数据地址
待核实 [来源2](https://arxiv.org/abs/2604.18934)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方入口
https://artificialanalysis.ai/evaluations/automationbench-aa [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 论文标题
AutomationBench [来源2](https://arxiv.org/abs/2604.18934)

## 发起与维护

### 机构与发起方
母基准：Zapier；AA实现与独立评测：Artificial Analysis。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

### 合作方
母论文致谢Prime Intellect等早期反馈；不意味着这些机构共同维护AA私有集。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

### 作者

```json
[
  "Daniel Shepard",
  "Robin Salimans"
]
```
 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

### 当前维护方
AutomationBench母项目由Zapier维护；AA运行与榜单由Artificial Analysis维护。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

### 资助
待核实 [来源2](https://arxiv.org/abs/2604.18934)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
跨SaaS应用自主发现API、处理数据、遵守分层业务规则并完成多步工作流。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

### 设计背景
很多工具基准只测单应用/函数选择，缺少跨应用协调、端点发现和业务政策组合。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

## 构建方式

### 题目来源
根据Zapier客户工作流形状合成，未使用PII/客户机密；涵盖6领域、约500端点与47模拟应用。 [来源2](https://arxiv.org/abs/2604.18934)

### 出题者背景
Zapier研究/工程团队；Opus4.6、GPT5.3Codex、Gemini3参与生成，再做审查。 [来源2](https://arxiv.org/abs/2604.18934)

### 审核流程
多轮现实性/难度迭代、抽样人工审计；通过不含实际参数的提示模式验证可解性。 [来源2](https://arxiv.org/abs/2604.18934)

### 质量控制
每题要求可观察状态修改、确定性检查与负断言防止撒网行为；RL试验识别奖励漏洞。 [来源2](https://arxiv.org/abs/2604.18934)

### 去污染
母协议公开600题，至少同规模私有题；AA保留657评测题，公开示例不是官方完整评分集。 [来源2](https://arxiv.org/abs/2604.18934)

## 数据形式

### 题量与规模
AA实现：657任务，6领域（Finance/HR/Marketing/Operations/Sales/Support）；母论文公开600及600+私有不是同一精确分母。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 题型
一次任务指令后自主多步API检索/调用，最后核对多个应用状态。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 模态

```json
[
  "文本",
  "结构化API与数据库",
  "模拟SaaS应用"
]
```
 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 语言
英语业务指令与API schema。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 难度
分层政策、噪声和相似记录造成困难；不等于真实生产SaaS连通性或凭证权限测试。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 公开与隐藏划分
AA评分题保留私有，部分样例公开；母项目公开题可研究，不能作为AA分数完全复现集。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

## 评测方法

### 指标
headline为每题objective完成比例，经guardrail门控后平均；另有严格整题成功率。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 评分
任一guardrail违规整题0；否则按该任务objective满足比例记分。无条件objective得分不是同一指标。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 提示与运行设置
Search/Execute接口与自主多步模拟；AA方法与母协议不同配置必须分别说明；母论文最多50步。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 官方评测脚本
https://github.com/zapier/AutomationBench [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 可比性警示
母论文严格全目标成功<10%和AA部分目标完成约78%不矛盾：数据、分母、门控/部分分均不同；切勿直接声称进步约70百分点。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "AA独立实现657任务；母协议AutomationBench",
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
      "date": "2026-10-28",
      "note": "Artificial Analysis 2026-10-28文章明确列出 AutomationBench-AA 为 Intelligence Index v5 的评测组成并报告模型领先表现。"
    }
  ]
}
```
 [来源4](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Daniel Shepard [ view email ] [v1] 2026-04-21 09:14:59 KST (420 KB) [来源2](https://arxiv.org/abs/2604.18934)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2604.18934)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
合成任务与模拟API可能偏离真实业务；仅终态评分不完整检查行为过程，guardrail口径影响解读。 [来源2](https://arxiv.org/abs/2604.18934) [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 衍生与版本关系
AutomationBench-AA为AA实现；母协议600公开题与657私有评测不拆计两条，应用/领域子项不另计。 [来源2](https://arxiv.org/abs/2604.18934) [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 官方榜单
https://artificialanalysis.ai/evaluations/automationbench-aa [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 独立评测覆盖
https://artificialanalysis.ai/evaluations/automationbench-aa [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

### 核验结果

```json
[
  {
    "model": "Gemini 4 Carbon (High)",
    "score": 77.8,
    "metric": "guardrail-gated objective score (%)",
    "benchmark_version": "AA657",
    "result_type": "AA独立当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Gemini 4 Carbon (Medium)",
    "score": 77.6,
    "metric": "guardrail-gated objective score (%)",
    "benchmark_version": "AA657",
    "result_type": "AA独立当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Gemini 4 Argon (High)",
    "score": 77.5,
    "metric": "guardrail-gated objective score (%)",
    "benchmark_version": "AA657",
    "result_type": "AA独立当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Claude Opus 4.7 (max)",
    "score": 9.9,
    "metric": "strict full-task completion (%)",
    "benchmark_version": "Zapier母协议私有集",
    "result_type": "母论文历史结果",
    "source_date": "2026-04",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

### 覆盖与时效说明
AA既是本实现发布/维护方，也是相对Zapier母协议的独立评测方；同一URL不冒充两份独立证据。母论文9.9%列作不同协议对照。原母榜另见https://zapier.com/benchmarks。 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源2](https://arxiv.org/abs/2604.18934)

## 联系方式

### 公开工作邮箱

```json
[
  "daniel.shepard@zapier.com",
  "robin.salimans@zapier.com"
]
```
 [来源2](https://arxiv.org/abs/2604.18934)

### 公开反馈
https://github.com/zapier/AutomationBench/issues [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2604.18934)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2604.18934)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2604.18934 [来源5](https://arxiv.org/pdf/2604.18934)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
348360cd2ccefc52d1a8ea65e0a334cb3363fab85e66f71e09f6f5935233cbc5 [来源5](https://arxiv.org/pdf/2604.18934)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
684375
```
 [来源5](https://arxiv.org/pdf/2604.18934)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O",
  "webViewLink": "https://drive.google.com/drive/folders/1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O"
}
```
 [来源6](https://drive.google.com/drive/folders/1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM",
    "webViewLink": "https://docs.google.com/document/d/1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM/edit?usp=drivesdk"
  }
]
```
 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa) [来源7](https://docs.google.com/document/d/1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE",
  "webViewLink": "https://drive.google.com/file/d/1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE/view?usp=drivesdk)

## 变更记录


```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  }
]
```
 [来源1](https://artificialanalysis.ai/evaluations/automationbench-aa)

## 来源

1. https://artificialanalysis.ai/evaluations/automationbench-aa — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2604.18934 — 采集：2026-11-07 KST。
3. https://github.com/zapier/AutomationBench/blob/main/LICENSE — 采集：2026-11-07 KST。
4. https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 — 采集：2026-11-07 KST。
5. https://arxiv.org/pdf/2604.18934 — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1NgpzI8h2aK9daBTqXuWmUYkvoL9R-H1O — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/1xuE7UD_fnv0r_Y6v-6IQezjMhLDP9jVjF6dZfaSbSJM/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1UHMv5FX-27Vo0lMavoG2Ju3n9jV3NsNE/view?usp=drivesdk — 采集：2026-11-07 KST。
