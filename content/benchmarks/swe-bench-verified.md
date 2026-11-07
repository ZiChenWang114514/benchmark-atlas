# SWE-bench Verified

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；采集日不等于运行日，历史榜单、研究复测与独立评测分别记录。

## 基本信息

### 简称

SWE-bench Verified

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 全称

SWE-bench Verified

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 基准版本

SWE-bench Verified，500题

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 论文版本

arXiv v3

> 论文修订版本不等同数据集版本。

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 发布日期

2024-08-13（官方公告日期，未标时间/时区）

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 主板块

代码

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 领域标签

仓库级真实软件问题修复

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 许可证

MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

来源：[https://github.com/SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-07 KST）

### 论文

https://arxiv.org/abs/2310.06770

> 2310.06770 是 SWE-bench 母基准论文，Verified 的筛选协议主要见官方公告，不冒称独立 Verified 论文。

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 官方代码

https://github.com/SWE-bench/SWE-bench

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 数据地址

https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 官方入口

https://www.swebench.com/verified

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 论文标题

SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

## 发起与维护

### 机构与发起方

OpenAI 与 SWE-bench 原作者合作发布。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 合作方

OpenAI（官网明确Verified在人类筛选中与OpenAI合作建立）。

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 作者

Verified 公告：Neil Chowdhury、James Aung、Chan Jun Shern、Oliver Jaffe、Dane Sherburn、Giulio Starace 等；母论文作者另见论文元数据。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 当前维护方

SWE-bench 官方团队维护数据与评测框架；OpenAI 提供人工标注和 Verified 公告。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

## 设计目标

### 衡量能力

理解真实 GitHub issue、定位代码并提交能解决问题且不造成回归的仓库级补丁。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 设计背景

原 SWE-bench 中描述欠明确、测试过窄及环境安装失败可把合理解判错；Verified 筛除这些不公平实例。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

## 构建方式

### 题目来源

来自 12 个开源 Python 仓库的已解决 issue / PR；从原测试集 1,699 个随机标注样本中筛出 500。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 出题者背景

93 名具有 Python 经验的专业开发者；先通过 50 道高置信 onboarding 题并获得反馈。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 审核流程

每个样本由 3 名独立标注者评价描述和测试；采用最高严重程度标签，任一严重问题均剔除。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 质量控制

描述/测试严重度 0–3；剔除任一维度 ≥2 或其他重大问题；Docker harness 提高运行稳定性。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 去污染

原 issue、仓库与 PR 公开；官方明确承认静态互联网抓取数据可能已进入预训练，人工 Verified 不表示去污染。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

## 数据形式

### 题量与规模

500 题；196 道预估少于 15 分钟的 easy、45 道大于 1 小时的 hard（人工估计，不是模型时限）。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 题型

仓库与问题说明 → 修改文件/代码补丁。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 模态

文本、代码、仓库环境

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 语言

Python 仓库，英语问题说明。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 难度

人工按 <15min、15min–1h、1–4h、>4h 标注；与是否可解筛选分开。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 公开与隐藏划分

Verified 数据公开；运行时不向 agent 提供 gold patch 和评分测试，公开可得性仍有污染风险。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

## 评测方法

### 指标

Resolved rate：完全解决任务的比例。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 评分

补丁可应用且 FAIL_TO_PASS 与 PASS_TO_PASS 两组测试全部通过才算 resolved。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）

### 提示与运行设置

官方Bash Only采用mini-SWE-agent最小ReAct循环。release 1.x支持时temperature=0；2.x及以后不设置temperature；版本记录必须随分数保留。

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 官方评测脚本

https://github.com/SWE-bench/SWE-bench

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 可比性警示

完整榜比较任意agent系统，Bash Only才固定mini-SWE-agent；1.x解析输出字符串，2.x用tool calling，官网明确两代结果不一定可比。500题Verified不是完整SWE-bench或SWE-bench Pro。

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "SWE-bench Verified，500题",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.20804v1",
      "date": "2026-09-17",
      "note": "Harness Design 研究§3.1实际使用500个人工核验GitHub问题，比较不同harness设置；不是同名SWE-Bench Pro Verified。"
    }
  ]
}
```

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 KST）；[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 论文修订历史

Submission history From: Carlos E. Jimenez [ view email ] [v1] 2023-10-11 01:47:29 KST (2,003 KB) [v2] 2024-04-06 03:16:29 KST (2,258 KB) [v3] 2024-11-12 08:05:04 KST (2,398 KB)

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 污染与争议

Verified 是质量筛选而非隐藏新题，且主要覆盖 Python 软件 issue；不能视为一般软件开发或无污染保证。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 KST）

### 衍生与版本关系

与 SWE-bench Lite、Multimodal、Multilingual 及 SWE-bench Pro 有关系但不同口径，不混排。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 KST）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 官方榜单

https://www.swebench.com/verified

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 独立评测覆盖

待核实

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

核验状态：待核实

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 核验结果

```json
[
  {
    "model": "gpt-4o-2024-05-13 + Agentless",
    "score": 33.2,
    "metric": "resolved (%)",
    "benchmark_version": "Verified500",
    "result_type": "官方公告历史基线",
    "source_date": "2024-08-13",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Nemotron-3 550B / 研究harness",
    "score": 69.4,
    "metric": "SR (%)",
    "benchmark_version": "Verified500",
    "result_type": "H2 学术实验",
    "source_date": "2026-09-17",
    "collected_at": "2026-11-07 KST",
    "settings": "T4/128k、planning、bash-only、最多300步、温度0"
  }
]
```

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 KST）

### 覆盖与时效说明

本次官方页面静态正文未核出当前动态榜前三；列出可核实的历史/学术结果，不冒称最新 SOTA。Harness Design 176设置显示 scaffold 会显著改变同模型表现。

来源：[https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/)（访问 2026-11-07 KST）；[https://arxiv.org/html/2609.20804v1](https://arxiv.org/html/2609.20804v1)（访问 2026-11-07 KST）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 公开反馈

https://github.com/SWE-bench/SWE-bench/issues

> 公开仓库反馈入口；未发送问题。

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770)（访问 2026-11-07 KST）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2310.06770

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[https://arxiv.org/pdf/2310.06770](https://arxiv.org/pdf/2310.06770)（访问 2026-11-07 KST）

### 原始PDF SHA-256

f7e8e1df64129742b8199a21a042734519a823a1dafd6f48f8f3ddcfb48ee296

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2310.06770](https://arxiv.org/pdf/2310.06770)（访问 2026-11-07 KST）

### 原始PDF字节数

4533722

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2310.06770](https://arxiv.org/pdf/2310.06770)（访问 2026-11-07 KST）

### Drive资料文件夹

```json
{
  "id": "1-YvqNLfMxUXoiTYWqbyPSsbJWrK7H9iL",
  "webViewLink": "https://drive.google.com/drive/folders/1-YvqNLfMxUXoiTYWqbyPSsbJWrK7H9iL"
}
```

来源：[https://drive.google.com/drive/folders/1-YvqNLfMxUXoiTYWqbyPSsbJWrK7H9iL](https://drive.google.com/drive/folders/1-YvqNLfMxUXoiTYWqbyPSsbJWrK7H9iL)（访问 2026-11-07 KST）

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "193rLgS0oSSznAPMtMovoito3n3jfiZIvz4T3WcUxaBQ",
    "webViewLink": "https://docs.google.com/document/d/193rLgS0oSSznAPMtMovoito3n3jfiZIvz4T3WcUxaBQ/edit?usp=drivesdk"
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）；[https://docs.google.com/document/d/193rLgS0oSSznAPMtMovoito3n3jfiZIvz4T3WcUxaBQ/edit?usp=drivesdk](https://docs.google.com/document/d/193rLgS0oSSznAPMtMovoito3n3jfiZIvz4T3WcUxaBQ/edit?usp=drivesdk)（访问 2026-11-07 KST）

### Drive 原始 PDF

```json
{
  "id": "1n47Le3puVRH6y64GwRSgTy41zEGlU32T",
  "webViewLink": "https://drive.google.com/file/d/1n47Le3puVRH6y64GwRSgTy41zEGlU32T/view?usp=drivesdk"
}
```

来源：[https://drive.google.com/file/d/1n47Le3puVRH6y64GwRSgTy41zEGlU32T/view?usp=drivesdk](https://drive.google.com/file/d/1n47Le3puVRH6y64GwRSgTy41zEGlU32T/view?usp=drivesdk)（访问 2026-11-07 KST）

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  },
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "第1轮深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。"
  }
]
```

来源：[https://www.swebench.com/verified](https://www.swebench.com/verified)（访问 2026-11-07 KST）
