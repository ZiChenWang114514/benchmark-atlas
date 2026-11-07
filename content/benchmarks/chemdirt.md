# ChemDIRT

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
ChemDIRT
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 全称
ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v1；最近论文日期 2026-08-21
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 发布日期
2026-08-21（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 板块
化学
来源：[https://arxiv.org/html/2608.21504v1](https://arxiv.org/html/2608.21504v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "指令、表示与任务鲁棒性"
]
来源：[https://arxiv.org/html/2608.21504v1](https://arxiv.org/html/2608.21504v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2608.21504
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 代码仓库
https://github.com/einae-nd/ChemDIRT
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 数据集
https://huggingface.co/datasets/Einae/ChemDIRT
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 官方主页
https://github.com/einae-nd/ChemDIRT
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 论文题名
ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
University of Notre Dame作者团队。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Inae, Eric",
  "Gunn, Tim",
  "Bond, Chris",
  "Jiang, Meng"
]
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 维护方
einae-nd/ChemDIRT及Einae数据发布账号。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
对同一化学任务的指令改写与分子表示变化保持可靠；跨八类任务诊断鲁棒性。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 弥补缺口
单一提示/表示的成绩容易高估稳定能力，任务平均值掩盖表示及提示敏感性。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
QM9、ZINC、ChEMBL、PubChem分子及MoleculeNet/ChemLLMBench等已有任务；RDKit构建可计算真值。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 构建者背景
Eric Inae、Tim Gunn、Chris Bond、Meng Jiang，Notre Dame。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 审核流程
GPT-5Pro生成十种提示模板并人工核查，实际评测取前四种；清洗继承数据。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 质量控制
以固定化学真值比较指令与表示，使用任务特定有效性检查和RDKit；保留来源差异。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 去污染
有继承公开任务与分子库，不能将提示改写视为已去预训练污染；独立模型训练语料审计待核实。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

## 5. 数据形式

### 规模
4,484例、33个任务—表示设置、八类任务，论文评测23个模型。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 任务类型
描述、分类、设计、分析、回归、计算、机理、关系任务。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 模态
SMILES、IUPAC名称、分子图像、英语指令与数值/结构答案。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 语言
英语自然语言；SMILES/IUPAC化学表示。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 难度
指令与表示扰动是主要难度轴；没有统一难度级别。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 公开与隐藏划分
官方HF公开数据；不是统一训练/验证/隐藏测试竞赛协议。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

## 6. 评测方法

### 指标
分类准确率/精确匹配、结构EM、MACCS/Morgan/RDK相似度、ROUGE、RMSE/MAE；指标随任务变化。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 评分方式
结构先解析再比对；数值任务计算误差；报告四提示下平均和标准差，不混为置信区间。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 提示与运行配置
共同system、zero-shot；直接回答128token，推理256token上限；部分设置交叉SMILES/IUPAC及四模板。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 官方脚本
https://github.com/einae-nd/ChemDIRT
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 可比性警告
不同任务指标无通用总分；图像转结构、逆合成与回归成绩不能同排。模型标签与API具体快照需区分。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.21504v1",
      "date": "2026-08-21",
      "note": "ChemDIRT 原始论文在H2提出并实际评测多指令、多分子表示及八类化学任务的鲁棒性。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "ChemDIRT: A Diversified Instruction, Representation, and Task Benchmark for Robust Chemistry-LLM Evaluation",
    "authors": [
      "Inae, Eric",
      "Gunn, Tim",
      "Bond, Chris",
      "Jiang, Meng"
    ],
    "release": "2026-08-21",
    "latest": "2026-08-21",
    "version": "v1"
  }
}
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）；[https://arxiv.org/html/2608.21504v1](https://arxiv.org/html/2608.21504v1)（采集 2026-11-07）

### 饱和情况
无有效统一饱和数；Llama3在ClinTox不同提示可从0.095到0.905，说明稳定性问题。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 污染与争议
继承数据集可能已被训练使用；提示标准差不是数据集采样置信区间。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 官方榜/结果入口
https://github.com/einae-nd/ChemDIRT
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
2026-08原论文历史：Claude-Sonnet-5图像→SMILES EM0.633±0.028、图像→IUPAC0.687±0.039（Table V）；RetroDFM-R的SMILES逆合成EM0.685±0.023（Table IV）。±为提示间标准差，模型标签照论文，不代表同一任务冠军。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "einae@nd.edu",
  "tgunn2@nd.edu",
  "cbond@nd.edu",
  "mjiang2@nd.edu"
]
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### Issues
https://github.com/einae-nd/ChemDIRT/issues
来源：[https://github.com/einae-nd/ChemDIRT](https://github.com/einae-nd/ChemDIRT)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2608.21504
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 原始PDF SHA256
70a4ee8128ed69e69bb9a7394b1a823571e1738592986f7fc345603826a12524
来源：[https://arxiv.org/pdf/2608.21504](https://arxiv.org/pdf/2608.21504)（采集 2026-11-07）

### 原始PDF字节数
466313
来源：[https://arxiv.org/pdf/2608.21504](https://arxiv.org/pdf/2608.21504)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1Z1arqpVyZtzUnhGEUznM1Oh02lQKFmh5",
  "webViewLink": "https://drive.google.com/drive/folders/1Z1arqpVyZtzUnhGEUznM1Oh02lQKFmh5"
}
来源：[https://arxiv.org/abs/2608.21504](https://arxiv.org/abs/2608.21504)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58",
    "webViewLink": "https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit"
  }
]
来源：[https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit](https://docs.google.com/document/d/1AhidDsbF1hMc58H_Jp9_0ud7B4hqmGJVdsEhhwuCS58/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "186sLc62vIHc-Ng9ZKqoGmn37H6CvHjjB",
  "webViewLink": "https://drive.google.com/file/d/186sLc62vIHc-Ng9ZKqoGmn37H6CvHjjB/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2608.21504（采集 2026-11-07）
