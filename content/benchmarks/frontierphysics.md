# FrontierPhysics

物理研究者用本人真实课题出题的端到端研究基准：56个任务要求智能体自主检索文献、开展计算或实验并写出论文，最高通过率不足三成。

## 基本信息

**name**: FrontierPhysics

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**full_name**: FrontierPhysics: Evaluating Agents for End-to-End Physics Research

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**version**: v0.1

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**paper_version**: arXiv v1

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**release_date**: arXiv v1 提交日期为2026-11-04。

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**section**: 物理

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**subfields**: 凝聚态物理, 原子分子与光物理, 量子信息, 天体物理, 流体力学, 统计物理, 光子学与成像, 高能物理, 化学物理

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**license**: 论文以 CC BY 4.0 发布；任务数据与评测代码的许可证待核实。

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**paper_url**: https://arxiv.org/abs/2611.06910

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**code_url**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**dataset_url**: https://huggingface.co/collections/benchflow/frontierphysics-task-datasets

来源: [1](https://huggingface.co/collections/benchflow/frontierphysics-task-datasets) (访问 2026-11-09)

**official_homepage**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**paper_title**: FrontierPhysics: Evaluating Agents for End-to-End Physics Research

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

## 发起与维护

**initiators**: BenchFlow 与 University of California, Berkeley 等机构的物理研究者

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**partners**: 论文作者来自37个机构，包括 Caltech、Harvard、Stanford、Lawrence Berkeley National Laboratory、Oak Ridge National Laboratory 等。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**authors**: Bingran You, Wenjun Ke, Ria Rosenauer, Bo Liu, Wenbo Chen, Min Chen, Shuqi Xu, Yue Ma, Jiechao Feng, Bo Chen, Xiangkai Sun, Jiarui Liu, Jinen Guo, Zeyu Zhou, Xu Huang, Zhuohan Li, Haoyu Li, Heguang Lin, Lijie Ding, Yadong Zeng, Kangqi Zhang, Xinge Liu, Hanwen Liu, Zhenghong Li, Alexander von Recum, Yuchen Zhu, Felix Schwarzfischer, Yizhou Zhao, Jicheng Wang, Binxu Li, Qian Yu, Chan Li, Cheng Dai, Di Wang, Haoyu Zhang, Jiankai Sun, Kaituo Feng, Mian Qin, Ruihong Yin, Yiqun Luo, Weiwei Wu, Shihong Pan, Tsung Yeh Hsieh, Xiao Huang, Yan Zhang, Sihan Li, Zirui Ren, Zengji Tu, Kyoung Whan Choe, Ke Sun, Vincenzo Galia, Vaisakhi Mishra, Jiashu He, Hongyang Wang, Zhiheng Yang, Shubham Gaur, Yifan Gu, Shuyi Wang, Zihao Zuo, Steven Dillmann, Yiyou Sun, Xinyang Han, Hanchung Lee, Molei Tao, Yue Zhao, Shilong Liu, Yuchen Wu, Xuandong Zhao, Xiangyi Li, Florian Brand, Gerbrand Ceder, Hartmut Haeffner

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**maintainer**: BenchFlow 团队（论文作者署名）

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**funders**: 待核实

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

## 设计目标

**capabilities**: 评测智能体能否端到端完成理论、计算与实验物理研究：检索文献、制定研究计划、开展研究与实验，并产出结构化结果和科研论文。

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**gap_in_prior_benchmarks**: 作者指出，现有物理基准多为固定问题、孤立子任务或给定答案的论文复现，很少同时检查研究质量与结果正确性。

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

## 构建方式

**question_sources**: 42位物理研究者依据本人亲自完成的研究项目出题；182份投稿中录用56题。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**author_background**: 出题人包括博士生、博士后与研究科学家，来自26个机构；论文称每位出题人平均被引420次。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**review_process**: 三道审核：真实性与来源审查、相近领域专家同行评审、由六位物理学博士组成的管理团队终审。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**quality_control**: 出题人须用当前最强智能体本地运行至少三次并做失败模式分析；团队人工复核 GPT-6 Astra 的168次运行，发现9次误判失败并据此修订任务。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**decontamination**: 任务不向智能体提供原论文；是否设置文献截止时间及其他去污染措施待核实。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

## 数据形式

**size**: 56个任务，覆盖9个物理领域。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**question_types**: 开放式多步研究任务，需提交可确定性校验的数值产物与论文 paper.pdf。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**modalities**: 文本、代码、数据文件，部分任务含图像或仿真设备；具体分布见论文附录C。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**languages**: 英语

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**difficulty**: 研究级；论文称原项目平均耗时约270天，累计超过8,000小时研究。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**public_hidden_split**: 部分任务输入数据在 Hugging Face 公开；参考答案、隐藏测试与评分细则是否公开待核实。

来源: [1](https://huggingface.co/collections/benchflow/frontierphysics-task-datasets) (访问 2026-11-09); [2](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

## 评测方法

**metrics**: 总体 Pass@1（三次运行平均）、Pass@3、确定性通过率与公式(1)的加权得分。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**scoring**: 确定性校验器检查数值结果；评审智能体（GPT-5.6 Sol xhigh，运行于 Codex CLI）按出题人编写的评分细则打分；未通过校验器或任一阻断项则记0分。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**prompt_settings**: 各模型用最高可用推理强度，每题运行3次，单次上限10小时；GPT 用 Codex CLI，Claude 用 Claude Code，Grok 用 Grok Build，Gemini 用 Antigravity，其余模型用 Claude Code。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**official_scripts**: 实验使用 BenchFlow CLI；FrontierPhysics 专用评测仓库地址待核实。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09); [2](https://github.com/benchflow-ai/benchflow) (访问 2026-11-09)

**comparability_warning**: 不同模型使用不同智能体框架，分数同时反映模型与框架；论文另指出 Claude Opus 5.5 作评审时对同系列模型更宽松。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

## 最新情况

**checked_at**: 2026-11-09

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**latest_dataset_version**: v0.1

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**paper_revision_history**: arXiv v1：2026-11-04。

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**saturation**: 远未饱和：最高总体 Pass@1 为 Claude Opus 5.5 的27.4%。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**contamination_and_issues**: 人工复核发现评审与任务设计会造成误判失败；修正后 GPT-6 Astra（xhigh）通过率由14.9%升至20.2%。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**derivatives**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

## 榜单快照

**snapshot_date**: 2026-11-09

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**official_url**: https://arxiv.org/pdf/2611.06910

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**third_party_url**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

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

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**coverage_note**: 以下为论文表8所列总体 Pass@1 前十个配置，均由基准作者测得。

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

## 联系方式

**public_emails**: 待核实

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**github_issues**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**official_social**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**privacy_policy**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

## 原始文件

**paper_pdf_url**: https://arxiv.org/pdf/2611.06910

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**sha256**: afec72218ffc2b82ebdf9a73374b6ed95c75e2ea8b292b21788555db8efb42cc

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**pdf_bytes**: 3235112

来源: [1](https://arxiv.org/pdf/2611.06910) (访问 2026-11-09)

**drive_folder**: 待核实

来源: [1](https://arxiv.org/abs/2611.06910) (访问 2026-11-09)

**other_documents**: 
- type: Hugging Face 任务数据集合集, url: https://huggingface.co/collections/benchflow/frontierphysics-task-datasets

来源: [1](https://huggingface.co/collections/benchflow/frontierphysics-task-datasets) (访问 2026-11-09)

## 变更记录

- 2026-11-09: 最近复核
