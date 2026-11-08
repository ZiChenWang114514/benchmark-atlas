# Agents’ Last Exam v1.1

> 核验日期：2026-11-07 （）。未知保留待核实；访问日不是测量日。

已核实存在；官方资料研究快照，未知保留待核实；trending: A

用真实专业软件交付物测长时程Agent；当前v1.1公开122任务，不能用1500+收集池作计分分母。独立审查发现严重捷径问题，作者回应与修复范围须并列阅读。

## 基本信息

### 简称

Agents’ Last Exam v1.1

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 全称

Agents’ Last Exam v1.1

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 基准版本

v1.1

[来源1](https://epoch.ai/benchmarks/agents-last-exam/review)（访问2026-11-07）

### 论文版本

arXiv v4（2026-10-25修订作者/机构，摘要称科学内容不变）

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 发布日期

论文首稿2026-06-04 04:20:46 （）；当前数据v1.1具体首发日待核实。

> 字段状态：待核实

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 主板块

Agent

> 编辑归档；跨领域只计主板块。

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 领域标签

- 职业软件工作流
- 长时程电脑操作
- 科学与工程交付物验证

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 许可证

框架代码Apache-2.0；tasks、selected_tasks、sample_run等数据与内容CC-BY-4.0，分别适用LICENSE和LICENSE-DATA。

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam/blob/main/LICENSE)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2606.05405

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 官方代码

https://github.com/rdi-berkeley/agents-last-exam

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

### 数据地址

https://huggingface.co/datasets/agents-last-exam/agents-last-exam

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问2026-11-07）

### 官方入口

https://agents-last-exam.org/

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 论文标题

Agents’ Last Exam

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

## 发起与维护

### 发起方

UC Berkeley RDI与RDI Foundation

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 作者

Yiyou Sun、Xinyang Han、Weichen Zhang、Yuanbo Pang、Tianyu Wang等；完整作者表见论文

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 维护方

UC Berkeley RDI与RDI Foundation

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 资助方

Tianqiao & Chrissy Chen Institute、Snorkel AI、UniPat AI（财务及算力credit支持）

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

## 设计目标

### 衡量能力

跨专业软件的长时程、高经济价值工作流，结合GUI、CLI、文件与工具交互。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 设计背景

知识问答或短程操作不足以衡量可验证的专业交付物与实际职业流程。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

## 构建方式

### 题目来源

专家提交已经完成的真实项目，经初审、工程化dry-run与专家委员会最终质量控制。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 出题者背景

实际从业专家提供已完成项目，不是通用众包工人；论文写250+行业专家，当前主页写300+，应按材料时点区分。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://agents-last-exam.org/)（访问2026-11-07）

### 审核流程

初审→工程实现及dry-run→专家委员会最终QC；论文总体池与v1.1公开题数分开记录。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 质量控制

论文附录B.2：专家审查参考产物正确性、验收边界及上下文充分性；当前v1.1有57任务须重跑、65可保留，47改指令/43改验证/32改环境/23改数据（类别重叠）。官方release明确其复查不是完整agent验证认证。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam/blob/main/docs/releases/v1.1.md)（访问2026-11-07）

### 去污染

论文设计保留私有池并滚动替换公开任务；运行时隐藏参考答案仅在agent结束后stage。此设计不排除公开评分代码/外网答案捷径，Epoch独立审查指出实际缺陷。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）；[来源3](https://epoch.ai/benchmarks/agents-last-exam/review)（访问2026-11-07）

## 数据形式

### 题量与规模

v1.1公开122任务；主页1,500+为整体收集池而非当前公开计分题量。

[来源1](https://epoch.ai/benchmarks/agents-last-exam/review)（访问2026-11-07）

### 题型

生成文件、工作簿、设计、动画、分析等交付物并进行软件操作。

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 模态

- 文本
- 图像
- 文件
- GUI/CLI交互

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 语言

- 英语任务说明
- 中文源文档（如损失事件、监管文件）；实际任务还含其他语言材料，不宣称只有两语

[来源1](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问2026-11-07）

### 难度

v1.1分轨45 Near-Term、46 Full-Spectrum、36 Last-Exam；轨道有重叠，所以不是45+46+36个互斥样本。122个活动任务中119 CPU、3 GPU。

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

### 公开与隐藏划分

当前v1.1公开122活动任务；HF本卡只含prompt/taxonomy/software/input描述，输入文件、隐藏参考产物和镜像另发。原论文图5收集池1490=150公开+1017私有+323待QC；论文正文又用152个公开评测实例，属时点/实例口径差异，不能与v1.1混算。

[来源1](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）；[来源3](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

## 评测方法

### 指标

mean score为任务细粒度[0,1]分的平均；full-pass rate为得满分任务比例，二者都可按百分显示。当前/历史、ALL/分层/CLI、不同agent harness独立分轨。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

### 评分

任务evaluate返回[0,1]，按任务使用精确值、容差、几何或行为检查，少数视觉/语义任务使用窄rubric模型判断；mean score与full-pass分开。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 运行设置

论文历史实验每次最多5小时，主设置为GUI-as-Tool、给任务说明和CLI+GUI工具桥；当前v1.1需固定matching code/images/data与agent配置，不能把论文预算自动施加到所有社区提交。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam/blob/main/docs/releases/v1.1.md)（访问2026-11-07）

### 官方脚本

https://github.com/rdi-berkeley/agents-last-exam

> 公开ale_run、任务evaluate、固定活动任务清单及匹配资产manifest；不执行任何下载/运行命令。

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

### 可比性警示

v1.1不得与论文原v1历史结果或厂商未注明版本的得分并榜；2026-10-18被Epoch评为Flawed，须同时保留作者回应。

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 （）

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 最新版本与采用证据

```json
{
  "version": "v1.1"
  "evidence_2026_h2": [
    {
      "url": "https://openai.com/index/introducing-gpt-6-1-terra/"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "厂商实际采用ALE测量职业电脑工作；页面未给出明确v1.1结果表，不据此编造当前排名。"
    }
    {
      "url": "https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks"
      "date": "2026-10-18"
      "date_type": "source_calendar_date"
      "note": "Epoch独立审查v1.1并判Flawed；热门不等于质量通过。"
    }
  ]
}
```

> 热度等级沿候选采用；只保留已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://openai.com/index/introducing-gpt-6-1-terra/)（访问2026-11-07）；[来源2](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-06-04"
  }
  {
    "version": "v2"
    "submitted_at": "2026-06-11"
  }
  {
    "version": "v3"
    "submitted_at": "2026-10-09"
  }
  {
    "version": "v4"
    "submitted_at": "2026-10-25"
  }
]
```

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### 饱和情况

原论文最难Last-Exam轨主流配置平均full-pass不足1%，这是历史协议，不是当前v1.1榜首；第三方数据卡显示当前模型条目但metric/提交协议不完整，不能据43.2直接断言整体饱和。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问2026-11-07）

### 污染与争议

```json
{
  "independent_review": "Epoch于2026-10-18审查公开122题中的分层50题，22题(44%)可经非预期捷径得满分，判Flawed；不外推为整个私有池错误率。"
  "developer_response": "作者认为白盒攻击不等于实际自然运行，报告排除两个未向agent展示网络规则的任务后3/1,617轨迹通过被指出路径得满分，拟在后续版本强制网络隔离；这是作者自报而非独立复核。"
}
```

[来源1](https://epoch.ai/benchmarks/agents-last-exam/review)（访问2026-11-07）；[来源2](https://agents-last-exam.org/blogs/verifier-check)（访问2026-11-07）

### 版本与衍生关系

ALE-CLI是原论文Linux子集（105实例）；当前v1.1的ale_cli清单为86任务。版本与操作系统/轨道须分别记录。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 （）

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 官方榜单

https://agents-last-exam.org/leaderboard

[来源1](https://agents-last-exam.org/leaderboard)（访问2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 分轨结果

#### 论文Table1/历史152实例

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 不适用（来源内选列，非全局排名） | Codex + GPT-5.5 | 24.0 | Overall full-pass rate (%) | [原表](https://arxiv.org/abs/2606.05405)，2026-11-07 |
| 不适用（来源内选列，非全局排名） | ALE-Claw + GPT-5.5 | 23.0 | Overall full-pass rate (%) | [原表](https://arxiv.org/abs/2606.05405)，2026-11-07 |
| 不适用（来源内选列，非全局排名） | Claude Code + Fable 5 | 22.0 | Overall full-pass rate (%) | [原表](https://arxiv.org/abs/2606.05405)，2026-11-07 |



#### HF模型提交/不是HF验证

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 不适用（来源内选列，非全局排名） | moonshotai/Kimi-K3.1-Pro | 43.2 | HF卡声明v1.1 ALL，metric未命名（界面映射pass rate，待核实） | [原表](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)，2026-11-07 |



> 字段状态：待核实

> 当前官方v1.1榜页面只返回标题，未取得可核验全排名。选列历史原论文与HF提交，严格分轨；43.2不是完整官方排名结论。

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问2026-11-07）；[来源3](https://agents-last-exam.org/leaderboard)（访问2026-11-07）

### 覆盖说明

官方当前v1.1完整榜名次/更新日待核实；HF混有原始152题导出与122题当前卡，不能按HF页面总排序拼成v1.1榜。历史论文三行明确标152实例。

> 字段状态：待核实

[来源1](https://agents-last-exam.org/leaderboard)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/agents-last-exam/agents-last-exam)（访问2026-11-07）；[来源3](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

- rdi_research@berkeley.edu

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 公开反馈

https://github.com/rdi-berkeley/agents-last-exam/issues

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

### 官方社交

- https://discord.gg/jsG4Th3aVt
- https://groups.google.com/g/agenthle-news

[来源1](https://github.com/rdi-berkeley/agents-last-exam)（访问2026-11-07）

### 隐私说明/政策

https://agents-last-exam.org/privacy

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2606.05405

[来源1](https://arxiv.org/abs/2606.05405)（访问2026-11-07）

### PDF SHA-256

300b7cf737cd52288e9bf34c8400adfa8a2331a99f05878681c7117ba67e68b3

> 实际下载字节的SHA-256；不表示已有副本已替换。

[来源1](https://arxiv.org/pdf/2606.05405)（访问2026-11-07）

### PDF字节数

23530631

[来源1](https://arxiv.org/pdf/2606.05405)（访问2026-11-07）

### 文件夹

待核实

> 字段状态：待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方方法或项目页"
    "url": "https://agents-last-exam.org/"
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

### 论文副本

待核实

[来源1](https://agents-last-exam.org/)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": " ()"
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": " ()"
    最近复核
  }
]
```

[来源1](https://agents-last-exam.org/)（访问2026-11-07）
