# Fortress

> Benchmark Constitution，研究快照 2026-11-07。采集时间不等于成绩实跑或榜单更新时间。

FORTRESS衡量国家安全与公共安全双用途场景中的防护稳健性，同时用主题相近的良性请求量化过度拒绝。它不是直接测“危险知识掌握率”；当前ARS榜与论文公开集成绩不同，低风险分还需结合ORS解读。

最近复核

## 基本信息

### 简称

Fortress

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 全称

Frontier Risk Evaluation for National Security and Public Safety

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 基准版本

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 论文版本

arXiv v2（论文修订，不等于数据集版本）

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 发布日期

2025-06-18（arXiv初稿时间，不是数据集的独立发布日期）

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 主板块

安全

说明：Benchmark Constitution 编辑归档，不作为官方分类。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 领域标签

- 公共安全
- 前沿风险

说明：编辑标签

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 许可与范围

官方HF卡license标签为CC BY 4.0；卡片正文另要求仅用于安全评估并禁止adversarial training/research。并列记录两种原文声明，不自行消解其许可范围张力。

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）


### 论文

https://arxiv.org/abs/2506.14922

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 代码

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 数据入口

https://huggingface.co/datasets/ScaleAI/fortress_public

说明：已读取的公开HF卡revision: 0c096becbc75bb12065c8059a53960c7f0d4d35c；只固定公开卡/仓库状态，不外推为私有测试版本。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）


### 官方主页

https://labs.scale.com/leaderboard/fortress

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 论文标题

FORTRESS: Frontier Risk Evaluation for National Security and Public Safety

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


## 发起与维护

### 发起/作者单位

Scale AI

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 合作与支持

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 作者

- Christina Q. Knight
- Kaustubh Deshpande
- Ved Sirdeshmukh
- Meher Mankikar
- Scale Red Team
- SEAL Research Team
- Julian Michael

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 维护方

Scale Labs

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 资助

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


## 设计目标

### 衡量能力

国家安全与公共安全双用途场景下，模型防护的有害协助风险和良性过度拒绝。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 设计背景

不只测双用途知识能力，还以配对良性提示衡量安全—实用性权衡。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


## 构建方式

### 题目来源

专家构建对抗提示，覆盖CBRNE、政治暴力／恐怖主义、犯罪／金融非法活动。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 出题者背景

经验丰富的人类红队人员；论文附录列多学科背景，但Limitations承认他们未必具有真实恶意行为者的深领域知识，因此不将其全部描述为CBRNE领域专家。

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 审核流程

每条对抗提示配4–7条二元评分rubric及主题相近良性提示。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 质量控制

三裁判按条目多数投票，非单一粗粒度关键词检查。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 污染控制

排行榜包含公开与私有提示；私有提示用于减少污染。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


## 数据形式

### 题量

当前官方榜介绍为over 1,010条对抗提示、其中500公开；HF公开train split为500行，每行同时有adversarial_prompt、4–7条rubric及benign_prompt，故500行不是1000条独立题。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）


### 任务形式

单轮对抗请求及配对良性请求。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 模态

- 文本

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 语言

公开论文及公开提示样例为英语；未据此推断另有多语言覆盖。

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）；[一手资料2](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）


### 难度与分层

按3风险域、10子域以及专家对抗提示构建，不提供可与普通知识题直接比较的统一难度等级；ARS反映防护响应而非领域知识考试分数。

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 公开与隐藏划分

公开500对抗/良性配对（HF split名为train仅为存储命名）；当前榜还使用私有提示。2025论文的500公开集结果与当前公私混合榜不同。

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）；[一手资料2](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料3](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


## 评测方法

### 指标

Average Risk Score (ARS)与Over-Refusal Score (ORS)，均越低越好。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 评分

ARS：每条rubric由o3、Claude 3.7 Sonnet、Gemini 2.5 Pro多数表决；ORS由GPT-4o-mini拒绝检测。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 提示与运行协议

原论文实验：普通模型temperature=0.7，reasoning模型=1.0；各模型最大completion/thinking budget见表8–9。仅对原论文协议成立，不擅自套用于当前新增模型。

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 评测脚本

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 可比性警示

当前Performance Comparison的ARS与正文Rankings历史表、原论文500公开集不同；只录当前榜ARS，不把老表ORS贴给新模型，也不把±数值未经定义当标准误。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


## 最新情况

### 核查日期

2026-11-07 （资料快照日期）

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 版本与采用证据

- **version**：待核实
- **heat_confidence**：B
- **why_trending**：主要是单一机构当前展示或厂商持续自评，不代表全行业广泛采纳。
- **evidence_2026_h2**：- - **url**：https://labs.scale.com/leaderboard/fortress
    - **date**：2026-11-07
    - **date_type**：observed_on
    - **organization**：官方维护方
    - **note**：已打开当前官方方法与榜单；观察日不冒充发布时间。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 材料沿革

- - **version**：v1
  - **submitted_at_kst**：2025-06-18
  - **timezone**：
- - **version**：v2
  - **submitted_at_kst**：2025-06-25
  - **timezone**：

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 饱和情况

当前最低ARS为5.78（越低越好），但缺少这些新模型同步ORS，且ARS是裁判对风险rubric的评分；不能单凭低ARS认定安全—实用性权衡已经饱和。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 污染与局限

公开提示可能污染；当前榜使用私有部分降低风险。论文局限包括单轮静态提示、红队非全部深领域专家、每子域样本有限；低ARS不等于已实测真实世界危害为零。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）；[一手资料2](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 版本/衍生关系

公开数据与私有排行榜扩展属于同一FORTRESS系列；良性配对用于ORS，不是第二个独立benchmark。

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）；[一手资料2](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


## 榜单快照

### 快照日期

2026-11-07 （快照日，非实跑日）

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 官方榜

https://labs.scale.com/leaderboard/fortress

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 其他评测入口

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 分轨结果（结构化快照）

```json
[
  {
    "rank": 1
    "model": "claude-opus-5-5-max"
    "score": 5.78
    "metric": "Average Risk Score (ARS), 越低越好"
    "displayed_uncertainty": 1.26
    "uncertainty_definition": "待核实：当前显示±，未据此推断SE或CI"
    "scope": "当前Performance Comparison，非正文历史Rankings表"
    "source_url": "https://labs.scale.com/leaderboard/fortress"
    "accessed": "2026-11-07"
    "ORS": "待核实：当前这些行未给配对ORS"
    "result_type": "官方当前页面快照"
  }
  {
    "rank": 2
    "model": "muse-spark-open"
    "score": 7.64
    "metric": "Average Risk Score (ARS), 越低越好"
    "displayed_uncertainty": 1.15
    "uncertainty_definition": "待核实：当前显示±，未据此推断SE或CI"
    "scope": "当前Performance Comparison，非正文历史Rankings表"
    "source_url": "https://labs.scale.com/leaderboard/fortress"
    "accessed": "2026-11-07"
    "ORS": "待核实：当前这些行未给配对ORS"
    "result_type": "官方当前页面快照"
  }
  {
    "rank": 3
    "model": "gpt-oss-120b"
    "score": 8.24
    "metric": "Average Risk Score (ARS), 越低越好"
    "displayed_uncertainty": 1.93
    "uncertainty_definition": "待核实：当前显示±，未据此推断SE或CI"
    "scope": "当前Performance Comparison，非正文历史Rankings表"
    "source_url": "https://labs.scale.com/leaderboard/fortress"
    "accessed": "2026-11-07"
    "ORS": "待核实：当前这些行未给配对ORS"
    "result_type": "官方当前页面快照"
  }
  {
    "rank": 4
    "model": "Claude Haiku 5.5"
    "score": 9.48
    "metric": "Average Risk Score (ARS), 越低越好"
    "displayed_uncertainty": 1.34
    "uncertainty_definition": "待核实：当前显示±，未据此推断SE或CI"
    "scope": "当前Performance Comparison，非正文历史Rankings表"
    "source_url": "https://labs.scale.com/leaderboard/fortress"
    "accessed": "2026-11-07"
    "ORS": "待核实：当前这些行未给配对ORS"
    "result_type": "官方当前页面快照"
  }
  {
    "rank": 5
    "model": "claude-opus-4-5-20251101-thinking"
    "score": 9.63
    "metric": "Average Risk Score (ARS), 越低越好"
    "displayed_uncertainty": 2.11
    "uncertainty_definition": "待核实：当前显示±，未据此推断SE或CI"
    "scope": "当前Performance Comparison，非正文历史Rankings表"
    "source_url": "https://labs.scale.com/leaderboard/fortress"
    "accessed": "2026-11-07"
    "ORS": "待核实：当前这些行未给配对ORS"
    "result_type": "官方当前页面快照"
  }
]
```

[榜单原始资料](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）

### 覆盖范围

当前Performance Comparison前五ARS已读到：5.78、7.64、8.24、9.48、9.63。ARS/ORS均越低越好，但当前新模型ORS与±定义尚待核实；未把原论文或正文历史表混成当前配对数据，未将观察日当运行日。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


## 联系方式

### 公开研究邮箱

- christina.knight@scale.com

[一手资料1](https://arxiv.org/abs/2506.14922)（访问 2026-11-07）


### 问题反馈

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 机构公开渠道

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 隐私政策

https://scale.com/legal/privacy

[一手资料1](https://scale.com/research/fortress)（访问 2026-11-07）


## 原始文件

### 论文PDF

https://arxiv.org/pdf/2506.14922

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 源站PDF SHA-256

0ad431682c60664c7af8efc9620eff9d384dfa55a0324f304d1a738a8a94edfd

说明：实际下载的源站PDF字节摘要；不据此声称副本已更新。

[一手资料1](https://arxiv.org/pdf/2506.14922)（访问 2026-11-07）


### 源站PDF字节数

4776777

[一手资料1](https://arxiv.org/pdf/2506.14922)（访问 2026-11-07）


### 资料目录

待核实

状态：待核实。

说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

[一手资料1](https://labs.scale.com/leaderboard/fortress)（访问 2026-11-07）


### 其他官方资料

- - **type**：核验的官方原始资料
  - **url**：https://huggingface.co/datasets/ScaleAI/fortress_public
  - **accessed**：2026-11-07

[一手资料1](https://huggingface.co/datasets/ScaleAI/fortress_public)（访问 2026-11-07）


### PDF归档

待核实

仅核对源站PDF和已有归档引用，未上传或覆盖文件。

## 变更记录

- - **date**：2026-11-07
  - **timezone**：
  - **change**：首次建立近期热门中文研究条目；逐项核实官方材料、分轨结果并保留缺口。
- - **date**：2026-11-07
  - **timezone**：
  - **change**：R2逐篇打开arXiv摘要与PDF文本（有论文者）、已定位官方README/LICENSE、HF数据卡及榜页；补字段并分轨刷新成绩，重写中文11节，保留无法核实项。
