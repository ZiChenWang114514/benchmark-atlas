# CUA-bench

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

已核验存在；研究快照；note: trending: B；未核实字段保留标记

CUA-bench把计算机使用能力放进实时商业游戏：agent只能读像素并使用键盘、鼠标，不能通过游戏API、内存或存档旁路取状态。六款游戏按沙盒、反应和体育配对，Minecraft、SUPERHOT、eFootball公开，另外三款隐藏。它同时考察视觉判断、操作时序、试错学习及长期目标推进。 [1](https://www.vals.ai/benchmarks/cua_bench)

每游戏三小时，逐级里程碑合计100分，再对六游戏等权平均；不是“六款游戏通关率”。官网2026-10-13的九模型表最高19.17分，仍有大幅余量，但每个模型—游戏仅一次试验，分差没有重复采样保障。隐藏游戏对照用于监测定向训练，不能单凭公开/隐藏差距宣布污染。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 基本信息

- **简称**：CUA-bench [1](https://www.vals.ai/benchmarks/cua_bench)

- **全称**：CUA-bench [1](https://www.vals.ai/benchmarks/cua_bench)

- **基准版本**：2026-10-13官方榜快照 [1](https://www.vals.ai/benchmarks/cua_bench)

- **主板块**：Agent [1](https://www.vals.ai/benchmarks/cua_bench) 注：编辑归档，不代表官方分类。

- **子领域**：游戏；计算机使用 [1](https://www.vals.ai/benchmarks/cua_bench) 注：编辑归档，不代表官方分类。

- **官方主页**：https://www.vals.ai/benchmarks/cua_bench [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 论文/报告版本：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 发布日期：已核对正式页的更新日期；尚不能把榜单更新日或访问日当作首次发布日期。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 许可证与限制：已检查正式发表材料，尚未确认覆盖任务数据/游戏资产的明确使用授权；软件、匿名预发布数据和商业游戏的许可证不能互套。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 论文/报告：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 官方代码：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 数据入口：已检查正式方法页及其外链；未定位经维护方确认的任务数据仓库/HF卡，不将结果表或上游数据充作完整题库。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 报告标题：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 发起与维护

- **发起方**：Vals AI [1](https://www.vals.ai/benchmarks/cua_bench)

- **维护方**：Vals AI [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 合作方：正式材料不足以确认独立研究合作方；工具提供者、模型厂商和上游仓库不能据此当作合作机构。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 核心作者：正式方法页可确认发布维护机构，但未找到足以确认作者姓名/出题者资格的署名或方法细目。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 设计目标

- **核心能力**：agent仅观察屏幕、使用键盘鼠标，在实时商业游戏中维持长期规划、视觉判断与操作。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **相对已有评测的缺口**：多数agent基准提供文本状态、API或DOM，这里只提供像素与键鼠，动作延迟本身影响结果。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 构建方式

- **题目来源**：六个商业游戏按三种类型配对：公开Minecraft、SUPERHOT、eFootball，各配一个同类型隐藏游戏。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **审核流程**：冻结rubric对持久证据事后重评；离线游戏原生状态、在线体育视频扫描及人工疑难复核；录像签名、哈希核验。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **质量控制**：冻结rubric对持久证据事后重评；离线游戏原生状态、在线体育视频扫描及人工疑难复核；录像签名、哈希核验。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **防污染/运行完整性**：三类游戏各设一对公开/隐藏游戏；隐藏游戏名称与里程碑不披露，用公开/隐藏差距监测后续定向训练。单次试验的差异本身不能证明污染。 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：正式方法页可确认发布维护机构，但未找到足以确认作者姓名/出题者资格的署名或方法细目。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 数据形式

- **规模**：6个游戏，每游戏3小时；每个模型-游戏单次trial。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **题型**：屏幕视觉与键鼠交互；里程碑要求按顺序完成。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **模态**：屏幕图像；视频证据；键盘鼠标 [1](https://www.vals.ai/benchmarks/cua_bench)

- **难度与任务跨度**：沙盒、第一人称反应、体育三类；每游戏3小时。Minecraft依次13级里程碑，SUPERHOT 25级，eFootball从Beginner至Professional五档；不是统一题目难度标签。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **公开与隐藏划分**：3个公开游戏；另3个游戏名与里程碑不公开（官网明确），按相同规则计分。 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 语言覆盖：正式方法页说明为英文，但没有完整披露任务指令、程序/游戏内容的语言覆盖，不能仅据报告语言确定全量语种。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 评测方法

- **指标**：六游戏各0–100里程碑分的均值；另报动作延迟和估计API成本。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **评分规则**：每游戏阶梯共100分，后续里程碑不能跳过先决步骤；不足证据为评分失败，不直接计零。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **提示与运行配置**：每游戏三小时含读屏、学习控制、失败重试和shell思考；使用厂商harness，通过MCP驱动GPU桌面，不得读取游戏内存或文件。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **可比性限制**：分数是里程碑均值，不等于游戏通关率；每cell单trial，公开-私有差距不能自动归因为训练污染。 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 最新情况

- **核验日期**：2026-11-07 [1](https://www.vals.ai/benchmarks/cua_bench)

- **现行版本与采用证据**：version：2026-10-13官方榜快照；trending：B；heat_evidence：Vals于2026-10-13更新9模型的商业游戏结果。热度B，目录与详情同属Vals，不能视为两个独立采纳方。；evidence_2026_h2：url：https://www.vals.ai/benchmarks/cua_bench；date：2026-11-07；date_type：observed_on；note：本次打开核验；来源发布/修订日以正文描述为准，观察日期不当作运行日期。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **饱和度判断**：编辑判断：当前榜首均分19.17/100，未接近满分；仅适用于六游戏里程碑协议，不能外推一般计算机使用能力。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **已知问题与证据边界**：分数是里程碑均值，不等于游戏通关率；每cell单trial，公开-私有差距不能自动归因为训练污染。 [1](https://www.vals.ai/benchmarks/cua_bench)

- **关联与衍生关系**：CUA-bench只收商业游戏键鼠评测；不能与OSWorld、一般CUA能力或游戏子分项混同。 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 更新与修订：当前可核实的是网页方法/榜表更新；尚未定位独立论文的版本历史，不把网页更新时间伪作arXiv修订。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 榜单快照

- **快照采集日**：2026-11-07 [1](https://www.vals.ai/benchmarks/cua_bench)

- **官方榜/正式委托榜**：https://www.vals.ai/benchmarks/cua_bench [1](https://www.vals.ai/benchmarks/cua_bench)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | GPT-6 Astra | 19.17 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 2 | Claude Opus 5.5 | 14.0 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 3 | Claude Fable 5.1 | 13.17 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 4 | Claude Opus 5 | 9.0 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 5 | GPT-5.6 Sol | 8.33 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 6 | Wonder | 7.17 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 7 | Muse Spark 1.3 Max | 5.83 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 8 | Gemini 4 Argon | 4.83 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 9 | Gemini 3.8 Flash | 4.17 | 六游戏平均里程碑分 /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |


表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：分数是里程碑均值，不等于游戏通关率；每cell单trial，公开-私有差距不能自动归因为训练污染。 榜表自写更新时间：2026-10-13；采集日不等于运行日。 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：未定位同一版本与可比协议下独立第三方成绩榜；论文被引用或模型卡自报不等于独立复现。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 联系方式

- **官方社交**：https://x.com/ValsAI [1](https://www.vals.ai/benchmarks/cua_bench) 注：官网页脚公开链接；不读取或操作X账户。

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 公开问题追踪：已检查正式方法页和所指向的代码入口；未定位可确认属于此基准的独立实现/问题追踪。上游harness链接不替代基准自身代码。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 隐私政策：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 原始文件

- **其他正式文档**：type：已打开官方网页/论文；url：https://www.vals.ai/benchmarks/cua_bench [1](https://www.vals.ai/benchmarks/cua_bench)

- **中的论文副本**：待核实 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 原始PDF：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cua_bench)
- SHA-256：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cua_bench)
- PDF字节数：已重读正式方法页及其外链；未定位可交叉确认的独立arXiv条目/PDF，故不填写论文版本、PDF校验或大小。网页研究报告与独立PDF区别记录；不将未定位解释为官方未公开。 [1](https://www.vals.ai/benchmarks/cua_bench)
- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [1](https://www.vals.ai/benchmarks/cua_bench)

## 变更记录

- date：2026-11-07；timezone：；change：首次建立近期热门中文研究条目。CUA-bench只收商业游戏键鼠评测；不能与OSWorld、一般CUA能力或游戏子分项混同。 热度与榜单口径分离，不确定值标记待核实。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://www.vals.ai/benchmarks/cua_bench)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
