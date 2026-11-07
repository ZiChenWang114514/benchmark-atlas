# MMMU-Pro

> 核验日期：2026-11-08（KST / Asia/Seoul，UTC+9）。未知不补造；来源访问日不等于实验运行日。

MMMU-Pro从原版筛去文本捷径可答题，扩展候选选项，并将题目嵌入图片以测试“看与读”的联合能力。底层1730道题对应Standard四选项、Standard十选项和Vision三种配置，不是5190道独立题。原论文整体分、官方JSON各列、Vals四选项与AA十选项均分轨；论文人类表现是作者利用原MMMU数据估计，不视作Pro重新实测。
[本页导读依据](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

## 基本信息

### 简称

MMMU-Pro

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 全称

MMMU-Pro

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 数据/基准版本

Pro（数据修订截至2026-10-04）

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 论文版本

arXiv v3（2025-05-22 17:22:02 KST；ACL 2025论文）

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### 发布日期

2024-09-05（官方数据首发公告；arXiv v1为2024-09-05 00:31:26 KST）

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 主板块

多模态

> 编辑归档，不代表官方分类。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 子领域

科学视觉推理

> 编辑归档，不代表官方分类。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 许可边界

Apache-2.0（HF数据卡）；原始素材版权依源站，版权反馈后可移除。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问 2026-11-07）

### 论文入口

https://arxiv.org/abs/2409.02813

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 代码入口

https://github.com/MMMU-Benchmark/MMMU

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 数据入口

https://huggingface.co/datasets/MMMU/MMMU_Pro

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 官方主页

https://mmmu-benchmark.github.io/

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）；[来源2](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### 论文标题

MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## 发起与维护

### 发起方

MMMU Team

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 合作机构

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 作者

Xiang Yue、Tianyu Zheng、Yuansheng Ni、Yubo Wang、Kai Zhang、Shengbang Tong、Yuxuan Sun、Botao Yu、Ge Zhang、Huan Sun、Yu Su、Wenhu Chen、Graham Neubig

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 当前维护方

MMMU Team

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 资助

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

## 设计目标

### 衡量能力

跨学科视觉理解、知识推理和图文整合；要求真正利用图片，而不只依赖选项或文本捷径。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 设计动机

原版 MMMU 的部分题目不看图也能答对，四选一又容许猜测。Pro通过过滤、扩展选项与纯视觉输入收紧评测。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## 构建方式

### 题目来源

从原版MMMU过滤纯文本模型可答题；四个文本模型各重复十次，筛去至少三个模型多数答对的题；抽取1,800题后经选项与图像相关性复核，保留1,730题。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 出题/构建者背景

由领域专家扩展选项并审查原答案/图像关联；先模型初筛，再人工两轮复核，第二轮由额外两名人工专家复查。不是重新组织整套题目的全新专家考试。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### 审核流程

GPT-4o生成额外选项、Claude 3.5过滤，再经两轮人工复核；截图和照片由人工在不同显示背景、字体与字号下采集。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 质量控制

GPT-4o生成额外选项、Claude 3.5过滤，再经两轮人工复核；截图和照片由人工在不同显示背景、字体与字号下采集。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 去污染/泄漏控制

过滤纯文本捷径不能证明无训练污染；公开题集仍存在记忆风险。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## 数据形式

### 精确规模与统计口径

1,730个底层问题；standard (4 options)、standard (10 options)、vision三个配置各1,730行，合计5,190配置行不是5,190道独立问题。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问 2026-11-07）

### 题型

学科多项选择；Standard文本配图、Vision将问题与选项嵌入图像。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 模态

文本；图像

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 语言/代码语种

英语题目与选项（原论文展示的Standard/Vision规范及示例）；未把编程语言或图片文字识别另计成自然语言覆盖。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 难度结构

从原MMMU筛出文本模型难以可靠回答的题；不按新增小学/高中/大学题库分级。HF Standard保留topic_difficulty字段，论文附录的人类表现是沿原MMMU数据推算而非重新实测；不将其当新增人类考试成绩。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 公开与隐藏划分

HF三个配置均为test split；样本id保留原版validation/test来源，不等于新增训练划分。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问 2026-11-07）

## 评测方法

### 指标

准确率；论文总体分为Standard 10选项与Vision准确率的平均，Standard 4选项仅作对照。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 评分规则

抽取选择答案并与参考标签比较；不能把四选项成绩当Pro十选项/Vision综合成绩。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 运行与提示设置

论文比较Direct与CoT并取较优；AA当前方法页列1730题十选项、1次运行、正则抽取pass@1，且明确是独立单项，不属于Intelligence Index v5.0.1。Vals使用四选项，应与前两者分开。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）；[来源3](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### 官方评测脚本

https://github.com/MMMU-Benchmark/MMMU

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 可比性警示

Vals使用Standard 4选项；AA使用10选项；原论文综合还包含Vision，三个口径不可直接混排。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## 最新情况

### 本轮核验日期

2026-11-08

> 本次源站访问日期；时区KST / Asia/Seoul；不等于榜单运行日期。

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "version": "Pro（数据修订截至2026-10-04）",
  "trending": "A",
  "heat_evidence": "AA当前方法页仍运行1,730题十选项；HF于2026-10-04修正选项及缺失条件。Vals于9月1日保留榜，但现已停止新模型评测，不能写成仍持续更新。",
  "evidence_2026_h2": [
    {
      "url": "https://huggingface.co/datasets/MMMU/MMMU_Pro",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    },
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    },
    {
      "url": "https://www.vals.ai/benchmarks/mmmu",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）；[来源3](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "arxiv_revisions": [
    {
      "version": "v1",
      "date_kst": "2024-09-05T00:31:26+09:00"
    },
    {
      "version": "v2",
      "date_kst": "2024-09-10T21:55:31+09:00"
    },
    {
      "version": "v3",
      "date_kst": "2025-05-22T17:22:02+09:00"
    }
  ],
  "dataset_corrections": [
    {
      "date": "2026-05-30",
      "ids": [
        "validation_Diagnostics_and_Laboratory_Medicine_17"
      ],
      "change": "Vision/十选项扩展修正"
    },
    {
      "date": "2026-07-10",
      "ids": [
        "validation_Design_15",
        "validation_Art_Theory_4"
      ],
      "change": "参考答案标签修正"
    },
    {
      "date": "2026-10-04",
      "ids": [
        "test_Chemistry_240",
        "validation_Finance_5"
      ],
      "change": "选项扩展及缺失题设条件修正"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 饱和性证据

Vals明确称该实现已饱和并停止对新模型运行；不外推到AA十选项或Pro Vision。

[来源1](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### 污染与已知争议

过滤纯文本可答题不是训练数据去污染；2026年仍持续更正答案/选项/缺失条件，必须固定数据revision。原论文Standard十选项与Vision均值、官方JSON整体列、Vals四选项、AA十选项不是同一口径；原论文人类成绩是作者估计，不是Pro独立复测。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源3](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源5](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）

### 衍生与条目关系

本页只收MMMU-Pro；原版保留在既有条目 /benchmarks/mmmu，Pro为其防捷径增强衍生版，不能用原版11.5K题量填入本页。

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

## 榜单快照

### 本次榜单采集日

2026-11-08

[来源1](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### 官方榜源

https://mmmu-benchmark.github.io/#leaderboard

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）；[来源2](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### 第三方覆盖

https://www.vals.ai/benchmarks/mmmu；https://artificialanalysis.ai/evaluations/mmmu-pro

[来源1](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### 官方JSON / Pro overall（官网原列）

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Chance Vision 1.5 | 86.9 % | accuracy | 2026-07-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 2 | GPT-5.4 Thinking w/ tools | 82.1 % | accuracy | 2026-03-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 3 | GPT-5.4 Thinking w/o tools | 81.2 % | accuracy | 2026-03-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 4 | Gemini 3.0 Pro | 81.0 % | accuracy | 2025-11-18 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 5 | Gemini 3.1 Pro Thinking (High) | 80.5 % | accuracy | 2026-02-19 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | Muse Spark Thinking | 80.4 % | accuracy | 2026-04-08 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | GPT-5.2 Thinking w/o Python | 80.4 % | accuracy | 2025-12-11 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 8 | GPT-5.2 Thinking w/o tools | 79.5 % | accuracy | 2025-12-11 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 9 | GPT-5.1 Thinking | 79.0 % | accuracy | 2025-11-13 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 10 | GPT-5 w/ thinking | 78.4 % | accuracy | 2025-08-07 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |

- 该原列已展示分数排序；工具/无工具标签保留，不构成同协议复测

- overall未同时提供两个组件时，不反推或补造组件成绩

#### 官方JSON / Pro Standard十选项（JSON original列）

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Chance Vision 1.5 | 87.6 % | accuracy | 2026-07-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 2 | Claude 3.5 Sonnet | 55.0 % | accuracy | 2024-06-20 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 3 | GPT-4o (0513) | 54.0 % | accuracy | 2024-05-13 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 4 | InternVL2.5-78B | 51.4 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 5 | Gemini 1.5 Pro (0801) | 49.4 % | accuracy | 2024-08-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | Qwen2-VL-72B | 49.2 % | accuracy | 2024-08-29 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 7 | InternVL2.5-38B | 48.0 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 8 | Gemini 1.5 Pro (0523) | 46.5 % | accuracy | 2024-05-23 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 9 | MiMo-VL 7B-RL | 46.2 % | accuracy | 2025-06-04 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 10 | Llama 3.2 90B | 45.2 % | accuracy | 2024-09-25 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |

- 该原列已展示分数排序；工具/无工具标签保留，不构成同协议复测

- overall未同时提供两个组件时，不反推或补造组件成绩

#### 官方JSON / Pro Vision

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Chance Vision 1.5 | 86.1 % | accuracy | 2026-07-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 2 | GPT-4o (0513) | 49.7 % | accuracy | 2024-05-13 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 3 | Claude 3.5 Sonnet | 48.0 % | accuracy | 2024-06-20 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 4 | InternVL2.5-78B | 45.9 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 5 | Gemini 1.5 Pro (0801) | 44.4 % | accuracy | 2024-08-01 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 6 | InternVL2.5-38B | 44.0 % | accuracy | 2024-12-05 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 7 | Qwen2-VL-72B | 43.3 % | accuracy | 2024-08-29 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 8 | Gemini 1.5 Pro (0523) | 40.5 % | accuracy | 2024-05-23 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 9 | MiMo-VL 7B-RL | 40.3 % | accuracy | 2025-06-04 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |
| 10 | MiMo-VL 7B-SFT | 39.4 % | accuracy | 2025-06-04 | [原始来源](https://mmmu-benchmark.github.io/leaderboard_data.json)（2026-11-08） |

- 该原列已展示分数排序；工具/无工具标签保留，不构成同协议复测

- overall未同时提供两个组件时，不反推或补造组件成绩

#### Vals / Standard四选项 / 已停止新模型评测

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Claude Fable 5.1 | 90.64% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 2 | Claude Opus 5 | 89.88% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 3 | Claude Fable 5 | 89.31% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 4 | Gemini 3.8 Flash | 89.08% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 5 | Gemini 3.7 Flash | 88.96% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 6 | GPT-5.6 Sol | 88.84% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 7 | Gemini 3.6 Flash | 88.38% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 8 | Gemini 3.5 Flash | 88.27% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 9 | GPT 5.5 | 88.27% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 10 | Gemini 3.1 Pro Preview (02/26) | 88.21% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 11 | Kimi K3 | 88.15% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 12 | Qwen 3.8 Max | 88.03% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 13 | Gemini 3 Flash (12/25) | 87.63% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 14 | Gemini 3 Pro (11/25) | 87.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 15 | GPT 5.4 (xhigh) | 87.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 16 | Muse Spark | 87.40% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 17 | GPT 5.2 | 86.67% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 18 | Muse Spark 1.1 | 86.59% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 19 | Claude Opus 4.8 | 86.59% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 20 | GPT-5.6 Terra | 86.47% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 21 | Kimi K2.6 | 86.30% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 22 | Muse Spark 1.2 | 86.13% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 23 | GLM 5.3 Flash | 86.01% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 24 | Claude Opus 4.7 | 85.55% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 25 | GPT-5.6 Luna | 85.03% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 26 | Kimi K2.5 | 84.33% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 27 | Qwen 3.6 Plus | 84.16% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 28 | Qwen 3.8 27B | 83.93% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 29 | Claude Opus 4.6 (Thinking) | 83.87% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 30 | Gemini 3.5 Flash Lite | 83.58% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 31 | Claude Sonnet 4.6 | 83.58% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 32 | Grok 4.20 (Reasoning) | 83.47% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 33 | GPT 5.1 | 83.18% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 34 | Grok 4.3 | 83.06% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 35 | Claude Sonnet 5 | 83.01% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 36 | Claude Opus 4.5 (Thinking) | 82.95% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 37 | Gemini 3.1 Flash Lite Preview | 82.49% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 38 | Qwen 3.5 Flash | 81.91% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 39 | GPT 5 | 81.50% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 40 | Gemini 2.5 Pro Exp | 81.34% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 41 | MiniMax-M3 | 81.16% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 42 | Claude Opus 4.5 (Nonthinking) | 81.10% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 43 | Gemini 2.5 Flash Preview (9/25) (Thinking) | 80.75% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 44 | o3 | 80.42% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 45 | MiMo V2.5 | 80.00% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 46 | o4 Mini | 79.67% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 47 | Gemini 2.5 Flash Preview (9/25) (Nonthinking) | 79.48% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 48 | Claude Sonnet 4.5 (Thinking) | 79.31% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 49 | GPT 5.4 Mini | 79.25% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 50 | GPT 5 Mini | 78.91% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 51 | Inkling | 78.50% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 52 | Claude Opus 4.1 (Thinking) | 77.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 53 | o1 | 77.41% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 54 | Grok 4 | 76.27% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 55 | Gemini 2.5 Flash Lite (9/25) (Thinking) | 75.43% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 56 | Claude 3.7 Sonnet (Thinking) | 75.10% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 57 | Claude Sonnet 4 (Thinking) | 74.93% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 58 | Claude Opus 4.1 (Nonthinking) | 73.72% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 59 | GPT 5.4 Nano | 73.58% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 60 | Claude Opus 4 (Nonthinking) | 73.31% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 61 | Grok 4 Fast (Reasoning) | 72.78% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 62 | Grok 4.1 Fast (Reasoning) | 72.66% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 63 | Gemini 2.5 Flash Lite (9/25) (Nonthinking) | 72.54% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 64 | Claude Sonnet 4 (Nonthinking) | 72.39% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 65 | GPT 4.1 | 72.39% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 66 | Gemini 2.5 Flash Preview 4/17 (Thinking) | 71.92% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 67 | Llama 4 Maverick | 71.69% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 68 | Claude 3.7 Sonnet (Nonthinking) | 71.52% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 69 | GPT 5 Nano | 70.94% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 70 | GPT 4.1 Mini | 70.54% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 71 | Gemini 2.0 Flash (001) | 69.79% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 72 | Claude 3.5 Sonnet Latest | 68.80% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 73 | Gemini 2.5 Flash Preview 4/17 (Nonthinking) | 68.00% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 74 | Mistral Large 3 | 66.19% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 75 | Gemini 1.5 Pro (002) | 65.51% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 76 | Magistral Small 1.2 (09/2025) | 65.20% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 77 | Magistral Medium 1.2 (09/2025) | 64.57% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 78 | GPT 4o (2024-08-06) | 64.01% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 79 | Grok 4.1 Fast Non-Reasoning | 63.70% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 80 | Grok 4 Fast (Non-Reasoning) | 63.41% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 81 | Mistral Medium 3.1 (05/2025) | 62.97% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 82 | GPT 4o (2024-11-20) | 62.16% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 83 | Grok 4.5 | 61.79% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 84 | Mistral Small 3.1 (03/2025) | 60.08% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 85 | Llama 4 Scout | 58.75% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 86 | Grok 2 Vision | 57.25% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 87 | Gemini 1.5 Flash (002) | 57.19% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 88 | GPT 4o Mini | 56.56% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 89 | GPT 4.1 Nano | 55.05% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 90 | Llama 3.2 Vision (90B) | 48.06% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 91 | Claude Haiku 4.5 (Thinking) | 46.07% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 92 | Llama 3.2 Vision (11B) | 38.82% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |
| 93 | Qwen 3.5 Plus | 22.77% | accuracy | 2026-09-01 | [原始来源](https://www.vals.ai/benchmarks/mmmu)（2026-11-08） |

- Vals独立实现历史保留榜

#### AA / Standard十选项 / 1730题 / 单次pass@1

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Gemini 4 Carbon (Medium) | 89 % | accuracy | 未逐项给出 | [原始来源](https://artificialanalysis.ai/evaluations/mmmu-pro)（2026-11-08） |
| 2 | Claude Opus 5.5 (Max, Default Fallback) | 88 % | accuracy | 未逐项给出 | [原始来源](https://artificialanalysis.ai/evaluations/mmmu-pro)（2026-11-08） |
| 3 | GPT-6 Astra (Max) | 87 % | accuracy | 未逐项给出 | [原始来源](https://artificialanalysis.ai/evaluations/mmmu-pro)（2026-11-08） |

- AA独立评测；非Vision均值

- 页面摘要显示整数百分比，未反推小数

#### 论文v3表1 / Standard十选项

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| — | GPT-4o (0513) | 54.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Claude 3.5 Sonnet | 55.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Gemini 1.5 Pro (0801) | 49.4 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |

- 论文历史基线；Direct/CoT取较优；非当前榜

#### 论文v3表1 / Vision

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| — | GPT-4o (0513) | 49.7 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Claude 3.5 Sonnet | 48.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |
| — | Gemini 1.5 Pro (0801) | 44.4 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2409.02813)（2026-11-08） |

- 论文历史基线；Direct/CoT取较优；非当前榜

[来源1](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### 覆盖范围与限制

本次补上官方JSON的Pro整体、Standard、Vision分列前10条；保留模型标签中的工具权限，缺组件不反推。Vals完整可读历史榜单单列，AA只抄其摘要能核验的三项整数百分比，不伪造更多精度。论文v3表1的历史组件另轨。所有赛道均不可跨列混排。

[来源1](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源2](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

## 联系方式

### 公开研究邮箱

xiangyue.work@gmail.com

[来源1](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）

### 项目反馈入口

https://github.com/MMMU-Benchmark/MMMU/issues

[来源1](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）

### 官方公开社交入口

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

### 公开渠道/隐私边界

本档案只收录官方已公开项目渠道；原题版权遵循来源，团队承诺核实侵权反馈后移除样本。未把开源许可证解读为放弃原素材权利。

[来源1](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2409.02813

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### PDF SHA-256

f833d6273318d53487ace892ed54289216f5d6034fcf37af2499146d12860f5b

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### PDF字节数

17320142

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源1](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）

### Drive文件夹

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-07）

### 其他官方文档

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://huggingface.co/datasets/MMMU/MMMU_Pro"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2409.02813"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://www.vals.ai/benchmarks/mmmu"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://artificialanalysis.ai/evaluations/mmmu-pro",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/pdf/2409.02813",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://mmmu-benchmark.github.io/",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://mmmu-benchmark.github.io/leaderboard_data.json",
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-08）；[来源2](https://artificialanalysis.ai/evaluations/mmmu-pro)（访问 2026-11-08）；[来源3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-08）；[来源4](https://arxiv.org/abs/2409.02813)（访问 2026-11-08）；[来源5](https://arxiv.org/pdf/2409.02813)（访问 2026-11-08）；[来源6](https://github.com/MMMU-Benchmark/MMMU/blob/main/README.md)（访问 2026-11-08）；[来源7](https://mmmu-benchmark.github.io/)（访问 2026-11-08）；[来源8](https://mmmu-benchmark.github.io/leaderboard_data.json)（访问 2026-11-08）；[来源9](https://www.vals.ai/benchmarks/mmmu)（访问 2026-11-08）

### Drive原始PDF

待核实

> 状态：待核实。

> 本组仅本地建页，未上传Drive，不伪造归档链接。

[来源1](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问 2026-11-07）

## 变更记录

### 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。本页只收MMMU-Pro；原版保留在既有条目 /benchmarks/mmmu，Pro为其防捷径增强衍生版，不能用原版11.5K题量填入本页。 热度与榜单口径分离，不确定值标记待核实。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST, UTC+9)",
    "change": "第二轮深度复核：重读官方数据卡、README/许可、可用论文abs与PDF及官方榜；补精确题量、修订边界与完整可读成绩；区分私有集、历史基线、厂商自报与独立测评。"
  }
]
```

[来源1](https://mmmu-benchmark.github.io/)（访问 2026-11-08）
