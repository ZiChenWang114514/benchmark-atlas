# CyberBench

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

 unknown information retained as Unverified.

CyberBench v1.1 measures two complementary abilities: constructing an input that distinguishes a vulnerable version from a fixed version, and patching a program while preserving normal function. The tasks come from ARVO's native OSS-Fuzz regression images of software vulnerabilities and use mini-swe-agent. The 60 PoC questions and the 56 Patch questions should not be conflated with a full intrusion of an enterprise network. [1](https://www.vals.ai/benchmarks/cyber)

v1.1 changes the offline sandbox and the clean-room scorer. It replaces the v1 scores rather than continuing them directly. On the official 48-model table of 2026-11-05, the leader of the Overall board is Wonder at 80.36%. Refusal and fallback strategies can affect the score. ARVO, CyberGym, and mini-swe-agent are upstream resources. Their public licenses do not automatically become the license of the CyberBench tasks. [1](https://www.vals.ai/benchmarks/cyber)

## Basic information

- **简称**：CyberBench [1](https://www.vals.ai/benchmarks/cyber)

- **全称**：CyberBench [1](https://www.vals.ai/benchmarks/cyber)

- **基准版本**：v1.1 [1](https://www.vals.ai/benchmarks/cyber)

- **主板块**：安全 [1](https://www.vals.ai/benchmarks/cyber) 注：Filed under one main section. That filing does not limit coverage of other disciplines.

- **子领域**：漏洞复现；Security patch generation；Native software memory safety [1](https://www.vals.ai/benchmarks/cyber)

- **许可证与限制**：A proprietary evaluation (the Vals catalog marks it Proprietary); this is not equivalent to an open-source software license. [2](https://www.vals.ai/benchmarks/)

- **官方主页**：https://www.vals.ai/benchmarks/cyber [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 论文/报告版本：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber)
- 发布日期：The update date on the formal page has been checked; the leaderboard update date or the access date still cannot be treated as the first-release date. [1](https://www.vals.ai/benchmarks/cyber)
- 论文/报告：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber)
- 官方代码：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cyber)
- 数据入口：The formal methods page and its outbound links have been checked; no task-data repository or HF card confirmed by the maintainer has been located, and result tables or upstream data are not treated as the complete question bank. [1](https://www.vals.ai/benchmarks/cyber)
- 报告标题：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber)

## Origin and maintenance

- **发起方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber)

- **维护方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 合作方：The formal materials are not sufficient to confirm an independent research partner; tool providers, model vendors, and upstream repositories are not treated as partner institutions on that basis. [1](https://www.vals.ai/benchmarks/cyber)
- 核心作者：The formal methods page can confirm the organization that releases and maintains it, but no byline or methods detail sufficient to confirm author names or question-writer qualifications was found. [1](https://www.vals.ai/benchmarks/cyber)
- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://www.vals.ai/benchmarks/cyber)

## Design goals

- **核心能力**：Reproduces and repairs real vulnerabilities end to end, while preserving normal program behavior. [1](https://www.vals.ai/benchmarks/cyber)

- **相对已有评测的缺口**：Focuses on OSS-Fuzz-style crashes in native code, rather than treating CTF scores as general security ability. [1](https://www.vals.ai/benchmarks/cyber)

## Construction

- **题目来源**：An OSS-Fuzz regression image based on ARVO; the tasks come from after CyberGym's original collection window. [1](https://www.vals.ai/benchmarks/cyber)

- **审核流程**：A differential oracle and a hidden holdout are compared with the repaired version of the maintainer. [1](https://www.vals.ai/benchmarks/cyber)

- **质量控制**：v1.1 reruns the offline sandbox, with a hardened clean-room grader. [1](https://www.vals.ai/benchmarks/cyber)

- **防污染/运行完整性**：A new time window and an offline sandbox reduce the effect of leakage and of external queries; this is not equivalent to proof of a complete absence of contamination. [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：The formal methods page can confirm the organization that releases and maintains it, but no byline or methods detail sufficient to confirm author names or question-writer qualifications was found. [1](https://www.vals.ai/benchmarks/cyber)

## Data format

- **规模**：PoC: 60 tasks; Patch: 56 tasks that can be scored reliably. [1](https://www.vals.ai/benchmarks/cyber)

- **题型**：The PoC track generates a triggering input; the Patch track edits the source to repair the vulnerability. [1](https://www.vals.ai/benchmarks/cyber)

- **模态**：文本；源码；二进制目标；容器 [1](https://www.vals.ai/benchmarks/cyber)

- **难度与任务跨度**：Memory-safety crashes, sanitizer crashes, and undefined-behavior crashes in real native open-source software; not an evaluation of general network intrusion or of vulnerabilities on the web. [1](https://www.vals.ai/benchmarks/cyber)

- **公开与隐藏划分**：Patch has hidden holdout inputs; the full task and the scope of the data license are Unverified. [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 语言覆盖：The formal methods page is written in English, but it does not fully disclose the language coverage of the task instructions and of the program and game content, so the full set of languages cannot be determined from the report language alone. [1](https://www.vals.ai/benchmarks/cyber)

## Evaluation

- **指标**：Overall, PoC, and Patch accuracy; the table at the head of the leaderboard is Overall. [1](https://www.vals.ai/benchmarks/cyber)

- **评分规则**：A PoC must crash the vulnerable version and must not crash the fixed version; a Patch must compile successfully, the original PoC must no longer trigger, and the hidden behavior must match the reference. [1](https://www.vals.ai/benchmarks/cyber)

- **提示与运行配置**：A unified mini-swe-agent; an offline task sandbox. [1](https://www.vals.ai/benchmarks/cyber)

- **可比性限制**：v1.1 replaces v1, and the results are not directly comparable; a refusal counts as a failure, fallback affects the result, and its marker must be kept. [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cyber)

## Current status

- **核验日期**：2026-11-07 [1](https://www.vals.ai/benchmarks/cyber)

- **现行版本与采用证据**：version：v1.1；heat_confidence：B；evidence_2026_h2：url：https://www.vals.ai/benchmarks/cyber；date：2026-11-05；note：The current Vals leaderboard of 48 models; attention comes mainly from a single evaluation organization, and it cannot be called broad adoption by the industry. [1](https://www.vals.ai/benchmarks/cyber)

- **更新与修订**：v1.1 retains 60 PoC questions and 56 Patch questions and replaces the offline sandbox and the hardened grader; v1 is not directly comparable. [1](https://www.vals.ai/benchmarks/cyber)

- **饱和度判断**：Editorial judgment: the current Overall leader is at 80.36% and still has headroom. The 60 PoC questions and the 56 Patch questions need to be checked separately, and they are not compared directly with v1. [1](https://www.vals.ai/benchmarks/cyber)

- **已知问题与证据边界**：The tasks are taken from after the original window of CyberGym; the offline sandbox and the clean-room grader of v1.1 reduce external access and leakage into scoring. A refusal by the vendor counts as a failure. Fallback is marked separately, and a counterfactual score that counts fallback tasks as failures can be viewed. Passing a local patch does not guarantee equivalence to a complete fix by the maintainer. [1](https://www.vals.ai/benchmarks/cyber)

- **关联与衍生关系**：Based on the CyberGym evaluation method, on ARVO OSS-Fuzz images, and on mini-swe-agent; these are upstream methods and infrastructure, and they cannot be treated as open-source tasks of CyberBench itself or as its license. [1](https://www.vals.ai/benchmarks/cyber)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://www.vals.ai/benchmarks/cyber)

- **官方榜/正式委托榜**：https://www.vals.ai/benchmarks/cyber [1](https://www.vals.ai/benchmarks/cyber)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | Wonder | 80.36 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 2 | GPT-6 Sol | 77.98 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 3 | Gemini 4 Argon | 77.86 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 4 | GPT-5.6 Sol | 76.31 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 5 | GPT-6 Luna | 76.25 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 6 | Claude Haiku 5.5 | 75.48 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 7 | MiMo V2.6 Flash | 75.36 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 8 | Kimi K3 | 75.24 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 9 | Claude Opus 5.5 (CVP) | 74.58 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 10 | DeepSeek V4.1 Flash | 73.69 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：Results on the official page; the collection date is not the time at which the leaderboard was updated. [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [1](https://www.vals.ai/benchmarks/cyber)

## Contact

- **官方社交**：https://x.com/ValsAI [1](https://www.vals.ai/benchmarks/cyber) 注：A public link in the footer of the official site; X accounts are neither read nor operated.

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://www.vals.ai/benchmarks/cyber)
- 公开问题追踪：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cyber)
- 隐私政策：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://www.vals.ai/benchmarks/cyber)

## Original files

- **其他正式文档**：type：v1.1 official methods and results；url：https://www.vals.ai/benchmarks/cyber；type：Upstream ARVO mirror project, not an implementation of this benchmark；url：https://github.com/n132/ARVO-Meta [1](https://www.vals.ai/benchmarks/cyber)

- **中的论文副本**：待核实 [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 原始PDF：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber)
- SHA-256：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber)
- PDF字节数：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cyber)
- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://www.vals.ai/benchmarks/cyber)

## Changelog

- date：2026-11-07；；change：按官方材料新建中文条目；区分热度、质量和不同版本评分。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://www.vals.ai/benchmarks/cyber)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
