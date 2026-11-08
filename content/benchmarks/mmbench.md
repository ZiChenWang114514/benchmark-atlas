# MMBench

> Benchmark Constitution · 深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MMBench以分层视觉能力而非单一任务组织图文选择题，核心协议是CircularEval：将候选项循环移位，所有轮次均答对才计成功。原README、论文和当前VLMEvalKit包含不同数量与命名版本；V11、EN/CN、dev/test及答案抽取器必须固定，单次准确率并非等价指标。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 简称

MMBench

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 全称

MMBench

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 基准版本

原版MMBench EN/CN及V11命名数据并存；官方VLMEvalKit明确提供DEV/TEST_EN/CN_V11四个配置，不与旧版混同。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py)（访问 2026-11-08）

### 论文版本

arXiv v5

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 发布日期

2023-07-13（；arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 主板块

多模态

> Benchmark Constitution编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 领域标签

- 通用图文能力

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 许可证与权利边界

Apache-2.0（官方仓库LICENSE）；不自动覆盖公共数据集和互联网原图等第三方权利。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/LICENSE)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2307.06281

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 代码仓库

https://github.com/open-compass/MMBench

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 数据集入口

- **repository_download_table**：https://github.com/open-compass/MMBench#dataset
- **current_vlmevalkit_config_source**：https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py
- **hf_mirror**：https://huggingface.co/datasets/opencompass/MMBench

> HF卡片内容极少；以项目下载表及官方工具定义为协议依据。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py)（访问 2026-11-08）；[来源](https://huggingface.co/datasets/opencompass/MMBench/raw/main/README.md)（访问 2026-11-08）

### 官方主页

https://mmbench.opencompass.org.cn/

[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）；[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 论文标题

MMBench: Is Your Multi-modal Model an All-around Player?

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

OpenCompass Community开发；论文作者单位包括上海人工智能实验室、南洋理工大学、香港中文大学、新加坡国立大学、浙江大学。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 合作方

待核实

> 本批尚未完成此字段的精确核验；不等于官方未公开。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 作者

- Liu, Yuan
- Duan, Haodong
- Zhang, Yuanhan
- Li, Bo
- Zhang, Songyang
- Zhao, Wangbo
- Yuan, Yike
- Wang, Jiaqi
- He, Conghui
- Liu, Ziwei
- Chen, Kai
- Lin, Dahua

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）

### 维护方

open-compass 官方仓库团队（当前具体个人职责待核实）

[来源](https://github.com/open-compass/MMBench)（访问 2026-11-07）

### 资助

待核实

> 本批尚未完成此字段的精确核验；不等于官方未公开。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

## 设计目标

### 衡量能力

细粒度图文感知与推理，按分层能力体系给出诊断。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 设计背景

VQAv2、图像描述等任务不充分反映细粒度能力，纯字符串匹配难兼容自由回答，人工主观打分难扩展。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

## 构建方式

### 题目来源

从公开数据集及互联网搜集图文题，组织为三层能力体系，20项细粒度能力；每题单一正确选项。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 出题与审阅者背景

研究团队负责能力体系、数据筛选和质量控制；标注员具体招募背景待核实。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 审核流程

论文附录B：先用GPT-4、Gemini-Pro、Qwen-Max做text-only CircularEval，能脱离图片答对的题送人工核验；再用五个VLM筛出全答错题，人工检查歧义、重复选项与错误标签。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 质量控制

原论文按三层20能力组织题目，附录B分别处理text-only捷径题和可能的错题；中文翻译再由人工核验。这不是对所有源图像授权或训练污染的保证。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 去污染及其证据边界

待核实

> 本批尚未完成此字段的精确核验；不等于官方未公开。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

2024年论文v5为3,217题；仓库README正文仍为2,974题，下载表dev 1,164及test 1,784，两者也不相加为2,974。保留各口径，不推测统一题量。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 题型

图像+问题+选项的单选题。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 模态

图像+文本

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 语言

中文与英文

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 难度

以三层细粒度能力分类而非统一学业等级定难度；CircularEval要求每次选项轮换都答对，官方README指出较单次评测更难。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 公开与隐藏划分

下载表EN/CN各有dev 1,164及test 1,784题；VLMEvalKit格式仅保留一份图片，Legacy为N选项CircularEval保留N份，正文内容相同；不能据图片副本数推题量。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

CircularEval准确率：N个选项循环移位N次，全部答对才算该题成功；与单次准确率分开。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 评分方法

先用规则提取选项，失败后用ChatGPT匹配答案，最多尝试3次；CircularEval循环移位全部选项，N次全部正确才判该原题成功。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 运行与提示设置

官方VLMEvalKit构建含图像、hint、问题、候选答案及选项指令的提示；保留EN/CN和CircularEval次数。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 官方脚本

https://github.com/open-compass/VLMEvalKit

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 可比性警示

README、论文及下载表题量冲突；EN/CN、dev/test、旧版/新文件和单次/CircularEval不能混比。MMVistaReason采用CompassVerifier，不能默认为官方CircularEval等价。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

当前VLMEvalKit可见V11（EN/CN dev/test），而原项目README仍列旧下载表。复现应记录确切配置名与文件校验值，不根据README题量猜版本。

[来源](https://raw.githubusercontent.com/open-compass/VLMEvalKit/main/vlmeval/dataset/image_mcq.py)（访问 2026-11-08）

### 论文修订及历史证据

- **revisions**：- - **version**：v1；- **submitted_at**：2023-07-13；- **timezone**：；- - **version**：v2；- **submitted_at**：2023-07-27；- **timezone**：；- - **version**：v3；- **submitted_at**：2023-08-13；- **timezone**：；- - **version**：v4；- **submitted_at**：2024-04-30；- **timezone**：；- - **version**：v5；- **submitted_at**：2024-08-20；- **timezone**：
- **continued_use_2026h2**：- - **url**：https://arxiv.org/html/2610.01352v2；- **date**：2026-10-22；- **note**：MMVistaReason v2 §4.1及表2实际评测 MMBench（EN设置），比较4B/9B及其他视觉语言模型；不把mini/val等划分另计。
- **verification**：已打开并复核证据原文的实际评测章节及表格，不只按参考文献或网页存活判断。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### 饱和情况

待核实

> 本批尚未完成此字段的精确核验；不等于官方未公开。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 污染、争议与限制

README、论文及下载表题量冲突；EN/CN、dev/test、旧版/新文件和单次/CircularEval不能混比。MMVistaReason采用CompassVerifier，不能默认为官方CircularEval等价。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### 衍生与版本关系

仓库另列CCBench：中文文化相关，dev 510题；2023-12-26公告删除噪声样本并更新榜单。CCBench不是MMBench EN/CN同一划分。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（；采集日，不冒充评测运行日）

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 官方入口

https://mmbench.opencompass.org.cn/leaderboard

> 本次抓取页面无可读榜单行；当前官方排名待核实，不改用研究论文伪装官方排名。

[来源](https://mmbench.opencompass.org.cn/leaderboard)（访问 2026-11-08）

### 第三方覆盖入口

待核实

> 本次打开AA评测目录，未确认该原始基准的独立追踪页。AA追踪MMMU-Pro不等于追踪MMMU原版；不拿LMArena偏好Elo或其他基准分数替代。Epoch/LMArena的同口径结果仍待逐项核实。

[来源](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07）

### 分来源与协议的精确成绩

#### 原论文v5表3 / EN test / CircularEval

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| InternLM-XComposer2* | 78.1 | CircularEval Top-1 accuracy / % |
| Qwen-VL-Max | 75.4 | CircularEval Top-1 accuracy / % |
| GPT-4v | 74.3 | CircularEval Top-1 accuracy / % |

- **InternLM-XComposer2***：- **scope**：历史论文榜，非当前官方网页动态榜
- **Qwen-VL-Max**：- **scope**：历史论文榜，非当前官方网页动态榜
- **GPT-4v**：- **scope**：历史论文榜，非当前官方网页动态榜

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

#### MMVistaReason作者论文 / EN / CompassVerifier

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| MMVistaReason-4B (MVR-4B) | 90.6 | 论文协议答案正确率（CompassVerifier） / % |
| MMVistaReason-9B (MVR-9B) | 92.2 | 论文协议答案正确率（CompassVerifier） / % |

- **MMVistaReason-4B (MVR-4B)**：- **scope**：MMBench-EN，论文未精确列出下载版本；- **date**：2026-10-22；- **provenance**：MMVistaReason作者自报表2；VLMEvalKit，T=0，max16384；§7.3用CompassVerifier替代传统字符串匹配，不是官方榜单/AA独立评测
- **MMVistaReason-9B (MVR-9B)**：- **scope**：MMBench-EN，论文未精确列出下载版本；- **date**：2026-10-22；- **provenance**：MMVistaReason作者自报表2；同上协议，不与其他榜单无条件混排

[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）


[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

### 覆盖范围与时效

官方leaderboard URL只返回前端应用壳，未取得动态分数，不能声称已刷新到其最新排名。补列原论文v5表3历史test成绩，并把2026研究CompassVerifier结果另轨；不同数据版、CN/EN、dev/test与评分器不得混排。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/html/2610.01352v2)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

待核实

> 本批尚未完成此字段的精确核验；不等于官方未公开。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 公开反馈

https://github.com/open-compass/MMBench/issues

[来源](https://github.com/open-compass/MMBench)（访问 2026-11-07）

### 官方社交

待核实

> 本批尚未完成此字段的精确核验；不等于官方未公开。

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://mmbench.opencompass.org.cn/)（访问 2026-11-08）

### 隐私边界

仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。

[来源](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2307.06281

[来源](https://arxiv.org/abs/2307.06281)（访问 2026-11-08）；[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### PDF SHA-256

3cd9025569600c548d29a987e1cef6bdac8dc07cdeb6bd49ef04690ae80ebd6b

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### PDF字节数

7311810

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2307.06281)（访问 2026-11-08）

### 文件夹

- **id**：1hUK_CiomC6c_SEKT-IHjmirQgcqKi7zE
- **webViewLink**：

[来源]( 2026-11-07）

### 其他官方材料

- - **kind**：中文介绍 Google Doc；- **id**：1S2YN9vaLoj9773TV08Q-a8KkpqeX-2HbMeZD-IfNBwE；- **webViewLink**：

[来源]( 2026-11-07）

### PDF归档

- **id**：14aYn-VWxa5JFb6QErhPEv6GdN6NTyMai
- **webViewLink**：

[来源]( 2026-11-07）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。
- - **date**：2026-11-07；- **timezone**：；- **change**：深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/open-compass/MMBench/main/README.md)（访问 2026-11-08）
