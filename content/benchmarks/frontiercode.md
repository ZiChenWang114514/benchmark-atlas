# FrontierCode

> Benchmark Constitution，研究快照 2026-11-07。采集时间不等于成绩实跑或榜单更新时间。

FrontierCode以维护者是否愿意合并修改为标准，将功能、范围纪律、测试和代码库约定纳入加权评分。2.0重建为132题；本页区分Cognition官方榜与Artificial Analysis的Stirrup复现，不能把两种harness的分数拼成一个排名。

最近复核

## 基本信息

### 简称

FrontierCode

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 全称

FrontierCode

说明：保留官方名称，不把论文标题自动扩写为全称。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 基准版本

FrontierCode 2.0；1.0与1.1保留为历史版本

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 论文版本

待核实

状态：待核实。

说明：已打开官方方法与榜页，未从已读取的一手资料定位相应论文/公开代码资产；保留待核实，不把未定位写成官方未公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 发布日期

2.0：2026-10-27（官方文章仅给日期，无时区或时刻）

说明：原始论文/旧版发布日期保留在最新情况的历史资料中；来源仅给日期者不推定时区。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 主板块

代码

说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 领域标签

- 前沿代码Agent能力

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 许可与范围

待核实

状态：待核实。

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 论文

待核实

状态：待核实。

说明：已打开官方方法与榜页，未从已读取的一手资料定位相应论文/公开代码资产；保留待核实，不把未定位写成官方未公开。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 代码

待核实

状态：待核实。

说明：已打开官方方法与榜页，未从已读取的一手资料定位相应论文/公开代码资产；保留待核实，不把未定位写成官方未公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 数据入口

https://cognition.com/frontiercode#methodology（私有132题的官方说明与部分任务展示，不是完整公开下载）

说明：官方方法明确任务保持私有；未伪造HF数据集或完整发布仓库。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 官方主页

https://cognition.com/frontiercode

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 论文标题

待核实

状态：待核实。

说明：已打开官方方法与榜页，未从已读取的一手资料定位相应论文/公开代码资产；保留待核实，不把未定位写成官方未公开。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


## 发起与维护

### 发起/作者单位

Cognition

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 合作与支持

20 多名顶尖开源维护者参与2.0任务构建。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 作者

The Cognition Team（官方方法文章署名）

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 维护方

Cognition；Artificial Analysis 独立运行其评测实现。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 资助

待核实

状态：待核实。

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


## 设计目标

### 衡量能力

能否提交维护者愿意合并的代码：功能正确、理解隐含需求、遵循现有抽象/兼容性并避免过度改写。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 设计背景

详尽规格和仅单元测试容易忽略真实开发中的未明说约束、可维护性与合并质量。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


## 构建方式

### 题目来源

从开源维护者自己维护的真实仓库设计任务；每位维护者每题投入超过40小时；2.0加入更多安全与性能任务。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 出题者背景

20 多位世界级开源开发者，不只是通用标注员。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 审核流程

每题由仓库维护者撰写任务和评分rubric，再经历对抗测试、校准、多阶段人工/自动复核，且每题有Cognition研究员手审；2.0的80%参考解不同于上游PR。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）；[一手资料2](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 质量控制

20多名开源开发者每题投入40小时以上，人工与自动多阶段审核。2.0中80%参考解不同于上游PR（1.0为60%），属于官方自述QC统计而非独立审计。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 污染控制

题目保持私有；轨迹扫描若发现查找现成解则记0，不能排除仓库本身的预训练接触。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


## 数据形式

### 题量

2.0：132任务；1.1 Main 是150任务中的100题，不能混合分母。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 任务形式

真实仓库代码修改，综合测试和维护者评分rubric。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 模态

- 文本
- 源代码
- 仓库环境

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 语言

官方公开示例涵盖JavaScript（Mock Service Worker）和Kotlin（PostHog Android SDK）；完整语言分布待核实，不由示例外推全套覆盖。

状态：待核实。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 难度与分层

强调隐含约束、完整修复和可合并标准；2.0非简单同题扩量。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 公开与隐藏划分

评分任务私有；官方和AA公开部分例题与方法，而非完整数据集。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


## 评测方法

### 指标

task等权的加权rubric得分 (%)。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 评分

任何blocking检查失败或查找解被轨迹扫描标记，整次尝试0分；其余按各项权重汇总。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 提示与运行协议

AA独立实现：全部132题，每题重复3次，Stirrup harness，最多500轮；GPT-6 Luna (medium)作为LLM judge。此设置不等同Cognition官方发布实验。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 评测脚本

待核实

状态：待核实。

说明：已打开官方方法与榜页，未从已读取的一手资料定位相应论文/公开代码资产；保留待核实，不把未定位写成官方未公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 可比性警示

Cognition官方harness与AA Stirrup独立实现不同；1.1与2.0不同；评分不是简单任务全对率，推理effort增加也可能因scope变化降分。

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


## 最新情况

### 核查日期

2026-11-07 （资料快照日期）

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 版本与采用证据

- **current_version**：FrontierCode 2.0；1.0与1.1保留为历史版本
- **release_date**：2.0：2026-10-27（官方文章仅给日期，无时区或时刻）
- **version_changes**：2.0为132个私有任务；相较1.0覆盖的仓库多55%，blocking criteria多43%；相较1.1，参考解修改文件数多67%、行数多89%，代码库大25%。强化隐含正确性/thoroughness、审计与安全任务，同时放宽部分scope标准。各数字比较基线不同，不能混用。
- **trending**：A
- **why_trending**：Cognition于2026-10-27发布2.0并公布跨模型对照；AA现独立运行完整132题、3次/题，且AA当前Intelligence Index v5.0.1列入FrontierCode 2.0。发布方与独立评测方均有实际采用，列A级；不是把10月28日仍报告的1.1成绩误当2.0。
- **history**：- **previous_version_field**：- **value**：2.0；1.1保留为历史快照
    - **sources**：- - **url**：https://cognition.com/blog/frontier-code-2.0
        - **accessed**：2026-11-07
  - **previous_release_date_field**：- **value**：2.0：2026-10-27（官方文章日期，未标时区/时间）
    - **sources**：- - **url**：https://cognition.com/blog/frontier-code-2.0
        - **accessed**：2026-11-07
  - **previous_status_field**：- **value**：- **version**：2.0；1.1保留为历史快照
      - **evidence_2026_h2**：- - **url**：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
          - **date**：2026-10-28
          - **note**：Artificial Analysis 2026-10-28文章明确报告 FrontierCode v1.1 的结果并将其纳入Coding Agent Index；独立机构评测。
    - **sources**：- - **url**：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
        - **accessed**：2026-11-07
      - - **url**：https://cognition.com/blog/frontier-code-2.0
        - **accessed**：2026-11-07
    - **note**：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。
  - **previous_results_field**：- **value**：- - **model**：Claude Opus 5.5 (Max, Default Fallback)
        - **score**：46.4
        - **metric**：weighted score (%)
        - **benchmark_version**：2.0/132题
        - **result_type**：AA独立当前页面
        - **source_date**：待核实（页面未给出该结果运行/发布日期）
        - **collected_at**：2026-11-07
        - **leaderboard_updated_at**：待核实（静态正文未标注整体更新时间）
      - - **model**：Claude Opus 5.5 (Xhigh, Default Fallback)
        - **score**：43.8
        - **metric**：weighted score (%)
        - **benchmark_version**：2.0/132题
        - **result_type**：AA独立当前页面
        - **source_date**：待核实（页面未给出该结果运行/发布日期）
        - **collected_at**：2026-11-07
        - **leaderboard_updated_at**：待核实（静态正文未标注整体更新时间）
      - - **model**：GPT-6 Astra (Max)
        - **score**：42.4
        - **metric**：weighted score (%)
        - **benchmark_version**：2.0/132题
        - **result_type**：AA独立当前页面
        - **source_date**：待核实（页面未给出该结果运行/发布日期）
        - **collected_at**：2026-11-07
        - **leaderboard_updated_at**：待核实（静态正文未标注整体更新时间）
      - - **model**：Claude Opus 5.5 (best effort)
        - **score**：45.5
        - **metric**：weighted score (%)
        - **benchmark_version**：2.0
        - **result_type**：Cognition官方发布实验
        - **source_date**：2026-10-27
        - **collected_at**：2026-11-07
    - **sources**：- - **url**：https://artificialanalysis.ai/evaluations/frontiercode-2-0
        - **accessed**：2026-11-07
      - - **url**：https://cognition.com/blog/frontier-code-2.0
        - **accessed**：2026-11-07

说明：保留历史字段原貌；旧快照不是新的排名。热度等级为编辑证据分级，不是官方认证。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）；[一手资料3](https://artificialanalysis.ai/evaluations/omniscience)（访问 2026-11-07）


### 材料沿革

官方方法文档沿革：1.0于2026-06-08介绍，1.1于2026-07-07修订，2.0于2026-10-27重建132题。这里记录方法文章而非虚构论文修订号。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 饱和情况

2.0官方发布实验最优约45%，官方判断远未饱和；这不是对所有未来系统的绝对结论。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 污染与局限

私有任务降低直接题目泄漏；scope约束与未明说需求会影响解释，官方已在2.0审计并调整范围标准。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 版本/衍生关系

1.0、1.1、2.0是套件版本，本库合计一个 benchmark。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


## 榜单快照

### 快照日期

2026-11-07 （快照日，非实跑日）

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 官方榜

https://cognition.com/frontiercode

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 其他评测入口

https://artificialanalysis.ai/evaluations/frontiercode-2-0

[一手资料1](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


### 分轨结果（结构化快照）

```json
[
  {
    "rank": 1
    "model": "Claude Opus 5.5"
    "score": 45.5
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 2
    "model": "GPT-6 Astra"
    "score": 42.8
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 3
    "model": "Claude Sonnet 5.5"
    "score": 41.0
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 4
    "model": "Gemini 4 Carbon"
    "score": 40.0
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 5
    "model": "GPT-6.1 Sol"
    "score": 39.0
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 6
    "model": "GPT-6 Sol"
    "score": 34.3
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 7
    "model": "Claude Fable 5.1"
    "score": 32.4
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 8
    "model": "Grok 4.7"
    "score": 28.6
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 9
    "model": "Claude Haiku 5.5"
    "score": 27.7
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 10
    "model": "GPT-5.6 Sol"
    "score": 27.6
    "metric": "weighted rubric score (%)"
    "benchmark_version": "2.0 / 132 tasks"
    "scope": "Cognition官方榜JSON-LD ItemList；非AA Stirrup实现"
    "source_url": "https://cognition.com/frontiercode"
    "accessed": "2026-11-07"
    "page_changelog_latest": "2026-11-05（网页最新模型添加记录，非每条运行日）"
    "settings": "具体effort/harness逐配置待核实；此结构化榜未列完整配置"
  }
  {
    "rank": 1
    "model": "Claude Opus 5.5 (Max, Default Fallback)"
    "score": 46.4
    "metric": "weighted rubric score (%)，Stirrup，3 attempts/task"
    "benchmark_version": "2.0"
    "source_url": "https://artificialanalysis.ai/evaluations/frontiercode-2-0"
    "accessed": "2026-11-07"
    "collected_at": "2026-11-07 （）"
    "leaderboard_updated_at": "待核实（当前页面未明确榜单整体更新时间）"
    "scope": "AA Stirrup独立实现，与官方榜分轨"
  }
  {
    "rank": 2
    "model": "Claude Opus 5.5 (Xhigh, Default Fallback)"
    "score": 43.8
    "metric": "weighted rubric score (%)，Stirrup，3 attempts/task"
    "benchmark_version": "2.0"
    "source_url": "https://artificialanalysis.ai/evaluations/frontiercode-2-0"
    "accessed": "2026-11-07"
    "collected_at": "2026-11-07 （）"
    "leaderboard_updated_at": "待核实（当前页面未明确榜单整体更新时间）"
    "scope": "AA Stirrup独立实现，与官方榜分轨"
  }
  {
    "rank": 3
    "model": "GPT-6 Astra (Max)"
    "score": 42.4
    "metric": "weighted rubric score (%)，Stirrup，3 attempts/task"
    "benchmark_version": "2.0"
    "source_url": "https://artificialanalysis.ai/evaluations/frontiercode-2-0"
    "accessed": "2026-11-07"
    "collected_at": "2026-11-07 （）"
    "leaderboard_updated_at": "待核实（当前页面未明确榜单整体更新时间）"
    "scope": "AA Stirrup独立实现，与官方榜分轨"
  }
]
```

[榜单原始资料](https://cognition.com/frontiercode)（访问 2026-11-07）；[榜单原始资料](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）

### 覆盖范围

新增当前Cognition官方页JSON-LD前10：45.5、42.8、41.0等；另列AA的46.4、43.8、42.4，二者不是同一harness，rank只在各轨内有效。官方11月5日有最新模型添加记录，不把它当每条运行日；JSON-LD未带完整effort，保留配置缺口。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）；[一手资料2](https://artificialanalysis.ai/evaluations/frontiercode-2-0)（访问 2026-11-07）


## 联系方式

### 公开研究邮箱

待核实

状态：待核实。

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 问题反馈

待核实

状态：待核实。

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 机构公开渠道

https://x.com/cognition（官方组织账号，官网sameAs元数据/页脚）

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 隐私政策

https://cognition.com/legal/privacy-policy

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


## 原始文件

### 论文PDF

待核实

状态：待核实。

说明：已打开官方方法与榜页，未从已读取的一手资料定位相应论文/公开代码资产；保留待核实，不把未定位写成官方未公开。

[一手资料1](https://cognition.com/blog/frontier-code-2.0)（访问 2026-11-07）


### 源站PDF SHA-256

待核实

状态：待核实。

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 源站PDF字节数

待核实

状态：待核实。

说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### 资料目录

- **id**：17CEUgtPsTmM1-FRtP00KFytv2hRwmeiK
- **webViewLink**：

[一手资料1]( 2026-11-07）


### 其他官方资料

- - **type**：官方方法页HTML归档（非论文PDF）
  - **id**：1pVb8sMOUBsDfBPqsjizyUdsZ-ebmX0Pr
  - **webViewLink**：
  - **source_url**：https://cognition.com/blog/frontier-code-2.0
  - **accessed**：2026-11-07
  - **sha256**：c0073b17387e29534db8ca821b92b524ba178cdbe36331b6873fdcdc7b49dedb
  - **bytes**：226414
- - **type**：中文介绍Google Doc
  - **id**：1vWlLpKFs5bGTOQWxrpv5Pa0O98NReU1uHnlksripJis
  - **webViewLink**：
- - **type**：核验的官方原始资料
  - **url**：https://cognition.com/frontiercode
  - **accessed**：2026-11-07

[一手资料1](https://cognition.com/frontiercode)（访问 2026-11-07）


### PDF归档

待核实

仅核对源站PDF和已有归档引用，未上传或覆盖文件。

## 变更记录

- - **date**：2026-11-07
  - **timezone**：
  - **change**：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：近期热门版本复核：2.0为132个私有任务；相较1.0覆盖的仓库多55%，blocking criteria多43%；相较1.1，参考解修改文件数多67%、行数多89%，代码库大25%。强化隐含正确性/thoroughness、审计与安全任务，同时放宽部分scope标准。各数字比较基线不同，不能混用。 刷新结构化当前榜单，旧版字段与旧快照保留，增加热门证据与证据边界。
  - **sources**：- - **url**：https://cognition.com/blog/frontier-code-2.0
      - **accessed**：2026-11-07
    - - **url**：https://artificialanalysis.ai/evaluations/frontiercode-2-0
      - **accessed**：2026-11-07
- - **date**：2026-11-07
  - **timezone**：
  - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位官方README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
