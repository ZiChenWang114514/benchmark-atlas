# DROP

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

an in-depth entry; items explicitly marked Unverified are kept

DROP (Discrete Reasoning Over Paragraphs) is a reading-comprehension dataset for numerical and discrete reasoning. The model finds evidence in a Wikipedia paragraph and completes counting, addition and subtraction, comparison, and multi-span answers, rather than only extracting a contiguous span of text. The original paper has 96567 questions, split by paragraph into 77409 for training, 9536 for development, and 9622 for hidden test, so that the same paragraph does not cross splits. [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) [4](https://registry.opendata.aws/allenai-drop/)

The paper, the official scoring script, the notes on the historical repository migration, the HF card, and the AWS registry entry were reread. The data-mirror counts and the license scope differ. The official hidden-test leaderboard currently returns an error, and a live SOTA cannot be claimed from a search cache. To avoid mixing vendor self-reported results into the official leaderboard, what follows falls back explicitly to the historical baselines in the original paper and marks them as not the current ranking. [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) [4](https://registry.opendata.aws/allenai-drop/)

## Basic information

- **简称**：DROP [2](https://arxiv.org/abs/1903.00161)

- **全称**：Discrete Reasoning Over Paragraphs [2](https://arxiv.org/abs/1903.00161)

- **基准版本**：A public dataset from 2019; the download-package version is not fixed [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161)

- **论文/报告版本**：arXiv v2 [2](https://arxiv.org/abs/1903.00161)

- **发布日期**：2019-03-01 (date of the first arXiv draft; not a statement of an independent dataset first release). [2](https://arxiv.org/abs/1903.00161)

- **主板块**：推理 [1](https://allennlp.org/drop)

- **子领域**：Discrete-reasoning reading comprehension [2](https://arxiv.org/abs/1903.00161)

- **许可证与限制**：The evaluation software allennlp-models is Apache-2.0; the HF ucinlp/drop mirror is marked CC BY-SA 4.0, and the official AWS open-data registry writes only CC BY. The data-license wording differs, and the Apache license of the software cannot be applied to the data. [5](https://github.com/allenai/allennlp-models/blob/main/LICENSE) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) [4](https://registry.opendata.aws/allenai-drop/)

- **论文/报告**：https://arxiv.org/abs/1903.00161 [2](https://arxiv.org/abs/1903.00161)

- **官方代码**：https://github.com/allenai/allennlp-models [6](https://raw.githubusercontent.com/allenai/allennlp-reading-comprehension/master/README.md) [7](https://raw.githubusercontent.com/allenai/allennlp-models/main/allennlp_models/rc/tools/drop.py)

- **数据入口**：https://huggingface.co/datasets/ucinlp/drop [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) 注：Corrects the fact that allennlp.org/drop now redirects to the old scoring script and can no longer serve as the data-download page.

- **官方主页**：https://allennlp.org/drop [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161)

- **报告标题**：DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs [2](https://arxiv.org/abs/1903.00161)

## Origin and maintenance

- **发起方**：Allen Institute for AI, University of California Irvine, University of Washington, and Peking University (affiliations signed in the paper). [2](https://arxiv.org/abs/1903.00161)

- **合作方**：University of California, Irvine；Peking University；University of Washington [2](https://arxiv.org/abs/1903.00161)

- **核心作者**：Dua, Dheeru；Wang, Yizhong；Dasigi, Pradeep；Stanovsky, Gabriel；Singh, Sameer；Gardner, Matt [2](https://arxiv.org/abs/1903.00161)

- **维护方**：The team of the Allen Institute for Artificial Intelligence / AllenNLP (the original paper and the release channel); no assurance is given about continued maintenance at present. [2](https://arxiv.org/abs/1903.00161) [8](https://github.com/allenai/allennlp-reading-comprehension)

- **资助方**：Google Cloud provides partial credits for beaker.org compute (paper acknowledgments); this is not used to infer that the entire project is funded that way. [2](https://arxiv.org/abs/1903.00161)

## Design goals

- **核心能力**：Measures the ability of the model to add and subtract, count, compare, sort, and extract answers from paragraph evidence. [2](https://arxiv.org/abs/1903.00161)

- **相对已有评测的缺口**：Reading comprehension that only locates an answer span is not sufficient to test discrete operations and integration of multiple facts. [2](https://arxiv.org/abs/1903.00161)

## Construction

- **题目来源**：The Wikipedia dump of October 2018, and Wikipedia online. Priority goes to NFL game summaries, to history, and to paragraphs that contain at least 20 numbers. About 7000 passages are extracted. Questions are written by hand on MTurk, and a submission is allowed only if the online BiDAF cannot answer it. [2](https://arxiv.org/abs/1903.00161)

- **出题与审核人员**：Questions written through MTurk crowdsourcing; the author team designed the adversarial collection and verification process. [2](https://arxiv.org/abs/1903.00161)

- **审核流程**：For development and test, at least two additional human answers are added to each question, and 0.7% invalid questions are marked and filtered; overall Cohen κ=0.74 (numbers 0.81, spans 0.62, dates 0.65). [2](https://arxiv.org/abs/1903.00161)

- **质量控制**：Train/dev/test are split by paragraph so that the same paragraph does not cross sets; the paper states that validation removed about 0.7% invalid questions. [2](https://arxiv.org/abs/1903.00161)

- **防污染/运行完整性**：Paragraph-level isolation reduces leakage inside the dataset; it is not a contamination-free certification aimed at the pretraining corpora of modern large models. [2](https://arxiv.org/abs/1903.00161)

## Data format

- **规模**：The original version in the paper has 96567 questions: train 77409, dev 9536, and hidden test 9622. The HF metadata are instead 77400/9535, while the body of the card still lists 77409/9536. The specific packaged version must be stated. [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md)

- **题型**：Short answers to paragraph reading; an answer may be a number, a date, or single-span or multi-span text. [2](https://arxiv.org/abs/1903.00161)

- **模态**：Text (mathematical symbols expressed as text); not an original image or video recognition task [2](https://arxiv.org/abs/1903.00161)

- **语言覆盖**：English question text; for formal or mathematical notation, see the modality and the repository format [2](https://arxiv.org/abs/1903.00161)

- **难度与任务跨度**：The difficulty is the coupling of evidence selection and discrete operations; questions are not leveled by subject or grade. [2](https://arxiv.org/abs/1903.00161)

- **公开与隐藏划分**：A random 80/10/10 split by paragraph, so that the same paragraph does not cross splits; the original hidden test has 9622 questions, and the HF mirror contains only train and validation. [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md)

## Evaluation

- **指标**：Exact Match (EM) and F1 for numeric and multi-span answers. [2](https://arxiv.org/abs/1903.00161)

- **评分规则**：Normalized EM and a macro F1 that is sensitive to numbers; when the numbers do not match, the corresponding pair receives no F1. Multiple spans are aligned and then averaged, and the highest value is taken when there are several gold answers. The paper says the alignment is greedy, but the current official drop_eval.py uses optimal matching by linear_sum_assignment, and the script version should be pinned. [2](https://arxiv.org/abs/1903.00161) [1](https://allennlp.org/drop)

- **提示与运行配置**：The original paper is a supervised reading-comprehension system; few-shot and CoT use with a modern LLM, answer extraction, and truncation of context need to be listed on their own. [2](https://arxiv.org/abs/1903.00161)

- **评分/运行脚本**：https://github.com/allenai/allennlp-reading-comprehension/blob/master/allennlp_rc/eval/drop_eval.py [1](https://allennlp.org/drop)

- **可比性限制**：F1 is not EM; the public development set and the hidden test set, and different implementations of numeric normalization, cannot be compared directly. [2](https://arxiv.org/abs/1903.00161) [9](https://arxiv.org/html/2609.27284v1)

## Current status

- **核验日期**：2026-11-07 [1](https://allennlp.org/drop) [9](https://arxiv.org/html/2609.27284v1)

- **现行版本与采用证据**：A new data version has not been verified; the original allennlp-reading-comprehension repository is explicitly deprecated, and the models were moved to allennlp-models; a migration of the code cannot be treated as an update of the data. [6](https://raw.githubusercontent.com/allenai/allennlp-reading-comprehension/master/README.md)

- **更新与修订**：arxiv_version：arXiv v2；history_note：See the arXiv metadata for the full history; the draft date has been converted, and the paper revision date is not treated as the data version.；2026_h2_evidence：url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.2 Reasoning and Tables 3–4 actually report DROP; a vendor self-reported evaluation. [2](https://arxiv.org/abs/1903.00161) [9](https://arxiv.org/html/2609.27284v1)

- **已知问题与证据边界**：Wikipedia and public question answering have long been available, so memory effects cannot be ruled out from the current score. [2](https://arxiv.org/abs/1903.00161) [1](https://allennlp.org/drop)

- **关联与衍生关系**：Modern LLMs are often reported with DROP F1; that figure should not be treated as ordinary multiple-choice accuracy. [2](https://arxiv.org/abs/1903.00161) [1](https://allennlp.org/drop)

**仍待核实**（不推断为未公开）：

- 饱和度判断：Whether it is saturated depends on the specific split, the tools, and the protocol; the scores below are only a snapshot from a limited source and are not a judgment of overall saturation or of SOTA [2](https://arxiv.org/abs/1903.00161) [9](https://arxiv.org/html/2609.27284v1)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 (date the materials were collected; the results are historical experiments from the 2019 paper). [2](https://arxiv.org/abs/1903.00161)

- **官方榜/正式委托榜**：https://leaderboard.allenai.org/drop/submissions/public [2](https://arxiv.org/abs/1903.00161) 注：The official leaderboard WebFetch returned 500, and a curl of the public web page also met a TLS error; a historical table is visible in the search index and is not presented as a successful live read.

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | NAQANet (Complete Model) | 47.01 | Original-paper test F1 (%)；运行/发布日见覆盖说明；[2](https://arxiv.org/abs/1903.00161) |
| 2 | BERT | 32.7 | Original-paper test F1 (%)；运行/发布日见覆盖说明；[2](https://arxiv.org/abs/1903.00161) |
| Reference non-model rank | Expert human | 96.42 | Human F1 (%) from the authors answering 560 test questions；运行/发布日见覆盖说明；[2](https://arxiv.org/abs/1903.00161) |

> NAQANet (Complete Model)：exact_match：44.07；result_type：Historical baseline from the 2019 paper, not the current leaderboard [2](https://arxiv.org/abs/1903.00161)

> BERT：exact_match：29.45；result_type：Historical baseline from the 2019 paper, not the current leaderboard [2](https://arxiv.org/abs/1903.00161)

> Expert human：exact_match：94.09；result_type：2019 historical human reference [2](https://arxiv.org/abs/1903.00161)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：The official leaderboard for the hidden test cannot be read (500/TLS). A refreshed live ranking is not claimed from anything held in a search cache. The fallback below is the historical baseline in Table 4 of the original paper, which was actually read, and it is explicitly not the latest SOTA of 2026. Different dev and test sets, different prompts, and different training protocols cannot share one leaderboard. [2](https://arxiv.org/abs/1903.00161)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [2](https://arxiv.org/abs/1903.00161)

## Contact

- **公开联系邮箱**：info@allenai.org [4](https://registry.opendata.aws/allenai-drop/)

- **公开问题追踪**：https://github.com/allenai/allennlp-models/issues [8](https://github.com/allenai/allennlp-reading-comprehension)

**仍待核实**（不推断为未公开）：

- 官方社交：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [2](https://arxiv.org/abs/1903.00161)
- 隐私政策：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [2](https://arxiv.org/abs/1903.00161)

## Original files

- **原始PDF**：https://arxiv.org/pdf/1903.00161 [10](https://arxiv.org/pdf/1903.00161)

- **SHA-256**：e5f409536a3b9b8b0fdb7f687be42bd990e34ff2cb5862b9c1b241c2d498c4e5 [10](https://arxiv.org/pdf/1903.00161) 注：Byte count of the PDF actually downloaded. It is not copied from an external web page.

- **PDF字节数**：1989064 [10](https://arxiv.org/pdf/1903.00161) 注：Downloaded byte count; not uploaded.

## Changelog

- date：2026-11-07；；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。；date：2026-11-07；；change：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。；fields_updated：basic_info.code_url；evaluation.official_scripts；evaluation.scoring；latest_status.latest_dataset_version；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://allennlp.org/drop)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
