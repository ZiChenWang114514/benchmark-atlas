# PaperBench

> Benchmark Constitution，核验 2026-11-08。未知保持“待核实”；访问日不等于实验日。

PaperBench要求agent从研究论文出发编写代码、执行实验并复现目标结论。层级rubric由原论文作者协作制定；完整复现、只做代码开发的Code-Dev以及不同运行预算不构成同一个排行榜。

来源：[原始说明](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）；[结果证据](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）

## 基本信息

### 简称

PaperBench

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 全称

PaperBench

说明：保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 基准版本

原始20篇ICML2024论文套件

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 论文版本

arXiv v3

说明：论文修订版本不等同数据集版本。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 发布日期

2025-04-03 00:55:24

说明：首次 arXiv 论文提交时间，已转；不自动视为数据集首发时间。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 主板块

Agent

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 领域标签

- AI论文复现Agent

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 许可与适用范围

frontier-evals根目录LICENSE.md为MIT；论文、ICML原文、外部数据与不可自动再分发的JudgeEval文件须分别遵守其授权，不由MIT替代。

来源：[1](https://raw.githubusercontent.com/openai/frontier-evals/main/LICENSE.md)（访问2026-11-08，）；[2](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）

### 论文

https://arxiv.org/abs/2504.01848

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 代码仓库

https://github.com/openai/frontier-evals

说明：论文链接openai/preparedness；本次GitHub元数据请求跳转至openai/frontier-evals。仓库根代码许可不自动等同每篇论文及rubric许可。

来源：[1](https://github.com/openai/frontier-evals)（访问2026-11-08，）

### 数据地址

https://github.com/openai/frontier-evals/tree/main/project/paperbench/data

说明：官方README说明数据由Git-LFS分发；JudgeEval部分材料不可自动再分发。

来源：[1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问2026-11-07，）

### 官方主页

https://openai.com/index/paperbench/

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 论文标题

PaperBench: Evaluating AI's Ability to Replicate AI Research

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

## 发起与维护

### 发起与机构归属

OpenAI

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 合作关系

被复现ICML论文作者共同制定rubric并签核；不意味着共同维护整个benchmark。

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 作者

- Starace, Giulio
- Jaffe, Oliver
- Sherburn, Dane
- Aung, James
- Chan, Jun Shern
- Maksin, Leon
- Dias, Rachel
- Mays, Evan
- Kinsella, Benjamin
- Thompson, Wyatt
- Heidecke, Johannes
- Glaese, Amelia
- Patwardhan, Tejal

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 当前维护方

OpenAI Preparedness / PaperBench团队

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 资助与支持

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

## 设计目标

### 衡量能力

从论文理解贡献、从零开发代码、执行实验并复现现代AI研究。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 设计背景与适用边界

代码题通过不等于能复现科研结论；PaperBench要求从论文编写、执行实验并按作者协作rubric核验实际复现成果，而Code-Dev仅评价代码开发部分。

来源：[1](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）

## 构建方式

### 题目或数据来源

20篇ICML2024 spotlight/oral论文，覆盖12个主题；另设2篇NeurIPS workshop开发论文和内部holdout。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 构建者背景

OpenAI研究团队与原论文作者共同分解复现目标。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 审核流程

层级rubric与原作者协作，多轮内部审查、澄清addendum，最终作者签核。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 质量控制

8,316个可独立评分叶节点；新VM执行reproduce.sh后裁判评分；另用JudgeEval测裁判。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 去污染与泄漏边界

禁止访问原作者仓库与其他复现；论文报告646次尝试中10次违规被取消，不能排除预训练中记忆代码。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

## 数据形式

### 规模

20篇ICML 2024 Spotlight/Oral论文，共8,316项可独立评分的rubric子任务。

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 题型与交付物

长程科研编程与实验执行；提交代码/文件，再按层级rubric检查。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 模态

- 论文文本/图表
- 代码
- 实验数据与输出

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 语言

英语论文与说明；代码语言/框架随论文。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 难度

原论文复现多小时预算；BasicAgent与IterativeAgent、12h/36h条件不同。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 公开与隐藏划分

公开论文、rubric与评测代码，另有开发论文与内部保留集；正式20篇不可和开发集混合。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

## 评测方法

### 指标

Replication Score：叶节点二元判定后按层级权重聚合，再对论文平均。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 评分方式

三阶段：agent在容器编写代码；独立带GPU容器复现执行；第三容器按论文rubric评分。Code-Dev跳过复现，只评代码开发要求，不可与完整PaperBench分数直比。

来源：[1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问2026-11-07，）

### 提示与运行设置

原论文自动裁判o3-mini-2025-01-31 high；不同agent scaffold、工具和实验预算分别记录。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 评测脚本

https://github.com/openai/frontier-evals/tree/main/project/paperbench

来源：[1](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）；[2](https://github.com/openai/frontier-evals)（访问2026-11-08，）

### 可比性提醒

BasicAgent21%与IterativeAgent24–26%并非仅模型能力变化；CodeDev、预算、judge版本、标准误和论文子集必须注明。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

## 最新情况

### 核验日期

2026-11-08

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 数据版本与更新

```json
{
  "version": "原始20篇ICML2024论文套件"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1"
      "date": "2026-09-16"
      "note": "ScienceIDE §4.1及参考文献明确引用 PaperBench，讨论以已有研究结果复现为目标的评价；为H2学术引用。"
    }
  ]
}
```

说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[1](https://arxiv.org/html/2609.19134v1)（访问2026-11-07，）；[2](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 论文修订记录

Submission history From: James Aung [ view email ] [v1] 2025-04-03 00:55:24 (4,982 KB) [v2] 2025-04-04 21:44:57 (4,982 KB) [v3] 2025-04-07 21:15:49 (4,982 KB)

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 饱和程度

官方README所列历史完整PaperBench最高为IterativeAgent o1-high 36h的26.0±0.3%；原论文BasicAgent最佳为Claude3.5 Sonnet的21.0%。不能把Code-Dev43.4%当完整复现率，也不能据旧实验推定2026当前饱和。

来源：[1](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）；[2](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）

### 争议与已知问题

官网介绍最佳测试agent为Claude 3.5 Sonnet (New) 21.0%；README同时列出IterativeAgent o1-high 36h的26.0%与24h的24.4%。预算和脚手架不同，保留各自证据，不互相覆盖。

来源：[1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问2026-11-07，）；[2](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 衍生与后续使用

PaperBench Code-Dev省略运行，是独立口径；JudgeEval评价裁判，不当作更多论文复现题计数。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

## 榜单快照

### 快照访问日期

2026-11-08 （网页访问日期；历史结果日期分别保留）

来源：[1](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）

### 官方结果入口

https://github.com/openai/frontier-evals/tree/main/project/paperbench

来源：[1](https://raw.githubusercontent.com/openai/frontier-evals/main/project/paperbench/README.md)（访问2026-11-07，）

### 第三方入口

待核实

说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）

### 分赛道结果

- {"model": "IterativeAgent o1-high (36h limit)", "score": 26.0, "track": "官方README/完整PaperBench/36h", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.3, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 1}
- {"model": "IterativeAgent o1-high (24h limit)", "score": 24.4, "track": "官方README/完整PaperBench/24h", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.7, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 1}
- {"model": "BasicAgent claude-3.5-sonnet", "score": 21.0, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.8, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 1}
- {"model": "IterativeAgent claude-3.5-sonnet", "score": 16.1, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.1, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 2}
- {"model": "BasicAgent o1-high", "score": 13.2, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.3, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 3}
- {"model": "IterativeAgent o3-mini-high", "score": 8.5, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.8, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 4}
- {"model": "BasicAgent deepseek-r1", "score": 6.0, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.3, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 5}
- {"model": "BasicAgent gpt-4o", "score": 4.1, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.1, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 6}
- {"model": "BasicAgent gemini-2.0-flash", "score": 3.2, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.2, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 7}
- {"model": "BasicAgent o3-mini-high", "score": 2.6, "track": "官方README/完整PaperBench/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.2, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 8}
- {"model": "IterativeAgent o1-high", "score": 43.4, "track": "官方README/Code-Dev/论文默认预算", "metric": "Replication score (%)", "source_url": "https://github.com/openai/frontier-evals/tree/main/project/paperbench", "collected_at": "2026-11-08 ", "reported_uncertainty": 0.8, "runs": 3, "source_date": "2025-04-02", "result_type": "原论文历史实验", "rank": 1}

来源：[1](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）

### 覆盖边界

完整抄录README两张结果表（10行完整PaperBench、1行Code-Dev），保留±值、运行次数和2025-04-02来源日期。36h、24h与未显式注明预算的论文默认配置分别成赛道，Code-Dev独立。官网21%来自BasicAgent设置，不覆盖IterativeAgent结果。

来源：[1](https://github.com/openai/frontier-evals/tree/main/project/paperbench)（访问2026-11-08，）

## 联系方式

### 公开项目邮箱

- giulio.starace@c-openai.com

来源：[1](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）

### 公开反馈渠道

https://github.com/openai/frontier-evals/issues

来源：[1](https://github.com/openai/frontier-evals)（访问2026-11-08，）

### 官方社交渠道

待核实

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）

### 联系方式收录原则

Benchmark Constitution仅收录论文/官方站公开的项目联系渠道，不收集私人信息；这不是对外站隐私政策的认证。

来源：[1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-08，）

## 原始文件

### 既存论文原件

```json
{
  "id": "1q29o7CEuVufMTKP1jYkNvVCdw6BPOrCk"
  "webViewLink": "
}
```

来源：[1](

### 原始PDF地址

https://arxiv.org/pdf/2504.01848

说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）

### 下载SHA-256

2f58f1a6581af9d99432422dccf3cf61f5c263377c1e4550e7333c4a22d7184d

说明：2026-11-08 下载字节的校验；没有覆盖或上传，不能据此认定既存原件同版本。

来源：[1](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）

### 下载字节数

```json
1703363
```

来源：[1](https://arxiv.org/pdf/2504.01848)（访问2026-11-08，）

### 既存文件夹

```json
{
  "id": "1ugn5Ag6iAx7DM3rz_I3B-g5wtpW_px2c"
  "webViewLink": "
}
```

来源：[1](

### 其他文档

- {"type": "中文介绍Google Doc", "id": "1ime8OV20vnxVACWfQdB0nSVryUAmmb13tYiSkhmq4vE", "webViewLink": "

说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://openai.com/index/paperbench/)（访问2026-11-07，）；[2](

## 变更记录

最近复核
最近复核
最近复核

来源：[1](https://arxiv.org/abs/2504.01848)（访问2026-11-08，）
