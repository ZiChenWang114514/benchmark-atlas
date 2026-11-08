# MATH
> Verification: 2026-11-08. Verified to exist; an in-depth entry; explicit Unverified items are retained.

MATH provides contest mathematics problems with complete solutions. The full test set is 5,000 questions; the commonly seen MATH-500 is only one subset of it. Reasoning budget, code tools, voting, and answer normalization for modern models change the protocol substantially, and a near-perfect score on one subset cannot be extended into a claim that all contest-mathematics ability is saturated.

Basis of the overview: [S1](https://arxiv.org/abs/2103.03874) [S2](https://github.com/hendrycks/math) [S3](https://arxiv.org/html/2609.27284v1)

## Basic information

**简称**：MATH [S1](https://arxiv.org/abs/2103.03874)

**全称**：Mathematics Aptitude Test of Heuristics [S1](https://arxiv.org/abs/2103.03874)

**版本口径**：Full MATH, 12500 questions; MATH-500 is listed separately as a derived scope [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**论文修订**：arXiv v2 [S4](https://arxiv.org/abs/2103.03874)

**发布时间**：2021-03-06 (date of the first arXiv draft; not a statement of an independent dataset first release). [S1](https://arxiv.org/abs/2103.03874)

**主板块**：数学 [S2](https://github.com/hendrycks/math)

**领域**：Competition mathematics problem solving [S1](https://arxiv.org/abs/2103.03874)

**许可与权利边界**：The LICENSE of the official repository is MIT (2021 Dan Hendrycks), and the paper likewise states that the data and the code are MIT; the HF mirror qwedsacf is marked MIT. Rights in the original contest questions still cannot be guaranteed automatically by the license of the repository. [S5](https://github.com/hendrycks/math/blob/main/LICENSE) [S6](https://arxiv.org/pdf/2103.03874) [S7](https://huggingface.co/datasets/qwedsacf/competition_math)

**论文**：https://arxiv.org/abs/2103.03874 [S1](https://arxiv.org/abs/2103.03874)

**代码入口**：https://github.com/hendrycks/math [S2](https://github.com/hendrycks/math)

**数据入口**：https://huggingface.co/datasets/qwedsacf/competition_math [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**官网**：https://github.com/hendrycks/math [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**论文标题**：Measuring Mathematical Problem Solving With the MATH Dataset [S1](https://arxiv.org/abs/2103.03874)

## Origin and maintenance

**发起方**：University of California Berkeley, University of Chicago (paper authorship) [S1](https://arxiv.org/abs/2103.03874)

**署名与合作**：The paper credits UC Berkeley and the University of Chicago; this is not used to add other unconfirmed collaborations. [S6](https://arxiv.org/pdf/2103.03874)

**作者**：Hendrycks, Dan；Burns, Collin；Kadavath, Saurav；Arora, Akul；Basart, Steven；Tang, Eric；Song, Dawn；Steinhardt, Jacob [S1](https://arxiv.org/abs/2103.03874)

**维护入口**：The official public entry points are hendrycks/math and Dan Hendrycks; these are entry points for maintenance and feedback and do not constitute a guarantee of active maintenance now. [S8](https://github.com/hendrycks/math)

**资助**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> Paper acknowledgments and current operational funding were not verified item by item; institutional affiliation is not a funding source

## Design goals

**衡量能力**：Evaluates multi-step solving, symbolic manipulation, and correctness of the final answer in contest mathematics. [S1](https://arxiv.org/abs/2103.03874)

**设计动机**：Simple arithmetic, or a set of short steps, is not enough to reflect broader mathematical abilities such as algebra, geometry, and number theory. [S1](https://arxiv.org/abs/2103.03874)

## Construction

**题目/样本来源**：Mathematics problems drawn from contests such as the AMC and AIME and compiled by AoPS, retaining complete solutions and final answers. [S1](https://arxiv.org/abs/2103.03874)

**构建者背景**：Researchers compiled existing human mathematics-contest problems and solutions; not all 12500 problems were original work by the authors. [S1](https://arxiv.org/abs/2103.03874)

**审查流程**：Questions, solutions, difficulty, and subject information are organized into one processable text format. [S1](https://arxiv.org/abs/2103.03874)

**质量控制**：Mathematical expressions are written in LaTeX, and the final answer is marked with boxed; some geometry problems provide figure information through Asymptote code. [S1](https://arxiv.org/abs/2103.03874)

**去污染与防泄漏**：The question sources have long been public; the original paper discusses pretraining and the capability gap, but it cannot guarantee that later models have no memory of the questions. [S1](https://arxiv.org/abs/2103.03874)

## Data format

**规模**：12500 contest mathematics questions in total: 7500 for training and 5000 for testing. MATH-500 must not be treated as the full test set. [S1](https://arxiv.org/abs/2103.03874)

**任务形式**：Open-ended mathematical problem solving; scoring emphasizes a normalizable final answer rather than a step-by-step proof. [S1](https://arxiv.org/abs/2103.03874)

**模态**：Natural language and LaTeX; geometric figures are represented by Asymptote code, and this is not a native raster-image evaluation. [S1](https://arxiv.org/abs/2103.03874)

**语言**：English question text; for formal or mathematical notation, see the modality and the repository format [S1](https://arxiv.org/abs/2103.03874)

**难度与覆盖**：5 difficulty levels and 7 subjects; accuracy should be examined separately by level and by subject. [S1](https://arxiv.org/abs/2103.03874)

**公开与测试划分**：The full training set of 7500 and the test set of 5000 are both public; MATH-500 selects only 500 of the test questions, and its score cannot stand for the full set. [S1](https://arxiv.org/abs/2103.03874)

## Evaluation

**指标**：Final-answer accuracy (normalized exact match / equivalence decision). [S1](https://arxiv.org/abs/2103.03874)

**评分**：Extracts the boxed answer and handles normalization of mathematical strings; details of format normalization change the score. [S1](https://arxiv.org/abs/2103.03874)

**提示/训练/运行设置**：The original paper includes fine-tuning experiments; modern CoT, calculators, code, voting, and single generation must be recorded separately. [S1](https://arxiv.org/abs/2103.03874)

**官方脚本**：The official hendrycks/math repository provides dataset loaders and evaluation code; reproduction must pin the code version. [S9](https://raw.githubusercontent.com/hendrycks/math/main/README.md)

**可比性警示**：The full MATH test of 5000 questions and MATH-500 are different denominators; the Hunyuan report writes MATH but cites Lightman, and the scope of the subset cannot yet be confirmed. [S1](https://arxiv.org/abs/2103.03874) [S3](https://arxiv.org/html/2609.27284v1)

## Current status

**核查日**：2026-11-08 [S8](https://github.com/hendrycks/math)

**数据版本与持续使用**：Full MATH, 12500 questions; MATH-500 is listed separately as a derived scope [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**论文版本与证据历史**：v1 2021-03-06；v2 2021-11-09。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S4](https://arxiv.org/abs/2103.03874)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：The current high on AA MATH-500 is 99.4%, which supports only that this subset of 500 questions is near a full score under that protocol; it cannot be used to conclude that the full set of 5,000 test questions, and every level of difficulty, are saturated. [S10](https://artificialanalysis.ai/evaluations/math-500)

**已知问题与争议**：The official paper states that the data/code are released under MIT, but rights in the original contest content cannot be unconditionally extrapolated from that; there has been no legal review. [S1](https://arxiv.org/abs/2103.03874) [S2](https://github.com/hendrycks/math)

**版本/衍生关系**：MATH-500 and PRM800K were developed around process supervision; AA provides only the MATH-500 leaderboard, which cannot be passed off as the full MATH leaderboard. [S1](https://arxiv.org/abs/2103.03874) [S2](https://github.com/hendrycks/math)

## Leaderboard snapshot

**快照日**：2026-11-08 [S8](https://github.com/hendrycks/math)

**官方榜入口**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> No independent, continuously updated official leaderboard has been confirmed; experiments in the paper are not presented as an official live leaderboard

**第三方入口**：https://artificialanalysis.ai/evaluations/math-500 [S11](https://artificialanalysis.ai/evaluations/math-500)

### An AA subset of 500 questions; not the complete MATH

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | GPT-5 (High) | 99.4% | AA MATH-500 accuracy | [来源](https://artificialanalysis.ai/evaluations/math-500)，2026-11-08 |
| 2 | o3 | 99.2% | AA MATH-500 accuracy | [来源](https://artificialanalysis.ai/evaluations/math-500)，2026-11-08 |
| 3 | Grok 3 mini Reasoning (High) | 99.2% | AA MATH-500 accuracy | [来源](https://artificialanalysis.ai/evaluations/math-500)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S10](https://artificialanalysis.ai/evaluations/math-500)

**覆盖与时效**：Only the top three of MATH-500 in the AA summary that was opened are recorded; tied scores keep the order of the source’s narrative, and a statistically significant difference is not inferred. The full official live overall leaderboard for MATH is Unverified. [S10](https://artificialanalysis.ai/evaluations/math-500)

## Contact

**公开研究邮箱**：hendrycks@berkeley.edu [S2](https://github.com/hendrycks/math) [S1](https://arxiv.org/abs/2103.03874)

**问题反馈**：https://github.com/hendrycks/math/issues [S2](https://github.com/hendrycks/math)

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> No dedicated official social account has been verified, and personal accounts of the same name are not included

**隐私口径**：待核实 [S1](https://arxiv.org/abs/2103.03874)

> A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

## Original files

**源站PDF**：https://arxiv.org/pdf/2103.03874 [S1](https://arxiv.org/abs/2103.03874)

**PDF SHA-256**：a6f448173e57d808a38679dd817bcc2e01324176cbf491d08c43cc0e7ca30bfe [S6](https://arxiv.org/pdf/2103.03874)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：2030715 [S6](https://arxiv.org/pdf/2103.03874)

**原有文件夹**：{"id": "1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL", "webViewLink": " [S12](

**其他材料**：{"chinese_intro_doc": {"id": "1s8SrmzMxF5AnMs2uZOKwSfgRQ18Qwu6IH1jsKu7qZ9o", "webViewLink": " "mimeType": "application/vnd.google-apps.document"}, "local_markdown": "content/benchmarks/math.md"} [S12](

**原有 PDF**：{"id": "1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu", "webViewLink": " [S13](

## Changelog

- 2026-11-07，核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07，实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://github.com/hendrycks/math) [S8](https://github.com/hendrycks/math)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874)，访问 2026-11-07
- S2，[https://github.com/hendrycks/math](https://github.com/hendrycks/math)，访问 2026-11-07
- S3，[https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)，访问 2026-11-07
- S4，[https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874)，访问 2026-11-08
- S5，[https://github.com/hendrycks/math/blob/main/LICENSE](https://github.com/hendrycks/math/blob/main/LICENSE)，访问 2026-11-08
- S6，[https://arxiv.org/pdf/2103.03874](https://arxiv.org/pdf/2103.03874)，访问 2026-11-08
- S7，[https://huggingface.co/datasets/qwedsacf/competition_math](https://huggingface.co/datasets/qwedsacf/competition_math)，访问 2026-11-08
- S8，[https://github.com/hendrycks/math](https://github.com/hendrycks/math)，访问 2026-11-08
- S9，[https://raw.githubusercontent.com/hendrycks/math/main/README.md](https://raw.githubusercontent.com/hendrycks/math/main/README.md)，访问 2026-11-07
- S10，[https://artificialanalysis.ai/evaluations/math-500](https://artificialanalysis.ai/evaluations/math-500)，访问 2026-11-08
- S11，[https://artificialanalysis.ai/evaluations/math-500](https://artificialanalysis.ai/evaluations/math-500)，访问 2026-11-07
- S12，[，访问 2026-11-07
- S13，[，访问 2026-11-07
