# MBPP

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P/view?usp=drivesdk)

## 基本信息

### 简称
MBPP [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

### 全称
Mostly Basic Programming Problems [来源2](https://arxiv.org/abs/2108.07732)

### 基准版本
原始 974 题；sanitized 子集需单独注明 [来源2](https://arxiv.org/abs/2108.07732)

### 论文版本
arXiv v1 [来源2](https://arxiv.org/abs/2108.07732)

> 论文修订版本不等同数据集版本。

### 发布日期
2021-08-16 12:57:30 KST [来源2](https://arxiv.org/abs/2108.07732)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
代码 [来源2](https://arxiv.org/abs/2108.07732)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "Python基础编程"
]
```
 [来源2](https://arxiv.org/abs/2108.07732)

### 许可证
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 论文
https://arxiv.org/abs/2108.07732 [来源2](https://arxiv.org/abs/2108.07732)

### 官方代码
https://github.com/google-research/google-research/tree/master/mbpp [来源2](https://arxiv.org/abs/2108.07732)

### 数据地址
https://github.com/google-research/google-research/tree/master/mbpp [来源2](https://arxiv.org/abs/2108.07732)

### 官方入口
https://github.com/google-research/google-research/tree/master/mbpp [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

### 论文标题
Program Synthesis with Large Language Models [来源2](https://arxiv.org/abs/2108.07732)

## 发起与维护

### 机构与发起方
Google Research；部分作者在 MIT 或以实习身份参与。 [来源2](https://arxiv.org/abs/2108.07732)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Austin, Jacob",
  "Odena, Augustus",
  "Nye, Maxwell",
  "Bosma, Maarten",
  "Michalewski, Henryk",
  "Dohan, David",
  "Jiang, Ellen",
  "Cai, Carrie",
  "Terry, Michael",
  "Le, Quoc",
  "Sutton, Charles"
]
```
 [来源2](https://arxiv.org/abs/2108.07732)

### 当前维护方
Google Research 官方 mbpp 数据目录 [来源2](https://arxiv.org/abs/2108.07732)

### 资助
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 设计目标

### 衡量能力
从简短自然语言要求生成基础 Python 程序，并使用执行结果检验功能。 [来源2](https://arxiv.org/abs/2108.07732)

### 设计背景
研究不同规模预训练模型的程序合成、提示与微调表现，需要多样且可执行的入门任务。 [来源2](https://arxiv.org/abs/2108.07732)

## 构建方式

### 题目来源
众包任务；每题有文字说明、Python 参考代码和 3 个断言测试。 [来源2](https://arxiv.org/abs/2108.07732)

### 出题者背景
具备基础 Python 的内部众包工作者，可使用互联网资源。 [来源2](https://arxiv.org/abs/2108.07732)

### 审核流程
研究团队对一部分任务做人工校订，改进描述、签名和测试。 [来源2](https://arxiv.org/abs/2108.07732)

### 质量控制
原论文报告人工校订 426 题；后续托管 sanitized 常见 427 题，不能假定完全相同快照。 [来源2](https://arxiv.org/abs/2108.07732)

### 去污染
原论文核查 974 题中 32 题与预训练样本有超过一半代码行匹配；这是当时模型的重叠检查，不是今天的清洁证明。 [来源2](https://arxiv.org/abs/2108.07732)

## 数据形式

### 题量与规模
974 道原始题；原论文 split 为 test 500、fine-tuning 374、few-shot 10、validation 90。 [来源2](https://arxiv.org/abs/2108.07732)

### 题型
文本到 Python 函数，附断言测试和参考程序。 [来源2](https://arxiv.org/abs/2108.07732)

### 模态

```json
[
  "文本",
  "代码"
]
```
 [来源2](https://arxiv.org/abs/2108.07732)

### 语言
Python（原论文执行环境 Python 3.6）；英语任务。 [来源2](https://arxiv.org/abs/2108.07732)

### 难度
面向基础编程；不是竞赛或仓库级软件工程。 [来源2](https://arxiv.org/abs/2108.07732)

### 公开与隐藏划分
上述划分是研究用途 split；原始文件公开，不等于隐藏评测题。 [来源2](https://arxiv.org/abs/2108.07732)

## 评测方法

### 指标
功能正确率；必须区分逐样本通过比例与多样本中至少一次解出。 [来源2](https://arxiv.org/abs/2108.07732)

### 评分
运行生成程序并检查断言；原始测试少，不能代替 MBPP+ 加强测试。 [来源2](https://arxiv.org/abs/2108.07732)

### 提示与运行设置
原论文常用 80 个样本、温度 0.5；少样本示例配置需一并报告。 [来源2](https://arxiv.org/abs/2108.07732)

### 官方评测脚本
https://github.com/google-research/google-research/tree/master/mbpp [来源2](https://arxiv.org/abs/2108.07732)

### 可比性警示
原始 974、test 500、sanitized 427、EvalPlus 评测 399 的分母不同；不可横向混排。 [来源2](https://arxiv.org/abs/2108.07732)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始 974 题；sanitized 子集需单独注明",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.27284v1",
      "date": "2026-09-23",
      "note": "Hunyuan-A13B §4.1/§4.2及表2–4实际报告 MBPP；CRUX-I/O作为同一个CRUXEval条目，不拆分计数。"
    }
  ]
}
```
 [来源3](https://arxiv.org/html/2609.27284v1) [来源2](https://arxiv.org/abs/2108.07732)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Augustus Odena [ view email ] [v1] 2021-08-16 12:57:30 KST (2,247 KB) [来源2](https://arxiv.org/abs/2108.07732)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
公开且被广泛使用的基础题库存在训练重叠风险；原始少量测试有漏检错误的局限。 [来源2](https://arxiv.org/abs/2108.07732)

### 衍生与版本关系
MBPP sanitized、MBPP+ 为子集/增强派生，不替换原始 MBPP 定义。 [来源2](https://arxiv.org/abs/2108.07732)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

### 官方榜单
https://github.com/google-research/google-research/tree/master/mbpp [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

### 独立评测覆盖
待核实 [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "Hunyuan-A13B base",
    "score": 83.86,
    "metric": "MBPP (%)",
    "benchmark_version": "split/版本待核实",
    "result_type": "厂商技术报告自报",
    "source_date": "2026-09-23",
    "collected_at": "2026-11-07 KST",
    "settings": "3-shot"
  }
]
```
 [来源3](https://arxiv.org/html/2609.27284v1)

### 覆盖与时效说明
下面仅列能从已打开来源核验的结果。历史论文基线、厂商自报与当前榜单分开，不构成跨设置综合排名。 [来源2](https://arxiv.org/abs/2108.07732)

## 联系方式

### 公开工作邮箱
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 公开反馈
https://github.com/google-research/google-research/issues [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2108.07732)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2108.07732 [来源4](https://arxiv.org/pdf/2108.07732)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
820a8de4a9fe8aef947a40d5da13db0d660baf3658b4a9cebf6d30ac5ba351ab [来源4](https://arxiv.org/pdf/2108.07732)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
1540169
```
 [来源4](https://arxiv.org/pdf/2108.07732)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB",
  "webViewLink": "https://drive.google.com/drive/folders/1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB"
}
```
 [来源5](https://drive.google.com/drive/folders/1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw",
    "webViewLink": "https://docs.google.com/document/d/18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw/edit?usp=drivesdk"
  }
]
```
 [来源1](https://github.com/google-research/google-research/tree/master/mbpp) [来源6](https://docs.google.com/document/d/18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P",
  "webViewLink": "https://drive.google.com/file/d/1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P/view?usp=drivesdk"
}
```
 [来源7](https://drive.google.com/file/d/1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P/view?usp=drivesdk)

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
 [来源1](https://github.com/google-research/google-research/tree/master/mbpp)

## 来源

1. https://github.com/google-research/google-research/tree/master/mbpp — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2108.07732 — 采集：2026-11-07 KST。
3. https://arxiv.org/html/2609.27284v1 — 采集：2026-11-07 KST。
4. https://arxiv.org/pdf/2108.07732 — 采集：2026-11-07 KST。
5. https://drive.google.com/drive/folders/1lBLOX-D6U7R6GsMuUhauqxp8YiFrKuWB — 采集：2026-11-07 KST。
6. https://docs.google.com/document/d/18bh5SmB0B_lb71z2FyPK0mJi2n75wvzwjSqinegTWWw/edit?usp=drivesdk — 采集：2026-11-07 KST。
7. https://drive.google.com/file/d/1WKLwDaRewmUx2tg1DJLInPU9kqdDOS6P/view?usp=drivesdk — 采集：2026-11-07 KST。
