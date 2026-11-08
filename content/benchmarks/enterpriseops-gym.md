# EnterpriseOps-Gym

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

EnterpriseOps-Gym以可重置数据库和MCP工具构成企业工作流沙箱，评估有状态的长程规划、政策遵循及副作用控制。原论文1150道专家任务覆盖八域、164张表、512个工具；每题按最终数据库状态验证，而不是要求复制某条操作轨迹。30道任务故意不可行，应拒绝而非越权完成。 [1](https://enterpriseops-gym.github.io/) [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

已定位真正官方项目页，其明确把最新榜交由Artificial Analysis维护。AA使用Stirrup、oracle工具及三次重复；README全量Oracle榜、原论文与AA并非同一协议，最高45.9%、37.4%、51.1%不应串成单一进步曲线。HF卡计数与论文也存在打包差异，公开多配置行数不能当独立任务总数。 [1](https://enterpriseops-gym.github.io/) [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

## 基本信息

- **简称**：EnterpriseOps-Gym [2](https://arxiv.org/abs/2603.13594)

- **全称**：EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings [2](https://arxiv.org/abs/2603.13594)

- **论文/报告版本**：arXiv v1（2026-03-13） [2](https://arxiv.org/abs/2603.13594)

- **发布日期**：2026-03-13（arXiv 提交） [2](https://arxiv.org/abs/2603.13594)

- **主板块**：Agent [2](https://arxiv.org/abs/2603.13594) 注：Benchmark Atlas 编辑归档。

- **子领域**：企业工作流；工具调用；有状态规划 [2](https://arxiv.org/abs/2603.13594)

- **许可证与限制**：Apache-2.0（官方仓库LICENSE；不推定附带第三方数据全部同许可） [5](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/LICENSE)

- **论文/报告**：https://arxiv.org/abs/2603.13594 [2](https://arxiv.org/abs/2603.13594)

- **官方代码**：https://github.com/ServiceNow/EnterpriseOps-Gym [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **数据入口**：https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

- **官方主页**：https://enterpriseops-gym.github.io/ [1](https://enterpriseops-gym.github.io/)

- **报告标题**：EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings [2](https://arxiv.org/abs/2603.13594)

**仍待核实**（不推断为未公开）：

- 基准版本：已读取所列论文/数据卡/README；未确认可追踪的正式版本编号。运行镜像tag、网页更新日与数据版本不混同。 [2](https://arxiv.org/abs/2603.13594)

## 发起与维护

- **发起方**：ServiceNow [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **合作方**：Mila – Quebec AI Institute；Université de Montréal；Turing（数据构建合作方） [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

- **核心作者**：Shiva Krishna Reddy Malay、Shravan Nayak、Jishnu Sethumadhavan Nair、Sagar Davasam、Aman Tiwari、Sathwik Tejaswi Madhusudhan、Sridhar Krishna Nemala、Srinivas Sunkara、Sai Rajeswar [2](https://arxiv.org/abs/2603.13594)

- **维护方**：ServiceNow（ServiceNow-AI） [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

**仍待核实**（不推断为未公开）：

- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [2](https://arxiv.org/abs/2603.13594)

## 设计目标

- **核心能力**：在有持久状态变化与严格访问规范的企业环境中进行长程规划与工具调用，并能拒绝不可行任务。 [2](https://arxiv.org/abs/2603.13594)

- **相对已有评测的缺口**：已有基准未反映专业环境中长程规划、持久状态与访问协议的复杂性。 [2](https://arxiv.org/abs/2603.13594)

## 构建方式

- **题目来源**：根据公开企业API文档和领域SME设计合成数据库与任务，不使用私有企业数据；Calendar、CSM、、Email、HR、ITSM、Teams及Hybrid八域。 [2](https://arxiv.org/abs/2603.13594)

- **出题与审核人员**：Turing组织160余名工程师、领域SME与标注人员；工程/计算机等相关学士背景，平均每域20名标注者和6名reviewer，历时约4个月含1个月试点。 [2](https://arxiv.org/abs/2603.13594)

- **审核流程**：场景设计→人工执行gold轨迹并写政策约束plan→编写最终状态SQL verifier→多轮可行性、清晰度、外键和权限约束检查；最终状态唯一但允许多条合法执行路径。 [2](https://arxiv.org/abs/2603.13594)

- **质量控制**：先用GPT-5/Gemini/Claude试跑排查缺失工具、无效数据、无意捷径与过简任务，再人工核查prompt、轨迹及verifier覆盖；每次任务重置数据库避免跨运行状态泄漏。 [2](https://arxiv.org/abs/2603.13594)

- **防污染/运行完整性**：环境由公开文档与SME独立合成，私有企业数据不进入；官方README只释放约60%样本。论文未给出可量化语料去重检索结果，不能宣称完全无污染。 [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

## 数据形式

- **规模**：1,150 个任务、8 个垂直领域；沙箱含164张数据库表、512个工具 [2](https://arxiv.org/abs/2603.13594)

- **题型**：有状态多步工具调用任务 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **模态**：文本；工具调用/数据库状态 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **语言覆盖**：自然语言指令和政策为英文，结构化工具调用及SQL verifier；公开HF样例为英文，不宣称跨语言覆盖。 [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) [2](https://arxiv.org/abs/2603.13594)

- **难度与任务跨度**：专家参考轨迹平均9.15步、最多34步，平均5.3项验证条件、最多44项；30题故意不可行，需拒绝且不产生副作用。 [2](https://arxiv.org/abs/2603.13594)

- **公开与隐藏划分**：README称约60%公开；论文总规模1150，HF卡域计数合计1115且viewer oracle649行，打包规模与论文存在差异。不能把HF多配置总行数2560当独立任务数。 [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) [2](https://arxiv.org/abs/2603.13594)

## 评测方法

- **指标**：严格任务成功率（无部分分） [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **评分规则**：按底层数据库终态的验证器判定（如 SQL 查询期望值），全部验证器通过才算成功 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

- **提示与运行配置**：AA：Stirrup harness、oracle tool 模式、每任务3次重复 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

- **评分/运行脚本**：runner：https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/evaluate.py；scoring：https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/compute_score.py [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

- **可比性限制**：官方项目页已将最新榜指向AA，但AA明确为Stirrup独立实现、oracle工具、每题3次；原论文ReAct及README分数分别保留，不能跨harness合并排名。README排除error文件，复现应核对分母。 [1](https://enterpriseops-gym.github.io/) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

## 最新情况

- **核验日期**：2026-11-07 [2](https://arxiv.org/abs/2603.13594)

- **现行版本与采用证据**：version：待核实；evidence_2026_h2：url：https://artificialanalysis.ai/methodology/intelligence-benchmarking；date：2026-11-07；organization：Artificial Analysis；note：当前方法页将EnterpriseOps-Gym列为正在实施的评测，披露任务或评分协议。；url：https://artificialanalysis.ai/evaluations；date：2026-11-07；organization：Artificial Analysis；note：当前公开评测目录单列EnterpriseOps-Gym，不是新闻提及。；url：https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym；date：2026-11-07；organization：ServiceNow；note：AA当前实现明确基于ServiceNow公开数据并以终态SQL验证。；trending：heat_confidence：A；summary：ServiceNow 企业工作流基准已有 AA 独立评测，按终态验证。 [7](https://artificialanalysis.ai/methodology/intelligence-benchmarking) [8](https://artificialanalysis.ai/evaluations) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) 注：近期热门证据取自候选研究与重开页面；A级：多家前沿实验室或评测机构独立采用。

- **更新与修订**：论文首版arXiv:2603.13594v1（2026-03-13）。当前README增列Opus4.6 45.9%、Sonnet4.6 42.2%，首页仍写旧34.1%；项目页旧论文摘要仍为37.4%，最新结果已委托AA维护。 [2](https://arxiv.org/abs/2603.13594) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [1](https://enterpriseops-gym.github.io/)

- **饱和度判断**：AA当前榜首51.1%严格任务成功率；官方README快照最高45.9%，原论文首版37.4%；协议不同均未接近满分，不能用版本间差值当纯模型进步。 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [2](https://arxiv.org/abs/2603.13594)

- **已知问题与证据边界**：公开/私有规模、README与论文成绩存在版本差异；oracle工具预先给正确工具，不能证明在真实企业中自主检索同样成功。全合成沙箱的表现不代表可安全直接部署。 [2](https://arxiv.org/abs/2603.13594) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md)

- **关联与衍生关系**：EnterpriseOps-Gym-AA是Artificial Analysis用Stirrup的独立实现；项目页将最新榜指向它，但数据集与原论文仍须单独标记协议。 [1](https://enterpriseops-gym.github.io/) [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

## 榜单快照

- **快照采集日**：2026-11-07 [2](https://arxiv.org/abs/2603.13594)

- **官方榜/正式委托榜**：https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa [1](https://enterpriseops-gym.github.io/) 注：官方项目页明确声明最新model results由AA维护；AA同时声明独立实现。

- **独立第三方入口**：https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | Claude Fable 5 (Max, Opus 4.8 Fallback) | 51.1% | EnterpriseOps-Gym-AA Task success rate；待核实（采集日2026-11-07）；[4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |
| 2 | Gemini 3.7 Flash (Medium) | 50.4% | EnterpriseOps-Gym-AA Task success rate；待核实（采集日2026-11-07）；[4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |
| 3 | Gemini 3.5 Flash (High) | 50.1% | EnterpriseOps-Gym-AA Task success rate；待核实（采集日2026-11-07）；[4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) |

> Claude Fable 5 (Max, Opus 4.8 Fallback)：result_type：AA 独立实现榜快照；protocol：Stirrup；oracle tools；每任务3次；严格全verifier通过 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

> Gemini 3.7 Flash (Medium)：result_type：AA 独立实现榜快照；protocol：Stirrup；oracle tools；每任务3次；严格全verifier通过 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

> Gemini 3.5 Flash (High)：result_type：AA 独立实现榜快照；protocol：Stirrup；oracle tools；每任务3次；严格全verifier通过 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：重读AA前三51.1/50.4/50.1。另读取官方README全量Oracle快照前三：Opus4.6 45.9、Sonnet4.6 42.2、Opus4.5 39.4；不与AA榜混排。原论文Opus4.5 37.4与README39.4亦有差异，优先按各来源原样标记。 [4](https://artificialanalysis.ai/evaluations/enterprise-ops-gym-aa) [3](https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md) [2](https://arxiv.org/abs/2603.13594)

## 联系方式

- **公开联系邮箱**：shivakrishnareddy.ma@servicenow.com [2](https://arxiv.org/abs/2603.13594)

- **公开问题追踪**：https://github.com/ServiceNow/EnterpriseOps-Gym/issues [9](https://github.com/ServiceNow/EnterpriseOps-Gym)

**仍待核实**（不推断为未公开）：

- 官方社交：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [2](https://arxiv.org/abs/2603.13594)
- 隐私政策：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [2](https://arxiv.org/abs/2603.13594)

## 原始文件

- **原始PDF**：https://arxiv.org/pdf/2603.13594 [10](https://arxiv.org/pdf/2603.13594)

- **SHA-256**：8a7639982494f4802148fa4bdb6de40040f9d2e01c061db57f4e2e5d0d66d751 [10](https://arxiv.org/pdf/2603.13594) 注：实际下载的PDF字节计算；不是外部网页抄录。

- **PDF字节数**：5330988 [10](https://arxiv.org/pdf/2603.13594) 注：下载字节数；未上传。

- **其他正式文档**：type：官方README及Oracle榜快照；url：https://github.com/ServiceNow/EnterpriseOps-Gym/blob/main/README.md；type：官方项目页面；url：https://enterpriseops-gym.github.io/；type：官方HF数据卡；url：https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym [1](https://enterpriseops-gym.github.io/) [9](https://github.com/ServiceNow/EnterpriseOps-Gym) [6](https://huggingface.co/datasets/ServiceNow-AI/EnterpriseOps-Gym)

- **中的论文副本**：待核实 [2](https://arxiv.org/abs/2603.13594)

**仍待核实**（不推断为未公开）：

- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [2](https://arxiv.org/abs/2603.13594)

## 变更记录

- date：2026-11-07；；change：近期热门批次首次建立中文条目；按官方页面核实基本信息、构建、评分与榜单快照，未核实字段保留待核实。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://enterpriseops-gym.github.io/)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
