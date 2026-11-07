# AstroBench

> 核查：2026-11-07（Asia/Shanghai，UTC+8）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

第2轮逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

AstroBench

来源：[1][2][3]

### 全称

AstroBench

来源：[1][2][3]

说明：使用官方名称；未有已核实全称扩展时保留原名，不把论文标题误当基准全称。

### 数据/软件版本

Astrobench_MCQ_v1_Public（3846题清理公开集）；与AstroMLab-1论文4425题内部实验集区分。

来源：[3][4]

### 论文版本

arXiv v2

来源：[1][2][3]

### 发布日期

2024-07-16 03:28:14（Asia/Shanghai，UTC+8；原论文arXiv v1提交时刻）

来源：[1]

### 主板块

地球与天文

来源：[1]

说明：Benchmark Constitution 编辑归档；跨学科条目只在主板块计数，另用标签导航。

### 学科标签

天文

来源：[1][2][3]

### 许可证与范围

MIT（官方HF数据集卡声明）。

来源：[3]

### 论文入口

https://arxiv.org/abs/2407.11194

来源：[1][2][3]

### 论文标题

AstroMLab 1: Who Wins Astronomy Jeopardy!?

来源：[1][2][3]

### 官方代码

待核实

来源：[1][2][3]

状态：待核实（本字段尚有未能确认的部分）。

### 数据入口

https://huggingface.co/datasets/AstroMLab/Astrobench_MCQ_v1_Public

来源：[1][2][3]

### 官方主页

https://astromlab.org/

来源：[1][2][3]

## 2. 发起与维护

### 发起团队

澳大利亚国立大学、俄亥俄州立大学等多机构作者团队（AstroMLab）

来源：[1][2][3]

说明：主要依据论文作者单位/官方团队介绍；不据此推断法律所有权或唯一发起方。文本已明确标注未核实的正式发起关系。

### 署名/合作机构

University of Pennsylvania；Oak Ridge National Laboratory；Hong Kong University of Science and Technology；IIT Patna；Tsinghua University；KEK/QUP；Argonne National Laboratory；Harvard & Smithsonian

来源：[2]

说明：原论文首页作者单位；不据此声称法律合作关系。

### 作者

Ting, Yuan-Sen；Nguyen, Tuan Dung；Ghosal, Tirthankar；Pan, Rui；Arora, Hardik；Sun, Zechang；de Haan, Tijmen；Ramachandra, Nesar；Wells, Azton；Madireddy, Sandeep；Accomazzi, Alberto

来源：[1][2][3]

### 维护入口

AstroMLab：天文学与AI研究者协作团队，官方HF组织维护数据与模型发布。

来源：[5][3]

### 资助与计算资源

计算资源：澳大利亚政府支持的NCI、Oak Ridge Leadership Computing Facility Frontier；Microsoft AFMR；Argonne部分工作获美国DOE高能物理与ASCR通过SciDAC-RAPIDS2支持（DE-AC02-06CH11357）。

来源：[2]

## 3. 设计目标

本轮最重要的变化是补上官方后续论文：4425题原始内部实验与3846题公开清理版之间的差异已有明确清理说明。它主要测试天文知识召回；不能把博士领域定位直接当作原创科研能力证明。
来源：[1][2][3][2][4]

### 测量能力

测量天文学及天体物理知识理解、学科差异和置信度校准。

来源：[1][2][3]

### 为何需要这个基准

MMLU等广域测试缺少天文学研究知识深度，而且通用平均分不能反映学科内模型差异及成本效率；本测试重点是天文知识召回与跨子领域联系，不是端到端原创研究能力。

来源：[2][4]

## 4. 构建方式

### 材料来源

从 Annual Review of Astronomy and Astrophysics 文章整理多项选择题。

来源：[1][2][3]

### 命题/编制背景

ARAA受邀综述提供领域专家知识；Gemini-1.5-Pro生成题目与解释，AstroMLab研究者设计提示并由人类专家抽查子集。综述作者不等于逐题命题者。

来源：[2]

### 审核流程

Gemini-1.5-Pro从885篇ARAA综述每篇生成5题，附说明与证据段；人类专家只审核了子集，不是全量专家逐题原创。

来源：[6]

### 质量控制

原论文要求题目可脱离原文独立作答、答案不引用特定段落、四选项长度相近，附解释与支持段落；专家抽查。AstroMLab-4又用Claude-3.5-Sonnet清理依赖论文特定数值/方法的题，修订不必要引用，形成3846题。

来源：[2][4]

### 去污染与证据边界

公开题目故意省略答案键以抑制直接答案训练；AstroSage作者报告从其训练语料中排除了ARAA来源文章。这是该模型训练控制，不能推广为所有参测模型无污染，亦不能排除题目和来源知识的间接暴露。

来源：[3][4]

## 5. 数据形式

### 规模与分母

original_internal_experiment：4425；public_cleaned_questions：3846；reason：AstroMLab-4 §4.1明确说明Claude-3.5-Sonnet清理删除依赖特定文章内容的题并修订引用；HF卡train元数据3846行。

来源：[2][4][3]

### 题型

四选一文本问答；公开清理集3846题，不含正确答案键。论文旧4425题不得作为公开版分母。

来源：[3][4]

### 模态与字段

纯文本题干及A/B/C/D四个字符串选项；公开卡没有图像字段。

来源：[3]

### 语言

英文

来源：[3]

### 难度定位

原论文定位博士级天文领域知识；后续AstroMLab-4明确指出主要测试知识召回，推理模式未普遍提升分数。不能把高分解释为自主天文研究成功率。

来源：[2][4]

### 公开、隐藏与划分

HF名为train的split只公开题干与A/B/C/D选项，故意不含正确答案；它不等于供监督训练的完整标注集。提交预测至官方邮箱取得评测分数。

来源：[3]

## 6. 评测方法

### 指标

选择题准确率与置信度校准分析。

来源：[1][2][3]

### 评分流程

原始论文先正则抽取JSON答案，失败时以GPT-4o解析；拒答题按模型单独剔除，强模型最多影响0.2%（10/4425），因此并非所有模型严格固定相同分母。后续清理版另按3846题评测，应单列。

来源：[2][4]

### 运行与提示

原论文使用Instruct/Chat模型，请求答案和解释（CoT）及JSON，通常沿厂商/HF默认参数；不使用RAG。后续清理版用简短天文专家system prompt，模型支持显式reasoning时开启。

来源：[2][4]

### 评测实现

待核实

来源：[1][2][3]

状态：待核实（本字段尚有未能确认的部分）。

### 不能混比的设置

原始4425题与清理3846题不可混排；原论文逐模型排除拒答，分母有细微差异。HF组织卡2025-05表是旧快照，不能覆盖2026-02修订AstroMLab-4表1。其正文称Gemini3Flash唯一超过AstroSage，但表1 GPT-5.2=89.4也超过89.0，本页以数值表为准并保留文本矛盾。

来源：[2][4][5]

## 7. 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8；本轮采集日，不是实验日）

来源：[1]

### 当前发布

本轮打开HF公开Astrobench_MCQ_v1_Public，3846题；2026-02修订AstroMLab-4使用同一清理版，不把模型论文版本当作新数据版本。

来源：[3][7]

### 版本脉络

original_paper：v1：2024-07-16T03:28:14+08:00；v2：2024-11-09T06:00:26+08:00；later_evaluation_paper：url：https://arxiv.org/abs/2505.17592；v1：2025-05-23T15:58:50+08:00；v2：2026-02-20T07:28:22+08:00

来源：[1][7]

### 分数上限与饱和度

2026-02 AstroMLab-4表1最高Gemini 3.0 Flash 90.3%（3846题）；仍有错误，不据此宣布本轮2026-11全球实时SOTA或完全饱和。

来源：[4]

### 争议与局限

公开集不提供答案以减少污染；论文同时承认LLM合成题可能含历史过时结论或表述含糊；不能据隐藏答案推断训练无污染。

来源：[6]

### 衍生版本

HF组织还列Astrobench_MCQ_v1_Chinese_Public（中文公开版）；AstroSage为受测模型家族，不另计为独立benchmark。

来源：[5]

## 8. 榜单快照

### 采集日期

2026-11-07（Asia/Shanghai，UTC+8；本轮采集日，不是实验日）

来源：[1]

### 官方入口

https://arxiv.org/pdf/2505.17592

来源：[7]

说明：官方作者后续论文表1；不是实时交互式排名。

### 第三方/补充实验

待核实

来源：[1][2][3]

说明：本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### AstroMLab-4 v2表1：3846题清理版

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Gemini 3.0 Flash | 90.3 | accuracy (%) |
| 2 | GPT-5.2 | 89.4 | accuracy (%) |
| 3 | AstroSage-Llama-3.1-70B | 89.0 | accuracy (%) |
| 3 | Claude 4.5 Opus | 89.0 | accuracy (%) |
| 5 | Gemini 3.0 Pro | 88.9 | accuracy (%) |

- Gemini 3.0 Flash：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20（Asia/Shanghai；论文修订日，不是逐模型运行日）；source_type：官方作者论文历史实验
- GPT-5.2：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20（Asia/Shanghai；论文修订日，不是逐模型运行日）；source_type：官方作者论文历史实验
- AstroSage-Llama-3.1-70B：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20（Asia/Shanghai；论文修订日，不是逐模型运行日）；source_type：官方作者论文历史实验
- Claude 4.5 Opus：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20（Asia/Shanghai；论文修订日，不是逐模型运行日）；source_type：官方作者论文历史实验
- Gemini 3.0 Pro：source_url：https://arxiv.org/pdf/2505.17592；accessed：2026-11-07；result_date：2026-02-20（Asia/Shanghai；论文修订日，不是逐模型运行日）；source_type：官方作者论文历史实验

#### AstroMLab-1 v2表1/2：4425题内部集（历史）

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Claude-3.5-Sonnet | 85.0 | accuracy (%) |
| 2 | Claude-3.0-Opus | 82.7 | accuracy (%) |
| 3 | LLaMA-3-70B | 80.6 | accuracy (%) |
| 4 | GPT-4o | 80.4 | accuracy (%) |

- Claude-3.5-Sonnet：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：原始论文历史实验
- Claude-3.0-Opus：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：原始论文历史实验
- LLaMA-3-70B：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：原始论文历史实验
- GPT-4o：source_url：https://arxiv.org/pdf/2407.11194；accessed：2026-11-07；source_type：原始论文历史实验

来源：[4][2]

### 覆盖边界

本轮优先转录2026-02-20（Asia/Shanghai）修订AstroMLab-4表1，并保留原始2024内部集作为独立历史轨。119模型是该论文覆盖数，不是2026-11已评119个最新模型；HF组织卡旧分数不与新版表混排。

来源：[7][4][5]

## 9. 联系方式

### 公开作者工作邮箱

astromachinelearninglab@gmail.com

来源：[3]

### 公开反馈

待核实

来源：[1][2][3]

说明：本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 官方账号

待核实

来源：[1][2][3]

说明：本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 隐私信息

只使用论文、官方站点或仓库公开联系方式；不收集私人渠道。

来源：[8]

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2407.11194

来源：[1][2]

### 下载源文件SHA-256

b31348a943177637d2e96d698974d5566a42a33f06e7c4a5772f2104984e074e

来源：[2]

说明：本轮实际下载的源站PDF字节校验；未声称重新核验Drive文件内容。

### 下载源文件字节数

10805582

来源：[2]

### 既有Drive文件夹

id：1p8tI1PveNY31y8XjJOUOm50eOVJ9jC8L；webViewLink：https://drive.google.com/drive/folders/1p8tI1PveNY31y8XjJOUOm50eOVJ9jC8L

来源：[9]

### 其他材料

- kind：中文介绍 Google Doc；id：1ldfA5JQ_ErScdlGU8UBROie6NcZv5by2prYp8QPKvv8；webViewLink：https://docs.google.com/document/d/1ldfA5JQ_ErScdlGU8UBROie6NcZv5by2prYp8QPKvv8/edit?usp=drivesdk

来源：[10]

### 既有Drive PDF链接

id：1OSiWWUsUV8xeWTAPzqbX2BhXycyVZzgT；webViewLink：https://drive.google.com/file/d/1OSiWWUsUV8xeWTAPzqbX2BhXycyVZzgT/view?usp=drivesdk

来源：[11]

> 本轮没有上传或改写Drive文件。以上SHA-256和字节数针对本轮实际下载的源站PDF，不等于重新核验既有Drive文件。

## 11. 变更记录

- 2026-11-07（Asia/Seoul）：首批官方材料核验、中文改写、PDF原件入Drive；未核实字段显式标记。
- 2026-11-07（Asia/Seoul）：第1轮深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- 2026-11-07（Asia/Shanghai (UTC+8)）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传Drive，未重跑评测。

来源：[1][2]

### 来源索引

[1]: https://arxiv.org/abs/2407.11194 "访问 2026-11-07"
[2]: https://arxiv.org/pdf/2407.11194 "访问 2026-11-07"
[3]: https://huggingface.co/datasets/AstroMLab/Astrobench_MCQ_v1_Public "访问 2026-11-07"
[4]: https://arxiv.org/pdf/2505.17592 "访问 2026-11-07"
[5]: https://huggingface.co/AstroMLab "访问 2026-11-07"
[6]: https://arxiv.org/html/2407.11194v2 "访问 2026-11-07"
[7]: https://arxiv.org/abs/2505.17592 "访问 2026-11-07"
[8]: urn:benchmark-atlas:constitution:v0.1 "访问 2026-11-07"
[9]: https://drive.google.com/drive/folders/1p8tI1PveNY31y8XjJOUOm50eOVJ9jC8L "访问 2026-11-07"
[10]: https://docs.google.com/document/d/1ldfA5JQ_ErScdlGU8UBROie6NcZv5by2prYp8QPKvv8/edit?usp=drivesdk "访问 2026-11-07"
[11]: https://drive.google.com/file/d/1OSiWWUsUV8xeWTAPzqbX2BhXycyVZzgT/view?usp=drivesdk "访问 2026-11-07"
