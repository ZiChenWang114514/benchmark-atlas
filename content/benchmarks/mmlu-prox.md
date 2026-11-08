# MMLU-ProX

> Benchmark Constitution · 深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MMLU-ProX在MMLU-Pro基础上提供29种语言的平行难题。Full的11,829及Lite的658都包含70条validation；实际test分别是11,759和588。翻译质量检查覆盖15种语言的固定抽样，而非所有29语每一道题都人工审校；跨语言差异仍可能混合语言能力、译文与文化因素。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

### 简称

MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 全称

MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 基准版本

MMLU-ProX：29语言全量版及Lite版；2025-05官方发布记录。

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 论文版本

arXiv v2

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 发布日期

2025-03-14（；arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 主板块

语言

> Benchmark Constitution编辑归档，不是论文指定的唯一领域。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 领域标签

- 多语言高难知识

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 许可证与权利边界

MIT（官方数据集卡声明）

[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX)（访问 2026-11-07）

### 论文入口

https://arxiv.org/abs/2503.10497

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 代码仓库

https://github.com/weihao1115/MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 数据集入口

https://huggingface.co/datasets/li-lab/MMLU-ProX

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 官方主页

https://mmluprox.github.io/

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 论文标题

MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

论文作者来自 University of Tokyo、Duke-NUS、Waseda 等多所机构；不把作者单位等同于正式合作协议。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 合作方

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 作者

- Xuan, Weihao
- Yang, Rui
- Qi, Heli
- Zeng, Qingcheng
- Xiao, Yunze
- Feng, Aosong
- Liu, Dairui
- Xing, Yun
- Wang, Junjue
- Gao, Fan
- Lu, Jinghui
- Jiang, Yuang
- Li, Huitao
- Li, Xin
- Yu, Kunyu
- Dong, Ruihai
- Gu, Shangding
- Li, Yuekang
- Xie, Xiaofei
- Juefei-Xu, Felix
- Khomh, Foutse
- Yoshie, Osamu
- Chen, Qingyu
- Teodoro, Douglas
- Liu, Nan
- Goebel, Randy
- Ma, Lei
- Marrese-Taylor, Edison
- Lu, Shijian
- Iwasawa, Yusuke
- Matsuo, Yutaka
- Li, Irene

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 维护方

官方公开代码托管于 weihao1115；此处记录仓库维护入口，不据此推断机构法律责任或持续维护承诺。

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 资助

官网致谢列出 JSPS KAKENHI 24K20832、JST ActX JPMJAX24CU、NVIDIA Academic Grant、Google Gemma Academic Program。

[来源](https://mmluprox.github.io/)（访问 2026-11-08）

## 设计目标

### 衡量能力

在相同难题上直接比较多语言知识与推理能力。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 设计背景

英语评测主导，现有多语题集常缺少相互平行、保持推理难度的题目。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## 构建方式

### 题目来源

以 MMLU-Pro 英语题为基础，采用多个 LLM 翻译后由专家审阅。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 出题与审阅者背景

英语清理由4名跨学科人员完成；翻译质检选择15种语言，每语种2名以该语种为母语且懂英语的专业译者，并非29语所有题逐题专家复核。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### 审核流程

Claude Sonnet3.7执行初译、自反思与改进；o3核查低资源非洲语言，GPT-4.1核查其余。人工每科抽20题，14科相同样本在15语检查准确性、流畅性、完整性。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### 质量控制

先删除或合并MMLU-Pro重复/部分重复题并修正语法符号；人工双译者以1–5分评审15语样本，某科任一指标双方均低于3则整科重译；论文记录Yoruba法律触发该规则。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### 去污染及其证据边界

论文§3.2处理题库内部重复/部分重复问题；这是去重而非对受测模型训练集的去污染。模型级训练污染审计仍待核实。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

29种语言；Full每语言11,829条=validation70+test11,759；Lite每语言658条=validation70+test588。总规模与实际测试题数不能互换。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

### 题型

多项选择知识/推理题

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 模态

文本

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 语言

29种语言（官方README当前描述；不是只统计非英语翻译）

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 难度

继承 MMLU-Pro 的推理导向；高低资源语言之间的分差不是单纯题目难度差。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 公开与隐藏划分

Full与Lite都公开validation/test及标准答案；Full test11,759，Lite test588，每种语言validation70用于演示。不同规模独立评测。

[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

各语言选择题准确率及跨语言平均。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 评分方法

提取最终选项并与标准答案比对，逐语言报告。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 运行与提示设置

通过 lm-evaluation-harness 的 mmlu_prox_<lang> 任务评测；README复现要求 vLLM 0.7.3，Llama3.1-405B例外使用0.6.6。

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 官方脚本

https://github.com/weihao1115/MMLU-ProX

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 可比性警示

full/lite、语言集合及 CoT 策略不同不能混比；官网模型名称未给 API 日期时不得自行补全。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/weihao1115/MMLU-ProX/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

README 2025-05记录29语言、Full与Lite；2025-08称正在开发更多语言的第二版，不把计划等同已发布。

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2025-03-14；- **timezone**：；- - **version**：v2；- **submitted_at**：2025-05-27；- **timezone**：

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 饱和情况

官网5-shot CoT静态表中DeepSeek-R1跨29语平均75.5%；这只是已列模型和协议的历史表现，不是当前全球最高分或统一饱和判据。

[来源](https://mmluprox.github.io/)（访问 2026-11-08）

### 污染、争议与限制

论文限制指出专家验证仅覆盖15种语言的抽样；译文偏差和文化差异仍可能影响分数。Full/Lite总数含70条validation，测试分别只有11,759/588，不能把总数写成测试题量。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX/raw/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

### 衍生与版本关系

MMLU-ProX-Lite是同项目节省评测成本的子集版，不另算一个独立benchmark；README仅公告第二版更多语言正在开发，不视为已发布。

[来源](https://raw.githubusercontent.com/weihao1115/MMLU-ProX/main/README.md)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/li-lab/MMLU-ProX-Lite/raw/main/README.md)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（；采集日，不冒充评测运行日）

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### 官方入口

https://mmluprox.github.io/

[来源](https://mmluprox.github.io/)（访问 2026-11-08）

### 第三方覆盖入口

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### 官方论文v2表6 / Full / 5-shot CoT

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| DeepSeek-R1 | 75.5 | 29-language average accuracy / % |
| Qwen3-235B-Think | 74.9 | 29-language average accuracy / % |
| GPT-4.1 | 72.7 | 29-language average accuracy / % |

- **DeepSeek-R1**：- **scope**：每语种test11,759；不含70 validation
- **Qwen3-235B-Think**：- **scope**：每语种test11,759；不含70 validation
- **GPT-4.1**：- **scope**：每语种test11,759；不含70 validation

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

#### 官方主页静态结果 / 5-shot CoT

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Qwen3-235B-Think | 74.9 | 29-language average accuracy / % |
| DeepSeek-R1 | 75.5 | 29-language average accuracy / % |
| GPT-4.1 | 72.7 | 29-language average accuracy / % |
| DeepSeek-V3 | 70.5 | 29-language average accuracy / % |
| o4-mini | 69.3 | 29-language average accuracy / % |
| Qwen3-235B | 66.7 | 29-language average accuracy / % |
| Qwen3-32B-Think | 66.3 | 29-language average accuracy / % |
| Qwen3-14B-Think | 65.4 | 29-language average accuracy / % |

- **Qwen3-235B-Think**：- **language_scores**：- **EN**：80.7；- **FR**：80.6；- **DE**：80.4；- **ES**：80.7；- **PT**：80.5；- **IT**：80.9；- **HI**：78.7；- **BN**：77.8；- **UR**：76.1；- **TE**：77.9；- **MR**：78.5；- **NE**：78.1；- **ZH**：77.4；- **JA**：77.1；- **KO**：78.3；- **VI**：72.6；- **TH**：77.1；- **ID**：79.9；- **AR**：78.7；- **AF**：80.6；- **SW**：70.8；- **WO**：36.9；- **YO**：49.3；- **ZU**：46.4；- **RU**：77.0；- **UK**：78.8；- **SR**：80.2；- **CS**：80.5；- **HU**：79.8；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **DeepSeek-R1**：- **language_scores**：- **EN**：79.5；- **FR**：81.3；- **DE**：76.7；- **ES**：80.2；- **PT**：78.0；- **IT**：79.9；- **HI**：77.5；- **BN**：66.6；- **UR**：76.2；- **TE**：71.9；- **MR**：70.4；- **NE**：78.9；- **ZH**：78.0；- **JA**：76.9；- **KO**：76.7；- **VI**：76.3；- **TH**：78.7；- **ID**：81.3；- **AR**：76.2；- **AF**：80.9；- **SW**：75.0；- **WO**：58.6；- **YO**：57.0；- **ZU**：67.3；- **RU**：76.4；- **UK**：76.8；- **SR**：80.9；- **CS**：76.8；- **HU**：79.1；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **GPT-4.1**：- **language_scores**：- **EN**：79.8；- **FR**：75.7；- **DE**：76.4；- **ES**：77.8；- **PT**：77.0；- **IT**：78.2；- **HI**：74.5；- **BN**：72.2；- **UR**：68.3；- **TE**：65.9；- **MR**：72.2；- **NE**：74.2；- **ZH**：75.5；- **JA**：75.6；- **KO**：75.4；- **VI**：76.7；- **TH**：75.1；- **ID**：75.6；- **AR**：74.1；- **AF**：77.2；- **SW**：71.9；- **WO**：43.2；- **YO**：53.4；- **ZU**：65.0；- **RU**：71.2；- **UK**：76.4；- **SR**：76.9；- **CS**：77.5；- **HU**：76.6；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **DeepSeek-V3**：- **language_scores**：- **EN**：79.6；- **FR**：76.3；- **DE**：75.1；- **ES**：76.9；- **PT**：75.7；- **IT**：75.9；- **HI**：71.6；- **BN**：69.8；- **UR**：70.3；- **TE**：67.6；- **MR**：69.8；- **NE**：69.3；- **ZH**：73.9；- **JA**：72.9；- **KO**：70.7；- **VI**：75.4；- **TH**：71.2；- **ID**：75.8；- **AR**：72.4；- **AF**：72.9；- **SW**：63.4；- **WO**：47.3；- **YO**：47.7；- **ZU**：53.7；- **RU**：74.9；- **UK**：74.2；- **SR**：72.9；- **CS**：74.7；- **HU**：71.4；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **o4-mini**：- **language_scores**：- **EN**：73.7；- **FR**：72.2；- **DE**：73.5；- **ES**：74.7；- **PT**：74.1；- **IT**：73.9；- **HI**：71.8；- **BN**：70.1；- **UR**：72.0；- **TE**：69.1；- **MR**：70.7；- **NE**：71.5；- **ZH**：72.6；- **JA**：71.5；- **KO**：73.2；- **VI**：73.4；- **TH**：72.0；- **ID**：73.8；- **AR**：72.5；- **AF**：73.5；- **SW**：66.9；- **WO**：24.1；- **YO**：54.9；- **ZU**：61.2；- **RU**：62.0；- **UK**：73.3；- **SR**：72.6；- **CS**：73.5；- **HU**：72.6；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **Qwen3-235B**：- **language_scores**：- **EN**：73.5；- **FR**：72.5；- **DE**：71.3；- **ES**：73.2；- **PT**：73.1；- **IT**：73.7；- **HI**：67.6；- **BN**：67.7；- **UR**：68.7；- **TE**：66.7；- **MR**：67.7；- **NE**：67.8；- **ZH**：70.5；- **JA**：68.8；- **KO**：69.6；- **VI**：71.4；- **TH**：68.8；- **ID**：72.5；- **AR**：70.1；- **AF**：71.1；- **SW**：56.3；- **WO**：26.6；- **YO**：40.2；- **ZU**：46.2；- **RU**：72.9；- **UK**：72.5；- **SR**：71.1；- **CS**：71.8；- **HU**：70.1；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **Qwen3-32B-Think**：- **language_scores**：- **EN**：74.9；- **FR**：72.1；- **DE**：71.7；- **ES**：72.8；- **PT**：72.7；- **IT**：73.5；- **HI**：70.4；- **BN**：66.4；- **UR**：70.8；- **TE**：70.3；- **MR**：70.7；- **NE**：70.7；- **ZH**：68.7；- **JA**：70.2；- **KO**：71.2；- **VI**：72.4；- **TH**：70.4；- **ID**：73.4；- **AR**：70.4；- **AF**：72.4；- **SW**：56.7；- **WO**：26.6；- **YO**：18.8；- **ZU**：35.2；- **RU**：69.1；- **UK**：73.5；- **SR**：72.3；- **CS**：72.8；- **HU**：71.1；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜
- **Qwen3-14B-Think**：- **language_scores**：- **EN**：74.7；- **FR**：72.2；- **DE**：71.4；- **ES**：72.2；- **PT**：71.6；- **IT**：73.0；- **HI**：67.9；- **BN**：66.8；- **UR**：68.0；- **TE**：64.6；- **MR**：66.9；- **NE**：67.3；- **ZH**：66.5；- **JA**：70.8；- **KO**：70.0；- **VI**：71.4；- **TH**：69.8；- **ID**：72.3；- **AR**：69.1；- **AF**：71.3；- **SW**：48.0；- **WO**：28.3；- **YO**：32.5；- **ZU**：32.3；- **RU**：72.2；- **UK**：71.3；- **SR**：71.6；- **CS**：71.1；- **HU**：69.8；- **scope**：官网静态Performance Results；独立Leaderboard Coming Soon，不冒称实时榜

[来源](https://mmluprox.github.io/)（访问 2026-11-08）


[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://mmluprox.github.io/)（访问 2026-11-08）

### 覆盖范围与时效

论文v2表6与官网静态表分轨、数值相同也不合并成两次独立复测。页面没有精确运行日，结果日期待核实；不把2026采集日当作2026新实验。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）；[来源](https://mmluprox.github.io/)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

- irene.li@weblab.t.u-tokyo.ac.jp
- weihaoxuan@g.ecc.u-tokyo.ac.jp

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 公开反馈

https://github.com/weihao1115/MMLU-ProX/issues

[来源](https://github.com/weihao1115/MMLU-ProX)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源](https://arxiv.org/abs/2503.10497)（访问 2026-11-08）

### 隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2503.10497

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### PDF SHA-256

b171ff829bfbb567974812dfebb860a63df7f756daf5662c7a1b659df76833bd

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### PDF字节数

730780

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2503.10497)（访问 2026-11-08）

### 文件夹

- **id**：1lkm8WYv2rby8F0gpXf1ZMevpAmGW0vk9
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍 Google Doc；- **id**：1iI9qctXi6aYW-mS7lXH46jm9PSI0fUQlkF3-W6KeXBE；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：1gohaRGvTuT_OgM7cpG7rgGG4oAjWNDuR
- **webViewLink**：

[来源]( 2026-11-07）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/weihao1115/MMLU-ProX/main/README.md)（访问 2026-11-08）
