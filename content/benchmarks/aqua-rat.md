# AQuA-RAT

> 第1轮深度复核 · 2026-11-07（Asia/Seoul）。以下结论按字段列明证据；待核实项不是已确认事实。

## 1. 基本信息

**简称**：AQuA-RAT
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**全称**：Algebra Question Answering with Rationales
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**版本**：公开众包release与原论文实验版不同；须指定发布文件
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**论文版本**：arXiv v3
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**发布日期**：2017-05-11（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**板块**：数学
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）

**子领域**：
- 代数应用题与推理
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**许可与使用边界**：Apache-2.0（官方仓库 LICENSE；论文版本及第三方原始材料的权利需另辨）
来源：[1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/LICENSE)（访问 2026-11-07）

**论文**：https://arxiv.org/abs/1705.04146
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**代码**：https://github.com/google-deepmind/AQuA
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）

**数据集**：https://github.com/google-deepmind/AQuA
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**官方主页**：https://github.com/google-deepmind/AQuA
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**论文标题**：Program Induction by Rationale Generation : Learning to Solve and Explain Algebraic Word Problems
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

## 2. 发起与维护

**发起机构**：DeepMind、University of Oxford（论文署名）
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**合作机构**：待核实
说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**作者**：
- Ling, Wang
- Yogatama, Dani
- Dyer, Chris
- Blunsom, Phil
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**维护方**：Google DeepMind 官方 AQuA 仓库；不据仓库归属推断持续活跃维护。
来源：[1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问 2026-11-07）

**资助**：待核实
说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

## 3. 设计目标

**测量能力**：从代数文字题生成自然语言推理依据并选择答案，研究rationale对求解和解释的帮助。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**设计动机**：只预测选项无法观察模型如何组织数学推理；原工作同时建模解释。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

## 4. 构建方式

**题目来源**：论文收集GRE/GMAT风格网络题种子并用众包扩展；官方README强调公开release为完整众包数据。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**出题背景**：众包写题与写解释，研究团队开发rationale生成模型。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**审核流程**：众包流程与去近重复过滤；公开发布版本与论文初始实验数据并非完全相同。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**质量控制**：原论文按编辑距离过滤近重复；README明确原版本不能完整公开，复现实验应使用公开release口径。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**去污染**：编辑距离过滤针对近重复，不保证语义改写分离或后续LLM无污染。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

## 5. 数据形式

**题量**：当前公开原始 JSON 行数：train 97,467；dev 254；test 254，共97,975题。README概述约100,000题。
来源：[1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/train.json)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/google-deepmind/AQuA/master/dev.json)（访问 2026-11-07）；[3](https://raw.githubusercontent.com/google-deepmind/AQuA/master/test.json)（访问 2026-11-07）；[4](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问 2026-11-07）

**题型**：每题question、5个options、rationale、correct，正确选项A–E。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**模态**：文本（数学符号按文本表达）；并非原始图像视频识别任务
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**语言**：英语题面；形式化/数学符号另见模态与仓库格式
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**难度**：代数应用题/考试风格；rationale存在多种写法，答案正确不意味着解释逻辑完备。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**划分与公开范围**：官方公开train/dev/test及对应tok文件；原论文实验版无法完全公开，README明确说明结果会不同。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问 2026-11-07）

## 6. 评测方法

**指标**：选项准确率；原论文还报告rationale的BLEU-4/困惑度，现代评测通常只看答案。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**评分**：预测选项与correct对比；若评解释应独立报告，不能用选项accuracy替代解释质量。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**提示设置**：原工作监督训练生成rationale后作答；CoT演示数、token预算及答案抽取需另外说明。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**评测脚本**：https://github.com/google-deepmind/AQuA
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**可比性说明**：原论文250测试与公开/Jev254测试、tok与untok、是否评价rationale均需区分。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

## 7. 最新情况

**复核日期**：2026-11-07（Asia/Seoul）
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

**最新数据版本**：公开众包release与原论文实验版不同；须指定发布文件
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**论文修订与后半年证据**：arxiv_version：arXiv v3；history_note：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。；2026_h2_evidence：
- url：https://arxiv.org/html/2610.11978v1；date：2026-10-08；note：Jev 研究§3.1和表1–2实际使用 AQuA-RAT 并比较专用决策模型与通用模型。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

**饱和情况**：待核实
说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

**争议与污染**：官方 README 明示：论文初始结果使用过一个无法完整发布的旧版本；当前公开数据为完全众包版本，运行论文系统所得分数会不同。不能把论文旧版数字和现行公开题库直接混排。
来源：[1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（访问 2026-11-07）

**派生版本**：MathQA从AQuA题源重标运算程序；两者不能按相同数据及评分方式处理。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）；[2](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）

## 8. 榜单快照

**快照采集日期**：2026-11-07（Asia/Seoul；采集日不是测量日）
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

**官方榜单**：待核实
说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**第三方榜单**：待核实
说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**结果快照**：
- model_version：Qwen3.8 Max；score：94.1；unit：%；scope_and_protocol：Jev表2 AQuA；附录测试254；result_date：2026-10-08；snapshot_date：2026-11-07；source_url：https://arxiv.org/html/2610.11978v1；source_class：研究论文实验，非官方实时榜；checkpoint_note：模型名按来源原样；若来源未列API checkpoint则不补造。
- model_version：Qwen3.8 Flash；score：91.7；unit：%；scope_and_protocol：同表；result_date：2026-10-08；snapshot_date：2026-11-07；source_url：https://arxiv.org/html/2610.11978v1；source_class：研究论文实验，非官方实时榜；checkpoint_note：模型名按来源原样；若来源未列API checkpoint则不补造。
- model_version：Gemini 3.8 Flash；score：91.3；unit：%；scope_and_protocol：同表；result_date：2026-10-08；snapshot_date：2026-11-07；source_url：https://arxiv.org/html/2610.11978v1；source_class：研究论文实验，非官方实时榜；checkpoint_note：模型名按来源原样；若来源未列API checkpoint则不补造。
来源：[1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

**覆盖边界**：非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07）

## 9. 联系方式

**公开项目邮箱**：
- lingwang@google.com
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**问题反馈**：https://github.com/google-deepmind/AQuA/issues
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）

**官方社交渠道**：待核实
说明：未核实专门官方社交账号，不收录同名个人账户
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**隐私政策**：待核实
说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

## 10. 原始文件

**Drive PDF**：id：1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J；webViewLink：https://drive.google.com/file/d/1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J/view?usp=drivesdk
来源：[1](https://drive.google.com/file/d/1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J/view?usp=drivesdk)（访问 2026-11-07）

**原始PDF地址**：https://arxiv.org/pdf/1705.04146
来源：[1](https://arxiv.org/abs/1705.04146)（访问 2026-11-07）

**SHA256**：5111754b10c77d287685cc64992c92989eecc9b7cca65089f97c0efd48a4feb7
来源：[1](https://arxiv.org/pdf/1705.04146)（访问 2026-11-07）

**PDF字节数**：534332
来源：[1](https://arxiv.org/pdf/1705.04146)（访问 2026-11-07）

**Drive目录**：id：14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc；webViewLink：https://drive.google.com/drive/folders/14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc
来源：[1](https://drive.google.com/drive/folders/14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc)（访问 2026-11-07）

**其他文档**：chinese_intro_doc：id：1eZjRI88WySYba1wenrGtoejhe6_rdLemJEcXKXDbWLU；webViewLink：https://docs.google.com/document/d/1eZjRI88WySYba1wenrGtoejhe6_rdLemJEcXKXDbWLU/edit?usp=drivesdk；mimeType：application/vnd.google-apps.document；local_markdown：content/benchmarks/aqua-rat.md
来源：[1](https://drive.google.com/drive/folders/14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc)（访问 2026-11-07）

## 11. 变更记录

**记录**：
- date：2026-11-07；timezone：Asia/Seoul；change：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- date：2026-11-07；timezone：Asia/Seoul；change：深度优化第1轮：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
来源：[1](https://github.com/google-deepmind/AQuA)（访问 2026-11-07）

