# IFBench

> Benchmark Constitution｜逐源深度核查：2026-11-08。采集日期不代表实验日期；待核实不等于未公开。

IFBench用58种未见可验证约束测试精确指令泛化，而非重命名IFEval。300条原测试、AA 294题实现、29类训练约束以及软件包83种验证器是四种不同统计口径；本页给出代码和数据各自许可。

导读依据：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-08）；[2](https://github.com/allenai/IFBench)（访问 2026-11-08）；[3](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）。

## 基本信息

### 简称

IFBench

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 全称

IFBench

> 沿用官方名称；不将论文标题臆造为全称。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 基准版本

原始300条IFBench_test、58种OOD约束；当前pip包另兼容25种经典IFEval约束，总注册83种验证器，不是测试题量83。

来源：[1](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）；[2](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）。

### 论文版本

arXiv v3

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-08）。

### 发布日期

2025-07-04（arXiv初稿日期，不是数据集的单独发布日）

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-08）。

### 主板块

语言

> Benchmark Atlas编辑分类。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 领域

```json
[
 "语言"
]
```

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 许可与使用范围

```json
{
 "code": "Apache-2.0"
 "data": "ODC-BY-1.0；依Ai2 Responsible Use Guidelines供研究教育；第三方生成输出另受对应条款约束。"
}
```

来源：[1](https://github.com/allenai/IFBench/blob/main/LICENSE)（访问 2026-11-08）；[2](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）；[3](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）。

### 论文入口

https://arxiv.org/abs/2507.02833

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 官方代码

https://github.com/allenai/IFBench

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 数据入口

https://huggingface.co/datasets/allenai/IFBench_test

来源：[1](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）；[2](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）。

### 官方主页

https://github.com/allenai/IFBench

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 论文标题

Generalizing Verifiable Instruction Following

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

## 发起与维护

### 发起方

Allen Institute for Artificial Intelligence、University of Washington

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 合作与作者单位

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 作者

```json
[
 "Valentina Pyatkin"
 "Saumya Malik"
 "Victoria Graf"
 "Hamish Ivison"
 "Shengyi Huang"
 "Pradeep Dasigi"
 "Nathan Lambert"
 "Hannaneh Hajishirzi"
]
```

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 维护方

AllenAI IFBench项目

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 资助与资源支持

NSF IIS-2044660

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

## 设计目标

### 测量能力

对58种新颖可程序验证的域外输出约束泛化，包括计数、比例、单词、句子、格式、自定义与复制。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 与既有基准的差异

IFEval的25种约束可能被过拟合；IFBench不是IFEval别名或新版本。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

## 构建方式

### 题目来源

人工收集用户反馈及核心技能需求设计约束，组合未发布的WildChat留出提示。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 出题者背景

指令遵循与后训练研究者；兼容性标注者具体资历待核实。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 审核流程

每实例人工检查提示与约束兼容，防止无法同时满足。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 质量控制

为约束编写Python验证函数；排除训练/测试约束重合。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 去污染与泄漏控制

测试58种新约束与IFTrain 29种训练约束分开，原始WildChat提示留出；公开后仍需防泄漏。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

## 数据形式

### 规模与统计口径

原始IFBench 300提示，每个含1或2约束；AA评294题。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 题型

开放文本输出，单轮任务+约束；多轮先回答原任务后按约束改写。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 模态

```json
[
 "文本"
]
```

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 语言

测试提示以英语为主，含要求日语、俄语等特定输出的约束；不能把输出语种约束误作所有题目单语声明。

来源：[1](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）。

### 难度

旨在测未见约束泛化，不以IFEval得分推断能力。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 公开与隐藏划分

IFBench评测300提示；IFTrain 29约束与训练提示为独立材料，不混成测试规模。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

## 评测方法

### 指标

strict/loose accuracy；论文报告prompt-level loose accuracy，AA采用规则评分pass@1。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 评分规则

strict直接验证，loose允许删首末行和部分字体标记后再检验；题级与约束级口径不可混用。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 提示、采样与工具设置

原论文通常temperature 0，思考模型调整token并移除思维链；DeepSeek R1用0.6/top_p.95，o3温度1。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 官方脚本

当前ifbench包可通过pip安装，命名空间ifbench.instructions、instructions_registry等；wheel含test JSONL，用ifbench.data_path访问。原论文主指标prompt-level loose accuracy。

来源：[1](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）。

### 可比性警告

AA 294题×5次不同于原始300提示；单/多轮与strict/loose差异须保留。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

## 最新情况

### 核查时间

2026-11-08

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-08）；[2](https://github.com/allenai/IFBench)（访问 2026-11-08）。

### 最新数据状态

原始IFBench_test 300题；58种OOD测试约束与29种IF-RLVR训练约束分离。当前包83验证器中25为经典IFEval，不表示原测试集扩到83类。

来源：[1](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）；[2](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）。

### 论文修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2025-07-04"
 }
 {
 "version": "v2"
 "submitted_at": "2025-08-04"
 }
 {
 "version": "v3"
 "submitted_at": "2025-11-11"
 }
]
```

> arXiv原始UTC时间已转换为；不等于数据集版本变更。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-08）。

### 饱和度与证据边界

AA294题最高83.3%；原论文300题prompt-loose轨IF-RLVR qwen2.5 7b为53.7%。不同题集/实现不能直接用于统一饱和结论。

来源：[1](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### 污染与已知问题

HF当前页面出现模型在IFBench_test上训练/微调的关联条目，证明公开测试集存在被用于训练的可见风险；不是对任一具体榜单模型泄漏的指控。基准也只测可验证形式约束，不保证语义回答质量。

来源：[1](https://huggingface.co/datasets/allenai/IFBench_test)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### 相关与衍生基准

与已收录ifeval不同：IFBench测试域外约束泛化，不能当IFEval新名字。

> 编辑去重说明；不将同基准子集、指标或版本重复计数。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

## 榜单快照

### 采集日期

2026-11-08 （采集日，不是运行或榜单更新日）

来源：[1](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### 官方结果入口

https://github.com/allenai/IFBench

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 独立评测入口

https://artificialanalysis.ai/evaluations/ifbench

来源：[1](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-07）。

### 结构化结果

```json
[
 {
 "rank": 1
 "model": "Grok 4.3 (Medium)"
 "score": "83.3"
 "metric": "pass@1 (%)"
 "track": "AA独立294题，规则验证pass@1"
 "source_url": "https://artificialanalysis.ai/evaluations/ifbench"
 "source_date": "待核实（页面快照）"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "Grok 4.20 0309 (Reasoning)"
 "score": "82.9"
 "metric": "pass@1 (%)"
 "track": "AA独立294题，规则验证pass@1"
 "source_url": "https://artificialanalysis.ai/evaluations/ifbench"
 "source_date": "待核实（页面快照）"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "MiniMax-M3"
 "score": "82.9"
 "metric": "pass@1 (%)"
 "track": "AA独立294题，规则验证pass@1"
 "source_url": "https://artificialanalysis.ai/evaluations/ifbench"
 "source_date": "待核实（页面快照）"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 1
 "model": "IF-RLVR qwen2.5 7b"
 "score": "53.7"
 "metric": "prompt-level loose accuracy (%)"
 "track": "作者论文表3，原始300题，prompt-level loose"
 "source_url": "https://arxiv.org/pdf/2507.02833"
 "result_type": "历史论文；表3列出模型子集内排序"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 2
 "model": "IF-RLVR TULU-DPO 8b"
 "score": "44.6"
 "metric": "prompt-level loose accuracy (%)"
 "track": "作者论文表3，原始300题，prompt-level loose"
 "source_url": "https://arxiv.org/pdf/2507.02833"
 "result_type": "历史论文；表3列出模型子集内排序"
 "snapshot_date": "2026-11-08 "
 }
 {
 "rank": 3
 "model": "TULU"
 "score": "28.9"
 "metric": "prompt-level loose accuracy (%)"
 "track": "作者论文表3，原始300题，prompt-level loose"
 "source_url": "https://arxiv.org/pdf/2507.02833"
 "result_type": "历史论文；表3列出模型子集内排序"
 "snapshot_date": "2026-11-08 "
 }
]
```

来源：[1](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### 覆盖与局限

AA294题与原论文300题分轨；HF自动模型成绩来自第三方模型卡，不作为作者维护实时总榜；不混淆83种软件验证器与58种OOD测试约束。

来源：[1](https://artificialanalysis.ai/evaluations/ifbench)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）；[3](https://github.com/allenai/IFBench/blob/main/README.md)（访问 2026-11-08）。

## 联系方式

### 官方公开邮箱

```json
[
 "valentinap@allenai.org"
]
```

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### 仓库反馈

https://github.com/allenai/IFBench/issues

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 官方社区

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 隐私与联系边界

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

## 原始文件

### 论文PDF

https://arxiv.org/pdf/2507.02833

> 原始论文PDF入口；未下载或上传，哈希与字节数待核实。

来源：[1](https://arxiv.org/abs/2507.02833)（访问 2026-11-07）。

### PDF SHA-256

a998a59fa3697631b508e9555ea5eb7d529f5a52512e65b2ad93882cc591dde9

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### PDF字节数

```json
2757383
```

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2507.02833)（访问 2026-11-08）。

### 已有文件夹

待核实

> 已检查所列材料，尚未精确核实此字段；不代表官方没有公开。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 其他官方文档

```json
[
 {
 "type": "官方网页方法与榜单（非PDF）"
 "url": "https://github.com/allenai/IFBench"
 }
]
```

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

### 已有 PDF归档

待核实

> 按本批范围不上传；不是官方未公开。

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）。

## 变更记录

### 历次核查

```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-08"
 最近复核
 }
]
```

来源：[1](https://github.com/allenai/IFBench)（访问 2026-11-07）；[2](https://arxiv.org/abs/2507.02833)（访问 2026-11-08）；[3](https://github.com/allenai/IFBench)（访问 2026-11-08）。
