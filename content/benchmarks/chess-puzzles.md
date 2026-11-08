# Chess Puzzles (Epoch)

> Benchmark Constitution，深度核验快照 2026-11-07。待核实不等于未公开；采集日期不等于榜单更新时间。

Epoch Chess Puzzles以100个程序新生成局面检验最佳下一着推理，输入是FEN而不是棋盘图像。此次关键变化是找到了公开的任务镜像和数据：2.1.0接受SAN写法；它与2.0.x的评分关系必须按官方changelog解释，不能沿用“只接受四字符”的旧说明。

导读依据：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）；[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 基本信息

**简称**：Chess Puzzles (Epoch)

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**全称**：Chess Puzzles (Epoch)

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**基准版本**：2.1.0已见官方运行CSV和2026-11-05镜像README；CHANGELOG标题仍标unreleased，保留文档状态冲突。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**论文版本**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**发布日期**：2025-12-10（初始发布）；v2于2026-10-14发布。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**主板块**：推理

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：编辑归档；跨领域只计主板块。

**领域**：推理

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**许可与范围**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**论文/技术报告**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**代码**：https://github.com/epoch-research/chess-puzzles-mirror

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**数据**：https://github.com/epoch-research/chess-puzzles-mirror/blob/main/bench/task/chess_puzzles/puzzles.csv

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**主页**：https://epoch.ai/benchmarks/chess-puzzles

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**论文标题**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

## 发起与维护

**发起/作者单位**：Epoch AI

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**合作关系**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**作者**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**维护方**：Epoch AI

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**资助**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

## 设计目标

**测量能力**：从文本棋局状态选择唯一最佳下一步，关注空间推理与规划。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**针对的不足**：低成本程序生成新题，避免直接依赖公开棋谱题库；不是视觉棋盘识别或完整对局水平。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 构建方式

**材料来源**：先随机走6个完整回合，再以随机Elo的Stockfish模拟；全强度Stockfish筛选唯一最佳着且未被模拟玩家选择的局面，排除明显吃子失误。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**出题背景**：由Epoch AI程序生成与评测；5位棋手仅作小样本人类基线，不是题目作者。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**审核**：Stockfish生成/筛选后接受Generality Labs外部审计；官网称2026-10审计为Verified，v2改为工具提交及确定性评分。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**质控**：Stockfish确定唯一最佳着；排除吃无防护子、低值吃高值等明显失误。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**去污染边界**：Epoch程序新生成，不来自已有题库；生成Stockfish具体版本因记录不足无法核实。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 数据形式

**规模与统计口径**：100个新生成棋局。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**任务形式**：FEN局面输入，submit_answer提交最佳走法；2.1.0除UCI起止格外接受SAN并依局面解析。另有同100题Decision变体，不能写文本的模型从合法走法中单次选择。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**模态**：文本

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**语言**：FEN为棋局编码，评测提示为英语。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**难度**：作者主观评价从相对直接到较难；5位人类各答约20题的样本测试，不能当完整题集人类基线。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**公开/保留划分**：100局面及目标着法在官方镜像puzzles.csv公开；镜像是手工刷新的内部仓库快照，不是自动实时同步。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 评测方法

**指标**：最佳走法精确匹配正确率。

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**评分**：2.1.0以python-chess按当前局面解析UCI/SAN，再对照最佳着法；2.0.x较严格字符串评分。Decision仍按UCI候选精确匹配。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**提示与运行设定**：qa_agent输出预算1,000,000 token，压缩阈值通常为模型上下文90%。公开镜像耗尽预算时按模型默认effort强制作答，内部跑分按最低effort；不能把镜像运行当内部设定完全相同。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**脚本/运行入口**：https://github.com/epoch-research/chess-puzzles-mirror/blob/main/bench/task/chess_puzzles/__init__.py

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**可比性**：1.x与2.x不可直接比较。作者称2.1.0与2.0.x可比、旧日志可重评分，但44/18,029旧样本曾因记法被误判；本快照仍分任务版本和Decision变体，避免选择性取最高分。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**当前版本证据**：version：2.1.0已见官方运行CSV和2026-11-05镜像README；CHANGELOG标题仍标unreleased，保留文档状态冲突。；evidence_2026_h2：url：https://epoch.ai/data/benchmarks.csv；date：2026-11-06；date_type：source_calendar_date；note：最新CSV中Kimi K3.1 Pro(Together,max)实跑2.1.0，45%；开始时间2026-11-06 09:59:23；不是引用次数。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**修订历史**：官网2026-10-14发布v2；镜像README称2026-11-05刷新2.1.0以接受SAN，但CHANGELOG仍写unreleased。该记录是软件历史，不冒称论文修订。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**饱和**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**争议与局限**：Stockfish生成版本因作者记录不足仍不可核实；2.1.0放宽记法，纠正少量2.0.x有效着法误判；题目与答案已公开，不能对后续模型保证无污染。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**派生/去重**：Chess Puzzles (Decision)复用同100题，属于输出/推理协议变体，不另增benchmark计数。

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 榜单快照

**快照日**：2026-11-07

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**官方榜**：https://epoch.ai/benchmarks/chess-puzzles

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**独立评测**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

### 分轨结果（不合并来源/题集/协议）

**Epoch CSV / Chess Puzzles / 2.0.0**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | GPT-6 Astra (max) | 0.74 | exact-match accuracy (0–1) |
| 2 | GPT-5.6 Sol (pro, max) | 0.68 | exact-match accuracy (0–1) |
| 2 | GPT-6.1 Sol (max) | 0.68 | exact-match accuracy (0–1) |

来源：[https://epoch.ai/data/benchmarks.csv](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**Epoch CSV / Chess Puzzles / 2.0.1**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | GPT-6 Astra (pro, max) | 0.76 | exact-match accuracy (0–1) |
| 2 | GPT-5.2 (xhigh) | 0.48 | exact-match accuracy (0–1) |
| 3 | DeepSeek V4.1 Flash 1017 (max) | 0.46 | exact-match accuracy (0–1) |

来源：[https://epoch.ai/data/benchmarks.csv](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**Epoch CSV / Chess Puzzles / 2.1.0**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | Kimi K3.1 Pro (Together, max) | 0.45 | exact-match accuracy (0–1) |

来源：[https://epoch.ai/data/benchmarks.csv](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：Success运行按Chess Puzzles和任务版本独立排序，各列前三配置；不混入Decision、不合并2.0.0/2.0.1/2.1.0。2.1.0当前仅见一条成功运行；采集日期不是实验日期，运行时间转。

来源：[1](https://epoch.ai/data/benchmarks.csv)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）

## 联系方式

**公开研究邮箱**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**Issues**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**公开社区**：https://github.com/epoch-research

来源：[1](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/README.md)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/epoch-research/chess-puzzles-mirror/main/bench/task/chess_puzzles/CHANGELOG.md)（访问 2026-11-07）；[3](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

**隐私原则**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

## 原始文件

**PDF**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**原件SHA-256**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**PDF字节数**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**目录**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

核验说明：已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

**其他文档**：type：官方方法或项目页；url：https://epoch.ai/benchmarks/chess-puzzles；accessed：2026-11-07

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

** PDF**：待核实

来源：[1](https://epoch.ai/benchmarks/chess-puzzles)（访问 2026-11-07）

## 变更记录

- date：2026-11-07；；change：首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传。
- date：2026-11-07；；change：深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
