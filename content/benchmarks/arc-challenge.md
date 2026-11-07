# ARC-Challenge｜中文深度介绍

在基础科学考试题上测量超越检索与词语共现的知识整合和推理。

来源：[https://arxiv.org/abs/1803.05457](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 一、基本信息

### 简称

ARC-Challenge

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 全称

AI2 Reasoning Challenge — Challenge Set

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 数据/协议版本

ARC-Challenge（2018）；不包含ARC-Easy

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）；[2](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 论文版本

arXiv v1

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 发布日期

2018-03-15（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 板块

推理

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）。

### 子领域

[
  "科学常识与组合推理"
]

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 许可证

待核实

状态：待核实。

说明：数据、代码、论文和原题权利分开；尚未核实对应发布文件许可证

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/1803.05457

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 代码

https://github.com/allenai/arc-solvers

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）。

### 数据集

https://github.com/allenai/arc-solvers

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）；[2](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 官网

http://data.allenai.org/arc

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）；[2](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 论文题名

Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

Allen Institute for AI

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 正式合作方

待核实

状态：待核实。

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 作者

[
  "Clark, Peter",
  "Cowhey, Isaac",
  "Etzioni, Oren",
  "Khot, Tushar",
  "Sabharwal, Ashish",
  "Schoenick, Carissa",
  "Tafjord, Oyvind"
]

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 当前维护

待核实

状态：待核实。

说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 资助

待核实

状态：待核实。

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

在基础科学考试题上测量超越检索与词语共现的知识整合和推理。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 设计缺口

既有选择问答可能被信息检索或词汇统计解决，难以单独衡量更深推理。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 四、构建方式

### 题源

收集3至9年级科学考试选择题；同时被检索和PMI基线答错的题进入Challenge。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 出题/标注人员

原始考试命题者与AI2整理团队；不是全部由LLM合成。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 审核

对题目清理并以两个基线筛选；不含必须依赖图像才能回答的问题。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 质量控制

保留多种科学学科和推理需求，原论文另给约1400万句科学语料供检索。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 去污染边界

Easy/Challenge依据基线表现划分，不构成预训练语料隔离；考试题可能已在网络公开。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 五、数据形式

### 题量

Challenge 2590题：训练1119、开发299、测试1172；整个ARC为7787题，不能当Challenge题量。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 题型

文本科学选择题，多为4选项，部分3至5选项。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 难度

Challenge仅表示被原检索与PMI模型筛掉的集合；不是固定的2026前沿难度。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 公开/隐藏划分

公开训练、开发和测试题文件；现代常用测试1172题。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 六、评测方法

### 指标

答案准确率；原论文对并列预测允许1/k分数。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 评分实现

原始tie-credit与现代生成答案accuracy/对数似然acc_norm实现不同，必须保留评测器设置。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 提示与预算

原论文包含检索与监督QA系统；LLM需要报告shot数、CoT、是否检索及似然长度归一化。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 评测脚本

https://github.com/allenai/arc-solvers

来源：[1](https://github.com/allenai/arc-solvers)（采集 2026-11-07）；[2](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 可比性警示

ARC-Challenge不是ARC-Easy、更不是视觉抽象推理ARC-AGI；1172题和合并3548题结果不可混排。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 最新可确认数据/协议

ARC-Challenge（2018）；不包含ARC-Easy

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）；[2](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 修订与2026H2收录证据

{
  "arxiv_version": "arXiv v1",
  "history_note": "完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。",
  "2026_h2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.11978v1",
      "date": "2026-10-08",
      "note": "Jev 研究表1–2及§3.1实际在 ARC-Challenge 上比较多类模型，不将ARC-Easy或其它子集另计。"
    }
  ]
}

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 饱和判断

待核实

状态：待核实。

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

旧考试题和公开答案存在污染风险；高分不能自动证明系统具有广泛科学研究能力。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）；[2](http://data.allenai.org/arc)（采集 2026-11-07）。

### 衍生与排除项

同家族ARC-Easy单独划分；本条只收录Challenge，不重复计数。

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）；[2](http://data.allenai.org/arc)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 官方榜

http://data.allenai.org/arc

来源：[1](https://github.com/allenai/arc-solvers)（采集 2026-11-07）；[2](http://data.allenai.org/arc)（采集 2026-11-07）。

### 二级机构榜

待核实

状态：待核实。

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 限定范围的分数快照

[
  {
    "model_version": "Jev",
    "score": "97.6",
    "unit": "%",
    "scope_and_protocol": "Jev表2，1172题；Jev checkpoint未明确",
    "result_date": "2026-10-08",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2610.11978v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Gemini 3.8 Flash",
    "score": "97.5",
    "unit": "%",
    "scope_and_protocol": "同表",
    "result_date": "2026-10-08",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2610.11978v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Qwen3.8 Flash",
    "score": "96.2",
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

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

待核实

状态：待核实。

说明：未从已核实官方材料收录专门联系邮箱；不猜测个人邮箱

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### Issues

https://github.com/allenai/arc-solvers/issues

来源：[1](https://github.com/allenai/arc-solvers)（采集 2026-11-07）。

### 官方社交

待核实

状态：待核实。

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### 隐私政策

待核实

状态：待核实。

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

## 十、原始文件

### 原始PDF

https://arxiv.org/pdf/1803.05457

来源：[1](https://arxiv.org/abs/1803.05457)（采集 2026-11-07）。

### SHA256

b24b722c93f304df6c3b4a48ebbe429e836f3b3e80837bb613112398e59bde43

来源：[1](https://arxiv.org/pdf/1803.05457)（采集 2026-11-07）。

### PDF字节数

290564

来源：[1](https://arxiv.org/pdf/1803.05457)（采集 2026-11-07）。

### Drive资料夹

{
  "id": "1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk",
  "webViewLink": "https://drive.google.com/drive/folders/1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk"
}

来源：[1](https://drive.google.com/drive/folders/1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk)（采集 2026-11-07）。

### 中文文档与本地稿

{
  "chinese_intro_doc": {
    "id": "1zeiTeYn28Vz7H0h4mPOEjzt7SDBGXmYdmKRcXs2_g24",
    "webViewLink": "https://docs.google.com/document/d/1zeiTeYn28Vz7H0h4mPOEjzt7SDBGXmYdmKRcXs2_g24/edit?usp=drivesdk",
    "mimeType": "application/vnd.google-apps.document"
  },
  "local_markdown": "content/benchmarks/arc-challenge.md"
}

来源：[1](https://drive.google.com/drive/folders/1hOZWrRuLGFb18AWzwJHfyFuJuPV_yLnk)（采集 2026-11-07）。

### drive_pdf

{
  "id": "1cz7sR0Bva9EQIZUhXIjebI5QWfMWtr6Q",
  "webViewLink": "https://drive.google.com/file/d/1cz7sR0Bva9EQIZUhXIjebI5QWfMWtr6Q/view?usp=drivesdk"
}

来源：[1](https://drive.google.com/file/d/1cz7sR0Bva9EQIZUhXIjebI5QWfMWtr6Q/view?usp=drivesdk)（采集 2026-11-07）。

## 十一、变更记录

### changelog

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。"
  }
]

来源：[1](http://data.allenai.org/arc)（采集 2026-11-07）。

