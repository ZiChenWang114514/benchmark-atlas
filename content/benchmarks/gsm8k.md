# GSM8K

> Benchmark Constitution，核查日期：2026-11-07。未知仍保留待核实；访问日不冒充实验日。

GSM8K以英语多步算术应用题检验解题和选解能力。题目概念简单，但单次生成、计算器、验证器选优及多样本投票不是同一协议；本页保留精确公开划分并将厂商报告与独立评测区分。

导读来源：[https://arxiv.org/abs/2110.14168](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）; [https://arxiv.org/html/2609.27284v1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

## 1. 基本信息

### 简称

GSM8K

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 全称

Grade School Math 8K

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 数据/协议版本

main数据；仓库标记Archive，代码按原样提供

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 论文版本

v2；2021-11-18（论文修订号，不是数据版本）

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 发布日期及口径

2021-10-27（arXiv初稿提交时间，非推定数据首发日）

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 主板块

数学

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）

### 子领域

- 数学应用题

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 许可证

MIT（官方仓库 LICENSE；不据此推断第三方原始材料权利）

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/LICENSE)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2110.14168

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 代码入口

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）

### 数据入口

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 官方主页

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 论文标题

Training Verifiers to Solve Math Word Problems

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

## 2. 发起与维护

### 发起团队

OpenAI

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 合作及署名机构

待核实

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 作者

- Cobbe, Karl
- Kosaraju, Vineet
- Bavarian, Mohammad
- Chen, Mark
- Jun, Heewoo
- Kaiser, Lukasz
- Plappert, Matthias
- Tworek, Jerry
- Hilton, Jacob
- Nakano, Reiichiro
- Hesse, Christopher
- Schulman, John

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 维护方

OpenAI官方仓库；当前Archive状态

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md)（访问 2026-11-07）

### 资助

待核实

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

## 3. 设计目标

### 评测能力

评估语言多样的小学/初中级数学应用题中的多步算术与验证器选解能力。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 设计动机

概念简单不等于可被语言模型稳定求解，需要避免只记住固定题型模板。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

## 4. 构建方式

### 材料来源

人工写题承包者编写应用题和自然语言解答；论文流程包括Upwork、Surge AI及可供改写的模型题目种子。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 编制背景

付费人工题目写作者，研究团队进行二次求解和数据审核；不能表述为每题都来自数学专家。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 审核流程

独立第二人解题，对分歧题修改或剔除，并做题目相似性检查。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 质量控制

自然语言解答带计算注释，####之后为最终数值；另提供自动生成苏格拉底式子问题版本。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 去污染边界

收集时检查模板/相似题有助于质量控制；不保证未来预训练数据没有公开题。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

## 5. 数据形式

### 规模

HF官方openai/gsm8k数据卡：train 7,473、test 1,319，共8,792；main和socratic各自使用相同划分，不能合计为17,584独立题。README的8.5K、7.5K/1K为作者概数，精确复现按数据卡/文件。

来源：[1](https://huggingface.co/datasets/openai/gsm8k/raw/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/openai/grade-school-math/HEAD/README.md)（访问 2026-11-07）

### 题型

2至8步基础算术应用题，输出自然语言解法和最终数值。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 难度

明亮的中学生应可解（作者设计意图）；不是高等数学或奥赛难度。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 公开及隐藏划分

train.jsonl与test.jsonl均公开；另有Socratic格式，不可当独立新benchmark。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

## 6. 评测方法

### 指标

最终数值答案准确率；验证器从多个候选中选择的得分需另标。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 计分

官方dataset.py提取####后的数字；计算器通过<<..>>标注运行，不是天然禁止工具。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 提示与运行设置

原论文训练生成器和验证器并比较多候选选优；best-of-100不等于pass@1。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 评测入口

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 可比性边界

单次、投票、验证器best-of-N、计算器和few-shot设置不能混排。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

## 7. 最新情况

### 核查日

2026-11-07（指定采集日期）

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 已核实版本

main数据；仓库标记Archive，代码按原样提供

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md)（访问 2026-11-07）

### 论文历史及后续证据

arxiv_submissions：- version：v1；submitted_at：2021-10-27；；- version：v2；submitted_at：2021-11-18；；2026_h2_evidence：- url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1–4.2及表2–4实际报告 GSM8K。AIME 的不同年份归同一条目，不用年份拆分凑数。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 饱和情况

待核实

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

### 已知问题

仓库注明示例模型解答中的旧计算器曾有约1%失败，代码已修复但示例未重生成；这是历史样例问题非当前整体标签错率。

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md)（访问 2026-11-07）

### 衍生关系

Socratic格式自动加子问题，原论文未用其进行实验；本库不另计数。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）；[2](https://github.com/openai/grade-school-math)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不代替榜单更新或实验日期）

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 官方结果入口

待核实

说明：未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 第三方结果入口

待核实

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 结果

| 赛道 | 名次 | 模型 | 分数 | 指标 | 来源及时间 |
|---|---|---|---|---|---|
| Hunyuan-A13B报告表2：基础模型，4-shot CoT | — | Hunyuan-Large-1116 | 92.8 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09（arXiv编号月份；确切实验日待核实） |
| Hunyuan-A13B报告表2：基础模型，4-shot CoT | — | Qwen2.5-72B | 91.5 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09（arXiv编号月份；确切实验日待核实） |
| Hunyuan-A13B报告表2：基础模型，4-shot CoT | — | Qwen3-A22B | 94.39 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09（arXiv编号月份；确切实验日待核实） |
| Hunyuan-A13B报告表2：基础模型，4-shot CoT | — | Hunyuan-A13B | 91.83 | accuracy % | [原始来源](https://arxiv.org/html/2609.27284v1)；采集2026-11-07；2026-09（arXiv编号月份；确切实验日待核实） |

说明：—表示只转录该赛道的历史/局部结果，未给予跨赛道总排名。

### 覆盖边界

非穷尽、非跨协议排名。仅转录打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

## 9. 联系方式

### 公开研究联系邮箱

- karl@openai.com
- vineet@openai.com

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 问题反馈

https://github.com/openai/grade-school-math/issues

来源：[1](https://github.com/openai/grade-school-math)（访问 2026-11-07）

### 官方账号

待核实

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### 隐私政策

待核实

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2110.14168

来源：[1](https://arxiv.org/abs/2110.14168)（访问 2026-11-07）

### PDF SHA-256

a52417d8fcd006de882e3b404850e2cc4246815828897c18c6ce6c7a448985a4

说明：下载原始PDF字节的SHA-256；与既有副本是否相同须以其校验值核对。

来源：[1](https://arxiv.org/pdf/2110.14168)（访问 2026-11-07）

### PDF字节数

2935719

来源：[1](https://arxiv.org/pdf/2110.14168)（访问 2026-11-07）

### 文件夹

来源：

### 其他原始材料

来源：

### PDF

来源：

## 11. 变更记录

### 本页修订

- date：2026-11-07；；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- date：2026-11-07；；change：深度优化：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
- date：2026-11-07；；change：q4逐篇复核arXiv摘要及PDF、官方仓库与许可、可用HF卡和榜单；修正版本/协议/数据规模，分赛道转录精确结果，保留证据缺口。

来源：[1](urn:benchmark-constitution:editorial:r2-q4)（访问 2026-11-07）
