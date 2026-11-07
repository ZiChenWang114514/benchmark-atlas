# VoiceCodeBench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: B；未核实保留标记

## 基本信息

### 简称

VoiceCodeBench

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 全称

VoiceCodeBench

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 论文版本

v2（本次打开全文的Version 2 note）

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 主板块

语音

> Benchmark Atlas编辑分类。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 领域标签

- 语音

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 许可证

非音频材料MIT；音频附加禁止声音克隆限制，须阅读完整LICENSE。

[来源](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2608.28916

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 代码

https://huggingface.co/datasets/besimple-ai/voice-code-bench

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/besimple-ai/voice-code-bench

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 官方主页

https://www.vals.ai/benchmarks/voice-code-bench

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 论文标题

VoiceCodeBench: Evaluating Exact Structured-Token Recovery in Automatic Speech Recognition

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

## 发起与维护

### 发起方

Besimple AI

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 合作方

Vals AI提供外部实现与榜单；不据此推断共同创建数据。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 作者

- Tyler Baumgartner
- Brandon Tai
- Lisa Kaelin-Martin
- Candice Fan
- Luc Debaupte
- Bill Wang
- Yi Zhong

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 维护方

Besimple AI维护数据；Vals AI维护其评测实现

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 资助

Besimple, Inc.

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

## 设计目标

### 衡量能力

英语工作语音中精确恢复电话、标识符、路径、URL、命令与单位等结构值。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 设计背景

WER相近的转写可能在关键值上不同，流畅文本未必可供软件正确执行。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

## 构建方式

### 题目来源

先选实体类型、数量与难度，再用合成值构建工作场景和脚本；人类录音。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 出题者背景

85位付费、同意数据发布的录音贡献者；研究团队审核实体。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 审核

LLM辅助脚本生成，经人工自然性、唯一性、实体一致性与可恢复性审核；录音质量差则重录。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 质量控制

1482实体审计；原12系统中分层200判决人工审计完全一致，但不保证裁判零错误。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 去污染

public test-only，不提供训练集；公开标签意味着可被适配，需披露任何benchmark特化。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

## 数据形式

### 题量与规模

300 WAV录音，5.587小时、85说话者、1482实体、26类型、8工作流领域。

[来源](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07）

### 题型

音频转写；template/acoustic/canonical三层文本与实体标注。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 模态

- 音频
- 文本

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 语言

英语

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 难度

light、standard、dense、stress；人为配额不代表生产分布。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 公开与隐藏划分

300录音单一公开test split，无训练语料或隐藏榜单。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

## 评测方法

### 指标

TSR=全部目标实体都正确的录音比例；CTEM=正确实体比例；WER/WAcc作辅助。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 评分

版本化LLM verifier判断canonical值是否可唯一恢复；无害格式变化允许，错符号、数字或单位不允许；TSR不给部分分。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 运行设置

raw-audio-only，不给领域、实体提示、词表、语法约束或转写后修正。流式仅评分final transcript。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 官方脚本

HF中scripts及评分/reproduce_release.sh；Vals移植到Valkyrie。

[来源](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07）

### 可比性警示

Vals榜与作者HF当前23系统结果不同，模型/端点/流式设置不同不得直接混排；WER还需区分v1普通与v2 format-invariant。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：待核实
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/voice-code-bench", "date": "2026-11-07", "date_type": "observed_on", "note": "Vals榜明确更新2026-09-24；作者卡还记录2026-10-08/09追加运行。按候选保留B，不声称行业广泛采用。"}, {"url": "https://huggingface.co/datasets/besimple-ai/voice-code-bench", "date": "2026-11-07", "date_type": "observed_on", "note": "Vals榜明确更新2026-09-24；作者卡还记录2026-10-08/09追加运行。按候选保留B，不声称行业广泛采用。"}]

> Vals榜明确更新2026-09-24；作者卡还记录2026-10-08/09追加运行。按候选保留B，不声称行业广泛采用。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 污染、争议与限制

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 为什么近期热门

Vals榜明确更新2026-09-24；作者卡还记录2026-10-08/09追加运行。按候选保留B，不声称行业广泛采用。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问2026-11-07）；[来源](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 官方榜单入口

https://www.vals.ai/benchmarks/voice-code-bench

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 第三方覆盖

https://www.vals.ai/benchmarks/voice-code-bench

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | GPT Live Transcribe | 67.67 | Vals实现 TSR (%) | 2026-09-24 |
| 2 | Grok Voice Transcribe 2.0 | 65.33 | Vals实现 TSR (%) | 2026-09-24 |
| 3 | Cartesia Ink 2 | 62.0 | Vals实现 TSR (%) | 2026-09-24 |

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问2026-11-07）

### 覆盖与时效

这里固定Vals 2026-09-24表。作者HF当前另报Deepgram Nova-3与GPT live streaming同为68.7%；不混排两个实现。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）；[来源](https://huggingface.co/datasets/besimple-ai/voice-code-bench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- tyler@besimple.ai
- yi@besimple.ai

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2608.28916

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2608.28916)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://www.vals.ai/benchmarks/voice-code-bench"}

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://www.vals.ai/benchmarks/voice-code-bench)（访问 2026-11-07）
