# WinoGrande

> 第2轮深度复核：2026-11-08（KST / Asia/Seoul）。采集日不等于榜单更新日；未取得的新证据不覆盖旧来源日期。

WinoGrande通过众包成对句子与AFLite降低词汇捷径，但“去偏”并不等于已排除现代模型训练污染。必须区分全量训练、去偏开发/测试、五种监督训练规模和现代零/少样本测试。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

## 基本信息

### 简称

WinoGrande

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 全称

WinoGrande

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 基准版本

1.1（官方仓库README）

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 论文版本

arXiv v2

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 发布日期

- **paper_first_submission_kst**：2019-07-25T03:11:59+09:00
- **date_type**：论文首次提交，不等同数据集首次上线

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 主板块

推理

来源：[1](http://winogrande.allenai.org)（访问 2026-11-07 KST）。

### 领域标签

- 常识指代推理

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 许可证

- **code**：Apache-2.0
- **dataset**：CC-BY（README未注明具体小版本）

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 论文

https://arxiv.org/abs/1907.10641

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 官方代码

https://github.com/allenai/winogrande

来源：[1](http://winogrande.allenai.org)（访问 2026-11-07 KST）。

### 数据地址

https://github.com/allenai/winogrande

来源：[1](http://winogrande.allenai.org)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 官方入口

http://winogrande.allenai.org

来源：[1](http://winogrande.allenai.org)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 论文标题

WinoGrande: An Adversarial Winograd Schema Challenge at Scale

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

## 发起与维护

### 发起机构

Allen Institute for AI、University of Washington

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 署名合作机构

- Allen Institute for Artificial Intelligence
- University of Washington

> 作者机构：全体作者署名AI2，Yejin Choi同时署名UW；不推断额外商业伙伴。

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）。

### 作者

- Sakaguchi, Keisuke
- Bras, Ronan Le
- Bhagavatula, Chandra
- Choi, Yejin

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 维护方

官方代码allenai/winogrande、数据分发与问答由AI2团队提供；README指定GitHub Issues及WinoGrande Google Group，公开联系人Keisuke Sakaguchi。

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）；[2](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）。

### 资助

NSF IIS-1524371、IIS-1714566；DARPA CwC经ARO W911NF-15-1-0543；DARPA MCS经NIWC Pacific N66001-19-2-4031。

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）。

## 设计目标

### 衡量能力

评估依靠常识与语境解决代词/指代消歧，而不是只利用词汇关联。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 设计背景

原始Winograd Schema题量小且可能受表面数据偏差影响，需要规模更大并经对抗去偏的集合。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

## 构建方式

### 题目与数据来源

众包人员以WikiHow词语为锚点编写语义相近但答案不同的成对句子，再经AFLite过滤。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 构建者背景

众包写题及独立验证；研究者设计AFLite和收集约束。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 审核流程

每题由多名人员验证；AFLite使用表示和简单分类器识别可由偏差猜中的样本。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 质量控制

3名人类验证者与自动去偏相结合；提供不同训练规模以衡量数据效率。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 去污染与泄漏防范

AFLite针对集合内部可学习偏差，不是现代LLM训练语料去重。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

## 数据形式

### 规模

全量43,972题：train_xl 40,938、validation 1,267、test 1,767；debiased train 9,248（与同一dev/test合计12,282）。训练规模XS/S/M/L/XL分别160/640/2,558/10,234/40,938，HF分别列config，不相加。

来源：[1](https://huggingface.co/datasets/allenai/winogrande/raw/main/README.md)（访问 2026-11-08 KST）；[2](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）。

### 任务形式

一个含空白的句子和2个填入选项。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 模态

纯文本：带空白的英语句子、两个候选名词短语及1/2答案；不是数学题，也不含图像/视频。

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）；[2](https://huggingface.co/datasets/allenai/winogrande/raw/main/README.md)（访问 2026-11-08 KST）。

### 语言

英语；官方HF数据卡language: en。

来源：[1](https://huggingface.co/datasets/allenai/winogrande/raw/main/README.md)（访问 2026-11-08 KST）。

### 难度与类型

常识指代消歧；XS/S/M/L/XL是训练规模而不是难度等级。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 公开与隐藏划分

train有xs/s/m/l/xl五种规模及独立标签，dev含标签，test不公开标签；预测文件每行五列，依次对应五种训练规模。

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

## 评测方法

### 指标

准确率；官方挑战同时要求XS/S/M/L/XL五列预测以考察数据效率/学习曲线。现代零/少样本validation准确率与官方五训练规模test协议不是同一赛道。

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）；[2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 评分

输出1或2，与答案比对；官方提交可带5个训练规模的预测列。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 提示和复现设置

原论文为监督微调；现代zero/few-shot生成评测并不等同官方学习曲线设置。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 官方脚本

官方README指示使用eval.py评估dev，输出metrics.json；test应向官方榜提交predictions.lst。

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 可比性提示

debiased与XL训练集合、dev与test、单点准确率与学习曲线必须区分。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07 KST）。

## 最新情况

### 本轮核验时间

2026-11-08 KST / Asia/Seoul

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 数据版本与当前状态

1.1（README所列版本；未以此推断近期开源活动或最新提交）

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 论文修订与H2证据

- **arxiv_version**：arXiv v2
- **history_note**：完整历史请见arXiv元数据；初稿日期已转Asia/Seoul，不将论文修订日混为数据版本。
- **2026_h2_evidence**：- - **url**：https://arxiv.org/html/2610.11978v1
    - **date**：2026-10-08
    - **note**：Jev 研究表1–2及§3.1实际在 WinoGrande 上比较多类模型，不将ARC-Easy或其它子集另计。
- **revisions**：- - **version**：v1
    - **date_kst**：2019-07-25T03:11:59+09:00
  - - **version**：v2
    - **date_kst**：2019-11-22T04:01:32+09:00
- **note**：论文修订时间已从arXiv的UTC转换为KST；不能当作数据发布日期。既有2026-H2证据保留原采集日期。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07 KST）。

### 饱和程度

待核实

> 是否饱和依赖具体split、工具和协议；下方分数仅为限定来源快照，不作整体饱和或SOTA判断

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07 KST）。

### 污染、冲突与限制

公开开发集、模板及词汇均可能被训练吸收；去偏不等于无污染。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](http://winogrande.allenai.org)（访问 2026-11-07 KST）。

### 后续工作与衍生

从Winograd Schema扩展而来；不是WSC273或所有Winograd数据的同义词。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](http://winogrande.allenai.org)（访问 2026-11-07 KST）。

## 榜单快照

### 快照采集日

2026-11-08 KST；只刷新论文历史表，官方实时榜失败

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）；[2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 官方榜单

https://leaderboard.allenai.org/winogrande/submissions/public

来源：[1](https://github.com/allenai/winogrande)（访问 2026-11-07 KST）；[2](https://leaderboard.allenai.org/winogrande/submissions/public)（访问 2026-11-07 KST）。

### 第三方覆盖

待核实

> 未确认AA/Epoch/LMArena有单独追踪该精确版本的可读榜；下列研究/厂商表仅补充，不冒充二级榜

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 结果快照

各轨分列；“—”表示来源未给统一名次。完整设置以相应JSON字段与来源为准。

#### 既有2026-H2研究实验（本轮未刷新）

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | Gemini 3.8 Flash | 97.1 % | accuracy Jev表2；checkpoint日期未列明 | 2026-10-08；https://arxiv.org/html/2610.11978v1 |
| — | Qwen3.8 Flash | 94.4 % | accuracy Jev表2；模型展示名 | 2026-10-08；https://arxiv.org/html/2610.11978v1 |
| — | Claude Opus 5.5 | 92.7 % | accuracy Jev表2；模型展示名 | 2026-10-08；https://arxiv.org/html/2610.11978v1 |

#### 原论文v2 Table 3/dev

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | WKH | 49.4 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | Ensemble LMs | 53.0 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | BERT | 65.8 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa | 79.3 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | BERT (local context) | 52.5 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa (local context) | 52.1 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | BERT-DPR (zero-shot) | 50.2 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa-DPR (zero-shot) | 59.4 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |
| — | Human | 94.1 % | accuracy WinoGrande_debiased dev | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 3/test

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | WKH | 49.6 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | Ensemble LMs | 50.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | BERT | 64.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa | 79.1 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | BERT (local context) | 51.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa (local context) | 50.0 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | BERT-DPR (zero-shot) | 51.0 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | RoBERTa-DPR (zero-shot) | 58.9 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |
| — | Human | 94.0 % | accuracy WinoGrande_debiased test | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/XS/dev

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 51.5 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/XS/test

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 50.4 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/S/dev

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 58.6 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/S/test

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 58.6 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/M/dev

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 66.9 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/M/test

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 67.6 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/L/dev

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 75.8 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/L/test

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 74.7 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/XL/dev

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 79.3 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

#### 原论文v2 Table 4/XL/test

|名次|模型|数值|指标/范围|设置与日期|
|---|---|---|---|---|
| — | RoBERTa | 79.1 % | accuracy  | https://arxiv.org/pdf/1907.10641 |

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）；[2](https://arxiv.org/html/2610.11978v1)（访问 2026-11-07 KST）。

### 覆盖说明

官方AI2榜本轮requests遇TLS EOF，WebFetch返回500；没有取得实时榜，不声称最新SOTA。原论文v2 Table3的9模型×dev/test及Table4五训练规模×dev/test均逐值恢复。既有2026-H2研究三行保留旧采集日，与官方test/学习曲线分开。

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）；[2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

## 联系方式

### 公开联系邮箱

- keisukes@allenai.org

来源：[1](http://winogrande.allenai.org)（访问 2026-11-07 KST）；[2](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### 问题反馈

https://github.com/allenai/winogrande/issues

来源：[1](https://github.com/allenai/winogrande)（访问 2026-11-07 KST）。

### 官方讨论渠道

https://groups.google.com/a/allenai.org/forum/#!forum/winogrande

> 官方README指定的问答Google Group；不是个人社交账号。

来源：[1](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。

### 隐私与数据使用

待核实

> 未核实benchmark专门隐私条款；许可证不能代替隐私政策

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

## 原始文件

### 源站论文PDF

https://arxiv.org/pdf/1907.10641

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）。

### SHA-256

780b26e4c9dd38c61f2f9e7b99a3e3dfec94fd19bb13bc06338770ca3733e67a

> 本轮重新下载的原始PDF字节；既有Drive副本未覆盖。

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）。

### 字节数

1098857

来源：[1](https://arxiv.org/pdf/1907.10641)（访问 2026-11-08 KST）。

### Drive文件夹

- **id**：1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4
- **webViewLink**：https://drive.google.com/drive/folders/1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4

来源：[1](https://drive.google.com/drive/folders/1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4)（访问 2026-11-07 KST）。

### 其他文档

- **chinese_intro_doc**：- **id**：1fxdzZYj0eXBh8jA5teDOzJcqpTc9o9X5-rF2NfnHFjg
  - **webViewLink**：https://docs.google.com/document/d/1fxdzZYj0eXBh8jA5teDOzJcqpTc9o9X5-rF2NfnHFjg/edit?usp=drivesdk
  - **mimeType**：application/vnd.google-apps.document
- **local_markdown**：content/benchmarks/winogrande.md

来源：[1](https://drive.google.com/drive/folders/1eg6WGLrTKFZ-aC8QNmtTIufy3rOCS5F4)（访问 2026-11-07 KST）。

### Drive原文归档

- **id**：1HV-a7K9n4KtUYj0_j7_ry31g8fKGvFKp
- **webViewLink**：https://drive.google.com/file/d/1HV-a7K9n4KtUYj0_j7_ry31g8fKGvFKp/view?usp=drivesdk

来源：[1](https://drive.google.com/file/d/1HV-a7K9n4KtUYj0_j7_ry31g8fKGvFKp/view?usp=drivesdk)（访问 2026-11-07 KST）。

## 变更记录

### 本页修订

- - **date**：2026-11-07
  - **timezone**：Asia/Seoul
  - **change**：核实官方身份，撰写11部分中文介绍；记录H2引用/实验、分协议榜单和来源冲突；PDF执行字节数及SHA256校验，AIME例外明确保留。
- - **date**：2026-11-07
  - **timezone**：Asia/Seoul
  - **change**：第1轮实证优化：核对官方数据卡/README/许可证与H2使用证据，补充可读官方榜单，明确数据和代码授权、划分及历史榜口径；未证实项保留。
  - **fields_updated**：- basic_info.version
    - latest_status.latest_dataset_version
    - evaluation.official_scripts
    - data_format.public_hidden_split
- - **date**：2026-11-08
  - **timezone**：Asia/Seoul
  - **round**：2
  - **change**：逐项打开arXiv摘要与PDF全文、官方README/LICENSE/数据卡及榜单；细化构建和评测协议，恢复分源结构化结果，未核实内容不填造。具体变更见research-q15/REPORT.md。

来源：[1](https://arxiv.org/abs/1907.10641)（访问 2026-11-08 KST）；[2](https://raw.githubusercontent.com/allenai/winogrande/master/README.md)（访问 2026-11-08 KST）。
