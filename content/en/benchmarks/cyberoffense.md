# CyberOffense

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

Verified to exist; 11-section research snapshot; note: trending: B; unknown fields retained as Unverified

CyberOffense uses two isolated enterprise-network ranges, Nova and Lighthouse, to observe whether an agent can complete authorized objectives in long-horizon, multi-step exploration. It does not rely on self-reported success. It checks whether command output contains a hidden marker corresponding to a private answer key. Each run rebuilds the range and reviews shortcuts. Only the evaluation protocol and the aggregate scores are recorded here. Specific attack steps are not restated. [1](https://www.vals.ai/benchmarks/cyber_offense)

Each run is at most 48 hours, with 500M tokens cumulative, including cache and reasoning. On Nova, the two leading models are each the mean of three runs, and the others are mostly single runs. The 21 objectives and the 31 objectives must be listed separately, and the raw objective counts must not be added into an "overall success rate." In the web report of 2026-10-23, no model completed the final stage of Lighthouse, and completion of the full task remains substantially below the partial-objective scores. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Basic information

- **简称**：CyberOffense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **全称**：CyberOffense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **论文/报告版本**：October 2026 web research report [1](https://www.vals.ai/benchmarks/cyber_offense)

- **主板块**：安全 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **子领域**：Autonomous cybersecurity evaluation；Multi-step cyber-range task [1](https://www.vals.ai/benchmarks/cyber_offense)

- **许可证与限制**：A proprietary evaluation (the Vals catalog marks it Proprietary); this is not equivalent to an open-source software license. [2](https://www.vals.ai/benchmarks/)

- **论文/报告**：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense) 注：The official BibTeX cites this page as a web research report of October 2026; it is not an arXiv paper or a PDF.

- **官方主页**：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **报告标题**：Evaluating frontier AI systems on realistic multi-step cybersecurity tasks [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 基准版本：The listed papers, dataset cards, and READMEs were read; no traceable formal version number was confirmed. A runtime image tag, a web-page update date, and the data version are not treated as the same thing. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 发布日期：The update date on the formal page has been checked; the leaderboard update date or the access date still cannot be treated as the first-release date. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 官方代码：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 数据入口：The formal methods page and its outbound links have been checked; no task-data repository or HF card confirmed by the maintainer has been located, and result tables or upstream data are not treated as the complete question bank. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Origin and maintenance

- **发起方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber_offense)

- **核心作者**：Nikil Ravi；Hung Tran；Langston Nashold；Rayan Krishnan [1](https://www.vals.ai/benchmarks/cyber_offense)

- **维护方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 合作方：The formal materials are not sufficient to confirm an independent research partner; tool providers, model vendors, and upstream repositories are not treated as partner institutions on that basis. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Design goals

- **核心能力**：Long-horizon, multi-step, autonomous completion of authorized cybersecurity objectives in an isolated enterprise-network range. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **相对已有评测的缺口**：Distinct from short standalone CTFs, it evaluates long-term planning, use of evidence, and the ability to chain steps across a complete organizational network. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Construction

- **题目来源**：Two simulated enterprise-network ranges, Nova and Lighthouse. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **审核流程**：The publisher says that each run is reviewed and that shortcuts are checked; the private answer key is not available for the model to read. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **质量控制**：A fresh range on every run; the hidden flag is obtained only by actually reaching the goal, and the recorded output is checked rather than the model's own report. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **防污染/运行完整性**：Each run resets a new range, with a hidden marker and a private answer key; the publisher reviews every run and states that no shortcut or reading of the answer key was found. This is a measure of run integrity, and it cannot prove that model pretraining is completely free of contamination. [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：The formal methods page can confirm the organization that releases and maintains it, but no byline or methods detail sufficient to confirm author names or question-writer qualifications was found. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Data format

- **规模**：2 ranges: Nova with 21 targets, Lighthouse with 31 targets; the current report covers 7 models. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **题型**：Autonomous multi-step interaction with the range; only the evaluation protocol is discussed, and this page does not provide operational attack guidance. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **模态**：文本指令；终端输出；Isolated network environment [1](https://www.vals.ai/benchmarks/cyber_offense)

- **难度与任务跨度**：Nova, a multi-domain enterprise network; Lighthouse, long-horizon tasks across two enterprise networks. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **公开与隐藏划分**：The scoring answer key is private; release of the range and the license for the full question set are Unverified. [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 语言覆盖：The formal methods page is written in English, but it does not fully disclose the language coverage of the task instructions and of the program and game content, so the full set of languages cannot be determined from the report language alone. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Evaluation

- **指标**：The share of objectives completed on each range; overall, the shares for the two ranges have equal weight. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **评分规则**：Scoring searches the command output for a hidden marker of the private answer key, and does not adopt the claim of success made by the model. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **提示与运行配置**：A Pi agent, an isolated Kali environment, connected only to the model provider and the authorized range; a cap of 48 hours per run, with scores counted within 500M cumulative tokens, including cached input and reasoning. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **可比性限制**：The two leading models on Nova are each the mean of 3 runs, and the rest are mostly single runs; the numbers of completed targets on the two ranges are not added directly as an overall score. [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Current status

- **核验日期**：2026-11-07 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **现行版本与采用证据**：version：待核实；heat_confidence：B；evidence_2026_h2：url：https://www.vals.ai/benchmarks/cyber_offense；date：2026-10-23；note：The update date written on the Vals official site; adopted mainly by a single organization. [1](https://www.vals.ai/benchmarks/cyber_offense) 注：B: current evaluation or vendor adoption mainly by a single institution; broad industry adoption cannot be claimed.

- **饱和度判断**：The deepest stage of both ranges is still difficult: no model completed the final objective on Lighthouse; in the whole Nova experiment, only one run entered the final stage. A completion rate on partial objectives cannot be read as a success rate on the complete task. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **已知问题与证据边界**：Evaluated only in a simulated authorized environment; the degree of transfer to a real network cannot be proved directly by the range score. [1](https://www.vals.ai/benchmarks/cyber_offense)

- **关联与衍生关系**：Pi is an execution agent framework, not the question-bank code of CyberOffense itself; Nova and Lighthouse are two range components under the same benchmark, and they are not counted as two further benchmarks. [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 更新与修订：What can currently be verified is an update to the web methods page or leaderboard table; a version history for a standalone paper has not been located, and the web-page update time is not misrepresented as an arXiv revision. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **官方榜/正式委托榜**：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| Official-site table row order, not overall leaderboard rank | GPT-6 Sol Daybreak | Nova：15.7/21 (mean of 3 runs; 12–19)；Lighthouse：27/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| Official-site table row order, not overall leaderboard rank | DeepSeek V4.1 Flash 1017 | Nova：16.3/21 (mean of 3 runs; 15–18)；Lighthouse：21/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| Official-site table row order, not overall leaderboard rank | Kimi K3.1 Pro | Nova：13/21；Lighthouse：20/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| Official-site table row order, not overall leaderboard rank | Meta Wonder | Nova：7/21；Lighthouse：28/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| Official-site table row order, not overall leaderboard rank | Grok 4.7 | Nova：12/21；Lighthouse：16/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| Official-site table row order, not overall leaderboard rank | Kimi K3 | Nova：9/21；Lighthouse：10/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| Official-site table row order, not overall leaderboard rank | GLM 5.3 Flash | Nova：5/21；Lighthouse：5/31 | Objective completion count (two ranges listed separately)；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：Only results under the listed sources and protocols are retained; the update time written on the leaderboard is 2026-10-23. The access date is not the evaluation run date. [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Contact

- **官方社交**：https://x.com/ValsAI [1](https://www.vals.ai/benchmarks/cyber_offense) 注：A public link in the footer of the official site; X accounts are neither read nor operated.

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 公开问题追踪：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 隐私政策：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Original files

- **其他正式文档**：type：Official introduction/protocol；url：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **中的论文副本**：待核实 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 原始PDF：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber_offense)
- SHA-256：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber_offense)
- PDF字节数：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber_offense)
- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://www.vals.ai/benchmarks/cyber_offense)

## Changelog

- date：2026-11-07；timezone：；change：首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://www.vals.ai/benchmarks/cyber_offense)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
