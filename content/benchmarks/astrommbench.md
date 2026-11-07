# AstroMMBench

> 第1轮实证核查 · 2026-11-07（KST）。正文与权威 JSON 同步；访问时间不是来源发表时间。未知保留，不以旧论文结果冒充最新总榜。

## 1. 基本信息

- **名称**：AstroMMBench （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **全称**：AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **版本**：2026正式期刊版（592题） （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **论文版本**：Universe 12(10),296，2026-09-30正式版 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **发布日期**：2026-09-30（正式发表）；2026-07-13 收稿、2026-09-21 修订、2026-09-23 接受。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **板块**：地球与天文 编辑分类沿用入选清单；不代表该基准只测本板块。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **子领域**：天文研究图像多模态问答 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **许可**：数据及原始图像再利用须遵循各 arXiv 原文许可；不能把论文或代码许可直接套到全部592题图像。统一数据许可待核实。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **论文**：https://www.mdpi.com/2218-1997/12/10/296 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **代码**：https://github.com/Shijinghang/benchmark_pipeline （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **数据**：https://huggingface.co/datasets/sjh11/AstroMMBench （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **官方主页**：https://www.mdpi.com/2218-1997/12/10/296 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **论文标题**：AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 2. 发起与维护

- **发起机构**：中国科学院国家天文台、中国科学院大学、浙江实验室、天津大学作者团队；作者单位不等同于法律所有权。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **合作机构**：中国科学院大学、浙江实验室、天津大学（作者机构）。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **作者**：Jinghang Shi；Xiaoyu Tang；Yang Huang；Yuyang Li；Yanxia Zhang；Xiao Kong；Caizhan Yue；A-Li Luo （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **维护方**：Shijinghang/benchmark_pipeline与sjh11/AstroMMBench官方发布账号。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **资助方**：NSFC 12273076、12203077、12373110、12133001；国家重点研发计划2025YFA1614101；载人航天 CMS-CSST-2025-A06；河北自然科学基金A2024205020。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 3. 设计目标

- **能力目标**：读懂天文研究图表、仪器图、观测图像并回答专业物理问题。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **设计动机**：通用VQA不能覆盖天文图像约定与领域推理；与文本AstroLLM、跨模态表示学习互补。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 4. 构建方式

- **数据来源**：2024-01-01 至2024-07-31 的3592篇 arXiv astro-ph 论文，提取19,299个图文对；LLaMA3.3-70B-Instruct 整理文本，InternVL2.5-78B 生成四选一候选。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **评审背景**：15名国家天文台评审：8名天文学博士生、5名硕士生、2名教授；按研究方向分配问题。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **审核流程**：五个纯文本 LLM 各答5次，单模型至少3次答对判为会答；至少两个模型会答则丢弃。余9677题抽1800题专家审核，保留592题。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **质量控制**：专家检查科学正确性、图题对应、上下文充分性、答案唯一性与干扰项；每题一名主审且可见答案和图注，无独立双评及一致性统计。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **去污染**：记录来源 arXiv ID，但未进行训练语料审计、近重复搜索或记忆探测；不能排除2024年后模型见过来源论文。不得描述为无污染。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 5. 数据形式

- **规模**：592四选一题：GA97、CO108、EP97、HE101、IM83、SR106；25个MLLM（22开放、3闭源）。旧621题摘要不能与正式版混用。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **任务形式**：图像+问题+四选项，单个正确答案。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **模态**：天文科研图、图表与文本；不是原始FITS时序分析。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **语言**：英语。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **难度**：六子领域；宇宙学均分最低，高能领域模型间方差最大，不应一律称最难。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **公开与隐藏划分**：论文结果统一使用592题；公开数据地址已给出。论文没有在本次已读段落定义独立训练/验证划分，划分细节待核实。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 6. 评测方法

- **指标**：四选一准确率；总体分母固定592，子领域按各自题数计算。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **评分方式**：A—D 单字母先精确匹配；其他自由回答交 DeepSeek-V3 固定二元裁判。解析失败、非法输出或 API 失败计错，不从分母删除。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **提示设置**：VLMEvalKit 0.2；输入为图像、题干和四个带标签选项；具体文本及裁判提示见 Supplementary File S1。图像处理沿各模型 adapter，非统一固定分辨率。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **评测脚本**：https://github.com/Shijinghang/benchmark_pipeline （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **可比性提示**：有效图像输入尺寸并未全局统一；头部区间重叠，点估计不能当显著排名；需成对检验及重复运行。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 7. 最新情况

- **核查日期**：2026-11-07 Asia/Seoul （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **最新版本**：2026正式版592题；版本以此次正式论文口径为准。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **修订与2026H2证据**：2026H2 使用证据：2026-09-30 正式论文用592题评估25个MLLM（22开放、3闭源）。这是发起方原始使用，不冒称独立后续引用。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **饱和度**：本组最高点估计71.28%；论文认为未饱和。前三总体准确率的 Wilson 95% 区间重叠，不能把小差距解读为显著优劣。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **已知问题**：公开 arXiv 来源可能进入模型预训练；单主审、可见答案和图注、单机构评审团，以及缺少重复运行均限制分数解释。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **后继资源**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 8. 榜单快照

- **采集日期**：2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期） （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **官方榜单**：https://www.mdpi.com/2218-1997/12/10/296#table_body_display_universe-12-00296-t002 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **第三方榜单**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **结果**：正式论文表2固定版本结果：Ovis2-34B 71.28%，ChatGPT-4o 69.76%，Doubao-1.5-vision-pro 69.09%；总体592题。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **口径说明**：2026-11-07 采集2026-09-30论文表2，不是持续更新的实时榜。前三置信区间重叠；模型后续版本与 API 变更不在此快照。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 9. 联系方式

- **公开邮箱**：tangxiaoyu@zhejianglab.org；zyx@bao.ac.cn （[来源1](https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf)；访问：2026-11-07）

- **问题反馈**：https://github.com/Shijinghang/benchmark_pipeline/issues （[来源1](https://github.com/Shijinghang/benchmark_pipeline)；访问：2026-11-07）

- **官方社交**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **隐私原则**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 10. 原始文件

- **PDF来源**：https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **SHA256**：5098322dcf0f8cbccdc5682a22fa6a4565c73464ef54937174540916f5f05a0c （[来源1](https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf)；访问：2026-11-07）

- **PDF字节**：7134595 （[来源1](https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf)；访问：2026-11-07）

- **Drive文件夹**：id：1TSOgqfwkB-dttJyEkuJMzgZJidF3HFdh；webViewLink：https://drive.google.com/drive/folders/1TSOgqfwkB-dttJyEkuJMzgZJidF3HFdh （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

- **其他文档**：type：中文介绍 Google Doc；id：1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4；webViewLink：https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit （[来源1](https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit)；访问：2026-11-07）

- **Drive PDF**：id：1U3D15tfPy2AbJbYlOx0vxQP2neBx4yZO；webViewLink：https://drive.google.com/file/d/1U3D15tfPy2AbJbYlOx0vxQP2neBx4yZO/view （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）

## 11. 变更记录

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。 （[来源1](https://www.mdpi.com/2218-1997/12/10/296)；访问：2026-11-07）
