# FrontierCode

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

> 尚未找到独立论文PDF；已保留官方方法页HTML原件，不用示例文件或自行导出的页面冒充原始论文。

## 基本信息

### 简称
FrontierCode [来源1](https://cognition.com/frontiercode)

### 全称
FrontierCode [来源1](https://cognition.com/frontiercode)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
2.0；1.1保留为历史快照 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 论文版本
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 发布日期
2.0：2026-10-27（官方文章日期，未标时区/时间） [来源2](https://cognition.com/blog/frontier-code-2.0)

### 主板块
代码 [来源1](https://cognition.com/frontiercode)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "前沿代码Agent能力"
]
```
 [来源1](https://cognition.com/frontiercode)

### 许可证
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 论文
待核实 [来源2](https://cognition.com/blog/frontier-code-2.0)

> 已核实官方方法文章与榜单；检索未找到独立原始学术论文。方法文章不冒充论文。

### 官方代码
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 数据地址
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方入口
https://cognition.com/frontiercode [来源1](https://cognition.com/frontiercode)

### 论文标题
待核实 [来源2](https://cognition.com/blog/frontier-code-2.0)

> 官方方法页标题 FrontierCode 2.0；独立论文标题待核实。

## 发起与维护

### 机构与发起方
Cognition [来源2](https://cognition.com/blog/frontier-code-2.0)

### 合作方
20 多名顶尖开源维护者参与2.0任务构建。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 作者
The Cognition Team（官方方法文章署名） [来源2](https://cognition.com/blog/frontier-code-2.0)

### 当前维护方
Cognition；Artificial Analysis 独立运行其评测实现。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 资助
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
能否提交维护者愿意合并的代码：功能正确、理解隐含需求、遵循现有抽象/兼容性并避免过度改写。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 设计背景
详尽规格和仅单元测试容易忽略真实开发中的未明说约束、可维护性与合并质量。 [来源2](https://cognition.com/blog/frontier-code-2.0)

## 构建方式

### 题目来源
从开源维护者自己维护的真实仓库设计任务；每位维护者每题投入超过40小时；2.0加入更多安全与性能任务。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 出题者背景
20 多位世界级开源开发者，不只是通用标注员。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 审核流程
人工与自动审查任务说明、参考解和评分规则；2.0中80%参考解区别于上游PR。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 质量控制
2.0较1.1覆盖更多仓库、43%更多 blocking criteria，强化彻底性与回归检查，并放宽不必要的scope限制。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 去污染
题目保持私有；轨迹扫描若发现查找现成解则记0，不能排除仓库本身的预训练接触。 [来源2](https://cognition.com/blog/frontier-code-2.0)

## 数据形式

### 题量与规模
2.0：132任务；1.1 Main 是150任务中的100题，不能混合分母。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 题型
真实仓库代码修改，综合测试和维护者评分rubric。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 模态

```json
[
  "文本",
  "源代码",
  "仓库环境"
]
```
 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 语言
跨仓库语言；公开示例包括 JavaScript 与 Kotlin，完整语言分布待核实。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 难度
强调隐含约束、完整修复和可合并标准；2.0非简单同题扩量。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 公开与隐藏划分
评分任务私有；官方和AA公开部分例题与方法，而非完整数据集。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

## 评测方法

### 指标
task等权的加权rubric得分 (%)。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 评分
任何blocking检查失败或查找解被轨迹扫描标记，整次尝试0分；其余按各项权重汇总。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 提示与运行设置
AA2.0：Stirrup，132题各3次，最多500turn，GPT-6 Luna medium作LLM评审；1.1上限250turn。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 官方评测脚本
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 可比性警示
Cognition官方harness与AA Stirrup独立实现不同；1.1与2.0不同；评分不是简单任务全对率，推理effort增加也可能因scope变化降分。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://cognition.com/frontiercode)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "2.0；1.1保留为历史快照",
  "evidence_2026_h2": [
    {
      "url": "https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1",
      "date": "2026-10-28",
      "note": "Artificial Analysis 2026-10-28文章明确报告 FrontierCode v1.1 的结果并将其纳入Coding Agent Index；独立机构评测。"
    }
  ]
}
```
 [来源4](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1) [来源2](https://cognition.com/blog/frontier-code-2.0)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 饱和情况
2.0官方发布实验最优约45%，官方判断远未饱和；这不是对所有未来系统的绝对结论。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 污染与争议
私有任务降低直接题目泄漏；scope约束与未明说需求会影响解释，官方已在2.0审计并调整范围标准。 [来源2](https://cognition.com/blog/frontier-code-2.0)

### 衍生与版本关系
1.0、1.1、2.0是套件版本，本库合计一个 benchmark。 [来源2](https://cognition.com/blog/frontier-code-2.0)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://cognition.com/frontiercode)

### 官方榜单
https://cognition.com/frontiercode [来源1](https://cognition.com/frontiercode)

### 独立评测覆盖
https://artificialanalysis.ai/evaluations/frontiercode-2-0 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0)

### 核验结果

```json
[
  {
    "model": "Claude Opus 5.5 (Max, Default Fallback)",
    "score": 46.4,
    "metric": "weighted score (%)",
    "benchmark_version": "2.0/132题",
    "result_type": "AA独立当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Claude Opus 5.5 (Xhigh, Default Fallback)",
    "score": 43.8,
    "metric": "weighted score (%)",
    "benchmark_version": "2.0/132题",
    "result_type": "AA独立当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "GPT-6 Astra (Max)",
    "score": 42.4,
    "metric": "weighted score (%)",
    "benchmark_version": "2.0/132题",
    "result_type": "AA独立当前页面",
    "source_date": "2026-11-07",
    "collected_at": "2026-11-07 KST"
  },
  {
    "model": "Claude Opus 5.5 (best effort)",
    "score": 45.5,
    "metric": "weighted score (%)",
    "benchmark_version": "2.0",
    "result_type": "Cognition官方发布实验",
    "source_date": "2026-10-27",
    "collected_at": "2026-11-07 KST"
  }
]
```
 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0) [来源2](https://cognition.com/blog/frontier-code-2.0)

### 覆盖与时效说明
官方文章明确列45.5%，AA独立页面46.4%，因不同实现/配置分别保留，不将差异强行归为一次分数修正；官方当前交互表完整排名待核实。 [来源3](https://artificialanalysis.ai/evaluations/frontiercode-2-0) [来源2](https://cognition.com/blog/frontier-code-2.0)

## 联系方式

### 公开工作邮箱
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方社交渠道
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 原始PDF SHA-256
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 原始PDF字节数
待核实 [来源1](https://cognition.com/frontiercode)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### Drive资料文件夹

```json
{
  "id": "17CEUgtPsTmM1-FRtP00KFytv2hRwmeiK",
  "webViewLink": "https://drive.google.com/drive/folders/17CEUgtPsTmM1-FRtP00KFytv2hRwmeiK"
}
```
 [来源5](https://drive.google.com/drive/folders/17CEUgtPsTmM1-FRtP00KFytv2hRwmeiK)

### 其他文档

```json
[
  {
    "type": "官方方法页HTML归档（非论文PDF）",
    "id": "1pVb8sMOUBsDfBPqsjizyUdsZ-ebmX0Pr",
    "webViewLink": "https://drive.google.com/file/d/1pVb8sMOUBsDfBPqsjizyUdsZ-ebmX0Pr/view?usp=drivesdk",
    "source_url": "https://cognition.com/blog/frontier-code-2.0",
    "accessed": "2026-11-07",
    "sha256": "c0073b17387e29534db8ca821b92b524ba178cdbe36331b6873fdcdc7b49dedb",
    "bytes": 226414
  },
  {
    "type": "中文介绍Google Doc",
    "id": "1vWlLpKFs5bGTOQWxrpv5Pa0O98NReU1uHnlksripJis",
    "webViewLink": "https://docs.google.com/document/d/1vWlLpKFs5bGTOQWxrpv5Pa0O98NReU1uHnlksripJis/edit?usp=drivesdk"
  }
]
```
 [来源2](https://cognition.com/blog/frontier-code-2.0) [来源6](https://docs.google.com/document/d/1vWlLpKFs5bGTOQWxrpv5Pa0O98NReU1uHnlksripJis/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件
待核实 [来源1](https://cognition.com/frontiercode)

> 官方方法页已核实，未找到独立原始论文 PDF；不伪造论文附件。

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
 [来源1](https://cognition.com/frontiercode)

## 来源

1. https://cognition.com/frontiercode — 采集：2026-11-07 KST。
2. https://cognition.com/blog/frontier-code-2.0 — 采集：2026-11-07 KST。
3. https://artificialanalysis.ai/evaluations/frontiercode-2-0 — 采集：2026-11-07 KST。
4. https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1 — 采集：2026-11-07 KST。
5. https://drive.google.com/drive/folders/17CEUgtPsTmM1-FRtP00KFytv2hRwmeiK — 采集：2026-11-07 KST。
6. https://docs.google.com/document/d/1vWlLpKFs5bGTOQWxrpv5Pa0O98NReU1uHnlksripJis/edit?usp=drivesdk — 采集：2026-11-07 KST。
