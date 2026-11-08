# GDPval (GDPval-AA v2.1)

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

GDPval takes occupational deliverables as its object. The original version compares blind-review preference between model products and expert products. GDPval-AA compares model products inside an independent agent environment and estimates Elo. Public HF data v2 and AA v2.1 are not the same version number.

Latest review

## Basic information

**简称**：GDPval (GDPval-AA v2.1)

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**全称**：GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**基准版本**：Public GDPval data v2 (the current HF commit note: rubrics + deliverables); GDPval-AA v2.1 is an independent evaluation implementation, not the same version number.

Sources: [1](https://huggingface.co/datasets/openai/gdpval/tree/main) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

**论文版本**：arXiv v1（2025-10-05）

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**发布日期**：2025-09-25 (official first release post; the first arXiv version is 2025-10-06 06:36:43 )

Sources: [1](https://openai.com/index/gdpval/) (accessed 2026-11-07); [2](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**主板块**：Agent

核验说明：Benchmark Constitution editorial filing. It is not an official classification.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**领域标签**：知识工作；金融；法律

核验说明：编辑标签

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**许可证与授权边界**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**论文或技术报告**：https://arxiv.org/abs/2510.04374

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**官方代码**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**数据地址**：https://huggingface.co/datasets/openai/gdpval

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**官方主页**：https://huggingface.co/datasets/openai/gdpval

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**论文题名**：GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

## Origin and maintenance

**发起方**：OpenAI

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**协作与机构边界**：The tasks are written and blindly reviewed together with outside professionals in each occupation; a list of their former employers is only an illustration from a résumé and cannot be taken as an institutional partnership.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07); [2](https://openai.com/index/gdpval/) (accessed 2026-11-07)

**作者**：Tejal Patwardhan；Rachel Dias；Elizabeth Proehl；Grace Kim；Michele Wang；Olivia Watkins；Simón Posada Fishman；Marwan Aljubeh；Phoebe Thacker；Laurance Fauconnet；Natalie S. Kim；Patrick Chao；Samuel Miserendino；Gildas Chabot；David Li；Michael Sharman；Alexandra Barr；Amelia Glaese；Jerry Tworek

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**维护方**：Original data: OpenAI; independent implementation: Artificial Analysis

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**资助方**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

## Design goals

**测量能力**：Measures the quality of deliverables in economically relevant knowledge work through real occupational tasks.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**相对既有评测的缺口**：Academic short-answer tests have difficulty covering file handling, aesthetics, and usability in professional work.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

## Construction

**题目来源**：Actual work products of professional practitioners; 44 occupations in 9 industries, selected by O*NET work activities.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**出题与研究背景**：Experts have at least 4 years of professional experience, with an average of 14 years; they pass an interview, a background check, training, and a test.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**审核流程**：Automated screening plus a generalist first review, peer review by occupational experts, and iterative final review.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**质量控制**：All 1,320 tasks had human review, averaging 5 rounds and at least 3 rounds.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**去污染与泄漏边界**：Identifying information of the problem setters has been removed from the public gold subset; this cannot, on that basis, be taken as a complete absence of training contamination.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

## Data format

**规模与口径**：The full set has 1,320 tasks; the public gold subset has 220 tasks, with 5 questions per occupation.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**任务类型**：Text requests, reference files, and professional deliverables; the files include documents, spreadsheets, slides, CAD, and audio and video.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**模态**：文本；文档；图像；音频；视频；表格

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**语言**：The public examples are occupational tasks in English; multilingual coverage is Unverified.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**难度**：Long-horizon occupational tasks; not the same as an entire occupation being open to automation.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**公开与隐藏划分**：A gold subset of 220 tasks is public; availability of the remaining full data is Unverified.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

## Evaluation

**指标**：Original track: blind-evaluation win rate of model deliverables against human-expert work products; AA track: Elo of paired model deliverables.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**评分方式**：The original recommendation is pairwise comparison by occupational experts; the automatic judge is an experimental proxy and not a full substitute for the experts.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**提示与运行设置**：AA uses the Stirrup agent loop and provides a shell and web browsing; two blinded outputs are compared by an LLM judge.

Sources: [1](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

**官方复现入口**：The original evaluation provides an automatic scoring service for experiments at evals.openai.com; the official paper states explicitly that it does not replace blinded review by professional experts. The independent AA implementation uses Stirrup and cannot be treated as the original official scoring script.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07); [2](https://openai.com/index/gdpval/) (accessed 2026-11-07); [3](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

**可比性警告**：The original win rate against humans is not equal to the GDPval-AA v2.1 Elo; differences of harness, budget, and judge must be kept on separate tracks.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**数据及热度证据**：```json
{
 "version": "GDPval public data v2 (rubrics + deliverables); GDPval-AA v2.1 is an independent implementation"
 "heat_confidence": "A"
 "why_trending": "Candidate heat tier A; the evidence reopened below is labeled, item by item, with the evaluating party and the nature of the evidence, and the number of web pages is not treated as the number of independently adopting organizations."
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "The current ECI composition explicitly lists this benchmark; inclusion does not equal running it."
 }
 {
 "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Artificial Analysis"
 "note": "The current v2.1 independent-evaluation leaderboard explicitly displays frontier-model Elo."
 }
 ]
}
```

Sources: [1](https://huggingface.co/datasets/openai/gdpval/tree/main) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

**论文与版本历史**：The current arXiv submission history contains only v1: 2025-10-06 06:36:43; the data and the release post predate that paper's first version.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07); [2](https://openai.com/index/gdpval/) (accessed 2026-11-07)

**饱和程度**：The original metric is a preference win rate relative to human experts, not absolute task accuracy; the AA metric is relative Elo (anchor 1600), with no 100%-style ceiling, so a leading score of 1866 cannot be called saturated.

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07); [2](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

**已知问题与局限**：Public gold tasks and deliverables may be seen by later training; a one-time explicit request does not cover clarification and multi-turn revision in real work; savings in model inference time and cost do not include supervision, integration, and error-correction costs.

Sources: [1](https://openai.com/index/gdpval/) (accessed 2026-11-07); [2](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07); [3](https://huggingface.co/datasets/openai/gdpval/tree/main) (accessed 2026-11-07)

**后续与衍生**：The GDPval data and the AA evaluation implementation are kept on separate tracks within the same entry and are not split into two items; AA v5 has been removed from the composite index but is still evaluated on its own.

核验说明：The editorial standard for deduplication; concrete differences among versions still follow the official materials.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**官方入口**：https://huggingface.co/datasets/openai/gdpval

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**第三方入口**：https://artificialanalysis.ai/evaluations/gdpval-aa

Sources: [1](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | Claude Opus 5.5 (Max, Default Fallback) | 1866 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 2 | Kimi K3.1 Pro | 1858 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 3 | Muse Wonder Full (Max) | 1857 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 4 | Claude Sonnet 5.5 (Max, Default Fallback) | 1838 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 5 | Claude Opus 5.5 (Xhigh, Default Fallback) | 1835 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 6 | Muse Wonder (Max) | 1770 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 7 | Claude Fable 5.1 (Max, Default Fallback) | 1763 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 8 | DeepSeek V4.1 Flash 1017 (Max) | 1746 | GDPval-AA v2.1 Elo | Unverified (leaderboard update time) | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：The top 8 of the current AA leaderboard were reread, keeping the reasoning and fallback configurations and the confidence intervals; the anchor is DeepSeek V4.1 Flash(max)=1600. A model's release month is not the leaderboard update time. The three accountings, data v2, AA v2.1, and the original expert win rate, must be distinguished.

Sources: [1](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07); [2](https://huggingface.co/datasets/openai/gdpval/tree/main) (accessed 2026-11-07)

## Contact

**公开联系邮箱**：tejal@openai.com (public correspondence channel given in the paper)

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**Issues或讨论入口**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**官方社交**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**隐私政策**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

## Original files

**原始PDF**：https://arxiv.org/pdf/2510.04374

Sources: [1](https://arxiv.org/abs/2510.04374) (accessed 2026-11-07)

**PDF SHA-256**：a04cca8451c486d871f8d2c6c57b8bc03b45daf1b5b0269146929bc8bf688dec

核验说明：Byte count of the original downloaded PDF, not the size displayed on the arXiv page.

Sources: [1](https://arxiv.org/pdf/2510.04374) (accessed 2026-11-07)

**PDF字节数**：```json
14203711
```

核验说明：Actual downloaded byte count; it does not mean the file was uploaded.

Sources: [1](https://arxiv.org/pdf/2510.04374) (accessed 2026-11-07)

**文件夹**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

**其他官方文档**：```json
[
 {
 "type": "First release and limitations"
 "url": "https://openai.com/index/gdpval/"
 }
 {
 "type": "Public data v2 catalog"
 "url": "https://huggingface.co/datasets/openai/gdpval/tree/main"
 }
 {
 "type": "Independent AA v2.1 methods and leaderboard"
 "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
 }
]
```

Sources: [1](https://openai.com/index/gdpval/) (accessed 2026-11-07); [2](https://huggingface.co/datasets/openai/gdpval/tree/main) (accessed 2026-11-07); [3](https://artificialanalysis.ai/evaluations/gdpval-aa) (accessed 2026-11-07)

**论文链接**：待核实

状态：待核实。

核验说明：This group only created a local research entry and did not upload.

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)

## Changelog

**及历史变更**：```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-07"
 Latest review
 }
]
```

Sources: [1](https://huggingface.co/datasets/openai/gdpval) (accessed 2026-11-07)
