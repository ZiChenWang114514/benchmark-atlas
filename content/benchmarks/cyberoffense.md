# CyberOffense

> 深度核验：2026-11-07（KST / Asia/Seoul）。未知不等于未公开；网页更新日、运行日与访问日分开记录。

已核验存在；11节研究快照；note: trending: B；未知字段保留待核实

CyberOffense使用Nova和Lighthouse两个隔离企业网络靶场，观察agent能否在长程、多步骤探索中完成授权目标。它不靠自报成功，而是检查命令输出是否含有私有答案键对应的隐藏marker；每次运行重建靶场并审查捷径。此处只记录评测协议与汇总成绩，不复述具体攻击步骤。 [1](https://www.vals.ai/benchmarks/cyber_offense)

每次最多48小时、累计500M token（含缓存和推理）。Nova领先两模型各三次取均值，其他多为单次；21个与31个目标必须分列，不能把原始目标数相加成“总体成功率”。2026-10-23网页报告中没有模型完成Lighthouse最终阶段，完整任务完成度仍显著低于部分目标得分。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 基本信息

- **简称**：CyberOffense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **全称**：CyberOffense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **论文/报告版本**：2026年10月网页研究报告 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **主板块**：安全 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **子领域**：自主网络安全评测；多步靶场任务 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **许可证与限制**：专有评测（Vals目录标记Proprietary）；不等于开源软件许可 [2](https://www.vals.ai/benchmarks/)

- **论文/报告**：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense) 注：官方BibTeX将本页作为2026年10月网页研究报告引用；不是arXiv论文或PDF。

- **官方主页**：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **报告标题**：Evaluating frontier AI systems on realistic multi-step cybersecurity tasks [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 基准版本：已读取本轮所列论文/数据卡/README；未确认可追踪的正式版本编号。运行镜像tag、网页更新日与数据版本不混同。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- 发布日期：已核对正式页的更新日期；尚不能把榜单更新日或本轮访问日当作首次发布日期。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- 官方代码：已检查正式方法页和所指向的代码入口；本轮未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- 数据入口：已检查正式方法页及其外链；本轮未定位经维护方确认的任务数据仓库/HF卡，不将结果表或上游数据充作完整题库。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 发起与维护

- **发起方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber_offense)

- **核心作者**：Nikil Ravi；Hung Tran；Langston Nashold；Rayan Krishnan [1](https://www.vals.ai/benchmarks/cyber_offense)

- **维护方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 合作方：本轮正式材料不足以确认独立研究合作方；工具提供者、模型厂商和上游仓库不能据此当作合作机构。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 设计目标

- **核心能力**：在隔离企业网络靶场中长程、多步骤、自主完成授权网络安全目标。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **相对已有评测的缺口**：区别于短程单独CTF，评估跨完整组织网络的长期规划、证据利用与串联能力。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 构建方式

- **题目来源**：Nova与Lighthouse两个模拟企业网络靶场。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **审核流程**：发布方称逐次审查运行并检查捷径；私有answer key不供模型读取。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **质量控制**：每次全新靶场；隐藏标记只由真正达到目标取得，检查记录输出而非相信模型自报。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **防污染/运行完整性**：每次运行重置新靶场，隐藏marker与私有答案键；发布方逐次审查并称未发现捷径或答案键读取。此为运行完整性措施，不能证明模型预训练完全无污染。 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：正式方法页可确认发布维护机构，但本轮未找到足以确认作者姓名/出题者资格的署名或方法细目。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 数据形式

- **规模**：2个靶场：Nova 21目标、Lighthouse 31目标；当前报告7模型。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **题型**：自主多步骤靶场交互；仅讨论评测协议，本页不提供攻击操作指导。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **模态**：文本指令；终端输出；隔离网络环境 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **难度与任务跨度**：Nova多域企业网络；Lighthouse跨两个企业网络的长程任务。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **公开与隐藏划分**：评分answer key为私有；靶场发布和完整题集许可待核实。 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 语言覆盖：正式方法页说明为英文，但没有完整披露任务指令、程序/游戏内容的语言覆盖，不能仅据报告语言确定全量语种。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 评测方法

- **指标**：各靶场目标完成比例；总体对两个靶场比例等权。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **评分规则**：在命令输出中检索私有答案键隐藏marker计分，不采用模型成功宣称。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **提示与运行配置**：Pi agent、隔离Kali环境、仅连接模型provider和授权靶场；每运行48小时上限，计500M累计token内成绩（含缓存输入、推理）。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **可比性限制**：Nova领先两模型各3次取均值，其余多为单次；不把两靶场完成目标数直接相加作总体分。 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：已检查正式方法页和所指向的代码入口；本轮未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 最新情况

- **本轮核验日期**：2026-11-07 KST [1](https://www.vals.ai/benchmarks/cyber_offense)

- **现行版本与采用证据**：version：待核实；heat_confidence：B；evidence_2026_h2：url：https://www.vals.ai/benchmarks/cyber_offense；date：2026-10-23；note：Vals官网自写更新日；主要单一机构采用。 [1](https://www.vals.ai/benchmarks/cyber_offense) 注：B：主要单一机构当前评测/厂商采用，不能声称行业广泛采用。

- **饱和度判断**：两靶场最深阶段仍困难：Lighthouse无模型完成最终目标；Nova整个实验仅一次运行进入最终阶段。不能将部分目标完成率解释为完整任务成功率。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **已知问题与证据边界**：只在模拟授权环境评测；可迁移到真实网络的程度不能直接由靶场分数证明。 [1](https://www.vals.ai/benchmarks/cyber_offense)

- **关联与衍生关系**：Pi是执行agent框架，不是CyberOffense自身题库代码；Nova与Lighthouse是同一基准下两个靶场分项，不另算两个benchmark。 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 更新与修订：当前可核实的是网页方法/榜表更新；尚未定位独立论文的版本历史，不把网页更新时间伪作arXiv修订。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 榜单快照

- **快照采集日**：2026-11-07 KST / Asia/Seoul [1](https://www.vals.ai/benchmarks/cyber_offense)

- **官方榜/正式委托榜**：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 官网表行序，非总榜名次 | GPT-6 Sol Daybreak | Nova：15.7/21（3次均值；12–19）；Lighthouse：27/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| 官网表行序，非总榜名次 | DeepSeek V4.1 Flash 1017 | Nova：16.3/21（3次均值；15–18）；Lighthouse：21/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| 官网表行序，非总榜名次 | Kimi K3.1 Pro | Nova：13/21；Lighthouse：20/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| 官网表行序，非总榜名次 | Meta Wonder | Nova：7/21；Lighthouse：28/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| 官网表行序，非总榜名次 | Grok 4.7 | Nova：12/21；Lighthouse：16/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| 官网表行序，非总榜名次 | Kimi K3 | Nova：9/21；Lighthouse：10/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |
| 官网表行序，非总榜名次 | GLM 5.3 Flash | Nova：5/21；Lighthouse：5/31 | 目标完成数（两靶场分列）；2026-10-23；[1](https://www.vals.ai/benchmarks/cyber_offense) |


表内所有条目采集于2026-11-07（KST）；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：仅保留所列来源与协议下的结果；榜单自写更新时间：2026-10-23。访问日期不是评测运行日期。 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：本轮未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 联系方式

- **官方社交**：https://x.com/ValsAI [1](https://www.vals.ai/benchmarks/cyber_offense) 注：官网页脚公开链接；本轮不读取或操作X账户。

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：本轮所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- 公开问题追踪：已检查正式方法页和所指向的代码入口；本轮未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- 隐私政策：本轮所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 原始文件

- **其他正式文档**：type：官方介绍/协议；url：https://www.vals.ai/benchmarks/cyber_offense [1](https://www.vals.ai/benchmarks/cyber_offense)

- **Drive中的论文副本**：待核实 [1](https://www.vals.ai/benchmarks/cyber_offense)

**仍待核实**（不推断为未公开）：

- 原始PDF：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- SHA-256：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- PDF字节数：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber_offense)
- Drive归档目录：本轮仅在本地生成研究输出与PDF校验，未执行Drive上传；正式归档文件夹链接仍需确认。 [1](https://www.vals.ai/benchmarks/cyber_offense)

## 变更记录

- date：2026-11-07；timezone：KST / Asia/Seoul；change：首次建立近期热门条目；核对官方协议、当前结果与来源限制；未上传Drive。；2026-11-07：第二轮逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://www.vals.ai/benchmarks/cyber_offense)

---

来源访问日期统一为2026-11-07（KST）；原始URL见各段链接，结构化逐字段证据见同名JSON。
