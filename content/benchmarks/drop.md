# DROP

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

深度条目；显式待核实项保留

DROP（Discrete Reasoning Over Paragraphs）是数值与离散推理阅读理解数据集：模型在Wikipedia段落中找证据，完成计数、加减、比较及多跨度回答，而非仅抽取连续文本。原论文96567题，按段落分为77409训练、9536开发、9622隐藏测试，避免同一段落跨集。 [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) [4](https://registry.opendata.aws/allenai-drop/)

实际重读论文、官方评分脚本、历史仓库迁移说明、HF卡和AWS登记。数据镜像计数与许可口径存在差异；官方隐藏测试榜当前返回错误，不能据搜索缓存声称取得实时SOTA。为避免把厂商自报结果混入官方榜，下面明确回退到原论文历史基线，并标注非当前排名。 [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) [4](https://registry.opendata.aws/allenai-drop/)

## 基本信息

- **简称**：DROP [2](https://arxiv.org/abs/1903.00161)

- **全称**：Discrete Reasoning Over Paragraphs [2](https://arxiv.org/abs/1903.00161)

- **基准版本**：2019 公开数据集；未固定下载包版本 [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161)

- **论文/报告版本**：arXiv v2 [2](https://arxiv.org/abs/1903.00161)

- **发布日期**：2019-03-01（arXiv初稿日期，非独立数据集首发声明） [2](https://arxiv.org/abs/1903.00161)

- **主板块**：推理 [1](https://allennlp.org/drop)

- **子领域**：离散推理阅读理解 [2](https://arxiv.org/abs/1903.00161)

- **许可证与限制**：评测软件allennlp-models为Apache-2.0；HF ucinlp/drop镜像标CC BY-SA 4.0，AWS官方开放数据登记仅写CC BY。数据许可存在口径差异，不能将软件Apache许可套用到数据。 [5](https://github.com/allenai/allennlp-models/blob/main/LICENSE) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) [4](https://registry.opendata.aws/allenai-drop/)

- **论文/报告**：https://arxiv.org/abs/1903.00161 [2](https://arxiv.org/abs/1903.00161)

- **官方代码**：https://github.com/allenai/allennlp-models [6](https://raw.githubusercontent.com/allenai/allennlp-reading-comprehension/master/README.md) [7](https://raw.githubusercontent.com/allenai/allennlp-models/main/allennlp_models/rc/tools/drop.py)

- **数据入口**：https://huggingface.co/datasets/ucinlp/drop [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md) 注：修正allennlp.org/drop已跳到旧评分脚本，不能再充当数据下载页。

- **官方主页**：https://allennlp.org/drop [1](https://allennlp.org/drop) [2](https://arxiv.org/abs/1903.00161)

- **报告标题**：DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs [2](https://arxiv.org/abs/1903.00161)

## 发起与维护

- **发起方**：Allen Institute for AI、University of California Irvine、University of Washington、Peking University（论文署名） [2](https://arxiv.org/abs/1903.00161)

- **合作方**：University of California, Irvine；Peking University；University of Washington [2](https://arxiv.org/abs/1903.00161)

- **核心作者**：Dua, Dheeru；Wang, Yizhong；Dasigi, Pradeep；Stanovsky, Gabriel；Singh, Sameer；Gardner, Matt [2](https://arxiv.org/abs/1903.00161)

- **维护方**：Allen Institute for Artificial Intelligence / AllenNLP团队（原论文和发布渠道）；当前持续维护情况未作保证。 [2](https://arxiv.org/abs/1903.00161) [8](https://github.com/allenai/allennlp-reading-comprehension)

- **资助方**：Google Cloud为beaker.org计算提供部分credits（论文致谢）；不据此推定全部项目资助。 [2](https://arxiv.org/abs/1903.00161)

## 设计目标

- **核心能力**：测量模型在段落证据上做加减、计数、比较、排序及抽取答案的能力。 [2](https://arxiv.org/abs/1903.00161)

- **相对已有评测的缺口**：仅靠定位答案跨度的阅读理解不足以检验离散运算与多事实整合。 [2](https://arxiv.org/abs/1903.00161)

## 构建方式

- **题目来源**：2018年10月Wikipedia dump及在线Wikipedia；优先NFL比赛总结、历史及含至少20个数字的段落，抽取约7000段；MTurk人工提问，在线BiDAF答不出才可提交。 [2](https://arxiv.org/abs/1903.00161)

- **出题与审核人员**：MTurk众包写题；作者团队设计对抗式收集和验证流程。 [2](https://arxiv.org/abs/1903.00161)

- **审核流程**：开发/测试每题至少追加两份人工答案，标记并过滤0.7%无效问题；总体Cohen κ=0.74（数字0.81、跨度0.62、日期0.65）。 [2](https://arxiv.org/abs/1903.00161)

- **质量控制**：按段落切分训练/开发/测试，避免同一段落跨集；论文称验证剔除约0.7%无效题。 [2](https://arxiv.org/abs/1903.00161)

- **防污染/运行完整性**：段落级隔离减少数据集内部泄漏，不是针对现代大模型预训练语料的无污染认证。 [2](https://arxiv.org/abs/1903.00161)

## 数据形式

- **规模**：论文原版96567题：train 77409、dev 9536、hidden test 9622。HF元数据则为77400/9535，卡片正文仍列77409/9536；必须注明具体打包版本。 [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md)

- **题型**：段落阅读短答案；答案可为数字、日期、单跨度或多跨度文本。 [2](https://arxiv.org/abs/1903.00161)

- **模态**：文本（数学符号按文本表达）；并非原始图像视频识别任务 [2](https://arxiv.org/abs/1903.00161)

- **语言覆盖**：英语题面；形式化/数学符号另见模态与仓库格式 [2](https://arxiv.org/abs/1903.00161)

- **难度与任务跨度**：难点是证据选择与离散运算耦合；不是依学科年级分级。 [2](https://arxiv.org/abs/1903.00161)

- **公开与隐藏划分**：按段落随机80/10/10划分，避免同一段落跨split；原隐藏测试9622题，HF镜像仅train与validation。 [2](https://arxiv.org/abs/1903.00161) [3](https://huggingface.co/datasets/ucinlp/drop/blob/main/README.md)

## 评测方法

- **指标**：Exact Match（EM）与面向数字/多跨度的F1。 [2](https://arxiv.org/abs/1903.00161)

- **评分规则**：归一化EM和数值敏感macro F1；数字不匹配时相关配对不给F1，多跨度对齐后平均，多份gold取最高值。论文称greedy对齐，但当前官方drop_eval.py使用linear_sum_assignment最优匹配，应锁定脚本版本。 [2](https://arxiv.org/abs/1903.00161) [1](https://allennlp.org/drop)

- **提示与运行配置**：原论文为监督阅读理解系统；现代LLM few-shot/CoT、答案抽取和上下文截断需单列。 [2](https://arxiv.org/abs/1903.00161)

- **评分/运行脚本**：https://github.com/allenai/allennlp-reading-comprehension/blob/master/allennlp_rc/eval/drop_eval.py [1](https://allennlp.org/drop)

- **可比性限制**：F1不是EM；公开开发集与隐藏测试集、不同数值归一化实现不能直接比较。 [2](https://arxiv.org/abs/1903.00161) [9](https://arxiv.org/html/2609.27284v1)

## 最新情况

- **核验日期**：2026-11-07 [1](https://allennlp.org/drop) [9](https://arxiv.org/html/2609.27284v1)

- **现行版本与采用证据**：未核实新的数据版本；原allennlp-reading-comprehension仓库明确弃用，模型迁至allennlp-models；不能将代码迁移当成数据更新。 [6](https://raw.githubusercontent.com/allenai/allennlp-reading-comprehension/master/README.md)

- **更新与修订**：arxiv_version：arXiv v2；history_note：完整历史请见arXiv元数据；初稿日期已转，不将论文修订日混为数据版本。；2026_h2_evidence：url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.2 Reasoning及表3–4实际报告 DROP；厂商自报评测。 [2](https://arxiv.org/abs/1903.00161) [9](https://arxiv.org/html/2609.27284v1)

- **已知问题与证据边界**：Wikipedia与公开问答长期可获得，无法由当前得分排除记忆效应。 [2](https://arxiv.org/abs/1903.00161) [1](https://allennlp.org/drop)

- **关联与衍生关系**：现代LLM常以DROP F1汇报；不应将其当成普通选择题准确率。 [2](https://arxiv.org/abs/1903.00161) [1](https://allennlp.org/drop)

**仍待核实**（不推断为未公开）：

- 饱和度判断：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断 [2](https://arxiv.org/abs/1903.00161) [9](https://arxiv.org/html/2609.27284v1)

## 榜单快照

- **快照采集日**：2026-11-07 （材料采集日；结果为2019论文历史实验） [2](https://arxiv.org/abs/1903.00161)

- **官方榜/正式委托榜**：https://leaderboard.allenai.org/drop/submissions/public [2](https://arxiv.org/abs/1903.00161) 注：官方榜WebFetch返回500，公开网页curl又遇TLS错误；搜索索引可见历史表，不冒充实时成功读取。

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | NAQANet (Complete Model) | 47.01 | 原论文test F1 (%)；运行/发布日见覆盖说明；[2](https://arxiv.org/abs/1903.00161) |
| 2 | BERT | 32.7 | 原论文test F1 (%)；运行/发布日见覆盖说明；[2](https://arxiv.org/abs/1903.00161) |
| 参考非模型名次 | Expert human | 96.42 | 作者作答560道test题的人工F1 (%)；运行/发布日见覆盖说明；[2](https://arxiv.org/abs/1903.00161) |

> NAQANet (Complete Model)：exact_match：44.07；result_type：2019论文历史基线，非当前排行榜 [2](https://arxiv.org/abs/1903.00161)

> BERT：exact_match：29.45；result_type：2019论文历史基线，非当前排行榜 [2](https://arxiv.org/abs/1903.00161)

> Expert human：exact_match：94.09；result_type：2019历史人工参考 [2](https://arxiv.org/abs/1903.00161)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：官方隐藏测试榜不可读（500/TLS）；未据搜索缓存宣称刷新实时名次。以下回退为已实际阅读原论文Table 4历史基线，明确非2026年最新SOTA；不同dev/test、prompt与训练协议不能混榜。 [2](https://arxiv.org/abs/1903.00161)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [2](https://arxiv.org/abs/1903.00161)

## 联系方式

- **公开联系邮箱**：info@allenai.org [4](https://registry.opendata.aws/allenai-drop/)

- **公开问题追踪**：https://github.com/allenai/allennlp-models/issues [8](https://github.com/allenai/allennlp-reading-comprehension)

**仍待核实**（不推断为未公开）：

- 官方社交：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [2](https://arxiv.org/abs/1903.00161)
- 隐私政策：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [2](https://arxiv.org/abs/1903.00161)

## 原始文件

- **原始PDF**：https://arxiv.org/pdf/1903.00161 [10](https://arxiv.org/pdf/1903.00161)

- **SHA-256**：e5f409536a3b9b8b0fdb7f687be42bd990e34ff2cb5862b9c1b241c2d498c4e5 [10](https://arxiv.org/pdf/1903.00161) 注：实际下载的PDF字节计算；不是外部网页抄录。

- **PDF字节数**：1989064 [10](https://arxiv.org/pdf/1903.00161) 注：下载字节数；未上传。

## 变更记录

- date：2026-11-07；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。；date：2026-11-07；change：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。；fields_updated：basic_info.code_url；evaluation.official_scripts；evaluation.scoring；latest_status.latest_dataset_version；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://allennlp.org/drop)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
