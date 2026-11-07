# GSM8K｜中文深度介绍

评估语言多样的小学/初中级数学应用题中的多步算术与验证器选解能力。

来源：[https://arxiv.org/abs/2110.14168](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 一、基本信息

### 简称

GSM8K

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 全称

Grade School Math 8K

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 数据/协议版本

main数据；仓库标记Archive，代码按原样提供

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 发布日期

2021-10-27（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 板块

数学

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）。

### 子领域

[
  "数学应用题"
]

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 许可证

待核实

状态：待核实。

说明：数据、代码、论文和原题权利分开；尚未核实对应发布文件许可证

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/2110.14168

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 代码

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）。

### 数据集

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 官网

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 论文题名

Training Verifiers to Solve Math Word Problems

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

OpenAI

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 正式合作方

待核实

状态：待核实。

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 作者

[
  "Cobbe, Karl",
  "Kosaraju, Vineet",
  "Bavarian, Mohammad",
  "Chen, Mark",
  "Jun, Heewoo",
  "Kaiser, Lukasz",
  "Plappert, Matthias",
  "Tworek, Jerry",
  "Hilton, Jacob",
  "Nakano, Reiichiro",
  "Hesse, Christopher",
  "Schulman, John"
]

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 当前维护

OpenAI官方仓库；当前Archive状态

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md)（采集 2026-11-07）。

### 资助

待核实

状态：待核实。

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

评估语言多样的小学/初中级数学应用题中的多步算术与验证器选解能力。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 设计缺口

概念简单不等于可被语言模型稳定求解，需要避免只记住固定题型模板。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 四、构建方式

### 题源

人工写题承包者编写应用题和自然语言解答；论文流程包括Upwork、Surge AI及可供改写的模型题目种子。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 出题/标注人员

付费人工题目写作者，研究团队进行二次求解和数据审核；不能表述为每题都来自数学专家。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 审核

独立第二人解题，对分歧题修改或剔除，并做题目相似性检查。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 质量控制

自然语言解答带计算注释，####之后为最终数值；另提供自动生成苏格拉底式子问题版本。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 去污染边界

收集时检查模板/相似题有助于质量控制；不保证未来预训练数据没有公开题。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 五、数据形式

### 题量

官方概述约8500题，约7500训练与1000测试；精确文件行数见本条若已固定的实测注释。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 题型

2至8步基础算术应用题，输出自然语言解法和最终数值。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 难度

明亮的中学生应可解（作者设计意图）；不是高等数学或奥赛难度。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 公开/隐藏划分

train.jsonl与test.jsonl均公开；另有Socratic格式，不可当独立新benchmark。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 六、评测方法

### 指标

最终数值答案准确率；验证器从多个候选中选择的得分需另标。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 评分实现

官方dataset.py提取####后的数字；计算器通过<<...>>标注运行，不是天然禁止工具。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 提示与预算

原论文训练生成器和验证器并比较多候选选优；best-of-100不等于pass@1。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 评测脚本

https://github.com/openai/grade-school-math

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 可比性警示

单次、投票、验证器best-of-N、计算器和few-shot设置不能混排。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 最新可确认数据/协议

main数据；仓库标记Archive，代码按原样提供

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md)（采集 2026-11-07）。

### 修订与2026H2收录证据

{
  "arxiv_version": "arXiv v2",
  "history_note": "完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。",
  "2026_h2_evidence": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1–4.2及表2–4实际报告 GSM8K。AIME 的不同年份归同一条目，不用年份拆分凑数。"
    }
  ]
}

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 饱和判断

待核实

状态：待核实。

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

仓库注明示例模型解答中的旧计算器曾有约1%失败，代码已修复但示例未重生成；这是历史样例问题非当前整体标签错率。

来源：[1](https://raw.githubusercontent.com/openai/grade-school-math/master/README.md)（采集 2026-11-07）。

### 衍生与排除项

Socratic格式自动加子问题，原论文未用其进行实验；本库不另计数。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）；[2](https://github.com/openai/grade-school-math)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 官方榜

待核实

状态：待核实。

说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 二级机构榜

待核实

状态：待核实。

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 限定范围的分数快照

[
  {
    "model_version": "Hunyuan-A13B",
    "score": "91.83",
    "unit": "%",
    "scope_and_protocol": "基础模型，表2，4-shot CoT",
    "result_date": "2026-09-23",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2609.27284v1",
    "source_class": "三级：模型厂商自报",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Qwen3-A22B",
    "score": "94.39",
    "unit": "%",
    "scope_and_protocol": "同表对照；厂商报告转录",
    "result_date": "2026-09-23",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2609.27284v1",
    "source_class": "三级：模型厂商自报",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  }
]

来源：[1](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

[
  "karl@openai.com",
  "vineet@openai.com"
]

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### Issues

https://github.com/openai/grade-school-math/issues

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）。

### 官方社交

待核实

状态：待核实。

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### 隐私政策

待核实

状态：待核实。

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

## 十、原始文件

### 原始PDF

https://arxiv.org/pdf/2110.14168

来源：[1](https://arxiv.org/abs/2110.14168)（采集 2026-11-07）。

### SHA256

a52417d8fcd006de882e3b404850e2cc4246815828897c18c6ce6c7a448985a4

来源：[1](https://arxiv.org/pdf/2110.14168)（采集 2026-11-07）。

### PDF字节数

2935719

来源：[1](https://arxiv.org/pdf/2110.14168)（采集 2026-11-07）。

### Drive资料夹

{
  "id": "1C6D6YXK-yBTIxFc1sWyfYFIxKjH54dmb",
  "webViewLink": "https://drive.google.com/drive/folders/1C6D6YXK-yBTIxFc1sWyfYFIxKjH54dmb"
}

来源：[1](https://drive.google.com/drive/folders/1C6D6YXK-yBTIxFc1sWyfYFIxKjH54dmb)（采集 2026-11-07）。

### 中文文档与本地稿

{
  "chinese_intro_doc": {
    "id": "1mgSxjZ0tSOCdaQ6bYp18z1g7T9ZZldF9DGBNzoeOnb8",
    "webViewLink": "https://docs.google.com/document/d/1mgSxjZ0tSOCdaQ6bYp18z1g7T9ZZldF9DGBNzoeOnb8/edit?usp=drivesdk",
    "mimeType": "application/vnd.google-apps.document"
  },
  "local_markdown": "content/benchmarks/gsm8k.md"
}

来源：[1](https://drive.google.com/drive/folders/1C6D6YXK-yBTIxFc1sWyfYFIxKjH54dmb)（采集 2026-11-07）。

### drive_pdf

{
  "id": "1TjNp6myEAC_TGomPvMQItLdxd9AUTS1y",
  "webViewLink": "https://drive.google.com/file/d/1TjNp6myEAC_TGomPvMQItLdxd9AUTS1y/view?usp=drivesdk"
}

来源：[1](https://drive.google.com/file/d/1TjNp6myEAC_TGomPvMQItLdxd9AUTS1y/view?usp=drivesdk)（采集 2026-11-07）。

## 十一、变更记录

### changelog

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。"
  }
]

来源：[1](https://github.com/openai/grade-school-math)（采集 2026-11-07）。

