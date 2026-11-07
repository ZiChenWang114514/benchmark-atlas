# MultiChallenge

> 核验日期：2026-11-08（KST / Asia/Seoul，UTC+9）。未知不补造；来源访问日不等于实验运行日。

MultiChallenge考查多轮指令保持、用户信息推断记忆、可靠版本编辑和自洽。原论文与原GitHub数据为273段对话，当前官方HF test为266段，这一差异尚无本轮可核验的官方解释，不能用一个分母笼统描述所有成绩。在线榜已修改裁判与54条rubric，原仓库多次attempts又按至少一次成功计分，因此人评、历史自动评、现在线榜及best-of-attempts必须分开。
[本页导读依据](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

## 基本信息

### 简称

MultiChallenge

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 全称

MultiChallenge

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 数据/基准版本

官方榜2026-02-03裁判/题目修订口径

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 论文版本

arXiv v2（2025-03-06 13:41:56 KST）

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 发布日期

2025-01-29 12:29:24 KST（arXiv v1）

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 主板块

语言

> 编辑归档，不代表官方分类。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 子领域

多轮指令保持；用户信息推断记忆；版本编辑；自洽

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/MultiChallenge)（访问 2026-11-08）

### 许可边界

HF官方数据卡为CC-BY-4.0；原GitHub仓库根目录未列LICENSE文件，不能据此把所有评测代码也宣称为CC-BY-4.0。代码许可待核实。

> 状态：待核实。

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源2](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2501.17399

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 代码入口

https://github.com/ekwinox117/multi-challenge

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 数据入口

https://huggingface.co/datasets/ScaleAI/MultiChallenge

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 官方主页

https://labs.scale.com/leaderboard/multichallenge?tab=large

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 论文标题

MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

## 发起与维护

### 发起方

Scale AI

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 合作机构

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 作者

Ved Sirdeshmukh、Kaustubh Deshpande、Johannes Mols、Lifeng Jin、Ed-Yeremai Cardona、Dean Lee、Jeremy Kritz、Willow Primack、Summer Yue、Chen Xing

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 当前维护方

Scale AI

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 资助

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

## 设计目标

### 衡量能力

多轮对话中的指令保持、用户信息推断记忆、可靠版本编辑与自洽，联合考察上下文注意及推理。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 设计动机

MT-Bench近饱和；纯格式多轮指令测试未覆盖自然对话中混合推理和约束。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

## 构建方式

### 题目来源

多agent合成候选，再由训练过的标注者审核编辑；仅保留令六个筛选模型中至少三个合理失败的样本。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 出题/构建者背景

由Scale AI招募并训练的人工标注者编辑多agent候选；复核池与第一轮编辑者独立，经过两层审核才接纳。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### 审核流程

审核定义一致性、自然真实性及失败合理性；初始编辑后另有两层独立复核。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 质量控制

审核定义一致性、自然真实性及失败合理性；初始编辑后另有两层独立复核。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 去污染/泄漏控制

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

## 数据形式

### 精确规模与统计口径

```json
{
  "paper_v2_conversations": 273,
  "original_github_jsonl_rows": 273,
  "original_axes": {
    "INFERENCE_MEMORY": 113,
    "SELF_COHERENCE": 50,
    "INSTRUCTION_RETENTION": 69,
    "RELIABLE_VERSION_EDITING": 41
  },
  "current_hf_test_rows": 266,
  "scope_caveat": "原论文/原JSONL273与当前HF266不一致；54个rubric修改公告并不等于删除7题的说明。未核实7题差异原因和当前官网每条成绩的精确样本数，禁止统一分母。",
  "turn_count": "论文最多10轮（用户-助手来回）；HF num_turns为消息数，显示3至19，不把19条消息误写成19轮来回。"
}
```

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

### 题型

给定对话历史，对最后用户请求生成开放回答。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 模态

文本

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 语言/代码语种

英语（官方HF卡language: en及Dataset Description明确说明）

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

### 难度结构

仅接纳六个筛选模型中至少三个发生合理失败的例子；困难来自指令/推断/编辑/自洽，不是单纯长上下文长度。部分更难rubric超出可靠裁判能力的样本未发布。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 公开与隐藏划分

当前HF只发布test split共266例；原论文与原GitHub JSONL为273例；官方称暂保留一部分无法可靠自动判分的更难样本，不把其误写成同一公开test的隐藏答案。

[来源1](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源3](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）

## 评测方法

### 指标

实例rubric二元通过准确率；官方榜Rank(UB)另依95%CI统计显著关系计算。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 评分规则

实例级yes/no rubric只评最终回答；原仓库默认attempts=1，多次attempts的总分按至少一次通过计算。该best-of-attempts分数不能与单次accuracy混用。

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源3](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 运行与提示设置

原README示例temp=0，默认attempts=1；--attempts 3按任一次通过计成功。官方在线榜于2026-02-03切换Gemini 2.5 Pro裁判并重写54题评估问题；不能将其冒充论文GPT-4o裁判同协议复测。

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源3](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### 官方评测脚本

https://github.com/ekwinox117/multi-challenge

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

### 可比性警示

模型选择偏差、裁判模型、rubric版本、273/266不同分母以及多次attempts均影响比较。官网Rank(UB)按95%区间非重叠关系计算；Performance Comparison的原分数顺序不是统计Rank(UB)。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）

## 最新情况

### 本轮核验日期

2026-11-08

> 本次源站访问日期；时区KST / Asia/Seoul；不等于榜单运行日期。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "version": "官方榜2026-02-03裁判/题目修订口径",
  "trending": "B",
  "heat_evidence": "2026-11-07打开Scale官方榜可见新前沿模型及当前结果；仅证明单一创建机构仍维护展示（B），不是11月7日发生新运行的证据。",
  "evidence_2026_h2": [
    {
      "url": "https://labs.scale.com/leaderboard/multichallenge?tab=large",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "revisions": [
    {
      "version": "v1",
      "date_kst": "2025-01-29T12:29:24+09:00"
    },
    {
      "version": "v2",
      "date_kst": "2025-03-06T13:41:56+09:00"
    }
  ],
  "online_update": {
    "date": "2026-02-03",
    "judge": "Gemini 2.5 Pro",
    "rubric_questions_modified": 54
  },
  "dataset_count_conflict": "论文/原仓库273；当前官方HF266，差异原因未在本轮已读官方材料中明确解释"
}
```

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）；[来源2](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）

### 饱和性证据

官方当前Performance Comparison榜首81.95%（95%CI ±4.16）；仍有未通过实例，但未据此定义一个通用“已饱和/未饱和”阈值。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 污染与已知争议

论文v2表2/3附近文字仍给出与表格不一致的历史均值，收录历史成绩以明确表格数值为准并单列人评/自动评。官方HF现266条而原JSONL273条，未解释的分母差异保留。样本按六模型共性失败筛选有选择偏差；公开测试集不保证训练无接触。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源3](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）；[来源4](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 衍生与条目关系

Large/Small是模型分组，不新建不同benchmark；与IFEval单轮形式约束互补而非同一测试。

[来源1](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）

## 榜单快照

### 本次榜单采集日

2026-11-08

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### 官方榜源

https://labs.scale.com/leaderboard/multichallenge?tab=large

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 第三方覆盖

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Scale官网 / Performance Comparison / Large

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | gpt 6.1 Sol | 81.95 (±4.16 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 2 | Gemini 4 Argon | 78.7 (±5.30 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 3 | Muse Spark | 75.52 (±4.05 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 4 | Muse Spark 1.1 | 75.3 (±0.60 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 5 | Deepseek V4p1 Flash 1017 | 74.9 (±5.30 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 6 | GPT 6.1 Terra | 74.2 (±5.40 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 6 | Muse Spark Open | 74.2 (±5.60 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 8 | gemini-3.1-pro-preview | 71.37 (±1.74 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 9 | gpt-5.4-pro-2026-03-05 | 69.23 (±3.05 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 10 | Claude Haiku 5.5 | 67.67 (±5.34 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 11 | gemini-3-pro-preview | 65.67 (±2.20 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 12 | gpt-5.1-2025-11-13-thinking | 63.41 (±2.11 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 13 | gpt-5-thinking | 63.19 (±1.63 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 14 | o3-pro-2025-06-10-reasoning-high | 62.4 (±2.49 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 15 | kimi-k2.5 | 61.39 (±0.46 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 16 | gemini-3.1-flash-lite-preview | 60.61 (±0.38 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 17 | gpt-5-mini-thinking | 58.99 (±4.07 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 18 | claude-opus-4-5-20251101-thinking | 58.97 (±0.42 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 19 | claude-4-opus-thinking | 58.62 (±0.77 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 20 | claude-opus-4-1-20250805-thinking | 57.2 (±0.95 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 21 | claude-4-sonnet-thinking | 57.11 (±0.81 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 22 | o3-2025-04-16-reasoning-high | 56.62 (±3.32 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 23 | claude-opus-4-6 (Non-Thinking) | 56.02 (±1.08 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 24 | kimi-k2-thinking | 55.42 (±1.88 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 25 | claude-sonnet-4-5-20250929-thinking | 55.32 (±1.47 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 26 | gemini-2-5-pro | 53.62 (±1.32 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 27 | claude-3-7-sonnet-thinking | 51.58 (±3.07 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 28 | gpt-5.1-2025-11-13-instant | 51.23 (±1.79 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 29 | claude-haiku-4-5-20251001-thinking | 50.49 (±2.04 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 30 | deepseek-v3p1 | 46.1 (±1.11 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 31 | gpt-oss-120b | 45.34 (±2.15 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 32 | o4-mini-2025-04-16-reasoning-high | 44.9 (±0.88 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 33 | qwen3-235b-a22b | 41.22 (±1.79 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 34 | gpt-4.1 | 39.43 (±0.94 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 35 | claude-opus-4-6-thinking-max | 37.15 (±2.16 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |
| 36 | gemini-2-0-flash | 36.35 (±0.78 percentage points) % | accuracy | 未逐项给出 | [原始来源](https://labs.scale.com/leaderboard/multichallenge?tab=large)（2026-11-08） |

- 页面Performance Comparison分数顺序，不是Rank(UB)

- 官方当前展示，未逐项给出精确运行日

#### 论文v2表2 / 人工裁判

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| — | GPT-4o (August 2024) | 12.52 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Llama 3.1 405B Instruct | 14.92 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Mistral Large | 14.63 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Claude 3.5 Sonnet (June 2024) | 41.42 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Gemini 1.5 Pro (August 27 2024) | 19.96 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | o1-preview | 37.23 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |

- 论文历史表格值；不与当前Gemini 2.5 Pro裁判榜混排

#### 论文v2表3 / GPT-4o实例rubric自动裁判

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| — | GPT-4o (August 2024) | 12.9 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Llama 3.1 405B Instruct | 16.5 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Mistral Large | 13.32 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Claude 3.5 Sonnet (June 2024) | 42.75 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | Gemini 1.5 Pro (August 27 2024) | 21.3 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |
| — | o1-preview | 35.73 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2501.17399)（2026-11-08） |

- 论文历史表格值；不与当前Gemini 2.5 Pro裁判榜混排

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### 覆盖范围与限制

完整收录当前Large Performance Comparison的36条可读成绩及其95%CI；保留原分数顺序，不伪造统计Rank(UB)。另存论文表2人评与表3自动裁判各6条；论文文字与表格冲突时用表格并说明。273题原JSONL、266题现HF、在线修订榜之间未擅自认定相同分母。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）

## 联系方式

### 公开研究邮箱

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 项目反馈入口

https://github.com/ekwinox117/multi-challenge/issues

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）

### 官方公开社交入口

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）

### 公开渠道/隐私边界

本档案只记录官方公开的项目反馈入口；不把合成对话中的角色、邮件或日程示例当真实个人联系信息。

[来源1](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2501.17399

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### PDF SHA-256

70b688b241c7f4e5ec0b6639f6eaf044ddc19dcf60ee7329d8078ec8a3aa285f

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### PDF字节数

2789352

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源1](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）

### Drive文件夹

待核实

> 状态：待核实。

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-07）

### 其他官方文档

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://labs.scale.com/leaderboard/multichallenge?tab=large"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2501.17399"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/pdf/2501.17399",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/ekwinox117/multi-challenge/blob/main/README.md",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/ScaleAI/MultiChallenge",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md",
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2501.17399)（访问 2026-11-08）；[来源3](https://arxiv.org/pdf/2501.17399)（访问 2026-11-08）；[来源4](https://github.com/ekwinox117/multi-challenge/blob/main/README.md)（访问 2026-11-08）；[来源5](https://github.com/ekwinox117/multi-challenge/blob/main/data/benchmark_questions.jsonl)（访问 2026-11-08）；[来源6](https://huggingface.co/datasets/ScaleAI/MultiChallenge)（访问 2026-11-08）；[来源7](https://huggingface.co/datasets/ScaleAI/MultiChallenge/raw/main/README.md)（访问 2026-11-08）

### Drive原始PDF

待核实

> 状态：待核实。

> 本组仅本地建页，未上传Drive，不伪造归档链接。

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-07）

## 变更记录

### 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。Large/Small是模型分组，不新建不同benchmark；与IFEval单轮形式约束互补而非同一测试。 热度与榜单口径分离，不确定值标记待核实。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST, UTC+9)",
    "change": "第二轮深度复核：重读官方数据卡、README/许可、可用论文abs与PDF及官方榜；补精确题量、修订边界与完整可读成绩；区分私有集、历史基线、厂商自报与独立测评。"
  }
]
```

[来源1](https://labs.scale.com/leaderboard/multichallenge?tab=large)（访问 2026-11-08）
