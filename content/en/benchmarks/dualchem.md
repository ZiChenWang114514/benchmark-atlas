# DualChem

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

Verified to exist; a research snapshot; note: trending: B; Unverified fields retain their marks

DualChem focuses on the dual-use ambiguity of chemistry: the same expertise may support legitimate research and may also be misused. 600 questions were built by chemistry experts, split into 485 multiple-choice and 115 open-response questions, covering seven experimental domains, and benign use, harmful use, and severity are recorded together. The rate of capable answers, the refusal rate, and risk awareness are different axes, and a single "higher is better" rank cannot conceal the safety tradeoff. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

In the no-tool Table 4 of the formal PDF, GPT-5.6 Sol has a full-set accuracy of 67.3%. 67.7% is only the conditional accuracy on questions that were answered. The human-assisted group is about 16 percentage points higher than the unassisted group, but this is not a strict causal experiment on the same random sample. An anonymous early HF card and code clues have been found. Their composition of human samples differs from the signed formal report, and they are not presented as a formal Scale data release. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

## Basic information

- **简称**：DualChem [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **全称**：DualChem [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **基准版本**：Snapshot released 2026-10-28 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **发布日期**：2026-10-28 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **主板块**：化学 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：Editorial filing. It does not represent an official classification.

- **子领域**：安全；双用途化学 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：Editorial filing. It does not represent an official classification.

- **论文/报告**：https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **官方主页**：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **报告标题**：DualChem: Measuring LLM Uplift and Dual-Use Risk Awareness in Chemistry [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 论文/报告版本：The listed papers, dataset cards, and READMEs were read; no traceable formal version number was confirmed. A runtime image tag, a web-page update date, and the data version are not treated as the same thing. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)
- 许可证与限制：Formally published materials have been checked, and an explicit license covering use of the task data and game assets has not been confirmed. Licenses for the software, the anonymized prerelease data, and the commercial games cannot be substituted for one another. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)
- 官方代码：The anonymous HF card links to anonymous.4open.science/r/dualchem-4318; it has not been cross-checked against a formal Scale publication page, and it is not treated as official code. [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)
- 数据入口：An anonymous DualChem-author/dualchem v1.0.0 was found, containing 600 questions and CC BY 4.0, but the composition of its human samples differs from that of the signed PDF; it has not yet been confirmed to be the current official version from Scale. [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md) [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Origin and maintenance

- **发起方**：Scale AI [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **合作方**：NIST CAISSI and domain experts of the U.S. government provided input on the scope and on how questions are classified; the first benchmark produced under a cooperative research agreement. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **核心作者**：Udari Madhushani Sehwag、Abhishek Dalvi、Yash Maurya、Drew Rein、Dylan Hardee、Jeremy Kritz、Jonathan Nguyen、Bert Herring、Evi Fuelle、Christina Q Knight、Joseph Brandifino、Max Fenkell [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **维护方**：Scale AI [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Design goals

- **核心能力**：It evaluates technical assistance, gains in human capability, risk identification, and severity judgment in ambiguous dual-use chemistry scenarios, rather than measuring only refusal of explicitly harmful requests. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **相对已有评测的缺口**：The same correct chemistry knowledge may be used for legitimate research or misused; tests of general ability, and safety tests of explicit harmful requests, do not cover this ambiguity. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

## Construction

- **题目来源**：Experts write original questions for real experimental settings, and also write benign and harmful use cases and a severity score of 1–5; the questions are not constructed by synthesis or by an explicit adversarial prompt. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **出题与审核人员**：130 chemistry experts: 19 with bachelor's degrees, 53 with master's degrees, and 58 with doctoral degrees; questions are reviewed by doctoral-level reviewers, then checked for quality by an LLM, and failed items are returned for review by the most senior doctoral reviewers. It must not be miswritten that every author holds a doctorate. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **审核流程**：Each question is accompanied by a benign use and a harmful use, each with severity 1–5. PhD reviewers examine scientific accuracy, clarity, and risk boundaries; after an LLM check, items with problems are revised by a senior chemistry PhD. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **质量控制**：Chemistry experts at doctoral level review accuracy, clarity, and safety; questions that do not pass are revised or rejected. A model quality check and a further review by more senior doctoral researchers follow. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 防污染/运行完整性：The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Data format

- **规模**：600 questions, 7 chemistry domains; there is also a controlled study of 120 participants who graduated with a bachelor's degree in chemistry, with and without model assistance. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **题型**：Most items are five-option multiple choice with at least one correct option; free-response items and 1–5 true/false rubric items are also included. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **模态**：文本 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **语言覆盖**：English (anonymous HF v1.0.0 data card language: en; examples in the published PDF are also in English) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **难度与任务跨度**：600 questions across 7 experimental-chemistry domains; 485 multiple-choice and 115 open questions. The model reports difficulty from 1–5 itself, which is not a unified difficulty calibrated by experts. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

- **公开与隐藏划分**：The anonymous HF card for v1.0.0 lists a test of 600 questions and 600 human baselines, and it provides CC BY 4.0. The makeup of its human study differs from the signed PDF of 2026-10-28. The Scale publication page does not link to that card directly. Exactly which version corresponds to which needs to be confirmed by the maintainers. [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：Only the test configuration of the anonymous pre-release card is verified at present; the public/hidden split of the named formal version remains Unverified.

  核实状态仍为待核实；部分字段或版本细节未解决。

## Evaluation

- **指标**：Accuracy, conditional accuracy on answered questions, refusal rate, agreement between risk flags and expert severity, and human gain. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **评分规则**：Acc in paper Table 4 counts refusals as incorrect; Acc.ans is computed only on answered questions, and the two have different denominators. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **提示与运行配置**：Table 4 reports both the no-tool condition and the web-search condition, and the rankings are not mixed. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **可比性限制**：67.7% is the conditional accuracy of GPT-5.6 Sol on the questions it answered; if refusals are counted as wrong over all 600 questions, the figure is 67.3%, and the two must not be mixed. The release blog’s roughly 50% and 67% is an overview, and the exact basis is the table in the paper. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Current status

- **核验日期**：2026-11-07 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **现行版本与采用证据**：version：Snapshot released 2026-10-28；trending：B；heat_evidence：Scale first released it on 2026-10-28 and reported 30+ models. NIST CAISSI and domain experts of the United States government took part in the scope and in the design of the classification. Heat B: at present this is mainly a release by the creating organization. Independent reproduction, or wide adoption in the industry, is not inferred from media reports.；evidence_2026_h2：url：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks；date：2026-11-07；date_type：observed_on；note：Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **饱和度判断**：The leader, when a refusal without tools counts as wrong, is 67.3%, and the conditional accuracy on questions that were answered is 67.7%. The two are not the same metric; the rate of technical answering is unsaturated, and recognition of risk, or a refusal, cannot be treated as that same score. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **已知问题与证据边界**：The questions measure dual-use ability and awareness of risk. A low refusal rate cannot be used to choose a “better” model directly. The human uplift study is not randomized, and the two groups are nearly separated. The difference 31.8→47.8 does not equal a strict randomized causal effect. The anonymous early HF sample and the signed formal PDF sample are composed differently. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

- **关联与衍生关系**：DualChem specifically tests dual-use chemical risk and is not merged with ChemBench general chemistry ability; specific sensitive question content is not collected or further distributed. [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 更新与修订：What can currently be verified is an update to the web methods page or leaderboard table; a version history for a standalone paper has not been located, and the web-page update time is not misrepresented as an arXiv revision. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **官方榜/正式委托榜**：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | GPT-5.6 Sol | 67.3 | Table 4 Acc (%) with no tools; refusals are counted as incorrect；2026-10-28 (release date; the specific evaluation run date is Unverified)；[2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) |
| 2 | GPT-6 Astra | 62.7 | Table 4 Acc (%) with no tools; refusals are counted as incorrect；2026-10-28 (release date; the specific evaluation run date is Unverified)；[2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) |
| 3 | GPT-6.1 Sol | 61.7 | Table 4 Acc (%) with no tools; refusals are counted as incorrect；2026-10-28 (release date; the specific evaluation run date is Unverified)；[2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) |

> GPT-5.6 Sol：result_type：Published PDF Table 4, historical experiments without tools；rank_type：Listed no-tool Acc order, not a live web leaderboard [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

> GPT-6 Astra：result_type：Published PDF Table 4, historical experiments without tools；rank_type：Listed no-tool Acc order, not a live web leaderboard [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

> GPT-6.1 Sol：result_type：Published PDF Table 4, historical experiments without tools；rank_type：Listed no-tool Acc order, not a live web leaderboard [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：67.7% is the conditional accuracy of GPT-5.6 Sol on the questions it answered; counting a refusal as wrong over all 600 questions gives 67.3%, and the two must not be mixed. The roughly 50% and 67% in the launch blog are an overview, and the exact accounting follows the tables in the paper. The update time written on the leaderboard itself is 2026-10-28 (the release date; the specific evaluation run date is Unverified); the collection date is not the run date. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Contact

- **公开联系邮箱**：udari.sehwag@scale.com；prep@scale.com [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **官方社交**：https://x.com/scale_ai [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **隐私政策**：https://scale.com/legal/privacy [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

**仍待核实**（不推断为未公开）：

- 公开问题追踪：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Original files

- **原始PDF**：https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **SHA-256**：0078a8853e2956595660fb004aca4320430fc3c950962fff2071e533788059ef [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) 注：Byte count of the PDF actually downloaded. It is not copied from an external web page.

- **PDF字节数**：3817998 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) 注：Downloaded byte count; not uploaded.

- **其他正式文档**：type：Formally published blog；url：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks；type：An anonymous early HF dataset card; which version it matches still awaits confirmation by the maintainer；url：https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

- **中的论文副本**：待核实 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

**仍待核实**（不推断为未公开）：

- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## Changelog

- date：2026-11-07；timezone：；change：首次建立近期热门中文研究条目。DualChem specifically tests dual-use chemical risk and is not merged with ChemBench general chemistry ability; specific sensitive question content is not collected or further distributed. 热度与榜单口径分离，不确定值标记待核实。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
