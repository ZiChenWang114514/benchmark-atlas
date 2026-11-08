# Code2Video Bench

> Benchmark Constitution · 深度核验快照 2026-11-07。待核实不等于未公开；采集日期不等于榜单更新时间。

Code2Video Bench评估“写代码生成好视频”，不是只检查代码能否运行。HeyGen原版为168个人工参考片段/brief及自训偏好裁判；AA是114 brief和Gemini裁判的独立实现。两套Elo依赖不同题集、裁判与对手池，必须分轨展示。

导读依据：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）；[1](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

## 基本信息

**简称**：Code2Video Bench

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**全称**：Code2Video Benchmark（Benchmarking Code-to-Video: Evaluating AI Agents on the Art of Motion Design）

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**基准版本**：HeyGen 2026-09-18网页报告：168条；AA独立Code2Video-AA：114条。不是同一题集的统一语义版本。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**论文版本**：2026-09-18官方网页技术报告；未据此冒称arXiv论文。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**发布日期**：2026-09-18（HeyGen 技术报告日期）

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**主板块**：多模态

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：Benchmark Constitution 编辑归档；AA 归入 Coding。

**领域**：代码生成；动效/视频设计

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**许可与范围**：HyperFrames渲染框架Apache-2.0；168条基准素材、参考视频及judge API的独立授权待核实。

来源：[1](https://raw.githubusercontent.com/heygen-com/hyperframes/main/LICENSE)（访问2026-11-07）；[2](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**论文/技术报告**：https://www.heygen.com/research/introducing-code2video-benchmark

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**代码**：https://github.com/heygen-com/hyperframes

来源：[1](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

核验说明：HyperFrames 渲染框架，非评测代码本身。

**数据**：https://www.kaggle.com/benchmarks/heygen/code2video

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**主页**：https://www.heygen.com/research/introducing-code2video-benchmark

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**论文标题**：Benchmarking Code-to-Video: Evaluating AI Agents on the Art of Motion Design

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

## 发起与维护

**发起/作者单位**：HeyGen

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**合作关系**：Kaggle（联合发布完整基准）；Artificial Analysis（独立实现 Code2Video-AA）

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

**作者**：Abhay Zala、Miao Yang、Wenbo Zhu、Bin Liu 及 Kaggle Team

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**维护方**：HeyGen

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**资助**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

**测量能力**：根据设计 brief 写出可确定性渲染为视频的代码（HTML/GSAP），衡量动效设计质量而不只是代码可运行。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

**针对的不足**：模型榜单多测可核对答案的题，创意/视频类缺少量化评价。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

## 构建方式

**材料来源**：HeyGen 设计 brief 与人类参考合成作品

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**出题背景**：人类参考动效作品与设计brief由人工创建；偏好标注者先接受动效设计基础训练和筛选。报告作者为HeyGen研究人员及Kaggle Team。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**审核**：按每个设计轴收集成对人类偏好，标注者培训/筛选后参与评价；报告以保留的样本对检验裁判与人类一致性。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**质控**：训练并筛选偏好标注者；作者报告裁判在人类对齐评估的1,464样本上为82%，通用VLM为75%。这是作者评估，不是视频任务正确率；比较VLM时交换视频顺序控制位置偏差。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**去污染边界**：报告展示未用于裁判训练的held-out样本对；这只支撑裁判泛化检验，不是被测生成模型预训练去污染证明。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

## 数据形式

**规模与统计口径**：HeyGen原版168个人工创建动效参考视频/brief，覆盖8类产品发布片段；AA独立版114 brief，不相加凑题量。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**任务形式**：代码生成 → 渲染视频 → 成对比较

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**模态**：文本 brief；HTML/JS 代码；视频

来源：[1](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

**语言**：报告和公开示例brief为英语；输出为HTML/CSS/JavaScript动效代码。未据此宣称只有一种渲染文本语言。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**难度**：覆盖Hook、Problem、Product intro、Key feature、Benefits、Social proof、Call to action、Brand outro；难点是时间/构图/工艺而非语法可运行性，不设统一考试难度等级。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**公开/保留划分**：HeyGen称与Kaggle发布全部参考、brief及judge API；Kaggle页面本次静态抓取仅得标题，未独立核实文件清单。AA页另标Private Dataset，同时展示3个公开split任务；不能把两套发布状态混写。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

## 评测方法

**指标**：Elo（成对比较）；AA 为五轴 Elo 平均，以 GPT-5.5 (xhigh)=1000 为锚

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

**评分**：五个轴：吸引力、贴合意图、构图、时间一致性、工艺；HeyGen 用自训裁判模型，AA 用 Gemini 4 Argon 盲评

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

**提示与运行设定**：HeyGen给被测模型HyperFrames skill，跑168 prompts并渲染，与人类参考和其他模型作round-robin配对；AA每brief生成一个HyperFrames HTML/GSAP作品。具体运行预算未核实，不推测。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**脚本/运行入口**：渲染框架与skill：https://github.com/heygen-com/hyperframes；HeyGen称Kaggle运行Harbor-compatible数据/定制harness，不能把渲染器当作完整benchmark评分代码。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**可比性**：HeyGen 原版与 AA 实现题量、裁判不同，Elo 不可互比；Elo 依赖对手池。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**当前版本证据**：version：HeyGen 2026-09-18网页报告：168条；AA独立Code2Video-AA：114条。不是同一题集的统一语义版本。；evidence_2026_h2：url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；organization：Artificial Analysis；note：当前方法页将Code2Video Bench列为正在实施的评测，披露任务或评分协议。；url：https://artificialanalysis.ai/evaluations；date：2026-11-07；organization：Artificial Analysis；note：当前公开评测目录单列Code2Video Bench，不是新闻提及。；url：https://www.heygen.com/research/introducing-code2video-benchmark；date：2026-11-07；organization：HeyGen；note：HeyGen官方原始基准介绍与AA独立实现并存。；trending：heat_confidence：A；summary：HeyGen 视频生成代码评测被 AA 目录标 New 并独立实现。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**修订历史**：已核实网页技术报告署期2026-09-18；未找到可核验arXiv修订序列。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**饱和**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**争议与局限**：Elo随对手池及裁判改变；HeyGen自训裁判与AA Gemini 4 Argon不是同一个评分器。报告top4置信区间重叠，不能只按点估计认定显著胜出。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**派生/去重**：Code2Video-AA为AA独立实现，114条和五轴Gemini裁判；与HeyGen168条/自训裁判分轨记录，不合并分数或重复计数。

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

## 榜单快照

**快照日**：2026-11-07

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**官方榜**：https://www.kaggle.com/benchmarks/heygen/code2video

来源：[1](https://www.kaggle.com/benchmarks/heygen/code2video)（访问2026-11-07）；[2](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

**独立评测**：https://artificialanalysis.ai/evaluations/code2video-aa

来源：[1](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）

### 分轨结果（不合并来源/题集/协议）

**AA / Code2Video-AA / 114 briefs**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | Claude Opus 5.5 (Max, Default Fallback) | 1536 | five-axis mean Elo |
| 2 | Claude Sonnet 5.5 (Max, Default Fallback) | 1443 | five-axis mean Elo |
| 3 | GPT-6 Astra (Max) | 1427 | five-axis mean Elo |
| 4 | GPT-6.1 Sol (Max) | 1369 | five-axis mean Elo |
| 5 | Claude Fable 5.1 (Max, Default Fallback) | 1325 | five-axis mean Elo |
| 6 | Gemini 4 Argon (High) | 1259 | five-axis mean Elo |
| 7 | Claude Haiku 5.5 (Max) | 1192 | five-axis mean Elo |
| 8 | Grok 4.7 (Xhigh) | 1127 | five-axis mean Elo |
| 9 | DeepSeek V4.1 Flash (Max) | 1053 | five-axis mean Elo |
| 10 | MiMo-V2.6-Flash | 1052 | five-axis mean Elo |
| 11 | MiMo-V2.6-Pro | 1052 | five-axis mean Elo |
| 12 | Kimi K3 (Max) | 1041 | five-axis mean Elo |
| 13 | GLM-5.3 (Max) | 1034 | five-axis mean Elo |
| 14 | GPT-6 Luna (Max) | 1030 | five-axis mean Elo |
| 15 | Qwen3.8 Max (0902) | 1021 | five-axis mean Elo |
| 16 | Inkling 2 Small | 1020 | five-axis mean Elo |
| 17 | Muse Spark 1.3 (Max) | 1019 | five-axis mean Elo |
| 18 | GPT-5.5 (Xhigh) | 1000 | five-axis mean Elo |
| 19 | Muse Wonder (Max) | 997 | five-axis mean Elo |
| 20 | GLM-5.3-Flash | 975 | five-axis mean Elo |
| 21 | Qwen3.8 27B (Xhigh) | 949 | five-axis mean Elo |
| 22 | Mistral Large 4 Preview | 931 | five-axis mean Elo |
| 23 | Gemini 3.8 Flash (High) | 899 | five-axis mean Elo |
| 24 | Step 5 Preview | 821 | five-axis mean Elo |
| 25 | MiniMax-M3 | 724 | five-axis mean Elo |
| 26 | Beam 1.0 | 675 | five-axis mean Elo |
| 27 | Inkling (Xhigh) | 467 | five-axis mean Elo |
| 28 | Nemotron 3 Ultra 550B A55B (Reasoning) | 304 | five-axis mean Elo |

来源：[https://artificialanalysis.ai/evaluations/code2video-aa](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Engagement**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-5.5 | 1578 | Elo |
| 2 | gpt-6-astra | 1576 | Elo |
| 3 | claude-opus-5 | 1571 | Elo |

scope：报告overall top5中的轴内排名，非全部模型轴榜

来源：[https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Prompt-Intent**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-6-astra | 1577 | Elo |
| 2 | gpt-5.5 | 1575 | Elo |
| 3 | claude-opus-5 | 1570 | Elo |

scope：报告overall top5中的轴内排名，非全部模型轴榜

来源：[https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Composition**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-5.5 | 1585 | Elo |
| 1 | gpt-6-astra | 1585 | Elo |
| 3 | claude-opus-5 | 1576 | Elo |

scope：报告overall top5中的轴内排名，非全部模型轴榜

来源：[https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Temporal**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-5.5 | 1579 | Elo |
| 2 | gpt-6-astra | 1578 | Elo |
| 3 | gpt-5.6-sol | 1568 | Elo |

scope：报告overall top5中的轴内排名，非全部模型轴榜

来源：[https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**HeyGen / 168 prompts / Craft**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | gpt-6-astra | 1586 | Elo |
| 2 | gpt-5.5 | 1585 | Elo |
| 3 | claude-opus-5 | 1574 | Elo |

scope：报告overall top5中的轴内排名，非全部模型轴榜

来源：[https://www.heygen.com/research/introducing-code2video-benchmark](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：AA表28配置全部录入（图表另写27 of 28，保留显示差异），保留Max及Default Fallback完整模型名。HeyGen仅收录可逐字核实的五轴top3数值，不从overall图估读。两来源分轨，Elo不合并、不平均；Kaggle静态抓取仅得标题，不能将其称已核验实时榜。

来源：[1](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[2](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[3](https://www.kaggle.com/benchmarks/heygen/code2video)（访问2026-11-07）

## 联系方式

**公开研究邮箱**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**Issues**：https://github.com/heygen-com/hyperframes/issues

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**公开社区**：HyperFrames官方README所链社区：https://discord.gg/fzbdWyjphr

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

**隐私原则**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

**PDF**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**原件SHA-256**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**PDF字节数**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**目录**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

**其他文档**：type：官方网页技术报告；url：https://www.heygen.com/research/introducing-code2video-benchmark；type：Kaggle官方基准入口；url：https://www.kaggle.com/benchmarks/heygen/code2video；type：AA独立评测；url：https://artificialanalysis.ai/evaluations/code2video-aa

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）；[2](https://artificialanalysis.ai/evaluations/code2video-aa)（访问2026-11-07）；[3](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md)（访问2026-11-07）

** PDF**：待核实

来源：[1](https://www.heygen.com/research/introducing-code2video-benchmark)（访问2026-11-07）

## 变更记录

- date：2026-11-07；timezone：；change：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。
- date：2026-11-07；timezone：；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
