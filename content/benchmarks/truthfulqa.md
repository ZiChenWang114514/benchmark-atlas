# TruthfulQA

> 本页中文整理与复核：2026-11-08。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

TruthfulQA专门检测模型是否复述人类常见误解，但“回答真实”与“回答有信息”是两件事。原始817题、当前官方CSV790题和2025二选一设置必须分版本；MC2的概率质量也不是普通单选准确率。

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08，）

## 基本信息

### 简称

TruthfulQA

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 全称

TruthfulQA: Measuring How Models Mimic Human Falsehoods

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md)（访问 2026-11-07，）

### 基准版本

官方README推荐2025年1月更新的二选一设置；原MC1、MC2与生成任务需分别标注。

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md)（访问 2026-11-07，）

### 论文版本

arXiv v2；提交于 2022-05-08 11:43:02

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 发布日期

2021-09-09 02:15:27 （arXiv v1提交；不是2025二选一改版日）

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 主板块

安全

说明：Benchmark Constitution编辑归档，不是论文指定的唯一领域。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 领域标签

- 真实性与误解诱发的幻觉

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 许可与适用范围

Apache-2.0（官方仓库LICENSE；参考答案涉及的外部文献另核授权）。

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/LICENSE)（访问 2026-11-07，）

### 论文

https://arxiv.org/abs/2109.07958

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 代码仓库

https://github.com/sylinrl/TruthfulQA

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 数据地址

https://github.com/sylinrl/TruthfulQA

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 官方主页

https://github.com/sylinrl/TruthfulQA

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 论文标题

TruthfulQA: Measuring How Models Mimic Human Falsehoods

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

## 发起与维护

### 机构与发起关系

作者 Stephanie Lin、Jacob Hilton、Owain Evans，单位涉及 Oxford 与 OpenAI；此处不推断正式联合发起协议。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 合作机构

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 作者

- Lin, Stephanie
- Hilton, Jacob
- Evans, Owain

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 当前维护方

官方代码与反馈由 sylinrl/TruthfulQA 仓库提供；个人持续维护职责及响应时限未核实。

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md)（访问 2026-11-07，）

### 资助与支持

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

## 设计目标

### 衡量能力

检验模型是否复述人类常见误解，而非只看回答流畅度。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 设计背景

模仿互联网文本可能学习流行错误；知识问答准确率不直接等于避免误导。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

## 构建方式

### 题目或数据来源

作者编写与常见误解相关的问题；437 道通过 GPT-3 对抗筛选，380 道未筛选。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 出题背景

研究团队撰写问题并核查答案，覆盖多个日常与专业领域。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 审核流程

区分真实与信息充分，人工检查答案并训练自动裁判。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 质量控制

同时衡量 truthfulness 与 informativeness，避免把无信息拒答误作有用事实回答。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 去污染与泄漏

README含训练排除canary，明确BIG-bench中有较小同源任务，两者相互测试时不得把另一套加入训练；这是使用约束，不是模型训练污染已排除的证明。

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）

## 数据形式

### 规模

原论文817题、38类；本次读取官方main/TruthfulQA.csv实际790条（不含表头），含Best Incorrect Answer列。HF传统卡仍为817条，属于旧协议，不能以817替代当前CSV题量。

来源：[1](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)（访问 2026-11-08，）；[2](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）；[3](https://huggingface.co/datasets/truthfulqa/truthful_qa/raw/main/README.md)（访问 2026-11-08，）；[4](https://arxiv.org/pdf/2109.07958)（访问 2026-11-08，）

### 题型

开放生成及多项选择两种评测方式

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 模态

文本

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 语言

英语

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 难度

专门诱发常见误解；对抗筛选题与未筛选题的分布不同。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 数据划分

公开题集及参考正确/错误答案；不得在测试示例上调优后当作原始零样本结果。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

## 评测方法

### 指标

生成任务同时报告真实性与信息性；MC1为最高答案对数概率的单正确答案准确率，MC2为正确答案归一化概率总和；2025二选一设置需随机化正确/错误选项顺序。

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md)（访问 2026-11-07，）

### 评分方式

生成任务可用人工或GPT-judge；MC2衡量正确答案集合的归一化概率质量，不是普通单选准确率。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 提示与运行设置

原论文零样本，不用本基准示例调优；greedy生成；提示风格会显著影响回答与拒答。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 评测脚本

https://github.com/sylinrl/TruthfulQA

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-07，）

### 可比性提醒

只答“我不知道”可能被判真实但无信息；truthfulness、true+informative、MC1、MC2不可混比。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）

### 数据版本与更新

```json
{
  "version": "README记载2025年1月二选一更新；精确commit未固定"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2610.11978v1"
      "date": "2026-10"
      "note": "Jev研究表1、表2和附录A实际使用TruthfulQA；MC2与所选答案准确率分别注明。"
    }
  ]
}
```

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md)（访问 2026-11-07，）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07，）

### 论文修订记录

- {"version": "v1", "submitted_at": "2021-09-09 02:15:27 ", "timezone": ""}
- {"version": "v2", "submitted_at": "2022-05-08 11:43:02 ", "timezone": ""}

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-08，）

### 饱和证据与局限

不同协议不能给出统一饱和判断。2026-H2 Jev研究在817题的选项准确率上Gemini 3.8 Flash为97.9%，不是2025二选一790题的分数，也不是生成任务真实且有信息的比例。

来源：[1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08，）；[2](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）

### 争议与已知问题

2025更新删除失效问题与Indexical Error: Time类；官方明确尚未完成其余问题及来源的完整复核。790条当前CSV、817条传统HF及论文选择题研究分开；“真实性”不等于“信息充分”。

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）；[2](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)（访问 2026-11-08，）；[3](https://huggingface.co/datasets/truthfulqa/truthful_qa/raw/main/README.md)（访问 2026-11-08，）

### 衍生或后继基准

BIG-bench包含较小同源任务；2025年1月官方新增二选一版（正确与最佳错误答案随机排A/B），推荐新设置但保留MC1/MC2有效性。

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）

## 榜单快照

### 快照访问日期

2026-11-08

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08，）

### 官方榜单入口

https://arxiv.org/abs/2109.07958

说明：未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-07，）

### 第三方入口

https://arxiv.org/html/2610.11978v1

来源：[1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08，）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| 官方README历史基线 / % true | 4 | GPT-3 175B | 20.44 | % true | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % info | 1 | GPT-3 175B | 97.55 | % info | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true (GPT-judge) | 4 | GPT-3 175B | 20.56 | % true (GPT-judge) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEURT | 4 | GPT-3 175B | -0.54 | BLEURT | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / ROUGE | 4 | GPT-3 175B | -17.17 | ROUGE | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEU | 4 | GPT-3 175B | -17.18 | BLEU | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC1 (0–1) | 2 | GPT-3 175B | 0.21 | MC1 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC2 (0–1) | 4 | GPT-3 175B | 0.33 | MC2 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true | 3 | GPT-J 6B | 26.68 | % true | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % info | 2 | GPT-J 6B | 89.96 | % info | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true (GPT-judge) | 3 | GPT-J 6B | 27.54 | % true (GPT-judge) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEURT | 3 | GPT-J 6B | -0.29 | BLEURT | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / ROUGE | 3 | GPT-J 6B | -10.93 | ROUGE | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEU | 3 | GPT-J 6B | -7.48 | BLEU | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC1 (0–1) | 3 | GPT-J 6B | 0.2 | MC1 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC2 (0–1) | 2 | GPT-J 6B | 0.36 | MC2 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true | 2 | GPT-2 1.5B | 29.5 | % true | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % info | 3 | GPT-2 1.5B | 89.84 | % info | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true (GPT-judge) | 2 | GPT-2 1.5B | 30.72 | % true (GPT-judge) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEURT | 2 | GPT-2 1.5B | -0.24 | BLEURT | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / ROUGE | 2 | GPT-2 1.5B | -9.02 | ROUGE | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEU | 2 | GPT-2 1.5B | -4.83 | BLEU | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC1 (0–1) | 1 | GPT-2 1.5B | 0.22 | MC1 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC2 (0–1) | 1 | GPT-2 1.5B | 0.39 | MC2 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true | 1 | UnifiedQA 3B | 53.86 | % true | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % info | 4 | UnifiedQA 3B | 64.5 | % info | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / % true (GPT-judge) | 1 | UnifiedQA 3B | 56.18 | % true (GPT-judge) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEURT | 1 | UnifiedQA 3B | 0.08 | BLEURT | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / ROUGE | 1 | UnifiedQA 3B | 1.92 | ROUGE | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / BLEU | 1 | UnifiedQA 3B | -0.17 | BLEU | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC1 (0–1) | 4 | UnifiedQA 3B | 0.19 | MC1 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| 官方README历史基线 / MC2 (0–1) | 3 | UnifiedQA 3B | 0.35 | MC2 (0–1) | README Baselines表；非2025二选一新跑分；greedy / temperature 0 | [来源页未列运行日](https://github.com/sylinrl/TruthfulQA)；采集2026-11-08 |
| Jev研究表2 / 原817题选项准确率 | 1 | Gemini 3.8 Flash（研究表2原标签） | 97.9 | selected-option accuracy (%) | 817-item evaluation；非MC2； | [2026-10-08（论文标示日）](https://arxiv.org/html/2610.11978v1)；采集2026-11-08 |
| Jev研究表2 / 原817题选项准确率 | 2 | Claude Opus 5.5（研究表2原标签） | 92.0 | selected-option accuracy (%) | 817-item evaluation；非MC2； | [2026-10-08（论文标示日）](https://arxiv.org/html/2610.11978v1)；采集2026-11-08 |
| Jev研究表2 / 原817题选项准确率 | 3 | Jev（研究表2原标签） | 87.5 | selected-option accuracy (%) | 817-item evaluation；非MC2； | [2026-10-08（论文标示日）](https://arxiv.org/html/2610.11978v1)；采集2026-11-08 |

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08，）

### 榜单覆盖边界

官方README历史Baselines完整4模型×8指标共32行，分指标不混排；另保留Jev论文表2的3条选项准确率并依据附录A明确817题、非MC2。此前未指明版本的问题已补齐。无本次新核实的2025二选一790题官方当前模型榜。

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08，）

## 联系方式

### 官方公开邮箱

- sylin07@gmail.com

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-07，）

### 公开反馈渠道

https://github.com/sylinrl/TruthfulQA/issues

说明：公开反馈入口；未发送问题。

来源：[1](https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md)（访问 2026-11-07，）

### 官方社交账号

待核实

说明：已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

来源：[1](https://arxiv.org/abs/2109.07958)（访问 2026-11-07，）

### 联系方式/隐私原则

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07，）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2109.07958

来源：[1](https://arxiv.org/pdf/2109.07958)（访问 2026-11-08，）

### PDF SHA-256

6e86175861d24d075bbd8fec987cbdabd0d6332700b001a1ccf335fa72f541b2

来源：[1](https://arxiv.org/pdf/2109.07958)（访问 2026-11-08，）

### PDF字节数

```json
819857
```

来源：[1](https://arxiv.org/pdf/2109.07958)（访问 2026-11-08，）

### 文件夹

```json
{
  "id": "1K67pMyWmwzHPTWfWS6Qbhpuz0ZhyOsLv"
  "webViewLink": "
}
```

来源：[1]( 2026-11-07，）

### 其他文档

- {"kind": "中文介绍", "id": "1Gd-3UCMu3Qp3aNooWo3Sq2Ar2Bo1hlC06er3pz1o26E", "webViewLink": "

来源：[1]( 2026-11-07，）

### 论文原件

```json
{
  "id": "12HuAWYz_OBaC5-Hlk_sLg1mzUbeHUD1k"
  "webViewLink": "
}
```

来源：[1]( 2026-11-07，）

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://github.com/sylinrl/TruthfulQA)（访问 2026-11-08，）
