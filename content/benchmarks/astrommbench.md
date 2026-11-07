# AstroMMBench

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
AstroMMBench
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 全称
AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 数据版本
2026正式期刊版（592题）
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 论文版本
Universe 12(10),296，2026-09-30正式版
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 发布日期
2026-09-30（正式版发表；非推定最早数据上线日）
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 板块
地球与天文
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "天文研究图像多模态问答"
]
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 许可证
论文CC BY；源arXiv图的再分发依各原稿许可证，不能把论文许可套给全部图像。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 论文
https://www.mdpi.com/2218-1997/12/10/296
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 代码仓库
https://github.com/Shijinghang/benchmark_pipeline
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 数据集
https://huggingface.co/datasets/sjh11/AstroMMBench
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 官方主页
https://www.mdpi.com/2218-1997/12/10/296
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 论文题名
AstroMMBench: A Benchmark for Evaluating Multimodal Large Language Model Capabilities in Astronomy
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
中国科学院国家天文台等论文作者团队。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 合作方
中国科学院大学、浙江实验室、天津大学（作者机构）。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 作者
[
  "Jinghang Shi",
  "Xiaoyu Tang",
  "Yang Huang",
  "Yuyang Li",
  "Yanxia Zhang",
  "Xiao Kong",
  "Caizhan Yue",
  "A-Li Luo"
]
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 维护方
Shijinghang/benchmark_pipeline与sjh11/AstroMMBench官方发布账号。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 资助
NSFC 12273076/12203077/12373110/12133001；2025YFA1614101；CMS-CSST-2025-A06；河北A2024205020（正式版致谢）。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

## 3. 设计目标

### 评测能力
读懂天文研究图表、仪器图、观测图像并回答专业物理问题。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 弥补缺口
通用VQA不能覆盖天文图像约定与领域推理；与文本AstroLLM、跨模态表示学习互补。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
2024-01至07的3,592篇astro-ph论文，19,299图文对。LLaMA3.3-70B改写上下文，InternVL2.5-78B拟题。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 构建者背景
15名国家天文台审核者：8博士生、5硕士生、2教授；按研究专长分题。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 审核流程
五模型文本盲答筛去易靠语言先验解的题；余9,677中随机选1,800人工审查，保留592。每题一名主审，非独立双盲。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 质量控制
检查科学正确、图题一致、上下文充分、唯一答案与干扰项；有问题直接丢弃；无一致性系数测量。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 去污染
保留来源arXiv ID；没有训练集审计、近重复搜索或记忆探测。2024公开论文可能被后来模型训练，正式版明确不可称contamination-free。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

## 5. 数据形式

### 规模
592四选一题：GA97、CO108、EP97、HE101、IM83、SR106；25个MLLM（22开放、3闭源）。旧621题摘要不能与正式版混用。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 任务类型
图像+问题+四选项，单个正确答案。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 模态
天文科研图、图表与文本；不是原始FITS时序分析。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 语言
英语。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 难度
六子领域；宇宙学均分最低，高能领域模型间方差最大，不应一律称最难。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 公开与隐藏划分
HF公开固定592题；当前不是隐藏测试竞赛。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

## 6. 评测方法

### 指标
整体及六子领域accuracy，整体分母固定592；Wilson95%区间辅助解释。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 评分方式
A–D精确匹配；自由文本用DeepSeek-V3固定二元判分，失败/无效均记错不丢弃。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 提示与运行配置
VLMEvalKit0.2，图像后接问题四选项；不同模型adapter独立缩放/切片，闭源走官方API。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 官方脚本
https://github.com/Shijinghang/benchmark_pipeline
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 可比性警告
有效图像输入尺寸并未全局统一；头部区间重叠，点估计不能当显著排名；需成对检验及重复运行。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 最新数据版本
2026正式版592题；版本以此次正式论文口径为准。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://www.mdpi.com/2218-1997/12/10/296",
      "date": "2026-09-30",
      "note": "期刊正式版发表于2026-09-30，在592道专家筛选题上实际评价25个多模态模型。采用打开的正式版，未沿用搜索摘要的旧621题。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "note": "见期刊/数据库官方入口"
  }
}
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）；[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 饱和情况
历史最高71.28%，尚未饱和；头部模型之间小差距无显著性结论。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 污染与争议
无训练语料审计；每题单主审且见到答案/原caption；五模型过滤选择偏差。文本盲答对照仅覆盖两个模型。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 官方榜/结果入口
https://www.mdpi.com/2218-1997/12/10/296
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
正式版2026-09 Table2历史：Ovis2-34B71.28%（Wilson67.51–74.78）；ChatGPT-4o69.76%（65.95–73.33）；Doubao1.5-vision-pro69.09%（65.25–72.68）。共同592题；GPT4o具体API快照待核实；不代表后发模型未超越。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "tangxiaoyu@zhejianglab.org",
  "zyx@bao.ac.cn"
]
来源：[https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf](https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf)（采集 2026-11-07）

### Issues
https://github.com/Shijinghang/benchmark_pipeline/issues
来源：[https://github.com/Shijinghang/benchmark_pipeline](https://github.com/Shijinghang/benchmark_pipeline)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 原始PDF SHA256
5098322dcf0f8cbccdc5682a22fa6a4565c73464ef54937174540916f5f05a0c
来源：[https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf](https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf)（采集 2026-11-07）

### 原始PDF字节数
7134595
来源：[https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf](https://mdpi-res.com/d_attachment/universe/universe-12-00296/article_deploy/universe-12-00296.pdf)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1TSOgqfwkB-dttJyEkuJMzgZJidF3HFdh",
  "webViewLink": "https://drive.google.com/drive/folders/1TSOgqfwkB-dttJyEkuJMzgZJidF3HFdh"
}
来源：[https://www.mdpi.com/2218-1997/12/10/296](https://www.mdpi.com/2218-1997/12/10/296)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4",
    "webViewLink": "https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit"
  }
]
来源：[https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit](https://docs.google.com/document/d/1nJ6uf32vtz8ukEZRmxJ5NK6uDrAyBIKeaFW3PYkQ-Q4/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "1U3D15tfPy2AbJbYlOx0vxQP2neBx4yZO",
  "webViewLink": "https://drive.google.com/file/d/1U3D15tfPy2AbJbYlOx0vxQP2neBx4yZO/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://www.mdpi.com/2218-1997/12/10/296（采集 2026-11-07）
