# AdvBench

> 核验日期：2026-11-07 Asia/Shanghai（UTC+8）。未知保留待核实；访问日不是测量日。

已核实存在与2026-H2实际使用；已建内容，待核实字段显式保留

有害请求与字符串攻击的实验数据，不是一个能把模型安全性压成通用名次的实时榜。历史ASR必须同时带上目标模型、攻击方法、样本和预算。

## 基本信息

### 简称

AdvBench

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 全称

AdvBench

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 基准版本

原论文AdvBench有害字符串/有害行为两任务；仓库未以独立语义版本号定义数据版本，复现需固定提交和CSV。

> 不把论文v2写成数据集v2。

[来源1](https://github.com/llm-attacks/llm-attacks)（访问2026-11-07）

### 论文版本

arXiv v2

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 发布日期

2023-07-28 01:49:12 Asia/Shanghai（UTC+8）（arXiv首稿；来源UTC日期为7月27日）

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 主板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 领域标签

- 有害请求与越狱

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 许可证

MIT（llm-attacks仓库软件与文档；数据/第三方材料适用范围须按制品核查）。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2307.15043

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 官方代码

https://github.com/llm-attacks/llm-attacks

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 数据地址

https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 官方入口

https://llm-attacks.org/

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 论文标题

Universal and Transferable Adversarial Attacks on Aligned Language Models

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

## 发起与维护

### 发起方

作者来自 CMU、Center for AI Safety、Google DeepMind、Bosch Center for AI 等单位；正式发起关系不作推断。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 作者

- Zou, Andy
- Wang, Zifan
- Carlini, Nicholas
- Nasr, Milad
- Kolter, J. Zico
- Fredrikson, Matt

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 维护方

官方代码与反馈由 llm-attacks/llm-attacks 仓库提供；个人持续维护职责及响应时限未核实。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问2026-11-07）

### 资助方

论文致谢列出 DARPA/AFRL FA8750-15-2-0277、Army MURI W911NF-21-1-0317、NSF CNS1943016 等支持。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

## 设计目标

### 衡量能力

评价对齐语言模型在有害行为及指定字符串上的对抗鲁棒性。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 设计背景

仅人工探索越狱难以系统比较可优化攻击及跨模型转移性，需要统一行为与目标字符串。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

## 构建方式

### 题目来源

作者人工种子示例配合Wizard-Vicuna-30B-Uncensored生成；论文区分有害字符串与有害行为。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 出题者背景

研究团队提供人工种子并筛选生成结果；不是安全专家逐条原创全部条目。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 审核流程

论文§2.3按有害行为/有害字符串分别构建，行为来源含初始例子与LLM扩写；不是第三方对模型安全认证。逐条外部专家复审记录待核实。

> 字段状态：待核实

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 质量控制

原论文与公开CSV规模存在差异，本条保留二者并固定来源；后续研究指出单看非拒答可能高估攻击效果。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 去污染

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

## 数据形式

### 题量与规模

原论文描述500条有害字符串、500条有害行为；采集日官方 harmful_behaviors.csv 实测520条数据行（不含表头）。这是不同版本/制品，不能默默统一为500或520。

> CSV使用Python csv.DictReader计数，仅计算数据行，不含表头；本次未修改原文件。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv)（访问2026-11-07）

### 题型

有害行为请求和目标字符串；此介绍不转载具体攻击后缀或危害步骤

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 难度

评测面向对抗攻击成功与迁移；难度受目标模型及攻击预算影响。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 公开与隐藏划分

仓库公开行为/字符串CSV；未核实独立隐藏测试划分。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

## 评测方法

### 指标

攻击成功率（ASR）；有害字符串匹配和行为合规需分别定义。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 评分

有害字符串按精确复现目标字符串计算ASR；有害行为要求reasonable attempt，需人工判断是否拒绝或回避。论文表与叙述存在个别数值差异，本页以Table1明确单列值为准；非拒答不等同真实有害帮助质量。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 运行设置

原论文白盒Table1：20个可优化token、500步、GCG batch512/top-k256；单样本实验前100条，通用攻击以25行为训练再用另100行为测试，分别报告train/test。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 官方脚本

https://github.com/llm-attacks/llm-attacks

[来源1](https://github.com/llm-attacks/llm-attacks)（访问2026-11-07）

### 可比性警示

ASR评价攻击效果，越高越危险；论文Table1前100样本白盒与Table2的388行为迁移测试不同，字符串触发/不拒绝也不等价于人工核验有害内容完成。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 Asia/Shanghai（UTC+8）

[来源1](https://llm-attacks.org/)（访问2026-11-07）

### 最新版本与采用证据

官方仓库data/advbench发布harmful_behaviors.csv和harmful_strings.csv；本轮按公开main与原论文v2核验，独立数据集版本号待核实。

> 字段状态：待核实

[来源1](https://github.com/llm-attacks/llm-attacks/tree/main/data/advbench)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1",
    "submitted_at": "2023-07-28T01:49:12+08:00",
    "timezone": "Asia/Shanghai（UTC+8）"
  },
  {
    "version": "v2",
    "submitted_at": "2023-12-21T04:48:57+08:00",
    "timezone": "Asia/Shanghai（UTC+8）"
  }
]
```

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 饱和情况

本页不据个别攻击99% ASR断言benchmark饱和或模型普遍不安全；ASR是攻击×目标模型×判定规则×预算的条件结果。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 污染与争议

规模冲突已并列：原论文500行为，官方CSV当前520行。StrongREJECT指出非拒答不代表有效有害回答，因此不同ASR裁判的结果不可直比。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/data/advbench/harmful_behaviors.csv)（访问2026-11-07）

### 版本与衍生关系

官方2024-08-01公告发布nanoGCG作为更易用的GCG算法实现；这是攻击实现更新，不等于AdvBench数据新版本。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 Asia/Shanghai（UTC+8）

[来源1](https://llm-attacks.org/)（访问2026-11-07）

### 官方榜单

https://arxiv.org/abs/2307.15043

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 分轨结果

#### 论文v2 Table1/前100行为白盒

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 不适用（来源内选列，非全局排名） | Vicuna-7B + GCG | 99.0 | individual Harmful Behavior ASR (%) | [原表](https://arxiv.org/abs/2307.15043) · 2026-11-07 |
| 不适用（来源内选列，非全局排名） | LLaMA-2-7B-Chat + GCG | 56.0 | individual Harmful Behavior ASR (%) | [原表](https://arxiv.org/abs/2307.15043) · 2026-11-07 |



#### 论文v2 Table1/通用后缀测试

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 不适用（来源内选列，非全局排名） | Vicuna-7B + GCG | 98.0 | multiple Harmful Behaviors test ASR (%) | [原表](https://arxiv.org/abs/2307.15043) · 2026-11-07 |
| 不适用（来源内选列，非全局排名） | LLaMA-2-7B-Chat + GCG | 84.0 | multiple Harmful Behaviors test ASR (%) | [原表](https://arxiv.org/abs/2307.15043) · 2026-11-07 |



> 原始历史实验，不是2026实时安全榜；ASR越高说明攻击更成功，不是受测模型更安全。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 覆盖说明

官方论文Table1转录四项历史GCG实验，按攻击设置分轨；本轮README未链接统一实时榜，当前跨模型排名待核实；不同攻击、裁判、预算不能混排。

> 字段状态：待核实

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）；[来源2](https://github.com/llm-attacks/llm-attacks)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 公开反馈

https://github.com/llm-attacks/llm-attacks/issues

> 公开反馈入口；未发送问题。

[来源1](https://raw.githubusercontent.com/llm-attacks/llm-attacks/main/README.md)（访问2026-11-07）

### 官方社交

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### 隐私说明/政策

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2307.15043

[来源1](https://arxiv.org/abs/2307.15043)（访问2026-11-07）

### PDF SHA-256

ab8745c2e3c6dfd939d5a590760bbae4682d92db010947cbb306688ad086bfd1

> 本轮实际下载字节的SHA-256；不表示已有Drive副本已替换。

[来源1](https://arxiv.org/pdf/2307.15043)（访问2026-11-07）

### PDF字节数

4656473

[来源1](https://arxiv.org/pdf/2307.15043)（访问2026-11-07）

### Drive文件夹

```json
{
  "id": "1k-z-nsz7sl4QiHxcjWQM2qSTeFtVv3_x",
  "webViewLink": "https://drive.google.com/drive/folders/1k-z-nsz7sl4QiHxcjWQM2qSTeFtVv3_x"
}
```

[来源1](https://drive.google.com/drive/folders/1k-z-nsz7sl4QiHxcjWQM2qSTeFtVv3_x)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1PyuJWY7qpUtChUoPScosfR0eqX-dPCaFCbHwLi2atC8",
    "webViewLink": "https://docs.google.com/document/d/1PyuJWY7qpUtChUoPScosfR0eqX-dPCaFCbHwLi2atC8/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1PyuJWY7qpUtChUoPScosfR0eqX-dPCaFCbHwLi2atC8/edit?usp=drivesdk)（访问2026-11-07）

### Drive论文副本

```json
{
  "id": "1YwG_SH_yRnyhuf_FPfhBigJl5Y4HfdYq",
  "webViewLink": "https://drive.google.com/file/d/1YwG_SH_yRnyhuf_FPfhBigJl5Y4HfdYq/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1YwG_SH_yRnyhuf_FPfhBigJl5Y4HfdYq/view?usp=drivesdk)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai (UTC+8)",
    "change": "Round2 q0：实际重读原始论文PDF、官方README/LICENSE、可用HF卡与排行榜；补方法、版本/样本/指标冲突及分轨结果，保留未核实信息。"
  }
]
```

[来源1](https://llm-attacks.org/)（访问2026-11-07）
