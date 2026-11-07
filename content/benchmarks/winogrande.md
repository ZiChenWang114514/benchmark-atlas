# WinoGrande｜中文深度介绍

核验日期：2026-11-07（Asia/Seoul）。事实按所列来源理解；未核实项不作推断。

评估依靠常识与语境解决代词/指代消歧，而不是只利用词汇关联。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

## 一、基本信息

### 简称

WinoGrande

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 全称

WinoGrande

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 数据/协议版本

1.1（官方仓库README）

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（采集 2026-11-07）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 发布日期

2019-07-25（Asia/Seoul；arXiv初稿日期，非独立数据集首发声明）

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 板块

推理

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）。

### 子领域

- 常识指代推理

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 许可证

- **代码许可**：Apache-2.0
- **数据许可**：CC-BY（README未注明具体小版本）

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（采集 2026-11-07）。

### 论文

https://arxiv.org/abs/1907.10641

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 代码

https://github.com/allenai/winogrande

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）。

### 数据集

https://github.com/allenai/winogrande

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）；[2](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 官网

http://winogrande.allenai.org

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）；[2](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 论文题名

WinoGrande: An Adversarial Winograd Schema Challenge at Scale

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

## 二、发起与维护

### 发起机构

Allen Institute for AI、University of Washington

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 正式合作方

待核实

核验说明：仅确认论文署名机构，不将所有署名单位自动认定为正式合作方

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 作者

- Sakaguchi, Keisuke
- Bras, Ronan Le
- Bhagavatula, Chandra
- Choi, Yejin

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 当前维护

待核实

核验说明：组织/仓库归属已核实，当前责任维护人和活跃维护状态未确认

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 资助

待核实

核验说明：未逐项核实论文致谢及当前运营资助；机构归属不等于资金来源

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

## 三、设计目标

### 测量能力

评估依靠常识与语境解决代词/指代消歧，而不是只利用词汇关联。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 设计缺口

原始Winograd Schema题量小且可能受表面数据偏差影响，需要规模更大并经对抗去偏的集合。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

## 四、构建方式

### 题源

众包人员以WikiHow词语为锚点编写语义相近但答案不同的成对句子，再经AFLite过滤。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 出题/标注人员

众包写题及独立验证；研究者设计AFLite和收集约束。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 审核

每题由多名人员验证；AFLite使用表示和简单分类器识别可由偏差猜中的样本。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 质量控制

3名人类验证者与自动去偏相结合；提供不同训练规模以衡量数据效率。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 去污染边界

AFLite针对集合内部可学习偏差，不是现代LLM训练语料去重。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

## 五、数据形式

### 题量

全量43972：训练40938、开发1267、测试1767；论文去偏子集12282（9248/1267/1767），须区分。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 题型

一个含空白的句子和2个填入选项。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 模态

文本（数学符号按文本表达）；并非原始图像视频识别任务

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 语言

英语题面；形式化/数学符号另见模态与仓库格式

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 难度

常识指代消歧；XS/S/M/L/XL是训练规模而不是难度等级。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 公开/隐藏划分

train有xs/s/m/l/xl五种规模及独立标签，dev含标签，test不公开标签；预测文件每行五列，依次对应五种训练规模。

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（采集 2026-11-07）。

## 六、评测方法

### 指标

准确率；原评测还观察随训练规模变化的学习曲线。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 评分实现

输出1或2，与答案比对；官方提交可带5个训练规模的预测列。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 提示与预算

原论文为监督微调；现代zero/few-shot生成评测并不等同官方学习曲线设置。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 评测脚本

官方README指示使用eval.py评估dev，输出metrics.json；test应向官方榜提交predictions.lst。

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（采集 2026-11-07）。

### 可比性警示

debiased与XL训练集合、dev与test、单点准确率与学习曲线必须区分。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 七、最新情况

### 核对日期

2026-11-07（Asia/Seoul）

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 最新可确认数据/协议

1.1（README所列版本；未以此推断近期开源活动或最新提交）

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（采集 2026-11-07）。

### 修订与2026H2收录证据

- **论文版本**：arXiv v2
- **历史说明**：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。
- **2026下半年引用/使用证据**：
  - 
    - **来源链接**：https://arxiv.org/html/2610.11978v1
    - **日期**：2026-10-08
    - **说明**：Jev 研究表1–2及§3.1实际在 WinoGrande 上比较多类模型，不将ARC-Easy或其它子集另计。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 饱和判断

待核实

核验说明：是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 污染、争议与版本冲突

公开开发集、模板及词汇均可能被训练吸收；去偏不等于无污染。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）；[2](http://winogrande.allenai.org)（采集 2026-11-07）。

### 衍生与排除项

从Winograd Schema扩展而来；不是WSC273或所有Winograd数据的同义词。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）；[2](http://winogrande.allenai.org)（采集 2026-11-07）。

## 八、榜单快照

### 榜单采集日

2026-11-07（Asia/Seoul；采集日不是测量日）

来源：[1](https://leaderboard.allenai.org/winogrande/submissions/public)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 官方榜

https://leaderboard.allenai.org/winogrande/submissions/public

来源：[1](https://github.com/allenai/winogrande)（采集 2026-11-07）；[2](https://leaderboard.allenai.org/winogrande/submissions/public)（采集 2026-11-07）。

### 二级机构榜

待核实

核验说明：未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 限定范围的分数快照

- 
  - **模型版本**：Gemini 3.8 Flash
  - **分数**：97.1
  - **单位**：%
  - **范围与协议**：Jev表2；checkpoint日期未列明
  - **结果日期**：2026-10-08
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2610.11978v1
  - **来源等级**：研究论文实验，非官方实时榜
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：Qwen3.8 Flash
  - **分数**：94.4
  - **单位**：%
  - **范围与协议**：Jev表2；模型展示名
  - **结果日期**：2026-10-08
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2610.11978v1
  - **来源等级**：研究论文实验，非官方实时榜
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。
- 
  - **模型版本**：Claude Opus 5.5
  - **分数**：92.7
  - **单位**：%
  - **范围与协议**：Jev表2；模型展示名
  - **结果日期**：2026-10-08
  - **采集日期**：2026-11-07
  - **来源链接**：https://arxiv.org/html/2610.11978v1
  - **来源等级**：研究论文实验，非官方实时榜
  - **检查点说明**：模型名按来源原样；若来源未列API checkpoint则不补造。

来源：[1](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

### 覆盖边界

非穷尽、非跨协议排名。仅转录本轮打开来源的所列行；未列模型不表示低于所列模型。结果日期不明保留待核实，展示名不是API检查点。

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）；[2](https://arxiv.org/html/2610.11978v1)（采集 2026-11-07）。

## 九、联系方式

### 公开工作邮箱

- keisukes@allenai.org

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）；[2](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### Issues

https://github.com/allenai/winogrande/issues

来源：[1](https://github.com/allenai/winogrande)（采集 2026-11-07）。

### 官方社交

待核实

核验说明：未核实专门官方社交账号，不收录同名个人账户

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### 隐私政策

待核实

核验说明：未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

## 十、原始文件

### Drive论文PDF

- **id**：1HV-a7K9n4KtUYj0_j7_ry31g8fKGvFKp
- **webViewLink**：https://drive.google.com/file/d/1HV-a7K9n4KtUYj0_j7_ry31g8fKGvFKp/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1HV-a7K9n4KtUYj0_j7_ry31g8fKGvFKp/view?usp=drivesdk)（采集 2026-11-07）。

### 原始论文PDF

https://arxiv.org/pdf/1907.10641

来源：[1](https://arxiv.org/abs/1907.10641)（采集 2026-11-07）。

### SHA256校验值

780b26e4c9dd38c61f2f9e7b99a3e3dfec94fd19bb13bc06338770ca3733e67a

来源：[1](https://arxiv.org/pdf/1907.10641)（采集 2026-11-07）。

### PDF字节数

1098857

来源：[1](https://arxiv.org/pdf/1907.10641)（采集 2026-11-07）。

### Drive文件夹

- **id**：1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4
- **webViewLink**：https://drive.google.com/drive/folders/1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4

来源：[1](https://drive.google.com/drive/folders/1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4)（采集 2026-11-07）。

### 其他文档

- **chinese_intro_doc**：
  - **id**：1fxdzZYj0eXBh8jA5teDOzJcqpTc9o9X5-rF2NfnHFjg
  - **webViewLink**：https://docs.google.com/document/d/1fxdzZYj0eXBh8jA5teDOzJcqpTc9o9X5-rF2NfnHFjg/edit?usp=drivesdk
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/winogrande.md

来源：[1](https://drive.google.com/drive/folders/1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4)（采集 2026-11-07）。

## 十一、变更记录

- 
  - **日期**：2026-11-07
  - **时区**：Asia/Seoul
  - **变更内容**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- 
  - **日期**：2026-11-07
  - **时区**：Asia/Seoul
  - **变更内容**：第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
  - **本轮更新字段**：
    - basic_info.version
    - latest_status.latest_dataset_version
    - evaluation.official_scripts
    - data_format.public_hidden_split

来源：[1](http://winogrande.allenai.org)（采集 2026-11-07）。
