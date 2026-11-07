# CHIPS-FF

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
CHIPS-FF
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 全称
Computational High-Performance Infrastructure for Predictive Simulation-based Force Fields
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v4；最近论文日期 2025-03-19
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 发布日期
2024-12-13（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 板块
材料
来源：[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "力场与材料物性"
]
来源：[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2412.10516
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 代码仓库
https://github.com/usnistgov/chipsff
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 数据集
https://github.com/usnistgov/chipsff
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 官方主页
https://pages.nist.gov/jarvis_leaderboard/Special/CHIPS_FF/
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 论文题名
CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
NIST Material Measurement Laboratory。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Wines, Daniel",
  "Choudhary, Kamal"
]
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 维护方
usnistgov/chipsff，Daniel Wines、Kamal Choudhary。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
通用ML力场的结构弛豫、弹性、声子、缺陷、表面、界面与非晶物性及计算开销。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 弥补缺口
仅看能量/力测试误差不足以说明真实半导体材料的下游物性可靠性。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
JARVIS-DFT参考与半导体部件相关材料，ASE+JARVIS-Tools自动化仿真。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 构建者背景
NIST材料计算与机器学习研究者。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 审核流程
固定参考DFT属性与自动收敛/弛豫工作流比较；独立人工逐结构审核规模待核实。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 质量控制
比较模型收敛、DFT偏差与成本，多种物性独立评分。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 去污染
uMLFF可能在重叠材料上训练；需要模型训练集与测试结构重叠审计，不能默认OOD。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

## 5. 数据形式

### 规模
原论文104材料、16个MLFF，另近200万结构力预测评测。H2工作流104晶格/弹性、49vacancy、82surface、15界面对；官网vacancy榜为48，协议不同。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）；[https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（采集 2026-11-07）

### 任务类型
材料物性数值回归与仿真工作流；非LLM问答。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 模态
原子结构、能量/力、弹性张量、声子与缺陷/表面数值。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 语言
数值与Python/ASE；无自然语言考试语言。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 难度
不同属性及材料族有独立难度；无统一总分。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 公开与隐藏划分
公开JARVIS参考与提交预测；每个物性榜的分母可不同，非统一train/test问答集。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

## 6. 评测方法

### 指标
属性级MAE及相关指标，收敛率/时间；官网总页称PCC，但vacancy子页实际定义MAE。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（采集 2026-11-07）

### 评分方式
使用同一物性工作流与DFT参考差值；不能把网站泛称ACC当分类准确率。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 提示与运行配置
非提示评测；须固定MLFF checkpoint、ASE弛豫器、阈值、参考晶胞与失败处理。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 官方脚本
https://github.com/usnistgov/chipsff
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 可比性警告
官网vacancy48点与H2的49点不同；H2界面参考晶胞不匹配改用split-slab protocol；不同参考流程不可直接比SOTA。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2609.19487v1",
      "date": "2026-09-16",
      "note": "ALIGNN 2.0 §2.3.3、表5实际在 CHIPS-FF 上评测缺陷、表面、界面及相关材料物性。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "CHIPS-FF: Evaluating Universal Machine Learning Force Fields for Material Properties",
    "authors": [
      "Wines, Daniel",
      "Choudhary, Kamal"
    ],
    "release": "2024-12-13",
    "latest": "2025-03-19",
    "version": "v4"
  }
}
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 饱和情况
各物性收敛/缺陷误差差异大，无统一饱和结论。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 污染与争议
参考结构、界面基线和失败处理影响误差；总页PCC与子页MAE命名冲突，以具体子页及物性定义为准。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）；[https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 官方榜/结果入口
https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/
来源：[https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
官网48点vacancy MAE(eV)快照：eqV2_31M_omat_mp_salex0.357、eqV2_86M_omat_mp_salex0.3619、mace-mpa0.4122。页面提交日期原样3-11-2025，格式歧义未擅转日期。H2 Table5另协议：UMA-S0.464eV/surface0.122Jm^-2，不能与官网48点混排。
来源：[https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/](https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/)（采集 2026-11-07）；[https://arxiv.org/html/2609.19487v1](https://arxiv.org/html/2609.19487v1)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "daniel.wines@nist.gov",
  "kamal.choudhary@nist.gov"
]
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### Issues
https://github.com/usnistgov/chipsff/issues
来源：[https://github.com/usnistgov/chipsff](https://github.com/usnistgov/chipsff)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2412.10516
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 原始PDF SHA256
f92bd2357b20db020e1cb92584f8b8882427ee86133019d91b75ac14c4844102
来源：[https://arxiv.org/pdf/2412.10516](https://arxiv.org/pdf/2412.10516)（采集 2026-11-07）

### 原始PDF字节数
4721218
来源：[https://arxiv.org/pdf/2412.10516](https://arxiv.org/pdf/2412.10516)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1VwsQVL22mQmsezJ5BqVl6vjHB-pYsNFl",
  "webViewLink": "https://drive.google.com/drive/folders/1VwsQVL22mQmsezJ5BqVl6vjHB-pYsNFl"
}
来源：[https://arxiv.org/abs/2412.10516](https://arxiv.org/abs/2412.10516)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo",
    "webViewLink": "https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit"
  }
]
来源：[https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit](https://docs.google.com/document/d/19XnwB4Sk71Z7ROiTLJFdMb6DVMQUmZhfenSKYlNWxqo/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "1R6k7Ykwhzm_clyHspieXbcEpedlyMJPL",
  "webViewLink": "https://drive.google.com/file/d/1R6k7Ykwhzm_clyHspieXbcEpedlyMJPL/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2412.10516（采集 2026-11-07）
