# miniF2F｜中文深度介绍

用形式化数学系统核验生成证明，并在不同定理证明器间建立共同竞赛数学评测。

来源：[https://arxiv.org/abs/2109.00110](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 一、基本信息

### 简称

miniF2F

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 全称

miniF2F: a cross-system benchmark for formal Olympiad-level mathematics

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 数据/协议版本

原版v1跨系统集合；现代Lean4移植需另记commit

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 发布日期

2021-09-01（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 板块

数学

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）。

### 子领域

[
  "Lean形式化数学证明"
]

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 许可证

{
  "Metamath": "MIT",
  "Lean/Isabelle": "Apache-2.0（按原论文说明，fork需复核）"
}

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/2109.00110

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 代码

https://github.com/openai/miniF2F

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）。

### 数据集

https://github.com/openai/miniF2F

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 官网

https://github.com/openai/miniF2F

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 论文题名

MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

École Polytechnique、OpenAI、University of Pittsburgh（论文署名）

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 正式合作方

待核实

状态：待核实。

说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 作者

[
  "Zheng, Kunhao",
  "Han, Jesse Michael",
  "Polu, Stanislas"
]

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 当前维护

待核实

状态：待核实。

说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 资助

待核实

状态：待核实。

说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

用形式化数学系统核验生成证明，并在不同定理证明器间建立共同竞赛数学评测。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 设计缺口

非形式化最终答案评分不能严格证明推理正确，且旧形式化库题目难度与竞赛数学不一致。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 四、构建方式

### 题源

从AMC、AIME、IMO、MATH及高中/本科数学题人工形式化，跨Lean、Metamath、Isabelle、HOL Light。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 出题/标注人员

具备形式化数学技能的研究者人工翻译题面和定理陈述，适配各证明系统。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 审核

由各系统检查形式化陈述及证明；不同系统覆盖程度并不完全相同。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 质量控制

488个题目按类型和难度分层划分验证与测试，避免只集中单一竞赛类型。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 去污染边界

公开题目与形式陈述可进入预训练；内核通过仍需检查是否调用sorry、axiom或过强假设。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 五、数据形式

### 题量

488题：验证244、测试244；原版为跨系统benchmark，不只Lean4。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 题型

输入形式化定理陈述、生成证明脚本，由证明内核检查。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 模态

形式化符号/代码与数学文本

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 难度

奥赛及高中/本科数学；形式化陈述有时给出答案或witness，会改变相对于原题的难度。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 公开/隐藏划分

公开valid/test各244；训练时不得把测试证明或同题变体混入而不披露。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 六、评测方法

### 指标

固定搜索预算下的证明成功率、pass@N等；本轮H2研究另使用PAB。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 评分实现

正确性由形式系统内核判定；还需审计依赖的公理和被信任环境，编译成功本身不等同无漏洞证明。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 提示与预算

MCTS研究固定Lean4.15、Mathlib4.15(commit9837ca9d)、KiminaServer2.0，5个种子；预算PAB需保留。

来源：[1](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 评测脚本

https://github.com/openai/miniF2F

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 可比性警示

Lean3/Lean4、Mathlib版本、tactic集合、尝试数和PAB不同不可直接跨表比较。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）；[2](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 最新可确认数据/协议

原版v1跨系统集合；现代Lean4移植需另记commit

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 修订与2026H2收录证据

{
  "arxiv_version": "arXiv v2",
  "history_note": "完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。",
  "2026_h2_evidence": [
    {
      "url": "https://arxiv.org/html/2608.28639v1",
      "date": "2026-08-11",
      "note": "Reward-Oracle MCTS 原始研究实际在 miniF2F 上比较三个证明模型及不同搜索预算；同时审计内核级证明有效性。"
    }
  ]
}

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）；[2](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 饱和判断

待核实

状态：待核实。

说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）；[2](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

H2 MCTS研究的sorryAx问题影响PutnamBench审计；作者明确本研究miniF2F成功证明未依赖sorryAx，不能把别的集合漏洞移植成miniF2F结论。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）；[2](https://github.com/openai/miniF2F)（采集 2026-11-07）；[3](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 衍生与排除项

Lean4移植与各证明器fork应标明源码commit；不能把所有fork的分数归于同一固定v1工具链。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）；[2](https://github.com/openai/miniF2F)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 官方榜

待核实

状态：待核实。

说明：本轮未确认独立持续更新的官方榜；论文实验不冒充官方实时榜

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 二级机构榜

待核实

状态：待核实。

说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 限定范围的分数快照

[
  {
    "model_version": "Goedel-Prover-V2-8B + MCTS",
    "score": "87.1 ± 0.2",
    "unit": "%",
    "scope_and_protocol": "miniF2F test244，PAB256，5种子",
    "result_date": "2026-08-11",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2608.28639v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "Goedel-Prover-V2-8B + MCTS",
    "score": "84.2 ± 0.5",
    "unit": "%",
    "scope_and_protocol": "同研究，PAB32；与上一行不同预算",
    "result_date": "2026-08-11",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2608.28639v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  },
  {
    "model_version": "DeepSeek-Prover-V2-7B + MCTS",
    "score": "82.6 ± 0.1",
    "unit": "%",
    "scope_and_protocol": "test244，PAB256",
    "result_date": "2026-08-11",
    "snapshot_date": "2026-11-07",
    "source_url": "https://arxiv.org/html/2608.28639v1",
    "source_class": "研究论文实验，非官方实时榜",
    "checkpoint_note": "模型名按来源原样；若来源未列API checkpoint则不补造。"
  }
]

来源：[1](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）；[2](https://arxiv.org/html/2608.28639v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

[
  "kunhao.zheng@polytechnique.edu",
  "jessemichaelhan@openai.com"
]

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）；[2](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### Issues

https://github.com/openai/miniF2F/issues

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）。

### 官方社交

待核实

状态：待核实。

说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### 隐私政策

待核实

状态：待核实。

说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

## 十、原始文件

### 原始PDF

https://arxiv.org/pdf/2109.00110

来源：[1](https://arxiv.org/abs/2109.00110)（采集 2026-11-07）。

### SHA256

e4dcbd37330caffea6ebe2baa0f2f4cd3596d8a873c00f44ea2ce62ab0aaeea2

来源：[1](https://arxiv.org/pdf/2109.00110)（采集 2026-11-07）。

### PDF字节数

267937

来源：[1](https://arxiv.org/pdf/2109.00110)（采集 2026-11-07）。

### Drive资料夹

{
  "id": "1Z3ygLn9nvmJ7OL77CifV-VTo5oGqwfIa",
  "webViewLink": "https://drive.google.com/drive/folders/1Z3ygLn9nvmJ7OL77CifV-VTo5oGqwfIa"
}

来源：[1](https://drive.google.com/drive/folders/1Z3ygLn9nvmJ7OL77CifV-VTo5oGqwfIa)（采集 2026-11-07）。

### 中文文档与本地稿

{
  "chinese_intro_doc": {
    "id": "1SmDycpie2iIEWiJN5gjyYjX8Uqpogk5wCu4yuuFHLug",
    "webViewLink": "https://docs.google.com/document/d/1SmDycpie2iIEWiJN5gjyYjX8Uqpogk5wCu4yuuFHLug/edit?usp=drivesdk",
    "mimeType": "application/vnd.google-apps.document"
  },
  "local_markdown": "content/benchmarks/minif2f.md"
}

来源：[1](https://drive.google.com/drive/folders/1Z3ygLn9nvmJ7OL77CifV-VTo5oGqwfIa)（采集 2026-11-07）。

### drive_pdf

{
  "id": "1B_2BIieglqoGSpFwqs_vdOHBFMK1e4U8",
  "webViewLink": "https://drive.google.com/file/d/1B_2BIieglqoGSpFwqs_vdOHBFMK1e4U8/view?usp=drivesdk"
}

来源：[1](https://drive.google.com/file/d/1B_2BIieglqoGSpFwqs_vdOHBFMK1e4U8/view?usp=drivesdk)（采集 2026-11-07）。

## 十一、变更记录

### changelog

[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。"
  }
]

来源：[1](https://github.com/openai/miniF2F)（采集 2026-11-07）。

