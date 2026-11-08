# ZebraLogic

> 深度复核：2026-11-08。采集日不等于榜单更新日；未取得的新证据不覆盖旧来源日期。

ZebraLogic把实体—属性关系写成有唯一解的约束谜题，观察模型如何随搜索空间与回溯复杂度退化。整题准确率、部分单元格正确率和最难XL子集不能互换；取最佳多次尝试也不等于一次作答。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

## 基本信息

### 简称

ZebraLogic

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 全称

ZebraLogic

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 基准版本

公开1000题集合；2024首发、2025论文版，未固定数据revision

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）；[2](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 发布日期

- **paper_first_submission_kst**：2025-02-03
- **date_type**：论文首次提交，不等同数据集首次上线

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 主板块

推理

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）。

### 领域标签

- 约束逻辑推理

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 许可证

- **evaluation_code**：Apache-2.0（ZeroEval LICENSE）
- **dataset**：待核实（本次打开的WildEval/ZebraLogic数据卡未声明license；代码许可不代替数据授权）

> 代码许可已核实；数据集许可仍待核实，本字段为部分完成，不计为授权全部核清。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/LICENSE)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md)（访问 2026-11-08 ）。

### 论文

https://arxiv.org/abs/2502.01100

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 官方代码

https://github.com/WildEval/ZeroEval

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）。

### 数据地址

https://huggingface.co/datasets/WildEval/ZebraLogic

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）；[2](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 官方入口

https://huggingface.co/spaces/allenai/ZebraLogic

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）；[2](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 论文标题

ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

## 发起与维护

### 发起机构

University of Washington、Allen Institute for AI、Stanford University（论文署名）

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 署名合作机构

- University of Washington
- Allen Institute for AI
- Stanford University

> PDF首页署名机构，不推断额外出资合作。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）。

### 作者

- Lin, Bill Yuchen
- Bras, Ronan Le
- Richardson, Kyle
- Sabharwal, Ashish
- Poovendran, Radha
- Clark, Peter
- Choi, Yejin

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 维护方

WildEval/ZeroEval维护公开评测与汇总表；数据卡位于WildEval/ZebraLogic，官方交互榜为allenai/ZebraLogic Space（配置同时链接allenai/ZebraLogicBench）。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md)（访问 2026-11-08 ）；[3](https://huggingface.co/spaces/allenai/ZebraLogic/raw/main/README.md)（访问 2026-11-08 ）。

### 资助

Yejin Choi研究获NSF DMS-2134012部分支持（论文致谢）；不推断该grant覆盖所有作者/全部项目成本。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）。

## 设计目标

### 衡量能力

用可验证的斑马逻辑网格谜题评估约束传播、全局一致性和随搜索空间增大而变化的推理能力。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 设计背景

传统知识问答难以区分记忆与逻辑搜索；该集合用可控规模的CSP分析推理计算的扩展极限。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

## 构建方式

### 题目与数据来源

程序先采样完整网格解，再生成线索并用求解器检查唯一解；删除冗余线索后得到自然语言题目。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 构建者背景

逻辑与自然语言推理研究者设计模板和生成程序，不是每题人工出题。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 审核流程

通过约束求解验证可解性及唯一解；论文分析求解器冲突数与模型难度的对应关系。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 质量控制

2–6个房屋×2–6个属性共25种尺寸，每种40题；求解器保证唯一解，逐条尝试去除冗余线索，得到相对于逐条删除的极小线索集，不等同全局最小题面。Z3每题运行32次，平均冲突数辅助刻画搜索难度。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）。

### 去污染与泄漏防范

合成与唯一解验证降低某些数据问题，但公开集合和模板不能证明后续模型未见过测试题。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

## 数据形式

### 规模

数据卡grid_mode测试集1000个谜题；mc_mode测试集3259道选择题。两者是不同配置，不相加为独立谜题数。

来源：[1](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md)（访问 2026-11-08 ）。

### 任务形式

根据自然语言线索填写完整实体—属性对应网格，输出结构化JSON。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 模态

纯文本线索与结构化实体—属性网格；答案为JSON表格。不是图像网格识别或数学公式问答。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）；[2](https://huggingface.co/datasets/WildEval/ZebraLogic/raw/main/README.md)（访问 2026-11-08 ）。

### 语言

英文自然语言线索、实体属性和JSON字段。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）。

### 难度与类型

按网格尺寸、搜索空间与Z3冲突等划分；同尺寸不代表同等求解难度。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 公开与隐藏划分

公开评测集合；没有在材料中确认一个独立隐藏官方测试集。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

## 评测方法

### 指标

整题完整网格正确率为主要指标，单元格正确率为辅助指标。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 评分

完整网格必须所有对应关系均正确；部分格正确不能等价成整题通过。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 提示和复现设置

论文§3采用one-shot格式示例并输出推理及JSON；大多数模型同一greedy提示/解析，o1例外运行三次取最佳。当前ZeroEval汇总表的Mode/N_Mode/N_Size照表记录；即使同模型81.0%，也不将表的single标记和论文best-of-3解释强行统一。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）；[2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md)（访问 2026-11-08 ）；[3](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）。

### 官方脚本

ZeroEval：以-d zebra-grid运行；src/evaluation/zebra_grid_eval.py评分，支持本地及API推理。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md)（访问 2026-11-08 ）。

### 可比性提示

整题Puzzle Acc、Cell Acc及Small/Medium/Large/XL分开；论文one-shot与o1三次取最佳、仓库greedy/single标签、模型提供商和API检查点都需保留。官方表包含仅16题的Llama-3.1-405B@hyperbolic行，不能当1000题全量名次。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）；[2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）。

## 最新情况

### 核验时间

2026-11-08

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）；[2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md)（访问 2026-11-08 ）。

### 数据版本与当前状态

公开1000题集合；2024首发、2025论文版，未固定数据revision

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）；[2](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 论文修订与H2证据

- **arxiv_version**：arXiv v2
- **history_note**：完整历史请见arXiv元数据；初稿日期已转，不将论文修订日混为数据版本。
- **2026_h2_evidence**：- - **url**：https://arxiv.org/html/2609.27284v1
    - **date**：2026-09-23
    - **note**：Hunyuan-A13B §4.2 Reasoning及表3–4实际报告 ZebraLogic；厂商自报评测。
- **revisions**：- - **version**：v1
    - **date_kst**：2025-02-03
  - - **version**：v2
    - **date_kst**：2025-07-15
- **note**：论文修订时间已从arXiv的UTC转换为；不能当作数据发布日期。既有2026-H2证据保留原采集日期。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 ）。

### 饱和程度

当前作者表最高全量Puzzle Acc为92.6%（grok-3-mini-fast-beta-high），同一行XL为76.5%；整体高分不等同大搜索空间已解决。o3-mini-high全量91.7%、XL75.5%，按困难子集与解码预算解释。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）。

### 污染、冲突与限制

生成时保证唯一解不意味着后续模型未见公开题目。论文的尺寸分类正文用10^10为Large/XL界限，但Table1表头写10^9，存在原文阈值不一致，优先记录正文的明确尺寸列表，不自行合并类别。o1论文三次取最佳与仓库single行标签也保留差异；16题不完整结果单列。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）；[2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）。

### 后续工作与衍生

属于ZeroEval评测框架中的zebra-grid任务；不是数独，也不等同所有Einstein谜题。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）；[2](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）。

## 榜单快照

### 快照采集日

2026-11-08；厂商自报保留既有采集日

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）。

### 官方榜单

https://huggingface.co/spaces/allenai/ZebraLogic

来源：[1](https://github.com/WildEval/ZeroEval)（访问 2026-11-07 ）；[2](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）。

### 第三方覆盖

待核实

> 未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### 作者完整1000题/greedy/single/1

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | grok-3-mini-fast-beta-high | 92.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 98.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 96.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 93.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 76.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 94.63 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-high | 1.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 91.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 99.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 97.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 87.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 75.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 95.7 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-high | 0.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 88.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 99.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 97.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 88.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 60.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 90.41 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-medium | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 81.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 97.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 92.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 78.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 42.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 78.74 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-2024-12-17 | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 80.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 98.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 96.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 77.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 33.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 84.22 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-mini-fast-beta-low | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 78.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 98.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 95.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 73.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 28.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 80.54 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-R1 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 74.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 99.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 91.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 64.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 23.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 72.6 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o3-mini-2025-01-31-low | 1.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 71.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 98.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 88.21 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 59.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 17.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 75.14 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12 | 0.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 70.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 97.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 88.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 55.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 16.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 74.18 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-preview-2024-09-12-v2 | 0.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 59.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 87.5 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 76.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 39.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 12.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 70.32 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v3 | 1.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 57.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 94.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 71.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 34.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 4.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 67.73 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-3-fast-beta | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 56.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 83.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 76.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 36.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 7.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 69.87 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12-v2 | 1.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 52.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 87.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 67.5 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 24.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 3.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 52.29 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | o1-mini-2024-09-12 | 0.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 42.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 85.62 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 44.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 10.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 1.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 42.04 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v3 | 27.9 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 36.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 84.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 28.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 4.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 1.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 54.27 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20241022 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 33.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 83.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 21.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 3.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 54.34 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-sonnet-20240620 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 32.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 81.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 22.5 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 1.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 45.8 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst-fp8@together | 12.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 31.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 80.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 19.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 2.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 0.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 50.34 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-08-06 | 3.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 30.5 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 75.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 20.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 3.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 50.84 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0827 | 0.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 30.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 79.06 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 16.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 0.5 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 39.06 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@sambanova | 24.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 29.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 76.88 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 17.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 1.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 48.83 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | chatgpt-4o-latest-24-09-07 | 4.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 29.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 75.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 15.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 2.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 47.64 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Large-2 | 1.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 28.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 75.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 15.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 47.9 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-turbo-2024-04-09 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 28.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 73.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 16.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 38.72 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-2024-05-13 | 19.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 27.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 71.88 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 13.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 4.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 48.16 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | grok-2-1212 | 3.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 27.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 71.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 13.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 2.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 47.43 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4-0314 | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 27.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 73.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 12.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 48.91 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-opus-20240229 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 26.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 72.5 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 12.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 40.92 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-72B-Instruct | 11.9 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 26.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 72.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 10.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 43.39 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-32B-Instruct | 6.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 25.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 66.56 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 13.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 48.5 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro-exp-0801 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 25.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 65.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 13.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 2.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 43.56 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash-exp-0827 | 8.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 24.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 67.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 10.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 1.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 27.98 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-70B-Instruct | 43.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 22.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 63.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 8.57 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 42.46 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-chat-0628 | 5.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 22.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 62.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 7.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 38.01 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2.5-0908 | 12.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 21.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 60.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 6.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 38.32 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-72B-Instruct | 10.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 21.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 59.69 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 7.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 41.58 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0614 | 4.9 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 20.5 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 57.5 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 7.14 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 42.35 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | deepseek-v2-coder-0724 | 3.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 20.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 58.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 4.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 41.26 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-4o-mini-2024-07-18 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 19.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 55.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 6.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 31.77 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-flash | 22.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 19.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 52.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 9.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 44.59 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemini-1.5-pro | 0.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 18.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 53.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 6.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 42.61 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large-preview | 1.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 18.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 54.37 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 5.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 39.83 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | yi-large | 1.8 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 18.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 53.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 6.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 43.22 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-5-haiku-20241022 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 18.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 54.06 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 4.29 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 1.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 43.66 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-sonnet-20240229 | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 16.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 48.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 4.64 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 42.31 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-70B-Instruct | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 16.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 48.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 3.93 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 32.98 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Athene-70B | 21.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 16.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 46.56 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 5.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 41.18 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-27b-it | 1.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 14.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 43.75 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 37.87 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | claude-3-haiku-20240307 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 13.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 40.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 2.86 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 39.01 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r-plus | 0.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 13.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 39.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 1.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 33.88 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-core-20240501 | 4.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 12.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 37.81 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 2.5 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 36.79 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-9b-it | 0.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 12.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 39.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 13.68 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3.1-8B-Instruct | 61.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 12.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 36.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 1.43 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 30.67 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-7B-Instruct | 9.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 11.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 36.88 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 0.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 23.7 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Meta-Llama-3-8B-Instruct | 29.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 11.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 35.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 1.79 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 34.93 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mistral-Nemo-Instruct-2407 | 1.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 11.6 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 35.94 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 0.36 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 13.5 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3-mini-4k-instruct | 59.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 11.5 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 35.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 32.73 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-34B-Chat | 4.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 10.1 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 30.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 0.5 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 33.06 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gpt-3.5-turbo-0125 | 0.1 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 9.9 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 30.31 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 32.66 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | command-r | 1.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 9.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 28.44 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 25.67 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | reka-flash-20240226 | 18.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 9.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 27.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 20.42 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | mathstral-7B-v0.1 | 36.0 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 8.7 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 26.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 1.07 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 26.47 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Mixtral-8x7B-Instruct-v0.1 | 20.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 8.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 26.25 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 22.06 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2-7B-Instruct | 24.4 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 7.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 23.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 13.14 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.2-3B-Instruct@together | 54.5 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 6.4 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 19.38 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 0.71 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 5.98 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Phi-3.5-mini-instruct | 80.6 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 4.8 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 15.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 11.44 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Qwen2.5-3B-Instruct | 56.7 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 4.2 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 13.12 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 9.97 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | gemma-2-2b-it | 57.2 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 2.3 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 7.19 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 0.0 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 7.53 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Yi-1.5-9B-Chat | 11.3 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |

#### 作者不完整子集/greedy/single/1

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Llama-3.1-405B-Inst@hyperbolic | 25.0 % | Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 50.0 % | Small Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 33.33 % | Medium Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 0.0 % | Large Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 0.0 % | XL Puzzle Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 46.62 % | Cell Acc | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |
| — | Llama-3.1-405B-Inst@hyperbolic | 6.25 % | No answer | greedy；https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md |

#### 既有厂商自报（未刷新）

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Hunyuan-A13B | 84.7 % | accuracy slow thinking，完整题准确率，报告表3 | 2026-09-23；https://arxiv.org/html/2609.27284v1 |
| — | OpenAI-o1-1217 | 81.0 % | accuracy 同表列名，检查点按报告原样记录 | 2026-09-23；https://arxiv.org/html/2609.27284v1 |

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07 ）。

### 覆盖说明

逐格恢复当前作者仓库汇总表全部69行的7项百分比指标，共483个数值；记录total_puzzles、mode、n_mode、n_size与reason length。完整1000题与16题不完整子集分轨；不制造未公开的运行日。既有Hunyuan两行自报保留原日期及来源，不列进官方排名。

来源：[1](https://raw.githubusercontent.com/WildEval/ZeroEval/main/result_dirs/zebra-grid.summary.md)（访问 2026-11-08 ）。

## 联系方式

### 公开联系邮箱

- byuchen@uw.edu
- ronanlb@allenai.org

来源：[1](https://huggingface.co/spaces/allenai/ZebraLogic)（访问 2026-11-07 ）；[2](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 问题反馈

https://github.com/WildEval/ZeroEval/issues

来源：[1](https://github.com/WildEval/ZeroEval)（访问 2026-11-07 ）。

### 官方讨论渠道

待核实

> 未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### 隐私与数据使用

待核实

> 未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2502.01100

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）。

### SHA-256

c252c5c4c6aa7394cb97f81d7e77fd69b3ec8d374ede75c7f0189a1530a3820d

> 重新下载的原始PDF字节；既有副本未覆盖。

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）。

### 字节数

3577291

来源：[1](https://arxiv.org/pdf/2502.01100)（访问 2026-11-08 ）。

### 文件夹

- **id**：1zdfv98gUtwSgZInQe0SU-tLvBK_3TWdy
- **webViewLink**：

来源：[1]( 2026-11-07 ）。

### 其他文档

- **chinese_intro_doc**：- **id**：125u-jDuDNBy2zes2eY4ZNY425O-LzOhjWowRw-F24vs
  - **webViewLink**：
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/zebralogic.md

来源：[1]( 2026-11-07 ）。

### 原文归档

- **id**：1udO6bEUq9MMLZuhldfpfTxSwt_8H1-uv
- **webViewLink**：

来源：[1]( 2026-11-07 ）。

## 变更记录

### 本页修订

- - **date**：2026-11-07
  - **timezone**：
  - **change**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
  - **fields_updated**：- basic_info.license
    - evaluation.official_scripts
    - data_format.size
    - leaderboard.results
    - leaderboard.coverage_note
- - **date**：2026-11-08
  - **timezone**：
  - **round**：2
  - **change**：逐项打开arXiv摘要与PDF全文、官方README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

来源：[1](https://arxiv.org/abs/2502.01100)（访问 2026-11-08 ）；[2](https://raw.githubusercontent.com/WildEval/ZeroEval/main/README.md)（访问 2026-11-08 ）。
