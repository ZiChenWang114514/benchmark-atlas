# BioCoder

> 核查日期：2026-11-07（Asia/Seoul）。事实按字段附来源；论文实验不代表当前排名，待核实不等于未公开。

## 1. 基本信息

### 简称

BioCoder

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 全称

BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 数据版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 论文版本

v5；最近论文日期 2024-05-20

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 发布日期

2023-08-31（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 子领域

生物信息学代码生成

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 许可证

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2308.16458

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 代码入口

https://github.com/gersteinlab/BioCoder

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 数据入口

https://github.com/gersteinlab/BioCoder

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 官方主页

https://biocoder-benchmark.github.io/

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 论文标题

BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 2. 发起与维护

### 发起团队

Yale与Google DeepMind论文作者合作。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 合作与署名机构

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 作者

Tang, Xiangru；Qian, Bill；Gao, Rick；Chen, Jiakang；Chen, Xinyun；Gerstein, Mark

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 维护方

gersteinlab/BioCoder与官方项目页。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 资助

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 3. 设计目标

### 评测能力

带依赖、类、全局变量等真实上下文的生物信息学函数代码生成。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 设计动机

一般短函数题不充分测试生物知识、复杂数据操作及真实项目上下文。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 4. 构建方式

### 材料来源

GitHub生物项目中的Python函数、Java方法及Rosalind编程题。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 编制背景

Yale/Google DeepMind生物信息与代码生成研究团队；非声称所有题均独立专家原创。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 审核流程

语法解析抽取真实函数，静态分析、人工测试和fuzzing结合构建验证。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 质量控制

Docker可执行测试环境与自动化模糊测试，保留依赖/类/全局环境。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 去污染

源代码与Rosalind公开，可能进入代码预训练；独立训练语料去重审计待核实。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 5. 数据形式

### 规模

1,026 Python函数、1,243 Java方法，另253个Rosalind例子；不要混同为同一语言总题数。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 题型

根据签名/上下文/描述生成函数或方法体；多个提示布局。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 模态与格式

源代码、自然语言说明、单元/模糊测试。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 语言

Python；Java；英语提示

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 难度

真实项目依赖和专业生物信息任务；无统一难度分档。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 公开与隐藏划分

README列出java_hidden 1,243、python_hidden 1,026；另各有50条public与50条similar；rosalind 253条。名称hidden不等于当前访问受限：README明确完整公共数据已在仓库发布。

来源：[1](https://raw.githubusercontent.com/gersteinlab/BioCoder/main/README.md)（访问 2026-11-07）

## 6. 评测方法

### 指标

Pass@1/5/10/20，分Python、Java、Rosalind。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 评分流程

代码运行与fuzz-testing判断Passed；Rosalind示例每题20次生成，按组合概率估计Pass@1/5/10/20并跨题均值。不可把Pass@20当成一次生成准确率。

来源：[1](https://raw.githubusercontent.com/gersteinlab/BioCoder/main/README.md)（访问 2026-11-07）

### 提示设置

官网Summary Only榜：temperature0.7、top-p0.95、最大生成256token；GPT4上下文8192。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）；[2](https://biocoder-benchmark.github.io/)（访问 2026-11-07）

### 评测入口

官方仓库evaluation/包含Docker/AWS队列执行框架，TestRosalind/tester.py生成results.json；README指出完全本地化框架为未来计划，不宣称已提供。

来源：[1](https://raw.githubusercontent.com/gersteinlab/BioCoder/main/README.md)（访问 2026-11-07）

### 可比性边界

提示布局、上下文窗口、生成长度和语言不同影响结果。官网模型日期为历史标签，不应误写采集日模型排名。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 7. 最新情况

### 核查日期

2026-11-07 Asia/Seoul

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 已核实版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 版本历史及后续引用

2026_H2_evidence：url：https://arxiv.org/html/2610.21074v1；date：2026-10-15；note：OmicsBench §2明确引用 BioCoder（Tang等2024），讨论其生物代码生成评测与新基准的区别。；evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。；paper_metadata：title：BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models；authors：Tang, Xiangru；Qian, Bill；Gao, Rick；Chen, Jiakang；Chen, Xinyun；Gerstein, Mark；release：2023-08-31；latest：2024-05-20；version：v5

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 饱和情况

官网历史低通过率不说明2026模型当前上限；本轮未获得更新统一实验。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 已知问题

公开GitHub代码可能训练暴露；fuzz覆盖率不足时通过不等于所有输入都正确。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 衍生版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 官方榜单入口

https://biocoder-benchmark.github.io/

来源：[1](https://biocoder-benchmark.github.io/)（访问 2026-11-07）

### 第三方榜单

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 结果快照

官网本轮仍为2023模型历史榜：gpt-4(Azure，2023-03-14标签) SummaryOnly Pass@1：Python38.439%、Java45.011%、Rosalind24.308%；同设置Python Pass@20 52.229%。并非2026新实验。

来源：[1](https://biocoder-benchmark.github.io/)（访问 2026-11-07）

### 覆盖边界

本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）；[2](https://artificialanalysis.ai/)（访问 2026-11-07）；[3](https://epoch.ai/)（访问 2026-11-07）；[4](https://lmarena.ai/)（访问 2026-11-07）

## 9. 联系方式

### 公开邮箱

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 问题反馈

https://github.com/gersteinlab/BioCoder/issues

来源：[1](https://github.com/gersteinlab/BioCoder)（访问 2026-11-07）

### 官方账号

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 隐私政策

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2308.16458

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### PDF SHA-256

c10e1ca00454f617439153c6646eb406ea01ffc3bf14fef420a6968223858b1e

来源：[1](https://arxiv.org/pdf/2308.16458)（访问 2026-11-07）

### PDF字节数

1569722

来源：[1](https://arxiv.org/pdf/2308.16458)（访问 2026-11-07）

### Drive文件夹

id：1QOAh5NYgNGWbpMDqIh5mq-XaSYEKEbea；webViewLink：https://drive.google.com/drive/folders/1QOAh5NYgNGWbpMDqIh5mq-XaSYEKEbea

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

### 其他文档

type：中文介绍 Google Doc；id：1Q2TZE2KmhY9m_nGvmSuRcgva8GaaoYHVfHi2djMz1lQ；webViewLink：https://docs.google.com/document/d/1Q2TZE2KmhY9m_nGvmSuRcgva8GaaoYHVfHi2djMz1lQ/edit

来源：[1](https://docs.google.com/document/d/1Q2TZE2KmhY9m_nGvmSuRcgva8GaaoYHVfHi2djMz1lQ/edit)（访问 2026-11-07）

### Drive PDF

id：1UGyQMMdGXcWUV18accbXO_a7H1Keg1Xk；webViewLink：https://drive.google.com/file/d/1UGyQMMdGXcWUV18accbXO_a7H1Keg1Xk/view

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）

## 11. 变更记录

### 本页修订

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。

来源：[1](https://arxiv.org/abs/2308.16458)（访问 2026-11-07）
