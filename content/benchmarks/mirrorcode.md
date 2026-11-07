# MirrorCode

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。已核验存在；中文研究快照；note: trending: A；未核实保留标记

## 基本信息

### 简称

MirrorCode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 全称

MirrorCode

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 论文版本

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 主板块

代码

> Benchmark Atlas编辑分类。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 领域标签

- 代码

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 许可证

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2606.30182

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 代码

https://github.com/epoch-research/MirrorCode/

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 数据集

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 官方主页

https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 论文标题

MirrorCode: AI can rebuild entire programs from behavior alone

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 发起与维护

### 发起方

Epoch AI；与METR共同开发

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 合作方

METR

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 作者

- Tom Adamczewski
- David Owen
- David Rein
- Florian Brand
- Giles Edkins
- Allen Hart
- Daniel O’Connell

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-07）

### 维护方

Epoch AI

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 资助

METR grant

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-07）

## 设计目标

### 衡量能力

从程序行为和文档端到端重建完整CLI程序，衡量长时程自主编程。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 设计背景

短补丁题和有人类引导的一次性演示难以系统比较整程序自主实现。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 构建方式

### 题目来源

25个目标程序：Unix工具、序列化、查询、生物信息、解释器、静态分析、密码学与压缩。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 出题者背景

程序任务贡献者与Epoch AI/METR评测研究团队。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 审核

任务贡献者审核测试；检查全部模型未解测试是否合理可解。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 质量控制

评分在独立sandbox，无参考二进制；字节级输出比较，并进行显式作弊红队。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 去污染

开发时无源代码、无网络；隐藏测试防查表。仍可能预训练见过开源代码，不能排除记忆贡献。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 数据形式

### 题量与规模

完整25程序；当前榜取Medium+Large的15程序，每个两种语言，共30任务，每任务3次。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 题型

CLI黑箱oracle、文档、可见输入输出示例；提交目标语言代码。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 模态

- 文本
- 代码
- 程序输入输出

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 语言

完整集支持Python、C、Rust、Go、OCaml、Ada；当前榜2L映射以Go/Ada为主。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 难度

Small、Medium、Large分桶；当前榜不含Small。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 公开与隐藏划分

发布22/25目标程序，共132个语言任务实例；3个目标私有。每程序另含隐藏测试，平均34%。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 评测方法

### 指标

100%-solve rate：每次尝试须通过全部端到端测试；跨目标与运行取平均。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 评分

参考与候选stdout/stderr一致才能通过；不以99%部分实现替代100%解题指标。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 运行设置

当前榜ML,+Private,2L：每题3次，每次100亿token及7天；Inspect ReAct scaffold，离线Docker，支持shell/text_editor/evaluate_testcases/submit。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 官方脚本

官方开源scaffold与22个目标程序，仓库入口见基本信息。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 可比性警示

当前榜15程序×2语言，与论文25程序/不同语言数/预算设置不直接可比；CSV还存在task version差异。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 当前版本与2026后半年证据

- **version**：待核实
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://epoch.ai/data/benchmarks.csv", "date": "2026-11-07", "date_type": "observed_on", "note": "Epoch公开CSV在2026年8–10月有15条MirrorCode运行，当前ECI纳入；这证明持续评测，不等于15家机构采纳。"}, {"url": "https://epoch.ai/data/eci-documentation/data", "date": "2026-11-07", "date_type": "observed_on", "note": "Epoch公开CSV在2026年8–10月有15条MirrorCode运行，当前ECI纳入；这证明持续评测，不等于15家机构采纳。"}]

> Epoch公开CSV在2026年8–10月有15条MirrorCode运行，当前ECI纳入；这证明持续评测，不等于15家机构采纳。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；[来源](https://epoch.ai/data/eci-documentation/data)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 污染、争议与限制

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 衍生与版本关系

与当前100条目的id、名称、版本字段去重后未收录

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 为什么近期热门

Epoch公开CSV在2026年8–10月有15条MirrorCode运行，当前ECI纳入；这证明持续评测，不等于15家机构采纳。

[来源](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）；[来源](https://epoch.ai/data/eci-documentation/data)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 官方榜单入口

https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 第三方覆盖

https://epoch.ai/data/benchmarks.csv

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

### 核验结果

| 顺序 | 模型 / 配置 | 分数 | 指标 | 来源自写更新时间 |
|---|---|---:|---|---|
| 1 | Claude Opus 5.5 (high) | 0.7889 | solve_at_100 proportion (0–1) | 待核实（页面未明示榜表更新时间） |
| 2 | Claude Fable 5.1 (high) | 0.733 | solve_at_100 proportion (0–1) | 待核实（页面未明示榜表更新时间） |
| 3 | Claude Fable 5 (high) | 0.638888888888889 | solve_at_100 proportion (0–1) | 待核实（页面未明示榜表更新时间） |

- Claude Opus 5.5 (high)：stderr 0.0788；task version 0.1.198；运行开始2026-09-23 01:42 KST

- Claude Fable 5.1 (high)：stderr 0.0917；CSV task version为空；运行开始2026-09-10 22:19:30 KST

- Claude Fable 5 (high)：stderr 0.1040409294；CSV task version为空；运行开始2026-08-11 01:12:44 KST

> 从Epoch公开CSV按mean_score降序提取已有运行，不冒称全部同一软件版本；页面定义的榜配置另列。source_date为各行运行开始而非网页更新日。

[来源](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

### 覆盖与时效

Epoch是基准共同创建者及运行机构，不称独立复核；已记录不同task version与缺失版本。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- tom@epoch.ai

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2606.30182

> 原始论文PDF入口；未下载或上传Drive，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### Drive文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方网页方法与榜单（非PDF）", "url": "https://epoch.ai/benchmarks/mirrorcode"}

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

### Drive PDF归档

待核实

> 按本批范围不上传Drive；不是官方未公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。"}

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-07）
