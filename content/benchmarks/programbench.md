# ProgramBench

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

已核验存在；11节研究快照；note: trending: A；未知字段保留待核实

## 基本信息

### 简称

ProgramBench

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 全称

ProgramBench

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 基准版本

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 论文版本

v1（本轮返回正文版本）

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 主板块

代码

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 子领域



[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 许可

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2605.03546

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 代码

https://github.com/facebookresearch/ProgramBench

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 数据

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 官网

https://programbench.com

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 论文标题

ProgramBench: Can Language Models Rebuild Programs From Scratch?

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## 发起与维护

### 发起方

- Meta Superintelligence Labs
- Stanford University
- Harvard University

[来源](https://programbench.com)（访问 2026-11-07）

### 合作方

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 作者

John Yang、Kilian Lieret、Jeffrey Ma、Parth Thakkar、Dmitrii Pedchenko 等（完整作者见论文）

[来源](https://programbench.com)（访问 2026-11-07）

### 维护方

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 资助

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 设计目标

### 衡量能力

仅给可执行程序与文档，自行设计架构、选择语言并从零实现行为等价程序。

[来源](https://programbench.com)（访问 2026-11-07）

### 设计背景

不提供函数签名、类骨架或预设目录，区别于局部bug修复及填空式整仓生成。

[来源](https://programbench.com)（访问 2026-11-07）

## 构建方式

### 题目来源

从开源仓库编译原程序，移除源码和测试，只保留二进制与使用文档。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 出题人背景

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 审核流程

agent探索原程序，覆盖率引导fuzz生成行为断言，收集现有行为测试。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 质量控制

静态linter筛弱断言；删除不能稳定通过原程序或能通过dummy程序的测试。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 去污染

离线沙箱、原二进制仅可执行，不允许反编译、源码检索或包装原程序；原仓库公开带来潜在记忆风险。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## 数据形式

### 规模

200任务；论文版本共248,853测试函数。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 题型

完整源码项目与build脚本生成，行为测试比较标准输出/错误、退出码与文件副作用。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 模态

- 程序二进制
- 文档
- 源代码
- 终端交互

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 语言

参考项目以Rust、Go、C/C++为主，另有Java和Haskell；模型可自选实现语言。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 难度

从小型CLI到FFmpeg、SQLite和PHP，原项目规模差异较大。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 公开与隐藏划分

200公开任务；推理时隐藏测试不向agent显示；公开任务不等于允许查看隐藏断言。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

## 评测方法

### 指标

Fully Resolved/Resolved：全部隐藏行为测试通过；Almost Resolved：至少95%测试通过；Raw Pass Rate：任务内测试通过率平均。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 评分

编译提交实现后用行为测试比较原程序，不靠LLM主观评分；有限测试不能证明所有输入等价。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 提示与运行设置

mini-SWE-agent、1000步、6小时，离线cleanroom；Vals统一bash工具与沙箱。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 评测脚本

官方代码入口为facebookresearch/ProgramBench，论文提供数据构建和评测流程。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 可比性警示

官网2026-10-22与Vals 2026-11-05的样本/运行结果分开；Fully Resolved不是Raw Pass Rate，也不是95%测试阈值。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度A：有当前独立评测或多来源采用证据；按下列日期类型解读。

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 当前版本与热门证据

- **version**：待核实
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://programbench.com", "date": "2026-10-22", "note": "官方榜单自写更新日。"}, {"url": "https://www.vals.ai/benchmarks/programbench", "date": "2026-11-05", "note": "Vals独立评测榜单自写更新日。"}]

> A：原始基准与独立评测材料交叉核验；不将仅引用等同独立实跑。

[来源](https://programbench.com)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 污染与争议

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 衍生及版本关系

与现有100条slug核对未发现同名旧版；不将评测实现或分项重复计为新benchmark。

> 编辑去重结论；版本关系以下述专门说明为准。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 官方榜单

https://programbench.com

[来源](https://programbench.com)（访问 2026-11-07）

### 独立评测入口

https://www.vals.ai/benchmarks/programbench

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "Claude Opus 5.5 (xhigh)", "score": "18.5%", "metric": "官方Resolved", "source_url": "https://programbench.com", "source_date": "2026-10-22", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}
- {"rank": 2, "model": "Claude Fable 5.1 (xhigh)", "score": "9.0%", "metric": "官方Resolved", "source_url": "https://programbench.com", "source_date": "2026-10-22", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}
- {"rank": 3, "model": "Muse Wonder Full", "score": "8.5%", "metric": "官方Resolved", "source_url": "https://programbench.com", "source_date": "2026-10-22", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}

[来源](https://programbench.com)（访问 2026-11-07）

### 覆盖与时效说明

官方前三如上；Vals 2026-11-05前三为Claude Opus 5.5 18.50%、Claude Fable 5.1 7.00%、Claude Sonnet 5.5 6.50%，独立运行差异并列保留，不合并为一张榜。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- johnby@meta.com
- klieret@meta.com

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2605.03546

> 官方论文正文对应的PDF入口；本轮未下载，故hash与字节数待核实。

[来源](https://arxiv.org/abs/2605.03546)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Drive资料夹

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方介绍/协议", "url": "https://www.vals.ai/benchmarks/programbench"}

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）

### Drive PDF归档

待核实（本任务未上传）

## 变更记录

### changelog

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传Drive。"}

[来源](https://www.vals.ai/benchmarks/programbench)（访问 2026-11-07）
