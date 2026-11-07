# WebArena

> 第1轮深度复核：2026-11-07（KST / Asia/Seoul）。采集日不等于榜单更新日或评测运行日；“待核实”不等于不存在。

[阅读Drive原始论文PDF](https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk)

## 基本信息

### 简称

WebArena

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 全称

WebArena

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 基准版本

canonical WebArena v0.2.0（2023-10-24注释修复后的812任务协议）；AgentLab/BrowserGym属于推荐运行框架。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-07 KST）。

### 论文版本

arXiv v4

> 论文修订版本不等同数据集版本。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 发布日期

2023-07-26 07:59:32 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 主板块

Agent

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 领域标签

- 网页任务执行

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 许可证

Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）

来源：[1](https://github.com/web-arena-x/webarena)（访问 2026-11-07 KST）。

### 论文

https://arxiv.org/abs/2307.13854

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 官方代码

https://github.com/web-arena-x/webarena

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 数据地址

https://github.com/web-arena-x/webarena/blob/main/config_files/test.raw.json

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 官方入口

https://webarena.dev/og/

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 论文标题

WebArena: A Realistic Web Environment for Building Autonomous Agents

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 发起与维护

### 发起机构

Carnegie Mellon University；作者也列Inspired Cognition单位。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 合作研究机构

- Carnegie Mellon University
- Inspired Cognition

> 依论文项目页作者署名机构；与环境中模仿的网站品牌无合作推断。

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 作者

- Zhou, Shuyan
- Xu, Frank F.
- Zhu, Hao
- Zhou, Xuhui
- Lo, Robert
- Sridhar, Abishek
- Cheng, Xianyi
- Ou, Tianyue
- Bisk, Yonatan
- Fried, Daniel
- Alon, Uri
- Neubig, Graham

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 维护方

web-arena-x / WebArena团队维护canonical复现仓库；2024-12-05官方建议新实验使用AgentLab/BrowserGym以改善并行运行、边界处理与统一报告。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-07 KST）。

### 资助

AFRL FA8750-19-2-0200；AWS AI gift；CAIS compute支持。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 设计目标

### 衡量能力

把高层自然语言意图转成跨网页多步行动，正确改变网页状态或获取信息。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 设计背景

静态网页快照与短步骤任务难评长程规划；单看动作相似度会拒绝不同但正确的路径。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 构建方式

### 题目来源

自托管拟真网站：电商、论坛、协作开发、内容管理四类；作者编写241模板派生812任务，附地图/计算器/wiki等。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 出题者背景

CMU研究者设计意图；网站数据模拟现实分布，不是对真实用户账户操作。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 审核流程

两名标注者生成参考答案，第三人解决分歧。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 质量控制

2023-10-24重新检查全部数据集并修复发现的标注错误；官方将v0.2.0称为相对稳定版本。每个测试任务以程序核查目标信息或网站状态。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-07 KST）；[2](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 去污染

本地环境支持可复现但数据/任务公开；模板相似性和后续训练污染仍需注意。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 数据形式

### 规模

812任务，来自241模板，覆盖4类主要网站。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 题型

信息查询、内容创建/修改和多网站联合操作。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 模态

- 网页文本/HTML/可访问性树
- 可选截图
- 工具动作

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 语言

英语指令；网站内容与代码相关语法。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 难度与类型

长程、部分需多网站/外部知识；同模板实例并非完全独立能力点。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 公开与隐藏划分

自托管网站、任务和功能评测代码公开；不等于线上真实网站或隐藏服务。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 评测方法

### 指标

端到端task success rate。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 评分

检查最终或必要中间网站状态；查询答案使用精确、包含或GPT-4-0613模糊比较。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 提示和复现设置

canonical README示例使用accessibility tree、p_cot_id_actree_2s.json两例CoT提示；评测须自部署网站而非演示站，跑完812例后重置环境。模型、最大步数和是否提供not-achievable hint需逐结果固定。

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-07 KST）。

### 官方脚本

https://github.com/web-arena-x/webarena

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 可比性提示

WebArena与VisualWebArena/WebArena-Infinity/Verified变体不同；截图与可访问树观察、外部浏览和步数预算也不同。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-07 KST / Asia/Seoul

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 最新版本与H2证据

- **version**：canonical v0.2.0，812任务；2023-10-24完成全数据复查与标注修复；2024-12-05推荐AgentLab
- **evidence_2026_h2**：[{"url": "https://arxiv.org/html/2609.19134v1", "date": "2026-09-17", "note": "ScienceIDE §4.2及参考文献明确引用 WebArena 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。", "date_kst": "2026-09-17T02:55:47+09:00", "verified_in_round1": "本轮重新打开ScienceIDE正文及参考文献，按原始论文ID确认；属于§4.2相关工作引用，非本文实跑。"}, {"url": "https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv", "date": "2026-09", "note": "官方维护Sheet主榜收录Narada AI Code 86.1，时间列09/2026；是当期榜单收录的参评者成绩，不推断独立复跑。"}]

来源：[1](https://raw.githubusercontent.com/web-arena-x/webarena/main/README.md)（访问 2026-11-07 KST）；[2](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07 KST）；[3](https://arxiv.org/abs/2609.19134)（访问 2026-11-07 KST）；[4](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv)（访问 2026-11-07 KST）。

### 论文修订与H2使用证据

Submission history From: Shuyan Zhou [ view email ] [v1] 2023-07-26 07:59:32 KST (9,497 KB) [v2] 2023-10-24 12:19:22 KST (8,751 KB) [v3] 2023-10-25 10:56:14 KST (8,751 KB) [v4] 2024-04-17 00:13:18 KST (9,472 KB)

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 饱和程度

官方Sheet最高汇总结果86.1%，不等同于统一协议独立评测；原始人类78.24%只在按模板选择的任务上，不应与全量系统结果直接比较。

来源：[1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv)（访问 2026-11-07 KST）。

### 污染、冲突与限制

固定模板、公开测试和使用LLM模糊裁判会影响泛化解释；网站环境版本需要固定。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 后续工作与衍生

VisualWebArena等增加视觉条件，WebArena-x/Infinity另有新任务；原始812题成绩不转贴到衍生版。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-07 KST / Asia/Seoul

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 官方榜单

https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/edit

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）；[2](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv)（访问 2026-11-07 KST）。

### 权威第三方覆盖

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 结果快照

- {"model": "Narada AI Code", "score": 86.1, "unit": "%", "metric": "task success (%)", "scope": "官方WebArena Sheet主榜；success rate，原始812任务口径，具体harness见原工作", "date": "09/2026", "accessed": "2026-11-07 KST", "source_url": "https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv", "provenance": "官方汇总参评者报告；非独立统一复跑。", "leaderboard_updated_at": "待核实", "result_source": "Narada AI Code"}
- {"model": "Deepseek v3.2", "score": 74.3, "unit": "%", "metric": "task success (%)", "scope": "官方WebArena Sheet主榜；success rate，原始812任务口径，具体harness见原工作", "date": "02/2026", "accessed": "2026-11-07 KST", "source_url": "https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv", "provenance": "官方汇总参评者报告；非独立统一复跑。", "leaderboard_updated_at": "待核实", "result_source": "WebTactix"}
- {"model": "OpAgent", "score": 71.6, "unit": "%", "metric": "task success (%)", "scope": "官方WebArena Sheet主榜；success rate，原始812任务口径，具体harness见原工作", "date": "01/2026", "accessed": "2026-11-07 KST", "source_url": "https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv", "provenance": "官方汇总参评者报告；非独立统一复跑。", "leaderboard_updated_at": "待核实", "result_source": "OpAgent"}
- {"model": "GPT-4-0613 + CoT", "score": 14.41, "metric": "task success (%)", "benchmark_version": "原始812任务", "result_type": "论文历史基线", "source_date": "原论文Table3", "collected_at": "2026-11-07 KST", "settings": "no unachievable hint；2-shot/30步"}

来源：[1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 覆盖说明

本轮从原始项目页Leaderboard链接读取公开Sheet，当前主榜前三Narada AI Code 86.1（09/2026）、Deepseek v3.2 74.3（02/2026，WebTactix）、OpAgent 71.6（01/2026）。日期是表中月份，不擅补日；整体榜单更新日待核实。不同系统、训练数据、harness与可达性提示不统一，部分结果自报。论文历史GPT-4+CoT 14.41与Sheet gpt-4-0613 14.9未完全一致，保留双方来源，不将其视为相同复测。

来源：[1](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/gviz/tq?tqx=out:csv)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 联系方式

### 公开联系邮箱

- shuyanzh@cs.cmu.edu
- fangzhex@cs.cmu.edu
- gneubig@cs.cmu.edu

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 问题反馈

https://github.com/web-arena-x/webarena/issues

> 公开仓库反馈入口；未发送问题。

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

### 官方讨论渠道

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

### 隐私政策

待核实

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

来源：[1](https://arxiv.org/abs/2307.13854)（访问 2026-11-07 KST）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2307.13854

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2307.13854)（访问 2026-11-07 KST）。

### SHA-256

f9731b92bc3d29a2ea7b5f9cb46b48540c76bc3f84a57e0c48fc37ea73107f95

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://arxiv.org/pdf/2307.13854)（访问 2026-11-07 KST）。

### 字节数

9128123

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[1](https://arxiv.org/pdf/2307.13854)（访问 2026-11-07 KST）。

### Drive文件夹

- **id**：1nFh380aqu7esGjwpLfEm0xF85brhlOzU
- **webViewLink**：https://drive.google.com/drive/folders/1nFh380aqu7esGjwpLfEm0xF85brhlOzU

来源：[1](https://drive.google.com/drive/folders/1nFh380aqu7esGjwpLfEm0xF85brhlOzU)（访问 2026-11-07 KST）。

### 其他文档

- {"type": "中文介绍Google Doc", "id": "1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4", "webViewLink": "https://docs.google.com/document/d/1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4/edit?usp=drivesdk"}

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）；[2](https://docs.google.com/document/d/1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4/edit?usp=drivesdk)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L
- **webViewLink**：https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"}
- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "round": "1 / 深度实证复核", "change": "补v0.2.0/AgentLab运行口径，重读官方Sheet当前前三和H2收录；并列论文14.41与Sheet14.9历史差异。"}

来源：[1](https://webarena.dev/og/)（访问 2026-11-07 KST）。

