# DeepSWE

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

 unknown information retained as Unverified.

DeepSWE covers 91 open-source repositories and five code languages with 113 original long-horizon engineering tasks. The tasks are not extracted from pull requests that have already been merged. The authors separately wrote the behavioral requirements, an executable verifier, and a reference implementation for review, and they used a shallow clone to block taking the answer directly from git history. Compared with short-horizon patch questions, it emphasizes exploring the codebase, implementing changes across files, and preserving existing function. [1](https://deepswe.datacurve.ai/) [2](https://arxiv.org/abs/2607.07946) [3](https://deepswe.datacurve.ai/blog/deepswe) [4](https://epoch.ai/benchmarks/deepswe/review)

The official blog was published on 2026-05-26, and the first arXiv version is dated 2026-07-08. The current leaderboard and repository use v1.1. The authors' low disagreement rate from the LLM audit is not human certification. Epoch independently reviewed v1.1, found false negatives on at least 23/113 questions, and judged it Flawed. Scores near the current 74% must be read together with the scoring defects, model effort, and the interval across repeated runs, and they cannot serve as a high-precision ranking of models. [1](https://deepswe.datacurve.ai/) [2](https://arxiv.org/abs/2607.07946) [3](https://deepswe.datacurve.ai/blog/deepswe) [4](https://epoch.ai/benchmarks/deepswe/review)

## Basic information

- **简称**：DeepSWE [1](https://deepswe.datacurve.ai/)

- **全称**：DeepSWE [1](https://deepswe.datacurve.ai/)

- **基准版本**：v1.1 [1](https://deepswe.datacurve.ai/)

- **论文/报告版本**：arXiv:2607.07946v1（2026-07-08） [2](https://arxiv.org/abs/2607.07946)

- **发布日期**：2026-05-26 (official release blog); first arXiv version 2026-07-08 [3](https://deepswe.datacurve.ai/blog/deepswe)

- **主板块**：代码 [1](https://deepswe.datacurve.ai/) 注：Filed under one main section. That filing does not limit coverage of other disciplines.

- **子领域**：Long-horizon software engineering；Code agent；行为验证 [2](https://arxiv.org/abs/2607.07946)

- **许可证与限制**：The official benchmark repository is Apache-2.0; each of the 91 upstream repositories under evaluation retains its own license. [5](https://github.com/datacurve-ai/deep-swe/blob/main/LICENSE)

- **论文/报告**：https://arxiv.org/abs/2607.07946 [2](https://arxiv.org/abs/2607.07946)

- **官方代码**：https://github.com/datacurve-ai/deep-swe [6](https://github.com/datacurve-ai/deep-swe)

- **数据入口**：https://huggingface.co/datasets/datacurve/deep-swe [7](https://huggingface.co/datasets/datacurve/deep-swe)

- **官方主页**：https://deepswe.datacurve.ai/ [1](https://deepswe.datacurve.ai/)

- **报告标题**：DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks [2](https://arxiv.org/abs/2607.07946)

## Origin and maintenance

- **发起方**：Datacurve [4](https://epoch.ai/benchmarks/deepswe/review)

- **核心作者**：Wenqi Huang；Charley Lee；Leonard Tng；Serena Ge [2](https://arxiv.org/abs/2607.07946)

- **维护方**：Datacurve [4](https://epoch.ai/benchmarks/deepswe/review)

**仍待核实**（不推断为未公开）：

- 合作方：The formal materials are not sufficient to confirm an independent research partner; tool providers, model vendors, and upstream repositories are not treated as partner institutions on that basis. [1](https://deepswe.datacurve.ai/)
- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://deepswe.datacurve.ai/)

## Design goals

- **核心能力**：The ability to complete original, long-horizon, real software-engineering tasks. [1](https://deepswe.datacurve.ai/)

- **相对已有评测的缺口**：Avoid adapting existing submissions or PRs, broaden the diversity of repositories and languages, and distinguish code agents that are nearing saturation. [1](https://deepswe.datacurve.ai/)

## Construction

- **题目来源**：113 original tasks, drawn from 91 repositories that are active, have at least 500 GitHub stars, and use a permissive open-source license; some questions are inspired by an unresolved issue, but the reference implementation does not copy an existing PR or commit. [2](https://arxiv.org/abs/2607.07946) [3](https://deepswe.datacurve.ai/blog/deepswe)

- **出题与审核人员**：Software engineers construct, item by item, the task, the container, the tests, and the reference implementation, and they review one another's work; the organization named on the paper is Datacurve. [2](https://arxiv.org/abs/2607.07946)

- **审核流程**：Checking assisted by an LLM runs in parallel with independent human review; the review covers correspondence between the prompt and the verifier, acceptable alternative implementations, whether the requirement is real, and cleanliness of the environment; trial runs of several agents help check whether a pass or a failure is reasonable. [2](https://arxiv.org/abs/2607.07946)

- **质量控制**：Each verifier is run 3 times when it is built, to filter out flaky tests; each scoring run adds a subset of the original repository’s tests and new regression checks; reference patches are used only for review and do not take part in run scoring. [2](https://arxiv.org/abs/2607.07946)

- **防污染/运行完整性**：The original implementation is not contributed back as upstream PRs or commits, and the container contains only a shallow clone of the base commit. This was a contamination-prevention design at the time of the first measurement. After the questions, tests, and trajectories are made public, future models may still ingest these materials, so a permanent claim of no contamination cannot be made. [2](https://arxiv.org/abs/2607.07946)

## Data format

- **规模**：113 tasks and 91 repositories; TypeScript 35, Go 34, Python 34, JavaScript 5, Rust 5. [3](https://deepswe.datacurve.ai/blog/deepswe)

- **题型**：Cross-file implementation of engineering features, fixes, and long-term maintenance of code. [1](https://deepswe.datacurve.ai/)

- **模态**：代码；文本；测试环境 [1](https://deepswe.datacurve.ai/)

- **语言覆盖**：TypeScript；Go；Python；JavaScript；Rust [2](https://arxiv.org/abs/2607.07946) 注：Here this is the code language; the natural-language prompt examples are in English, and multilingual coverage is not claimed.

- **难度与任务跨度**：Long-horizon refers to the scale of a task's reference implementation, its span across files, and the exploration required, rather than measured human labor time; short repairs and localization tasks account for an insufficient share. [2](https://arxiv.org/abs/2607.07946)

- **公开与隐藏划分**：The 113 questions and the verifier are public through the official repository. On each run, tests/ and solution/ are hidden from the agent. In v1.1, scoring is applied after the agent's submitted patch is applied in an independent clean container, so that the agent cannot intervene directly in the scoring environment. [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md) [7](https://huggingface.co/datasets/datacurve/deep-swe)

## Evaluation

- **指标**：Pass@1; with cost, output tokens, and Agent steps. [1](https://deepswe.datacurve.ai/)

- **评分规则**：Hand-written functional tests and regression tests are scored as pass or fail. pass@1 is the macro-average of the proportion passed on each question. pass@4 is the proportion of questions that pass at least once in at most four attempts. A timeout or exhaustion of context counts as a failure. Errors of the provider, the verifier, or the network are excluded from the denominator and are not collected again. [2](https://arxiv.org/abs/2607.07946)

- **提示与运行配置**：mini-swe-agent shares a single bash tool and a system prompt; the paper pins commit adfe2023, a single rollout is limited to 9000 seconds, and there is no step cap and no cost cap; there are about 4 rollouts per question per configuration. A v1.1 run needs a separate verifier environment with Pier>0.3.0. [2](https://arxiv.org/abs/2607.07946) [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

- **评分/运行脚本**：https://github.com/datacurve-ai/deep-swe [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

- **可比性限制**：A unified harness is not the same as each vendor's production product experience. Reasoning effort differs from vendor to vendor. The 95% error bars mainly reflect fluctuation across repeated runs, and they do not include all of the uncertainty from sampling tasks. The rate at which LLM audits disagree is not the verifier's true error rate. [2](https://arxiv.org/abs/2607.07946)

## Current status

- **核验日期**：2026-11-07 [1](https://deepswe.datacurve.ai/)

- **现行版本与采用证据**：version：v1.1；evidence_2026_h2：url：https://epoch.ai/benchmarks/deepswe/review；date：2026-09-07；note：An independent Epoch review rates it Flawed.；url：https://openai.com/index/gpt-6-astra/；date：2026-11-07；date_type：observed_on；note：Adopted in the GPT-6 Astra release table. [4](https://epoch.ai/benchmarks/deepswe/review) [9](https://openai.com/index/gpt-6-astra/)

- **更新与修订**：The PDF is arXiv v1; the current repository at v1.1 adds a separate verifier container, which must be distinguished from the experiments in the first version of the paper. [2](https://arxiv.org/abs/2607.07946) [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

- **饱和度判断**：Editorial judgment: the readable leader of official v1.1 shows 74%±3%, and the other two configurations also round to 74%; overlapping intervals do not support treating the small differences among the three as a significant lead. [1](https://deepswe.datacurve.ai/)

- **已知问题与证据边界**：On 2026-09-07, Epoch gave v1.1 a Flawed rating: human review confirmed false negatives on at least 23/113 questions (>20.3%). 18 cases are related to conflicts in which, after the agent changed the tests, the verifier restored tests or added tests. The review stopped once the threshold was reached. It did not estimate the overall error rate, and it did not prove that the remaining 90 questions are free of error. This and the authors' LLM-audit conclusion of a 1.4% disagreement come from different methods and cannot substitute for each other. [4](https://epoch.ai/benchmarks/deepswe/review) [2](https://arxiv.org/abs/2607.07946)

- **关联与衍生关系**：Pier is a runtime framework, and Harbor is a task and trajectory format; neither is a new version of the DeepSWE question bank. [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://deepswe.datacurve.ai/)

- **官方榜/正式委托榜**：https://deepswe.datacurve.ai/ [1](https://deepswe.datacurve.ai/)

- **独立第三方入口**：https://epoch.ai/benchmarks/deepswe/review [4](https://epoch.ai/benchmarks/deepswe/review)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | gpt-6-astra [xhigh] | 74% ±3% | v1.1 pass@1; rounded on the webpage；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 2 | gemini-3.8-flash [high] | 74% ±1% | v1.1 pass@1; rounded on the webpage；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 3 | claude-opus-5 [max] | 74% ±4% | v1.1 pass@1; rounded on the webpage；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 4 | gpt-5.6-sol [max] | 73% ±3% | v1.1 pass@1; rounded on the webpage；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 5 | claude-fable-5 [xhigh] | 70% ±3% | v1.1 pass@1; rounded on the webpage；2026-09-22；[1](https://deepswe.datacurve.ai/) |

> gpt-6-astra [xhigh]：rank_type：Row order shown on the official site, not significance order [1](https://deepswe.datacurve.ai/)

> gemini-3.8-flash [high]：rank_type：Row order shown on the official site, not significance order [1](https://deepswe.datacurve.ai/)

> claude-opus-5 [max]：rank_type：Row order shown on the official site, not significance order [1](https://deepswe.datacurve.ai/)

> gpt-5.6-sol [max]：rank_type：Row order shown on the official site, not significance order [1](https://deepswe.datacurve.ai/)

> claude-fable-5 [xhigh]：rank_type：Row order shown on the official site, not significance order [1](https://deepswe.datacurve.ai/)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：Display order on the official website; the three displayed values are the same, the error intervals overlap, and significant superiority or inferiority is not claimed on this basis. [1](https://deepswe.datacurve.ai/)

## Contact

- **公开问题追踪**：https://github.com/datacurve-ai/deep-swe/issues [6](https://github.com/datacurve-ai/deep-swe)

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://deepswe.datacurve.ai/)
- 官方社交：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://deepswe.datacurve.ai/)
- 隐私政策：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://deepswe.datacurve.ai/)

## Original files

- **原始PDF**：https://arxiv.org/pdf/2607.07946 [10](https://arxiv.org/pdf/2607.07946)

- **SHA-256**：1d988c90737299c6d844694ba967ff63f4e2aa13c66be20b97b8fa4bd89754ce [10](https://arxiv.org/pdf/2607.07946) 注：Byte count of the PDF actually downloaded. It is not copied from an external web page.

- **PDF字节数**：713926 [10](https://arxiv.org/pdf/2607.07946) 注：Downloaded byte count; not uploaded.

- **其他正式文档**：type：Repository README (v1.1 scoring kept separate)；url：https://github.com/datacurve-ai/deep-swe/blob/main/README.md；type：Task and dataset card；url：https://huggingface.co/datasets/datacurve/deep-swe [6](https://github.com/datacurve-ai/deep-swe) [7](https://huggingface.co/datasets/datacurve/deep-swe)

- **中的论文副本**：待核实 [1](https://deepswe.datacurve.ai/)

**仍待核实**（不推断为未公开）：

- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://deepswe.datacurve.ai/)

## Changelog

- date：2026-11-07；；change：按官方材料新建中文条目；区分热度、质量和不同版本评分。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://deepswe.datacurve.ai/)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
