# MultiPL-E

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk)

## 基本信息

### 简称
MultiPL-E [来源1](https://github.com/nuprl/MultiPL-E)

### 全称
MultiPL-E [来源1](https://github.com/nuprl/MultiPL-E)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 论文版本
arXiv v4 [来源2](https://arxiv.org/abs/2208.08227)

> 论文修订版本不等同数据集版本。

### 发布日期
2022-08-17 20:16:52 KST [来源2](https://arxiv.org/abs/2208.08227)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
代码 [来源2](https://arxiv.org/abs/2208.08227)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "多语言代码生成"
]
```
 [来源2](https://arxiv.org/abs/2208.08227)

### 许可证
BSD 3-Clause + Machine Learning Restriction；仓库第4条明确禁止将内容用作任何机器学习模型训练数据。 [来源3](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE)

### 论文
https://arxiv.org/abs/2208.08227 [来源2](https://arxiv.org/abs/2208.08227)

### 官方代码
https://github.com/nuprl/MultiPL-E [来源1](https://github.com/nuprl/MultiPL-E)

### 数据地址
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 官方入口
https://github.com/nuprl/MultiPL-E [来源1](https://github.com/nuprl/MultiPL-E)

### 论文标题
MultiPL-E: A Scalable and Extensible Approach to Benchmarking Neural Code Generation [来源2](https://arxiv.org/abs/2208.08227)

## 发起与维护

### 机构与发起方
以 Northeastern University 等多校研究人员组成的作者团队为主；详见论文作者单位。 [来源2](https://arxiv.org/abs/2208.08227)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Cassano, Federico",
  "Gouwar, John",
  "Nguyen, Daniel",
  "Nguyen, Sydney",
  "Phipps-Costin, Luna",
  "Pinckney, Donald",
  "Yee, Ming-Ho",
  "Zi, Yangtian",
  "Anderson, Carolyn Jane",
  "Feldman, Molly Q",
  "Guha, Arjun",
  "Greenberg, Michael",
  "Jangda, Abhinav"
]
```
 [来源2](https://arxiv.org/abs/2208.08227)

### 当前维护方
nuprl / MultiPL-E 官方仓库团队 [来源2](https://arxiv.org/abs/2208.08227)

### 资助
论文致谢 NSF CCF-2052696 的部分支持。 [来源2](https://arxiv.org/abs/2208.08227)

## 设计目标

### 衡量能力
跨编程语言的函数级代码生成、编译与功能测试。 [来源2](https://arxiv.org/abs/2208.08227)

### 设计背景
只评 Python 难以判断语言模型在其他编程语言中的迁移能力；逐语言手工造题成本高。 [来源2](https://arxiv.org/abs/2208.08227)

## 构建方式

### 题目来源
将 Python HumanEval 和 MBPP 的签名、类型、文档及测试翻译为其他语言；不翻译参考实现函数体。 [来源2](https://arxiv.org/abs/2208.08227)

### 出题者背景
编程语言与程序合成研究人员。 [来源2](https://arxiv.org/abs/2208.08227)

### 审核流程
语言专用翻译器把规范与测试转成目标语言；以容器运行编译与测试。 [来源2](https://arxiv.org/abs/2208.08227)

### 质量控制
处理目标语言类型、标准库与运行时差异，保留语言特定排除项。 [来源2](https://arxiv.org/abs/2208.08227)

### 去污染
翻译不能保证去除 Python 原题污染；模型仍可能记忆语义或已公开译题。 [来源2](https://arxiv.org/abs/2208.08227)

## 数据形式

### 题量与规模
原论文：Python 加 18 种目标语言，共 19 种；MultiPL-HumanEval 3,059 个任务、MultiPL-MBPP 7,619 个任务，含语言特定排除。 [来源2](https://arxiv.org/abs/2208.08227)

### 题型
函数级程序补全与单元测试。 [来源2](https://arxiv.org/abs/2208.08227)

### 模态

```json
[
  "文本",
  "代码"
]
```
 [来源2](https://arxiv.org/abs/2208.08227)

### 语言
19 种编程语言（含原始 Python）；英语自然语言规范。 [来源2](https://arxiv.org/abs/2208.08227)

### 难度
继承 HumanEval 与 MBPP，不解释为 19 个独立 benchmark。 [来源2](https://arxiv.org/abs/2208.08227)

### 公开与隐藏划分
翻译器、提示、测试和执行框架公开；不同语言允许的题目并非完全相同。 [来源2](https://arxiv.org/abs/2208.08227)

## 评测方法

### 指标
执行测试的 pass@k。 [来源2](https://arxiv.org/abs/2208.08227)

### 评分
代码在目标语言容器内编译并运行；使用 pass@k 无偏估计。 [来源2](https://arxiv.org/abs/2208.08227)

### 提示与运行设置
原论文每题 200 个样本；pass@1 温度 0.2，pass@10/100 温度 0.8。 [来源2](https://arxiv.org/abs/2208.08227)

### 官方评测脚本
https://github.com/nuprl/MultiPL-E [来源1](https://github.com/nuprl/MultiPL-E)

### 可比性警示
语言集合、有效题目、温度和 k 都影响结果；8 语言报告不可冒称完整 19 语言总分。 [来源2](https://arxiv.org/abs/2208.08227)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/nuprl/MultiPL-E)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "待核实",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1/§4.2及表2–4实际报告 MultiPL-E；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。"
    }
  ]
}
```
 [来源4](https://arxiv.org/html/2609.27284v1)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Arjun Guha [ view email ] [v1] 2022-08-17 20:16:52 KST (1,172 KB) [v2] 2022-08-19 10:12:49 KST (1,172 KB) [v3] 2022-11-08 14:48:57 KST (1,172 KB) [v4] 2022-12-19 19:30:12 KST (1,780 KB) [来源2](https://arxiv.org/abs/2208.08227)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
当前仓库采用带禁止ML训练条款的BSD衍生许可；原论文datasheet提到母题MIT及许可证问答，不能据此把当前仓库写成MIT。以本次读取LICENSE界定仓库使用，母题来源权利仍单列。 [来源3](https://github.com/nuprl/MultiPL-E/blob/main/LICENSE) [来源2](https://arxiv.org/abs/2208.08227)

### 衍生与版本关系
MultiPL-HumanEval 与 MultiPL-MBPP 是 MultiPL-E 两个来源分支，不重复计数。 [来源2](https://arxiv.org/abs/2208.08227)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/nuprl/MultiPL-E)

### 官方榜单
https://github.com/nuprl/MultiPL-E [来源1](https://github.com/nuprl/MultiPL-E)

### 独立评测覆盖
待核实 [来源1](https://github.com/nuprl/MultiPL-E)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "Hunyuan-A13B base",
    "score": 69.33,
    "metric": "MultiPL-E (%)",
    "benchmark_version": "8语言子集；版本待核实",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST",
    "settings": "0-shot；Python/C++/Java/PHP/TypeScript/C#/Bash/JavaScript"
  }
]
```
 [来源4](https://arxiv.org/html/2609.27284v1)

### 覆盖与时效说明
下面仅列能从已打开来源核验的结果。历史论文基线、厂商自报与当前榜单分开，不构成跨设置综合排名。 [来源2](https://arxiv.org/abs/2208.08227)

## 联系方式

### 公开工作邮箱
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
https://github.com/nuprl/MultiPL-E/issues [来源1](https://github.com/nuprl/MultiPL-E)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2208.08227)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2208.08227 [来源5](https://arxiv.org/pdf/2208.08227)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
b905b9874ffcb4cee63f74cdc30524eae97013691e79313049ad72c6d6197580 [来源5](https://arxiv.org/pdf/2208.08227)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
443169
```
 [来源5](https://arxiv.org/pdf/2208.08227)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF",
  "webViewLink": "https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF"
}
```
 [来源6](https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM",
    "webViewLink": "https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk"
  }
]
```
 [来源1](https://github.com/nuprl/MultiPL-E) [来源7](https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ",
  "webViewLink": "https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk)

## 变更记录


```json
[
  {
    "date": "2026-11-07",
    "timezone": "KST / Asia/Seoul",
    "change": "首次建立中文条目；核实官方存在性、原论文与 H2 证据；不确定字段保留待核实。"
  }
]
```
 [来源1](https://github.com/nuprl/MultiPL-E)

## 来源

1. https://github.com/nuprl/MultiPL-E — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2208.08227 — 采集：2026-11-07 KST。
3. https://github.com/nuprl/MultiPL-E/blob/main/LICENSE — 采集：2026-11-07 KST。
4. https://arxiv.org/html/2609.27284v1 — 采集：2026-11-07 KST。
5. https://arxiv.org/pdf/2208.08227 — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1khgOwh78nDrW-SHYR5WFiy8QxpgBJVMF — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/1cJ2CHUDqpMhq8jz6w_gMky6AfkFohAGgYYayDoSpGlM/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1VJo6JR3mrGnJtUCicWx2ULogJB0i9DgZ/view?usp=drivesdk — 采集：2026-11-07 KST。
