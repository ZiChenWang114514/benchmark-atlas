# DROP｜中文深度介绍

核验日期：2026-11-07（Asia/Seoul）。事实按所列来源理解；未核实项不作推断。

测量模型在段落证据上做加减、计数、比较、排序及抽取答案的能力。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 一、基本信息

### 简称

DROP

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 全称

Discrete Reasoning Over Paragraphs

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 数据/协议版本

2019 公开数据集；本轮未固定下载包版本

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）；[2](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 发布日期

2019-03-01（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 板块

推理

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）。

### 子领域

- 离散推理阅读理解

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 许可证

待核实

核验说明：数据、代码、论文和原题权利分开；尚未核实对应发布文件许可证

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/1903.00161

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 代码

https://github.com/allenai/allennlp-models

来源：[1](https://raw.githubusercontent.com/allenai/allennlp-reading-comprehension/master/README.md)（采集 2026-11-07）；[2](https://raw.githubusercontent.com/allenai/allennlp-models/main/allennlp_models/rc/tools/drop.py)（采集 2026-11-07）。

### 数据集

https://allennlp.org/drop

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）；[2](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 官网

https://allennlp.org/drop

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）；[2](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 论文题名

DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning Over Paragraphs

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

Allen Institute for AI、University of California Irvine、University of Washington、Peking University（论文署名）

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 正式合作方

待核实

核验说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 作者

- Dua, Dheeru
- Wang, Yizhong
- Dasigi, Pradeep
- Stanovsky, Gabriel
- Singh, Sameer
- Gardner, Matt

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 当前维护

待核实

核验说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 资助

待核实

核验说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

测量模型在段落证据上做加减、计数、比较、排序及抽取答案的能力。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 设计缺口

仅靠定位答案跨度的阅读理解不足以检验离散运算与多事实整合。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 四、构建方式

### 题源

从Wikipedia 2018年10月数据与体育、历史材料选择含数值段落，由众包人员编写能难倒BiDAF的问答。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 出题/标注人员

MTurk众包写题；作者团队设计对抗式收集和验证流程。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 审核

开发集与测试集额外收集两个参考答案，处理无效或含糊的问题。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 质量控制

按段落切分训练/开发/测试，避免同一段落跨集；论文称验证剔除约0.7%无效题。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 去污染边界

段落级隔离减少数据集内部泄漏，不是针对现代大模型预训练语料的无污染认证。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 五、数据形式

### 题量

96567题：训练77409、开发9536、测试9622；对应段落5565、582、588。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 题型

段落阅读短答案；答案可为数字、日期、单跨度或多跨度文本。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 难度

难点是证据选择与离散运算耦合；不是依学科年级分级。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 公开/隐藏划分

训练和开发集提供参考答案；论文测试集用于隐藏答案评测。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 六、评测方法

### 指标

Exact Match（EM）与面向数字/多跨度的F1。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 评分实现

官方脚本先规范化大小写、冠词、标点、空白及数值；EM比较规范化答案跨度，多跨度F1通过最优一对一匹配汇总，gold含数字时要求数字匹配；多个参考答案取最佳得分。

来源：[1](https://raw.githubusercontent.com/allenai/allennlp-models/main/allennlp_models/rc/tools/drop.py)（采集 2026-11-07）。

### 提示与预算

原论文为监督阅读理解系统；现代LLM few-shot/CoT、答案抽取和上下文截断需单列。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 评测脚本

https://raw.githubusercontent.com/allenai/allennlp-models/main/allennlp_models/rc/tools/drop.py

来源：[1](https://raw.githubusercontent.com/allenai/allennlp-models/main/allennlp_models/rc/tools/drop.py)（采集 2026-11-07）。

### 可比性警示

F1不是EM；公开开发集与隐藏测试集、不同数值归一化实现不能直接比较。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 最新可确认数据/协议

本轮未核实新的数据版本；原allennlp-reading-comprehension仓库明确弃用，模型迁至allennlp-models；不能将代码迁移当成数据更新。

来源：[1](https://raw.githubusercontent.com/allenai/allennlp-reading-comprehension/master/README.md)（采集 2026-11-07）。

### 修订与2026H2收录证据

- **论文版本**：arXiv v2
- **历史说明**：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。
- **2026下半年引用/使用证据**：
  - 
    - **来源链接**：https://arxiv.org/html/2609.27284v1
    - **日期**：2026-09-23
    - **说明**：Hunyuan-A13B §4.2 Reasoning及表3–4实际报告 DROP；厂商自报评测。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 饱和判断

待核实

核验说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

Wikipedia与公开问答长期可获得，无法由当前得分排除记忆效应。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://allennlp.org/drop)（采集 2026-11-07）。

### 衍生与排除项

现代LLM常以DROP F1汇报；不应将其当成普通选择题准确率。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://allennlp.org/drop)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 官方榜

https://allennlp.org/drop

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://allennlp.org/drop)（采集 2026-11-07）。

### 二级机构榜

待核实

核验说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 限定范围的分数快照

- 
  - **模型版本**：Hunyuan-A13B
  - **分数**：91.1
  - **单位**：%
  - **范围与协议**：slow thinking，F1，报告表3
  - **结果日期**：2026-09-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2609.27284v1
  - **来源等级**：三级：模型厂商自报
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：DeepSeek-R1-0120
  - **分数**：92.2
  - **单位**：%
  - **范围与协议**：同表F1，对照值由报告转录
  - **结果日期**：2026-09-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2609.27284v1
  - **来源等级**：三级：模型厂商自报
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。

来源：[1](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

- ddua@uci.edu

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）；[2](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### Issues

待核实

核验说明：未核实官方Issues入口

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 官方社交

待核实

核验说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### 隐私政策

待核实

核验说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

## 十、原始文件

### Drive论文PDF

- **id**：1sBEpQfkBHqnUWTYiQ2jnD5uGxIV0g08_
- **webViewLink**：https://drive.google.com/file/d/1sBEpQfkBHqnUWTYiQ2jnD5uGxIV0g08_/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1sBEpQfkBHqnUWTYiQ2jnD5uGxIV0g08_/view?usp=drivesdk)（采集 2026-11-07）。

### 原始论文PDF

https://arxiv.org/pdf/1903.00161

来源：[1](https://arxiv.org/abs/1903.00161)（采集 2026-11-07）。

### SHA256校验值

e5f409536a3b9b8b0fdb7f687be42bd990e34ff2cb5862b9c1b241c2d498c4e5

来源：[1](https://arxiv.org/pdf/1903.00161)（采集 2026-11-07）。

### PDF字节数

1989064

来源：[1](https://arxiv.org/pdf/1903.00161)（采集 2026-11-07）。

### Drive文件夹

- **id**：1PlCYG_zi6XpiJ2JXUf-rR2DDg0ATAKTc
- **webViewLink**：https://drive.google.com/drive/folders/1PlCYG_zi6XpiJ2JXUf-rR2DDg0ATAKTc

来源：[1](https://drive.google.com/drive/folders/1PlCYG_zi6XpiJ2JXUf-rR2DDg0ATAKTc)（采集 2026-11-07）。

### 其他文档

- **chinese_intro_doc**：
  - **id**：1M2N1ClM56C6ClfXOroYNlxaFR-oo1DCdkaqWCYiFp4w
  - **webViewLink**：https://docs.google.com/document/d/1M2N1ClM56C6ClfXOroYNlxaFR-oo1DCdkaqWCYiFp4w/edit?usp=drivesdk
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/drop.md

来源：[1](https://drive.google.com/drive/folders/1PlCYG_zi6XpiJ2JXUf-rR2DDg0ATAKTc)（采集 2026-11-07）。

## 十一、变更记录

- 
  - **日期**：2026-11-07
  - **时区**：Asia/Seoul
  - **变更内容**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 
  - **日期**：2026-11-07
  - **时区**：Asia/Seoul
  - **变更内容**：第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
  - **本轮更新字段**：
    - basic_info.code_url
    - evaluation.official_scripts
    - evaluation.scoring
    - latest_status.latest_dataset_version

来源：[1](https://allennlp.org/drop)（采集 2026-11-07）。
