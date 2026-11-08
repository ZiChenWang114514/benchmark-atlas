# HumanEvalFix

> Benchmark Constitution, source-by-source in-depth check: 2026-11-08. The collection date does not represent the experiment date; Unverified is not the same as Not disclosed.

HumanEvalFix inserts functional errors by hand into reference programs in the six languages of HumanEvalPack and requires the program to be repaired so that the tests pass. The same 164 original questions rewritten across languages cannot be treated as 984 independent knowledge questions; the exact FixTests baselines by language from the original paper are restored, and they are kept separate from FixDocs and from later experiments on relative improvement.

Basis of the reading guide: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-08); [2](https://github.com/bigcode-project/octopack) (accessed 2026-11-08); [3](https://huggingface.co/datasets/bigcode/humanevalpack) (accessed 2026-11-08).

## Basic information

### Short name

HumanEvalFix

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### Full name

HumanEvalFix

> The official name is retained, and the paper title is not automatically expanded into a full name.

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### Benchmark version

HumanEvalFix within HumanEvalPack; 6 languages × 164 questions

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Paper version

arXiv v2

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-08).

### Release date

2023-08-14 (date of the first arXiv draft; not the separate release date of the dataset).

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-08).

### Section

Code

> Benchmark Constitution editorial filing. Only the main section is counted.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 领域

```json
[
 "Code repair"
]
```

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 许可与使用范围

MIT. OctoPack officially states that HumanEvalPack and all of the code are included under the MIT license of this repository, rather than the license being marked on the code alone. CommitPack and CommitPackFT samples have the licenses of their original repositories, and those licenses should not be mixed in.

Sources: [1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md) (accessed 2026-11-07).

### 论文入口

https://arxiv.org/abs/2308.07124

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Code

https://github.com/bigcode-project/octopack

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### Dataset

https://huggingface.co/datasets/bigcode/humanevalpack

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Official homepage

https://github.com/bigcode-project/octopack

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### Paper title

OctoPack: Instruction Tuning Code Large Language Models

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

## Origin and maintenance

### Initiators

BigCode / OctoPack author team

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 合作与作者单位

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Authors

```json
[
 "Muennighoff, Niklas"
 "Liu, Qian"
 "Zebaze, Armel"
 "Zheng, Qinkai"
 "Hui, Binyuan"
 "Zhuo, Terry Yue"
 "Singh, Swayam"
 "Tang, Xiangru"
 "von Werra, Leandro"
 "Longpre, Shayne"
]
```

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Maintainer

BigCode octopack project

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 资助与资源支持

The paper thanks Hugging Face for providing compute instances; this is evidence of compute support and is not a basis for inferring an amount of cash funding that is not listed.

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08).

## Design goals

### 测量能力

Repairs functional errors according to the task specification and an existing program that contains errors; measures instruction-tuned code models.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 与既有基准的差异

Code completion covers only synthesis and lacks cross-language, instruction-driven repair and explanation tasks.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

## Construction

### Question sources

One bug is inserted manually into each of the 164 HumanEval reference functions in each language, keeping the same kind of error across languages as far as possible.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 出题者背景

The paper team designed the bugs by hand, rather than having a model automatically decide repair ground truth.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Review process

The work starts from the JSON of solutions in each language of HumanEval-X. Bugs are introduced into each language in parallel, by hand. Problems in HumanEval-X are corrected, and the corrections are recorded. The material is then turned into JSONL of a buggy solution, an instruction, and metadata, and it is uploaded as HumanEvalPack.

Sources: [1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md) (accessed 2026-11-07).

### Quality control

6 languages use similar bugs in support of comparability; the appendix gives categories and instances.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 去污染与泄漏控制

Derived from public HumanEval; adding human-authored errors does not remove the possibility that a model remembers the original correct implementation.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

## Data format

### 规模与统计口径

164 questions per language, and 984 bugs across 6 languages; this is not 984 original questions unrelated to one another.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Question types

Natural language plus faulty code → repaired code; tests and docstring prompts have different variants.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Modalities

```json
[
 "文本"
 "源代码"
]
```

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Languages

```json
[
 "Python"
 "JavaScript"
 "Java"
 "Go"
 "C++"
 "Rust"
]
```

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Difficulty

Minor functional bugs; the easier variant indicated in the documentation must be distinguished from the variant that supplies only tests.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### Public and hidden splits

Released through HumanEvalPack; Fix, Explain, and Synthesize are different tasks in the same suite.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

## Evaluation

### Metrics

pass@1 and related results for execution tests, reported separately by language.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 评分规则

Repaired code must pass the reference tests; the quality of a natural-language explanation is not a substitute for functional correctness.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 提示、采样与工具设置

humanevalfixtests (tests are given and the docstring is not; the paper's primary setting) is distinguished from humanevalfixdocs (the docstring is given). The official example uses temperature=0.2, n_samples=20, batch_size=5, and max_length_generation=2048.

Sources: [1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md) (accessed 2026-11-07).

### 官方脚本

https://github.com/bigcode-project/octopack

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### 可比性警告

Comparisons must be separated by language and by the fixdocs and fixtests protocols. The official notes say that the Python version and batch_size affect randomness. The paper uses Python3.9.13 and batch_size=5. Execution of generated code that is not trusted should be isolated.

Sources: [1](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md) (accessed 2026-11-07).

## Current status

### 核查时间

2026-11-08

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-08); [2](https://github.com/bigcode-project/octopack) (accessed 2026-11-08).

### 最新数据状态

```json
{
 "version": "HumanEvalFix within HumanEvalPack; 6 languages × 164 questions"
 "evidence_2026_h2": [
 {
 "url": "https://arxiv.org/html/2609.19134v1"
 "date": "2026-09-16"
 "note": "ScienceIDE §3.3 and Appendix 11.1 actually use code-repair tasks, including HumanEvalFix JavaScript, to evaluate transfer from training on scientific trajectories."
 }
 ]
}
```

> Active H2 evidence distinguishes actual evaluation, third-party tracking, and academic citation alone; a citation is not used to infer an actual run.

Sources: [1](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-07); [2](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2023-08-14"
 }
 {
 "version": "v2"
 "submitted_at": "2024-02-18"
 }
]
```

> The original arXiv UTC time has been converted; this does not constitute a dataset version change.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-08).

### 饱和度与证据边界

Table 2 of the original paper, mean pass@1 over six languages: GPT-4 47.8% and OctoCoder 27.0%; this is a historical baseline from 2023/2024, and the current degree of saturation in 2026 cannot be judged from it.

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08).

### 污染与已知问题

Adapting HumanEval mixes memory of the original problems with the ability to repair them, and a bug that is the same across languages is not a fully independent sample.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 相关与衍生基准

HumanEvalExplain and HumanEvalSynthesize are sibling tasks of HumanEvalPack; this entry includes only HumanEvalFix.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not a run date or a leaderboard-update date)

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08); [2](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-08).

### 官方结果入口

https://github.com/bigcode-project/octopack

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### 独立评测入口

Unverified

> Independent leaderboard coverage of this benchmark by AA / Epoch / LMArena, on the same definition, was not verified in these sources; other tasks are not used as substitutes.

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "GPT-4"
 "score": "47.0"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Python."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "WizardCoder"
 "score": "31.8"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Python."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "OctoCoder"
 "score": "30.4"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Python."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "48.2"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / JavaScript"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "WizardCoder"
 "score": "29.5"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / JavaScript"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "OctoCoder"
 "score": "28.4"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / JavaScript"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "50.0"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Java."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "WizardCoder"
 "score": "30.7"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Java."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "OctoCoder"
 "score": "30.6"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Java."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "50.6"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / Go"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "WizardCoder"
 "score": "30.4"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / Go"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "OctoCoder"
 "score": "30.2"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / Go"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "47.6"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / C++"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "OctoCoder"
 "score": "26.1"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / C++"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "WizardCoder"
 "score": "18.7"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper Table 2 HumanEvalFixTests / C++"
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "GPT-4"
 "score": "43.3"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Rust."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "OctoCoder"
 "score": "16.5"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Rust."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "WizardCoder"
 "score": "13.0"
 "metric": "zero-shot pass@1 (%)"
 "track": "Original paper, Table 2, HumanEvalFixTests / Rust."
 "source_url": "https://arxiv.org/pdf/2308.07124"
 "result_type": "Historical baselines from the authors' paper; ranking within the listed three-model subset, not the current full leaderboard"
 "source_date": "Paper v2; actual API run date Unverified"
 "snapshot_date": "2026-11-08 "
 }
 {
 "model": "The ScienceIDE 4B SFT training setting (the exact checkpoint is Unverified)."
 "result": "A relative improvement of 10.98 percentage points on HumanEvalFix JavaScript"
 "metric": "The paper reports relative improvement, not absolute scores"
 "benchmark_version": "HumanEvalFix JS"
 "result_type": "H2 academic experiment"
 "source_date": "2026-09-16"
 "collected_at": "2026-11-07 "
 "track": "ScienceIDE H2 academic experiment (relative improvement, not an absolute leaderboard score)"
 "snapshot_date": "2026-11-07 (historical evidence retained; this article was not reopened)"
 "rank": null
 }
]
```

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08); [2](https://arxiv.org/html/2609.19134v1) (accessed 2026-11-08).

### 覆盖与局限

Exact per-language FixTests baselines from Table 2 of the original authors' paper are added. No independent live official overall leaderboard was found. ScienceIDE relative improvement keeps the earlier collection date and is listed on its own, and it is not converted to absolute pass@1. FixDocs must not be mixed into this track.

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08); [2](https://github.com/bigcode-project/octopack/blob/main/README.md) (accessed 2026-11-08).

## Contact

### 官方公开邮箱

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 仓库反馈

https://github.com/bigcode-project/octopack/issues

> Public repository feedback entry point; no question was sent.

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07).

### 官方社区

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

### 隐私与联系边界

Unverified

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

Sources: [1](https://arxiv.org/abs/2308.07124) (accessed 2026-11-07).

## Original files

### Paper PDF

https://arxiv.org/pdf/2308.07124

> Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-07).

### PDF SHA-256

c03f04d06e000e4a251bea07c8b654721a97dbf23009ba45909439c7d814502a

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08).

### PDF bytes

```json
2618401
```

> Measured value of the PDF downloaded on 2026-11-08; the internal copy was not downloaded again, and this does not prove that it is identical to the present file.

Sources: [1](https://arxiv.org/pdf/2308.07124) (accessed 2026-11-08).

## Changelog

### 历次核查

```json
[
 {
 "date": "2026-11-07"
 Latest review
 }
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

Sources: [1](https://github.com/bigcode-project/octopack) (accessed 2026-11-07); [2](https://arxiv.org/abs/2308.07124) (accessed 2026-11-08); [3](https://github.com/bigcode-project/octopack) (accessed 2026-11-08).
