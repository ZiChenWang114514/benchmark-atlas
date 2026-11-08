# HSS

> Benchmark Constitution｜逐源深度核查：2026-11-08。采集日期不代表实验日期；待核实不等于未公开。

HSS针对成人直觉可解、但模型容易过度思考的视觉隐含推理：522道人工作答与rubric题，含288图像和234视频。补齐arXiv论文及2026-10-08题卡修订，明确标注MIT只覆盖标注，不覆盖原始媒体。

导读依据：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）；[2](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）；[3](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

## 基本信息

### 简称

HSS

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 全称

Humanity's Sixth Sense

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 基准版本

522题冻结发布；HF更新记录2026-10-08新增全部234视频证据时间窗并修订一个题目提示。

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

### 发布日期

2026-10-07（arXiv初稿日期，不冒充数据集单独首发日）

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

### 主板块

多模态

> Benchmark Atlas 编辑归档。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 领域

```json
[
  "直觉视觉推理"
  "视频理解"
  "空间/社会推理"
]
```

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 许可与使用范围

```json
{
  "annotations": "MIT：提示、参考答案、rubric、taxonomy标签"
  "media": "图像/视频不受上述MIT授权覆盖；权利仍归原作者，HF声明仅随基准提供供非商业研究/评测，使用者须遵守原媒体条款。"
}
```

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 论文入口

https://arxiv.org/abs/2610.08966

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）；[2](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

### 官方代码

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 数据入口

https://huggingface.co/datasets/ScaleAI/HSS

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 官方主页

https://labs.scale.com/leaderboard/hss

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 论文标题

Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

## 发起与维护

### 发起方

Scale AI

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 合作与作者单位

Elorian；另有University of California, Santa Cruz作者单位。

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）；[2](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 作者

 Xingang Guo¹*, Jing Gu²*, Brian Jang¹*, Renxiong Wang¹, Utkarsh Tyagi¹, Daniel Quigley¹, Steven Li¹, David Yan², Daniel Yue Zhang¹, Darvin Yi¹, Forrest Huang², HiJae Kim¹, Tianyi Zhang², Jared Lichtarge², Jihua Huang², Le Xue², Manan Tomar², Qiuyi Richard Zhang², Ruofei Yu², Seth Neel², Yaning Hu², Marcella Valentine², Xinzhe Jiang², Daniel Evans¹, Chenguang Wang¹·³, Dustin Tran², Tong Zhao¹, Yinfei Yang², Yunzhong He¹ ¹Scale AI, ²Elorian, ³University of California, Santa Cruz · *Equal contribution

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 维护方

Scale AI

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 资助与资源支持

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

## 设计目标

### 测量能力

人类一眼即可推断的隐含时间、空间、社会与抽象结构（因果、轨迹、权力关系、潜规则等）。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 与既有基准的差异

旧视觉基准常侧重专业知识分析或低层感知，缺少对成人一眼可得的隐含时空、社会、因果结构的测量。HSS排除仅靠清晰裁剪即可解决的感知题及专业知识题。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）。

## 构建方式

### 题目来源

人类撰写提示，配图像/视频；视频媒体来自公开网络，题目为新撰写

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 出题者背景

受训人类标注者原创；题目与答案须满足成人直觉可理解、无需专业学术训练的原则，每题作者外至少三位独立审核者。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）；[2](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 审核流程

共撰写3,466题，经三轮独立评审收录522题（15.1%通过率）

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 质量控制

三轮独立一致批准；Edit需从头复审，Drop永久剔除。3466→1164→559→522题；删除纯感知、歧义和无法形成共识题。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）。

### 去污染与泄漏控制

题目新撰写，但公开网络媒体可能已在训练数据中，无法完全排除

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

## 数据形式

### 规模与统计口径

522 题：4个领域、11个子领域；288图像题、234视频题（视频总17.6小时，中位76秒，最长28分钟）；723条评分标准

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 题型

自由作答，按 rubric 判分

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 模态

```json
[
  "图像"
  "视频（无音轨、无字幕）"
]
```

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 语言

公开prompt/参考答案及官方提示以英语呈现；完整语种分布统计待核实。

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）。

### 难度

人类标注者93.1%；首发最佳模型53.6%，模型中位30.9%

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 公开与隐藏划分

HF仅test split，共522题；视频证据时间窗仅为分析元数据，评测必须输入完整视频，不得只喂证据片段。

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

## 评测方法

### 指标

Pass@1（每题3次尝试平均），附95%聚类 bootstrap 区间；rubric 分作诊断

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 评分规则

Claude-Opus-5 作为自动 LLM 裁判逐条判定

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 提示、采样与工具设置

每模型每题3次；原生视频优先，否则均匀采帧上限500帧并服从提供商更严格上限；图像原分辨率，必要时降采样。官网概述high/最大输出，但当前榜行存在max/xhigh等实际设置，按行保留而非强行改写为全high。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）；[2](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）。

### 官方脚本

官方评测 harness（含模型注册、评测与评分提示）

> 仓库地址待核实。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 可比性警告

依赖 LLM 裁判，存在自偏好风险；心智理论结果只代表与标注者一致度。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

## 最新情况

### 核查时间

2026-11-08

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）；[2](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）。

### 最新数据状态

522题；HF 2026-10-08记录：添加全部234视频时间窗、修订task 6a7f82ad5cfeb63114fa869b提示；不是新增题量。

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 论文修订历史

```json
[
  {
    "version": "v1"
    "submitted_at": "2026-10-07"
    "timezone": ""
  }
  {
    "version": "v2"
    "submitted_at": "2026-10-09"
    "timezone": ""
  }
]
```

> arXiv原始UTC时间已转换为；不等于数据集版本变更。

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

### 饱和度与证据边界

论文明确称尚未饱和：首发最佳53.6%，人类20位标注者基线93.1%；当前官网最高55.40 ± 4.20，不能把首发25模型数量当当前29行榜数量。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）；[2](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）。

### 污染与已知问题

视觉通道限定、裁判依赖、媒体可能已被训练见过（官方 Limitations）。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 相关与衍生基准

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

## 榜单快照

### 采集日期

2026-11-08 （采集日，不是运行或榜单更新日）

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）。

### 官方结果入口

https://labs.scale.com/leaderboard/hss

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 独立评测入口

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 结构化结果

```json
[
  {
    "rank": 1
    "model": "Gemini-4-Argon (high)"
    "score": "55.40 ± 4.20"
    "metric": "Pass@1"
    "result_type": "官方榜单快照"
    "source_date": "待核实（页面未标榜单更新日）"
    "collected_at": "2026-11-08 "
    "source_url": "https://labs.scale.com/leaderboard/hss"
    "track": "官方当前522题，pass@1，按模型行保留推理设置"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 2
    "model": "GPT-6-Astra (max)"
    "score": "53.60 ± 4.10"
    "metric": "Pass@1"
    "result_type": "官方榜单快照"
    "source_date": "待核实（页面未标榜单更新日）"
    "collected_at": "2026-11-08 "
    "source_url": "https://labs.scale.com/leaderboard/hss"
    "track": "官方当前522题，pass@1，按模型行保留推理设置"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 3
    "model": "GPT-6.1-Sol (max)"
    "score": "46.60 ± 3.80"
    "metric": "Pass@1"
    "result_type": "官方榜单快照"
    "source_date": "待核实（页面未标榜单更新日）"
    "collected_at": "2026-11-08 "
    "source_url": "https://labs.scale.com/leaderboard/hss"
    "track": "官方当前522题，pass@1，按模型行保留推理设置"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 4
    "model": "Claude-Opus-5.5 (xhigh)"
    "score": "44.60 ± 3.80"
    "metric": "Pass@1"
    "result_type": "官方榜单快照"
    "source_date": "待核实（页面未标榜单更新日）"
    "collected_at": "2026-11-08 "
    "source_url": "https://labs.scale.com/leaderboard/hss"
    "track": "官方当前522题，pass@1，按模型行保留推理设置"
    "snapshot_date": "2026-11-08 "
  }
  {
    "rank": 5
    "model": "Muse Wonder 1.0 (max)"
    "score": "43.70 ± 4.20"
    "metric": "Pass@1"
    "result_type": "官方榜单快照"
    "source_date": "待核实（页面未标榜单更新日）"
    "collected_at": "2026-11-08 "
    "source_url": "https://labs.scale.com/leaderboard/hss"
    "track": "官方当前522题，pass@1，按模型行保留推理设置"
    "snapshot_date": "2026-11-08 "
  }
]
```

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）。

### 覆盖与局限

官网当前可读29行模型，方法摘要的25模型指首发论文。±为按题聚类bootstrap的95%区间半宽，不是标准差或三次重复的标准误。当前官网榜与论文首发结果不能冒充同日实验。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）；[2](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）。

## 联系方式

### 官方公开邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 仓库反馈

待核实

> 官网提到evaluation harness，但公开页面/论文未提供可验证GitHub仓库地址；不编造仓库。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）；[2](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

### 官方社区

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 隐私与联系边界

HF媒体权利人可在数据集讨论区提供task_id或文件路径申请下架；不收集私人联系方式。

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）。

## 原始文件

### 论文PDF

https://arxiv.org/pdf/2610.08966

来源：[1](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

### PDF SHA-256

86538d4f2ff2e648a97693fff6bfc2f2c25d99c71f877f4d7797430d4ef283ed

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）。

### PDF字节数

```json
9845488
```

> 2026-11-08 下载PDF的实测值；未重新下载内副本，不证明其与本次文件相同。

来源：[1](https://arxiv.org/pdf/2610.08966)（访问 2026-11-08）。

### 已有文件夹

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

### 其他官方文档

```json
[
  {
    "type": "官方数据卡/方法入口"
    "url": "https://huggingface.co/datasets/ScaleAI/HSS"
  }
  {
    "type": "官方说明"
    "url": "https://labs.scale.com/leaderboard/hss"
  }
]
```

来源：[1](https://huggingface.co/datasets/ScaleAI/HSS)（访问 2026-11-08）；[2](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）。

### 已有 PDF归档

待核实

> 本组按任务要求不上传；原始PDF URL见original_files。

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）。

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

来源：[1](https://labs.scale.com/leaderboard/hss)（访问 2026-11-07）；[2](https://arxiv.org/abs/2610.08966)（访问 2026-11-08）；[3](https://labs.scale.com/leaderboard/hss)（访问 2026-11-08）。

