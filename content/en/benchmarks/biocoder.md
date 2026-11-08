# BioCoder

> Check: 2026-11-07. This page is a sourced research snapshot; the collection date is not treated as the experiment date. Unverified is not the same as Not disclosed.

Item-by-item empirical review: the paper PDF, official release materials, and per-protocol leaderboards; items that are not confirmed continue to be retained.

## Basic information

### Short name

BioCoder

### Full name

BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models

### 数据/软件版本

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### Paper version

arXiv v5: 2024-05-21 02:19:13; also Bioinformatics 40(Supplement_1):i266–i276, 2024, doi:10.1093/bioinformatics/btae230.

### Release date

2023-08-31 (date of the first arXiv version; not an inferred date on which the data went online).

### Section

Biology and medicine

Note: The editorial section follows the selection list. It does not mean the benchmark measures only that section.

### 学科标签

Bioinformatics code generation

### 许可证与范围

The HF dataset card linked from the official README is marked CC-BY-4.0; the website source states CC-BY-SA-4.0. No code license was found in LICENSE or LICENSE.md at the repository root, and the website license or the HF data license cannot be extended automatically to the whole code repository and to all third-party source code.

Note: The licenses for the data and the website have been verified; the overall license for the code remains Unverified.

Status: Unverified (part of this field is still unconfirmed).

### 论文入口

https://arxiv.org/abs/2308.16458

### Paper title

BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models

### Code

https://github.com/gersteinlab/BioCoder

### Dataset

https://huggingface.co/datasets/lilbillbiscuit/biocoder_public

### Official homepage

https://biocoder-benchmark.github.io/

## Origin and maintenance

### 发起团队

A collaboration between paper authors at Yale and Google DeepMind.

### 署名/合作机构

Yale University；Google DeepMind

Note: Author affiliations as signed on the paper; the first four authors and Mark Gerstein are at Yale, and Xinyun Chen is at Google DeepMind.

### Authors

Tang, Xiangru；Qian, Bill；Gao, Rick；Chen, Jiakang；Chen, Xinyun；Gerstein, Mark

### 维护入口

gersteinlab/BioCoder and the official project page.

### 资助与计算资源

Schmidt Futures supports Mark Gerstein and Xiangru Tang (thanked explicitly in the Acknowledgment of the original paper).

## Design goals

真实项目上下文与fuzz功能等价检查比孤立短函数更贴近生物信息工程，但测试通过仍受输入覆盖限制。源代码公开和作者混淆消融只说明记忆风险被分析过，不意味着训练/评测完全隔离。

### 测量能力

Bioinformatics function-code generation in real context, including dependencies, classes, and global variables.

### 为何需要这个基准

Ordinary short-function questions do not adequately test biological knowledge, complex data operations, and real project context.

## Construction

### 材料来源

Python functions, Java methods, and Rosalind programming problems from GitHub biology projects.

### 命题/编制背景

The Yale/Google DeepMind research team on bioinformatics and code generation; it is not claimed that every question is an independent expert original.

### Review process

Real functions are extracted by syntactic parsing, and verification is built by combining static analysis, human tests, and fuzzing.

### Quality control

A Docker-executable test environment and automated fuzzing, retaining dependencies, classes, and the global environment.

### 去污染与证据边界

Appendix M changes function names and parameters to forms such as FUNCTION/VAR0 for an obfuscation ablation, which reduces the effect of remembering the code directly; this is not strict isolation of the training corpus. In that ablation, Python Pass@1 falls from 25.960 to 22.771 and Java from 34.700 to 30.700; this is a specific prompt and a specific experiment, and it does not replace the official Summary Only leaderboard.

## Data format

### 规模与分母

1,026 Python functions and 1,243 Java methods, plus 253 Rosalind examples; these must not be conflated into a total question count for one language.

### Question types

Generate a function or method body from a signature, context, or description; multiple prompt layouts.

### 模态与字段

### Languages

Python；Java；英语提示

### 难度定位

Real project dependencies and professional bioinformatics tasks; there is no unified difficulty banding.

### 公开、隐藏与划分

The README lists java_hidden 1,243 and python_hidden 1,026; each also has 50 public items and 50 similar items; rosalind has 253 items. The name hidden does not mean that access is currently restricted: the README states explicitly that the complete public data have been published in the repository.

## Evaluation

### Metrics

Pass@1/5/10/20, split by Python, Java, and Rosalind.

### 评分流程

Whether a result is Passed is decided by running the code and by fuzz-testing. The Rosalind example generates 20 times per question, estimates Pass@1, Pass@5, Pass@10, and Pass@20 from the combined probability, and averages across questions. Pass@20 cannot be treated as the accuracy of a single generation.

### 运行与提示

The official Summary Only leaderboard: temperature 0.7, top-p 0.95, and a maximum generation of 256 tokens; GPT4 context 8192.

### 评测实现

evaluation/ in the official repository contains the Docker and AWS queue execution framework. TestRosalind/tester.py generates results.json. The README notes that a fully local framework is a plan for the future, and it does not claim that one is already provided.

### 不能混比的设置

Differences in prompt layout, context window, generation length, and language affect results. Model dates on the official site are historical labels and should not be miswritten as the model ranking on the collection date.

## Current status

### 核查日期

2026-11-07 (collection date, not the experiment date)

### 当前发布

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 版本脉络

v1：2023-08-31；v2：2023-09-06；v3：2023-09-30；v4：2023-12-04；v5：2024-05-21；journal：Bioinformatics2024 doi:10.1093/bioinformatics/btae230; the revision date of the paper is not treated as the date the data were updated.

### 分数上限与饱和度

A historically low pass rate on the official website does not indicate the current upper bound for models in 2026; an updated unified experiment has not been obtained.

### 争议与局限

Public code on GitHub and the Rosalind questions can enter pretraining. The paper includes an ablation on confusion of names and of parameters, but that ablation cannot rule out data leakage. Coverage of the fuzz tests is limited. GPT-assisted filtering of bioinformatics code can produce selection bias. A historical label on the official site is not the time at which a model was actually tested.

### 衍生版本

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date, not the experiment date)

### Official entry

https://biocoder-benchmark.github.io/

### 第三方/补充实验

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 分轨成绩

#### BioCoder-Py / Summary Only / historical display order on the official site

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | gpt-4 | 38.439 | Pass@1 (%) |
| 2 | gpt-3.5-turbo | 24.682 | Pass@1 (%) |
| 3 | Starcoder | 4.682 | Pass@1 (%) |

- gpt-4：pass_at_5：48.491；pass_at_10：50.619；pass_at_20：52.229；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1
- gpt-3.5-turbo：pass_at_5：33.997；pass_at_10：37.132；pass_at_20：40.127；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1
- Starcoder：pass_at_5：15.225；pass_at_10：21.2；pass_at_20：27.166；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1

#### BioCoder-Java / Summary Only / historical display order on the official site

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | gpt-4 | 45.011 | Pass@1 (%) |
| 2 | gpt-3.5-turbo | 17.4 | Pass@1 (%) |
| 3 | Starcoder+ | 1.3 | Pass@1 (%) |

- gpt-4：pass_at_5：55.35；pass_at_10：57.616；pass_at_20：60.0；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1
- gpt-3.5-turbo：pass_at_5：33.199；pass_at_10：37.878；pass_at_20：42.0；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1
- Starcoder+：pass_at_5：5.031；pass_at_10：8.042；pass_at_20：12.0；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1

#### BioCoder-Rosalind / Summary Only / historical display order on the official site

| Source order / track index | Model / system | Score | Metric |
|---|---|---:|---|
| 1 | gpt-4 | 24.308 | Pass@1 (%) |
| 2 | gpt-3.5-turbo | 23.671 | Pass@1 (%) |
| 3 | Starcoder | 0.534 | Pass@1 (%) |

- gpt-4：pass_at_5：39.551；pass_at_10：44.864；pass_at_20：50.198；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1
- gpt-3.5-turbo：pass_at_5：31.953；pass_at_10：36.702；pass_at_20：40.725；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1
- Starcoder：pass_at_5：2.042；pass_at_10：3.228；pass_at_20：4.743；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：Historical leaderboard readable on the official site; not a new 2026 experiment；ranking_note：In the order shown on the web page; Rosalind Starcoder’s Pass@1 is lower than the CodeGen that follows it, and the page may be sorted by a different K. This page does not claim to reorder by Pass@1

### 覆盖边界

The Python, Java, and Rosalind tracks on the official site were each transcribed for Summary Only and for the full Pass@1/5/10/20, following the displayed sequence. A ranking by Pass@20 is not, on its own, presented as a ranking by Pass@1. The model-row labels on the site are 2023 model dates, and they do not confirm a measurement date for each row. The scores remain a historical leaderboard. Tables 4/5 of the paper and the confusion ablation are other protocols and are not merged with this one.

## Contact

### 公开作者工作邮箱

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 公开反馈

https://github.com/gersteinlab/BioCoder/issues

### 官方账号

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

### 隐私信息

Unverified

Note: The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

Status: Unverified (part of this field is still unconfirmed).

## Original files

### 原文PDF

https://arxiv.org/pdf/2308.16458

### 下载源文件SHA-256

c10e1ca00454f617439153c6646eb406ea01ffc3bf14fef420a6968223858b1e

Note: Checksum of the PDF bytes downloaded from the source site. This does not claim that the file contents were checked again.

### 下载源文件字节数

1569722

### 既有 PDF链接

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## Changelog

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：深度优化：打开Official README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- 2026-11-07（）：实际读取论文摘要和PDF全文、Official README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

### 来源索引

[1]: https://arxiv.org/abs/2308.16458 "访问 2026-11-07"
[2]: https://raw.githubusercontent.com/gersteinlab/BioCoder/main/README.md "访问 2026-11-07"
[3]: https://arxiv.org/html/2610.21074v1 "访问 2026-11-07"
[4]: https://huggingface.co/datasets/lilbillbiscuit/biocoder_public/raw/main/README.md "访问 2026-11-07"
[5]: https://biocoder-benchmark.github.io/ "访问 2026-11-07"
[6]: https://huggingface.co/datasets/lilbillbiscuit/biocoder_public "访问 2026-11-07"
[7]: https://arxiv.org/pdf/2308.16458 "访问 2026-11-07"
[8]: https://github.com/gersteinlab/BioCoder "访问 2026-11-07"
[9]: "访问 2026-11-07"
