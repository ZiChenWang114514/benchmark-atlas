# MMAU

> Benchmark Constitution · 深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MMAU把语音、环境声音和音乐放在同一个音频理解评测框架下，以音频加多选题测试27类任务。当前修订版v05.15.25与原论文首版不同，且test-mini公开答案、完整test保留答案；两者规模与成绩不能混合排名。代码Apache-2.0和数据CC-BY-NC-4.0也应分别记录。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini)（访问 2026-11-07）

### 简称

MMAU

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 全称

Massive Multi-Task Audio Understanding and Reasoning

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 基准版本

MMAU-v05.15.25

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 论文版本

arXiv v1

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 发布日期

2024-10-25（；arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 主板块

多模态

> Benchmark Constitution编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 领域标签

- 语音、声音与音乐理解推理

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 许可证与权利边界

代码仓库LICENSE为Apache-2.0；HF test-mini数据卡为CC-BY-NC-4.0。代码许可不等于音频再利用许可，上游音频权利另遵守。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/LICENSE)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini/raw/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2410.19168

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 代码仓库

https://github.com/Sakshi113/MMAU

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini)（访问 2026-11-07）

### 官方主页

https://sakshi113.github.io/mmau_homepage/

[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 论文标题

MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

马里兰大学College Park与Adobe作者团队。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 合作方

- University of Maryland, College Park
- Adobe

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 作者

- Sakshi, S
- Tyagi, Utkarsh
- Kumar, Sonal
- Seth, Ashish
- Selvakumar, Ramaneswaran
- Nieto, Oriol
- Duraiswami, Ramani
- Ghosh, Sreyan
- Manocha, Dinesh

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）

### 维护方

MMAU作者团队；官方README列S Sakshi、Sonal Kumar与Sreyan Ghosh为联系方，test评测自2026-01-30迁至sonalkum/MMAU-Eval。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 资助

待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

## 设计目标

### 衡量能力

语音、环境声音、音乐的专家知识、信息提取及复杂推理。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 设计背景

早期音频评测偏识别或单一领域，缺少跨三大音频领域的专家级复杂推理。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

## 构建方式

### 题目来源

从13个音频语料出发，优先真实录音；专家将初选90任务筛至27任务，编写问题答案，经独立专家筛查，再扩增干扰选项并复审。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 出题与审阅者背景

语音、声音、音乐领域专家，作者协助筛选音频与迭代设计。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 审核流程

不同专家团队剔除歧义、过度复杂及音质差的问答；2025年版本更新进一步修订问题答案和部分音频。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 质量控制

v05.15.25按社区反馈修订约25%问答、改善约5%音频；原论文C.3要求音频不损坏、英语问句、task/difficulty/dataset标签、仅保留MCQ。版权指南要求排除禁止复制和再分发的网站素材。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 去污染及其证据边界

test答案和解释不公开，通过HF Space计算分数；公开音频原料仍可能与训练语料重叠，不能宣称无污染。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

10,000音频问答、27任务；test-mini 1,000、test 9,000。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/gamma-lab-umd/MMAU-test-mini)（访问 2026-11-07）

### 题型

音频加自然语言多选问答，覆盖speech、sound、music。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 模态

音频+文本

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 语言

- **question_language**：English（原论文Appendix C.3要求所有问题使用英语）
- **audio_language_distribution**：待核实

> 严格区分问句语言和源音频语言，不用英语问题推断所有音频为英语。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 难度

原论文Easy:Medium:Hard = 22%:56%:22%；不能默认代表v05.15.25修订后的精确分布。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 公开与隐藏划分

10,000题：test-mini 1,000题公开答案；test 9,000题公开问题而保留答案与解释，通过官方HF Space提交预测评测。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

官方evaluation.py解析model_prediction并计算选项正确率；三音频领域和平均分分别报告。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 评分方法

官方evaluation.py解析model_prediction并计算选项正确率；三音频领域和平均分分别报告。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 运行与提示设置

记录音频预处理、输出解析、test-mini/test及数据版本。2026年不确定性研究将正确选项放到各位置后取均值，另有删除选项的open-ended协议。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 官方脚本

https://github.com/Sakshi113/MMAU

[来源](https://github.com/Sakshi113/MMAU)（访问 2026-11-07）

### 可比性警示

新版v05.15.25与旧榜单不可混用；README/主页称12提取+15推理任务，但arXiv v1正文为11提取+16推理，合计均27，细分待核实。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

MMAU-v05.15.25：约25%问答修订、约5%音频改进；2026-01-30 test评测从EvalAI迁到HF Space。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2024-10-25；- **timezone**：
- **continued_use_2026h2**：- - **url**：https://arxiv.org/html/2609.28879v1；- **date**：2026-09-24；- **note**：Broadening Uncertainty Estimation for Audio Question Answering 在 MMAU 音频问答数据上实际研究不确定性估计与不同问题格式。；- **date_kst**：2026-09-24；- **verified_in_round1**：重新打开正文及实验表格和abs提交历史；是实际评测而非仅参考文献。
- **verification**：已打开并复核证据原文的实际评测章节及表格，不只按参考文献或网页存活判断。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2609.28879)（访问 2026-11-08）

### 饱和情况

v05.15.25完整test当前官方parsed文件最高Avg 75.98%，低于满分；不能拿test-mini、旧版本或选择题排列平均结果混合推断饱和。

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 污染、争议与限制

新版v05.15.25与旧榜单不可混用；README/主页称12提取+15推理任务，但arXiv v1正文为11提取+16推理，合计均27，细分待核实。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

### 衍生与版本关系

MMAU-Pro（官方2025-08-19公告），不与MMAU原版/修订版成绩混合。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（；采集日，不冒充评测运行日）

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）

### 官方入口

https://sakshi113.github.io/mmau_homepage/#leaderboard-v15-parsed

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 第三方覆盖入口

待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

[来源](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07）

### 分来源与协议的精确成绩

#### 官方v05.15.25 parsed / Test

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Audio-Thinker | 75.98 | accuracy / % |
| Nova 2 Omni | 75.28 | accuracy / % |
| Step-Audio-2 | 73.86 | accuracy / % |
| MiMo-Audio | 72.59 | accuracy / % |
| Audio Flamingo 3 | 72.42 | accuracy / % |
| Qwen2.5-Omni | 71.00 | accuracy / % |
| Step-Audio-2-mini | 70.23 | accuracy / % |
| Gemini 2.5 Pro | 69.36 | accuracy / % |
| Gemini 2.5 Flash | 67.39 | accuracy / % |
| Gemini 2.0 Flash | 67.03 | accuracy / % |
| DeSTA2.5-Audio | 65.21 | accuracy / % |
| Kimi-Audio | 64.40 | accuracy / % |
| Audio Reasoner | 63.78 | accuracy / % |
| Phi-4-multimodal | 62.81 | accuracy / % |
| Gemini 2.5 Flash Lite | 61.61 | accuracy / % |
| Audio Flamingo 2 | 61.06 | accuracy / % |
| GPT-4o Audio | 60.82 | accuracy / % |
| Qwen2-Audio-Instruct | 57.40 | accuracy / % |
| Gemma 3n | 55.20 | accuracy / % |
| Gemma 3n | 52.06 | accuracy / % |
| GPT-4o mini Audio | 51.03 | accuracy / % |
| M2UGen | 39.76 | accuracy / % |
| MusiLingo | 38.29 | accuracy / % |
| SALMONN | 36.23 | accuracy / % |
| MuLLaMa | 25.91 | accuracy / % |
| GAMA-IT | 22.22 | accuracy / % |
| GAMA | 21.68 | accuracy / % |
| LTU | 17.23 | accuracy / % |
| Audio Flamingo Chat | 15.59 | accuracy / % |

- **Audio-Thinker**：- **rank**：1；- **scope**：9000题test；- **sound**：78.8；- **music**：73.8；- **speech**：75.16；- **model_link**：https://arxiv.org/pdf/2508.08039v1；- **model_size**：8.4B
- **Nova 2 Omni**：- **rank**：2；- **scope**：9000题test；- **sound**：77.87；- **music**：66.37；- **speech**：81.82；- **model_link**：https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models；- **model_size**：-
- **Step-Audio-2**：- **rank**：3；- **scope**：9000题test；- **sound**：80.60；- **music**：68.23；- **speech**：72.75；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：-
- **MiMo-Audio**：- **rank**：4；- **scope**：9000题test；- **sound**：77.2；- **music**：69.73；- **speech**：70.77；- **model_link**：https://github.com/XiaomiMiMo/MiMo-Audio/；- **model_size**：7B
- **Audio Flamingo 3**：- **rank**：5；- **scope**：9000题test；- **sound**：75.83；- **music**：74.47；- **speech**：66.97；- **model_link**：https://www.arxiv.org/abs/2507.08128；- **model_size**：8.2B
- **Qwen2.5-Omni**：- **rank**：6；- **scope**：9000题test；- **sound**：76.77；- **music**：67.33；- **speech**：68.90；- **model_link**：https://arxiv.org/abs/2503.20215；- **model_size**：8.2B
- **Step-Audio-2-mini**：- **rank**：7；- **scope**：9000题test；- **sound**：75.57；- **music**：66.85；- **speech**：66.49；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：8.3B
- **Gemini 2.5 Pro**：- **rank**：8；- **scope**：9000题test；- **sound**：70.63；- **music**：64.77；- **speech**：72.67；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Gemini 2.5 Flash**：- **rank**：9；- **scope**：9000题test；- **sound**：69.50；- **music**：69.40；- **speech**：68.27；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Gemini 2.0 Flash**：- **rank**：10；- **scope**：9000题test；- **sound**：68.93；- **music**：59.30；- **speech**：72.87；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **DeSTA2.5-Audio**：- **rank**：11；- **scope**：9000题test；- **sound**：66.83；- **music**：57.10；- **speech**：71.94；- **model_link**：https://arxiv.org/abs/2507.02768；- **model_size**：8B
- **Kimi-Audio**：- **rank**：12；- **scope**：9000题test；- **sound**：70.70；- **music**：65.93；- **speech**：56.57；- **model_link**：https://arxiv.org/abs/2504.18425；- **model_size**：8.2B
- **Audio Reasoner**：- **rank**：13；- **scope**：9000题test；- **sound**：67.27；- **music**：61.53；- **speech**：62.53；- **model_link**：https://huggingface.co/zhifeixie/Audio-Reasoner/tree/main；- **model_size**：8.2B
- **Phi-4-multimodal**：- **rank**：14；- **scope**：9000题test；- **sound**：62.67；- **music**：61.97；- **speech**：63.80；- **model_link**：https://huggingface.co/microsoft/phi-4；- **model_size**：5.5B
- **Gemini 2.5 Flash Lite**：- **rank**：15；- **scope**：9000题test；- **sound**：62.50；- **music**：54.87；- **speech**：67.47；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Audio Flamingo 2**：- **rank**：16；- **scope**：9000题test；- **sound**：68.13；- **music**：70.20；- **speech**：44.87；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：3B
- **GPT-4o Audio**：- **rank**：17；- **scope**：9000题test；- **sound**：63.20；- **music**：49.93；- **speech**：69.33；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **Qwen2-Audio-Instruct**：- **rank**：18；- **scope**：9000题test；- **sound**：61.17；- **music**：55.67；- **speech**：55.37；- **model_link**：https://arxiv.org/abs/2407.10759；- **model_size**：7B
- **Gemma 3n**：- **rank**：19；- **scope**：9000题test；- **sound**：50.27；- **music**：53.20；- **speech**：62.13；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：4B
- **Gemma 3n**：- **rank**：20；- **scope**：9000题test；- **sound**：47.47；- **music**：51.63；- **speech**：57.07；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：2B
- **GPT-4o mini Audio**：- **rank**：21；- **scope**：9000题test；- **sound**：49.67；- **music**：35.97；- **speech**：67.47；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **M2UGen**：- **rank**：22；- **scope**：9000题test；- **sound**：44.97；- **music**：38.53；- **speech**：35.77；- **model_link**：https://huggingface.co/M2UGen/M2UGen-MusicGen-medium；- **model_size**：7B
- **MusiLingo**：- **rank**：23；- **scope**：9000题test；- **sound**：41.93；- **music**：41.23；- **speech**：31.70；- **model_link**：https://huggingface.co/m-a-p/MusiLingo-long-v1；- **model_size**：7B
- **SALMONN**：- **rank**：24；- **scope**：9000题test；- **sound**：42.10；- **music**：37.83；- **speech**：28.77；- **model_link**：https://arxiv.org/pdf/2310.13289；- **model_size**：13B
- **MuLLaMa**：- **rank**：25；- **scope**：9000题test；- **sound**：30.97；- **music**：29.67；- **speech**：17.10；- **model_link**：https://arxiv.org/pdf/2308.11276；- **model_size**：7B
- **GAMA-IT**：- **rank**：26；- **scope**：9000题test；- **sound**：32.73；- **music**：22.37；- **speech**：11.57；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA-IT；- **model_size**：7B
- **GAMA**：- **rank**：27；- **scope**：9000题test；- **sound**：30.73；- **music**：17.33；- **speech**：16.97；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA；- **model_size**：7B
- **LTU**：- **rank**：28；- **scope**：9000题test；- **sound**：20.67；- **music**：15.68；- **speech**：15.33；- **model_link**：https://openreview.net/pdf?id=nBZBPXdJlC；- **model_size**：7B
- **Audio Flamingo Chat**：- **rank**：29；- **scope**：9000题test；- **sound**：23.33；- **music**：15.77；- **speech**：7.67；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：1B

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）

#### 官方v05.15.25 parsed / Test-mini

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Nova 2 Omni | 77.8 | accuracy / % |
| Audio-Thinker | 77.7 | accuracy / % |
| Step-Audio-2 | 77.58 | accuracy / % |
| MiMo-Audio | 74.7 | accuracy / % |
| Audio Flamingo 3 | 73.30 | accuracy / % |
| Step-Audio-2-mini | 72.73 | accuracy / % |
| Gemini 2.5 Flash | 71.80 | accuracy / % |
| Gemini 2.5 Pro | 71.60 | accuracy / % |
| Qwen2.5-Omni | 71.50 | accuracy / % |
| Gemini 2.0 Flash | 70.50 | accuracy / % |
| Kimi-Audio | 68.20 | accuracy / % |
| Audio Reasoner | 67.70 | accuracy / % |
| Gemini 2.5 Flash Lite | 66.20 | accuracy / % |
| DeSTA2.5-Audio | 66.00 | accuracy / % |
| Phi-4-multimodal | 65.70 | accuracy / % |
| GPT-4o Audio | 62.50 | accuracy / % |
| Audio Flamingo 2 | 62.40 | accuracy / % |
| Qwen2-Audio-Instruct | 59.60 | accuracy / % |
| Gemma 3n | 58.00 | accuracy / % |
| GPT-4o mini Audio | 53.00 | accuracy / % |
| Gemma 3n | 51.69 | accuracy / % |
| MusiLingo | 38.20 | accuracy / % |
| M2UGen | 37.90 | accuracy / % |
| SALMONN | 34.90 | accuracy / % |
| MuLLaMa | 27.60 | accuracy / % |
| GAMA-IT | 22.83 | accuracy / % |
| GAMA | 20.82 | accuracy / % |
| LTU | 17.44 | accuracy / % |
| Audio Flamingo Chat | 16.60 | accuracy / % |

- **Nova 2 Omni**：- **rank**：1；- **scope**：1000题test-mini；- **sound**：81.08；- **music**：70.36；- **speech**：81.98；- **model_link**：https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models；- **model_size**：-
- **Audio-Thinker**：- **rank**：2；- **scope**：1000题test-mini；- **sound**：81.98；- **music**：74.25；- **speech**：76.88；- **model_link**：https://arxiv.org/pdf/2508.08039v1；- **model_size**：8.4B
- **Step-Audio-2**：- **rank**：3；- **scope**：1000题test-mini；- **sound**：84.04；- **music**：73.56；- **speech**：75.15；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：-
- **MiMo-Audio**：- **rank**：4；- **scope**：1000题test-mini；- **sound**：81.68；- **music**：74.25；- **speech**：68.17；- **model_link**：https://github.com/XiaomiMiMo/MiMo-Audio/；- **model_size**：7B
- **Audio Flamingo 3**：- **rank**：5；- **scope**：1000题test-mini；- **sound**：79.58；- **music**：73.95；- **speech**：66.37；- **model_link**：https://www.arxiv.org/abs/2507.08128；- **model_size**：8.2B
- **Step-Audio-2-mini**：- **rank**：6；- **scope**：1000题test-mini；- **sound**：79.30；- **music**：68.44；- **speech**：68.16；- **model_link**：https://arxiv.org/abs/2507.16632；- **model_size**：8.3B
- **Gemini 2.5 Flash**：- **rank**：7；- **scope**：1000题test-mini；- **sound**：73.27；- **music**：65.57；- **speech**：76.58；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Gemini 2.5 Pro**：- **rank**：8；- **scope**：1000题test-mini；- **sound**：75.08；- **music**：68.26；- **speech**：71.47；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Qwen2.5-Omni**：- **rank**：9；- **scope**：1000题test-mini；- **sound**：78.10；- **music**：65.90；- **speech**：70.60；- **model_link**：https://arxiv.org/abs/2503.20215；- **model_size**：8.2B
- **Gemini 2.0 Flash**：- **rank**：10；- **scope**：1000题test-mini；- **sound**：71.17；- **music**：65.27；- **speech**：75.08；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **Kimi-Audio**：- **rank**：11；- **scope**：1000题test-mini；- **sound**：75.68；- **music**：66.77；- **speech**：62.16；- **model_link**：https://arxiv.org/abs/2504.18425；- **model_size**：8.2B
- **Audio Reasoner**：- **rank**：12；- **scope**：1000题test-mini；- **sound**：67.87；- **music**：69.16；- **speech**：66.07；- **model_link**：https://huggingface.co/zhifeixie/Audio-Reasoner/tree/main；- **model_size**：8.2B
- **Gemini 2.5 Flash Lite**：- **rank**：13；- **scope**：1000题test-mini；- **sound**：63.06；- **music**：63.47；- **speech**：72.07；- **model_link**：https://ai.google.dev/gemini-api/docs/models；- **model_size**：-
- **DeSTA2.5-Audio**：- **rank**：14；- **scope**：1000题test-mini；- **sound**：70.27；- **music**：56.29；- **speech**：71.47；- **model_link**：https://arxiv.org/abs/2507.02768；- **model_size**：8B
- **Phi-4-multimodal**：- **rank**：15；- **scope**：1000题test-mini；- **sound**：65.47；- **music**：64.37；- **speech**：67.27；- **model_link**：https://huggingface.co/microsoft/phi-4；- **model_size**：5.5B
- **GPT-4o Audio**：- **rank**：16；- **scope**：1000题test-mini；- **sound**：64.56；- **music**：56.29；- **speech**：66.67；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **Audio Flamingo 2**：- **rank**：17；- **scope**：1000题test-mini；- **sound**：71.47；- **music**：70.96；- **speech**：44.74；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：3B
- **Qwen2-Audio-Instruct**：- **rank**：18；- **scope**：1000题test-mini；- **sound**：67.27；- **music**：56.29；- **speech**：55.26；- **model_link**：https://arxiv.org/abs/2407.10759；- **model_size**：7B
- **Gemma 3n**：- **rank**：19；- **scope**：1000题test-mini；- **sound**：55.86；- **music**：56.89；- **speech**：61.26；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：4B
- **GPT-4o mini Audio**：- **rank**：20；- **scope**：1000题test-mini；- **sound**：50.75；- **music**：39.22；- **speech**：69.07；- **model_link**：https://arxiv.org/abs/2410.21276；- **model_size**：-
- **Gemma 3n**：- **rank**：21；- **scope**：1000题test-mini；- **sound**：51.35；- **music**：52.10；- **speech**：52.22；- **model_link**：https://deepmind.google/models/gemma/gemma-3n/；- **model_size**：2B
- **MusiLingo**：- **rank**：22；- **scope**：1000题test-mini；- **sound**：43.24；- **music**：40.12；- **speech**：31.23；- **model_link**：https://huggingface.co/m-a-p/MusiLingo-long-v1；- **model_size**：7B
- **M2UGen**：- **rank**：23；- **scope**：1000题test-mini；- **sound**：43.24；- **music**：37.13；- **speech**：33.33；- **model_link**：https://huggingface.co/M2UGen/M2UGen-MusicGen-medium；- **model_size**：7B
- **SALMONN**：- **rank**：24；- **scope**：1000题test-mini；- **sound**：41.14；- **music**：37.13；- **speech**：26.43；- **model_link**：https://arxiv.org/pdf/2310.13289；- **model_size**：13B
- **MuLLaMa**：- **rank**：25；- **scope**：1000题test-mini；- **sound**：33.03；- **music**：32.34；- **speech**：17.42；- **model_link**：https://arxiv.org/pdf/2308.11276；- **model_size**：7B
- **GAMA-IT**：- **rank**：26；- **scope**：1000题test-mini；- **sound**：30.93；- **music**：26.74；- **speech**：10.81；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA-IT；- **model_size**：7B
- **GAMA**：- **rank**：27；- **scope**：1000题test-mini；- **sound**：31.83；- **music**：17.71；- **speech**：12.91；- **model_link**：https://huggingface.co/spaces/sonalkum/GAMA；- **model_size**：7B
- **LTU**：- **rank**：28；- **scope**：1000题test-mini；- **sound**：20.42；- **music**：15.97；- **speech**：15.92；- **model_link**：https://openreview.net/pdf?id=nBZBPXdJlC；- **model_size**：7B
- **Audio Flamingo Chat**：- **rank**：29；- **scope**：1000题test-mini；- **sound**：25.23；- **music**：17.66；- **speech**：6.91；- **model_link**：https://huggingface.co/nvidia/audio-flamingo；- **model_size**：1B

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）

#### 独立不确定性研究 / test-mini选项排列平均

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Qwen2.5-Omni-7B | 75.3 | accuracy / % |
| Audio Flamingo 3 | 74.6 | accuracy / % |

- **Qwen2.5-Omni-7B**：- **scope**：MMAU test-mini 1,000，选择题排列平均，Table1；- **date**：2026-09-24；- **provenance**：独立研究作者复测，非官方标准单次协议，未明确数据修订版本
- **Audio Flamingo 3**：- **scope**：MMAU test-mini 1,000，选择题排列平均，Table1；- **date**：2026-09-24；- **provenance**：独立研究作者复测，不是原论文或官方榜单分数

[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）


[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

### 覆盖范围与时效

已全量读取官方parsed JSON，按Test及Test-mini独立排序，不纳入另一个community/unverified文件。研究论文选项排列平均另轨。原始JSON没有提交时间字段，结果日期待核实，采集日不是测量日。

[来源](https://sakshi113.github.io/mmau_homepage/leaderboard_data_v15_parsed.json)（访问 2026-11-08）；[来源](https://arxiv.org/html/2609.28879v1)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

- ssakshi@umd.edu
- sonalkum@umd.edu
- sreyang@umd.edu

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）

### 公开反馈

https://github.com/Sakshi113/MMAU/issues

[来源](https://github.com/Sakshi113/MMAU)（访问 2026-11-07）

### 官方社交

待核实

> 已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://sakshi113.github.io/mmau_homepage/)（访问 2026-11-08）

### 隐私边界

仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2410.19168

[来源](https://arxiv.org/abs/2410.19168)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### PDF SHA-256

455dbfa3f7cb020120e3e0d0c624f707324e9596dd3b26b8c82e9b855580d41a

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### PDF字节数

8505593

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2410.19168)（访问 2026-11-08）

### 文件夹

- **id**：1jL7cEn2wJW2BUPvBczHAQ48-trhfAWPP
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍 Google Doc；- **id**：1HYU_qKEN39kM7XToCN4Gpo2r6HC8pMKxKK5rb51s0Ks；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：13ewKCqXHV0WhBIedBk0uzWbrNjp5CNdG
- **webViewLink**：

[来源]( 2026-11-07）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- - **date**：2026-11-07；- **timezone**：；- **round**：1 / 深度实证复核；- **change**：补机构、维护、英语问句与音频语言的区分、隐藏test协议；重读官方parsed榜单并重核H2。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/Sakshi113/MMAU/main/README.md)（访问 2026-11-08）
