# SWE-bench Multimodal

> Benchmark Constitution, in-depth review 2026-11-08. Existence has been verified; a research snapshot of the official materials, with what is unknown kept as Unverified; trending: B

SWE-bench Multimodal brings repair of visual software issues into repository-level agent evaluation. Images are not merely decorative input. The 2026 v2 on the official site retains 480 reproducible tasks, but the original paper, the historical project description, and the current HF card still carry more than one set of figures for the older question counts. This entry sets that evidence side by side and notes that the revision must be locked. HF main and the 480-question protocol cannot automatically be treated as fully identical.

[Source 1](https://arxiv.org/abs/2410.03859) (accessed 2026-11-08); [Source 2](https://github.com/SWE-bench/SWE-bench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal) (accessed 2026-11-08); [Source 4](https://www.vals.ai/benchmarks/swebench-multimodal) (accessed 2026-11-08)

## Basic information

### Short name

SWE-bench Multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Full name

SWE-bench Multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Benchmark version

Multimodal v2

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### Paper version

v1 (paper version; not equal to the dataset version)

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### Release date

2026-09-01（Multimodal v2）

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### Section

Code

> Editorial filing. Only the main section is counted.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 领域

```json
[
  "多模态"
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 许可与适用范围

The official harness code is MIT (the LICENSE has been opened); the tasks, the patches, and the visual assets involve 17 upstream repositories and the copyrights of the original authors, and it cannot be asserted that every material is MIT merely because the harness is MIT.

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）

### Paper

https://arxiv.org/abs/2410.03859

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Code

https://github.com/SWE-bench/SWE-bench

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

### 数据

https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal

[来源1](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源2](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

### Official entry

https://www.swebench.com/multimodal.html

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Paper title

SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

## Origin and maintenance

### Initiators

Research team at Stanford University and Princeton University

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 合作/参与机构

Paper author affiliations include Stanford, Princeton, Cornell, the Tübingen AI Center, and Meta AI; not every author is from the first two universities.

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### Authors

```json
[
  "John Yang"
  "Carlos E. Jimenez"
  "Alex L. Zhang"
  "Kilian Lieret"
  "Joyce Yang"
  "Xindi Wu"
  "Ori Press"
  "Niklas Muennighoff"
  "Gabriel Synnaeve"
  "Karthik R. Narasimhan"
  "Diyi Yang"
  "Sida I. Wang"
  "Ofir Press"
]
```

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### Maintainer

Research team at Stanford University and Princeton University

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Funders

Open Philanthropy, Oracle, and NSF Grant No. 2239363 (acknowledgments in the original paper); the experiments were run by the Stanford and Princeton authors on Princeton servers, and the Meta authors served in an advisory role.

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

## Design goals

### Abilities measured

Uses screenshots or short screen recordings to understand problems in real JavaScript repositories, locate them, and repair the code.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Design background

Text-only SWE-bench cannot cover cases in which visual evidence, such as charts, interfaces, and syntax highlighting, determines the requirements.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## Construction

### Question sources

SWE-bench is extended from visual issues in real repositories; v2 removes tests known to be unstable or impossible to score and rebuilds the Docker environment and the handling of visual assets.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 出题者背景

The research team builds the tasks from real JavaScript/TypeScript issue–PR pairs; the paper uses human experts to verify that vision is necessary, and judges that for 83.5% of instances the image is information required to solve the problem.

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### Review process

The original pipeline filters for issues or tests that contain visual content, builds JavaScript containers and executable tests, and then has human experts review whether the vision is necessary. v2 of 2026-09-01 further removes instances that are flaky or ungradeable.

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源2](https://www.swebench.com/multimodal.html)（访问 2026-11-08）

### Quality control

v2 removes flaky/ungradeable tests and rebuilds the environment, resolving dependencies and browser drift.

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 污染控制

Instance ids contain upstream fix PR numbers, creating a risk of looking up answers online; Vals disables the network throughout and downloads visual assets in advance.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## Data format

### 题量

The v2 official site retains 480 tasks (the Vals methods say 11 repositories). The historical description on the official site has 517 visual issues. The arXiv v1 abstract has 617, and the introduction in the body has 619. The current HF card also says 612=dev102+test510, with 17 repositories, and the viewer shows 580 rows. The version and page counts above are not equivalent to one another. The v2 question count follows the official site's 480. The mapping to a specific HF revision is Unverified.

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源3](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 任务形式

issue text and image input, with a code diff as output.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Modalities

```json
[
  "文本"
  "图像"
  "代码"
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### Languages

Code: JavaScript/TypeScript, including HTML/CSS; issues are mainly in English and also include Chinese. The official HF card states that they were not cleaned by language.

[来源1](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### Difficulty

Real front-end and visual software repair cannot fully replace visual evidence with a text requirement; the original paper’s SWE-agent solve rate of 12.2% is an older historical track, not the current score of the 480-question v2.

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### Public and hidden splits

The v2 official site states that the full test split and the tooling are open source; the official README points to an HF address, but the current HF card still describes the old dev102/test510, and the viewer total is 580, which does not agree with 480 in v2. The data revision and the list of instances must be pinned before reproduction, and HF main cannot be assumed to be exactly 480.

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源3](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

The accuracy with which tests judge an issue to be resolved (Accuracy).

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 评分

Vals runs mini-swe-agent once and attaches pre-downloaded screenshots to the first message; the upstream harness decides that a fix succeeded by the repository's own tests.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 运行设置

mini-swe-agent; the issue text, a screenshot attached on the first turn, a shell, and an independent sandbox; each model is run once per question, and the error bar is the binomial standard error.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 评测工具

The official SWE-bench harness supports swebench eval multimodal, and it also keeps python -m swebench.harness.run_evaluation; the HF card provides dataset_name, split=test, and the command that checks regression against the gold patch.

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）

### Comparability

It is in the same series as the existing swe-bench-verified, with a different task domain and modality, and it is not a new version of the same Verified questions; Vals disables the network, so the results cannot be compared with networked results that can look up the official patch.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## Current status

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
  "version": "Multimodal v2"
  "evidence_2026_h2": [
    {
      "url": "https://www.vals.ai/benchmarks/swebench-multimodal"
      "date": "2026-11-05"
      "date_type": "source_calendar_date"
      "note": "The current Vals AI methods and leaderboard actually evaluate multiple models; the current presentation is mainly from a single institution and does not represent broad industry adoption."
    }
  ]
}
```

> The heat grade is adopted from the candidate; only evidence that has been opened and can be verified is retained. A does not guarantee that every version received independent reruns by multiple institutions.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2024-10-05"
    "timezone": ""
  }
]
```

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 饱和与能力边界

The current high on Vals no-internet v2 is 70.21%, still short of a perfect score; the highest internet-enabled diagnostic result, 77.92%, cannot be used in place of the official no-internet leaderboard.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 风险与争议

With network access, the answer can be looked up from the number of the fixing PR inside instance_id. In the Vals diagnostic, the networked scores of three groups of Muse models are clearly higher than the official scores with the network forbidden, and diagnostic scores do not enter the official leaderboard. The HF card also notes that a small number of Carbon accessibility tests need an online rule engine and therefore fluctuate independently of the patch; the current HF card and the v2 question count conflict, so the revision must be pinned.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）

### 系列与衍生关系

It belongs to the same series as the existing swe-bench-verified, but the input modality and the task domain differ, and Multimodal v2 is recorded on its own; of the original 517 questions, 480 that can be reproduced are now kept.

> Already deduplicated against the existing_slugs list; relations among versions are based on the methods pages that are listed, and a different task domain is not treated as an update of the same questions.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## Leaderboard snapshot

### Snapshot date

2026-11-08

[Source 1](https://arxiv.org/abs/2410.03859) (accessed 2026-11-08); [Source 2](https://github.com/SWE-bench/SWE-bench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal) (accessed 2026-11-08); [Source 4](https://www.vals.ai/benchmarks/swebench-multimodal) (accessed 2026-11-08)

### Official entry

https://www.swebench.com/multimodal.html

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-08）

### 独立来源

https://www.vals.ai/benchmarks/swebench-multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 分来源与协议结果

#### Vals v2 / no network

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Claude Opus 5.5 | 70.21 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 2 | Claude Fable 5.1 | 61.25 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 3 | Claude Sonnet 5.5 | 58.33 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 4 | Gemini 4 Argon | 56.04 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 5 | Wonder Full | 47.29 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 6 | DeepSeek V4.1 Flash | 46.46 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 7 | Wonder | 45.63 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 8 | Kimi K3 | 44.17 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 9 | Claude Haiku 5.5 | 43.96 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 10 | GPT-6.1 Sol | 43.54 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 11 | GPT-6 Astra | 43.33 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 12 | Muse Spark 1.3 Max | 43.13 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 13 | Inkling 2 Small | 43.13 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 14 | Grok 4.7 | 42.92 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 15 | Qwen 3.8 Max | 42.5 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 16 | MiMo V2.6 Pro | 41.25 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 17 | Gemini 3.8 Flash | 40.83 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 18 | Step 5 Preview | 40.83 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 19 | GPT-6 Luna | 37.5 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 20 | MiniMax-M3 | 33.33 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 21 | Mistral Large 4 Preview | 33.13 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |

#### Vals v2 / network diagnostic

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | Muse Spark 1.2 | 62.71 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 | 69.17 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 Max | 77.92 | Accuracy (%) | {"diagnostic":true} |

#### Vals v2 / no network paired diagnostic

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | Muse Spark 1.2 | 41.25 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 | 42.08 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 Max | 43.33 | Accuracy (%) | {"diagnostic":true} |

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 覆盖与时效

The full official Vals no-internet leaderboard has 21 rows, plus 6 diagnostic rows for three models × with and without internet. Diagnostic scores are tracked separately from official ranking scores. The body text currently readable on the official project page has no independent live scores, and Vals is not labeled as the original authors' official leaderboard. Historical scores from the 2024 paper are not presented as v2.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）；[来源2](https://www.swebench.com/multimodal.html)（访问 2026-11-08）

## Contact

### 公开工作邮箱

```json
[
  "johnby@stanford.edu"
  "carlosej@cs.princeton.edu"
]
```

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 官方反馈

https://github.com/SWE-bench/SWE-bench/issues

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

### 公开社区

Unverified

> The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 隐私边界

Unverified

> The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## Original files

### 源站PDF

https://arxiv.org/pdf/2410.03859

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

### PDF SHA-256

4fa09c3734547e8ba4a5288e7e8d9273d1136c70295e4f91ef3592df0ead2a71

> Byte count of the PDF actually downloaded. It was not uploaded.

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

### PDF bytes

```json
4379827
```

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

### Folder

Unverified

> The listed official materials have been consulted, and exact verification of this field is not yet complete; this is not equivalent to Not disclosed by the official source.

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "type": "Official methods or project page"
    "url": "https://www.vals.ai/benchmarks/swebench-multimodal"
    "accessed": "2026-11-07"
  }
  {
    "type": "Opened primary material"
    "url": "https://arxiv.org/abs/2410.03859"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://github.com/SWE-bench/SWE-bench"
    "accessed": "2026-11-08"
  }
  {
    "type": "Opened primary material"
    "url": "https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal"
    "accessed": "2026-11-08"
  }
]
```

[Source 1](https://arxiv.org/abs/2410.03859) (accessed 2026-11-08); [Source 2](https://github.com/SWE-bench/SWE-bench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal) (accessed 2026-11-08); [Source 4](https://www.vals.ai/benchmarks/swebench-multimodal) (accessed 2026-11-08)

### PDF归档

Unverified

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## Changelog

```json
[
  {
    "date": "2026-11-07"
    "timezone": " ()"
    Latest review
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    Latest review
  }
]
```

[Source 1](https://arxiv.org/abs/2410.03859) (accessed 2026-11-08); [Source 2](https://github.com/SWE-bench/SWE-bench) (accessed 2026-11-08); [Source 3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal) (accessed 2026-11-08); [Source 4](https://www.vals.ai/benchmarks/swebench-multimodal) (accessed 2026-11-08)
