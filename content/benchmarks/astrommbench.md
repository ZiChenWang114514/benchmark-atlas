# AstroMMBench

> 核查：2026-11-07（，UTC+8）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

AstroMMBench

来源：[1]

### 全称

AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy

来源：[1]

### 数据/软件版本

2026正式期刊版（592题）

来源：[1]

### 论文版本

arXiv v2（2025-10-22 01:29:47，）为621题预印本；Universe 12(10),296（2026-09-30）为592题正式版。

来源：[2][3]

### 发布日期

2025-09-29 17:02:30（，UTC+8；arXiv v1）；2026-09-30是Universe正式发表日，不是首次提出日。

来源：[2][3]

### 主板块

地球与天文

来源：[1]

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 学科标签

天文研究图像多模态问答

来源：[1]

### 许可证与范围

hf_card：README标记apache-2.0；preprint_promise：2025预印本Ethics Statement称计划CC-BY-4.0发布；journal_restriction：2026正式论文明确原始图文再利用服从各arXiv提交的许可

来源：[4][5][3]

说明：三个官方声明范围与时间不一致。不能用HF总标签抹掉原始图像权利；代码仓库没有找到README/LICENSE根文件，代码许可仍待核实。

状态：待核实（本字段尚有未能确认的部分）。

### 论文入口

https://www.mdpi.com/2218-1997/12/10/296

来源：[1]

### 论文标题

AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy

来源：[1]

### 官方代码

https://github.com/Shijinghang/benchmark_pipeline

来源：[1]

### 数据入口

https://huggingface.co/datasets/sjh11/AstroMMBench

来源：[1]

### 官方主页

https://www.mdpi.com/2218-1997/12/10/296

来源：[1]

## 2. 发起与维护

### 发起团队

中国科学院国家天文台、中国科学院大学、浙江实验室、天津大学作者团队；作者单位不等同于法律所有权。

来源：[1]

### 署名/合作机构

中国科学院大学、浙江实验室、天津大学（作者机构）。

来源：[1]

### 作者

Jinghang Shi；Xiaoyu Tang；Yang Huang；Yuyang Li；Yanxia Zhang；Xiao Kong；Caizhan Yue；A-Li Luo

来源：[1]

### 维护入口

Shijinghang/benchmark_pipeline与sjh11/AstroMMBench官方发布账号。

来源：[1]

### 资助与计算资源

NSFC 12273076、12203077、12373110、12133001；国家重点研发计划2025YFA1614101；载人航天 CMS-CSST-2025-A06；河北自然科学基金A2024205020。

来源：[1]

## 3. 设计目标

应同时保留2025年621题预印本和2026年592题正式版。正式版更明确讨论训练暴露、单主审和统计区间限制，分数变化首先是题集/协议变化，不能直接解释为模型进步。
来源：[1][1]

### 测量能力

读懂天文研究图表、仪器图、观测图像并回答专业物理问题。

来源：[1]

### 为何需要这个基准

通用VQA不能覆盖天文图像约定与领域推理；与文本AstroLLM、跨模态表示学习互补。

来源：[1]

## 4. 构建方式

### 材料来源

2024-01-01 至2024-07-31 的3592篇 arXiv astro-ph 论文，提取19,299个图文对；LLaMA3.3-70B-Instruct 整理文本，InternVL2.5-78B 生成四选一候选。

来源：[1]

### 命题/编制背景

15名国家天文台评审：8名天文学博士生、5名硕士生、2名教授；按研究方向分配问题。

来源：[1]

### 审核流程

五个纯文本 LLM 各答5次，单模型至少3次答对判为会答；至少两个模型会答则丢弃。余9677题抽1800题专家审核，保留592题。

来源：[1]

### 质量控制

专家检查科学正确性、图题对应、上下文充分性、答案唯一性与干扰项；每题一名主审且可见答案和图注，无独立双评及一致性统计。

来源：[1]

### 去污染与证据边界

记录来源 arXiv ID，但未进行训练语料审计、近重复搜索或记忆探测；不能排除2024年后模型见过来源论文。不得描述为无污染。

来源：[1]

## 5. 数据形式

### 规模与分母

592四选一题：GA97、CO108、EP97、HE101、IM83、SR106；25个MLLM（22开放、3闭源）。旧621题摘要不能与正式版混用。

来源：[1]

### 题型

图像+问题+四选项，单个正确答案。

来源：[1]

### 模态与字段

天文科研图、图表与文本；不是原始FITS时序分析。

来源：[1]

### 语言

英语。

来源：[1]

### 难度定位

六子领域；宇宙学均分最低，高能领域模型间方差最大，不应一律称最难。

来源：[1]

### 公开、隐藏与划分

HF卡明确最终592题；论文为所有模型固定同一592题。与早期arXiv621题版本不同；独立训练/验证/测试命名及答案隐藏策略仍待核实。

来源：[4][3]

状态：待核实（本字段尚有未能确认的部分）。

## 6. 评测方法

### 指标

四选一准确率；总体分母固定592，子领域按各自题数计算。

来源：[1]

### 评分流程

A—D 单字母先精确匹配；其他自由回答交 DeepSeek-V3 固定二元裁判。解析失败、非法输出或 API 失败计错，不从分母删除。

来源：[1]

### 运行与提示

VLMEvalKit 0.2；输入为图像、题干和四个带标签选项；具体文本及裁判提示见 Supplementary File S1。图像处理沿各模型 adapter，非统一固定分辨率。

来源：[1]

### 评测实现

https://github.com/Shijinghang/benchmark_pipeline

来源：[1]

### 不能混比的设置

有效图像输入尺寸并未全局统一；头部区间重叠，点估计不能当显著排名；需成对检验及重复运行。

来源：[1]

## 7. 最新情况

### 核查日期

2026-11-07（，UTC+8；采集日，不是实验日）

来源：[1]

### 当前发布

2026正式版592题；版本以此次正式论文口径为准。

来源：[1]

### 版本脉络

arxiv_v1：2025-09-29；arxiv_v2：2025-10-22；preprint_questions：621；journal_publication：2026-09-30；journal_questions：592；version_boundary：题量、作者表和分数随正式版本变化；不是简单保留同一分母重命名。

来源：[2][3]

### 分数上限与饱和度

本组最高点估计71.28%；论文认为未饱和。前三总体准确率的 Wilson 95% 区间重叠，不能把小差距解读为显著优劣。

来源：[1]

### 争议与局限

公开 arXiv 来源可能进入模型预训练；单主审、可见答案和图注、单机构评审团，以及缺少重复运行均限制分数解释。

来源：[1]

### 衍生版本

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 8. 榜单快照

### 采集日期

2026-11-07（，UTC+8；采集日，不是实验日）

来源：[1]

### 官方入口

https://www.mdpi.com/2218-1997/12/10/296#table_body_display_universe-12-00296-t002

来源：[1]

### 第三方/补充实验

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### 2026 Universe表2：592题正式版

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Ovis2-34B | 71.28 | accuracy (%) |
| 2 | ChatGPT-4o | 69.76 | accuracy (%) |
| 3 | Doubao-1.5-vision-pro | 69.09 | accuracy (%) |
| 4 | InternVL3-38B | 68.24 | accuracy (%) |
| 4 | Qwen2.5-VL-72B | 68.24 | accuracy (%) |

- Ovis2-34B：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：官方原论文固定实验；dataset_size：592
- ChatGPT-4o：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：官方原论文固定实验；dataset_size：592
- Doubao-1.5-vision-pro：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：官方原论文固定实验；dataset_size：592
- InternVL3-38B：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：官方原论文固定实验；dataset_size：592
- Qwen2.5-VL-72B：source_url：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf；accessed：2026-11-07；source_type：官方原论文固定实验；dataset_size：592

#### 2025 arXiv v2表1：621题历史版

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Ovis2-34B | 70.53 | accuracy (%) |
| 2 | ChatGPT-4o | 69.07 | accuracy (%) |
| 3 | Doubao-1.5-vision-pro | 68.12 | accuracy (%) |

- Ovis2-34B：source_url：https://arxiv.org/pdf/2510.00063v2；accessed：2026-11-07；source_type：官方预印本历史实验；dataset_size：621
- ChatGPT-4o：source_url：https://arxiv.org/pdf/2510.00063v2；accessed：2026-11-07；source_type：官方预印本历史实验；dataset_size：621
- Doubao-1.5-vision-pro：source_url：https://arxiv.org/pdf/2510.00063v2；accessed：2026-11-07；source_type：官方预印本历史实验；dataset_size：621

来源：[3][5]

### 覆盖边界

正式592题与历史621题分轨，保留精确表值；OpenCompass列为通用多模态对照而非AstroMMBench第三方复跑分数。根目录README/LICENSE请求404、期刊HTML403；正式PDF、HF卡和原始arXiv全文均实际读取。

来源：[3][5][4]

## 9. 联系方式

### 公开作者工作邮箱

tangxiaoyu@zhejianglab.org；zyx@bao.ac.cn

来源：[3]

### 公开反馈

https://github.com/Shijinghang/benchmark_pipeline/issues

来源：[6]

### 官方账号

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 隐私信息

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 10. 原始文件

### 原文PDF

https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf

来源：[1]

### 下载源文件SHA-256

5098322dcf0f8cbccdc5682a22fa6a4565c73464ef54937174540916f5f05a0c

来源：[3]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

7134595

来源：[3]

### 既有文件夹

id：1TSOgqfwkB-dttJyEkuJMzgZJidF3HFdh；webViewLink：

来源：[1]

### 其他材料

- type：中文介绍 Google Doc；id：1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4；webViewLink：https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit

来源：[7]

### 既有 PDF链接

id：1U3D15tfPy2AbJbYlOx0vxQP2neBx4yZO；webViewLink：

来源：[1]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。
- 2026-11-07（ (UTC+8)）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[1]

### 来源索引

[1]: https://www.mdpi.com/2218-1997/12/10/296 "访问 2026-11-07"
[2]: https://arxiv.org/abs/2510.00063 "访问 2026-11-07"
[3]: https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf "访问 2026-11-07"
[4]: https://huggingface.co/datasets/sjh11/AstroMMBench "访问 2026-11-07"
[5]: https://arxiv.org/pdf/2510.00063v2 "访问 2026-11-07"
[6]: https://github.com/Shijinghang/benchmark_pipeline "访问 2026-11-07"
[7]: https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit "访问 2026-11-07"
