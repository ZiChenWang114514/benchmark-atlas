# MBPP

> 第1轮深度复核 · 2026-11-07（Asia/Seoul）。以下结论按字段列明证据；待核实项不是已确认事实。

## 1. 基本信息

**简称**：MBPP
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**全称**：Mostly Basic Programming Problems
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**版本**：原始 974 题；sanitized 子集需单独注明
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**论文版本**：arXiv v1
说明：论文修订版本不等同数据集版本。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**发布日期**：2021-08-16 12:57:30 KST
说明：首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**板块**：代码
说明：Benchmark Atlas 编辑归档；跨领域仅主板块计数。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**子领域**：
- Python基础编程
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**许可与使用边界**：Google Research 根目录 LICENSE 为 Apache-2.0；mbpp目录未读到独立LICENSE（404），数据单独授权仍待核实，不以代码仓库根许可推断第三方题目权利。
来源：[1](https://raw.githubusercontent.com/google-research/google-research/master/LICENSE)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md)（访问 2026-11-07）

**论文**：https://arxiv.org/abs/2108.07732
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**代码**：https://github.com/google-research/google-research/tree/master/mbpp
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**数据集**：https://github.com/google-research/google-research/tree/master/mbpp
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**官方主页**：https://github.com/google-research/google-research/tree/master/mbpp
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**论文标题**：Program Synthesis with Large Language Models
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 2. 发起与维护

**发起机构**：Google Research；部分作者在 MIT 或以实习身份参与。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**合作机构**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**作者**：
- Austin, Jacob
- Odena, Augustus
- Nye, Maxwell
- Bosma, Maarten
- Michalewski, Henryk
- Dohan, David
- Jiang, Ellen
- Cai, Carrie
- Terry, Michael
- Le, Quoc
- Sutton, Charles
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**维护方**：Google Research 官方 mbpp 数据目录
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**资助**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 3. 设计目标

**测量能力**：从简短自然语言要求生成基础 Python 程序，并使用执行结果检验功能。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**设计动机**：研究不同规模预训练模型的程序合成、提示与微调表现，需要多样且可执行的入门任务。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 4. 构建方式

**题目来源**：众包任务；每题有文字说明、Python 参考代码和 3 个断言测试。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**出题背景**：具备基础 Python 的内部众包工作者，可使用互联网资源。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**审核流程**：研究团队对一部分任务做人工校订，改进描述、签名和测试。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**质量控制**：原论文报告人工校订 426 题；后续托管 sanitized 常见 427 题，不能假定完全相同快照。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**去污染**：原论文核查 974 题中 32 题与预训练样本有超过一半代码行匹配；这是当时模型的重叠检查，不是今天的清洁证明。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 5. 数据形式

**题量**：官方文件实读：原始 mbpp.jsonl 为974题，sanitized-mbpp.json为427题；不是两个独立benchmark。
来源：[1](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/mbpp.jsonl)（访问 2026-11-07）；[2](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/sanitized-mbpp.json)（访问 2026-11-07）

**题型**：文本到 Python 函数，附断言测试和参考程序。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**模态**：
- 文本
- 代码
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**语言**：Python（原论文执行环境 Python 3.6）；英语任务。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**难度**：面向基础编程；不是竞赛或仓库级软件工程。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**划分与公开范围**：官方README按ID划分：11–510测试（500），1–10 few-shot（10），511–600验证（90），601–974训练（374）；sanitized子集继承这些分组。所有文件公开，不是隐藏测试。
来源：[1](https://raw.githubusercontent.com/google-research/google-research/master/mbpp/README.md)（访问 2026-11-07）

## 6. 评测方法

**指标**：功能正确率；必须区分逐样本通过比例与多样本中至少一次解出。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**评分**：运行生成程序并检查断言；原始测试少，不能代替 MBPP+ 加强测试。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**提示设置**：原论文常用 80 个样本、温度 0.5；少样本示例配置需一并报告。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**评测脚本**：https://github.com/google-research/google-research/tree/master/mbpp
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**可比性说明**：原始 974、test 500、sanitized 427、EvalPlus 评测 399 的分母不同；不可横向混排。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 7. 最新情况

**复核日期**：2026-11-07 KST / Asia/Seoul
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**最新数据版本**：version：原始 974 题；sanitized 子集需单独注明；evidence_2026_h2：
- url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1/§4.2及表2–4实际报告 MBPP；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。
说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。
来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）；[2](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**论文修订与后半年证据**：Submission history From: Augustus Odena [ view email ] [v1] 2021-08-16 12:57:30 KST (2,247 KB)
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**饱和情况**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**争议与污染**：公开且被广泛使用的基础题库存在训练重叠风险；原始少量测试有漏检错误的局限。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**派生版本**：MBPP sanitized、MBPP+ 为子集/增强派生，不替换原始 MBPP 定义。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 8. 榜单快照

**快照采集日期**：2026-11-07 KST / Asia/Seoul
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**官方榜单**：https://github.com/google-research/google-research/tree/master/mbpp
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**第三方榜单**：待核实
说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**结果快照**：
- model：Hunyuan-A13B base；score：83.86；metric：MBPP (%)；benchmark_version：split/版本待核实；result_type：厂商技术报告自报；source_date：2026-09-23；collected_at：2026-11-07 KST；settings：3-shot
来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

**覆盖边界**：下面仅列能从已打开来源核验的结果。历史论文基线、厂商自报与当前榜单分开，不构成跨设置综合排名。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 9. 联系方式

**公开项目邮箱**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**问题反馈**：https://github.com/google-research/google-research/issues
说明：公开仓库反馈入口；未发送问题。
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

**官方社交渠道**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

**隐私政策**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2108.07732)（访问 2026-11-07）

## 10. 原始文件

**Drive PDF**：id：1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P；webViewLink：https://drive.google.com/file/d/1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P/view?usp=drivesdk
来源：[1](https://drive.google.com/file/d/1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P/view?usp=drivesdk)（访问 2026-11-07）

**原始PDF地址**：https://arxiv.org/pdf/2108.07732
说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。
来源：[1](https://arxiv.org/pdf/2108.07732)（访问 2026-11-07）

**SHA256**：820a8de4a9fe8aef947a40d5da13db0d660baf3658b4a9cebf6d30ac5ba351ab
说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。
来源：[1](https://arxiv.org/pdf/2108.07732)（访问 2026-11-07）

**PDF字节数**：1540169
说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。
来源：[1](https://arxiv.org/pdf/2108.07732)（访问 2026-11-07）

**Drive目录**：id：1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB；webViewLink：https://drive.google.com/drive/folders/1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB
来源：[1](https://drive.google.com/drive/folders/1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB)（访问 2026-11-07）

**其他文档**：
- type：中文介绍Google Doc；id：18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw；webViewLink：https://docs.google.com/document/d/18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw/edit?usp=drivesdk
说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）；[2](https://docs.google.com/document/d/18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw/edit?usp=drivesdk)（访问 2026-11-07）

## 11. 变更记录

**记录**：
- date：2026-11-07；timezone：KST / Asia/Seoul；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；timezone：Asia/Seoul；change：深度优化第1轮：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
来源：[1](https://github.com/google-research/google-research/tree/master/mbpp)（访问 2026-11-07）

