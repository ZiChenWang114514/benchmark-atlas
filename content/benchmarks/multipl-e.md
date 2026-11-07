# MultiPL-E

> 第1轮深度复核 · 2026-11-07（Asia/Seoul）。以下结论按字段列明证据；待核实项不是已确认事实。

## 1. 基本信息

**简称**：MultiPL-E
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**全称**：MultiPL-E
说明：保留官方名称，不把论文标题自动扩写为全称。
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**版本**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**论文版本**：arXiv v4
说明：论文修订版本不等同数据集版本。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**发布日期**：2022-08-17 20:16:52 KST
说明：首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**板块**：代码
说明：Benchmark Atlas 编辑归档；跨领域仅主板块计数。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**子领域**：
- 多语言代码生成
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**许可与使用边界**：仓库：BSD 3-Clause with Machine Learning Restriction，第4条禁止训练用途；官方HF数据卡另标MIT。两种发布载体声明不一致，分别保留，不能据HF标签绕过仓库条款。
来源：[1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/LICENSE)（访问 2026-11-07）；[2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-07）

**论文**：https://arxiv.org/abs/2208.08227
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**代码**：https://github.com/nuprl/MultiPL-E
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**数据集**：https://huggingface.co/datasets/nuprl/MultiPL-E
来源：[1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/README.md)（访问 2026-11-07）；[2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-07）

**官方主页**：https://github.com/nuprl/MultiPL-E
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**论文标题**：MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 2. 发起与维护

**发起机构**：以 Northeastern University 等多校研究人员组成的作者团队为主；详见论文作者单位。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**合作机构**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**作者**：
- Cassano, Federico
- Gouwar, John
- Nguyen, Daniel
- Nguyen, Sydney
- Phipps-Costin, Luna
- Pinckney, Donald
- Yee, Ming-Ho
- Zi, Yangtian
- Anderson, Carolyn Jane
- Feldman, Molly Q
- Guha, Arjun
- Greenberg, Michael
- Jangda, Abhinav
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**维护方**：nuprl / MultiPL-E 官方仓库团队
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**资助**：论文致谢 NSF CCF-2052696 的部分支持。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 3. 设计目标

**测量能力**：跨编程语言的函数级代码生成、编译与功能测试。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**设计动机**：只评 Python 难以判断语言模型在其他编程语言中的迁移能力；逐语言手工造题成本高。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 4. 构建方式

**题目来源**：将 Python HumanEval 和 MBPP 的签名、类型、文档及测试翻译为其他语言；不翻译参考实现函数体。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**出题背景**：编程语言与程序合成研究人员。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**审核流程**：语言专用翻译器把规范与测试转成目标语言；以容器运行编译与测试。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**质量控制**：处理目标语言类型、标准库与运行时差异，保留语言特定排除项。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**去污染**：翻译不能保证去除 Python 原题污染；模型仍可能记忆语义或已公开译题。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 5. 数据形式

**题量**：原论文：Python 加 18 种目标语言，共 19 种；MultiPL-HumanEval 3,059 个任务、MultiPL-MBPP 7,619 个任务，含语言特定排除。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**题型**：函数级程序补全与单元测试。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**模态**：
- 文本
- 代码
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**语言**：19 种编程语言（含原始 Python）；英语自然语言规范。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**难度**：继承 HumanEval 与 MBPP，不解释为 19 个独立 benchmark。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**划分与公开范围**：翻译器、提示、测试和执行框架公开；不同语言允许的题目并非完全相同。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 6. 评测方法

**指标**：执行测试的 pass@k。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**评分**：代码在目标语言容器内编译并运行；使用 pass@k 无偏估计。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**提示设置**：原论文每题 200 个样本；pass@1 温度 0.2，pass@10/100 温度 0.8。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**评测脚本**：https://github.com/nuprl/MultiPL-E
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**可比性说明**：语言集合、有效题目、温度和 k 都影响结果；8 语言报告不可冒称完整 19 语言总分。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 7. 最新情况

**复核日期**：2026-11-07 KST / Asia/Seoul
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**最新数据版本**：version：待核实；evidence_2026_h2：
- url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1/§4.2及表2–4实际报告 MultiPL-E；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。
说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。
来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

**论文修订与后半年证据**：Submission history From: Arjun Guha [ view email ] [v1] 2022-08-17 20:16:52 KST (1,172 KB) [v2] 2022-08-19 10:12:49 KST (1,172 KB) [v3] 2022-11-08 14:48:57 KST (1,172 KB) [v4] 2022-12-19 19:30:12 KST (1,780 KB)
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**饱和情况**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**争议与污染**：权利冲突：官方GitHub LICENSE为带禁止机器学习训练条款的BSD衍生许可；官方HF卡license字段为MIT。应核实具体下载载体、版本及上游母题权利，不将其统一标成MIT。
来源：[1](https://raw.githubusercontent.com/nuprl/MultiPL-E/main/LICENSE)（访问 2026-11-07）；[2](https://huggingface.co/datasets/nuprl/MultiPL-E/raw/main/README.md)（访问 2026-11-07）

**派生版本**：MultiPL-HumanEval 与 MultiPL-MBPP 是 MultiPL-E 两个来源分支，不重复计数。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 8. 榜单快照

**快照采集日期**：2026-11-07 KST / Asia/Seoul
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**官方榜单**：https://github.com/nuprl/MultiPL-E
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**第三方榜单**：待核实
说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**结果快照**：
- model：Hunyuan-A13B base；score：69.33；metric：MultiPL-E (%)；benchmark_version：8语言子集；版本待核实；result_type：厂商技术报告自报；source_date：2026-09-23；collected_at：2026-11-07 KST；settings：0-shot；Python/C++/Java/PHP/TypeScript/C#/Bash/JavaScript
来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

**覆盖边界**：下面仅列能从已打开来源核验的结果。历史论文基线、厂商自报与当前榜单分开，不构成跨设置综合排名。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 9. 联系方式

**公开项目邮箱**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**问题反馈**：https://github.com/nuprl/MultiPL-E/issues
说明：公开仓库反馈入口；未发送问题。
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

**官方社交渠道**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

**隐私政策**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2208.08227)（访问 2026-11-07）

## 10. 原始文件

**Drive PDF**：id：1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ；webViewLink：https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk
来源：[1](https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk)（访问 2026-11-07）

**原始PDF地址**：https://arxiv.org/pdf/2208.08227
说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。
来源：[1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-07）

**SHA256**：b905b9874ffcb4cee63f74cdc30524eae97013691e79313049ad72c6d6197580
说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。
来源：[1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-07）

**PDF字节数**：443169
说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。
来源：[1](https://arxiv.org/pdf/2208.08227)（访问 2026-11-07）

**Drive目录**：id：1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF；webViewLink：https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF
来源：[1](https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF)（访问 2026-11-07）

**其他文档**：
- type：中文介绍Google Doc；id：1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM；webViewLink：https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk
说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）；[2](https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk)（访问 2026-11-07）

## 11. 变更记录

**记录**：
- date：2026-11-07；timezone：KST / Asia/Seoul；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；timezone：Asia/Seoul；change：深度优化第1轮：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
来源：[1](https://github.com/nuprl/MultiPL-E)（访问 2026-11-07）

