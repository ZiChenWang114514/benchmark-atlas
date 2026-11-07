# SciGym

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
SciGym
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 全称
SciGym systems-biology dry-lab benchmark
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v2；最近论文日期 2025-07-14
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 发布日期
2025-07-02（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 板块
生物与医学
来源：[https://arxiv.org/html/2609.19134v1](https://arxiv.org/html/2609.19134v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "系统生物学干实验室"
]
来源：[https://arxiv.org/html/2609.19134v1](https://arxiv.org/html/2609.19134v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2507.02083
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 代码仓库
https://github.com/h4duan/SciGym
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 数据集
https://huggingface.co/datasets/h4duan/scigym-sbml
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 官方主页
https://h4duan.github.io/scigym-benchmark/
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 论文题名
Measuring Scientific Capabilities of Language Models with a Systems Biology Dry Lab
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
Toronto、SickKids、Axiom、Mila与Vector等论文署名团队；不推断正式合作协议。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Duan, Haonan",
  "Lu, Stephen Zhewen",
  "Harrigan, Caitlin Fiona",
  "Desai, Nishkrit",
  "Lu, Jiarui",
  "Koziarski, Michał",
  "Cotta, Leonardo",
  "Maddison, Chris J."
]
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 维护方
h4duan/SciGym与项目页团队。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
交互实验设计：改变初始浓度、观察动力学，重建隐藏生化反应系统并验证模型。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 弥补缺口
静态问答不能测可证伪假设、主动实验与迭代科学建模。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
BioModels的1,096个人工策展模型过滤为350个可执行SBML系统。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 构建者背景
系统生物学、机器学习与分子建模研究者；源库为人工策展模型。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 审核流程
剔除无法执行、无反应/物种、含不支持规则/事件模型；以程序模拟检查。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 质量控制
去注释/元数据、匿名化ID、打乱元素、去反应引用；验证Tellurium仿真兼容。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 去污染
匿名化降低靠名称记忆的捷径；源BioModels公开，所以不宣称未进入模型预训练。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

## 5. 数据形式

### 规模
350系统；小系统137个（少于10反应），大系统213个（最多约400反应）。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 任务类型
多步交互实验、Python建模、隐藏反应网络与动力学重建。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 模态
数值浓度轨迹、SBML/XML、Python与英语交互。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 语言
英语任务/代理提示及Python/SBML。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 难度
按反应系统规模分small/large；强模型在反应结构恢复上仍有限。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 公开与隐藏划分
模型库公开下载；每次实验的真实内部反应系统对代理隐藏。公开数据不等于运行时可直接读gold。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

## 6. 评测方法

### 指标
NTS拓扑F1、RMS反应F1（区分是否包括modifier）、STE轨迹SMAPE（低为好）。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 评分方式
比对反应图及预测轨迹；系统行为相近不等于动力学表达式唯一正确。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 提示与运行配置
ReAct代理最多20迭代，另3次debug；Python/Tellurium模拟与浓度扰动。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 官方脚本
https://github.com/h4duan/SciGym
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 可比性警告
有无modifier、small/large与动力学误差方向必须保留；无噪声仿真不代表湿实验。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §4.1明确列举系统生物学 SciGym 并引用其原始论文 arXiv:2507.02083；为H2学术引用，不是本文实跑。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "Measuring Scientific Capabilities of Language Models with a Systems Biology Dry Lab",
    "authors": [
      "Duan, Haonan",
      "Lu, Stephen Zhewen",
      "Harrigan, Caitlin Fiona",
      "Desai, Nishkrit",
      "Lu, Jiarui",
      "Koziarski, Michał",
      "Cotta, Leonardo",
      "Maddison, Chris J."
    ],
    "release": "2025-07-02",
    "latest": "2025-07-14",
    "version": "v2"
  }
}
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）；[https://arxiv.org/html/2609.19134v1](https://arxiv.org/html/2609.19134v1)（采集 2026-11-07）

### 饱和情况
在隐藏系统恢复的历史低F1下不能称饱和；H2仅引用，未提供更新头部成绩。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 污染与争议
理想无噪声模拟及可识别性限制；重建相似轨迹不是唯一恢复真实反应机理。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 官方榜/结果入口
https://h4duan.github.io/scigym-benchmark/
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
2025论文Table1历史：Gemini-2.5-Pro-Preview-03-25 STE0.3212、RMS含modifier F1 0.1817；Claude-3.7-Sonnet-20250219 STE0.3615/F1 0.1688；GPT-4.1-2025-04-14 STE0.4611/F1 0.1740。不是2026重新运行。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### Issues
https://github.com/h4duan/SciGym/issues
来源：[https://github.com/h4duan/SciGym](https://github.com/h4duan/SciGym)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2507.02083
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 原始PDF SHA256
8f490e009f6448434412f43ec8c89cd97d6100ebfa001bf6b38d17f7433f86b1
来源：[https://arxiv.org/pdf/2507.02083](https://arxiv.org/pdf/2507.02083)（采集 2026-11-07）

### 原始PDF字节数
7093862
来源：[https://arxiv.org/pdf/2507.02083](https://arxiv.org/pdf/2507.02083)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1pMHOGBbhMwADTWVpcSndAPPvQYNqM5DP",
  "webViewLink": "https://drive.google.com/drive/folders/1pMHOGBbhMwADTWVpcSndAPPvQYNqM5DP"
}
来源：[https://arxiv.org/abs/2507.02083](https://arxiv.org/abs/2507.02083)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1e-0ecKgh4yUcUPBaUZz0z0IxxMN23URYbsAWLtC7TUk",
    "webViewLink": "https://docs.google.com/document/d/1e-0ecKgh4yUcUPBaUZz0z0IxxMN23URYbsAWLtC7TUk/edit"
  }
]
来源：[https://docs.google.com/document/d/1e-0ecKgh4yUcUPBaUZz0z0IxxMN23URYbsAWLtC7TUk/edit](https://docs.google.com/document/d/1e-0ecKgh4yUcUPBaUZz0z0IxxMN23URYbsAWLtC7TUk/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "16ZviC4sNbrI2MV3Z7ORtEc02fArVV7WT",
  "webViewLink": "https://drive.google.com/file/d/16ZviC4sNbrI2MV3Z7ORtEc02fArVV7WT/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2507.02083（采集 2026-11-07）
