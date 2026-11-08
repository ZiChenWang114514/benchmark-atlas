# AtomBench

> 核查：2026-11-07（，）。本页是有来源的研究快照，不把采集日当作实验日；待核实不等于未公开。

逐条实证复核：论文PDF、官方发布材料与分协议榜单；未证实项继续保留

## 1. 基本信息

### 简称

AtomBench

来源：[1]

### 全称

AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors

来源：[1]

### 数据/软件版本

软件包atombench 0.1.0（当前pyproject.toml）；论文v2及底层数据源版本独立记录。

来源：[2][1]

### 论文版本

v2；最近论文日期 2026-07-07

来源：[1]

### 发布日期

2025-10-18 03:07:37（，；arXiv v1首次提交；非推定软件上架日）

来源：[1]

### 主板块

材料

来源：[3]

说明：编辑分类沿用入选清单；不代表该基准只测本板块。

### 学科标签

晶体结构生成与重构

来源：[3]

### 许可证与范围

软件：MIT；底层数据许可另核实。

来源：[4]

### 论文入口

https://arxiv.org/abs/2510.16165

来源：[1]

### 论文标题

AtomBench: A Benchmarking Framework for Generative Crystal Reconstruction Models in Conventional Superconductors

来源：[1]

### 官方代码

https://github.com/atomgptlab/atombench

来源：[4]

### 数据入口

https://doi.org/10.6084/m9.figshare.6815699；https://doi.org/10.6084/m9.figshare.31045597

来源：[5]

说明：原论文Data Availability明确列出的底层数据DOI；与软件仓库地址分开。

### 官方主页

https://atomgptlab.github.io/atombench/

来源：[4][6]

## 2. 发起与维护

### 发起团队

West Virginia University与Johns Hopkins University署名团队。

来源：[1]

### 署名/合作机构

West Virginia University；Johns Hopkins University

来源：[5]

说明：论文作者单位；作者贡献节明确KC提出项目、CC与KC开发并计算、AHR/KC/CC共同分析。

### 作者

Charles Rhys Campbell；Aldo H. Romero；Kamal Choudhary

来源：[1]

### 维护入口

atomgptlab/atombench官方仓库。

来源：[1]

### 资助与计算资源

ACCESS分配DMR140031（Bridges2/Expanse），NSF 2138259/2138286/2138307/2137603/2138296；WVU Dolly Sods部分获NSF OAC-2117575支持；西弗吉尼亚高教政策委员会Research Challenge Grant 2022，RCG23-007；AtomGPTLab集群计算支持。

来源：[5]

## 3. 设计目标

这是给定条件下重构已知晶体的评测框架，而不是无条件发现超导体的成功率。配方、配方+Tc与全结构latent所含目标信息不同；必须先按条件分组，再比较误差。
来源：[1][1]

### 测量能力

给定晶体相关信息后的重构保真度，量化晶格/原子坐标及匹配覆盖。

来源：[1]

### 为何需要这个基准

生成器获得条件信息不等，单看匹配成功样本RMSD会掩盖失败；强调全样本ccRMSD。

来源：[1]

## 4. 构建方式

### 材料来源

JARVIS Supercon-3D与Alexandria DS-A/B超导体结构数据。

来源：[1]

### 命题/编制背景

凝聚态物理、材料生成模型与计算材料研究者。

来源：[1]

### 审核流程

固定目标结构、训练/测试与模型条件组；用统一结构匹配器计算重构指标。

来源：[1]

### 质量控制

CSV保留目标与预测CIF/POSCAR，统一结构匹配与连续纠正误差。

来源：[1]

### 去污染与证据边界

作者用 CIF 文本哈希检查分区不重叠和唯一性；这是作者报告，不等价于全面结构近重复审计。

来源：[1]

## 5. 数据形式

### 规模与分母

JARVIS Supercon-3D 1,058结构/Tc对；Alexandria DS-A/B 8,253对；示范研究四模型、两数据集及可选Tc条件，共12个训练实例。

来源：[1]

### 题型

条件晶体重构；不是无条件从零发现新晶体。

来源：[1]

### 模态与字段

原子晶体结构；CSV含id、target、prediction，后两列为POSCAR字符串（论文也描述CIF）。

来源：[4][1]

### 语言

结构与数值格式，Python工具。

来源：[1]

### 难度定位

依给定条件信息和目标结构而变，无固定自然语言难度分档。

来源：[1]

### 公开、隐藏与划分

每个数据集固定同一10%测试集；需验证集的模型80/10/10，不需验证集的模型90/10；固定种子123；不做交叉验证。

来源：[1]

## 6. 评测方法

### 指标

晶格参数KLD与MAE、匹配率、匹配结构平均RMSD，以及覆盖所有测试结构的ccRMSD（AMD k=100）；不能把匹配子集RMSD当全测试集误差。

来源：[1]

### 评分流程

结构匹配器处理对称性/容差；ccRMSD对每个测试结构定义，避免只报成功者。

来源：[1]

### 运行与提示

不是统一LLM提示；AtomGPT、CDVAE、FlowMM、MatterGen需按条件可见信息分组。

来源：[1]

### 评测实现

https://github.com/atomgptlab/atombench

来源：[1]

### 不能混比的设置

这是晶体重建而非 de novo 生成评测；CDVAE可见全结构潜表示，其他模型只见组成或组成+Tc，跨条件分数不能归因为架构优劣。

来源：[1]

## 7. 最新情况

### 核查日期

2026-11-07（，；采集日，不是实验日）

来源：[1]

### 当前发布

软件包0.1.0；论文v2基准使用JARVIS Supercon-3D与Alexandria DS-A/B。数据集独立语义版本编号仍待核实；不以软件版本替代结构数据版本。

来源：[2][5]

状态：待核实（本字段尚有未能确认的部分）。

### 版本脉络

v1：2025-10-18；v2：2026-07-07；change_boundary：v2标题/协议强调generative crystal reconstruction；ccRMSD不等于旧网页单晶格参数RMSE。

来源：[1][5]

### 分数上限与饱和度

不同条件/指标下优胜模型不同，不宜统一宣布饱和。

来源：[1]

### 争议与局限

当前论文v2明确重构而非de novo生成；旧官网AtomGenBench名称与新版AtomBench指标不同；保留版本边界。

来源：[1][3]

### 衍生版本

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

## 8. 榜单快照

### 采集日期

2026-11-07（，；采集日，不是实验日）

来源：[1]

### 官方入口

https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/

来源：[7]

### 第三方/补充实验

待核实

来源：[1]

说明：已核查原始论文/官方入口，但此字段未得到充分证据；不代表确定未公开。

状态：待核实（本字段尚有未能确认的部分）。

### 分轨成绩

#### 论文v2表2：Alexandria / composition

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | MatterGen | 0.238 | ccRMSD (Å), lower is better |
| 2 | AtomGPT | 0.5224 | ccRMSD (Å), lower is better |
| 3 | FlowMM | 1.3998 | ccRMSD (Å), lower is better |

- MatterGen：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition；k：100；source_type：论文固定实验
- AtomGPT：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition；k：100；source_type：论文固定实验
- FlowMM：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition；k：100；source_type：论文固定实验

#### 论文v2表2：Alexandria / composition+Tc

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | MatterGen Tc | 0.244 | ccRMSD (Å), lower is better |
| 2 | AtomGPT Tc | 0.5228 | ccRMSD (Å), lower is better |

- MatterGen Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition+Tc；k：100；source_type：论文固定实验
- AtomGPT Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：composition+Tc；k：100；source_type：论文固定实验

#### 论文v2表2：Alexandria / full-structure latent

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | CDVAE | 1.2218 | ccRMSD (Å), lower is better |

- CDVAE：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：Alexandria；conditioning：full-structure latent；k：100；source_type：论文固定实验

#### 论文v2表2：JARVIS / composition

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | MatterGen | 0.4854 | ccRMSD (Å), lower is better |
| 2 | AtomGPT | 0.8262 | ccRMSD (Å), lower is better |
| 3 | FlowMM | 1.5392 | ccRMSD (Å), lower is better |

- MatterGen：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition；k：100；source_type：论文固定实验
- AtomGPT：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition；k：100；source_type：论文固定实验
- FlowMM：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition；k：100；source_type：论文固定实验

#### 论文v2表2：JARVIS / composition+Tc

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | MatterGen Tc | 0.4988 | ccRMSD (Å), lower is better |
| 2 | AtomGPT Tc | 0.7665 | ccRMSD (Å), lower is better |

- MatterGen Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition+Tc；k：100；source_type：论文固定实验
- AtomGPT Tc：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：composition+Tc；k：100；source_type：论文固定实验

#### 论文v2表2：JARVIS / full-structure latent

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | CDVAE | 1.1555 | ccRMSD (Å), lower is better |

- CDVAE：source_url：https://arxiv.org/pdf/2510.16165；accessed：2026-11-07；dataset：JARVIS；conditioning：full-structure latent；k：100；source_type：论文固定实验

#### JARVIS官网旧alex_supercon_Tc_a：晶格参数a

| 来源次序/轨内序号 | 模型/系统 | 分数 | 指标 |
|---|---|---:|---|
| 1 | cdvae_invatoms | 0.3137 | lattice-a RMSE, lower is better |
| 2 | atomgpt_invatoms | 0.4821 | lattice-a RMSE, lower is better |
| 3 | flowmm_invatoms | 1.003 | lattice-a RMSE, lower is better |

- cdvae_invatoms：source_url：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/；accessed：2026-11-07；submitted_date：2025-10-17（来源仅给日期）；source_type：官方网页提交榜；各模型条件不同，不当作严格同条件竞赛
- atomgpt_invatoms：source_url：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/；accessed：2026-11-07；submitted_date：2025-10-17（来源仅给日期）；source_type：官方网页提交榜；各模型条件不同，不当作严格同条件竞赛
- flowmm_invatoms：source_url：https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/；accessed：2026-11-07；submitted_date：2025-10-17（来源仅给日期）；source_type：官方网页提交榜；各模型条件不同，不当作严格同条件竞赛

来源：[5][7]

### 覆盖边界

论文ccRMSD按两数据集×三条件独立分轨；旧官方网页仅比较晶格参数a的RMSE，不能把0.3137/0.4821/1.003混入论文ccRMSD。网页8253是数据总量，不自行推定测试分母。

来源：[5][7]

## 9. 联系方式

### 公开作者工作邮箱

crhysc@gmail.com；alromero@mail.wvu.edu；kchoudh2@jhu.edu

来源：[1]

### 公开反馈

https://github.com/atomgptlab/atombench/issues

来源：[4]

说明：官方公开仓库的问题反馈入口；未发送消息。

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

https://arxiv.org/pdf/2510.16165

来源：[1]

### 下载源文件SHA-256

cf0464f374b215992e91190f1bc398d1dbb01af8199cb2fcb7b4fdb0ae39dcf6

来源：[5]

说明：实际下载的源站PDF字节校验；未声称重新核验文件内容。

### 下载源文件字节数

5917762

来源：[5]

### 既有文件夹

id：1AGppe7PfAY02bOHYn6m1h1RjoUZ2h3ON；webViewLink：

来源：[1]

### 其他材料

- type：中文介绍；id：1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY；webViewLink：https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit

来源：[8]

### 既有 PDF链接

id：11zXVL6xA5D2JNgNvaptGg3rlfXdkUOo0；webViewLink：

来源：[1]

> 没有上传或改写文件。以上SHA-256和字节数针对实际下载的源站PDF，不等于重新核验既有文件。

## 11. 变更记录

- 2026-11-07：首次深度核查：官方存在性、2026H2证据、构建与评测、历史/当前榜单边界、原始材料和中文介绍。
- 2026-11-07：：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。
- 2026-11-07（ ()）：实际读取论文摘要和PDF全文、官方README/可取得的LICENSE、关联HF卡与榜单；补充真实来源，分开版本/条件/输出协议；重写11节中文介绍。未上传，未重跑评测。

来源：[1]

### 来源索引

[1]: https://arxiv.org/abs/2510.16165 "访问 2026-11-07"
[2]: https://raw.githubusercontent.com/atomgptlab/atombench/main/pyproject.toml "访问 2026-11-07"
[3]: https://arxiv.org/html/2609.19487v1 "访问 2026-11-07"
[4]: https://raw.githubusercontent.com/atomgptlab/atombench/main/README.md "访问 2026-11-07"
[5]: https://arxiv.org/pdf/2510.16165 "访问 2026-11-07"
[6]: https://atomgptlab.github.io/atombench/ "访问 2026-11-07"
[7]: https://atomgptlab.github.io/jarvis_leaderboard/AI/AtomGen/alex_supercon_Tc_a/ "访问 2026-11-07"
[8]: https://docs.google.com/document/d/1iim04Q6mKRDhhX9bcGgw3QA14VmKrh9YKaX_-mSjcsY/edit "访问 2026-11-07"
