# DualChem

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

DualChem聚焦化学的双用途歧义：相同专业知识既可能支持正当研究，也可能被滥用。600道题由化学专家构建，分485道多选、115道开放回答，覆盖七个实验领域，同时记录良性/有害用途及严重度。能力答题率、拒答率和风险意识是不同轴，不能用单一“越高越好”名次掩盖安全取舍。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

正式PDF的无工具Table 4中GPT-5.6 Sol全题准确率67.3%，67.7%仅是已回答题的条件准确率。人类辅助组相对无辅助组提高约16个百分点，但不是同一随机样本的严格因果实验。已发现匿名HF早期卡及代码线索，其人类样本构成与署名正式报告不同，尚不冒充正式Scale数据发布。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

## 基本信息

- **简称**：DualChem [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **全称**：DualChem [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **基准版本**：2026-10-28发布快照 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **发布日期**：2026-10-28 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **主板块**：化学 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：编辑归档，不代表官方分类。

- **子领域**：安全；双用途化学 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：编辑归档，不代表官方分类。

- **论文/报告**：https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **官方主页**：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **报告标题**：DualChem: Measuring LLM Uplift and Dual-Use Risk Awareness in Chemistry [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 论文/报告版本：已读取所列论文/数据卡/README；未确认可追踪的正式版本编号。运行镜像tag、网页更新日与数据版本不混同。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)
- 许可证与限制：已检查正式发表材料，尚未确认覆盖任务数据/游戏资产的明确使用授权；软件、匿名预发布数据和商业游戏的许可证不能互套。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)
- 官方代码：匿名HF卡链接anonymous.4open.science/r/dualchem-4318；未由Scale正式发表页交叉确认，不当作正式官方代码。 [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)
- 数据入口：发现匿名DualChem-author/dualchem v1.0.0，含600题与CC BY 4.0，但与署名PDF人类样本构成不同；尚未确认其为Scale当前正式版本。 [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md) [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 发起与维护

- **发起方**：Scale AI [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **合作方**：NIST CAISSI及美国政府领域专家对范围与题目分类提供输入；合作研究协议产生的首个基准。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **核心作者**：Udari Madhushani Sehwag、Abhishek Dalvi、Yash Maurya、Drew Rein、Dylan Hardee、Jeremy Kritz、Jonathan Nguyen、Bert Herring、Evi Fuelle、Christina Q Knight、Joseph Brandifino、Max Fenkell [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **维护方**：Scale AI [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 设计目标

- **核心能力**：评估含糊双用途化学情境中的技术帮助、人类能力增益、风险识别与严重性判断，而非仅测显式有害请求拒答。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **相对已有评测的缺口**：相同正确化学知识可能用于正当科研或被滥用；一般能力与显式有害请求安全测验未覆盖这种歧义。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

## 构建方式

- **题目来源**：专家为真实实验场景原创题目，并写良性/有害用例及1–5严重性评分；不靠合成或显式对抗提示构题。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **出题与审核人员**：130名化学专家：19名学士、53名硕士、58名博士；题目经博士级reviewer复核，再经LLM质检，失败项返最高层博士审核。不能误写全部作者均为博士。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **审核流程**：每题附良性/有害用途及各自1–5严重度；博士审科学准确性、清晰性和风险边界，LLM检查后有问题再交资深化学博士修订。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **质量控制**：博士级化学专家审核准确性、清晰度及安全性；不合格题修订或拒绝；之后模型质检及高阶博士复核。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 防污染/运行完整性：所列已打开材料未完成精确核验；不代表官方未公开。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 数据形式

- **规模**：600题，7个化学领域；另有120名化学本科毕业参与者的有无模型帮助对照研究。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **题型**：多数为五选项、至少一个正确选项的多项选择，另含自由回答及1–5个true/false rubric。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **模态**：文本 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **语言覆盖**：英文（匿名HF v1.0.0数据卡language: en；发表PDF样例亦为英文） [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **难度与任务跨度**：600题跨7个实验化学领域；485道多选和115道开放题。模型自行报告1–5难度，不是统一专家标定难度。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

- **公开与隐藏划分**：匿名HF v1.0.0卡列600题test及600人类基线，并提供CC BY 4.0；但其人类研究构成与2026-10-28署名PDF不同，Scale发表页未直接链接该卡，二者确切版本对应需维护方确认。 [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md) [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：当前仅核实匿名预发布卡的test配置；署名正式版本的公开/隐藏划分仍待核实。

 核实状态仍为待核实；部分字段或版本细节未解决。

## 评测方法

- **指标**：准确率、回答题条件准确率、拒答率、风险标记与专家严重性一致性、人类增益。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **评分规则**：论文Table 4的Acc把拒答记错；Acc.ans只在已回答题计算，二者分母不同。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **提示与运行配置**：Table 4同时报告无工具与可网页搜索两条件，不混合排名。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **可比性限制**：67.7%为GPT-5.6 Sol已回答题条件准确率；全600题拒答计错为67.3%，不能混用。发布博客约50%/67%为概述，精确口径以论文表格为准。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 最新情况

- **核验日期**：2026-11-07 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **现行版本与采用证据**：version：2026-10-28发布快照；trending：B；heat_evidence：Scale于2026-10-28首发并报告30+模型；NIST CAISSI与美国政府领域专家参与范围及分类设计。热度B：当前主要为创建机构发布，不据媒体报道推断独立复现或行业广泛采用。；evidence_2026_h2：url：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks；date：2026-11-07；date_type：observed_on；note：本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **饱和度判断**：无工具拒答计错榜首67.3%，已回答题条件准确率67.7%，两者不是同一指标；技术答题率未饱和，更不能把风险识别或拒答视作同一个分数。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **已知问题与证据边界**：题目为双用途能力与风险意识测量，不能用低拒答率直接选“更好”模型。人类uplift研究非随机、两组近乎分离，31.8→47.8差值不等于严格随机因果效应；匿名早期HF与署名正式PDF样本构成不同。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

- **关联与衍生关系**：DualChem专门测双用途化学风险，与ChemBench一般化学能力不合并；不收录或再传播具体敏感题目内容。 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

**仍待核实**（不推断为未公开）：

- 更新与修订：当前可核实的是网页方法/榜表更新；尚未定位独立论文的版本历史，不把网页更新时间伪作arXiv修订。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 榜单快照

- **快照采集日**：2026-11-07 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **官方榜/正式委托榜**：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | GPT-5.6 Sol | 67.3 | Table 4 无工具Acc (%)，拒答计错；2026-10-28（发布日；具体评测运行日待核实）；[2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) |
| 2 | GPT-6 Astra | 62.7 | Table 4 无工具Acc (%)，拒答计错；2026-10-28（发布日；具体评测运行日待核实）；[2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) |
| 3 | GPT-6.1 Sol | 61.7 | Table 4 无工具Acc (%)，拒答计错；2026-10-28（发布日；具体评测运行日待核实）；[2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) |

> GPT-5.6 Sol：result_type：发表PDF Table 4无工具历史实验；rank_type：所列无工具Acc顺序，非实时网页榜 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

> GPT-6 Astra：result_type：发表PDF Table 4无工具历史实验；rank_type：所列无工具Acc顺序，非实时网页榜 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

> GPT-6.1 Sol：result_type：发表PDF Table 4无工具历史实验；rank_type：所列无工具Acc顺序，非实时网页榜 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：67.7%为GPT-5.6 Sol已回答题条件准确率；全600题拒答计错为67.3%，不能混用。发布博客约50%/67%为概述，精确口径以论文表格为准。 榜表自写更新时间：2026-10-28（发布日；具体评测运行日待核实）；采集日不等于运行日。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 联系方式

- **公开联系邮箱**：udari.sehwag@scale.com；prep@scale.com [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **官方社交**：https://x.com/scale_ai [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

- **隐私政策**：https://scale.com/legal/privacy [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

**仍待核实**（不推断为未公开）：

- 公开问题追踪：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 原始文件

- **原始PDF**：https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf)

- **SHA-256**：0078a8853e2956595660fb004aca4320430fc3c950962fff2071e533788059ef [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) 注：实际下载的PDF字节计算；不是外部网页抄录。

- **PDF字节数**：3817998 [2](https://cdn.sanity.io/files/50zba0eo/production/740e74ec297aa119d37b87d4706540e322551ba0.pdf) 注：下载字节数；未上传。

- **其他正式文档**：type：正式发表博客；url：https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks；type：匿名早期HF数据卡，版本对应尚待维护方确认；url：https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) [3](https://huggingface.co/datasets/DualChem-author/dualchem/blob/main/README.md)

- **中的论文副本**：待核实 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

**仍待核实**（不推断为未公开）：

- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

## 变更记录

- date：2026-11-07；；change：首次建立近期热门中文研究条目。DualChem专门测双用途化学风险，与ChemBench一般化学能力不合并；不收录或再传播具体敏感题目内容。 热度与榜单口径分离，不确定值标记待核实。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
