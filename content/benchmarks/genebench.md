# GeneBench / GeneBench Pro

> Benchmark Constitution｜深度核验：2026-11-07。访问日沿固定采集日，运行时间另列。待核实不等于未公开；来源冲突并列保留。

GeneBench与GeneBench-Pro测试基因组学定量分析中的连续判断，而不是生物知识选择题。旧档只依据模型发布文而漏掉论文与开放案例；补齐后特别纠正：任务基于现实研究模式，但底层评测数据为构造性模拟。

最近复核

## 基本信息

**简称**：GeneBench / GeneBench Pro

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**全称**：GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics and Quantitative Biology；扩展版GeneBench-Pro分轨

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**基准版本**：GeneBench；GeneBench Pro v13另轨

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**论文版本**：官方PDF日期2026-04-23；GeneBench-Pro官方发布文日期2026-06-30，Pro v13见Astra脚注12。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

**发布日期**：GeneBench论文日期2026-04-23；GeneBench-Pro发布日2026-06-30（不把Rosalind 6月模型更新日当基准首发）。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**主板块**：生物与医学

核验说明：Benchmark Constitution 编辑归档，不作为官方分类。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**领域标签**：计算生物学；统计遗传学；多阶段科学推断；定量生物学Agent

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**许可证与授权边界**：GeneBench-Pro公开10案例包为MIT（HF卡与LICENSE）；这不自动授予完整103/129题或未发布资产同一许可证。

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/LICENSE)（访问 2026-11-07）

**论文或技术报告**：https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf

核验说明：官方直接PDF，未定位可核验arXiv编号，不杜撰abs链接。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

**官方代码**：https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/reference_grader.py

核验说明：官方HF内含Python参考grader，并非另有已核验GitHub仓库。

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**数据地址**：https://huggingface.co/datasets/openai/genebench-pro-public-package

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**官方主页**：https://openai.com/index/introducing-genebench-pro/

来源：[1](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**论文题名**：GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics and Quantitative Biology

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

## 发起与维护

**发起方**：OpenAI

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**协作与机构边界**：原论文署名机构为OpenAI与Herasight（Jeremy Li双署名）；Pro另有外部专家审核82题，不能把专家所属单位自动视为合作主办方。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**作者**：Jeremy Li；Andrew Ho

核验说明：原GeneBench论文署名，不能据此断言这就是全部Pro贡献者。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

**维护方**：OpenAI

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**资助方**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

## 设计目标

**测量能力**：基因组学与定量生物学的长程端到端分析：规划、质控、建模与校正，得到决策相关答案。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**相对既有评测的缺口**：不只测生物知识检索、常规分析流水线或孤立步骤，而测能否依据诊断信号更新estimand、质控与模型选择，并把变化传递到最终决策。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

## 构建方式

**题目来源**：纠正旧档“真实科学数据”概括：基于文献与内部专家归纳现实分析模式，但GeneBench及Pro采用构造性模拟数据，控制完整因果/生成过程以得到可识别数值答案；不是直接复用历史真实队列。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**出题与研究背景**：GeneBench由Jeremy Li（OpenAI/Herasight）与Andrew Ho（OpenAI）署名；Pro审核者包括研究生、博士后、产业科学家及教授。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**审核流程**：原版进行科学有效性、方法合理性、目标可识别性的独立复核；Pro的129题中82题交外部领域专家审查，反馈用于修订；并非全部129题均已外审。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**质量控制**：对合理分析扰动保持数值容忍，对错误分析用消融验证其必须失败；多轮前沿模型试跑和完整轨迹审计检查信息泄漏、提示与grader不匹配及非预期捷径。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**去污染与泄漏边界**：避免复刻著名教材/论文案例，合成新数据并做泄漏与捷径审计；公开10案例含ground truth和容差，官方明确用于复现而非隐藏答案榜单，不能用该包测无污染泛化。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

## 数据形式

**规模与口径**：原GeneBench：103评测/10领域；GeneBench-Pro：129题/10领域/21子领域；公开案例10题；另计划向Artificial Analysis提供50题，不把计划误称已独立实跑。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**任务类型**：隔离工作区中的多阶段科学数据分析，输出题目指定JSON数值/决策字段与简短推理；不是五选一Genome-Bench问答。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**模态**：科学数据；代码；文本分析

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**语言**：公开GeneBench-Pro卡标注en；数据分析工具包含Python与PLINK 2.0等，不能将工具语言当自然语言覆盖。

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**难度**：原版每题含3–13个实质推断决策点，中位数6；Pro外部审核者估计典型题需专家20–40小时，该估计不是实测人类完成时间。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**公开与隐藏划分**：Pro公开10代表案例，含任务、模拟文件、ground_truth、grader合同及参考脚本；官方另宣布50题拟供AA。未公开资产的可获取性不由此推断。公开包不是隐藏测试集。

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

## 评测方法

**指标**：原版主指标为每题多次运行通过率的非加权均值（103题）；Pro以确定性目标及容差判pass。公开grader的passed为权威结论，score仅字段诊断汇总，不替代pass。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**评分方式**：根据可由可见证据恢复的目标与逐字段校准容差确定性二元评分，不是LLM按长篇rubric偏好打分；公开包依eval_config.json的ground_truth与grader.config。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**提示与运行设置**：Pro提供隔离工作区、简短科学背景、目标estimand和数据文件，工具栈含Python科学计算与基础基因组包；公开复现只给Agent task与data_files，答案及grader留在runner端。模型reasoning档及Pro harness必须分轨。

来源：[1](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**官方复现入口**：https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/reference_grader.py（Python>=3.10；读取问题eval_config.json和eval_answer.json）

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**可比性警告**：GeneBench 103题、Pro 129题、Pro v13、公开10题、拟AA 50题不能混排；GPT Pro harness也不等同同名普通推理档。Rosalind更新页21.6/20.4与论文历史配置不同，保留各自来源语境。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）；[4](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

## 最新情况

**本次核验**：2026-11-07

来源：[1](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**数据及热度证据**：```json
{
 "version": "GeneBench；GeneBench Pro v13另轨"
 "heat_confidence": "B"
 "why_trending": "主要是单一机构当前展示或厂商持续自评，不代表全行业广泛采纳。"
 "evidence_2026_h2": [
 {
 "url": "https://openai.com/index/gpt-6-astra/"
 "date": "2026-11-07"
 "date_type": "observed_on"
 "organization": "OpenAI"
 "note": "当前发布页实际报告该benchmark分数；厂商自报。"
 }
 ]
}
```

来源：[1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

**论文与版本历史**：原GeneBench官方PDF署2026-04-23；2026-06-30发布更难Pro（129题）。Astra后续报告GeneBench Pro v13；未把PDF日期或Pro编号拼成不存在的arXiv版号。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

**饱和程度**：Pro发布文曾预测年底可能饱和，但这是预测不是已发生事实；当前重新打开的Astra发布文报告Pro v13 37.1%，仍非满分，不能按预测写已饱和。

来源：[1](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[2](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）

**已知问题与局限**：公开案例含标准答案与容差，不能作为隐藏测评；合成数据保可识别性但不自动代表全部真实生物研究。Pro用前沿GPT试跑硬化可能有家族选择偏差；82/129题外审不等于全量外审。

来源：[1](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）

**后续与衍生**：GeneBench-Pro是原103题GeneBench的扩展、更难套件；与Princeton/Stanford的Genome-Bench（3332条CRISPR讨论问答）不是同一基准。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://arxiv.org/abs/2505.19501)（访问 2026-11-07）

## 榜单快照

**快照日期**：2026-11-07

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**官方入口**：https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**第三方入口**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

| 分轨/范围 | 名次 | 模型/系统 | 得分 | 指标 | 运行/提交日期 | 来源 |
|---|---:|---|---:|---|---|---|
| Astra发布文自报 | 1 | GPT-6 Astra | 37.1 | GeneBench Pro v13 accuracy (%) | 待核实 | [原始来源](https://openai.com/index/gpt-6-astra/) |
| Astra发布文自报 | 2 | GPT-5.6 Sol | 32.3 | GeneBench Pro v13 accuracy (%) | 待核实 | [原始来源](https://openai.com/index/gpt-6-astra/) |
| GeneBench-Pro 129题发布时 | — | GPT-5.6 Sol Pro | 31.5 | pass rate (%) | 时间未标注 | [原始来源](https://openai.com/index/introducing-genebench-pro/) |
| GeneBench-Pro 129题发布时 | — | GPT-5.6 Sol highest reasoning | 28.7 | pass rate (%) | 时间未标注 | [原始来源](https://openai.com/index/introducing-genebench-pro/) |
| GeneBench 103题原论文历史 | — | GPT-5.5 Pro | 33.2 | pass rate (%) | 时间未标注 | [原始来源](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf) |
| GeneBench 103题原论文历史 | — | GPT-5.5 xhigh | 25.0 | pass rate (%) | 时间未标注 | [原始来源](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf) |
| GeneBench 103题原论文历史 | — | Gemini 3.1 Pro | 11.2 | pass rate (%) | 时间未标注 | [原始来源](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf) |

采集：2026-11-07；运行日/提交日与榜表更新时间不混同。分轨名次只在各自协议中成立。

**覆盖说明**：找到并读取原GeneBench完整官方PDF与Pro发布页、HF卡/LICENSE。v13当前对比沿Astra原表核验37.1/32.3；补充原版及Pro历史分轨，不把公开10例或AA计划50题拼成统一榜。榜表总体更新时间待核实。

来源：[1](https://openai.com/index/gpt-6-astra/)（访问 2026-11-07）；[2](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[3](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）；[4](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

## 联系方式

**公开联系邮箱**：h.jeremy.li@gmail.com；ajh@openai.com

核验说明：仅收原论文公开的通讯作者邮箱，不推断其他私人联系方式。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

**Issues或讨论入口**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**官方社交**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**隐私政策**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

## 原始文件

**原始PDF**：https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

**PDF SHA-256**：85b64c95d938cbe54ff9d6c2279fa88a0421f908b953d9a245c88d083e6b9bdb

核验说明：下载原始PDF字节计算，非arXiv网页显示大小。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

**PDF字节数**：```json
772256
```

核验说明：实际下载字节数；不代表已上传。

来源：[1](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/oai_genebench_benchmark.pdf)（访问 2026-11-07）

**文件夹**：待核实

状态：待核实。

核验说明：已检查所列官方材料，但本字段尚未完成精确核验；不表示官方未公开。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

**其他官方文档**：```json
[
 {
 "type": "Pro发布与方法"
 "url": "https://openai.com/index/introducing-genebench-pro/"
 }
 {
 "type": "公开案例及参考grader"
 "url": "https://huggingface.co/datasets/openai/genebench-pro-public-package"
 }
]
```

来源：[1](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）；[2](https://huggingface.co/datasets/openai/genebench-pro-public-package/blob/main/README.md)（访问 2026-11-07）

**论文链接**：待核实

状态：待核实。

核验说明：本组仅建立本地研究条目，未上传。

来源：[1](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/)（访问 2026-11-07）

## 变更记录

**及历史变更**：```json
[
 {
 "date": "2026-11-07"
 最近复核
 }
 {
 "date": "2026-11-07"
 最近复核
 }
]
```

来源：[1](https://openai.com/index/introducing-genebench-pro/)（访问 2026-11-07）
