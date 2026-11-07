# PubMedQA

> 第2轮深度核验：2026-11-08（KST / Asia/Seoul）。访问日不等于发布日期或实验运行日；未知保留，不推定“未公开”。

PubMedQA以真实生物医学研究标题作问题，要求根据去掉结论的摘要预测yes/no/maybe。PQA-L为1,000道双专家标注题；PQA-A则由规则自动生成弱标签，不是二十多万道人工编写题。HF把PQA-L整体打包成train不改变官方500题测试集，直接整包训练会泄漏测试。

编辑状态：第1轮实证补全；未确认项保留待核实，论文历史分数与实时榜单分开记录。

## 1. 基本信息

### 简称

PubMedQA

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 全称

PubMedQA

> 使用官方名称；未有已核实全称扩展时保留原名，不把论文标题误当基准全称。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 数据版本

原始PubMedQA三配置：pqa_labeled、pqa_unlabeled、pqa_artificial；HF文件和官方测试ID定义实际评测集，不自拟语义版本号。

[1](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）

### 论文版本

EMNLP-IJCNLP 2019正式论文D19-1259；arXiv:1909.06146v1。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 发布时间

论文预印本首发：2019-09-13 20:18:20 KST；正式会议论文2019-11。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 板块

生物与医学

> Benchmark Atlas 编辑归档；跨学科条目只在主板块计数，另用标签导航。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）

### 子领域

```json
[
  "生物与医学"
]
```

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 许可

官方仓库 MIT；不自动代表所有原始 PubMed 摘要的版权条款。

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/LICENSE)（访问 2026-11-07）

### 论文

https://aclanthology.org/D19-1259/

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 代码

https://github.com/pubmedqa/pubmedqa

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 数据集

https://github.com/pubmedqa/pubmedqa

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 官方主页

https://pubmedqa.github.io/

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 论文题名

PubMedQA: A Dataset for Biomedical Research Question Answering

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## 2. 发起与维护

### 发起方

```json
[
  "University of Pittsburgh",
  "Carnegie Mellon University",
  "Google AI（按论文作者单位）"
]
```

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 合作单位

```json
[
  "University of Pittsburgh",
  "Carnegie Mellon University",
  "Google AI（论文合作作者单位；非额外推定的机构协议）"
]
```

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 作者

```json
[
  "Qiao Jin",
  "Bhuwan Dhingra",
  "Zhengping Liu",
  "William Cohen",
  "Xinghua Lu"
]
```

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 维护方

pubmedqa官方GitHub组织；Qiao Jin在README列为项目联系人。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 资助

待核实

> 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## 3. 设计目标

### 目标能力

根据医学论文摘要回答研究问题，特别考查对定量证据的理解。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 相对既有评测的缺口

既有生物医学QA常偏事实抽取且专家标注规模小；PubMedQA要求根据原研究摘要尤其定量结果推断yes/no/maybe，并提供独立long_answer供辅助监督。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

## 4. 构建方式

### 题目与标签来源

PQA-L/U取真实PubMed疑问式文章标题和去结论摘要；PQA-A由陈述式标题按词性和否定状态自动转成问题与yes/no标签，不是人工逐题撰写的211.3k题。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 出题/标注背景

PQA-L由两位具资格的M.D. candidates标注；原文未把他们称作已执业专科医生。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 审核流程

标注者1看问题、上下文和结论（reasoning-free）；标注者2只看问题和去结论上下文（reasoning-required）。分歧时讨论；无法达成一致则删除该题。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 质量控制

人工筛除不能以yes/no/maybe作答的题；双人讨论消歧。PQA-U用规则排除wh问句及多实体选项，识别可回答性与标注者1一致超过93%，不把该比例当测试标签准确率。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 去污染与隔离

待核实

> 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## 5. 数据形式

### 规模

```json
{
  "pqa_labeled": 1000,
  "pqa_unlabeled": 61249,
  "pqa_artificial": 211269,
  "basis": "HF数据卡精确行数；原论文1k/61.2k/211.3k为四舍五入描述，非精确行数。"
}
```

[1](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）

### 题型

依据研究摘要回答 yes/no/maybe 三分类问题。

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### 模态

研究问题与对应摘要文本。

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### 语言

英语（HF数据卡明确en、monolingual）。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 难度

生物医学研究阅读推断；论文单人reasoning-required 78.0% accuracy，reasoning-free 90.4%。无逐题统一难度标签，不能把两种人类条件混同。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 公开/隐藏划分

PQA-L官方划分500测试；另500用于10折交叉验证，内层每折450训练/50验证。HF三个配置都以train打包，但不能覆盖官方测试隔离。PQA-U无官方划分脚本；PQA-A用于预训练。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[3](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）

## 6. 评测方法

### 指标

官方 reasoning-required 榜单报告 Accuracy (%) 与 Macro-F1 (%)；部分模型的 Macro-F1 为 NA。

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### 判分

将模型预测按 PMID 对齐后，以官方 evaluation.py 计算性能。

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 提示/推理设置

原论文为BioBERT等监督微调，按PQA-A→PQA-U→PQA-L多阶段训练及long-answer bag-of-words辅助监督；reasoning-required测试仅给问题和去结论上下文。后续LLM提示法以每条提交设定为准。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 官方实现

evaluation.py：预测 JSON 的键为 PMID，值为 yes/no/maybe；运行 python evaluation.py PREDICTIONS_PATH。

[1](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-07）

### 可比性边界

PQA-L官方test为500题；HF把全部1,000个PQA-L样本标作train只是打包配置，不是官方训练/测试协议。reasoning-free能看结论，不能与reasoning-required直接比较；PQA-A是弱标注预训练数据而非测试集。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

## 7. 最新情况

### 核验日

2026-11-08 KST / Asia/Seoul

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 本次版本快照

本次HF卡仍列PQA-L 1000、PQA-U 61249、PQA-A 211269；未以HF split名取代官方500题测试协议。

[1](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）

### 论文修订

```json
[
  {
    "version": "arXiv v1",
    "submitted_at": "2019-09-13T20:18:20+09:00",
    "timezone": "Asia/Seoul"
  },
  {
    "version": "EMNLP-IJCNLP正式论文",
    "date": "2019-11",
    "identifier": "D19-1259"
  }
]
```

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 饱和情况

官网当前可见首位82.0%（GPT-4 Medprompt，2023-11-28），未到100%；这是较早提交的官网榜，不代表2026所有模型最佳结果或基准已饱和。

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 污染/限制/争议

PQA-L仅1,000题，需严守500题test隔离；HF打包train包含全部PQA-L，若直接用于训练将泄漏测试。PQA-A按否定规则生成且yes占92.8%，存在标签偏置；现代预训练污染规模待核实。

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）；[2](https://huggingface.co/datasets/qiaojin/PubMedQA/raw/main/README.md)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/pubmedqa/pubmedqa/master/README.md)（访问 2026-11-08）；[4](https://arxiv.org/abs/1909.06146)（访问 2026-11-08）

### 衍生与相关版本

待核实

> 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-08 KST / Asia/Seoul（采集日，不是实验运行日）

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 官方结果入口

https://pubmedqa.github.io/

[1](https://pubmedqa.github.io/)（访问 2026-11-07）

### 第三方入口

待核实

> 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| 官方公开提交榜 / PQA-L test | 1 | [GPT-4 (Medprompt) Microsoft (Nori et al. 2023)](https://pubmedqa.github.io/) | 82.0 | reasoning-required test Accuracy (%) | Nov 28, 2023 |
| 官方公开提交榜 / PQA-L test | 2 | [Med-PaLM 2 Google Research & DeepMind (Singhal et al. 2023)](https://pubmedqa.github.io/) | 81.8 | reasoning-required test Accuracy (%) | May 16, 2023 |
| 官方公开提交榜 / PQA-L test | 3 | [MEDITRON EPFL (Chen et al. 2023)](https://pubmedqa.github.io/) | 81.6 | reasoning-required test Accuracy (%) | Nov 27, 2023 |
| 官方公开提交榜 / PQA-L test | 4 | [Palmyra-Med Writer Inc. (Kamble et al. 2023)](https://pubmedqa.github.io/) | 81.1 | reasoning-required test Accuracy (%) | Jul 6, 2023 |
| 官方公开提交榜 / PQA-L test | 5 | [AntGLM-Med Ant Group (Li et al. 2023)](https://pubmedqa.github.io/) | 80.6 | reasoning-required test Accuracy (%) | Dec 1, 2023 |
| 官方公开提交榜 / PQA-L test | 6 | [GPT-4-base Microsoft & OpenAI (Nori et al. 2023)](https://pubmedqa.github.io/) | 80.4 | reasoning-required test Accuracy (%) | Apr 12, 2023 |
| 官方公开提交榜 / PQA-L test | 7 | [Claude 3 Anthropic (Anthropic, 2024)](https://pubmedqa.github.io/) | 79.7 | reasoning-required test Accuracy (%) | Mar 4, 2024 |
| 官方公开提交榜 / PQA-L test | 8 | [GPT-3.5 + Z-Code++ Microsoft Azure AI (He et al. 2022)](https://pubmedqa.github.io/) | 79.6 | reasoning-required test Accuracy (%) | Jan 11, 2023 |
| 官方公开提交榜 / PQA-L test | 9 | [Flan-PaLM (3-shot) Google Research & DeepMind (Singhal et al. 2022)](https://pubmedqa.github.io/) | 79.0 | reasoning-required test Accuracy (%) | Dec 26, 2022 |
| 官方公开提交榜 / PQA-L test | 10 | [HEAL DeepScribe Inc (Yuan et al. 2024)](https://pubmedqa.github.io/) | 78.4 | reasoning-required test Accuracy (%) | Mar 14, 2024 |
| 官方公开提交榜 / PQA-L test | 11 | [Codex (5-shot) Technical University of Denmark & Copenhagen University Hospital (Liévin et al. 2022)](https://pubmedqa.github.io/) | 78.2 | reasoning-required test Accuracy (%) | Dec 20, 2022 |
| 官方公开提交榜 / PQA-L test | 12 | [Human Performance University of Pittsburgh & Carnegie Mellon University (Jin et al. 2019)](https://pubmedqa.github.io/) | 78.0 | reasoning-required test Accuracy (%) | Sep 13, 2019 |
| 官方公开提交榜 / PQA-L test | 13 | [Galactica Meta AI (Taylor et al. 2022)](https://pubmedqa.github.io/) | 77.6 | reasoning-required test Accuracy (%) | Nov 16, 2022 |
| 官方公开提交榜 / PQA-L test | 14 | [GatorTronGPT University of Florida & NVIDIA (Peng et al. 2023)](https://pubmedqa.github.io/) | 77.6 | reasoning-required test Accuracy (%) | May 22, 2023 |
| 官方公开提交榜 / PQA-L test | 15 | [MediSwift-XL Cerebras Systems (Thangarasa et al. 2024)](https://pubmedqa.github.io/) | 76.8 | reasoning-required test Accuracy (%) | Mar 4, 2024 |
| 官方公开提交榜 / PQA-L test | 16 | [GPT-4 Microsoft & OpenAI (Nori et al. 2023)](https://pubmedqa.github.io/) | 75.2 | reasoning-required test Accuracy (%) | Mar 20, 2023 |
| 官方公开提交榜 / PQA-L test | 17 | [Reka Core Reka (Ormazabal et al. 2024)](https://pubmedqa.github.io/) | 74.6 | reasoning-required test Accuracy (%) | Apr 18, 2024 |
| 官方公开提交榜 / PQA-L test | 18 | [PubMedGPT Stanford University (Bolton et al. 2022)](https://pubmedqa.github.io/) | 74.4 | reasoning-required test Accuracy (%) | Dec 15, 2022 |
| 官方公开提交榜 / PQA-L test | 19 | [DRAGON Stanford University & EPFL (Yasunaga et al. 2022)](https://pubmedqa.github.io/) | 73.4 | reasoning-required test Accuracy (%) | Oct 17, 2022 |
| 官方公开提交榜 / PQA-L test | 20 | [PMC-LLaMA Shanghai Jiao Tong University (Wu et al. 2023)](https://pubmedqa.github.io/) | 73.4 | reasoning-required test Accuracy (%) | Apr 27, 2023 |
| 官方公开提交榜 / PQA-L test | 21 | [BioLinkBERT (large) Stanford University (Yasunaga et al. 2022)](https://pubmedqa.github.io/) | 72.2 | reasoning-required test Accuracy (%) | Mar 29, 2022 |
| 官方公开提交榜 / PQA-L test | 22 | [BioLinkBERT (base) Stanford University (Yasunaga et al. 2022)](https://pubmedqa.github.io/) | 70.2 | reasoning-required test Accuracy (%) | Mar 29, 2022 |
| 官方公开提交榜 / PQA-L test | 23 | [BioBERT (multi-phase tuning) University of Pittsburgh & Carnegie Mellon University (Jin et al. 2019)](https://pubmedqa.github.io/) | 68.1 | reasoning-required test Accuracy (%) | Sep 13, 2019 |
| 官方公开提交榜 / PQA-L test | 24 | [BioELECTRA SAAMA AI Research Lab (Kanakarajan et al. 2019)](https://pubmedqa.github.io/) | 64.0 | reasoning-required test Accuracy (%) | June, 2021 |
| 官方公开提交榜 / PQA-L test | 25 | [PubMedBERT Microsoft Research (Gu et al. 2020)](https://pubmedqa.github.io/) | 55.8 | reasoning-required test Accuracy (%) | July 31, 2020 |

> 所有行采集于2026-11-08 KST；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

### 覆盖与限制

收录官网reasoning-required榜全部25行（含人类、多数类及随机基线）；保留原行号、日期、模型/方法名称。NA保持NA，不补估F1；官网日期未给时区，原日历日保留且不臆造时间。

[1](https://pubmedqa.github.io/)（访问 2026-11-08）

## 9. 联系方式

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

待核实

> 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### 隐私边界

只使用论文、官方站点或仓库公开联系方式；不收集私人渠道。

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 10. 原始文件

### 原始PDF

https://aclanthology.org/D19-1259.pdf

[1](https://aclanthology.org/D19-1259/)（访问 2026-11-07）；[2](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-07）

### SHA-256

05d2c994c3a0cbf02967ed83cd22a319722e81039bb998f9b8c92e6a13f302da

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）

### PDF字节数

1072208

[1](https://aclanthology.org/D19-1259.pdf)（访问 2026-11-08）

### Drive文件夹

```json
{
  "id": "1p4BxGveCspWrwqeJtetU_eLA9Rnl3iEk",
  "webViewLink": "https://drive.google.com/drive/folders/1p4BxGveCspWrwqeJtetU_eLA9Rnl3iEk"
}
```

[1](https://drive.google.com/drive/folders/1p4BxGveCspWrwqeJtetU_eLA9Rnl3iEk)（访问 2026-11-07）

### 其他材料

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1S_9mued4KL0JikJSKoGtB2cca379JaKco99qTqDyeu4",
    "webViewLink": "https://docs.google.com/document/d/1S_9mued4KL0JikJSKoGtB2cca379JaKco99qTqDyeu4/edit?usp=drivesdk"
  }
]
```

[1](https://docs.google.com/document/d/1S_9mued4KL0JikJSKoGtB2cca379JaKco99qTqDyeu4/edit?usp=drivesdk)（访问 2026-11-07）

### Drive论文PDF

{
  "id": "1CB2QjxkaK3viyZtpkSoVba9sypsRqTiV",
  "webViewLink": "https://drive.google.com/file/d/1CB2QjxkaK3viyZtpkSoVba9sypsRqTiV/view?usp=drivesdk"
}

[1](https://drive.google.com/file/d/1CB2QjxkaK3viyZtpkSoVba9sypsRqTiV/view?usp=drivesdk)（访问 2026-11-07）

## 11. 变更记录

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方材料核验、中文改写、PDF原件入Drive；未核实字段显式标记。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "第1轮：打开官方文档核验许可、数据形式和评测协议；复核2026H2证据，区分历史结果与实时榜单；同步中文介绍。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul",
    "change": "第2轮q11：重开论文abs/PDF、官方README/许可、数据卡及榜单；补齐可核实字段、重写中文介绍，完整采集分轨精确成绩，保留版本冲突与不可访问材料。"
  }
]

[1](https://pubmedqa.github.io/)（访问 2026-11-08）
