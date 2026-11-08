# FullStackBench

> Benchmark Constitution｜深度核验：2026-11-07。访问日沿固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

“FullStack”指跨开发领域与16种编程语言的可执行代码评测，不等于完整网站Agent。此次发现数据授权的官方材料互相冲突，且论文题量与当前HF双语配置行数必须分口径记录。

最近复核

## 基本信息

**简称**：FullStackBench

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**全称**：FullStackBench

核验说明：保留官方名称，不把论文标题自动扩写为全称。

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**基准版本**：公开 3,374 题快照；数据版本号待核实

状态：待核实。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**论文版本**：arXiv v6

核验说明：论文修订版本不等同数据集版本。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**发布日期**：2024-12-01 01:58:42

核验说明：首次 arXiv 论文提交时间，已转；不自动视为数据集首发时间。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**主板块**：代码

核验说明：Benchmark Constitution 编辑归档；跨领域仅主板块计数。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**领域标签**：全栈代码生成

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**许可证与授权边界**：代码根LICENSE与README：Apache-2.0；数据授权存在官方冲突：HF YAML为Apache-2.0，但同卡正文与仓库README徽章均写CC-BY-SA-4.0。数据许可证待核实，重用前应请维护者澄清，不能直接按Apache处理。

状态：待核实。

来源：[1](https://github.com/bytedance/FullStackBench/blob/HEAD/LICENSE)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）；[3](https://huggingface.co/datasets/ByteDance/FullStackBench/blob/main/README.md)（访问2026-11-07）

**论文或技术报告**：https://arxiv.org/abs/2412.00535

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**官方代码**：https://github.com/bytedance/FullStackBench

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**数据地址**：https://huggingface.co/datasets/ByteDance/FullStackBench

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**官方主页**：https://github.com/bytedance/FullStackBench

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**论文题名**：FullStack Bench: Evaluating LLMs as Full Stack Coders

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 发起与维护

**发起方**：ByteDance / Seed Foundation Code Team

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**协作与机构边界**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**作者**：Bytedance, Seed Foundation Code Team

核验说明：v6扉页为团队署名；贡献名单见论文§8。旧版BibTeX个人作者列表与v6团队署名分开，不保留旧自动解析中的冒号伪作者。

来源：[1](https://arxiv.org/abs/2412.00535v6)（访问2026-11-07）

**维护方**：ByteDance FullStackBench 团队

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 设计目标

**测量能力**：跨语言、跨应用领域的实际代码开发与库使用能力。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**相对既有评测的缺口**：简单算法题及从 Python 翻译的多语言题不能充分覆盖全栈场景、外部依赖和真实开发复杂性。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 构建方式

**题目来源**：从GitHub、代码文档/书籍和XLCoST采样代码，再由LLM与人工生成指令、测试和参考解；另邀请各领域编程人员（含内部数据工程团队）撰写领域题目。领域配比参考50万条StackOverflow问题。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**出题与研究背景**：ByteDance 代码模型与执行沙箱研究团队。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**审核流程**：每条按难度、歧义和可解性审核，标注者交换数据交叉修订；分歧通过共识或高级标注员裁决。六模型投票辅助难度划分与样本筛选。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**质量控制**：每题配参考代码与可执行单测；论文共15,168测试、平均4.5/题，并覆盖不同错误类型。以SandboxFusion固定语言及依赖环境运行。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**去污染与泄漏边界**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 数据形式

**规模与口径**：论文v6口径为3,374问题、15,168单测；当前HF en/test与zh/test各1,687行（3,374语言配置行）。保留论文与现发数据两种口径，不把相加行数断言为3,374个互异原题。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://huggingface.co/datasets/ByteDance/FullStackBench/blob/main/README.md)（访问2026-11-07）

**任务类型**：代码生成；记录包括content、canonical_solution、id、labels，以及test.asset/test.code；labels含category、difficulty、programming_language、execution_language、fewshot、is_lctx、locale。

来源：[1](https://huggingface.co/datasets/ByteDance/FullStackBench/raw/main/README.md)（访问2026-11-07）

**模态**：文本；代码

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**语言**：自然语言配置为en和zh；编程语言覆盖16种（官方README）。两种语言配置行数不可当作互不重叠的原题数。

来源：[1](https://huggingface.co/datasets/ByteDance/FullStackBench/raw/main/README.md)（访问2026-11-07）

**难度**：论文v6 Table 1：Easy 1,466、Medium 1,184、Hard 724；六模型投票中仅1个答对列hard，5或6个答对列easy，其余medium。该分布是论文口径，不推定单独HF语言配置也有同一数量。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**公开与隐藏划分**：官方HF卡公开en、zh两个配置，各自只有test划分，各1,687行；含canonical_solution和test字段，不是隐藏答案服务。

来源：[1](https://huggingface.co/datasets/ByteDance/FullStackBench/raw/main/README.md)（访问2026-11-07）

## 评测方法

**指标**：pass@1 / 单次代码功能正确率。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**评分方式**：用 SandboxFusion 在对应语言环境执行生成程序并检查单元测试。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**提示与运行设置**：论文开源模型temperature=0，max_completion_tokens=2048，其余默认；通过SandboxFusion抽取代码、执行单测。第三方报告若预算/语言配置不同，应单列。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**官方复现入口**：https://github.com/bytedance/FullStackBench；使用SandboxFusion服务及src/main.py，README示例镜像固定server-20241204。

来源：[1](https://raw.githubusercontent.com/bytedance/FullStackBench/main/README.md)（访问2026-11-07）

**可比性警告**：不同语言/领域覆盖与执行环境影响结果；该名称不意味着实际构建/上线完整网站的 UI agent。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**数据及热度证据**：```json
{
  "version": "公开 3,374 题快照；数据版本号待核实"
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1"
      "date": "2026-09-23"
      "note": "Hunyuan-A13B §4.1/§4.2及表2–4实际报告 FullStackBench；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。"
    }
  ]
}
```

状态：待核实。

核验说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

来源：[1](https://arxiv.org/html/2609.27284v1)（访问2026-11-07）；[2](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**论文与版本历史**：Submission history From: Siyao Liu [ view email ] [v1] 2024-12-01 01:58:42 (10,754 KB) [v2] 2024-12-04 01:55:24 (11,370 KB) [v3] 2024-12-10 02:31:54 (7,770 KB) [v4] 2024-12-13 01:59:55 (7,769 KB) [v5] 2024-12-20 23:58:59 (7,770 KB) [v6] 2025-05-12 19:24:14 (7,770 KB)

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**饱和程度**：重读v6论文Table 2，历史最高OpenAI o1-preview 65.62%；官网README仍链接静态结果图，不把论文历史结果当作2026实时上限。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）；[2](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**已知问题与局限**：公开测试与任务在后续训练中可能泄漏；题目来源覆盖并不等于无污染证明。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**后续与衍生**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 榜单快照

**快照日期**：2026-11-07

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**官方入口**：https://github.com/bytedance/FullStackBench

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**第三方入口**：待核实

状态：待核实。

核验说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| 厂商自报，配置与原论文不保证一致 | — | Hunyuan-A13B slow-thinking | 67.8 | FullStackBench (%) | 2026-09-23 | [原始来源](https://arxiv.org/html/2609.27284v1) |
| 厂商自报，配置与原论文不保证一致 | — | Hunyuan-A13B fast-thinking | 58.3 | FullStackBench (%) | 2026-09-23 | [原始来源](https://arxiv.org/html/2609.27284v1) |
| 原论文v6 Table 2历史基线 | 1 | OpenAI o1-preview | 65.62 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |
| 原论文v6 Table 2历史基线 | 2 | OpenAI o1-mini | 64.73 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |
| 原论文v6 Table 2历史基线 | 3 | Claude-3.5-Sonnet | 62.57 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |
| 原论文v6 Table 2历史基线 | 4 | GPT-4o-0806 | 61.77 | pass@1 (%) | 2025-05-12 | [原始来源](https://arxiv.org/abs/2412.00535v6) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

核验说明：刷新原论文轨；Hunyuan两条继承前轮已核验的H2报告，未重新读该报告，不称新核验。

**覆盖说明**：官方仓库仅展示静态论文结果图，未取得动态统一榜。新增重新读取的v6 Table 2历史基线；继承的Hunyuan报告自报单列，不能与原论文轨排序。数据授权冲突及当前HF行数口径另见基本信息。

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）；[2](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 联系方式

**公开联系邮箱**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**Issues或讨论入口**：https://github.com/bytedance/FullStackBench/issues

核验说明：公开仓库反馈入口；未发送问题。

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

**官方社交**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

**隐私政策**：待核实

状态：待核实。

核验说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

来源：[1](https://arxiv.org/abs/2412.00535)（访问2026-11-07）

## 原始文件

**原始PDF**：https://arxiv.org/pdf/2412.00535

核验说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

来源：[1](https://arxiv.org/pdf/2412.00535)（访问2026-11-07）

**PDF SHA-256**：d68951598d6b201b93b57ea71052944f28bacd77bd3b6f2c6acb2d46b090fb98

核验说明：下载原始PDF字节计算，非arXiv网页显示大小。

来源：[1](https://arxiv.org/pdf/2412.00535)（访问2026-11-07）

**PDF字节数**：```json
4251352
```

核验说明：实际下载字节数；不代表已上传。

来源：[1](https://arxiv.org/pdf/2412.00535)（访问2026-11-07）

**文件夹**：```json
{
  "id": "1vAewLYiHS2Ta9LHgZgpCyiffgsHzztL0"
  "webViewLink": "
}
```

来源：[1](

**其他官方文档**：```json
[
  {
    "type": "中文介绍Google Doc"
    "id": "1ZQmcPus9I5v9JKGpJDp1aqzVsUk1yzCaXcFVMj-p5Kc"
    "webViewLink": "
  }
]
```

核验说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）；[2](

**论文链接**：```json
{
  "id": "1tq-_KLfUzmLu_gHbuJ4aVoMgkXggG8an"
  "webViewLink": "
}
```

来源：[1](

## 变更记录

**及历史变更**：```json
[
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    "timezone": ""
    最近复核
  }
  {
    "date": "2026-11-07"
    最近复核
  }
]
```

来源：[1](https://github.com/bytedance/FullStackBench)（访问2026-11-07）

