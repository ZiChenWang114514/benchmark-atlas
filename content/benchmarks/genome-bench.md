# Genome-Bench

> Benchmark Constitution｜深度核验：2026-11-07（KST / Asia/Seoul）。访问日沿本轮固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

Genome-Bench是Princeton/Stanford研究者把长期CRISPR专家讨论转成的文本问答集，与OpenAI的GeneBench/Pro完全不同。论文路由系统成绩来自多个RL专家，不能当作单一小模型的独立成绩。

编辑状态：已核验存在；研究快照；缺失字段显式待核实

## 基本信息

**简称**：Genome-Bench

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**全称**：Genome-Bench（RL4GenomeBench配套基因组学问答）

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**基准版本**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**论文版本**：v2；最近论文日期 2025-06-02

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**发布日期**：2025-05-26（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**主板块**：生物与医学

核验说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07）

**领域标签**：基因组学能力

来源：[1](https://arxiv.org/html/2610.21074v1)（访问2026-11-07）

**许可证与授权边界**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**论文或技术报告**：https://arxiv.org/abs/2505.19501

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**官方代码**：https://github.com/mingyin0312/RL4GenomeBench

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**数据地址**：https://huggingface.co/datasets/Mingyin0312/Genome-Bench

来源：[1](https://raw.githubusercontent.com/mingyin0312/RL4GenomeBench/main/README.md)（访问2026-11-07）

**官方主页**：https://github.com/mingyin0312/RL4GenomeBench

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**论文题名**：Toward Scientific Reasoning in LLMs: Training from Expert Discussions via Reinforcement Learning

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 发起与维护

**发起方**：Princeton与Stanford论文作者合作。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**协作与机构边界**：Princeton University与Stanford University作者联合署名；公开README提及使用TRL，不把依赖库组织认作合作单位。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）；[2](https://github.com/mingyin0312/RL4GenomeBench)（访问2026-11-07）

**作者**：Ming Yin；Yuanhao Qu；Ling Yang；Le Cong；Mengdi Wang

核验说明：按PDF扉页纠正旧作者解析的姓/名倒置和拼写。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**维护方**：mingyin0312/RL4GenomeBench官方仓库。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 设计目标

**测量能力**：基于专家讨论的CRISPR/基因组实验科学推理与问答；无工具MCQ。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**相对既有评测的缺口**：教材事实问答不足以反映专家社区的实验设计、故障诊断与经验知识。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 构建方式

**题目来源**：CRISPR相关专家讨论和论坛线程；官方dataset_pipeline可解析.mbox邮件档案并转换为标准MCQ及QA格式。

来源：[1](https://raw.githubusercontent.com/mingyin0312/RL4GenomeBench/main/README.md)（访问2026-11-07）

**出题与研究背景**：社区原问题来自实验/基因组学参与者；论文作者做QA提取与清洗。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**审核流程**：GPT-4Turbo抽取QA/context，GPT-4o改写和构建干扰项，人工检查。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**质量控制**：去重、去未解答/离题内容、随机选项顺序与人工质量检查。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**去污染与泄漏边界**：源讨论公开；划分问答不保证预训练无暴露或同主题讨论完全隔离。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 数据形式

**规模与口径**：3,332条问答，来自11年基因组编辑研究讨论；HF固定train 2,671、test 661，不能与GeneBench 103/129题混淆。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）；[2](https://huggingface.co/datasets/Mingyin0312/Genome-Bench/blob/main/README.md)（访问2026-11-07）

**任务类型**：英语五选一科学/实验推理；不是基因序列预测或执行型组学分析。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**模态**：纯文本问题、上下文、五个选项和答案。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**语言**：英语。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**难度**：专家讨论改编，原论文按七类任务口径；不补造统一难度标签。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**公开与隐藏划分**：公开train/test 2671/661，固定测试准确率。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 评测方法

**指标**：661题test accuracy。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**评分方式**：提取结构化最终答案标签并与标准选项比对。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**提示与运行设置**：论文比较base/CoT/RL-Router，必须保留相同提示与路由/多专家设置。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**官方复现入口**：evaluation/genome-bench_eval.py（官方README的测试集评测入口）。

来源：[1](https://raw.githubusercontent.com/mingyin0312/RL4GenomeBench/main/README.md)（访问2026-11-07）

**可比性警告**：RL-Router的四专家系统不同于单一7B模型；不是通用生物分析代理能力总榜。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07 KST / Asia/Seoul

来源：[1](https://github.com/mingyin0312/RL4GenomeBench)（访问2026-11-07）

**数据及热度证据**：公开default配置train/test快照（2671/661）；官方HF卡未标语义版本号，复现应固定revision。

来源：[1](https://huggingface.co/datasets/Mingyin0312/Genome-Bench/blob/main/README.md)（访问2026-11-07）

**论文与版本历史**：```json
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
```

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）；[2](https://arxiv.org/html/2610.21074v1)（访问2026-11-07）

**饱和程度**：历史最好81.07%，非2026当前上限；未核实更新实时榜。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**已知问题与局限**：源讨论和题库公开，答案改写不消除语义记忆；661题样本规模需考虑误差。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**后续与衍生**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 榜单快照

**快照日期**：2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**官方入口**：https://github.com/mingyin0312/RL4GenomeBench

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**第三方入口**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| arXiv v2 Table 2历史实验 | 1 | RL-Router (Qwen2.5-7B + four RL experts) | 81.07 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2历史实验 | 2 | DeepSeek-R1 01-20-25 | 78.97 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2历史实验 | 3 | Gemini-2.5-Pro exp-03-25 | 77.46 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2历史实验 | 4 | Qwen2.5-7B RL-tuned | 76.85 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |
| arXiv v2 Table 2历史实验 | 5 | Claude-3.7-Sonnet 02-19-25 | 76.4 | Genome-Bench test accuracy (%) | 2025-06-02 | [原始来源](https://arxiv.org/abs/2505.19501v2) |

采集：2026-11-07（KST / Asia/Seoul）；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：重新读v2 PDF Table 1/2核验版本与分数，将原字符串改结构化结果。RL-Router为四专家路由系统，不能当单一7B模型；官方README未提供更新的统一实时榜，不宣称2026 SOTA。

来源：[1](https://arxiv.org/abs/2505.19501v2)（访问2026-11-07）；[2](https://github.com/mingyin0312/RL4GenomeBench)（访问2026-11-07）

## 联系方式

**公开联系邮箱**：my0049@princeton.edu；yhqu@stanford.edu

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**Issues或讨论入口**：https://github.com/mingyin0312/RL4GenomeBench/issues

来源：[1](https://github.com/mingyin0312/RL4GenomeBench)（访问2026-11-07）

**官方社交**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**隐私政策**：待核实

状态：待核实。

核验说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 原始文件

**原始PDF**：https://arxiv.org/pdf/2505.19501

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**PDF SHA-256**：ea37fbd1578b8906f5d975c28a63898f9139e3fcd4177bacc5d99f67dec2d9b3

核验说明：本轮下载原始PDF字节计算，非arXiv网页显示大小。

来源：[1](https://arxiv.org/pdf/2505.19501)（访问2026-11-07）

**PDF字节数**：```json
24536967
```

核验说明：本轮实际下载字节数；不代表Drive已上传。

来源：[1](https://arxiv.org/pdf/2505.19501)（访问2026-11-07）

**Drive文件夹**：```json
{
  "id": "1Ujb8zb_jipEtvQBq_eUglTPU4MJXlI04",
  "webViewLink": "https://drive.google.com/drive/folders/1Ujb8zb_jipEtvQBq_eUglTPU4MJXlI04"
}
```

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

**其他官方文档**：```json
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8",
    "webViewLink": "https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit"
  }
]
```

来源：[1](https://docs.google.com/document/d/1enUvw7XP8aREmtFrobp5qfWIRIY0cHRYwBlV_fJPmE8/edit)（访问2026-11-07）

**Drive论文链接**：```json
{
  "id": "1zvsJcz5mzrqjItFIVfStqXqZHd-Kt_0r",
  "webViewLink": "https://drive.google.com/file/d/1zvsJcz5mzrqjItFIVfStqXqZHd-Kt_0r/view"
}
```

来源：[1](https://arxiv.org/abs/2505.19501)（访问2026-11-07）

## 变更记录

**本轮及历史变更**：```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "第1轮深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。"
  },
  {
    "date": "2026-11-07",
    "change": "Round 2逐项深核：重读官方论文PDF/网页、仓库与可访问数据卡，修正版本、授权与方法边界，刷新分轨结构化成绩；无证据字段保留待核实。"
  }
]
```

来源：[1](https://github.com/mingyin0312/RL4GenomeBench)（访问2026-11-07）

