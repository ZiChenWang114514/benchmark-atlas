# QMOF

> 第1轮实证核查 · 2026-11-07（KST）。正文与权威 JSON 同步；访问时间不是来源发表时间。未知保留，不以旧论文结果冒充最新总榜。

## 1. 基本信息

- **名称**：QMOF （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **全称**：Quantum MOF (QMOF) Database （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **版本**：官方updates.md最新列出 Figshare v18（加入初步 QMOF Thermo Database）；仓库版本日志不等于本次已核实Figshare全部最新发布。 （[来源1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)；访问：2026-11-07）

- **论文版本**：Matter 4,1578–1597 (2021)；20k+版同时引用2022 npj Computational Materials扩展论文。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **发布日期**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **板块**：材料 编辑分类沿用入选清单；不代表该基准只测本板块。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **子领域**：金属有机框架带隙预测 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **许可**：数据库数据：CC BY 4.0；须适当署名并注明修改。 （[来源1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)；访问：2026-11-07）

- **论文**：https://doi.org/10.1016/j.matt.2021.02.015 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **代码**：https://github.com/Andrew-S-Rosen/QMOF （[来源1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)；访问：2026-11-07）

- **数据**：https://doi.org/10.6084/m9.figshare.13147324 （[来源1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)；访问：2026-11-07）

- **官方主页**：https://github.com/Andrew-S-Rosen/QMOF （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **论文标题**：Machine learning the quantum-chemical properties of metal–organic frameworks for accelerated materials discovery （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

## 2. 发起与维护

- **发起机构**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **合作机构**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **作者**：Andrew S. Rosen；Shaelyn M. Iyer；Debmalya Ray；Zhenpeng Yao；Alán Aspuru-Guzik；Laura Gagliardi；Justin M. Notestein；Randall Q. Snurr （[来源1](https://www.osti.gov/pages/biblio/1774653)；访问：2026-11-07）

- **维护方**：Andrew-S-Rosen/QMOF；Materials Project MOF Explorer为数据浏览入口。 （[来源1](https://github.com/Andrew-S-Rosen/QMOF) [来源2](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

- **资助方**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

## 3. 设计目标

- **能力目标**：从MOF结构预测量子化学性质，本文收录的明确评测任务为固定划分的带隙回归，而非把数据库当统一Agent基准。 （[来源1](https://github.com/Andrew-S-Rosen/QMOF) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **设计动机**：大规模MOF电子结构DFT成本高，需图模型代理进行材料筛选；不同DFT泛函应分开评估。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

## 4. 构建方式

- **数据来源**：实验MOF/配位聚合物结构经高通量周期DFT计算产生性质标签；无自然语言命题。 （[来源1](https://github.com/Andrew-S-Rosen/QMOF) [来源2](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

- **评审背景**：量子化学、MOF、DFT及图神经网络研究者合作；2022作者机构含Berkeley/LBNL、Northwestern、ORNL、Minnesota。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

- **审核流程**：统一DFT工作流、结构及电子态分析；不是专家逐题审阅考试题。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

- **质量控制**：v9使用pymatgen StructureMatcher移除重复结构并修正186个EDIFF设置；v12移除带错误键合/缺氢问题的部分结构。属于版本化清理，不代表数据无误。 （[来源1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)；访问：2026-11-07）

- **去污染**：H2固定train/val/test评估预测误差；结构重叠与多保真泄漏需单独审计。2022多保真允许同结构不同泛函跨划分，不同于结构外推。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

## 5. 数据形式

- **规模**：官方当前概述20,000+结构；H2固定带隙任务16,340训练、2,042验证、2,042测试。初版规模与后续数据库版不同，不能混用。 （[来源1](https://github.com/Andrew-S-Rosen/QMOF) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **任务形式**：结构→带隙连续值回归；数据库也含其他量子化学性质，但未逐属性拆成独立条目。 （[来源1](https://github.com/Andrew-S-Rosen/QMOF) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **模态**：MOF/配位聚合物原子结构及周期DFT量化学性质；官方FAQ明确不提供轨迹。 （[来源1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)；访问：2026-11-07）

- **语言**：数值及结构数据；英语说明，无自然语言考试语言。 （[来源1](https://github.com/Andrew-S-Rosen/QMOF)；访问：2026-11-07）

- **难度**：电子开壳层过渡金属与不同泛函的带隙差异较难；并无统一题目难度标签。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

- **公开与隐藏划分**：数据公开；H2 16340/2042/2042固定划分，2022原论文则80/5/15随机划分，两种协议不同。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

## 6. 评测方法

- **指标**：带隙MAE，单位eV，越低越好；报告对应DFT层级。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **评分方式**：对测试结构预测带隙与DFT参考值计算绝对误差平均。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **提示设置**：非LLM提示；H2 ALIGNN2.0与原ALIGNN比较需固定结构划分及训练设置。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **评测脚本**：https://github.com/Andrew-S-Rosen/QMOF （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **可比性提示**：QMOF是数据库+下游协议，不存在由数据库名唯一决定的全局榜。PBE带隙不等于实验光学带隙；不同结构/泛函划分不可混排。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

## 7. 最新情况

- **核查日期**：2026-11-07 Asia/Seoul （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **最新版本**：仓库更新日志列至v18；v15—v17各移除一个结构，v18加入初步热力学数据库。发布日期待核实。 （[来源1](https://raw.githubusercontent.com/arosen93/QMOF/main/updates.md)；访问：2026-11-07）

- **修订与2026H2证据**：2026H2 使用证据：ALIGNN 2.0（2026-09-16）表2报告QMOF带隙任务，16,340训练/2042验证/2042测试，ALIGNN 2.0与原ALIGNN的MAE均0.202 eV。 （[来源1](https://arxiv.org/abs/2609.19487)；访问：2026-11-07）

- **饱和度**：H2同协议MAE未改善不代表所有MOF电子性质饱和，也不证明结构外推已解决。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **已知问题**：源结构重复、训练/测试划分与DFT系统误差会影响材料泛化结论；2021原始论文PDF本轮公开站点下载受阻，Drive未以替代论文冒充。 （[来源1](https://www.nature.com/articles/s41524-022-00796-6) [来源2](https://github.com/Andrew-S-Rosen/QMOF)；访问：2026-11-07）

- **后继资源**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

## 8. 榜单快照

- **采集日期**：2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期） （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **官方榜单**：待核实 （[来源1](https://github.com/Andrew-S-Rosen/QMOF)；访问：2026-11-07）

- **第三方榜单**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **结果**：可核实的近期研究对比（非实时官方总榜）：ALIGNN 2.0 与原 ALIGNN，QMOF带隙 MAE 均0.202 eV；同一16,340/2042/2042划分，论文表2。 （[来源1](https://arxiv.org/abs/2609.19487)；访问：2026-11-07）

- **口径说明**：2026-11-07 读取2026-09-16模型论文；这是开发团队自报对比，不代表QMOF数据库维护方官方排名；实时榜前列待核实。 （[来源1](https://arxiv.org/abs/2609.19487)；访问：2026-11-07）

## 9. 联系方式

- **公开邮箱**：rosen@u.northwestern.edu （[来源1](https://www.nature.com/articles/s41524-022-00796-6)；访问：2026-11-07）

- **问题反馈**：https://github.com/Andrew-S-Rosen/QMOF/issues 官方公开仓库的问题反馈入口；未发送消息。 （[来源1](https://raw.githubusercontent.com/Andrew-S-Rosen/QMOF/main/README.md)；访问：2026-11-07）

- **官方社交**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **隐私原则**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

## 10. 原始文件

- **PDF来源**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **SHA256**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **PDF字节**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **Drive文件夹**：id：16710civVuRQy4imv33HqI4LGvAE8rIGF；webViewLink：https://drive.google.com/drive/folders/16710civVuRQy4imv33HqI4LGvAE8rIGF （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

- **其他文档**：type：中文介绍 Google Doc；id：16w8iieykbWu2_oUxwzSuqlAGEVLfYBHs-ssbWCx-igA；webViewLink：https://docs.google.com/document/d/16w8iieykbWu2_oUxwzSuqlAGEVLfYBHs-ssbWCx-igA/edit （[来源1](https://docs.google.com/document/d/16w8iieykbWu2_oUxwzSuqlAGEVLfYBHs-ssbWCx-igA/edit)；访问：2026-11-07）

- **Drive PDF**：待核实 原始2021论文PDF的公开下载入口本轮被站点拦截；未用别篇论文冒充。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）

## 11. 变更记录

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。 （[来源1](https://doi.org/10.1016/j.matt.2021.02.015)；访问：2026-11-07）
