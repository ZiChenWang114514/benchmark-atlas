# MedCode

> Benchmark Constitution, in-depth review 2026-11-08. The access date is not the date the experiment was run; dates from historical sources keep their original record.

MedCode concerns the diagnostic coding required for inpatient medical billing, rather than medical-knowledge question answering. Vals AI and Protege curated 2,755 de-identified inpatient records and require the model to identify principal and secondary diagnoses in the discharge summary, progress notes, and consultation materials, and to map them to CMS ICD-10-CM.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08); [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08)

## Basic information

### Short name

MedCode

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Full name

MedCode

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 版本与作用域

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 论文/报告版本

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 首次公开日期

Released no later than 2026-02-23 (the official blog that day called it recently released); the exact first-launch date is Unverified.

核验状态：待核实

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08)

### Section

Biology and medicine

Note: Filed under one main section. That filing does not limit coverage of other disciplines.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Subfields

```json
[
 "Medical coding"
]
```

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 许可与权利边界

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 论文/报告入口

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Code

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Dataset

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Official homepage

https://www.vals.ai/benchmarks/medcode

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 论文/报告标题

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Origin and maintenance

### 研究发起团队

Vals AI

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 合作研究机构与顾问

Protege provides curated de-identified medical data. Pranav Rajpurkar of Harvard Medical School provides advisory opinions. Harvard is not inferred to be a legal co-sponsoring institution from an individual advisory role.

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Authors

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Maintainer

Vals AI

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Funders

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Design goals

### 测量能力

Output primary and secondary ICD-10-CM diagnosis codes from a complete inpatient record.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 设计动机

Simulates the constraints of real medical-billing documents, rather than testing only clinical multiple-choice questions.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Construction

### 材料来源

2755 de-identified patient records, comprising discharge summaries, progress notes, and consultation notes.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 命题与标注背景

Each case is annotated independently by two certified professional coders.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Review process

Checking with Codify is allowed, but AI is prohibited; disagreements are resolved collaboratively.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Quality control

Required population and regional information is retained, and the first three digits of the ZIP code are mapped to jurisdictions; class-O delivery codes are excluded because confounding makes them unreliable.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 去污染与留出

The official release note explicitly adopts patient-level holdouts; the general Vals method requires that published scores for a proprietary benchmark use only a test set that remains private, in order to reduce training leakage. De-identification is a privacy measure and not, by itself, proof against contamination, and a private holdout is not proof that every training run has no overlap.

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08)

## Data format

### 规模与统计对象

2755 de-identified inpatient records.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 题型与字段

Generates principal and secondary CMS ICD-10-CM diagnosis codes.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Modalities

```json
[
 "Text medical record"
]
```

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### Languages

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 难度与覆盖

Coding of primary and secondary diagnoses across the whole inpatient course. CMS ICD-10-CM coding rules must be applied together with the discharge summary, progress notes and consultation notes, and demographic and geographic information. The official error analysis is by chapter, by primary versus secondary diagnosis, and by code precision. No unified easy, medium, and hard bins are provided.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 公开/私有与数据划分

The officially published scores come from a private test set (the general method for proprietary Vals benchmarks explicitly keeps it private). For this entry, the download address of a specific public validation set, the train and validation counts, and the split ratio are Unverified. It cannot be inferred, from the general statement that most benchmarks have a public validation set, that this entry must be public.

核验状态：待核实

Sources: [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08); [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Evaluation

### Metrics

Official main table Accuracy(%); principal/secondary diagnosis, ICD chapter, and coding-precision breakdowns are also reported.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 评分与聚合

Evaluated against a reference diagnostic-coding rubric; the aggregation formula for exact match and partial scores is Unverified.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 提示与推理预算

temperature=1, at most 30000 tokens.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 官方实现

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 可比性边界

Medical-coding scores do not represent diagnostic ability or clinical deployability; breakdowns by chapter, code granularity, and principal/secondary diagnosis cannot be compared together.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Current status

### 核验时间

2026-11-08

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 当前数据与协议

```json
{
 "version": "MedCode (leaderboard updated 2026-10-29; the semantic version number of the data is Unverified)."
 "heat_confidence": "B"
 "evidence_2026_h2": [
 {
 "url": "https://www.vals.ai/benchmarks/medcode"
 "date": "2026-10-29"
 "note": "The current Vals leaderboard of 107 models; attention comes mainly from a single evaluation organization, and it is not described as broad adoption."
 }
 ]
}
```

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 论文修订与延续使用证据

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 饱和判断边界

The highest Accuracy on the current official results is 63.57%. Official analysis shows that primary diagnoses are better than secondary diagnoses, and missing a reference diagnosis is more common than confusing primary and secondary labels. Clear room for improvement remains. 63.57% is not interpreted as the proportion of complete inpatient records in which every code is correct.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 污染、冲突与复现风险

The official statement says that the patient-level holdout and the proprietary test are private; without open data for each question and a script that can reproduce the score, a third party cannot audit every overlap and every score from the leaderboard alone. Model names are the labels as given by the source, and an API snapshot is not filled in.

Sources: [https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works](https://www.vals.ai/blogs/measuring-healthcare-ai-where-it-actually-works) (accessed 2026-11-08); [https://www.vals.ai/methodology](https://www.vals.ai/methodology) (accessed 2026-11-08); [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 衍生实现

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Leaderboard snapshot

### 访问快照日期

2026-11-08 (access; run and submission dates of each source are listed separately)

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 官方榜单入口

https://www.vals.ai/benchmarks/medcode

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 第三方评测入口

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 分来源、分协议结果

```json
[
 {
 "rank": 1
 "model": "Claude Opus 5"
 "score": 63.57
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 2
 "model": "Gemini 3.1 Pro Preview (02/26)"
 "score": 59.06
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 3
 "model": "Gemini 4 Argon"
 "score": 58.8
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 4
 "model": "Claude Fable 5"
 "score": 56.07
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 5
 "model": "Gemini 3 Flash (12/25)"
 "score": 55.92
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 6
 "model": "Gemini 3.5 Flash"
 "score": 55.83
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 7
 "model": "Claude Opus 4.7"
 "score": 54.86
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 8
 "model": "Claude Fable 5.1"
 "score": 53.51
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 9
 "model": "Gemini 3.7 Flash"
 "score": 53.39
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
 {
 "rank": 10
 "model": "Claude Opus 4.8"
 "score": 53.22
 "unit": "%"
 "metric": "Accuracy"
 "track": "Vals official / MedCode / page snapshot of 2026-10-29."
 "source_url": "https://www.vals.ai/benchmarks/medcode"
 "accessed": "2026-11-08"
 "source_date": "2026-10-29"
 "result_type": "Unified evaluation by the benchmark maintainer; not a vendor self-report"
 "settings": "temperature 1; at most 30k output tokens"
 }
]
```

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 快照覆盖说明

The top 10 of the official leaderboard were reread, one row at a time. The page itself writes Updated 2026-10-29. The access date is 2026-11-08. A count of model rows is not a count of questions, and the latest access is not a rerun on that same day. Vals maintains this task. The Vals leaderboard is a primary official source, rather than a further organization adopting the benchmark on its own.

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Contact

### 官方公开联系邮箱

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 项目反馈入口

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 公开社交渠道

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 联系信息原则

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

## Original files

### 原始论文/技术报告PDF

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### PDF SHA-256

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### PDF原始字节数

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

### 资料夹

Unverified

Note: Still not precisely verified after the listed materials were opened; this does not mean the official source has not made it public.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

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

Note: This group is local research only and was not uploaded.

核验状态：待核实

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)

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

Sources: [https://www.vals.ai/benchmarks/medcode](https://www.vals.ai/benchmarks/medcode) (accessed 2026-11-08)
