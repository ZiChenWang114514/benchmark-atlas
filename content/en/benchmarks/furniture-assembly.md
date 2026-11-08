# Furniture Assembly Benchmark

> Benchmark Constitution | In-depth verification: 2026-11-07. The access date follows the fixed collection date, and run times are listed separately. Unverified is not the same as Not disclosed; conflicting sources are retained side by side.

The model has to connect a real assembly photograph with the PDF manual, locate the step that produced the error, and describe the error. It is not a task of actual assembly by a robot; the 60 photographs come from only three kinds of furniture, and any extension to physical reasoning in general should stay restrained.

Latest review

## Basic information

**简称**：Furniture Assembly Benchmark

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**全称**：Furniture Assembly Benchmark

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**基准版本**：The run CSV contains 1.0.0 and 1.0.1; the leaderboard is limited to the 1.0.0 track

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**论文版本**：Official research report on the web (recorded separately from the methods page, which is updated continuously)

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**发布日期**：2026-09-23 (datePublished of the officially published research report; not used to assert the first date on which every task asset went online)

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07)

**主板块**：多模态

核验说明：Filed under one main section. That filing does not limit coverage of other disciplines.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**领域标签**：空间推理

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**许可证与授权边界**：The JSON-LD of the official research report declares CC-BY-4.0; this does not cover the underlying IKEA images and instructions. The official statement explicitly does not distribute or sell that copyrighted material, and a single license for redistributing the question bank is Unverified.

状态：待核实。

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**论文或技术报告**：https://epoch.ai/publications/furniture-assembly

核验说明：An official research report on the web; an independent arXiv paper or PDF has not been located.

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07)

**官方代码**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**数据地址**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**官方主页**：https://epoch.ai/benchmarks/furniture-assembly

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**论文题名**：AI has improved significantly at reasoning about IKEA furniture assembly

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07)

## Origin and maintenance

**发起方**：Epoch AI

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**协作与机构边界**：The research is independent of IKEA; use of the products and the manuals is not taken to imply a collaboration.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**作者**：Aiden Ament；Greg Burnham

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07)

**维护方**：Epoch AI

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**资助方**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Design goals

**测量能力**：Connects real assembly photographs with technical diagrams, identifies errors, and locates the step that produced each error.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**相对既有评测的缺口**：Measures spatial and multi-step reasoning in physical construction, rather than abstract visual questions alone.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Construction

**题目来源**：Researchers bought three pieces of IKEA furniture and filmed the assembly, deliberately introducing visible errors after which assembly could continue.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**出题与研究背景**：The Epoch AI research report is signed by Aiden Ament and Greg Burnham; the original tasks were photographed after the researchers actually bought and assembled IKEA furniture, and they are not data from a robot carrying out the task.

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**审核流程**：For samples that contain errors, the steps are checked first, and GPT-5.6 Sol then reviews the error description leniently.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**质量控制**：A correctly assembled item that is correctly identified passes directly; a sample with an error must have that error correctly located and described approximately.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**去污染与泄漏边界**：The official source does not distribute or sell the underlying copyrighted images and manuals; complete openness of the data is not inferred from this.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Data format

**规模与口径**：60 photographs: Ställ shoe cabinet 14, Tonstad bed frame 25, Gullaberg chest of drawers 21.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**任务类型**：Judge whether an installation is correct; identify erroneous steps and their causes; when it is correct, state the next step.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**模态**：照片；PDF assembly manual；文本

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**语言**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**难度**：Three products are chosen by complexity; an error can occur at an earlier step rather than at the last step.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**公开与隐藏划分**：The official statement explicitly does not distribute or sell the underlying copyrighted photographs and IKEA instructions. Publishing the methods and the results is not the same as publishing the underlying question bank; this entry is not read as a standard public train/test split.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Evaluation

**指标**：Accuracy on 60 photos, with error bars of ± standard error.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**评分方式**：For incorrect questions, the steps are matched first and an LLM then judges the description; the human baseline judges only the steps, and that task is slightly easier.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**提示与运行设置**：The product name, the steps completed so far, photographs, a PDF manual, zoom, and Python are provided; an 80-step budget; the highest supported reasoning effort.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**官方复现入口**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**可比性警告**：The human 84% best combination cannot be called one person's score on the full set; the run CSV has different task versions and must be split into tracks.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Current status

**本次核验**：2026-11-07

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**数据及热度证据**：```json
{
 "version": "Latest CSV run: see 1.0.1"
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/benchmarks.csv"
 "date": "2026-11-06"
 "note": "Kimi K3.1 Pro, run on 2026-11-06 20:34:34, id UNKjzcpUBaxGsrr7zZZZWC; evidence of a continuing live run."
 }
 ]
}
```

Sources: [1](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-07)

**论文与版本历史**：The official web research report was released on 2026-09-23; the release text says that humans had not yet been tested, while the current methods page adds a human experiment from September 2026, so the two are cited separately as the historical release text and the page that is kept up to date.

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**饱和程度**：The highest score at 1.0.0 in the CSV is 0.833333 (Claude Opus 5.5). The highest score at 1.0.1 is 0.791667 (GPT-6.1 Terra). Versions are kept on separate tracks. 60 photographs and three products cannot support a generalization that spatial reasoning as a whole is already saturated.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-07)

**已知问题与局限**：The original release text had not yet measured human performance; the current method page has added a baseline of 15 volunteers, with a mean of 63% and 84% for the combination of the best person on each product, and the humans need only locate the step and do not have to describe the error. The current method page is given priority, and the combined 84% cannot be treated as one person's score on the whole set.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07)

**后续与衍生**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Leaderboard snapshot

**快照日期**：2026-11-07

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**官方入口**：https://epoch.ai/benchmarks/furniture-assembly

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**第三方入口**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 1.0.0 | 1 | Claude Opus 5.5 (max) | 0.8333333333333334 | mean_score (0–1) | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 2 | GPT-6.1 Sol (max) | 0.8 | mean_score (0–1) | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 3 | GPT-6 Astra (max) | 0.8 | mean_score (0–1) | 2026-09-11 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 4 | Claude Sonnet 5.5 (max) | 0.75 | mean_score (0–1) | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 5 | Claude Fable 5.1 (max) | 0.7 | mean_score (0–1) | 2026-09-11 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 1 | GPT-6.1 Terra (max) | 0.7916666666666666 | mean_score (0–1) | 2026-10-27 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 2 | Gemini 4 Argon (high) | 0.725 | mean_score (0–1) | 2026-10-14 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 3 | Kimi K3.1 Pro (Together, max) | 0.5583333333333333 | mean_score (0–1) | 2026-11-06 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 4 | Muse Wonder (max) | 0.5416666666666666 | mean_score (0–1) | 2026-10-16 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 5 | Mistral Large 4 (high) | 0.3083333333333333 | mean_score (0–1) | 2026-11-02 | [原始来源](https://epoch.ai/data/benchmarks.csv) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：Records of successful runs are refreshed, and the top 5 of 1.0.0 and the top 5 of 1.0.1 are listed separately; rank starts again inside each version, and the two versions must not be mixed into one overall leaderboard. The day a run started is not the time the leaderboard was updated.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/data/benchmarks.csv) (accessed 2026-11-07)

## Contact

**公开联系邮箱**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**Issues或讨论入口**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**官方社交**：https://x.com/EpochAIResearch

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**隐私政策**：https://epoch.ai/privacy

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

## Original files

**原始PDF**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**PDF SHA-256**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**PDF字节数**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**文件夹**：待核实

状态：待核实。

核验说明：Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**其他官方文档**：```json
[
 {
 "type": "Published research report"
 "url": "https://epoch.ai/publications/furniture-assembly"
 }
 {
 "type": "Continuously updated methods and human baselines"
 "url": "https://epoch.ai/benchmarks/furniture-assembly"
 }
]
```

Sources: [1](https://epoch.ai/publications/furniture-assembly) (accessed 2026-11-07); [2](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

**论文链接**：待核实

状态：待核实。

核验说明：This group is local research only and was not uploaded.

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)

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

Sources: [1](https://epoch.ai/benchmarks/furniture-assembly) (accessed 2026-11-07)
