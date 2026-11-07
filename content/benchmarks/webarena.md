# WebArena

> 核验：2026-11-07（KST / Asia/Seoul）。依据已打开官方材料中文改写；“待核实”不等于官方未公开。采集日不等于评测运行日。

[📄 阅读原始论文 PDF](https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk)

## 基本信息

### 简称
WebArena [来源1](https://webarena.dev/og/)

### 全称
WebArena [来源1](https://webarena.dev/og/)

> 保留官方名称，不把论文标题自动扩写为全称。

### 基准版本
原始812任务协议；不同WebArena衍生独立注明 [来源2](https://arxiv.org/abs/2307.13854)

### 论文版本
arXiv v4 [来源2](https://arxiv.org/abs/2307.13854)

> 论文修订版本不等同数据集版本。

### 发布日期
2023-07-26 07:59:32 KST [来源2](https://arxiv.org/abs/2307.13854)

> 首次 arXiv 论文提交时间，已转 KST；不自动视为数据集首发时间。

### 主板块
Agent [来源2](https://arxiv.org/abs/2307.13854)

> Benchmark Atlas 编辑归档；跨领域仅主板块计数。

### 领域标签

```json
[
  "网页任务执行"
]
```
 [来源2](https://arxiv.org/abs/2307.13854)

### 许可证
Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据） [来源3](https://github.com/web-arena-x/webarena)

### 论文
https://arxiv.org/abs/2307.13854 [来源2](https://arxiv.org/abs/2307.13854)

### 官方代码
https://github.com/web-arena-x/webarena [来源1](https://webarena.dev/og/)

### 数据地址
https://github.com/web-arena-x/webarena/blob/main/config_files/test.raw.json [来源1](https://webarena.dev/og/)

### 官方入口
https://webarena.dev/og/ [来源1](https://webarena.dev/og/)

### 论文标题
WebArena: A Realistic Web Environment for Building Autonomous Agents [来源2](https://arxiv.org/abs/2307.13854)

## 发起与维护

### 机构与发起方
Carnegie Mellon University；作者也列Inspired Cognition单位。 [来源2](https://arxiv.org/abs/2307.13854)

### 合作方
待核实 [来源2](https://arxiv.org/abs/2307.13854)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 作者

```json
[
  "Zhou, Shuyan",
  "Xu, Frank F.",
  "Zhu, Hao",
  "Zhou, Xuhui",
  "Lo, Robert",
  "Sridhar, Abishek",
  "Cheng, Xianyi",
  "Ou, Tianyue",
  "Bisk, Yonatan",
  "Fried, Daniel",
  "Alon, Uri",
  "Neubig, Graham"
]
```
 [来源2](https://arxiv.org/abs/2307.13854)

### 当前维护方
WebArena / web-arena-x 项目团队 [来源2](https://arxiv.org/abs/2307.13854)

### 资助
AFRL FA8750-19-2-0200；AWS AI gift；CAIS compute支持。 [来源2](https://arxiv.org/abs/2307.13854)

## 设计目标

### 衡量能力
把高层自然语言意图转成跨网页多步行动，正确改变网页状态或获取信息。 [来源2](https://arxiv.org/abs/2307.13854)

### 设计背景
静态网页快照与短步骤任务难评长程规划；单看动作相似度会拒绝不同但正确的路径。 [来源2](https://arxiv.org/abs/2307.13854)

## 构建方式

### 题目来源
自托管拟真网站：电商、论坛、协作开发、内容管理四类；作者编写241模板派生812任务，附地图/计算器/wiki等。 [来源2](https://arxiv.org/abs/2307.13854)

### 出题者背景
CMU研究者设计意图；网站数据模拟现实分布，不是对真实用户账户操作。 [来源2](https://arxiv.org/abs/2307.13854)

### 审核流程
两名标注者生成参考答案，第三人解决分歧。 [来源2](https://arxiv.org/abs/2307.13854)

### 质量控制
Docker可复现环境，程序化网站终态检查；信息查询支持exact/must-include/fuzzy比较。 [来源2](https://arxiv.org/abs/2307.13854)

### 去污染
本地环境支持可复现但数据/任务公开；模板相似性和后续训练污染仍需注意。 [来源2](https://arxiv.org/abs/2307.13854)

## 数据形式

### 题量与规模
812任务，来自241模板，覆盖4类主要网站。 [来源2](https://arxiv.org/abs/2307.13854)

### 题型
信息查询、内容创建/修改和多网站联合操作。 [来源2](https://arxiv.org/abs/2307.13854)

### 模态

```json
[
  "网页文本/HTML/可访问性树",
  "可选截图",
  "工具动作"
]
```
 [来源2](https://arxiv.org/abs/2307.13854)

### 语言
英语指令；网站内容与代码相关语法。 [来源2](https://arxiv.org/abs/2307.13854)

### 难度
长程、部分需多网站/外部知识；同模板实例并非完全独立能力点。 [来源2](https://arxiv.org/abs/2307.13854)

### 公开与隐藏划分
自托管网站、任务和功能评测代码公开；不等于线上真实网站或隐藏服务。 [来源2](https://arxiv.org/abs/2307.13854)

## 评测方法

### 指标
端到端task success rate。 [来源2](https://arxiv.org/abs/2307.13854)

### 评分
检查最终或必要中间网站状态；查询答案使用精确、包含或GPT-4-0613模糊比较。 [来源2](https://arxiv.org/abs/2307.13854)

### 提示与运行设置
原论文2-shot，温度1、top-p0.9、最多30步；可达性提示变体须另列。 [来源2](https://arxiv.org/abs/2307.13854)

### 官方评测脚本
https://github.com/web-arena-x/webarena [来源1](https://webarena.dev/og/)

### 可比性警示
WebArena与VisualWebArena/WebArena-Infinity/Verified变体不同；截图与可访问树观察、外部浏览和步数预算也不同。 [来源2](https://arxiv.org/abs/2307.13854)

## 最新情况

### 核查日期
2026-11-07 KST / Asia/Seoul [来源1](https://webarena.dev/og/)

### 当前版本与2026年后半年活跃证据

```json
{
  "version": "原始812任务协议；不同WebArena衍生独立注明",
  "evidence_2026_h2": [
    {
      "url": "https://arxiv.org/html/2609.19134v1",
      "date": "2026-09-16",
      "note": "ScienceIDE §4.2及参考文献明确引用 WebArena 作为语言模型Agent/交互环境先行基准；为H2学术引用，不声称本文实跑。"
    }
  ]
}
```
 [来源4](https://arxiv.org/html/2609.19134v1) [来源2](https://arxiv.org/abs/2307.13854)

> H2 活跃证据区分实际评测、第三方追踪和仅学术引用；不据引用推断实跑。

### 论文修订历史
Submission history From: Shuyan Zhou [ view email ] [v1] 2023-07-26 07:59:32 KST (9,497 KB) [v2] 2023-10-24 12:19:22 KST (8,751 KB) [v3] 2023-10-25 10:56:14 KST (8,751 KB) [v4] 2024-04-17 00:13:18 KST (9,472 KB) [来源2](https://arxiv.org/abs/2307.13854)

### 饱和情况
待核实 [来源2](https://arxiv.org/abs/2307.13854)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 污染与争议
固定模板、公开测试和使用LLM模糊裁判会影响泛化解释；网站环境版本需要固定。 [来源2](https://arxiv.org/abs/2307.13854)

### 衍生与版本关系
VisualWebArena等增加视觉条件，WebArena-x/Infinity另有新任务；原始812题成绩不转贴到衍生版。 [来源2](https://arxiv.org/abs/2307.13854)

## 榜单快照

### 快照日期
2026-11-07 KST / Asia/Seoul [来源1](https://webarena.dev/og/)

### 官方榜单
https://webarena.dev/og/ [来源1](https://webarena.dev/og/)

### 独立评测覆盖
待核实 [来源1](https://webarena.dev/og/)

> 未在本次来源中核实 AA / Epoch / LMArena 对该基准的独立同口径榜单覆盖；不以其他任务替代。

### 核验结果

```json
[
  {
    "model": "GPT-4-0613 + CoT",
    "score": 14.41,
    "metric": "task success (%)",
    "benchmark_version": "原始812任务",
    "result_type": "论文历史基线",
    "source_date": "原论文Table3",
    "collected_at": "2026-11-07 KST",
    "settings": "no unachievable hint；2-shot/30步"
  }
]
```
 [来源2](https://arxiv.org/abs/2307.13854)

### 覆盖与时效说明
保留原论文无不可达提示的历史基线；有提示11.70%是另一设置，不当作同榜更新。当前网站已出现WebArena-x内容，原始协议用/og/归档核验；H2证据是ScienceIDE引用而非实跑。 [来源2](https://arxiv.org/abs/2307.13854)

## 联系方式

### 公开工作邮箱

```json
[
  "shuyanzh@cs.cmu.edu",
  "fangzhex@cs.cmu.edu",
  "gneubig@cs.cmu.edu"
]
```
 [来源1](https://webarena.dev/og/)

### 公开反馈
https://github.com/web-arena-x/webarena/issues [来源1](https://webarena.dev/og/)

> 公开仓库反馈入口；未发送问题。

### 官方社交渠道
待核实 [来源2](https://arxiv.org/abs/2307.13854)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

### 隐私政策
待核实 [来源2](https://arxiv.org/abs/2307.13854)

> 本次已检索所列官方材料，但未完成该字段的精确核验；不代表官方没有公开。

## 原始文件

### 源站论文PDF
https://arxiv.org/pdf/2307.13854 [来源5](https://arxiv.org/pdf/2307.13854)

> 归档为下载时源站提供的 PDF；论文版本和基准版本分别记录。

### 原始PDF SHA-256
f9731b92bc3d29a2ea7b5f9cb46b48540c76bc3f84a57e0c48fc37ea73107f95 [来源5](https://arxiv.org/pdf/2307.13854)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### 原始PDF字节数

```json
9128123
```
 [来源5](https://arxiv.org/pdf/2307.13854)

> 源站下载的原始字节，未压缩或重写；SHA-256 / 字节数由本次下载计算。

### Drive资料文件夹

```json
{
  "id": "1nFh380aqu7esGjwpLfEm0xF85brhlOzU",
  "webViewLink": "https://drive.google.com/drive/folders/1nFh380aqu7esGjwpLfEm0xF85brhlOzU"
}
```
 [来源6](https://drive.google.com/drive/folders/1nFh380aqu7esGjwpLfEm0xF85brhlOzU)

### 其他文档

```json
[
  {
    "type": "中文介绍Google Doc",
    "id": "1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4",
    "webViewLink": "https://docs.google.com/document/d/1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4/edit?usp=drivesdk"
  }
]
```
 [来源1](https://webarena.dev/og/) [来源7](https://docs.google.com/document/d/1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4/edit?usp=drivesdk)

> 官方原始材料与中文改写介绍分别标示；HTML方法页不是原始论文PDF。

### Drive论文附件

```json
{
  "id": "1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L",
  "webViewLink": "https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk"
}
```
 [来源8](https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk)

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
 [来源1](https://webarena.dev/og/)

## 来源

1. https://webarena.dev/og/ — 采集：2026-11-07 KST。
2. https://arxiv.org/abs/2307.13854 — 采集：2026-11-07 KST。
3. https://github.com/web-arena-x/webarena — 采集：2026-11-07 KST。
4. https://arxiv.org/html/2609.19134v1 — 采集：2026-11-07 KST。
5. https://arxiv.org/pdf/2307.13854 — 采集：2026-11-07 KST。
6. https://drive.google.com/drive/folders/1nFh380aqu7esGjwpLfEm0xF85brhlOzU — 采集：2026-11-07 KST。
7. https://docs.google.com/document/d/1OTl6lnoV0OsMnUUEnn544z3E_2EaRfU3HH5BAKTVbl4/edit?usp=drivesdk — 采集：2026-11-07 KST。
8. https://drive.google.com/file/d/1vlsk1lC8L3o4gI4h9qaTUwELS4bwG60L/view?usp=drivesdk — 采集：2026-11-07 KST。
