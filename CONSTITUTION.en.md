# Benchmark Constitution, v0.1

## Chapter 1. Purpose and scope
1. This collection follows AI evaluation benchmarks over time. The core sections are the natural sciences (physics, chemistry, biology and medicine, Earth and astronomy, and materials). Language, reasoning, mathematics, code, multimodal tasks, Agent, and safety are secondary sections.
2. A benchmark is included when it has a public dataset or evaluation protocol, and a paper, technical report, or official page that can be checked.

## Chapter 2. Accuracy, the highest rule
3. Every fact and every number must carry a source link and the date it was collected.
4. Information that cannot be found is written “Not disclosed” or “Unverified.” It is never estimated, inferred, or filled in.
5. A dossier is rewritten from official material. It does not copy the source. A direct quotation is marked with quotation marks and a citation.
6. When sources conflict, each account is listed, with a note of which one is followed and why.

## Chapter 3. Source grades
7. Grade 1: the original paper, the official website, the official code repository, and the official leaderboard.
8. Grade 2: established third-party evaluation organizations, such as Artificial Analysis, LMArena, Epoch AI, Papers with Code, Scale SEAL, and HELM.
9. Grade 3: model-provider model cards and technical reports. These must be marked as self-reported scores.
10. Grade 4: news, blogs, and social media. These are leads only. They enter the record only after they have been checked against grades 1 to 3.

## Chapter 4. Standard structure of a benchmark dossier
1. **Basic information**: full name and short name, version, release date, section and subfields, license, paper link, code repository, dataset address, and official homepage.
2. **Origin and maintenance**: initiating organizations, partners, principal authors, current maintainer, and funders when they have been published.
3. **Design goals**: which abilities are measured, and why existing benchmarks were not enough.
4. **Construction**: question sources (expert original work, textbooks, examinations, adaptation from papers, or synthetic generation), author background, review process, quality control, and decontamination.
5. **Data format**: size, question types (choice, completion, open answer, code, multi-step interaction), modalities, languages, difficulty, and the division between public and hidden splits.
6. **Evaluation**: metrics, scoring (exact match, human grading, or model grading), prompt settings, and official evaluation scripts.
7. **Current status**: the latest version and changelog, whether the benchmark is near saturation, known contamination or disputes, and later derivative benchmarks.
8. **Leaderboard snapshot**: leading results from the official leaderboard and from grade-2 organizations such as Artificial Analysis. Each score records its source, model version, and collection date.
9. **Contact**: official public email, GitHub Issues, discussion forum, or social account. Only official public channels are included. Private contact details are not collected.
10. **Original files**: the paper PDF and other official documents are linked from public sources.
11. **Changelog**: the date and substance of each change to the page.

## Chapter 5. Updates and maintenance
11. Daily scan: new arXiv papers, official leaderboards, organizations such as Artificial Analysis, Hugging Face, and releases from major laboratories. A new benchmark or a changed score is updated when it is found.
12. Once a month, every entry is checked again for links and current status.
13. Old versions are not deleted. They are marked “superseded,” and the historical data is kept.

## Chapter 6. Storage and names
14. Records are filed by section and entry. The dossier and the public source of the paper PDF are kept.
15. Names use `section_short-name_version`, for example `Chemistry_ChemBench_v1`.

## Chapter 7. Presentation
16. The home page reads like a news site: the latest news is at the top, then navigation by section. Each card opens the full dossier for that benchmark.

## Chapter 8. Revision
17. Amendments to this constitution record a version number and a date.
