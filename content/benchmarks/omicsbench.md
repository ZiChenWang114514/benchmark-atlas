# OmicsBench

核查日期：2026-11-07（Asia/Seoul）。本页为官方来源的中文改写；引用、实跑和新发布分别标明，历史成绩不冒充当前SOTA。

## 1. 基本信息

### 简称
OmicsBench
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 全称
OmicsBench
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 数据版本
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文版本
v1；最近论文日期 2026-10-15
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 发布日期
2026-10-15（首个arXiv版本日期；非推定数据上线日）
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 板块
生物与医学
来源：[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）
核查说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 子领域
[
  "研究规模组学多轮分析"
]
来源：[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）

### 许可证
runner/graders MIT；公开任务CC BY 4.0；底层论文数据与参考数据库保留各自许可。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 论文
https://arxiv.org/abs/2610.21074
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 代码仓库
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 数据集
https://huggingface.co/datasets/gideonshaked/OmicsBench
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 官方主页
https://huggingface.co/datasets/gideonshaked/OmicsBench
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 论文题名
OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

## 2. 发起与维护

### 发起方
Gideon Shaked与Siddharth Nagisetty作者团队；正式发起机构待核实。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 合作方
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 作者
[
  "Shaked, Gideon",
  "Nagisetty, Siddharth"
]
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 维护方
gideonshaked/OmicsBench与grader-databases发布账号。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 资助
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 3. 设计目标

### 评测能力
研究规模、长时多轮组学工作流，跨依赖子任务产出可自动检查的生物学分析。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 弥补缺口
一次请求或局部代码片段不能充分测试长工作流、依赖管理及反馈利用。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

## 4. 构建方式

### 题目与数据来源
已发表生物研究与对应公开数据集，按研究工作流拆成任务DAG。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 构建者背景
计算生物学研究生专家策划；writer/reviewer代理辅助后由人工编辑。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 审核流程
writer/reviewer代理最多三轮修改，再由专家修订与QC。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 质量控制
58类确定性生物grader与实体同义词参考库；分步依赖DAG检查。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 去污染
94私有任务控制答案访问，3公开任务作示例；源论文公开及grader反馈可能使记忆/奖励投机仍存在。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

## 5. 数据形式

### 规模
97任务、662子任务、58确定性生物评分器；3公开、94私有。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 任务类型
长时多轮组学数据分析；有向无环依赖子任务。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 模态
组学矩阵、表格、代码、分析产物与文字结果。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 语言
英语任务与生物标识符、Python/R分析环境；语言覆盖统计待核实。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 难度
研究规模而非短题；依赖链及迭代分析是难点。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 公开与隐藏划分
3公开示例、94私有评测任务；runner与参考评分库有公开HF入口。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

## 6. 评测方法

### 指标
任务/子任务生物grader得分；single-pass与gated两协议分开。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 评分方式
确定性grader；gated合格阈值0.7、最多3轮，每任务3次运行。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 提示与运行配置
每轮1800秒；Docker无网络、4核、12GB内存、20GB盘；支持时reasoning high。12模型、3harness、14组合。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 官方脚本
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 可比性警告
模型与harness混杂；gated反馈可能导致reward hacking，因此提升可作为上界而非独立能力提升。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

## 7. 最新情况

### 本轮核查
2026-11-07 Asia/Seoul
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 最新数据版本
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 论文及2026下半年使用证据
{
  "2026_H2_evidence": [
    {
      "url": "https://arxiv.org/html/2610.21074v1",
      "date": "2026-10-15",
      "note": "OmicsBench 原始论文于H2发布并评测研究规模、多轮组学数据分析Agent。"
    }
  ],
  "evidence_boundary": "引用不等于重新运行；本页将论文历史实验与现榜分开。",
  "paper_metadata": {
    "title": "OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics",
    "authors": [
      "Shaked, Gideon",
      "Nagisetty, Siddharth"
    ],
    "release": "2026-10-15",
    "latest": "2026-10-15",
    "version": "v1"
  }
}
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）；[https://arxiv.org/html/2610.21074v1](https://arxiv.org/html/2610.21074v1)（采集 2026-11-07）

### 饱和情况
原论文最佳约0.57/0.67，并未饱和；当前公开在线榜单更新频率待核实。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 污染与争议
私有问题仍源于公开研究；反馈泄漏、grader漏洞与模型/harness耦合是重要解释边界。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 后续衍生
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 8. 榜单快照

### 快照日期
2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期）
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 官方榜/结果入口
https://huggingface.co/datasets/gideonshaked/OmicsBench
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 第三方榜
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 结果快照
2026-10原论文历史：Opus5/OpenCode single-pass0.57/gated0.67；Grok4.3为0.43/0.54。harness OpenCode1.18.11、ClaudeCode2.1.222、Codex0.142.5（按论文记录）；API快照待核实。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 覆盖边界
本轮官方入口与Artificial Analysis / Epoch AI / LMArena定向检索未核实到可比的实时统一榜单；不以检索未命中证明不存在。下列论文分数均是历史快照，不宣称截至采集日SOTA。
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）；[https://artificialanalysis.ai/](https://artificialanalysis.ai/)（采集 2026-11-07）；[https://epoch.ai/](https://epoch.ai/)（采集 2026-11-07）；[https://lmarena.ai/](https://lmarena.ai/)（采集 2026-11-07）

## 9. 联系方式

### 公开学术邮箱
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### Issues
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 官方社交账号
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

### 隐私政策
待核实
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）
核查说明：本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

## 10. 原始文件

### 原始PDF地址
https://arxiv.org/pdf/2610.21074
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 原始PDF SHA256
34555d4ef285b66a95fc368bc903980f44d436e0de2987992bc3729a7f4f0171
来源：[https://arxiv.org/pdf/2610.21074](https://arxiv.org/pdf/2610.21074)（采集 2026-11-07）

### 原始PDF字节数
1891438
来源：[https://arxiv.org/pdf/2610.21074](https://arxiv.org/pdf/2610.21074)（采集 2026-11-07）

### Drive资料夹
{
  "id": "1xJuAwVBG1yPF04Nbzc7zU3ba0C80UKaf",
  "webViewLink": "https://drive.google.com/drive/folders/1xJuAwVBG1yPF04Nbzc7zU3ba0C80UKaf"
}
来源：[https://arxiv.org/abs/2610.21074](https://arxiv.org/abs/2610.21074)（采集 2026-11-07）

### 中文介绍文档
[
  {
    "type": "中文介绍 Google Doc",
    "id": "1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto",
    "webViewLink": "https://docs.google.com/document/d/1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto/edit"
  }
]
来源：[https://docs.google.com/document/d/1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto/edit](https://docs.google.com/document/d/1Rd0YR0hdWTNilcviY6cOx7JbUr4BTkLASeFwL65IKto/edit)（采集 2026-11-07）

Drive原始论文：{
  "id": "1MBjoelJtmqKWsHEhAC4vwW6VbwC4iX6G",
  "webViewLink": "https://drive.google.com/file/d/1MBjoelJtmqKWsHEhAC4vwW6VbwC4iX6G/view"
}

## 11. 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。"
  }
]
来源：https://arxiv.org/abs/2610.21074（采集 2026-11-07）
