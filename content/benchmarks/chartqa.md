# ChartQA

> Benchmark Constitution · 深度复核：2026-11-08 KST / Asia/Seoul。第1轮已重新检索官方材料；历史榜单/当前快照/厂商自报分离；未实证字段保留待核实

ChartQA把真实图表、人工问答与摘要驱动的机器问答组合起来，测视觉引用与多步数值推理。其常用测试集2,500条QA包含人工与机器各1,250题，问题条数不等于独立图像数。基线是否获得底层gold table会显著改变任务；5%数值容差协议也不能与另一论文的LLM裁判成绩直接混排。

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

## 基本信息

### 简称

ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 全称

ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 版本边界

官方Full Version（含annotations）；另保留不含annotations的First Version。README未采用可核实的数字版本号。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 论文版本

arXiv v1

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 发布日期

2022-03-19

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

> arXiv元数据首发日期原值；不是推测数据集首次上线时间。

### 板块

多模态

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

> Benchmark Atlas编辑归档；跨学科条目只在主板块计数，不声称分类由基准官方规定。

### 领域

```json
[
  "图表问答"
]
```

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 许可与限制

官方仓库LICENSE全文为GNU GPL v3；HF卡同标GPL-3.0。第三方原始图表版权不因代码许可自动转移。

[来源1](https://github.com/vis-nlp/ChartQA/blob/main/LICENSE)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/blob/main/README.md)（访问2026-11-08）

### 论文

https://arxiv.org/abs/2203.10244

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 官方代码

https://github.com/vis-nlp/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 数据入口

https://huggingface.co/datasets/ahmed-masry/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA)（访问2026-11-07）

### 官方主页

https://github.com/vis-nlp/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）；[来源2](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 论文题名

ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

## 发起与维护

### 发起方

论文作者单位：York University、南洋理工大学、Salesforce Research。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 合作机构

```json
[
  "York University, Canada",
  "Nanyang Technological University, Singapore",
  "Salesforce Research"
]
```

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问2026-11-07）

> 论文作者署名机构，不推断额外商业合作关系。

### 作者

```json
[
  "Masry, Ahmed",
  "Long, Do Xuan",
  "Tan, Jia Qing",
  "Joty, Shafiq",
  "Hoque, Enamul"
]
```

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）

### 维护入口

vis-nlp / Ahmed Masry；官方仓库Contact由Ahmed Masry负责接收问题。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 资助披露

Natural Sciences and Engineering Research Council (NSERC) of Canada。

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问2026-11-07）

> 论文Acknowledgement明确资助机构；未补造项目编号。

## 设计目标

### 测量对象

需要视觉引用、逻辑及算术组合运算的真实图表问答。

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 既有评测的缺口

既有图表QA多使用模板问题及固定答案词表，难覆盖自然复杂问题。

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

## 构建方式

### 题源

从Statista、Pew、Our World in Data、OECD采集真实图表；人工问答ChartQA-H与从人工图表摘要自动生成的ChartQA-M并存。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 构建人员

人工标注者提出自然问题；自动部分由摘要驱动生成，不把全部称为专家原创。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）

### 审核

人工问答由另一标注员复核；不一致答案再人工裁定。论文报告原始exact-match一致率61.04%，另抽500例考虑拼写/词形变化后一致率78.55%。机器生成test剔除无效问题。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-08）

### 质控

官方从SVG自动产生框标注；损坏、缺失或带噪的SVG会引入噪声。Pew图表没有SVG，需人工标注并用启发式加速；机器生成测试问答另经手工清理。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）；[来源2](https://aclanthology.org/2022.findings-acl.177.pdf)（访问2026-11-07）

### 去污染及边界

待核实

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

## 数据形式

### 规模与计数口径

```json
{
  "total_qa": 32719,
  "train_qa": 28299,
  "validation_qa": 1920,
  "test_qa": 2500,
  "paper_human_qa": 9608,
  "paper_machine_qa": 23111,
  "paper_human_charts": 4804,
  "paper_machine_charts": 17141
}
```

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/raw/main/README.md)（访问2026-11-07）

> 论文Table2与官方HF splits一致；图表计数为两个来源集合口径，不将4804+17141冒充全库去重图表数。

### 题型

开放式数值或文本回答；条形图、折线图和饼图，附原始表格及部分框标注。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 模态

图像+文本

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 语言

英文（本次公开问题/官方说明；完整语言分布待核实）

[来源1](https://huggingface.co/datasets/ahmed-masry/ChartQA)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 难度

```json
{
  "proxy": "无统一easy/medium/hard标注；论文以任务类型和推理操作分析。",
  "sample_analysis": "论文Table4随机300个人工问题：data retrieval 13.0%、visual 10.7%、compositional 43.0%、visual+compositional 33.3%。"
}
```

[来源1](https://aclanthology.org/2022.findings-acl.177.pdf)（访问2026-11-07）

> 这是论文抽样类型分布，不外推为完整32,719题的难度分布。

### 划分与公开范围

公开train/val/test为28,299/1,920/2,500条QA；test人工/机器各1,250题。论文Table 2对应人工625图、机器987图；不要将QA条数写成独立图像数量。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-08）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/blob/main/README.md)（访问2026-11-08）

## 评测方法

### 指标

relaxed accuracy：数值误差在参考值5%以内算正确，非数值采用字符串匹配。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 评分

relaxed accuracy：数值误差在参考值5%以内算正确，非数值采用字符串匹配。

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 提示与运行条件

论文基线可使用图像和底层数据表；评测时应说明是否使用oracle表格、OCR或仅图像，不能同口径排名。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）

### 官方评测入口

https://github.com/vis-nlp/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 可比性边界

机器生成/人工子集分别报告；官方指出SVG缺失/损坏使框标注有噪声。MMVistaReason使用CompassVerifier，不等同于原始5%数值容差。

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）；[来源3](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）

## 最新情况

### 复核时间

2026-11-08 KST / Asia/Seoul

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-08）

### 当前版本

本轮核实官方Full Version（含图像框标注），HF train/val/test为28,299/1,920/2,500；官方后续ChartQAPro是独立基准，不替代原版数据版本。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）；[来源2](https://huggingface.co/datasets/ahmed-masry/ChartQA/raw/main/README.md)（访问2026-11-07）

### 论文修订与后续使用

```json
{
  "revisions": [
    {
      "version": "v1",
      "date_kst": "2022-03-19T14:00:30+09:00"
    }
  ],
  "continued_use_2026h2": [
    {
      "url": "https://arxiv.org/html/2610.01352v2",
      "date": "2026-10-23",
      "note": "MMVistaReason v2 §4.1及表2实际评测 ChartQA（ChartQA设置），比较4B/9B及其他视觉语言模型；不把mini/val等划分另计。",
      "date_kst": "2026-10-23T01:54:37+09:00",
      "verified_in_round1": "本轮重新打开arXiv v2正文§4.1/Table2与abs提交历史，确认实际评测；源站v2为2026-10-22 16:54:37 UTC。"
    }
  ],
  "verification": "已打开并复核证据原文的实际评测章节及表格，不只按参考文献或网页存活判断。",
  "arxiv_revisions_kst": [
    {
      "version": "v1",
      "submitted_at_kst": "2022-03-19T14:00:30+09:00"
    }
  ]
}
```

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-08）

### 饱和情况

待核实

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

### 风险与冲突

机器生成/人工子集分别报告；官方指出SVG缺失/损坏使框标注有噪声。MMVistaReason使用CompassVerifier，不等同于原始5%数值容差。

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）；[来源3](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）

### 衍生与后续工作

ChartQAPro，官方仓库推荐的更具挑战的真实图表QA后续基准；本条不将Pro另计入原版结果。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

## 榜单快照

### 快照时间

2026-11-08 KST / Asia/Seoul（实际复核日；批次标签2026-11-07）

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-08）

### 官方榜入口

https://github.com/vis-nlp/ChartQA

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 第三方榜入口

待核实

[来源1](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问2026-11-07）

> 本轮已重新检查官方README/项目页及可读论文；该字段仍未取得足够的明确官方声明，保留待核实，不推断未公开或不存在。

### 逐轨结果

```json
[
  {
    "model": "VisionTaPas",
    "score": 45.52,
    "unit": "%",
    "metric": "原论文准确率（数值答案允许5%容差）",
    "scope": "ChartQA原论文Table5，gold data table not provided，test；历史基线",
    "date": "2022-05",
    "accessed": "2026-11-08",
    "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf",
    "provenance": "原始基准作者公布；本轮从官方ACL论文重新读取，不宣称当前排名。",
    "track": "原论文Table 5／无gold table／历史基线",
    "rank": null
  },
  {
    "model": "VL-T5",
    "score": 41.56,
    "unit": "%",
    "metric": "原论文准确率（数值答案允许5%容差）",
    "scope": "ChartQA原论文Table5，gold data table not provided，test；历史基线",
    "date": "2022-05",
    "accessed": "2026-11-08",
    "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf",
    "provenance": "原始基准作者公布；本轮从官方ACL论文重新读取，不宣称当前排名。",
    "track": "原论文Table 5／无gold table／历史基线",
    "rank": null
  },
  {
    "model": "TaPas",
    "score": 41.28,
    "unit": "%",
    "metric": "原论文准确率（数值答案允许5%容差）",
    "scope": "ChartQA原论文Table5，gold data table not provided，test；历史基线",
    "date": "2022-05",
    "accessed": "2026-11-08",
    "source_url": "https://aclanthology.org/2022.findings-acl.177.pdf",
    "provenance": "原始基准作者公布；本轮从官方ACL论文重新读取，不宣称当前排名。",
    "track": "原论文Table 5／无gold table／历史基线",
    "rank": null
  },
  {
    "model": "MMVistaReason-4B (MVR-4B)",
    "score": 86.2,
    "unit": "%",
    "metric": "论文协议答案正确率（CompassVerifier）",
    "scope": "ChartQA",
    "date": "2026-10-23",
    "accessed": "2026-11-08",
    "source_url": "https://arxiv.org/html/2610.01352v2",
    "provenance": "MMVistaReason作者自报表2；VLMEvalKit，T=0，max16384；§7.3用CompassVerifier替代传统字符串匹配，不是官方榜单/AA独立评测",
    "date_basis": "arXiv v2提交时间换算KST；不是未公开的评测运行日期。",
    "track": "MMVistaReason v2／CompassVerifier／作者自报",
    "rank": null
  },
  {
    "model": "MMVistaReason-9B (MVR-9B)",
    "score": 87.6,
    "unit": "%",
    "metric": "论文协议答案正确率（CompassVerifier）",
    "scope": "ChartQA",
    "date": "2026-10-23",
    "accessed": "2026-11-08",
    "source_url": "https://arxiv.org/html/2610.01352v2",
    "provenance": "MMVistaReason作者自报表2；同上协议，不与其他榜单无条件混排",
    "date_basis": "arXiv v2提交时间换算KST；不是未公开的评测运行日期。",
    "track": "MMVistaReason v2／CompassVerifier／作者自报",
    "rank": null
  }
]
```

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-08）；[来源2](https://arxiv.org/html/2610.01352v2)（访问2026-11-08）

### 覆盖边界

本轮重新检查官方README、Full Version数据卡及AA评测目录，未核实持续更新的原版ChartQA独立榜单。以下新采集官方论文Table5历史基线（无gold table），与2026-H2作者复测分组；这些不是2026实时前三。当前官方排名仍待核实。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）；[来源2](https://aclanthology.org/2022.findings-acl.177.pdf)（访问2026-11-07）；[来源3](https://artificialanalysis.ai/evaluations?skill=multimodal)（访问2026-11-07）；[来源4](https://arxiv.org/html/2610.01352v2)（访问2026-11-07）

## 联系方式

### 公开研究联系

```json
[
  "amasry17@ku.edu.tr"
]
```

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

> 官方README明确旧邮箱masry20@yorku.ca已停用；当前联系不再推荐旧邮箱。

### 项目反馈

https://github.com/vis-nlp/ChartQA/issues

[来源1](https://github.com/vis-nlp/ChartQA)（访问2026-11-07）

### 官方社交入口

旧学校邮箱masry20@yorku.ca已停用，采用官方README当前公开联系邮箱。

[来源1](https://raw.githubusercontent.com/vis-nlp/ChartQA/main/README.md)（访问2026-11-07）

### 联系信息边界

仅记录官方公开项目反馈渠道，不收集或推测私人联系方式。

[来源1](urn:benchmark-atlas:constitution:v0.1)（访问2026-11-07）

## 原始文件

### 原始PDF

https://arxiv.org/pdf/2203.10244

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-07）；[来源2](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）

### PDF SHA-256

3b1d863e6f9ca45e84131bc51c8e47c8026faf6a6875edb9032bce2b9fadf0f9

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）

> 下载原始字节校验，未压缩、未改写。

### PDF字节数

2938574

[来源1](https://arxiv.org/pdf/2203.10244)（访问2026-11-07）

### Drive目录

```json
{
  "id": "1elALF3JQUPeGjv3Ee6JqeABOnA8QVlFq",
  "webViewLink": "https://drive.google.com/drive/folders/1elALF3JQUPeGjv3Ee6JqeABOnA8QVlFq"
}
```

[来源1](https://drive.google.com/drive/folders/1elALF3JQUPeGjv3Ee6JqeABOnA8QVlFq)（访问2026-11-07）

### 其他官方材料

```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1UkqHF3gkf4lU5t9Ef0agnMxVRhs5_KmcDXVOy1cIsgM",
    "webViewLink": "https://docs.google.com/document/d/1UkqHF3gkf4lU5t9Ef0agnMxVRhs5_KmcDXVOy1cIsgM/edit?usp=drivesdk"
  }
]
```

[来源1](https://docs.google.com/document/d/1UkqHF3gkf4lU5t9Ef0agnMxVRhs5_KmcDXVOy1cIsgM/edit?usp=drivesdk)（访问2026-11-07）

### Drive论文归档

```json
{
  "id": "1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy",
  "webViewLink": "https://drive.google.com/file/d/1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy/view?usp=drivesdk"
}
```

[来源1](https://drive.google.com/file/d/1eGMZQoZFHWZZ4dshNpUWUiA0SOWaTyYy/view?usp=drivesdk)（访问2026-11-07）

## 变更记录

```json
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方存在、收集原始资料、编写中文档案，逐项复核2026-H2使用证据并保留协议与版本差异。"
  },
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "round": "1 / 深度实证复核",
    "change": "补Full/First版本区别、NSERC资助、机构、最新联系邮箱和题量/类型分布；采集官方论文历史基线，当前独立实时榜仍未核实；重核H2。"
  },
  {
    "date": "2026-11-08",
    "timezone": "Asia/Seoul (KST)",
    "change": "第2轮q2：重读一级材料、保留版本/许可冲突；榜单按来源与协议分轨，中文介绍重写。"
  }
]
```

[来源1](https://arxiv.org/abs/2203.10244)（访问2026-11-08）；[来源2](https://github.com/vis-nlp/ChartQA)（访问2026-11-08）
