# MirrorCode

> Benchmark Constitution，深度核查 2026-11-08。事实按所列来源及访问日期；未决项不等于官方未公开。

## 基本信息

MirrorCode将软件工程评测从修改一个补丁推进到复刻完整CLI程序：模型只能查询可执行的黑箱、查看文档与可见测试，再独立实现同样行为。全25程序论文实验与当前15程序双语言在线榜是两套配置。严格的100%-solve指标不等于代码质量评分，也不能与99%用例通过率混用。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 简称

MirrorCode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 全称

MirrorCode

> 沿用官方名称；不将论文标题臆造为全称。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 基准版本

当前main的pyproject.toml为0.1.193；运行CSV另含0.1.198。二者是不同代码快照，不能据此断言main就是最新已部署版本。

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/pyproject.toml)（访问 2026-11-08）；[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 论文版本

arXiv v2

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### 发布日期

2026-06-29（arXiv首稿时间，不等于独立数据集首发）

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### 主板块

代码

> Benchmark Constitution编辑分类。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 领域标签

- 代码

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 许可证与权利边界

MIT（官方仓库LICENSE及pyproject.toml）；不自动覆盖各目标上游项目原有权利。

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/LICENSE)（访问 2026-11-08）；[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/pyproject.toml)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2606.30182

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 代码仓库

https://github.com/epoch-research/MirrorCode/

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 数据集入口

https://github.com/epoch-research/MirrorCode/

> 公共任务定义与harness同仓发布；不是独立HF数据集。

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/README.md)（访问 2026-11-08）

### 官方主页

https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 论文标题

MirrorCode: AI can rebuild entire programs from behavior alone

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 发起与维护

### 发起方与作者单位

Epoch AI；与METR共同开发

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 合作方

METR

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 作者

- Tom Adamczewski
- David Owen
- David Rein
- Florian Brand
- Giles Edkins
- Allen Hart
- Daniel O’Connell

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### 维护方

Epoch AI

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 资助

METR grant

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

## 设计目标

### 衡量能力

从程序行为和文档端到端重建完整CLI程序，衡量长时程自主编程。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 设计背景

短补丁题和有人类引导的一次性演示难以系统比较整程序自主实现。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 构建方式

### 题目来源

25个目标程序：Unix工具、序列化、查询、生物信息、解释器、静态分析、密码学与压缩。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 出题与审阅者背景

程序任务贡献者与Epoch AI/METR评测研究团队。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 审核流程

任务贡献者审核测试；检查全部模型未解测试是否合理可解。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 质量控制

评分在独立sandbox，无参考二进制；字节级输出比较，并进行显式作弊红队。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 去污染及其证据边界

开发时无源代码、无网络；隐藏测试防查表。仍可能预训练见过开源代码，不能排除记忆贡献。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 数据形式

### 题量与版本口径

完整25程序；当前榜取Medium+Large的15程序，每个两种语言，共30任务，每任务3次。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 题型

CLI黑箱oracle、文档、可见输入输出示例；提交目标语言代码。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 模态

- 文本
- 代码
- 程序输入输出

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 语言

完整集支持Python、C、Rust、Go、OCaml、Ada；当前榜2L映射以Go/Ada为主。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 难度

Small、Medium、Large分桶；当前榜不含Small。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 公开与隐藏划分

发布22/25目标程序，共132个语言任务实例；3个目标私有。每程序另含隐藏测试，平均34%。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 评测方法

### 指标

100%-solve rate：每次尝试须通过全部端到端测试；跨目标与运行取平均。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 评分方法

评分harness在独立容器外比较stdout、stderr及exit status；必须全部端到端用例通过才算100%-solve，99%-solve只是论文另报的部分实现指标。

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 运行与提示设置

当前榜ML,+Private,2L：每题3次，每次100亿token及7天；Inspect ReAct scaffold，离线Docker，支持shell/text_editor/evaluate_testcases/submit。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 官方脚本

官方开源scaffold与22个目标程序，仓库入口见基本信息。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 可比性警示

当前榜15程序×2语言，与论文25程序/不同语言数/预算设置不直接可比；CSV还存在task version差异。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 最新情况

### 核查日期

2026-11-08

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/README.md)（访问 2026-11-08）

### 当前数据与工具版本

- **repository_package**：0.1.193（当前main）
- **observed_run_versions**：- 0.1.198；- 0.1.200
- **leaderboard_configuration**：ML,+Private,2L；与论文全25程序协议分开

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/pyproject.toml)（访问 2026-11-08）；[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 论文修订及历史证据

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）；[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 饱和情况

论文全25程序实验中8/25从未达到100%通过，4/25从未达到99%通过；这属于论文历史实验。当前ML,+Private,2L榜分数另列，不跨协议推断饱和。

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 污染、争议与限制

原论文记忆筛查在17个目标上找到潜在记忆证据，但也观察到未记忆目标被解决、记忆目标未解。离线黑箱与隐藏测试主要抑制运行时作弊，并不证明无预训练污染；另仅衡量功能，不衡量代码质量。

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 衍生与版本关系

论文将ProgramBench列为同期独立相关工作，并明确预算、提示与目标覆盖不同；它不是MirrorCode新版本。

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08（采集日，不是评测运行日）

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 官方入口

https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 第三方覆盖入口

https://epoch.ai/data/benchmarks.csv

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 分来源与协议的精确成绩

#### Epoch运行CSV / ML,+Private,2L

| 模型 / 配置 | 原始分数 | 指标与单位 |
|---|---:|---|
| Claude Opus 5.5 (high) | 0.7889 | solve_at_100 / proportion (0–1) |
| Claude Fable 5.1 (high) | 0.733 | solve_at_100 / proportion (0–1) |
| Claude Fable 5 (high) | 0.638888888888889 | solve_at_100 / proportion (0–1) |
| Gemini 4 Argon (high) | 0.5888888888888889 | solve_at_100 / proportion (0–1) |
| GPT-6 Astra (high) | 0.467 | solve_at_100 / proportion (0–1) |
| Gemini 3.7 Flash (high) | 0.4111111111111111 | solve_at_100 / proportion (0–1) |
| Grok 4.6 (xhigh) | 0.4111111111111111 | solve_at_100 / proportion (0–1) |
| Grok 4.5 (high) | 0.32222222222222224 | solve_at_100 / proportion (0–1) |
| Claude Opus 4.7 (high) | 0.3111111111111111 | solve_at_100 / proportion (0–1) |
| GPT-6 Luna (max) | 0.26666666666666666 | solve_at_100 / proportion (0–1) |
| GPT-5.6 Sol (high) | 0.2 | solve_at_100 / proportion (0–1) |
| GPT-5.4 (high) | 0.15555555555555556 | solve_at_100 / proportion (0–1) |
| GPT-5.5 (high) | 0.1 | solve_at_100 / proportion (0–1) |
| Gemini 3.1 Pro Preview (high) | 0.08888888888888888 | solve_at_100 / proportion (0–1) |
| GPT-5 (high) | 0.044444444444444446 | solve_at_100 / proportion (0–1) |

- **Claude Opus 5.5 (high)**：- **rank**：1；- **stderr**：0.0788；- **run_id**：mirrorcode-ml-2l-claude-opus-5-5；- **run_started_at**：2026-09-23；- **task_version**：0.1.198；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Claude Fable 5.1 (high)**：- **rank**：2；- **stderr**：0.0917；- **run_id**：mirrorcode-ml-2l-claude-fable-5-1；- **run_started_at**：2026-09-10；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Claude Fable 5 (high)**：- **rank**：3；- **stderr**：0.10404092940368063；- **run_id**：mirrorcode-ml-2l-claude-fable-5；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Gemini 4 Argon (high)**：- **rank**：4；- **stderr**：0.1171381252539371；- **run_id**：h7xMzFUTMGSGqUSKUpxkUW；- **run_started_at**：2026-10-14；- **task_version**：0.1.200；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **GPT-6 Astra (high)**：- **rank**：5；- **stderr**：0.1186；- **run_id**：mirrorcode-ml-2l-gpt-6-astra；- **run_started_at**：2026-08-31；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Gemini 3.7 Flash (high)**：- **rank**：6；- **stderr**：0.12157113738962926；- **run_id**：eeq6feqZLzfjfVsx4aeAWL；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Grok 4.6 (xhigh)**：- **rank**：7；- **stderr**：0.1101546131612538；- **run_id**：Hoz4Uioui4GNZaLD6fiAvD；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Grok 4.5 (high)**：- **rank**：8；- **stderr**：0.10723394129558436；- **run_id**：fiqzdAtVJVP9wdMT2QFeUn；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Claude Opus 4.7 (high)**：- **rank**：9；- **stderr**：0.09036473223803354；- **run_id**：mirrorcode-ml-2l-claude-opus-4-7；- **run_started_at**：2026-08-12；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **GPT-6 Luna (max)**：- **rank**：10；- **stderr**：0.09026709338484401；- **run_id**：WQ4gVVhGBfWoRkRwUvNYgs；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **GPT-5.6 Sol (high)**：- **rank**：11；- **stderr**：0.09229582069908972；- **run_id**：mirrorcode-ml-2l-gpt-5-6-sol；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **GPT-5.4 (high)**：- **rank**：12；- **stderr**：0.0770945044100374；- **run_id**：mirrorcode-ml-2l-gpt-5-4；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **GPT-5.5 (high)**：- **rank**：13；- **stderr**：0.06042179781166438；- **run_id**：mirrorcode-ml-2l-gpt-5-5；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **Gemini 3.1 Pro Preview (high)**：- **rank**：14；- **stderr**：0.04561939004190448；- **run_id**：mirrorcode-ml-2l-gemini-3-1-pro-preview；- **run_started_at**：2026-08-11；- **task_version**：待核实；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。
- **GPT-5 (high)**：- **rank**：15；- **stderr**：0.034375250520170986；- **run_id**：Th39ihgvLFnsDGMed7Q55b；- **run_started_at**：2026-10-22；- **task_version**：0.1.200；- **protocol_note**：按官网当前榜配置解释；CSV缺失的任务版本不补造，不能视为同版本重复测量。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

> 保留CSV十进制原字符串，未四舍五入；rank仅为该CSV已收录运行的显示顺序。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）

### 覆盖范围与时效

全量转录CSV中MirrorCode已收录运行；Epoch是共同创建者，不是独立第三方复测。运行开始时间与榜单网页更新日不同；缺失task version待核实。

[来源](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-08）；[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

- tom@epoch.ai

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### 公开反馈

https://github.com/epoch-research/MirrorCode/issues

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 官方社交

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 隐私边界

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 原始文件

### 原论文PDF

https://arxiv.org/pdf/2606.30182

> 原始论文PDF入口；未下载或上传，哈希与字节数待核实。

[来源](https://arxiv.org/abs/2606.30182)（访问 2026-11-08）

### PDF SHA-256

d0ab2a256a1ab9cee34842128aaee124c38bc2f43e95571d37aa1bec42df9e37

> 下载PDF字节的SHA-256；不冒称已重新上传。

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### PDF字节数

660665

> 直接下载的PDF文件字节数。

[来源](https://arxiv.org/pdf/2606.30182)（访问 2026-11-08）

### 文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### 其他官方材料

- - **type**：官方网页方法与榜单（非PDF）；- **url**：https://epoch.ai/benchmarks/mirrorcode

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

### PDF归档

待核实

[来源](https://epoch.ai/benchmarks/mirrorcode)（访问 2026-11-08）

## 变更记录

- - **date**：2026-11-07；- **timezone**：；- **change**：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。
- - **date**：2026-11-08；- **timezone**：；- **change**：深度核查论文abs/PDF、官方README/LICENSE、数据卡及榜单；精确区分版本、来源与协议，重写中文档案。

[来源](https://raw.githubusercontent.com/epoch-research/MirrorCode/main/README.md)（访问 2026-11-08）
