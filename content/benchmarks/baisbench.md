# BAISBench

> 核查日期：2026-11-07（Asia/Seoul）。事实按字段附来源；论文实验不代表当前排名，待核实不等于未公开。

## 1. 基本信息

### 简称

BAISBench

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 全称

BAISBench: Benchmarking AI scientists for omics data–driven biological discovery

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 数据版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 论文版本

v2；最近论文日期 2026-01-18

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 发布日期

2025-05-13（首个arXiv版本日期；非推定数据上线日）

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 板块

生物与医学

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 子领域

组学数据驱动科学发现Agent

来源：[1](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 许可证

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 论文

https://arxiv.org/abs/2505.08341

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 代码入口

https://github.com/EperLuo/BAISBench

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 数据入口

https://huggingface.co/datasets/EperLuo/BaisBench

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 官方主页

https://github.com/EperLuo/BAISBench

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 论文标题

Benchmarking AI scientists for omics data driven biological discovery

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 2. 发起与维护

### 发起团队

Tsinghua、Beijing Jiaotong、Capital Medical等论文署名团队；正式牵头协议待核实。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 合作与署名机构

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 作者

Luo, Erpai；Jia, Jinmeng；Xiong, Yifan；Li, Xiangyu；Guo, Xiaobo；Yu, Baoqi；Hao, Minsheng；Wei, Lei；Zhang, Xuegong

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 维护方

EperLuo/BAISBench与EperLuo/BaisBench数据账号。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 资助

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 3. 设计目标

### 评测能力

从单细胞组学数据到细胞注释与研究结论重现，评估AI scientist。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 设计动机

一般问答/代码生成无法确认代理能在真实组学数据上重现生物发现。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 4. 构建方式

### 材料来源

公开单细胞研究与CellxGene h5ad；BAIS-SD来自41项研究的已发表结论。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 编制背景

生物信息专家注释与研究生人类参考；六名生物信息研究生参与对比。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 审核流程

专家标注细胞类型层级；GPT-4o辅助从论文结论拟题，人工纠正和实验核查。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 质量控制

uHAF层级兼容评分与按题型评分；固定数据文件支持可复现分析。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 去污染

来源研究及结论公开，主要是rediscovery而非真正未知发现；需警惕靠论文记忆作答。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 5. 数据形式

### 规模

主文：BAIS-DPTA 15个专家注释单细胞数据集；BAIS-SD 193题/41研究。附录TableS1可见列数与15叙述存在核对问题，未自行改为14。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 题型

细胞类型注释、基于组学数据的单选/多选结论重现。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 模态与格式

h5ad表达矩阵、细胞元数据、代码与文字/选择答案。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 语言

英语研究问题与生物标识符；数据驱动。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 难度

真实研究数据分析；已发表结论重现不同于原创发现。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 公开与隐藏划分

Task1/Task2 notebook及HF容器提供数据；Task2 README明确包含reference answer。隐藏测试设计仍待核实，不能称全部答案隐藏。

来源：[1](https://raw.githubusercontent.com/EperLuo/BAISBench/main/README.md)（访问 2026-11-07）

## 6. 评测方法

### 指标

DPTA专家uHAF层级分；SD按单选/多选正确性计分。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 评分流程

细胞层级：准确1、父类0.5、祖父类0.2；SD单选正确1，多选全对1、部分对且无错0.5。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 提示设置

五个AI scientist系统对比，六名研究生参考；系统工具与模型配置需随分数保留。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 评测入口

Task1.ipynb下载并评测数据处理/细胞注释；Task2.ipynb提供研究背景、选择题及参考答案，论文提示可按被测AI scientist调整。

来源：[1](https://raw.githubusercontent.com/EperLuo/BAISBench/main/README.md)（访问 2026-11-07）

### 可比性边界

主文15数据集和附录列表需核对；paper CC BY-NC-ND不自动等于数据集许可；STELLA叙述领先不能补造图中数值。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 7. 最新情况

### 核查日期

2026-11-07 Asia/Seoul

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 已核实版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 版本历史及后续引用

2026_H2_evidence：url：https://arxiv.org/html/2610.21074v1；date：2026-10-15；note：OmicsBench §2及参考文献引用 BAISBench（Luo等2026），讨论其数据环境中的生物分析评测。；evidence_boundary：引用不等于重新运行；本页将论文历史实验与现榜分开。；paper_metadata：title：Benchmarking AI scientists for omics data driven biological discovery；authors：Luo, Erpai；Jia, Jinmeng；Xiong, Yifan；Li, Xiangyu；Guo, Xiaobo；Yu, Baoqi；Hao, Minsheng；Wei, Lei；Zhang, Xuegong；release：2025-05-13；latest：2026-01-18；version：v2

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）；[2](https://arxiv.org/html/2610.21074v1)（访问 2026-11-07）

### 饱和情况

缺乏本轮可核对的完整数值榜，饱和度待核实。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 已知问题

官方README称AISBench，HF卡称Biological AI Scientist Benchmark（BAISBench），本库保留BAISBench slug并注明命名差异。HF显示56行元数据，不是56道题；科学发现任务为193题、来自41项研究。

来源：[1](https://raw.githubusercontent.com/EperLuo/BAISBench/main/README.md)（访问 2026-11-07）

### 衍生版本

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 8. 榜单快照

### 采集日期

2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 官方榜单入口

https://github.com/EperLuo/BAISBench

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 第三方榜单

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 结果快照

原论文v2（2026-01）比较五系统，叙述STELLA较强；本轮未从可核对表格获得准确图值，数字成绩待核实，不估算图中柱高。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 覆盖边界

本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）；[2](https://artificialanalysis.ai/)（访问 2026-11-07）；[3](https://epoch.ai/)（访问 2026-11-07）；[4](https://lmarena.ai/)（访问 2026-11-07）

## 9. 联系方式

### 公开邮箱

zhangxg@tsinghua.edu.cn

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 问题反馈

https://github.com/EperLuo/BAISBench/issues

来源：[1](https://github.com/EperLuo/BAISBench)（访问 2026-11-07）

### 官方账号

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 隐私政策

待核实

说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2505.08341

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### PDF SHA-256

72b6410e415b16c9de82f8bab63ba68978a3ecc735231b2b20ddaa5f7378ebc8

来源：[1](https://arxiv.org/pdf/2505.08341)（访问 2026-11-07）

### PDF字节数

2666576

来源：[1](https://arxiv.org/pdf/2505.08341)（访问 2026-11-07）

### Drive文件夹

id：1UnT52NfQw39t6FVzCs21Y3-XVIzVzNJC；webViewLink：https://drive.google.com/drive/folders/1UnT52NfQw39t6FVzCs21Y3-XVIzVzNJC

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

### 其他文档

type：中文介绍 Google Doc；id：1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg；webViewLink：https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit

来源：[1](https://docs.google.com/document/d/1gHMfyiYw-QqyYpR4fnFgYsUYLdK9QG0TH8QengjG2xg/edit)（访问 2026-11-07）

### Drive PDF

id：1LLtrgHSJRkbgGS7FUtvJBdDl3mdbYPlo；webViewLink：https://drive.google.com/file/d/1LLtrgHSJRkbgGS7FUtvJBdDl3mdbYPlo/view

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）

## 11. 变更记录

### 本页修订

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。

来源：[1](https://arxiv.org/abs/2505.08341)（访问 2026-11-07）
