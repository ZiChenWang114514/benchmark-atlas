# FrontierSWE v2

> Benchmark Constitution｜深度核验：2026-11-07。访问日沿固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

这是20小时级长程工程评测，34项任务同时覆盖实现、性能、科学计算、视觉与AI研究。重要变化不只是加题，还包括独立验证器、可重复性能代理指标和鼓励持续工作的Proximus harness。

最近复核

## 基本信息

**简称**：FrontierSWE v2

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**全称**：FrontierSWE

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**基准版本**：V2

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**论文版本**：2026-09-02网页技术报告；无arXiv版号可据此填写。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**发布日期**：2026-09-02（官方V2发布文日期）

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**主板块**：代码

核验说明：Benchmark Constitution 编辑归档，不作为官方分类。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**领域标签**：代码

核验说明：编辑标签

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**许可证与授权边界**：README仅声明任务及测试harness供评测使用，并要求逐任务检查上游归属；统一开源许可证待核实。

状态：待核实。

核验说明：根目录LICENSE请求返回404；不能由公开仓库推定MIT/Apache授权。

来源：[1](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）

**论文或技术报告**：https://www.frontierswe.com/blog/v2

核验说明：官方技术发布文，不把博客冒充arXiv论文。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**官方代码**：https://github.com/Proximal-Labs/frontier-swe-v2

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**数据地址**：https://github.com/Proximal-Labs/frontier-swe-v2

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**官方主页**：https://www.frontierswe.com/

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**论文题名**：FrontierSWE v2（官方技术发布文；README引用题名为FrontierSWE v2: Testing Coding Agents at the Frontier of Software Engineering）

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）；[2](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）

## 发起与维护

**发起方**：Proximal团队

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**协作与机构边界**：与外部贡献者合作；致谢把Bilal Bakht Ahmad和Ayush Nangia列为独立贡献者，Animesh Sinha与Bhuvanesh Sridharan列为BayesMech。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**作者**：Rishyanth Kondra；Sanket Mhatre；Akshit Kumar；Evan Chu；Bilal Bakht Ahmad；Ayush Nangia；Rajan Agarwal；Arpan Dasgupta；Animesh Sinha；Bhuvanesh Sridharan；Krupa Dave；Brendan Graham；Guanyu Song；Anirudh Rahul；Wei Hern Lim；Abishek Thangamuthu；Ramneet Singh；Danna Liu；Navid Pour；Calvin Chen；Justus Mattern

来源：[1](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）；[2](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**维护方**：Proximal-Labs / Proximal团队

来源：[1](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）；[2](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

## 设计目标

**测量能力**：衡量人类能力边缘的软件工程能力，涵盖AI研究实现、优化、科学计算及视觉推理。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**相对既有评测的缺口**：面向20小时级工程与科研，修正v1模型过早提交、共享主机计时噪声及测试器可篡改等问题；测量固定长时间预算内最终实现的功能和性能。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

## 构建方式

**题目来源**：v2新增21项并退役4项v1任务，总计34项；来自编译器重写、数据库兼容、GPU推理优化、天气预测、MEG解码等真实技术场景。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）；[2](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）

**出题与研究背景**：Proximal核心工程团队与外部贡献者；Kondra、Mhatre和Kumar列为共同负责人，具体个人履历不作推断。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**审核流程**：全部任务重新QA；提供与最终评分单调相关的self-check反馈；运行后评审面板检查完整轨迹、标记可疑行为，确认违规试次清零。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**质量控制**：固定镜像、代理与干净验证器双容器隔离、非root执行及root私有评分资产；实现任务采用结构变异测试，性能任务改用固定微架构加权指令数以提高可复现性。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**去污染与泄漏边界**：防作弊措施包括隐藏变体、独立验证器及轨迹审查；任务内容公开，这些防作弊措施不构成预训练去污染证明，训练污染程度待核实。

状态：待核实。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

## 数据形式

**规模与口径**：34任务

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**任务类型**：长程软件工程任务，含编译器、科学计算、模型优化及视觉交互工程。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**模态**：代码；文本；视觉环境

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**语言**：任务覆盖Zig、Rust、Go、Free Pascal、Swift、Haskell、CUDA、Python等技术栈；任务要求逐项定义，不使用单一编程语言口径。

来源：[1](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）；[2](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**难度**：每任务20小时运行预算。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**公开与隐藏划分**：公开34项任务的instruction.md、task.toml、环境及参考solution；最终验证采用干净容器与部分隐藏结构变异/域外数据，不是标准train/test百分比切分。

来源：[1](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）；[2](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

## 评测方法

**指标**：mean@5；另展示worst@5至best@5区间及平均成本、用时。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**评分方式**：每模型每任务运行5次；跨34任务报告mean@5。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**提示与运行设置**：官方榜显示proximus harness；每trial 20小时。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**官方复现入口**：https://github.com/Proximal-Labs/frontier-swe-v2

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**可比性警告**：不同harness、GPU与推理预算须分轨；Kimi发布文中dominance历史分数不能直接与当前V2 mean@5排序混合。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**数据及热度证据**：```json
{
 "version": "V2"
 "heat_confidence": "A"
 "why_trending": "候选热度等级A；下列已重新打开的证据分别标明评测方与证据性质，不把网页数量当作独立采纳机构数量。"
 "evidence_2026_h2": [
 {
 "url": "https://epoch.ai/data/eci-documentation/data"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "Epoch AI"
 "note": "当前ECI组成明确列出该benchmark；纳入不等于运行。"
 }
 {
 "url": "https://www.frontierswe.com/"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "官方维护方"
 "note": "已打开当前官方方法与榜单；观察日不冒充发布时间。"
 }
 ]
}
```

来源：[1](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）；[2](https://www.frontierswe.com/)（访问 2026-11-07）

**论文与版本历史**：V2发布文日期2026-09-02；README明确任务内容与评分仍可能更新，应固定仓库提交与镜像digest。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）；[2](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）

**饱和程度**：当前首页最高mean@5为65.5%，未达满分；发布日最高56.29%是历史结果，不能混作当前榜首。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）；[2](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**已知问题与局限**：发布文记录reward-hacking与越权读取评测资产事件，相关确认试次清零；性能代理指标虽可复现，仍不是所有硬件上的真实耗时；Proximus提示使模型意识到正在被评测。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

**后续与衍生**：V2取代v1的主榜；PCQM4Mv2 Molecular Gap Prediction、Pyright优化、Revideo优化、Dependent Type Checker四项退役。

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

## 榜单快照

**快照日期**：2026-11-07

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**官方入口**：https://www.frontierswe.com/

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**第三方入口**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 当前官方网页榜 | 1 | GPT-6 Astra / proximus | 65.5 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 2 | Claude Opus 5.5 / proximus | 62.3 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 3 | Gemini 4 Carbon / proximus | 61.2 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 4 | GLM-5.3 / proximus | 30.2 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 5 | Grok 4.7 / proximus | 29.5 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 6 | Kimi K3 / proximus | 25.9 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 7 | Muse Spark 1.3 / proximus | 25.8 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 8 | Qwen3.8-Max-0902 / proximus | 17.8 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 9 | DeepSeek V4 Flash Vision Exp / proximus | 14.8 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |
| 当前官方网页榜 | 10 | Inkling / proximus | 4.1 | V2 mean@5 (%) | 待核实 | [原始来源](https://www.frontierswe.com/) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：已重新打开首页前10。mean@5为34任务各5次试验的均值；worst@5–best@5 whiskers不是95%置信区间。官网未标榜表更新时间，保留待核实；2026-09-02发布文不是当前榜日期。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）；[2](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）

## 联系方式

**公开联系邮箱**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**Issues或讨论入口**：https://github.com/Proximal-Labs/frontier-swe-v2/issues

来源：[1](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）

**官方社交**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**隐私政策**：https://proximal.ai/privacy

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

## 原始文件

**原始PDF**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**PDF SHA-256**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**PDF字节数**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**文件夹**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

**其他官方文档**：```json
[
 {
 "type": "V2技术报告"
 "url": "https://www.frontierswe.com/blog/v2"
 }
 {
 "type": "公开任务与复现说明"
 "url": "https://github.com/Proximal-Labs/frontier-swe-v2"
 }
]
```

来源：[1](https://www.frontierswe.com/blog/v2)（访问 2026-11-07）；[2](https://github.com/Proximal-Labs/frontier-swe-v2)（访问 2026-11-07）

**论文链接**：待核实

状态：待核实。

核验说明：本组仅建立本地研究条目，未上传。

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）

## 变更记录

**及历史变更**：```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-07"
 最近复核
 }
]
```

来源：[1](https://www.frontierswe.com/)（访问 2026-11-07）
