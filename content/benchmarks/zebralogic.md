# ZebraLogic｜中文深度介绍

核验日期：2026-11-07（Asia/Seoul）。事实按所列来源理解；未核实项不作推断。

用可验证的斑马逻辑网格谜题评估约束传播、全局一致性和随搜索空间增大而变化的推理能力。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 一、基本信息

### 简称

ZebraLogic

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 全称

ZebraLogic

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 数据/协议版本

公开1000题集合；2024首发、2025论文版，未固定数据revision

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 发布日期

2025-02-03（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 板块

推理

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）。

### 子领域

- 约束逻辑推理

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 许可证

- **评测代码许可**：Apache-2.0（ZeroEval LICENSE）
- **数据许可**：待核实（本次打开的WildEval/ZebraLogic数据卡未声明license；代码许可不代替数据授权）

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/LICENSE)（采集 2026-11-07）；[2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md)（采集 2026-11-07）。


核验说明：代码许可已核实，数据集许可仍待核实。

### 论文

https://arxiv.org/abs/2502.01100

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 代码

https://github.com/WildEval/ZeroEval

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）。

### 数据集

https://huggingface.co/datasets/WildEval/ZebraLogic

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 官网

https://huggingface.co/spaces/allenai/ZebraLogic

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 论文题名

ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

University of Washington、Allen Institute for AI、Stanford University（论文署名）

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 正式合作方

待核实

核验说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 作者

- Lin, Bill Yuchen
- Bras, Ronan Le
- Richardson, Kyle
- Sabharwal, Ashish
- Poovendran, Radha
- Clark, Peter
- Choi, Yejin

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 当前维护

待核实

核验说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 资助

待核实

核验说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

用可验证的斑马逻辑网格谜题评估约束传播、全局一致性和随搜索空间增大而变化的推理能力。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 设计缺口

传统知识问答难以区分记忆与逻辑搜索；该集合用可控规模的CSP分析推理计算的扩展极限。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 四、构建方式

### 题源

程序先采样完整网格解，再生成线索并用求解器检查唯一解；删除冗余线索后得到自然语言题目。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 出题/标注人员

逻辑与自然语言推理研究者设计模板和生成程序，不是每题人工出题。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 审核

通过约束求解验证可解性及唯一解；论文分析求解器冲突数与模型难度的对应关系。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 质量控制

N和M均取2至6，共25种尺寸，每种40题；同时控制搜索空间与逻辑约束结构。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 去污染边界

合成与唯一解验证降低某些数据问题，但公开集合和模板不能证明后续模型未见过测试题。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 五、数据形式

### 题量

数据卡grid_mode测试集1000个谜题；mc_mode测试集3259道选择题。两者是不同配置，不相加为独立谜题数。

来源：[1](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md)（采集 2026-11-07）。

### 题型

根据自然语言线索填写完整实体—属性对应网格，输出结构化JSON。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 难度

按网格尺寸、搜索空间与Z3冲突等划分；同尺寸不代表同等求解难度。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 公开/隐藏划分

公开评测集合；没有在本轮材料中确认一个独立隐藏官方测试集。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 六、评测方法

### 指标

整题完整网格正确率为主要指标，单元格正确率为辅助指标。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 评分实现

完整网格必须所有对应关系均正确；部分格正确不能等价成整题通过。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 提示与预算

论文采用含格式示例的CoT/JSON设置；ZeroEval通用README称zero-shot，须使用具体任务配置而非混淆框架总称。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 评测脚本

ZeroEval：以-d zebra-grid运行；src/evaluation/zebra_grid_eval.py评分，支持本地及API推理。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md)（采集 2026-11-07）。

### 可比性警示

一轮解答、best-of-3和不同推理预算不能混排；完整题准确率与cell accuracy必须分列。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 最新可确认数据/协议

公开1000题集合；2024首发、2025论文版，未固定数据revision

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 修订与2026H2收录证据

- **论文版本**：arXiv v2
- **历史说明**：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。
- **2026下半年引用/使用证据**：
  - 
    - **来源链接**：https://arxiv.org/html/2609.27284v1
    - **日期**：2026-09-23
    - **说明**：Hunyuan-A13B §4.2 Reasoning及表3–4实际报告 ZebraLogic；厂商自报评测。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 饱和判断

待核实

核验说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

论文o1-full的多次尝试设置与部分greedy基线不一致；公开网格可能受训练污染。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）；[2](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）。

### 衍生与排除项

属于ZeroEval评测框架中的zebra-grid任务；不是数独，也不等同所有Einstein谜题。

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）；[2](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 官方榜

https://huggingface.co/spaces/allenai/ZebraLogic

来源：[1](https://github.com/WildEval/ZeroEval)（采集 2026-11-07）；[2](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）。

### 二级机构榜

待核实

核验说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 限定范围的分数快照

- 
  - **模型版本**：grok-3-mini-fast-beta-high
  - **分数**：92.6
  - **单位**：%
  - **范围与协议**：作者仓库ZebraLogic grid结果表；greedy、single、1000 puzzles、Puzzle Acc；不是Cell Acc。
  - **结果日期**：待核实
  - **采集日期**：2026-11-07
  - **来源链接**：https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md
  - **来源等级**：一级：官方榜单
  - **检查点说明**：按来源展示名原样记录，未推断API checkpoint。
- 
  - **模型版本**：o3-mini-2025-01-31-high
  - **分数**：91.7
  - **单位**：%
  - **范围与协议**：作者仓库ZebraLogic grid结果表；greedy、single、1000 puzzles、Puzzle Acc；不是Cell Acc。
  - **结果日期**：待核实
  - **采集日期**：2026-11-07
  - **来源链接**：https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md
  - **来源等级**：一级：官方榜单
  - **检查点说明**：按来源展示名原样记录，未推断API checkpoint。
- 
  - **模型版本**：o3-mini-2025-01-31-medium
  - **分数**：88.9
  - **单位**：%
  - **范围与协议**：作者仓库ZebraLogic grid结果表；greedy、single、1000 puzzles、Puzzle Acc；不是Cell Acc。
  - **结果日期**：待核实
  - **采集日期**：2026-11-07
  - **来源链接**：https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md
  - **来源等级**：一级：官方榜单
  - **检查点说明**：按来源展示名原样记录，未推断API checkpoint。
- 
  - **模型版本**：Hunyuan-A13B
  - **分数**：84.7
  - **单位**：%
  - **范围与协议**：slow thinking，完整题准确率，报告表3
  - **结果日期**：2026-09-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2609.27284v1
  - **来源等级**：三级：模型厂商自报
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：OpenAI-o1-1217
  - **分数**：81.0
  - **单位**：%
  - **范围与协议**：同表列名，检查点按报告原样记录
  - **结果日期**：2026-09-23
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2609.27284v1
  - **来源等级**：三级：模型厂商自报
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 覆盖边界

新增官方快照与既有论文/厂商结果分开解读，不能跨split/协议混排。榜单自身最后更新日期：待核实（结果表未注明最后更新日）；2026-11-07仅为采集日期（Asia/Seoul）。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

- byuchen@uw.edu
- ronanlb@allenai.org

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）；[2](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### Issues

https://github.com/WildEval/ZeroEval/issues

来源：[1](https://github.com/WildEval/ZeroEval)（采集 2026-11-07）。

### 官方社交

待核实

核验说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### 隐私政策

待核实

核验说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

## 十、原始文件

### Drive论文PDF

- **id**：1udO6bEUq9MMLZuhldfpfTxSwt_8H1-uv
- **webViewLink**：https://drive.google.com/file/d/1udO6bEUq9MMLZuhldfpfTxSwt_8H1-uv/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1udO6bEUq9MMLZuhldfpfTxSwt_8H1-uv/view?usp=drivesdk)（采集 2026-11-07）。

### 原始论文PDF

https://arxiv.org/pdf/2502.01100

来源：[1](https://arxiv.org/abs/2502.01100)（采集 2026-11-07）。

### SHA256校验值

c252c5c4c6aa7394cb97f81d7e77fd69b3ec8d374ede75c7f0189a1530a3820d

来源：[1](https://arxiv.org/pdf/2502.01100)（采集 2026-11-07）。

### PDF字节数

3577291

来源：[1](https://arxiv.org/pdf/2502.01100)（采集 2026-11-07）。

### Drive文件夹

- **id**：1zdfv98gUtwSgZInQe0SU-tLvBK_3TWdy
- **webViewLink**：https://drive.google.com/drive/folders/1zdfv98gUtwSgZInQe0SU-tLvBK_3TWdy

来源：[1](https://drive.google.com/drive/folders/1zdfv98gUtwSgZInQe0SU-tLvBK_3TWdy)（采集 2026-11-07）。

### 其他文档

- **chinese_intro_doc**：
  - **id**：125u-jDuDNBy2zes2eY4ZNY425O-LzOhjWowRw-F24vs
  - **webViewLink**：https://docs.google.com/document/d/125u-jDuDNBy2zes2eY4ZNY425O-LzOhjWowRw-F24vs/edit?usp=drivesdk
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/zebralogic.md

来源：[1](https://drive.google.com/drive/folders/1zdfv98gUtwSgZInQe0SU-tLvBK_3TWdy)（采集 2026-11-07）。

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
    - evaluation.official_scripts
    - data_format.size
    - leaderboard.results
    - leaderboard.coverage_note

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（采集 2026-11-07）。
