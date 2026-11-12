# ChemLLMBench

> Benchmark Constitution, in-depth verification snapshot 2026-11-07. Unverified is not the same as Not disclosed; the collection date is not the leaderboard update time.

ChemLLMBench is not a set of multiple-choice questions on chemistry knowledge. It is an eight-task experimental suite that uses existing molecule and reaction data to test three kinds of ability: understanding, reasoning, and explanation. The metrics of tasks such as molecule design, retrosynthesis, and yield classification cannot stand in for one another; the 100 test instances in Table 1 of the paper are the accounting of a single experiment and should not be written directly as 800 independent questions in the full bank.

Basis of the reading guide: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

## Basic information

**简称**：ChemLLMBench

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**全称**：ChemLLMBench

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

**基准版本**：The original suite of 8 tasks that accompanies the paper; the README has a data and prompt update from 2023-12 and does not claim a unified semantic version of the data.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**论文版本**：arXiv v3

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**发布日期**：2023/05/27

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**主板块**：化学

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07)

核验说明：Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

**领域**：化学

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**许可与范围**：待核实

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：A single license has not been verified in the official README or at the root of the repository; the paper lists several upstream projects as MIT, which does not mean that the whole of the aggregated repository is MIT. The introvoyz041 copy on HF that was retrieved is not the official release indicated by the README.

**论文/技术报告**：https://arxiv.org/abs/2305.18365

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**代码**：https://github.com/ChemFoundationModels/ChemLLMBench

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**数据**：https://github.com/ChemFoundationModels/ChemLLMBench/tree/main/data

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**主页**：https://github.com/ChemFoundationModels/ChemLLMBench

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**论文标题**：What can Large Language Models do in chemistry? A comprehensive benchmark on eight tasks

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

## Origin and maintenance

**发起/作者单位**：University of Notre Dame.

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：Based primarily on paper author affiliations and the official team description; this is not used to infer legal ownership or a sole initiator. The text has explicitly marked the formal initiating relationship as unverified.

**合作关系**：NSF Center for Computer Assisted Synthesis (C-CAS): the paper explicitly says that task design was discussed with senior doctoral students at the center.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**作者**：Guo, Taicheng；Guo, Kehan；Nan, Bozhao；Liang, Zhenwen；Guo, Zhichun；Chawla, Nitesh V.；Wiest, Olaf；Zhang, Xiangliang

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**维护方**：The official ChemFoundationModels/ChemLLMBench repository; the contacts in the README are Taicheng Guo and Xiangliang Zhang.

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**资助**：U.S. National Science Foundation NSF CHE–2202693, supported through the NSF Center for Computer Assisted Synthesis (C-CAS).

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

## Design goals

**测量能力**：Along the three capabilities of understanding, reasoning, and explanation, it evaluates 8 practical chemistry tasks; it both compares numerical metrics and checks whether the results actually help a chemist.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**针对的不足**：A high score on general language ability, or on a single chemistry task, cannot show whether an LLM can reliably handle molecular representations, reactions, and chemistry instructions; this study does not aim to take the SOTA on any single item.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

## Construction

**材料来源**：Brings together existing resources, including USPTO, ChEBI-20, reaction-yield data, and BBBP/BACE/HIV/Tox21/ClinTox; some files must be downloaded separately from upstream.

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**出题背景**：Olaf Wiest (a professor in the Department of Chemistry at Notre Dame) directed the selection of tasks; there were discussions with senior doctoral students at C-CAS, and chemistry researchers made a qualitative analysis of the answers.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**审核**：Tasks are built from chemistry datasets that are already widely used, and prompts and worked examples are designed for zero-shot and few-shot settings.

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**质控**：Samples drawn from the original test set do not overlap the ICL training candidates; each experiment is repeated 5 times and the mean and variance are reported; chemistry researchers also carry out a qualitative review of practical usefulness.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**去污染边界**：The paper confirms only that the sampled test items do not overlap the ICL training candidates; the original chemistry data are already public, so this cannot be taken as decontamination of LLM pretraining.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

## Data format

**规模与统计口径**：8 task families; Table 1 lists 100 test instances by task. Where one task has more than one dataset or subdirection, those must be understood separately. 8×100 is not to be claimed as the deduplicated total question count.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**任务形式**：名称互译；Molecular property classification；High/low reaction-yield classification；Reaction product prediction；Reagent selection/ranking；逆合成；Text-to-molecule design；Molecular description generation

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**模态**：English natural language；SMILES/SELFIES molecular strings；反应字符串

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**语言**：English prompts and molecular descriptions; SMILES is the primary molecular representation, and SELFIES is also compared.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**难度**：There is no unified difficulty grading; different tasks and prompt settings are evaluated separately, and chemistry ability cannot be judged by the mean accuracy across 8 tasks.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**公开/保留划分**：100 instances are drawn from the original test set for single-item experiments, and the ICL candidates come from the training set; the README publishes the test data and the prompt logs that were used. Some original resources must be downloaded separately.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

## Evaluation

**指标**：Name, yield, and reagent tasks use accuracy. Property classification uses Accuracy and F1. Reaction and retrosynthesis report Top-1 Accuracy and the proportion of illegal SMILES. Molecular design additionally uses BLEU, Exact Match, Levenshtein, fingerprint similarity, FCD, and Validity. Description uses BLEU, ROUGE, and METEOR.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**评分**：Metrics are computed deterministically by the task scripts, and 5 experiments report the mean and the variance; chemists also review the results qualitatively. The yield task is a high/low classification, not a regression of continuous yield by RMSE.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**提示与运行设定**：The official materials provide zero-shot and in-context learning prompts; the update of 2023-12 places the actual prompt logs in each task directory.

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**脚本/运行入口**：The Jupyter notebooks in each task directory of the official repository.

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**可比性**：Different data versions, subsets, prompts, tool permissions, and model snapshots must not be mixed in a direct comparison; scores in historical papers do not represent the current SOTA.

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [3](https://arxiv.org/html/2609.35336v1) (accessed 2026-11-07)

核验说明：2026H2 activity review: in 2026-09, TMCS used the molecular-design and molecular-description tasks of ChemLLMBench in experiments; this is real reuse of the tasks.

**当前版本证据**：Dated data update verifiable in the README: 2023-12, supplying the test data used and the prompt logs; this is not the same as the current latest semantic version.

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**修订历史**：arXiv v1：2023-05-27 23:17:33；v2：2023-09-11 01:37:36；v3：2023-12-28 13:29:36。

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07)

**饱和**：待核实

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：This field has not been verified exactly; that does not mean it is officially Not disclosed.

**争议与局限**：Public upstream data may overlap pretraining. The authors note a gap between text metrics such as BLEU and chemical usefulness, and text similarity cannot replace exactness and validity of the molecule.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**派生/去重**：待核实

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：This field has not been verified exactly; that does not mean it is officially Not disclosed.

## Leaderboard snapshot

**快照日**：2026-11-07

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**官方榜**：https://arxiv.org/pdf/2305.18365#page=20

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**独立评测**：待核实

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：This field has not been verified exactly; that does not mean it is officially Not disclosed.

### 分轨结果（不合并来源/题集/协议）

**Paper v3 / reaction prediction / zero-shot**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | GPT-4 | 0.004 | Top-1 Accuracy (0–1) |

Sources: [https://arxiv.org/pdf/2305.18365](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**Paper v3 / reaction prediction / Scaffold k=20**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | GPT-4 | 0.23 | Top-1 Accuracy (0–1) |
| 2 | Davinci-003 | 0.218 | Top-1 Accuracy (0–1) |
| 3 | GPT-3.5 | 0.184 | Top-1 Accuracy (0–1) |

Sources: [https://arxiv.org/pdf/2305.18365](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**Paper v3 / reaction prediction / Random k=20**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | GPT-4 | 0.012 | Top-1 Accuracy (0–1) |

Sources: [https://arxiv.org/pdf/2305.18365](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**Paper v3 / reaction prediction / a dedicated supervised baseline.**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | Chemformer | 0.938 | Top-1 Accuracy (0–1) |

Sources: [https://arxiv.org/pdf/2305.18365](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); 其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：Historical reaction-prediction results from Table 11 of paper v3 are added, on separate tracks for zero-shot, Scaffold k=20, and Random k=20; this is not the current real-time overall leaderboard. The dedicated Chemformer baseline in the table is on another track and cannot be passed off, together with LLM prompting results, as a unified ability ranking.

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07); [2](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

## Contact

**公开研究邮箱**：tguo2@nd.edu；xzhang33@nd.edu

Sources: [1](https://raw.githubusercontent.com/ChemFoundationModels/ChemLLMBench/main/README.md) (accessed 2026-11-07)

**Issues**：https://github.com/ChemFoundationModels/ChemLLMBench/issues

Sources: [1](https://github.com/ChemFoundationModels/ChemLLMBench) (accessed 2026-11-07)

**公开社区**：待核实

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：This field has not been verified exactly; that does not mean it is officially Not disclosed.

**隐私原则**：Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected.

Sources: [1](urn:benchmark-atlas:constitution:v0.1) (accessed 2026-11-07)

## Original files

**PDF**：https://arxiv.org/pdf/2305.18365

Sources: [1](https://arxiv.org/abs/2305.18365) (accessed 2026-11-07); [2](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

**原件SHA-256**：9623bba95a935d5d3272e26cbadfbcf64348a28aa88ec1cc7f933c69447977f8

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

核验说明：SHA-256 of the original bytes downloaded this time. They were not compressed or modified.

**PDF字节数**：3437726

Sources: [1](https://arxiv.org/pdf/2305.18365) (accessed 2026-11-07)

## Changelog

- date：2026-11-07；change：首批官方材料核验、中文改写、；未核实字段显式标记。
- date：2026-11-07；change：：打开官方文档核验许可、数据形式和评测协议；复核2026H2证据，区分历史结果与实时榜单；同步中文介绍。
- date：2026-11-07；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
