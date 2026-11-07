# AtomBench

> 第1轮实证核查 · 2026-11-07（KST）。正文与权威 JSON 同步；访问时间不是来源发表时间。未知保留，不以旧论文结果冒充最新总榜。

## 1. 基本信息

- **名称**：AtomBench （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **全称**：AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **版本**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **论文版本**：v2；最近论文日期 2026-07-07 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **发布日期**：2025-10-17（首个arXiv版本日期；非推定数据上线日） （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **板块**：材料 编辑分类沿用入选清单；不代表该基准只测本板块。 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **子领域**：晶体结构生成与重构 （[来源1](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **许可**：软件：MIT；底层数据许可另核实。 （[来源1](https://raw.githubusercontent.com/atomgptlab/atombench/main/README.md)；访问：2026-11-07）

- **论文**：https://arxiv.org/abs/2510.16165 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **代码**：https://github.com/atomgptlab/atombench （[来源1](https://raw.githubusercontent.com/atomgptlab/atombench/main/README.md)；访问：2026-11-07）

- **数据**：https://github.com/atomgptlab/atombench （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **官方主页**：https://atomgptlab.github.io/jarvis_leaderboard/Special/AtomGenBench/ （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **论文标题**：AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 2. 发起与维护

- **发起机构**：West Virginia University与Johns Hopkins University署名团队。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **合作机构**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **作者**：Charles Rhys Campbell；Aldo H. Romero；Kamal Choudhary （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **维护方**：atomgptlab/atombench官方仓库。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **资助方**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 3. 设计目标

- **能力目标**：给定晶体相关信息后的重构保真度，量化晶格/原子坐标及匹配覆盖。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **设计动机**：生成器获得条件信息不等，单看匹配成功样本RMSD会掩盖失败；强调全样本ccRMSD。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 4. 构建方式

- **数据来源**：JARVIS Supercon-3D与Alexandria DS-A/B超导体结构数据。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **评审背景**：凝聚态物理、材料生成模型与计算材料研究者。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **审核流程**：固定目标结构、训练/测试与模型条件组；用统一结构匹配器计算重构指标。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **质量控制**：CSV保留目标与预测CIF/POSCAR，统一结构匹配与连续纠正误差。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **去污染**：作者用 CIF 文本哈希检查分区不重叠和唯一性；这是作者报告，不等价于全面结构近重复审计。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 5. 数据形式

- **规模**：JARVIS Supercon-3D 1,058结构/Tc对；Alexandria DS-A/B 8,253对；示范研究四模型、两数据集及可选Tc条件，共12个训练实例。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **任务形式**：条件晶体重构；不是无条件从零发现新晶体。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **模态**：原子晶体结构；CSV含id、target、prediction，后两列为POSCAR字符串（论文也描述CIF）。 （[来源1](https://raw.githubusercontent.com/atomgptlab/atombench/main/README.md) [来源2](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **语言**：结构与数值格式，Python工具。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **难度**：依给定条件信息和目标结构而变，无固定自然语言难度分档。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **公开与隐藏划分**：每个数据集固定同一10%测试集；需验证集的模型80/10/10，不需验证集的模型90/10；固定种子123；不做交叉验证。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 6. 评测方法

- **指标**：晶格参数KLD与MAE、匹配率、匹配结构平均RMSD，以及覆盖所有测试结构的ccRMSD（AMD k=100）；不能把匹配子集RMSD当全测试集误差。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **评分方式**：结构匹配器处理对称性/容差；ccRMSD对每个测试结构定义，避免只报成功者。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **提示设置**：不是统一LLM提示；AtomGPT、CDVAE、FlowMM、MatterGen需按条件可见信息分组。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **评测脚本**：https://github.com/atomgptlab/atombench （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **可比性提示**：这是晶体重建而非 de novo 生成评测；CDVAE可见全结构潜表示，其他模型只见组成或组成+Tc，跨条件分数不能归因为架构优劣。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 7. 最新情况

- **核查日期**：2026-11-07 Asia/Seoul （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **最新版本**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **修订与2026H2证据**：2026H2 独立使用证据：ALIGNN 2.0（2026-09-16）第2.4节和表8使用 AtomBench 方法，比较 ALIGNN-CSP、AtomGPT、MatterGen、CDVAE、FlowMM。 （[来源1](https://arxiv.org/abs/2609.19487)；访问：2026-11-07）

- **饱和度**：不同条件/指标下优胜模型不同，不宜统一宣布饱和。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **已知问题**：当前论文v2明确重构而非de novo生成；旧官网AtomGenBench名称与新版AtomBench指标不同；保留版本边界。 （[来源1](https://arxiv.org/abs/2510.16165) [来源2](https://arxiv.org/html/2609.19487v1)；访问：2026-11-07）

- **后继资源**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 8. 榜单快照

- **采集日期**：2026-11-07 Asia/Seoul（网页采集日，不等于模型实验日期） （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **官方榜单**：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/ （[来源1](https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/)；访问：2026-11-07）

- **第三方榜单**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **结果**：原论文表2，Alexandria、组成条件、ccRMSD（Å，越低越好）：MatterGen 0.2380、AtomGPT 0.5224、FlowMM 1.3998；CDVAE 1.2218但属于全结构潜表示条件，应单列。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **口径说明**：2026-11-07 读取原论文表2固定实验，不冒称实时榜；论文当前版本更新日期待核实。各条件、数据集及匹配/非匹配指标必须分开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 9. 联系方式

- **公开邮箱**：crhysc@gmail.com；alromero@mail.wvu.edu；kchoudh2@jhu.edu （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **问题反馈**：https://github.com/atomgptlab/atombench/issues 官方公开仓库的问题反馈入口；未发送消息。 （[来源1](https://raw.githubusercontent.com/atomgptlab/atombench/main/README.md)；访问：2026-11-07）

- **官方社交**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **隐私原则**：待核实 本轮已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 10. 原始文件

- **PDF来源**：https://arxiv.org/pdf/2510.16165 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **SHA256**：cf0464f374b215992e91190f1bc398d1dbb01af8199cb2fcb7b4fdb0ae39dcf6 （[来源1](https://arxiv.org/pdf/2510.16165)；访问：2026-11-07）

- **PDF字节**：5917762 （[来源1](https://arxiv.org/pdf/2510.16165)；访问：2026-11-07）

- **Drive文件夹**：id：1AGppe7PfAY02bOHYn6m1h1RjoUZ2h3ON；webViewLink：https://drive.google.com/drive/folders/1AGppe7PfAY02bOHYn6m1h1RjoUZ2h3ON （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

- **其他文档**：type：中文介绍 Google Doc；id：1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY；webViewLink：https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit （[来源1](https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit)；访问：2026-11-07）

- **Drive PDF**：id：11zXVL6xA5D2JNgNvaptGg3rlfXdkUOo0；webViewLink：https://drive.google.com/file/d/11zXVL6xA5D2JNgNvaptGg3rlfXdkUOo0/view （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）

## 11. 变更记录

date：2026-11-07；timezone：Asia/Seoul；change：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。 （[来源1](https://arxiv.org/abs/2510.16165)；访问：2026-11-07）
