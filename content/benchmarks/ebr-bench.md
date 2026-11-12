# EBR-bench

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

EBR-bench在Earthborne Rangers桌游的初始五个游戏日中，测agent如何规划、管理资源并从重复游玩与笔记中改进。它统计21个目标的完成比例，不是对完整20–25日战役的通关测量；agent只能靠笔记在游戏重置后保留经验，权重不更新。 [1](https://epoch.ai/benchmarks/ebr-bench) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

2026-07-01发布文章的“没有学会”结论对应早期配置。当前方法已到2026-09-22 v4：通常8次学习后2次评分取最好、5个独立样本，另有无学习消融。禁卡、压缩阈值和采样量几经变化，不能把不同版本得分或高绝对分等同学习增益；公开CSV首位均值约0.781。 [1](https://epoch.ai/benchmarks/ebr-bench) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

## 基本信息

- **简称**：EBR-bench [1](https://epoch.ai/benchmarks/ebr-bench)

- **全称**：EBR-bench [1](https://epoch.ai/benchmarks/ebr-bench)

- **基准版本**：v4 methodology（2026-09-22） [1](https://epoch.ai/benchmarks/ebr-bench)

- **论文/报告版本**：2026-07-01网页发布文章；当前方法v4另见benchmark更新记录 [2](https://epoch.ai/publications/earthborne-rangers-benchmark) [1](https://epoch.ai/benchmarks/ebr-bench)

- **发布日期**：2026-07-01（Epoch发布文章日期） [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

- **主板块**：Agent [1](https://epoch.ai/benchmarks/ebr-bench) 注：编辑归档，不代表官方分类。

- **子领域**：持续学习；游戏 [1](https://epoch.ai/benchmarks/ebr-bench) 注：编辑归档，不代表官方分类。

- **论文/报告**：https://epoch.ai/publications/earthborne-rangers-benchmark [2](https://epoch.ai/publications/earthborne-rangers-benchmark) 注：网页研究文章，不冒充arXiv/PDF。

- **官方主页**：https://epoch.ai/benchmarks/ebr-bench [1](https://epoch.ai/benchmarks/ebr-bench)

- **报告标题**：AI doesn't get better at this board game with practice [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

**仍待核实**（不推断为未公开）：

- 许可证与限制：已检查正式发表材料，尚未确认覆盖任务数据/游戏资产的明确使用授权；软件、匿名预发布数据和商业游戏的许可证不能互套。 [1](https://epoch.ai/benchmarks/ebr-bench)
- 官方代码：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://epoch.ai/benchmarks/ebr-bench)
- 数据入口：可读https://epoch.ai/data/benchmarks.csv仅含模型评测结果，不是原游戏任务/卡牌材料；正式任务数据发布地址尚未定位。 [1](https://epoch.ai/benchmarks/ebr-bench) [3](https://epoch.ai/data/benchmarks.csv)

## 发起与维护

- **发起方**：Epoch AI [1](https://epoch.ai/benchmarks/ebr-bench)

- **合作方**：Generality Labs受Epoch委托独立审计；Earthborne Games并非研究合作或背书方，Epoch明确称独立开展。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **核心作者**：Benjamin Ou；Greg Burnham [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

- **维护方**：Epoch AI [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 设计目标

- **核心能力**：通过反复游玩陌生复杂桌游Earthborne Rangers，衡量记笔记、长期策略与从经验中学习的能力。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **相对已有评测的缺口**：不只检查首次答题，而是在同一任务连续尝试后是否改善；表现分和学习增益必须区分。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 构建方式

- **题目来源**：独立数字化游戏初始五个游戏日；从任务、奖励及重要事件定义21个可得目标。游戏版权属于Earthborne Games，不代表其参与基准开发。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **审核流程**：Generality Labs受Epoch委托于2026年7月审核v1；肯定游戏设计，同时质疑持续学习诱发与上下文整理；8月27日修复一个引擎bug。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **质量控制**：Generality Labs受Epoch委托于2026年7月审核v1；肯定游戏设计，同时质疑持续学习诱发与上下文整理；8月27日修复一个引擎bug。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **防污染/运行完整性**：选用较冷门游戏降低记忆可能，但不是检索式去重或可验证训练截断保证；v4从参考材料和游戏中同时移除可绕过战略难点的一张卡，主要是有效性修正而非训练去污染。 [1](https://epoch.ai/benchmarks/ebr-bench) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：正式方法页可确认发布维护机构，但未找到足以确认作者姓名/出题者资格的署名或方法细目。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 数据形式

- **规模**：每run 10次游玩：8次学习、最后2次评分；每模型通常5个独立样本，旧实验10个；每次最多21目标。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **题型**：卡牌查阅、路线规划、笔记管理和多步游戏决策。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **模态**：文本；地图图像；工具调用 [1](https://epoch.ai/benchmarks/ebr-bench)

- **难度与任务跨度**：重复游玩五个游戏日的入门战役；完整战役20–25日。单次人类熟手约2–4小时，需战略组牌、战术资源管理和跨局笔记；不能当作一般终身学习的直接测量。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **公开与隐藏划分**：Epoch明确不分发或出售底层受版权保护游戏材料；公开的是方法与成绩，完整游戏及评测数据许可待核实。 [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 语言覆盖：正式方法页说明为英文，但没有完整披露任务指令、程序/游戏内容的语言覆盖，不能仅据报告语言确定全量语种。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 评测方法

- **指标**：Topline：每run最后两次得分取较高，再跨样本汇总；得分为21目标比例；另研究消融学习增益。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **评分规则**：以完成目标计分，不把游戏高分直接视为持续学习增益；学习增益需与仅两次游玩的消融对照。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **提示与运行配置**：默认单agent、禁用特定卡牌，250k token压缩阈值；Fable系列用标称上下文90%；ReAct与Deep Agent多agent分开。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **可比性限制**：v1/v2计分变更、v3压缩阈值取优、v4禁卡和采样量更改导致历史不完全可比；默认单agent不混多agent。 [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 最新情况

- **核验日期**：2026-11-07 [1](https://epoch.ai/benchmarks/ebr-bench)

- **现行版本与采用证据**：version：v4 methodology（2026-09-22）；trending：A；heat_evidence：官方2026-09-22更新v4并在10月审计回应中报告新模型学习结果；本次重读Epoch CSV可见11月2日Mistral Large 4运行。A为候选分级，不据此声称多个独立创建机构。；evidence_2026_h2：url：https://epoch.ai/benchmarks/ebr-bench；date：2026-11-07；date_type：observed_on；note：本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **更新与修订**：网页方法更新：2026-07-27 v2改为末两局取最好并加入ablated learning；08-11 v3比较压缩阈值；08-19加入人类实验；09-22 v4禁卡、默认5样本、统一大多数模型250k压缩，并将非默认学习图转内部分析。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **饱和度判断**：当前CSV最高mean_score约0.781；方法页称前沿模型偶尔达顶尖人类表现，但默认成绩不等于学习增益。满分21目标，人类已有21/21。 [1](https://epoch.ai/benchmarks/ebr-bench) [3](https://epoch.ai/data/benchmarks.csv)

- **已知问题与证据边界**：v1/v2计分变更、v3压缩阈值取优、v4禁卡和采样量更改导致历史不完全可比；默认单agent不混多agent。 [1](https://epoch.ai/benchmarks/ebr-bench)

- **关联与衍生关系**：Earthborne Rangers为游戏名，EBR-bench为Epoch研究基准；与游戏本体版权及作者关系区分。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 榜单快照

- **快照采集日**：2026-11-07 [1](https://epoch.ai/benchmarks/ebr-bench)

- **官方榜/正式委托榜**：https://epoch.ai/benchmarks/ebr-bench [1](https://epoch.ai/benchmarks/ebr-bench)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | GPT-6.1 Terra (max) | 0.780952380952381 | CSV mean_score (0–1；21目标比例)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 2 | GPT-6 Astra (max) | 0.7619047619047619 | CSV mean_score (0–1；21目标比例)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 3 | Claude Opus 5.5 (max) | 0.7142857142857142 | CSV mean_score (0–1；21目标比例)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 4 | Gemini 4 Argon (high) | 0.6476190476190476 | CSV mean_score (0–1；21目标比例)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 5 | Claude Fable 5.1 (max) | 0.5714285714285714 | CSV mean_score (0–1；21目标比例)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |

> GPT-6.1 Terra (max)：stderr：0.05128728387747146；run_id：65SHyNJX5oxVADzzjkssFK；started_at：2026-10-27；note：按当前CSV均值排序，task version为空，不能认证全部为统一v4禁卡协议。 [3](https://epoch.ai/data/benchmarks.csv)

> GPT-6 Astra (max)：stderr：0.08384198505551908；run_id：GhVYxWxttDxZ7akiJQPYsE；started_at：2026-08-31；note：按当前CSV均值排序，task version为空，不能认证全部为统一v4禁卡协议。 [3](https://epoch.ai/data/benchmarks.csv)

> Claude Opus 5.5 (max)：stderr：0.07063046178186345；run_id：iKWWUmcuzRjqisoshKVEpL；started_at：2026-09-23；note：按当前CSV均值排序，task version为空，不能认证全部为统一v4禁卡协议。 [3](https://epoch.ai/data/benchmarks.csv)

> Gemini 4 Argon (high)：stderr：0.04902681019517619；run_id：mSJNKA7nCp2eZVqMo5nTUP；started_at：2026-10-14；note：按当前CSV均值排序，task version为空，不能认证全部为统一v4禁卡协议。 [3](https://epoch.ai/data/benchmarks.csv)

> Claude Fable 5.1 (max)：stderr：0.06023386019368341；run_id：8JukffGviNAYHXSdTJvswB；started_at：2026-09-08；note：按当前CSV均值排序，task version为空，不能认证全部为统一v4禁卡协议。 [3](https://epoch.ai/data/benchmarks.csv)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：当前CSV重读并按task=EBR-bench精确筛选；task version字段为空，保留run_id与运行起始时间。与方法页所列v1/v2/v3/v4存在可比性限制；CSV未提供统一榜表更新时间，不用采集日代替。 [3](https://epoch.ai/data/benchmarks.csv) [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 联系方式

- **官方社交**：https://x.com/EpochAIResearch [1](https://epoch.ai/benchmarks/ebr-bench)

- **隐私政策**：https://epoch.ai/privacy [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://epoch.ai/benchmarks/ebr-bench)
- 公开问题追踪：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 原始文件

- **其他正式文档**：type：官方研究文章，非独立PDF；url：https://epoch.ai/publications/earthborne-rangers-benchmark；type：模型成绩CSV，不是任务数据；url：https://epoch.ai/data/benchmarks.csv [1](https://epoch.ai/benchmarks/ebr-bench) [3](https://epoch.ai/data/benchmarks.csv)

- **中的论文副本**：待核实 [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 原始PDF：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://epoch.ai/benchmarks/ebr-bench)
- SHA-256：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://epoch.ai/benchmarks/ebr-bench)
- PDF字节数：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://epoch.ai/benchmarks/ebr-bench)
- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [1](https://epoch.ai/benchmarks/ebr-bench)

## 变更记录

- date：2026-11-07；change：首次建立近期热门中文研究条目。Earthborne Rangers为游戏名，EBR-bench为Epoch研究基准；与游戏本体版权及作者关系区分。 热度与榜单口径分离，不确定值标记待核实。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://epoch.ai/benchmarks/ebr-bench)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
