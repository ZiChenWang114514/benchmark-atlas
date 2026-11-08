# AQuA-RAT

> 核验日期：2026-11-07 （UTC+8）。未知保留待核实；访问日不是测量日。

官方证据复核；授权与版本冲突显式保留；未核实项不补造

带自然语言推理解释的五选一代数应用题。公开众包release与论文不能完整公开的先前版本不同；raw/tokenized是同题表示，不可双计题量。

## 基本信息

### 简称

AQuA-RAT

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 全称

Algebra Question Answering with Rationales

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 基准版本

公开众包release与原论文实验版不同；须指定发布文件

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 论文版本

arXiv v3

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 发布日期

2017-05-11 21:04:47 （UTC+8）（arXiv首稿，不等同数据发布声明）

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 主板块

数学

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 领域标签

- 代数应用题与推理

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 许可证

Apache-2.0（官方仓库 LICENSE；论文版本及第三方原始材料的权利需另辨）

[来源1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/LICENSE)（访问2026-11-07）

### 论文

https://arxiv.org/abs/1705.04146

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 官方代码

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 数据地址

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 官方入口

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 论文标题

Program Induction by Rationale Generation : Learning to Solve and Explain Algebraic Word Problems

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## 发起与维护

### 发起方

DeepMind、University of Oxford（论文署名）

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 作者

- Ling, Wang
- Yogatama, Dani
- Dyer, Chris
- Blunsom, Phil

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 维护方

Google DeepMind 官方 AQuA 仓库；不据仓库归属推断持续活跃维护。

[来源1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问2026-11-07）

### 资助方

待核实

> 字段状态：待核实

> 未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## 设计目标

### 衡量能力

从代数文字题生成自然语言推理依据并选择答案，研究rationale对求解和解释的帮助。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 设计背景

只预测选项无法观察模型如何组织数学推理；原工作同时建模解释。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## 构建方式

### 题目来源

论文收集GRE/GMAT风格网络题种子并用众包扩展；官方README强调公开release为完整众包数据。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 出题者背景

众包写题与写解释，研究团队开发rationale生成模型。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 审核流程

众包流程与去近重复过滤；公开发布版本与论文初始实验数据并非完全相同。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 质量控制

论文§2人工抽查众包任务并要求新题的答案/推理与seed不同；并不保证所有标签正确。HF公开预览存在推导与correct标签矛盾的个例，例如边长16的等边三角形题推导64√3、选项B却标D；仅作为样例错误，不估计整体错误率。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）

### 去污染

编辑距离过滤针对近重复，不保证语义改写分离或后续LLM无污染。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## 数据形式

### 题量与规模

公开每个raw/tokenized配置：train 97,467、validation 254、test 254，总97,975条；HF页面195,950为两个配置相加，不能当不同题数。

[来源1](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）；[来源2](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 题型

每题question、5个options、rationale、correct，正确选项A–E。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 难度

代数应用题/考试风格；rationale存在多种写法，答案正确不意味着解释逻辑完备。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 公开与隐藏划分

公开train/dev/test文件（含tokenized及raw两种同题表示）；原论文实验使用先前版本，README明确该版本不能完整公开，因此原表分数不保证在当前release复现。

[来源1](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）；[来源2](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

## 评测方法

### 指标

选项准确率；原论文还报告rationale的BLEU-4/困惑度，现代评测通常只看答案。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 评分

预测选项与correct对比；若评解释应独立报告，不能用选项accuracy替代解释质量。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 运行设置

原工作监督训练生成rationale后作答；CoT演示数、token预算及答案抽取需另外说明。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 官方脚本

https://github.com/google-deepmind/AQuA

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 可比性警示

原论文250测试与公开/Jev254测试、tok与untok、是否评价rationale均需区分。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源2](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 （UTC+8）

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 最新版本与采用证据

公开众包release与原论文实验版不同；须指定发布文件

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2017-05-11"
  }
  {
    "version": "v2"
    "submitted_at": "2017-10-10"
  }
  {
    "version": "v3"
    "submitted_at": "2017-10-24"
  }
]
```

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 饱和情况

第三方Jev实验在test254中最高94.1%，但选列模型、提示与标签噪声均限制解释；不是官方饱和结论。

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/deepmind/aqua_rat)（访问2026-11-07）

### 污染与争议

官方 README 明示：论文初始结果使用过一个无法完整发布的旧版本；当前公开数据为完全众包版本，运行论文系统所得分数会不同。不能把论文旧版数字和现行公开题库直接混排。

[来源1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问2026-11-07）

### 版本与衍生关系

MathQA从AQuA题源重标运算程序；两者不能按相同数据及评分方式处理。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源2](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 （UTC+8）

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 官方榜单

待核实

> 字段状态：待核实

> 未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 第三方覆盖

https://arxiv.org/html/2610.11978v1

> 研究论文Table2，不是持续维护排行榜。

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）

### 分轨结果

#### Jev论文Table2/非官方实时榜

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Qwen3.8-Max | 94.1 | Accuracy (%)，test254/单次运行 | [原表](https://arxiv.org/html/2610.11978v1) · 2026-11-07 |
| 2 | Qwen3.8-Flash | 91.7 | Accuracy (%)，test254/单次运行 | [原表](https://arxiv.org/html/2610.11978v1) · 2026-11-07 |
| 3 | Gemini 3.8 Flash | 91.3 | Accuracy (%)，test254/单次运行 | [原表](https://arxiv.org/html/2610.11978v1) · 2026-11-07 |



#### 原论文Table3/不可完整公开旧版本

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 不适用（来源内选列，非全局排名） | Our Model（program induction） | 36.4 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146) · 2026-11-07 |
| 不适用（来源内选列，非全局排名） | Seq2Seq | 20.8 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146) · 2026-11-07 |
| 不适用（来源内选列，非全局排名） | Seq2Seq + Copy Input | 20.4 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146) · 2026-11-07 |
| 不适用（来源内选列，非全局排名） | Seq2Seq + Copy Output | 20.2 | Accuracy (%) | [原表](https://arxiv.org/abs/1705.04146) · 2026-11-07 |



> 字段状态：待核实

> 重新打开Jev全文确认前三分数；其实际实验日期待核实，不沿用未经证实的2026-10-08。当前公开数据与原论文旧版本严格分轨。

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 覆盖说明

核验Jev全文Table2及附录A（test254，单次运行）和原论文Table3；两者不是同一版本/同一协议，不据选列分数宣称全局榜首。

[来源1](https://arxiv.org/html/2610.11978v1)（访问2026-11-07）；[来源2](https://arxiv.org/abs/1705.04146)（访问2026-11-07）；[来源3](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

- lingwang@google.com
- dyogatama@google.com
- cdyer@google.com
- pblunsom@google.com

> 仅论文首页公开科研邮箱。

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 公开反馈

https://github.com/google-deepmind/AQuA/issues

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）

### 官方社交

待核实

> 字段状态：待核实

> 未核实专门官方社交账号，不收录同名个人账户

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### 隐私说明/政策

待核实

> 字段状态：待核实

> 未核实benchmark专门隐私条款；许可证不能代替隐私政策

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/1705.04146

[来源1](https://arxiv.org/abs/1705.04146)（访问2026-11-07）

### PDF SHA-256

5111754b10c77d287685cc64992c92989eecc9b7cca65089f97c0efd48a4feb7

> 实际下载字节的SHA-256；不表示已有副本已替换。

[来源1](https://arxiv.org/pdf/1705.04146)（访问2026-11-07）

### PDF字节数

534332

[来源1](https://arxiv.org/pdf/1705.04146)（访问2026-11-07）

### 文件夹

```json
{
  "id": "14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc"
  "webViewLink": "
}
```

[来源1](

### 其他官方材料

```json
{
  "chinese_intro_doc": {
    "id": "1eZjRI88WySYba1wenrGtoejhe6_rdLemJEcXKXDbWLU"
    "webViewLink": "
    "mimeType": "application/vnd.google-apps.document"
  }
  "local_markdown": "content/benchmarks/aqua-rat.md"
}
```

[来源1](

### 论文副本

```json
{
  "id": "1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J"
  "webViewLink": "
}
```

[来源1](

## 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": "（UTC+8）"
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": "（UTC+8）"
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": " (UTC+8)"
    最近复核
  }
]
```

[来源1](https://github.com/google-deepmind/AQuA)（访问2026-11-07）
