# DistressBench

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

Verified to exist; a Chinese research snapshot; note: trending: B; Unverified marks are retained

DistressBench evaluates support in a psychological crisis and does not treat "no harmful content was produced" as a sufficient condition. 718 simulated English conversations cover 23 categories of crisis. 299 are single-turn and 419 are multi-turn. Clinicians and crisis counselors took part in the design. 6901 weighted atomic criteria measure seven dimensions, including empathy, recognition, de-escalation, and referral. The materials are not patient records or real clinical conversations. [1](https://labs.scale.com/leaderboard/distressbench) [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

There are 359 public items and 359 private items. The main leaderboard uses a majority vote of three judge models to decide whether a criterion is met, aggregated over three runs. The HF scoring code can be read publicly, but HF's "no system prompt" is inconsistent with the helpful-assistant setting in the paper and on the leaderboard page. The CC BY 4.0 wording and the evaluation-only wording also need clarification from the maintainer. Neither the leaderboard nor the long-term accompanying study is a trial of clinical effectiveness or proof of safety for deployment. [1](https://labs.scale.com/leaderboard/distressbench) [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

## Basic information

- **简称**：DistressBench [1](https://labs.scale.com/leaderboard/distressbench)

- **全称**：DistressBench [1](https://labs.scale.com/leaderboard/distressbench) 注：The official name is kept; the paper title is not fabricated as a full name.

- **基准版本**：v1 [2](https://arxiv.org/abs/2610.12758)

- **论文/报告版本**：arXiv:2610.12758v1（2026-10-08） [2](https://arxiv.org/abs/2610.12758)

- **发布日期**：2026-10-08 (the date marked on the first version of the paper PDF) [2](https://arxiv.org/abs/2610.12758)

- **主板块**：安全 [1](https://labs.scale.com/leaderboard/distressbench) 注：Benchmark Constitution editorial classification.

- **子领域**：生物与医学；心理健康 [1](https://labs.scale.com/leaderboard/distressbench)

- **许可证与限制**：The HF data card explicitly states CC BY 4.0. The paper and the leaderboard page also say evaluation use only, and LH has separate research-use terms. The two restriction wordings conflict. The maintainers should be asked to confirm before use or redistribution. [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [2](https://arxiv.org/abs/2610.12758) [1](https://labs.scale.com/leaderboard/distressbench)

- **论文/报告**：https://arxiv.org/abs/2610.12758 [2](https://arxiv.org/abs/2610.12758)

- **官方代码**：https://huggingface.co/datasets/ScaleAI/DistressBench/tree/main/code [3](https://huggingface.co/datasets/ScaleAI/DistressBench) 注：The scoring code and code/README are in the official HF data repository; a GitHub repository is not fabricated.

- **数据入口**：https://huggingface.co/datasets/ScaleAI/DistressBench [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

- **官方主页**：https://labs.scale.com/leaderboard/distressbench [1](https://labs.scale.com/leaderboard/distressbench)

- **报告标题**：DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models [2](https://arxiv.org/abs/2610.12758)

## Origin and maintenance

- **发起方**：Scale AI [2](https://arxiv.org/abs/2610.12758)

- **核心作者**：Drew Rein；Patrick Oathout；Vishal Kumar；Udari Madhushani Sehwag [2](https://arxiv.org/abs/2610.12758)

- **维护方**：Scale Labs [2](https://arxiv.org/abs/2610.12758)

**仍待核实**（不推断为未公开）：

- 合作方：The formal materials are not sufficient to confirm an independent research partner; tool providers, model vendors, and upstream repositories are not treated as partner institutions on that basis. [1](https://labs.scale.com/leaderboard/distressbench)
- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://labs.scale.com/leaderboard/distressbench)

## Design goals

- **核心能力**：Recognition, appropriate empathy, de-escalation, and referral to human assistance in psychological-crisis support, rather than measuring only refusal. [2](https://arxiv.org/abs/2610.12758)

- **相对已有评测的缺口**：Not producing harmful content is not the same as giving effective support; a single-turn binary refusal metric misses latent crises and failure to act after recognition. [2](https://arxiv.org/abs/2610.12758)

## Construction

- **题目来源**：Simulated dialogues written by licensed clinical personnel and crisis counselors; these are not patient chats or clinical records. [2](https://arxiv.org/abs/2610.12758)

- **出题与审核人员**：Licensed clinicians and crisis counselors; no information from real patients. [2](https://arxiv.org/abs/2610.12758)

- **审核流程**：Clinicians write the user prompt and the note; the model drafts the rubric and the reference answer, which clinicians then rewrite. Automatic checks and several layers of human review are applied. [2](https://arxiv.org/abs/2610.12758)

- **质量控制**：75 calibration tasks and 2908 clinical consensus judgments are used to select the judge panel, from 455 candidate panels; the selected panel has κ=0.732. The clinicians' Fleiss κ=0.640 is not the same kind of agreement statistic, and it cannot be used to declare that the machine outperforms clinicians. Multi-turn tasks have an additional coherence gate. [2](https://arxiv.org/abs/2610.12758)

- **防污染/运行完整性**：A stratified public/private split of 50/50; the private half is used to check for contamination. [2](https://arxiv.org/abs/2610.12758)

## Data format

- **规模**：718 dialogues, 23 subcategories, and 6901 weighted atomic criteria; 299 single-turn and 419 multi-turn (3–5 user turns). [2](https://arxiv.org/abs/2610.12758)

- **题型**：Replies in crisis dialogue, with the final assistant turn scored by a task-specific rubric. [2](https://arxiv.org/abs/2610.12758)

- **模态**：文本对话 [2](https://arxiv.org/abs/2610.12758)

- **语言覆盖**：English only; standards for aid resources are centered on the United States. [2](https://arxiv.org/abs/2610.12758)

- **难度与任务跨度**：23 types of simulated crisis, 299 single-turn and 419 multi-turn (3–5 user turns), covering 165 implicit signals; this is a stratification by scenario, not a scale of clinical risk or of difficulty. [2](https://arxiv.org/abs/2610.12758)

- **公开与隐藏划分**：359 public questions and 359 private questions; the main leaderboard is scoped to all 718 questions. [2](https://arxiv.org/abs/2610.12758)

## Evaluation

- **指标**：Weighted Rubric Score: the proportion of clinical-criterion weight satisfied on each question, as the mean of three runs. [2](https://arxiv.org/abs/2610.12758)

- **评分规则**：Opus 4.8, Llama 4 Maverick, and Gemini 3.1 Pro give independent binary judgments, and a majority vote is then taken; the final round is a weighted average, and an empty reply scores 0; the interval is from 10000 bootstrap draws. [2](https://arxiv.org/abs/2610.12758)

- **提示与运行配置**：The paper and the leaderboard page refer to a standard helpful-assistant system instruction and the endpoint's minimum temperature. The HF Usage Notes instead write no system prompt, a default output limit of 4096, and 8192/16384 in individual cases. The two protocols conflict. Reproduction must lock release_metadata.json, and they cannot be silently merged. [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [1](https://labs.scale.com/leaderboard/distressbench)

- **评分/运行脚本**：https://huggingface.co/datasets/ScaleAI/DistressBench/tree/main/code [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

- **可比性限制**：The paper and the leaderboard describe a standard helpful system, but the current HF release notes state no system prompt; release_metadata must be pinned before the result is reproduced. The main leaderboard, the public half set, and LH cannot be used one for another. [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

## Current status

- **核验日期**：2026-11-07 [1](https://labs.scale.com/leaderboard/distressbench)

- **现行版本与采用证据**：version：v1；heat_confidence：B；evidence_2026_h2：url：https://labs.scale.com/leaderboard/distressbench；date：2026-11-07；date_type：observed_on；note：The October 2026 paper and the current Scale leaderboard still compare frontier models. Heat B: mainly a single-organization evaluation, not general adoption across multiple organizations.；url：https://arxiv.org/abs/2610.12758；date：2026-11-07；date_type：observed_on；note：The October 2026 paper and the current Scale leaderboard still compare frontier models. Heat B: mainly a single-organization evaluation, not general adoption across multiple organizations. [1](https://labs.scale.com/leaderboard/distressbench) [2](https://arxiv.org/abs/2610.12758) 注：The October 2026 paper and the current Scale leaderboard still compare frontier models. Heat B: mainly a single-organization evaluation, not general adoption across multiple organizations.

- **更新与修订**：arXiv v1 and the HF public release card for 359 questions were read; the paper’s experiment on 25 models and the expanded model list on the live web page must be recorded separately. A ranking in the old paper cannot be treated as the latest leaderboard. [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [1](https://labs.scale.com/leaderboard/distressbench)

- **饱和度判断**：A highest weighted satisfaction rate of about 88.4% on the main leaderboard does not equal passing the full rubric or clinical safety; a high score does not authorize deployment of a mental-health product. [2](https://arxiv.org/abs/2610.12758)

- **已知问题与证据边界**：The private 359 questions are used for a contamination check; the public 359 questions can no longer guarantee that future training has not used them. The final-round scoring in the paper conflicts with the HF accounting that uses no system prompt, and CC BY 4.0 on the dataset card conflicts with the evaluation-only narrative. LLM drafts were substantially revised by clinicians, and it cannot be said that there was no model assistance at all. [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [1](https://labs.scale.com/leaderboard/distressbench)

- **关联与衍生关系**：DistressBench-LH is an appendix of 20 long-duration red-team items, and it is not included in this main leaderboard. [2](https://arxiv.org/abs/2610.12758)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://labs.scale.com/leaderboard/distressbench)

- **官方榜/正式委托榜**：https://labs.scale.com/leaderboard/distressbench [1](https://labs.scale.com/leaderboard/distressbench)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | muse-spark-1.2 | 88.39 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 5 | muse-glimmer-30b | 80.57 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 6 | deepseek-v4.1-flash | 79.78 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 7 | inkling | 78.47 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 8 | qwen3.8-max | 77.64 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |

> muse-spark-1.2：ci95_halfwidth：0.93；rank_type：Web-page display position does not equal a statistical band [1](https://labs.scale.com/leaderboard/distressbench)

> muse-glimmer-30b：ci95_halfwidth：0.96；rank_type：Web-page display position does not equal a statistical band [1](https://labs.scale.com/leaderboard/distressbench)

> deepseek-v4.1-flash：ci95_halfwidth：1.01；rank_type：Web-page display position does not equal a statistical band [1](https://labs.scale.com/leaderboard/distressbench)

> inkling：ci95_halfwidth：1.06；rank_type：Web-page display position does not equal a statistical band [1](https://labs.scale.com/leaderboard/distressbench)

> qwen3.8-max：ci95_halfwidth：1.03；rank_type：Web-page display position does not equal a statistical band [1](https://labs.scale.com/leaderboard/distressbench)


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：In the dynamic table on the official website, some model names and scores cannot be paired in full, and only displayed entries that can be matched reliably are recorded; the serial numbers on the leaderboard page and the statistical bands in the paper are not the same basis. The extended list on the web page goes beyond the 25 models in the paper, and the exact date on which the page was updated has not been verified precisely. [1](https://labs.scale.com/leaderboard/distressbench)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [1](https://labs.scale.com/leaderboard/distressbench)

## Contact

- **公开联系邮箱**：drew.rein@scale.com [2](https://arxiv.org/abs/2610.12758)

- **官方社交**：https://x.com/scale_ai [4](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：The public organization account of the publishing organization Scale AI; it is not a channel for crisis support or medical help.

- **隐私政策**：https://scale.com/legal/privacy [4](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：The organizational privacy policy pointed to by the footer of the official website of the publishing organization; a separate benchmark-specific policy is not inferred.

**仍待核实**（不推断为未公开）：

- 公开问题追踪：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://labs.scale.com/leaderboard/distressbench)

## Original files

- **原始PDF**：https://arxiv.org/pdf/2610.12758 [5](https://arxiv.org/pdf/2610.12758)

- **SHA-256**：7f2a98944fd44c993a37758dfd157b672e9025cc3d10933fa5b83f368f1cf900 [5](https://arxiv.org/pdf/2610.12758) 注：Byte count of the PDF actually downloaded. It is not copied from an external web page.

- **PDF字节数**：610907 [5](https://arxiv.org/pdf/2610.12758) 注：Downloaded byte count; not uploaded.

- **其他正式文档**：type：Official web-page methods and leaderboard (not a PDF)；url：https://labs.scale.com/leaderboard/distressbench [1](https://labs.scale.com/leaderboard/distressbench)

- **中的论文副本**：待核实 [1](https://labs.scale.com/leaderboard/distressbench)

**仍待核实**（不推断为未公开）：

- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://labs.scale.com/leaderboard/distressbench)

## Changelog

- date：2026-11-07；timezone：；change：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://labs.scale.com/leaderboard/distressbench)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
