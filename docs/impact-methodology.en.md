# Benchmark Constitution Academic Impact Index (BCI)

**Method version: 0.3 (documentary evidence, independent external review, single-track headroom, neutral prior; still an exploratory ranking)**
**Updated: 2026-11-08. All weights are methodological choices published by this site. They are not parameters endorsed by an external institution, and they are not parameters already fitted empirically.**

## 1. What We Measure

BCI (Academic Impact Index) jointly measures a benchmark’s **scholarly dissemination, actual use, original contribution, and evaluation reliability**. It does not rank paper authors, institutions, or models. Popularity does not equal correctness, and obscurity does not equal low quality; a citation may also arise from criticism. This site displays the raw data, the components, the sources, the missing items, the evidence coverage, and the risk labels together, and it forbids displaying only one total score.

The statistical unit is an **identifiable benchmark/version**. If the same evaluation appears more than once across one model’s release page, model card, and performance display page, it counts as one adoption. One paper or GitHub repository may contain several independent benchmarks, and those benchmarks are not merged automatically because they share a paper or a repository. Only an explicit abbreviation, and entries that bear the same name, may be merged. Historical versions are retained. Scores or citations of an older version are not treated as facts about a newer version.

This method draws on the Altmetric, RCR, FWCI, and BetterBench systems, among others, and **does not claim to reproduce** them. In particular, the field × age-bucket percentiles in this catalog are only a “correction within this catalog.” They are not a field-normalized citation over the whole scholarly community, and they are not NIH RCR or Elsevier FWCI.

## 2. Dimensions and Weights

The weights sum to 100%. Dissemination of impact carries a larger share, while quality at 18% and novelty at 12% stand on their own, so that stars or vendor promotion do not dominate “academic standing.”

| key | Dimension | Weight | Definition, source, normalization, and rationale |
|---|---|---:|---|
| citations_total | Accumulated citations | 10% | The primary paper’s raw total citations are retained. Scoring uses the citation count discounted by the square root of the number of attributions to the same paper, so that a subtask does not inherit the influence of an entire collection paper. An OpenAlex record of an exact external identity takes priority, and Semantic Scholar is the fallback. The two databases are not added together. Within the field, `log1p` and the percentile are mixed, and the source and the paper-matching method are recorded. The dimension represents durable dissemination, but its weight is lower than that of age-adjusted velocity, which reduces the advantage of seniority. |
| citation_velocity | Same-age citation velocity | 15% | Attribution-discounted citations C* / (age in months since release a + 3), compared within the same field × the same age bucket. A benchmark can enter a high percentile of its own age bucket even early after release. The 3-month smoother avoids a chance citation explosion one day after release. Linear extrapolation is not written down as real future citations. Citations by year are archived at the same time and reserved for a later analysis of recent acceleration. |
| github | Code ecosystem | 8% | The official repository’s `stargazers_count` (65% internally) and the monthly net increase from two measured snapshots (35%). The source is GitHub REST `/repos/{owner}/{repo}`. Each part is a logarithm plus a percentile. A shared repository is down-weighted by the square root of the number of catalog entries that share it, so that the stars of a public harness are not inherited repeatedly by every subtask. When no snapshot exists, growth is null. Star count or repository age is not used to disguise the recent rate of growth. |
| huggingface | Data use | 5% | Downloads over the most recent 30 days (70%) and cumulative likes (30%) of the official HF dataset, taken from the Hub API dataset page. Each part is a logarithm plus a percentile. When the same HF dataset is shared by more than one entry, it is down-weighted by the square root of the number of sharing entries, so that a collection’s download count is not attributed repeatedly. Downloads are not a count of unique users, and they are not a count of evaluations. Different download-counting mechanisms cannot be compared too strongly, and the weight is therefore low. |
| model_adoption | Frontier-model adoption | 10% | The number of adoptions by the most recent 20 models is read from `frontier/heat.json` and deduplicated by model. Logarithm plus percentile. The raw count/share remains the primary indicator of the industry frequency ranking. When the heat file is missing, the mapping is unclear, or exhaustive coverage has not been declared, an unmatched item is not recorded as 0. |
| evaluator_adoption | Adoption by independent evaluation organizations | 8% | The number of independent organizations, such as AA, Epoch, LMArena, HELM, Scale SEAL, and Vals, that have actually placed the benchmark in ongoing evaluation. Several web pages of one organization still count as one organization. The value must be verified by a person or by a dedicated collector: `assessment.evaluator_adoptions={value:[organization names],sources:[...]}`. A mere mention in a report, a news story, or a negative Epoch review does not count as adoption. Logarithm plus percentile. |
| community | Independent community feedback | 5% | Deduplicated count of public discussions (15%), active issue events over 90 days (7.5%), number of distinct issue threads updated within 90 days (7.5%), number of third-party re-evaluation reports (60%), and a fork-participation proxy (10%). The sources are GitHub Issues and Discussions, together with third-party papers and reproduction repositories. Each part is a logarithm plus a percentile. Negative feedback is recorded as risk and is not treated as endorsement. A fork is only a weak signal of participation. It is not a favorable rating, a count of independent contributors, or a reproduction; its reliability coefficient is 0.5. The count of updated threads is not an event count. Open issues are not treated as 90-day activity. An independent organization, deduplicated by public result rows, counts as one re-evaluation. That count can show only an operational re-evaluation and cannot show reproduction under a strict protocol; the reliability coefficient of this proxy is 0.5. |
| novelty | Research novelty (proxy) | 12% | Comparison with benchmarks **released earlier**: text TF-IDF cosine distance (70%), task-form rarity (15%), and field rarity (15%). The description is encoded, and the name is not. Character 2–4-grams support Chinese and English. Each part maps naturally to 0–100. The present text method is only a proxy, with a credibility coefficient of 0.35. Textual rarity ≠ scientific innovation. Only human confirmation can upgrade it. |
| quality | Methodological and engineering quality | 18% | Human or expert validation 20%, contamination protection 20%, independent reproduction 20%, clarity of the applicable license 10%, maintenance review 10%, and independent external review 20%. Drawing on the BetterBench lifecycle, each item must carry its original evidence. 0 = reviewed and not satisfied, 50 = partially satisfied, 100 = fully satisfied, and a finer score may be stored. A missing value is not recorded as 0. A license file on GitHub does not mean that the data license is clear, so that item is not given full marks automatically. |
| distinctiveness | Non-homogeneity | 4% | Maximum similarity s to neighboring descriptions in the current catalog. The score is `100×[1−max(0,s−0.8)/0.2]`, clipped to 0–100. Homogenization is penalized through a separate small dimension. The dimension is related to novelty, but it is not a second large penalty. s>0.8 is marked homogeneous. The credibility coefficient of the text proxy is 0.35. |
| headroom | Unsaturation and discrimination | 3% | For a high-is-better indicator with comparable bounds: `100×[1−(best score of that source/track snapshot−floor)/(ceiling−floor)]` (70%), plus a discrimination score after audit (30%). Normalized SOTA ≥95% is marked saturated. An unbounded indicator, a low-is-better indicator, an indicator that mixes versions, or an indicator without a unified budget is not computed on our own initiative. Saturation does not erase historical scholarly value, so the dimension is only 3%. |
| maintenance | Timeliness and maintenance | 2% | Let d be the number of days from the last substantive update to the present. The score is `100×2^(−d/365)`. A human-verified substantive update takes priority. GitHub pushed_at and HF lastModified are only a weaker proxy (credibility coefficient 0.5). A stable and correct older evaluation is not heavily devalued merely because it is updated rarely. |

### Shared normalization of quantities

For an observed non-negative quantity x, with comparison group P as the baseline:

```
L(x) = min(1, log(1+x) / Q95(log(1+P)))
F(x) = [count(P<x) + 0.5×count(P=x)] / |P|
N(x) = 100×[0.5×L(x) + 0.5×F(x)]
```

If every member of the comparison group is 0, the result is 0. A negative net increase is clipped to 0 in the “growth score,” while the original negative value is retained in full. Q95 restrains extreme values in the head. Equal values use mid-ranks, so that the order is not arbitrary. Percentile values depend on the composition of the catalog. A change in the sample changes the scores, and the scores are not to be read as absolute units of measurement.

A quantity is normalized first within the same field, among at least 20 entries that have a value. Otherwise it falls back to the full catalog, and the comparison group and the sample size are published in `normalization`. **This is not a complete estimate of a true disciplinary citation baseline.**

### A fairness mechanism for new benchmarks

The age buckets are `[0,3), [3,6), [6,12), [12,24), [24,60), 60+` months. The release date is taken from the registry first. When it is missing, the date of first submission from the official arXiv API is preferred, and the next fallback is the API publicationDate of an exactly matched paper. The substitute basis is published. A later journal publication date must not reset citation age. A human-verified first-release date of the benchmark takes priority over the date of the paper. A date that carries only a year and a month is computed as the 15th day of that month. This is a computational convention, and it does not claim that the exact release date is known. A date that carries only a year is computed as July 1 and marked approximate.

Citation velocity uses the same field × age bucket first. When fewer than 20 entries are available, it falls back to the same age bucket across fields. When fewer than 20 entries are still available, the small-sample percentile is retained, the credibility coefficient is multiplied by `n/20`, and the result is marked `small_age_cohort`. The procedure must not fall back to the all-ages group and let new and old samples compete directly. An age of fewer than 3 months is marked `early_signal`. That mark is not a label of low quality. When a valid date is missing, velocity is null, and the release date is not guessed. Truncated citations from the most recent year are not currently used to compute an “exact recent-month velocity” automatically, because a calendar-year count is not a rolling 365 days, and some APIs return only part of the history.

A new benchmark can reach a high position through same-age dissemination, an original task, and quality evidence, without waiting through years of accumulation. At the same time, “a short time since release” is not itself a bonus. Unstable extrapolation must not be used to manufacture high impact.

## 3. Missing Values, Credibility, and the Composite Score

### Do not write “not obtained” as zero

Every component s_k is 0–100 or null. An API failure, an unmatched paper identity, a quality item that has not been checked, or a case that has only a shared project and no attributable indicator is explicit missingness. Only a numeric 0 returned successfully, or a “none” confirmed by a complete check, may be recorded as 0.

Each dimension has an evidence credibility coefficient r_k. A direct count is generally 1. When the sub-items are incomplete, r_k equals the sum of the weights of the available sub-items. The text proxy for novelty and for homogeneity is 0.35; when the task or field sub-items of novelty are missing, that coefficient is multiplied further by the available sub-item weights. Maintenance represented only by a push proxy is 0.5. A small age bucket reduces the coefficient further. Within a dimension, reweighting likewise uses only the available sub-items.

```
effective weight w'_k = w_k × r_k (0 when missing)
observed_score = Σ(w'_k × s_k) / Σw'_k
coverage = Σw'_k
BCI = coverage × observed_score + (1−coverage) × 50
    = 50 + Σ w'_k × (s_k − 50)
```

Missingness is therefore not treated as a punitive zero. It does reduce the amount of usable evidence, and it draws thin evidence back toward the published neutral prior of 50. The value 50 is not an observed value, and it is not an estimate of the quality of a given entry. Same-age peers are used only for diagnosis. The diagnostic median is taken from reference entries with coverage ≥ 0.4 and with no unresolved identity conflict, excluding the entry itself. The preferred group is the same field × the same age group (at least 5 entries), then the same age group (at least 10 entries), then entries in the full catalog that have sufficient evidence. Whatever the level of the reference sample, the scoring prior is fixed at 50. The score produced by the old same-age-median formula is retained for diagnosis as legacy_peer_shrunk_score and is not used for ranking. The outputs are alpha, prior, peer_median_diagnostic, peer_group_diagnostic, peer_n, and the raw observed_score. Coverage is only **evidence coverage. It is not a statistical confidence interval, and it is not a “probability that the score is correct.”** A value ≥ 0.8 is high, 0.6–0.8 is medium, and the remainder is low. Each item also outputs `dimension_reliability` and the coverage of the quality sub-items.

**Two-tier publication thresholds.** Exploratory ranking requires coverage ≥ 0.4 and no unresolved identity conflict. An entry below the threshold is listed as unscored and marked insufficient_evidence. Its components, observed_score, and shrunk_score are retained for diagnosis, but it receives no rank. Exploratory ranking is still labeled provisional. The stricter formal eligibility for a quality audit still requires coverage ≥ 0.6, internal quality coverage ≥ 0.5, evidenced citations or organizational adoption, and no verified Flawed conclusion. That eligibility is distinguished by official_rank_eligible. An exploratory Top30 must not be presented as a verified and authoritative conclusion about academic standing.

### Quality floor

When a sourced Epoch `Flawed` conclusion is present, the entry is marked flawed and the cap on the composite score is set at 40. This cap is a **normative rule of this site**. It is not a number supplied by Epoch. Flawed must correspond exactly to the version and to the review date. Neither an unreviewed status nor Not enough info may be written as Verified or Flawed on our own initiative. Severe contamination, versions that cannot be compared, retraction, and duplicate reskins should enter the queue for human review. A confirmed defect of reliability must not be offset by a high star count or by promotion.

Raw citations and impact through use are retained. A quality label does not rewrite a historical fact. After a future repair, the earlier review and the record of the change should be kept.

## 4. Audit Boundary of Novelty and Homogeneity

The current implementation is a **recomputable lexical proxy, not a general sentence-vector embedding**. It prefers the paper abstract actually returned by the API, of length ≥ 100 characters. Otherwise it uses the description, the subfield, and the task form from the registry. It does not use the full text of a paper that has not been obtained. Abstracts and counts are bound to the exact external identity, and the source is retained. Novelty is compared only with entries that have a known and earlier date. If there is no earlier reference, or if the description is too short, the value is null. Task rarity is 1 minus the proportion of the same task in the earlier catalog. Field rarity is defined in the same way.

Limits: a short Chinese paraphrase may cause a misjudgment; translation and a change of wording can produce a spurious distance; inheritance of a problem within the same research is not necessarily homogeneity; and a rare field is not necessarily innovation. No cross-lingual semantic model, and no human genealogy of the research, has been built. The front end must display `lexical_novelty_proxy` and the size of the reference sample, and it must not claim that “originality” has been verified. A multi-sentence vector version may later be frozen and cross-checked with clustering, with double-blind review by two domain experts, and with a matrix of coverage of new capabilities. When the encoder or the corpus changes, the method version is raised and the scores are recomputed. Old scores are not mixed in silently.

## 5. Industry Heat Index, Published Separately from BCI

**The primary ranking remains strictly the deduplicated count of appearances among the most recent 20 frontier models, ordered from high to low.** The same model counts once, however many web pages it has. An auxiliary “time × vendor-diversity heat” is supplied for the observation of trends:

```
w_m = 2^(−days since model release/90)
A_b = Σ_m 1[b adopted by m] × w_m
p_v = (contribution of vendor v to A_b) / A_b
V_eff = exp(−Σ_v p_v log p_v)
D_b = 0.5 + 0.5×min(1, V_eff / number of known vendors in the current window)
IndustryHeat_b = 100 × (A_b / actual number of models at present) × D_b
```

When the window is full at 20, the denominator is 20. When fewer than 20 models are present, the actual sample size must be displayed and must not be filled in. The index is ≤ 100. The 90-day half-life balances new releases and stable adoption. The entropy effective number of vendors limits heat produced by a large number of models from a single vendor. If the date or the vendor is missing, the auxiliary score is not computed, and count is retained. When every adopter of a benchmark comes from one vendor, the auxiliary score is lower. That lower score does not deny the benchmark’s use. It reduces the concentration of promotion from one side. The file `industry-heat.json` is output separately and does not alter the original frequency order of Frontier Heat.

The rules for admitting a model to the window, for merging model families, and for assigning a vendor are decided in public by the Frontier Heat collector. Whether mere inclusion in a comparison table on a page counts as adoption must be kept consistent. The model_adoption term of BCI uses count. It does not quietly replace the raw adoption count with this auxiliary score.

## 7. Prevention of Leaderboard Gaming, and Governance

- **Identity deduplication.** A preprint and the formal version of a paper are not added together. Citations of the same model on several pages are not repeated. Relations of subset, replica, translation, and version are published.
- **Attribution of shared resources.** Stars of a public harness, of a collection repository, or of an author homepage are not attributed directly to one evaluation. A shared repository is labeled explicitly and down-weighted, and resources that cannot be attributed should later be removed by hand. HF mirrors and shards are not added blindly.
- **Anomaly monitoring.** Daily snapshots retain the net increase in stars, the change in downloads, and the source. A surge is not, by itself, a finding of cheating, and it is not treated as reliable dissemination before it has been checked. Anomaly labels and review records are published. The data are not altered out of sight. The present scripts do not identify bot accounts, do not identify paid likes, and do not analyze a complete citation circle, so they cannot be said to prevent gaming automatically.
- **Citation manipulation.** When a complete author and citation graph can be obtained, self-citation and the count with self-citation removed, together with the concentration of the citation network, will be reported side by side. The present total of citations does not pass itself off as a total from which self-citation has already been removed. A critical citation, and a citation of a dataset name, do not necessarily represent actual adoption.
- **Dual review of quality.** Each human item is scored independently by at least two people, and conflicts are arbitrated. Authors’ conflicts of interest are disclosed. This review is not yet complete, and scores are not filled in automatically.
- **Transparent change.** Weights, sample pools, encoders, normalization baselines, and code versions are archived. Each daily snapshot is compared with the previous version, and reordering caused by newly added samples is shown. Filters by field and by age are provided, so that an overall ranking does not conceal a small field of the natural sciences.
- **Robustness checks before launch.** It is recommended that each weight be perturbed by ±20%, that the ranking be recomputed after removing a single dimension, and that within-field ranks and Kendall correlation be compared. The range of ranks is published. The current version does not package a range of that kind as a statistical confidence interval that has already been computed.

## 8. Limitations and Proper Use

BCI is an open methodological proposal. It has not been calibrated for external validity. At the present stage, the acquisition rate, mistaken inclusion of training sets in the catalog, ambiguity of titles, API coverage, and cross-field bias may each be larger than a difference in rank. Citation databases lag, repeat records, or omit records. The release date of a paper need not equal the first release of the benchmark. A difference in an API count from one day to the next is not necessarily an anomaly. Novelty and homogeneity are both lexical proxies. Like the quality review, they cannot let promotional language stand in for facts. **An overall ranking that lacks coverage of human quality review and of independent reproduction is not sufficient to measure “how high or low the academic standing is.”**

The number of catalog entries is not the number of completed audits. The API hit rate is not the accuracy of inclusion. A trial Top20 is not a formal recommendation. It is recommended that the following be presented together: an adoption-frequency ranking, an age-group rising ranking, a quality-audit ranking, a ranking for each field, and a historical-impact ranking. One overall ranking does not replace every judgment.

## 9. References (retrieval date of the original method: 2026-11-07; retrieval date of the added independent reviews: 2026-11-08)

1. Altmetric, *How is the Altmetric Attention Score calculated?*: multi-source weighting, deduplication, and the point that attention does not equal academic quality. https://help.altmetric.com/en/articles/9800513
2. Hirsch (2005), *An index to quantify an individual’s scientific research output*: the h-index is an indicator of a researcher or of a body of output, and it is not suitable for direct application to a single benchmark. It is used only as a reference for “accumulation bias,” and it is not entered into the formula. https://doi.org/10.1073/pnas.0507655102 (retrieval of the original timed out; the definition was checked separately against https://guides.lib.usf.edu/promotiontenure/metricsglossary)
3. Hutchins et al. (2016), *Relative Citation Ratio*: article influence adjusted by co-citation field and by year. https://doi.org/10.1371/journal.pbio.1002541
4. NIH iCite, an account of the RCR method and of the provisional status of new papers. https://support.icite.nih.gov/hc/en-us/articles/9105587565851-Relative-Citation-Ratio-RCR
5. Elsevier, *What is Field-Weighted Citation Impact (FWCI)?*: adjustment by the expected citations of papers in the same field, the same year, and the same document type. This site does not claim to hold a complete Scopus baseline. https://service.elsevier.com/app/answers/detail/a_id/14894/supporthub/scopus/ (the official page returned 401; the definition was checked separately against the University of Florida library, https://guides.uflib.ufl.edu/metrics/article)
6. BetterBench methodology: 46 lifecycle best practices, scoring by two experts, and the dimensions of design, implementation, documentation, and maintenance. https://betterbench.stanford.edu/methodology.html; https://arxiv.org/abs/2411.12990
7. Epoch Benchmark Reviews rubric v1: review of Verified/Flawed/Not enough info, of scoring defects, of incomparable versions, and of related matters. https://epoch.ai/data/benchmark-reviews-documentation/methodology
10. GitHub REST semantics of a repository and of a star. https://docs.github.com/en/rest/repos/repos#get-a-repository; https://docs.github.com/en/rest/activity/starring
11. Hugging Face Hub dataset API. https://huggingface.co/docs/hub/api; https://huggingface.co/docs/huggingface_hub/guides/search

> The references are grounds for the method. They do not mean that the institutions named above endorse this site’s weights, thresholds, or conclusions.

### Additional safeguards of the current implementation

- When no indicator of dissemination or of use has been observed, no composite score is emitted, even if the text proxy shows distinctiveness (score=null). An entry that “has only a description, and no evidence of impact” must not receive a score of 100 from one proxy dimension.
- When the same ID presents a substantive conflict between different arXiv or DOI identifiers, it enters identity_conflict and is not scored for the time being. The original conflict remains in the report. Different IDs that share a name, but are not corroborated by a paper identifier, are not merged rashly. A placeholder title in the catalog is not used to merge across IDs.
- A record that could not be scored is listed on its own as `unscored` (rank and score are null). It does not enter `ranking`. Rank on the primary ranking is therefore an integer, and score lies in 0–100. An unscored entry is not forced into an academic rank that would carry a meaning.
- A human quality item and a community item must carry a real HTTP(S) source and a valid accessed date. A number with no source must not be entered by itself.

## v0.2 Record of Fixes and Explainability

This version repairs the severe ranking bias in v0.1, which came from truncating the online sample, in alphabetical order, to 180 entries. The old Top20 is retired. Every row of the current catalog enters collection and cache continuation runs. When the budget is insufficient, a deterministic hash order is used instead of alphabetical order, and the items left uncovered are published. A model card is matched first to a canonical ID and then to an unambiguous alias. The versions of MMLU/MMMLU, and the versions of SWE, must not have their adoption counts hijacked by a parent’s aliases.

Shared attribution of papers, repositories, and HF collections retains the true raw counts. The discount used in scoring is only a derived quantity, and it is labeled as such. The citations of an entire survey paper, attached to one MTEB subtask, and the stars of a public harness, are not treated as the independent influence of that subtask. After a family has been merged, the indicators of its subtasks are not added over again. Length of an abstract, completeness of metadata, and innovativeness are not the same concept. Novelty remains only a proxy, with a credibility coefficient of 0.35.

The common-sense check is used only as a diagnosis of error. It checks source identity, missing values, version mapping, and the threshold for entering the ranking for SWE-bench, GPQA, HLE, MMLU, MATH, HumanEval, ARC-AGI, and LiveCodeBench. An entry is not placed by hand according to an expected rank, and points are not added by name. When the evidence is genuinely insufficient, or when a newer version lacks citations, the entry remains in insufficient_evidence, as the record stands.

### Explanation of the science2 fields

The organization supplied by science2 is principally the affiliation of the paper’s first author. Without verification, it is not to be read as the benchmark’s sole publisher. In scientific evaluation, non-LLM subfields are retained explicitly. An overall ranking across tasks or fields must provide filters. Evaluations attached to some models, self-descriptions held in the archive, and version families still await a human review of scope. Retention in the catalog is not an endorsement of quality.

## v0.3 Completion of Evidence and Correction of Bias (2026-11-08)

### A. Completing the evidence, not an automatic declaration of formal status

The scope is fixed at the existing 1668 entries. No historical entry is added. All 178 published complete dossiers were read again from the public JSON snapshots. Of these, 173 matched an existing ID exactly (RealWorldQA uses only an explicit spelling mapping). The other 5 are not mapped by force. A family or a sub-version, a different name, or an unclear scope stays blank. The components of PRBench Legal/Finance must not quietly be treated as the parent item’s total score.

The original quality weight of 18% is unchanged. Machine-assisted extraction is not expert scoring.

- An explicit and affirmative process of human or expert review → `human_validation=50`.
- An explicitly implemented canary, hidden test, deduplication, training exclusion, or similar control → `contamination_protection=50`. A negation, a warning of contamination risk, or the statement that “absence of contamination has not been proved” does not itself count as a control. The value 50 does not equal 50% free of contamination.
- An official script entry point, together with a scoring specification that has content → `reproducibility=50`. This does not claim that the code has been run, that tests have been passed, or that independent reproduction has been achieved.
- A concrete license in the dossier with no unresolved license conflict, or a registry-only entry that corresponds exactly to one explicit license statement on an HF dataset card → `license_clarity=50`. Upstream compatibility is not inferred, and a code license is not inferred. When the dossier has already recorded a conflict, an HF label cannot override it.
- A version number, a release date, a GitHub push, and the existence of a paper do not, by themselves, become maintenance quality, human review, or proof of novelty. `maintenance_review` still has no evidence, and it cannot be used to pad coverage.

Each 50 above is a published normative rubric value for “partial documentary conditions satisfied.” It is not a quality score given by a paper, and it is not an accuracy rate of the evaluation estimated from nothing. The reliability coefficient of each machine-extracted item is **0.5**. Effective coverage inside quality is Σ(sub-item weight×reliability coefficient). The presence of one item is not 100% evidence of quality. The source is stored together with the field path, the original text, and the upstream source, so that each item can be checked again. Where there is no affirmative evidence that meets the rule, the value remains null. A 0 is not inferred from “not found.”

### B. Independent quality review takes priority, and versions do not inherit from one another

The official Epoch review table and the specific review pages are read directly. Under this site’s external-review rubric, passage of the minimum scoring-validity check on independent review (Verified) is recorded as 100. Explicitly exceeding the defect threshold (Flawed) is recorded as 0, with reliability coefficient 1. This is a normative mapping, made by this site, of a public classification. It is not a number supplied by Epoch. Not enough info is not treated as 0 or as Verified. Flawed continues to invoke this site’s existing rule that the total score is ≤ 40, and it bars formal eligibility. A critical review does not count as adoption of the benchmark by that organization.

The mapping is applied exactly to original HLE, SWE-bench Verified, original SWE-Bench Pro, HealthBench Professional, DeepSWE v1.1, Agents’ Last Exam v1.1, BFCL v4, and GraphWalks and SimpleQA Verified. It is **not** passed on to HLE-Diamond/HLE-Rolling, to HealthBench in general, to SWE-Bench Pro V2, to original SimpleQA, or to historical BFCL V1–V3.

The PostTrainBench review concerns v1.1, while the existing dossier is v1.2. The Terminal-Bench review concerns 4.0.0, while the latest tag in the dossier is 4.1.0 and the displayed leaderboard is still 4.0. These two items store only the historical review. They do not add points to the current entry, and they do not place a cap on the whole item. This is conservative isolation of versions. It does not mean that the newer version has been repaired, or that it has passed external review.

Direct sources (actual date of access: 2026-11-08):
- https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks
- https://epoch.ai/data/benchmark-reviews-documentation/methodology
- https://epoch.ai/benchmarks/hle/review
- https://epoch.ai/benchmarks/swe-bench-verified/review
- https://epoch.ai/benchmarks/swe-bench-pro/review
- https://epoch.ai/benchmarks/healthbench-professional/review
- https://epoch.ai/benchmarks/deepswe/review
- https://epoch.ai/benchmarks/agents-last-exam/review
- https://epoch.ai/benchmarks/graphwalks/review

### C. The boundary of community feedback

The weight remains 5%. The internal composition is now public discussion 15%, events over 90 days 7.5%, threads updated over 90 days 7.5%, independent re-evaluation 60%, and fork participation 10%. The proxy reliability coefficient of forks, of updated threads, and of operational re-evaluation is 0.5. The community score of a shared repository is discounted by the square root of the number of sharing entries. Social platforms were not scraped. HF likes are not counted a second time inside the community item. The total number of open issues is not presented as the count of events over 90 days. A fork, and negative feedback, are not treated as endorsement. Issue threads are a search count over the calendar window from 2026-08-10 through 2026-11-08, including both endpoint dates, with a precision of one day. The filter `is:issue` excludes pull requests, and only a total with `incomplete_results=false` is accepted.

A third-party re-evaluation is supported only by a readable row of model scores and by an explicit independent-evaluation track or third-party track, and it is deduplicated by organization. Evaluation conducted by the creator of the benchmark does not count as independent reproduction. HF downloads and likes remain only in the original dimension of data use. There are not at present two comparable observations of a download trend, and a rate of growth is not fabricated.

### D. Saturation: only a bounded track of the same version and the same protocol is recognized

Each group is separated by source URL, track, metric, and the fields for version, subset, protocol, and budget. Only accuracy on an explicit percentage scale, pass@k/pass^k, and a success rate or a solve rate are admitted, and the values lie in 0–100. A baseline from a historical paper, a human baseline, a win rate, Elo, an unbounded error, a bare Score/Accuracy whose unit is unclear, and a mixture of versions or of budgets are not converted automatically. The values 0 and 100 are the mathematical lower and upper bounds in the definition of this class of bounded rates of correctness or success. They are not an estimate of human performance.

The best **reported snapshot** of every eligible track is retained, and the best model, the number of sample result rows, and the original date of collection are published. “Best” is limited to that source and that track. It is not a worldwide SOTA. The track used for the score is chosen by a rule published in advance: an identified independent evaluation organization comes first, then the track with the largest number of readable rows, then a deterministic break of ties on the source, track, and metric strings. The choice is not made in the hope that a given benchmark will rank high or low. This choice has bias of its own, and the full array of tracks must be displayed together with it. The reliability coefficient of this item is 0.5. Unknown bounds are not counted. Discrimination in the head, when it has not been measured, remains null. A figure of ≥95% refers only to the selected track. It is not extended to saturation of the whole family.

### E. Repair of the real bias by which “supplying evidence lowers the score, while missing evidence is favored”

A trial computation found that the old formula, applied to reference samples with high citations and low quality coverage, produced an empirical prior of about 80. An unreviewed item therefore received an excessively high shrinkage of its missing portion. The newly supplied rubric for partial documentation is 50, so entries for which more evidence had been supplied were harmed instead. The problem is an **artifact of the missingness mechanism**. It cannot be solved by adjusting the Top30 by hand, name by name.

v0.3 retains the same-age median for diagnosis, but ranking uses one explicit neutral prior of 50 throughout:

`BCI = 50 + Σ_k weight_k × reliability_k × (component_k − 50)`.

This does not fill in a missing fact. The original components remain null, and coverage still shows, truthfully, how much is missing. The value 50 is only the neutral anchor of the published scoring policy. The contribution of one newly added documentary item scored 50 is strictly 0. It neither lowers nor raises that entry’s score, and a newly added regression test guarantees this. A definite negative external review can lower the score. Definite positive evidence can raise it. What is unknown cannot receive a hidden reward equivalent to quality scored 80. The minimum coverage threshold of 40% for an under-evidenced item to enter the ranking, the formal total coverage of 60%, and the internal quality-coverage threshold of 50% are not lowered.

This is a general correction of the formula. It does not fix a rank for any name. The score under the old empirical prior is listed separately as `legacy_peer_shrunk_score`, so that sensitivity can be inspected. There is still no certification of validity across fields. Residual bias, including missingness that is not random and a collection effort tilted toward common projects with high star counts, should be disclosed. It cannot be claimed that every coverage bias has been removed in full.
