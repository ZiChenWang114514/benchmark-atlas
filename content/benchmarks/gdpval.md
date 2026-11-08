# GDPval (GDPval-AA v2.1)

> Benchmark Constitution｜深度核验：2026-11-07。访问日沿固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

GDPval以职业交付物为对象，原版比较模型与专家产物的盲评偏好；GDPval-AA则在独立Agent环境里比较模型产物并估计Elo。HF公开数据v2与AA v2.1不是同一个版本号。

最近复核

## 基本信息

**简称**：GDPval (GDPval-AA v2.1)

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**全称**：GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**基准版本**：GDPval公开数据v2（HF当前提交说明：rubrics + deliverables）；GDPval-AA v2.1为独立评测实现，不是同一版本号。

来源：[1](https://huggingface.co/datasets/openai/gdpval/tree/main)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

**论文版本**：arXiv v1（2025-10-05）

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**发布日期**：2025-09-25（官方首次发布文；arXiv首版为2025-10-06 06:36:43 ）

来源：[1](https://openai.com/index/gdpval/)（访问 2026-11-07）；[2](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**主板块**：Agent

核验说明：Benchmark Constitution 编辑归档，不作为官方分类。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**领域标签**：知识工作；金融；法律

核验说明：编辑标签

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**许可证与授权边界**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**论文或技术报告**：https://arxiv.org/abs/2510.04374

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**官方代码**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**数据地址**：https://huggingface.co/datasets/openai/gdpval

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**官方主页**：https://huggingface.co/datasets/openai/gdpval

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**论文题名**：GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 发起与维护

**发起方**：OpenAI

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**协作与机构边界**：任务由各职业的外部专业人员协作编写并盲评；其过往雇主名单只是履历例举，不能作为机构合作关系。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）；[2](https://openai.com/index/gdpval/)（访问 2026-11-07）

**作者**：Tejal Patwardhan；Rachel Dias；Elizabeth Proehl；Grace Kim；Michele Wang；Olivia Watkins；Simón Posada Fishman；Marwan Aljubeh；Phoebe Thacker；Laurance Fauconnet；Natalie S. Kim；Patrick Chao；Samuel Miserendino；Gildas Chabot；David Li；Michael Sharman；Alexandra Barr；Amelia Glaese；Jerry Tworek

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**维护方**：原始数据：OpenAI；独立实现：Artificial Analysis

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

## 设计目标

**测量能力**：以真实职业任务衡量经济相关知识工作的交付物质量。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**相对既有评测的缺口**：学术短答案测试难以覆盖职业工作中的文件处理、审美与可用性。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 构建方式

**题目来源**：专业从业者实际工作产物，按O*NET工作活动选择9个产业的44个职业。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**出题与研究背景**：专家至少4年职业经验，平均14年；通过面试、背景核查、训练与测验。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**审核流程**：自动筛查加通才初审、同行职业专家复审、迭代最终审核。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**质量控制**：全体1,320任务平均5轮、至少3轮人工审核。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**去污染与泄漏边界**：公开gold子集已清理出题者识别信息；不能据此认定完全无训练污染。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 数据形式

**规模与口径**：全量1,320任务；公开gold子集220任务，每职业5题。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**任务类型**：文本请求、参考文件、职业交付物；文件包括文档、表格、幻灯片、CAD及音视频。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**模态**：文本；文档；图像；音频；视频；表格

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**语言**：公开样例为英语职业任务；多语言覆盖待核实。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**难度**：职业长程任务；不等同完整职业可被自动化。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**公开与隐藏划分**：220任务gold子集公开；其余全量数据的可获取性待核实。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 评测方法

**指标**：原始轨：模型交付物相对人类专家产物的盲评胜率；AA轨：成对模型交付物Elo。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**评分方式**：原始推荐职业专家成对比较；自动裁判为实验代理而非完全替代专家。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**提示与运行设置**：AA使用Stirrup agent循环，提供shell与网页浏览；盲化两份输出由LLM裁判比较。

来源：[1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

**官方复现入口**：原始评测提供evals.openai.com实验自动评分服务；官方论文明确它不替代职业专家盲评。独立AA实现采用Stirrup，不能当作原始官方评分脚本。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）；[2](https://openai.com/index/gdpval/)（访问 2026-11-07）；[3](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

**可比性警告**：原始对人类胜率不等于GDPval-AA v2.1 Elo；harness、预算与裁判差异须分轨。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**数据及热度证据**：```json
{
 "version": "GDPval公开数据v2（rubrics + deliverables）；GDPval-AA v2.1独立实现"
 "heat_confidence": "A"
 "why_trending": "候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。"
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "当前ECI组成明确列出该benchmark；纳入不等于运行。"
 }
 {
 "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Artificial Analysis"
 "note": "当前v2.1独立评测榜明确展示前沿模型Elo。"
 }
 ]
}
```

来源：[1](https://huggingface.co/datasets/openai/gdpval/tree/main)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

**论文与版本历史**：arXiv当前提交历史仅v1：2025-10-06 06:36:43；数据与发布文早于该论文首版。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）；[2](https://openai.com/index/gdpval/)（访问 2026-11-07）

**饱和程度**：原始指标是相对人类专家的偏好胜率，不是任务绝对正确率；AA指标为相对Elo（锚点1600），无100%式上限，不可用榜首1866称已饱和。

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

**已知问题与局限**：公开gold任务和交付物可能被后续训练看到；一次性明确请求不覆盖真实工作澄清与多轮修改；模型推理时间/费用节约不含监督、集成及纠错成本。

来源：[1](https://openai.com/index/gdpval/)（访问 2026-11-07）；[2](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）；[3](https://huggingface.co/datasets/openai/gdpval/tree/main)（访问 2026-11-07）

**后续与衍生**：GDPval数据与AA评测实现同条分轨，不拆成两项；AA v5已移出综合指数但仍单独评测。

核验说明：编辑去重口径；具体版本差异仍以官方材料为准。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

## 榜单快照

**快照日期**：2026-11-07

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**官方入口**：https://huggingface.co/datasets/openai/gdpval

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**第三方入口**：https://artificialanalysis.ai/evaluations/gdpval-aa

来源：[1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | Claude Opus 5.5 (Max, Default Fallback) | 1866 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 2 | Kimi K3.1 Pro | 1858 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 3 | Muse Wonder Full (Max) | 1857 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 4 | Claude Sonnet 5.5 (Max, Default Fallback) | 1838 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 5 | Claude Opus 5.5 (Xhigh, Default Fallback) | 1835 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 6 | Muse Wonder (Max) | 1770 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 7 | Claude Fable 5.1 (Max, Default Fallback) | 1763 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| 当前官方网页榜 | 8 | DeepSeek V4.1 Flash 1017 (Max) | 1746 | GDPval-AA v2.1 Elo | 待核实（榜表更新时间） | [原始来源](https://artificialanalysis.ai/evaluations/gdpval-aa) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：重读AA当前榜前8，保留reasoning及fallback配置、置信区间；锚定DeepSeek V4.1 Flash(max)=1600。模型发行月不是榜表更新时间。数据v2、AA v2.1及原始专家胜率三种口径必须区分。

来源：[1](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/gdpval/tree/main)（访问 2026-11-07）

## 联系方式

**公开联系邮箱**：tejal@openai.com（论文公开通讯渠道）

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**Issues或讨论入口**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**官方社交**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**隐私政策**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

## 原始文件

**原始PDF**：https://arxiv.org/pdf/2510.04374

来源：[1](https://arxiv.org/abs/2510.04374)（访问 2026-11-07）

**PDF SHA-256**：a04cca8451c486d871f8d2c6c57b8bc03b45daf1b5b0269146929bc8bf688dec

核验说明：下载原始PDF字节计算，非arXiv网页显示大小。

来源：[1](https://arxiv.org/pdf/2510.04374)（访问 2026-11-07）

**PDF字节数**：```json
14203711
```

核验说明：实际下载字节数；不代表已上传。

来源：[1](https://arxiv.org/pdf/2510.04374)（访问 2026-11-07）

**文件夹**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

**其他官方文档**：```json
[
 {
 "type": "首次发布与限制"
 "url": "https://openai.com/index/gdpval/"
 }
 {
 "type": "公开数据v2目录"
 "url": "https://huggingface.co/datasets/openai/gdpval/tree/main"
 }
 {
 "type": "独立AA v2.1方法与榜单"
 "url": "https://artificialanalysis.ai/evaluations/gdpval-aa"
 }
]
```

来源：[1](https://openai.com/index/gdpval/)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/gdpval/tree/main)（访问 2026-11-07）；[3](https://artificialanalysis.ai/evaluations/gdpval-aa)（访问 2026-11-07）

**论文链接**：待核实

状态：待核实。

核验说明：本组仅建立本地研究条目，未上传。

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）

## 变更记录

**及历史变更**：```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-07"
 最近复核
 }
]
```

来源：[1](https://huggingface.co/datasets/openai/gdpval)（访问 2026-11-07）
