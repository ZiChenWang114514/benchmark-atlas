# AudioMultiChallenge

> 核验日期：2026-11-07（Asia/Shanghai，UTC+8）。官方资料中文改写；待核实不等于未公开。

已核实存在；官方资料研究快照，未知保留待核实；trending: B

## 基本信息

### 简称

AudioMultiChallenge

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 全称

AudioMultiChallenge

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 基准版本

原始Audio MultiChallenge；编号待核实

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 论文版本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 发布日期

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 主板块

语音

> 编辑归档；跨领域只计主板块。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 领域标签

```json
[
  "多模态",
  "多轮对话"
]
```

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 许可证

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2512.14865

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 官方代码

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 数据地址

https://huggingface.co/datasets/ScaleAI/audiomc

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 官方入口

https://labs.scale.com/leaderboard/audiomc

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 论文标题

Audio MultiChallenge: A Multi-Turn Evaluation of Spoken Dialogue Systems on Natural Human Interaction

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

## 发起与维护

### 机构与发起方

Scale AI

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 合作方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 作者

Advait Gosai、Tyler Vuong、Utkarsh Tyagi、Steven Li、Wenjia You等

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

### 维护方

Scale AI

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 资助方

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 设计目标

### 衡量能力

自然人声多轮对话中的推断记忆、指令保持、自洽与口头修订。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 设计背景

ASR/TTS或单轮合成语音测试难衡量犹豫、打断、环境声音与多轮修订的鲁棒性。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 构建方式

### 题目来源

多智能体先用TTS探索失败策略，提炼为蓝图；人类按蓝图即兴录制自然对话并写原子rubric。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 出题者背景

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 审核流程

专门审核员、独立QC团队及内部研究团队三阶段审核自然性、失败有效性、音频与rubric。

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

### 质量控制

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 去污染

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 数据形式

### 题量与规模

452对话、1,712项rubric、47位说话人；14.99小时用户音频，48kHz；每对话3–8轮。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 题型

提供固定对话历史，只评最终助手回复；用户轮为音频，历史助手轮为文本。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 模态

```json
[
  "音频",
  "文本"
]
```

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 语言

英语

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

### 难度

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 公开与隐藏划分

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 评测方法

### 指标

APR为主要任务全通过率，ARS为rubric部分通过诊断指标。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 评分

o4-mini逐条二元判断；APR要求同一任务所有rubric通过，ARS为每任务rubric通过比例再平均。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 运行设置

固定历史，用户轮音频/助手轮文本，只生成并评分最后一轮；Text Output与Audio Output分别配置。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 官方脚本

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 可比性警示

Text与Audio输出分轨；Audio模式仍评模型输出文本流，不直接评价声音质量；不是MMAU升级版。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 最新情况

### 核查日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 最新版本与热门证据

```json
{
  "version": "原始Audio MultiChallenge；编号待核实",
  "evidence_2026_h2": [
    {
      "url": "https://labs.scale.com/leaderboard/audiomc",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "Scale当前多轮语音榜保留实测结果；主要单一机构展示，不将多条Scale链接算多个独立采用者。"
    }
  ]
}
```

> 热度等级沿候选采用；只保留本轮已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 修订历史

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 饱和情况

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 污染与争议

官网将Self-Coherence/Voice Editing数写83/117；论文表1却写117/83，来源冲突待核实，保留452总数。只评文本流而非原始音频质量。

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

### 版本与已有条目关系

不是已有mmau的新版本；MMAU侧重音频理解问答，本条为自然多轮语音对话；Text/Audio输出子轨不重复新建。

> 已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 为什么近期热门

主要单一机构当前展示或持续评测，不能称为行业广泛采纳。

- 2026-11-07（observed_on）：Scale当前多轮语音榜保留实测结果；主要单一机构展示，不将多条Scale链接算多个独立采用者。 [来源](https://labs.scale.com/leaderboard/audiomc)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07（Asia/Shanghai，UTC+8）

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 官方榜单

https://labs.scale.com/leaderboard/audiomc

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 第三方覆盖

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 核验结果

```json
[
  {
    "rank": 1,
    "model": "gemini-3.8-flash (high)",
    "score": 60.4,
    "metric": "APR (%)；页面综合展示，前三输出模式未明确，待核实",
    "source_url": "https://labs.scale.com/leaderboard/audiomc",
    "accessed": "2026-11-07",
    "source_date": "待核实"
  },
  {
    "rank": 2,
    "model": "salesforce-launa-omni-1",
    "score": 59.69,
    "metric": "APR (%)；页面综合展示，前三输出模式未明确，待核实",
    "source_url": "https://labs.scale.com/leaderboard/audiomc",
    "accessed": "2026-11-07",
    "source_date": "待核实"
  },
  {
    "rank": 3,
    "model": "gemini-4-argon (high)",
    "score": 58.41,
    "metric": "APR (%)；页面综合展示，前三输出模式未明确，待核实",
    "source_url": "https://labs.scale.com/leaderboard/audiomc",
    "accessed": "2026-11-07",
    "source_date": "待核实"
  }
]
```

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 覆盖说明

仅记录已打开页面可读的当前分数；表内模型配置保留，不将不同harness当裸模型对比。榜表更新时间：待核实（采集日不是榜表更新日）

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

```json
[
  "advait.gosai@scale.com"
]
```

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

### 公开反馈

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 官方社交

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 隐私政策

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2512.14865

> 官方arXiv原论文PDF入口；本组不下载、不上传Drive。

[来源1](https://arxiv.org/abs/2512.14865)（访问 2026-11-07）

### PDF SHA-256

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### PDF字节数

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### Drive文件夹

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "官方方法或项目页",
    "url": "https://labs.scale.com/leaderboard/audiomc",
    "accessed": "2026-11-07"
  }
]
```

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Shanghai (UTC+8)",
    "change": "首次建立中文近期热门研究条目；完整11节、分版榜单、证据与缺口标注，不上传Drive。"
  }
]
```

[来源1](https://labs.scale.com/leaderboard/audiomc)（访问 2026-11-07）

