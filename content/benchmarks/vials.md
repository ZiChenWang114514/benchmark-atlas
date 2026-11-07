# VIALS

> 本页中文整理与本轮复核：2026-11-08（KST / Asia/Seoul）。历史结果、不同数据版本、scaffold与评分协议分别记录；待核实不等于未公开。

VIALS面向生命科学日常实验产物的视觉解读，而非教科书中整理完好的图表。161题的官方直接视觉accuracy与AA带代码工具的pass^3测量不同能力；数据2.0.0修了三题，论文1.0.0结果不应自动改标签。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-08，KST）；[3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）

## 基本信息

### 简称

VIALS

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 全称

Visual Interpretation of Artifacts in the Life Sciences

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 基准版本

2.0.0

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 论文版本

arXiv v2；提交于 2026-09-20 00:59:27 KST

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 发布日期

数据v1.0.0 tag发布2026-09-15；v2.0.0发布2026-10-30（数据卡CHANGELOG标示日，未给时区）；arXiv v1另为2026-08-22 02:59:26 KST，不混为数据上线日。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）；[2](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 主板块

多模态

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 领域标签

- 科学图像
- 物理
- 化学
- 生物与医学
- 材料

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 许可与适用范围

数据及图像CC BY 4.0（逐图引用attributions.csv原始来源）；评测代码另为MIT。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 论文

https://arxiv.org/abs/2608.21357

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 代码仓库

https://github.com/Handshake-AI-Research/VIALS

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 数据地址

https://huggingface.co/datasets/Handshake-AI-Research/VIALS

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 官方主页

https://joinhandshake.com/research/benchmarks/vials/

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 论文标题

VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

## 发起与维护

### 机构与发起关系

Handshake AI

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 合作机构

待核实

说明：已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 作者

- Elaine Lau
- Thanuka Udumulla
- Lee Izhaki-Tavor
- Francisco Guzmán
- Nicholas Magazine
- Jonas Mueller

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 当前维护方

Handshake AI

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 资助与支持

待核实

说明：已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

## 设计目标

### 衡量能力

解释生命科学专业流程中的凝胶、流式图、质粒图、系统发育树与分子结构等真实视觉证据。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 设计背景

强调日常科研视觉产物而非教材考试图或只描述自然图片，检验视觉定位及领域解释。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

## 构建方式

### 题目或数据来源

未发表实验数据、科学软件生成产物、CC-BY开放论文图；专家依自身工作编写问题与参考答案。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 出题背景

31名专业贡献者，87%具博士级训练，74%有超过6年生命科学行业经验。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 审核流程

第二位、经常第三位领域专家盲答；独立答案一致或复审达共识方保留。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 质量控制

检查图像现实性、可答性、任务多样性；GPT-5-mini裁判与4685个人工标注答复的一致率为99.9%（作者自报）。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 去污染与泄漏

构建时检查任务未在线出现；数据卡要求不入训练语料；未来额外任务私有开发，不当作本版题量。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

## 数据形式

### 规模

161任务；HF test分片parquet。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 题型

一个或多个图像加问题，开放式短答案，含可接受数值范围。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 模态

- 科学图像
- 文本问题
- 短文本答案

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 语言

- 英语

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/README.md)（访问 2026-11-08，KST）

### 难度

面向受过相关训练的专业科学家日常任务；不等于全科研流程难度。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

### 数据划分

当前161题公开；模型输入只能用images与question，answer及数值区间仅供评分。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07，KST）

## 评测方法

### 指标

官方直接视觉评测为三次独立rollout平均accuracy；AA Agent实现headline为pass^3。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 评分方式

官方抽取最终ANSWER:后答案，用GPT-5-mini判科学语义等价；标签歧义时带图复核。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 提示与运行设置

论文直接VLM设temperature 1.0、32768完成token、每题3次；AA用Stirrup代码/看图工具、无网络，GPT-6 Luna medium裁判。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 评测脚本

Handshake-AI-Research/VIALS；数据卡明确代码MIT。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 可比性提醒

直接视觉、官方工具辅助与AA工具辅助须分开；AA pass^3不等于官网平均accuracy，不能凭较高分说同协议性能提升。

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

## 最新情况

### 核验日期

2026-11-08 KST / Asia/Seoul

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）

### 数据版本与更新

2.0.0，2026-10-30发布；额外专家审阅后更改3个任务：2处prompt、一处参考答案、一张图像，必须重跑受影响任务。论文结果用1.0.0，不能静默升级成绩。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）；[2](https://github.com/Handshake-AI-Research/VIALS)（访问 2026-11-08，KST）

### 论文修订记录

- {"version": "v1", "submitted_at": "2026-08-22 02:59:26 KST", "timezone": "Asia/Seoul"}
- {"version": "v2", "submitted_at": "2026-09-20 00:59:27 KST", "timezone": "Asia/Seoul"}

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-08，KST）

### 饱和证据与局限

官网直接视觉平均accuracy最高49.9%；AA工具辅助headline pass^3最高64%。工具和裁判不同，不可视为同协议从49.9升64%，更不能推断专业视觉任务已饱和。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-08，KST）

### 争议与已知问题

2.0.0修正三题，要求重跑；数据卡domain文字称九类，论文及AA按八类，本页保留来源冲突。论文对4685答复99.9%裁判一致率是v1.0.0自报，不外推为每个新版本绝对正确。

来源：[1](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）；[2](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/README.md)（访问 2026-11-08，KST）；[3](https://arxiv.org/pdf/2608.21357)（访问 2026-11-08，KST）；[4](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-08，KST）

### 衍生或后继基准

与现有100条slug核对未发现同名旧版；不将评测实现或分项重复计为新benchmark。

说明：编辑去重结论；版本关系以下述专门说明为准。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

## 榜单快照

### 快照访问日期

2026-11-08 KST / Asia/Seoul

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-08，KST）；[3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）

### 官方榜单入口

https://joinhandshake.com/research/benchmarks/vials/

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 第三方入口

https://artificialanalysis.ai/evaluations/vials-aa

来源：[1](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-07，KST）

### 可核验结果

| 分轨 | 轨内名次 | 模型/系统 | 分数 | 指标 | 版本/设置 | 来源 |
|---|---:|---|---:|---|---|---|
| Handshake官网 / 直接视觉 | 1 | GPT-6 Astra | 49.9 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 2 | GPT-6.1 Sol | 49.1 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 3 | Gemini 4 Argon | 47.2 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 4 | Claude Sonnet 5.5 | 41.0 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 5 | Claude Opus 5.5 | 40.2 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 6 | Muse Wonder | 31.5 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 7 | Gemini 3.8 Flash | 29.4 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 8 | GPT-5.6 Sol | 26.5 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 9 | Claude Opus 5 | 24.4 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 10 | Muse Spark 1.2 | 22.6 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 11 | Kimi K3 | 20.9 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 12 | Grok 4.7 | 18.2 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 13 | DeepSeek V4.1 Flash | 12.6 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Handshake官网 / 直接视觉 | 14 | MiniMax-M3 | 10.8 | average accuracy (%) | 官网当前榜；README称最新版本榜，网页未逐行标revision；官方直接视觉评测；非AA pass^3 | [来源页未列运行日](https://joinhandshake.com/research/benchmarks/vials/)；采集2026-11-08 KST / Asia/Seoul |
| Artificial Analysis / 工具辅助 | 1 | Gemini 4 Carbon (High) | 64 | pass^3 (%) | 161 tasks；AA当前实现；Stirrup；Python+看图；无网络；3独立重复；GPT-6 Luna medium裁判 | [待核实（网页未标结果运行或全榜更新时间）](https://artificialanalysis.ai/evaluations/vials-aa)；采集2026-11-08 KST / Asia/Seoul |
| Artificial Analysis / 工具辅助 | 2 | GPT-6 Astra (Max) | 63 | pass^3 (%) | 161 tasks；AA当前实现；Stirrup；Python+看图；无网络；3独立重复；GPT-6 Luna medium裁判 | [待核实（网页未标结果运行或全榜更新时间）](https://artificialanalysis.ai/evaluations/vials-aa)；采集2026-11-08 KST / Asia/Seoul |
| Artificial Analysis / 工具辅助 | 3 | Claude Opus 5.5 (Max, Default Fallback) | 61 | pass^3 (%) | 161 tasks；AA当前实现；Stirrup；Python+看图；无网络；3独立重复；GPT-6 Luna medium裁判 | [待核实（网页未标结果运行或全榜更新时间）](https://artificialanalysis.ai/evaluations/vials-aa)；采集2026-11-08 KST / Asia/Seoul |

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-08，KST）；[3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）

### 榜单覆盖边界

官网14条直接视觉平均accuracy和AA明确列出的前三条pass^3分轨；官网未逐行提供数据revision，不能默认所有旧分数已完成v2重跑。论文v1.0.0、数据v2.0.0和AA独立工具实现分别标明。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）；[2](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-08，KST）；[3](https://huggingface.co/datasets/Handshake-AI-Research/VIALS/raw/main/CHANGELOG.md)（访问 2026-11-08，KST）

## 联系方式

### 官方公开邮箱

- elaine.lau@joinhandshake.com
- nicholas.magazine@joinhandshake.com
- jonas.mueller@joinhandshake.com

来源：[1](https://arxiv.org/abs/2608.21357)（访问 2026-11-07，KST）

### 公开反馈渠道

https://github.com/Handshake-AI-Research/VIALS/issues

来源：[1](https://github.com/Handshake-AI-Research/VIALS)（访问 2026-11-08，KST）

### 官方社交账号

待核实

说明：已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 联系方式/隐私原则

待核实

说明：已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2608.21357

来源：[1](https://arxiv.org/pdf/2608.21357)（访问 2026-11-08，KST）

### PDF SHA-256

5d5756cb7d10aa1859a3b8bcbc1155384025a69fbd10efbaaec0e0e80f973f83

来源：[1](https://arxiv.org/pdf/2608.21357)（访问 2026-11-08，KST）

### PDF字节数

```json
8757144
```

来源：[1](https://arxiv.org/pdf/2608.21357)（访问 2026-11-08，KST）

### Drive文件夹

待核实

说明：已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### 其他文档

- {"type": "官方介绍/协议", "url": "https://joinhandshake.com/research/benchmarks/vials/"}

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

### Drive论文原件

待核实

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07，KST）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传Drive。"}
- {"date": "2026-11-08", "timezone": "Asia/Seoul", "change": "第2轮逐源深核：补数据首发9月15日和v2十月30日，三题修正需重跑，论文结果实际v1。；恢复官网14个直接视觉分数，与AA3个工具pass^3分轨；补英语与Issue渠道及PDF哈希。"}

来源：[1](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-08，KST）
