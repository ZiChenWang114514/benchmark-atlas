# EnterpriseOps-Gym

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

Verified to exist; a recently popular newly created entry, with Unverified fields retaining their marks; trending: A

EnterpriseOps-Gym builds an enterprise-workflow sandbox from a resettable database and MCP tools, and it evaluates stateful long-horizon planning, policy following, and control of side effects. The original paper has 1150 expert tasks covering eight domains, 164 tables, and 512 tools. Each question is verified by the final database state, rather than by requiring a copy of one particular operation trajectory. 30 tasks are intentionally infeasible and should be refused rather than completed by exceeding authority. [1](https://enterpriseops-gym.github.io/) [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

The genuine official project page was located. It explicitly assigns maintenance of the latest leaderboard to Artificial Analysis. AA uses Stirrup, oracle tools, and three repetitions. The full Oracle leaderboard in the README, the original paper, and AA are not the same protocol. The highs of 45.9%, 37.4%, and 51.1% should not be strung into a single curve of progress. The HF card's counts also differ from the paper in how the data are packaged, and the number of rows across public configurations cannot be taken as the total number of independent tasks. [1](https://enterpriseops-gym.github.io/) [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

## Basic information

- **简称**：EnterpriseOps-Gym [2](https://arxiv.org/abs/2603.13594)

- **全称**：EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings [2](https://arxiv.org/abs/2603.13594)

- **论文/报告版本**：arXiv v1（2026-03-13） [2](https://arxiv.org/abs/2603.13594)

- **发布日期**：2026-03-13 (arXiv submission) [2](https://arxiv.org/abs/2603.13594)

- **主板块**：Agent [2](https://arxiv.org/abs/2603.13594) 注：Benchmark Constitution editorial filing.

- **子领域**：企业工作流；工具调用；有状态规划 [2](https://arxiv.org/abs/2603.13594)

- **许可证与限制**：Apache-2.0 (official repository LICENSE; it is not assumed that all accompanying third-party data share the same license) [5](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/LICENSE)

- **论文/报告**：https://arxiv.org/abs/2603.13594 [2](https://arxiv.org/abs/2603.13594)

- **官方代码**：https://github.com/ServiceNow/EnterpriseOps-Gym [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **数据入口**：https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

- **官方主页**：https://enterpriseops-gym.github.io/ [1](https://enterpriseops-gym.github.io/)

- **报告标题**：EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings [2](https://arxiv.org/abs/2603.13594)

**仍待核实**（不推断为未公开）：

- 基准版本：The listed papers, dataset cards, and READMEs were read; no traceable formal version number was confirmed. A runtime image tag, a web-page update date, and the data version are not treated as the same thing. [2](https://arxiv.org/abs/2603.13594)

## Origin and maintenance

- **发起方**：ServiceNow [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **合作方**：Mila – Quebec AI Institute；Université de Montréal；Turing (data-construction partner) [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

- **核心作者**：Shiva Krishna Reddy Malay、Shravan Nayak、Jishnu Sethumadhavan Nair、Sagar Davasam、Aman Tiwari、Sathwik Tejaswi Madhusudhan、Sridhar Krishna Nemala、Srinivas Sunkara、Sai Rajeswar [2](https://arxiv.org/abs/2603.13594)

- **维护方**：ServiceNow（ServiceNow-AI） [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

**仍待核实**（不推断为未公开）：

- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [2](https://arxiv.org/abs/2603.13594)

## Design goals

- **核心能力**：Long-horizon planning and tool calls in an enterprise environment that has persistent state changes and strict access rules, including the ability to refuse a task that is not feasible. [2](https://arxiv.org/abs/2603.13594)

- **相对已有评测的缺口**：Existing benchmarks do not reflect the complexity of long-horizon planning, persistent state, and access protocols in professional settings. [2](https://arxiv.org/abs/2603.13594)

## Construction

- **题目来源**：Synthetic databases and tasks are designed from public enterprise API documentation and from domain SMEs, and private enterprise data are not used; eight domains: Calendar, CSM, , Email, HR, ITSM, Teams, and Hybrid. [2](https://arxiv.org/abs/2603.13594)

- **出题与审核人员**：Turing organized more than 160 engineers, domain SMEs, and annotators; their backgrounds are bachelor's degrees in engineering, computer science, and related fields, with an average of 20 annotators and 6 reviewers per domain, over about 4 months including a 1-month pilot. [2](https://arxiv.org/abs/2603.13594)

- **审核流程**：Scenario design → a human executes the gold trajectory and writes a plan constrained by policy → the SQL verifier of the final state is written → several rounds of checks on feasibility, clarity, foreign keys, and permission constraints; the final state is unique, but more than one legal path of execution is allowed. [2](https://arxiv.org/abs/2603.13594)

- **质量控制**：GPT-5, Gemini, and Claude are first used in trial runs to look for missing tools, invalid data, unintended shortcuts, and tasks that are too simple. Prompts, trajectories, and verifier coverage are then checked by hand. The database is reset on every task to avoid state leakage across runs. [2](https://arxiv.org/abs/2603.13594)

- **防污染/运行完整性**：The environment is synthesized independently from public documents and SMEs, and private enterprise data does not enter it; the official README releases only about 60% of the samples. The paper does not give a quantifiable result for corpus-deduplication retrieval, so a complete absence of contamination cannot be claimed. [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

## Data format

- **规模**：1,150 tasks and 8 vertical domains; the sandbox contains 164 database tables and 512 tools [2](https://arxiv.org/abs/2603.13594)

- **题型**：Stateful multi-step tool-calling tasks [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **模态**：文本；Tool calls/database state [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **语言覆盖**：Natural-language instructions and policies are in English, with structured tool calls and an SQL verifier; the public HF examples are in English, and cross-language coverage is not claimed. [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) [2](https://arxiv.org/abs/2603.13594)

- **难度与任务跨度**：Expert reference trajectories average 9.15 steps and at most 34 steps, with 5.3 verification conditions on average and at most 44; 30 questions are intentionally infeasible and must be refused without side effects. [2](https://arxiv.org/abs/2603.13594)

- **公开与隐藏划分**：The README says about 60% is public. The paper's total size is 1150. Domain counts on the HF card sum to 1115, and the viewer oracle has 649 rows. The packaged size differs from the paper. The HF multi-configuration total of 2560 rows cannot be treated as the number of independent tasks. [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) [2](https://arxiv.org/abs/2603.13594)

## Evaluation

- **指标**：Strict task success rate (no partial credit) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **评分规则**：Judged by verifiers of the final state of the underlying database (for example, expected values of SQL queries); success requires every verifier to pass [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

- **提示与运行配置**：AA: Stirrup harness, oracle tool mode, 3 repetitions per task [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **评分/运行脚本**：runner：https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/evaluate.py；scoring：https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/compute_score.py [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

- **可比性限制**：The official project page now points the latest leaderboard to AA, but AA explicitly states an independent Stirrup implementation, oracle tools, and 3 runs per question; the ReAct scores in the original paper and the README scores are each kept, and rankings cannot be merged across harnesses. The README excludes error files, and reproduction should check the denominator. [1](https://enterpriseops-gym.github.io/) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

## Current status

- **核验日期**：2026-11-07 [2](https://arxiv.org/abs/2603.13594)

- **现行版本与采用证据**：version：待核实；evidence_2026_h2：url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；organization：Artificial Analysis；note：The current methods page lists EnterpriseOps-Gym as an evaluation under way and discloses the tasks or the scoring protocol.；url：https://artificialanalysis.ai/evaluations；date：2026-11-07；organization：Artificial Analysis；note：The current public evaluation catalog lists EnterpriseOps-Gym on its own; this is not a news mention.；url：https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym；date：2026-11-07；organization：ServiceNow；note：The current implementation of AA is explicitly based on public ServiceNow data and is verified by final-state SQL.；trending：heat_confidence：A；summary：The ServiceNow enterprise-workflow benchmark already has an independent AA evaluation, verified by final state. [7](https://artificialanalysis.ai/methodology/intelligence-benchmarking) [8](https://artificialanalysis.ai/evaluations) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) 注：Recent popularity evidence is taken from candidate studies and reopened pages; grade A: adopted independently by multiple frontier laboratories or evaluation organizations.

- **更新与修订**：The first version of the paper is arXiv:2603.13594v1 (2026-03-13). The current README adds Opus4.6 at 45.9% and Sonnet4.6 at 42.2%, while the homepage still writes the older 34.1%; the older paper abstract on the project page is still 37.4%, and maintenance of the latest results has been entrusted to AA. [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [1](https://enterpriseops-gym.github.io/)

- **饱和度判断**：The current AA leader is a strict task success rate of 51.1%; the high in the official README snapshot is 45.9%, and the first version of the original paper is 37.4%; the protocols differ, and none is close to a perfect score, so the difference between versions cannot be treated as progress of the model alone. [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [2](https://arxiv.org/abs/2603.13594)

- **已知问题与证据边界**：The public and private scales, the README, and the scores in the paper differ across versions; an oracle tool supplies the correct tool in advance and cannot prove that autonomous retrieval would succeed in the same way inside a real enterprise. Performance in a fully synthetic sandbox does not mean that the system can be deployed directly and safely. [2](https://arxiv.org/abs/2603.13594) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

- **关联与衍生关系**：EnterpriseOps-Gym-AA is an independent implementation by Artificial Analysis that uses Stirrup; the project page points the latest leaderboard to it, but the dataset and the original paper must still have their protocols marked separately. [1](https://enterpriseops-gym.github.io/) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [2](https://arxiv.org/abs/2603.13594)

- **官方榜/正式委托榜**：https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa [1](https://enterpriseops-gym.github.io/) 注：The official project page explicitly states that the latest model results are maintained by AA; AA also states an independent implementation.

- **独立第三方入口**：https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | Claude Fable 5 (Max, Opus 4.8 Fallback) | 51.1% | EnterpriseOps-Gym-AA Task success rate；Unverified (collection date 2026-11-07)；[4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |
| 2 | Gemini 3.7 Flash (Medium) | 50.4% | EnterpriseOps-Gym-AA Task success rate；Unverified (collection date 2026-11-07)；[4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |
| 3 | Gemini 3.5 Flash (High) | 50.1% | EnterpriseOps-Gym-AA Task success rate；Unverified (collection date 2026-11-07)；[4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |

> Claude Fable 5 (Max, Opus 4.8 Fallback)：result_type：AA independent-implementation leaderboard snapshot；protocol：Stirrup; oracle tools; 3 times per task; strict requirement that every verifier passes [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

> Gemini 3.7 Flash (Medium)：result_type：AA independent-implementation leaderboard snapshot；protocol：Stirrup; oracle tools; 3 times per task; strict requirement that every verifier passes [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

> Gemini 3.5 Flash (High)：result_type：AA independent-implementation leaderboard snapshot；protocol：Stirrup; oracle tools; 3 times per task; strict requirement that every verifier passes [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：The AA top three were reread as 51.1/50.4/50.1. The top three of the full Oracle snapshot in the official README were also read: Opus4.6 45.9, Sonnet4.6 42.2, and Opus4.5 39.4; they are not ranked together with the AA leaderboard. Opus4.5 at 37.4 in the original paper also differs from 39.4 in the README, and each source is marked as it stands. [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [2](https://arxiv.org/abs/2603.13594)

## Contact

- **公开联系邮箱**：shivakrishnareddy.ma@servicenow.com [2](https://arxiv.org/abs/2603.13594)

- **公开问题追踪**：https://github.com/ServiceNow/EnterpriseOps-Gym/issues [9](https://github.com/ServiceNow/EnterpriseOps-Gym)

**仍待核实**（不推断为未公开）：

- 官方社交：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [2](https://arxiv.org/abs/2603.13594)
- 隐私政策：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [2](https://arxiv.org/abs/2603.13594)

## Original files

- **原始PDF**：https://arxiv.org/pdf/2603.13594 [10](https://arxiv.org/pdf/2603.13594)

- **SHA-256**：8a7639982494f4802148fa4bdb6de40040f9d2e01c061db57f4e2e5d0d66d751 [10](https://arxiv.org/pdf/2603.13594) 注：Byte count of the PDF actually downloaded. It is not copied from an external web page.

- **PDF字节数**：5330988 [10](https://arxiv.org/pdf/2603.13594) 注：Downloaded byte count; not uploaded.

- **其他正式文档**：type：The official README and a snapshot of the Oracle leaderboard；url：https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md；type：Official project page；url：https://enterpriseops-gym.github.io/；type：Official HF dataset card；url：https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym [1](https://enterpriseops-gym.github.io/) [9](https://github.com/ServiceNow/EnterpriseOps-Gym) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

- **中的论文副本**：待核实 [2](https://arxiv.org/abs/2603.13594)

**仍待核实**（不推断为未公开）：

- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [2](https://arxiv.org/abs/2603.13594)

## Changelog

- date：2026-11-07；timezone：；change：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://enterpriseops-gym.github.io/)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
