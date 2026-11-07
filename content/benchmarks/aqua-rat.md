# AQuA-RAT｜中文深度介绍

从代数文字题生成自然语言推理依据并选择答案，研究rationale对求解和解释的帮助。

来源：[https://arxiv.org/abs/1705.04146](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

## 一、基本信息

### 简称

AQuA-RAT

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 全称

Algebra Question Answering with Rationales

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 数据/协议版本

公开众包release与原论文实验版不同；须指定发布文件

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 论文版本

arXiv v3

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 发布日期

2017-05-11（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 板块

数学

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）。

### 子领域

[
  "代数应用题与推理"
]

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 许可证

待核实

状态：待核实。

说明：数据、代码、论文和原题权利分开；尚未核实对应发布文件许可证

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/1705.04146

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 代码

https://github.com/google-deepmind/AQuA

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）。

### 数据集

https://github.com/google-deepmind/AQuA

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 官网

https://github.com/google-deepmind/AQuA

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 论文题名

Program Induction by Rationale Generation : Learning to Solve and Explain Algebraic Word Problems

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

DeepMind、University of Oxford（论文署名）

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 正式合作方

待核实

状态：待核实。

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 作者

[
  "Ling, Wang",
  "Yogatama, Dani",
  "Dyer, Chris",
  "Blunsom, Phil"
]

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 当前维护

待核实

状态：待核实。

说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 资助

待核实

状态：待核实。

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

从代数文字题生成自然语言推理依据并选择答案，研究rationale对求解和解释的帮助。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 设计缺口

只预测选项无法观察模型如何组织数学推理；原工作同时建模解释。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

## 四、构建方式

### 题源

论文收集GRE/GMAT风格网络题种子并用众包扩展；官方README强调公开release为完整众包数据。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 出题/标注人员

众包写题与写解释，研究团队开发rationale生成模型。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 审核

众包流程与去近重复过滤；公开发布版本与论文初始实验数据并非完全相同。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 质量控制

原论文按编辑距离过滤近重复；README明确原版本不能完整公开，复现实验应使用公开release口径。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 去污染边界

编辑距离过滤针对近重复，不保证语义改写分离或后续LLM无污染。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

## 五、数据形式

### 题量

原论文过滤后训练100949、开发250、测试250；公开release具体计数须以文件实测为准，Jev测试口径254，不能默认为同一版。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（采集 2026-11-07）。

### 题型

每题question、5个options、rationale、correct，正确选项A–E。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 难度

代数应用题/考试风格；rationale存在多种写法，答案正确不意味着解释逻辑完备。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 公开/隐藏划分

官方公开train/dev/test及对应tok文件；原论文实验版无法完全公开，README明确说明结果会不同。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（采集 2026-11-07）。

## 六、评测方法

### 指标

选项准确率；原论文还报告rationale的BLEU-4/困惑度，现代评测通常只看答案。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 评分实现

预测选项与correct对比；若评解释应独立报告，不能用选项accuracy替代解释质量。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 提示与预算

原工作监督训练生成rationale后作答；CoT演示数、token预算及答案抽取需另外说明。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 评测脚本

https://github.com/google-deepmind/AQuA

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 可比性警示

原论文250测试与公开/Jev254测试、tok与untok、是否评价rationale均需区分。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 最新可确认数据/协议

公开众包release与原论文实验版不同；须指定发布文件

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 修订与2026H2收录证据

{
  "arxiv_version": "arXiv v3",
  "history_note": "完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。",
  "2026_h2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.11978v1",
      "date": "2026-10-08",
      "note": "Jev 研究§3.1和表1–2实际使用 AQuA-RAT 并比较专用决策模型与通用模型。"
    }
  ]
}

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 饱和判断

待核实

状态：待核实。

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

官方明确公开版不同于初始发表版，这是版本冲突而非采集者可自行修正的笔误。

来源：[1](https://raw.githubusercontent.com/google-deepmind/AQuA/master/README.md)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 衍生与排除项

MathQA从AQuA题源重标运算程序；两者不能按相同数据及评分方式处理。

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 官方榜

待核实

状态：待核实。

说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 二级机构榜

待核实

状态：待核实。

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 限定范围的分数快照

[
  {
    "model_version": "Qwen3.8 Max",
    "score": "94.1",
    "unit": "%",
    "scope_and_protocol": "Jev表2 AQuA；附录测试254",
    "result_date": "2026-10-08",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2610.11978v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Qwen3.8 Flash",
    "score": "91.7",
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
    "score": "91.3",
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

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

[
  "lingwang@google.com"
]

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）；[2](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### Issues

https://github.com/google-deepmind/AQuA/issues

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）。

### 官方社交

待核实

状态：待核实。

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### 隐私政策

待核实

状态：待核实。

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

## 十、原始文件

### 原始PDF

https://arxiv.org/pdf/1705.04146

来源：[1](https://arxiv.org/abs/1705.04146)（采集 2026-11-07）。

### SHA256

5111754b10c77d287685cc64992c92989eecc9b7cca65089f97c0efd48a4feb7

来源：[1](https://arxiv.org/pdf/1705.04146)（采集 2026-11-07）。

### PDF字节数

534332

来源：[1](https://arxiv.org/pdf/1705.04146)（采集 2026-11-07）。

### Drive资料夹

{
  "id": "14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc",
  "webViewLink": "https://drive.google.com/drive/folders/14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc"
}

来源：[1](https://drive.google.com/drive/folders/14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc)（采集 2026-11-07）。

### 中文文档与本地稿

{
  "chinese_intro_doc": {
    "id": "1eZjRI88WySYba1wenrGtoejhe6_rdLemJEcXKXDbWLU",
    "webViewLink": "https://docs.google.com/document/d/1eZjRI88WySYba1wenrGtoejhe6_rdLemJEcXKXDbWLU/edit?usp=drivesdk",
    "mimeType": "application/vnd.google-apps.document"
  },
  "local_markdown": "content/benchmarks/aqua-rat.md"
}

来源：[1](https://drive.google.com/drive/folders/14h-nu4DAu3Vs6hx0zge6frTv-jqcw9Vc)（采集 2026-11-07）。

### drive_pdf

{
  "id": "1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J",
  "webViewLink": "https://drive.google.com/file/d/1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J/view?usp=drivesdk"
}

来源：[1](https://drive.google.com/file/d/1gjTQogYMjSS4Mf4MbpT3wwXbuZawnC5J/view?usp=drivesdk)（采集 2026-11-07）。

## 十一、变更记录

### changelog

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。"
  }
]

来源：[1](https://github.com/google-deepmind/AQuA)（采集 2026-11-07）。

