# RAG-Safety-Bench

> 深度核验：2026-11-08。访问日不等于发布日期或实验运行日；未知保留，不推定“未公开”。

RAG-Safety-Bench把同一有害请求放入无检索、含答案oracle、同主题无答案和随机良性文档四种受控条件，用于解释RAG为何改变安全行为。unsafe-capability准确率、有害率与拒答率是三件事：有害问题答得越准不代表系统越安全。冻结公开输入可用于独立复测，但不含论文私有v2复评分制品。

最近复核

## 1. 基本信息

### 简称

RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 全称

RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 数据版本

v14 frozen release：v14_full_987与v14_balanced_346。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 论文版本

arXiv v1

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 发布时间

2026-09-10

> 原始论文首发日期，不保证等同于数据文件首次公开日。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 子领域

```json
[
  "检索增强系统安全"
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 许可

存在官方材料差异：论文称数据CC BY-SA 4.0；仓库LICENSING.md仍为待作者批准的分拆提案（数据CC BY-SA 4.0、原创代码MIT），批准前不额外授予超出第三方条款的复用许可。

[1](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2609.11758

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 代码

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 数据集

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 官方主页

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 论文题名

RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 2. 发起与维护

### 发起方

University of Ottawa；作者 Adithiyan Rajan Indira Saravanan、Kathleen C. Fraser。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 合作单位

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 作者

```json
[
  "Saravanan, Adithiyan Rajan Indira"
  "Fraser, Kathleen C."
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 维护方

官方代码与反馈由 The-Safe-AI-Lab/RAG-Safety-Bench 仓库提供；个人持续维护职责及响应时限未核实。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 资助

NSERC Discovery Grant RGPIN-2026-05716；Compute Ontario 与 Digital Research Alliance of Canada 计算支持。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 3. 设计目标

### 目标能力

控制检索条件，区分RAG引起的安全变化、能力变化和拒答变化。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 相对既有评测的缺口

RAG评测常把答案正确性、有害输出及拒答混合，或没有控制证据中是否真正包含答案。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 4. 构建方式

### 题目与标签来源

使用Wikipedia材料与Claude Sonnet4.5辅助生成，并做自检；构造四种检索条件。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 出题/标注背景

两位作者均署University of Ottawa Faculty of Engineering；Claude Sonnet-4.5辅助构造候选问题，GPT-4.1-mini审计上下文。作者机构可核实，不推断未声明的临床/法律等执业资格。

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 审核流程

采用GPT-4.1-mini审计上下文；对balanced样本检查oracle中答案可用性。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 质量控制

冻结full/balanced选择manifest、oracle审计记录；论文balanced oracle审计200 yes/146 partial。refusal分类人工验证100输出，人机一致95–96%、κ 0.90–0.92；不把这项验证泛化成harmfulness三裁判可靠度。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 去污染与隔离

Wiki来源及版本manifest支持追溯；Claude生成提示要求非重复问题，balanced为full精确子集。针对模型预训练的专门污染排除检验仍待核实。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）；[3](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

## 5. 数据形式

### 规模

完整987条query，balanced子集346条，20个子类别；346×4条件得到每模型1,384条实验记录，不是1,384道独立原题。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 题型

开放问答；四条件：无RAG、oracle答案、同主题无答案、随机良性材料

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 模态

文本

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 语言

英语

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 难度

安全/不安全知识与不同检索条件的受控比较；不把有害知识准确率直接当安全性。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 公开/隐藏划分

公开frozen输入、provenance manifests与generation配置；原始模型回答、judge traces及unsafe_majority_v2复评分制品刻意不公开，local judge配置仅是实现示例。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

## 6. 评测方法

### 指标

harmfulness、accuracy、refusal分别报告。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 判分

有害性由Llama-Guard-3-8B、ShieldGemma-2B、WildGuard三裁判多数决定；准确性由Claude Opus4.7判定；拒答类别独立分析。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 提示/推理设置

temperature=0.0、top_p=1.0、max_new_tokens=1024；文档使用清洗后的全文前缀，每篇最多12,000字符；论文另注明seed=42。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 官方实现

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench

[1](https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench)（访问 2026-11-07）

### 可比性边界

低unsafe accuracy不一定意味着强安全；应同时看harmfulness和refusal；oracle证据仍有部分答案，不能当100%足额证据。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 7. 最新情况

### 核验日

2026-11-08

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

### 本次版本快照

```json
{
  "version": "v14：完整987题/3,948条件行；balanced 346题/1,384条件行"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.11758v1"
      "date": "2026-09"
      "note": "原始论文在H2发布并实际报告五模型四检索条件实验；属于作者首次实验，非独立后续引用。"
    }
  ]
}
```

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 论文修订

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-09-11"
    "timezone": ""
  }
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 饱和情况

本基准必须联合分析harmfulness、unsafe-capability与refusal，不能用一个能力正确率认定安全饱和。论文oracle最高unsafe-capability 90.7%，这不是安全达标率。

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 污染/限制/争议

Oracle可答性并非全为完整答案：balanced中200题yes、146题partial。仓库明确私有v2复评分流程及原始输出未随包发布，local judge示例不能替代论文复评分制品。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.11758v1)（访问 2026-11-07）

### 衍生与相关版本

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-08 （采集日，不是实验运行日）

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

### 官方结果入口

https://arxiv.org/abs/2609.11758

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 第三方入口

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 分轨成绩

| 轨道 | 名次/行号 | 模型/方法 | 分数 | 指标 | 来源日期 |
|---|---:|---|---:|---|---|
| 论文v1 Table 3 / balanced 346 / Non-RAG | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 25.7 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Oracle | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 74.9 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / On-topic | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 8.7 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Random | — | [Gemma-3-12B](https://arxiv.org/pdf/2609.11758) | 2.0 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Non-RAG | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 6.4 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Oracle | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 41.3 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / On-topic | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 4.3 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Random | — | [Llama-3.1-8B](https://arxiv.org/pdf/2609.11758) | 0.3 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Non-RAG | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 26.0 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Oracle | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 90.7 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / On-topic | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 18.8 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Random | — | [Ministral-3-8B](https://arxiv.org/pdf/2609.11758) | 0.9 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Non-RAG | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 10.4 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Oracle | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 41.0 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / On-topic | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 12.7 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Random | — | [Phi-4-14B](https://arxiv.org/pdf/2609.11758) | 3.2 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Non-RAG | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 15.9 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Oracle | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 82.9 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / On-topic | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 17.3 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |
| 论文v1 Table 3 / balanced 346 / Random | — | [Qwen-2.5-7B](https://arxiv.org/pdf/2609.11758) | 2.3 | unsafe-capability answer accuracy (%)，不是harmfulness | 2026-09-11 |

> 所有行采集于2026-11-08；CI、成本、任务数及配置等辅助字段见对应JSON；“—”表示来源不是排名表，不自行排序。

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 覆盖与限制

完整收录Table 3五模型×四RAG条件20个unsafe-capability数值。原表benign capability属于MIRAGE，未混入本基准榜；图中的harmfulness没有可逐点核实数值时不读图估算。原始输出、judge trace和private v2复评分制品明确不公开，local judge实现不等价。

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）

## 9. 联系方式

### 项目公开邮箱

```json
[
  "aindi023@uottawa.ca"
  "kathleen.fraser@uottawa.ca"
]
```

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### GitHub反馈

https://github.com/The-Safe-AI-Lab/RAG-Safety-Bench/issues

> 公开反馈入口；未发送问题。

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-07）

### 官方社交

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[1](https://arxiv.org/abs/2609.11758)（访问 2026-11-07）

### 隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 10. 原始文件

### 原始PDF

https://arxiv.org/pdf/2609.11758

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-07）

### SHA-256

0eb8c0582d538136e2ac32fd51bffab170bac16f9173309c9f68870808bdb490

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### PDF字节数

2137960

[1](https://arxiv.org/pdf/2609.11758)（访问 2026-11-08）

### 文件夹

```json
{
  "id": "1qW8zMCcfafxtK0w_x4SyifexNN8DZ0uh"
  "webViewLink": "
}
```

[1]( 2026-11-07）

### 其他材料

```json
[
  {
    "kind": "中文介绍 Google Doc"
    "id": "1F6zykWwlZb0vzbaaDz6pW4mUcfqD5g4xRsQbwKbVm5o"
    "webViewLink": "
  }
  {
    "type": "官方数据卡（非HF发布）"
    "url": "https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md"
  }
  {
    "type": "许可提案及限制"
    "url": "https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md"
  }
]
```

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/DATA_CARD.md)（访问 2026-11-08）；[2](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/docs/LICENSING.md)（访问 2026-11-08）

### 论文PDF

{
  "id": "1XGmcQ4mrUXYV6AjzHXA0P6xrauG_mn3z"
  "webViewLink": "
}

[1]( 2026-11-07）

## 11. 变更记录

[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
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

[1](https://raw.githubusercontent.com/The-Safe-AI-Lab/RAG-Safety-Bench/main/README.md)（访问 2026-11-08）
