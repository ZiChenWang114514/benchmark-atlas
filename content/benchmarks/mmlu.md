# MMLU

> Benchmark Constitution，深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MMLU是覆盖57学科的英语四选一知识与问题求解测试，不是专家新编的隐藏题库。官方原论文与当前Hugging Face发行的实际划分数量不同，本页同时保留两种口径，不把历史README榜当作当代前沿排名。MMLU-Pro、Redux和多语变体改变了题库或协议，不能用名字相近就直接合并分数。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 简称

MMLU

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 全称

Massive Multitask Language Understanding

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 基准版本

原始MMLU（ICLR2021）；当前HF cais/mmlu为57学科配置，不等同MMLU-Pro、Redux或多语衍生版。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 论文版本

arXiv v3

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 发布日期

2020-09-08（arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 主板块

语言

> Benchmark Constitution编辑归档，不是论文指定的唯一领域。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 领域标签

- 多学科知识

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 许可证与权利边界

MIT（官方hendrycks/test master/LICENSE及cais/mmlu数据卡）；第三方题目来源的权利应另审查。

[来源](https://raw.githubusercontent.com/hendrycks/test/master/LICENSE)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2009.03300

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 代码仓库

https://github.com/hendrycks/test

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/cais/mmlu

> 官方原始data.tar仍由README链接；HF发布统计与论文存在差异，见题量字段。

[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）

### 官方主页

https://github.com/hendrycks/test

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 论文标题

Measuring Massive Multitask Language Understanding

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

论文作者单位包括 UC Berkeley、Columbia University、University of Chicago、UIUC；此处记录作者单位，不推断正式机构发起关系。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 合作方

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 作者

- Hendrycks, Dan
- Burns, Collin
- Basart, Steven
- Zou, Andy
- Mazeika, Mantas
- Song, Dawn
- Steinhardt, Jacob

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 维护方

官方公开代码托管于 hendrycks；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 资助

论文致谢列出 NSF Graduate Research Fellowship、Open Philanthropy AI Fellowship 与 NSF Frontier Award 1804794 等支持。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## 设计目标

### 衡量能力

衡量语言模型在广泛学科中的知识与问题求解能力，而非只在单一任务上训练后评测。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 设计背景

以往语言理解数据集往往狭窄、容易被任务微调或模式匹配攻克；本基准采用跨学科、零样本或少样本测试。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## 构建方式

### 题目来源

学生贡献者人工搜集网上可自由获取的考试、教材与练习题，覆盖人文、社会科学、STEM 和专业知识。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 出题与审阅者背景

论文说明题目主要由本科生搜集，并非所有题目均为领域专家原创。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 审核流程

作者整理各科选择题并形成开发、验证、测试划分；精确的逐题复核职责分配待进一步核实。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 质量控制

各题采用统一的四选一格式；后续 MMLU-Redux 研究仍发现歧义、标注和题目错误，不能视为已完全纠错。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 去污染及其证据边界

原论文附录以问题压缩/熵和答题正确率相关性分析GPT-3记忆风险，多数来源题答分处PDF或网页不同页；这是当时模型的诊断，不能推出后来公开题库无污染。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

原论文§3：test14,079、validation1,540、dev每科5题。当前cais/mmlu数据卡57科配置逐科合计test14,042、validation1,531、dev285；不含auxiliary_train。两个版本口径并列，删除无依据的“共15,908题”。

> 数据卡数量为57个学科配置num_examples的精确求和，不重复加all聚合配置。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 题型

四选一选择题

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 模态

文本

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 语言

英语

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 难度

从基础教育知识到大学及专业资格难度；学科间难度不同。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 公开与隐藏划分

开发示例、验证集、测试集均公开；不要把各划分混合评测。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## 评测方法

### 指标

选择题准确率，按任务汇总。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 评分方法

原始实验比较 A、B、C、D 选项的模型概率，取概率最高的选项。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 运行与提示设置

原始论文报告零样本、少样本等设置；标准少样本使用每科 5 道开发题。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 官方脚本

https://github.com/hendrycks/test

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 可比性警示

零样本、5-shot、CoT、学科宏平均与题目微平均不可不加标记地混比；MMLU 与其纠错/扩展/翻译版本也不同。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 当前数据与工具版本

原始MMLU论文与当前HF发行口径并存；当前HF test14,042/validation1,531/dev285，采用哪个发行文件需在实验里固定，不能默认为论文原始计数。

[来源](https://huggingface.co/datasets/cais/mmlu/raw/main/README.md)（访问 2026-11-08）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2020-09-08；- **timezone**：；- - **version**：v2；- **submitted_at**：2020-09-21；- **timezone**：；- - **version**：v3；- **submitted_at**：2021-01-13；- **timezone**：

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 饱和情况

MMLU-Pro原论文把原始MMLU前沿成绩趋于平台作为设计动机；原仓库历史榜不含当代前沿模型，不能用其67.5%最高分断言当前未饱和。

[来源](https://arxiv.org/pdf/2406.01574)（访问 2026-11-08）

### 污染、争议与限制

MMLU-Pro 与 MMLU-Redux 的原始研究分别指出简单题、噪声与标签错误；错误率随学科变化，不应把局部抽样错误率外推到全部题目。

[来源](https://arxiv.org/abs/2406.04127)（访问 2026-11-08）

### 衍生与版本关系

- MMLU-Pro
- MMLU-Redux
- MMMLU

[来源](https://arxiv.org/abs/2610.11978)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-08（采集日，不是评测运行日）

[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）

### 官方入口

https://github.com/hendrycks/test#test-leaderboard

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 第三方覆盖入口

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### 原始官方README历史榜

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Chinchilla (70B, few-shot) | 67.5 | Average accuracy / % |
| Gopher (280B, few-shot) | 60.0 | Average accuracy / % |
| GPT-3 (175B, fine-tuned) | 53.9 | Average accuracy / % |
| flan-T5-xl | 49.3 | Average accuracy / % |
| UnifiedQA | 48.9 | Average accuracy / % |
| GPT-3 (175B, few-shot) | 43.9 | Average accuracy / % |
| GPT-3 (6.7B, fine-tuned) | 43.2 | Average accuracy / % |
| flan-T5-large | 41.9 | Average accuracy / % |
| flan-T5-base | 34.2 | Average accuracy / % |
| GPT-2 | 32.4 | Average accuracy / % |
| flan-T5-small | 29.5 | Average accuracy / % |
| Random Baseline | 25.0 | Average accuracy / % |

- **Chinchilla (70B, few-shot)**：- **humanities**：63.6；- **social_sciences**：79.3；- **stem**：54.9；- **other**：73.9；- **authors**：Hoffmann et al., 2022；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **Gopher (280B, few-shot)**：- **humanities**：56.2；- **social_sciences**：71.9；- **stem**：47.4；- **other**：66.1；- **authors**：Rae et al., 2021；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **GPT-3 (175B, fine-tuned)**：- **humanities**：52.5；- **social_sciences**：63.9；- **stem**：41.4；- **other**：57.9；- **authors**：Brown et al., 2020；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **flan-T5-xl**：- **humanities**：46.3；- **social_sciences**：57.7；- **stem**：39.0；- **other**：55.1；- **authors**：Chung et al., 2022；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **UnifiedQA**：- **humanities**：45.6；- **social_sciences**：56.6；- **stem**：40.2；- **other**：54.6；- **authors**：Khashabi et al., 2020；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **GPT-3 (175B, few-shot)**：- **humanities**：40.8；- **social_sciences**：50.4；- **stem**：36.7；- **other**：48.8；- **authors**：Brown et al., 2020；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **GPT-3 (6.7B, fine-tuned)**：- **humanities**：42.1；- **social_sciences**：49.2；- **stem**：35.1；- **other**：46.9；- **authors**：Brown et al., 2020；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **flan-T5-large**：- **humanities**：39.1；- **social_sciences**：49.1；- **stem**：33.2；- **other**：47.4；- **authors**：Chung et al., 2022；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **flan-T5-base**：- **humanities**：34.0；- **social_sciences**：38.1；- **stem**：27.6；- **other**：37.0；- **authors**：Chung et al., 2022；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **GPT-2**：- **humanities**：32.8；- **social_sciences**：33.3；- **stem**：30.2；- **other**：33.1；- **authors**：Radford et al., 2019；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **flan-T5-small**：- **humanities**：29.9；- **social_sciences**：30.9；- **stem**：27.5；- **other**：29.7；- **authors**：Chung et al., 2022；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜
- **Random Baseline**：- **humanities**：25.0；- **social_sciences**：25.0；- **stem**：25.0；- **other**：25.0；- **authors**：N/A；- **scope**：不同few-shot/fine-tuned设置按原表保留，不是2026统一实时榜

[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）


[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）

### 覆盖范围与时效

以官方 README 可读表替代非官方研究比较表作为本栏快照；榜单未给统一更新日期，模型年代和提示协议不同，禁止视为2026前沿排名。

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 公开反馈

https://github.com/hendrycks/test/issues

[来源](https://github.com/hendrycks/test)（访问 2026-11-08）

### 官方社交

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2009.03300

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF SHA-256

d3a7b0f8589f5365ebfd34a3876a9a8b3fde83e0adb9ed19ccf8f0034bb48fc1

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF字节数

2074939

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### 文件夹

- **id**：16jdkBY7vMWPeny-ZoCn5i4limN90OF26
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍；- **id**：10X_jNgeT4GCIeP3q17ZGinf7YmmYmD1g4wxlM6aLIOc；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：1_7QVvJvbgngMAfsCYTyOLG7QjAa1NbO9
- **webViewLink**：

[来源]( 2026-11-07）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/hendrycks/test/master/README.md)（访问 2026-11-08）
