# Benchmark Atlas · 2026H2 百项候选清单

核验窗口：2026-07-01—2026-11-07；采集日：2026-11-07。

共100项：已有24项、新增76项；自然科学40项（40%）；34个不同的日期化证据来源。仅候选清单，未构建/部署条目。

## 分区与名称

### 物理（12）

GPQA、SciBench、SciEval、SciCode、PHYBench、UGPhysics、PhysicsEval、OlympiadBench、PDEBench、The Well、SciRigor、ScienceIDE-Hard

### 化学（4）

ChemBench、MoleculeNet、ChemLLMBench、ChemDIRT

### 生物与医学（12）

LAB-Bench、BixBench、BioProBench、PubMedQA、MedQA、MedMCQA、SciGym、OmicsBench、GenoTEX、BioCoder、Genome-Bench、BAISBench

### 地球与天文（6）

AstroBench、GEO-Bench、ClimateBench、WeatherBench、WeatherBench 2、AstroMMBench

### 材料（6）

Matbench、Matbench Discovery、JARVIS-Leaderboard、CHIPS-FF、AtomBench、QMOF

### 语言（12）

MMLU、MMLU-Pro、MMLU-Redux、C-Eval、MMLU-ProX、MMMLU、IFEval、SysBench、LongBench v2、RULER、FRAMES、AA-Omniscience

### 推理（7）

BIG-Bench Hard (BBH)、ZebraLogic、DROP、HellaSwag、WinoGrande、ARC-Challenge、Humanity’s Last Exam (HLE)

### 数学（7）

MATH、GSM8K、AIME、MathQA、AQuA-RAT、FrontierMath、miniF2F

### 代码（10）

EvalPlus、MultiPL-E、MBPP、CRUXEval、LiveCodeBench、FullStackBench、HumanEvalFix、SWE-bench Verified、Terminal-Bench、FrontierCode

### 多模态（10）

MMMU、MMBench、MathVista、MathVerse、ScienceQA、ChartQA、CharXiv、RealWorldQA、Video-MME、MMAU

### Agent（9）

GAIA、AgentBench、WebArena、Berkeley Function Calling Leaderboard (BFCL)、τ-bench、AutomationBench-AA、AA-Briefcase、CORE-Bench、PaperBench

### 安全（5）

TruthfulQA、HarmBench、StrongREJECT、AdvBench、RAG-Safety-Bench

## 现有条目审计

24/24均达到“2026H2仍被引用/使用”的门槛，无需排除。部分只有H2引用而非新实验，不能据此宣称有新榜单。

## 证据边界

- 主要使用固定版本arXiv全文、ACL正式PDF、期刊正式版及Artificial Analysis日期化评测文章。
- 来源发布/版本日期与采集日期分开。ACL仅给月份时原样保留，未编造具体日。
- 本名单不是“全球引用最多的100项”；是满足时效门槛、兼顾覆盖与自然科学优先的建设清单。
- 其他候选与合并去重理由见JSON的considered_but_dropped。
- JSON采用顶层对象，以同时容纳benchmarks（100项数组）、审计、分区统计及未选候选。
