# CRUXEval

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9/view?usp=drivesdk)

## 基本信息

### 简称
CRUXEval [来源1](https://crux-eval.github.io/)

### 全称
CRUXEval [来源1](https://crux-eval.github.io/)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
原始 800 函数；CRUXEval-I / CRUXEval-O 双方向 [来源2](https://arxiv.org/abs/2401.03065)

### 论文版本
arXiv v1 [来源2](https://arxiv.org/abs/2401.03065)

> 论文修订版本不等同数据集版本。

### 发布日期
2024-01-06 05:53:51 KST [来源2](https://arxiv.org/abs/2401.03065)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
代码 [来源2](https://arxiv.org/abs/2401.03065)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "代码输入输出推断"
]
```
 [来源2](https://arxiv.org/abs/2401.03065)

### 许可证
MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源3](https://github.com/facebookresearch/cruxeval)

### 论文
https://arxiv.org/abs/2401.03065 [来源2](https://arxiv.org/abs/2401.03065)

### 官方代码
https://github.com/facebookresearch/cruxeval [来源1](https://crux-eval.github.io/)

### 数据地址
https://huggingface.co/datasets/cruxeval-org/cruxeval [来源1](https://crux-eval.github.io/)

### 官方入口
https://crux-eval.github.io/ [来源1](https://crux-eval.github.io/)

### 论文标题
CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution [来源2](https://arxiv.org/abs/2401.03065)

## 发起与维护

### 机构与发起方
MIT 与 Meta AI 作者团队（作者单位口径） [来源2](https://arxiv.org/abs/2401.03065)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2401.03065)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Gu, Alex",
  "Rozière, Baptiste",
  "Leather, Hugh",
  "Solar-Lezama, Armando",
  "Synnaeve, Gabriel",
  "Wang, Sida I."
]
```
 [来源2](https://arxiv.org/abs/2401.03065)

### 当前维护方
facebookresearch/cruxeval当前已标为archived（2026-11-07核验）；历史维护方为CRUXEval团队，不能推断仍在活跃维护。 [来源3](https://github.com/facebookresearch/cruxeval)

### 资助
待核实 [来源2](https://arxiv.org/abs/2401.03065)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
代码理解、输入反推和输出预测，尤其在不运行代码时模拟程序执行。 [来源2](https://arxiv.org/abs/2401.03065)

### 设计背景
生成代码的成功率无法独立揭示模型是否理解简单程序的执行语义。 [来源2](https://arxiv.org/abs/2401.03065)

## 构建方式

### 题目来源
使用 CodeLlama-34B 生成候选 Python 函数及输入输出，经筛选后随机抽取 800 个。 [来源1](https://crux-eval.github.io/)

### 出题者背景
MIT / Meta AI 研究者；候选程序由模型合成。 [来源1](https://crux-eval.github.io/)

### 审核流程
筛选约可由程序员一分钟内心算的短函数与有效输入输出。 [来源1](https://crux-eval.github.io/)

### 质量控制
限制程序复杂性并执行验证配对的输入输出；双方向共用程序，不能算成两个独立题库。 [来源1](https://crux-eval.github.io/)

### 去污染
合成新程序旨在减少既有人工题复用，但不构成所有后续模型的无污染证明。 [来源1](https://crux-eval.github.io/)

## 数据形式

### 题量与规模
800 个 Python 函数/输入/输出样本；输入预测与输出预测是同一数据的两种评测。 [来源2](https://arxiv.org/abs/2401.03065)

### 题型
CRUXEval-I：给程序与输出求可行输入；CRUXEval-O：给程序与输入求输出。 [来源2](https://arxiv.org/abs/2401.03065)

### 模态

```json
[
  "代码",
  "文本"
]
```
 [来源2](https://arxiv.org/abs/2401.03065)

### 语言
Python；英语提示。 [来源2](https://arxiv.org/abs/2401.03065)

### 难度
短小、可人类心算的程序也可能难于模型；不等同软件开发难度。 [来源2](https://arxiv.org/abs/2401.03065)

### 公开与隐藏划分
原始数据、脚本与提示公开；未据此主张隐藏集。 [来源2](https://arxiv.org/abs/2401.03065)

## 评测方法

### 指标
按方向分别报告 pass@1 / pass@5 等；CoT 与直接回答分开。 [来源2](https://arxiv.org/abs/2401.03065)

### 评分
输出预测检查程序真实输出；输入预测接受能经执行产生目标输出的有效输入。 [来源2](https://arxiv.org/abs/2401.03065)

### 提示与运行设置
论文分别报告直接作答与 chain-of-thought；提示、采样数、是否使用执行工具必须说明。 [来源2](https://arxiv.org/abs/2401.03065)

### 官方评测脚本
https://github.com/facebookresearch/cruxeval [来源1](https://crux-eval.github.io/)

### 可比性警示
CRUX-I / CRUX-O 分数不平均冒称单一官方总分；不把带解释提示与直接预测混排。 [来源2](https://arxiv.org/abs/2401.03065)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://crux-eval.github.io/)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始 800 函数；CRUXEval-I / CRUXEval-O 双方向",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1/§4.2及表2–4实际报告 CRUXEval；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。"
    }
  ]
}
```
 [来源4](https://arxiv.org/html/2609.27284v1) [来源2](https://arxiv.org/abs/2401.03065)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Alex Gu [ view email ] [v1] 2024-01-06 05:53:51 KST (1,309 KB) [来源2](https://arxiv.org/abs/2401.03065)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2401.03065)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
Hunyuan 报告参考文献把 CRUXEval 关联到 Liu 2023（EvalPlus）；本条依 Gu 等人 2401.03065 识别原基准。 [来源2](https://arxiv.org/abs/2401.03065) [来源4](https://arxiv.org/html/2609.27284v1)

### 衍生与版本关系
CRUXEval-I 与 CRUXEval-O 是同一 benchmark 两个子任务。 [来源2](https://arxiv.org/abs/2401.03065) [来源4](https://arxiv.org/html/2609.27284v1)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://crux-eval.github.io/)

### 官方榜单
https://crux-eval.github.io/ [来源1](https://crux-eval.github.io/)

### 独立评测覆盖
待核实 [来源1](https://crux-eval.github.io/)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "Hunyuan-A13B base",
    "score": 70.13,
    "metric": "CRUX-I (%)",
    "benchmark_version": "原始双方向；版本待核实",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST",
    "settings": "1-shot"
  },
  {
    "model": "Hunyuan-A13B base",
    "score": 77,
    "metric": "CRUX-O (%)",
    "benchmark_version": "原始双方向；版本待核实",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST",
    "settings": "1-shot"
  }
]
```
 [来源4](https://arxiv.org/html/2609.27284v1)

### 覆盖与时效说明
下面仅列能从已打开来源核验的结果。历史论文基线、厂商自报与当前榜单分开，不构成跨设置综合排名。 [来源2](https://arxiv.org/abs/2401.03065)

## 联系方式

### 公开工作邮箱
待核实 [来源2](https://arxiv.org/abs/2401.03065)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
https://github.com/facebookresearch/cruxeval/issues [来源1](https://crux-eval.github.io/)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2401.03065)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2401.03065)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2401.03065 [来源5](https://arxiv.org/pdf/2401.03065)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
1a356948d0d2543ab7b142029f208271a2581575cee4f5b37eb647cbbf0b435e [来源5](https://arxiv.org/pdf/2401.03065)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
2012215
```
 [来源5](https://arxiv.org/pdf/2401.03065)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou",
  "webViewLink": "https://drive.google.com/drive/folders/1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou"
}
```
 [来源6](https://drive.google.com/drive/folders/1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c",
    "webViewLink": "https://docs.google.com/document/d/14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c/edit?usp=drivesdk"
  }
]
```
 [来源1](https://crux-eval.github.io/) [来源7](https://docs.google.com/document/d/14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9",
  "webViewLink": "https://drive.google.com/file/d/1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9/view?usp=drivesdk)

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
 [来源1](https://crux-eval.github.io/)

## 来源

1. https://crux-eval.github.io/ — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2401.03065 — 采集：2026-11-07 KST。
3. https://github.com/facebookresearch/cruxeval — 采集：2026-11-07 KST。
4. https://arxiv.org/html/2609.27284v1 — 采集：2026-11-07 KST。
5. https://arxiv.org/pdf/2401.03065 — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9/view?usp=drivesdk — 采集：2026-11-07 KST。
