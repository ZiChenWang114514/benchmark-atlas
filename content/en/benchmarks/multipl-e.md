# MultiPL-E

> Verification date: 2026-11-08. Unknowns are not filled in; the date on which the source was accessed is not the experiment run date.

MultiPL-E translates the interfaces, specifications, and tests of HumanEval and MBPP into multiple programming languages. Functional correctness is still determined by compilation and unit tests. The original paper's experiment on 19 languages cannot represent the current HF release: the dataset card's latest listing is version 3.3, which fixes the Lua stop-word problem. The numbers of target-language configurations for HumanEval and for MBPP now also differ. GitHub additionally prohibits machine-learning training, while HF marks MIT. The conflict between the two license statements is still retained explicitly.
[Sources for this page](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md) (accessed 2026-11-08)

[Supplementary guide basis](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE) (accessed 2026-11-08)

[Additional guide source](https://arxiv.org/pdf/2208.08227) (accessed 2026-11-08)

## Basic information

### Short name

MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### Full name

Multi-Programming Language Evaluation of Large Language Models of Code

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）

### 数据/基准版本

```json
{
  "hf_changelog_latest": "3.3"
  "hf_revision": "28441b6024e71d4a1c1c0f6bf171c935cd5a43f2"
  "scope": "The current HF data release; the 19-language protocol of the original paper is listed separately"
}
```

[来源1](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E)（访问 2026-11-08）

### Paper version

arXiv v4

> A paper revision is not the same as a dataset version.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Release date

2022-08-17 20:16:52

> The time of the first arXiv paper submission; it is not automatically treated as the first-release time of the dataset.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Section

Code

> Benchmark Constitution editorial filing. Only the main section is counted.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Subfields

Multilingual code generation

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 许可边界

The repository is under BSD 3-Clause with Machine Learning Restriction. Clause 4 prohibits use for training. The official HF data card marks MIT in addition. The two carriers of publication do not say the same thing, and each statement is kept. The HF label is not a way around the terms of the repository.

[来源1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/LICENSE)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2208.08227

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 代码入口

https://github.com/nuprl/MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### Dataset

https://huggingface.co/datasets/nuprl/MultiPL-E

[来源1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/README.md)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### Official homepage

https://nuprl.github.io/MultiPL-E/

[来源1](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）

### Paper title

MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## Origin and maintenance

### Initiators

Primarily an author team of researchers from Northeastern University and other universities; see the paper's author affiliations for details.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Partner organizations

Unverified

> 状态：待核实。

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Authors

Cassano, Federico；Gouwar, John；Nguyen, Daniel；Nguyen, Sydney；Phipps-Costin, Luna；Pinckney, Donald；Yee, Ming-Ho；Zi, Yangtian；Anderson, Carolyn Jane；Feldman, Molly Q；Guha, Arjun；Greenberg, Michael；Jangda, Abhinav

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Current maintainer

nuprl / MultiPL-E official repository team

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Funders

The paper acknowledges partial support from NSF CCF-2052696.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## Design goals

### Abilities measured

Function-level code generation, compilation, and functional tests across programming languages.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 设计动机

Evaluating only Python makes it difficult to judge how well a language model transfers to other programming languages; writing questions by hand for each language is costly.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## Construction

### Question sources

Signatures, types, documentation, and tests from Python HumanEval and MBPP are translated into other languages; the bodies of the reference implementations are not translated.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 出题/构建者背景

Programming-language and program-synthesis researchers.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Review process

A language-specific translator converts the specification and the tests into the target language; compilation and tests are run in a container.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Quality control

The compiler translates the signature, the types, and the doctest or tests, rather than the body of the reference function, then compiles and runs inside a container and sets a timeout. The current HF 3.3 fixes a superfluous Lua stop token; 3.1.1 fixes the type brackets of TypeScript MBPP, and 3.0 fixes some Scala prompts and tests and adjusts whitespace in several languages.

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源3](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）

### 去污染/泄漏控制

Translation cannot guarantee that contamination from the original Python questions is removed; a model may still remember the meaning or translated questions that are already public.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## Data format

### 精确规模与统计口径

```json
{
  "paper_protocol": {
    "languages_including_python": 19
    "multipl_humaneval_instances": 3059
    "multipl_mbpp_instances": 7619
    "note": "The appendix of the paper counts 161/401 parent questions multiplied by 19 languages; this does not represent every current HF configuration."
  }
  "current_hf": {
    "humaneval_target_language_configs": 24
    "mbpp_target_language_configs": 23
    "humaneval_rows": 3811
    "mbpp_rows": 8856
    "per_config": [
      {
        "config": "humaneval-adb"
        "test_rows": 157
      }
      {
        "config": "humaneval-clj"
        "test_rows": 161
      }
      {
        "config": "humaneval-cpp"
        "test_rows": 161
      }
      {
        "config": "humaneval-cs"
        "test_rows": 158
      }
      {
        "config": "humaneval-d"
        "test_rows": 156
      }
      {
        "config": "humaneval-dart"
        "test_rows": 157
      }
      {
        "config": "humaneval-elixir"
        "test_rows": 161
      }
      {
        "config": "humaneval-go"
        "test_rows": 154
      }
      {
        "config": "humaneval-hs"
        "test_rows": 156
      }
      {
        "config": "humaneval-java"
        "test_rows": 158
      }
      {
        "config": "humaneval-jl"
        "test_rows": 159
      }
      {
        "config": "humaneval-js"
        "test_rows": 161
      }
      {
        "config": "humaneval-lua"
        "test_rows": 161
      }
      {
        "config": "humaneval-ml"
        "test_rows": 155
      }
      {
        "config": "humaneval-php"
        "test_rows": 161
      }
      {
        "config": "humaneval-pl"
        "test_rows": 161
      }
      {
        "config": "humaneval-r"
        "test_rows": 161
      }
      {
        "config": "humaneval-rb"
        "test_rows": 161
      }
      {
        "config": "humaneval-rkt"
        "test_rows": 161
      }
      {
        "config": "humaneval-rs"
        "test_rows": 156
      }
      {
        "config": "humaneval-scala"
        "test_rows": 160
      }
      {
        "config": "humaneval-sh"
        "test_rows": 158
      }
      {
        "config": "humaneval-swift"
        "test_rows": 158
      }
      {
        "config": "humaneval-ts"
        "test_rows": 159
      }
      {
        "config": "mbpp-adb"
        "test_rows": 365
      }
      {
        "config": "mbpp-clj"
        "test_rows": 397
      }
      {
        "config": "mbpp-cpp"
        "test_rows": 397
      }
      {
        "config": "mbpp-cs"
        "test_rows": 386
      }
      {
        "config": "mbpp-d"
        "test_rows": 358
      }
      {
        "config": "mbpp-elixir"
        "test_rows": 397
      }
      {
        "config": "mbpp-go"
        "test_rows": 374
      }
      {
        "config": "mbpp-hs"
        "test_rows": 355
      }
      {
        "config": "mbpp-java"
        "test_rows": 386
      }
      {
        "config": "mbpp-jl"
        "test_rows": 390
      }
      {
        "config": "mbpp-js"
        "test_rows": 397
      }
      {
        "config": "mbpp-lua"
        "test_rows": 397
      }
      {
        "config": "mbpp-ml"
        "test_rows": 355
      }
      {
        "config": "mbpp-php"
        "test_rows": 397
      }
      {
        "config": "mbpp-pl"
        "test_rows": 396
      }
      {
        "config": "mbpp-r"
        "test_rows": 397
      }
      {
        "config": "mbpp-rb"
        "test_rows": 397
      }
      {
        "config": "mbpp-rkt"
        "test_rows": 397
      }
      {
        "config": "mbpp-rs"
        "test_rows": 354
      }
      {
        "config": "mbpp-scala"
        "test_rows": 396
      }
      {
        "config": "mbpp-sh"
        "test_rows": 382
      }
      {
        "config": "mbpp-swift"
        "test_rows": 396
      }
      {
        "config": "mbpp-ts"
        "test_rows": 390
      }
    ]
  }
  "warning": "Language-translation rows are not an independent count of new questions; current exclusions differ by language, so the 3.3 data volume must not be applied to the original paper's experiments."
}
```

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### Question types

Function-level program completion and unit tests.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Modalities

文本；代码

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 语言/代码语种

The original paper is Python plus 18 target languages; the current HF card actually lists 24 configurations of HumanEval target languages and 23 configurations of MBPP target languages. The description in natural language is English, and the number of programming languages is not the same as the number of natural languages.

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 难度结构

It inherits HumanEval and MBPP and is not interpreted as 19 independent benchmarks.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Public and hidden splits

The translator, prompts, tests, and execution framework are public; the questions permitted in different languages are not exactly the same.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## Evaluation

### Metrics

pass@k on execution tests.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 评分规则

Code is compiled and run inside a container for the target language; an unbiased pass@k estimate is used.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 运行与提示设置

The original paper uses 200 samples per question; the temperature is 0.2 for pass@1 and 0.8 for pass@10/100.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### Official evaluation scripts

https://github.com/nuprl/MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 可比性警示

The HF revision, the sub-benchmark, the language list, the number of valid questions, the temperature, the number of samples, and k must be fixed. The 3.3 fix affects Lua results. The historical 19 languages, the current 24 and 23 configurations, and the vendor average over 8 languages cannot be substituted for one another. The official GitHub repository contains a prohibition on training, and the HF MIT label does not automatically cover that restriction.

[来源1](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源3](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE)（访问 2026-11-08）

## Current status

### Date checked

2026-11-08

> Access date of the source site for this visit; not the leaderboard run date.

[来源1](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "version": "HF changelog 3.3"
  "hf_revision": "28441b6024e71d4a1c1c0f6bf171c935cd5a43f2"
  "last_modified_kst": "2025-07-15"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1"
      "date": "2026-09-23"
      "note": "Hunyuan-A13B §4.1 and §4.2, and Tables 2–4, actually report MultiPL-E; CRUX-I/O is kept as the same CRUXEval entry and is not counted separately."
    }
  ]
}
```

[来源1](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E)（访问 2026-11-08）；[来源3](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "arxiv_revisions": [
    {
      "version": "v1"
      "date_kst": "2022-08-17"
    }
    {
      "version": "v2"
      "date_kst": "2022-08-19"
    }
    {
      "version": "v3"
      "date_kst": "2022-11-08"
    }
    {
      "version": "v4"
      "date_kst": "2022-12-19"
    }
  ]
  "dataset_changelog_latest": "3.3 (fix for the Lua stop token)"
  "other_notable_fixes": [
    "3.2 added Ada"
    "3.1.1 fixes the TypeScript MBPP type parentheses"
    "3.1 adds Dart"
    "3.0 adds Clojure/Elixir/Haskell/OCaml and several Scala fixes"
  ]
  "date_warning": "These semantic-version titles on the HF card have no per-item dates; API lastModified is not treated as the release date of every version."
}
```

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/nuprl/MultiPL-E)（访问 2026-11-08）

### 饱和性证据

Unverified

> 状态：待核实。

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 污染与已知争议

A conflict of rights: the official GitHub LICENSE is a BSD-derived license with a clause prohibiting machine-learning training, while the license field of the official HF card is MIT. The specific download carrier, the version, and the rights in the upstream parent questions should be verified. They are not labeled MIT as one license.

[来源1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/LICENSE)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 衍生与条目关系

MultiPL-HumanEval and MultiPL-MBPP are two source branches; the current README also recommends the harder Ag-LiveCodeBench-X and the Agnostics paper. The latter is a different task source and is not treated as an upgrade of the same MultiPL-E questions.

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

## Leaderboard snapshot

### 本次榜单采集日

2026-11-08

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### 官方榜源

https://github.com/nuprl/MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 第三方覆盖

https://huggingface.co/spaces/bigcode/multilingual-code-evals

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/spaces/bigcode/multilingual-code-evals)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Hunyuan report, Table 2 / Base / 0-shot / eight-language subset.

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Hunyuan-A13B | 69.33 % | MultiPL-E (the original metric in report Table 2; k is not stated for each entry) | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |
| 2 | Qwen3-A22B | 65.94 % | MultiPL-E (the original metric in report Table 2; k is not stated for each entry) | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |
| 3 | Qwen2.5-72B | 60.5 % | MultiPL-E (the original metric in report Table 2; k is not stated for each entry) | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |
| 4 | Hunyuan-Large-1116 | 59.13 % | MultiPL-E (the original metric in report Table 2; k is not stated for each entry) | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |

- Python/C++/Java/PHP/TypeScript/C#/Bash/JavaScript; the data revision and k are not stated item by item

- A comparison of vendor reports, not the official unified live leaderboard for MultiPL-E

#### Original paper v4 §5.1 / MultiPL-HumanEval / Python

| Order in source | Model and configuration | Score | Metric | Source record / run time | Source (collection date) |
|---|---|---|---|---|---|
| 1 | Codex | 45.9 % | pass@1 | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2208.08227)（2026-11-08） |
| 2 | CodeGen | 19.2 % | pass@1 | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2208.08227)（2026-11-08） |

- 200 samples per question; pass@1, temperature 0.2.

- A historical pass@1 stated explicitly in the body of the paper; not a total score over all languages

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### 覆盖范围与限制

Table 2 of Hunyuan was read back for the eight-language scores of all 4 Base models; two passages on Python in the original paper put pass@1 on a separate track explicitly. Values are taken only from numbers in the text, and they are not estimated from bar charts. The entry to the BigCode HF Space has been opened, but the shell page did not return a complete current sub-leaderboard that can be checked, and a live entry point is not written up as a real-time SOTA that has been obtained.

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源3](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源4](https://huggingface.co/spaces/bigcode/multilingual-code-evals)（访问 2026-11-08）

## Contact

### 公开研究邮箱

Unverified

> 状态：待核实。

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 项目反馈入口

https://github.com/nuprl/MultiPL-E/issues

> Public repository feedback entry point; no question was sent.

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 官方公开社交入口

Unverified

> 状态：待核实。

> The listed official materials were searched this time, but exact verification of this field was not completed; this does not mean that the official source has not made it public.

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 公开渠道/隐私边界

Only officially public project feedback channels are included; when generated code is executed, the repository's recommendation to use container isolation is followed, and run examples are not treated as local instructions that can be executed directly.

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）

## Original files

### 源站PDF

https://arxiv.org/pdf/2208.08227

> Archived as the PDF provided by the source site at the time of download; the paper version and the benchmark version are recorded separately.

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### PDF SHA-256

b905b9874ffcb4cee63f74cdc30524eae97013691e79313049ad72c6d6197580

> The original bytes downloaded from the source site, neither compressed nor rewritten; the SHA-256 and the byte count were computed from this download.

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### PDF bytes

443169

> The original bytes downloaded from the source site, neither compressed nor rewritten; the SHA-256 and the byte count were computed from this download.

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### Folder

```json
{
  "id": "1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

### 其他官方文档

```json
[
  {
    "type": "Chinese-language introductory Google Doc"
    "id": "1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM"
    "webViewLink": "
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/abs/2208.08227"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/html/2609.27284v1"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://arxiv.org/pdf/2208.08227"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://github.com/nuprl/MultiPL-E/blob/main/LICENSE"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://github.com/nuprl/MultiPL-E/blob/main/README.md"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/nuprl/MultiPL-E"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://huggingface.co/spaces/bigcode/multilingual-code-evals"
    "accessed": "2026-11-08"
  }
  {
    "type": "Official/research sources opened for verification"
    "url": "https://nuprl.github.io/MultiPL-E/"
    "accessed": "2026-11-08"
  }
]
```

> The official original materials and the rewritten Chinese introduction are labeled separately; the HTML methods page is not the PDF of the original paper.

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）；[来源2]( 2026-11-07）；[来源3](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）；[来源4](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源5](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源6](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE)（访问 2026-11-08）；[来源7](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源8](https://huggingface.co/datasets/nuprl/MultiPL-E)（访问 2026-11-08）；[来源9](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源10](https://huggingface.co/spaces/bigcode/multilingual-code-evals)（访问 2026-11-08）；[来源11](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）

### 原始PDF

```json
{
  "id": "1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

## Changelog

### Changelog

```json
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
    "date": "2026-11-08"
    "timezone": " (, UTC+9)"
    Latest review
  }
]
```

[来源1](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）
