# MedScribe

> 核验日期：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；未知不等于未公开。热度与成绩快照分开记录。

编辑状态：官方存在性已核验；字段级研究快照；note: trending: B

## 基本信息

### 简称

MedScribe

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 全称

MedScribe

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 基准版本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 论文版本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 发布日期

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 主板块

生物与医学

> Benchmark Atlas 编辑分类。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 领域标签

- 临床文书

> 编辑标签；空列表表示尚未补充细分标签。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 许可证

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 论文入口

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 官方代码

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 数据地址

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 官方入口

https://www.vals.ai/benchmarks/medscribe

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 论文标题

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 发起与维护

### 发起机构

Vals AI

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 合作方

Protege（去标识化SOAP笔记合作方）

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 作者

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 维护方

Vals AI

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 资助

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 设计目标

### 衡量能力

将临床问诊转录组织成准确、合规SOAP文书，减轻行政记录负担。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 设计背景

不以医学考试正确率替代真实临床文书质量比较。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 构建方式

### 题目来源

使用Protege真实去标识SOAP笔记，改编NoteChat生成合成医患对话。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 出题者背景

medical scribes与physician assistant参与专家验证。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 审核流程

专家先建SOAP结构模板、独立标注rubric，再共同解决冲突。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 质量控制

对合成转录做专家真实性感知对照；裁判提示经180 checks人类对齐研究调整，最终与人类多数意见80.5%一致。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 去污染

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 数据形式

### 题量与规模

100套评分rubric；不把100直接假定为独立病人数。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 题型

输入医患对话转录，输出Subjective、Objective、Assessment、Plan四段SOAP笔记。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 模态

- 文本对话
- 文本SOAP笔记

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 语言

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 难度

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 公开与隐藏划分

公开方法与示例；完整数据获取及公开/隐藏比例待核实。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 评测方法

### 指标

Accuracy（rubric checks通过情况）；分SOAP类别与子类别分析。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 评分方式

根据专家金标准rubric评估SOAP笔记，模型裁判提示经人类一致性校准；裁判具体版本待核实。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 提示与运行设置

所有模型temperature 1、最大30k输出tokens，统一专家模板。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 官方评测脚本

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 可比性警示

不是语音识别或临床诊断安全性指标；格式及SOAP节归属会影响裁判，与人类偏好并非完全一致。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 最新情况

### 为什么近期热门

热度B：本轮近期热度主要由单一评测机构持续运行/展示支持，不表示行业广泛采纳。

- Vals榜更新，109模型，临床行政文书任务。 [来源](https://www.vals.ai/benchmarks/medscribe)（证据日期 2026-10-29；访问 2026-11-07）

### 核验日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 当前版本与2026H2使用证据

- **version**：待核实
- **heat_confidence**：B
- **evidence_2026_h2**：[{"url": "https://www.vals.ai/benchmarks/medscribe", "date": "2026-10-29", "date_type": "source_calendar_date", "note": "Vals榜更新，109模型，临床行政文书任务。"}]

> 热度B：本轮近期热度主要由单一评测机构持续运行/展示支持，不表示行业广泛采纳。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 修订历史

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 饱和情况

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 污染与争议

合成转录由真实去标识笔记派生；真实性研究不等价于实际临床部署验证；正文关于80段转录和10真实样例的不同研究口径不合并。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 衍生与版本关系

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 榜单快照

### 快照日期

2026-11-07 KST / Asia/Seoul

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 官方榜单入口

https://www.vals.ai/benchmarks/medscribe

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 第三方评测入口

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 核验结果

- {"rank": 1, "model": "Claude Opus 5.5", "score": 91.43, "metric": "Accuracy %", "source_url": "https://www.vals.ai/benchmarks/medscribe", "source_date": "2026-10-29", "collected_at": "2026-11-07 KST"}
- {"rank": 2, "model": "Claude Fable 5.1", "score": 91.29, "metric": "Accuracy %", "source_url": "https://www.vals.ai/benchmarks/medscribe", "source_date": "2026-10-29", "collected_at": "2026-11-07 KST"}
- {"rank": 3, "model": "Claude Sonnet 5.5", "score": 91.1, "metric": "Accuracy %", "source_url": "https://www.vals.ai/benchmarks/medscribe", "source_date": "2026-10-29", "collected_at": "2026-11-07 KST"}

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 覆盖与时效说明

Vals当前单一机构持续评测；109模型为榜单行数而不是题量。两条Vals目录/详情URL不表示两家独立采纳。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 联系方式

### 公开工作邮箱

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 公开反馈渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 官方社交渠道

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 隐私政策

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

## 原始文件

### 源站论文PDF

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 原始PDF SHA-256

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 原始PDF字节数

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### Drive资料目录

待核实

> 本轮已打开所列材料，但该字段尚未精确核实；不表示官方没有公开。

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### 其他官方材料

- {"type": "官方方法/介绍网页（不是论文PDF）", "url": "https://www.vals.ai/benchmarks/medscribe"}

[来源1](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）

### Drive PDF归档

待核实

> 本组只建立本地研究文件，不上传或声明已有Drive PDF。

## 变更记录

- {"date": "2026-11-07", "timezone": "KST / Asia/Seoul", "change": "新建近期热门中文研究条目；区分当前榜单与历史结果；缺项逐字段标记。"}

[来源](https://www.vals.ai/benchmarks/medscribe)（访问 2026-11-07）
