# BAISBench

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
BAISBench
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 全称
BAISBench: Benchmarking AI scientists for omics data–driven biological discovery
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v2；最近论文日期 2026-01-18
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 发布日期
2025-05-13（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 板块
生物与医学
来源：[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "组学数据驱动科学发现Agent"
]
来源：[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）

### 许可证
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文
https://arxiv.org/abs/2505.08341
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 代码仓库
https://github.com/EperLuo/BAISBench
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 数据集
https://huggingface.co/datasets/EperLuo/BaisBench
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 官方主页
https://github.com/EperLuo/BAISBench
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 论文题名
Benchmarking AI scientists for omics data driven biological discovery
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
Tsinghua、Beijing Jiaotong、Capital Medical等论文署名团队；正式牵头协议待核实。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Luo, Erpai",
  "Jia, Jinmeng",
  "Xiong, Yifan",
  "Li, Xiangyu",
  "Guo, Xiaobo",
  "Yu, Baoqi",
  "Hao, Minsheng",
  "Wei, Lei",
  "Zhang, Xuegong"
]
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 维护方
EperLuo/BAISBench与EperLuo/BaisBench数据账号。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
从单细胞组学数据到细胞注释与研究结论重现，评估AI scientist。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 弥补缺口
一般问答/代码生成无法确认代理能在真实组学数据上重现生物发现。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
公开单细胞研究与CellxGene h5ad；BAIS-SD来自41项研究的已发表结论。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 构建者背景
生物信息专家注释与研究生人类参考；六名生物信息研究生参与对比。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 审核流程
专家标注细胞类型层级；GPT-4o辅助从论文结论拟题，人工纠正和实验核查。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 质量控制
uHAF层级兼容评分与按题型评分；固定数据文件支持可复现分析。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 去污染
来源研究及结论公开，主要是rediscovery而非真正未知发现；需警惕靠论文记忆作答。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

## 5. 数据形式

### 规模
主文：BAIS-DPTA 15个专家注释单细胞数据集；BAIS-SD 193题/41研究。附录TableS1可见列数与15叙述存在核对问题，未自行改为14。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 任务类型
细胞类型注释、基于组学数据的单选/多选结论重现。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 模态
h5ad表达矩阵、细胞元数据、代码与文字/选择答案。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 语言
英语研究问题与生物标识符；数据驱动。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 难度
真实研究数据分析；已发表结论重现不同于原创发现。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 公开与隐藏划分
官方GitHub/HF公开数据；当前隐藏测试设计待核实。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

## 6. 评测方法

### 指标
DPTA专家uHAF层级分；SD按单选/多选正确性计分。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 评分方式
细胞层级：准确1、父类0.5、祖父类0.2；SD单选正确1，多选全对1、部分对且无错0.5。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 提示与运行配置
五个AI scientist系统对比，六名研究生参考；系统工具与模型配置需随分数保留。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 官方脚本
https://github.com/EperLuo/BAISBench
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 可比性警告
主文15数据集和附录列表需核对；paper CC BY-NC-ND不自动等于数据集许可；STELLA叙述领先不能补造图中数值。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.21074v1",
      "date": "2026-10-15",
      "note": "OmicsBench §2及参考文献引用 BAISBench（Luo等2026），讨论其数据环境中的生物分析评测。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "Benchmarking AI scientists for omics data driven biological discovery",
    "authors": [
      "Luo, Erpai",
      "Jia, Jinmeng",
      "Xiong, Yifan",
      "Li, Xiangyu",
      "Guo, Xiaobo",
      "Yu, Baoqi",
      "Hao, Minsheng",
      "Wei, Lei",
      "Zhang, Xuegong"
    ],
    "release": "2025-05-13",
    "latest": "2026-01-18",
    "version": "v2"
  }
}
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）；[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）

### 饱和情况
缺乏本轮可核对的完整数值榜，饱和度待核实。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 污染与争议
已发表结论和GPT-4o拟题带来记忆/生成偏差；附录数据集计数需维护者核对。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 官方榜/结果入口
https://github.com/EperLuo/BAISBench
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
原论文v2（2026-01）比较五系统，叙述STELLA较强；本轮未从可核对表格获得准确图值，数字成绩待核实，不估算图中柱高。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
[
  "zhangxg@tsinghua.edu.cn"
]
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### Issues
https://github.com/EperLuo/BAISBench/issues
来源：[https://github.com/EperLuo/BAISBench](https://github.com/EperLuo/BAISBench)（采集 2026-11-07）

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2505.08341
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 原始PDF SHA256
72b6410e415b16c9de82f8bab63ba68978a3ecc735231b2b20ddaa5f7378ebc8
来源：[https://arxiv.org/pdf/2505.08341](https://arxiv.org/pdf/2505.08341)（采集 2026-11-07）

### 原始PDF字节数
2666576
来源：[https://arxiv.org/pdf/2505.08341](https://arxiv.org/pdf/2505.08341)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1UnT52NfQw39t6FVzCs21Y3-XVIzVzNJC",
  "webViewLink": "https://drive.google.com/drive/folders/1UnT52NfQw39t6FVzCs21Y3-XVIzVzNJC"
}
来源：[https://arxiv.org/abs/2505.08341](https://arxiv.org/abs/2505.08341)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg",
    "webViewLink": "https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit"
  }
]
来源：[https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit](https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "1LLtrgHSJRkbgGS7FUtvJBdDl3mdbYPlo",
  "webViewLink": "https://drive.google.com/file/d/1LLtrgHSJRkbgGS7FUtvJBdDl3mdbYPlo/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2505.08341（采集 2026-11-07）
