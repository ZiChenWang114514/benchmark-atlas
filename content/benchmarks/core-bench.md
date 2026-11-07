# CORE-Bench

> Benchmark Constitution · 深度核验快照 2026-11-07。待核实不等于未公开；采集日期不等于榜单更新时间。

CORE-Bench要求Agent利用研究者已发布的代码和数据复现结果并回答问题，不是从论文描述重新实现整个研究。90篇论文生成270个难度任务，同篇的Easy/Medium/Hard共享研究问题；论文级45/45划分、任务内全题正确和多次运行平均是解释分数的关键。

导读依据：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）；[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

## 基本信息

**简称**：CORE-Bench

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

**全称**：Computational Reproducibility Agent Benchmark（CORE-Bench）

来源：[1](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md)（访问2026-11-07）；[2](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）

**基准版本**：原始90篇论文×3级=270任务

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**论文版本**：arXiv v2

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：论文修订版本不等同数据集版本。

**发布日期**：2024-09-18 02:13:19 KST

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

**主板块**：Agent

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

**领域**：科学计算结果复现Agent

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**许可与范围**：官方GitHub代码/LICENSE及HF数据卡均标MIT；HF主要提供任务元数据而非研究capsule，capsule所含论文代码/数据仍核各自授权。

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/LICENSE)（访问2026-11-07）；[2](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md)（访问2026-11-07）

**论文/技术报告**：https://arxiv.org/abs/2409.11363

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**代码**：https://github.com/siegelz/core-bench

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

**数据**：https://huggingface.co/datasets/siegelz/core-bench

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）

**主页**：https://github.com/siegelz/core-bench

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

**论文标题**：CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

## 发起与维护

**发起/作者单位**：Princeton University 作者团队

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**合作关系**：待核实

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**作者**：Zachary S. Siegel；Sayash Kapoor；Nitya Nadgir；Benedikt Stroebl；Arvind Narayanan

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**维护方**：siegelz / CORE-Bench项目团队

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**资助**：Princeton CSML compute；OpenAI researcher access支持。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

## 设计目标

**测量能力**：通过已有研究代码与环境重新执行实验、读取输出并回答科学结果问题。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**针对的不足**：计算可复现性既是研究可信度问题，也是需要工具、软件环境与结果解释的Agent综合任务。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

## 构建方式

**材料来源**：Code Ocean上的90篇计算机科学、社会科学和医学论文的代码capsule。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**出题背景**：Princeton研究团队人工整理可复现问题。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**审核**：每个capsule人工运行3次，验证问题可答与输出稳定性。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**质控**：确定性输出精确答案；非确定性数值用重复运行构造95%预测区间。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**去污染边界**：论文级split避免同篇跨train/test；评测禁止从Code Ocean取现成输出。测试元数据和解密方式公开，公开代码/论文的预训练泄漏不能排除。

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）；[2](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）

## 数据形式

**规模与统计口径**：90论文、270任务（每篇3难度）；45论文train/45test；181个独特问题被复用于各难度，不等于270篇论文。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**任务形式**：读取科研任务与问题、安装依赖、执行Python/R代码复现结果，并把问题到答案的键值写入report.json。

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）

**模态**：论文/README文本；代码；实验数据/结果文件

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**语言**：Python / R科研代码；英语问题与文档。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**难度**：Easy给出输出；Medium给Dockerfile+README；Hard只有README，需自行配置执行。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**公开/保留划分**：按论文45 train/45 test；测试任务元数据以GPG文件发布，官方README给公开解密方法。capsule代码/数据由Princeton服务器按ID另下载；不是永久私有题库。

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）；[2](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md)（访问2026-11-07）；[3](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）

## 评测方法

**指标**：任务全问题正确率；按Easy/Medium/Hard分别报告。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**评分**：一项任务内全部问题都正确才通过，数值允许按官方区间检查。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**提示与运行设定**：CORE-Agent / AutoGPT等harness与模型快照、环境信息权限必须注明；禁止浏览Code Ocean找输出。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**脚本/运行入口**：推荐HAL harness：https://github.com/princeton-pli/hal-harness；旧版：https://github.com/siegelz/core-bench（不再积极维护）。

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）

**可比性**：不同难度提供信息不同；270任务存在同篇与同问题复用，不能解释为270独立科学研究复现。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07 KST / Asia/Seoul

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

**当前版本证据**：version：原始270任务；原harness已不再积极维护，官方推荐HAL harness；evidence_2026_h2：url：https://arxiv.org/html/2609.19134v1；date：2026-09-16；note：ScienceIDE §4.1及参考文献明确引用 CORE-Bench，讨论以已有研究结果复现为目标的评价；为H2学术引用。

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）；[2](https://arxiv.org/html/2609.19134v1)（访问2026-11-07）

**修订历史**：Submission history From: Zachary Siegel [ view email ] [v1] 2024-09-18 02:13:19 KST (2,912 KB) [v2] 2026-06-23 07:36:12 KST (2,906 KB)

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**饱和**：待核实

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**争议与局限**：非确定性实验、依赖安装和数据下载会影响复现；论文Easy结果存在60.00/60.60文本冲突，保留而不擅自修正。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

**派生/去重**：Easy/Medium/Hard为同一套件信息权限级别，计一个benchmark；与从头复写论文的PaperBench不同。

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

## 榜单快照

**快照日**：2026-11-07 KST / Asia/Seoul

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

**官方榜**：https://agent-evals-leaderboard.hf.space

来源：[1](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）

核验说明：由官方README指定；本轮访问返回503，分数和榜单更新日期保留待核实。

**独立评测**：待核实

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

核验说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 分轨结果（不合并来源/题集/协议）

**论文v2 Table 5 / test / Easy**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | CORE-Agent + gpt-4o-2024-05-13 | 60.0 | task pass@1 (%) |
| 2 | CORE-Agent + gpt-4o-mini-2024-07-18 | 44.44 | task pass@1 (%) |
| 3 | AutoGPT + gpt-4o-2024-05-13 | 35.56 | task pass@1 (%) |
| 4 | AutoGPT + gpt-4o-mini-2024-07-18 | 8.89 | task pass@1 (%) |

protocol：CORE-Agent 3次运行平均；AutoGPT 1次

来源：[https://arxiv.org/pdf/2409.11363](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**论文v2 Table 5 / test / Medium**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | CORE-Agent + gpt-4o-2024-05-13 | 57.78 | task pass@1 (%) |
| 3 | CORE-Agent + gpt-4o-mini-2024-07-18 | 32.59 | task pass@1 (%) |
| 2 | AutoGPT + gpt-4o-2024-05-13 | 37.78 | task pass@1 (%) |
| 4 | AutoGPT + gpt-4o-mini-2024-07-18 | 2.22 | task pass@1 (%) |

protocol：CORE-Agent 3次运行平均；AutoGPT 1次

来源：[https://arxiv.org/pdf/2409.11363](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**论文v2 Table 5 / test / Hard**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | CORE-Agent + gpt-4o-2024-05-13 | 21.48 | task pass@1 (%) |
| 2 | CORE-Agent + gpt-4o-mini-2024-07-18 | 16.3 | task pass@1 (%) |
| 3 | AutoGPT + gpt-4o-2024-05-13 | 6.67 | task pass@1 (%) |
| 4 | AutoGPT + gpt-4o-mini-2024-07-18 | 2.22 | task pass@1 (%) |

protocol：CORE-Agent 3次运行平均；AutoGPT 1次

来源：[https://arxiv.org/pdf/2409.11363](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：实时HAL链接本次返回503，未取得当前总榜；完整录入论文v2 Table 5的四配置×三难度历史基线，修正旧条目误指Table 1。Easy主表60.00与正文/附录60.60冲突并列说明。Hard附录单次test pass@1 22.2不同于三次平均21.48，不能混排。

来源：[1](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）；[2](https://raw.githubusercontent.com/siegelz/core-bench/main/README.md)（访问2026-11-07）；[3](https://agent-evals-leaderboard.hf.space)（访问2026-11-07）

## 联系方式

**公开研究邮箱**：zachary@siegel.com；zss@princeton.edu；sayashk@princeton.edu；nn7887@princeton.edu；stroebl@princeton.edu；arvindn@cs.princeton.edu

来源：[1](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）；[2](https://huggingface.co/datasets/siegelz/core-bench/raw/main/README.md)（访问2026-11-07）

核验说明：论文公开zachary@siegel.com，HF数据卡另列zss@princeton.edu；保留来源差异，仅列公开研究联系地址。

**Issues**：https://github.com/siegelz/core-bench/issues

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）

核验说明：公开仓库反馈入口；未发送问题。

**公开社区**：待核实

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**隐私原则**：待核实

来源：[1](https://arxiv.org/abs/2409.11363)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

**PDF**：https://arxiv.org/pdf/2409.11363

来源：[1](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）

核验说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

**原件SHA-256**：1d1fbe8a3cf472fc468495e6a3bcd6b90224ba1eae3dac8d8174f98d666c3d76

来源：[1](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）

核验说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

**PDF字节数**：2885202

来源：[1](https://arxiv.org/pdf/2409.11363)（访问2026-11-07）

核验说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

**Drive目录**：id：1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl；webViewLink：https://drive.google.com/drive/folders/1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl

来源：[1](https://drive.google.com/drive/folders/1E-Hv1SyK00WNfo687WrhcDLj5vqJ2pDl)（访问2026-11-07）

**其他文档**：type：中文介绍Google Doc；id：1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA；webViewLink：https://docs.google.com/document/d/1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA/edit?usp=drivesdk

来源：[1](https://github.com/siegelz/core-bench)（访问2026-11-07）；[2](https://docs.google.com/document/d/1fsTi4y2eCdou0kLx6j5H2XfISM18p2lQ8qrQ5miLPEA/edit?usp=drivesdk)（访问2026-11-07）

核验说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

**Drive PDF**：id：1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8；webViewLink：https://drive.google.com/file/d/1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1bQtKC7OaO6g7Loph76jiNaLKzFcJZsG8/view?usp=drivesdk)（访问2026-11-07）

## 变更记录

- date：2026-11-07；timezone：KST / Asia/Seoul；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；timezone：KST / Asia/Seoul；change：第1轮深度优化：重开官方材料，补充版本、许可证范围、数据划分、维护迁移及评分可比性；区分实时榜与历史结果，保留冲突与未核实字段。
- date：2026-11-07；timezone：Asia/Seoul；change：第2轮深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
