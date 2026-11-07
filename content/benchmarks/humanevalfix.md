# HumanEvalFix

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；采集日不等于运行日，历史榜单、研究复测与独立评测分别记录。

## 基本信息

### 简称

HumanEvalFix

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 全称

HumanEvalFix

> 保留官方名称，不把论文标题自动扩写为全称。

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 基准版本

HumanEvalPack 中的 HumanEvalFix；6语言×164题

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 论文版本

arXiv v2

> 论文修订版本不等同数据集版本。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 发布日期

2023-08-14 22:53:54 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 主板块

代码

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 领域标签

代码修复

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 许可证

MIT；OctoPack官方明确将HumanEvalPack和全部代码纳入本仓库MIT许可，而非只标代码。CommitPack/CommitPackFT样本另有原仓库许可，不应混用。

来源：[https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07 KST）

### 论文

https://arxiv.org/abs/2308.07124

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 官方代码

https://github.com/bigcode-project/octopack

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 数据地址

https://huggingface.co/datasets/bigcode/humanevalpack

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 官方入口

https://github.com/bigcode-project/octopack

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 论文标题

OctoPack: Instruction Tuning Code Large Language Models

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 发起与维护

### 机构与发起方

BigCode / OctoPack 作者团队

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 合作方

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 作者

Muennighoff, Niklas、Liu, Qian、Zebaze, Armel、Zheng, Qinkai、Hui, Binyuan、Zhuo, Terry Yue、Singh, Swayam、Tang, Xiangru、von Werra, Leandro、Longpre, Shayne

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 当前维护方

BigCode octopack 项目

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 资助

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 设计目标

### 衡量能力

根据任务规范和已有带错误的程序修复功能错误；测量指令微调代码模型。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 设计背景

代码补全只覆盖合成，缺少跨语言指令驱动修复与解释任务。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 构建方式

### 题目来源

在每种语言的 164 个 HumanEval 参考函数中人工加入一个 bug，跨语言尽量保持同类错误。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 出题者背景

论文团队人工设计 bug，而非由模型自动判定修复真值。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 审核流程

从HumanEval-X各语言解答JSON开始，人工并行向各语言引入bug；修正HumanEval-X问题并记录，转为带bug解答、instruction及元数据的JSONL上传HumanEvalPack。

来源：[https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07 KST）

### 质量控制

六种语言使用相近 bug 以支持可比性；附录给出类别与实例。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 去污染

源自公开 HumanEval；添加人工错误不消除模型记忆原始正确实现的可能性。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 数据形式

### 题量与规模

每语言 164 个问题，6 语言共 984 个 bug；不等于 984 个互不相关原题。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 题型

自然语言+错误代码 → 修复代码；tests 与 docstring 提示有不同变体。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 模态

文本、源代码

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 语言

Python、JavaScript、Java、Go、C++、Rust

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 难度

细微功能 bug；文档提示的较易变体与只给测试的变体须区分。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 公开与隐藏划分

通过 HumanEvalPack 公开；Fix、Explain、Synthesize 是同套件不同任务。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 评测方法

### 指标

执行测试的 pass@1 等；按语言分别报告。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 评分

修复代码必须通过参考测试，不以自然语言解释质量代替功能正确。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 提示与运行设置

区分humanevalfixtests（给测试、不含docstring，论文主设置）与humanevalfixdocs（给docstring）；官方示例temperature=0.2、n_samples=20、batch_size=5、max_length_generation=2048。

来源：[https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07 KST）

### 官方评测脚本

https://github.com/bigcode-project/octopack

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 可比性警示

必须分语言及fixdocs/fixtests协议比较；官方说明Python版本和batch_size影响随机性，论文使用Python3.9.13、batch_size=5；执行不可信生成代码应隔离。

来源：[https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md](https://raw.githubusercontent.com/bigcode-project/octopack/main/README.md)（访问 2026-11-07 KST）

## 最新情况

### 核查日期

2026-11-07 KST / Asia/Seoul

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "HumanEvalPack 中的 HumanEvalFix；6语言×164题",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §3.3、附录11.1实际用 HumanEvalFix JavaScript 等代码修复任务评测科学轨迹训练迁移。"
    }
  ]
}
```

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[https://arxiv.org/html/2609.19134v1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07 KST）；[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 论文修订历史

Submission history From: Niklas Muennighoff [ view email ] [v1] 2023-08-14 22:53:54 KST (1,643 KB) [v2] 2024-02-18 18:46:06 KST (1,647 KB)

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 饱和情况

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 污染与争议

HumanEval 改编造成原题记忆与修复能力混合，跨语言一致 bug 也不是完全独立样本。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 衍生与版本关系

HumanEvalExplain 与 HumanEvalSynthesize 是 HumanEvalPack 兄弟任务；本条仅收 HumanEvalFix。

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 官方榜单

https://github.com/bigcode-project/octopack

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 独立评测覆盖

待核实

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

核验状态：待核实

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 核验结果

```json
[
  {
    "model": "ScienceIDE 4B SFT 训练设置（精确检查点待核实）",
    "result": "HumanEvalFix JavaScript 相对提升 10.98 个百分点",
    "metric": "论文报告相对改善，不是绝对得分",
    "benchmark_version": "HumanEvalFix JS",
    "result_type": "H2 学术实验",
    "source_date": "2026-09-16",
    "collected_at": "2026-11-07 KST"
  }
]
```

核验状态：待核实

来源：[https://arxiv.org/html/2609.19134v1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07 KST）

### 覆盖与时效说明

ScienceIDE §3.3 与附录 11.1 实际使用 JS 修复；不将相对提升填成 pass@1 绝对值，当前官方全语言榜首待核实。

核验状态：待核实

来源：[https://arxiv.org/html/2609.19134v1](https://arxiv.org/html/2609.19134v1)（访问 2026-11-07 KST）

## 联系方式

### 公开工作邮箱

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 公开反馈

https://github.com/bigcode-project/octopack/issues

> 公开仓库反馈入口；未发送问题。

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）

### 官方社交渠道

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

### 隐私政策

待核实

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

核验状态：待核实

来源：[https://arxiv.org/abs/2308.07124](https://arxiv.org/abs/2308.07124)（访问 2026-11-07 KST）

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/2308.07124

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[https://arxiv.org/pdf/2308.07124](https://arxiv.org/pdf/2308.07124)（访问 2026-11-07 KST）

### 原始PDF SHA-256

c03f04d06e000e4a251bea07c8b654721a97dbf23009ba45909439c7d814502a

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2308.07124](https://arxiv.org/pdf/2308.07124)（访问 2026-11-07 KST）

### 原始PDF字节数

2618401

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

来源：[https://arxiv.org/pdf/2308.07124](https://arxiv.org/pdf/2308.07124)（访问 2026-11-07 KST）

### Drive资料文件夹

```json
{
  "id": "1xXVcvs2QJOirQEtIZUomvCncd0wm0nkK",
  "webViewLink": "https://drive.google.com/drive/folders/1xXVcvs2QJOirQEtIZUomvCncd0wm0nkK"
}
```

来源：[https://drive.google.com/drive/folders/1xXVcvs2QJOirQEtIZUomvCncd0wm0nkK](https://drive.google.com/drive/folders/1xXVcvs2QJOirQEtIZUomvCncd0wm0nkK)（访问 2026-11-07 KST）

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1VdSi5h_gTRKSEqG_HYOcUmV6YHox8eeex48YUrwHtUY",
    "webViewLink": "https://docs.google.com/document/d/1VdSi5h_gTRKSEqG_HYOcUmV6YHox8eeex48YUrwHtUY/edit?usp=drivesdk"
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）；[https://docs.google.com/document/d/1VdSi5h_gTRKSEqG_HYOcUmV6YHox8eeex48YUrwHtUY/edit?usp=drivesdk](https://docs.google.com/document/d/1VdSi5h_gTRKSEqG_HYOcUmV6YHox8eeex48YUrwHtUY/edit?usp=drivesdk)（访问 2026-11-07 KST）

### Drive 原始 PDF

```json
{
  "id": "10-4Bu_ewHurkjd6393FPJH4XwOO8jXtn",
  "webViewLink": "https://drive.google.com/file/d/10-4Bu_ewHurkjd6393FPJH4XwOO8jXtn/view?usp=drivesdk"
}
```

来源：[https://drive.google.com/file/d/10-4Bu_ewHurkjd6393FPJH4XwOO8jXtn/view?usp=drivesdk](https://drive.google.com/file/d/10-4Bu_ewHurkjd6393FPJH4XwOO8jXtn/view?usp=drivesdk)（访问 2026-11-07 KST）

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  },
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "第1轮深度优化续核：打开官方README/数据卡/榜单核对许可、协议及划分；保留既有H2证据和历史成绩，区分采集日与运行日；介绍页同步。"
  }
]
```

来源：[https://github.com/bigcode-project/octopack](https://github.com/bigcode-project/octopack)（访问 2026-11-07 KST）
