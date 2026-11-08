# EBR-bench

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.

;

Over the first five in-game days of the Earthborne Rangers board game, EBR-bench tests how an agent plans, manages resources, and improves from repeated play and from notes. It counts the completion proportion of 21 objectives. It is not a measurement of clearing a full campaign of 20–25 days. After a game reset, the agent can retain experience only through notes, and the weights are not updated. [1](https://epoch.ai/benchmarks/ebr-bench) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

The conclusion that the system "did not learn," in the article published on 2026-07-01, corresponds to an early configuration. The current method has reached v4 of 2026-09-22: usually the best of 2 scored attempts after 8 learning attempts, with 5 independent samples, plus a no-learning ablation. Banned cards, the compression threshold, and the sample size have changed several times. A score from a different version, or a high absolute score, cannot be equated with a learning gain. The mean of the first-place entry in the public CSV is about 0.781. [1](https://epoch.ai/benchmarks/ebr-bench) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

## Basic information

- **简称**：EBR-bench [1](https://epoch.ai/benchmarks/ebr-bench)

- **全称**：EBR-bench [1](https://epoch.ai/benchmarks/ebr-bench)

- **基准版本**：v4 methodology（2026-09-22） [1](https://epoch.ai/benchmarks/ebr-bench)

- **论文/报告版本**：Web release article of 2026-07-01; for the current methods v4, see also the benchmark update record [2](https://epoch.ai/publications/earthborne-rangers-benchmark) [1](https://epoch.ai/benchmarks/ebr-bench)

- **发布日期**：2026-07-01 (date the Epoch article was published) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

- **主板块**：Agent [1](https://epoch.ai/benchmarks/ebr-bench) 注：Editorial filing. It does not represent an official classification.

- **子领域**：持续学习；游戏 [1](https://epoch.ai/benchmarks/ebr-bench) 注：Editorial filing. It does not represent an official classification.

- **论文/报告**：https://epoch.ai/publications/earthborne-rangers-benchmark [2](https://epoch.ai/publications/earthborne-rangers-benchmark) 注：A research article on the web; it is not presented as an arXiv/PDF.

- **官方主页**：https://epoch.ai/benchmarks/ebr-bench [1](https://epoch.ai/benchmarks/ebr-bench)

- **报告标题**：AI doesn't get better at this board game with practice [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

**仍待核实**（不推断为未公开）：

- 许可证与限制：Formally published materials have been checked, and an explicit license covering use of the task data and game assets has not been confirmed. Licenses for the software, the anonymized prerelease data, and the commercial games cannot be substituted for one another. [1](https://epoch.ai/benchmarks/ebr-bench)
- 官方代码：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://epoch.ai/benchmarks/ebr-bench)
- 数据入口：The readable file at https://epoch.ai/data/benchmarks.csv contains only model evaluation results, not the original game tasks or card materials; a release address for the formal task data has not yet been located. [1](https://epoch.ai/benchmarks/ebr-bench) [3](https://epoch.ai/data/benchmarks.csv)

## Origin and maintenance

- **发起方**：Epoch AI [1](https://epoch.ai/benchmarks/ebr-bench)

- **合作方**：Generality Labs conducted an independent audit commissioned by Epoch; Earthborne Games is neither a research collaborator nor an endorser, and Epoch explicitly states that the work was carried out independently. [1](https://epoch.ai/benchmarks/ebr-bench)

- **核心作者**：Benjamin Ou；Greg Burnham [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

- **维护方**：Epoch AI [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://epoch.ai/benchmarks/ebr-bench)

## Design goals

- **核心能力**：By repeatedly playing the unfamiliar, complex board game Earthborne Rangers, it measures note-taking, long-term strategy, and the ability to learn from experience. [1](https://epoch.ai/benchmarks/ebr-bench)

- **相对已有评测的缺口**：It checks not only the first answer, but whether performance improves after consecutive attempts on the same task; the performance score and the learning gain must be kept distinct. [1](https://epoch.ai/benchmarks/ebr-bench)

## Construction

- **题目来源**：An independent digital game, with an initial five game days; 21 attainable objectives are defined from tasks, rewards, and important events. Copyright in the game belongs to Earthborne Games, which does not mean that it took part in developing the benchmark. [1](https://epoch.ai/benchmarks/ebr-bench)

- **审核流程**：Generality Labs, commissioned by Epoch, reviewed v1 in July 2026; it endorsed the game design and at the same time questioned whether continual learning was actually elicited and how context was organized; an engine bug was fixed on August 27. [1](https://epoch.ai/benchmarks/ebr-bench)

- **质量控制**：Generality Labs, commissioned by Epoch, reviewed v1 in July 2026; it endorsed the game design and at the same time questioned whether continual learning was actually elicited and how context was organized; an engine bug was fixed on August 27. [1](https://epoch.ai/benchmarks/ebr-bench)

- **防污染/运行完整性**：A relatively little-known game was chosen to reduce the chance of memorization, but this is not deduplication by retrieval, nor a verifiable guarantee of a training cutoff; v4 removes, from both the reference materials and the game, one card that could bypass a strategic difficulty, which is mainly a correction of validity rather than removal of training contamination. [1](https://epoch.ai/benchmarks/ebr-bench) [2](https://epoch.ai/publications/earthborne-rangers-benchmark)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：The formal methods page can confirm the organization that releases and maintains it, but no byline or methods detail sufficient to confirm author names or question-writer qualifications was found. [1](https://epoch.ai/benchmarks/ebr-bench)

## Data format

- **规模**：Each run has 10 plays: 8 for learning and the last 2 for scoring; each model usually has 5 independent samples, and older experiments have 10; each play has at most 21 goals. [1](https://epoch.ai/benchmarks/ebr-bench)

- **题型**：Card lookup, route planning, note management, and multi-step game decisions. [1](https://epoch.ai/benchmarks/ebr-bench)

- **模态**：文本；地图图像；工具调用 [1](https://epoch.ai/benchmarks/ebr-bench)

- **难度与任务跨度**：The introductory campaign of five game days is played repeatedly; the full campaign is 20–25 days. One session for a skilled human takes about 2–4 hours and requires strategic deck building, tactical management of resources, and notes across games; it cannot be treated as a direct measure of general lifelong learning. [1](https://epoch.ai/benchmarks/ebr-bench)

- **公开与隐藏划分**：Epoch explicitly does not distribute or sell the underlying copyrighted game materials; what is public is the method and the scores, and the license for the complete games and the evaluation data is Unverified. [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 语言覆盖：The formal methods page is written in English, but it does not fully disclose the language coverage of the task instructions and of the program and game content, so the full set of languages cannot be determined from the report language alone. [1](https://epoch.ai/benchmarks/ebr-bench)

## Evaluation

- **指标**：Topline: for each run, take the higher of the last two scores, then aggregate across samples; the score is the proportion of 21 goals; learning gains are also studied by ablation. [1](https://epoch.ai/benchmarks/ebr-bench)

- **评分规则**：Scoring is by completed objectives, and a high game score is not treated directly as a continual-learning gain; learning gain must be compared with an ablation that plays only twice. [1](https://epoch.ai/benchmarks/ebr-bench)

- **提示与运行配置**：The default is a single agent, with specified cards disabled and a compression threshold of 250k tokens; the Fable series uses 90% of the nominal context; ReAct and the Deep Agent multi-agent setting are kept separate. [1](https://epoch.ai/benchmarks/ebr-bench)

- **可比性限制**：Scoring changes in v1/v2, selection of the better compression-threshold result in v3, and the v4 card ban together with the sample-size change make historical results not fully comparable; the default single agent is not mixed with multi-agent runs. [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://epoch.ai/benchmarks/ebr-bench)

## Current status

- **核验日期**：2026-11-07 [1](https://epoch.ai/benchmarks/ebr-bench)

- **现行版本与采用证据**：version：v4 methodology（2026-09-22）；trending：A；heat_evidence：The official update of 2026-09-22 moved to v4 and, in the audit response of October, reported learning results for new models. This rereading of the Epoch CSV shows a Mistral Large 4 run on November 2. A is a candidate grade, and multiple independent creating organizations are not claimed on that basis.；evidence_2026_h2：url：https://epoch.ai/benchmarks/ebr-bench；date：2026-11-07；date_type：observed_on；note：Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date. [1](https://epoch.ai/benchmarks/ebr-bench)

- **更新与修订**：Updates to the method on the web page: on 2026-07-27, v2 was changed to take the best of the last two games and ablated learning was added; on 08-11, v3 compares compression thresholds; on 08-19, a human experiment was added; on 09-22, v4 bans cards, defaults to 5 samples, unifies compression at 250k for most models, and moves non-default learning graphs into internal analysis. [1](https://epoch.ai/benchmarks/ebr-bench)

- **饱和度判断**：The highest mean_score in the current CSV is about 0.781; the methods page says that frontier models occasionally reach top human performance, but the default score is not a learning gain. A full score is 21 objectives, and humans already have 21/21. [1](https://epoch.ai/benchmarks/ebr-bench) [3](https://epoch.ai/data/benchmarks.csv)

- **已知问题与证据边界**：Scoring changes in v1/v2, selection of the better compression-threshold result in v3, and the v4 card ban together with the sample-size change make historical results not fully comparable; the default single agent is not mixed with multi-agent runs. [1](https://epoch.ai/benchmarks/ebr-bench)

- **关联与衍生关系**：Earthborne Rangers is the name of the game, and EBR-bench is an Epoch research benchmark; this is kept distinct from the copyright in the game itself and from the relationship to its authors. [1](https://epoch.ai/benchmarks/ebr-bench)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://epoch.ai/benchmarks/ebr-bench)

- **官方榜/正式委托榜**：https://epoch.ai/benchmarks/ebr-bench [1](https://epoch.ai/benchmarks/ebr-bench)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | GPT-6.1 Terra (max) | 0.780952380952381 | CSV mean_score (0–1; proportion of 21 targets)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 2 | GPT-6 Astra (max) | 0.7619047619047619 | CSV mean_score (0–1; proportion of 21 targets)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 3 | Claude Opus 5.5 (max) | 0.7142857142857142 | CSV mean_score (0–1; proportion of 21 targets)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 4 | Gemini 4 Argon (high) | 0.6476190476190476 | CSV mean_score (0–1; proportion of 21 targets)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |
| 5 | Claude Fable 5.1 (max) | 0.5714285714285714 | CSV mean_score (0–1; proportion of 21 targets)；运行/发布日见覆盖说明；[3](https://epoch.ai/data/benchmarks.csv) |

> GPT-6.1 Terra (max)：stderr：0.05128728387747146；run_id：65SHyNJX5oxVADzzjkssFK；started_at：2026-10-27；note：Sorted by the mean in the current CSV; task version is empty, so it cannot be certified that all entries follow the unified v4 card-ban protocol. [3](https://epoch.ai/data/benchmarks.csv)

> GPT-6 Astra (max)：stderr：0.08384198505551908；run_id：GhVYxWxttDxZ7akiJQPYsE；started_at：2026-08-31；note：Sorted by the mean in the current CSV; task version is empty, so it cannot be certified that all entries follow the unified v4 card-ban protocol. [3](https://epoch.ai/data/benchmarks.csv)

> Claude Opus 5.5 (max)：stderr：0.07063046178186345；run_id：iKWWUmcuzRjqisoshKVEpL；started_at：2026-09-23；note：Sorted by the mean in the current CSV; task version is empty, so it cannot be certified that all entries follow the unified v4 card-ban protocol. [3](https://epoch.ai/data/benchmarks.csv)

> Gemini 4 Argon (high)：stderr：0.04902681019517619；run_id：mSJNKA7nCp2eZVqMo5nTUP；started_at：2026-10-14；note：Sorted by the mean in the current CSV; task version is empty, so it cannot be certified that all entries follow the unified v4 card-ban protocol. [3](https://epoch.ai/data/benchmarks.csv)

> Claude Fable 5.1 (max)：stderr：0.06023386019368341；run_id：8JukffGviNAYHXSdTJvswB；started_at：2026-09-08；note：Sorted by the mean in the current CSV; task version is empty, so it cannot be certified that all entries follow the unified v4 card-ban protocol. [3](https://epoch.ai/data/benchmarks.csv)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：The current CSV was reread and filtered exactly on task=EBR-bench; the task version field is empty, and run_id and the run start time are kept. Comparability with v1, v2, v3, and v4 listed on the methods page is limited; the CSV does not provide a unified leaderboard update time, and the collection date is not used in its place. [3](https://epoch.ai/data/benchmarks.csv) [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [1](https://epoch.ai/benchmarks/ebr-bench)

## Contact

- **官方社交**：https://x.com/EpochAIResearch [1](https://epoch.ai/benchmarks/ebr-bench)

- **隐私政策**：https://epoch.ai/privacy [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://epoch.ai/benchmarks/ebr-bench)
- 公开问题追踪：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://epoch.ai/benchmarks/ebr-bench)

## Original files

- **其他正式文档**：type：Official research article, not a standalone PDF；url：https://epoch.ai/publications/earthborne-rangers-benchmark；type：Model-score CSV, not task data；url：https://epoch.ai/data/benchmarks.csv [1](https://epoch.ai/benchmarks/ebr-bench) [3](https://epoch.ai/data/benchmarks.csv)

- **中的论文副本**：待核实 [1](https://epoch.ai/benchmarks/ebr-bench)

**仍待核实**（不推断为未公开）：

- 原始PDF：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://epoch.ai/benchmarks/ebr-bench)
- SHA-256：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://epoch.ai/benchmarks/ebr-bench)
- PDF字节数：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://epoch.ai/benchmarks/ebr-bench)
- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://epoch.ai/benchmarks/ebr-bench)

## Changelog

- date：2026-11-07；；change：首次建立近期热门中文研究条目。Earthborne Rangers is the name of the game, and EBR-bench is an Epoch research benchmark; this is kept distinct from the copyright in the game itself and from the relationship to its authors. 热度与榜单口径分离，不确定值标记待核实。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://epoch.ai/benchmarks/ebr-bench)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
