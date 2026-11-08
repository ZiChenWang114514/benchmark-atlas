# SWE-bench Multimodal

> Benchmark Constitution，深度复核 2026-11-08。

SWE-bench Multimodal把视觉软件issue修复纳入仓库级agent评测，图像不只是装饰输入。官网2026年v2保留480可复现任务，但原论文、项目历史介绍和当前HF卡对旧题量仍存在多套数字。本档并列这些证据并提醒锁定revision，不能把HF main和480题协议自动视为完全一致。

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源2](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

## 基本信息

### 简称

SWE-bench Multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 全称

SWE-bench Multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 基准版本

Multimodal v2

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 论文版本

v1（论文版本；不等于数据集版本）

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 发布日期

2026-09-01（Multimodal v2）

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 主板块

代码

> 编辑归档；跨领域只计主板块。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 领域

```json
[
 "多模态"
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 许可与适用范围

官方harness代码MIT（LICENSE已打开）；任务、补丁及视觉资产涉及17个上游仓库和原作者版权，不能只因harness MIT就断言全部素材MIT。

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/LICENSE)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）

### 论文

https://arxiv.org/abs/2410.03859

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 官方代码

https://github.com/SWE-bench/SWE-bench

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

### 数据

https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal

[来源1](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源2](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

### 官方入口

https://www.swebench.com/multimodal.html

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 论文标题

SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

## 发起与维护

### 发起方

Stanford University与Princeton University研究团队

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 合作/参与机构

论文作者单位包括Stanford、Princeton、Cornell、Tübingen AI Center及Meta AI；不是全部作者均来自前两校。

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 作者

```json
[
 "John Yang"
 "Carlos E. Jimenez"
 "Alex L. Zhang"
 "Kilian Lieret"
 "Joyce Yang"
 "Xindi Wu"
 "Ori Press"
 "Niklas Muennighoff"
 "Gabriel Synnaeve"
 "Karthik R. Narasimhan"
 "Diyi Yang"
 "Sida I. Wang"
 "Ofir Press"
]
```

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 维护方

Stanford University与Princeton University研究团队

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 资助

Open Philanthropy、Oracle与NSF Grant No. 2239363（原始论文致谢）；实验由Stanford与Princeton作者在Princeton服务器执行，Meta作者为顾问角色。

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

## 设计目标

### 衡量能力

利用截图或短录屏理解真实JavaScript仓库问题，定位并修复代码。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 设计背景

纯文本SWE-bench不能覆盖图表、界面、语法高亮等视觉证据决定需求的场景。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 构建方式

### 题目来源

从真实仓库视觉issue扩展SWE-bench；v2移除已知不稳定或不可评分测试，重建Docker环境与视觉资产处理。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 出题者背景

研究团队从真实JavaScript/TypeScript issue–PR对构建任务；论文以人工专家验证视觉必要性，对83.5%实例判断图像是解题必要信息。

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 审核流程

原始流水线筛选带视觉内容的issue或测试，构建JavaScript容器与可执行测试，再做人类专家视觉必要性审查；2026-09-01 v2进一步剔除flaky/ungradeable实例。

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源2](https://www.swebench.com/multimodal.html)（访问 2026-11-08）

### 质量控制

v2剔除flaky/ungradeable测试并重建环境，解决依赖和browser drift。

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 污染控制

实例id包含上游修复PR号，有联网查答案风险；Vals全程禁网络并提前下载视觉素材。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 数据形式

### 题量

v2官网保留480任务（Vals方法称11仓库）；官网历史介绍517视觉issue。arXiv v1摘要617、正文引言619；当前HF卡又称612=dev102+test510、17仓库，viewer显示580行。上述版本/页面统计互不等价，v2题量以官网480为准，HF具体revision映射待核实。

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源3](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 任务形式

issue文本与图像输入，输出代码diff。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 模态

```json
[
 "文本"
 "图像"
 "代码"
]
```

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 语言

代码：JavaScript/TypeScript，含HTML/CSS；issue以英语为主也含中文，官方HF卡说明未按语言清洗。

[来源1](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 难度

真实前端与视觉软件修复，不能靠文本需求完全替代视觉证据；论文原始SWE-agent解决率12.2%，是旧版历史轨而非480题v2当前成绩。

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 公开与隐藏划分

v2官网说明完整test split与tooling开源；官方README指向HF地址，但当前HF卡仍描述旧dev102/test510且viewer总580，与v2 480不一致，必须固定数据revision/实例清单后再复现，不能默认HF main正好480。

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源3](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

## 评测方法

### 指标

测试判定issue解决正确率（Accuracy）。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 评分

Vals以mini-swe-agent单次运行，预下载截图附到首条消息；上游harness按仓库自身测试判定修复成功。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 运行设置

mini-swe-agent；issue文本、首轮附截图、shell与独立sandbox；每模型每题运行一次，误差条为二项标准误。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 评测工具

官方SWE-bench harness支持swebench eval multimodal，也保留python -m swebench.harness.run_evaluation；HF卡提供dataset_name、split=test和gold patch回归校验命令。

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）

### 可比性

与已有swe-bench-verified是同系列不同任务域/模态，不是Verified同题新版；Vals关闭网络，不能与能查官方补丁的联网结果比较。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 最新情况

### 复核日期

2026-11-08

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 当前版本及历史热度证据

```json
{
 "version": "Multimodal v2"
 "evidence_2026_h2": [
 {
 "url": "https://www.vals.ai/benchmarks/swebench-multimodal"
 "date": "2026-11-05"
 "date_type": "source_calendar_date"
 "note": "Vals AI当前方法与榜单实际评测多模型；主要单一机构当前展示，不代表行业广泛采纳。"
 }
 ]
}
```

> 热度等级沿候选采用；只保留已打开、可核实证据。A不保证每一版都获多个机构独立复跑。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 修订历史

```json
[
 {
 "version": "v1"
 "submitted_at": "2024-10-05"
 }
]
```

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）

### 饱和与能力边界

Vals禁网v2当前最高70.21%，尚非满分；联网诊断最高77.92%不能用于替代正式禁网榜。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 风险与争议

联网可通过instance_id中的修复PR号查询答案。Vals诊断三组Muse模型联网成绩显著高于正式禁网成绩，诊断分不入正式榜。HF卡还提示少量Carbon无障碍测试需在线规则引擎而有独立于补丁的波动；当前HF卡和v2题量矛盾须锁revision。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）

### 系列与衍生关系

与已有swe-bench-verified属于同系列但输入模态和任务域不同，独立收Multimodal v2；原始517题现保留480可复现题。

> 已与existing_slugs清单去重；版本关系基于所列方法页，不把不同任务域当同题更新。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-08

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源2](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 官方入口

https://www.swebench.com/multimodal.html

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-08）

### 独立来源

https://www.vals.ai/benchmarks/swebench-multimodal

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 分来源与协议结果

#### Vals v2 / no network

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| 1 | Claude Opus 5.5 | 70.21 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 2 | Claude Fable 5.1 | 61.25 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 3 | Claude Sonnet 5.5 | 58.33 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 4 | Gemini 4 Argon | 56.04 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 5 | Wonder Full | 47.29 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 6 | DeepSeek V4.1 Flash | 46.46 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 7 | Wonder | 45.63 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 8 | Kimi K3 | 44.17 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 9 | Claude Haiku 5.5 | 43.96 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 10 | GPT-6.1 Sol | 43.54 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 11 | GPT-6 Astra | 43.33 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 12 | Muse Spark 1.3 Max | 43.13 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 13 | Inkling 2 Small | 43.13 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 14 | Grok 4.7 | 42.92 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 15 | Qwen 3.8 Max | 42.5 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 16 | MiMo V2.6 Pro | 41.25 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 17 | Gemini 3.8 Flash | 40.83 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 18 | Step 5 Preview | 40.83 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 19 | GPT-6 Luna | 37.5 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 20 | MiniMax-M3 | 33.33 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |
| 21 | Mistral Large 4 Preview | 33.13 | Accuracy (%) | {"source_date":"2026-11-05","harness":"mini-swe-agent"} |

#### Vals v2 / network diagnostic

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | Muse Spark 1.2 | 62.71 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 | 69.17 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 Max | 77.92 | Accuracy (%) | {"diagnostic":true} |

#### Vals v2 / no network paired diagnostic

| 名次 | 模型 / 配置 | 原始分数 | 指标 | 关键配置 |
|---|---|---|---|---|
| — | Muse Spark 1.2 | 41.25 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 | 42.08 | Accuracy (%) | {"diagnostic":true} |
| — | Muse Spark 1.3 Max | 43.33 | Accuracy (%) | {"diagnostic":true} |

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### 覆盖与时效

完整Vals正式禁网榜21行，另附三模型×联网/禁网诊断6行，诊断分与正式排名分轨。官方项目页当前可读正文没有独立实时分数，不把Vals标成原作者官方榜。2024论文历史分不冒充v2。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）；[来源2](https://www.swebench.com/multimodal.html)（访问 2026-11-08）

## 联系方式

### 公开工作邮箱

```json
[
 "johnby@stanford.edu"
 "carlosej@cs.princeton.edu"
]
```

[来源1](https://www.swebench.com/multimodal.html)（访问 2026-11-07）

### 官方反馈

https://github.com/SWE-bench/SWE-bench/issues

[来源1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)（访问 2026-11-08）

### 公开社区

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 隐私边界

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2410.03859

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

### PDF SHA-256

4fa09c3734547e8ba4a5288e7e8d9273d1136c70295e4f91ef3592df0ead2a71

> 本次实际下载的PDF字节计算；未上传。

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

### PDF字节数

```json
4379827
```

[来源1](https://arxiv.org/pdf/2410.03859)（访问 2026-11-08）

### 文件夹

待核实

> 已查所列官方材料，尚未完成本字段精确核验；不等于官方未公开。

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

### 其他材料

```json
[
 {
 "type": "官方方法或项目页"
 "url": "https://www.vals.ai/benchmarks/swebench-multimodal"
 "accessed": "2026-11-07"
 }
 {
 "type": "已打开一手材料"
 "url": "https://arxiv.org/abs/2410.03859"
 "accessed": "2026-11-08"
 }
 {
 "type": "已打开一手材料"
 "url": "https://github.com/SWE-bench/SWE-bench"
 "accessed": "2026-11-08"
 }
 {
 "type": "已打开一手材料"
 "url": "https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal"
 "accessed": "2026-11-08"
 }
]
```

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源2](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）

### PDF归档

待核实

[来源1](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-07）

## 变更记录

```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-08"
 最近复核
 }
]
```

[来源1](https://arxiv.org/abs/2410.03859)（访问 2026-11-08）；[来源2](https://github.com/SWE-bench/SWE-bench)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/SWE-bench/SWE-bench_Multimodal)（访问 2026-11-08）；[来源4](https://www.vals.ai/benchmarks/swebench-multimodal)（访问 2026-11-08）
