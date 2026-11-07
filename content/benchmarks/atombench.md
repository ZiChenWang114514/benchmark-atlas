# AtomBench

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
AtomBench
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 全称
AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v2；最近论文日期 2026-07-07
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 发布日期
2025-10-17（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 板块
材料
来源：[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "晶体结构生成与重构"
]
来源：[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2510.16165
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 代码仓库
https://github.com/atomgptlab/atombench
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 数据集
https://github.com/atomgptlab/atombench
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 官方主页
https://atomgptlab.github.io/jarvis_leaderboard/Special/AtomGenBench/
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 论文题名
AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
West Virginia University与Johns Hopkins University署名团队。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Campbell, Charles Rhys",
  "Romero, Aldo H.",
  "Choudhary, Kamal"
]
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 维护方
atomgptlab/atombench官方仓库。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
给定晶体相关信息后的重构保真度，量化晶格/原子坐标及匹配覆盖。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 弥补缺口
生成器获得条件信息不等，单看匹配成功样本RMSD会掩盖失败；强调全样本ccRMSD。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
JARVIS Supercon-3D与Alexandria DS-A/B超导体结构数据。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 构建者背景
凝聚态物理、材料生成模型与计算材料研究者。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 审核流程
固定目标结构、训练/测试与模型条件组；用统一结构匹配器计算重构指标。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 质量控制
CSV保留目标与预测CIF/POSCAR，统一结构匹配与连续纠正误差。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 去污染
同源结构训练/测试与生成器预训练可能重叠；需要逐结构审计，不能默认所有模型同等未见。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

## 5. 数据形式

### 规模
H2比较JARVIS103个测试目标、Alexandria825个测试目标；官网旧Alexandria榜显示dataset size8253，是旧口径，不混为测试825。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）；[https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/](https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/)（采集 2026-11-07）

### 任务类型
条件晶体重构；不是无条件从零发现新晶体。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 模态
CIF/POSCAR晶体结构、晶格/坐标、超导临界温度等条件。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 语言
结构与数值格式，Python工具。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 难度
依给定条件信息和目标结构而变，无固定自然语言难度分档。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 公开与隐藏划分
JARVIS/Alexandria训练测试协议；原文与旧官网的样本口径须分开。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

## 6. 评测方法

### 指标
match rate、匹配样本RMSD、全测试集ccRMSD、晶格MAE与KLD；官网旧子榜可能用RMSE。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 评分方式
结构匹配器处理对称性/容差；ccRMSD对每个测试结构定义，避免只报成功者。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 提示与运行配置
不是统一LLM提示；AtomGPT、CDVAE、FlowMM、MatterGen需按条件可见信息分组。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 官方脚本
https://github.com/atomgptlab/atombench
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 可比性警告
H2 ALIGNN-CSP使用32候选+力场筛选/弛豫/对称处理，与单次生成器不等预算。旧榜RMSE不能直接代替新版ccRMSD。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2609.19487v1",
      "date": "2026-09-16",
      "note": "ALIGNN 2.0 §2.4及表7–8使用 AtomBench 的结构匹配和重构评测定义，对比晶体生成器。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors",
    "authors": [
      "Campbell, Charles Rhys",
      "Romero, Aldo H.",
      "Choudhary, Kamal"
    ],
    "release": "2025-10-17",
    "latest": "2026-07-07",
    "version": "v2"
  }
}
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 饱和情况
不同条件/指标下优胜模型不同，不宜统一宣布饱和。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 污染与争议
当前论文v2明确重构而非de novo生成；旧官网AtomGenBench名称与新版AtomBench指标不同；保留版本边界。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 官方榜/结果入口
https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/
来源：[https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/](https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
官网旧Tc_a子榜（2025-10-17提交标签，8253口径）晶格a RMSE：cdvae_invatoms0.3137、atomgpt_invatoms0.4821、flowmm_invatoms1.003。H2 Table8新测试825：MatterGen_Tc match0.6352/RMSD0.0182/ccRMSD0.2440；ALIGNN-CSP0.5661/0.0253/0.3177；AtomGPT_Tc0.4939/0.0347/0.5228。非等预算排序。
来源：[https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/](https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "crhysc@gmail.com",
  "alromero@mail.wvu.edu",
  "kchoudh2@jhu.edu"
]
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### Issues
https://github.com/atomgptlab/atombench/issues
来源：[https://github.com/atomgptlab/atombench](https://github.com/atomgptlab/atombench)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2510.16165
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 原始PDF SHA256
cf0464f374b215992e91190f1bc398d1dbb01af8199cb2fcb7b4fdb0ae39dcf6
来源：[https://arxiv.org/pdf/2510.16165](https://arxiv.org/pdf/2510.16165)（采集 2026-11-07）

### 原始PDF字节数
5917762
来源：[https://arxiv.org/pdf/2510.16165](https://arxiv.org/pdf/2510.16165)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1AGppe7PfAY02bOHYn6m1h1RjoUZ2h3ON",
  "webViewLink": "https://drive.google.com/drive/folders/1AGppe7PfAY02bOHYn6m1h1RjoUZ2h3ON"
}
来源：[https://arxiv.org/abs/2510.16165](https://arxiv.org/abs/2510.16165)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY",
    "webViewLink": "https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit"
  }
]
来源：[https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit](https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "11zXVL6xA5D2JNgNvaptGg3rlfXdkUOo0",
  "webViewLink": "https://drive.google.com/file/d/11zXVL6xA5D2JNgNvaptGg3rlfXdkUOo0/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2510.16165（采集 2026-11-07）
