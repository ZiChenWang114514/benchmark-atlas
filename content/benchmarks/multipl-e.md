# MultiPL-E

> 核验日期：2026-11-08（KST / Asia/Seoul，UTC+9）。未知不补造；来源访问日不等于实验运行日。

MultiPL-E把HumanEval和MBPP的接口、说明与测试翻译到多种编程语言，功能正确性仍由编译及单元测试确定。原论文19语言的实验不能代表当前HF发布：数据卡最新列3.3版，修正Lua停止词问题；其HumanEval与MBPP目标语言配置数量也已不同。GitHub额外禁止机器学习训练，而HF标MIT，两种授权声明冲突仍显式保留。
[本页导读依据](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

[补充导读依据](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE)（访问 2026-11-08）

[补充导读依据](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

## 基本信息

### 简称

MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 全称

Multi-Programming Language Evaluation of Large Language Models of Code

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）

### 数据/基准版本

```json
{
  "hf_changelog_latest": "3.3",
  "hf_revision": "28441b6024e71d4a1c1c0f6bf171c935cd5a43f2",
  "scope": "当前HF数据发布；原论文19语言协议另列"
}
```

[来源1](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/api/datasets/nuprl/MultiPL-E)（访问 2026-11-08）

### 论文版本

arXiv v4

> 论文修订版本不等同数据集版本。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 发布日期

2022-08-17 20:16:52 KST

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 主板块

代码

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 子领域

多语言代码生成

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 许可边界

仓库：BSD 3-Clause with Machine Learning Restriction，第4条禁止训练用途；官方HF数据卡另标MIT。两种发布载体声明不一致，分别保留，不能据HF标签绕过仓库条款。

[来源1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/LICENSE)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 论文入口

https://arxiv.org/abs/2208.08227

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 代码入口

https://github.com/nuprl/MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 数据入口

https://huggingface.co/datasets/nuprl/MultiPL-E

[来源1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/README.md)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 官方主页

https://nuprl.github.io/MultiPL-E/

[来源1](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）

### 论文标题

MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## 发起与维护

### 发起方

以 Northeastern University 等多校研究人员组成的作者团队为主；详见论文作者单位。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 合作机构

待核实

> 状态：待核实。

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 作者

Cassano, Federico；Gouwar, John；Nguyen, Daniel；Nguyen, Sydney；Phipps-Costin, Luna；Pinckney, Donald；Yee, Ming-Ho；Zi, Yangtian；Anderson, Carolyn Jane；Feldman, Molly Q；Guha, Arjun；Greenberg, Michael；Jangda, Abhinav

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 当前维护方

nuprl / MultiPL-E 官方仓库团队

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 资助

论文致谢 NSF CCF-2052696 的部分支持。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## 设计目标

### 衡量能力

跨编程语言的函数级代码生成、编译与功能测试。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 设计动机

只评 Python 难以判断语言模型在其他编程语言中的迁移能力；逐语言手工造题成本高。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## 构建方式

### 题目来源

将 Python HumanEval 和 MBPP 的签名、类型、文档及测试翻译为其他语言；不翻译参考实现函数体。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 出题/构建者背景

编程语言与程序合成研究人员。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 审核流程

语言专用翻译器把规范与测试转成目标语言；以容器运行编译与测试。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 质量控制

编译器翻译签名、类型、doctest/测试而非参考函数体，容器内编译执行并设超时。当前HF 3.3修复Lua多余stop token；3.1.1修复TypeScript MBPP类型括号，3.0修复部分Scala prompts/tests并调整若干语言空白。

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源3](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）

### 去污染/泄漏控制

翻译不能保证去除 Python 原题污染；模型仍可能记忆语义或已公开译题。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## 数据形式

### 精确规模与统计口径

```json
{
  "paper_protocol": {
    "languages_including_python": 19,
    "multipl_humaneval_instances": 3059,
    "multipl_mbpp_instances": 7619,
    "note": "论文附录按161/401母题乘19语言计数；不代表当前所有HF配置。"
  },
  "current_hf": {
    "humaneval_target_language_configs": 24,
    "mbpp_target_language_configs": 23,
    "humaneval_rows": 3811,
    "mbpp_rows": 8856,
    "per_config": [
      {
        "config": "humaneval-adb",
        "test_rows": 157
      },
      {
        "config": "humaneval-clj",
        "test_rows": 161
      },
      {
        "config": "humaneval-cpp",
        "test_rows": 161
      },
      {
        "config": "humaneval-cs",
        "test_rows": 158
      },
      {
        "config": "humaneval-d",
        "test_rows": 156
      },
      {
        "config": "humaneval-dart",
        "test_rows": 157
      },
      {
        "config": "humaneval-elixir",
        "test_rows": 161
      },
      {
        "config": "humaneval-go",
        "test_rows": 154
      },
      {
        "config": "humaneval-hs",
        "test_rows": 156
      },
      {
        "config": "humaneval-java",
        "test_rows": 158
      },
      {
        "config": "humaneval-jl",
        "test_rows": 159
      },
      {
        "config": "humaneval-js",
        "test_rows": 161
      },
      {
        "config": "humaneval-lua",
        "test_rows": 161
      },
      {
        "config": "humaneval-ml",
        "test_rows": 155
      },
      {
        "config": "humaneval-php",
        "test_rows": 161
      },
      {
        "config": "humaneval-pl",
        "test_rows": 161
      },
      {
        "config": "humaneval-r",
        "test_rows": 161
      },
      {
        "config": "humaneval-rb",
        "test_rows": 161
      },
      {
        "config": "humaneval-rkt",
        "test_rows": 161
      },
      {
        "config": "humaneval-rs",
        "test_rows": 156
      },
      {
        "config": "humaneval-scala",
        "test_rows": 160
      },
      {
        "config": "humaneval-sh",
        "test_rows": 158
      },
      {
        "config": "humaneval-swift",
        "test_rows": 158
      },
      {
        "config": "humaneval-ts",
        "test_rows": 159
      },
      {
        "config": "mbpp-adb",
        "test_rows": 365
      },
      {
        "config": "mbpp-clj",
        "test_rows": 397
      },
      {
        "config": "mbpp-cpp",
        "test_rows": 397
      },
      {
        "config": "mbpp-cs",
        "test_rows": 386
      },
      {
        "config": "mbpp-d",
        "test_rows": 358
      },
      {
        "config": "mbpp-elixir",
        "test_rows": 397
      },
      {
        "config": "mbpp-go",
        "test_rows": 374
      },
      {
        "config": "mbpp-hs",
        "test_rows": 355
      },
      {
        "config": "mbpp-java",
        "test_rows": 386
      },
      {
        "config": "mbpp-jl",
        "test_rows": 390
      },
      {
        "config": "mbpp-js",
        "test_rows": 397
      },
      {
        "config": "mbpp-lua",
        "test_rows": 397
      },
      {
        "config": "mbpp-ml",
        "test_rows": 355
      },
      {
        "config": "mbpp-php",
        "test_rows": 397
      },
      {
        "config": "mbpp-pl",
        "test_rows": 396
      },
      {
        "config": "mbpp-r",
        "test_rows": 397
      },
      {
        "config": "mbpp-rb",
        "test_rows": 397
      },
      {
        "config": "mbpp-rkt",
        "test_rows": 397
      },
      {
        "config": "mbpp-rs",
        "test_rows": 354
      },
      {
        "config": "mbpp-scala",
        "test_rows": 396
      },
      {
        "config": "mbpp-sh",
        "test_rows": 382
      },
      {
        "config": "mbpp-swift",
        "test_rows": 396
      },
      {
        "config": "mbpp-ts",
        "test_rows": 390
      }
    ]
  },
  "warning": "语言翻译行不是独立新问题数；当前各语言排除项不同，勿将3.3数据量套进原论文实验。"
}
```

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 题型

函数级程序补全与单元测试。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 模态

文本；代码

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 语言/代码语种

原论文为Python加18种目标语言；当前HF卡实际列出24个HumanEval目标语言配置、23个MBPP目标语言配置。自然语言描述为英语，编程语言数量与自然语言语种不同。

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 难度结构

继承 HumanEval 与 MBPP，不解释为 19 个独立 benchmark。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 公开与隐藏划分

翻译器、提示、测试和执行框架公开；不同语言允许的题目并非完全相同。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

## 评测方法

### 指标

执行测试的 pass@k。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 评分规则

代码在目标语言容器内编译并运行；使用 pass@k 无偏估计。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 运行与提示设置

原论文每题 200 个样本；pass@1 温度 0.2，pass@10/100 温度 0.8。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 官方评测脚本

https://github.com/nuprl/MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 可比性警示

必须固定HF revision、子基准、语言列表、有效题数、温度、采样量与k。3.3修复会影响Lua结果，历史19语言、当前24/23配置与厂商8语言平均不能互换。官方GitHub含禁止训练条款，HF MIT标签不自动覆盖该限制。

[来源1](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源3](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE)（访问 2026-11-08）

## 最新情况

### 本轮核验日期

2026-11-08

> 本次源站访问日期；时区KST / Asia/Seoul；不等于榜单运行日期。

[来源1](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "version": "HF changelog 3.3",
  "hf_revision": "28441b6024e71d4a1c1c0f6bf171c935cd5a43f2",
  "last_modified_kst": "2025-07-15T19:43:47+09:00",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1/§4.2及表2–4实际报告 MultiPL-E；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。"
    }
  ]
}
```

[来源1](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/api/datasets/nuprl/MultiPL-E)（访问 2026-11-08）；[来源3](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "arxiv_revisions": [
    {
      "version": "v1",
      "date_kst": "2022-08-17T20:16:52+09:00"
    },
    {
      "version": "v2",
      "date_kst": "2022-08-19T10:12:49+09:00"
    },
    {
      "version": "v3",
      "date_kst": "2022-11-08T14:48:57+09:00"
    },
    {
      "version": "v4",
      "date_kst": "2022-12-19T19:30:12+09:00"
    }
  ],
  "dataset_changelog_latest": "3.3（Lua stop token修复）",
  "other_notable_fixes": [
    "3.2新增Ada",
    "3.1.1修复TypeScript MBPP类型括号",
    "3.1新增Dart",
    "3.0新增Clojure/Elixir/Haskell/OCaml及若干Scala修正"
  ],
  "date_warning": "HF卡这些语义版本标题没有逐项日期；不把API lastModified当作所有版本的发布日期。"
}
```

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源3](https://huggingface.co/api/datasets/nuprl/MultiPL-E)（访问 2026-11-08）

### 饱和性证据

待核实

> 状态：待核实。

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 污染与已知争议

权利冲突：官方GitHub LICENSE为带禁止机器学习训练条款的BSD衍生许可；官方HF卡license字段为MIT。应核实具体下载载体、版本及上游母题权利，不将其统一标成MIT。

[来源1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/LICENSE)（访问 2026-11-07）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

### 衍生与条目关系

MultiPL-HumanEval和MultiPL-MBPP是两条来源分支；当前README另推荐更难的Ag-LiveCodeBench-X及Agnostics论文。后者是不同任务来源，不当作MultiPL-E同题升级。

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）

## 榜单快照

### 本次榜单采集日

2026-11-08

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### 官方榜源

https://github.com/nuprl/MultiPL-E

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 第三方覆盖

https://huggingface.co/spaces/bigcode/multilingual-code-evals

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源2](https://huggingface.co/spaces/bigcode/multilingual-code-evals)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### Hunyuan报告表2 / Base / 0-shot / 八语言子集

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Hunyuan-A13B | 69.33 % | MultiPL-E（报告表2原指标，k未逐项明示） | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |
| 2 | Qwen3-A22B | 65.94 % | MultiPL-E（报告表2原指标，k未逐项明示） | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |
| 3 | Qwen2.5-72B | 60.5 % | MultiPL-E（报告表2原指标，k未逐项明示） | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |
| 4 | Hunyuan-Large-1116 | 59.13 % | MultiPL-E（报告表2原指标，k未逐项明示） | 未逐项给出 | [原始来源](https://arxiv.org/html/2609.27284v1)（2026-11-08） |

- Python/C++/Java/PHP/TypeScript/C#/Bash/JavaScript；数据revision与k未逐项明确

- 厂商报告比较，不是MultiPL-E官方统一实时榜

#### 原论文v4 §5.1 / MultiPL-HumanEval / Python

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | Codex | 45.9 % | pass@1 | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2208.08227)（2026-11-08） |
| 2 | CodeGen | 19.2 % | pass@1 | 未逐项给出 | [原始来源](https://arxiv.org/pdf/2208.08227)（2026-11-08） |

- 每题200样本；pass@1 temperature 0.2

- 论文正文明确给出的历史pass@1；非全语言总分

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### 覆盖范围与限制

回读Hunyuan表2完整4个Base模型八语言成绩；原论文Python两条文本明确pass@1另轨。只从明文数值取值，不从柱状图估算。BigCode HF Space入口已打开，但外壳页未返回可核验当前完整分榜，不把入口存活写成已取得实时SOTA。

[来源1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源3](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源4](https://huggingface.co/spaces/bigcode/multilingual-code-evals)（访问 2026-11-08）

## 联系方式

### 公开研究邮箱

待核实

> 状态：待核实。

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 项目反馈入口

https://github.com/nuprl/MultiPL-E/issues

> 公开仓库反馈入口；未发送问题。

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

### 官方公开社交入口

待核实

> 状态：待核实。

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

[来源1](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）

### 公开渠道/隐私边界

只收录官方公开项目反馈渠道；执行生成代码时遵循仓库建议使用容器隔离，不将运行示例当作可直接执行的本地指令。

[来源1](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）

## 原始文件

### 源站PDF

https://arxiv.org/pdf/2208.08227

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### PDF SHA-256

b905b9874ffcb4cee63f74cdc30524eae97013691e79313049ad72c6d6197580

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### PDF字节数

443169

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

[来源1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）

### Drive文件夹

```json
{
  "id": "1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF",
  "webViewLink": "https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF"
}
```

[来源1](https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF)（访问 2026-11-07）

### 其他官方文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM",
    "webViewLink": "https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/abs/2208.08227",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/html/2609.27284v1",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://arxiv.org/pdf/2208.08227",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/nuprl/MultiPL-E/blob/main/LICENSE",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://github.com/nuprl/MultiPL-E/blob/main/README.md",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/api/datasets/nuprl/MultiPL-E",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://huggingface.co/spaces/bigcode/multilingual-code-evals",
    "accessed": "2026-11-08"
  },
  {
    "type": "本轮打开核验的官方/研究来源",
    "url": "https://nuprl.github.io/MultiPL-E/",
    "accessed": "2026-11-08"
  }
]
```

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

[来源1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）；[来源2](https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk)（访问 2026-11-07）；[来源3](https://arxiv.org/abs/2208.08227)（访问 2026-11-08）；[来源4](https://arxiv.org/html/2609.27284v1)（访问 2026-11-08）；[来源5](https://arxiv.org/pdf/2208.08227)（访问 2026-11-08）；[来源6](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE)（访问 2026-11-08）；[来源7](https://github.com/nuprl/MultiPL-E/blob/main/README.md)（访问 2026-11-08）；[来源8](https://huggingface.co/api/datasets/nuprl/MultiPL-E)（访问 2026-11-08）；[来源9](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-08）；[来源10](https://huggingface.co/spaces/bigcode/multilingual-code-evals)（访问 2026-11-08）；[来源11](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）

### Drive原始PDF

```json
{
  "id": "1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ",
  "webViewLink": "https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk)（访问 2026-11-07）

## 变更记录

### 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  },
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "深度优化第1轮：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST, UTC+9)",
    "change": "第二轮深度复核：重读官方数据卡、README/许可、可用论文abs与PDF及官方榜；补精确题量、修订边界与完整可读成绩；区分私有集、历史基线、厂商自报与独立测评。"
  }
]
```

[来源1](https://nuprl.github.io/MultiPL-E/)（访问 2026-11-08）
