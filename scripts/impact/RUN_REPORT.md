# Benchmark Constitution：现有学术影响力指数补证报告

生成：2026-11-08（ UTC+8）

## 结论：补证已落盘，但不能把称为“正式榜单”

固定1668条，原探索榜60条 → 当前探索榜97条；**正式资格0条**；证据不足1571条。未降低40%探索覆盖、60%正式覆盖、50%质量内部覆盖门槛。机器文档代理不冒充专家质量审查。主仓库只读、没有发布；未读取凭据文件。

## 各维度：有非null分项的条目数 / 全部1668条

注意：这里的“有值覆盖率”不是质量审查完成率，也不是整个维度权重全部有证据。特别是许可标签仅是质量的一小项，机器项可靠系数0.5；平均内部可靠度另列，避免把少量许可元数据宣传成质量补齐。

|维度|之前|之后|之后平均内部可靠度|
|---|---:|---:|---:|
|引用积累|1231 (73.80%)|1231 (73.80%)|73.80%|
|同龄引用速度|1231 (73.80%)|1231 (73.80%)|73.80%|
|代码生态|101 (6.06%)|154 (9.23%)|6.00%|
|数据使用|313 (18.76%)|313 (18.76%)|18.76%|
|前沿模型采用|240 (14.39%)|240 (14.39%)|14.39%|
|评测机构采用|14 (0.84%)|14 (0.84%)|0.84%|
|独立社区反馈|0 (0.00%)|166 (9.95%)|0.82%|
|研究新颖度（代理）|1197 (71.76%)|1197 (71.76%)|21.38%|
|方法与工程质量|0 (0.00%)|303 (18.17%)|1.89%|
|非同质性|1617 (96.94%)|1617 (96.94%)|33.93%|
|未饱和与区分度|0 (0.00%)|34 (2.04%)|0.71%|
|时效与维护|371 (22.24%)|404 (24.22%)|12.11%|

## 实际证据与局限

- 178份公开完整档案快照全部取到；173份精确映射，5份未强行合并：arc-challenge, furniture-assembly, hss, prbench-finance, prbench-legal。
- 301个现有条目的HF card成功精确对应；只对registry-only且没有完整档案冲突审查的条目提取明确单一数据许可。
- 质量子项有证据数：{"human_validation": 57, "contamination_protection": 42, "reproducibility": 93, "license_clarity": 212, "external_review": 9}。维护质量和完整双人独立评分没有补造。
- 明确独立评测结果支持19条操作性复测；4个仓库的issue查询映射7条现有版本条目；其余社区有值主要为弱fork参与代理，不能称为好评或已复现。
- 84条精确命中connector元数据，其中53条此前无star观测。star增速仍全部null；今日仅建基线，不能估算。
- 34条有可安全处理的百分正确/成功率赛道；保留所有分轨、仅选单轨快照最佳分。裸Accuracy/Score、Elo、RMSE、历史论文、人类结果、混预算和不同版本均不自动混算。尚非全局SOTA或完整饱和度审计。
- 178份档案及308个唯一现有HF dataset ID均做了顺序读取；原始响应含失败状态也缓存。原始论文/榜单的上游采集日期保留；8日访问的是公开档案快照时不会伪称8日重新访问原始榜单。

## 独立质量审查的实质发现

直接核实Epoch审查表及具体审查页。以下7项审查结论为Flawed，精确匹配到对应版本并触发总分≤40；不能因高引用/高star抵消可靠性缺陷：

|条目|结论|范围|
|---|---|---|
|hle|Flawed|original HLE; excludes HLE-Rolling, HLE-Verified and HLE-Diamond|
|swe-bench-verified|Flawed|500-problem Verified subset|
|healthbench-professional|Flawed|Professional 525-task release; NOT HealthBench general|
|deepswe|Flawed|v1.1|
|agents-last-exam|Flawed|v1.1; 122 public tasks|
|graphwalks|Verified|reviewed public 1150-task release; version not separately specified|
|swe-bench-pro|Flawed|original 731 public / 276 private / 858 held-out; NOT Pro V2|
|bfcl|Flawed|BFCL v4|
|simpleqa-verified|Verified|SimpleQA Verified; not original SimpleQA|

- HLE审查原集48题，22题被确认存在影响准确性的错误（46%）；不扩展到HLE-Diamond/Rolling/Verified。来源：https://epoch.ai/benchmarks/hle/review （访问2026-11-08）。
- SWE-bench Verified的结论不传给原始SWE-bench或Pro V2；HealthBench Professional不传给一般HealthBench。
- PostTrainBench审查v1.1但档案已是v1.2；Terminal-Bench审查4.0.0、最新tag为4.1.0但展示榜仍4.0。二者仅记录历史审查并显示版本不匹配警告，不当作当前通过，也不自动给整个家族封顶。Terminal-Bench在当前Top30，不意味着4.1.0已修复或已通过审查。

## 方法变化及覆盖偏差诊断

- 12个全局权重不变；社区内部拆开90日事件与更新线程，加入低可靠度fork参与，独立复测与严格复现分开。
- 机器文档项按部分满足的规范性rubric记50，可靠系数0.5；不把“有论文/有仓库”本身当成高质量。渲染器不等于评测代码，代码许可不等于数据许可，已加入负例测试。
- 第一版试算暴露旧高分参照先验的缺失优势：较少质量证据的MME浮到第一，补到中性50文档的GPQA反而受损。这是公式伪影，不按名称手调。现在统一公开中性50先验：`score=50+Σ(weight×reliability×(component−50))`。新增50文档项分数贡献恰为0，回归测试保证补文档不反向扣分。旧同龄中位数及旧分保留诊断。
- 当前97条探索排序与ID字母序的Spearman rho=-0.135；与覆盖率的rho=-0.365，只做描述性诊断，不能据此声称所有缺失偏差已消除。资源获取仍偏向已知/高star项目，总榜仍有领域和数据可得性限制。
- 24个逐维权重±20%敏感性情景（固定入榜集合）：Kendall tau最小0.957、中位0.995。下列名次范围是政策敏感性，不是统计置信区间。

## Top30：全部为探索性，不是正式排名

|名次|Benchmark|分数|证据覆盖|权重敏感性名次范围|
|---:|---|---:|---:|---:|
|1|HealthBench|70.624|47.77%|1–1|
|2|MMLU-Pro|70.106|56.11%|2–4|
|3|GPQA|70.025|60.46%|2–4|
|4|Terminal-Bench|69.880|52.87%|2–4|
|5|SWE-bench|68.919|51.61%|5–7|
|6|MME|68.664|41.42%|5–7|
|7|HumanEval|68.576|52.32%|5–7|
|8|LAB-Bench|67.607|55.92%|8–9|
|9|GDPval|67.180|49.27%|8–10|
|10|ProgramBench|66.890|49.87%|9–10|
|11|MMMLU|66.022|54.12%|11–13|
|12|MBPP|65.814|40.47%|11–15|
|13|MASK|65.785|45.97%|11–17|
|14|MMMU-Pro (A More Robust Multi-discipline Multimodal Understanding Benchmark)|65.542|57.42%|13–17|
|15|BIG-bench|65.514|42.32%|13–17|
|16|ExploitGym|65.292|42.67%|12–19|
|17|BrowseComp|65.238|50.02%|15–17|
|18|LiveCodeBench|64.845|49.72%|15–19|
|19|MMStar|64.685|41.42%|18–20|
|20|PostTrainBench|64.275|47.32%|18–22|
|21|MMMU Benchmark|64.145|40.02%|20–22|
|22|PubMedQA|64.057|44.27%|21–24|
|23|ExploitBench v0.1|63.646|45.37%|21–31|
|24|PaperBench|63.507|43.22%|23–27|
|25|GSM8K|63.313|47.77%|24–28|
|26|MMLU|63.304|43.30%|23–29|
|27|AGENTHARM|63.240|51.42%|24–30|
|28|EvalPlus|63.069|40.17%|26–32|
|29|SciCode|62.846|52.32%|23–39|
|30|BigCodeBench|62.820|52.32%|24–35|

## 验证与下一步

- 31个单元/回归测试通过；本报告的12项完整性检查全部通过。既有引用计数没有丢失；ID集合完全未变；所有新assessment附公开HTTP(S)来源及真实accessed；Flawed不允许正式资格。
- 若要正式发布，下一步应对已有高覆盖条目做小批逐项独立复核（而非再扩大库）：先确认构造/QA、许可范围、污染防护和评测脚本可运行性；补足质量内部覆盖后再检验60%总覆盖。不能为了得到正式榜而调低门槛、把脚本入口当成执行成功、把fork或下载当口碑。

## 交付文件

- 新指数：`
- 新登记库（1668条不变，含assessment与来源）：`
- 方法：`
- 本报告：`
- 原始证据、覆盖和核验：`evidence-report.json`、`evidence-coverage.json`、`evidence-validation.json`、`independent-quality.json`、`cache/{dossiers,hf-cards,epoch-reviews,github-connector,snapshots}/`。
- 流水线：`evidence_overlay.py`由`compute.py`自动应用；重跑计算不访问网络。采集器为`fetch_dossier_snapshots.py`、`fetch_hf_cards.py`、`fetch_epoch_reviews.py`；只读公共源、缓存续跑。
- 发布前可复跑：`.venv/bin/python -m unittest -v test_impact test_evidence && .venv/bin/python compute.py && .venv/bin/python write_evidence_report.py`。
- 改动均未发布到主仓库；基线备份：`archive/2026-11-08-before-evidence/`。
