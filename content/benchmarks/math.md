# MATH｜中文深度介绍

评估竞赛数学多步求解、符号操作及最终答案正确性。

来源：[https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 一、基本信息

### 简称

MATH

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 全称

Mathematics Aptitude Test of Heuristics

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 数据/协议版本

完整MATH 12500题；MATH-500单列衍生口径

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 发布日期

2021-03-06（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 板块

数学

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）。

### 子领域

[
  "竞赛数学问题求解"
]

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 许可证

原论文声明数据及代码MIT；不对原始竞赛内容的权利作法律保证

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/2103.03874

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 代码

https://github.com/hendrycks/math

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）。

### 数据集

https://huggingface.co/datasets/qwedsacf/competition_math

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 官网

https://github.com/hendrycks/math

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 论文题名

Measuring Mathematical Problem Solving With the MATH Dataset

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

University of California Berkeley、University of Chicago（论文署名）

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 正式合作方

待核实

状态：待核实。

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 作者

[
  "Hendrycks, Dan",
  "Burns, Collin",
  "Kadavath, Saurav",
  "Arora, Akul",
  "Basart, Steven",
  "Tang, Eric",
  "Song, Dawn",
  "Steinhardt, Jacob"
]

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 当前维护

待核实

状态：待核实。

说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 资助

待核实

状态：待核实。

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

评估竞赛数学多步求解、符号操作及最终答案正确性。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 设计缺口

简单算术或短步骤集合不足以反映代数、几何和数论等更广的数学能力。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 四、构建方式

### 题源

来自AMC、AIME等竞赛及AoPS整理的数学题，保留完整解答与最终答案。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 出题/标注人员

研究者整理已有人类数学竞赛题及解答；并非12500题全由作者原创。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 审核

整理题目、解答、难度和学科信息，统一为可处理的文本格式。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 质量控制

用LaTeX表示数学式，最终答案以boxed标注；几何题部分通过Asymptote代码提供图形信息。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 去污染边界

题源长期公开；原论文讨论预训练与能力差距，但不能保证后续模型无题目记忆。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 五、数据形式

### 题量

12500题：训练7500、测试5000；7个学科、5档难度。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 题型

数学开放式求解，评分重点为可规范化的最终答案而非逐步证明。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 难度

5级难度，7学科；不同级别和科目准确率应分别考察。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 公开/隐藏划分

完整训练7500与测试5000均公开；MATH-500仅选取测试中的500题，不能用其分数代表完整集。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 六、评测方法

### 指标

最终答案准确率（规范化精确匹配/等价判定）。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 评分实现

抽取boxed答案并处理数学字符串的规范化；格式归一化细节会改变得分。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 提示与预算

原论文包含微调实验；现代CoT、计算器、代码、投票与单次生成必须另记。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 评测脚本

https://github.com/hendrycks/math

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 可比性警示

MATH全量5000测试题与MATH-500是不同分母；Hunyuan报告写MATH但引用Lightman，子集口径尚不能确认。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 最新可确认数据/协议

完整MATH 12500题；MATH-500单列衍生口径

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 修订与2026H2收录证据

{
  "arxiv_version": "arXiv v2",
  "history_note": "完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。",
  "2026_h2_evidence": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1–4.2及表2–4实际报告 MATH。AIME 的不同年份归同一条目，不用年份拆分凑数。"
    }
  ]
}

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 饱和判断

待核实

状态：待核实。

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/math-500)（采集 2026-11-07）；[3](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

官方论文称数据/代码以MIT发布，但原竞赛内容的权利不能据此无条件外推；本轮未法律审查。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）；[2](https://github.com/hendrycks/math)（采集 2026-11-07）。

### 衍生与排除项

MATH-500/PRM800K围绕过程监督发展；AA只给MATH-500榜，不能冒充完整MATH榜。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）；[2](https://github.com/hendrycks/math)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/math-500)（采集 2026-11-07）；[3](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 官方榜

待核实

状态：待核实。

说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 二级机构榜

https://artificialanalysis.ai/evaluations/math-500

来源：[1](https://artificialanalysis.ai/evaluations/math-500)（采集 2026-11-07）。

### 限定范围的分数快照

[
  {
    "model_version": "GPT-5 (High)",
    "score": "99.4",
    "unit": "%",
    "scope_and_protocol": "AA MATH-500，非完整MATH5000；确切checkpoint/测量日未明",
    "result_date": "待核实",
    "snapshot_date": "2026-11-07",
    "source_url": "https://artificialanalysis.ai/evaluations/math-500",
    "source_class": "二级：独立评测",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "o3",
    "score": "99.2",
    "unit": "%",
    "scope_and_protocol": "AA MATH-500，同口径",
    "result_date": "待核实",
    "snapshot_date": "2026-11-07",
    "source_url": "https://artificialanalysis.ai/evaluations/math-500",
    "source_class": "二级：独立评测",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Hunyuan-A13B",
    "score": "72.35",
    "unit": "%",
    "scope_and_protocol": "基础模型，表2 MATH，4-shot CoT；非AA榜",
    "result_date": "2026-09-23",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2609.27284v1",
    "source_class": "三级：模型厂商自报",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  }
]

来源：[1](https://artificialanalysis.ai/evaluations/math-500)（采集 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）；[2](https://artificialanalysis.ai/evaluations/math-500)（采集 2026-11-07）；[3](https://arxiv.org/html/2609.27284v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

[
  "hendrycks@berkeley.edu"
]

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）；[2](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### Issues

https://github.com/hendrycks/math/issues

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）。

### 官方社交

待核实

状态：待核实。

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### 隐私政策

待核实

状态：待核实。

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

## 十、原始文件

### 原始PDF

https://arxiv.org/pdf/2103.03874

来源：[1](https://arxiv.org/abs/2103.03874)（采集 2026-11-07）。

### SHA256

a6f448173e57d808a38679dd817bcc2e01324176cbf491d08c43cc0e7ca30bfe

来源：[1](https://arxiv.org/pdf/2103.03874)（采集 2026-11-07）。

### PDF字节数

2030715

来源：[1](https://arxiv.org/pdf/2103.03874)（采集 2026-11-07）。

### Drive资料夹

{
  "id": "1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL",
  "webViewLink": "https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL"
}

来源：[1](https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL)（采集 2026-11-07）。

### 中文文档与本地稿

{
  "chinese_intro_doc": {
    "id": "1s8SrmzMxF5AnMs2uZOKwSfgRQ18Qwu6IH1jsKu7qZ9o",
    "webViewLink": "https://docs.google.com/document/d/1s8SrmzMxF5AnMs2uZOKwSfgRQ18Qwu6IH1jsKu7qZ9o/edit?usp=drivesdk",
    "mimeType": "application/vnd.google-apps.document"
  },
  "local_markdown": "content/benchmarks/math.md"
}

来源：[1](https://drive.google.com/drive/folders/1ltIfNz6lcnYoP3nio5vVLG_Xr8cBeOFL)（采集 2026-11-07）。

### drive_pdf

{
  "id": "1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu",
  "webViewLink": "https://drive.google.com/file/d/1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu/view?usp=drivesdk"
}

来源：[1](https://drive.google.com/file/d/1hvvzCdJR5-kbKHXCnRvEIdKsb-4k6lzu/view?usp=drivesdk)（采集 2026-11-07）。

## 十一、变更记录

### changelog

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。"
  }
]

来源：[1](https://github.com/hendrycks/math)（采集 2026-11-07）。

