# CUA-bench

> In-depth verification: 2026-11-07. Unknown is not the same as Not disclosed; the web-page update date, the run date, and the access date are recorded separately.



CUA-bench places computer-use ability inside real-time commercial games. The agent can only read pixels and use a keyboard and a mouse. It cannot obtain state through a game API, memory, or a save-file side path. The six games are paired as sandbox, reaction, and sports. Minecraft, SUPERHOT, and eFootball are public, and the other three are hidden. It examines visual judgment, the timing of actions, learning by trial and error, and progress toward long-term goals. [1](https://www.vals.ai/benchmarks/cua_bench)

Each game lasts three hours. Milestones at each level sum to 100 points, and the six games are then averaged with equal weight. This is not a "clear rate across six games." The nine-model table on the official site dated 2026-10-13 has a high of 19.17 points, so substantial headroom remains, but each model-game pair has only one trial, and score differences have no guarantee from repeated sampling. The hidden-game control is used to monitor targeted training. Contamination cannot be declared from the public/hidden gap alone. [1](https://www.vals.ai/benchmarks/cua_bench)

## Basic information

- **简称**：CUA-bench [1](https://www.vals.ai/benchmarks/cua_bench)

- **全称**：CUA-bench [1](https://www.vals.ai/benchmarks/cua_bench)

- **基准版本**：2026-10-13 official leaderboard snapshot [1](https://www.vals.ai/benchmarks/cua_bench)

- **主板块**：Agent [1](https://www.vals.ai/benchmarks/cua_bench) 注：Editorial filing. It does not represent an official classification.

- **子领域**：游戏；计算机使用 [1](https://www.vals.ai/benchmarks/cua_bench) 注：Editorial filing. It does not represent an official classification.

- **官方主页**：https://www.vals.ai/benchmarks/cua_bench [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 论文/报告版本：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cua_bench)
- 发布日期：The update date on the formal page has been checked; the leaderboard update date or the access date still cannot be treated as the first-release date. [1](https://www.vals.ai/benchmarks/cua_bench)
- 许可证与限制：Formally published materials have been checked, and an explicit license covering use of the task data and game assets has not been confirmed. Licenses for the software, the anonymized prerelease data, and the commercial games cannot be substituted for one another. [1](https://www.vals.ai/benchmarks/cua_bench)
- 论文/报告：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cua_bench)
- 官方代码：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cua_bench)
- 数据入口：The formal methods page and its outbound links have been checked; no task-data repository or HF card confirmed by the maintainer has been located, and result tables or upstream data are not treated as the complete question bank. [1](https://www.vals.ai/benchmarks/cua_bench)
- 报告标题：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cua_bench)

## Origin and maintenance

- **发起方**：Vals AI [1](https://www.vals.ai/benchmarks/cua_bench)

- **维护方**：Vals AI [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 合作方：The formal materials are not sufficient to confirm an independent research partner; tool providers, model vendors, and upstream repositories are not treated as partner institutions on that basis. [1](https://www.vals.ai/benchmarks/cua_bench)
- 核心作者：The formal methods page can confirm the organization that releases and maintains it, but no byline or methods detail sufficient to confirm author names or question-writer qualifications was found. [1](https://www.vals.ai/benchmarks/cua_bench)
- 资助方：Author, collaboration, and acknowledgment information in the papers and official reports has been checked; no direct funder that can be listed for this project was confirmed, and none is inferred from institutional affiliation or from collaboration agreements. [1](https://www.vals.ai/benchmarks/cua_bench)

## Design goals

- **核心能力**：The agent only observes the screen and uses the keyboard and mouse, maintaining long-term planning, visual judgment, and operation in a real-time commercial game. [1](https://www.vals.ai/benchmarks/cua_bench)

- **相对已有评测的缺口**：Most agent benchmarks provide text state, an API, or the DOM; here only pixels and keyboard and mouse are provided, and the delay of an action itself affects the result. [1](https://www.vals.ai/benchmarks/cua_bench)

## Construction

- **题目来源**：Six commercial games are paired by three types: public Minecraft, SUPERHOT, and eFootball, each paired with one hidden game of the same type. [1](https://www.vals.ai/benchmarks/cua_bench)

- **审核流程**：Persistent evidence is rescored after the fact against a frozen rubric; offline native game state, online sports-video scanning, and human review of difficult cases; recording signatures and hash verification. [1](https://www.vals.ai/benchmarks/cua_bench)

- **质量控制**：Persistent evidence is rescored after the fact against a frozen rubric; offline native game state, online sports-video scanning, and human review of difficult cases; recording signatures and hash verification. [1](https://www.vals.ai/benchmarks/cua_bench)

- **防污染/运行完整性**：Each of the three game types has one public and one hidden game; the names and milestones of the hidden games are not disclosed, and the gap between public and hidden is used to monitor later targeted training. A difference in a single trial cannot by itself prove contamination. [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 出题与审核人员：The formal methods page can confirm the organization that releases and maintains it, but no byline or methods detail sufficient to confirm author names or question-writer qualifications was found. [1](https://www.vals.ai/benchmarks/cua_bench)

## Data format

- **规模**：6 games, 3 hours per game; one trial per model-game pair. [1](https://www.vals.ai/benchmarks/cua_bench)

- **题型**：Screen vision together with keyboard and mouse interaction; milestones are required to be completed in order. [1](https://www.vals.ai/benchmarks/cua_bench)

- **模态**：屏幕图像；视频证据；键盘鼠标 [1](https://www.vals.ai/benchmarks/cua_bench)

- **难度与任务跨度**：Three categories: sandbox, first-person reaction, and sports. 3 hours per game. Minecraft proceeds through 13 levels of milestones, SUPERHOT has 25 levels, and eFootball has five tiers from Beginner to Professional. These are not one unified label of question difficulty. [1](https://www.vals.ai/benchmarks/cua_bench)

- **公开与隐藏划分**：3 public games; the names and milestones of another 3 games are not disclosed (the official website states this explicitly), and scoring uses the same rules. [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 语言覆盖：The formal methods page is written in English, but it does not fully disclose the language coverage of the task instructions and of the program and game content, so the full set of languages cannot be determined from the report language alone. [1](https://www.vals.ai/benchmarks/cua_bench)

## Evaluation

- **指标**：The mean, across 6 games, of milestone scores on a scale of 0–100; action latency and estimated API cost are also reported. [1](https://www.vals.ai/benchmarks/cua_bench)

- **评分规则**：Each game ladder totals 100 points, and later milestones cannot skip prerequisite steps; insufficient evidence is a scoring failure and is not scored directly as zero. [1](https://www.vals.ai/benchmarks/cua_bench)

- **提示与运行配置**：Three hours per game, including reading the screen, learning the controls, retrying after failure, and thinking in the shell; a vendor harness is used, a GPU desktop is driven through MCP, and the memory and the files of the game must not be read. [1](https://www.vals.ai/benchmarks/cua_bench)

- **可比性限制**：The score is a mean of milestones and does not equal the game-completion rate; each cell is a single trial, and the public-private gap cannot automatically be attributed to training contamination. [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 评分/运行脚本：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cua_bench)

## Current status

- **核验日期**：2026-11-07 [1](https://www.vals.ai/benchmarks/cua_bench)

- **现行版本与采用证据**：version：2026-10-13 official leaderboard snapshot；trending：B；heat_evidence：On 2026-10-13 Vals updated commercial-game results for 9 models. Heat B; the catalog and the detail page both belong to Vals and cannot be treated as two independent adopters.；evidence_2026_h2：url：https://www.vals.ai/benchmarks/cua_bench；date：2026-11-07；date_type：observed_on；note：Opened and verified this time; the release or revision date of the source follows the description in the body, and the observation date is not treated as the run date. [1](https://www.vals.ai/benchmarks/cua_bench)

- **饱和度判断**：Editorial judgment: the current first-place mean is 19.17/100 and is not close to full marks; this applies only to the six-game milestone protocol and cannot be extrapolated to general computer-use ability. [1](https://www.vals.ai/benchmarks/cua_bench)

- **已知问题与证据边界**：The score is a mean of milestones and does not equal the game-completion rate; each cell is a single trial, and the public-private gap cannot automatically be attributed to training contamination. [1](https://www.vals.ai/benchmarks/cua_bench)

- **关联与衍生关系**：CUA-bench admits only keyboard-and-mouse evaluation of commercial games; it must not be conflated with OSWorld, with general CUA ability, or with a game subscore. [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 更新与修订：What can currently be verified is an update to the web methods page or leaderboard table; a version history for a standalone paper has not been located, and the web-page update time is not misrepresented as an arXiv revision. [1](https://www.vals.ai/benchmarks/cua_bench)

## Leaderboard snapshot

- **快照采集日**：2026-11-07 [1](https://www.vals.ai/benchmarks/cua_bench)

- **官方榜/正式委托榜**：https://www.vals.ai/benchmarks/cua_bench [1](https://www.vals.ai/benchmarks/cua_bench)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | GPT-6 Astra | 19.17 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 2 | Claude Opus 5.5 | 14.0 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 3 | Claude Fable 5.1 | 13.17 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 4 | Claude Opus 5 | 9.0 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 5 | GPT-5.6 Sol | 8.33 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 6 | Wonder | 7.17 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 7 | Muse Spark 1.3 Max | 5.83 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 8 | Gemini 4 Argon | 4.83 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |
| 9 | Gemini 3.8 Flash | 4.17 | Mean milestone score across six games /100；2026-10-13；[1](https://www.vals.ai/benchmarks/cua_bench) |

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：The score is a mean of milestones, and it is not the same as the rate of clearing the game; there is a single trial per cell, and the gap between public and private cannot automatically be attributed to training contamination. The update time written on the leaderboard table itself is 2026-10-13; the collection date is not the run date. [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 独立第三方入口：No independent third-party results leaderboard under the same version and a comparable protocol was located; citation of the paper, or a self-report on a model card, is not independent reproduction. [1](https://www.vals.ai/benchmarks/cua_bench)

## Contact

- **官方社交**：https://x.com/ValsAI [1](https://www.vals.ai/benchmarks/cua_bench) 注：A public link in the footer of the official site; X accounts are neither read nor operated.

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://www.vals.ai/benchmarks/cua_bench)
- 公开问题追踪：The official methods page and the code entry it points to were checked; no independent implementation or issue tracker that can be confirmed to belong to this benchmark was located. A link to an upstream harness does not replace the benchmark’s own code. [1](https://www.vals.ai/benchmarks/cua_bench)
- 隐私政策：Among the formal papers, READMEs, and official-site links that were checked, this public contact channel could not be located in a form that confirms the corresponding maintainer; email addresses and policy paths are not guessed. [1](https://www.vals.ai/benchmarks/cua_bench)

## Original files

- **其他正式文档**：type：Official web page/paper opened；url：https://www.vals.ai/benchmarks/cua_bench [1](https://www.vals.ai/benchmarks/cua_bench)

- **中的论文副本**：待核实 [1](https://www.vals.ai/benchmarks/cua_bench)

**仍待核实**（不推断为未公开）：

- 原始PDF：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cua_bench)
- SHA-256：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cua_bench)
- PDF字节数：The official method page and its outbound links have been reread; no independent arXiv entry or PDF that could be confirmed against another source was located, so the paper version, the PDF checksum, and the size are left unfilled. The research report on the web page and an independent PDF are recorded as distinct; failure to locate one is not interpreted as officially Not disclosed. [1](https://www.vals.ai/benchmarks/cua_bench)
- 归档目录：Research output and PDF checks were produced only locally, and no upload was carried out; the link to the formal archive folder still needs confirmation. [1](https://www.vals.ai/benchmarks/cua_bench)

## Changelog

- date：2026-11-07；change：首次建立近期热门中文研究条目。CUA-bench admits only keyboard-and-mouse evaluation of commercial games; it must not be conflated with OSWorld, with general CUA ability, or with a game subscore. 热度与榜单口径分离，不确定值标记待核实。；2026-11-07: a source-by-source deep check. Official methods, paper PDFs that had been located, repository README and LICENSE files, and HF cards were reread. Located facts were filled in, versions that conflict with one another were distinguished, and readable leaderboards were collected again. Private material of the original game, and formal artifacts that were not located, remain blank. [1](https://www.vals.ai/benchmarks/cua_bench)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
