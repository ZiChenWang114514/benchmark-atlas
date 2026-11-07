# MMLU-Redux

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1ta0g5jbJkYUKiPSsZySck8P4n0Y-9zAn/view?usp=drivesdk)

## 基本信息

### 简称
MMLU-Redux
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 全称
MMLU-Redux
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 基准版本
2.0
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 论文版本
arXiv v3
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 发布日期
2024-06-06
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "纠错后的多学科知识"
]
```
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 许可证
论文声明 CC BY 4.0；具体数据文件再分发仍应检查数据卡。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 论文
https://arxiv.org/abs/2406.04127
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 官方代码
https://github.com/aryopg/mmlu-redux
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 数据地址
https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 官方入口
https://github.com/aryopg/mmlu-redux
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 论文标题
Are We Done with MMLU?
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
论文作者来自 University of Edinburgh、Sapienza University of Rome、University of Bari、UCL、University of Trento 等；此为作者单位记录。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Gema, Aryo Pradipta",
  "Leang, Joshua Ong Jun",
  "Hong, Giwon",
  "Devoto, Alessio",
  "Mancino, Alberto Carlo Maria",
  "Saxena, Rohit",
  "He, Xuanli",
  "Zhao, Yu",
  "Du, Xiaotang",
  "Madani, Mohammad Reza Ghasemi",
  "Barale, Claire",
  "McHardy, Robert",
  "Harris, Joshua",
  "Kaddour, Jean",
  "van Krieken, Emile",
  "Minervini, Pasquale"
]
```
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
重新检查 MMLU 的题目与答案质量，区分模型失误和基准本身的错误。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 既有评测缺口
已有高分不代表题库可靠；题干歧义、错误标签和缺少正确选项会扭曲模型排序与能力判断。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

## 构建方式

### 题目来源
从 MMLU 每个学科抽取 100 题，并人工标注题目和答案中的错误。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 出题与标注背景
研究者与相关学科审阅人员进行人工核验；并非重新原创全部考试题。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 审核
依据错误分类体系人工检查，并查询可信材料核实答案。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 质量控制
保留 error_type、source、correct_answer、potential_reason 等字段，便于追溯纠错依据。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
当前 2.0 数据卡与正式论文覆盖 57 学科、5,700 道人工标注题；早期仓库/版本介绍为 30 学科、3,000 题，不能混用。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07） [来源2](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（采集2026-11-07）

### 题型
MMLU 四选一题，加错误标签、修正答案及依据
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 语言
英语
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 难度
沿用 MMLU 跨教育阶段、跨学科难度；主要变化是质量核验，不是统一增加难度。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 公开与隐藏划分
2.0 数据卡按学科提供 test，每科 100 条；它是 MMLU 抽样纠错集，不是 MMLU 全量替代物。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

## 评测方法

### 指标
纠错前后准确率与题目错误类型统计。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 评分
依据人工纠错结果分析模型评价变化；需明确是原始标签、无错子集还是修正标签得分。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 提示与生成设置
论文分析包含 HELM v1.3.0（2024-05-15）预测；不同模型/实验的提示设置需分别记录。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 脚本
https://github.com/aryopg/mmlu-redux
[来源1](https://github.com/aryopg/mmlu-redux)（采集2026-11-07）

### 可比性警告
3,000 题早期版与 5,700 题 2.0 不可直接混比；只用原标签算分不等于完成 Redux 纠错评测。
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 对比研究的表1–2和§3.1实际使用 MMLU-Redux，将其纳入13个多选基准的模型评测。

### 数据版本
2.0
[来源1](https://huggingface.co/datasets/edinburgh-dawg/mmlu-redux-2.0)（采集2026-11-07）

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2024-06-06T23:49:06+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2024-06-08T00:19:06+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2025-01-10T23:31:21+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

### 饱和情况
该工作主要诊断题库错误；不能由纠错集上的分数推出 MMLU 已饱和或尚未饱和。
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

### 污染与已知问题
版本冲突：早期材料 3,000 题/30 学科，2.0 与 NAACL 正式论文 5,700 题/57 学科。本条以当前 2.0 为规模基准，保留早期记录而不静默覆盖。
[来源1](https://aclanthology.org/2025.naacl-long.262/)（采集2026-11-07）

### 衍生评测
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://arxiv.org/abs/2406.04127
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

### 二级机构榜单
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果
```json
[
  {
    "model": "Jev（研究表2原标签）",
    "score": 95.0,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Qwen3.8-Max（研究表2原标签）",
    "score": 94.3,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Claude Opus 5.5（研究表2原标签）",
    "score": 94.2,
    "unit": "%",
    "metric": "accuracy（研究表2口径）",
    "scope": "2026-H2 Jev对比研究表2；不是基准官方实时榜或AA独立榜",
    "evaluation_date": "论文2026-10-08；精确运行日期和API版本待核实",
    "snapshot_date": "2026-11-07"
  }
]
```
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

### 覆盖与时效限制
H2对比研究可读结果；保留论文模型标签，未核实精确API日期，不将混合提示或历史引用成绩都视为同协议。未核实当前官方统一实时榜和AA/Epoch/LMArena对应独立单项榜。
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07） [来源2](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 仓库讨论与Issues
https://github.com/aryopg/mmlu-redux/issues
[来源1](https://github.com/aryopg/mmlu-redux)（采集2026-11-07）

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2406.04127)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2406.04127
[来源1](https://arxiv.org/pdf/2406.04127)（采集2026-11-07）

### 原件SHA-256
a45720c5df8c7e7fe243846a849e4799a07fa453d77b4cd55094c6e058b8b8ab
[来源1](https://arxiv.org/pdf/2406.04127)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
747909
```
[来源1](https://arxiv.org/pdf/2406.04127)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1xg8wVXxTJ3hwpqxa6FxWizpKQXYGDW2c",
  "webViewLink": "https://drive.google.com/drive/folders/1xg8wVXxTJ3hwpqxa6FxWizpKQXYGDW2c"
}
```
[来源1](https://drive.google.com/drive/folders/1xg8wVXxTJ3hwpqxa6FxWizpKQXYGDW2c)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1PvrGue4_EH6leNh5jz4DzwZGfpdqSK2qTbkzo-WgwSM",
    "webViewLink": "https://docs.google.com/document/d/1PvrGue4_EH6leNh5jz4DzwZGfpdqSK2qTbkzo-WgwSM/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/1PvrGue4_EH6leNh5jz4DzwZGfpdqSK2qTbkzo-WgwSM/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2406.04127)（采集2026-11-07） [来源](https://arxiv.org/pdf/2406.04127)（采集2026-11-07）
