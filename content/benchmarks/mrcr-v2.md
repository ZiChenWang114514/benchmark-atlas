# OpenAI MRCR / MRCR v2

> 核验日期：2026-11-08（，UTC+9）。未知不补造；来源访问日不等于实验运行日。

OpenAI MRCR测试长对话中多份同类写作回复的顺序辨识与重现。公开HF版有2/4/8-needle配置，评分是带随机前缀门槛的SequenceMatcher匹配率，不是严格逐字全对准确率。厂商发布文的“v2”尚未映射到公开HF commit，本页不把二者当作已确认同一数据版本；其灵感来源Michelangelo论文也不冒称OpenAI的独立基准论文。
[本页导读依据](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

[补充导读依据](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）

## 基本信息

### 简称

OpenAI MRCR / MRCR v2

[来源1](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 全称

OpenAI MRCR (Multi-round co-reference resolution)

[来源1](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 数据/基准版本

模型发布文标签v2；与公开HF数据revision的精确映射待核实

[来源1](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 论文版本

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 发布日期

公开HF仓库创建2025-04-12 08:55:25；数据卡写4/12/2025 initial publication。公开初版与厂商MRCR v2首发不是同一事实，v2首发日期待核实。

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 主板块

语言

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 子领域

长上下文；多轮检索

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 许可边界

MIT（HF公开数据卡）

[来源1](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 论文入口

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 代码入口

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 数据入口

https://huggingface.co/datasets/openai/mrcr

[来源1](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 官方主页

https://huggingface.co/datasets/openai/mrcr

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 论文标题

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 发起与维护

### 发起方

OpenAI

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 合作机构

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 作者

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 当前维护方

OpenAI

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 资助

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 设计目标

### 衡量能力

从长多轮对话中区分相似请求，找出指定顺序的回复并重现。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 设计动机

needle和distractor来自相同分布，需同时识别主题、格式与先后次序。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 构建方式

### 题目来源

合成多轮对话，回复由gpt4o生成，植入2、4、8个相同请求。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 出题/构建者背景

官方说明合成assistant内容由gpt4o生成，主题涉及438个实体和10种写作格式；这是程序合成任务，不是专家手编问答集。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 审核流程

数据卡承认生成错误：历史样本中目标needle过多、参考答案错误，后续替换相应样本并加date_added以追踪修订；未提供更广人工复核协议。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 质量控制

数据卡记录生成bug修复：约10%目标needle过多，约5%ground truth错误；不能把历史错误比例当当前仍有。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 去污染/泄漏控制

公开数据存在训练接触可能；未核实v2额外防污染措施。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 数据形式

### 精确规模与统计口径

公开数据卡显示2400行；438实体、10写作格式、每bin100样本；不据此断言v2私有集题量。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 题型

按顺序检索并复现指定写作回复，前置随机字符串。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 模态

文本

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 语言/代码语种

数据卡任务说明与示例为英语；其他语言覆盖待核实。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 难度结构

2/4/8 needles；按prompt+answer token从4K至1M分8个长度bin。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 公开与隐藏划分

HF公开数据；v2模型卡所用精确revision与分区待核实。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 评测方法

### 指标

difflib.SequenceMatcher ratio，不是严格exact-match准确率。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 评分规则

随机字符串前缀不正确得0；去前缀后比较生成与标准答案的匹配率。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 运行与提示设置

官方卡提供o200k_base长度计数与运行示例；发布文报告8-needle、256K–512K和512K–1M。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 官方评测脚本

HF数据卡内含运行与grade示例。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 可比性警示

不能将不同needle数量、长度窗口、数据revision或匹配率/准确率混比；v2标签未映射到公开revision。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 最新情况

### 核验日期

2026-11-08

> 本次源站访问日期；时区；不等于榜单运行日期。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 最新数据状态与使用证据

```json
{
  "version": "v2发布文标签，公开数据精确revision待核实"
  "heat_confidence": "B"
  "evidence_2026_h2": [
    {
      "url": "https://openai.com/index/gpt-6-astra/"
      "date": "2026-11-07"
      "date_type": "observed_on"
      "note": "OpenAI当前发布表使用MRCR v2；热度主要来自单一机构OpenAI，不能称行业广泛采用。"
    }
  ]
  "public_hf_revision": "f4c69fae7cf81f7ca26b9fee34b392a50f6b8a1d"
  "revision_mapping": "厂商v2与此公开commit的对应关系待核实"
}
```

> 状态：待核实。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）

### 论文/数据修订历史

```json
{
  "scope": "OpenAI公开HF数据，不等同厂商v2内部版本映射"
  "hf_revision": "f4c69fae7cf81f7ca26b9fee34b392a50f6b8a1d"
  "last_modified_kst": "2025-12-09"
  "card_dates_verbatim": [
    "4/12/2025: Initial dataset published"
    "12/5/2025: Bugfix"
  ]
  "date_caveat": "数据卡数字日期可能存在美式/其他记法歧义；保留原文，HF明确ISO元数据另列，不强行替代修订语义。"
  "predecessor_paper": {
    "title": "Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries"
    "url": "https://arxiv.org/abs/2409.12640"
    "pdf_read": "https://arxiv.org/pdf/2409.12640v2"
    "scope": "Google/DeepMind原始MRCR灵感来源，不是OpenAI MRCR v2独立论文"
  }
}
```

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源3](https://arxiv.org/abs/2409.12640)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.12640v2)（访问 2026-11-08）

### 饱和性证据

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 污染与已知争议

公开版历史约10%样本needle过多、约5%ground truth错误，官方称已替换并添加date_added；比例指过去bug而非当前残留错误率。v2发布文未明确映射公开HF commit；重复相似请求导致的顺序辨识和最长token筛选均影响比较。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源2](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）

### 衍生与条目关系

OpenAI数据卡明确承认受Michelangelo论文MRCR启发并扩大难度；2/4/8 needle是同基准配置，不另计三个benchmark；厂商v2分数不能倒填成该Google论文的结果。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源2](https://arxiv.org/pdf/2409.12640v2)（访问 2026-11-08）

## 榜单快照

### 本次榜单采集日

2026-11-08

[来源1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）

### 官方榜源

https://openai.com/index/gpt-6-astra/

[来源1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）

### 第三方覆盖

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 分源、分版本、分协议成绩

以下仅在各自赛道内展示；厂商自报、研究复测与创建者榜不视作相同的独立评测。没有明确运行日时只列采集日；“—”不是补造名次。

#### OpenAI发布文 / MRCR v2 / 8-needle / 256K–512K

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | GPT-6 Astra | 100.0 % | MRCR v2发布表分数（8-needle） | 未逐项给出 | [原始来源](https://openai.com/index/gpt-6-astra/)（2026-11-08） |
| 2 | GPT-5.6 Sol | 91.5 % | MRCR v2发布表分数（8-needle） | 未逐项给出 | [原始来源](https://openai.com/index/gpt-6-astra/)（2026-11-08） |

- 厂商研究环境/API；各项取最大effort结果；两个窗口不平均

- 厂商自报对照表；非独立实时总榜

#### OpenAI发布文 / MRCR v2 / 8-needle / 512K–1M

| 源内名次/顺序 | 模型与配置 | 成绩 | 指标 | 来源记录/运行时间 | 来源（采集日） |
|---|---|---|---|---|---|
| 1 | GPT-6 Astra | 96.3 % | MRCR v2发布表分数（8-needle） | 未逐项给出 | [原始来源](https://openai.com/index/gpt-6-astra/)（2026-11-08） |
| 2 | GPT-5.6 Sol | 73.8 % | MRCR v2发布表分数（8-needle） | 未逐项给出 | [原始来源](https://openai.com/index/gpt-6-astra/)（2026-11-08） |

- 厂商研究环境/API；各项取最大effort结果；两个窗口不平均

- 厂商自报对照表；非独立实时总榜

[来源1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）

### 覆盖范围与限制

将原先一个字符串中的两个长度窗口拆成4条结构化成绩，每个窗口单独排序；保留厂商口径，不把匹配率当严格exact-match，也不推断v2使用HF哪一commit。精确运行日未给出，访问日与运行日分开。

[来源1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 联系方式

### 公开研究邮箱

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 项目反馈入口

https://huggingface.co/datasets/openai/mrcr/discussions（官方HF社区反馈入口，不是已核验的独立GitHub仓库）

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 官方公开社交入口

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 公开渠道/隐私边界

仅记录公开官方研究入口；不收集示例中占位符的姓名、地址、邮箱或其他私人联系信息。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

## 原始文件

### 源站PDF

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### PDF SHA-256

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### PDF字节数

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）

### 文件夹

待核实

> 状态：待核实。

> 打开所列材料后仍未精确核实；不代表官方没有公开。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 其他官方文档

```json
[
  {
    "type": "官方HF数据卡及内联运行/grade示例"
    "url": "https://huggingface.co/datasets/openai/mrcr"
    "accessed": "2026-11-08"
  }
  {
    "type": "公开HF commit元数据"
    "url": "https://huggingface.co/datasets/openai/mrcr"
    "revision": "f4c69fae7cf81f7ca26b9fee34b392a50f6b8a1d"
    "accessed": "2026-11-08"
  }
  {
    "type": "MRCR前身论文，非OpenAI v2论文"
    "url": "https://arxiv.org/pdf/2409.12640v2"
    "accessed": "2026-11-08"
  }
  {
    "type": "厂商v2使用证据"
    "url": "https://openai.com/index/gpt-6-astra/"
    "accessed": "2026-11-08"
  }
  {
    "type": "打开核验的官方/研究来源"
    "url": "https://arxiv.org/abs/2409.12640"
    "accessed": "2026-11-08"
  }
]
```

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源2](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）；[来源3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-08）；[来源4](https://arxiv.org/pdf/2409.12640v2)（访问 2026-11-08）；[来源5](https://arxiv.org/abs/2409.12640)（访问 2026-11-08）

### 原始PDF

待核实

> 状态：待核实。

> 本组仅本地研究，未上传。

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 变更记录

### 变更记录

```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-08"
    "timezone": " (, UTC+9)"
    最近复核
  }
]
```

[来源1](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-08）
