# MMMLU

> 核验日期：2026-11-08（KST / Asia/Seoul，UTC+9）。未知不补造；来源访问日不等于实验运行日。

OpenAI将MMLU测试题以专业人工翻译扩展到14个非英语语种，核心用途是比较同类学科知识的跨语言可用性，而非重新出一道更难的MMLU题库。本次固定HF commit下载全部14个CSV：每个语种14042行、57学科，总计196588条译文。HF查看器393176的聚合计数重复包含default与各语种配置，不能当作独立题数。
[本页导读依据](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

## 基本信息

### 简称

MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 全称

Multilingual Massive Multitask Language Understanding

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 数据/基准版本

```json
{
  "release_name": "MMMLU（未单列语义版本号）",
  "hf_revision": "325a01dc3e173cac1578df94120499aaca2e2504"
}
```

[来源1](https://huggingface.co/api/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### 论文版本

所链接的是MMLU母题论文arXiv v3（2021-01-13 03:57:11 KST）；MMMLU独立论文及版本待核实。

> 状态：待核实。

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### 发布日期

HF仓库创建于2024-09-14 01:37:19 KST；这不是已确认的MMMLU正式首发时间，正式发布日期待核实。

> 状态：待核实。

[来源1](https://huggingface.co/api/datasets/openai/MMMLU)（访问 2026-11-08）

### 主板块

语言

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 子领域

多语言多学科知识

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 许可边界

MIT（OpenAI 官方数据集卡声明）

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2009.03300

> 这是母题MMLU论文链接，不证明MMMLU独立论文存在。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）

### 代码入口

https://github.com/openai/simple-evals

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 数据入口

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 官方主页

https://huggingface.co/datasets/openai/MMMLU

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 论文标题

母题论文：Measuring Massive Multitask Language Understanding；MMMLU独立论文待核实。

> 状态：待核实。

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## 发起与维护

### 发起方

OpenAI 官方数据集。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 合作机构

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 作者

数据发布署名OpenAI；数据卡未列出各译者或MMMLU独立论文作者名单，个人名单待核实。

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### 当前维护方

OpenAI（官方数据发布命名空间 openai/MMMLU）

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 资助

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## 设计目标

### 衡量能力

通过专业人工翻译检验多语言的一般知识能力，尤其关注低资源语言翻译质量。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 设计动机

只测英语无法反映跨语言表现；机器翻译题的质量可能影响低资源语种测评。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## 构建方式

### 题目来源

原始 MMLU 测试集的14种语言专业人工翻译，覆盖原MMLU的57学科。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 出题/构建者背景

由专业人工译者翻译 MMLU 测试集，不是机器翻译版本。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 审核流程

专业人工翻译，官方称其可提高低资源语言翻译准确性的可信度；逐题复核及双盲审校流程待核实。

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### 质量控制

人工译文覆盖同一MMLU测试任务；本次文件核查每语种均14042行、57学科。空名索引列在各学科内重复，不能作为全局题目ID；SW-KE、YO-NG与AR-XY的学科/索引顺序并不完全一致，逐题配对前须核对原题而非直接按行号连接。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv)（访问 2026-11-08）；[来源4](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv)（访问 2026-11-08）

### 去污染/泄漏控制

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## 数据形式

### 精确规模与统计口径

```json
{
  "base_test_items_per_locale": 14042,
  "translated_locales": 14,
  "total_translation_rows": 196588,
  "subjects_per_locale": 57,
  "hf_viewer_aggregate_rows": 393176,
  "count_method": "逐个下载同一HF revision的14个CSV，csv.DictReader与pandas.read_csv分别核对；default配置汇总所有语言，viewer再计各语言配置，393176不代表独立题量。"
}
```

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/api/datasets/openai/MMMLU)（访问 2026-11-08）；[来源3](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv)（访问 2026-11-08）；[来源4](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_BN-BD.csv)（访问 2026-11-08）；[来源5](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_DE-DE.csv)（访问 2026-11-08）；[来源6](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ES-LA.csv)（访问 2026-11-08）；[来源7](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_FR-FR.csv)（访问 2026-11-08）；[来源8](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_HI-IN.csv)（访问 2026-11-08）；[来源9](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ID-ID.csv)（访问 2026-11-08）；[来源10](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_IT-IT.csv)（访问 2026-11-08）；[来源11](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_JA-JP.csv)（访问 2026-11-08）；[来源12](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_KO-KR.csv)（访问 2026-11-08）；[来源13](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_PT-BR.csv)（访问 2026-11-08）；[来源14](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv)（访问 2026-11-08）；[来源15](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv)（访问 2026-11-08）；[来源16](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ZH-CN.csv)（访问 2026-11-08）

### 题型

四选一知识题

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 模态

文本

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 语言/代码语种

阿拉伯语；孟加拉语；德语；西班牙语；法语；印地语；印度尼西亚语；意大利语；日语；韩语；巴西葡萄牙语；斯瓦希里语；约鲁巴语；简体中文

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 难度结构

沿用 MMLU，从基础到专业学科；翻译不是新难度等级。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 公开与隐藏划分

官方卡列出14个语言配置，均为公开test/*.csv测试文件；不将这些test文件当训练集。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## 评测方法

### 指标

选择题准确率，需标明语言与跨语种汇总方法。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 评分规则

回答归一化后用多语言答案正则抽取字母，匹配Answer列计1，否则0；同一语种以样本级分数聚合。跨语言如何再汇总须另行声明。

[来源1](https://github.com/openai/simple-evals/blob/main/mmlu_eval.py)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/common.py)（访问 2026-11-08）

### 运行与提示设置

官方MMLUEval(language=...)载入对应语种CSV；单题zero-shot CoT，要求最后一行Answer: A/B/C/D；language默认EN-US，跑翻译集必须显式指定语言。num_examples抽样使用Random(0)。

[来源1](https://github.com/openai/simple-evals/blob/main/mmlu_eval.py)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/common.py)（访问 2026-11-08）；[来源3](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）

### 官方评测脚本

https://github.com/openai/simple-evals

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### 可比性警示

MMMLU 是 OpenAI 对 MMLU 的专业人工翻译数据集，不是 MMLU-ProX；14 个翻译语种不应被误写为包含原英语的14语种。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

## 最新情况

### 本轮核验日期

2026-11-08

> 本次源站访问日期；时区KST / Asia/Seoul；不等于榜单运行日期。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "hf_revision": "325a01dc3e173cac1578df94120499aaca2e2504",
  "last_modified_kst": "2024-10-17T03:39:00+09:00",
  "scope": "HF公开MMMLU译文，不是新MMLU版本"
}
```

[来源1](https://huggingface.co/api/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "scope": "MMLU母题论文修订，不冒称MMMLU独立论文",
  "revisions": [
    {
      "version": "v1",
      "date_kst": "2020-09-08T02:59:25+09:00"
    },
    {
      "version": "v2",
      "date_kst": "2020-09-21T14:06:57+09:00"
    },
    {
      "version": "v3",
      "date_kst": "2021-01-13T03:57:11+09:00"
    }
  ],
  "mmmlu_repository_last_modified_kst": "2024-10-17T03:39:00+09:00"
}
```

[来源1](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源2](https://huggingface.co/api/datasets/openai/MMMLU)（访问 2026-11-08）

### 饱和性证据

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 污染与已知争议

人工翻译不等于原题去污染。HF卡展示的393176是配置聚合计数，不能当作原始题量；simple-evals自2025年7月停止更新新模型/成绩，其英语MMLU表格不能当作MMMLU多语言榜。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源2](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）

### 衍生与条目关系

MMMLU是MMLU的14语种人工翻译发布；不与MMLU-ProX、Global-MMLU或英语MMLU混为同一版本。

[来源1](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）

## 榜单快照

### 本次榜单采集日

2026-11-08

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 官方榜源

https://huggingface.co/datasets/openai/MMMLU

> 未有已核实实时榜时提供原始论文/数据卡结果入口；不宣称是实时排行榜。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 第三方覆盖

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Jev研究表2：本研究复测组／14语种MMMLU

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Gemini 3.8 Flash | 92.6 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 2 | Qwen3.8-Max | 90.3 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 3 | DeepSeek-V4.1-Flash | 88.8 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 4 | Qwen3.8-Flash | 88.3 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 5 | Claude Opus 5.5 | 87.2 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 6 | GPT-5.6 Sol | 85.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |
| 6 | Jev | 85.0 % | accuracy | 未逐项给出 | [原始来源](https://arxiv.org/html/2610.11978v1)（2026-11-08） |

- 有限答案选择；每模型单次运行；按原论文模型标签保留

- 第三方研究复测；非OpenAI官方统一榜

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）

### 覆盖范围与限制

已回读Jev表2并扩展为7个本研究实测条目；代表/小模型部分引用异协议历史成绩，未并入此赛道。官方HF卡未给出统一实时榜，simple-evals中的英语MMLU成绩不挪作MMMLU。

[来源1](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源3](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）

## 联系方式

### 公开研究邮箱

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 项目反馈入口

https://github.com/openai/simple-evals/issues

[来源1](https://github.com/openai/simple-evals)（访问 2026-11-07）

### 官方公开社交入口

待核实

> 状态：待核实。

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）

### 公开渠道/隐私边界

只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问 2026-11-07）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2009.03300

> PDF已重下载读文并验证hash一致；该Drive存档是MMLU母题论文，不标为MMMLU独立论文。

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF SHA-256

d3a7b0f8589f5365ebfd34a3876a9a8b3fde83e0adb9ed19ccf8f0034bb48fc1

> 原始下载字节SHA-256；未压缩或改写。

[来源1](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### PDF字节数

2074939

[来源1](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）

### Drive文件夹

```json
{
  "id": "1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC",
  "webViewLink": "https://drive.google.com/drive/folders/1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC"
}
```

[来源1](https://drive.google.com/drive/folders/1OPPheSgFyaAe2V-nV5RJwvz34TO4r8qC)（访问 2026-11-07）

### 其他官方文档

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g",
    "webViewLink": "https://docs.google.com/document/d/1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g/edit?usp=drivesdk"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/abs/2009.03300",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/html/2610.11978v1",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/pdf/2009.03300",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/openai/simple-evals/blob/main/README.md",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/openai/simple-evals/blob/main/common.py",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/openai/simple-evals/blob/main/mmlu_eval.py",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/api/datasets/openai/MMMLU",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_BN-BD.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_DE-DE.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ES-LA.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_FR-FR.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_HI-IN.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ID-ID.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_IT-IT.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_JA-JP.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_KO-KR.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_PT-BR.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ZH-CN.csv",
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://docs.google.com/document/d/1UZFDALJVykwbz968O2R0VZ8cHhmZ_j10e9qps5hcB_g/edit?usp=drivesdk)（访问 2026-11-07）；[来源2](https://arxiv.org/abs/2009.03300)（访问 2026-11-08）；[来源3](https://arxiv.org/html/2610.11978v1)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2009.03300)（访问 2026-11-08）；[来源5](https://github.com/openai/simple-evals/blob/main/README.md)（访问 2026-11-08）；[来源6](https://github.com/openai/simple-evals/blob/main/common.py)（访问 2026-11-08）；[来源7](https://github.com/openai/simple-evals/blob/main/mmlu_eval.py)（访问 2026-11-08）；[来源8](https://huggingface.co/api/datasets/openai/MMMLU)（访问 2026-11-08）；[来源9](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）；[来源10](https://huggingface.co/datasets/openai/MMMLU/raw/main/README.md)（访问 2026-11-08）；[来源11](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_AR-XY.csv)（访问 2026-11-08）；[来源12](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_BN-BD.csv)（访问 2026-11-08）；[来源13](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_DE-DE.csv)（访问 2026-11-08）；[来源14](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ES-LA.csv)（访问 2026-11-08）；[来源15](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_FR-FR.csv)（访问 2026-11-08）；[来源16](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_HI-IN.csv)（访问 2026-11-08）；[来源17](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ID-ID.csv)（访问 2026-11-08）；[来源18](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_IT-IT.csv)（访问 2026-11-08）；[来源19](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_JA-JP.csv)（访问 2026-11-08）；[来源20](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_KO-KR.csv)（访问 2026-11-08）；[来源21](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_PT-BR.csv)（访问 2026-11-08）；[来源22](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_SW-KE.csv)（访问 2026-11-08）；[来源23](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_YO-NG.csv)（访问 2026-11-08）；[来源24](https://huggingface.co/datasets/openai/MMMLU/resolve/325a01dc3e173cac1578df94120499aaca2e2504/test/mmlu_ZH-CN.csv)（访问 2026-11-08）

### Drive原始PDF

```json
{
  "id": "10nTX-hZcL0fXPaatAK5f_f47-_-daG2g",
  "webViewLink": "https://drive.google.com/file/d/10nTX-hZcL0fXPaatAK5f_f47-_-daG2g/view?usp=drivesdk"
}
```

> 所附为数据卡引用的 MMLU 原始论文，非 MMMLU 独立论文。

[来源1](https://drive.google.com/file/d/10nTX-hZcL0fXPaatAK5f_f47-_-daG2g/view?usp=drivesdk)（访问 2026-11-07）

## 变更记录

### 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "第一轮深度优化：重读官方仓库、数据卡及H2使用论文；补许可、维护入口、版本与评测口径；区分历史榜与实时榜，并保留文档日期冲突。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST, UTC+9)",
    "change": "第二轮深度复核：重读官方数据卡、README/许可、可用论文abs与PDF及官方榜；补精确题量、修订边界与完整可读成绩；区分私有集、历史基线、厂商自报与独立测评。"
  }
]
```

[来源1](https://huggingface.co/datasets/openai/MMMLU)（访问 2026-11-08）
