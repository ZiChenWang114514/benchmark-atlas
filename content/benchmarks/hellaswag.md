# HellaSwag｜中文深度介绍

核验日期：2026-11-07（Asia/Seoul）。事实按所列来源理解；未核实项不作推断。

衡量日常活动和操作说明中下一事件的常识合理性判断。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

## 一、基本信息

### 简称

HellaSwag

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 全称

HellaSwag: Can a Machine Really Finish Your Sentence?

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 数据/协议版本

2019数据集；官方测试榜于2024年11月停止接收提交

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 发布日期

2019-05-20（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 板块

推理

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

### 子领域

- 常识情景推理

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 许可证

HF的Rowan/hellaswag数据卡标MIT并链接原仓库LICENSE；本轮原LICENSE访问失败，保留此证据层级限制，未完成原许可证逐字核对。

来源：[1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/1905.07830

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 代码

https://github.com/rowanz/hellaswag

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

### 数据集

https://github.com/rowanz/hellaswag

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 官网

https://rowanzellers.com/hellaswag/

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 论文题名

HellaSwag: Can a Machine Really Finish Your Sentence?

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

University of Washington、Allen Institute for AI

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 正式合作方

待核实

核验说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 作者

- Zellers, Rowan
- Holtzman, Ari
- Bisk, Yonatan
- Farhadi, Ali
- Choi, Yejin

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 当前维护

待核实

核验说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 资助

待核实

核验说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

衡量日常活动和操作说明中下一事件的常识合理性判断。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 设计缺口

语言模型可能利用表面流畅度而不理解物理与事件常识；需要人类容易、模型困难的干扰项。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

## 四、构建方式

### 题源

ActivityNet视频字幕与WikiHow操作说明作为上下文和正确结尾，生成模型产生错误结尾。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 出题/标注人员

研究团队设计对抗过滤；众包人员判断候选结尾的合理性。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 审核

多轮判别器过滤模型生成负例，并以人工验证保留可区分样本。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 质量控制

对抗过滤迭代挑选不易被当时判别模型识别的错误答案；同时控制长度与语境。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 去污染边界

按活动类别设置in-domain与zero-shot类别；这不等于现代预训练污染审计。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

## 五、数据形式

### 题量

论文概述约70000题，ActivityNet约25000、WikiHow约45000；精确当前发布包题数待固定版本后复核。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 题型

给上下文和4个候选结尾，选择唯一合理的续写。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 难度

原论文人类95.6%与当时模型差距是历史背景，不能描述2026模型仍低于48%。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 公开/隐藏划分

HF卡列train 39905、validation 10042、test 10003；官网test榜与普遍采用的validation评测不是同一split。

来源：[1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md)（采集 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

## 六、评测方法

### 指标

4选1准确率；官方榜另分in-domain/zero-shot、ActivityNet/WikiHow。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 评分实现

选择标签与参考答案匹配；LLM的生成字母或对数似然实现需说明。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 提示与预算

官方历史榜GPT-4 base使用10-shot；当代生成/似然模板、长度归一化和shot数必须注明。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 评测脚本

https://github.com/rowanz/hellaswag

来源：[1](https://github.com/rowanz/hellaswag)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 可比性警示

停止更新的官方测试榜不等于当代验证集SOTA；不能把两个split混排。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 最新可确认数据/协议

官网声明自2024年11月关闭提交；当前可读的是历史test榜，不应称为2026年持续更新榜。

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

### 修订与2026H2收录证据

- **论文版本**：arXiv v1
- **历史说明**：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。
- **2026下半年引用/使用证据**：
  - 
    - **来源链接**：https://arxiv.org/html/2610.11978v1
    - **日期**：2026-10-08
    - **说明**：Jev 研究表1–2及§3.1实际在 HellaSwag 上比较多类模型，不将ARC-Easy或其它子集另计。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 饱和判断

待核实

核验说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[3](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

验证集普遍公开使用；对抗过滤是构建方式，不是防止未来训练污染的保证。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

### 衍生与排除项

继承SWAG方向但扩大干扰项难度；本条不把ActivityNet与WikiHow视作独立benchmark。

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 官方榜

https://rowanzellers.com/hellaswag/

来源：[1](https://github.com/rowanz/hellaswag)（采集 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

### 二级机构榜

待核实

核验说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 限定范围的分数快照

- 
  - **模型版本**：GPT4 base 10-shot
  - **分数**：95.3
  - **单位**：%
  - **范围与协议**：官方test历史榜overall accuracy；提交自2024年11月关闭，不与validation论文表混排。
  - **结果日期**：2023-03-08
  - **采集日期**：2026-11-07
  - **来源链接**：https://rowanzellers.com/hellaswag/
  - **来源等级**：一级：官方榜单
  - **检查点说明**：按来源展示名原样记录，未推断API checkpoint。
- 
  - **模型版本**：ALUM
  - **分数**：85.6
  - **单位**：%
  - **范围与协议**：官方test历史榜overall accuracy；提交自2024年11月关闭，不与validation论文表混排。
  - **结果日期**：2020-03-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://rowanzellers.com/hellaswag/
  - **来源等级**：一级：官方榜单
  - **检查点说明**：按来源展示名原样记录，未推断API checkpoint。
- 
  - **模型版本**：RoBERTa
  - **分数**：85.2
  - **单位**：%
  - **范围与协议**：官方test历史榜overall accuracy；提交自2024年11月关闭，不与validation论文表混排。
  - **结果日期**：2019-07-25
  - **采集日期**：2026-11-07
  - **来源链接**：https://rowanzellers.com/hellaswag/
  - **来源等级**：一级：官方榜单
  - **检查点说明**：按来源展示名原样记录，未推断API checkpoint。
- 
  - **模型版本**：GPT-4 base
  - **分数**：95.3
  - **单位**：%
  - **范围与协议**：官方历史测试榜，10-shot
  - **结果日期**：2023-03-08
  - **采集日期**：2026-11-07
  - **来源链接**：https://rowanzellers.com/hellaswag/
  - **来源等级**：一级：官方榜（可能为历史结果）
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：ALUM
  - **分数**：85.6
  - **单位**：%
  - **范围与协议**：官方历史测试榜
  - **结果日期**：2020-03-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://rowanzellers.com/hellaswag/
  - **来源等级**：一级：官方榜（可能为历史结果）
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：Gemini 3.8 Flash
  - **分数**：97.5
  - **单位**：%
  - **范围与协议**：Jev论文表2，作者测量；非官方测试榜
  - **结果日期**：2026-10-08
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2610.11978v1
  - **来源等级**：研究论文实验，非官方实时榜
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）；[3](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 覆盖边界

新增官方快照与既有论文/厂商结果分开解读，不能跨split/协议混排。榜单自身最后更新日期：待核实（榜关闭于2024-11；所列结果日依次2023-03-08、2020-03-23、2019-07-25）；2026-11-07仅为采集日期（Asia/Seoul）。

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

待核实

核验说明：未从已核实官方材料收录专门联系邮箱；不猜测个人邮箱

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### Issues

https://github.com/rowanz/hellaswag/issues

来源：[1](https://github.com/rowanz/hellaswag)（采集 2026-11-07）。

### 官方社交

待核实

核验说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### 隐私政策

待核实

核验说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

## 十、原始文件

### Drive论文PDF

- **id**：14I9LvyrpWsQfFnhlwJu0O_Ag-RrqKjNL
- **webViewLink**：https://drive.google.com/file/d/14I9LvyrpWsQfFnhlwJu0O_Ag-RrqKjNL/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/14I9LvyrpWsQfFnhlwJu0O_Ag-RrqKjNL/view?usp=drivesdk)（采集 2026-11-07）。

### 原始论文PDF

https://arxiv.org/pdf/1905.07830

来源：[1](https://arxiv.org/abs/1905.07830)（采集 2026-11-07）。

### SHA256校验值

9a042fdcc4a22848cffde37e9c5257e423443980172bab7367dffb4e779aac37

来源：[1](https://arxiv.org/pdf/1905.07830)（采集 2026-11-07）。

### PDF字节数

1192712

来源：[1](https://arxiv.org/pdf/1905.07830)（采集 2026-11-07）。

### Drive文件夹

- **id**：1XmPAIntfyK79BR_x3RMsy2mZCedenwBL
- **webViewLink**：https://drive.google.com/drive/folders/1XmPAIntfyK79BR_x3RMsy2mZCedenwBL

来源：[1](https://drive.google.com/drive/folders/1XmPAIntfyK79BR_x3RMsy2mZCedenwBL)（采集 2026-11-07）。

### 其他文档

- **chinese_intro_doc**：
  - **id**：1Ht_XIC4UXIKL0om0ZQTRcNfOJ4hDUFIchol5N807ACc
  - **webViewLink**：https://docs.google.com/document/d/1Ht_XIC4UXIKL0om0ZQTRcNfOJ4hDUFIchol5N807ACc/edit?usp=drivesdk
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/hellaswag.md

来源：[1](https://drive.google.com/drive/folders/1XmPAIntfyK79BR_x3RMsy2mZCedenwBL)（采集 2026-11-07）。

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
    - latest_status.latest_dataset_version
    - data_format.public_hidden_split
    - leaderboard.results
    - leaderboard.coverage_note

来源：[1](https://rowanzellers.com/hellaswag/)（采集 2026-11-07）。
