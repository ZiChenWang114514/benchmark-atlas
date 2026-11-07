# BIG-Bench Hard (BBH)｜中文深度介绍

核验日期：2026-11-07（Asia/Seoul）。事实按所列来源理解；未核实项不作推断。

测量组合逻辑、符号操作、算法执行和多步推理，以及显式思维链能否改善这些能力。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 一、基本信息

### 简称

BIG-Bench Hard (BBH)

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 全称

BIG-Bench Hard

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 数据/协议版本

2022 公开任务集；未固定本轮仓库 commit

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 发布日期

2022-10-18（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 板块

推理

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）。

### 子领域

- 多任务复杂推理

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 许可证

仓库LICENSE为MIT（Copyright 2022 suzgunmirac）；适用措辞为software/documentation，不将其自动扩大为BIG-Bench原始任务或论文的统一授权。

来源：[1](https://raw.githubusercontent.com/suzgunmirac/BIG-Bench-Hard/main/LICENSE)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/2210.09261

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 代码

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）。

### 数据集

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 官网

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 论文题名

Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

Google Research、Stanford University（论文署名机构）

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 正式合作方

待核实

核验说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 作者

- Suzgun, Mirac
- Scales, Nathan
- Schärli, Nathanael
- Gehrmann, Sebastian
- Tay, Yi
- Chung, Hyung Won
- Chowdhery, Aakanksha
- Le, Quoc V.
- Chi, Ed H.
- Zhou, Denny
- Wei, Jason

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 当前维护

待核实

核验说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 资助

待核实

核验说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

测量组合逻辑、符号操作、算法执行和多步推理，以及显式思维链能否改善这些能力。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 设计缺口

BIG-Bench 多任务平均值可能掩盖难题；本研究选择此前语言模型仍落后于人类的任务，单独测量推理瓶颈。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 四、构建方式

### 题源

从 BIG-Bench 的209个任务中，依题量、自动评分适用性和此前模型相对人类表现筛出23类任务；部分任务细分，形成27个评测子任务。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 出题/标注人员

继承 BIG-Bench 社区任务；BBH研究者负责筛选并手写每类任务的思维链演示。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 审核

以人类基线及此前模型结果进行筛选；不是重新由专家逐题原创一套试卷。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 质量控制

限制每子任务最多250道，避免大任务支配比较；多数250道，causal_judgement 187、penguins_in_a_table 146、snarks 178。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 去污染边界

论文含评测污染警示和识别措施；公开任务不能据此保证未来模型无训练污染。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 五、数据形式

### 题量

23类任务、27个子任务，共6511道评测题；统计口径为原论文所用BBH。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 题型

多项选择、布尔判断、短答案和字符串输出，随子任务变化。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 难度

按此前模型低于人类基线筛选，属于相对难度定义，不是统一年级或难度等级。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 公开/隐藏划分

公开评测题及每任务3个人工CoT示例；不应把示例计入评测题量。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 六、评测方法

### 指标

最终答案精确匹配准确率；同时按任务报告，不把所有题直接混合为唯一分数。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 评分实现

抽取最终答案后与目标答案比对，原论文比较直接回答与思维链提示。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 提示与预算

原论文3-shot示例，比较有无CoT，greedy / temperature 0；不同模型上下文与输出格式需另记。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 评测脚本

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 可比性警示

任务宏平均与全题微平均、23类与27子任务、直接回答与CoT不是同一口径。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 最新可确认数据/协议

2022 公开任务集；未固定本轮仓库 commit

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 修订与2026H2收录证据

- **论文版本**：arXiv v1
- **历史说明**：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。
- **2026下半年引用/使用证据**：
  - 
    - **来源链接**：https://arxiv.org/html/2609.27284v1
    - **日期**：2026-09-23
    - **说明**：Hunyuan-A13B §4.2 Reasoning及表3–4实际报告 BIG-Bench Hard (BBH)；厂商自报评测。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 饱和判断

待核实

核验说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

公开答案、演示与任务生成规则可能进入训练；模型自报分数不是独立去污染证明。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）；[2](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）。

### 衍生与排除项

BBH是BIG-Bench子集，不等于完整BIG-Bench；本库不把各子任务拆为额外benchmark。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）；[2](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 官方榜

待核实

核验说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 二级机构榜

待核实

核验说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 限定范围的分数快照

- 
  - **模型版本**：Hunyuan-A13B
  - **分数**：87.56
  - **单位**：%
  - **范围与协议**：基础模型，3-shot CoT，报告表2
  - **结果日期**：2026-09-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2609.27284v1
  - **来源等级**：三级：模型厂商自报
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：Qwen3-A22B
  - **分数**：88.87
  - **单位**：%
  - **范围与协议**：基础模型对照，报告表2
  - **结果日期**：2026-09-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2609.27284v1
  - **来源等级**：三级：模型厂商自报
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。

来源：[1](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

- msuzgun@cs.stanford.edu

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）；[2](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### Issues

https://github.com/suzgunmirac/BIG-Bench-Hard/issues

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）。

### 官方社交

待核实

核验说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### 隐私政策

待核实

核验说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

## 十、原始文件

### Drive论文PDF

- **id**：1nmUl5QNGTZKijqLcX6GXqLqwODkV0-GW
- **webViewLink**：https://drive.google.com/file/d/1nmUl5QNGTZKijqLcX6GXqLqwODkV0-GW/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1nmUl5QNGTZKijqLcX6GXqLqwODkV0-GW/view?usp=drivesdk)（采集 2026-11-07）。

### 原始论文PDF

https://arxiv.org/pdf/2210.09261

来源：[1](https://arxiv.org/abs/2210.09261)（采集 2026-11-07）。

### SHA256校验值

168f6fff020e9fde7563905f69e6a59d0648f195f48820d52c83c7adfaee18ec

来源：[1](https://arxiv.org/pdf/2210.09261)（采集 2026-11-07）。

### PDF字节数

5375941

来源：[1](https://arxiv.org/pdf/2210.09261)（采集 2026-11-07）。

### Drive文件夹

- **id**：1ISeb201NpVdzOdwUQ5IA9veSJL8smlBq
- **webViewLink**：https://drive.google.com/drive/folders/1ISeb201NpVdzOdwUQ5IA9veSJL8smlBq

来源：[1](https://drive.google.com/drive/folders/1ISeb201NpVdzOdwUQ5IA9veSJL8smlBq)（采集 2026-11-07）。

### 其他文档

- **chinese_intro_doc**：
  - **id**：1N0fQBJOZu3qwT8NX-UfZwCJuvdJnfJzP3HGJtXaKrqs
  - **webViewLink**：https://docs.google.com/document/d/1N0fQBJOZu3qwT8NX-UfZwCJuvdJnfJzP3HGJtXaKrqs/edit?usp=drivesdk
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/bbh.md

来源：[1](https://drive.google.com/drive/folders/1ISeb201NpVdzOdwUQ5IA9veSJL8smlBq)（采集 2026-11-07）。

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
    - basic_info.license

来源：[1](https://github.com/suzgunmirac/BIG-Bench-Hard)（采集 2026-11-07）。
