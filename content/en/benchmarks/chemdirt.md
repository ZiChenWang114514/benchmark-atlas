# ChemDIRT

> Benchmark Constitution, in-depth review: 2026-11-08. Supplemented from evidence; items that are not confirmed remain Unverified, and historical scores from papers are recorded separately from the live leaderboard.

ChemDIRT diagnoses the stability of chemistry LLMs along three axes, task, prompt rewriting, and molecular representation, rather than compressing them into one total score. The paper contains 33 task settings and eight categories of task. Image-to-structure, retrosynthesis, and property regression must keep their own metrics. The current README claims 4,484 questions, while the HF card states 4,482 rows. The difference between these two records still requires an explanation from the maintainer, and it cannot be covered with "4.48k."

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

## Basic information

### Short name

ChemDIRT

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### Full name

ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 版本边界

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### Paper version

v1; latest paper date 2026-08-21

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### Release date

2026-08-21 (date of the first arXiv version; not an inferred date on which the data went online).

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 板块

Chemistry

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

> The editorial section follows the selection list. It does not mean the benchmark measures only that section.

### 领域

```json
[
  "Instruction, representation, and task robustness"
]
```

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 许可与限制

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### Paper

https://arxiv.org/abs/2608.21504

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### Code

https://github.com/einae-nd/ChemDIRT

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### Dataset

https://huggingface.co/datasets/Einae/ChemDIRT

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### Official homepage

https://github.com/einae-nd/ChemDIRT

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 论文题名

ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

## Origin and maintenance

### Initiators

Author affiliation in the paper: University of Notre Dame; a sole legal owner is not inferred from this.

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### Partner organizations

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### Authors

```json
[
  "Inae, Eric"
  "Gunn, Tim"
  "Bond, Chris"
  "Jiang, Meng"
]
```

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 维护入口

The data-release accounts einae-nd/ChemDIRT and Einae.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 资助披露

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

## Design goals

### 测量对象

Remains reliable under rewrites of the instruction and changes of molecular representation for the same chemistry task; robustness is diagnosed across eight classes of tasks.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 既有评测的缺口

Scores from a single prompt or representation easily overestimate stable ability, and the task average conceals sensitivity to representation and prompt.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

## Construction

### 题源

Existing tasks on QM9, ZINC, ChEMBL, and PubChem molecules, and on MoleculeNet, ChemLLMBench, and others; RDKit builds computable ground truth.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 构建人员

Eric Inae、Tim Gunn、Chris Bond、Meng Jiang，Notre Dame。

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 审核

GPT-5Pro generates ten prompt templates, which are checked by hand, and the actual evaluation uses the first four; inherited data are cleaned.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 质控

The official source provides a bundled data/image verification script; run results save the raw predictions, task metrics, configuration, input hash, and checkpoint.

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### 去污染及边界

It inherits public tasks and molecular libraries, so prompt rewriting cannot be treated as removal of pretraining contamination; an independent audit of model training corpora is Unverified.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

## Data format

### 规模与计数口径

```json
{
  "readme_questions": 4484
  "readme_molecular_images": 300
  "hf_card_train_records": 4482
  "paper_task_settings": 33
  "warning": "README 4484 and the current HF data card, 4482, do not agree; they are not rounded into agreement, and the reason the two questions are missing is not inferred. 33 is a task setting, not a question count."
}
```

[来源1](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/Einae/ChemDIRT/blob/main/README.md)（访问2026-11-08）；[来源3](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）

### Question types

Description, classification, design, analysis, regression, computation, mechanism, and relation tasks.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### Modalities

Molecular text representations and molecular images.

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### Languages

English natural language; SMILES/IUPAC chemical representations.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### Difficulty

Instruction and representation perturbations are the main axes of difficulty; there is no unified difficulty level.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 划分与公开范围

The HF metadata publish a single split named train, with 4,482 rows; it is a release container and does not prove a separate supervised-training process or a hidden test set; the local package described in the README claims 4,484 questions, and the conflict of basis is retained.

[来源1](https://huggingface.co/datasets/Einae/ChemDIRT/blob/main/README.md)（访问2026-11-08）；[来源2](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）

## Evaluation

### Metrics

Classification uses accuracy. Molecular design reports exact match and similarity of MACCS, Morgan, and RDK fingerprints. Numeric tasks report log RMSE, MAE, relative RMSE, and RMSE.

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 评分

Structures are parsed and then compared; numeric tasks compute error; the mean and standard deviation under four prompts are reported and are not treated as a confidence interval.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 提示与运行条件

For each task the paper uses GPT-5 Pro to generate 10 templates and checks their semantics by hand; the reported evaluation uses the first 4 templates that pass validation.

[来源1](https://arxiv.org/html/2608.21504v1)（访问2026-11-07）

### 官方评测入口

src/cli.py runs inference and scoring; scripts/validate_data.py checks the data and the images.

[来源1](https://raw.githubusercontent.com/einae-nd/ChemDIRT/main/README.md)（访问2026-11-07）

### 可比性边界

Metrics of different tasks have no common total score; results for image-to-structure, retrosynthesis, and regression cannot be ranked together. A model label and the specific API snapshot must be distinguished.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

## Current status

### 复核时间

2026-11-08

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）；[来源2](https://arxiv.org/abs/2608.21504)（访问2026-11-08）

### 当前版本

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### 论文修订与后续使用

```json
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.21504v1"
      "date": "2026-08-21"
      "note": "The original ChemDIRT paper proposes in H2, and actually evaluates, robustness under multiple instructions, multiple molecular representations, and eight classes of chemistry tasks."
    }
  ]
  "evidence_boundary": "A citation is not a rerun; this page keeps the historical experiments in the paper separate from the current leaderboard."
  "paper_metadata": {
    "title": "ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation"
    "authors": [
      "Inae, Eric"
      "Gunn, Tim"
      "Bond, Chris"
      "Jiang, Meng"
    ]
    "release": "2026-08-21"
    "latest": "2026-08-21"
    "version": "v1"
  }
  "arxiv_revisions_kst": [
    {
      "version": "v1"
      "submitted_at_kst": "2026-08-22"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）

### Saturation

There is no valid unified saturation figure; Llama3 on ClinTox can range from 0.095 to 0.905 under different prompts, which indicates a stability problem.

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 风险与冲突

Taking over a public molecule library and its tasks, and rewriting the prompts, is not the same as removing pretraining contamination. The overall standard deviation among the four prompts is not a confidence interval for sampling. The question count of 4,484 in the README and of 4,482 on the HF card needs an explanation from the maintainers. No LICENSE file was found, and the HF card does not mark a license. This remains Unverified.

[来源1](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/Einae/ChemDIRT/blob/main/README.md)（访问2026-11-08）；[来源3](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）

### 衍生与后续工作

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

## Leaderboard snapshot

### 快照时间

2026-11-08 (actual review date; batch label 2026-11-07).

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）

### 官方榜入口

https://github.com/einae-nd/ChemDIRT

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 第三方榜入口

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### 逐轨结果

```json
[
  {
    "rank": null
    "model": "Claude-Sonnet-5"
    "score": 0.633
    "metric": "exact match"
    "track": "Paper Table V / image→SMILES"
    "source_url": "https://arxiv.org/pdf/2608.21504"
    "accessed": "2026-11-08"
    "std_across_prompts": 0.028
    "unit": "比例"
  }
  {
    "rank": null
    "model": "Claude-Sonnet-5"
    "score": 0.687
    "metric": "exact match"
    "track": "Paper Table V / image→IUPAC"
    "source_url": "https://arxiv.org/pdf/2608.21504"
    "accessed": "2026-11-08"
    "std_across_prompts": 0.039
    "unit": "比例"
  }
  {
    "rank": null
    "model": "RetroDFM-R"
    "score": 0.685
    "metric": "exact match"
    "track": "Paper Table IV / SMILES retrosynthesis."
    "source_url": "https://arxiv.org/pdf/2608.21504"
    "accessed": "2026-11-08"
    "std_across_prompts": 0.023
    "unit": "比例"
  }
]
```

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）

### 覆盖边界

All three are locked to the v1 paper and structured on three tracks, image→SMILES, image→IUPAC, and SMILES retrosynthesis; rank=null because this is not a complete ranking of one and the same task. ± is the overall standard deviation across four prompts, not a confidence interval; the current real-time SOTA is not claimed.

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-08）；[来源2](https://github.com/einae-nd/ChemDIRT)（访问2026-11-08）

## Contact

### 公开研究联系

```json
[
  "einae@nd.edu"
  "tgunn2@nd.edu"
  "cbond@nd.edu"
  "mjiang2@nd.edu"
]
```

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 项目反馈

https://github.com/einae-nd/ChemDIRT/issues

[来源1](https://github.com/einae-nd/ChemDIRT)（访问2026-11-07）

### 官方社交入口

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

### 联系信息边界

Unverified

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

> The original paper and the official entry points have been checked, but this field did not receive sufficient evidence; this does not establish that it is Not disclosed.

## Original files

### 原始PDF

https://arxiv.org/pdf/2608.21504

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### PDF SHA-256

70a4ee8128ed69e69bb9a7394b1a823571e1738592986f7fc345603826a12524

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-07）

### PDF bytes

466313

[来源1](https://arxiv.org/pdf/2608.21504)（访问2026-11-07）

### 目录

```json
{
  "id": "1Z1arqpVyZtzUnhGEUznM1Oh02lQKFmh5"
  "webViewLink": "
}
```

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

### 其他官方材料

```json
[
  {
    "type": "Chinese introduction"
    "id": "1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58"
    "webViewLink": "https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit"
  }
]
```

[来源1](https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit)（访问2026-11-07）

### 论文归档

```json
{
  "id": "186sLc62vIHc-Ng9ZKqoGmn37H6CvHjjB"
  "webViewLink": "
}
```

[Source 1](https://arxiv.org/abs/2608.21504) (accessed 2026-11-07)

## Changelog

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
    "timezone": ""
    Latest review
  }
]
```

[来源1](https://arxiv.org/abs/2608.21504)（访问2026-11-08）
