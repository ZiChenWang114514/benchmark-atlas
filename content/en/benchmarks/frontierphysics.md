# FrontierPhysics

An end-to-end research benchmark whose tasks come from physicists' own projects: 56 tasks require agents to review literature, run computations or experiments and write a paper, and no configuration passes more than 30 percent.

## Basic information

**name**: FrontierPhysics

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**full_name**: FrontierPhysics: Evaluating Agents for End-to-End Physics Research

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**version**: v0.1

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**paper_version**: arXiv v1

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**release_date**: arXiv v1 was submitted on 2026-11-04.

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**section**: Physics

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**subfields**: Condensed matter physics, Atomic, molecular and optical physics, Quantum information, Astrophysics, Fluid dynamics, Statistical physics, Photonics and imaging, High energy physics, Chemical physics

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**license**: The paper is released under CC BY 4.0; the license for the task data and evaluation code is unverified.

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**paper_url**: https://arxiv.org/abs/2611.06910

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**code_url**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**dataset_url**: https://huggingface.co/collections/benchflow/frontierphysics-task-datasets

Sources: [1](https://huggingface.co/collections/benchflow/frontierphysics-task-datasets) (accessed 2026-11-09)

**official_homepage**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**paper_title**: FrontierPhysics: Evaluating Agents for End-to-End Physics Research

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

## Origin and maintenance

**initiators**: Physics researchers from BenchFlow, the University of California, Berkeley and other institutions

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**partners**: The authors come from 37 institutions, including Caltech, Harvard, Stanford, Lawrence Berkeley National Laboratory and Oak Ridge National Laboratory.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**authors**: Bingran You, Wenjun Ke, Ria Rosenauer, Bo Liu, Wenbo Chen, Min Chen, Shuqi Xu, Yue Ma, Jiechao Feng, Bo Chen, Xiangkai Sun, Jiarui Liu, Jinen Guo, Zeyu Zhou, Xu Huang, Zhuohan Li, Haoyu Li, Heguang Lin, Lijie Ding, Yadong Zeng, Kangqi Zhang, Xinge Liu, Hanwen Liu, Zhenghong Li, Alexander von Recum, Yuchen Zhu, Felix Schwarzfischer, Yizhou Zhao, Jicheng Wang, Binxu Li, Qian Yu, Chan Li, Cheng Dai, Di Wang, Haoyu Zhang, Jiankai Sun, Kaituo Feng, Mian Qin, Ruihong Yin, Yiqun Luo, Weiwei Wu, Shihong Pan, Tsung Yeh Hsieh, Xiao Huang, Yan Zhang, Sihan Li, Zirui Ren, Zengji Tu, Kyoung Whan Choe, Ke Sun, Vincenzo Galia, Vaisakhi Mishra, Jiashu He, Hongyang Wang, Zhiheng Yang, Shubham Gaur, Yifan Gu, Shuyi Wang, Zihao Zuo, Steven Dillmann, Yiyou Sun, Xinyang Han, Hanchung Lee, Molei Tao, Yue Zhao, Shilong Liu, Yuchen Wu, Xuandong Zhao, Xiangyi Li, Florian Brand, Gerbrand Ceder, Hartmut Haeffner

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**maintainer**: The BenchFlow team (as listed by the paper authors)

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**funders**: Unverified

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

## Design goals

**capabilities**: Tests whether agents can carry out theoretical, computational and experimental physics research end to end: review the literature, plan the research, run studies and experiments, and deliver structured results plus a scientific manuscript.

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**gap_in_prior_benchmarks**: The authors note that existing physics benchmarks mostly use fixed questions, isolated subtasks or paper reproduction with given solutions, and rarely check research quality together with correctness.

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

## Construction

**question_sources**: 42 physics researchers built tasks from research projects they personally carried out; 56 of 182 submissions were accepted.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**author_background**: Task authors include PhD students, postdocs and research scientists from 26 institutions; the paper reports an average of 420 citations per task author.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**review_process**: Three review stages: an authenticity and provenance check, peer review by an expert in a closely related field, and final approval by an admin team of six physics PhDs.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**quality_control**: Each task author must run state-of-the-art agents locally at least three times and analyse failure modes; the team manually reviewed 168 GPT-6 Astra rollouts, found 9 incorrect failures and revised tasks accordingly.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**decontamination**: Agents are not given the original paper; whether a literature cutoff or other decontamination measures apply is unverified.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

## Data format

**size**: 56 tasks across 9 physics domains.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**question_types**: Open-ended multi-step research tasks that require numerical artifacts checked by deterministic tests plus a manuscript, paper.pdf.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**modalities**: Text, code and data files, with images or simulated devices in some tasks; see Appendix C of the paper for the breakdown.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**languages**: English

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**difficulty**: Research level; the paper reports that the original projects took about 270 days each on average, more than 8,000 research hours in total.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**public_hidden_split**: Some task inputs are public on Hugging Face; whether reference values, hidden tests and rubrics are public is unverified.

Sources: [1](https://huggingface.co/collections/benchflow/frontierphysics-task-datasets) (accessed 2026-11-09); [2](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

## Evaluation

**metrics**: Overall Pass@1 (averaged over three rollouts), Pass@3, deterministic pass rate and the weighted score of Equation 1.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**scoring**: Deterministic verifiers check numerical outputs; a reviewer agent (GPT-5.6 Sol at xhigh in Codex CLI) grades against the author-written rubric; failing the verifier or any blocker scores zero.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**prompt_settings**: Each model runs at its highest available inference effort, three rollouts per task, with a 10-hour cap per rollout; GPT models use Codex CLI, Claude uses Claude Code, Grok uses Grok Build, Gemini uses Antigravity and the rest use Claude Code.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**official_scripts**: Experiments use the BenchFlow CLI; the address of a dedicated FrontierPhysics evaluation repository is unverified.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09); [2](https://github.com/benchflow-ai/benchflow) (accessed 2026-11-09)

**comparability_warning**: Models run in different agent harnesses, so scores reflect both model and harness; the paper also notes that Claude Opus 5.5 is more lenient on its own model family when used as reviewer.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

## Current status

**checked_at**: 2026-11-09

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**latest_dataset_version**: v0.1

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**paper_revision_history**: arXiv v1: 2026-11-04.

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**saturation**: Far from saturated: the best overall Pass@1 is 27.4% by Claude Opus 5.5.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**contamination_and_issues**: Manual review found that grading and task design can cause false failures; after correction the GPT-6 Astra (xhigh) pass rate rose from 14.9% to 20.2%.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**derivatives**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

## Leaderboard snapshot

**snapshot_date**: 2026-11-09

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**official_url**: https://arxiv.org/pdf/2611.06910

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**third_party_url**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**results**:
- rank: 1, model: claude-opus-5-5, score: 27.4, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 2, model: gpt-6-astra, score: 23.2, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / max / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 3, model: gpt-6-astra, score: 19.6, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / xhigh / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 4, model: gpt-6-1-sol, score: 19.6, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 5, model: gpt-6-1-terra, score: 14.3, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 6, model: gpt-6-sol, score: 14.3, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 7, model: claude-fable-5-1, score: 11.3, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 8, model: claude-opus-5, score: 9.5, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 9, model: gemini-4-argon, score: 8.3, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910
- rank: 10, model: kimi-k3-1-pro, score: 6.5, metric: overall Pass@1 (%), track: FrontierPhysics v0.1 / 56 tasks / 3 rollouts per task / paper Table 8, source_url: https://arxiv.org/pdf/2611.06910

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**coverage_note**: The top ten configurations by overall Pass@1 from Table 8 of the paper, all measured by the benchmark authors.

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

## Contact

**public_emails**: Unverified

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**github_issues**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**official_social**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**privacy_policy**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

## Original files

**paper_pdf_url**: https://arxiv.org/pdf/2611.06910

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**sha256**: afec72218ffc2b82ebdf9a73374b6ed95c75e2ea8b292b21788555db8efb42cc

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**pdf_bytes**: 3235112

Sources: [1](https://arxiv.org/pdf/2611.06910) (accessed 2026-11-09)

**drive_folder**: Unverified

Sources: [1](https://arxiv.org/abs/2611.06910) (accessed 2026-11-09)

**other_documents**:
- type: Hugging Face task dataset collection, url: https://huggingface.co/collections/benchflow/frontierphysics-task-datasets

Sources: [1](https://huggingface.co/collections/benchflow/frontierphysics-task-datasets) (accessed 2026-11-09)

## Changelog

- 2026-11-09: Latest review
