# MedPhysBench

用协议代码判分的医学物理计算与同行核查基准，覆盖放疗、影像、核医学与辐射防护。

## 基本信息

**简称**：MedPhysBench

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**全称**：MedPhysBench

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**基准版本**：v1.0（Prime Intellect Environments Hub 环境 omar/medphysbench 1.0.1）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**论文版本**：arXiv:2611.05340v1（2026-11-03）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**发布日期**：2026-11-03

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**主板块**：物理

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**领域标签**：医学物理；放射治疗；剂量计算；错误检测

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**许可证**：代码仓库为 MIT

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**论文或技术报告**：https://arxiv.org/abs/2611.05340

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**官方代码**：https://github.com/onusrat/medphysbench

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**数据地址**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**官方主页**：https://github.com/onusrat/medphysbench

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**论文题名**：MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 发起与维护

**发起方**：Omar Nusrat（多伦多都会大学物理系；圣迈克尔医院 iBEST）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**协作机构**：Prime Intellect（托管环境并提供推理与评测平台）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**作者**：Omar Nusrat

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**当前维护方**：Omar Nusrat

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**资助方**：Prime Intellect 通过 RL Residency 提供平台额度与算力

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 设计目标

**要测的能力**：检验语言模型完成医学物理计算，并核查同事计算中错误的能力，覆盖放射治疗、诊断影像、核医学与辐射防护

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**现有基准的缺口**：论文指出该领域既有评测多为选择题考试或开放式评分，缺少对带单位的物理量计算结果以及同行核查能力的判分

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 构建方式

**题目来源**：十个带随机种子的生成器依据 TG-51、TG-71、TG-43U1、NCRP 151 等协议生成题目，参考答案由实现协议的代码计算

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**出题人背景**：医学物理研究者

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**审核流程**：冻结前用独立的第二实现交叉核对全部求解器，并在开发集上试运行四个模型逐一复核失败；作者说明外部医学物理师盲审尚在计划中

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**质量控制**：两套实现在60,000道题上相对差异不超过1.3×10⁻¹⁵；以经验敏感度分析推导容差带；测试后与已发表算例比对，并对照 NCRP 151 原文复核屏蔽题

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**去污染**：测试集由未公开密钥经 HMAC-SHA256 派生种子生成，每题带 canary 字符串，并公开测试题参数哈希承诺

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 数据形式

**题量**：测试集1,200题（600道计算、300道工作表核查、300道结果核查）；公开开发集600题

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**题型**：数值计算（带单位）；工作表核查（判定并定位首个错误步骤）；结果核查

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**模态**：纯文本

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**语言**：英语

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**难度**：分三级，三级为完整临床手算任务，如 TG-51 校准工作表与等中心 MU 计算

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**公开与隐藏划分**：开发集公开；测试集仅可由密钥生成，作者代为评分

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 评测方法

**指标**：计算题容差内正确率；核查题的检出率、误报率与 Youden J

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**评分方式**：确定性评分，无模型裁判：解析最后的 boxed 答案，用 pint 统一单位后按0.5%到2%的相对容差判定

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**提示设置**：各模型使用服务商默认温度与推理设置，不使用工具，最多32,768个输出词元，每题作答一次

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**官方评测脚本**：https://github.com/onusrat/medphysbench

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**可比性说明**：部分模型只作答预先指定的分层半数测试集；论文披露 NCRP 151 题目的两处问题会影响少量三级屏蔽题判分

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 最新情况

**核验日期**：2026-11-10

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**最新数据版本**：v1.0（环境版本1.0.1）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**论文修订**：v1（2026-11-03）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**饱和情况**：计算任务对前四名模型已接近饱和（99.3%至100.0%）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**污染与争议**：论文自报 NCRP 151 屏蔽题在两源规则与患者散射使用因子上与原报告不一致，1.1版将修正；另有七道结果核查题改变了所报告的物理量，主分析仍计入

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**衍生基准**：作者早前的选择题基准 omar/medphysbench-kq（与本基准无共享题目）

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 榜单快照

**快照日期**：2026-11-10

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**官方榜**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**第三方榜**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**结果快照**：论文表2计算题正确率：GPT-6 Astra 100.0%（半数测试集）、GPT-6.1 Sol 99.7%、Gemini 4 Argon 99.5%、Claude Opus 5.5 99.3%、Claude Sonnet 5.5 93.7%、Gemma 3 27B 33.3%

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**覆盖说明**：结果取自论文，共评测12个模型

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 联系方式

**公开邮箱**：omar.nusrat@torontomu.ca

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**代码讨论**：https://github.com/onusrat/medphysbench/issues

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**官方社交账号**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**隐私政策**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 原始文件

**论文PDF**：https://arxiv.org/pdf/2611.05340v1

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**文件校验**：dfdd0079dc599d9c4d71e0b2d9ef52d02661eabcef118cc3f8d31c4592f90456

来源: [1](https://arxiv.org/pdf/2611.05340v1) (访问 2026-11-10)

**文件大小**：1129352

来源: [1](https://arxiv.org/pdf/2611.05340v1) (访问 2026-11-10)

**文件夹**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

**其他文件**：待核实

来源: [1](https://arxiv.org/abs/2611.05340) [2](https://github.com/onusrat/medphysbench) (访问 2026-11-10)

## 变更记录

2026-11-10：初次收录。
