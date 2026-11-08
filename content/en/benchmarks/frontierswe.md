# FrontierSWE v2

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

This is an engineering evaluation on the scale of 20 hours. The 34 tasks cover implementation, performance, scientific computing, vision, and AI research at the same time. The important changes are not only added questions. They also include independent verifiers, reproducible proxy metrics for performance, and the Proximus harness, which encourages work to continue.

Latest review

## Basic information

**简称**：FrontierSWE v2

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**全称**：FrontierSWE

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**基准版本**：V2

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**论文版本**：A web technical report dated 2026-09-02; there is no arXiv version number from which this can be filled in.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**发布日期**：2026-09-02 (date of the official V2 release article)

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**主板块**：代码

核验说明：Benchmark Constitution editorial filing. It is not an official classification.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**领域标签**：代码

核验说明：编辑标签

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**许可证与授权边界**：The README states only that the tasks and the test harness are for evaluation use, and it requires upstream attribution to be checked task by task; a unified open-source license is Unverified.

状态：待核实。

核验说明：A request for the root LICENSE returns 404; an MIT/Apache license cannot be inferred from the public repository.

Sources: [1](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 )

**论文或技术报告**：https://www.frontierswe.com/blog/v2

核验说明：An official technical release article; a blog post is not presented as an arXiv paper.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**官方代码**：https://github.com/Proximal-Labs/frontier-swe-v2

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**数据地址**：https://github.com/Proximal-Labs/frontier-swe-v2

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**官方主页**：https://www.frontierswe.com/

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**论文题名**：FrontierSWE v2 (official technical release note; the title cited by the README is FrontierSWE v2: Testing Coding Agents at the Frontier of Software Engineering)

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 ) ; [2](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 )

## Origin and maintenance

**发起方**：Proximal team

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**协作与机构边界**：Work was done with external contributors. The acknowledgments list Bilal Bakht Ahmad and Ayush Nangia as independent contributors, and Animesh Sinha and Bhuvanesh Sridharan as BayesMech.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**作者**：Rishyanth Kondra；Sanket Mhatre；Akshit Kumar；Evan Chu；Bilal Bakht Ahmad；Ayush Nangia；Rajan Agarwal；Arpan Dasgupta；Animesh Sinha；Bhuvanesh Sridharan；Krupa Dave；Brendan Graham；Guanyu Song；Anirudh Rahul；Wei Hern Lim；Abishek Thangamuthu；Ramneet Singh；Danna Liu；Navid Pour；Calvin Chen；Justus Mattern

Sources: [1](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**维护方**：Proximal-Labs / Proximal team

Sources: [1](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**资助方**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

## Design goals

**测量能力**：Measures software-engineering ability at the edge of human ability, covering implementation of AI research, optimization, scientific computing, and visual reasoning.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**相对既有评测的缺口**：Aimed at engineering and scientific research on the scale of 20 hours, and correcting v1 problems such as models submitting too early, timing noise on a shared host, and a tester that can be tampered with; it measures the functionality and performance finally achieved inside a fixed long time budget.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

## Construction

**题目来源**：v2 adds 21 items and retires 4 tasks from v1, for 34 items in total; they come from real technical settings such as compiler rewriting, database compatibility, GPU inference optimization, weather prediction, and MEG decoding.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 ) ; [2](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 )

**出题与研究背景**：The Proximal core engineering team and external contributors; Kondra, Mhatre, and Kumar are listed as co-leads, and individual biographies are not inferred.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**审核流程**：Every task goes through QA again; self-check feedback that is monotonically related to the final score is provided; after a run, a review panel inspects the full trajectory, flags suspicious behavior, and sets a trial to zero once a violation is confirmed.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**质量控制**：A fixed image, dual-container isolation of the proxy and a clean verifier, execution as non-root, and scoring assets that are private to root; implementation tasks use structural mutation testing, and performance tasks instead use a fixed instruction count weighted by microarchitecture, in order to make results more reproducible.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**去污染与泄漏边界**：Anti-cheating measures include hidden variants, an independent verifier, and review of trajectories. The task content is public, and these anti-cheating measures are not proof of pretraining decontamination. The extent of training contamination is Unverified.

状态：待核实。

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

## Data format

**规模与口径**：34任务

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**任务类型**：Long-horizon software-engineering tasks, including compilers, scientific computing, model optimization, and visual-interaction engineering.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**模态**：代码；文本；视觉环境

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**语言**：The tasks cover technology stacks including Zig, Rust, Go, Free Pascal, Swift, Haskell, CUDA, and Python; the requirements of a task are defined item by item, and a single programming-language basis is not used.

Sources: [1](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**难度**：20-hour runtime budget per task.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**公开与隐藏划分**：instruction.md, task.toml, the environment, and the reference solution are public for 34 tasks. Final verification uses a clean container, together with partly hidden structural variants and out-of-domain data. This is not a standard percentage split into train and test.

Sources: [1](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

## Evaluation

**指标**：mean@5; the range from worst@5 to best@5, and the average cost and time, are also shown.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**评分方式**：Each model is run 5 times on each task; mean@5 is reported across 34 tasks.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**提示与运行设置**：The official leaderboard shows the proximus harness; 20 hours per trial.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**官方复现入口**：https://github.com/Proximal-Labs/frontier-swe-v2

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**可比性警告**：Different harnesses, GPUs, and inference budgets must be kept on separate tracks; historical dominance scores in the Kimi release post cannot be mixed directly with the current V2 mean@5 ranking.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

## Current status

**本次核验**：2026-11-07

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**数据及热度证据**：```json
{
  "version": "V2"
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
      "url": "https://www.frontierswe.com/"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "organization": "Official maintainer"
      "note": "The current official methods and leaderboard have been opened; the observation date is not presented as the publication date."
    }
  ]
}
```

Sources: [1](https://epoch.ai/data/eci-documentation/data) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/) (accessed 2026-11-07 )

**论文与版本历史**：The V2 release post is dated 2026-09-02; the README states that task content and scoring may still be updated, so the repository commit and the image digest should be pinned.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 ) ; [2](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 )

**饱和程度**：The highest mean@5 on the current homepage is 65.5%, short of a perfect score; the launch-day high of 56.29% is a historical result and cannot be mixed in as the current leaderboard leader.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**已知问题与局限**：The release text records incidents of reward-hacking and of reading evaluation assets beyond what was authorized, and the related trials that were confirmed were set to zero; although the proxy metrics of performance can be reproduced, they are still not the true elapsed time on every kind of hardware; the Proximus prompt makes the model aware that it is being evaluated.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

**后续与衍生**：V2 replaces v1 as the main leaderboard. Four items are retired: PCQM4Mv2 Molecular Gap Prediction, Pyright optimization, Revideo optimization, and Dependent Type Checker.

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**官方入口**：https://www.frontierswe.com/

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**第三方入口**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | GPT-6 Astra / proximus | 65.5 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 2 | Claude Opus 5.5 / proximus | 62.3 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 3 | Gemini 4 Carbon / proximus | 61.2 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 4 | GLM-5.3 / proximus | 30.2 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 5 | Grok 4.7 / proximus | 29.5 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 6 | Kimi K3 / proximus | 25.9 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 7 | Muse Spark 1.3 / proximus | 25.8 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 8 | Qwen3.8-Max-0902 / proximus | 17.8 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 9 | DeepSeek V4 Flash Vision Exp / proximus | 14.8 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 10 | Inkling / proximus | 4.1 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：The top 10 on the homepage were opened again. mean@5 is the mean of 5 trials on each of 34 tasks. The worst@5–best@5 whiskers are not a 95% confidence interval. The official site does not mark when the leaderboard table was updated, and that time remains Unverified. The release text of 2026-09-02 is not the date of the current leaderboard.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 ) ; [2](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 )

## Contact

**公开联系邮箱**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**Issues或讨论入口**：https://github.com/Proximal-Labs/frontier-swe-v2/issues

Sources: [1](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 )

**官方社交**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**隐私政策**：https://proximal.ai/privacy

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

## Original files

**原始PDF**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**PDF SHA-256**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**PDF字节数**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**文件夹**：待核实

状态：待核实。

核验说明：The listed official materials have been checked, but exact verification of this field is not yet complete; this does not indicate Not disclosed by the official source.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

**其他官方文档**：```json
[
  {
    "type": "V2 technical report"
    "url": "https://www.frontierswe.com/blog/v2"
  }
  {
    "type": "Public tasks and reproduction notes"
    "url": "https://github.com/Proximal-Labs/frontier-swe-v2"
  }
]
```

Sources: [1](https://www.frontierswe.com/blog/v2) (accessed 2026-11-07 ) ; [2](https://github.com/Proximal-Labs/frontier-swe-v2) (accessed 2026-11-07 )

**论文链接**：待核实

状态：待核实。

核验说明：This group only created a local research entry and did not upload.

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

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

Sources: [1](https://www.frontierswe.com/) (accessed 2026-11-07 )

