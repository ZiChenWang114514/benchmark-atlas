# BioBasicsBench

衡量智能体能否判读日常湿实验的原始数据、识别错误，并知道证据何时不能支持结论。

## 基本信息

**简称**：BioBasicsBench

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**全称**：BioBasicsBench

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**基准版本**：2026-11-06官方页面所述版本

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**论文版本**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**发布日期**：2026-11-06

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**主板块**：生物与医学

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**领域标签**：湿实验；实验数据判读

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**许可证**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**论文或技术报告**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**官方代码**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**数据地址**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**官方主页**：https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**论文题名**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 发起与维护

**发起方**：OpenAI与Ligo。页面称Ligo是一家做酶设计的生物技术公司。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**协作机构**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**作者**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**当前维护方**：OpenAI

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**资助方**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 设计目标

**要测的能力**：判读原始实验数据，识别错误，并判断证据能否支持结论。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**现有基准的缺口**：页面认为，用论文里挑选过的图表和图像做成的基准，会漏掉湿实验里失败实验、含糊图像和互相冲突的观察。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 构建方式

**题目来源**：科学家用自己实验中的数据出题，并为每题写评分标准。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**出题人背景**：出题的是做湿实验的科学家；外部复核者是在湿实验室工作的博士层级科学家。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**审核流程**：每题经过未参与出题的Ligo科学家内部复核、湿实验室博士层级科学家外部复核，以及最后一次内部复核。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**质量控制**：复核者检查提示、实验证据、量规、作者笔记，以及一次已评分的模型作答。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**去污染**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 数据形式

**题量**：100道任务，分属蛋白质方法、成像与流式、定量与测定、核酸方法、分子克隆。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**题型**：智能体返回结构化答案，包含所要求的结论、测量或建议，并在需要时给出推理。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**模态**：凝胶和印迹图像、平板照片、显微镜堆栈、测序读段、酶标仪导出和实验台视频等原始证据。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**语言**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**难度**：从读取凝胶中DNA样品分子量，到较详细的测定分析。页面称这些都是湿实验科学家应能稳定完成的日常工作。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**公开与隐藏划分**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 评测方法

**指标**：平均奖励，即任务得分占可用分数的百分比。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**评分方式**：按量规中的单项标准给分，用以区分正确结论和部分正确的分析。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**提示设置**：页面报告7个模型、37组模型与推理力度设置，每个设置对100题各做5次。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**官方评测脚本**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**可比性说明**：页面上的分数是OpenAI自报，不是独立机构复测。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 最新情况

**核验日期**：2026-11-08

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**最新数据版本**：2026-11-06官方页面所述版本

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**论文修订**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**饱和情况**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**污染与争议**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**衍生基准**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 榜单快照

**快照日期**：2026-11-06

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**官方榜**：https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**第三方榜**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**结果快照**：页面的xhigh表中，GPT-6 Astra平均奖励66.7%，GPT-5.6 Sol为43.8%。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**覆盖说明**：这是厂商在自己的页面上报告的结果。

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 联系方式

**公开邮箱**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**代码讨论**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**官方社交账号**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**隐私政策**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 原始文件

**论文PDF**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**文件校验**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**文件大小**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**文件夹**：待核实

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

**其他文件**：https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/

来源: [1](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) (访问 2026-11-08)

## 变更记录

2026-11-08：初次收录。
