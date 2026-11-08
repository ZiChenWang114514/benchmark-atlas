# Furniture Assembly Benchmark

> Benchmark Constitution｜深度核验：2026-11-07。访问日沿固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

模型需要把真实装配照片与PDF手册联系起来，定位错误产生的步骤并描述错误。它不是机器人实际装配任务；60张照片来自仅三种家具，推广到一般物理推理时应保持克制。

最近复核

## 基本信息

**简称**：Furniture Assembly Benchmark

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**全称**：Furniture Assembly Benchmark

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**基准版本**：运行CSV中见1.0.0与1.0.1；榜单限1.0.0分轨

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**论文版本**：官方网页研究报告（与持续更新的方法页分开记录）

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**发布日期**：2026-09-23（官方发布研究报告的datePublished；不据此断言所有任务资产首次上线日）

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）

**主板块**：多模态

核验说明：编辑主板块归档，不据此限制跨学科覆盖。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**领域标签**：空间推理

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**许可证与授权边界**：官方研究报告JSON-LD声明CC-BY-4.0；这不涵盖底层IKEA图片/说明书。官方明确不分发或售卖该受版权保护材料，题库统一再分发许可待核实。

状态：待核实。

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**论文或技术报告**：https://epoch.ai/publications/furniture-assembly

核验说明：官方网页研究报告；未定位独立arXiv论文或PDF。

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）

**官方代码**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**数据地址**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**官方主页**：https://epoch.ai/benchmarks/furniture-assembly

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**论文题名**：AI has improved significantly at reasoning about IKEA furniture assembly

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）

## 发起与维护

**发起方**：Epoch AI

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**协作与机构边界**：研究独立于IKEA，不据使用产品及说明书推断合作。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**作者**：Aiden Ament；Greg Burnham

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）

**维护方**：Epoch AI

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 设计目标

**测量能力**：将真实装配照片与技术图示连接，识别错误并定位产生错误的步骤。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**相对既有评测的缺口**：衡量物理构建的空间及多步推理，而非仅抽象视觉题。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 构建方式

**题目来源**：研究人员购买三件IKEA家具并拍摄装配过程，故意制造可见错误后可继续安装。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**出题与研究背景**：Epoch AI研究报告署名Aiden Ament与Greg Burnham；原任务由研究者实际购买和组装IKEA家具后拍摄，不是机器人执行数据。

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**审核流程**：有错样本先核对步骤，再由GPT-5.6 Sol宽松评阅错误描述。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**质量控制**：正确构建正确识别直接通过；有错样本必须正确定位并大致描述。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**去污染与泄漏边界**：官方不分发或出售底层受版权保护图片和说明书；不由此推断完整数据开放。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 数据形式

**规模与口径**：60张照片：Ställ鞋柜14、Tonstad床架25、Gullaberg斗柜21。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**任务类型**：判断安装正确性；识别错误步骤与原因；正确时指出下一步。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**模态**：照片；PDF装配手册；文本

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**语言**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**难度**：三产品按复杂度选择，错误可发生于较早而非最后一步。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**公开与隐藏划分**：官方明确不分发或出售底层受版权保护的照片及IKEA说明书。公开方法和结果并不等于公开底层题库；本条不按标准公开train/test拆分理解。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 评测方法

**指标**：60照片准确率，误差条为±标准误。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**评分方式**：错题先匹配步骤，再LLM判描述；人类基线仅判步骤，任务略容易。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**提示与运行设置**：提供产品名、当前完成步骤、照片、PDF手册、zoom与Python；80步budget；最高支持reasoning effort。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**官方复现入口**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**可比性警告**：不能把人类84%最佳组合称单人全卷成绩；运行CSV有不同任务版本，须分轨。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**数据及热度证据**：```json
{
  "version": "CSV最新运行见1.0.1"
  "evidence_2026_h2": [
    {
      "url": "https://epoch.ai/data/benchmarks.csv"
      "date": "2026-11-06"
      "note": "Kimi K3.1 Pro，运行2026-11-06 20:34:34，id UNKjzcpUBaxGsrr7zZZZWC；持续实跑证据。"
    }
  ]
}
```

来源：[1](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

**论文与版本历史**：官方网页研究报告2026-09-23发布；发布文写尚未测人类，而当前方法页新增2026年9月人类实验，因此两者按历史发布文/持续维护页分别引用。

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**饱和程度**：CSV中1.0.0最高0.833333（Claude Opus 5.5）；1.0.1最高0.791667（GPT-6.1 Terra）。不同版本分轨，60张照片/三产品不能支持泛化到全部空间推理已饱和。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

**已知问题与局限**：原发布文尚未测人类表现；现方法页已增加15名志愿者基线，平均63%、每产品最佳者组合84%，人类只需定位步骤而不用描述错误。优先现方法页，不能把组合84%当单人全卷分数。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）

**后续与衍生**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 榜单快照

**快照日期**：2026-11-07

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**官方入口**：https://epoch.ai/benchmarks/furniture-assembly

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**第三方入口**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 1.0.0 | 1 | Claude Opus 5.5 (max) | 0.8333333333333334 | mean_score (0–1) | 2026-09-23 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 2 | GPT-6.1 Sol (max) | 0.8 | mean_score (0–1) | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 3 | GPT-6 Astra (max) | 0.8 | mean_score (0–1) | 2026-09-11 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 4 | Claude Sonnet 5.5 (max) | 0.75 | mean_score (0–1) | 2026-09-30 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.0 | 5 | Claude Fable 5.1 (max) | 0.7 | mean_score (0–1) | 2026-09-11 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 1 | GPT-6.1 Terra (max) | 0.7916666666666666 | mean_score (0–1) | 2026-10-27 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 2 | Gemini 4 Argon (high) | 0.725 | mean_score (0–1) | 2026-10-14 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 3 | Kimi K3.1 Pro (Together, max) | 0.5583333333333333 | mean_score (0–1) | 2026-11-06 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 4 | Muse Wonder (max) | 0.5416666666666666 | mean_score (0–1) | 2026-10-16 | [原始来源](https://epoch.ai/data/benchmarks.csv) |
| 1.0.1 | 5 | Mistral Large 4 (high) | 0.3083333333333333 | mean_score (0–1) | 2026-11-02 | [原始来源](https://epoch.ai/data/benchmarks.csv) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：刷新成功运行记录，分别列1.0.0及1.0.1各前5；rank在各版本内重新开始，严禁将两版混合成总榜。运行开始日不是榜单更新时间。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/data/benchmarks.csv)（访问2026-11-07）

## 联系方式

**公开联系邮箱**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**Issues或讨论入口**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**官方社交**：https://x.com/EpochAIResearch

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**隐私政策**：https://epoch.ai/privacy

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 原始文件

**原始PDF**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**PDF SHA-256**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**PDF字节数**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**文件夹**：待核实

状态：待核实。

核验说明：打开所列材料后仍未精确核实；不代表官方没有公开。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**其他官方文档**：```json
[
  {
    "type": "发布研究报告"
    "url": "https://epoch.ai/publications/furniture-assembly"
  }
  {
    "type": "持续更新方法与人类基线"
    "url": "https://epoch.ai/benchmarks/furniture-assembly"
  }
]
```

来源：[1](https://epoch.ai/publications/furniture-assembly)（访问2026-11-07）；[2](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

**论文链接**：待核实

状态：待核实。

核验说明：本组仅本地研究，未上传。

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

## 变更记录

**及历史变更**：```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    最近复核
  }
]
```

来源：[1](https://epoch.ai/benchmarks/furniture-assembly)（访问2026-11-07）

