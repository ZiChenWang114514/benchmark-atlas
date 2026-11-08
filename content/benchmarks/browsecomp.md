# BrowseComp

> Benchmark Constitution · 深度复核：2026-11-08。已核验存在；近期热门新建条目，未核实字段保留标记；trending: A

BrowseComp用短答案衡量长程网页检索：答案容易核验，寻找答案却可能需要持续搜索、重述查询和交叉约束。它不是对真实用户查询的随机抽样，也不评价长报告是否实用。原论文明确使用AI裁判核对语义等价性，因此第三方追踪页“不需要LLM judge”的说法不能覆盖官方协议；多agent、压缩策略和运行预算不同的分数也不应被当作同协议排名。

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

## 基本信息

### 简称

BrowseComp

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 全称

BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 版本边界

v1（1,266题原始集）

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 论文版本

arXiv v1（2025-04-16）

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 发布日期

2025-04-16（arXiv 提交日）

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 板块

Agent

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

> Benchmark Atlas 编辑归档。

### 领域

```json
[
  "深度搜索"
  "网页浏览"
  "信息检索"
]
```

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 许可与限制

MIT（simple-evals 仓库）

[来源1](https://github.com/openai/simple-evals)（访问2026-11-07）

> 题目数据集本身的许可另行待核实；simple-evals 已于2025年7月发布弃用公告。

### 论文

https://arxiv.org/abs/2504.12516

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 官方代码

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（访问2026-11-07）

### 数据入口

https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv

[来源1](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问2026-11-08）

### 官方主页

https://openai.com/index/browsecomp/

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 论文题名

BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

## 发起与维护

### 发起方

OpenAI

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 合作机构

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

Jason Wei、Zhiqing Sun、Spencer Papay、Scott McKinney、Jeffrey Han、Isa Fulford、Hyung Won Chung、Alex Tachard Passos、William Fedus、Amelia Glaese

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 维护入口

OpenAI

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 资助披露

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 测量对象

持续、富有创造性地在互联网上检索难找、相互纠缠的信息。

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 既有评测的缺口

以短且易验证的答案测浏览 agent 的核心坚持与检索能力；论文自述回避了真实用户分布、长答案与歧义消解等问题。

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

## 构建方式

### 题源

人类训练员从可查证的事实反向构造带多重约束的问题，答案须简短、明确、稳定并有证据；不是模型合成题或真实用户查询的随机样本。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 构建人员

负责创建高质量评测数据的人类训练员；解题基线来自同一训练员群体但不得作答自己出的题。论文不把他们称为竞赛级搜索专家。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 审核

核验GPT-4o（带/不带浏览）、o1和早期Deep Research不能解题；进行5次简单Google搜索检查答案不在首屏；部分题由另一训练员限10分钟尝试，若该作者题目被解比例超过40%则要求修订。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 质控

要求短且可验证的稳定参考答案、作者熟悉题域并补约束；另一训练员若发现不同但有效答案会反馈修订。论文明确承认无法穷尽验证所有可能答案，不能称绝对唯一答案集。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 去污染及边界

原论文Table 1说明加入canary以便训练语料过滤，并请求不在网上明文或图片再发布题目；官方公开CSV对题干和答案采用canary派生的可逆编码，不是保密或访问控制保证。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问2026-11-08）

## 数据形式

### 规模与计数口径

1,266 题

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 题型

短答案问答，可与参考答案对照验证

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 模态

```json
[
  "文本"
  "网页"
]
```

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 语言

```json
[
  "英语"
]
```

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）

> 中文版 BrowseComp-ZH 为另一基准。

### 难度

原论文§3：1,255道实际被人类尝试的题中，888道在搜索两小时后放弃；367道自称可解中317道参考匹配。题目筛选针对当时模型，不能当成2026模型难度分布。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 划分与公开范围

官方脚本读取公开browse_comp_test_set.csv，内含编码题干、答案及canary；不是独立公开训练集加隐藏测试答案的竞赛协议。

[来源1](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问2026-11-08）

## 评测方法

### 指标

准确率（与参考短答案比对）

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）；[来源2](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）

### 评分

原论文§2.3与附录B使用AI裁判比较预测与参考短答案的语义等价性，采用HLE式裁判提示；不是简单精确匹配，更不是无需LLM judge。裁判模型由调用者配置。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问2026-11-08）

### 提示与运行条件

官方QUERY_TEMPLATE要求Explanation、Exact Answer、Confidence；浏览工具、上下文压缩、推理档位、次数和并行agent数不由数据集统一固定。

[来源1](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问2026-11-08）；[来源2](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 官方评测入口

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（访问2026-11-07）

### 可比性边界

分数高度依赖工具、上下文管理策略（如压缩阈值）、尝试次数与多 agent 并行；纯模型与带工具系统不可直接比较。

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）；[来源2](https://www.kimi.com/blog/kimi-k3)（访问2026-11-07）

## 最新情况

### 复核时间

2026-11-08

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-08）

### 当前版本

```json
{
  "version": "v1（1,266题原始集）"
  "evidence_2026_h2": [
    {
      "url": "https://www.kimi.com/blog/kimi-k3"
      "date": "2026-11-07"
      "organization": "Moonshot AI"
      "note": "Kimi K3生产力评测脚注详细规定BrowseComp上下文压缩，并报告无压缩对照。"
    }
    {
      "url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
      "date": "2026-10-11"
      "organization": "Steel.dev"
      "note": "10月11日更新的独立榜单列OpenAI、Anthropic、Moonshot多方带来源结果。"
    }
    {
      "url": "https://openai.com/index/gpt-6-astra/"
      "date": "2026-11-07"
      "organization": "OpenAI"
      "note": "GPT-6 Astra正式发布评测表明确报告BrowseComp，作为近期厂商采用证据。"
    }
  ]
  "trending": {
    "heat_confidence": "A"
    "summary": "OpenAI、Moonshot 等前沿发布反复采用，独立追踪器10月仍更新。"
  }
}
```

[来源1](https://www.kimi.com/blog/kimi-k3)（访问2026-11-07）；[来源2](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）；[来源3](https://openai.com/index/gpt-6-astra/)（访问2026-11-07）

> 近期热门证据取自候选研究与重开页面；A级：多家前沿实验室或评测机构独立采用。

### 论文修订与后续使用

```json
{
  "arxiv_revisions_kst": [
    {
      "version": "v1"
      "submitted_at_kst": "2025-04-17"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-08）

### 饱和情况

接近饱和：Steel.dev 跟踪的最高分已达 92.2%（GPT-5.6 Sol Ultra，多 agent），单 agent 前列在 90% 上下。

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）

### 风险与冲突

Steel方法页称“不需要LLM judge”，与原论文§2.3及官方评分模板冲突；评分方法以一级来源为准。题目公开后存在检索答案及训练污染风险；canary是防护提示，不是无污染证明。

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py)（访问2026-11-08）；[来源3](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-08）

### 衍生与后续工作

BrowseComp-ZH、BrowseComp-Plus 等衍生基准不并入本条。

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）

## 榜单快照

### 快照时间

2026-11-08 （实际复核日；批次标签2026-11-07）

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-08）

### 官方榜入口

https://openai.com/index/browsecomp/

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-08）

### 第三方榜入口

https://leaderboard.steel.dev/leaderboards/browsecomp.md

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）

### 逐轨结果

```json
[
  {
    "model": "GPT-5.6 Sol Ultra"
    "score": "92.2%"
    "metric": "BrowseComp accuracy"
    "note": "4个并行agent"
    "result_type": "Steel汇总／厂商自报，非Steel独立复测"
    "source_date": "2026-10-11"
    "collected_at": "2026-11-07 "
    "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
    "reported_rank": 1
    "rank": null
    "track": "Steel 混合配置参考表／不得视为同协议排名"
    "accessed": "2026-11-08"
  }
  {
    "model": "GPT-6 Astra"
    "score": "91.5%"
    "metric": "BrowseComp accuracy"
    "note": "单agent"
    "result_type": "Steel汇总／厂商自报，非Steel独立复测"
    "source_date": "2026-10-11"
    "collected_at": "2026-11-07 "
    "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
    "reported_rank": 2
    "rank": null
    "track": "Steel 混合配置参考表／不得视为同协议排名"
    "accessed": "2026-11-08"
  }
  {
    "model": "Kimi K3"
    "score": "91.2%"
    "metric": "BrowseComp accuracy"
    "note": "300K压缩"
    "result_type": "Steel汇总／厂商自报，非Steel独立复测"
    "source_date": "2026-10-11"
    "collected_at": "2026-11-07 "
    "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
    "reported_rank": 3
    "rank": null
    "track": "Steel 混合配置参考表／不得视为同协议排名"
    "accessed": "2026-11-08"
  }
  {
    "model": "Claude Opus 5"
    "score": "90.8%"
    "metric": "BrowseComp accuracy"
    "result_type": "Steel汇总／厂商自报，非Steel独立复测"
    "source_date": "2026-10-11"
    "collected_at": "2026-11-07 "
    "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
    "reported_rank": 4
    "rank": null
    "track": "Steel 混合配置参考表／不得视为同协议排名"
    "accessed": "2026-11-08"
  }
  {
    "model": "GPT-5.6 Sol"
    "score": "90.4%"
    "metric": "BrowseComp accuracy"
    "result_type": "Steel汇总／厂商自报，非Steel独立复测"
    "source_date": "2026-10-11"
    "collected_at": "2026-11-07 "
    "source_url": "https://leaderboard.steel.dev/leaderboards/browsecomp.md"
    "reported_rank": 5
    "rank": null
    "track": "Steel 混合配置参考表／不得视为同协议排名"
    "accessed": "2026-11-08"
  }
  {
    "rank": null
    "model": "OpenAI Deep Research"
    "score": 51.5
    "metric": "accuracy (%)"
    "track": "原论文Table 3／浏览系统历史实验"
    "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
    "accessed": "2026-11-08"
    "unit": "%"
  }
  {
    "rank": null
    "model": "gpt-4o-search-preview-2025-03-11"
    "score": 1.9
    "metric": "accuracy (%)"
    "track": "原论文Table 3／浏览系统历史实验"
    "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
    "accessed": "2026-11-08"
    "unit": "%"
  }
  {
    "rank": 1
    "model": "o1-2024-12-17 (medium)"
    "score": 9.9
    "metric": "accuracy (%)"
    "track": "原论文Table 3／无浏览历史实验"
    "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
    "accessed": "2026-11-08"
    "unit": "%"
  }
  {
    "rank": 2
    "model": "gpt-4.5-preview-2025-02-27"
    "score": 0.9
    "metric": "accuracy (%)"
    "track": "原论文Table 3／无浏览历史实验"
    "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
    "accessed": "2026-11-08"
    "unit": "%"
  }
  {
    "rank": 3
    "model": "gpt-4o-2024-08-06"
    "score": 0.6
    "metric": "accuracy (%)"
    "track": "原论文Table 3／无浏览历史实验"
    "source_url": "https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf"
    "accessed": "2026-11-08"
    "unit": "%"
  }
]
```

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-08）；[来源2](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

### 覆盖边界

Steel页面自写更新时间2026-10-11，但包含11月新模型，应将该日期视为页面声明而非可靠逐行实验日期；保留reported_rank但取消混合协议的本库rank。原论文浏览/无浏览分别成轨，51.5%为历史Deep Research，不冒充当前榜首。

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-08）；[来源2](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

## 联系方式

### 公开研究联系

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 项目反馈

https://github.com/openai/simple-evals/issues

[来源1](https://github.com/openai/simple-evals)（访问2026-11-07）

### 官方社交入口

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 联系信息边界

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 原始PDF

https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf

[来源1](https://leaderboard.steel.dev/leaderboards/browsecomp.md)（访问2026-11-07）

### PDF SHA-256

1bd473341db82cb66ad7cdff3ee911f9d157c083bad08d33440fa7244a4b1916

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

> 下载PDF字节的SHA-256；不表示已上传。

### PDF字节数

335891

[来源1](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)（访问2026-11-08）

> 下载PDF字节数；归档仍待核实。

### 目录

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 其他官方材料

```json
[
  "https://arxiv.org/pdf/2504.12516"
]
```

[来源1](https://arxiv.org/abs/2504.12516)（访问2026-11-07）

### 论文归档

待核实

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-07）

## 变更记录

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

[来源1](https://openai.com/index/browsecomp/)（访问2026-11-08）
