# MedScribe

> Benchmark Constitution, in-depth review 2026-11-08. The access date is not the date the experiment was run; dates from historical sources keep their original record.

MedScribe evaluates the ability to generate a structured SOAP note from a clinician-patient text transcript, rather than speech recognition. The benchmark derives synthetic dialogues from real de-identified SOAP materials, and experts then set the scoring rubric; the realism study, the human-judge alignment study, and the actual leaderboard samples are different statistical objects.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08); [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08)

## Basic information

### Short name

MedScribe

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Full name

MedScribe

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 版本与作用域

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 论文/报告版本

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 首次公开日期

Released no later than 2026-02-23 (the official blog that day called it recently released); the exact first-launch date is Unverified.

核验状态：待核实

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08)

### Section

Biology and medicine

Note: Benchmark Constitution editorial classification.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Subfields

```json
[
 "Clinical documentation"
]
```

Note: Editorial tags; an empty list means finer-grained tags have not yet been added.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 许可与权利边界

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 论文/报告入口

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Code

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Dataset

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Official homepage

https://www.vals.ai/benchmarks/medscribe

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 论文/报告标题

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Origin and maintenance

### 研究发起团队

Vals AI

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 合作研究机构与顾问

Protege provides curated de-identified medical data. Pranav Rajpurkar of Harvard Medical School provides advisory opinions. Harvard is not inferred to be a legal co-sponsoring institution from an individual advisory role.

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Authors

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Maintainer

Vals AI

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Funders

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Design goals

### 测量能力

Organizes transcripts of clinical consultations into accurate, compliant SOAP documents, and reduces the burden of administrative recording.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 设计动机

Correctness on medical examinations is not used in place of comparing the quality of real clinical documents.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Construction

### 材料来源

Real de-identified SOAP notes from Protege are used, and NoteChat is adapted to generate synthetic doctor-patient dialogues.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 命题与标注背景

medical scribes and physician assistant participate in expert verification.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Review process

Experts first build a SOAP structure template and annotate the rubrics independently, then resolve conflicts together.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Quality control

NoteChat generates synthetic transcripts from real de-identified SOAP notes in Protege. The experts include medical scribes and a physician assistant. A realism-perception trial used 80 transcripts (40 real and 40 simulated), with an identification accuracy of 39%, chance50%, and p>0.05. Another judge-alignment trial used only 3 samples/180 checks. After the prompt was adjusted, agreement with the human majority opinion was 80.5%. The two studies cannot be extrapolated to effectiveness in clinical deployment.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 去污染与留出

The official release note explicitly adopts patient-level holdouts; the general Vals method requires that published scores for a proprietary benchmark use only a test set that remains private, in order to reduce training leakage. De-identification is a privacy measure and not, by itself, proof against contamination, and a private holdout is not proof that every training run has no overlap.

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08)

## Data format

### 规模与统计对象

The official launch blog says that 100 sets of expert rubrics cover 80 transcripts; the leaderboard method also reports, separately, a study of perceived realism on 80 transcripts (40 real and 40 simulated) and 10 examples of real transcripts. The three numbers belong to different levels of description. They are not added up into a count of patients, and the realism experiment is not taken directly as the composition of the leaderboard questions.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08); [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08)

### 题型与字段

A clinician-patient dialogue transcript is the input, and a four-section SOAP note is the output: Subjective, Objective, Assessment, and Plan.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Modalities

```json
[
 "Text dialogue"
 "Text SOAP notes"
]
```

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### Languages

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 难度与覆盖

A complete SOAP note is generated from a clinician-patient text transcript. Facts must be retained and organized according to the expert template. The official analysis is split into S/O/A/P and subclasses such as HPI and General Survey, and Plan includes orders, prescriptions, referrals, and follow-up. This is a clinical documentation task, not ASR and not a safety certification of real clinical care.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 公开/私有与数据划分

The officially published scores come from a private test set (the general method for proprietary Vals benchmarks explicitly keeps it private). For this entry, the download address of a specific public validation set, the train and validation counts, and the split ratio are Unverified. It cannot be inferred, from the general statement that most benchmarks have a public validation set, that this entry must be public.

核验状态：待核实

Sources: [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08); [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Evaluation

### Metrics

Accuracy (pass status of the rubric checks); analyzed by SOAP category and subcategory.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 评分与聚合

SOAP notes are evaluated against an expert gold-standard rubric, and the prompt of the model judge is calibrated for agreement with humans; the specific version of the judge is Unverified.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 提示与推理预算

Every model uses temperature 1 and a maximum of 30k output tokens, with a unified expert template.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 官方实现

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 可比性边界

This is not a metric of speech recognition or of safety in clinical diagnosis; format, and which SOAP section an item is assigned to, affect the judge, and agreement with human preference is not complete.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Current status

### 核验时间

2026-11-08

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 当前数据与协议

```json
{
 "version": "MedScribe (leaderboard updated 2026-10-29; the data semantic version number is Unverified)"
 "heat_confidence": "B"
 "evidence_2026_h2": [
 {
 "url": "https://www.vals.ai/benchmarks/medscribe"
 "date": "2026-10-29"
 "date_type": "source_calendar_date"
 "note": "Vals leaderboard update, 109 models, clinical administrative document tasks."
 }
 ]
}
```

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 论文修订与延续使用证据

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 饱和判断边界

The current highest rubric Accuracy is 91.43%, but this is not a medical record that is completely free of error at 100%; the official source still finds weak points such as Plan and HPI, and a study of alignment with humans on 3 samples is also insufficient to prove that every clinical-documentation task is saturated.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 污染、冲突与复现风险

The official statement says that the patient-level holdout and the proprietary test are private; without open data for each question and a script that can reproduce the score, a third party cannot audit every overlap and every score from the leaderboard alone. Model names are the labels as given by the source, and an API snapshot is not filled in.

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08); [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 衍生实现

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Leaderboard snapshot

### 访问快照日期

2026-11-08 (access; run and submission dates of each source are listed separately)

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 官方榜单入口

https://www.vals.ai/benchmarks/medscribe

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 第三方评测入口

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 分来源、分协议结果

```json
[
 {
 "rank": 1
 "model": "Claude Opus 5.5"
 "score": 91.43
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 2
 "model": "Claude Fable 5.1"
 "score": 91.29
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 3
 "model": "Claude Sonnet 5.5"
 "score": 91.1
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 4
 "model": "Claude Opus 5"
 "score": 90.98
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 5
 "model": "Muse Spark 1.2"
 "score": 90.06
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 6
 "model": "Claude Haiku 5.5"
 "score": 89.54
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 7
 "model": "Grok 4.7"
 "score": 89.38
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 8
 "model": "Wonder Full"
 "score": 89.33
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 9
 "model": "GLM 5.3 Flash"
 "score": 88.94
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 10
 "model": "Muse Spark 1.1"
 "score": 88.89
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedScribe / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medscribe"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
]
```

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 快照覆盖说明

The top 10 of the official leaderboard were reread, one row at a time. The page itself writes Updated 2026-10-29. The access date is 2026-11-08. A count of model rows is not a count of questions, and the latest access is not a rerun on that same day. Vals maintains this task. The Vals leaderboard is a primary official source, rather than a further organization adopting the benchmark on its own.

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Contact

### 官方公开联系邮箱

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 项目反馈入口

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 公开社交渠道

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 联系信息原则

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Original files

### 原始论文/技术报告PDF

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### PDF SHA-256

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### PDF原始字节数

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 资料夹

Unverified

Note: The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

### 其他官方资料

```json
[
 {
 "title": "Measuring Healthcare AI Where It Actually Works"
 "url": "https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works"
 "source_date": "2026-02-23"
 "byline": "Rayan Krishnan"
 }
 {
 "title": "Vals AI Evaluation Methodology"
 "url": "https://www.vals.ai/methodology"
 }
]
```

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08)

### 已存PDF

Unverified

Note: This group only creates local research files and does not upload a PDF or claim that one already exists.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)

## Changelog

### Changelog

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
 {
 "date": "2026-11-08"
 Latest review
 }
]
```

Sources: [https://www.vals.ai/benchmarks/medscribe](https://www.vals.ai/benchmarks/medscribe) (accessed 2026-11-08)
