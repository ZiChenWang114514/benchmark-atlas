# VIALS

> 核查：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

已核验存在；11节研究快照；note: trending: A；未知字段保留待核实

## 基本信息

### 简称

VIALS

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 全称

Visual Interpretation of Artifacts in the Life Sciences

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 基准版本

2.0.0

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 论文版本

v2，2026-09-19

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 发布日期

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 主板块

多模态

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 子领域

- 科学图像
- 物理
- 化学
- 生物与医学
- 材料

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 许可

数据及图像CC BY 4.0（逐图引用attributions.csv原始来源）；评测代码另为MIT。

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2608.21357

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 代码

https://github.com/Handshake-AI-Research/VIALS

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 数据

https://huggingface.co/datasets/Handshake-AI-Research/VIALS

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 官网

https://joinhandshake.com/research/benchmarks/vials/

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 论文标题

VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

## 发起与维护

### 发起方

Handshake AI

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 合作方

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 作者

- Elaine Lau
- Thanuka Udumulla
- Lee Izhaki-Tavor
- Francisco Guzmán
- Nicholas Magazine
- Jonas Mueller

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 维护方

Handshake AI

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 资助

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

## 设计目标

### 衡量能力

解释生命科学专业流程中的凝胶、流式图、质粒图、系统发育树与分子结构等真实视觉证据。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 设计背景

强调日常科研视觉产物而非教材考试图或只描述自然图片，检验视觉定位及领域解释。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

## 构建方式

### 题目来源

未发表实验数据、科学软件生成产物、CC-BY开放论文图；专家依自身工作编写问题与参考答案。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 出题人背景

31名专业贡献者，87%具博士级训练，74%有超过6年生命科学行业经验。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 审核流程

第二位、经常第三位领域专家盲答；独立答案一致或复审达共识方保留。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 质量控制

检查图像现实性、可答性、任务多样性；GPT-5-mini裁判与4685个人工标注答复的一致率为99.9%（作者自报）。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 去污染

构建时检查任务未在线出现；数据卡要求不入训练语料；未来额外任务私有开发，不当作本版题量。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

## 数据形式

### 规模

161任务；HF test分片parquet。

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 题型

一个或多个图像加问题，开放式短答案，含可接受数值范围。

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 模态

- 科学图像
- 文本问题
- 短文本答案

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 语言

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 难度

面向受过相关训练的专业科学家日常任务；不等于全科研流程难度。

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

### 公开与隐藏划分

当前161题公开；模型输入只能用images与question，answer及数值区间仅供评分。

[来源](https://huggingface.co/datasets/Handshake-AI-Research/VIALS)（访问 2026-11-07）

## 评测方法

### 指标

官方直接视觉评测为三次独立rollout平均accuracy；AA Agent实现headline为pass^3。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 评分

官方抽取最终ANSWER:后答案，用GPT-5-mini判科学语义等价；标签歧义时带图复核。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 提示与运行设置

论文直接VLM设temperature 1.0、32768完成token、每题3次；AA用Stirrup代码/看图工具、无网络，GPT-6 Luna medium裁判。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 评测脚本

Handshake-AI-Research/VIALS；数据卡明确代码MIT。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 可比性警示

直接视觉、官方工具辅助与AA工具辅助须分开；AA pass^3不等于官网平均accuracy，不能凭较高分说同协议性能提升。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度A：有当前独立评测或多来源采用证据；按下列日期类型解读。

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 当前版本与热门证据

- **version**：2.0.0
- **heat_confidence**：A
- **evidence_2026_h2**：[{"url": "https://artificialanalysis.ai/evaluations/vials-aa", "date": "2026-11-07", "note": "AA当前独立工具辅助评测，观察日。"}, {"url": "https://arxiv.org/abs/2608.21357", "date": "2026-09-19", "note": "论文v2含工具辅助分析；论文版本日期。"}]

> A：原始基准与独立评测材料交叉核验；不将仅引用等同独立实跑。

[来源](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-07）

### 修订历史

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 饱和情况

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 污染与争议

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 衍生及版本关系

与现有100条slug核对未发现同名旧版；不将评测实现或分项重复计为新benchmark。

> 编辑去重结论；版本关系以下述专门说明为准。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 官方榜单

https://joinhandshake.com/research/benchmarks/vials/

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 独立评测入口

https://artificialanalysis.ai/evaluations/vials-aa

[来源](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "Gemini 4 Carbon (High)", "score": "64%", "metric": "VIALS-AA agent pass^3", "source_url": "https://artificialanalysis.ai/evaluations/vials-aa", "source_date": "待核实", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}
- {"rank": 2, "model": "GPT-6 Astra (Max)", "score": "63%", "metric": "VIALS-AA agent pass^3", "source_url": "https://artificialanalysis.ai/evaluations/vials-aa", "source_date": "待核实", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}
- {"rank": 3, "model": "Claude Opus 5.5 (Max, Default Fallback)", "score": "61%", "metric": "VIALS-AA agent pass^3", "source_url": "https://artificialanalysis.ai/evaluations/vials-aa", "source_date": "待核实", "collected_at": "2026-11-07 KST", "result_type": "公开榜单快照"}

[来源](https://artificialanalysis.ai/evaluations/vials-aa)（访问 2026-11-07）

### 覆盖与时效说明

AA上述为三次均正确的pass^3；Handshake官网直接accuracy前三另为GPT-6 Astra 49.9%、GPT-6.1 Sol 49.1%、Gemini 4 Argon 47.2%。数据卡domain文字写九类，而预览/论文/AA为八类，本页按论文八类，不静默修改来源。榜单自写更新时间待核实。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

- elaine.lau@joinhandshake.com
- nicholas.magazine@joinhandshake.com
- jonas.mueller@joinhandshake.com

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### 公开反馈

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 隐私政策

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2608.21357

> 官方论文正文对应的PDF入口；本轮未下载，故hash与字节数待核实。

[来源](https://arxiv.org/abs/2608.21357)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### PDF字节数

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### Drive资料夹

待核实

> 已检查所引官方材料，本轮未完成精确核验；不代表官方未公开。

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方介绍/协议", "url": "https://joinhandshake.com/research/benchmarks/vials/"}

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）

### Drive PDF归档

待核实（本任务未上传）

## 变更记录

### changelog

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传Drive。"}

[来源](https://joinhandshake.com/research/benchmarks/vials/)（访问 2026-11-07）
