# Genome-Bench

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
Genome-Bench
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 全称
Genome-Bench（RL4GenomeBench配套基因组学问答）
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v2；最近论文日期 2025-06-02
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 发布日期
2025-05-26（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 板块
生物与医学
来源：[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "基因组学能力"
]
来源：[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2505.19501
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 代码仓库
https://github.com/mingyin0312/RL4GenomeBench
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 数据集
https://github.com/mingyin0312/RL4GenomeBench
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 官方主页
https://github.com/mingyin0312/RL4GenomeBench
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 论文题名
Toward Scientific Reasoning in LLMs: Training from Expert Discussions via Reinforcement Learning
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
Princeton与Stanford论文作者合作。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Yin, Ming",
  "Qu, Yuanhao",
  "Yang, Ling",
  "Cong, Le",
  "Wang, Mengdi"
]
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 维护方
mingyin0312/RL4GenomeBench官方仓库。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
基于专家讨论的CRISPR/基因组实验科学推理与问答；无工具MCQ。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 弥补缺口
教材事实问答不足以反映专家社区的实验设计、故障诊断与经验知识。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
2013—2023公开CRISPR Google讨论组约4,000个线程。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 构建者背景
社区原问题来自实验/基因组学参与者；论文作者做QA提取与清洗。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 审核流程
GPT-4Turbo抽取QA/context，GPT-4o改写和构建干扰项，人工检查。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 质量控制
去重、去未解答/离题内容、随机选项顺序与人工质量检查。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 去污染
源讨论公开；划分问答不保证预训练无暴露或同主题讨论完全隔离。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

## 5. 数据形式

### 规模
3,332道五选一题：2,671 train、661 test。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 任务类型
英语五选一科学/实验推理；不是基因序列预测或执行型组学分析。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 模态
纯文本问题、上下文、五个选项和答案。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 语言
英语。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 难度
专家讨论改编，原论文按七类任务口径；不补造统一难度标签。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 公开与隐藏划分
公开train/test 2671/661，固定测试准确率。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

## 6. 评测方法

### 指标
661题test accuracy。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 评分方式
提取结构化最终答案标签并与标准选项比对。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 提示与运行配置
论文比较base/CoT/RL-Router，必须保留相同提示与路由/多专家设置。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 官方脚本
https://github.com/mingyin0312/RL4GenomeBench
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 可比性警告
RL-Router的四专家系统不同于单一7B模型；不是通用生物分析代理能力总榜。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.21074v1",
      "date": "2026-10-15",
      "note": "OmicsBench §2明确列举 Genome-Bench（Yin等2025），作为生物学局部能力评测的先行基准；为H2学术引用。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "Toward Scientific Reasoning in LLMs: Training from Expert Discussions via Reinforcement Learning",
    "authors": [
      "Yin, Ming",
      "Qu, Yuanhao",
      "Yang, Ling",
      "Cong, Le",
      "Wang, Mengdi"
    ],
    "release": "2025-05-26",
    "latest": "2025-06-02",
    "version": "v2"
  }
}
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）；[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）

### 饱和情况
历史最好81.07%，非2026当前上限；未核实更新实时榜。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 污染与争议
源讨论和题库公开，答案改写不消除语义记忆；661题样本规模需考虑误差。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 官方榜/结果入口
https://github.com/mingyin0312/RL4GenomeBench
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
2025 v2论文历史：RL-Router（Qwen2.5-7B-Instruct路由+四RL专家）81.07%；DeepSeekR1(01-20-25)78.97%；Gemini2.5Pro(exp03-25)77.46%；Claude3.7Sonnet(02-19-25)76.40%。H2仅引用，无新实跑。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "my0049@princeton.edu",
  "yhqu@stanford.edu"
]
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### Issues
https://github.com/mingyin0312/RL4GenomeBench/issues
来源：[https://github.com/mingyin0312/RL4GenomeBench](https://github.com/mingyin0312/RL4GenomeBench)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2505.19501
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 原始PDF SHA256
ea37fbd1578b8906f5d975c28a63898f9139e3fcd4177bacc5d99f67dec2d9b3
来源：[https://arxiv.org/pdf/2505.19501](https://arxiv.org/pdf/2505.19501)（采集 2026-11-07）

### 原始PDF字节数
24536967
来源：[https://arxiv.org/pdf/2505.19501](https://arxiv.org/pdf/2505.19501)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1Ujb8zb_jipEtvQBq_eUglTPU4MJXlI04",
  "webViewLink": "https://drive.google.com/drive/folders/1Ujb8zb_jipEtvQBq_eUglTPU4MJXlI04"
}
来源：[https://arxiv.org/abs/2505.19501](https://arxiv.org/abs/2505.19501)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8",
    "webViewLink": "https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit"
  }
]
来源：[https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit](https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "1zvsJcz5mzrqjItFIVfStqXqZHd-Kt_0r",
  "webViewLink": "https://drive.google.com/file/d/1zvsJcz5mzrqjItFIVfStqXqZHd-Kt_0r/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2505.19501（采集 2026-11-07）
