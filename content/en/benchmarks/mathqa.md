# MathQA
> Verification: 2026-11-08. Official evidence rechecked; license and version conflicts retained explicitly; Unverified items are not filled in

MathQA turns AQuA questions into executable operation programs. It tests the final answer and also provides formal supervision for the steps of the analysis. It is not the MATH contest set, and it is not equal to every question in the original AQuA. The order of the dev and test proportions is corrected, and the difference in license scope between MIT for the website template and Apache-2.0 for the HF dataset card is identified.

Basis of the overview: [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/) [S3](https://arxiv.org/html/2610.11978v1)

## Basic information

**简称**：MathQA [S1](https://arxiv.org/abs/1905.13319)

**全称**：MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms [S1](https://arxiv.org/abs/1905.13319)

**版本口径**：2019 Operation-Based Formalisms data; the data commit is not fixed [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319)

**论文修订**：arXiv v1 [S4](https://arxiv.org/abs/1905.13319)

**发布时间**：2019-05-31 (date of the first arXiv draft; not a statement of an independent dataset first release). [S1](https://arxiv.org/abs/1905.13319)

**主板块**：数学 [S2](https://math-qa.github.io/math-QA/)

**领域**：Multi-step mathematics word problem [S1](https://arxiv.org/abs/1905.13319)

**许可与权利边界**：The AllenAI dataset card on HF states Apache-2.0 explicitly; the LICENSE at the root of the GitHub repository is MIT, but it is signed 2013–2019 Blackrock Digital LLC (a template for a web page), and it cannot be taken as an unconditional MIT grant over the whole MathQA dataset. The difference of source is kept, and use of the data should check the dataset card and the rights in the original questions first. [S5](https://huggingface.co/datasets/allenai/math_qa) [S6](https://github.com/math-qa/math-QA/blob/master/LICENSE)

**论文**：https://arxiv.org/abs/1905.13319 [S1](https://arxiv.org/abs/1905.13319)

**代码入口**：https://github.com/math-qa/math-QA [S2](https://math-qa.github.io/math-QA/)

**数据入口**：https://math-qa.github.io/math-QA/data/MathQA.zip [S2](https://math-qa.github.io/math-QA/) [S7](https://math-qa.github.io/math-QA/data/MathQA.zip)

**官网**：https://math-qa.github.io/math-QA/ [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319)

**论文标题**：MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms [S1](https://arxiv.org/abs/1905.13319)

## Origin and maintenance

**发起方**：University of Washington、Allen Institute for AI [S1](https://arxiv.org/abs/1905.13319)

**署名与合作**：The institutions on the first page of the paper are the University of Washington and the Allen Institute for AI; Figure Eight is a crowdsourcing platform and is not treated, in addition, as an institution of the authors. [S8](https://arxiv.org/pdf/1905.13319)

**作者**：Aida Amini；Saadia Gabriel；Shanchuan Lin；Rik Koncel-Kedziorski；Yejin Choi；Hannaneh Hajishirzi [S8](https://arxiv.org/pdf/1905.13319) [S5](https://huggingface.co/datasets/allenai/math_qa)

> Shanchuan Lin is recorded from the PDF and from the NAACL citation; Peter Lin in the arXiv metadata and in the project BibTeX differs, and the original difference between the sources is kept.

**维护入口**：The MathQA authors’ project homepage (Aida Amini and others); the homepage lists the public contact affiliation as the University of Washington, and a current commitment to provide service is not asserted from that. [S2](https://math-qa.github.io/math-QA/)

**资助**：ONR N00014-18-1-2826, NSF IIS 1616112, the Allen Distinguished Investigator Award, and donations from Google, the Allen Institute for AI, Amazon, and Bloomberg; acknowledgments in the paper. [S8](https://arxiv.org/pdf/1905.13319)

## Design goals

**衡量能力**：An executable operation program is generated from a textual applied problem, and the final answer and the interpretable computation steps are checked. [S1](https://arxiv.org/abs/1905.13319)

**设计动机**：Looking only at a natural-language rationale may conceal logical errors; a machine-executable formal language with explicit steps is needed. [S1](https://arxiv.org/abs/1905.13319)

## Construction

**题目/样本来源**：Some questions on AQuA-RAT are re-annotated and corrected, and formal programs are constructed with 58 operations and 6 domains. [S1](https://arxiv.org/abs/1905.13319)

**构建者背景**：Figure Eight crowdsourced annotators; the authors designed the operation interface, quality-check questions, and expert spot checks. [S1](https://arxiv.org/abs/1905.13319)

**审查流程**：A program may be submitted only when its final value is close to the correct answer; it is then checked whether the program is logically consistent with the question and the explanation, and at least 2/3 of the verifiers must accept it. [S1](https://arxiv.org/abs/1905.13319)

**质量控制**：The validation pass rate is 94.64%; 92% of an expert sample of 500 questions are correct (the convention in the paper); a value that happens to be numerically correct can still be logically wrong. [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/)

**去污染与防泄漏**：The paper diagnoses near-duplicates in AQuA and mismatched rationales. Annotation expansion transfers similar questions using a Levenshtein distance threshold of 4 words. A random split is not template-level isolation, and it cannot be used to prove the absence of cross-split similarity or later LLM contamination. [S8](https://arxiv.org/pdf/1905.13319)

## Data format

**规模**：The official MathQA.zip, as actually read: train 29,837, dev 4,475, and test 2,985, for 37,297 in the main splits. There is also challenge_test with 604, which is not automatically counted as a set of mutually exclusive new questions. [S7](https://math-qa.github.io/math-QA/data/MathQA.zip)

**任务形式**：5-choose-1 applied problems, which also provide an operation program, a rationale, and a domain label. [S1](https://arxiv.org/abs/1905.13319)

**模态**：Text (mathematical symbols expressed as text); not an original image or video recognition task [S1](https://arxiv.org/abs/1905.13319)

**语言**：English question text; for formal or mathematical notation, see the modality and the repository format [S1](https://arxiv.org/abs/1905.13319)

**难度与覆盖**：General applied-mathematics and examination questions, covering 6 categories of domain; this is not another name for the MATH competition set. [S1](https://arxiv.org/abs/1905.13319)

**公开与测试划分**：Section §6.1 of the original paper writes 80/12/8% in the order training/dev/test (an earlier entry wrongly wrote training/test/dev). The public package actually has train=29,837, dev=4,475, and test=2,985, consistent with HF; challenge_test=604 is kept on its own. [S8](https://arxiv.org/pdf/1905.13319) [S9](https://math-qa.github.io/math-QA/data/MathQA.zip) [S5](https://huggingface.co/datasets/allenai/math_qa)

## Evaluation

**指标**：Answer accuracy, with executability of the program and reasonableness of the steps available as supplementary metrics. [S1](https://arxiv.org/abs/1905.13319)

**评分**：The generated program is executed to obtain a number, which is then mapped to an option; checking only the final number is not enough to show that every reasoning step is correct. [S1](https://arxiv.org/abs/1905.13319)

**提示/训练/运行设置**：The original paper uses a bidirectional RNN or LSTM sequence-to-program model and OpenNMT, with 2 layers each for the encoder and the decoder, hidden size=100, and Adam lr=0.001; MathQA uses beam=100 and AQuA uses beam=200. LLM results under study must record the prompting protocol separately. [S8](https://arxiv.org/pdf/1905.13319)

**官方脚本**：https://github.com/math-qa/math-QA [S10](https://github.com/math-qa/math-QA) [S1](https://arxiv.org/abs/1905.13319)

**可比性警示**：MathQA program supervision, the original AQuA rationale, and the MATH competition set are not the same benchmark; scores cannot be merged only because the question sources overlap. [S1](https://arxiv.org/abs/1905.13319) [S3](https://arxiv.org/html/2610.11978v1)

## Current status

**核查日**：2026-11-08 [S11](https://math-qa.github.io/math-QA/)

**数据版本与持续使用**：2019 Operation-Based Formalisms data; the data commit is not fixed [S2](https://math-qa.github.io/math-QA/) [S1](https://arxiv.org/abs/1905.13319)

**论文版本与证据历史**：v1 2019-05-31。此前H2使用证据继续保留于结构化档案，不把其日期当论文修订日。 [S4](https://arxiv.org/abs/1905.13319)

> Earlier H2 usage evidence is retained; only the exact revision time of the arXiv opened this time is updated to.

**饱和度边界**：待核实 [S1](https://arxiv.org/abs/1905.13319) [S3](https://arxiv.org/html/2610.11978v1)

> Whether it is saturated depends on the specific split, the tools, and the protocol; the scores below are only a snapshot from a limited source and are not a judgment of overall saturation or of SOTA

**已知问题与争议**：The authors' official website explicitly acknowledges that the original rationale may be noisy, incomplete, or wrong; the author name is Peter Lin on the website and in the arXiv metadata, and Shanchuan Lin in the PDF, and each source is kept as it stands. [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/)

**版本/衍生关系**：A re-annotated subset of operation programs from AQuA-RAT; it should not be conflated with the whole original AQuA of about 100,000 questions. [S1](https://arxiv.org/abs/1905.13319) [S2](https://math-qa.github.io/math-QA/)

## Leaderboard snapshot

**快照日**：2026-11-08 [S12](https://math-qa.github.io/math-QA/html/)

**官方榜入口**：https://math-qa.github.io/math-QA/html/ [S13](https://math-qa.github.io/math-QA/html/)

**第三方入口**：待核实 [S1](https://arxiv.org/abs/1905.13319)

> No readable leaderboard was confirmed on which AA, Epoch, or LMArena separately tracks this exact version; the research and vendor tables below are supplementary only and are not passed off as a secondary leaderboard

### Historical research paper / original collection date retained

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Qwen3.8 Max | 94.4 | % | [来源](https://arxiv.org/html/2610.11978v1)，2026-11-07 |
| 2 | Qwen3.8 Flash | 93.3 | % | [来源](https://arxiv.org/html/2610.11978v1)，2026-11-07 |
| 3 | Gemini 3.8 Flash | 92.7 | % | [来源](https://arxiv.org/html/2610.11978v1)，2026-11-07 |

### Official static / MathQA Challenge

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 37.4% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

### Official static / Geometry

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 40.2% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

### Official static / Physics

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 37.8% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

### Official static / General

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 36.3% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

### Official static / Gain

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 38.3% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

### Official static / Probability

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 35.3% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

### Official static / Other

| Rank / order | Model | Score | Metric | Source and collection date |
|---|---|---|---|---|
| 1 | Seq2Prog+Cat | 33.3% | Official-site historical leaderboard score | [来源](https://math-qa.github.io/math-QA/html/)，2026-11-08 |

分项成绩、模型日期、上下文或样本覆盖等元数据保存在本条结构化档案；表中顺序仅在注明的赛道内有意义。 [S12](https://math-qa.github.io/math-QA/html/) [S14](https://arxiv.org/html/2610.11978v1)

**覆盖与时效**：Existing scores from the research papers, and the original collection dates, are retained; seven historical tracks from reopening the official website on this occasion are added. MathQA Challenge 37.4 and the scores in each domain cannot be mixed into an industry-wide overall leaderboard; the official website does not mark a single time at which the results were updated. [S12](https://math-qa.github.io/math-QA/html/)

## Contact

**公开研究邮箱**：amini91@cs.washington.edu [S2](https://math-qa.github.io/math-QA/)

**问题反馈**：https://github.com/math-qa/math-QA/issues [S10](https://github.com/math-qa/math-QA)

**官方发布渠道**：待核实 [S1](https://arxiv.org/abs/1905.13319)

> No dedicated official social account has been verified, and personal accounts of the same name are not included

**隐私口径**：待核实 [S1](https://arxiv.org/abs/1905.13319)

> A dedicated privacy clause for the benchmark has not been verified; a license cannot replace a privacy policy.

## Original files

**源站PDF**：https://arxiv.org/pdf/1905.13319 [S1](https://arxiv.org/abs/1905.13319)

**PDF SHA-256**：220cd30ed121d4472bace7ce7a1a80c28cd4ed65669d248d5773ed3b866fdaf2 [S8](https://arxiv.org/pdf/1905.13319)

> Checksum of the PDF bytes downloaded from the source site this time. This does not claim that an existing copy was re-sent or replaced.

**PDF字节数**：850027 [S8](https://arxiv.org/pdf/1905.13319)

**原有文件夹**：{"id": "1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-", "webViewLink": " [S15](

**其他材料**：{"chinese_intro_doc": {"id": "1YKyOOE-Xx6_XxZAJbkBTqSlXhvtnUM4QRxJCRThRgBs", "webViewLink": " "mimeType": "application/vnd.google-apps.document"}, "local_markdown": "content/benchmarks/mathqa.md"} [S15](

**原有 PDF**：{"id": "1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE", "webViewLink": " [S16](

## Changelog

- 2026-11-07，核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07，深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- 2026-11-08，逐篇核验：重开原论文摘要/PDF文本、Official README/LICENSE、可定位HF数据卡与官方/第三方榜；更正版本、授权与评分口径，分赛道更新结构化成绩，重写中文11节；未知值保留。
[S2](https://math-qa.github.io/math-QA/) [S11](https://math-qa.github.io/math-QA/)

### 来源索引

访问日期只表示本库读取来源的日期，不代替模型运行日、数据发布日期或榜单更新时间。

- S1，[https://arxiv.org/abs/1905.13319](https://arxiv.org/abs/1905.13319)，访问 2026-11-07
- S2，[https://math-qa.github.io/math-QA/](https://math-qa.github.io/math-QA/)，访问 2026-11-07
- S3，[https://arxiv.org/html/2610.11978v1](https://arxiv.org/html/2610.11978v1)，访问 2026-11-07
- S4，[https://arxiv.org/abs/1905.13319](https://arxiv.org/abs/1905.13319)，访问 2026-11-08
- S5，[https://huggingface.co/datasets/allenai/math_qa](https://huggingface.co/datasets/allenai/math_qa)，访问 2026-11-08
- S6，[https://github.com/math-qa/math-QA/blob/master/LICENSE](https://github.com/math-qa/math-QA/blob/master/LICENSE)，访问 2026-11-08
- S7，[https://math-qa.github.io/math-QA/data/MathQA.zip](https://math-qa.github.io/math-QA/data/MathQA.zip)，访问 2026-11-07
- S8，[https://arxiv.org/pdf/1905.13319](https://arxiv.org/pdf/1905.13319)，访问 2026-11-08
- S9，[https://math-qa.github.io/math-QA/data/MathQA.zip](https://math-qa.github.io/math-QA/data/MathQA.zip)，访问 2026-11-08
- S10，[https://github.com/math-qa/math-QA](https://github.com/math-qa/math-QA)，访问 2026-11-07
- S11，[https://math-qa.github.io/math-QA/](https://math-qa.github.io/math-QA/)，访问 2026-11-08
- S12，[https://math-qa.github.io/math-QA/html/](https://math-qa.github.io/math-QA/html/)，访问 2026-11-08
- S13，[https://math-qa.github.io/math-QA/html/](https://math-qa.github.io/math-QA/html/)，访问 2026-11-07
- S14，[https://arxiv.org/html/2610.11978v1](https://arxiv.org/html/2610.11978v1)，访问 2026-11-08
- S15，[，访问 2026-11-07
- S16，[，访问 2026-11-07
