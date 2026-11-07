# MedQA

> 核查日期：2026-11-07（Asia/Seoul）。事实按字段附来源；论文实验不代表当前排名，待核实不等于未公开。

## 1. 基本信息

### 简称

MedQA

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 全称

MedQA

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 数据版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 论文版本

v1；最近论文日期 2020-09-28

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 发布日期

2020-09-28（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2608.19029v1)（访问 2026-11-07）

### 子领域

医学执照考试式临床推理

来源：[1](https://arxiv.org/html/2608.19029v1)（访问 2026-11-07）

### 许可证

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2009.13081

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 代码入口

https://github.com/jind11/MedQA

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 数据入口

https://github.com/jind11/MedQA

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 官方主页

https://github.com/jind11/MedQA

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 论文标题

What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 2. 发起与维护

### 发起团队

MIT CSAIL与华中科技大学同济医学院署名作者；正式机构发起协议待核实。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 合作与署名机构

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 作者

Jin, Di；Pan, Eileen；Oufattole, Nassim；Weng, Wei-Hung；Fang, Hanyi；Szolovits, Peter

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 维护方

jind11/MedQA官方仓库。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 资助

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 3. 设计目标

### 评测能力

医学执照考试式多项选择，结合临床知识、病例推理与外部证据检索。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 设计动机

给定短文抽取答案的阅读理解难以代表需检索多个医学来源的开放域问答。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 4. 构建方式

### 材料来源

美国、中国大陆、台湾医学资格考试题及相关医学教科书/文档语料。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 编制背景

医学与计算机研究者合作；原考试命题专家逐题身份待核实。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 审核流程

从考试资料收集整理并进行选项/格式处理；独立医学双审人数待核实。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 质量控制

多语言数据与固定划分，论文分析检索噪声和多证据推理失败。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 去污染

公开考试及GitHub测试集存在训练暴露风险；2020原始划分不能证明2026模型无污染。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 5. 数据形式

### 规模

英语12,723、简体中文34,251、繁体中文14,123题；三语合计61,097（由原论文分项相加）。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 题型

病例或医学知识的多项选择；原版与US/大陆4选项处理版须分开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）；[2](https://github.com/jind11/MedQA)（访问 2026-11-07）

### 模态与格式

文本题干、选项、答案；QA逐行保存为JSONL，每行是一个dict；附英语与简体中文教材检索语料。

来源：[1](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问 2026-11-07）

### 语言

英语；简体中文；繁体中文

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 难度

专业医学考试；不等同真实临床工作流或安全性验证。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 公开与隐藏划分

官方仓库提供train/dev/test；US、China及Taiwan分别划分；当前4选项版本与原选项版本不可混用。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）；[2](https://arxiv.org/html/2608.19029v1)（访问 2026-11-07）；[3](https://github.com/jind11/MedQA)（访问 2026-11-07）

## 6. 评测方法

### 指标

Accuracy：选择答案匹配标准答案。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 评分流程

原论文结合检索器与阅读器，也可闭卷选择；检索/开卷与闭卷分开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 提示设置

原论文非统一现代LLM提示；后续模型需注明4/5选项、CoT、shot、检索和测试子集。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 评测入口

https://github.com/jind11/MedQA

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 可比性边界

三语、选项数量、工具与子集必须一致；医学考试高分不代表临床有效或安全。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 7. 最新情况

### 核查日期

2026-11-07 Asia/Seoul

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 已核实版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 版本历史及后续引用

2026_H2_evidence：url：https://arxiv.org/html/2608.19029v1；date：2026-08-19；note：Adaptive Memory and Reflection Multi-Agent System 实际在 MedQA 上评测医学问答。；evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。；paper_metadata：title：What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams；authors：Jin, Di；Pan, Eileen；Oufattole, Nassim；Weng, Wei-Hung；Fang, Hanyi；Szolovits, Peter；release：2020-09-28；latest：2020-09-28；version：v1

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）；[2](https://arxiv.org/html/2608.19029v1)（访问 2026-11-07）

### 饱和情况

后续论文高分不能据此认定所有版本饱和；本轮未核实同一协议下的当前全量头部榜单。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 已知问题

2026 AMR论文方法叙述含逐题反馈，但实验称冻结检索且不写回测试反馈；需结合代码核实，不把该分数当统一榜单。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）；[2](https://arxiv.org/html/2608.19029v1)（访问 2026-11-07）

### 衍生版本

官方另提供美国和中国大陆4_options处理版；不得与原选项版直接混排比较。

来源：[1](https://raw.githubusercontent.com/jind11/MedQA/master/README.md)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 官方榜单入口

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 第三方榜单

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 结果快照

H2使用证据/历史结果：2026-08 AMR(GPT-4o，API快照未给)报告MedQA93.2%；论文称使用官方test、训练集检索。但模型快照、完整评测样本清单待核实；非实时SOTA。

来源：[1](https://arxiv.org/html/2608.19029v1)（访问 2026-11-07）

### 覆盖边界

本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）；[2](https://artificialanalysis.ai/)（访问 2026-11-07）；[3](https://epoch.ai/)（访问 2026-11-07）；[4](https://lmarena.ai/)（访问 2026-11-07）

## 9. 联系方式

### 公开邮箱

jindi15@mit.edu；eileenp@mit.edu；nassim@mit.edu；ckbjimmy@mit.edu；psz@mit.edu；fanghanyi@hust.edu.cn

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 问题反馈

https://github.com/jind11/MedQA/issues

来源：[1](https://github.com/jind11/MedQA)（访问 2026-11-07）

### 官方账号

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 隐私政策

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2009.13081

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### PDF SHA-256

5e19522f21c0ab5c24cc0dacd3feaa5d4b7057391520075f2e521a271d062ee6

来源：[1](https://arxiv.org/pdf/2009.13081)（访问 2026-11-07）

### PDF字节数

189006

来源：[1](https://arxiv.org/pdf/2009.13081)（访问 2026-11-07）

### Drive文件夹

id：1AYwJpnQXewH8Hk2KHLsemGjydd3Fvco0；webViewLink：https://drive.google.com/drive/folders/1AYwJpnQXewH8Hk2KHLsemGjydd3Fvco0

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

### 其他文档

type：中文介绍 Google Doc；id：1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE；webViewLink：https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit

来源：[1](https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit)（访问 2026-11-07）

### Drive PDF

id：1zmvFZ0lC8HCOh62LXlOrjcHf25kzF4gZ；webViewLink：https://drive.google.com/file/d/1zmvFZ0lC8HCOh62LXlOrjcHf25kzF4gZ/view

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）

## 11. 变更记录

### 本页修订

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。

来源：[1](https://arxiv.org/abs/2009.13081)（访问 2026-11-07）
