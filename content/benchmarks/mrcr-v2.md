# OpenAI MRCR / MRCR v2

> 核验：2026-11-07（KST / Asia/Seoul）；仅记录真实打开的材料，未知不代表未公开。

研究快照；trending: B；未知信息保留待核实。

## 基本信息

### 简称

OpenAI MRCR / MRCR v2

[来源](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 全称

OpenAI MRCR (Multi-round co-reference resolution)

[来源](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 版本

模型发布文标签v2；与公开HF数据revision的精确映射待核实

[来源](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### paper_version

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 发布日期

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### section

语言

> 编辑主板块归档，不据此限制跨学科覆盖。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### subfields

```json
[
  "长上下文",
  "多轮检索"
]
```

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 许可证

MIT（HF公开数据卡）

[来源](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 论文链接

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 官方代码

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 数据集

https://huggingface.co/datasets/openai/mrcr

[来源](https://huggingface.co/datasets/openai/mrcr/raw/main/README.md)（访问 2026-11-07）

### 官网

https://huggingface.co/datasets/openai/mrcr

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 论文标题

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 发起与维护

### 发起方

OpenAI

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### partners

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 作者

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 维护方

OpenAI

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### funders

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 设计目标

### 衡量能力

从长多轮对话中区分相似请求，找出指定顺序的回复并重现。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 设计动机

needle和distractor来自相同分布，需同时识别主题、格式与先后次序。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 构建方式

### question_sources

合成多轮对话，回复由gpt4o生成，植入2、4、8个相同请求。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### author_background

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### review_process

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### quality_control

数据卡记录生成bug修复：约10%目标needle过多，约5%ground truth错误；不能把历史错误比例当当前仍有。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### decontamination

公开数据存在训练接触可能；本轮未核实v2额外防污染措施。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 数据形式

### 题量与规模

公开数据卡显示2400行；438实体、10写作格式、每bin100样本；不据此断言v2私有集题量。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 题型

按顺序检索并复现指定写作回复，前置随机字符串。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### modalities

```json
[
  "文本"
]
```

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### languages

数据卡任务说明与示例为英语；其他语言覆盖待核实。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### difficulty

2/4/8 needles；按prompt+answer token从4K至1M分8个长度bin。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 公开与隐藏划分

HF公开数据；v2模型卡所用精确revision与分区待核实。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 评测方法

### 指标

difflib.SequenceMatcher ratio，不是严格exact-match准确率。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 评分方式

随机字符串前缀不正确得0；去前缀后比较生成与标准答案的匹配率。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 提示与运行设置

官方卡提供o200k_base长度计数与运行示例；发布文报告8-needle、256K–512K和512K–1M。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 官方评测实现

HF数据卡内含运行与grade示例。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 可比性警告

不能将不同needle数量、长度窗口、数据revision或匹配率/准确率混比；v2标签未映射到公开revision。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 最新情况

### checked_at

2026-11-07 KST / Asia/Seoul

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 当前版本与近期使用证据

```json
{
  "version": "v2发布文标签，公开数据精确revision待核实",
  "heat_confidence": "B",
  "evidence_2026_h2": [
    {
      "url": "https://openai.com/index/gpt-6-astra/",
      "date": "2026-11-07",
      "date_type": "observed_on",
      "note": "OpenAI当前发布表使用MRCR v2；本轮热度主要来自单一机构OpenAI，不能称行业广泛采用。"
    }
  ]
}
```

[来源](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### paper_revision_history

HF卡使用4/12/2025与12/5/2025两种数字日期记法且viewer日期有歧义，本轮不转换为确定ISO发布日期。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### saturation

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 污染与争议

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### derivatives

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 为什么近期热门

本轮主要来自单一机构的当前评测或厂商自评，不宣称行业广泛采用。

## 榜单快照

### snapshot_date

2026-11-07 KST / Asia/Seoul

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### official_url

https://openai.com/index/gpt-6-astra/

[来源](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### third_party_url

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### 模型成绩

```json
[
  {
    "rank": 1,
    "model": "GPT-6 Astra",
    "score": "100.0% (256K–512K); 96.3% (512K–1M)",
    "metric": "MRCR v2 8-needle 厂商报告",
    "source_url": "https://openai.com/index/gpt-6-astra/",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "厂商发布表比较，不是独立实时排行榜；两个长度窗口不能平均。"
  },
  {
    "rank": 2,
    "model": "GPT-5.6 Sol",
    "score": "91.5% (256K–512K); 73.8% (512K–1M)",
    "metric": "MRCR v2 8-needle 厂商报告",
    "source_url": "https://openai.com/index/gpt-6-astra/",
    "source_date": "待核实",
    "collected_at": "2026-11-07 KST",
    "result_type": "厂商发布表比较，不是独立实时排行榜；两个长度窗口不能平均。"
  }
]
```

[来源](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

### 时效与可比性

厂商发布表比较，不是独立实时排行榜；两个长度窗口不能平均。

[来源](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### github_issues

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### official_social

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### privacy_policy

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

## 原始文件

### 原论文PDF

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### sha256

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### pdf_bytes

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### drive_folder

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### other_documents

待核实

> 本轮打开所列材料后仍未精确核实；不代表官方没有公开。

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）

### Drive PDF

待核实

> 本组未上传Drive。

## 变更记录

### changelog

```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "按官方材料新建中文条目；区分热度、质量和不同版本评分。"
  }
]
```

[来源](https://huggingface.co/datasets/openai/mrcr)（访问 2026-11-07）
