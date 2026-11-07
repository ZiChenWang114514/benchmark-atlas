# CRUXEval

> 第1轮深度复核 · 2026-11-07（Asia/Seoul）。以下结论按字段列明证据；待核实项不是已确认事实。

## 1. 基本信息

**简称**：CRUXEval
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**全称**：CRUXEval
说明：保留官方名称，不把论文标题自动扩写为全称。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**版本**：原始 800 函数；CRUXEval-I / CRUXEval-O 双方向
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**论文版本**：arXiv v1
说明：论文修订版本不等同数据集版本。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**发布日期**：2024-01-06 05:53:51 KST
说明：首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**板块**：代码
说明：Benchmark Atlas 编辑归档；跨领域仅主板块计数。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**子领域**：
- 代码输入输出推断
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**许可与使用边界**：MIT（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）
来源：[1](https://github.com/facebookresearch/cruxeval)（访问 2026-11-07）

**论文**：https://arxiv.org/abs/2401.03065
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**代码**：https://github.com/facebookresearch/cruxeval
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**数据集**：https://huggingface.co/datasets/cruxeval-org/cruxeval
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**官方主页**：https://crux-eval.github.io/
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**论文标题**：CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 2. 发起与维护

**发起机构**：MIT 与 Meta AI 作者团队（作者单位口径）
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**合作机构**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**作者**：
- Gu, Alex
- Rozière, Baptiste
- Leather, Hugh
- Solar-Lezama, Armando
- Synnaeve, Gabriel
- Wang, Sida I.
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**维护方**：facebookresearch/cruxeval当前已标为archived（2026-11-07核验）；历史维护方为CRUXEval团队，不能推断仍在活跃维护。
来源：[1](https://github.com/facebookresearch/cruxeval)（访问 2026-11-07）

**资助**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 3. 设计目标

**测量能力**：代码理解、输入反推和输出预测，尤其在不运行代码时模拟程序执行。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**设计动机**：生成代码的成功率无法独立揭示模型是否理解简单程序的执行语义。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 4. 构建方式

**题目来源**：使用 CodeLlama-34B 生成候选 Python 函数及输入输出，经筛选后随机抽取 800 个。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**出题背景**：MIT / Meta AI 研究者；候选程序由模型合成。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**审核流程**：筛选约可由程序员一分钟内心算的短函数与有效输入输出。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**质量控制**：限制程序复杂性并执行验证配对的输入输出；双方向共用程序，不能算成两个独立题库。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**去污染**：合成新程序旨在减少既有人工题复用，但不构成所有后续模型的无污染证明。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

## 5. 数据形式

**题量**：800 个 Python 函数/输入/输出样本；输入预测与输出预测是同一数据的两种评测。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**题型**：CRUXEval-I：给程序与输出求可行输入；CRUXEval-O：给程序与输入求输出。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**模态**：
- 代码
- 文本
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**语言**：Python；英语提示。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**难度**：短小、可人类心算的程序也可能难于模型；不等同软件开发难度。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**划分与公开范围**：原始数据、脚本与提示公开；未据此主张隐藏集。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 6. 评测方法

**指标**：按方向分别报告 pass@1 / pass@5 等；CoT 与直接回答分开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**评分**：输出预测检查程序真实输出；输入预测接受能经执行产生目标输出的有效输入。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**提示设置**：论文分别报告直接作答与 chain-of-thought；提示、采样数、是否使用执行工具必须说明。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**评测脚本**：https://github.com/facebookresearch/cruxeval
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**可比性说明**：CRUX-I / CRUX-O 分数不平均冒称单一官方总分；不把带解释提示与直接预测混排。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 7. 最新情况

**复核日期**：2026-11-07 KST / Asia/Seoul
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**最新数据版本**：version：原始 800 函数；CRUXEval-I / CRUXEval-O 双方向；evidence_2026_h2：
- url：https://arxiv.org/html/2609.27284v1；date：2026-09-23；note：Hunyuan-A13B §4.1/§4.2及表2–4实际报告 CRUXEval；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。
说明：H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。
来源：[1](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）；[2](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**论文修订与后半年证据**：Submission history From: Alex Gu [ view email ] [v1] 2024-01-06 05:53:51 KST (1,309 KB)
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**饱和情况**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**争议与污染**：Hunyuan 报告参考文献把 CRUXEval 关联到 Liu 2023（EvalPlus）；本条依 Gu 等人 2401.03065 识别原基准。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

**派生版本**：CRUXEval-I 与 CRUXEval-O 是同一 benchmark 两个子任务。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）；[2](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

## 8. 榜单快照

**快照采集日期**：2026-11-07 KST / Asia/Seoul
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**官方榜单**：https://crux-eval.github.io/leaderboard.html
来源：[1](https://crux-eval.github.io/leaderboard.html)（访问 2026-11-07）

**第三方榜单**：待核实
说明：未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**结果快照**：
- model：gpt-4-turbo-2024-04-09+cot (n=3)；score：75.7；metric：i@1 (%)；settings：模型名保留+cot与(n=...)标记；两个子任务分别排序；result_type：官方静态榜快照；source_url：https://crux-eval.github.io/data.csv；source_updated_at：待核实：官方CSV未标统一更新时间；collected_at：2026-11-07 Asia/Seoul
- model：gpt-4o+cot (n=3)；score：75.6；metric：i@1 (%)；settings：模型名保留+cot与(n=...)标记；两个子任务分别排序；result_type：官方静态榜快照；source_url：https://crux-eval.github.io/data.csv；source_updated_at：待核实：官方CSV未标统一更新时间；collected_at：2026-11-07 Asia/Seoul
- model：gpt-4-0613+cot；score：75.5；metric：i@1 (%)；settings：模型名保留+cot与(n=...)标记；两个子任务分别排序；result_type：官方静态榜快照；source_url：https://crux-eval.github.io/data.csv；source_updated_at：待核实：官方CSV未标统一更新时间；collected_at：2026-11-07 Asia/Seoul
- model：gpt-4-turbo-2024-04-09+cot (n=3)；score：82.0；metric：o@1 (%)；settings：模型名保留+cot与(n=...)标记；两个子任务分别排序；result_type：官方静态榜快照；source_url：https://crux-eval.github.io/data.csv；source_updated_at：待核实：官方CSV未标统一更新时间；collected_at：2026-11-07 Asia/Seoul
- model：claude-3-opus+cot (n=1)；score：82.0；metric：o@1 (%)；settings：模型名保留+cot与(n=...)标记；两个子任务分别排序；result_type：官方静态榜快照；source_url：https://crux-eval.github.io/data.csv；source_updated_at：待核实：官方CSV未标统一更新时间；collected_at：2026-11-07 Asia/Seoul
- model：gpt-4-0613+cot；score：77.1；metric：o@1 (%)；settings：模型名保留+cot与(n=...)标记；两个子任务分别排序；result_type：官方静态榜快照；source_url：https://crux-eval.github.io/data.csv；source_updated_at：待核实：官方CSV未标统一更新时间；collected_at：2026-11-07 Asia/Seoul
- model：Hunyuan-A13B base；score：70.13；metric：CRUX-I (%)；benchmark_version：原始双方向；版本待核实；result_type：厂商技术报告自报；source_date：2026-09-23；collected_at：2026-11-07 KST；settings：1-shot
- model：Hunyuan-A13B base；score：77；metric：CRUX-O (%)；benchmark_version：原始双方向；版本待核实；result_type：厂商技术报告自报；source_date：2026-09-23；collected_at：2026-11-07 KST；settings：1-shot
来源：[1](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；[2](https://crux-eval.github.io/leaderboard.html)（访问 2026-11-07）；[3](https://arxiv.org/html/2609.27284v1)（访问 2026-11-07）

**覆盖边界**：直接读取官方leaderboard.html加载的data.csv，分别列I/O的pass@1前三行，保留CoT和n标记。官方静态数据未标更新时间，不宣称为2026全球SOTA；厂商自报另列，不合并排名。
来源：[1](https://crux-eval.github.io/data.csv)（访问 2026-11-07）；[2](https://crux-eval.github.io/leaderboard.html)（访问 2026-11-07）

## 9. 联系方式

**公开项目邮箱**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**问题反馈**：https://github.com/facebookresearch/cruxeval/issues
说明：公开仓库反馈入口；未发送问题。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

**官方社交渠道**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

**隐私政策**：待核实
说明：本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。
来源：[1](https://arxiv.org/abs/2401.03065)（访问 2026-11-07）

## 10. 原始文件

**Drive PDF**：id：1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9；webViewLink：https://drive.google.com/file/d/1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9/view?usp=drivesdk
来源：[1](https://drive.google.com/file/d/1i5PlfnmPWcdgwpLBx7QzGG4sM5GQjPr9/view?usp=drivesdk)（访问 2026-11-07）

**原始PDF地址**：https://arxiv.org/pdf/2401.03065
说明：归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。
来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

**SHA256**：1a356948d0d2543ab7b142029f208271a2581575cee4f5b37eb647cbbf0b435e
说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。
来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

**PDF字节数**：2012215
说明：源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。
来源：[1](https://arxiv.org/pdf/2401.03065)（访问 2026-11-07）

**Drive目录**：id：1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou；webViewLink：https://drive.google.com/drive/folders/1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou
来源：[1](https://drive.google.com/drive/folders/1qn4p1I6dvvu5vgEmKvTMsHfElROPZ5ou)（访问 2026-11-07）

**其他文档**：
- type：中文介绍Google Doc；id：14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c；webViewLink：https://docs.google.com/document/d/14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c/edit?usp=drivesdk
说明：官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）；[2](https://docs.google.com/document/d/14mrYcERScHID5m5l9rGgjWvRpEag9WhAjK0AplL5Z3c/edit?usp=drivesdk)（访问 2026-11-07）

## 11. 变更记录

**记录**：
- date：2026-11-07；timezone：KST / Asia/Seoul；change：首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。
- date：2026-11-07；timezone：Asia/Seoul；change：深度优化第1轮：重开官方材料与2026H2引用，补授权边界、文件级题量、版本冲突及官方静态榜；未知项保留，不将采集日期当榜单更新时间。
来源：[1](https://crux-eval.github.io/)（访问 2026-11-07）

