# BioMysteryBench

> Benchmark Constitution, in-depth review: 2026-11-08. Official existence has been verified; a field-level research snapshot; note: trending: A

BioMysteryBench gives real omics files to a programmable agent and tests whether it can recover information that has an independent ground truth, such as species, tissue of origin, or experimental treatment, without forcing one specified analysis route. Its key distinction is that a "verifiable answer" and "solvable by a human from scratch" are not the same thing. Of the final 99 questions, 76 were solved by at least one expert, and 23 were not solved by as many as five experts. The latter cannot be called unsolved scientific problems directly. The independent Vals evaluation and the original Anthropic experiment are also not the same scoring track.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

## Basic information

### Short name

BioMysteryBench

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### Full name

BioMysteryBench

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 版本边界

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Paper version

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Release date

2026-04-29 (date of the Anthropic introductory article)

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 板块

Biology and medicine

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> Benchmark Constitution editorial classification.

### 领域

```json
[
  "Science agent"
]
```

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> Editorial tags; an empty list means finer-grained tags have not yet been added.

### 许可与限制

The Vals method page says the task materials are CC BY 4.0, with an additional restriction against model training; the underlying biological data follow the original repository's policy. The full license text still needs to be checked.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### Paper

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Code

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Dataset

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Official homepage

https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 论文题名

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

## Origin and maintenance

### Initiators

Anthropic

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### Partner organizations

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Authors

The Anthropic Science / discovery team (the article introduces the researcher Brianna and does not supply a surname that was not given)

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 维护入口

Original Anthropic benchmark; Vals AI maintains an independent evaluation leaderboard

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 资助披露

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

## Design goals

### 测量对象

Open-path analysis of real bioinformatics data, recovering verifiable metadata such as species, sample origin, and genetic manipulation.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 既有评测的缺口

It avoids testing only knowledge or only simulated experiments, and it avoids treating one researcher's subjective analysis path, or an unconfirmed scientific conclusion, as the sole ground truth.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

## Construction

### 题源

Domain experts construct questions from raw or lightly processed DNA and RNA sequencing data and from proteomic and metabolomic data, using controllable attributes or experimental and clinical metadata as ground truth.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 构建人员

Bioinformatics domain experts.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 审核

The author of each question must submit a verification notebook showing that a signal is present in the data. At most 5 domain experts solve each question from scratch. After an additional quality check, 4 questions whose construction was faulty were removed. The final 99 questions are divided into 76 human-solvable and 23 human-difficult.

[来源1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）

### 质控

Questions answered correctly by at least 1 expert are classed as human-solvable, for 76 questions in the end; the remaining 23 are human-difficult, which does not mean that they are mathematically unsolvable.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 去污染及边界

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

## Data format

### 规模与计数口径

```json
{
  "final_questions": 99
  "human_solvable": 76
  "human_difficult": 23
  "excluded_broken_questions": 4
  "warning": "99 is the final set after 4 questions were removed; it is not 99 with another 4 removed. Whether the Vals evaluation denominator matches the original version is Unverified."
}
```

[来源1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-08）

### Question types

Investigates data files, writes analysis code, calls the command line, and queries biological databases, then submits a final answer.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### Modalities

```json
[
  "文本"
  "Sequencing and omics data files"
  "Code and database output"
]
```

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### Languages

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Difficulty

human-difficult means unsolved by at most 5 domain experts, which is not the same as proven unsolvable by humans.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 划分与公开范围

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

## Evaluation

### Metrics

The original text reports accuracy for the two question types, with 5 runs per question; the Vals headline is the mean accuracy of 3 complete evaluations.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 评分

Vals uses openai/gpt-5.6-terra to judge the final answer. Full acceptance = 1; refusal, failure, or non-acceptance = 0. A fixed path of analysis is not required.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 提示与运行条件

Vals: a Terminus 2 bioinformatics sandbox, limited to 200 turns and 4 hours; network access is allowed only to the repositories of necessary scientific packages and to biological databases, at the default reasoning level in the registry.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 官方评测入口

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### 可比性边界

The original version runs each question 5 times and reports the two subsets, 76 and 23, separately. Vals is the mean of 3 complete runs, with Terminus 2 and another judge. The two protocols must not be merged into one ranking. A model answering correctly does not mean that its chain of analysis has passed scientific or clinical validation.

[来源1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-08）

## Current status

### 复核时间

2026-11-08

[来源1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）

### 当前版本

```json
{
  "version": "待核实"
  "heat_confidence": "A"
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/biomysterybench"
      "date": "2026-11-05"
      "date_type": "source_calendar_date"
      "note": "Vals currently re-evaluates it independently, covering 30 models; this is not merely a restatement of Anthropic's self-report."
    }
  ]
}
```

[来源1](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

> Heat A follows the candidate grading; the nature of the evidence is labeled item by item. Multiple URLs do not automatically equal multiple independent adopters, and what is currently visible is not treated as a recent first release.

### 论文修订与后续使用

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### Saturation

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### 风险与冲突

The validation notebook shows that a signal is present, but it does not guarantee that the problem is solvable from scratch; the Vals final-answer judge does not verify complete scientific correctness or the validity of a new discovery.

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)；[来源2](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 衍生与后续工作

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）

### 官方榜入口

https://www.vals.ai/benchmarks/biomysterybench

[来源1](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 第三方榜入口

https://www.vals.ai/benchmarks/biomysterybench

[来源1](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-07）

### 逐轨结果

```json
[
  {
    "rank": 1
    "model": "Claude Sonnet 5.5"
    "score": 81.11
    "metric": "Vals Accuracy %; 3 runs"
    "source_url": "https://www.vals.ai/benchmarks/biomysterybench"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-07 "
    "track": "Vals independent retest/3 runs"
    "accessed": "2026-11-08"
  }
  {
    "rank": 2
    "model": "GPT-6.1 Sol"
    "score": 79.63
    "metric": "Vals Accuracy %; 3 runs"
    "source_url": "https://www.vals.ai/benchmarks/biomysterybench"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-07 "
    "track": "Vals independent retest/3 runs"
    "accessed": "2026-11-08"
  }
  {
    "rank": 3
    "model": "GPT-6 Astra"
    "score": 79.26
    "metric": "Vals Accuracy %; 3 runs"
    "source_url": "https://www.vals.ai/benchmarks/biomysterybench"
    "source_date": "2026-11-05"
    "collected_at": "2026-11-07 "
    "track": "Vals independent retest/3 runs"
    "accessed": "2026-11-08"
  }
  {
    "rank": null
    "model": "Claude Opus 4.6"
    "score": 77.4
    "metric": "accuracy (%)"
    "track": "Anthropic original report/human-solvable/5 episodes"
    "source_url": "https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench"
    "accessed": "2026-11-08"
    "unit": "%"
    "source_context": "A reliability-analysis passage included in, and endorsed by, the official article"
  }
  {
    "rank": null
    "model": "Claude Opus 4.6"
    "score": 23.5
    "metric": "accuracy (%)"
    "track": "Anthropic original report/human-difficult/5 episodes"
    "source_url": "https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench"
    "accessed": "2026-11-08"
    "unit": "%"
    "source_context": "Another subset of the same model; it cannot be ranked directly together with Vals percentages"
  }
]
```

[来源1](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-08）；[来源2](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）

### 覆盖边界

The current Vals top three have been reread. For the original version, only the two exact Opus 4.6 figures explicitly given in the official body text are added, and other models are not estimated from the figures. The Vals and Anthropic tracks are both kept. Consistency between the 99 questions and the actual Vals denominator is Unverified.

[来源1](https://www.vals.ai/benchmarks/biomysterybench)（访问2026-11-08）；[来源2](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）

## Contact

### 公开研究联系

```json
[
  "scienceblog@anthropic.com"
]
```

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The article publishes a research-feedback email address; it is not assumed to be dedicated technical support.

### 项目反馈

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### 官方社交入口

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### 联系信息边界

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

## Original files

### 原始PDF

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### PDF SHA-256

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### PDF bytes

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### 目录

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

> The listed materials have been opened, but this field has not yet been precisely verified; this does not indicate that the official source has not published it.

### 其他官方材料

```json
[
  {
    "type": "Official methods and introduction page (not the paper PDF)"
    "url": "https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench"
  }
]
```

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

### 论文归档

Unverified

[Source 1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench) (accessed 2026-11-07)

## Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]
```

[来源1](https://www.anthropic.com/research/Evaluating-Claude-For-Bioinformatics-With-BioMysteryBench)（访问2026-11-08）
