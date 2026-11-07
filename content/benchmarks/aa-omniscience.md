# AA-Omniscience

> 核验日期：2026-11-07 Asia/Shanghai（UTC+8）。未知保留待核实；访问日不是测量日。

已核实存在与2026-H2实际使用；已建内容，待核实字段显式保留；trending: B

把“知道答案”和“承认不知道”一起计分。当前v1.1为3000题，不能用原始6000题论文摘要或旧版分数解释现榜。

## 基本信息

### 简称

AA-Omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 全称

AA-Omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 基准版本

AA-Omniscience v1.1；v1.0为历史版本，分数不直接可比

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问2026-11-07）

### 论文版本

arXiv v1

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### 发布日期

v1.1：2026-10（官方数据卡仅确认月份；精确日与时刻待核实）

> 原始论文/旧版发布日期保留在最新情况的历史资料中；来源仅给日期者不推定时区。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问2026-11-07）

### 主板块

语言

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### 领域标签

- 知识准确性、幻觉与校准

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 许可证

Apache-2.0（公开v1.1子集）；不能据此推断私有2700题的再分发许可。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2511.13029

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### 官方代码

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 数据地址

https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

### 官方入口

https://artificialanalysis.ai/evaluations/omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 论文标题

AA-Omniscience: Evaluating Cross-Domain Knowledge Reliability in Large Language Models

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

## 发起与维护

### 发起方

Artificial Analysis。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 合作方

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 作者

- Jackson, Declan
- Keating, William
- Cameron, George
- Hill-Smith, Micah

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### 维护方

Artificial Analysis

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 资助方

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

## 设计目标

### 衡量能力

测量跨领域事实知识与知道何时不作答的知识校准，惩罚错误猜测。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 设计背景

一般能力分数不能代表可靠事实输出，也不体现模型是否承认知识缺口。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

## 构建方式

### 题目来源

LLM 问题生成 agent 从权威学术与行业材料生成问题。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 出题者背景

Artificial Analysis 研究团队设计自动生成与评测流程。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 审核流程

原论文§2.2：题目代理从权威材料生成并按相似度、难度、歧义过滤，人工介入复核；v1.1数据卡说明修正歧义/错误，但未给逐题人工复核数量。

> 描述已披露流程，不将未给出的人工数量编为0或全量。

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

### 质量控制

v1.1 移除已饱和问题，官网同时展示公开/私有题的表现一致性分析。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 去污染

v1.1移除v1.0公开集问题、过滤饱和题、增补新题并修正歧义/错误；保留2700题私有以维护评测完整性。上述措施不构成模型训练无污染证明。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问2026-11-07）

## 数据形式

### 题量与规模

v1.1全量3000题，公开300题、私有2700题；v1.0为6000题、公开600题。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

### 题型

开放式事实问答，允许放弃作答

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 模态

文本

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 语言

公开子集题目与回答/评分提示为英语；私有题库完整语种声明待核实。

> 字段状态：待核实

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

### 难度

v1.1 删除饱和题；分数降低可以来自题库变化，不能直接断言模型退步。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 公开与隐藏划分

v1.1全量3000题，公开test子集300题、私有2700题；六领域公开比例与全量一致：科学工程数学60/600、软件工程60/600，其余四领域各45/450。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

## 评测方法

### 指标

Net Score（-100至100）、accuracy、hallucination rate；三者不同。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 评分

AA-Omniscience Index = 100×(正确−错误)/总题数，范围−100至100；部分正确及弃答得0。裁判模型为GPT-5.6 Luna (medium)，四类判断为正确、错误、部分正确、未作答。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问2026-11-07）

### 运行设置

不提供上下文或工具；提示仅回答答案，明确鼓励在不确定或需要上下文/工具时弃答。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md)（访问2026-11-07）

### 官方脚本

https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1

> 数据卡直接公开回答提示和完整四分类裁判模板；这是可复现协议，不声称有独立可执行评测仓库。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

### 可比性警示

v1 与 v1.1 题库和分数不可直接混比；当前页仍保留 v1 论文摘要的 Claude4.1Opus 4.8 分，那不是当前榜首。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 Asia/Shanghai（UTC+8）

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 最新版本与采用证据

```json
{
  "current_version": "AA-Omniscience v1.1；v1.0为历史版本，分数不直接可比",
  "release_date": "v1.1：2026-10（官方数据卡仅确认月份；精确日与时刻待核实）",
  "version_changes": "v1.0为6000题/公开600题；v1.1为3000题/公开300题、私有2700题，保留6大领域。删除饱和题及旧公开题，增加新题，修正歧义和错误；v1.0/v1.1分数不能直接比较。公开子集Apache-2.0许可，不自动外推至私有题。",
  "trending": "B",
  "why_trending": "AA官方数据卡明确v1.1于2026年10月上线，发布时比较86个模型；AA 2026-10-28文章明确报道v1.1，当前官方页面继续跟踪124个模型配置。近期证据主要来自AA同一机构，保守列B，不写成行业普遍采用。",
  "history": {
    "previous_version_field": {
      "value": "v1.1",
      "sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/omniscience",
          "accessed": "2026-11-07"
        }
      ]
    },
    "previous_release_date_field": {
      "value": "2025-11-17",
      "sources": [
        {
          "url": "https://arxiv.org/abs/2511.13029",
          "accessed": "2026-11-07"
        }
      ],
      "note": "原始论文首发日期，不保证等同于数据文件首次公开日。"
    },
    "previous_status_field": {
      "value": "v1.1（官方卡注明2026年10月上线）；与v1.0分数不直接可比。",
      "sources": [
        {
          "url": "https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1/raw/main/README.md",
          "accessed": "2026-11-07"
        }
      ]
    },
    "previous_results_field": {
      "value": [
        {
          "model_version": "Gemini 4 Carbon (High)",
          "score": "54",
          "unit": "指数点",
          "scope_and_protocol": "AA-Omniscience v1.1 Net Score，范围−100至100；仅官方页面摘要可读的前三名。",
          "result_date": "待核实",
          "snapshot_date": "2026-11-07",
          "source_url": "https://artificialanalysis.ai/evaluations/omniscience",
          "source_class": "一级：官方榜单",
          "checkpoint_note": "按来源展示名原样记录，未推断API checkpoint。"
        },
        {
          "model_version": "Claude Opus 5.5 (Max, Default Fallback)",
          "score": "48",
          "unit": "指数点",
          "scope_and_protocol": "AA-Omniscience v1.1 Net Score，范围−100至100；仅官方页面摘要可读的前三名。",
          "result_date": "待核实",
          "snapshot_date": "2026-11-07",
          "source_url": "https://artificialanalysis.ai/evaluations/omniscience",
          "source_class": "一级：官方榜单",
          "checkpoint_note": "按来源展示名原样记录，未推断API checkpoint。"
        },
        {
          "model_version": "Gemini 4 Carbon (Medium)",
          "score": "47",
          "unit": "指数点",
          "scope_and_protocol": "AA-Omniscience v1.1 Net Score，范围−100至100；仅官方页面摘要可读的前三名。",
          "result_date": "待核实",
          "snapshot_date": "2026-11-07",
          "source_url": "https://artificialanalysis.ai/evaluations/omniscience",
          "source_class": "一级：官方榜单",
          "checkpoint_note": "按来源展示名原样记录，未推断API checkpoint。"
        },
        {
          "model": "Gemini 4 Carbon (High)",
          "score": 54,
          "unit": "points",
          "metric": "v1.1 Net Score",
          "scope": "AA独立评测官网可读前列",
          "snapshot_date": "2026-11-07",
          "model_release_date": "2026-10-28"
        },
        {
          "model": "Claude Opus 5.5 (Max, Default Fallback)",
          "score": 48,
          "unit": "points",
          "metric": "v1.1 Net Score",
          "scope": "AA独立评测官网可读前列",
          "snapshot_date": "2026-11-07"
        },
        {
          "model": "Gemini 4 Carbon (Medium)",
          "score": 47,
          "unit": "points",
          "metric": "v1.1 Net Score",
          "scope": "AA独立评测官网可读前列",
          "snapshot_date": "2026-11-07"
        }
      ],
      "sources": [
        {
          "url": "https://artificialanalysis.ai/evaluations/omniscience",
          "accessed": "2026-11-07"
        },
        {
          "url": "https://artificialanalysis.ai/evaluations/omniscience",
          "accessed": "2026-11-07"
        }
      ]
    }
  }
}
```

> 保留历史字段原貌；旧快照不是新的排名。热度等级为编辑证据分级，不是官方认证。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问2026-11-07）

### 修订历史

```json
[
  {
    "version": "v1",
    "submitted_at": "2025-11-17T14:27:16+08:00",
    "timezone": "Asia/Shanghai"
  }
]
```

> arXiv仅列v1；原始论文6000题，不是v1.1的3000题技术报告。

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### 饱和情况

官方说明 v1.1 移除了饱和题；这说明题库发生筛选，不代表整个知识任务已饱和。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 污染与争议

同页含 v1 论文摘要和 v1.1 当前方法，题量、最高分与分数含义必须按版本区分；当前幻觉率分母使用官网给出的定义，不按惯例改写。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 版本与衍生关系

AA-Omniscience-Public v1.0/v1.1为同家族公开子集；不得将公开300题结果视作私有2700题正式榜，亦不拆条凑数。

[来源1](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 Asia/Shanghai（UTC+8）

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 官方榜单

https://artificialanalysis.ai/evaluations/omniscience

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 第三方覆盖

待核实

> 字段状态：待核实

> 原值与官方榜完全相同，已纠正；不把AA自评标成独立复评。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 分轨结果

#### v1.1 Net Score

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (High) | 54 | 100×(correct−incorrect)/total | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |
| 2 | Claude Opus 5.5 (Max, Default Fallback) | 48 | 100×(correct−incorrect)/total | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |
| 3 | Gemini 4 Carbon (Medium) | 47 | 100×(correct−incorrect)/total | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |



#### v1.1 Accuracy

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Claude Fable 5.1 (Max, Default Fallback) | 68 | 正确率 (%) | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |
| 2 | Claude Fable 5.1 (Xhigh, Default Fallback) | 67 | 正确率 (%) | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |
| 3 | Claude Opus 5.5 (Xhigh, Default Fallback) | 66 | 正确率 (%) | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |



#### v1.1 Hallucination Rate

| 来源内名次 | 模型 / 配置 | 分数 | 指标 | 来源与访问日 |
| --- | --- | ---: | --- | --- |
| 1 | Gemini 4 Carbon (Medium) | 4 | 官网幻觉率 (%)；越低越好 | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |
| 1 | Gemini 4 Argon (High) | 4 | 官网幻觉率 (%)；越低越好 | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |
| 3 | Gemini 4 Carbon (High) | 11 | 官网幻觉率 (%)；越低越好 | [原表](https://artificialanalysis.ai/evaluations/omniscience) · 2026-11-07 |



> 字段状态：待核实

> 保留原网页显示整数精度；整体更新时间及各模型运行时间待核实；三指标分轨不能混排。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 覆盖说明

当前快照来源：https://artificialanalysis.ai/evaluations/omniscience。保留模型配置原名。整体更新时间与各模型实际运行日期待核实。 

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)（访问2026-11-07）

## 联系方式

### 公开科研联系邮箱

- declan@artificialanalysis.ai
- william@artificialanalysis.ai
- george@artificialanalysis.ai
- micah@artificialanalysis.ai

> 论文首页公开科研通讯地址。

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### 公开反馈

待核实

> 字段状态：待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 官方社交

- https://x.com/ArtificialAnlys
- https://www.linkedin.com/company/artificial-analysis/

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

### 隐私说明/政策

https://artificialanalysis.ai/privacy-policy

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2511.13029

[来源1](https://arxiv.org/abs/2511.13029)（访问2026-11-07）

### PDF SHA-256

abedc69e8235329cbfe0fe49cc33928a5b1732bc054637328c00b07f588b5dfa

> 本轮实际下载字节的SHA-256；不表示已有Drive副本已替换。

[来源1](https://arxiv.org/pdf/2511.13029)（访问2026-11-07）

### PDF字节数

3786016

[来源1](https://arxiv.org/pdf/2511.13029)（访问2026-11-07）

### Drive文件夹

```json
{
  "id": "1Mrrp24vyM98TfiB-wQ0QON4zu8XdEJWO",
  "webViewLink": "https://drive.google.com/drive/folders/1Mrrp24vyM98TfiB-wQ0QON4zu8XdEJWO"
}
```

[来源1](https://drive.google.com/drive/folders/1Mrrp24vyM98TfiB-wQ0QON4zu8XdEJWO)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1Suli8iNzIoHvLMfAxHiSjWdZaSYSX22WFU-Wznw_V1k",
    "webViewLink": "https://docs.google.com/document/d/1Suli8iNzIoHvLMfAxHiSjWdZaSYSX22WFU-Wznw_V1k/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1Suli8iNzIoHvLMfAxHiSjWdZaSYSX22WFU-Wznw_V1k/edit?usp=drivesdk)（访问2026-11-07）

### Drive论文副本

```json
{
  "id": "1x28FX-LyGRAjXuPwOHCqqhubxSLh7OJj",
  "webViewLink": "https://drive.google.com/file/d/1x28FX-LyGRAjXuPwOHCqqhubxSLh7OJj/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1x28FX-LyGRAjXuPwOHCqqhubxSLh7OJj/view?usp=drivesdk)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai（UTC+8）",
    "change": "第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。",
    "fields_updated": [
      "basic_info.license",
      "construction.decontamination",
      "data_format.size",
      "evaluation.scoring",
      "evaluation.prompt_settings",
      "latest_status.latest_dataset_version",
      "latest_status.paper_revision_history",
      "leaderboard.results",
      "leaderboard.coverage_note"
    ]
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai",
    "change": "近期热门版本复核：v1.0为6000题/公开600题；v1.1为3000题/公开300题、私有2700题，保留6大领域。删除饱和题及旧公开题，增加新题，修正歧义和错误；v1.0/v1.1分数不能直接比较。公开子集Apache-2.0许可，不自动外推至私有题。 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。",
    "sources": [
      {
        "url": "https://artificialanalysis.ai/evaluations/omniscience",
        "accessed": "2026-11-07"
      },
      {
        "url": "https://huggingface.co/datasets/ArtificialAnalysis/AA-Omniscience-Public-v1.1",
        "accessed": "2026-11-07"
      },
      {
        "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
        "accessed": "2026-11-07"
      }
    ]
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai (UTC+8)",
    "change": "Round2 q0：实际重读原始论文PDF、官方README/LICENSE、可用HF卡与排行榜；补方法、版本/样本/指标冲突及分轨结果，保留未核实信息。"
  }
]
```

[来源1](https://artificialanalysis.ai/evaluations/omniscience)（访问2026-11-07）
