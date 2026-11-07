# SysBench

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/19-Vjl0qkIT7uZezwcrYIIYyGtVxhAIAU/view?usp=drivesdk)

## 基本信息

### 简称
SysBench
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 全称
SysBench
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 基准版本
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本
arXiv v2
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 发布日期
2024-08-20
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "系统指令遵循"
]
```
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 许可证
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文
https://arxiv.org/abs/2408.10943
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 官方代码
https://github.com/PKU-Baichuan-MLSystemLab/SysBench
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 数据地址
https://github.com/PKU-Baichuan-MLSystemLab/SysBench
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 官方入口
https://github.com/PKU-Baichuan-MLSystemLab/SysBench
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 论文标题
SysBench: Can Large Language Models Follow System Messages?
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
论文作者来自北京大学与百川智能等单位；作者单位记录不等于唯一发起机构。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Qin, Yanzhao",
  "Zhang, Tao",
  "Zhang, Tao",
  "Shen, Yanjun",
  "Luo, Wenjing",
  "Sun, Haoze",
  "Zhang, Yan",
  "Qiao, Yujing",
  "Chen, Weipeng",
  "Zhou, Zenan",
  "Zhang, Wentao",
  "Cui, Bin"
]
```
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
评估模型遵守系统消息约束，以及多轮交互中的持续性。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 既有评测缺口
常见指令评测主要针对用户消息，无法充分衡量系统指令优先级、多轮依赖和稳定性。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

## 构建方式

### 题目来源
人工设计系统消息和配套多轮对话，涵盖 6 类系统约束。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 出题与标注背景
研究团队人工设计对话、约束和检查清单。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 审核
为数据配置 ground-truth assistant/checklist，并结合可自动检查与模型裁判的评估。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 质量控制
从约束、指令、会话三个粒度统计表现，避免只看单轮是否拒答。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
500 组系统消息/对话，合计 2,500 轮，6 类约束。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 题型
带系统指令的多轮文本对话
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 语言
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 难度
约束违反、指令误判、多轮不稳定三个问题，包含依赖或平行对话设置。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 公开与隐藏划分
官方仓库提供 datas/system_benchmark_eval_datas.json；独立隐藏划分待核实。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

## 评测方法

### 指标
Constraint Satisfaction Rate (CSR)、Instruction Satisfaction Rate (ISR)、Session Stability Rate (SSR)。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 评分
依据检查清单评价约束是否满足；再按指令及整段会话汇总。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 提示与生成设置
系统消息与用户轮次必须保持原角色和顺序，记录被测模型的 system-role 支持和模板。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 脚本
https://github.com/PKU-Baichuan-MLSystemLab/SysBench
[来源1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（采集2026-11-07）

### 可比性警告
CSR、ISR、SSR 粒度不同；不能将厂商报告中未指定指标的 SysBench 分数默认为三者之一。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-09-23：Hunyuan-A13B §4.2–4.3实际使用 SysBench 并报告结果；厂商自报，需保留各基准的提示/上下文条件。

### 数据版本
待核实
[来源1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2024-08-21T00:33:16+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2024-10-23T00:07:35+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 饱和情况
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 衍生评测
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://arxiv.org/abs/2408.10943
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果
```json
[
  {
    "model": "Hunyuan-A13B（报告命名）",
    "score": 76.1,
    "unit": "%",
    "metric": "SysBench，报告表3原标签",
    "scope": "slow-thinking；厂商自报，报告未在此表区分 CSR/ISR/SSR",
    "evaluation_date": "报告日期2026-09-23；精确运行日期待核实",
    "snapshot_date": "2026-11-07"
  }
]
```
[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

### 覆盖与时效限制
仅收录H2技术报告中明确可读的厂商自报成绩；模型标签按报告保留，未核实其精确API运行日期。不能把这些成绩冒充独立机构当前排行榜。
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07） [来源2](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
```json
[
  "qinyanzhao123@pku.edu.cn"
]
```
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

### 仓库讨论与Issues
https://github.com/PKU-Baichuan-MLSystemLab/SysBench/issues
[来源1](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)（采集2026-11-07）

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2408.10943)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2408.10943
[来源1](https://arxiv.org/pdf/2408.10943)（采集2026-11-07）

### 原件SHA-256
192a6383d66f9075c26bff148774396da331daad4c69e1dafea9222fc20c10ed
[来源1](https://arxiv.org/pdf/2408.10943)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
788584
```
[来源1](https://arxiv.org/pdf/2408.10943)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1pfSl-HONOkg-IIPEDuBZHElwxzgJxc7M",
  "webViewLink": "https://drive.google.com/drive/folders/1pfSl-HONOkg-IIPEDuBZHElwxzgJxc7M"
}
```
[来源1](https://drive.google.com/drive/folders/1pfSl-HONOkg-IIPEDuBZHElwxzgJxc7M)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1kRYVWgWz8ZqkciI-cdjGgFEJHxGu5ElCjqgdk_BrH8I",
    "webViewLink": "https://docs.google.com/document/d/1kRYVWgWz8ZqkciI-cdjGgFEJHxGu5ElCjqgdk_BrH8I/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/1kRYVWgWz8ZqkciI-cdjGgFEJHxGu5ElCjqgdk_BrH8I/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2408.10943)（采集2026-11-07） [来源](https://arxiv.org/pdf/2408.10943)（采集2026-11-07）
