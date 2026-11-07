# MMMU-Pro

> 核验：2026-11-07（KST / Asia/Seoul）。基于已打开官方材料中文改写；待核实不等于未公开。

## 为什么近期热门

**trending: A**。AA当前方法页仍运行1,730题十选项；HF于2026-10-04修正选项及缺失条件。Vals于9月1日保留榜，但现已停止新模型评测，不能写成仍持续更新。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）；[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

## 基本信息

### 简称

MMMU-Pro

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 全称

MMMU-Pro

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 基准版本

Pro（数据修订截至2026-10-04）

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 论文版本

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 发布日期

2024-09-05（数据卡首发）

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 主板块

多模态

> 编辑归档，不代表官方分类。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 领域标签

```json
[
  "科学视觉推理"
]
```

> 编辑归档，不代表官方分类。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 许可证

Apache-2.0（HF数据卡）；原始素材版权依源站，版权反馈后可移除。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 论文

https://arxiv.org/abs/2409.02813

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 官方代码

https://github.com/MMMU-Benchmark/MMMU

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 数据地址

https://huggingface.co/datasets/MMMU/MMMU_Pro

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 官方入口

https://huggingface.co/datasets/MMMU/MMMU_Pro

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 论文标题

MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

## 发起与维护

### 发起机构

MMMU Team

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 合作方

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 作者

Xiang Yue、Tianyu Zheng、Yuansheng Ni、Yubo Wang、Kai Zhang、Shengbang Tong、Yuxuan Sun、Botao Yu、Ge Zhang、Huan Sun、Yu Su、Wenhu Chen、Graham Neubig

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 维护方

MMMU Team

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 资助

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

## 设计目标

### 衡量能力

跨学科视觉理解、知识推理和图文整合；要求真正利用图片，而不只依赖选项或文本捷径。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 设计背景

原版 MMMU 的部分题目不看图也能答对，四选一又容许猜测。Pro通过过滤、扩展选项与纯视觉输入收紧评测。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

## 构建方式

### 题目来源

从原版MMMU过滤纯文本模型可答题；四个文本模型各重复十次，筛去至少三个模型多数答对的题；抽取1,800题后经选项与图像相关性复核，保留1,730题。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 出题者背景

选项扩展及复核由领域专家参与；具体每人学历待核实。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 审核流程

GPT-4o生成额外选项、Claude 3.5过滤，再经两轮人工复核；截图和照片由人工在不同显示背景、字体与字号下采集。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 质量控制

GPT-4o生成额外选项、Claude 3.5过滤，再经两轮人工复核；截图和照片由人工在不同显示背景、字体与字号下采集。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 去污染

过滤纯文本捷径不能证明无训练污染；公开题集仍存在记忆风险。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

## 数据形式

### 题量与规模

1,730个底层问题；standard (4 options)、standard (10 options)、vision三个配置各1,730行，合计5,190配置行不是5,190道独立问题。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 题型

学科多项选择；Standard文本配图、Vision将问题与选项嵌入图像。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 模态

```json
[
  "文本",
  "图像"
]
```

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 语言

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 难度

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 公开与隐藏划分

HF三个配置均为test split；样本id保留原版validation/test来源，不等于新增训练划分。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

## 评测方法

### 指标

准确率；论文总体分为Standard 10选项与Vision准确率的平均，Standard 4选项仅作对照。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 评分

抽取选择答案并与参考标签比较；不能把四选项成绩当Pro十选项/Vision综合成绩。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 提示与运行设置

论文比较Direct与CoT并取较优；AA单列1,730题十选项、一次运行、正则抽取pass@1。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 官方评测脚本

https://github.com/MMMU-Benchmark/MMMU

> 链接由已打开原始论文/数据卡指向；本轮未逐文件核验代码。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 可比性警示

Vals使用Standard 4选项；AA使用10选项；原论文综合还包含Vision，三个口径不可直接混排。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 当前版本与2026H2证据

```json
{
  "version": "Pro（数据修订截至2026-10-04）",
  "trending": "A",
  "heat_evidence": "AA当前方法页仍运行1,730题十选项；HF于2026-10-04修正选项及缺失条件。Vals于9月1日保留榜，但现已停止新模型评测，不能写成仍持续更新。",
  "evidence_2026_h2": [
    {
      "url": "https://huggingface.co/datasets/MMMU/MMMU_Pro",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    },
    {
      "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    },
    {
      "url": "https://www.vals.ai/benchmarks/mmmu",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。"
    }
  ]
}
```

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）；[来源](https://artificialanalysis.ai/methodology/intelligence-benchmarking)（访问2026-11-07）；[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

### 修订历史

HF 2026-10-04修正test_Chemistry_240选项扩展及validation_Finance_5缺失条件。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 饱和情况

Vals明确称该实现已饱和并停止对新模型运行；不外推到AA十选项或Pro Vision。

[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

### 污染与争议

Vals使用Standard 4选项；AA使用10选项；原论文综合还包含Vision，三个口径不可直接混排。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 版本与衍生关系

本页只收MMMU-Pro；原版保留在既有条目 /benchmarks/mmmu，Pro为其防捷径增强衍生版，不能用原版11.5K题量填入本页。

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

### 官方榜单

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 第三方覆盖

https://www.vals.ai/benchmarks/mmmu

[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

### 结构化结果

```json
[
  {
    "rank": 1,
    "model": "Claude Fable 5.1",
    "score": 90.64,
    "metric": "Vals Standard 4选项准确率 (%)；历史保留榜",
    "source_url": "https://www.vals.ai/benchmarks/mmmu",
    "source_date": "2026-09-01",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 2,
    "model": "Claude Opus 5",
    "score": 89.88,
    "metric": "Vals Standard 4选项准确率 (%)；历史保留榜",
    "source_url": "https://www.vals.ai/benchmarks/mmmu",
    "source_date": "2026-09-01",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  },
  {
    "rank": 3,
    "model": "Claude Fable 5",
    "score": 89.31,
    "metric": "Vals Standard 4选项准确率 (%)；历史保留榜",
    "source_url": "https://www.vals.ai/benchmarks/mmmu",
    "source_date": "2026-09-01",
    "collected_at": "2026-11-07 KST",
    "result_type": "页面榜表快照",
    "rank_type": "所列协议下顺序"
  }
]
```

[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

### 时效与覆盖说明

Vals使用Standard 4选项；AA使用10选项；原论文综合还包含Vision，三个口径不可直接混排。 榜表自写更新时间：2026-09-01；采集日不等于运行日。

[来源](https://www.vals.ai/benchmarks/mmmu)（访问2026-11-07）

## 联系方式

### 官方公开工作邮箱

xiangyue.work@gmail.com

[来源](https://arxiv.org/abs/2409.02813)（访问2026-11-07）

### 公开反馈渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 官方社交渠道

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 隐私政策

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

## 原始文件

### 源站原始论文PDF

https://arxiv.org/pdf/2409.02813

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2409.02813)（访问2026-11-07）

### PDF SHA-256

f833d6273318d53487ace892ed54289216f5d6034fcf37af2499146d12860f5b

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2409.02813)（访问2026-11-07）

### PDF字节数

17320142

> 本轮直接读取原始PDF字节核验；未上传Drive。

[来源](https://arxiv.org/pdf/2409.02813)（访问2026-11-07）

### Drive资料文件夹

待核实

> 本轮所列已打开材料未完成精确核验；不代表官方未公开。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "type": "已打开官方网页/论文",
    "url": "https://huggingface.co/datasets/MMMU/MMMU_Pro"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://arxiv.org/abs/2409.02813"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://artificialanalysis.ai/methodology/intelligence-benchmarking"
  },
  {
    "type": "已打开官方网页/论文",
    "url": "https://www.vals.ai/benchmarks/mmmu"
  }
]
```

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### Drive PDF归档

待核实；本轮未上传。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立近期热门中文研究条目。本页只收MMMU-Pro；原版保留在既有条目 /benchmarks/mmmu，Pro为其防捷径增强衍生版，不能用原版11.5K题量填入本页。 热度与榜单口径分离，不确定值标记待核实。"
  }
]
```

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro)（访问2026-11-07）

### 口径补充来源

三个配置各1,730行、test划分与Apache-2.0元数据以HF原始卡片为准。

[来源](https://huggingface.co/datasets/MMMU/MMMU_Pro/raw/main/README.md)（访问2026-11-07）
