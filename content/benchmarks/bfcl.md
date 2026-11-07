# Berkeley Function Calling Leaderboard (BFCL)

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk)

## 基本信息

### 简称
Berkeley Function Calling Leaderboard (BFCL) [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 全称
Berkeley Function Calling Leaderboard [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 基准版本
当前BFCL V4；Hunyuan报告为V3 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 论文版本
ICML 2025，PMLR 267，页48371–48392 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 发布日期
ICML论文2025-07-13至19会议；首次基准发布日期待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 主板块
Agent [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "函数调用"
]
```
 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 许可证
Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源3](https://github.com/ShishirPatil/gorilla)

### 论文
https://proceedings.mlr.press/v267/patil25a.html [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 官方代码
https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 数据地址
https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 官方入口
https://gorilla.cs.berkeley.edu/leaderboard.html [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 论文标题
The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models [来源2](https://proceedings.mlr.press/v267/patil25a.html)

## 发起与维护

### 机构与发起方
UC Berkeley Gorilla研究团队（机构口径） [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 合作方
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Shishir G Patil",
  "Huanzhi Mao",
  "Fanjia Yan",
  "Charlie Cheng-Jie Ji",
  "Vishnu Suresh",
  "Ion Stoica",
  "Joseph E. Gonzalez"
]
```
 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 当前维护方
Gorilla / BFCL团队 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 资助
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
选择工具、构造合法参数、串并行函数调用、拒绝无关调用及有状态多步Agent决策。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 设计背景
工具调用既需要多样真实函数来源，也需要可扩展地判断不同语法表达是否同样有效。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

## 构建方式

### 题目来源
专家整理函数与用户/企业/开源社区贡献的真实函数和提示；覆盖多编程语言。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 出题者背景
Berkeley研究者与企业/开源工具贡献者。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 审核流程
专家整理与用户贡献结合，使用AST/执行等按类别验证调用。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 质量控制
区分单轮、并行、多轮、相关性与状态；AST验证语义参数而非纯字符串表面。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

### 去污染
真实函数多样化与后续版本增加覆盖；公开函数/提示仍不能提供无污染保证。 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

## 数据形式

### 题量与规模
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 题型
单/并行函数调用、多轮状态交互、相关性/拒绝调用与agentic任务。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 模态

```json
[
  "文本",
  "结构化函数schema",
  "工具调用"
]
```
 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 语言
多种编程语言函数；自然语言分布需按具体版本核实。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 难度
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开与隐藏划分
官方发布数据和评测包；各版本子集与隐藏性需按V4材料确认。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

## 评测方法

### 指标
分类准确率；Overall为子类别分数的非加权均值。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 评分
按类别使用AST匹配、执行或有状态检查；FC原生调用与提示转换分别标注。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 提示与运行设置
页面当前标示代码commit f7cf7359b7ac615a0b294831c5ba2bc95ee4a000；bfcl-eval==2025.12.17；模型提示和native-FC须一起固定。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 官方评测脚本
https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 可比性警示
V1(AST)、V2(真实贡献函数)、V3(多轮)、V4(agentic)覆盖变化，Hunyuan的BFCLv3不可当作当前V4成绩。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "当前BFCL V4；Hunyuan报告为V3",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.2 Agents及表3–4实际报告 Berkeley Function Calling Leaderboard (BFCL)（BFCL为v3），属于厂商自报评测。"
    }
  ]
}
```
 [来源4](https://arxiv.org/html/2609.27284v1) [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 饱和情况
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
AST正确不等于业务任务完成；多轮与记忆带来新评测维度，版本间不可用一个总分追踪。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 衍生与版本关系
BFCL V1–V4为演进版本；本库只计一个函数调用benchmark。 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 官方榜单
https://gorilla.cs.berkeley.edu/leaderboard.html [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

### 独立评测覆盖
待核实 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "Hunyuan-A13B slow-thinking",
    "score": 78.3,
    "metric": "BFCLv3 (%)",
    "benchmark_version": "V3",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Hunyuan-A13B fast-thinking",
    "score": 65.9,
    "metric": "BFCLv3 (%)",
    "benchmark_version": "V3",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源4](https://arxiv.org/html/2609.27284v1)

### 覆盖与时效说明
已核实官方V4页面及2026-04-12更新标示，但静态正文未核出动态榜单行；当前V4前三待核实，不把V3厂商自报移入V4。 [来源4](https://arxiv.org/html/2609.27284v1)

## 联系方式

### 公开工作邮箱
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
https://github.com/ShishirPatil/gorilla/issues [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://proceedings.mlr.press/v267/patil25a.html)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf [来源5](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
5248f4770823b2a73fd52e3b12339d94121ff1b359c45163c5a47168edab7a2f [来源5](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
1200643
```
 [来源5](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT",
  "webViewLink": "https://drive.google.com/drive/folders/1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT"
}
```
 [来源6](https://drive.google.com/drive/folders/1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748",
    "webViewLink": "https://docs.google.com/document/d/1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748/edit?usp=drivesdk"
  }
]
```
 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html) [来源7](https://docs.google.com/document/d/1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw",
  "webViewLink": "https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk)

## 变更记录


```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  }
]
```
 [来源1](https://gorilla.cs.berkeley.edu/leaderboard.html)

## 来源

1. https://gorilla.cs.berkeley.edu/leaderboard.html — 采集：2026-11-07 KST。
2. https://proceedings.mlr.press/v267/patil25a.html — 采集：2026-11-07 KST。
3. https://github.com/ShishirPatil/gorilla — 采集：2026-11-07 KST。
4. https://arxiv.org/html/2609.27284v1 — 采集：2026-11-07 KST。
5. https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1zwtuIHkLTUGoh5pBXvvm-b-3MEG3Y1eT — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/1BWPxXO2EdhGmVqtsOB6Jza18t-l6H88biHblVLrc748/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1XG8s-CDiGwupc7p1y5tOE2nKnK877fBw/view?usp=drivesdk — 采集：2026-11-07 KST。
