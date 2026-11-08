# HellaSwag

> Benchmark Constitution，核查日期：2026-11-07。未知仍保留待核实；访问日不冒充实验日。

HellaSwag由ActivityNet字幕和WikiHow说明构造四选一续写题，以生成负例及对抗过滤减少表面语言线索。官方test提交已在2024年11月关闭；当代常用validation成绩不能接在该历史榜上宣称同一赛道进步。

导读来源：[https://arxiv.org/abs/1905.07830](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）; [https://arxiv.org/html/2610.11978v1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

## 1. 基本信息

### 简称

HellaSwag

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 全称

HellaSwag: Can a Machine Really Finish Your Sentence?

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 数据/协议版本

2019数据集；官方测试榜于2024年11月停止接收提交

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 论文版本

v1；2019-05-20（论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 发布日期及口径

2019-05-20（arXiv初稿提交时间，非推定数据首发日）

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 主板块

推理

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 子领域

- 常识情景推理

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 许可证

HF的Rowan/hellaswag数据卡标MIT并链接原仓库LICENSE；原LICENSE访问失败，保留此证据层级限制，未完成原许可证逐字核对。

来源：[1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/1905.07830

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 代码入口

https://github.com/rowanz/hellaswag

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 数据入口

https://github.com/rowanz/hellaswag

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 官方主页

https://rowanzellers.com/hellaswag/

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 论文标题

HellaSwag: Can a Machine Really Finish Your Sentence?

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

## 2. 发起与维护

### 发起团队

University of Washington、Allen Institute for AI

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 合作及署名机构

待核实

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 作者

- Zellers, Rowan
- Holtzman, Ari
- Bisk, Yonatan
- Farhadi, Ali
- Choi, Yejin

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 维护方

官方页面由Rowan Zellers团队提供，明确自2024年11月关闭test榜提交；不据旧榜推断持续维护承诺。

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 资助

NSF Graduate Research Fellowship及研究资助、DARPA CwC（经ARO）、IARPA DIVA、Sloan Fellowship、Allen Institute for AI、NVIDIA AI Lab，及Google/Facebook赠款；Google Cloud TPU团队提供计算协助。

来源：[1](https://arxiv.org/pdf/1905.07830)（访问 2026-11-07）

## 3. 设计目标

### 评测能力

衡量日常活动和操作说明中下一事件的常识合理性判断。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 设计动机

语言模型可能利用表面流畅度而不理解物理与事件常识；需要人类容易、模型困难的干扰项。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

## 4. 构建方式

### 材料来源

ActivityNet视频字幕与WikiHow操作说明作为上下文和正确结尾，生成模型产生错误结尾。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 编制背景

研究团队设计对抗过滤；众包人员判断候选结尾的合理性。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 审核流程

多轮判别器过滤模型生成负例，并以人工验证保留可区分样本。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 质量控制

对抗过滤迭代挑选不易被当时判别模型识别的错误答案；同时控制长度与语境。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 去污染边界

按活动类别设置in-domain与zero-shot类别；这不等于现代预训练污染审计。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

## 5. 数据形式

### 规模

HF数据卡公开行数：train 39,905、validation 10,042、test 10,003，共59,950；论文约70,000的收集规模不能替代这个公开包精确计数。

来源：[1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/pdf/1905.07830)（访问 2026-11-07）

### 题型

给上下文和4个候选结尾，选择唯一合理的续写。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 模态

文本上下文及4个文本结尾；ActivityNet视频提供字幕题源，但公开标准任务不要求模型直接观看视频。

来源：[1](https://arxiv.org/pdf/1905.07830)（访问 2026-11-07）；[2](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md)（访问 2026-11-07）

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 难度

原论文人类95.6%与当时模型差距是历史背景，不能描述2026模型仍低于48%。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 公开及隐藏划分

HF卡列train 39905、validation 10042、test 10003；官网test榜与普遍采用的validation评测不是同一split。

来源：[1](https://huggingface.co/datasets/Rowan/hellaswag/raw/main/README.md)（访问 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

## 6. 评测方法

### 指标

4选1准确率；官方榜另分in-domain/zero-shot、ActivityNet/WikiHow。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 计分

选择标签与参考答案匹配；LLM的生成字母或对数似然实现需说明。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 提示与运行设置

官方历史榜GPT-4 base使用10-shot；当代生成/似然模板、长度归一化和shot数必须注明。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 评测入口

https://github.com/rowanz/hellaswag

来源：[1](https://github.com/rowanz/hellaswag)（访问 2026-11-07）；[2](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 可比性边界

停止更新的官方测试榜不等于当代验证集SOTA；不能把两个split混排。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

## 7. 最新情况

### 核查日

2026-11-07（指定采集日期）

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 已核实版本

官网声明自2024年11月关闭提交；当前可读的是历史test榜，不应称为2026年持续更新榜。

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2019-05-20；；2026_h2_evidence：- url：https://arxiv.org/html/2610.11978v1；date：2026-10-08；note：Jev 研究表1–2及§3.1实际在 HellaSwag 上比较多类模型，不将ARC-Easy或其它子集另计。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 饱和情况

待核实

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）；[3](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

### 已知问题

验证集普遍公开使用；对抗过滤是构建方式，不是防止未来训练污染的保证。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 衍生关系

继承SWAG方向但扩大干扰项难度；本条不把ActivityNet与WikiHow视作独立benchmark。

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不代替榜单更新或实验日期）

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 官方结果入口

https://rowanzellers.com/hellaswag/

来源：[1](https://github.com/rowanz/hellaswag)（访问 2026-11-07）；[2](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

### 第三方结果入口

待核实

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| 官方历史test榜；2024-11停止接收提交 | 1 | GPT4 base 10-shot | 95.3 | overall test accuracy % | [原始来源](https://rowanzellers.com/hellaswag/)；采集2026-11-07；2023-03-08（官网列示日期，未给时区） |
| 官方历史test榜；2024-11停止接收提交 | 2 | ALUM | 85.6 | overall test accuracy % | [原始来源](https://rowanzellers.com/hellaswag/)；采集2026-11-07；2020-03-23（官网列示日期，未给时区） |
| 官方历史test榜；2024-11停止接收提交 | 3 | RoBERTa | 85.2 | overall test accuracy % | [原始来源](https://rowanzellers.com/hellaswag/)；采集2026-11-07；2019-07-25（官网列示日期，未给时区） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

去掉重复GPT-4/ALUM行，仅列可在官方关闭榜核对的前三个模型；不混入validation研究结果。榜单关闭月份为2024-11，最后一次更新日待核实；模型旁日期不是采集日。

来源：[1](https://rowanzellers.com/hellaswag/)（访问 2026-11-07）

## 9. 联系方式

### 公开研究联系邮箱

待核实

说明：未从已核实官方材料收录专门联系邮箱；不猜测个人邮箱

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 问题反馈

https://github.com/rowanz/hellaswag/issues

来源：[1](https://github.com/rowanz/hellaswag)（访问 2026-11-07）

### 官方账号

待核实

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### 隐私政策

待核实

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/1905.07830

来源：[1](https://arxiv.org/abs/1905.07830)（访问 2026-11-07）

### PDF SHA-256

9a042fdcc4a22848cffde37e9c5257e423443980172bab7367dffb4e779aac37

说明：下载原始PDF字节的SHA-256；与既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/1905.07830)（访问 2026-11-07）

### PDF字节数

1192712

来源：[1](https://arxiv.org/pdf/1905.07830)（访问 2026-11-07）

### 文件夹

来源：

### 其他原始材料

来源：

### PDF

来源：

## 11. 变更记录

### 本页修订

- date：2026-11-07；；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- date：2026-11-07；；change：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。；fields_updated：- basic_info.license；- latest_status.latest_dataset_version；- data_format.public_hidden_split；- leaderboard.results；- leaderboard.coverage_note
- date：2026-11-07；；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）
