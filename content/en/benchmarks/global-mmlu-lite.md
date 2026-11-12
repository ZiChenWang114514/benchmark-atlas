# Global-MMLU-Lite

> Benchmark Constitution, check date: 2026-11-07. Unknowns remain Unverified; the access date is not presented as the experiment date.

Global-MMLU-Lite evaluates ability in more than one language with a subset of MMLU that people translated or post-edited, and it analyzes sensitivity to culture apart from how the model scores. The range of 23 languages on the current data card for 3.0 is not the range of the original paper's experiment on 15 languages, and it is not the range covered by the AA implementation. Sharing a name is not a reason to merge the three.

Sources for the reading guide: [https://artificialanalysis.ai/methodology/intelligence-benchmarking](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07); [https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [https://arxiv.org/abs/2412.03304](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

## Basic information

### Short name

Global-MMLU-Lite

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Full name

Global-MMLU-Lite

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Dataset version

3.0

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Paper version

v2; 2025-02-19 (paper revision number, not a data version)

Sources: [1](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### Release date

First released in 2024-12; 3.0 was updated in 2026-05 (the data card gives only the month).

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Section

Language

Note: Benchmark Constitution editorial classification.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Subfields

- 多语言

Note: Editorial tags; an empty list means finer-grained tags have not yet been added.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### License

Apache 2.0 (dataset)

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Paper

https://arxiv.org/abs/2412.03304

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 代码入口

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Dataset

https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Official homepage

https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Paper title

Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

## Origin and maintenance

### 发起团队

Cohere Labs

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [2](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### 合作及署名机构

The Cohere For AI community and paid language experts jointly completed the cultural annotation and the translation review; this field only states that contribution and does not treat every author affiliation as a formal collaborating institution.

Sources: [1](https://arxiv.org/pdf/2412.03304) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Authors

Shivalika Singh, Angelika Romanou, Clémentine Fourrier, David I. Adelani, and others; the full list of authors follows the paper.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [2](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### Maintainer

Cohere Labs and the Open Science community

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [2](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### Funders

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

## Design goals

### 评测能力

Multilingual knowledge and reasoning, with a separate analysis of performance on culturally sensitive CS questions and culture-independent CA questions.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [2](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### 设计动机

Machine translation of English MMLU on its own both introduces translation artifacts and retains a Western knowledge bias; human review of the translation and cultural annotation make the evaluation more interpretable.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [2](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

## Construction

### 材料来源

Questions are drawn from MMLU, with 200 culturally sensitive CS questions and 200 culture-independent CA questions per language.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 编制背景

Professional annotators and community contributors from Cohere Labs.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Review process

All Lite questions were translated by humans or post-edited by humans; cultural annotations are recorded by the vote counts of multiple annotators.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Quality control

CS/CA balanced; metadata such as country, region, culture, and time_sensitive are retained.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 去污染边界

It reuses public MMLU question sources. Human translation and cultural annotation improve translation quality and interpretability, but they are not a guarantee that pretraining exposure has been removed. A dedicated audit of training contamination is Unverified.

Sources: [1](https://arxiv.org/pdf/2412.03304) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

## Data format

### Size

test 9,200 items (23 languages, 400 per language); dev 4,655 items (22 languages).

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Question types

Four-choice A/B/C/D, with the fields sample_id, subject, question, options, answer, and cultural annotation.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Modalities

- 文本

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Languages

23 languages (3.0 data card); the original paper's 15 languages and the AA-supported subset are listed separately and are not the same as all 23 current languages.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### Difficulty

It reuses MMLU subject questions and does not set a separate unified Lite difficulty level; CS/CA are cultural-sensitivity labels, not easy/hard labels.

Sources: [1](https://arxiv.org/pdf/2412.03304) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 公开及隐藏划分

Public test and dev; the data viewer's total of 14,000 rows must not be taken as the exact number of test questions.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

## Evaluation

### Metrics

Accuracy/pass@1; it should be reported separately by language and by CS/CA.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [3](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### 计分

AA extracts 4-choice answers with a regular expression, at pass@1, once per question, with no tools.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [3](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### 提示与运行设置

AA standard zero-shot instructions; about 400 questions per language. The original paper's 5-shot experiments cannot be ranked together with AA without an accompanying note.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [3](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### 评测入口

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 可比性边界

The full Global-MMLU has 42 languages, rather than the 23 languages of Lite; the AA method page still writes about 6,000 questions alongside 16 supported languages, and the language count and the approximate figure need to be rechecked, so coverage of the whole of 3.0 cannot be claimed from this.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07); [2](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [3](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

## Current status

### 核查日

2026-11-07 (designated collection date)

Sources: [1](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### 已核实版本

version：3.0；heat_confidence：B；evidence_2026_h2：- url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；date_type：observed_on；note：AA's current Multilingual Index is based on this test, and there is a separate evaluation page.

Note: Heat B: recent heat is supported mainly by one evaluation organization continuing to run and display it, and does not indicate wide adoption across the industry.

Sources: [1](https://artificialanalysis.ai/methodology/intelligence-benchmarking) (accessed 2026-11-07)

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2024-12-04；- version：v2；submitted_at：2025-02-19；Sources: [1](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### Saturation

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 已知问题

Marking cultural sensitivity is not the same as having solved cultural inclusion; community contributions are unevenly distributed, and dialect coverage is limited.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 衍生关系

The full Global-MMLU of the same family is no longer split into separate entries; it partly overlaps OpenAI MMMLU in translation sources, but it is not the same question set.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07); [2](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

## Leaderboard snapshot

### 采集日期

2026-11-07 (collection date; it does not replace a leaderboard update or an experiment date)

Sources: [1](https://artificialanalysis.ai/evaluations/global-mmlu-lite) (accessed 2026-11-07)

### 官方结果入口

https://artificialanalysis.ai/evaluations/global-mmlu-lite

Sources: [1](https://artificialanalysis.ai/evaluations/global-mmlu-lite) (accessed 2026-11-07)

### 第三方结果入口

https://artificialanalysis.ai/evaluations/global-mmlu-lite

Sources: [1](https://artificialanalysis.ai/evaluations/global-mmlu-lite) (accessed 2026-11-07)

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Independent evaluation by Artificial Analysis | 1 | Gemini 3.1 Pro Preview | 93.2 | accuracy % | [原始来源](https://artificialanalysis.ai/evaluations/global-mmlu-lite)；采集2026-11-07；Unverified (page does not show a measurement/update date) |
| Independent evaluation by Artificial Analysis | 2 | Gemini 3 Flash Preview (Non-reasoning) | 92.7 | accuracy % | [原始来源](https://artificialanalysis.ai/evaluations/global-mmlu-lite)；采集2026-11-07；Unverified (page does not show a measurement/update date) |
| Independent evaluation by Artificial Analysis | 3 | Gemini 3 Pro Preview (High) | 92.2 | accuracy % | [原始来源](https://artificialanalysis.ai/evaluations/global-mmlu-lite)；采集2026-11-07；Unverified (page does not show a measurement/update date) |

Note: —表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

Results currently visible on the web page; the page does not mark a leaderboard update date, and the collection date cannot be substituted for the update date.

Sources: [1](https://artificialanalysis.ai/evaluations/global-mmlu-lite) (accessed 2026-11-07)

## Contact

### 公开研究联系邮箱

- shivalika@cohere.com
- beyza@cohere.com
- sarahooker@cohere.com

Sources: [1](https://arxiv.org/pdf/2412.03304) (accessed 2026-11-07)

### 问题反馈

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 官方账号

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 隐私政策

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

## Original files

### 原文PDF

https://arxiv.org/pdf/2412.03304

Note: An original paper of the same family; it is not presented as an independent 3.0 paper.

Sources: [1](https://arxiv.org/abs/2412.03304) (accessed 2026-11-07)

### PDF SHA-256

33355d08932663acd0631ad63c0d35977fd6944c22f28cc802abdba5c91baa8e

Note: SHA-256 of the originally downloaded PDF bytes. Whether it matches an existing copy has to be checked with that copy's checksum.

Sources: [1](https://arxiv.org/pdf/2412.03304) (accessed 2026-11-07)

### PDF bytes

7733572

Sources: [1](https://arxiv.org/pdf/2412.03304) (accessed 2026-11-07)

### Folder

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### 其他原始材料

- type：Official methods and introduction page (not the paper PDF)；url：https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

### PDF

Unverified

Note: This group only creates local research files and does not upload a PDF or claim that one already exists.

Sources: [1](https://huggingface.co/datasets/CohereLabs/Global-MMLU-Lite) (accessed 2026-11-07)

## Changelog

### 本页修订

- date：2026-11-07；change：新建近期热门中文研究条目；区分当前榜单与历史结果；缺项逐字段标记。
- date：2026-11-07；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

Sources: [1](urn:benchmark-constitution:editorial:r2-q4) (accessed 2026-11-07)
