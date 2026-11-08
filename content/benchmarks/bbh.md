# BIG-Bench Hard (BBH)

> 核查：2026-11-07（，）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

BIG-Bench Hard (BBH)

来源：[1]

### 全称

BIG-Bench Hard

来源：[1]

### 数据/软件版本

2022 公开任务集；未固定仓库 commit

来源：[2][1]

### 论文版本

arXiv v1

来源：[1]

### 发布日期

2022-10-18 01:08:26（arXiv v1首次提交）

来源：[1]

### 主板块

推理

来源：[2]

### 学科标签

多任务复杂推理

来源：[1]

### 许可证与范围

仓库LICENSE为MIT（Copyright 2022 suzgunmirac）；适用措辞为software/documentation，不将其自动扩大为BIG-Bench原始任务或论文的统一授权。

来源：[3]

### 论文入口

https://arxiv.org/abs/2210.09261

来源：[1]

### 论文标题

Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them

来源：[1]

### 官方代码

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[2]

### 数据入口

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[2][1]

### 官方主页

https://github.com/suzgunmirac/BIG-Bench-Hard

来源：[2][1]

## 2. 发起与维护

### 发起团队

Google Research、Stanford University（论文署名机构）

来源：[1]

### 署名/合作机构

Google Research；Stanford University

来源：[4]

说明：论文作者署名单位；非另行证实的资助/合作协议。

### 作者

Suzgun, Mirac；Scales, Nathan；Schärli, Nathanael；Gehrmann, Sebastian；Tay, Yi；Chung, Hyung Won；Chowdhery, Aakanksha；Le, Quoc V.；Chi, Ed H.；Zhou, Denny；Wei, Jason

来源：[1]

### 维护入口

公开数据、CoT示例及Codex输出由suzgunmirac/BIG-Bench-Hard发布维护；沿Google Research/Stanford作者团队来源。

来源：[5][4]

### 资助与计算资源

待核实

来源：[1]

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

状态：待核实（本字段尚有未能确认的部分）。

## 3. 设计目标

23任务是论文等权平均的单位，27个JSON子任务和6511道题是发布组织方式；换成所有题微平均会改变权重。3-shot直接回答、CoT、slow/fast-thinking和基础模型不能混排。
来源：[1][1]

### 测量能力

测量组合逻辑、符号操作、算法执行和多步推理，以及显式思维链能否改善这些能力。

来源：[1]

### 为何需要这个基准

BIG-Bench 多任务平均值可能掩盖难题；本研究选择此前语言模型仍落后于人类的任务，单独测量推理瓶颈。

来源：[1]

## 4. 构建方式

### 材料来源

从 BIG-Bench 的209个任务中，依题量、自动评分适用性和此前模型相对人类表现筛出23类任务；部分任务细分，形成27个评测子任务。

来源：[1]

### 命题/编制背景

继承 BIG-Bench 社区任务；BBH研究者负责筛选并手写每类任务的思维链演示。

来源：[1]

### 审核流程

以人类基线及此前模型结果进行筛选；不是重新由专家逐题原创一套试卷。

来源：[1]

### 质量控制

限制每子任务最多250道，避免大任务支配比较；多数250道，causal_judgement 187、penguins_in_a_table 146、snarks 178。

来源：[1]

### 去污染与证据边界

论文含评测污染警示和识别措施；公开任务不能据此保证未来模型无训练污染。

来源：[1]

## 5. 数据形式

### 规模与分母

23类任务、27个子任务，共6511道评测题；统计口径为原论文所用BBH。

来源：[1]

### 题型

多项选择、布尔判断、短答案和字符串输出，随子任务变化。

来源：[1]

### 模态与字段

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1]

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1]

### 难度定位

按此前模型低于人类基线筛选，属于相对难度定义，不是统一年级或难度等级。

来源：[1]

### 公开、隐藏与划分

公开评测题及每任务3个人工CoT示例；不应把示例计入评测题量。

来源：[1]

## 6. 评测方法

### 指标

最终答案精确匹配准确率；同时按任务报告，不把所有题直接混合为唯一分数。

来源：[1]

### 评分流程

抽取最终答案后与目标答案比对，原论文比较直接回答与思维链提示。

来源：[1]

### 运行与提示

原论文3-shot示例，比较有无CoT，greedy / temperature 0；不同模型上下文与输出格式需另记。

来源：[1]

### 评测实现

官方仓库发布bbh/题目、cot-prompts/三例提示和code-davinci-002-outputs/；README未给统一现代LLM runner，不能把仓库本身说成已验证的全模型评分脚本。

来源：[5]

### 不能混比的设置

任务宏平均与全题微平均、23类与27子任务、直接回答与CoT不是同一口径。

来源：[1][6]

## 7. 最新情况

### 核查日期

2026-11-07（采集日，不是实验日）

来源：[1]

### 当前发布

2022 公开任务集；未固定仓库 commit

来源：[2][1]

### 版本脉络

original_v1：2022-10-18；subsequent_use：url：https://arxiv.org/html/2609.27284v1；evidence：基础/slow-thinking/fast-thinking分别报告BBH；不是同一轨

来源：[1][6]

### 分数上限与饱和度

Hunyuan-A13B报告分别列基础模型87.56、slow-thinking89.1、fast-thinking87.0；这些是特定协议的厂商自报，不据此认定2026-11所有模型饱和。

来源：[6]

### 争议与局限

公开答案、演示与任务生成规则可能进入训练；模型自报分数不是独立去污染证明。

来源：[1][2]

### 衍生版本

BBH是BIG-Bench子集，不等于完整BIG-Bench；本库不把各子任务拆为额外benchmark。

来源：[1][2]

## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不是实验日）

来源：[1]

### 官方入口

待核实

来源：[1]

说明：未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

状态：待核实（本字段尚有未能确认的部分）。

### 第三方/补充实验

待核实

来源：[1]

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### Hunyuan报告表2：基础模型，BBH 3-shot

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Qwen3-A22B | 88.87 | accuracy (%) |
| 2 | Hunyuan-A13B | 87.56 | accuracy (%) |
| 3 | Hunyuan-Large-1116 | 86.3 | accuracy (%) |
| 4 | Qwen2.5-72B | 85.8 | accuracy (%) |

- Qwen3-A22B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Hunyuan-A13B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Hunyuan-Large-1116：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Qwen2.5-72B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照

#### Hunyuan报告表3：slow-thinking

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Hunyuan-A13B | 89.1 | accuracy (%) |
| 2 | Qwen3-A22B | 88.9 | accuracy (%) |
| 3 | Deepseek-R1-0120 | 83.7 | accuracy (%) |
| 4 | OpenAI-o1-1217 | 80.4 | accuracy (%) |

- Hunyuan-A13B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Qwen3-A22B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Deepseek-R1-0120：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- OpenAI-o1-1217：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照

#### Hunyuan报告表4：fast-thinking

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Hunyuan-A13B | 87.0 | accuracy (%) |
| 2 | Hunyuan-Large-1116 | 86.5 | accuracy (%) |
| 3 | Qwen2.5-72B-instruct | 80.5 | accuracy (%) |
| 4 | Qwen3-A22B | 68.1 | accuracy (%) |

- Hunyuan-A13B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Hunyuan-Large-1116：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Qwen2.5-72B-instruct：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照
- Qwen3-A22B：source_url：https://arxiv.org/html/2609.27284v1；accessed：2026-11-07；source_type：厂商技术报告自报及其对照

#### 原始论文表2：3-shot CoT，23任务等权宏平均

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Codex (code-davinci-002) | 73.9 | accuracy (%) |
| 2 | InstructGPT (text-davinci-002) | 68.4 | accuracy (%) |
| 3 | PaLM 540B | 65.2 | accuracy (%) |

- Codex (code-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022历史实验
- InstructGPT (text-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022历史实验
- PaLM 540B：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022历史实验

#### 原始论文表2：3-shot Answer-only，23任务等权宏平均

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Codex (code-davinci-002) | 56.6 | accuracy (%) |
| 2 | PaLM 540B | 52.3 | accuracy (%) |
| 3 | InstructGPT (text-davinci-002) | 51.8 | accuracy (%) |

- Codex (code-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022历史实验
- PaLM 540B：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022历史实验
- InstructGPT (text-davinci-002)：source_url：https://arxiv.org/pdf/2210.09261；accessed：2026-11-07；source_type：2022历史实验

来源：[6][4]

### 覆盖边界

公开仓库不是持续滚动的排行榜；重新读取原论文表2及Hunyuan报告表2/3/4。基础、慢思考、快思考、原始CoT和直接回答分轨，不将不同设置排序为统一SOTA。BBH宏平均以原论文23任务口径为准。

来源：[5][6][4]

## 9. 联系方式

### 公开作者工作邮箱

msuzgun@cs.stanford.edu

来源：[2][1]

### 公开反馈

https://github.com/suzgunmirac/BIG-Bench-Hard/issues

来源：[2]

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

https://arxiv.org/pdf/2210.09261

来源：[1]

### 下载源文件SHA-256

168f6fff020e9fde7563905f69e6a59d0648f195f48820d52c83c7adfaee18ec

来源：[4]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

5375941

来源：[4]

### 既有文件夹

来源：[7]

### 其他材料

来源：[7]

### 既有 PDF链接

来源：[8]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 2026-11-07：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
- 2026-11-07（）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[2]

### 来源索引

[1]: https://arxiv.org/abs/2210.09261 "访问 2026-11-07"
[2]: https://github.com/suzgunmirac/BIG-Bench-Hard "访问 2026-11-07"
[3]: https://raw.githubusercontent.com/suzgunmirac/BIG-Bench-Hard/main/LICENSE "访问 2026-11-07"
[4]: https://arxiv.org/pdf/2210.09261 "访问 2026-11-07"
[5]: https://raw.githubusercontent.com/suzgunmirac/BIG-Bench-Hard/main/README.md "访问 2026-11-07"
[6]: https://arxiv.org/html/2609.27284v1 "访问 2026-11-07"
[7]: "访问 2026-11-07"
[8]: "访问 2026-11-07"
