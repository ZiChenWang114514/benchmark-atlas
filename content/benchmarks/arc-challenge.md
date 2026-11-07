# ARC-Challenge

> 核查：2026-11-07（Asia/Shanghai，UTC+8）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

第2轮逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

ARC-Challenge

来源：[1]

### 全称

AI2 Reasoning Challenge — Challenge Set

来源：[1]

### 数据/软件版本

ARC-Challenge（2018）；不包含ARC-Easy

来源：[2][1]

### 论文版本

arXiv v1

来源：[1]

### 发布日期

2018-03-15 02:04:21（Asia/Shanghai，UTC+8；arXiv v1提交时刻；不是数据单独上线时刻）

来源：[1]

### 主板块

推理

来源：[2]

### 学科标签

科学常识与组合推理

来源：[1]

### 许可证与范围

dataset：CC-BY-SA-4.0（allenai/ai2_arc卡头标记；卡正文许可段仍为More Information Needed，保留冲突）；baseline_code：Apache-2.0（arc-solvers/LICENSE）

来源：[3][4]

### 论文入口

https://arxiv.org/abs/1803.05457

来源：[1]

### 论文标题

Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge

来源：[1]

### 官方代码

https://github.com/allenai/arc-solvers

来源：[2]

### 数据入口

https://huggingface.co/datasets/allenai/ai2_arc

来源：[3]

### 官方主页

http://data.allenai.org/arc

来源：[2][1]

## 2. 发起与维护

### 发起团队

Allen Institute for AI

来源：[1]

### 署名/合作机构

原论文所有作者的唯一署名单位为Allen Institute for Artificial Intelligence；本字段记录公开署名机构，不据此推断未列出的法律合作关系。

来源：[5]

### 作者

Clark, Peter；Cowhey, Isaac；Etzioni, Oren；Khot, Tushar；Sabharwal, Ashish；Schoenick, Carissa；Tafjord, Oyvind

来源：[1]

### 维护入口

AllenAI官方数据发布账号allenai与arc-solvers仓库；这是公开发布维护入口，不推断当前人员任命。

来源：[3][6]

### 资助与计算资源

待核实

来源：[1]

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

状态：待核实（本字段尚有未能确认的部分）。

## 3. 设计目标

它衡量的是自然科学考试选择题上的知识与组合推理，不是视觉ARC-AGI，也不是科研自动化。Challenge源于2018检索/PMI基线筛选，难度定义不随2026模型自动更新。
来源：[1][1]

### 测量能力

在基础科学考试题上测量超越检索与词语共现的知识整合和推理。

来源：[1]

### 为何需要这个基准

既有选择问答可能被信息检索或词汇统计解决，难以单独衡量更深推理。

来源：[1]

## 4. 构建方式

### 材料来源

收集3至9年级科学考试选择题；同时被检索和PMI基线答错的题进入Challenge。

来源：[1]

### 命题/编制背景

原始考试命题者与AI2整理团队；不是全部由LLM合成。

来源：[1]

### 审核流程

对题目清理并以两个基线筛选；不含必须依赖图像才能回答的问题。

来源：[1]

### 质量控制

保留多种科学学科和推理需求，原论文另给约1400万句科学语料供检索。

来源：[1]

### 去污染与证据边界

Easy/Challenge依据基线表现划分，不构成预训练语料隔离；考试题可能已在网络公开。

来源：[1]

## 5. 数据形式

### 规模与分母

ARC-Challenge：train 1119、validation 299、test 1172，共2590题；不得用全ARC的7787题或ARC-Easy混替。

来源：[7]

### 题型

文本科学选择题，多为4选项，部分3至5选项。

来源：[1]

### 模态与字段

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1]

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1]

### 难度定位

Challenge仅表示被原检索与PMI模型筛掉的集合；不是固定的2026前沿难度。

来源：[1]

### 公开、隐藏与划分

公开训练、开发和测试题文件；现代常用测试1172题。

来源：[1]

## 6. 评测方法

### 指标

答案准确率；原论文对并列预测允许1/k分数。

来源：[1]

### 评分流程

原始tie-credit与现代生成答案accuracy/对数似然acc_norm实现不同，必须保留评测器设置。

来源：[1]

### 运行与提示

原论文包含检索与监督QA系统；LLM需要报告shot数、CoT、是否检索及似然长度归一化。

来源：[1]

### 评测实现

官方arc-solvers提供scripts/evaluate_solver.sh与scripts/evaluate_bidaf.sh；为历史检索/蕴含/阅读理解基线，不是现代LLM统一提示协议。

来源：[6]

### 不能混比的设置

ARC-Challenge不是ARC-Easy、更不是视觉抽象推理ARC-AGI；1172题和合并3548题结果不可混排。

来源：[1][8]

## 7. 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8；本轮采集日，不是实验日）

来源：[1]

### 当前发布

ARC-Challenge（2018）；不包含ARC-Easy

来源：[2][1]

### 版本脉络

paper：v1；submitted_at：2018-03-15T02:04:21+08:00；later_use：report：https://arxiv.org/html/2610.11978v1；scope：ARC-Challenge；区别于ARC-Easy+Challenge合并3548题

来源：[1][8]

### 分数上限与饱和度

Jev报告表2在ARC-Challenge上列Jev 97.6%、Gemini 3.8 Flash 97.5%；所列协议的头部已接近满分，但这不是全面污染审计，也不是所有提示设置下的统一饱和结论。

来源：[8]

### 争议与局限

旧考试题和公开答案存在污染风险；高分不能自动证明系统具有广泛科学研究能力。

来源：[1][2]

### 衍生版本

同家族ARC-Easy单独划分；本条只收录Challenge，不重复计数。

来源：[1][2]

## 8. 榜单快照

### 采集日期

2026-11-07（Asia/Shanghai，UTC+8；本轮采集日，不是实验日）

来源：[1]

### 官方入口

http://data.allenai.org/arc

来源：[9][2]

### 第三方/补充实验

https://arxiv.org/html/2610.11978v1

来源：[8]

说明：论文实验对照，不是持续更新的独立第三方官方榜。

### 分轨成绩

#### Jev报告表2：Jev+六个前沿LLM，ARC-Challenge

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Jev | 97.6 | accuracy (%) |
| 2 | Gemini 3.8 Flash | 97.5 | accuracy (%) |
| 3 | Qwen3.8-Flash | 96.2 | accuracy (%) |
| 4 | DeepSeek-V4.1-Flash | 95.9 | accuracy (%) |
| 5 | GPT-5.6 Sol | 95.1 | accuracy (%) |
| 6 | Claude Opus 5.5 | 94.8 | accuracy (%) |
| 7 | Qwen3.8-Max | 91.4 | accuracy (%) |

- Jev：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排
- Gemini 3.8 Flash：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排
- Qwen3.8-Flash：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排
- DeepSeek-V4.1-Flash：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排
- GPT-5.6 Sol：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排
- Claude Opus 5.5：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排
- Qwen3.8-Max：source_url：https://arxiv.org/html/2610.11978v1；accessed：2026-11-07；source_type：研究报告实验；非AllenAI现榜；protocol：选项判定；具体模型提示见报告；不与其附录转引的异协议旧模型混排

#### 原始2018论文表6：Challenge test，1172题

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | DGEM | 27.11 | tie-credit accuracy (%) |
| 2 | TableILP | 26.97 | tie-credit accuracy (%) |
| 3 | BiDAF | 26.54 | tie-credit accuracy (%) |

- DGEM：source_url：https://arxiv.org/pdf/1803.05457；accessed：2026-11-07；source_type：原始论文历史基线
- TableILP：source_url：https://arxiv.org/pdf/1803.05457；accessed：2026-11-07；source_type：原始论文历史基线
- BiDAF：source_url：https://arxiv.org/pdf/1803.05457；accessed：2026-11-07；source_type：原始论文历史基线

来源：[8][5]

### 覆盖边界

分轨展示：Jev报告中的Jev+六前沿模型，与2018原始基线分开。官方旧站本轮未取得可读榜；不冒称2026 AllenAI官方前列。Jev表2另列代表模型，其中部分成绩为外部来源转引，未与本轮实测模型合并排序。

来源：[8][1]

## 9. 联系方式

### 公开作者工作邮箱

peterc@allenai.org；isaacc@allenai.org；orene@allenai.org；tushark@allenai.org；ashishs@allenai.org；carissas@allenai.org；oyvindt@allenai.org

来源：[5]

说明：原论文首页公开作者工作邮箱；属于2018历史联系方式，本轮不发信验证有效性。

### 公开反馈

https://github.com/allenai/arc-solvers/issues

来源：[9]

### 官方账号

待核实

来源：[1]

说明：未核实专门官方社交账号，不收录同名个人账户

状态：待核实（本字段尚有未能确认的部分）。

### 隐私信息

待核实

来源：[1]

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

状态：待核实（本字段尚有未能确认的部分）。

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/1803.05457

来源：[1]

### 下载源文件SHA-256

b24b722c93f304df6c3b4a48ebbe429e836f3b3e80837bb613112398e59bde43

来源：[5]

说明：本轮实际下载的源站PDF字节校验；未声称重新核验Drive文件内容。

### 下载源文件字节数

290564

来源：[5]

### 既有Drive文件夹

id：1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk；webViewLink：https://drive.google.com/drive/folders/1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk

来源：[10]

### 其他材料

chinese_intro_doc：id：1zeiTeYn28Vz7H0h4mPOEjzt7SDBGXmYdmKRcXs2_g24；webViewLink：https://docs.google.com/document/d/1zeiTeYn28Vz7H0h4mPOEjzt7SDBGXmYdmKRcXs2_g24/edit?usp=drivesdk；mimeType：application/vnd.google-apps.document；local_markdown：content/benchmarks/arc-challenge.md

来源：[10]

### 既有Drive PDF链接

id：1cz7sR0Bva9EQIZUhXIjebI5QWfMWtr6Q；webViewLink：https://drive.google.com/file/d/1cz7sR0Bva9EQIZUhXIjebI5QWfMWtr6Q/view?usp=drivesdk

来源：[11]

> 本轮没有上传或改写Drive文件。以上SHA-256和字节数针对本轮实际下载的源站PDF，不等于重新核验既有Drive文件。

## 11. 变更记录

- 2026-11-07（Asia/Seoul）：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07（Asia/Seoul）：第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
- 2026-11-07（Asia/Shanghai (UTC+8)）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传Drive，未重跑评测。

来源：[2]

### 来源索引

[1]: https://arxiv.org/abs/1803.05457 "访问 2026-11-07"
[2]: http://data.allenai.org/arc "访问 2026-11-07"
[3]: https://huggingface.co/datasets/allenai/ai2_arc "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/allenai/arc-solvers/master/LICENSE "访问 2026-11-07"
[5]: https://arxiv.org/pdf/1803.05457 "访问 2026-11-07"
[6]: https://raw.githubusercontent.com/allenai/arc-solvers/master/README.md "访问 2026-11-07"
[7]: https://huggingface.co/datasets/allenai/ai2_arc/raw/main/README.md "访问 2026-11-07"
[8]: https://arxiv.org/html/2610.11978v1 "访问 2026-11-07"
[9]: https://github.com/allenai/arc-solvers "访问 2026-11-07"
[10]: https://drive.google.com/drive/folders/1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk "访问 2026-11-07"
[11]: https://drive.google.com/file/d/1cz7sR0Bva9EQIZUhXIjebI5QWfMWtr6Q/view?usp=drivesdk "访问 2026-11-07"
