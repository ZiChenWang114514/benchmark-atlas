# FullStackBench

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

“FullStack” means an executable-code evaluation spanning development domains and 16 programming languages. It does not equal a full-website agent. Official materials on data licensing found in this pass conflict with one another, and the question count in the paper and the row count of the current HF bilingual configuration must be recorded under separate scopes.

Latest review

## Basic information

**简称**：FullStackBench

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**全称**：FullStackBench

核验说明：The official name is retained, and the paper title is not automatically expanded into a full name.

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**基准版本**：A public snapshot of 3,374 questions; the data version number is Unverified

状态：待核实。

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**论文版本**：arXiv v6

核验说明：A paper revision is not the same as a dataset version.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**发布日期**：2024-12-01 01:58:42

核验说明：The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**主板块**：代码

核验说明：Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**领域标签**：Full-stack code generation

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**许可证与授权边界**：The root LICENSE and the README for the code state Apache-2.0; the data license has an official conflict: the HF YAML is Apache-2.0, but the body of the same card and the badge in the repository README both write CC-BY-SA-4.0. The data license is Unverified. The maintainers should be asked to clarify it before reuse, and it cannot be treated directly as Apache.

状态：待核实。

Sources: [1](https://github.com/bytedance/FullStackBench/blob/HEAD/LICENSE) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 ) ; [3](https://huggingface.co/datasets/ByteDance/FullStackBench/blob/main/README.md) (accessed 2026-11-07 )

**论文或技术报告**：https://arxiv.org/abs/2412.00535

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**官方代码**：https://github.com/bytedance/FullStackBench

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**数据地址**：https://huggingface.co/datasets/ByteDance/FullStackBench

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**官方主页**：https://github.com/bytedance/FullStackBench

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**论文题名**：FullStack Bench: Evaluating LLMs as Full Stack Coders

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Origin and maintenance

**发起方**：ByteDance / Seed Foundation Code Team

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**协作与机构边界**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**作者**：Bytedance, Seed Foundation Code Team

核验说明：The v6 title page credits a team; the contribution list is in paper §8. The older BibTeX list of individual authors is kept separate from the v6 team credit, and the colon pseudo-authors from the old automatic parse are not retained.

Sources: [1](https://arxiv.org/abs/2412.00535v6) (accessed 2026-11-07 )

**维护方**：ByteDance FullStackBench team

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**资助方**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Design goals

**测量能力**：Practical ability in code development and library use across languages and application domains.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**相对既有评测的缺口**：Simple algorithm problems, and multilingual problems translated from Python, cannot adequately cover full-stack settings, external dependencies, and the complexity of real development.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Construction

**题目来源**：Code is sampled from GitHub, from documentation and books about code, and from XLCoST. An LLM and people then produce the instructions, the tests, and the reference solutions. People who program in each domain, including an internal team for data engineering, are also invited to write questions for that domain. The balance across domains refers to 500,000 questions on StackOverflow.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**出题与研究背景**：ByteDance research team on code models and execution sandboxes.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**审核流程**：Each item is reviewed for difficulty, ambiguity, and solvability, and annotators exchange data for cross-revision; disagreements are settled by consensus or by a senior annotator. Votes from six models assist difficulty assignment and sample screening.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**质量控制**：Each question is paired with reference code and executable unit tests; the paper has 15,168 tests in total, an average of 4.5 per question, and covers different error types. Runs use SandboxFusion with the language and dependency environment fixed.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**去污染与泄漏边界**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Data format

**规模与口径**：The scope of paper v6 is 3,374 questions and 15,168 unit tests. The current HF en/test and zh/test each have 1,687 rows, which is 3,374 rows of language configuration. Both the scope in the paper and the scope of the data now released are kept. The summed row count is not asserted to be 3,374 distinct original questions.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://huggingface.co/datasets/ByteDance/FullStackBench/blob/main/README.md) (accessed 2026-11-07 )

**任务类型**：Code generation. The record includes content, canonical_solution, id, and labels, together with test.asset/test.code. labels contains category, difficulty, programming_language, execution_language, fewshot, is_lctx, and locale.

Sources: [1](https://huggingface.co/datasets/ByteDance/FullStackBench/raw/main/README.md) (accessed 2026-11-07 )

**模态**：文本；代码

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**语言**：The natural-language settings are en and zh; programming languages cover 16 (official README). Row counts for the two language settings cannot be treated as counts of non-overlapping original questions.

Sources: [1](https://huggingface.co/datasets/ByteDance/FullStackBench/raw/main/README.md) (accessed 2026-11-07 )

**难度**：Paper v6, Table 1: Easy 1,466, Medium 1,184, Hard 724. In the vote of six models, items that only 1 model answered correctly are listed as hard, items that 5 or 6 models answered correctly are listed as easy, and the rest are medium. This distribution is the paper's accounting, and it is not inferred that a separate HF language configuration has the same counts.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**公开与隐藏划分**：The official HF card publishes two configs, en and zh, each with only a test split and 1,687 rows; they contain canonical_solution and test fields, and they are not a service that hides the answers.

Sources: [1](https://huggingface.co/datasets/ByteDance/FullStackBench/raw/main/README.md) (accessed 2026-11-07 )

## Evaluation

**指标**：pass@1 / the functional-correctness rate of a single attempt.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**评分方式**：SandboxFusion is used to execute the generated program in the corresponding language environment and check the unit tests.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**提示与运行设置**：For open-source models, the paper sets temperature=0 and max_completion_tokens=2048, with the remaining settings left at their defaults. Code is extracted through SandboxFusion, and the unit tests are executed there. A third-party report should be listed on its own if its budget or its language configuration differs.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**官方复现入口**：https://github.com/bytedance/FullStackBench. It uses the SandboxFusion service and src/main.py. The example image in the README is fixed as server-20241204.

Sources: [1](https://raw.githubusercontent.com/bytedance/FullStackBench/main/README.md) (accessed 2026-11-07 )

**可比性警告**：Differences in language and domain coverage and in the execution environment affect results; the name does not mean a UI agent that actually builds or launches a complete website.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

## Current status

**本次核验**：2026-11-07

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**数据及热度证据**：```json
{
  "version": "A public snapshot of 3,374 questions; the data version number is Unverified"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1"
      "date": "2026-09-23"
      "note": "Hunyuan-A13B §4.1/§4.2 and Tables 2–4 actually report FullStackBench; CRUX-I/O is kept as the same CRUXEval entry and is not split into a separate count."
    }
  ]
}
```

状态：待核实。

核验说明：Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

Sources: [1](https://arxiv.org/html/2609.27284v1) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**论文与版本历史**：Submission history From: Siyao Liu [ view email ] [v1] 2024-12-01 01:58:42 (10,754 KB) [v2] 2024-12-04 01:55:24 (11,370 KB) [v3] 2024-12-10 02:31:54 (7,770 KB) [v4] 2024-12-13 01:59:55 (7,769 KB) [v5] 2024-12-20 23:58:59 (7,770 KB) [v6] 2025-05-12 19:24:14 (7,770 KB)

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**饱和程度**：Table 2 of the v6 paper was reread, and the historical high is OpenAI o1-preview at 65.62%; the README on the official website still links a static figure of the results, and the historical results in the paper are not treated as the live upper bound for 2026.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 ) ; [2](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**已知问题与局限**：Public tests and tasks may leak into later training; coverage of the sources of the questions is not equivalent to proof of no contamination.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**后续与衍生**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**官方入口**：https://github.com/bytedance/FullStackBench

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**第三方入口**：待核实

状态：待核实。

核验说明：Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| Vendor self-report; configuration is not guaranteed to match the original paper | — | Hunyuan-A13B slow-thinking | 67.8 | FullStackBench (%) | 2026-09-23 | [原始来源](https://arxiv.org/html/2609.27284v1) |
| Vendor self-report; configuration is not guaranteed to match the original paper | — | Hunyuan-A13B fast-thinking | 58.3 | FullStackBench (%) | 2026-09-23 | [原始来源](https://arxiv.org/html/2609.27284v1) |
| Original paper v6 Table 2 historical baseline | 1 | OpenAI o1-preview | 65.62 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |
| Original paper v6 Table 2 historical baseline | 2 | OpenAI o1-mini | 64.73 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |
| Original paper v6 Table 2 historical baseline | 3 | Claude-3.5-Sonnet | 62.57 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |
| Original paper v6 Table 2 historical baseline | 4 | GPT-4o-0806 | 61.77 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

核验说明：The original-paper track was refreshed; the two Hunyuan entries inherit the previously verified H2 report, that report was not reread, and this is not presented as a new verification.

**覆盖说明**：The official repository shows only static figures of results from the paper. A dynamic unified leaderboard was not obtained. The historical baseline of v6 Table 2, reread for this update, is newly added. Self-reports inherited from the Hunyuan report are listed on their own and cannot be ranked on the track of the original paper. The conflict over data licensing, and the current scope of HF row counts, are given under basic information.

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 ) ; [2](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Contact

**公开联系邮箱**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**Issues或讨论入口**：https://github.com/bytedance/FullStackBench/issues

核验说明：Public repository feedback entry point; no question was sent.

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

**官方社交**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

**隐私政策**：待核实

状态：待核实。

核验说明：The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2412.00535) (accessed 2026-11-07 )

## Original files

**原始PDF**：https://arxiv.org/pdf/2412.00535

核验说明：Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

Sources: [1](https://arxiv.org/pdf/2412.00535) (accessed 2026-11-07 )

**PDF SHA-256**：d68951598d6b201b93b57ea71052944f28bacd77bd3b6f2c6acb2d46b090fb98

核验说明：Byte count of the original downloaded PDF, not the size displayed on the arXiv page.

Sources: [1](https://arxiv.org/pdf/2412.00535) (accessed 2026-11-07 )

**PDF字节数**：```json
4251352
```

核验说明：Actual downloaded byte count; it does not mean the file was uploaded.

Sources: [1](https://arxiv.org/pdf/2412.00535) (accessed 2026-11-07 )

**文件夹**：```json
{
  "id": "1vAewLYiHS2Ta9LHgZgpCyiffgsHzztL0"
  "webViewLink": "
}
```

Sources: [1](

**其他官方文档**：```json
[
  {
    "type": "Chinese-language introductory Google Doc"
    "id": "1ZQmcPus9I5v9JKGpJDp1aqzVsUk1yzCaXcFVMj-p5Kc"
    "webViewLink": "
  }
]
```

核验说明：The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 ) ; [2](

**论文链接**：```json
{
  "id": "1tq-_KLfUzmLu_gHbuJ4aVoMgkXggG8an"
  "webViewLink": "
}
```

Sources: [1](

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
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-07"
    Latest review
  }
]
```

Sources: [1](https://github.com/bytedance/FullStackBench) (accessed 2026-11-07 )

