# WeatherBench

> 第1轮实证核查 · 2026-11-07（KST）。正文与权威 JSON 同步；访问时间不是来源发表时间。未知保留，不以旧论文结果冒充最新总榜。

## 1. 基本信息

- **名称**：WeatherBench （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **全称**：WeatherBench 使用官方名称；未有已核实全称扩展时保留原名，不把论文标题误当基准全称。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **版本**：待核实 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **论文版本**：arXiv v3 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **发布日期**：2020/02/02 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **板块**：地球与天文 Benchmark Atlas 编辑归档；跨学科条目只在主板块计数，另用标签导航。 （[来源1](https://arxiv.org/abs/2002.00469)；访问：2026-11-07）

- **子领域**：气象科学 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **许可**：代码：MIT（Copyright 2019 Stephan Rasp）；ERA5 派生数据条款需单独核实。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/LICENSE)；访问：2026-11-07）

- **论文**：https://arxiv.org/abs/2002.00469 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **代码**：https://github.com/pangeo-data/WeatherBench （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **数据**：https://github.com/pangeo-data/WeatherBench （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **官方主页**：https://github.com/pangeo-data/WeatherBench （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **论文标题**：WeatherBench: A benchmark dataset for data-driven weather forecasting （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

## 2. 发起与维护

- **发起机构**：慕尼黑工业大学、ECMWF、斯德哥尔摩大学、华盛顿大学、多伦多大学 主要依据论文作者单位/官方团队介绍；不据此推断法律所有权或唯一发起方。文本已明确标注未核实的正式发起关系。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **合作机构**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **作者**：Rasp, Stephan；Dueben, Peter D.；Scher, Sebastian；Weyn, Jonathan A.；Mouatadid, Soukayna；Thuerey, Nils （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **维护方**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **资助方**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

## 3. 设计目标

- **能力目标**：统一数据驱动中期全球天气预报的数据与评测标准。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **设计动机**：统一数据驱动中期全球天气预报的数据与评测标准。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

## 4. 构建方式

- **数据来源**：ERA5 再分析月度归档经下载及重网格处理；IFS 基线来自 TIGGE；另提供 MPI-ESM-HR CMIP 历史模拟。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **评审背景**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **审核流程**：从 ERA5 再分析资料加工数据，并提供线性、深度学习和物理模型基线。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **质量控制**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **去污染**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

## 5. 数据形式

- **规模**：三种网格分辨率 1.40625°、2.8125°、5.625°；5.625° 整套下载约175G（README 标法）。不把存储容量当样本数量。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **任务形式**：全球天气时空场；具体分辨率、变量和划分须按版本核实。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **模态**：数值气象时空场（不是自然语言选择题）；预测采用 NetCDF，维度 init_time、lead_time、lat、lon。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **语言**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **难度**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **公开与隐藏划分**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

## 6. 评测方法

- **指标**：Z500 RMSE（m²/s²）、T850 RMSE（K），报告3天及5天预报；需对齐网格、初值和时效。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **评分方式**：统一天气预报指标，促进模型间可比性；参数细则待核实。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **提示设置**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **评测脚本**：https://github.com/pangeo-data/WeatherBench/blob/master/src/score.py （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **可比性提示**：不同数据版本、子集、提示、工具权限及模型快照不得直接混比；历史论文分数不代表当前SOTA。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

## 7. 最新情况

- **核查日期**：2026-11-07 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **最新版本**：旧版数据已调整垂直层：现为 50、100、150、200、250、300、400、500、600、700、850、925、1000 hPa；另加入 MPI-ESM-HR 历史模拟派生数据。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **修订与2026H2证据**：2026H2 引用证据：Spatial Generalization Tests for Machine Learning-based Weather Models to Assess Physical Consistency（arXiv:2607.20716v1）在引言引用 WeatherBench/Rasp et al. (2020)。该文参考文献作者与 DOI 元信息存在可疑不一致，保留题名与引用上下文，不沿用其作者表。 （[来源1](https://arxiv.org/html/2607.20716v1)；访问：2026-11-07）

- **饱和度**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **已知问题**：待核实 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **后继资源**：官方仓库推荐转向 WeatherBench 2：更新后的数据更全面，访问更方便。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

## 8. 榜单快照

- **采集日期**：2026-11-07 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **官方榜单**：https://github.com/pangeo-data/WeatherBench#leaderboard （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **第三方榜单**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **结果**：官方旧版表：Operational IFS：Z500 154/334、T850 1.36/2.03；Rasp and Thuerey 2020：268/499、1.65/2.41；IFS T63：268/463、1.85/2.52。每对数字依次为3/5天。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **口径说明**：2026-11-07 读取旧版基线表，榜单更新时间待核实；含物理模式与不同分辨率模型，不称为当前统一 SOTA 排名。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

## 9. 联系方式

- **公开邮箱**：stephan.rasp@tum.de （[来源1](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **问题反馈**：https://github.com/pangeo-data/WeatherBench/issues 官方公开仓库的问题反馈入口；未发送消息。 （[来源1](https://raw.githubusercontent.com/pangeo-data/WeatherBench/master/README.md)；访问：2026-11-07）

- **官方社交**：待核实 本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **隐私原则**：只使用论文、官方站点或仓库公开联系方式；不收集私人渠道。 （[来源1](urn:benchmark-atlas:constitution:v0.1)；访问：2026-11-07）

## 10. 原始文件

- **PDF来源**：https://arxiv.org/pdf/2002.00469 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **SHA256**：7d60b0fe08c470ee3e7c1985003837a6f21b8b692ae5b0604652da8c642677e4 本次下载原始字节的SHA-256；未压缩、未修改。 （[来源1](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **PDF字节**：5734556 （[来源1](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）

- **Drive文件夹**：id：1DrGzbkVTidm6O_FvSVbTgui8CwOFi0DH；webViewLink：https://drive.google.com/drive/folders/1DrGzbkVTidm6O_FvSVbTgui8CwOFi0DH （[来源1](https://drive.google.com/drive/folders/1DrGzbkVTidm6O_FvSVbTgui8CwOFi0DH)；访问：2026-11-07）

- **其他文档**：kind：中文介绍 Google Doc；id：1G4dF_ZzXwwKENT_Pq7fZ83060HU-Ha5MByRN08KmnYw；webViewLink：https://docs.google.com/document/d/1G4dF_ZzXwwKENT_Pq7fZ83060HU-Ha5MByRN08KmnYw/edit?usp=drivesdk （[来源1](https://docs.google.com/document/d/1G4dF_ZzXwwKENT_Pq7fZ83060HU-Ha5MByRN08KmnYw/edit?usp=drivesdk)；访问：2026-11-07）

- **Drive PDF**：id：1CoA6xcHxeaeDVqAhG5_Mw5oLdP-K8kGp；webViewLink：https://drive.google.com/file/d/1CoA6xcHxeaeDVqAhG5_Mw5oLdP-K8kGp/view?usp=drivesdk （[来源1](https://drive.google.com/file/d/1CoA6xcHxeaeDVqAhG5_Mw5oLdP-K8kGp/view?usp=drivesdk)；访问：2026-11-07）

## 11. 变更记录

date：2026-11-07；timezone：Asia/Seoul；change：首批官方材料核验、中文改写、PDF原件入Drive；未核实字段显式标记。；date：2026-11-07；timezone：Asia/Seoul；change：第1轮：核对官方README、许可、评测与分任务分数；补2026H2使用证据，区分论文固定实验和实时榜，保留官方标签冲突。 （[来源1](https://arxiv.org/abs/2002.00469) [来源2](https://arxiv.org/pdf/2002.00469)；访问：2026-11-07）
