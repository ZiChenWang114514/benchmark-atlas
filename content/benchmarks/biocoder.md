# BioCoder

> 核查：2026-11-07（，）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

BioCoder

来源：[1]

### 全称

BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models

来源：[1]

### 数据/软件版本

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 论文版本

arXiv v5：2024-05-21 02:19:13；另有Bioinformatics 40(Supplement_1):i266–i276，2024，doi:10.1093/bioinformatics/btae230。

来源：[1][2]

### 发布日期

2023-08-31（首个arXiv版本日期；非推定数据上线日）

来源：[1]

### 主板块

生物与医学

来源：[3]

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 学科标签

生物信息学代码生成

来源：[3]

### 许可证与范围

官方README链接的HF数据卡标记CC-BY-4.0；网站源码说明CC-BY-SA-4.0。未在根目录LICENSE/LICENSE.md找到代码授权，不能把网站或HF数据许可自动扩大到整个代码仓库及所有第三方源代码。

来源：[4][5][2]

说明：数据与网站许可已核实；代码总许可仍待核实。

状态：待核实（本字段尚有未能确认的部分）。

### 论文入口

https://arxiv.org/abs/2308.16458

来源：[1]

### 论文标题

BioCoder: A Benchmark for Bioinformatics Code Generation with Large Language Models

来源：[1]

### 官方代码

https://github.com/gersteinlab/BioCoder

来源：[1]

### 数据入口

https://huggingface.co/datasets/lilbillbiscuit/biocoder_public

来源：[2][6]

### 官方主页

https://biocoder-benchmark.github.io/

来源：[1]

## 2. 发起与维护

### 发起团队

Yale与Google DeepMind论文作者合作。

来源：[1]

### 署名/合作机构

Yale University；Google DeepMind

来源：[7][5]

说明：论文作者署名单位；前四作者与Mark Gerstein为Yale，Xinyun Chen为Google DeepMind。

### 作者

Tang, Xiangru；Qian, Bill；Gao, Rick；Chen, Jiakang；Chen, Xinyun；Gerstein, Mark

来源：[1]

### 维护入口

gersteinlab/BioCoder与官方项目页。

来源：[1]

### 资助与计算资源

Schmidt Futures支持Mark Gerstein与Xiangru Tang（原论文Acknowledgment明确致谢）。

来源：[7]

## 3. 设计目标

真实项目上下文与fuzz功能等价检查比孤立短函数更贴近生物信息工程，但测试通过仍受输入覆盖限制。源代码公开和作者混淆消融只说明记忆风险被分析过，不意味着训练/评测完全隔离。
来源：[1][1]

### 测量能力

带依赖、类、全局变量等真实上下文的生物信息学函数代码生成。

来源：[1]

### 为何需要这个基准

一般短函数题不充分测试生物知识、复杂数据操作及真实项目上下文。

来源：[1]

## 4. 构建方式

### 材料来源

GitHub生物项目中的Python函数、Java方法及Rosalind编程题。

来源：[1]

### 命题/编制背景

Yale/Google DeepMind生物信息与代码生成研究团队；非声称所有题均独立专家原创。

来源：[1]

### 审核流程

语法解析抽取真实函数，静态分析、人工测试和fuzzing结合构建验证。

来源：[1]

### 质量控制

Docker可执行测试环境与自动化模糊测试，保留依赖/类/全局环境。

来源：[1]

### 去污染与证据边界

附录M把函数名与参数改为FUNCTION/VAR0等做混淆消融，降低直接代码记忆作用；不是训练语料严格隔离。该消融Python Pass@1从25.960降至22.771、Java从34.700降至30.700；这是特定提示/实验，不替换官网Summary Only榜。

来源：[7]

## 5. 数据形式

### 规模与分母

1,026 Python函数、1,243 Java方法，另253个Rosalind例子；不要混同为同一语言总题数。

来源：[1]

### 题型

根据签名/上下文/描述生成函数或方法体；多个提示布局。

来源：[1]

### 模态与字段

源代码、自然语言说明、单元/模糊测试。

来源：[1]

### 语言

Python；Java；英语提示

来源：[1]

### 难度定位

真实项目依赖和专业生物信息任务；无统一难度分档。

来源：[1]

### 公开、隐藏与划分

README列出java_hidden 1,243、python_hidden 1,026；另各有50条public与50条similar；rosalind 253条。名称hidden不等于当前访问受限：README明确完整公共数据已在仓库发布。

来源：[2]

## 6. 评测方法

### 指标

Pass@1/5/10/20，分Python、Java、Rosalind。

来源：[1]

### 评分流程

代码运行与fuzz-testing判断Passed；Rosalind示例每题20次生成，按组合概率估计Pass@1/5/10/20并跨题均值。不可把Pass@20当成一次生成准确率。

来源：[2]

### 运行与提示

官网Summary Only榜：temperature0.7、top-p0.95、最大生成256token；GPT4上下文8192。

来源：[1][5]

### 评测实现

官方仓库evaluation/包含Docker/AWS队列执行框架，TestRosalind/tester.py生成results.json；README指出完全本地化框架为未来计划，不宣称已提供。

来源：[2]

### 不能混比的设置

提示布局、上下文窗口、生成长度和语言不同影响结果。官网模型日期为历史标签，不应误写采集日模型排名。

来源：[1]

## 7. 最新情况

### 核查日期

2026-11-07（采集日，不是实验日）

来源：[1]

### 当前发布

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 版本脉络

v1：2023-08-31；v2：2023-09-06；v3：2023-09-30；v4：2023-12-04；v5：2024-05-21；journal：Bioinformatics2024 doi:10.1093/bioinformatics/btae230；不把论文修订日当数据更新日。

来源：[1][2]

### 分数上限与饱和度

官网历史低通过率不说明2026模型当前上限；未获得更新统一实验。

来源：[1]

### 争议与局限

公开GitHub代码与Rosalind题可进入预训练；论文有名称/参数混淆消融但不能排除数据泄漏。Fuzz测试覆盖有限；GPT辅助筛选生物信息代码可产生选择偏差。官网历史标签不是模型实际测试时刻。

来源：[7][5]

### 衍生版本

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 8. 榜单快照

### 采集日期

2026-11-07（采集日，不是实验日）

来源：[1]

### 官方入口

https://biocoder-benchmark.github.io/

来源：[5]

### 第三方/补充实验

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### BioCoder-Py / Summary Only / 官网历史展示次序

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | gpt-4 | 38.439 | Pass@1 (%) |
| 2 | gpt-3.5-turbo | 24.682 | Pass@1 (%) |
| 3 | Starcoder | 4.682 | Pass@1 (%) |

- gpt-4：pass_at_5：48.491；pass_at_10：50.619；pass_at_20：52.229；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排
- gpt-3.5-turbo：pass_at_5：33.997；pass_at_10：37.132；pass_at_20：40.127；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排
- Starcoder：pass_at_5：15.225；pass_at_10：21.2；pass_at_20：27.166；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排

#### BioCoder-Java / Summary Only / 官网历史展示次序

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | gpt-4 | 45.011 | Pass@1 (%) |
| 2 | gpt-3.5-turbo | 17.4 | Pass@1 (%) |
| 3 | Starcoder+ | 1.3 | Pass@1 (%) |

- gpt-4：pass_at_5：55.35；pass_at_10：57.616；pass_at_20：60.0；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排
- gpt-3.5-turbo：pass_at_5：33.199；pass_at_10：37.878；pass_at_20：42.0；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排
- Starcoder+：pass_at_5：5.031；pass_at_10：8.042；pass_at_20：12.0；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排

#### BioCoder-Rosalind / Summary Only / 官网历史展示次序

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | gpt-4 | 24.308 | Pass@1 (%) |
| 2 | gpt-3.5-turbo | 23.671 | Pass@1 (%) |
| 3 | Starcoder | 0.534 | Pass@1 (%) |

- gpt-4：pass_at_5：39.551；pass_at_10：44.864；pass_at_20：50.198；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排
- gpt-3.5-turbo：pass_at_5：31.953；pass_at_10：36.702；pass_at_20：40.725；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排
- Starcoder：pass_at_5：2.042；pass_at_10：3.228；pass_at_20：4.743；temperature：0.7；top_p：0.95；max_generation_tokens：256；max_context_length：8192；source_url：https://biocoder-benchmark.github.io/；accessed：2026-11-07；source_type：官网可读历史榜；非2026新实验；ranking_note：沿网页显示顺序；Rosalind Starcoder的Pass@1低于其后CodeGen，页面可能按不同K排序，本页不冒称按Pass@1重排

来源：[5]

### 覆盖边界

官网Python/Java/Rosalind三轨分别转录Summary Only及完整Pass@1/5/10/20，沿其显示序号，不自行把Pass@20排序冒称Pass@1排序。网站模型行标签是2023模型日期，并未证实逐行测量日；分数仍是历史榜。论文表4/5及混淆消融为其他协议，不与此合并。

来源：[5][7]

## 9. 联系方式

### 公开作者工作邮箱

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 公开反馈

https://github.com/gersteinlab/BioCoder/issues

来源：[8]

### 官方账号

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 隐私信息

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 10. 原始文件

### 原文PDF

https://arxiv.org/pdf/2308.16458

来源：[1]

### 下载源文件SHA-256

c10e1ca00454f617439153c6646eb406ea01ffc3bf14fef420a6968223858b1e

来源：[7]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

1569722

来源：[7]

### 既有文件夹

来源：[1]

### 其他材料

来源：[9]

### 既有 PDF链接

来源：[1]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- 2026-11-07（）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[1]

### 来源索引

[1]: https://arxiv.org/abs/2308.16458 "访问 2026-11-07"
[2]: https://raw.githubusercontent.com/gersteinlab/BioCoder/main/README.md "访问 2026-11-07"
[3]: https://arxiv.org/html/2610.21074v1 "访问 2026-11-07"
[4]: https://huggingface.co/datasets/lilbillbiscuit/biocoder_public/raw/main/README.md "访问 2026-11-07"
[5]: https://biocoder-benchmark.github.io/ "访问 2026-11-07"
[6]: https://huggingface.co/datasets/lilbillbiscuit/biocoder_public "访问 2026-11-07"
[7]: https://arxiv.org/pdf/2308.16458 "访问 2026-11-07"
[8]: https://github.com/gersteinlab/BioCoder "访问 2026-11-07"
[9]: "访问 2026-11-07"
