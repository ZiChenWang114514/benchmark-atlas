# LongBench v2

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1zR9mNbXLbLSQimS1M2M3X98NBO9XvScx/view?usp=drivesdk)

## 基本信息

### 简称
LongBench v2
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 全称
LongBench v2
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 基准版本
v2
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 论文版本
arXiv v2
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 发布日期
2024-12-19
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "长上下文理解"
]
```
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 许可证
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文
https://arxiv.org/abs/2412.15204
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 官方代码
https://github.com/THUDM/LongBench
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 数据地址
https://huggingface.co/datasets/THUDM/LongBench-v2
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 官方入口
https://longbench2.github.io/
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 论文标题
LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
论文作者单位包括清华大学、智谱；Yushi Bai 为首作者。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Bai, Yushi",
  "Tu, Shangqing",
  "Zhang, Jiajie",
  "Peng, Hao",
  "Wang, Xiaozhi",
  "Lv, Xin",
  "Cao, Shulin",
  "Xu, Jiazheng",
  "Hou, Lei",
  "Dong, Yuxiao",
  "Tang, Jie",
  "Li, Juanzi"
]
```
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
检验真实长上下文中的深层理解与推理，超越简单大海捞针。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 既有评测缺口
仅检索固定针或较易短问答不足以测量长文档、多文档、代码仓库和结构数据理解。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

## 构建方式

### 题目来源
由标注者提交实际接触的学术、法律、小说、代码及表格材料，再依据材料编题。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 出题与标注背景
97 名受过高等教育的标注者、24 名专家审阅者。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 审核
三模型难度筛选、人工审查与返工；只有通过审核的条目才获得奖励。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 质量控制
使用选择题提高评分一致性，同时用专家限时作答估计难度。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
503 道四选一题，6 大任务类、20 子任务；上下文 8k–2M words（词，非 token）。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 题型
基于长上下文的四选一选择题
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 语言
英语
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 难度
192 道 easy、311 道 hard；人类专家在 15 分钟限时下准确率 53.7%。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 公开与隐藏划分
公开测试题及答案，不能把不同长度段看作同难度随机分组。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

## 评测方法

### 指标
总体准确率，以及 easy/hard 和 short/medium/long 分组准确率。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 评分
从模型生成中提取最终选项，与金标准比较。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 提示与生成设置
原论文 0-shot / 0-shot CoT；temperature 0.1，直接回答上限 128 token、CoT 1024 token；过长输入中间截断。官网后续模型另有预算说明。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 脚本
https://github.com/THUDM/LongBench
[来源1](https://github.com/THUDM/LongBench)（采集2026-11-07）

### 可比性警告
words 不等于 tokens；上下文截断、CoT、思考预算和 YaRN 会影响结果。官网脚注说明 Qwen 结果使用 YaRN factor4，不能照搬为原论文所有模型设置。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-09-23：Hunyuan-A13B §4.2–4.3实际使用 LongBench v2 并报告结果；厂商自报，需保留各基准的提示/上下文条件。

### 数据版本
v2
[来源1](https://huggingface.co/datasets/THUDM/LongBench-v2)（采集2026-11-07）

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2024-12-20T03:59:17+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2025-01-03T20:44:51+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 饱和情况
官网可读最高 overall w/CoT 为 63.3%，不足以据此宣布全部长上下文任务已饱和；其静态表更新时间也需谨慎。
[来源1](https://longbench2.github.io/)（采集2026-11-07）

### 污染与已知问题
论文主体与官网人类分数为 53.7%；论文结论曾出现 50.1%，该数值亦为 GPT-4o 的历史直接回答分数。本条采用主体及官网的人类 53.7%，保留冲突说明。
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

### 衍生评测
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 榜单快照

### 采集日
2026-11-07
[来源1](https://longbench2.github.io/)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://longbench2.github.io/
[来源1](https://longbench2.github.io/)（采集2026-11-07）

### 二级机构榜单
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 可读结果
```json
[
  {
    "model": "Gemini-2.5-Pro",
    "model_date": "2025-03-25（官网Date列）",
    "score": 63.3,
    "unit": "%",
    "metric": "overall accuracy w/CoT",
    "scope": "官方静态榜，1M上下文",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Gemini-2.5-Flash",
    "model_date": "2025-04-17（官网Date列）",
    "score": 62.1,
    "unit": "%",
    "metric": "overall accuracy w/CoT",
    "scope": "官方静态榜，1M上下文",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Qwen3-235B-A22B-Thinking-2507",
    "model_date": "2025-07-25（官网Date列）",
    "score": 60.6,
    "unit": "%",
    "metric": "overall accuracy w/CoT",
    "scope": "官方静态榜，256k上下文",
    "snapshot_date": "2026-11-07"
  }
]
```
[来源1](https://longbench2.github.io/)（采集2026-11-07）

### 覆盖与时效限制
官网采集日可读表前列如上；页面 Last Update 标为 2025-05-06，却包含 2025-07 行，更新标记不一致。分数是官网可读快照，不宣称覆盖2026所有新模型；H2厂商报告的同名分数不并入此榜。
[来源1](https://longbench2.github.io/)（采集2026-11-07） [来源2](https://arxiv.org/html/2609.27284v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 仓库讨论与Issues
https://github.com/THUDM/LongBench/issues
[来源1](https://github.com/THUDM/LongBench)（采集2026-11-07）

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2412.15204)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2412.15204
[来源1](https://arxiv.org/pdf/2412.15204)（采集2026-11-07）

### 原件SHA-256
35e7e66bb3323d8da0a6dde553a9f5fc9be97ed3232d87a24be89f5a8f9024d5
[来源1](https://arxiv.org/pdf/2412.15204)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
9951437
```
[来源1](https://arxiv.org/pdf/2412.15204)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE",
  "webViewLink": "https://drive.google.com/drive/folders/1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE"
}
```
[来源1](https://drive.google.com/drive/folders/1mmQ7rlb_FLxxhHcU5XzUsBvk1iAYKCwE)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8",
    "webViewLink": "https://docs.google.com/document/d/17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/17TDazsrZ5DvO4AHSc0I8ObvxYn7OnskRniIB842v5-8/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2412.15204)（采集2026-11-07） [来源](https://arxiv.org/pdf/2412.15204)（采集2026-11-07）
