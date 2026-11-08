# CyberBench

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

研究快照；trending: B；未知信息保留待核实。

CyberBench v1.1测两种互补能力：构造能区分漏洞版与修复版的输入，以及修补程序同时保留正常功能。任务来自ARVO的OSS-Fuzz原生软件漏洞回归镜像，采用mini-swe-agent；60道PoC题和56道Patch题不应与完整企业网络入侵混为一谈。 [1](https://www.vals.ai/benchmarks/cyber)

v1.1更换离线沙箱和clean-room评分器，替代而非直接延续v1成绩。2026-11-05官方48模型表的Overall榜首为Wonder 80.36%；拒答和fallback策略会影响分数。ARVO、CyberGym、mini-swe-agent属于上游资源，其公开许可证不自动成为CyberBench任务的许可证。 [1](https://www.vals.ai/benchmarks/cyber)

## 基本信息

- **简称**：CyberBench [1](https://www.vals.ai/benchmarks/cyber)

- **全称**：CyberBench [1](https://www.vals.ai/benchmarks/cyber)

- **基准版本**：v1.1 [1](https://www.vals.ai/benchmarks/cyber)

- **主板块**：安全 [1](https://www.vals.ai/benchmarks/cyber) 注：编辑主板块归档，不据此限制跨学科覆盖。

- **子领域**：漏洞复现；安全补丁生成；原生软件内存安全 [1](https://www.vals.ai/benchmarks/cyber)

- **许可证与限制**：专有评测（Vals目录标记Proprietary）；不等于开源软件许可 [2](https://www.vals.ai/benchmarks/)

- **官方主页**：https://www.vals.ai/benchmarks/cyber [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 论文/报告版本：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber)
- 发布日期：已核对正式页的更新日期；尚不能把榜单更新日或访问日当作首次发布日期。 [1](https://www.vals.ai/benchmarks/cyber)
- 论文/报告：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber)
- 官方代码：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cyber)
- 数据入口：已检查正式方法页及其外链；未定位经维护方确认的任务数据仓库/HF卡，不将结果表或上游数据充作完整题库。 [1](https://www.vals.ai/benchmarks/cyber)
- 报告标题：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber)

## 发起与维护

- **发起方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber)

- **维护方**：Vals AI [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 合作方：正式材料不足以确认独立研究合作方；工具提供者、模型厂商和上游仓库不能据此当作合作机构。 [1](https://www.vals.ai/benchmarks/cyber)
- 核心作者：正式方法页可确认发布维护机构，但未找到足以确认作者姓名/出题者资格的署名或方法细目。 [1](https://www.vals.ai/benchmarks/cyber)
- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://www.vals.ai/benchmarks/cyber)

## 设计目标

- **核心能力**：端到端复现真实漏洞并修补，同时保持正常程序行为。 [1](https://www.vals.ai/benchmarks/cyber)

- **相对已有评测的缺口**：聚焦OSS-Fuzz风格原生代码崩溃，而非把CTF成绩等同通用安全能力。 [1](https://www.vals.ai/benchmarks/cyber)

## 构建方式

- **题目来源**：基于ARVO的OSS-Fuzz回归镜像；任务来自CyberGym原始收集窗口之后。 [1](https://www.vals.ai/benchmarks/cyber)

- **审核流程**：差分oracle和hidden holdout对照维护者修复版本。 [1](https://www.vals.ai/benchmarks/cyber)

- **质量控制**：v1.1重跑离线沙箱，hardened clean-room grader。 [1](https://www.vals.ai/benchmarks/cyber)

- **防污染/运行完整性**：新时间窗口与离线沙箱降低泄漏/外部查询影响；不等于已证明完全无污染。 [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：正式方法页可确认发布维护机构，但未找到足以确认作者姓名/出题者资格的署名或方法细目。 [1](https://www.vals.ai/benchmarks/cyber)

## 数据形式

- **规模**：PoC 60任务；Patch 56可靠可评分任务。 [1](https://www.vals.ai/benchmarks/cyber)

- **题型**：PoC生成触发输入；Patch轨编辑源码修复漏洞。 [1](https://www.vals.ai/benchmarks/cyber)

- **模态**：文本；源码；二进制目标；容器 [1](https://www.vals.ai/benchmarks/cyber)

- **难度与任务跨度**：真实原生开源软件的内存安全、sanitizer和未定义行为崩溃；非通用网络入侵或网页漏洞评测。 [1](https://www.vals.ai/benchmarks/cyber)

- **公开与隐藏划分**：Patch有隐藏holdout输入；完整任务与数据许可范围待核实。 [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 语言覆盖：正式方法页说明为英文，但没有完整披露任务指令、程序/游戏内容的语言覆盖，不能仅据报告语言确定全量语种。 [1](https://www.vals.ai/benchmarks/cyber)

## 评测方法

- **指标**：Overall、PoC、Patch准确率；榜首表为Overall。 [1](https://www.vals.ai/benchmarks/cyber)

- **评分规则**：PoC须使漏洞版崩溃而修复版不崩溃；Patch须编译成功、原PoC不再触发且隐藏行为匹配参考。 [1](https://www.vals.ai/benchmarks/cyber)

- **提示与运行配置**：统一mini-swe-agent；离线任务沙箱。 [1](https://www.vals.ai/benchmarks/cyber)

- **可比性限制**：v1.1取代v1，结果不直接可比；拒答算失败，fallback会影响结果，需保留其标记。 [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cyber)

## 最新情况

- **核验日期**：2026-11-07 [1](https://www.vals.ai/benchmarks/cyber)

- **现行版本与采用证据**：version：v1.1；heat_confidence：B；evidence_2026_h2：url：https://www.vals.ai/benchmarks/cyber；date：2026-11-05；note：Vals当前48模型榜；热度主要来自单一评测机构，不能称行业广泛采纳。 [1](https://www.vals.ai/benchmarks/cyber)

- **更新与修订**：v1.1保留60题PoC、56题Patch并更换离线沙箱和hardened grader；v1不可直接比较。 [1](https://www.vals.ai/benchmarks/cyber)

- **饱和度判断**：编辑判断：当前Overall榜首80.36%，仍有余量；需分别检查60题PoC和56题Patch，不与v1直接比较。 [1](https://www.vals.ai/benchmarks/cyber)

- **已知问题与证据边界**：任务取自CyberGym原窗口之后；v1.1离线沙箱和clean-room grader降低外部访问与评分泄漏。厂商拒答计失败，fallback另有标记并可查看将fallback任务计失败的反事实分数。通过局部补丁不保证等价于维护者完整修复。 [1](https://www.vals.ai/benchmarks/cyber)

- **关联与衍生关系**：基于CyberGym评测方法、ARVO OSS-Fuzz镜像与mini-swe-agent；这些是上游方法/基础设施，不能当作CyberBench自身开源任务或许可证。 [1](https://www.vals.ai/benchmarks/cyber)

## 榜单快照

- **快照采集日**：2026-11-07 [1](https://www.vals.ai/benchmarks/cyber)

- **官方榜/正式委托榜**：https://www.vals.ai/benchmarks/cyber [1](https://www.vals.ai/benchmarks/cyber)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | Wonder | 80.36 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 2 | GPT-6 Sol | 77.98 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 3 | Gemini 4 Argon | 77.86 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 4 | GPT-5.6 Sol | 76.31 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 5 | GPT-6 Luna | 76.25 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 6 | Claude Haiku 5.5 | 75.48 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 7 | MiMo V2.6 Flash | 75.36 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 8 | Kimi K3 | 75.24 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 9 | Claude Opus 5.5 (CVP) | 74.58 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |
| 10 | DeepSeek V4.1 Flash | 73.69 | Overall Accuracy (%)；2026-11-05；[1](https://www.vals.ai/benchmarks/cyber) |


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：官方页面结果；采集日期不等于榜单更新时间。 [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [1](https://www.vals.ai/benchmarks/cyber)

## 联系方式

- **官方社交**：https://x.com/ValsAI [1](https://www.vals.ai/benchmarks/cyber) 注：官网页脚公开链接；不读取或操作X账户。

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://www.vals.ai/benchmarks/cyber)
- 公开问题追踪：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cyber)
- 隐私政策：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://www.vals.ai/benchmarks/cyber)

## 原始文件

- **其他正式文档**：type：v1.1官方方法与结果；url：https://www.vals.ai/benchmarks/cyber；type：上游ARVO镜像项目，非本基准实现；url：https://github.com/n132/ARVO-Meta [1](https://www.vals.ai/benchmarks/cyber)

- **中的论文副本**：待核实 [1](https://www.vals.ai/benchmarks/cyber)

**仍待核实**（不推断为未公开）：

- 原始PDF：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber)
- SHA-256：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber)
- PDF字节数：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cyber)
- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [1](https://www.vals.ai/benchmarks/cyber)

## 变更记录

- date：2026-11-07；timezone：；change：按官方材料新建中文条目；区分热度、质量和不同版本评分。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://www.vals.ai/benchmarks/cyber)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
