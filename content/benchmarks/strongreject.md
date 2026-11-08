# StrongREJECT

最近复核

StrongREJECT首先是越狱输出评估器与313请求提示集，而不是一张通用模型安全榜。它关注回答是否具体、可信且真正有助于有害请求，纠正“没有拒绝就是越狱成功”的误判。下方MAE榜只验证自动评分与人工标签的一致性，越低越好，不代表目标模型更安全。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）；[来源2](https://github.com/dsbowen/strong_reject)（访问 2026-11-08）；[来源3](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）

## 基本信息

### 简称

StrongREJECT

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 全称

StrongREJECT

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 基准版本

313请求公开提示集；rubric与Gemma-2B微调评估器是两种实现，独立包release版本待核实。

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 论文版本

v2（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 发布日期

2024-02-16 （arXiv v1 2024-02-16；arXiv网页历日为2024-02-15 UTC）

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 主板块

安全

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 领域

```json
[
  "有害请求完成度与拒答评价"
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 许可与适用范围

MIT（本项目代码）；汇编数据继承来源约束：README注明部分来源无许可，不能把MIT直接套用全部数据。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2402.10260

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方代码

https://github.com/dsbowen/strong_reject

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 数据

https://github.com/dsbowen/strong_reject

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方入口

https://strong-reject.readthedocs.io/

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 论文标题

A StrongREJECT for Empty Jailbreaks

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 发起与维护

### 发起方

UC Berkeley / Center for Human-Compatible AI 相关作者团队。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 合作/参与机构

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 作者

```json
[
  "Souly, Alexandra"
  "Lu, Qingyuan"
  "Bowen, Dillon"
  "Trinh, Tu"
  "Hsieh, Elvis"
  "Pandey, Sana"
  "Abbeel, Pieter"
  "Svegliato, Justin"
  "Emmons, Scott"
  "Watkins, Olivia"
  "Toyer, Sam"
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 维护方

官方代码与反馈由 dsbowen/strong_reject 仓库提供；个人持续维护职责及响应时限未核实。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 资助

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 设计目标

### 衡量能力

判定越狱输出是否真正提供具体、可信的有害帮助，而不只判断是否拒答。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 设计背景

简单非拒答指标会把空泛、无用或不可信回答错误计为越狱成功。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 构建方式

### 题目来源

从既有越狱数据与系统卡中筛选整理，包括AdvBench、DAN、MasterKey、MaliciousInstruct、HarmfulQ及GPT-4 System Card；按6类危害组织。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 出题者背景

研究团队结合人工、GPT-4与pplx-70b-online辅助编写及核实。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 审核流程

语义去重，检查拒答、回答可能性与提示质量，并人工复核。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 质量控制

以人类标注验证结构化rubric与微调评估器。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 污染控制

汇编既有公开有害请求，论文不声称提示库无预训练污染；对评估器验证集与微调训练/验证提示作区分。不能把评估器验证一致性当成目标模型未见过请求的证明。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

## 数据形式

### 题量

313 个禁止请求，6 大类别。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 任务形式

禁止请求与回答完成度评价；不在本页复现危害操作内容

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 模态

文本

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 难度

关注回答的具体性和说服力，而非仅统计拒答词是否出现。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 公开与隐藏划分

公开提示与评估器；模型裁判验证集与实际目标模型攻击测试不是相同对象。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 评测方法

### 指标

拒答、具体性、说服力的组合分，归一化到0–1；另有评估器与人类的一致性指标。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 评分

拒答时记零；否则结合具体性、说服力；提供rubric评估器与Gemma-2B微调评估器。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 运行设置

按官方评价提示对有害请求及目标回答打分，必须记录裁判模型版本。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 评测工具

strong_reject包提供evaluate_dataset；rubric-based LLM evaluator和fine-tuned Gemma 2B evaluator是两个不同实现，报告需明确选择。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 可比性

rubric评分、微调评估器分数和二值ASR不同；评估器MAE也不是目标模型的安全分。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 当前版本及历史热度证据

本次官方文档仍描述六类请求与两种StrongREJECT评价器；没有将WMDP beta混入原始313题库存。

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2024-02-16"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2024-08-27"
    "timezone": ""
  }
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 饱和与能力边界

本基准核心是越狱评估器而非统一模型能力榜。论文MAE=0.077/0.084衡量相对人工标签误差，不能用接近0或1判断目标模型安全能力饱和。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 风险与争议

README列明若干源数据无license；项目MIT不自动补足来源授权。H2裁判比较使用共享Qwen3.8-27B-Uncensored backbone的rubric版，不能视为原生微调评分器验证。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）；[来源2](https://arxiv.org/html/2609.10594v1)（访问 2026-11-07）

### 系列与衍生关系

官方文档另有WMDP开放问答beta：从多选转开放题、附危险性权重及StrongREJECT风格评价器；不是原313请求集的同版本扩容。

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）

## 榜单快照

### 快照日期

2026-11-08

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）；[来源2](https://github.com/dsbowen/strong_reject)（访问 2026-11-08）；[来源3](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）

### 官方入口

https://arxiv.org/abs/2402.10260

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 独立来源

待核实

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 分来源与协议结果

#### paper v2 Table 1 evaluator validation

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 9 | String matching | 0.58 | MAE vs human labels；lower is better | {"bias":0.484,"mae_95ci_plus_minus":0.03,"mae_human_nonzero":0.372,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":-0.394} |
| 8 | Jailbroken - binary | 0.407 | MAE vs human labels；lower is better | {"bias":0.354,"mae_95ci_plus_minus":0.03,"mae_human_nonzero":0.254,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":-0.291} |
| 7 | PICT | 0.291 | MAE vs human labels；lower is better | {"bias":0.232,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.278,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":0.101} |
| 6 | GPT-4 Judge | 0.262 | MAE vs human labels；lower is better | {"bias":0.208,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.212,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.157} |
| 5 | PAIR | 0.205 | MAE vs human labels；lower is better | {"bias":0.152,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.224,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.249} |
| 4 | OpenAI moderation API | 0.197 | MAE vs human labels；lower is better | {"bias":-0.161,"mae_95ci_plus_minus":0.02,"mae_human_nonzero":0.761,"mae_human_nonzero_95ci_plus_minus":0.04,"spearman_jailbreak_rank":-0.103} |
| 3 | HarmBench | 0.09 | MAE vs human labels；lower is better | {"bias":0.013,"mae_95ci_plus_minus":0.01,"mae_human_nonzero":0.239,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.819} |
| 2 | StrongREJECT fine-tuned | 0.084 | MAE vs human labels；lower is better | {"bias":-0.023,"mae_95ci_plus_minus":0.01,"mae_human_nonzero":0.244,"mae_human_nonzero_95ci_plus_minus":0.02,"spearman_jailbreak_rank":0.9} |
| 1 | StrongREJECT rubric | 0.077 | MAE vs human labels；lower is better | {"bias":0.012,"mae_95ci_plus_minus":0.01,"mae_human_nonzero":0.196,"mae_human_nonzero_95ci_plus_minus":0.03,"spearman_jailbreak_rank":0.846} |

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）

### 覆盖与时效

完整收录论文Table 1九个自动评估器MAE等验证统计；rank仅按MAE越低越好重排，非被攻击模型的安全排名。HF walledai/StrongREJECT卡已打开，但它是第三方镜像且未列独立实时统一安全榜。

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/walledai/StrongREJECT)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

```json
[
  "alexandrasouly@gmail.com"
  "sdt@berkeley.edu"
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-07）

### 官方反馈

https://github.com/dsbowen/strong_reject/issues

> 公开反馈入口；未发送问题。

[来源1](https://raw.githubusercontent.com/dsbowen/strong_reject/main/README.md)（访问 2026-11-07）

### 公开社区

官方文档和GitHub Issues为已核实反馈入口；不将第三方HF镜像当官方维护账号。

[来源1](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）；[来源2](https://github.com/dsbowen/strong_reject)（访问 2026-11-08）

### 隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2402.10260

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-08）

### PDF SHA-256

10caab98ed5a75b019ef3c8a6697527f83edda067516996d2cb612f02ff746bc

> 本次实际下载的PDF字节计算；未上传。

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-08）

### PDF字节数

```json
600542
```

[来源1](https://arxiv.org/pdf/2402.10260)（访问 2026-11-08）

### 文件夹

```json
{
  "id": "1Rjik34iUFEZBTeLqjtMXs8us5Ea3NsvV"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

### 其他材料

```json
[
  {
    "kind": "中文介绍"
    "id": "15uyExEs5PXDPaRliDItqwcrgvzhdto9GUXOBBbZueIE"
    "webViewLink": "
  }
  {
    "type": "已打开一手材料"
    "url": "https://arxiv.org/abs/2402.10260"
    "accessed": "2026-11-08"
  }
  {
    "type": "已打开一手材料"
    "url": "https://github.com/dsbowen/strong_reject"
    "accessed": "2026-11-08"
  }
  {
    "type": "已打开一手材料"
    "url": "https://strong-reject.readthedocs.io/en/latest/"
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）；[来源2](https://github.com/dsbowen/strong_reject)（访问 2026-11-08）；[来源3](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）

### PDF归档

```json
{
  "id": "1qVDkFDcnFVOGYrw9wE7T7e6myH6wJoor"
  "webViewLink": "
}
```

[来源1]( 2026-11-07）

## 变更记录

```json
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
```

[来源1](https://arxiv.org/abs/2402.10260)（访问 2026-11-08）；[来源2](https://github.com/dsbowen/strong_reject)（访问 2026-11-08）；[来源3](https://strong-reject.readthedocs.io/en/latest/)（访问 2026-11-08）
