# GDP.pdf

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

This benchmark requires finding the correct evidence in the professional PDF itself and then answering with the correct interpretation in the domain; extracting the text correctly is not sufficient. The main leaderboard requires every rubric item to pass in full, and a partial score cannot be interchanged with the strict task success rate.

Latest review

## Basic information

**简称**：GDP.pdf

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**全称**：GDP.pdf

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**基准版本**：100-question public version

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**论文版本**：arXiv v3（2026-07-15）

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**发布日期**：2026-04-14 (benchmark release date stated by the paper in §5.1; the July paper is not the first-release date)

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**主板块**：语言

核验说明：Editorial filing. It does not represent an official classification.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**领域标签**：长上下文；多模态；专业文档

核验说明：Editorial filing. It does not represent an official classification.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**许可证与授权边界**：Apache-2.0 (the public benchmark described in paper Table 2); third-party PDFs retain their original rights.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**论文或技术报告**：https://arxiv.org/abs/2607.11192

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**官方代码**：https://github.com/surge-ai/gdp-pdf

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**数据地址**：https://huggingface.co/datasets/surgeai/GDP.pdf

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**官方主页**：https://surgehq.ai/benchmarks/gdp-pdf

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**论文题名**：GDP.pdf: Benchmarking Grounded Multimodal Reasoning over Professional PDF Documents

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

## Origin and maintenance

**发起方**：Surge AI

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**协作与机构边界**：待核实

状态：待核实。

核验说明：The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**作者**：Suhaas Garre、Emily Ritchie、Sushant Mehta、Edwin Chen

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**维护方**：Surge AI

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**资助方**：待核实

状态：待核实。

核验说明：The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

## Design goals

**测量能力**：Carry out evidence-based question answering for real work on the original professional PDFs, while also testing visual parsing, domain semantics, cross-page citation, and refusal when there is no evidence.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**相对既有评测的缺口**：Meeting the standard separately on OCR, on single-table question answering, and on visual questions in a subject does not mean that a real contract, a benefits document, an architectural drawing, or a clinical document can be interpreted correctly.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

## Construction

**题目来源**：Practitioners in ten professional fields submitted real work questions and the original PDFs; only candidates on which at least two frontier models made a substantive error were kept, and questions answerable from common sense alone, or semantically ambiguous, were excluded.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**出题与研究背景**：The tasks were proposed, from daily work, by working practitioners in ten professional fields; the authors of the paper are Suhaas Garre, Emily Ritchie, Sushant Mehta, and Edwin Chen of Surge AI. The authors of the paper are not conflated with all of the experts who wrote the questions.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**审核流程**：Experts write the reference answers, the atomic rubrics, and the capability labels; a reference answer must pass its own rubric, and intentionally wrong answers must be caught by the corresponding criteria; the paper’s error analysis checks the original text by hand, separately.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**质量控制**：Experts write the reference answers, the atomic rubrics, and the capability labels; a reference answer must pass its own rubric, and intentionally wrong answers must be caught by the corresponding criteria; the paper’s error analysis checks the original text by hand, separately.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**去污染与泄漏边界**：The paper uses screening by the failures of several models, and it requires that a question depend on the original PDF; this controls difficulty and dependence on evidence, and it does not prove that training was decontaminated. The original PDFs come from real work and the questions have been published, so exposure in pretraining remains Unverified.

状态：待核实。

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

## Data format

**规模与口径**：100 questions, balanced across ten domains; the AA methods page records a 4,592-page PDF and 1,275 scoring criteria.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07 )

**任务类型**：Retrieval, comparison, calculation, summarization, cross-page coordination, and refusal when supporting information is absent; open answers.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**模态**：PDF原文；文本；图像；表格；图表

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**语言**：待核实

状态：待核实。

核验说明：The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**难度**：Every retained sample makes at least two frontier multimodal models commit a substantive error; samples are labeled on 11 ability axes and in a three-level system of ability, and no unified counts of easy, medium, and hard are provided.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**公开与隐藏划分**：The paper states that all 100 questions, together with the PDFs, prompts, rubrics, and labels, are public; on this access the HF data page returned 401. Public availability is recorded as the paper states it, and this record does not claim that the question bank was downloaded.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

## Evaluation

**指标**：Strict task pass rate (every rubric item holds) and average rubric score; the leaderboard uses the strict pass rate.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**评分方式**：Each criterion is scored independently as binary, and a task counts as a pass only when every criterion is passed; the original version uses Gemini 3.5 Flash as the judge.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**提示与运行设置**：The original version runs each model 5 times on each question, with no tools; the original PDF is passed through the provider’s native file input. AA instead uses the full OCR text and the page images, with the judge GPT-5.6 Luna at medium.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07 )

**官方复现入口**：https://github.com/surge-ai/gdp-pdf. The Inspect AI entry is src/gdp_pdf/task.py, with --epochs 5 and a Gemini 3.5 Flash judge. all_pass/mean is the primary leaderboard, and mean_criteria/mean retains partial credit.

Sources: [1](https://github.com/surge-ai/gdp-pdf) (accessed 2026-11-07 )

**可比性警告**：AA and Surge share the question set, but the PDF input and the judge differ; scores from the native PDF and from pre-parsed OCR cannot be exchanged directly.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

## Current status

**本次核验**：2026-11-07

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**数据及热度证据**：```json
{
  "version": "100-question public version"
  "trending": "A"
  "heat_evidence": "The AA v5 release text of 2026-10-27 continues to include GDP.pdf at a weight of 5%, and the current method page states 100 questions × 5 runs; the official Surge leaderboard shows new models at the same time. The two organizations are different implementations and are not treated as a check of one and the same score."
  "evidence_2026_h2": [
    {
      "url": "https://surgehq.ai/benchmarks/gdp-pdf"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
    }
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
    }
    {
      "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date."
    }
  ]
}
```

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 ) ; [2](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07 ) ; [3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) (accessed 2026-11-07 )

**论文与版本历史**：arXiv v1: 2026-07-13 16:44:07; v2: 07-14 16:57:18; v3: 07-15 16:47:22. The first release of the benchmark in April and the release of the paper in July should be kept separate.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**饱和程度**：The current leader on the Surge strict pass rate is 35.0%, second is 34.2%, and third is 33.2%; none is a perfect score. A high average rubric score cannot be used to infer that the strict task pass rate is already saturated.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**已知问题与局限**：AA and Surge share the question set, but the PDF input and the judge differ; scores from the native PDF and from pre-parsed OCR cannot be exchanged directly.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**后续与衍生**：GDP.pdf is not GDPval, and it is not GDP.xlsx: this entry records only professional PDF question answering and does not merge occupational deliverables or spreadsheet tasks.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**官方入口**：https://surgehq.ai/benchmarks/gdp-pdf

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**第三方入口**：待核实

状态：待核实。

核验说明：The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | GPT 6.1 Sol (Max reasoning) | 35 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 2 | GPT 6 Astra (Max reasoning) | 34.2 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 3 | Muse Wonder Full (Max reasoning) | 33.2 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 4 | Claude Sonnet 5.5 (Adaptive/Max) | 31.4 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 5 | Muse Wonder (Max reasoning) | 30.8 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 6 | GPT 5.6 Sol (Max reasoning) | 30.7 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 7 | Claude Opus 5.5 (Adaptive/Max) | 30.6 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 8 | Claude Fable 5 (Adaptive/Max) | 29.8 | Surge strict task pass rate (%) | Unverified (leaderboard update time) | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：AA and Surge share the question set, but the PDF inputs and the judges differ; scores from native PDF and from pre-parsed OCR cannot be exchanged directly. The update time written on the leaderboard itself: Unverified; the collection date is not the run date.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

## Contact

**公开联系邮箱**：suhaas@surgehq.ai

核验说明：The correspondence address explicitly published in the paper, for research contact only.

Sources: [1](https://arxiv.org/abs/2607.11192) (accessed 2026-11-07 )

**Issues或讨论入口**：https://github.com/surge-ai/gdp-pdf/issues

Sources: [1](https://github.com/surge-ai/gdp-pdf) (accessed 2026-11-07 )

**官方社交**：https://x.com/HelloSurgeAI

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**隐私政策**：https://surgehq.ai/privacy-policy

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

## Original files

**原始PDF**：https://arxiv.org/pdf/2607.11192

核验说明：Verified by reading the raw PDF bytes directly; not uploaded.

Sources: [1](https://arxiv.org/pdf/2607.11192) (accessed 2026-11-07 )

**PDF SHA-256**：e139828de98e24caee6ba7f749dd39e9c541ff16c7a6c91ddb18dcd5a8defda4

核验说明：Byte count of the original downloaded PDF, not the size displayed on the arXiv page.

Sources: [1](https://arxiv.org/pdf/2607.11192) (accessed 2026-11-07 )

**PDF字节数**：```json
223397
```

核验说明：Actual downloaded byte count; it does not mean the file was uploaded.

Sources: [1](https://arxiv.org/pdf/2607.11192) (accessed 2026-11-07 )

**文件夹**：待核实

状态：待核实。

核验说明：The listed materials that were opened have not been precisely verified; this is not the same as Not disclosed by the official source.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**其他官方文档**：```json
[
  {
    "type": "Official web page/paper opened"
    "url": "https://surgehq.ai/benchmarks/gdp-pdf"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://arxiv.org/abs/2607.11192"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
  }
  {
    "type": "Official web page/paper opened"
    "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
  }
]
```

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

**论文链接**：待核实

状态：待核实。

核验说明：The page for this group was built only locally and was not uploaded; no archive link is fabricated.

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

## Changelog

**及历史变更**：```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-07"
    Latest review
  }
]
```

Sources: [1](https://surgehq.ai/benchmarks/gdp-pdf) (accessed 2026-11-07 )

