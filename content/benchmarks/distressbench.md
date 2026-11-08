# DistressBench

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

已核验存在；中文研究快照；note: trending: B；未核实保留标记

DistressBench评估心理危机支持，不把“没有输出有害内容”当成充分条件。718条英文模拟对话覆盖23类危机；299条单轮、419条多轮，临床人员和危机咨询师参与设计，使用6901项加权原子标准衡量共情、识别、降级和转介等七个维度。材料不是患者病历或真实临床对话。 [1](https://labs.scale.com/leaderboard/distressbench) [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

公开/私有各359条；主榜由三个裁判模型多数票判断标准是否满足，三次运行汇总。HF评分代码可公开读取，但HF“无system prompt”与论文/榜页的helpful-assistant设置不一致；CC BY 4.0与evaluation-only文字也需维护方澄清。榜单和长期伴随研究均不是临床有效性试验或部署安全证明。 [1](https://labs.scale.com/leaderboard/distressbench) [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

## 基本信息

- **简称**：DistressBench [1](https://labs.scale.com/leaderboard/distressbench)

- **全称**：DistressBench [1](https://labs.scale.com/leaderboard/distressbench) 注：沿用官方名称；不将论文标题臆造为全称。

- **基准版本**：v1 [2](https://arxiv.org/abs/2610.12758)

- **论文/报告版本**：arXiv:2610.12758v1（2026-10-08） [2](https://arxiv.org/abs/2610.12758)

- **发布日期**：2026-10-08（论文PDF首版标记） [2](https://arxiv.org/abs/2610.12758)

- **主板块**：安全 [1](https://labs.scale.com/leaderboard/distressbench) 注：Benchmark Atlas编辑分类。

- **子领域**：生物与医学；心理健康 [1](https://labs.scale.com/leaderboard/distressbench)

- **许可证与限制**：HF数据卡明确CC BY 4.0；论文/榜页同时称仅evaluation use，LH另有research-use terms。两种限制口径有冲突，使用或再分发前应向维护方确认。 [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [2](https://arxiv.org/abs/2610.12758) [1](https://labs.scale.com/leaderboard/distressbench)

- **论文/报告**：https://arxiv.org/abs/2610.12758 [2](https://arxiv.org/abs/2610.12758)

- **官方代码**：https://huggingface.co/datasets/ScaleAI/DistressBench/tree/main/code [3](https://huggingface.co/datasets/ScaleAI/DistressBench) 注：评分代码与code/README在官方HF数据仓库，不伪造GitHub仓库。

- **数据入口**：https://huggingface.co/datasets/ScaleAI/DistressBench [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

- **官方主页**：https://labs.scale.com/leaderboard/distressbench [1](https://labs.scale.com/leaderboard/distressbench)

- **报告标题**：DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models [2](https://arxiv.org/abs/2610.12758)

## 发起与维护

- **发起方**：Scale AI [2](https://arxiv.org/abs/2610.12758)

- **核心作者**：Drew Rein；Patrick Oathout；Vishal Kumar；Udari Madhushani Sehwag [2](https://arxiv.org/abs/2610.12758)

- **维护方**：Scale Labs [2](https://arxiv.org/abs/2610.12758)

**仍待核实**（不推断为未公开）：

- 合作方：正式材料不足以确认独立研究合作方；工具提供者、模型厂商和上游仓库不能据此当作合作机构。 [1](https://labs.scale.com/leaderboard/distressbench)
- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://labs.scale.com/leaderboard/distressbench)

## 设计目标

- **核心能力**：心理危机支持中的识别、恰当共情、降级干预和人类援助转介，而非只测拒答。 [2](https://arxiv.org/abs/2610.12758)

- **相对已有评测的缺口**：不输出有害内容不等于给予有效支持；单轮二元拒答指标漏测隐性危机与识别后不行动。 [2](https://arxiv.org/abs/2610.12758)

## 构建方式

- **题目来源**：持证临床人员与危机咨询师编写的模拟对话，不是患者聊天或临床记录。 [2](https://arxiv.org/abs/2610.12758)

- **出题与审核人员**：持证临床人员和危机咨询师；无真实患者信息。 [2](https://arxiv.org/abs/2610.12758)

- **审核流程**：临床写用户提示及笔记，模型起草rubric/参考回答，经临床人员重写；自动检查与多层人工审核。 [2](https://arxiv.org/abs/2610.12758)

- **质量控制**：75条校准任务、2908份临床共识判断用于选择裁判面板，候选面板455种；所选面板κ=0.732，临床人员Fleiss κ=0.640并非同一种一致性统计，不能据此宣布机器优于临床人员。多轮任务另有连贯性门控。 [2](https://arxiv.org/abs/2610.12758)

- **防污染/运行完整性**：50/50分层公开/私有划分，私有半集用于污染检查。 [2](https://arxiv.org/abs/2610.12758)

## 数据形式

- **规模**：718对话、23子类、6901加权原子标准；299单轮，419多轮（3–5用户轮）。 [2](https://arxiv.org/abs/2610.12758)

- **题型**：危机对话回复，按任务专有rubric评价最终assistant轮。 [2](https://arxiv.org/abs/2610.12758)

- **模态**：文本对话 [2](https://arxiv.org/abs/2610.12758)

- **语言覆盖**：仅英语；援助资源标准以美国为中心。 [2](https://arxiv.org/abs/2610.12758)

- **难度与任务跨度**：23类模拟危机，299单轮、419多轮（3–5个用户回合），并覆盖165条隐式信号；这是场景分层，不是临床风险或难度标尺。 [2](https://arxiv.org/abs/2610.12758)

- **公开与隐藏划分**：公开359题、私有359题；主榜以全部718题为口径。 [2](https://arxiv.org/abs/2610.12758)

## 评测方法

- **指标**：Weighted Rubric Score：每题满足的临床标准权重比例，三次运行均值。 [2](https://arxiv.org/abs/2610.12758)

- **评分规则**：Opus 4.8、Llama 4 Maverick、Gemini 3.1 Pro独立二元判决后多数票；最终轮权重平均，空回复0；10000次bootstrap区间。 [2](https://arxiv.org/abs/2610.12758)

- **提示与运行配置**：论文/榜页称标准helpful-assistant system instruction及endpoint最低温度；HF Usage Notes则写no system prompt、默认4096输出上限、个别8192/16384。两处协议冲突，复现需锁定release_metadata.json，不能静默合并。 [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [1](https://labs.scale.com/leaderboard/distressbench)

- **评分/运行脚本**：https://huggingface.co/datasets/ScaleAI/DistressBench/tree/main/code [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

- **可比性限制**：论文/榜单描述标准helpful system，但当前HF发布说明no system prompt；需固定release_metadata再复现。主榜与公开半集、LH不可混用。 [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench)

## 最新情况

- **核验日期**：2026-11-07 [1](https://labs.scale.com/leaderboard/distressbench)

- **现行版本与采用证据**：version：v1；heat_confidence：B；evidence_2026_h2：url：https://labs.scale.com/leaderboard/distressbench；date：2026-11-07；date_type：observed_on；note：2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。；url：https://arxiv.org/abs/2610.12758；date：2026-11-07；date_type：observed_on；note：2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。 [1](https://labs.scale.com/leaderboard/distressbench) [2](https://arxiv.org/abs/2610.12758) 注：2026年10月论文及当前Scale榜仍比较前沿模型。热度B：主要单一机构评测，非多机构普遍采用。

- **更新与修订**：读取arXiv v1及HF公开359题发布卡；论文25模型实验与实时网页扩展模型名单需分开记录，不能把旧论文名次当最新榜。 [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [1](https://labs.scale.com/leaderboard/distressbench)

- **饱和度判断**：主榜最高约88.4%权重满足率不等于完全rubric通过或临床安全；高分不授权心理健康产品部署。 [2](https://arxiv.org/abs/2610.12758)

- **已知问题与证据边界**：私有359题用于污染检查；公开359题不能再保证未来训练未使用。论文末轮评分与HF无system prompt口径冲突，数据卡CC BY 4.0与evaluation-only叙述冲突；LLM草稿经临床人员大幅修改，不能说完全无模型辅助。 [2](https://arxiv.org/abs/2610.12758) [3](https://huggingface.co/datasets/ScaleAI/DistressBench) [1](https://labs.scale.com/leaderboard/distressbench)

- **关联与衍生关系**：DistressBench-LH是20条长时红队附录，不纳入本主榜。 [2](https://arxiv.org/abs/2610.12758)

## 榜单快照

- **快照采集日**：2026-11-07 [1](https://labs.scale.com/leaderboard/distressbench)

- **官方榜/正式委托榜**：https://labs.scale.com/leaderboard/distressbench [1](https://labs.scale.com/leaderboard/distressbench)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | muse-spark-1.2 | 88.39 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 5 | muse-glimmer-30b | 80.57 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 6 | deepseek-v4.1-flash | 79.78 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 7 | inkling | 78.47 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |
| 8 | qwen3.8-max | 77.64 | Weighted Rubric Score (%)；运行/发布日见覆盖说明；[1](https://labs.scale.com/leaderboard/distressbench) |

> muse-spark-1.2：ci95_halfwidth：0.93；rank_type：网页显示位置，不等于统计band [1](https://labs.scale.com/leaderboard/distressbench)

> muse-glimmer-30b：ci95_halfwidth：0.96；rank_type：网页显示位置，不等于统计band [1](https://labs.scale.com/leaderboard/distressbench)

> deepseek-v4.1-flash：ci95_halfwidth：1.01；rank_type：网页显示位置，不等于统计band [1](https://labs.scale.com/leaderboard/distressbench)

> inkling：ci95_halfwidth：1.06；rank_type：网页显示位置，不等于统计band [1](https://labs.scale.com/leaderboard/distressbench)

> qwen3.8-max：ci95_halfwidth：1.03；rank_type：网页显示位置，不等于统计band [1](https://labs.scale.com/leaderboard/distressbench)


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：官网动态表有部分模型名/分数无法完整配对，仅记录可可靠对应的已显示条目；榜页序号与论文统计band不是同一口径。网页扩展名单超过论文25模型，页面具体更新日没有精确核实。 [1](https://labs.scale.com/leaderboard/distressbench)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [1](https://labs.scale.com/leaderboard/distressbench)

## 联系方式

- **公开联系邮箱**：drew.rein@scale.com [2](https://arxiv.org/abs/2610.12758)

- **官方社交**：https://x.com/scale_ai [4](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：发布机构Scale AI的公开组织账号，不是危机支持或医疗求助渠道。

- **隐私政策**：https://scale.com/legal/privacy [4](https://scale.com/blog/dualchem-evaluating-ai-models-dual-use-chemistry-risks) 注：发布机构官网页脚指向的组织隐私政策；不推定另有基准专属政策。

**仍待核实**（不推断为未公开）：

- 公开问题追踪：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://labs.scale.com/leaderboard/distressbench)

## 原始文件

- **原始PDF**：https://arxiv.org/pdf/2610.12758 [5](https://arxiv.org/pdf/2610.12758)

- **SHA-256**：7f2a98944fd44c993a37758dfd157b672e9025cc3d10933fa5b83f368f1cf900 [5](https://arxiv.org/pdf/2610.12758) 注：实际下载的PDF字节计算；不是外部网页抄录。

- **PDF字节数**：610907 [5](https://arxiv.org/pdf/2610.12758) 注：下载字节数；未上传。

- **其他正式文档**：type：官方网页方法与榜单（非PDF）；url：https://labs.scale.com/leaderboard/distressbench [1](https://labs.scale.com/leaderboard/distressbench)

- **中的论文副本**：待核实 [1](https://labs.scale.com/leaderboard/distressbench)

**仍待核实**（不推断为未公开）：

- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [1](https://labs.scale.com/leaderboard/distressbench)

## 变更记录

- date：2026-11-07；timezone：；change：首次建立中文条目；逐项核实官方材料、热度和榜单；未知不推测。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://labs.scale.com/leaderboard/distressbench)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
