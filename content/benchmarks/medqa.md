# MedQA

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
MedQA
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 全称
MedQA
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v1；最近论文日期 2020-09-28
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 发布日期
2020-09-28（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 板块
生物与医学
来源：[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "医学执照考试式临床推理"
]
来源：[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2009.13081
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 代码仓库
https://github.com/jind11/MedQA
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 数据集
https://github.com/jind11/MedQA
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 官方主页
https://github.com/jind11/MedQA
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 论文题名
What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
MIT CSAIL与华中科技大学同济医学院署名作者；正式机构发起协议待核实。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Jin, Di",
  "Pan, Eileen",
  "Oufattole, Nassim",
  "Weng, Wei-Hung",
  "Fang, Hanyi",
  "Szolovits, Peter"
]
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 维护方
jind11/MedQA官方仓库。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
医学执照考试式多项选择，结合临床知识、病例推理与外部证据检索。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 弥补缺口
给定短文抽取答案的阅读理解难以代表需检索多个医学来源的开放域问答。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
美国、中国大陆、台湾医学资格考试题及相关医学教科书/文档语料。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 构建者背景
医学与计算机研究者合作；原考试命题专家逐题身份待核实。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 审核流程
从考试资料收集整理并进行选项/格式处理；独立医学双审人数待核实。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 质量控制
多语言数据与固定划分，论文分析检索噪声和多证据推理失败。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 去污染
公开考试及GitHub测试集存在训练暴露风险；2020原始划分不能证明2026模型无污染。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

## 5. 数据形式

### 规模
英语12,723、简体中文34,251、繁体中文14,123题；三语合计61,097（由原论文分项相加）。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 任务类型
病例或医学知识的多项选择；原版与US/大陆4选项处理版须分开。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）；[https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)（采集 2026-11-07）

### 模态
文本题干、选项、标准答案及可检索医学资料。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 语言
[
  "英语",
  "简体中文",
  "繁体中文"
]
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 难度
专业医学考试；不等同真实临床工作流或安全性验证。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 公开与隐藏划分
官方仓库提供train/dev/test；US、China及Taiwan分别划分；当前4选项版本与原选项版本不可混用。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（采集 2026-11-07）；[https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)（采集 2026-11-07）

## 6. 评测方法

### 指标
Accuracy：选择答案匹配标准答案。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 评分方式
原论文结合检索器与阅读器，也可闭卷选择；检索/开卷与闭卷分开。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 提示与运行配置
原论文非统一现代LLM提示；后续模型需注明4/5选项、CoT、shot、检索和测试子集。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 官方脚本
https://github.com/jind11/MedQA
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 可比性警告
三语、选项数量、工具与子集必须一致；医学考试高分不代表临床有效或安全。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.19029v1",
      "date": "2026-08-19",
      "note": "Adaptive Memory and Reflection Multi-Agent System 实际在 MedQA 上评测医学问答。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams",
    "authors": [
      "Jin, Di",
      "Pan, Eileen",
      "Oufattole, Nassim",
      "Weng, Wei-Hung",
      "Fang, Hanyi",
      "Szolovits, Peter"
    ],
    "release": "2020-09-28",
    "latest": "2020-09-28",
    "version": "v1"
  }
}
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（采集 2026-11-07）

### 饱和情况
后续论文高分不能据此认定所有版本饱和；本轮未核实同一协议下的当前全量头部榜单。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 污染与争议
2026 AMR论文方法叙述含逐题反馈，但实验称冻结检索且不写回测试反馈；需结合代码核实，不把该分数当统一榜单。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）；[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 官方榜/结果入口
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
H2使用证据/历史结果：2026-08 AMR(GPT-4o，API快照未给)报告MedQA93.2%；论文称使用官方test、训练集检索。但模型快照、完整评测样本清单待核实；非实时SOTA。
来源：[https://arxiv.org/html/2608.19029v1](https://arxiv.org/html/2608.19029v1)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "jindi15@mit.edu",
  "eileenp@mit.edu",
  "nassim@mit.edu",
  "ckbjimmy@mit.edu",
  "psz@mit.edu",
  "fanghanyi@hust.edu.cn"
]
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### Issues
https://github.com/jind11/MedQA/issues
来源：[https://github.com/jind11/MedQA](https://github.com/jind11/MedQA)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2009.13081
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 原始PDF SHA256
5e19522f21c0ab5c24cc0dacd3feaa5d4b7057391520075f2e521a271d062ee6
来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（采集 2026-11-07）

### 原始PDF字节数
189006
来源：[https://arxiv.org/pdf/2009.13081](https://arxiv.org/pdf/2009.13081)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1AYwJpnQXewH8Hk2KHLsemGjydd3Fvco0",
  "webViewLink": "https://drive.google.com/drive/folders/1AYwJpnQXewH8Hk2KHLsemGjydd3Fvco0"
}
来源：[https://arxiv.org/abs/2009.13081](https://arxiv.org/abs/2009.13081)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE",
    "webViewLink": "https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit"
  }
]
来源：[https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit](https://docs.google.com/document/d/1wgYP6J_7FZI1T2zTSeH_8rtDz7Rfyhei-uAksX9iNaE/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "1zmvFZ0lC8HCOh62LXlOrjcHf25kzF4gZ",
  "webViewLink": "https://drive.google.com/file/d/1zmvFZ0lC8HCOh62LXlOrjcHf25kzF4gZ/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2009.13081（采集 2026-11-07）
