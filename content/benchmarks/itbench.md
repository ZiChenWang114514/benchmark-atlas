# ITBench / ITBench-AA

> Benchmark Constitution｜逐源深度核查：2026-11-08。采集日期不代表实验日期；待核实不等于未公开。

ITBench原框架评测可部署IT环境内的诊断与修复，覆盖SRE、CISO和FinOps；ITBench-AA则只测59个快照场景的离线根因分析。本页将实际修复率与根因实体precision分轨，不能把后者称为事故修复成功率。

导读依据：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-08）；[2](https://github.com/itbench-hub/ITBench)（访问 2026-11-08）；[3](https://github.com/itbench-hub/ITBench#scenarios)（访问 2026-11-08）。

## 基本信息

### 简称

ITBench / ITBench-AA

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 全称

ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 基准版本

原始ITBench与AA独立59场景实现分轨记录

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-08）。

### 发布日期

2025-02-08（arXiv初稿日期，不是数据集的单独发布日）

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-08）。

### 主板块

代码

> Benchmark Atlas 编辑分类。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

### 领域

```json
[
  "运维"
  "根因分析"
]
```

> 编辑标签；空列表表示尚未补充细分标签。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

### 许可与使用范围

原ITBench仓库Apache-2.0；不能据此推断AA私有场景许可。

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/LICENSE)（访问 2026-11-08）。

### 论文入口

https://arxiv.org/abs/2502.05352

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 官方代码

https://github.com/itbench-hub/ITBench

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 数据入口

https://github.com/itbench-hub/ITBench#scenarios

> 这是可部署场景而非单一HF表格；README另链接IBM Enterprise Agents and Benchmarks集合。

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

### 官方主页

https://github.com/itbench-hub/ITBench

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

### 论文标题

ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

## 发起与维护

### 发起方

IBM；原论文含University of Illinois at Urbana-Champaign作者

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 合作与作者单位

Artificial Analysis与ITBench团队共享19私有场景用于AA实现，不据此扩写原始机构合作名单。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 作者

Saurabh Jha、Rohan Arora、Yuji Watanabe、Takumi Yanagawa等，完整作者见论文。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 维护方

ITBench团队维护原项目，Artificial Analysis维护ITBench-AA独立结果。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 资助与资源支持

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

## 设计目标

### 测量能力

真实IT自动化：SRE事件诊断与缓解、CISO合规评估、FinOps成本优化；AA聚焦Kubernetes离线根因诊断。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 与既有基准的差异

区别于普通代码生成或静态工单：需要环境、遥测、故障传播和任务级可解释指标。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

## 构建方式

### 题目来源

原SRE基于自有SaaS真实事件，CISO基于CIS规范，FinOps基于FinOps Foundation能力与成果。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 出题者背景

IBM研究与工程团队及UIUC研究者。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 审核流程

原框架部署场景、注入故障后校验目标告警，再运行诊断/修复；SRE来源于真实运维经验并以故障机制重现。AA改为静态incident snapshot，只判根因实体，不验证线上修复。

来源：[1](https://arxiv.org/pdf/2502.05352)（访问 2026-11-08）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）。

### 质量控制

原框架部署环境、注入故障并断言告警；AA改用离线incident snapshot并识别根因实体。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 去污染与泄漏控制

AA的59任务含40公开和19私有，不等同原论文11/94公开口径。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

## 数据形式

### 规模与统计口径

原始94场景：SRE 42、CISO 50、FinOps 2；AA：59 Kubernetes场景，每题3次。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 题型

原始环境交互执行任务；AA读取alerts/events/traces/metrics/topology并写结构化JSON根因实体。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 模态

```json
[
  "文本"
  "日志"
  "指标"
  "调用trace"
  "拓扑"
  "结构化JSON诊断"
]
```

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 语言

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

### 难度

原始按故障传播链、操作步骤与技术多样性设Easy/Medium/Hard，不用通用代码题难度代替。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 公开与隐藏划分

原论文：94场景中11个开源样例；当前README列6个SRE场景/21种机制、4类CISO、1个FinOps场景，分类口径与历史题数不同。AA固定40公开+19私有场景。

来源：[1](https://arxiv.org/pdf/2502.05352)（访问 2026-11-08）；[2](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）；[3](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）。

## 评测方法

### 指标

原始pass@1、故障定位/传播链NTAM、诊断/修复耗时；AA主指标Average precision at full recall。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）；[3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）。

### 评分规则

AA每任务若FN=0则TP/(TP+FP)，否则0；LLM归一化实体匹配，再对任务与3次重复平均。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）；[3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）。

### 提示、采样与工具设置

AA在Stirrup离线sandbox读取已挂载Kubernetes snapshot，用shell探索，最多100轮，提交JSON文件。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）；[3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）。

### 官方脚本

AA实现：https://github.com/ArtificialAnalysis/ITBench-AA；原项目：https://github.com/itbench-hub/ITBench

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）；[3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）。

### 可比性警告

AA仅离线根因实体识别，不是实际修复成功率；原论文94场景与AA59场景不能把分数直接比较。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）；[3](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）。

## 最新情况

### 核查时间

2026-11-08

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-08）；[2](https://github.com/itbench-hub/ITBench)（访问 2026-11-08）。

### 最新数据状态

```json
{
  "version": "原始ITBench与AA独立59场景实现分轨记录"
  "heat_confidence": "B"
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "AA当前持续开展59场景ITBench-AA根因分析。"
    }
  ]
}
```

> 热度B：近期热度主要由单一评测机构持续运行/展示支持，不表示行业广泛采纳。

来源：[1](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问 2026-11-07）。

### 论文修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2025-02-08"
    "timezone": ""
  }
]
```

> arXiv原始UTC时间已转换为；不等于数据集版本变更。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-08）。

### 饱和度与证据边界

AA当前最高56.2%；原仓库SRE单次轨GPT-4o修复25.00%，多次轨24.79%。均非任务普遍解决的证据；各自协议内解读，不混排。

来源：[1](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）；[2](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md)（访问 2026-11-08）。

### 污染与已知问题

AA含40个公开场景与19个私有场景；需要分别审视公开场景泄漏与私有泛化。原始实际执行诊断修复和AA离线根因指标不是同一任务，不能用56.2%解释为真实事故修复成功率。

来源：[1](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2502.05352)（访问 2026-11-08）。

### 相关与衍生基准

ITBench-AA（README公告2026-05-27，59个SRE任务）；STRATUS论文为基于该环境的多agent SRE系统；IBM另有AssetOpsBench但不是ITBench新版本。

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

## 榜单快照

### 采集日期

2026-11-08 （采集日，不是运行或榜单更新日）

来源：[1](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）；[2](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md)（访问 2026-11-08）。

### 官方结果入口

https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md)（访问 2026-11-08）。

### 独立评测入口

https://artificialanalysis.ai/evaluations/itbench-aa

来源：[1](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-07）。

### 结构化结果

```json
[
  {
    "rank": 1
    "model": "GPT-5.6 Sol (Max)"
    "score": "56.2"
    "metric": "Average precision at full recall (%)"
    "track": "AA独立59场景，静态根因分析"
    "source_url": "https://artificialanalysis.ai/evaluations/itbench-aa"
    "source_date": "待核实（页面快照）"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "Step 5 Preview"
    "score": "55.6"
    "metric": "Average precision at full recall (%)"
    "track": "AA独立59场景，静态根因分析"
    "source_url": "https://artificialanalysis.ai/evaluations/itbench-aa"
    "source_date": "待核实（页面快照）"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "Gemini 3.8 Flash (High)"
    "score": "52.5"
    "metric": "Average precision at full recall (%)"
    "track": "AA独立59场景，静态根因分析"
    "source_url": "https://artificialanalysis.ai/evaluations/itbench-aa"
    "source_date": "待核实（页面快照）"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "ITBench-SRE-Agent-GPT-4o"
    "score": "25.00"
    "metric": "% Resolved"
    "track": "原始SRE Single Trial / 16 incidents"
    "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
    "source_update_label": "02/05/2025 18:06:54（原文无明确时区及日月格式，保留原标签，不擅自转日期）"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "ITBench-SRE-Agent-LLama-3-3-70B"
    "score": "12.50"
    "metric": "% Resolved"
    "track": "原始SRE Single Trial / 16 incidents"
    "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
    "source_update_label": "02/05/2025 18:06:54（原文无明确时区及日月格式，保留原标签，不擅自转日期）"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "ITBench-SRE-Agent-Granite-3-2"
    "score": "0.00"
    "metric": "% Resolved"
    "track": "原始SRE Single Trial / 16 incidents"
    "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
    "source_update_label": "02/05/2025 18:06:54（原文无明确时区及日月格式，保留原标签，不擅自转日期）"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 1
    "model": "ITBench-SRE-Agent-GPT-4o"
    "score": "24.79"
    "metric": "% Resolved"
    "track": "原始SRE Multiple Trials / 162 incidents"
    "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": null
    "model": "ciso-agent-expert-rhel9-opa"
    "score": "0.30"
    "metric": "Average benchmark score (0–1)"
    "track": "原始CISO / 各自场景类别"
    "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_CISO.md"
    "scenario_category": "Gen-CIS-b-RHEL9-Ansible-OPA"
    "passed": 3
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": null
    "model": "pre-release-agent-2025-0428"
    "score": "0.20"
    "metric": "Average benchmark score (0–1)"
    "track": "原始CISO / 各自场景类别"
    "source_url": "https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_CISO.md"
    "scenario_category": "Gen-CIS-b-K8s-Kyverno"
    "passed": 2
    "snapshot_date": "2026-11-08 "
  }
]
```

来源：[1](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）；[2](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md)（访问 2026-11-08）；[3](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_CISO.md)（访问 2026-11-08）。

### 覆盖与局限

原项目SRE操作环境单次与多次轨、AA静态根因轨分开。README现已有SRE/CISO榜，修正此前只链接AA为官方榜的做法；原榜更新时间标签不明时区/日月格式，不把它当运行日。

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/LEADERBOARD_SRE.md)（访问 2026-11-08）；[2](https://artificialanalysis.ai/evaluations/itbench-aa)（访问 2026-11-08）；[3](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

## 联系方式

### 官方公开邮箱

```json
[
  "agent-bench-automation@ibm.com"
  "saurabh.jha@ibm.com"
  "muew@jp.ibm.com"
]
```

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

### 仓库反馈

https://github.com/itbench-hub/ITBench/issues

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

### 官方社区

https://discord.gg/6fzy3JRHmt

> 官方README列明的社区讨论入口。

来源：[1](https://github.com/itbench-hub/ITBench/blob/main/README.md)（访问 2026-11-08）。

### 隐私与联系边界

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

## 原始文件

### 论文PDF

https://arxiv.org/pdf/2502.05352

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

### PDF SHA-256

da47aa02d9cf0cd2a330d3c9890e0338d4f3c3cdd89521c7b8979ab4986f932c

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2502.05352)（访问 2026-11-08）。

### PDF字节数

```json
4068098
```

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2502.05352)（访问 2026-11-08）。

### 已有文件夹

待核实

> 已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

### 其他官方文档

```json
[
  {
    "type": "官方方法/介绍网页（不是论文PDF）"
    "url": "https://arxiv.org/abs/2502.05352"
  }
]
```

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

### 已有 PDF归档

待核实

> 本组只建立本地研究文件，不上传或声明已有 PDF。

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）。

## 变更记录

### 历次核查

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": ""
    最近复核
  }
]
```

来源：[1](https://arxiv.org/abs/2502.05352)（访问 2026-11-07）；[2](https://arxiv.org/abs/2502.05352)（访问 2026-11-08）；[3](https://github.com/itbench-hub/ITBench)（访问 2026-11-08）。

