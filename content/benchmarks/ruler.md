# RULER

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1jrXqZ9i4OPxWrgbz9D-xEwGusBAFeiiQ/view?usp=drivesdk)

## 基本信息

### 简称
RULER
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 全称
RULER
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 基准版本
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本
arXiv v3
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 发布日期
2024-04-09
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "长上下文利用"
]
```
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 许可证
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文
https://arxiv.org/abs/2404.06654
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 官方代码
https://github.com/hsiehjackson/RULER
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 数据地址
https://github.com/hsiehjackson/RULER
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 官方入口
https://github.com/hsiehjackson/RULER
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 论文标题
RULER: What's the Real Context Size of Your Long-Context Language Models?
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
NVIDIA 研究团队。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Hsieh, Cheng-Ping",
  "Sun, Simeng",
  "Kriman, Samuel",
  "Acharya, Shantanu",
  "Rekesh, Dima",
  "Jia, Fei",
  "Zhang, Yang",
  "Ginsburg, Boris"
]
```
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
检验模型实际可用上下文长度，而不只看标称窗口。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 既有评测缺口
单一 needle-in-a-haystack 容易被模型攻克，不能代表长上下文中的多跳追踪、聚合与问答。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

## 构建方式

### 题目来源
程序合成检索、多跳变量追踪、聚合与问答任务，可配置长度及复杂度。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 出题与标注背景
研究团队设计可控生成器，不是人工逐题知识考试。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 审核
生成器根据任务规则产生可验证标准答案；精确人工逐条审查量待核实。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 质量控制
分任务及长度评测，以多种任务避免只测一种检索模式。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
13 个任务配置；原论文各任务、各长度 500 条，测试长度 4k、8k、16k、32k、64k、128k token。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 题型
合成检索、变量追踪、聚合与问答
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 语言
英语任务模板；具体语料配置应固定
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 难度
通过长度、目标数量、变量链等控制难度，而非单一固定难度集。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 公开与隐藏划分
生成代码及任务配置公开，可重新合成；需保存随机种子和配置以复现。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

## 评测方法

### 指标
任务准确率/目标召回，任务平均与按长度汇总的指标；以所用脚本定义为准。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 评分
按任务要求比较模型回答中的目标答案，再汇总任务与长度。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 提示与生成设置
原论文使用 greedy decoding、模型聊天模板与答案前缀；需记录 tokenizer、模板及长度设定。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 脚本
https://github.com/hsiehjackson/RULER
[来源1](https://github.com/hsiehjackson/RULER)（采集2026-11-07）

### 可比性警告
不同 token 长度、任务子集、分词器和长度加权分数不能混比；Hunyuan报告的 QA 子任务不是13任务全量。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-09-23：Hunyuan-A13B §4.2–4.3实际使用 RULER 并报告结果；厂商自报，需保留各基准的提示/上下文条件。

### 数据版本
待核实
[来源1](https://github.com/hsiehjackson/RULER)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2024-04-10T08:41:27+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2024-04-12T08:53:59+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2024-08-07T06:48:58+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 饱和情况
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题
标称上下文长度不等于有效窗口；长文本长度、任务复杂度和模板选择可能改变结论。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 衍生评测
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://arxiv.org/abs/2404.06654
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果
```json
[
  {
    "model": "Hunyuan-A13B（报告命名）",
    "score": 76.7,
    "unit": "%",
    "metric": "RULER QA子任务，0–128K四长度段平均",
    "scope": "Hunyuan技术报告表6，厂商自报；不是原始13任务综合分",
    "evaluation_date": "报告日期2026-09-23；精确运行日期待核实",
    "snapshot_date": "2026-11-07"
  }
]
```
[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

### 覆盖与时效限制
仅收录H2技术报告中明确可读的厂商自报成绩；模型标签按报告保留，未核实其精确API运行日期。不能把这些成绩冒充独立机构当前排行榜。
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07） [来源2](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
```json
[
  "chsieh@nvidia.com",
  "simengs@nvidia.com"
]
```
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

### 仓库讨论与Issues
https://github.com/hsiehjackson/RULER/issues
[来源1](https://github.com/hsiehjackson/RULER)（采集2026-11-07）

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2404.06654)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2404.06654
[来源1](https://arxiv.org/pdf/2404.06654)（采集2026-11-07）

### 原件SHA-256
8a4bc6ca28d84570eec7f42652400c2121f4c8bc361701634e596772e396fc22
[来源1](https://arxiv.org/pdf/2404.06654)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
682955
```
[来源1](https://arxiv.org/pdf/2404.06654)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1tj6vWFyQX2ASPe0dVeBL5yRrcunkap7I",
  "webViewLink": "https://drive.google.com/drive/folders/1tj6vWFyQX2ASPe0dVeBL5yRrcunkap7I"
}
```
[来源1](https://drive.google.com/drive/folders/1tj6vWFyQX2ASPe0dVeBL5yRrcunkap7I)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1BXarcTj97jqzXNsQCTNfsSGu4mnKXyY3yYCp-eiUak4",
    "webViewLink": "https://docs.google.com/document/d/1BXarcTj97jqzXNsQCTNfsSGu4mnKXyY3yYCp-eiUak4/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/1BXarcTj97jqzXNsQCTNfsSGu4mnKXyY3yYCp-eiUak4/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2404.06654)（采集2026-11-07） [来源](https://arxiv.org/pdf/2404.06654)（采集2026-11-07）
