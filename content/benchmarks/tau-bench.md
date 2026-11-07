# τ-bench

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ/view?usp=drivesdk)

## 基本信息

### 简称
τ-bench [来源1](https://github.com/sierra-research/tau-bench)

### 全称
τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains [来源2](https://arxiv.org/abs/2406.12045)

### 基准版本
原始retail / airline协议；不与τ²混合 [来源2](https://arxiv.org/abs/2406.12045)

### 论文版本
arXiv v1 [来源2](https://arxiv.org/abs/2406.12045)

> 论文修订版本不等同数据集版本。

### 发布日期
2024-06-18 04:33:08 KST [来源2](https://arxiv.org/abs/2406.12045)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2406.12045)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "工具—Agent—用户交互"
]
```
 [来源2](https://arxiv.org/abs/2406.12045)

### 许可证
MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源1](https://github.com/sierra-research/tau-bench)

### 论文
https://arxiv.org/abs/2406.12045 [来源2](https://arxiv.org/abs/2406.12045)

### 官方代码
https://github.com/sierra-research/tau-bench [来源1](https://github.com/sierra-research/tau-bench)

### 数据地址
https://github.com/sierra-research/tau-bench [来源2](https://arxiv.org/abs/2406.12045)

### 官方入口
https://github.com/sierra-research/tau-bench [来源1](https://github.com/sierra-research/tau-bench)

### 论文标题
$\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains [来源2](https://arxiv.org/abs/2406.12045)

## 发起与维护

### 机构与发起方
Sierra [来源2](https://arxiv.org/abs/2406.12045)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2406.12045)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Shunyu Yao",
  "Noah Shinn",
  "Pedram Razavi",
  "Karthik Narasimhan"
]
```
 [来源2](https://arxiv.org/abs/2406.12045)

### 当前维护方
Sierra Research / tau-bench团队 [来源2](https://arxiv.org/abs/2406.12045)

### 资助
待核实 [来源2](https://arxiv.org/abs/2406.12045)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
与用户多轮交流、调用数据库工具并遵守业务政策，稳定完成现实服务任务。 [来源2](https://arxiv.org/abs/2406.12045)

### 设计背景
单轮工具调用或固定计划不能测清楚持续用户交互、政策遵循与重复运行可靠性。 [来源2](https://arxiv.org/abs/2406.12045)

## 构建方式

### 题目来源
人工设计零售/航空业务政策、Python工具API和JSON数据库；模型辅助生成数据库内容，人工写任务场景。 [来源2](https://arxiv.org/abs/2406.12045)

### 出题者背景
Sierra研究团队；用户由语言模型模拟，不能称为真实客户对话。 [来源2](https://arxiv.org/abs/2406.12045)

### 审核流程
人工场景与多次agent运行迭代验证任务可行性。 [来源2](https://arxiv.org/abs/2406.12045)

### 质量控制
以目标数据库终态及必要用户回复子串判断成功，检查无关/禁止变更。 [来源2](https://arxiv.org/abs/2406.12045)

### 去污染
公开环境与任务可能被后续训练接触；模拟用户随机性不能替代去污染。 [来源2](https://arxiv.org/abs/2406.12045)

## 数据形式

### 题量与规模
原始retail测试115题、airline测试50题。 [来源2](https://arxiv.org/abs/2406.12045)

### 题型
工具—Agent—用户多轮业务交互。 [来源2](https://arxiv.org/abs/2406.12045)

### 模态

```json
[
  "文本对话",
  "结构化数据库",
  "函数调用"
]
```
 [来源2](https://arxiv.org/abs/2406.12045)

### 语言
英语对话与Markdown政策；Python工具/JSON状态。 [来源2](https://arxiv.org/abs/2406.12045)

### 难度
跨政策、用户信息收集与多动作；原论文按领域报告，不假定统一难度配比。 [来源2](https://arxiv.org/abs/2406.12045)

### 公开与隐藏划分
原始数据、工具、政策与评测代码公开；用户目标和金标准终态不展示给agent。 [来源2](https://arxiv.org/abs/2406.12045)

## 评测方法

### 指标
pass^k（重复k次全成功），也报告平均成功率；与pass@k至少一次成功定义相反。 [来源2](https://arxiv.org/abs/2406.12045)

### 评分
终态数据库与金标准对比，加所需回复内容检查；不完整审计所有中间行为。 [来源2](https://arxiv.org/abs/2406.12045)

### 提示与运行设置
原实验agent温度0、user温度1、gpt-4-0613用户、最多30动作、至少3次试验。 [来源2](https://arxiv.org/abs/2406.12045)

### 官方评测脚本
https://github.com/sierra-research/tau-bench [来源1](https://github.com/sierra-research/tau-bench)

### 可比性警示
领域平均与按任务加权均值不同；user模型、次数、pass^k/pass@k及τ²/τ³版本必须区分。 [来源2](https://arxiv.org/abs/2406.12045)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/sierra-research/tau-bench)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始retail / airline协议；不与τ²混合",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.2 Agents及表3–4实际报告 τ-bench（BFCL为v3），属于厂商自报评测。"
    }
  ]
}
```
 [来源3](https://arxiv.org/html/2609.27284v1) [来源2](https://arxiv.org/abs/2406.12045)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Karthik Narasimhan [ view email ] [v1] 2024-06-18 04:33:08 KST (647 KB) [来源2](https://arxiv.org/abs/2406.12045)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2406.12045)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
论文明确：终态奖励未检查全部规则，例如未确认就修改仍可能得1；成功率不等于完整政策遵从率。 [来源2](https://arxiv.org/abs/2406.12045)

### 衍生与版本关系
τ²-Bench加入双控制电信等新环境，τ³/τ-Knowledge另扩展知识；与本条原始τ-bench分开注明。 [来源2](https://arxiv.org/abs/2406.12045)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/sierra-research/tau-bench)

### 官方榜单
https://github.com/sierra-research/tau-bench [来源1](https://github.com/sierra-research/tau-bench)

### 独立评测覆盖
待核实 [来源1](https://github.com/sierra-research/tau-bench)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "GPT-4o",
    "score": 48.2,
    "metric": "领域平均成功率 (%)",
    "benchmark_version": "原始retail/airline",
    "result_type": "论文历史基线",
    "source_date": "原始论文",
    "collected_at": "2026-11-07 KST",
    "settings": "两个领域等权；非165题任务加权"
  },
  {
    "model": "Hunyuan-A13B slow-thinking",
    "score": 54.7,
    "metric": "报告中的τ-bench (%)",
    "benchmark_version": "原始τ；具体聚合待核实",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源2](https://arxiv.org/abs/2406.12045) [来源3](https://arxiv.org/html/2609.27284v1)

### 覆盖与时效说明
保留原始论文与H2自报，均不冒称当前全榜首；τ²-Bench Telecom属于不同环境，不能拿其AA成绩填本条。 [来源2](https://arxiv.org/abs/2406.12045) [来源3](https://arxiv.org/html/2609.27284v1)

## 联系方式

### 公开工作邮箱
待核实 [来源2](https://arxiv.org/abs/2406.12045)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
https://github.com/sierra-research/tau-bench/issues [来源1](https://github.com/sierra-research/tau-bench)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2406.12045)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2406.12045)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2406.12045 [来源4](https://arxiv.org/pdf/2406.12045)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
0ce66a1763d698c61bb311c3c874bf593d1e9a5bfff11bb35f6f72b981f6da56 [来源4](https://arxiv.org/pdf/2406.12045)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
663224
```
 [来源4](https://arxiv.org/pdf/2406.12045)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2",
  "webViewLink": "https://drive.google.com/drive/folders/1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2"
}
```
 [来源5](https://drive.google.com/drive/folders/1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ",
    "webViewLink": "https://docs.google.com/document/d/1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ/edit?usp=drivesdk"
  }
]
```
 [来源1](https://github.com/sierra-research/tau-bench) [来源6](https://docs.google.com/document/d/1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ",
  "webViewLink": "https://drive.google.com/file/d/1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ/view?usp=drivesdk"
}
```
 [来源7](https://drive.google.com/file/d/1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ/view?usp=drivesdk)

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
 [来源1](https://github.com/sierra-research/tau-bench)

## 来源

1. https://github.com/sierra-research/tau-bench — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2406.12045 — 采集：2026-11-07 KST。
3. https://arxiv.org/html/2609.27284v1 — 采集：2026-11-07 KST。
4. https://arxiv.org/pdf/2406.12045 — 采集：2026-11-07 KST。
5. https://drive.google.com/drive/folders/1OSJJGGjM50lJjBWupTy-CH-8zprFfzC2 — 采集：2026-11-07 KST。
6. https://docs.google.com/document/d/1Wt6ZxjHPH_kc-ECvPjbH1vXfrvufjw409sMahTTSDCQ/edit?usp=drivesdk — 采集：2026-11-07 KST。
7. https://drive.google.com/file/d/1cMD6GLUb-mTNgyvnKsthuUraunZbJWHQ/view?usp=drivesdk — 采集：2026-11-07 KST。
