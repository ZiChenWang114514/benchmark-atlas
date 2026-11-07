# AudioMultiChallenge

> 核查：2026-11-07（Asia/Shanghai，UTC+8）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

第2轮逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留；trending: B

## 1. 基本信息

### 简称

AudioMultiChallenge

来源：[1]

### 全称

Audio MultiChallenge

来源：[2][3]

### 数据/软件版本

原始Audio MultiChallenge；编号待核实

来源：[1]

### 论文版本

arXiv:2512.14865v1；2025-12-17 03:26:44（Asia/Shanghai，UTC+8）

来源：[2]

### 发布日期

2025-12-17（Asia/Shanghai；arXiv v1提交03:26:44；Scale研究页另标12/17/2025，无时区时刻）

来源：[2][4]

### 主板块

语音

来源：[1]

说明：编辑归档；跨领域只计主板块。

### 学科标签

多模态；多轮对话

来源：[1]

### 许可证与范围

MIT（ScaleAI/audiomc官方数据卡YAML）

来源：[3]

### 论文入口

https://arxiv.org/abs/2512.14865

来源：[1]

### 论文标题

Audio MultiChallenge: A Multi-Turn Evaluation of Spoken Dialogue Systems on Natural Human Interaction

来源：[2]

### 官方代码

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 数据入口

https://huggingface.co/datasets/ScaleAI/audiomc

来源：[1]

### 官方主页

https://labs.scale.com/leaderboard/audiomc

来源：[1]

## 2. 发起与维护

### 发起团队

Scale AI

来源：[1]

### 署名/合作机构

论文首页11位作者统一署名Scale AI；这里记录公开论文机构，不把说话人或未署名贡献者推定为合作机构。

来源：[5]

### 作者

Advait Gosai；Tyler Vuong；Utkarsh Tyagi；Steven Li；Wenjia You；Miheer Bavare；Arda Uçar；Zhongwang Fang；Brian Jang；Bing Liu；Yunzhong He

来源：[2][3]

### 维护入口

Scale AI

来源：[1]

### 资助与计算资源

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 3. 设计目标

固定历史测试只让受测模型生成最后一轮，重点是对自然音频中的约束、记忆和修订保持。Text与Audio是不同输出模式；Audio轨评分仍看输出文本流，不等于语音自然度或音色质量。
来源：[1][1]

### 测量能力

自然人声多轮对话中的推断记忆、指令保持、自洽与口头修订。

来源：[1]

### 为何需要这个基准

ASR/TTS或单轮合成语音测试难衡量犹豫、打断、环境声音与多轮修订的鲁棒性。

来源：[1]

## 4. 构建方式

### 材料来源

多智能体先用TTS探索失败策略，提炼为蓝图；人类按蓝图即兴录制自然对话并写原子rubric。

来源：[1]

### 命题/编制背景

论文称highly trained core contributors；47位说话人按对抗蓝图自然即兴录制，专门审核员、独立质控团队与内部研究团队复审。不是TTS音频直接充当最终人声测试集。

来源：[5]

### 审核流程

专门审核员、独立QC团队及内部研究团队三阶段审核自然性、失败有效性、音频与rubric。

来源：[2]

### 质量控制

三阶段核查自然性、真实失败、提示多样性、音质与rubric。官方方法页报告在1712次rubric判断上o4-mini与人工Cohen κ约0.87、Macro F1约0.94（作者近似报告值，非本库推算）。

来源：[5][6]

### 去污染与证据边界

新采集的人声对抗对话与实例专用最终轮rubric可减少直接搬用既有问答，但公开HF卡含转录/历史；本轮未在论文中找到训练语料逐条去重审计证据，不能称无污染。

来源：[5][7]

## 5. 数据形式

### 规模与分母

452对话、1,712项rubric、47位说话人；14.99小时用户音频，48kHz；每对话3–8轮。

来源：[1]

### 题型

提供固定对话历史，只评最终助手回复；用户轮为音频，历史助手轮为文本。

来源：[1]

### 模态与字段

音频；文本

来源：[1]

### 语言

英语

来源：[2]

### 难度定位

3–8轮固定上下文：Inference Memory、Instruction Retention、Self Coherence、Voice Editing；42题需背景声/副语言等audio cue。难点为跨轮状态与口头修订，而非只增加轮数或衡量发音质量。

来源：[5][6]

### 公开、隐藏与划分

官方HF公开452对话及rubric数据；用户各轮音频、转录与历史助手文本用于固定历史输入。最后助手回复由受测模型新生成；不能把历史助手回答当该模型自由交互轨迹。本轮未核实独立训练集/隐藏测试划分。

来源：[7][3][5]

状态：待核实（本字段尚有未能确认的部分）。

## 6. 评测方法

### 指标

APR为主要任务全通过率，ARS为rubric部分通过诊断指标。

来源：[1]

### 评分流程

o4-mini逐条二元判断；APR要求同一任务所有rubric通过，ARS为每任务rubric通过比例再平均。

来源：[1]

### 运行与提示

固定历史，用户轮音频/助手轮文本，只生成并评分最后一轮；Text Output与Audio Output分别配置。

来源：[1]

### 评测实现

官方HF数据卡直接发布o4-mini裁判system prompt与Python build_grading_conversation_history函数：沿数据集历史文本，仅将最后助手轮替换为被测模型输出。它是公开评分构造代码，不是一键覆盖所有模型API的完整运行器。

来源：[3]

说明：独立完整代码仓库地址仍保留在basic_info.code_url待核实；不因只找到片段便声称全流程runner已发布。

### 不能混比的设置

Text与Audio输出分轨；Audio模式仍评模型输出文本流，不直接评价声音质量；不是MMAU升级版。

来源：[1]

## 7. 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8；本轮采集日，不是实验日）

来源：[2]

### 当前发布

version：原始Audio MultiChallenge；编号待核实；evidence_2026_h2：- url：https://labs.scale.com/leaderboard/audiomc；date：2026-11-07；date_type：observed_on；note：Scale当前多轮语音榜保留实测结果；主要单一机构展示，不将多条Scale链接算多个独立采用者。

来源：[1]

说明：热度等级沿候选采用；只保留本轮已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

### 版本脉络

v1：2025-12-17T03:26:44+08:00；arxiv_id：2512.14865；paper_reported_best：model：Gemini 3 Pro Preview (Thinking)；APR：54.65；output：Text；boundary：论文历史实验与持续更新的Text/Audio官方榜分别展示

来源：[2][5][6][8]

### 分数上限与饱和度

本轮官方Text榜头部60.40% APR，Audio榜头部48.45% APR；两者均明显未满分，但不把这两个不同输出协议直接合并为唯一排名。

来源：[6][8]

### 争议与局限

官网四轴题数将Self-Coherence/Voice Editing写成83/117，论文表1写117/83；452总数一致，两个轴归属冲突仍待核实。Audio轨只以输出文本流评分，不检查原始音频自然度或音色；不能把分数解释为全面语音质量。

来源：[5][1]

状态：待核实（本字段尚有未能确认的部分）。

### 衍生版本

不是已有mmau的新版本；MMAU侧重音频理解问答，本条为自然多轮语音对话；Text/Audio输出子轨不重复新建。

来源：[1]

说明：已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

## 8. 榜单快照

### 采集日期

2026-11-07（Asia/Shanghai，UTC+8；本轮采集日，不是实验日）

来源：[2]

### 官方入口

https://labs.scale.com/leaderboard/audiomc

来源：[1]

### 第三方/补充实验

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### 官方现榜：Text Output

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | gemini-3.8-flash (high) | 60.4 | APR (%) |
| 2 | salesforce-launa-omni-1 | 59.69 | APR (%) |
| 3 | gemini-4-argon (high) | 58.41 | APR (%) |
| 4 | Inkling (Thinking) | 56.64 | APR (%) |
| 5 | Inkling-small | 54.87 | APR (%) |

- gemini-3.8-flash (high)：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale官网快照；displayed_ci_plus_minus：4.49
- salesforce-launa-omni-1：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale官网快照；displayed_ci_plus_minus：4.13
- gemini-4-argon (high)：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale官网快照；displayed_ci_plus_minus：4.53
- Inkling (Thinking)：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale官网快照；displayed_ci_plus_minus：2.7
- Inkling-small：source_url：https://labs.scale.com/leaderboard/audiomc-text；accessed：2026-11-07；output_modality：text；source_type：Scale官网快照；displayed_ci_plus_minus：4.57

#### 官方现榜：Audio Output

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | gpt-realtime-2 (xHigh) | 48.45 | APR (%) |
| 2 | tml-interaction-small | 43.36 | APR (%) |
| 3 | gpt-realtime-2 | 37.61 | APR (%) |
| 4 | gemini-3.1-flash-live-preview (Thinking) | 36.06 | APR (%) |
| 5 | gpt-realtime-1.5 | 34.73 | APR (%) |

- gpt-realtime-2 (xHigh)：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale官网快照；displayed_ci_plus_minus：4.59
- tml-interaction-small：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale官网快照；displayed_ci_plus_minus：4.55
- gpt-realtime-2：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale官网快照；displayed_ci_plus_minus：4.45
- gemini-3.1-flash-live-preview (Thinking)：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale官网快照；displayed_ci_plus_minus：4.41
- gpt-realtime-1.5：source_url：https://labs.scale.com/leaderboard/audiomc-audio；accessed：2026-11-07；output_modality：audio；source_type：Scale官网快照；displayed_ci_plus_minus：4.38

#### 原论文v1表2：Text Output（历史）

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Gemini 3 Pro Preview (Thinking) | 54.65 | APR (%) |
| 2 | Gemini 2.5 Pro (Thinking) | 46.9 | APR (%) |
| 3 | Gemini 2.5 Flash (Thinking) | 40.04 | APR (%) |

- Gemini 3 Pro Preview (Thinking)：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：text；source_type：论文固定实验
- Gemini 2.5 Pro (Thinking)：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：text；source_type：论文固定实验
- Gemini 2.5 Flash (Thinking)：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：text；source_type：论文固定实验

#### 原论文v1表2：Audio Output（历史）

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Qwen 3 Omni | 24.34 | APR (%) |
| 2 | GPT 4o Audio Preview | 23.23 | APR (%) |
| 3 | GPT Realtime | 20.35 | APR (%) |

- Qwen 3 Omni：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：audio；source_type：论文固定实验
- GPT 4o Audio Preview：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：audio；source_type：论文固定实验
- GPT Realtime：source_url：https://arxiv.org/pdf/2512.14865；accessed：2026-11-07；output_modality：audio；source_type：论文固定实验

来源：[6][8][5]

### 覆盖边界

已分别打开Text Output与Audio Output专榜，不再把综合页面前三的输出模式留空。rank为各页面当前显示次序，不自行计算统计显著排名；页面另定义Rank(UB)。Inkling置信区间综合页±4.55、Text专页±2.70，采用对应专页值并记录冲突。逐模型运行日期及榜表更新时间仍待核实。

来源：[6][8]

## 9. 联系方式

### 公开作者工作邮箱

advait.gosai@scale.com

来源：[2]

### 公开反馈

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 官方账号

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 隐私信息

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2512.14865

来源：[2]

说明：官方arXiv原论文PDF入口；本组不下载、不上传Drive。

### 下载源文件SHA-256

d724dd047b476408bef588fac478984c0237e76a84c7e9096ff64f330d145e57

来源：[5]

说明：本轮实际下载的源站PDF字节校验；未声称重新核验Drive文件内容。

### 下载源文件字节数

2393184

来源：[5]

### 既有Drive文件夹

待核实

来源：[1]

说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 其他材料

- type：官方方法或项目页；url：https://labs.scale.com/leaderboard/audiomc；accessed：2026-11-07

来源：[1]

### 既有Drive PDF链接

待核实

来源：[1]

说明：本组只建立暂存条目，未上传Drive。

状态：待核实（本字段尚有未能确认的部分）。

> 本轮没有上传或改写Drive文件。以上SHA-256和字节数针对本轮实际下载的源站PDF，不等于重新核验既有Drive文件。

## 11. 变更记录

- 2026-11-07（Asia/Shanghai (UTC+8)）：首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传Drive。
- 2026-11-07（Asia/Shanghai (UTC+8)）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传Drive，未重跑评测。

来源：[1]

### 来源索引

[1]: https://labs.scale.com/leaderboard/audiomc "访问 2026-11-07"
[2]: https://arxiv.org/abs/2512.14865 "访问 2026-11-07"
[3]: https://huggingface.co/datasets/ScaleAI/audiomc/raw/main/README.md "访问 2026-11-07"
[4]: https://scale.com/research/audiomc "访问 2026-11-07"
[5]: https://arxiv.org/pdf/2512.14865 "访问 2026-11-07"
[6]: https://labs.scale.com/leaderboard/audiomc-text "访问 2026-11-07"
[7]: https://huggingface.co/datasets/ScaleAI/audiomc "访问 2026-11-07"
[8]: https://labs.scale.com/leaderboard/audiomc-audio "访问 2026-11-07"
