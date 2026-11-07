# Code Migration v1.1

> Benchmark Constitution · 深度核验快照 2026-11-07。待核实不等于未公开；采集日期不等于榜单更新时间。

Vals Code Migration v1.1检验完整程序迁移后的行为保持：30个CLI仓库分别迁到四种其他语言，再加10个COBOL→Java仓库。主分按40个源仓库等权，绝不是130次迁移简单等权；可读性等代码质量只作独立诊断。

导读依据：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）；[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 基本信息

**简称**：Code Migration v1.1

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**全称**：Code Migration v1.1

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：沿用官方名称；不将论文标题臆造为全称。

**基准版本**：v1.1

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**论文版本**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**发布日期**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：页面2026-10-30是本榜更新日；不足以核实v1.1首次发布日。

**主板块**：代码

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：Benchmark Constitution编辑分类。

**领域**：代码

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**许可与范围**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**论文/技术报告**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**代码**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**数据**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**主页**：https://www.vals.ai/benchmarks/code-migration-v1-1

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**论文标题**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

## 发起与维护

**发起/作者单位**：Vals AI

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**合作关系**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**作者**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**维护方**：Vals AI

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**资助**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

## 设计目标

**测量能力**：把完整可运行程序迁移到另一语言并忠实复现行为，含遗留COBOL现代化。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**针对的不足**：短代码翻译不能代表仓库级CLI迁移与有状态遗留业务系统。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 构建方式

**材料来源**：CLI为30个开源仓库；COBOL为10仓库，混合开源程序与为本基准合成的业务系统。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**出题背景**：Vals AI构建工程迁移基准；官方方法说明COBOL部分含为评测合成的业务系统，具体出题人员履历仍待核实。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**审核**：隐藏行为测试评分前进行独立反作弊审查；核对目标语言并拒绝包装原程序、复制参考产物或硬编码预期输出。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**质控**：隐藏行为测试前进行反作弊检查：禁止原程序包装、参考材料复制、硬编码输出，并检查目标语言。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**去污染边界**：隐藏行为测试不向模型公开；源仓库本身公开，不能保证预训练未见。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 数据形式

**规模与统计口径**：CLI 30源仓库各迁到另外4语言，共120迁移；COBOL→Java另10仓库。headline按40源仓库等权，不是按130任务简单等权。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**任务形式**：提供源程序及指令，提交目标语言实现和Dockerfile。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**模态**：代码；文本；CLI执行

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**语言**：CLI源/目标Python、Java、Kotlin、Rust、C++；另有COBOL→Java。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**难度**：CLI完整仓库跨语言迁移；COBOL→Java覆盖文件格式、批处理、终端接口与持久状态。不等同函数级翻译，官方未给统一数值难度级别。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**公开/保留划分**：30个CLI源仓库来自开源项目，COBOL为开源和合成混合；隐藏行为测试明确不向模型展示。完整题目与数据集下载授权仍待核实。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 评测方法

**指标**：Hidden-test pass rate (%)；代码质量另行诊断，不影响主分。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**评分**：构建提交Docker镜像运行隐藏测试；CLI先对每源仓库4目标取均值，再40源仓库等权，CLI:COBOL权重3:1。作弊提交0。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**提示与运行设定**：v1.1统一Pi agent harness，离线sandbox，给源程序与任务指令。具体token/时限待核实。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**脚本/运行入口**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**可比性**：v1.1从mini-SWE-agent换Pi并修订隐藏测试；任务不变但与v1分数不可直接比较。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07 KST / Asia/Seoul

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**当前版本证据**：version：v1.1；heat_confidence：B；evidence_2026_h2：url：https://www.vals.ai/benchmarks/code-migration-v1-1；date：2026-11-07；date_type：observed_on；note：Vals榜明确更新2026-10-30并列29模型。热度B，主要单一机构当前榜，不称全行业快速增长。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：Vals榜明确更新2026-10-30并列29模型。热度B，主要单一机构当前榜，不称全行业快速增长。

**修订历史**：v1.1更换Pi harness并修订隐藏测试；独立论文与修订历史待核实。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**饱和**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**争议与局限**：测试通过只表示被测行为；可读性、文档、文件结构和语言习惯是独立review维度，不能将隐藏测试分当代码质量。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**派生/去重**：v1.1沿用v1任务，换Pi harness并修订隐藏测试；作为协议版本保留，不把v1与v1.1算成两项独立benchmark。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 榜单快照

**快照日**：2026-11-07 KST / Asia/Seoul

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**官方榜**：https://www.vals.ai/benchmarks/code-migration-v1-1

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**独立评测**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

### 分轨结果（不合并来源/题集/协议）

**Vals / v1.1 / Overall**

| 排名 | 模型/配置 | 分数 | 指标 |
|---:|---|---:|---|
| 1 | Claude Sonnet 5.5 | 86.88 | hidden-test pass rate (%) |
| 2 | Claude Opus 5.5 | 81.01 | hidden-test pass rate (%) |
| 3 | GPT-6 Astra | 80.58 | hidden-test pass rate (%) |
| 4 | GPT-6.1 Sol | 77.32 | hidden-test pass rate (%) |
| 5 | Wonder | 72.36 | hidden-test pass rate (%) |
| 6 | Gemini 4 Argon | 70.8 | hidden-test pass rate (%) |
| 7 | DeepSeek V4.1 Flash 1017 | 67.52 | hidden-test pass rate (%) |
| 8 | Wonder Full | 62.79 | hidden-test pass rate (%) |
| 9 | DeepSeek V4.1 Flash | 58.94 | hidden-test pass rate (%) |
| 10 | Qwen 3.8 Max 0902 | 57.19 | hidden-test pass rate (%) |
| 11 | GLM 5.3 | 55.07 | hidden-test pass rate (%) |
| 12 | Grok 4.7 | 53.22 | hidden-test pass rate (%) |
| 13 | Claude Haiku 5.5 | 52.36 | hidden-test pass rate (%) |
| 14 | DeepSeek V4 Pro 0813 | 51.99 | hidden-test pass rate (%) |
| 15 | GLM 5.3 Flash | 51.65 | hidden-test pass rate (%) |
| 16 | MiMo V2.6 Pro | 48.79 | hidden-test pass rate (%) |
| 17 | Step 5 Preview | 47.0 | hidden-test pass rate (%) |
| 18 | GPT-6 Luna | 46.67 | hidden-test pass rate (%) |
| 19 | Hy4 Preview | 45.36 | hidden-test pass rate (%) |
| 20 | MiMo V2.6 Flash | 39.55 | hidden-test pass rate (%) |
| 21 | Mercury 3 | 39.26 | hidden-test pass rate (%) |
| 22 | Gemini 3.8 Flash | 38.65 | hidden-test pass rate (%) |
| 23 | Kimi K3 | 28.59 | hidden-test pass rate (%) |
| 24 | Muse Spark Open | 26.89 | hidden-test pass rate (%) |
| 25 | Beam 1.0 | 22.85 | hidden-test pass rate (%) |
| 26 | MiniMax-M3 | 20.9 | hidden-test pass rate (%) |
| 27 | Nemotron 3.5 Super VL | 16.44 | hidden-test pass rate (%) |
| 28 | Inkling Small | 10.43 | hidden-test pass rate (%) |
| 29 | Inkling | 8.82 | hidden-test pass rate (%) |

来源：[https://www.vals.ai/benchmarks/code-migration-v1-1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）；其他运行ID、时间、误差及配置见配套JSON。

**覆盖范围**：当前官方Overall表29个模型全部录入；分数保留网页百分比精度，不反推130任务简单均值。页面标更新2026-10-30；CLI、COBOL及effort曲线不混入Overall排名。

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 联系方式

**公开研究邮箱**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**Issues**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**公开社区**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**隐私原则**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

## 原始文件

**PDF**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**原件SHA-256**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**PDF字节数**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**Drive目录**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

核验说明：已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

**其他文档**：type：官方网页方法与榜单（非PDF）；url：https://www.vals.ai/benchmarks/code-migration-v1-1

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

**Drive PDF**：待核实

来源：[1](https://www.vals.ai/benchmarks/code-migration-v1-1)（访问2026-11-07）

## 变更记录

- date：2026-11-07；timezone：KST / Asia/Seoul；change：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。
- date：2026-11-07；timezone：Asia/Seoul；change：第2轮深度核验：重开论文摘要/PDF、官方仓库与可得数据卡/榜单，分来源/版本/提示轨保存精确结果，改写中文11节；抓取失败及未知保留。
