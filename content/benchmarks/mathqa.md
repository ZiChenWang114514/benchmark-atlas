# MathQA｜中文深度介绍

从文字应用题生成可执行的运算程序，检验最终答案与可解释计算步骤。

来源：[https://arxiv.org/abs/1905.13319](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 一、基本信息

### 简称

MathQA

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 全称

MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 数据/协议版本

2019 Operation-Based Formalisms数据；未固定本轮数据commit

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 发布日期

2019-05-31（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 板块

数学

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）。

### 子领域

[
  "多步数学应用题"
]

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 许可证

待核实

状态：待核实。

说明：数据、代码、论文和原题权利分开；尚未核实对应发布文件许可证

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/1905.13319

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 代码

https://github.com/math-qa/math-QA

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）。

### 数据集

https://github.com/math-qa/math-QA

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 官网

https://math-qa.github.io/math-QA/

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 论文题名

MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

University of Washington、Allen Institute for AI

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 正式合作方

待核实

状态：待核实。

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 作者

[
  "Amini, Aida",
  "Gabriel, Saadia",
  "Lin, Peter",
  "Koncel-Kedziorski, Rik",
  "Choi, Yejin",
  "Hajishirzi, Hannaneh"
]

说明：arXiv元数据/官网列Peter Lin，下载PDF列Shanchuan Lin；两种署名并列，未自行认定为不同作者或同名。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 当前维护

待核实

状态：待核实。

说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 资助

待核实

状态：待核实。

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

从文字应用题生成可执行的运算程序，检验最终答案与可解释计算步骤。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 设计缺口

仅看自然语言rationale可能掩盖逻辑错误，需要机器可执行、步骤明确的形式语言。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 四、构建方式

### 题源

在AQuA-RAT上重新标注和修正部分题目，以58种运算和6个领域构造形式程序。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 出题/标注人员

Figure Eight众包标注者，作者设计运算接口、质量题与专家抽查。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 审核

程序最终值接近正确答案才可提交，之后验证程序与题目/解释是否逻辑一致，至少2/3验证者认可。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 质量控制

验证通过率94.64%；500题专家样本92%正确（论文口径）；数值碰巧正确仍可能逻辑不对。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://math-qa.github.io/math-QA/)（采集 2026-11-07）。

### 去污染边界

原AQuA题源和众包数据继承公开性，随机划分不是防止语义近重复或LLM污染的充分手段。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 五、数据形式

### 题量

论文正文称37200，表1为37259；两者并列保留，未固定发布文件前不强行选择一个精确数。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 题型

5选1应用题，同时提供运算程序、rationale、领域标签。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 难度

一般应用数学/考试题，涵盖6类领域；不是MATH竞赛集的别名。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 公开/隐藏划分

论文按80%/12%/8%随机划分训练/测试/开发；具体发布包行数与顺序需以文件核验为准。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 六、评测方法

### 指标

答案准确率，程序可执行性和步骤合理性可作补充指标。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 评分实现

执行生成程序得到数值并映射选项；只检查最终数值不足以证明每一步推理正确。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 提示与预算

原论文是程序生成模型，beam search设置不等于现代LLM few-shot；Jev仅给答案accuracy。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 评测脚本

https://github.com/math-qa/math-QA

来源：[1](https://github.com/math-qa/math-QA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 可比性警示

MathQA程序监督、AQuA原rationale和MATH竞赛集不是同一基准；不可只因题源重叠就合并得分。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 最新可确认数据/协议

2019 Operation-Based Formalisms数据；未固定本轮数据commit

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 修订与2026H2收录证据

{
  "arxiv_version": "arXiv v1",
  "history_note": "完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。",
  "2026_h2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.11978v1",
      "date": "2026-10-08",
      "note": "Jev 研究§3.1和表1–2实际使用 MathQA 并比较专用决策模型与通用模型。"
    }
  ]
}

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 饱和判断

待核实

状态：待核实。

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

作者官网明确承认原rationale可能嘈杂/不完整/错误；官网与arXiv元数据作者名Peter Lin、PDF Shanchuan Lin有差异，保持来源原样。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://math-qa.github.io/math-QA/)（采集 2026-11-07）。

### 衍生与排除项

AQuA-RAT的操作程序重标注子集；不应混为原AQuA全部约10万题。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://math-qa.github.io/math-QA/)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 官方榜

待核实

状态：待核实。

说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 二级机构榜

待核实

状态：待核实。

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 限定范围的分数快照

[
  {
    "model_version": "Qwen3.8 Max",
    "score": "94.4",
    "unit": "%",
    "scope_and_protocol": "Jev表2，答案accuracy；checkpoint未明",
    "result_date": "2026-10-08",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2610.11978v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Qwen3.8 Flash",
    "score": "93.3",
    "unit": "%",
    "scope_and_protocol": "同表",
    "result_date": "2026-10-08",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2610.11978v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Gemini 3.8 Flash",
    "score": "92.7",
    "unit": "%",
    "scope_and_protocol": "同表",
    "result_date": "2026-10-08",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2610.11978v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  }
]

来源：[1](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

[
  "amini91@cs.washington.edu"
]

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）；[2](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### Issues

https://github.com/math-qa/math-QA/issues

来源：[1](https://github.com/math-qa/math-QA)（采集 2026-11-07）。

### 官方社交

待核实

状态：待核实。

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### 隐私政策

待核实

状态：待核实。

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

## 十、原始文件

### 原始PDF

https://arxiv.org/pdf/1905.13319

来源：[1](https://arxiv.org/abs/1905.13319)（采集 2026-11-07）。

### SHA256

220cd30ed121d4472bace7ce7a1a80c28cd4ed65669d248d5773ed3b866fdaf2

来源：[1](https://arxiv.org/pdf/1905.13319)（采集 2026-11-07）。

### PDF字节数

850027

来源：[1](https://arxiv.org/pdf/1905.13319)（采集 2026-11-07）。

### Drive资料夹

{
  "id": "1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-",
  "webViewLink": "https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-"
}

来源：[1](https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-)（采集 2026-11-07）。

### 中文文档与本地稿

{
  "chinese_intro_doc": {
    "id": "1YKyOOE-Xx6_XxZAJbkBTqSlXhvtnUM4QRxJCRThRgBs",
    "webViewLink": "https://docs.google.com/document/d/1YKyOOE-Xx6_XxZAJbkBTqSlXhvtnUM4QRxJCRThRgBs/edit?usp=drivesdk",
    "mimeType": "application/vnd.google-apps.document"
  },
  "local_markdown": "content/benchmarks/mathqa.md"
}

来源：[1](https://drive.google.com/drive/folders/1AIl9KnTS86A0rTXfwSmttZaowkUY1LX-)（采集 2026-11-07）。

### drive_pdf

{
  "id": "1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE",
  "webViewLink": "https://drive.google.com/file/d/1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE/view?usp=drivesdk"
}

来源：[1](https://drive.google.com/file/d/1el6sfpgfosIr-ufSW98mtNqP9JJKjeVE/view?usp=drivesdk)（采集 2026-11-07）。

## 十一、变更记录

### changelog

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。"
  }
]

来源：[1](https://math-qa.github.io/math-QA/)（采集 2026-11-07）。

