# BAISBench

> 核查：2026-11-07（，）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

BAISBench

来源：[1]

### 全称

Biological AI Scientist Benchmark（BAISBench；仓库README仍称AISBench）

来源：[2][3][4]

### 数据/软件版本

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 论文版本

v2；最近论文日期 2026-01-18

来源：[1]

### 发布日期

2025-05-13 16:33:54（arXiv v1首次提交）

来源：[1]

### 主板块

生物与医学

来源：[5]

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 学科标签

组学数据驱动科学发现Agent

来源：[5]

### 许可证与范围

code：MIT（Copyright 2025 Erpai Luo）；hf_dataset_card：Apache-2.0；底层各研究h5ad许可须各自遵守

来源：[6][3]

### 论文入口

https://arxiv.org/abs/2505.08341

来源：[1]

### 论文标题

Benchmarking AI scientists for omics data driven biological discovery

来源：[1]

### 官方代码

https://github.com/EperLuo/BAISBench

来源：[1]

### 数据入口

https://huggingface.co/datasets/EperLuo/BaisBench

来源：[1]

### 官方主页

https://github.com/EperLuo/BAISBench

来源：[1]

## 2. 发起与维护

### 发起团队

清华大学生物信息团队牵头作者署名；含北京交通大学、首都医科大学研究者。按作者单位归属，不推断另有正式法律牵头协议。

来源：[2]

### 署名/合作机构

清华大学自动化系/BNRIST生物信息学团队；北京交通大学软件学院；首都医科大学基础医学院生理与病理生理系；清华大学合成与系统生物学中心

来源：[2]

说明：署名机构列表而非推定联合所有权。

### 作者

Luo, Erpai；Jia, Jinmeng；Xiong, Yifan；Li, Xiangyu；Guo, Xiaobo；Yu, Baoqi；Hao, Minsheng；Wei, Lei；Zhang, Xuegong

来源：[1]

### 维护入口

EperLuo/BAISBench与EperLuo/BaisBench数据账号。

来源：[1]

### 资助与计算资源

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 3. 设计目标

这是已发表生物研究的再发现与细胞注释诊断，不是衡量新发现原创性。官方Notebook藏有可精确抄录的保存输出，但Pantheon只算6器官，必须独立于15器官宏平均和193题科学发现分数。
来源：[1][1]

### 测量能力

从单细胞组学数据到细胞注释与研究结论重现，评估AI scientist。

来源：[1]

### 为何需要这个基准

一般问答/代码生成无法确认代理能在真实组学数据上重现生物发现。

来源：[1]

## 4. 构建方式

### 材料来源

公开单细胞研究与CellxGene h5ad；BAIS-SD来自41项研究的已发表结论。

来源：[1]

### 命题/编制背景

生物信息专家注释与研究生人类参考；六名生物信息研究生参与对比。

来源：[1]

### 审核流程

专家标注细胞类型层级；GPT-4o辅助从论文结论拟题，人工纠正和实验核查。

来源：[1]

### 质量控制

数据统一h5ad；用uHAF对齐细胞类型层级，精确或更细后代类型给全分。官方Task1提供映射与评分实现，Task2提供题目及reference answer。人工基线由6位研究生分担完成，不是每人独立全套重复。

来源：[2][7][8]

### 去污染与证据边界

来源研究及结论公开，主要是rediscovery而非真正未知发现；需警惕靠论文记忆作答。

来源：[1]

## 5. 数据形式

### 规模与分母

BAIS_DPTA：datasets：15；evidence：HF BAISBench_task1.csv逐行核对15个器官/组织数据集；附录S1排版列表并不作为删减分母的依据；BAIS_SD：questions：193；studies：41；metadata_note：HF卡56行对应元数据记录，不是全体问题数。

来源：[3][9][2]

### 题型

细胞类型注释、基于组学数据的单选/多选结论重现。

来源：[1]

### 模态与字段

h5ad表达矩阵、细胞元数据、代码与文字/选择答案。

来源：[1]

### 语言

英语研究问题与生物标识符；数据驱动。

来源：[1]

### 难度定位

真实研究数据分析；已发表结论重现不同于原创发现。

来源：[1]

### 公开、隐藏与划分

Task1/Task2 notebook及HF容器提供数据；Task2 README明确包含reference answer。隐藏测试设计仍待核实，不能称全部答案隐藏。

来源：[4]

## 6. 评测方法

### 指标

DPTA专家uHAF层级分；SD按单选/多选正确性计分。

来源：[1]

### 评分流程

DPTA：与参考类型相同或为其后代给1，父类0.5、祖父类0.2；代码排除参考Unclassified细胞，逐器官算分后取宏平均。SD：单选正确1，多选全对1、仅部分正确且无错0.5；否则0。uHAF名称映射过程也会影响复现。

来源：[2][7][8]

### 运行与提示

五个AI scientist系统对比，六名研究生参考；系统工具与模型配置需随分数保留。

来源：[1]

### 评测实现

Task1.ipynb下载并评测数据处理/细胞注释；Task2.ipynb提供研究背景、选择题及参考答案，论文提示可按被测AI scientist调整。

来源：[4]

### 不能混比的设置

Task1保存输出中Pantheon只运行organ_list[:6]，其均分0.4207667294406579不得混入15器官总榜或据此否定论文叙述STELLA领先。Task2目前只见Biomni精确保存输出；论文图中其他柱高不作读图估算。DPTA的0–1宏平均与SD的百分制不混比。

来源：[7][8][2]

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

v1：2025-05-13；v2：2026-01-18；scope：两任务官方发布与复现Notebook；引用不代表他人重新运行。

来源：[1][4]

### 分数上限与饱和度

论文与Notebook都显示细胞注释仍有明显差距；已核实的15器官STELLA保存均分0.39986219727575084，SD保存Biomni=136/193。它们是公开历史复现输出，不是最新全模型实时上限。

来源：[7][8][2]

### 争议与局限

仓库AISBench与论文/HF BAISBench命名并存；科学发现是恢复已发表研究结论，不直接量化新颖发现；Task2明确公开reference answer，需防止只记忆答案。HF task1 CSV证实15个数据集。Notebook的Pantheon仅6器官，不能按15器官总榜排序。

来源：[4][9][7][8][2]

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

https://github.com/EperLuo/BAISBench；https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task2.ipynb

来源：[4][7][8]

### 第三方/补充实验

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### 官方Task1.ipynb保存输出：DPTA，15器官

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | STELLA | 0.39986219727575084 | hierarchical annotation macro score (0–1) |
| 2 | Human with GPT-4o | 0.3477723428012859 | hierarchical annotation macro score (0–1) |
| 3 | Biomni | 0.2437880291331723 | hierarchical annotation macro score (0–1) |
| 4 | scChat | 0.15367114184342404 | hierarchical annotation macro score (0–1) |
| 5 | AutoBA | 0.0 | hierarchical annotation macro score (0–1) |

- STELLA：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：官方复现notebook既有输出；未重跑；n_organs：15
- Human with GPT-4o：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：官方复现notebook既有输出；未重跑；n_organs：15
- Biomni：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：官方复现notebook既有输出；未重跑；n_organs：15
- scChat：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：官方复现notebook既有输出；未重跑；n_organs：15
- AutoBA：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：官方复现notebook既有输出；未重跑；n_organs：15

#### 官方Task1.ipynb保存输出：DPTA，仅前6器官

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Pantheon | 0.4207667294406579 | hierarchical annotation macro score (0–1) |

- Pantheon：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb；accessed：2026-11-07；source_type：部分器官复现输出；不构成全量排名；n_organs：6

#### 官方Task2.ipynb保存输出：SD，193题

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | Biomni | 70.46632124352331 | 100 point scale |

- Biomni：source_url：https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task2.ipynb；accessed：2026-11-07；source_type：官方复现notebook保存输出；非实时榜；total_score：136.0；questions：193

来源：[7][8]

### 覆盖边界

实际读取两个官方Notebook保存输出，不估算论文图柱。DPTA15器官、Pantheon6器官、SD193题三轨分开；rank只在本页已转录同轨条目内排序，不能称项目完整实时排名。Notebook未注明每次运行日期，采集日不是实验日。论文其他系统精确数值仍待核实。

来源：[7][8][2]

## 9. 联系方式

### 公开作者工作邮箱

zhangxg@tsinghua.edu.cn

来源：[1]

### 公开反馈

https://github.com/EperLuo/BAISBench/issues

来源：[10]

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

https://arxiv.org/pdf/2505.08341

来源：[1]

### 下载源文件SHA-256

72b6410e415b16c9de82f8bab63ba68978a3ecc735231b2b20ddaa5f7378ebc8

来源：[2]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

2666576

来源：[2]

### 既有文件夹

来源：[1]

### 其他材料

来源：[11]

### 既有 PDF链接

来源：[1]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：深度优化：打开官方README/数据卡/论文补实字段，区分公开与隐藏划分、论文历史实验与实时排名；未知仍明确保留。
- 2026-11-07（）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[1]

### 来源索引

[1]: https://arxiv.org/abs/2505.08341 "访问 2026-11-07"
[2]: https://arxiv.org/pdf/2505.08341 "访问 2026-11-07"
[3]: https://huggingface.co/datasets/EperLuo/BaisBench "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/README.md "访问 2026-11-07"
[5]: https://arxiv.org/html/2610.21074v1 "访问 2026-11-07"
[6]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/LICENSE "访问 2026-11-07"
[7]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task1.ipynb "访问 2026-11-07"
[8]: https://raw.githubusercontent.com/EperLuo/BAISBench/main/Task2.ipynb "访问 2026-11-07"
[9]: https://huggingface.co/datasets/EperLuo/BaisBench/resolve/main/BAISBench_task1.csv "访问 2026-11-07"
[10]: https://github.com/EperLuo/BAISBench "访问 2026-11-07"
[11]: "访问 2026-11-07"
