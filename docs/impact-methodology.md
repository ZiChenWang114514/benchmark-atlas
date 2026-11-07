# Benchmark Constitution 学术影响力指数（BCI）

**方法版本：0.2（全名录、证据收缩、最低覆盖门槛；探索性学术影响排序）**  
**更新日期：2026-11-08，Asia/Seoul / KST。所有权重均为本站公开的方法选择，并非外部机构认可或已经实证拟合的参数。**

## 一、我们衡量什么

BCI（Academic Impact Index）综合衡量一个 benchmark 的**学术传播、实际使用、原创贡献与评测可靠性**，而不是给论文作者、机构或模型排名。流行不等于正确，冷门不等于低质量；引用也可能源于批评。本站同时展示原始数据、分项、来源、缺失项、证据覆盖与风险标签，禁止只展示一个总分。

统计单位是**可识别的 benchmark/版本**。同一模型的发布页、model card、性能展示页重复出现同一评测，只算一次采用。一个论文或 GitHub 仓库可能包含多个独立 benchmark，不能因为共用论文/仓库就自动合并；明确的简称和同名条目才能合并。历史版本保留，不能将旧版成绩或引用直接当成新版事实。

本方法借鉴而**不冒称复现** Altmetric、RCR、FWCI、BetterBench 等体系。尤其：本库的领域×年龄组分位数只是“本名录内的校正”，不是全学界 field-normalized citation，也不是 NIH RCR 或 Elsevier FWCI。

## 二、维度与权重

权重合计 100%。影响传播占较大比重，但质量 18%、新颖度 12% 独立存在，避免 star 或厂商宣传支配“学术水平”。

| key | 维度 | 权重 | 定义、来源、归一化与理由 |
|---|---|---:|---|
| citations_total | 引用积累 | 10% | 保留主论文原始总引用；计分采用按同论文归属数平方根折减的引用量，防止子任务继承整篇合集论文影响力。OpenAlex精确外部身份记录优先，Semantic Scholar备用，两库不相加。领域内 `log1p` 与百分位混合，记录来源与论文匹配方式。代表持久传播，但权重低于年龄校正速度，减少资历优势。 |
| citation_velocity | 同龄引用速度 | 15% | 归属折减后的引用 C* /（发布月龄 a + 3），同领域×同年龄桶比较；发布初期也能进入本年龄桶高分位。3个月平滑避免刚发布一天的偶然引用爆炸。不把线性外推写成真实未来引用。按年引用同时存档，留作后续近期加速度分析。 |
| github | 代码生态 | 8% | 官方仓库 `stargazers_count`（内部65%）和两次实测快照的月净增（35%）。来源 GitHub REST `/repos/{owner}/{repo}`。各自对数+分位；共享仓库按名录中共享条目数平方根降权，避免公共 harness 的 star 被每个子任务重复继承。无快照时增长为 null，不以 star/仓库年龄伪装近期增速。 |
| huggingface | 数据使用 | 5% | 官方 HF dataset 的最近30日下载（70%）和累计点赞（30%），Hub API `/api/datasets/{org/name}`。分别对数+分位。同一HF dataset被多个条目共享时按共享条目数平方根降权，防止合集下载量重复归属。下载不是唯一用户数，更不是评测次数；不同下载计数机制不可过度比较，因此权重较低。 |
| model_adoption | 前沿模型采用 | 10% | 从 `frontier/heat.json` 读取被最近20个模型采用的次数；按模型去重。对数+分位，原始 count/share 仍是业界频次榜主指标。缺少 heat 文件、映射不明或未声明穷尽覆盖时，不把未匹配项记为0。 |
| evaluator_adoption | 独立评测机构采用 | 8% | AA、Epoch、LMArena、HELM、Scale SEAL、Vals 等机构实际纳入持续评测的独立机构数；一个机构多个网页仍算一个。必须人工/专门采集器核验 `assessment.evaluator_adoptions={value:[机构名],sources:[...]}`。只在报告提及、新闻报道或 Epoch 负面审查不算采用。对数+分位。 |
| community | 独立社区反馈 | 5% | 去重公开讨论数（20%）、90日 issue 活跃事件（20%）、第三方可复现报告数（60%）；GitHub Issues/Discussions 与第三方论文、复现仓库为来源。每项对数+分位；负面反馈记录风险，不能等同认可。当前脚本不自动爬取社交平台或把 open issues 当活跃度，未审计即 null。 |
| novelty | 研究新颖度（代理） | 12% | 与**更早发布**的 benchmark 比较：文本 TF-IDF 余弦距离（70%）、任务形式稀有度（15%）、领域稀有度（15%）。描述而非名称参与编码，字符2–4gram支持中英文。每项天然映射0–100；当前文本方法仅代理，可信系数0.35。文本稀有≠科学创新，人工确认才可升级。 |
| quality | 方法与工程质量 | 18% | 人工/专家验证20%、污染防护20%、独立复现20%、适用许可明确10%、维护审查10%、独立外审20%。借鉴 BetterBench 生命周期，必须逐项附原始证据；0=已审查且不满足，50=部分满足，100=充分满足，可保存细化分。缺失不记0。GitHub有license文件不代表数据许可清晰，因此不自动给该项满分。 |
| distinctiveness | 非同质性 | 4% | 与当前名录近邻描述的最大相似度 s。得分 `100×[1−max(0,s−0.8)/0.2]`，截断0–100。以独立小维度施加同质化惩罚，和新颖度相关但不是第二次大幅惩罚。s>0.8 标记 homogeneous；文本代理可信系数0.35。 |
| headroom | 未饱和与区分度 | 3% | 有可比上下界的高分为优指标：`100×[1−(SOTA−floor)/(ceiling−floor)]`（70%），另加审计后的区分度评分（30%）。归一化SOTA≥95%标记 saturated。非有界、低分为优、混版本或无统一预算的指标不擅自计算。饱和不抹去历史学术价值，因此仅占3%。 |
| maintenance | 时效与维护 | 2% | 最后一次实质更新距今d日，得分`100×2^(−d/365)`。人工核验的实质更新优先，GitHub pushed_at/HF lastModified 只是较弱代理（可信系数0.5）。不能把稳定、正确的旧测评仅因少更新而大幅贬值。 |

### 共同的数量归一化

对已观测的非负数量 x，以比较组 P 为基准：

```
L(x) = min(1, log(1+x) / Q95(log(1+P)))
F(x) = [数量(P<x) + 0.5×数量(P=x)] / |P|
N(x) = 100×[0.5×L(x) + 0.5×F(x)]
```

若比较组全为0，返回0；负净增在“增长得分”中截为0，但原始负值完整保留。Q95 抑制头部极端值；同值使用中秩，避免任意排序。分位值受名录组成影响，样本变动会改变得分，不应解释成绝对计量单位。

数量优先在同领域、至少20个有值的条目中归一化，否则回退全名录，并在 `normalization` 公布比较组与样本数。**这不是对真实学科引用基线的完整估计。**

### 新 benchmark 公平机制

年龄桶为 `[0,3)、[3,6)、[6,12)、[12,24)、[24,60)、60+` 月；发布日期优先用 registry，缺失时优先使用 arXiv 官方 API 的首次提交日期，再回退精确匹配论文的 API publicationDate，并公开替代依据。后来的期刊出版日期不得重置引用年龄；人工核验的 benchmark 首发日期优先于论文日期。只有年月的日期按月15日作为计算约定，不冒称知道准确发布日期；只有年份按7月1日计算并标记近似。

引用速度优先用同领域×年龄桶；不足20个时退为同年龄桶跨领域；仍不足20个则保留小样本分位，但可信系数乘 `n/20`，标记 `small_age_cohort`。不能退到全年龄组让新旧样本直接竞争。月龄不足3个月标记 `early_signal`，不是低质量标签。缺少有效日期则速度为 null，不猜发布日期。当前不使用最近一年的截断引用自动计算“精确近月速度”，因为自然年计数并非滚动365日，且部分 API 只返回部分历史。

新benchmark可以靠同龄传播、原创任务与质量证据进入高位，不必等待多年积累。与此同时，“发布短”本身不是加分项，不能用不稳定外推制造高影响力。

## 三、缺失值、可信度与综合分

### 不把“没有取得”写成零

每个分项 s_k 都是0–100或 null。API失败、论文身份未匹配、未核查质量项、只有共享项目但无可归属指标等情况显式缺失。只有成功返回的数字0或完整核查确认的“没有”才能记0。

每个维度有证据可信系数 r_k：直接计数一般为1；子项不齐时等于可用子项权重之和；新颖度/同质化文本代理0.35（新颖度的任务/领域子项缺失时再乘可用子项权重）；维护仅push代理0.5；小年龄桶进一步缩减。维度内部也只按可用子项重新加权。

```
有效权重 w'_k = w_k × r_k （缺失时为0）
observed_score = Σ(w'_k × s_k) / Σw'_k
coverage = Σw'_k
BCI = coverage × observed_score + (1−coverage) × peer_median
```

因此不把缺失当成惩罚性零分，但会降低可用证据量，并把过于极端的稀薄证据得分拉回同龄参照中位数。peer_median来自coverage≥0.4且身份无未解决冲突的参照条目，排除自己；优先同领域×同龄组（至少5条），再同龄组（至少10条），再全库有足够证据的条目。若没有任何参照，公开使用中性50作为方法先验，而不是声称观测到了50分。输出alpha、peer_group、peer_n及原始observed_score。coverage 只是**证据覆盖度，不是统计置信区间或“得分正确概率”**。≥0.8为high，0.6–0.8为medium，其余low。每项同时输出 `dimension_reliability` 和质量子项覆盖。

**两层发布门槛**：探索性排序必须coverage≥0.4且身份无未解决冲突；低于门槛的条目列入unscored并标记insufficient_evidence，保留分项、observed_score及shrunk_score用于诊断，但不赋名次。探索性排序仍标provisional。更严格的质量审计正式资格仍要求coverage≥0.6、质量内部覆盖≥0.5，且引用或机构采用有据，以official_rank_eligible区分。不得把探索性Top30宣传为已验证的学术水平权威结论。

### 质量底线

有带来源的 Epoch `Flawed` 结论时标记 flawed，并将综合分上限设为40；这是**本站规范性规则**，不是 Epoch 给出的数值。Flawed 必须精确对应版本与审查日期；未审查与 Not enough info 都不能擅自写 Verified/Flawed。严重污染、不可比较版本、撤稿、重复套壳应进入人工复核队列；不得通过高star或宣传抵消已确认的可靠性缺陷。

原始引用与使用影响仍保留，质量标签不改写历史事实。将来修复后应留存旧版审查与变更记录。

## 四、新颖度与同质化的审计边界

当前实现是**可复算的词面代理，不是通用句向量嵌入**：优先使用API实际返回的论文摘要（长度≥100字符），否则使用registry的描述、子领域与任务形式；不使用未经获取的论文全文。摘要与计数均按精确外部身份绑定并保留来源。新颖度仅与有已知、较早日期的条目比较，无较早参照或描述过短则 null。任务稀有度为1减去更早名录中同任务比例；领域同理。

限制：简短中文释义可能造成误判；翻译和措辞变化能产生虚假距离；同一研究的问题继承未必同质化，罕见领域也未必创新；当前未构建跨语言语义模型或人工研究谱系。前端必须显示 `lexical_novelty_proxy` 和参照样本量，不得声称已验证“原创性”。将来可冻结多语句向量版本，用聚类、领域专家双人盲审和新能力覆盖矩阵交叉确认。变更编码器/语料时升级方法版本并重算，不静默混合旧分。

## 五、业界热度指数：与BCI分开发布

**主榜仍严格按最近20个前沿模型中出现的去重次数count从高到低**；同一模型无论多少网页都只计一次。辅助“时间×厂商多样性热度”供趋势观察：

```
w_m = 2^(−模型距今发布天数/90)
A_b = Σ_m 1[b被m采用] × w_m
p_v = 厂商v对A_b的贡献 / A_b
V_eff = exp(−Σ_v p_v log p_v)
D_b = 0.5 + 0.5×min(1, V_eff / 当前窗口的已知厂商总数)
IndustryHeat_b = 100 × (A_b / 当前实际模型数) × D_b
```

当窗口满20个时分母就是20；不足20必须展示实际样本数，不补造。指数≤100。90日半衰期兼顾新发布与稳定采用；熵有效厂商数限制单一厂商大量模型制造的热度。日期或厂商缺失则辅助分不计算，count仍保留。某benchmark的采纳者均来自一家厂商时辅助分较低；这不是否认其用途，而是降低单方宣传集中度。文件 `industry-heat.json` 另行输出，不篡改Frontier Heat原来的频次排序。

模型入窗规则、模型家族合并与供应商归属由Frontier Heat采集器公开决定；仅被页面列入对比表是否算采用必须保持一致。BCI的model_adoption使用count，不暗中把这一辅助分替代原始采用次数。

## 六、数据管线与事实溯源

1. `registry_merge.py`对原始分片建立不可变occurrence快照，先绑定审计修正再改ID；应用两份corrections中的drop/merge_into/fix/add。相同ID的独立benchmark先分离，RAR-b检索改写不能覆盖原推理基准。自合并只移除确切的重复发生项，家族/版本/子任务完整历史存入variants，错误/非benchmark的drop另存归档。science2.jsonl是增量而非整表替代：按science2.changes仅应用真实变动字段，合并sources；与审计重叠时审计结论优先，尤其不能恢复旧日期、错误论文或已清空字段。实现先绑定/执行审计再应用不冲突增量，与science2先改善、审计最终覆盖等价。21条science新增中的4个既有ID全局去重；MoleculeNet子任务显式标注family_id和entry_type，共享论文不重复计满额引用。未指定新ID的24项命名建议不凭空补名，列入待审。
2. 全名录而非字母序样本：S2 POST /paper/batch最多500个外部ID；OpenAlex DOI OR过滤每批最多50项，arXiv标识符使用10.48550/arXiv.<id>查询。OpenAlex携带公开项目mailto，限速低于5req/s、429指数退避并自适应降低请求频率。外部ID失败才使用严格标题/规范URL身份匹配；未确认则null。GitHub和HF按唯一资源去重调用，不用抽样补全。
3. OpenAlex counts_by_year保留供应商可用年份窗口，明确不是全历史。当前S2批量只取得总引用与论文元信息，没有取得逐条引文时不会伪造按年数据。精确外部身份对应多个索引版本时，不相加，而选择单一版本中实际返回的最大计数及其work ID，作为避免重复累计的可复算口径；优先OpenAlex，缺失才S2。跨供应商差异与版本覆盖限制公开，不宣称计数已去自引或为完整引文并集。
4. GitHub只查公开仓库元数据；HF只查明确的dataset ID，不猜测同名镜像。所有原始指标均在 `metrics.provenance` 保留API URL、accessed时间和对应字段。GitHub原始时间有自带时区，输出保留机器可读ISO；面向用户的运行报告统一KST。
5. `cache/responses` 存无密钥的请求URL与原始响应、状态、采集日期；成功缓存24h；404及资源级拒绝负缓存30min；429按退避/冷却处理，不把未知锁成24h零值。逐条落盘 `cache/records`；快照单独保存。超时、429指数退避和主机熔断，不使用高并发绕限流。GitHub全局配额/鉴权拒绝后停止该主机；HF某个private/gated数据集的401只保留该资源为null、不重试它，不影响其他公开数据集。绝不通过cookie、凭据文件或替代身份绕过限制。
6. 每次compute重新读取所有当前分片，按未变更记录读取缓存；新分片可追加，重跑即可加入。输出 `impact/index.json`（集成时复制为仓库 `data/impact/index.json`）和 `registry/registry.json`（集成为 `data/registry/registry.json`）。脚本只操作 `/workspace/bc` staging，不改主仓库、不push、不设定新外部定时任务。
7. 环境变量可提供 `S2_API_KEY`、`OPENALEX_API_KEY`、**明确获准用于公共仓库指标的** `GH_TOKEN`。脚本不读取任何凭据文件，不打印请求头，不将token写入缓存或URL。历史临时token仅授权项目仓库/Pages，不扩大到其他仓库的指标采集；本轮公开GitHub查询不读该token。未授权或受限则保留null。

### 人工证据扩展格式

```json
{
  "assessment": {
    "human_validation": {"value": 50, "sources": [{"url":"https://官方论文或报告", "accessed":"2026-11-07"}]},
    "evaluator_adoptions": {"value": ["HELM"], "sources": [{"url":"https://实际评测证据", "accessed":"2026-11-07"}]},
    "epoch_verdict": {"value":"Flawed", "sources":[{"url":"https://准确版本审查页", "accessed":"2026-11-07"}]}
  }
}
```

示例只是schema说明，**不代表任何条目的事实或已有评级**。分项键包括 `human_validation`、`contamination_protection`、`reproducibility`、`license_clarity`、`maintenance_review`、`external_review`；社区键为 `community_discussions`、`issue_activity_90d`、`third_party_reproductions`；饱和度为 `sota_score`、`metric_floor`、`metric_ceiling`、`discrimination_score`；实质更新时间为 `last_substantive_update`。来源必须有真实URL与accessed，审查者/版本应另附，以便复核。

## 七、防刷榜与治理

- **身份去重**：论文预印本与正式版不累加；同一模型的多页引用不重复；子集、复刻、翻译及版本关系需要公开。
- **共享资源归属**：公共harness、合集仓库、作者主页的star不直接归属某一个评测；共享仓库显式标注、降权，后续应人工剔除不可归属资源。HF镜像/分片不盲目相加。
- **异常监测**：日快照保留star净增、下载变化和来源；暴涨不能直接认定作弊，也不能未经核查当成可靠传播。发布异常标签与复核记录，而非暗中改数据。当前脚本没有实现机器人账号识别、付费点赞识别或完整引文圈分析，不能宣称已自动防刷。
- **引用操纵**：未来在可取得完整作者/引文图时并列报告自引与去自引、引文网络集中度；目前总引用不冒充已去自引。批评性引用和引用数据集名称未必代表实际采用。
- **质量双人审查**：人工项至少两人独立评分、冲突仲裁；作者利益冲突公开。当前尚未完成，不自动填充分。
- **透明变更**：权重、样本池、编码器、归一化基准和代码版本留档；每日快照与上一版对照，显示因为新增样本造成的重排。按领域和年龄提供筛选，避免总榜掩盖自然科学小领域。
- **上线前稳健性检验**：建议对各权重±20%扰动、去掉单一维度重排、比较领域内名次和Kendall相关；公布名次范围。当前版本未把这类范围包装成已经计算的统计置信区间。

## 八、局限性与正确使用

BCI是开放的方法提案，未经外部效度标定。现阶段获取率、名录中的训练集误收、标题歧义、API覆盖与跨领域偏差都可能大于名次差异。引用库会滞后、重复或漏记，paper发布日期不必等于benchmark首次发布；API计数跨天不同不一定异常。新颖度与同质化都是词面代理，和质量审查一样不能由宣传语代替事实。**没有人工质量与独立复现覆盖的总榜，不足以衡量“学术水平高低”。**

名录条数不是审计完成数；API命中率不是收录准确率；试算Top20不是正式推荐。建议同时呈现：采用频次榜、年龄组上升榜、质量审计榜、各领域榜、历史影响榜，而不是一张总榜取代全部判断。

## 九、参考资料（本轮检索日：2026-11-07）

1. Altmetric，*How is the Altmetric Attention Score calculated?*：多源加权、去重与注意力不等于学术质量。https://help.altmetric.com/en/articles/9800513
2. Hirsch (2005)，*An index to quantify an individual's scientific research output*：h-index是研究者/产出集合指标，不适宜直接套给单一benchmark，因此仅作为“积累偏置”的参照，不加入公式。https://doi.org/10.1073/pnas.0507655102 （原文抓取超时，定义另据 https://guides.lib.usf.edu/promotiontenure/metricsglossary 核对）
3. Hutchins et al. (2016)，*Relative Citation Ratio*：按共被引领域与年份校正的文章影响力。https://doi.org/10.1371/journal.pbio.1002541
4. NIH iCite，RCR方法与新论文暂定状态说明。https://support.icite.nih.gov/hc/en-us/articles/9105587565851-Relative-Citation-Ratio-RCR
5. Elsevier，*What is Field-Weighted Citation Impact (FWCI)?*：以同领域、同年与同类型论文的预期引用校正；本站不声称拥有Scopus全量基线。https://service.elsevier.com/app/answers/detail/a_id/14894/supporthub/scopus/ （官方页本轮返回401；定义另据佛罗里达大学图书馆 https://guides.uflib.ufl.edu/metrics/article 核对）
6. BetterBench 方法：46条生命周期最佳实践、专家双人评分与设计/实现/文档/维护维度。https://betterbench.stanford.edu/methodology.html ；https://arxiv.org/abs/2411.12990
7. Epoch Benchmark Reviews rubric v1：Verified/Flawed/Not enough info、评分缺陷与不可比版本等审查。https://epoch.ai/data/benchmark-reviews-documentation/methodology
8. Semantic Scholar Graph API。https://api.semanticscholar.org/api-docs/graph
9. OpenAlex works与鉴权文档。https://help.openalex.org/data/works/ ；https://help.openalex.org/api/authentication/
10. GitHub REST repository与star语义。https://docs.github.com/en/rest/repos/repos#get-a-repository ；https://docs.github.com/en/rest/activity/starring
11. Hugging Face Hub dataset API。https://huggingface.co/docs/hub/api ；https://huggingface.co/docs/huggingface_hub/guides/search

> 参考资料为方法依据，不代表上述机构背书本站权重、阈值或结论。

### 当前实现的额外保障

- 没有任何已观测传播/使用指标时，即使文本代理显示独特，也不输出综合分（score=null）；不能让“仅有描述、没有影响力证据”的条目凭一个代理维度获得100分。
- 同一ID出现不同arXiv/DOI的实质冲突时，进入identity_conflict并暂不评分；原始冲突仍保留报告。名字相同但没有论文标识符印证的不同ID不贸然合并。名录中的占位标题不用于跨ID合并。
- 未能评分的记录单列 `unscored`（rank/score为null），不进入 `ranking`，确保主榜rank是整数、score为0–100；不把未评分条目硬塞到有意义的学术名次中。
- 质量人工项和社区项必须附真实HTTP(S)来源与有效accessed日期，不能只填一个无来源数字。


## v0.2 修复记录与可解释性

本轮明确修复了v0.1在线样本按字母序截取180条导致的严重排序偏差；旧Top20已废弃。所有当前名录行都进入采集/缓存续跑，预算不足时使用确定性哈希顺序而非字母序，并公开未覆盖项。模型卡采用先匹配规范ID，再采用不歧义别名；MMLU/MMMLU、SWE各版本不得由父级aliases劫持对方的采用次数。

论文、仓库、HF合集共享归属均保留真实原始计数，计分折减只是明确标注的派生量。不能把一个MTEB子任务的整篇综述论文引用、公共harness的star当作该子任务的独立影响力；家族归并后也不重复累加子任务指标。摘要长度、元数据完整度与创新性本身并非同一概念，新颖度仍仅为可信系数0.35的代理。

common-sense核查只作为错误诊断：检查SWE-bench、GPQA、HLE、MMLU、MATH、HumanEval、ARC-AGI、LiveCodeBench的来源身份、缺失值、版本映射和入榜门槛。不按预期名次手工放置、不按名称加分；确实证据不足或较新版本缺少引用时如实留在insufficient_evidence。

### science2 字段解释

science2 补充的 organization 主要为论文第一作者隶属，不能未经核验解释为 benchmark 唯一发布者。科学评测中 non-LLM 子域明确保留，跨任务/领域总榜必须提供筛选。部分模型附带评测、存档自述及版本家族仍待人工范围审查；名录保留不等于质量背书。
