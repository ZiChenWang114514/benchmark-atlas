# CRUXEval

> Benchmark Constitution，深度核验快照 2026-11-07。待核实不等于未公开；采集日期不等于榜单更新时间。

CRUXEval用800个短Python函数及真实执行产生的输入输出配对，分别测输入反推和输出预测。I/O共享样本，不应凑成两个独立题库；direct、CoT、pass@1和pass@5各有不同含义。本次明确核实HF数据本身也为MIT，并把静态榜分成八条协议轨。

导读依据：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）；[1](https://crux-eval.github.io/)（访问 2026-11-07）

## 基本信息

**简称**：CRUXEval

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**全称**：Code Reasoning, Understanding, and eXecution Evaluation（CRUXEval）

来源：[1](https://huggingface.co/datasets/cruxeval-org/cruxeval/raw/main/README.md)（访问 2026-11-07）

**基准版本**：原始 800 函数；CRUXEval-I / CRUXEval-O 双方向

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**论文版本**：arXiv v1

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：论文修订版本不等同数据集版本。

**发布日期**：2024-01-06 05:53:51

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：首次 arXiv 论文提交时间，已转；不自动视为数据集首发时间。

**主板块**：代码

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

**领域**：代码输入输出推断

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**许可与范围**：MIT：GitHub LICENSE与官方HF数据卡均明确标示；因此数据授权不再只推断自代码许可。

来源：[1](https://raw.githubusercontent.com/facebookresearch/cruxeval/main/LICENSE)（访问 2026-11-07）；[2](https://huggingface.co/datasets/cruxeval-org/cruxeval/raw/main/README.md)（访问 2026-11-07）

**论文/技术报告**：https://arxiv.org/abs/2401.03065

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**代码**：https://github.com/facebookresearch/cruxeval

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**数据**：https://huggingface.co/datasets/cruxeval-org/cruxeval

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**主页**：https://crux-eval.github.io/

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**论文标题**：CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 发起与维护

**发起/作者单位**：MIT 与 Meta AI 作者团队（作者单位口径）

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**合作关系**：论文单位为MIT CSAIL与Meta AI；首位作者注明主要工作在Meta AI实习期间完成。按研究参与关系记录，不推断法律合作协议。

来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

**作者**：Gu, Alex；Rozière, Baptiste；Leather, Hugh；Solar-Lezama, Armando；Synnaeve, Gabriel；Wang, Sida I.

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**维护方**：facebookresearch/cruxeval当前已标为archived（2026-11-07核验）；历史维护方为CRUXEval团队，不能推断仍在活跃维护。

来源：[1](https://github.com/facebookresearch/cruxeval)（访问 2026-11-07）

**资助**：A. Gu获NSF Graduate Research Fellowship Grant 2141064；A. Solar-Lezama获NSF及Intel Corporation经NSF CCF:2217064支持（论文致谢）。

来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

## 设计目标

**测量能力**：代码理解、输入反推和输出预测，尤其在不运行代码时模拟程序执行。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**针对的不足**：生成代码的成功率无法独立揭示模型是否理解简单程序的执行语义。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 构建方式

**材料来源**：使用 CodeLlama-34B 生成候选 Python 函数及输入输出，经筛选后随机抽取 800 个。

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**出题背景**：MIT / Meta AI 研究者；候选程序由模型合成。

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**审核**：筛选约可由程序员一分钟内心算的短函数与有效输入输出。

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**质控**：限制程序复杂性并执行验证配对的输入输出；双方向共用程序，不能算成两个独立题库。

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**去污染边界**：合成新程序旨在减少既有人工题复用，但不构成所有后续模型的无污染证明。

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

## 数据形式

**规模与统计口径**：800 个 Python 函数/输入/输出样本；输入预测与输出预测是同一数据的两种评测。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**任务形式**：CRUXEval-I：给程序与输出求可行输入；CRUXEval-O：给程序与输入求输出。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**模态**：代码；文本

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**语言**：Python；英语提示。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**难度**：短小、可人类心算的程序也可能难于模型；不等同软件开发难度。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**公开/保留划分**：原始数据、脚本与提示公开；未据此主张隐藏集。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 评测方法

**指标**：按方向分别报告 pass@1 / pass@5 等；CoT 与直接回答分开。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**评分**：输出预测检查程序真实输出；输入预测接受能经执行产生目标输出的有效输入。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**提示与运行设定**：论文分别报告直接作答与 chain-of-thought；提示、采样数、是否使用执行工具必须说明。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**脚本/运行入口**：https://github.com/facebookresearch/cruxeval

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**可比性**：CRUX-I / CRUX-O 分数不平均冒称单一官方总分；不把带解释提示与直接预测混排。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**当前版本证据**：version：原始 800 函数；CRUXEval-I / CRUXEval-O 双方向；evidence_2026_h2：url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1/§4.2及表2–4实际报告 CRUXEval；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。

来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）；[2](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

**修订历史**：Submission history From: Alex Gu [ view email ] [v1] 2024-01-06 05:53:51 (1,309 KB)

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**饱和**：待核实

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**争议与局限**：Hunyuan 报告参考文献把 CRUXEval 关联到 Liu 2023（EvalPlus）；本条依 Gu 等人 2401.03065 识别原基准。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

**派生/去重**：CRUXEval-I 与 CRUXEval-O 是同一 benchmark 两个子任务。

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

## 榜单快照

**快照日**：2026-11-07

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**官方榜**：https://crux-eval.github.io/leaderboard.html

来源：[1](https://crux-eval.github.io/leaderboard.html)（访问 2026-11-07）

**独立评测**：待核实

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

核验说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 分轨结果（不合并来源/题集/协议）

**CRUXEval official CSV / direct / i@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613 | 69.8 | i@1 (%) |
| 2 | gpt-4-turbo-2024-04-09 (n=3) | 68.5 | i@1 (%) |
| 3 | gpt-4o (n=3) | 65.1 | i@1 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / direct / i@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613 | 76.8 | i@5 (%) |
| 2 | codetulu-2-34b | 68.0 | i@5 (%) |
| 3 | starcoder2-15b | 66.9 | i@5 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / direct / o@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4o (n=3) | 70.0 | o@1 (%) |
| 2 | gpt-4-0613 | 68.7 | o@1 (%) |
| 3 | gpt-4-turbo-2024-04-09 (n=3) | 67.7 | o@1 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / direct / o@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613 | 73.0 | o@5 (%) |
| 2 | deepseek-instruct-33b | 61.8 | o@5 (%) |
| 3 | deepseek-base-33b | 61.6 | o@5 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / i@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-turbo-2024-04-09+cot (n=3) | 75.7 | i@1 (%) |
| 2 | gpt-4o+cot (n=3) | 75.6 | i@1 (%) |
| 3 | gpt-4-0613+cot | 75.5 | i@1 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / i@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613+cot | 88.9 | i@5 (%) |
| 2 | gpt-3.5-turbo-0613+cot | 74.9 | i@5 (%) |
| 3 | codellama-34b+cot | 73.8 | i@5 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / o@1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-turbo-2024-04-09+cot (n=3) | 82.0 | o@1 (%) |
| 1 | claude-3-opus+cot (n=1) | 82.0 | o@1 (%) |
| 3 | gpt-4-0613+cot | 77.1 | o@1 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**CRUXEval official CSV / CoT / o@5**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-4-0613+cot | 88.2 | o@5 (%) |
| 2 | gpt-3.5-turbo-0613+cot | 76.7 | o@5 (%) |
| 3 | codellama-34b+cot | 69.4 | o@5 (%) |

来源：[https://crux-eval.github.io/data.csv](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：直接重读官方data.csv（43配置）；分别对direct/CoT、I/O及pass@1/pass@5共8轨列前三，剔除模型名明确under verification两行并保留n配置。并列使用competition rank。此为静态榜快照非2026全球SOTA；本快照不将旧厂商自报混入官方排名。

来源：[1](https://crux-eval.github.io/data.csv)（访问 2026-11-07）

## 联系方式

**公开研究邮箱**：gua@mit.edu；broz@meta.com；hleather@meta.com；asolar@csail.mit.edu；gab@meta.com；sida@meta.com

来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

**Issues**：https://github.com/facebookresearch/cruxeval/issues

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

核验说明：公开仓库反馈入口；未发送问题。

**公开社区**：待核实

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**隐私原则**：待核实

来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

**PDF**：https://arxiv.org/pdf/2401.03065

来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

核验说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

**原件SHA-256**：1a356948d0d2543ab7b142029f208271a2581575cee4f5b37eb647cbbf0b435e

来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

核验说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

**PDF字节数**：2012215

来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

核验说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](

来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）；[2](

核验说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](

## 变更记录

- date：2026-11-07；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；change：深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- date：2026-11-07；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
