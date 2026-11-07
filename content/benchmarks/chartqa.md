# ChartQA

> 第1轮深度复核：2026-11-07（KST / Asia/Seoul）。采集日不等于榜单更新日或评测运行日；“待核实”不等于不存在。

[阅读Drive原始论文PDF](https://drive.google.com/file/d/1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy/view?usp=drivesdk)

## 基本信息

### 简称

ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 全称

ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 基准版本

官方Full Version（含annotations）；另保留不含annotations的First Version。README未采用可核实的数字版本号。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 发布日期

2022-03-19

> arXiv元数据首发日期原值；不是推测数据集首次上线时间。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 主板块

多模态

> Benchmark Atlas编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 领域标签

- 图表问答

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 许可证

GPL-3.0（官方HF元数据标示；不据此推断第三方图表版权）

来源：[1](https://huggingface.co/datasets/ahmed-masry/ChartQA/blob/main/README.md)（访问 2026-11-07 KST）。

### 论文

https://arxiv.org/abs/2203.10244

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 官方代码

https://github.com/vis-nlp/ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 数据地址

https://huggingface.co/datasets/ahmed-masry/ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/ahmed-masry/ChartQA)（访问 2026-11-07 KST）。

### 官方入口

https://github.com/vis-nlp/ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 论文标题

ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

## 发起与维护

### 发起机构

论文作者单位：York University、南洋理工大学、Salesforce Research。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 合作研究机构

- York University, Canada
- Nanyang Technological University, Singapore
- Salesforce Research

> 论文作者署名机构，不推断额外商业合作关系。

来源：[1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）。

### 作者

- Masry, Ahmed
- Long, Do Xuan
- Tan, Jia Qing
- Joty, Shafiq
- Hoque, Enamul

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）。

### 维护方

vis-nlp / Ahmed Masry；官方仓库Contact由Ahmed Masry负责接收问题。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 资助

Natural Sciences and Engineering Research Council (NSERC) of Canada。

> 论文Acknowledgement明确资助机构；未补造项目编号。

来源：[1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）。

## 设计目标

### 衡量能力

需要视觉引用、逻辑及算术组合运算的真实图表问答。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 设计背景

既有图表QA多使用模板问题及固定答案词表，难覆盖自然复杂问题。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

## 构建方式

### 题目来源

从Statista、Pew、Our World in Data、OECD采集真实图表；人工问答ChartQA-H与从人工图表摘要自动生成的ChartQA-M并存。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 出题者背景

人工标注者提出自然问题；自动部分由摘要驱动生成，不把全部称为专家原创。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）。

### 审核流程

自动生成数据移除无效问答；SVG自动解析得到视觉标注；Pew缺SVG，另做人工标注和启发式处理。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 质量控制

官方从SVG自动产生框标注；损坏、缺失或带噪的SVG会引入噪声。Pew图表没有SVG，需人工标注并用启发式加速；机器生成测试问答另经手工清理。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）；[2](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）。

### 去污染

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

## 数据形式

### 规模

- **total_qa**：32719
- **train_qa**：28299
- **validation_qa**：1920
- **test_qa**：2500
- **paper_human_qa**：9608
- **paper_machine_qa**：23111
- **paper_human_charts**：4804
- **paper_machine_charts**：17141

> 论文Table2与官方HF splits一致；图表计数为两个来源集合口径，不将4804+17141冒充全库去重图表数。

来源：[1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/ahmed-masry/ChartQA/raw/main/README.md)（访问 2026-11-07 KST）。

### 题型

开放式数值或文本回答；条形图、折线图和饼图，附原始表格及部分框标注。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 模态

图像+文本

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 语言

英文（本次公开问题/官方说明；完整语言分布待核实）

来源：[1](https://huggingface.co/datasets/ahmed-masry/ChartQA)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 难度与类型

- **proxy**：无统一easy/medium/hard标注；论文以任务类型和推理操作分析。
- **sample_analysis**：论文Table4随机300个人工问题：data retrieval 13.0%、visual 10.7%、compositional 43.0%、visual+compositional 33.3%。

> 这是论文抽样类型分布，不外推为完整32,719题的难度分布。

来源：[1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）。

### 公开与隐藏划分

官方数据含train/val/test；human与augmented子集独立文件，test共2,500问题。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

## 评测方法

### 指标

relaxed accuracy：数值误差在参考值5%以内算正确，非数值采用字符串匹配。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 评分

relaxed accuracy：数值误差在参考值5%以内算正确，非数值采用字符串匹配。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 提示和复现设置

论文基线可使用图像和底层数据表；评测时应说明是否使用oracle表格、OCR或仅图像，不能同口径排名。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）；[2](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）。

### 官方脚本

https://github.com/vis-nlp/ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 可比性提示

机器生成/人工子集分别报告；官方指出SVG缺失/损坏使框标注有噪声。MMVistaReason使用CompassVerifier，不等同于原始5%数值容差。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）；[3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-07 KST / Asia/Seoul

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 最新版本与H2证据

本轮核实官方Full Version（含图像框标注），HF train/val/test为28,299/1,920/2,500；官方后续ChartQAPro是独立基准，不替代原版数据版本。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）；[2](https://huggingface.co/datasets/ahmed-masry/ChartQA/raw/main/README.md)（访问 2026-11-07 KST）。

### 论文修订与H2使用证据

- **revisions**：[{"version": "v1", "date_kst": "2022-03-19T14:00:30+09:00"}]
- **continued_use_2026h2**：[{"url": "https://arxiv.org/html/2610.01352v2", "date": "2026-10-23", "note": "MMVistaReason v2 §4.1及表2实际评测 ChartQA（ChartQA设置），比较4B/9B及其他视觉语言模型；不把mini/val等划分另计。", "date_kst": "2026-10-23T01:54:37+09:00", "verified_in_round1": "本轮重新打开arXiv v2正文§4.1/Table2与abs提交历史，确认实际评测；源站v2为2026-10-22 16:54:37 UTC。"}]
- **verification**：已打开并复核证据原文的实际评测章节及表格，不只按参考文献或网页存活判断。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）；[3](https://arxiv.org/abs/2610.01352)（访问 2026-11-07 KST）。

### 饱和程度

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 污染、冲突与限制

机器生成/人工子集分别报告；官方指出SVG缺失/损坏使框标注有噪声。MMVistaReason使用CompassVerifier，不等同于原始5%数值容差。

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）；[3](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

### 后续工作与衍生

ChartQAPro，官方仓库推荐的更具挑战的真实图表QA后续基准；本条不将Pro另计入原版结果。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-07

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 官方榜单

https://github.com/vis-nlp/ChartQA

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 权威第三方覆盖

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07 KST）。

### 结果快照

- {"model": "VisionTaPas", "score": 45.52, "unit": "%", "metric": "原论文准确率（数值答案允许5%容差）", "scope": "ChartQA原论文Table5，gold data table not provided，test；历史基线", "date": "2022-05", "accessed": "2026-11-07 KST", "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf", "provenance": "原始基准作者公布；本轮从官方ACL论文重新读取，不宣称当前排名。"}
- {"model": "VL-T5", "score": 41.56, "unit": "%", "metric": "原论文准确率（数值答案允许5%容差）", "scope": "ChartQA原论文Table5，gold data table not provided，test；历史基线", "date": "2022-05", "accessed": "2026-11-07 KST", "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf", "provenance": "原始基准作者公布；本轮从官方ACL论文重新读取，不宣称当前排名。"}
- {"model": "TaPas", "score": 41.28, "unit": "%", "metric": "原论文准确率（数值答案允许5%容差）", "scope": "ChartQA原论文Table5，gold data table not provided，test；历史基线", "date": "2022-05", "accessed": "2026-11-07 KST", "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf", "provenance": "原始基准作者公布；本轮从官方ACL论文重新读取，不宣称当前排名。"}
- {"model": "MMVistaReason-4B (MVR-4B)", "score": 86.2, "unit": "%", "metric": "论文协议答案正确率（CompassVerifier）", "scope": "ChartQA", "date": "2026-10-23", "accessed": "2026-11-07", "source_url": "https://arxiv.org/html/2610.01352v2", "provenance": "MMVistaReason作者自报表2；VLMEvalKit，T=0，max16384；§7.3用CompassVerifier替代传统字符串匹配，不是官方榜单/AA独立评测", "date_basis": "arXiv v2提交时间换算KST；不是未公开的评测运行日期。"}
- {"model": "MMVistaReason-9B (MVR-9B)", "score": 87.6, "unit": "%", "metric": "论文协议答案正确率（CompassVerifier）", "scope": "ChartQA", "date": "2026-10-23", "accessed": "2026-11-07", "source_url": "https://arxiv.org/html/2610.01352v2", "provenance": "MMVistaReason作者自报表2；同上协议，不与其他榜单无条件混排", "date_basis": "arXiv v2提交时间换算KST；不是未公开的评测运行日期。"}

来源：[1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）；[2](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

### 覆盖说明

本轮重新检查官方README、Full Version数据卡及AA评测目录，未核实持续更新的原版ChartQA独立榜单。以下新采集官方论文Table5历史基线（无gold table），与2026-H2作者复测分组；这些不是2026实时前三。当前官方排名仍待核实。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）；[2](https://aclanthology.org/2022.findings-acl.177.pdf)（访问 2026-11-07 KST）；[3](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问 2026-11-07 KST）；[4](https://arxiv.org/html/2610.01352v2)（访问 2026-11-07 KST）。

## 联系方式

### 公开联系邮箱

- amasry17@ku.edu.tr

> 官方README明确旧邮箱masry20@yorku.ca已停用；当前联系不再推荐旧邮箱。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 问题反馈

https://github.com/vis-nlp/ChartQA/issues

来源：[1](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

### 官方讨论渠道

旧学校邮箱masry20@yorku.ca已停用，采用官方README当前公开联系邮箱。

来源：[1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问 2026-11-07 KST）。

### 隐私政策

仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07 KST）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2203.10244

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）。

### SHA-256

3b1d863e6f9ca45e84131bc51c8e47c8026faf6a6875edb9032bce2b9fadf0f9

> 下载原始字节校验，未压缩、未改写。

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）。

### 字节数

2938574

来源：[1](https://arxiv.org/pdf/2203.10244)（访问 2026-11-07 KST）。

### Drive文件夹

- **id**：1elALF3JQUPeGjv3Ee6JqeABOnA8QVlFq
- **webViewLink**：https://drive.google.com/drive/folders/1elALF3JQUPeGjv3Ee6JqeABOnA8QVlFq

来源：[1](https://drive.google.com/drive/folders/1elALF3JQUPeGjv3Ee6JqeABOnA8QVlFq)（访问 2026-11-07 KST）。

### 其他文档

- {"kind": "中文介绍 Google Doc", "id": "1UkqHF3gkf4lU5t9Ef0agnMxVRhs5_KmcDXVOy1cIsgM", "webViewLink": "https://docs.google.com/document/d/1UkqHF3gkf4lU5t9Ef0agnMxVRhs5_KmcDXVOy1cIsgM/edit?usp=drivesdk"}

来源：[1](https://docs.google.com/document/d/1UkqHF3gkf4lU5t9Ef0agnMxVRhs5_KmcDXVOy1cIsgM/edit?usp=drivesdk)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy
- **webViewLink**：https://drive.google.com/file/d/1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- {"date": "2026-11-07", "timezone": "Asia/Seoul", "change": "核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "round": "1 / 深度实证复核", "change": "补Full/First版本区别、NSERC资助、机构、最新联系邮箱和题量/类型分布；采集官方论文历史基线，当前独立实时榜仍未核实；重核H2。"}

来源：[1](https://arxiv.org/abs/2203.10244)（访问 2026-11-07 KST）；[2](https://github.com/vis-nlp/ChartQA)（访问 2026-11-07 KST）。

