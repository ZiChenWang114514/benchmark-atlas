# AgentBench

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk)

## 基本信息

### 简称
AgentBench [来源1](https://github.com/THUDM/AgentBench)

### 全称
AgentBench [来源1](https://github.com/THUDM/AgentBench)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
原始8环境协议；当前仓库版本待核实 [来源2](https://arxiv.org/abs/2308.03688)

### 论文版本
arXiv v3 [来源2](https://arxiv.org/abs/2308.03688)

> 论文修订版本不等同数据集版本。

### 发布日期
2023-08-08 01:08:11 KST [来源2](https://arxiv.org/abs/2308.03688)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2308.03688)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "交互式Agent综合能力"
]
```
 [来源2](https://arxiv.org/abs/2308.03688)

### 许可证
Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源1](https://github.com/THUDM/AgentBench)

### 论文
https://arxiv.org/abs/2308.03688 [来源2](https://arxiv.org/abs/2308.03688)

### 官方代码
https://github.com/THUDM/AgentBench [来源1](https://github.com/THUDM/AgentBench)

### 数据地址
待核实 [来源2](https://arxiv.org/abs/2308.03688)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方入口
https://github.com/THUDM/AgentBench [来源1](https://github.com/THUDM/AgentBench)

### 论文标题
AgentBench: Evaluating LLMs as Agents [来源2](https://arxiv.org/abs/2308.03688)

## 发起与维护

### 机构与发起方
Tsinghua University、Ohio State University、UC Berkeley 等作者单位。 [来源2](https://arxiv.org/abs/2308.03688)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2308.03688)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Liu, Xiao",
  "Yu, Hao",
  "Zhang, Hanchen",
  "Xu, Yifan",
  "Lei, Xuanyu",
  "Lai, Hanyu",
  "Gu, Yu",
  "Ding, Hangliang",
  "Men, Kaiwen",
  "Yang, Kejuan",
  "Zhang, Shudan",
  "Deng, Xiang",
  "Zeng, Aohan",
  "Du, Zhengxiao",
  "Zhang, Chenhui",
  "Shen, Sheng",
  "Zhang, Tianjun",
  "Su, Yu",
  "Sun, Huan",
  "Huang, Minlie",
  "Dong, Yuxiao",
  "Tang, Jie"
]
```
 [来源2](https://arxiv.org/abs/2308.03688)

### 当前维护方
THUDM / AgentBench 项目团队 [来源2](https://arxiv.org/abs/2308.03688)

### 资助
论文致谢 Zhipu AI 的 GPU/API 支持及科研项目资助；完整资助清单见原文。 [来源2](https://arxiv.org/abs/2308.03688)

## 设计目标

### 衡量能力
跨环境长程交互、工具执行、决策、遵循反馈与完成目标的综合Agent能力。 [来源2](https://arxiv.org/abs/2308.03688)

### 设计背景
单轮静态语言/知识任务难以评估可行动Agent，不同交互环境的能力差异被单任务掩盖。 [来源2](https://arxiv.org/abs/2308.03688)

## 构建方式

### 题目来源
8环境：OS、Database、Knowledge Graph、Digital Card Game、Lateral Thinking Puzzles、Household(ALFWorld)、Web Shopping(WebShop)、Web Browsing(Mind2Web)。 [来源2](https://arxiv.org/abs/2308.03688)

### 出题者背景
多校研究团队；混合自建环境和既有任务，不是统一专家原创题。 [来源2](https://arxiv.org/abs/2308.03688)

### 审核流程
各环境构造任务、交互接口与专用评测；不能把所有环境说成同一审核流程。 [来源2](https://arxiv.org/abs/2308.03688)

### 质量控制
统一消息/行动框架，环境特定预算与有效性检查；失败轨迹用于误差分析。 [来源2](https://arxiv.org/abs/2308.03688)

### 去污染
包含已公开数据和环境，不能保证完全排除训练重叠；原论文设置不等于隐藏新题。 [来源2](https://arxiv.org/abs/2308.03688)

## 数据形式

### 题量与规模
原始dev269、test1,014；各环境题量和指标不相同。 [来源2](https://arxiv.org/abs/2308.03688)

### 题型
多轮文本交互与环境行动，包含SQL、shell、游戏、家务与网页。 [来源2](https://arxiv.org/abs/2308.03688)

### 模态

```json
[
  "文本",
  "代码/工具动作",
  "模拟环境"
]
```
 [来源2](https://arxiv.org/abs/2308.03688)

### 语言
英语指令为主；含SQL、shell等行动语言。 [来源2](https://arxiv.org/abs/2308.03688)

### 难度
依环境和任务变化；不能按一个统一题目难度分布概括。 [来源2](https://arxiv.org/abs/2308.03688)

### 公开与隐藏划分
原论文报告dev/test划分，代码与环境公开；split用途不等于永久隐藏测试。 [来源2](https://arxiv.org/abs/2308.03688)

## 评测方法

### 指标
各环境SR、F1、reward、游戏进度、step SR等；Overall为归一化后的加权环境平均，不是百分准确率。 [来源2](https://arxiv.org/abs/2308.03688)

### 评分
环境专用成功判定后再规范化聚合；必须保留单项分数与归一化方式。 [来源2](https://arxiv.org/abs/2308.03688)

### 提示与运行设置
原论文简单CoT策略，温度0，无多重重试/集成，约3500-token上下文裁剪，环境各有固定行动预算。 [来源2](https://arxiv.org/abs/2308.03688)

### 官方评测脚本
https://github.com/THUDM/AgentBench [来源1](https://github.com/THUDM/AgentBench)

### 可比性警示
综合OA与环境百分比不能直接比较；不同环境集、上下文截断和框架会改变结果。 [来源2](https://arxiv.org/abs/2308.03688)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/THUDM/AgentBench)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始8环境协议；当前仓库版本待核实",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §4.2及参考文献明确引用 AgentBench 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。"
    }
  ]
}
```
 [来源3](https://arxiv.org/html/2609.19134v1) [来源2](https://arxiv.org/abs/2308.03688)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Xiao Liu [ view email ] [v1] 2023-08-08 01:08:11 KST (20,331 KB) [v2] 2023-10-25 16:41:24 KST (20,908 KB) [v3] 2025-10-04 12:54:18 KST (20,753 KB) [来源2](https://arxiv.org/abs/2308.03688)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2308.03688)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
异质环境与指标聚合可能掩盖不同短板；公开任务污染与上下文/工具失败须和推理能力分开。 [来源2](https://arxiv.org/abs/2308.03688)

### 衍生与版本关系
待核实 [来源2](https://arxiv.org/abs/2308.03688)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/THUDM/AgentBench)

### 官方榜单
https://github.com/THUDM/AgentBench [来源1](https://github.com/THUDM/AgentBench)

### 独立评测覆盖
待核实 [来源1](https://github.com/THUDM/AgentBench)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "GPT-4-0613",
    "score": 4.01,
    "metric": "Overall归一化分",
    "benchmark_version": "原始8环境",
    "result_type": "论文历史基线",
    "source_date": "论文Table3",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Claude 3 Opus",
    "score": 3.11,
    "metric": "Overall归一化分",
    "benchmark_version": "原始8环境",
    "result_type": "论文历史基线",
    "source_date": "论文Table3",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "GLM-4",
    "score": 2.89,
    "metric": "Overall归一化分",
    "benchmark_version": "原始8环境",
    "result_type": "论文历史基线",
    "source_date": "论文Table3",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源2](https://arxiv.org/abs/2308.03688)

### 覆盖与时效说明
原论文Table3结果为历史基线（精确API快照仅在源文有明示时保留），不是当前排行榜；H2 ScienceIDE仅相关工作引用。 [来源2](https://arxiv.org/abs/2308.03688)

## 联系方式

### 公开工作邮箱

```json
[
  "yuxiaod@tsinghua.edu.cn",
  "jietang@tsinghua.edu.cn"
]
```
 [来源2](https://arxiv.org/abs/2308.03688)

### 公开反馈
https://github.com/THUDM/AgentBench/issues [来源1](https://github.com/THUDM/AgentBench)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2308.03688)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2308.03688)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2308.03688 [来源4](https://arxiv.org/pdf/2308.03688)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
9c780e35fc0b2de6c2e21e0572f6aaaadcf7ecdd56d63cfaae2b415bc0dc83c3 [来源4](https://arxiv.org/pdf/2308.03688)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
23017024
```
 [来源4](https://arxiv.org/pdf/2308.03688)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6",
  "webViewLink": "https://drive.google.com/drive/folders/1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6"
}
```
 [来源5](https://drive.google.com/drive/folders/1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA",
    "webViewLink": "https://docs.google.com/document/d/1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA/edit?usp=drivesdk"
  }
]
```
 [来源1](https://github.com/THUDM/AgentBench) [来源6](https://docs.google.com/document/d/1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp",
  "webViewLink": "https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk"
}
```
 [来源7](https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk)

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
 [来源1](https://github.com/THUDM/AgentBench)

## 来源

1. https://github.com/THUDM/AgentBench — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2308.03688 — 采集：2026-11-07 KST。
3. https://arxiv.org/html/2609.19134v1 — 采集：2026-11-07 KST。
4. https://arxiv.org/pdf/2308.03688 — 采集：2026-11-07 KST。
5. https://drive.google.com/drive/folders/1IO7G7wtK89QKtc_1ryb1OVJmtYENUOj6 — 采集：2026-11-07 KST。
6. https://docs.google.com/document/d/1MVdoSN9bIBHzJqTIy7n3VwMQgPk-XK-KwQIa8cR13OA/edit?usp=drivesdk — 采集：2026-11-07 KST。
7. https://drive.google.com/file/d/16ym4zaqvjgltLRCp6GUVsQu10I7cM5wp/view?usp=drivesdk — 采集：2026-11-07 KST。
