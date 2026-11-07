# GDP.pdf

> Benchmark Constitution｜深度核验：2026-11-07（KST / Asia/Seoul）。访问日沿本轮固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

这套基准要求从专业PDF本身找对证据，再用正确的领域解释回答问题；抽取文本正确并不足够。主榜要求每项rubric全部通过，不能把部分评分与严格任务成功率互换。

编辑状态：已核验存在；研究快照；note: trending: A；未核实字段保留标记

## 基本信息

**简称**：GDP.pdf

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**全称**：GDP.pdf

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**基准版本**：100题公开版

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**论文版本**：arXiv v3（2026-07-15）

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**发布日期**：2026-04-14（论文§5.1自述基准发布日期；7月论文不是首发日）

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**主板块**：语言

核验说明：编辑归档，不代表官方分类。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**领域标签**：长上下文；多模态；专业文档

核验说明：编辑归档，不代表官方分类。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**许可证与授权边界**：Apache-2.0（论文Table 2所述公开基准）；第三方PDF保留原始权利。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**论文或技术报告**：https://arxiv.org/abs/2607.11192

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**官方代码**：https://github.com/surge-ai/gdp-pdf

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**数据地址**：https://huggingface.co/datasets/surgeai/GDP.pdf

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**官方主页**：https://surgehq.ai/benchmarks/gdp-pdf

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**论文题名**：GDP.pdf: Benchmarking Grounded Multimodal Reasoning over Professional PDF Documents

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 发起与维护

**发起方**：Surge AI

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**协作与机构边界**：待核实

状态：待核实。

核验说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**作者**：Suhaas Garre、Emily Ritchie、Sushant Mehta、Edwin Chen

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**维护方**：Surge AI

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 设计目标

**测量能力**：围绕原始专业PDF完成有证据依据的真实工作问答，同时检验视觉解析、领域语义、跨页引用与无证据时的拒答。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**相对既有评测的缺口**：OCR、单表格问答和学科视觉题分别达标，不代表能正确解释实际合同、福利文件、建筑图纸或临床文档。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 构建方式

**题目来源**：十个专业领域的从业者提交实际工作问题及原PDF；仅保留至少两个前沿模型产生实质错误的候选，排除仅靠常识能答或语义含混的题。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**出题与研究背景**：任务由十类专业领域的在职从业者按日常工作提出；论文作者为Surge AI的Suhaas Garre、Emily Ritchie、Sushant Mehta、Edwin Chen，不把论文作者与全部出题专家混为一谈。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**审核流程**：专家编写参考答案、原子rubric和能力标签；参考答案须通过自己的rubric，故意错误答案须被对应标准拦截；论文的错误分析另行人工核对原文。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**质量控制**：专家编写参考答案、原子rubric和能力标签；参考答案须通过自己的rubric，故意错误答案须被对应标准拦截；论文的错误分析另行人工核对原文。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**去污染与泄漏边界**：论文采用多模型失败筛选与必须依据原PDF的题目要求；这控制题目难度/依证性，不证明训练去污染。原PDF来自现实工作且题目已发布，预训练暴露状况待核实。

状态：待核实。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 数据形式

**规模与口径**：100题，十领域均衡分布；AA方法页记4,592页PDF和1,275项评分标准。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）；[2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

**任务类型**：检索、比较、核算、摘要、跨页协调及无支持信息时的拒答；开放回答。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**模态**：PDF原文；文本；图像；表格；图表

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**语言**：待核实

状态：待核实。

核验说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**难度**：每个保留样本都使至少两个前沿多模态模型犯实质错误；按11种能力轴、三级能力体系标注，不提供统一easy/medium/hard数量。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**公开与隐藏划分**：论文称100题及PDF、提示、rubric、标签全部公开；本次HF数据页返回401，公开性按论文陈述记录，不宣称已下载题库。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 评测方法

**指标**：严格任务通过率（全部rubric成立）与平均rubric得分；榜单采用严格通过率。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**评分方式**：每个标准独立二元评分，任务全部标准通过才计pass；原版以Gemini 3.5 Flash裁判。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**提示与运行设置**：原版每模型每题5次，无工具；原PDF通过供应商原生文件输入。AA改用OCR全文和页面图像，裁判GPT-5.6 Luna medium。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）；[2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）

**官方复现入口**：https://github.com/surge-ai/gdp-pdf；Inspect AI入口src/gdp_pdf/task.py，--epochs 5，Gemini 3.5 Flash judge；all_pass/mean为主榜，mean_criteria/mean保留部分分。

来源：[1](https://github.com/surge-ai/gdp-pdf)（访问2026-11-07）

**可比性警告**：AA与Surge共享题集但PDF输入和裁判不同；原生PDF与预解析OCR两套成绩不能直接互换。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07 KST / Asia/Seoul

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**数据及热度证据**：```json
{
  "version": "100题公开版",
  "trending": "A",
  "heat_evidence": "AA 2026-10-27 v5发布文继续以5%权重收录GDP.pdf，当前方法页明确100题×5次；Surge官方榜同时展示新模型。两机构是不同实现，不视为相同分数复核。",
  "evidence_2026_h2": [
    {
      "url": "https://surgehq.ai/benchmarks/gdp-pdf",
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
      "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）；[2](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[3](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)（访问2026-11-07）

**论文与版本历史**：arXiv v1：2026-07-13 16:44:07 KST；v2：07-14 16:57:18 KST；v3：07-15 16:47:22 KST。基准4月首发与7月论文发布应分开。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**饱和程度**：当前Surge严格通过率榜首35.0%，次席34.2%、第三33.2%；未达满分。不能由平均rubric高分推断严格任务通过率已经饱和。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**已知问题与局限**：AA与Surge共享题集但PDF输入和裁判不同；原生PDF与预解析OCR两套成绩不能直接互换。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**后续与衍生**：GDP.pdf不是GDPval，也不是GDP.xlsx：本条只记录专业PDF问答，不合并职业交付物或电子表格任务。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

## 榜单快照

**快照日期**：2026-11-07 KST / Asia/Seoul

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**官方入口**：https://surgehq.ai/benchmarks/gdp-pdf

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**第三方入口**：待核实

状态：待核实。

核验说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | GPT 6.1 Sol (Max reasoning) | 35 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 2 | GPT 6 Astra (Max reasoning) | 34.2 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 3 | Muse Wonder Full (Max reasoning) | 33.2 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 4 | Claude Sonnet 5.5 (Adaptive/Max) | 31.4 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 5 | Muse Wonder (Max reasoning) | 30.8 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 6 | GPT 5.6 Sol (Max reasoning) | 30.7 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 7 | Claude Opus 5.5 (Adaptive/Max) | 30.6 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |
| 当前官方网页榜 | 8 | Claude Fable 5 (Adaptive/Max) | 29.8 | Surge严格任务通过率 (%) | 待核实（榜表更新时间） | [原始来源](https://surgehq.ai/benchmarks/gdp-pdf) |

采集：2026-11-07（KST / Asia/Seoul）；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：AA与Surge共享题集但PDF输入和裁判不同；原生PDF与预解析OCR两套成绩不能直接互换。 榜表自写更新时间：待核实；采集日不等于运行日。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 联系方式

**公开联系邮箱**：suhaas@surgehq.ai

核验说明：论文明确公开的通讯地址，仅用于研究联系。

来源：[1](https://arxiv.org/abs/2607.11192)（访问2026-11-07）

**Issues或讨论入口**：https://github.com/surge-ai/gdp-pdf/issues

来源：[1](https://github.com/surge-ai/gdp-pdf)（访问2026-11-07）

**官方社交**：https://x.com/HelloSurgeAI

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**隐私政策**：https://surgehq.ai/privacy-policy

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 原始文件

**原始PDF**：https://arxiv.org/pdf/2607.11192

核验说明：本轮直接读取原始PDF字节核验；未上传Drive。

来源：[1](https://arxiv.org/pdf/2607.11192)（访问2026-11-07）

**PDF SHA-256**：e139828de98e24caee6ba7f749dd39e9c541ff16c7a6c91ddb18dcd5a8defda4

核验说明：本轮下载原始PDF字节计算，非arXiv网页显示大小。

来源：[1](https://arxiv.org/pdf/2607.11192)（访问2026-11-07）

**PDF字节数**：```json
223397
```

核验说明：本轮实际下载字节数；不代表Drive已上传。

来源：[1](https://arxiv.org/pdf/2607.11192)（访问2026-11-07）

**Drive文件夹**：待核实

状态：待核实。

核验说明：本轮所列已打开材料未完成精确核验；不代表官方未公开。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**其他官方文档**：```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://surgehq.ai/benchmarks/gdp-pdf"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2607.11192"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5"
  }
]
```

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

**Drive论文链接**：待核实

状态：待核实。

核验说明：本组仅本地建页，未上传Drive，不伪造归档链接。

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

## 变更记录

**本轮及历史变更**：```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。GDP.pdf不是GDPval，也不是GDP.xlsx：本条只记录专业PDF问答，不合并职业交付物或电子表格任务。 热度与榜单口径分离，不确定值标记待核实。"
  },
  {
    "date": "2026-11-07",
    "change": "Round 2逐项深核：重读官方论文PDF/网页、仓库与可访问数据卡，修正版本、授权与方法边界，刷新分轨结构化成绩；无证据字段保留待核实。"
  }
]
```

来源：[1](https://surgehq.ai/benchmarks/gdp-pdf)（访问2026-11-07）

