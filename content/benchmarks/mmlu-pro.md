# MMLU-Pro

> 核验：2026-11-07（KST / Asia/Seoul）。官方材料中文改写；待核实不等于未公开。

[阅读原始论文 PDF](https://drive.google.com/file/d/1Da_rxFnMCLvHV1ywvyHwmTfVzKATfUgQ/view?usp=drivesdk)

## 基本信息

### 简称
MMLU-Pro
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 全称
MMLU-Pro
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 基准版本
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文版本
arXiv v6
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 发布日期
2024-06-03
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 原始论文首发日期，不保证等同于数据文件首次公开日。

### 主板块
语言
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> Benchmark Atlas编辑归档，不是论文指定的唯一领域。

### 领域标签
```json
[
  "高难多学科知识与推理"
]
```
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 许可证
数据：论文附录说明 MIT；代码仓库当前显示 Apache-2.0，二者不是同一许可对象。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 论文
https://arxiv.org/abs/2406.01574
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 官方代码
https://github.com/TIGER-AI-Lab/MMLU-Pro
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 数据地址
https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 官方入口
https://github.com/TIGER-AI-Lab/MMLU-Pro
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 论文标题
MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

## 发起与维护

### 机构与作者单位
论文作者来自 University of Waterloo、University of Toronto、Carnegie Mellon University 等；作者单位不等同于唯一发起方。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 正式合作机构
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 作者
```json
[
  "Wang, Yubo",
  "Ma, Xueguang",
  "Zhang, Ge",
  "Ni, Yuansheng",
  "Chandra, Abhranil",
  "Guo, Shiguang",
  "Ren, Weiming",
  "Arulraj, Aaran",
  "He, Xuan",
  "Jiang, Ziyan",
  "Li, Tianle",
  "Ku, Max",
  "Wang, Kai",
  "Zhuang, Alex",
  "Fan, Rongqi",
  "Yue, Xiang",
  "Chen, Wenhu"
]
```
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 当前维护方
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 资助
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 设计目标

### 测量能力
在多学科知识问答中提高推理强度、难度与提示稳健性。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 既有评测缺口
原始 MMLU 存在过易题、噪声及提示敏感问题；增加候选项和推理题以继续区分强模型。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

## 构建方式

### 题目来源
筛选原始 MMLU，并补充 STEM 网站、TheoremQA 与 SciBench 等来源的题目；使用 GPT-4-Turbo 辅助生成干扰选项。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 出题与标注背景
作者组织专业背景审阅者进行学科审核；具体每位出题人的资历需以论文附录为准。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 审核
两阶段专家审核；利用 Gemini-1.5-Pro 检查筛选过程中的假阴性等问题。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 质量控制
剔除简单、模糊和错误题，检查增加的干扰选项；不是对所有未来训练集的去污染保证。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 去污染
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 数据形式

### 题量
12,032 题，14 个学科；83% 的题目有 10 个选项，平均 9.47 个选项。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 题型
单答案多项选择，通常 10 个候选项
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 模态
文本
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 语言
英语
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 难度
更强调推理并减少原始 MMLU 的简单题；不能把所有题都称为研究生级专家原创题。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 公开与隐藏划分
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

## 评测方法

### 指标
选择题准确率；可按学科查看。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 评分
从生成回答中抽取答案选项，官方提供多种答案抽取策略；原论文脚本无法匹配答案时使用随机回退，复现需记录实现。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 提示与生成设置
原论文主设置为 5-shot CoT；直接回答与 CoT 分开报告。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 脚本
https://github.com/TIGER-AI-Lab/MMLU-Pro
[来源1](https://github.com/TIGER-AI-Lab/MMLU-Pro)（采集2026-11-07）

### 可比性警告
不得把原论文、官方 mini 榜、动态 Hugging Face 榜和 AA 的不同提示设置视为同一轮评测。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

## 最新情况

### 本次核验日与H2使用证据
2026-11-07
[来源1](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

> 2026-H2实际使用证据：2026-10-08：Jev 对比研究的表1–2和§3.1实际使用 MMLU-Pro，将其纳入13个多选基准的模型评测。

### 数据版本
待核实
[来源1](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 论文修订记录
```json
[
  {
    "version": "v1",
    "submitted_at": "2024-06-04T02:53:00+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v2",
    "submitted_at": "2024-06-04T19:36:49+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v3",
    "submitted_at": "2024-06-05T13:03:36+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v4",
    "submitted_at": "2024-06-24T00:57:16+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v5",
    "submitted_at": "2024-10-08T02:46:08+09:00",
    "timezone": "Asia/Seoul (KST)"
  },
  {
    "version": "v6",
    "submitted_at": "2024-11-06T11:54:00+09:00",
    "timezone": "Asia/Seoul (KST)"
  }
]
```
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 饱和情况
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 污染与已知问题
原始 MMLU 的噪声和提示敏感是该基准的设计动机；它仍是公开静态题集，不能由难度较高推出无训练污染。
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

### 衍生评测
```json
[
  "MMLU-ProX"
]
```
[来源1](https://arxiv.org/abs/2503.10497)（采集2026-11-07）

## 榜单快照

### 采集日
2026-11-07
[来源1](https://artificialanalysis.ai/evaluations/mmlu-pro)（采集2026-11-07）

> 采集日期，不代表所有列出模型的运行日期；结果行另标历史/实时属性。

### 官方榜或原始结果入口
https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro
[来源1](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)（采集2026-11-07）

### 二级机构榜单
https://artificialanalysis.ai/evaluations/mmlu-pro
[来源1](https://artificialanalysis.ai/evaluations/mmlu-pro)（采集2026-11-07）

### 可读结果
```json
[
  {
    "model": "Gemini 3 Pro Preview (High)",
    "score": 89.8,
    "unit": "%",
    "metric": "accuracy",
    "scope": "AA 页面公开内嵌摘要；模型标签按原页，非自行推定 API 快照",
    "evaluation_date": "待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Gemini 3 Pro Preview (Low)",
    "score": 89.5,
    "unit": "%",
    "metric": "accuracy",
    "scope": "AA 页面公开内嵌摘要",
    "evaluation_date": "待核实",
    "snapshot_date": "2026-11-07"
  },
  {
    "model": "Claude Opus 4.5 (Reasoning)",
    "score": 89.5,
    "unit": "%",
    "metric": "accuracy",
    "scope": "AA 页面公开内嵌摘要",
    "evaluation_date": "待核实",
    "snapshot_date": "2026-11-07"
  }
]
```
[来源1](https://artificialanalysis.ai/evaluations/mmlu-pro)（采集2026-11-07）

### 覆盖与时效限制
AA 网页可见正文未展开具体分数，但公开 HTML 的页面摘要载荷给出所列三项；只作采集日可读快照，更新时间和精确 API 版本待核实。官方仓库 mini 榜最高列 Claude-3.5-Sonnet 76.12%，缺乏明确运行日期，属于较旧口径，未与 AA 排名合并。
[来源1](https://artificialanalysis.ai/evaluations/mmlu-pro)（采集2026-11-07） [来源2](https://arxiv.org/html/2610.11978v1)（采集2026-11-07）

## 联系方式

### 公开研究联系邮箱
```json
[
  "y726wang@uwaterloo.ca",
  "x93ma@uwaterloo.ca",
  "wenhuchen@uwaterloo.ca"
]
```
[来源1](https://github.com/TIGER-AI-Lab/MMLU-Pro)（采集2026-11-07）

### 仓库讨论与Issues
https://github.com/TIGER-AI-Lab/MMLU-Pro/issues
[来源1](https://github.com/TIGER-AI-Lab/MMLU-Pro)（采集2026-11-07）

### 官方社交渠道
待核实
[来源1](https://arxiv.org/abs/2406.01574)（采集2026-11-07）

> 已检查所列材料，但本批尚未完成该字段的精确核验；不表示官方未公开。

### 收录边界
只收录论文、官网、官方仓库公开的研究联系渠道，不收集私人联系方式。
[来源1](urn:benchmark-atlas:constitution:v0.1)（采集2026-11-07）

## 原始文件

### 源PDF
https://arxiv.org/pdf/2406.01574
[来源1](https://arxiv.org/pdf/2406.01574)（采集2026-11-07）

### 原件SHA-256
e8f695db151fc8820f20c2864e6f6e27769fd94a307b7e60e211912cc9a3ef59
[来源1](https://arxiv.org/pdf/2406.01574)（采集2026-11-07）

> 原始下载字节SHA-256；未压缩或改写。

### 原件字节数
```json
959520
```
[来源1](https://arxiv.org/pdf/2406.01574)（采集2026-11-07）

### Drive目录
```json
{
  "id": "1Po20Xg2cDMJSdwXW4FNQNzaDKXQL8Zyk",
  "webViewLink": "https://drive.google.com/drive/folders/1Po20Xg2cDMJSdwXW4FNQNzaDKXQL8Zyk"
}
```
[来源1](https://drive.google.com/drive/folders/1Po20Xg2cDMJSdwXW4FNQNzaDKXQL8Zyk)（采集2026-11-07）

### 中文介绍
```json
[
  {
    "kind": "中文介绍 Google Doc",
    "id": "1kNKY72GZu__3yga22rvnqfenFh1W4shyrzS0cooj7VM",
    "webViewLink": "https://docs.google.com/document/d/1kNKY72GZu__3yga22rvnqfenFh1W4shyrzS0cooj7VM/edit?usp=drivesdk"
  }
]
```
[来源1](https://docs.google.com/document/d/1kNKY72GZu__3yga22rvnqfenFh1W4shyrzS0cooj7VM/edit?usp=drivesdk)（采集2026-11-07）

## 变更记录
[
  {
    "date": "2026-11-07",
    "timezone": "Asia/Seoul",
    "change": "首批官方来源深检、H2使用证据及版本冲突记录；原始PDF归档；未核实项显式标记。"
  }
]
[来源](https://arxiv.org/abs/2406.01574)（采集2026-11-07） [来源](https://arxiv.org/pdf/2406.01574)（采集2026-11-07）
