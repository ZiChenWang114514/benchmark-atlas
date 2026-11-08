# miniF2F

> Benchmark Constitution，深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

miniF2F测的是给定形式化定理之后生成可被内核检查的证明，不是自然语言自动形式化，也不是只输出数值答案。原论文明确v1为488题；不同形式系统对同一题的翻译不能重复计作独立样本。阅读成绩时，必须同时看证明器、数学库及搜索预算。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### 简称

miniF2F

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 全称

miniF2F: a cross-system benchmark for formal Olympiad-level mathematics

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 基准版本

v1（2021年8月冻结；官方要求报告v1分支而不是开发main）

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### 论文版本

arXiv v2

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 发布日期

2021-09-01（arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 主板块

数学

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

### 领域标签

- Lean形式化数学证明

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 许可证与权利边界

按系统目录授权：Lean/Isabelle Apache-2.0、Metamath MIT、HOL Light FreeBSD。已逐一打开四个LICENSE，不能简写为全仓MIT。

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/lean/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/isabelle/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/metamath/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/hollight/LICENSE)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2109.00110

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 代码仓库

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

### 数据集入口

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 官方主页

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 论文标题

MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

École Polytechnique、OpenAI、University of Pittsburgh（论文署名）

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 合作方

待核实

> 仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 作者

- Zheng, Kunhao
- Han, Jesse Michael
- Polu, Stanislas

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 维护方

openai/miniF2F 官方仓库贡献者；README欢迎补充形式化题目与证明，不据此断言活跃维护频率。

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### 资助

待核实

> 未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## 设计目标

### 衡量能力

用形式化数学系统核验生成证明，并在不同定理证明器间建立共同竞赛数学评测。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 设计背景

非形式化最终答案评分不能严格证明推理正确，且旧形式化库题目难度与竞赛数学不一致。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## 构建方式

### 题目来源

从AMC、AIME、IMO、MATH及高中/本科数学题人工形式化，跨Lean、Metamath、Isabelle、HOL Light。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 出题与审阅者背景

受过形式化训练的实践者参与人工翻译，包括刚接触形式系统的学生；论文不要求全部是领域专家。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 审核流程

论文记录人工形式化后再复核；单题形式化平均约15分钟、复核约为其一半。对难以忠实形式化的自然语言题可舍弃，不能仅把编译通过当作题意复核。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 质量控制

按题源和MATH难度进行分层随机划分，使valid/test类型与难度平衡；选择题及求witness题有时将正确答案写入形式化陈述，会降低相对原题的难度。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 去污染及其证据边界

公开题目与形式陈述可进入预训练；内核通过仍需检查是否调用sorry、axiom或过强假设。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

原论文v2表1明确：v1共488个不同数学题，valid/test各244；当前README表中Lean、Metamath、Isabelle均244+244，HOL Light为165+165。README版本段的“244 statements”不能替代论文的完整题量定义。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### 题型

输入形式化定理陈述、生成证明脚本，由证明内核检查。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 模态

形式化符号/代码与数学文本

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 难度

奥赛及高中/本科数学；形式化陈述有时给出答案或witness，会改变相对于原题的难度。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 公开与隐藏划分

公开valid/test各244；训练时不得把测试证明或同题变体混入而不披露。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## 评测方法

### 指标

固定搜索预算下的证明成功率、pass@N等；H2研究另使用PAB。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 评分方法

正确性由形式系统内核判定；还需审计依赖的公理和被信任环境，编译成功本身不等同无漏洞证明。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 运行与提示设置

MCTS研究固定Lean4.15、Mathlib4.15(commit9837ca9d)、KiminaServer2.0，5个种子；预算PAB需保留。

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 官方脚本

https://github.com/openai/miniF2F

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 可比性警示

Lean3/Lean4、Mathlib版本、tactic集合、尝试数和PAB不同不可直接跨表比较。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

原版v1跨系统集合；现代Lean4移植需另记commit

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2021-09-01；- **timezone**：；- - **version**：v2；- **submitted_at**：2022-02-28；- **timezone**：
- **2026_h2_evidence**：- - **url**：https://arxiv.org/html/2608.28639v1；- **date**：2026-08-11；- **note**：Reward-Oracle MCTS 原始研究实际在 miniF2F 上比较三个证明模型及不同搜索预算；同时审计内核级证明有效性。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 饱和情况

复核的2026年MCTS研究在test 244、PAB256下报告Goedel 87.1 ± 0.2%；这是指定工具链与预算下的实验，不能推出所有移植版或更高预算的统一饱和度。

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 污染、争议与限制

H2 MCTS研究的sorryAx问题影响PutnamBench审计；作者明确本研究miniF2F成功证明未依赖sorryAx，不能把别的集合漏洞移植成miniF2F结论。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 衍生与版本关系

Lean4移植与各证明器fork应标明源码commit；不能把所有fork的分数归于同一固定v1工具链。

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）；[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（采集日，不是评测运行日）

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 官方入口

https://github.com/openai/miniF2F

> 原论文明确没有正式提交成绩流程；此链接是项目入口，不是假定存在官方实时排行榜。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 第三方覆盖入口

待核实

> 未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### 原论文v2表3 / Metamath / Pass@1

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| GPT-f | 1.3 | Pass@1 / % |

- **GPT-f**：- **scope**：v1 test244；每搜索128 expansions；GPT-f每扩展16 tactics，tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### 原论文v2表3 / Metamath / Pass@8

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| GPT-f | 1.6 | Pass@8 / % |

- **GPT-f**：- **scope**：v1 test244；每搜索128 expansions；GPT-f每扩展16 tactics，tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### 原论文v2表3 / Lean / Pass@1

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| tidy | 18.0 | Pass@1 / % |
| GPT-f / PACT 700M | 24.6 | Pass@1 / % |

- **tidy**：- **scope**：v1 test244；每搜索128 expansions；GPT-f每扩展16 tactics，tidy17
- **GPT-f / PACT 700M**：- **scope**：v1 test244；每搜索128 expansions；GPT-f每扩展16 tactics，tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### 原论文v2表3 / Lean / Pass@8

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| GPT-f / PACT 700M | 29.2 | Pass@8 / % |

- **GPT-f / PACT 700M**：- **scope**：v1 test244；每搜索128 expansions；GPT-f每扩展16 tactics，tidy17

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

#### 独立研究MCTS / miniF2F test244，PAB256，5种子

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Goedel-Prover-V2-8B + MCTS | 87.1 ± 0.2 | 证明成功率 / % |

- **Goedel-Prover-V2-8B + MCTS**：- **scope_and_protocol**：miniF2F test244，PAB256，5种子；- **result_date**：2026-08-11；- **snapshot_date**：2026-11-08；- **source_class**：研究论文实验，非官方实时榜；- **checkpoint_note**：模型名按来源原样；若来源未列API checkpoint则不补造。

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

#### 独立研究MCTS / 同研究，PAB32；与上一行不同预算

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Goedel-Prover-V2-8B + MCTS | 84.2 ± 0.5 | 证明成功率 / % |

- **Goedel-Prover-V2-8B + MCTS**：- **scope_and_protocol**：同研究，PAB32；与上一行不同预算；- **result_date**：2026-08-11；- **snapshot_date**：2026-11-08；- **source_class**：研究论文实验，非官方实时榜；- **checkpoint_note**：模型名按来源原样；若来源未列API checkpoint则不补造。

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

#### 独立研究MCTS / test244，PAB256

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| DeepSeek-Prover-V2-7B + MCTS | 82.6 ± 0.1 | 证明成功率 / % |

- **DeepSeek-Prover-V2-7B + MCTS**：- **scope_and_protocol**：test244，PAB256；- **result_date**：2026-08-11；- **snapshot_date**：2026-11-08；- **source_class**：研究论文实验，非官方实时榜；- **checkpoint_note**：模型名按来源原样；若来源未列API checkpoint则不补造。

[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）


[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

### 覆盖范围与时效

原论文历史基线与2026年MCTS论文实验分轨；后者不是官方实时榜。不同证明系统、PAB、Lean/Mathlib版本不能混排；未知独立第三方榜入口仍保留待核实。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）；[来源](https://arxiv.org/html/2608.28639v1)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

- kunhao.zheng@polytechnique.edu
- jessemichaelhan@openai.com

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 公开反馈

https://github.com/openai/miniF2F/issues

[来源](https://github.com/openai/miniF2F)（访问 2026-11-08）

### 官方社交

待核实

> 未核实专门官方社交账号，不收录同名个人账户

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### 隐私边界

待核实

> 未核实benchmark专门隐私条款；许可证不能代替隐私政策

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2109.00110

[来源](https://arxiv.org/abs/2109.00110)（访问 2026-11-08）

### PDF SHA-256

e4dcbd37330caffea6ebe2baa0f2f4cd3596d8a873c00f44ea2ce62ab0aaeea2

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### PDF字节数

267937

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2109.00110)（访问 2026-11-08）

### 文件夹

- **id**：1Z3ygLn9nvmJ7OL77CifV-VTo5oGqwfIa
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- **chinese_intro_doc**：- **id**：1SmDycpie2iIEWiJN5gjyYjX8Uqpogk5wCu4yuuFHLug；- **webViewLink**： **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/minif2f.md

[来源]( 2026-11-07）

### PDF归档

- **id**：1B_2BIieglqoGSpFwqs_vdOHBFMK1e4U8
- **webViewLink**：

[来源]( 2026-11-07）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/openai/miniF2F/main/README.md)（访问 2026-11-08）
