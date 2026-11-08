# PubMedQA

> In-depth verification: 2026-11-08. The access date is not the publication date or the experiment run date; unknowns are retained, and "Not disclosed" is not inferred.

PubMedQA uses real biomedical research titles as questions and asks for a yes/no/maybe prediction from the abstract with the conclusion removed. PQA-L is 1,000 questions annotated by two experts. PQA-A is weakly labeled automatically by rules, and it is not a set of more than 200,000 human-written questions. HF packaging all of PQA-L as train does not change the official 500-question test set. Training directly on the whole package would leak the test set.

Latest review

## Basic information

### Short name

PubMedQA

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### Full name

PubMedQA

> The official name is used; when no verified expansion of the full name exists, the original name is retained, and the title of the paper is not mistaken for the full name of the benchmark.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### Dataset version

The original three configurations of PubMedQA are pqa_labeled, pqa_unlabeled, and pqa_artificial; the HF files and the official test IDs define the set that is actually evaluated, and a semantic version number is not invented.

[1](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）

### Paper version

EMNLP-IJCNLP 2019 formal paper D19-1259; arXiv:1909.06146v1.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 发布时间

First preprint release: 2019-09-13 20:18:20; the formal conference paper is 2019-11.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 板块

Biology and medicine

> Benchmark Constitution editorial filing. A cross-disciplinary entry is counted only in its main section. Other subjects are found through tags.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）

### Subfields

```json
[
 "Biology and medicine"
]
```

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### License

The official repository is MIT; this does not automatically represent the copyright terms of every original PubMed abstract.

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/LICENSE)（访问 2026-11-07）

### Paper

https://aclanthology.org/D19-1259/

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 代码

https://github.com/pubmedqa/pubmedqa

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### Dataset

https://github.com/pubmedqa/pubmedqa

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### Official homepage

https://pubmedqa.github.io/

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 论文题名

PubMedQA: A Dataset for Biomedical Research Question Answering

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## Origin and maintenance

### Initiators

```json
[
 "University of Pittsburgh"
 "Carnegie Mellon University"
 "Google AI (by the author affiliation in the paper)"
]
```

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 合作单位

```json
[
 "University of Pittsburgh"
 "Carnegie Mellon University"
 "Google AI (a co-author affiliation in the paper; not an additionally inferred institutional agreement)."
]
```

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### Authors

```json
[
 "Qiao Jin"
 "Bhuwan Dhingra"
 "Zhengping Liu"
 "William Cohen"
 "Xinghua Lu"
]
```

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### Maintainer

The pubmedqa official GitHub organization; Qiao Jin is listed in the README as the project contact.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### Funders

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## Design goals

### 目标能力

Answer research questions from medical-paper abstracts, with particular attention to understanding of quantitative evidence.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 相对既有评测的缺口

Existing biomedical QA often leans toward extraction of facts, and the scale of expert annotation is small; PubMedQA requires inferring yes/no/maybe from the abstract of the original study, especially from quantitative results, and it provides an independent long_answer for auxiliary supervision.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

## Construction

### 题目与标签来源

PQA-L/U takes real question-style PubMed article titles and abstracts with the conclusion removed; PQA-A turns declarative titles into questions and yes/no labels automatically, according to part of speech and the state of negation, and these are not 211.3k questions written by humans one by one.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 出题/标注背景

PQA-L was annotated by two qualified M.D. candidates; the original text does not describe them as practicing specialists.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### Review process

Annotator 1 sees the question, the context, and the conclusion (reasoning-free); annotator 2 sees only the question and the context with the conclusion removed (reasoning-required). Disagreement is discussed; if agreement cannot be reached, the question is deleted.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### Quality control

Humans screen out questions that cannot be answered with yes/no/maybe; two people discuss them in order to remove ambiguity. PQA-U uses rules to exclude wh-questions and options that name more than one entity, and agreement with annotator 1 on identifying whether a question can be answered exceeds 93%, which is not treated as the accuracy of the labels on the test set.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 去污染与隔离

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## Data format

### Size

```json
{
 "pqa_labeled": 1000
 "pqa_unlabeled": 61249
 "pqa_artificial": 211269
 "basis": "Exact row counts on the HF data card; the original paper's 1k/61.2k/211.3k are rounded descriptions, not exact row counts."
}
```

[1](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）

### Question types

Answer three-class yes/no/maybe questions on the basis of research abstracts.

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### Modalities

Research questions and the corresponding abstract text.

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### Languages

English (the HF dataset card specifies en and monolingual).

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### Difficulty

Reading and inference in biomedical research. The paper reports 78.0% accuracy for the single-person reasoning-required condition and 90.4% for the reasoning-free condition. There is no unified per-question difficulty label, and the two human conditions cannot be treated as the same.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 公开/隐藏划分

The official PQA-L split has 500 test items. Another 500 are used for 10-fold cross-validation, with 450 for training and 50 for validation in each inner fold. All three HF configurations are packaged as train, but that packaging cannot override the official isolation of the test set. PQA-U has no official split script. PQA-A is used for pretraining.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[3](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）

## Evaluation

### Metrics

The official reasoning-required leaderboard reports Accuracy (%) and Macro-F1 (%); Macro-F1 is NA for some models.

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### 判分

After model predictions are aligned by PMID, performance is computed with the official evaluation.py.

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 提示/推理设置

The original paper uses supervised fine-tuning, including BioBERT, with multi-stage training from PQA-A to PQA-U to PQA-L and with auxiliary supervision from a long-answer bag-of-words; the reasoning-required test gives only the question and the context with the conclusion removed. Later LLM prompting methods follow the setting recorded for each submission.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 官方实现

evaluation.py: the keys of the prediction JSON are PMIDs, and the values are yes/no/maybe; run python evaluation.py PREDICTIONS_PATH.

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 可比性边界

The official PQA-L test has 500 questions; HF marks all 1,000 PQA-L samples as train only as a packaging configuration, not as the official training and test protocol. reasoning-free can see the conclusion and cannot be compared directly with reasoning-required; PQA-A is weakly labeled pretraining data, not a test set.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

## Current status

### 核验日

2026-11-08

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 本次版本快照

The HF card, as read here, still lists PQA-L 1000, PQA-U 61249, and PQA-A 211269; the names of the HF splits are not used in place of the official test protocol of 500 questions.

[1](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）

### Paper revisions

```json
[
 {
 "version": "arXiv v1"
 "submitted_at": "2019-09-13"
 }
 {
 "version": "EMNLP-IJCNLP formal paper"
 "date": "2019-11"
 "identifier": "D19-1259"
 }
]
```

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### Saturation

The first place currently visible on the official website is 82.0% (GPT-4 Medprompt, 2023-11-28), which is short of 100%; this is an official leaderboard of relatively early submissions, and it does not represent the best result of every model in 2026 or show that the benchmark is already saturated.

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 污染/限制/争议

PQA-L has only 1,000 questions, and the test of 500 questions must be kept strictly isolated. The train package on HF contains the whole of PQA-L, and training on it directly would leak the test. PQA-A is generated by a negation rule, and yes accounts for 92.8%, so the labels are biased. The scale of contamination from modern pretraining is Unverified.

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 衍生与相关版本

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## Leaderboard snapshot

### 采集日期

2026-11-08 (collection date, not the experiment run date)

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 官方结果入口

https://pubmedqa.github.io/

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### 第三方入口

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| Official public submission leaderboard / PQA-L test | 1 | [GPT-4 (Medprompt) Microsoft (Nori et al. 2023)](https://pubmedqa.github.io/) | 82.0 | reasoning-required test Accuracy (%) | Nov 28, 2023 |
| Official public submission leaderboard / PQA-L test | 2 | [Med-PaLM 2 Google Research & DeepMind (Singhal et al. 2023)](https://pubmedqa.github.io/) | 81.8 | reasoning-required test Accuracy (%) | May 16, 2023 |
| Official public submission leaderboard / PQA-L test | 3 | [MEDITRON EPFL (Chen et al. 2023)](https://pubmedqa.github.io/) | 81.6 | reasoning-required test Accuracy (%) | Nov 27, 2023 |
| Official public submission leaderboard / PQA-L test | 4 | [Palmyra-Med Writer Inc. (Kamble et al. 2023)](https://pubmedqa.github.io/) | 81.1 | reasoning-required test Accuracy (%) | Jul 6, 2023 |
| Official public submission leaderboard / PQA-L test | 5 | [AntGLM-Med Ant Group (Li et al. 2023)](https://pubmedqa.github.io/) | 80.6 | reasoning-required test Accuracy (%) | Dec 1, 2023 |
| Official public submission leaderboard / PQA-L test | 6 | [GPT-4-base Microsoft & OpenAI (Nori et al. 2023)](https://pubmedqa.github.io/) | 80.4 | reasoning-required test Accuracy (%) | Apr 12, 2023 |
| Official public submission leaderboard / PQA-L test | 7 | [Claude 3 Anthropic (Anthropic, 2024)](https://pubmedqa.github.io/) | 79.7 | reasoning-required test Accuracy (%) | Mar 4, 2024 |
| Official public submission leaderboard / PQA-L test | 8 | [GPT-3.5 + Z-Code++ Microsoft Azure AI (He et al. 2022)](https://pubmedqa.github.io/) | 79.6 | reasoning-required test Accuracy (%) | Jan 11, 2023 |
| Official public submission leaderboard / PQA-L test | 9 | [Flan-PaLM (3-shot) Google Research & DeepMind (Singhal et al. 2022)](https://pubmedqa.github.io/) | 79.0 | reasoning-required test Accuracy (%) | Dec 26, 2022 |
| Official public submission leaderboard / PQA-L test | 10 | [HEAL DeepScribe Inc (Yuan et al. 2024)](https://pubmedqa.github.io/) | 78.4 | reasoning-required test Accuracy (%) | Mar 14, 2024 |
| Official public submission leaderboard / PQA-L test | 11 | [Codex (5-shot) Technical University of Denmark & Copenhagen University Hospital (Liévin et al. 2022)](https://pubmedqa.github.io/) | 78.2 | reasoning-required test Accuracy (%) | Dec 20, 2022 |
| Official public submission leaderboard / PQA-L test | 12 | [Human Performance University of Pittsburgh & Carnegie Mellon University (Jin et al. 2019)](https://pubmedqa.github.io/) | 78.0 | reasoning-required test Accuracy (%) | Sep 13, 2019 |
| Official public submission leaderboard / PQA-L test | 13 | [Galactica Meta AI (Taylor et al. 2022)](https://pubmedqa.github.io/) | 77.6 | reasoning-required test Accuracy (%) | Nov 16, 2022 |
| Official public submission leaderboard / PQA-L test | 14 | [GatorTronGPT University of Florida & NVIDIA (Peng et al. 2023)](https://pubmedqa.github.io/) | 77.6 | reasoning-required test Accuracy (%) | May 22, 2023 |
| Official public submission leaderboard / PQA-L test | 15 | [MediSwift-XL Cerebras Systems (Thangarasa et al. 2024)](https://pubmedqa.github.io/) | 76.8 | reasoning-required test Accuracy (%) | Mar 4, 2024 |
| Official public submission leaderboard / PQA-L test | 16 | [GPT-4 Microsoft & OpenAI (Nori et al. 2023)](https://pubmedqa.github.io/) | 75.2 | reasoning-required test Accuracy (%) | Mar 20, 2023 |
| Official public submission leaderboard / PQA-L test | 17 | [Reka Core Reka (Ormazabal et al. 2024)](https://pubmedqa.github.io/) | 74.6 | reasoning-required test Accuracy (%) | Apr 18, 2024 |
| Official public submission leaderboard / PQA-L test | 18 | [PubMedGPT Stanford University (Bolton et al. 2022)](https://pubmedqa.github.io/) | 74.4 | reasoning-required test Accuracy (%) | Dec 15, 2022 |
| Official public submission leaderboard / PQA-L test | 19 | [DRAGON Stanford University & EPFL (Yasunaga et al. 2022)](https://pubmedqa.github.io/) | 73.4 | reasoning-required test Accuracy (%) | Oct 17, 2022 |
| Official public submission leaderboard / PQA-L test | 20 | [PMC-LLaMA Shanghai Jiao Tong University (Wu et al. 2023)](https://pubmedqa.github.io/) | 73.4 | reasoning-required test Accuracy (%) | Apr 27, 2023 |
| Official public submission leaderboard / PQA-L test | 21 | [BioLinkBERT (large) Stanford University (Yasunaga et al. 2022)](https://pubmedqa.github.io/) | 72.2 | reasoning-required test Accuracy (%) | Mar 29, 2022 |
| Official public submission leaderboard / PQA-L test | 22 | [BioLinkBERT (base) Stanford University (Yasunaga et al. 2022)](https://pubmedqa.github.io/) | 70.2 | reasoning-required test Accuracy (%) | Mar 29, 2022 |
| Official public submission leaderboard / PQA-L test | 23 | [BioBERT (multi-phase tuning) University of Pittsburgh & Carnegie Mellon University (Jin et al. 2019)](https://pubmedqa.github.io/) | 68.1 | reasoning-required test Accuracy (%) | Sep 13, 2019 |
| Official public submission leaderboard / PQA-L test | 24 | [BioELECTRA SAAMA AI Research Lab (Kanakarajan et al. 2019)](https://pubmedqa.github.io/) | 64.0 | reasoning-required test Accuracy (%) | June, 2021 |
| Official public submission leaderboard / PQA-L test | 25 | [PubMedBERT Microsoft Research (Gu et al. 2020)](https://pubmedqa.github.io/) | 55.8 | reasoning-required test Accuracy (%) | July 31, 2020 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 覆盖与限制

All 25 rows of the reasoning-required leaderboard on the official site are included, including the human baseline, the majority-class baseline, and the random baseline. Original row numbers, dates, and names of models and methods are kept. NA stays NA, and F1 is not filled in by estimation. The dates on the official site do not give a timezone. The original calendar day is kept, and no time is invented.

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

## Contact

### 项目公开邮箱

```json
[
 "qiaojin.andy@gmail.com"
]
```

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### GitHub反馈

https://github.com/pubmedqa/pubmedqa/issues

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 官方社交

Unverified

> This field has not been verified exactly; that does not mean it is officially Not disclosed.

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 隐私边界

Only contact details published in the paper, on the official site, or in the repository are used; private channels are not collected.

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## Original files

### 原始PDF

https://aclanthology.org/D19-1259.pdf

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### SHA-256

05d2c994c3a0cbf02967ed83cd22a319722e81039bb998f9b8c92e6a13f302da

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）

### PDF bytes

1072208

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）

### Paper PDF

{
 "id": "1CB2QjxkaK3viyZtpkSoVba9sypsRqTiV"
}

## Changelog

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

[1](https://pubmedqa.github.io/)（访问 2026-11-08）
