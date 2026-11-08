# DeepSWE

> 深度核验：2026-11-07。未知不等于未公开；网页更新日、运行日与访问日分开记录。

未知信息保留待核实。

DeepSWE以113道原创长程工程任务覆盖91个开源仓库、五种代码语言。任务不是从已合并PR抽取：作者分别编写行为需求、可执行verifier与审稿用参考实现，并用浅克隆阻断从git历史直接取答案。相较短程补丁题，它强调探索代码库、跨文件实现和保持原有功能。 [1](https://deepswe.datacurve.ai/) [2](https://arxiv.org/abs/2607.07946) [3](https://deepswe.datacurve.ai/blog/deepswe) [4](https://epoch.ai/benchmarks/deepswe/review)

官方博客2026-05-26发布，arXiv首版为2026-07-08；当前榜和仓库采用v1.1。作者的LLM审计低分歧率不是人工认证：Epoch对v1.1独立审查，在至少23/113题发现假阴性并判Flawed。当前74%附近的分数必须连同评分缺陷、模型effort和重复运行区间阅读，不能作为高精度模型名次。 [1](https://deepswe.datacurve.ai/) [2](https://arxiv.org/abs/2607.07946) [3](https://deepswe.datacurve.ai/blog/deepswe) [4](https://epoch.ai/benchmarks/deepswe/review)

## 基本信息

- **简称**：DeepSWE [1](https://deepswe.datacurve.ai/)

- **全称**：DeepSWE [1](https://deepswe.datacurve.ai/)

- **基准版本**：v1.1 [1](https://deepswe.datacurve.ai/)

- **论文/报告版本**：arXiv:2607.07946v1（2026-07-08） [2](https://arxiv.org/abs/2607.07946)

- **发布日期**：2026-05-26（官方发布博客）；arXiv首版2026-07-08 [3](https://deepswe.datacurve.ai/blog/deepswe)

- **主板块**：代码 [1](https://deepswe.datacurve.ai/) 注：编辑主板块归档，不据此限制跨学科覆盖。

- **子领域**：长程软件工程；代码Agent；行为验证 [2](https://arxiv.org/abs/2607.07946)

- **许可证与限制**：官方基准仓库Apache-2.0；被评测的91个上游仓库各自保留其许可 [5](https://github.com/datacurve-ai/deep-swe/blob/main/LICENSE)

- **论文/报告**：https://arxiv.org/abs/2607.07946 [2](https://arxiv.org/abs/2607.07946)

- **官方代码**：https://github.com/datacurve-ai/deep-swe [6](https://github.com/datacurve-ai/deep-swe)

- **数据入口**：https://huggingface.co/datasets/datacurve/deep-swe [7](https://huggingface.co/datasets/datacurve/deep-swe)

- **官方主页**：https://deepswe.datacurve.ai/ [1](https://deepswe.datacurve.ai/)

- **报告标题**：DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks [2](https://arxiv.org/abs/2607.07946)

## 发起与维护

- **发起方**：Datacurve [4](https://epoch.ai/benchmarks/deepswe/review)

- **核心作者**：Wenqi Huang；Charley Lee；Leonard Tng；Serena Ge [2](https://arxiv.org/abs/2607.07946)

- **维护方**：Datacurve [4](https://epoch.ai/benchmarks/deepswe/review)

**仍待核实**（不推断为未公开）：

- 合作方：正式材料不足以确认独立研究合作方；工具提供者、模型厂商和上游仓库不能据此当作合作机构。 [1](https://deepswe.datacurve.ai/)
- 资助方：已核对论文/官方报告的作者、合作与致谢信息；未确认可列入该项目的直接资助方，不从机构隶属或合作协议推定。 [1](https://deepswe.datacurve.ai/)

## 设计目标

- **核心能力**：原创、长程真实软件工程任务的完成能力。 [1](https://deepswe.datacurve.ai/)

- **相对已有评测的缺口**：避免已有提交或PR改编，并扩大仓库和语言多样性，区分趋于饱和的代码Agent。 [1](https://deepswe.datacurve.ai/)

## 构建方式

- **题目来源**：113道原创任务，来自91个活跃、至少500 GitHub stars且使用宽松开源许可的仓库；部分题目受未解决issue启发，但参考实现不复制已有PR/commit。 [2](https://arxiv.org/abs/2607.07946) [3](https://deepswe.datacurve.ai/blog/deepswe)

- **出题与审核人员**：软件工程师逐题构造任务、容器、测试和参考实现，并互相评审；论文作者署名机构Datacurve。 [2](https://arxiv.org/abs/2607.07946)

- **审核流程**：LLM辅助检查与独立人工复核并行；审核prompt-verifier对应性、可接受替代实现、真实需求与环境洁净度；多种agent试跑辅助检查通过/失败是否合理。 [2](https://arxiv.org/abs/2607.07946)

- **质量控制**：每个verifier构建时重复运行3次筛除flaky测试；每次评分加入原仓库测试子集与新增回归检查；参考补丁仅用于审稿，不参与运行评分。 [2](https://arxiv.org/abs/2607.07946)

- **防污染/运行完整性**：原创实现不回流上游PR/commit，容器仅含base commit的浅克隆；这是初次测量时的防污染设计。公开题目、测试与轨迹后，未来模型仍可能摄入这些材料，不能永久声称无污染。 [2](https://arxiv.org/abs/2607.07946)

## 数据形式

- **规模**：113任务、91仓库；TypeScript 35、Go 34、Python 34、JavaScript 5、Rust 5。 [3](https://deepswe.datacurve.ai/blog/deepswe)

- **题型**：跨文件工程功能实现、修复和长期代码维护。 [1](https://deepswe.datacurve.ai/)

- **模态**：代码；文本；测试环境 [1](https://deepswe.datacurve.ai/)

- **语言覆盖**：TypeScript；Go；Python；JavaScript；Rust [2](https://arxiv.org/abs/2607.07946) 注：此处为代码语言；自然语言prompt样例为英文，未宣称多语覆盖。

- **难度与任务跨度**：长程指任务参考实现规模、多文件跨度和所需探索，而非经测量的人类工时；短小修复和定位任务占比不足。 [2](https://arxiv.org/abs/2607.07946)

- **公开与隐藏划分**：113题与verifier通过官方仓库公开；每次运行对agent隐藏tests/和solution/。v1.1在独立干净容器应用agent提交补丁后评分，避免agent直接干预评分环境。 [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md) [7](https://huggingface.co/datasets/datacurve/deep-swe)

## 评测方法

- **指标**：Pass@1；附成本、输出token和Agent步数。 [1](https://deepswe.datacurve.ai/)

- **评分规则**：手工功能测试及回归测试二值评分；pass@1为每题通过比例宏平均；pass@4为最多四次中至少一次通过的题占比。超时/上下文耗尽计失败，provider/verifier/网络错误排除分母且不补采。 [2](https://arxiv.org/abs/2607.07946)

- **提示与运行配置**：mini-swe-agent共享单bash工具与system prompt；论文固定commit adfe2023，单rollout限9000秒，不设step或cost cap；约每题每配置4次rollout。v1.1运行需Pier>0.3.0的独立verifier环境。 [2](https://arxiv.org/abs/2607.07946) [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

- **评分/运行脚本**：https://github.com/datacurve-ai/deep-swe [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

- **可比性限制**：统一harness不等于各厂商生产产品体验；reasoning effort各家不同。95%误差条主要反映重复运行波动，不包含全部任务抽样不确定性；LLM审计分歧率不是verifier真实错误率。 [2](https://arxiv.org/abs/2607.07946)

## 最新情况

- **核验日期**：2026-11-07 [1](https://deepswe.datacurve.ai/)

- **现行版本与采用证据**：version：v1.1；evidence_2026_h2：url：https://epoch.ai/benchmarks/deepswe/review；date：2026-09-07；note：Epoch独立审查为Flawed。；url：https://openai.com/index/gpt-6-astra/；date：2026-11-07；date_type：observed_on；note：GPT-6 Astra发布表采用。 [4](https://epoch.ai/benchmarks/deepswe/review) [9](https://openai.com/index/gpt-6-astra/)

- **更新与修订**：PDF为arXiv v1；当前仓库v1.1增加独立verifier容器，与论文初版实验需区分。 [2](https://arxiv.org/abs/2607.07946) [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

- **饱和度判断**：编辑判断：官方v1.1可读榜首显示74%±3%，另外两配置四舍五入也为74%；重叠区间不支持把三者细微差异视作显著领先。 [1](https://deepswe.datacurve.ai/)

- **已知问题与证据边界**：Epoch对v1.1于2026-09-07作Flawed评价：人工确认至少23/113题（>20.3%）有假阴性；18例与agent改测试后verifier恢复/新增测试产生冲突有关。审查达到阈值即停止，并未估计全部错误率，也未证明其余90题无误。这与作者LLM审计1.4%分歧结论来自不同方法，不可互相替代。 [4](https://epoch.ai/benchmarks/deepswe/review) [2](https://arxiv.org/abs/2607.07946)

- **关联与衍生关系**：Pier是运行框架，Harbor是任务/轨迹格式；均不是新的DeepSWE题库版本。 [8](https://github.com/datacurve-ai/deep-swe/blob/main/README.md)

## 榜单快照

- **快照采集日**：2026-11-07 [1](https://deepswe.datacurve.ai/)

- **官方榜/正式委托榜**：https://deepswe.datacurve.ai/ [1](https://deepswe.datacurve.ai/)

- **独立第三方入口**：https://epoch.ai/benchmarks/deepswe/review [4](https://epoch.ai/benchmarks/deepswe/review)

| 标记/名次 | 模型或配置 | 结果 | 指标与来源 |
|---|---|---|---|
| 1 | gpt-6-astra [xhigh] | 74% ±3% | v1.1 pass@1；网页四舍五入；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 2 | gemini-3.8-flash [high] | 74% ±1% | v1.1 pass@1；网页四舍五入；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 3 | claude-opus-5 [max] | 74% ±4% | v1.1 pass@1；网页四舍五入；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 4 | gpt-5.6-sol [max] | 73% ±3% | v1.1 pass@1；网页四舍五入；2026-09-22；[1](https://deepswe.datacurve.ai/) |
| 5 | claude-fable-5 [xhigh] | 70% ±3% | v1.1 pass@1；网页四舍五入；2026-09-22；[1](https://deepswe.datacurve.ai/) |

> gpt-6-astra [xhigh]：rank_type：官网显示行序，非显著性次序 [1](https://deepswe.datacurve.ai/)

> gemini-3.8-flash [high]：rank_type：官网显示行序，非显著性次序 [1](https://deepswe.datacurve.ai/)

> claude-opus-5 [max]：rank_type：官网显示行序，非显著性次序 [1](https://deepswe.datacurve.ai/)

> gpt-5.6-sol [max]：rank_type：官网显示行序，非显著性次序 [1](https://deepswe.datacurve.ai/)

> claude-fable-5 [xhigh]：rank_type：官网显示行序，非显著性次序 [1](https://deepswe.datacurve.ai/)

表内所有条目采集于2026-11-07；行序不自动代表统计显著性，历史实验与实时榜均按说明区分。

- **覆盖范围与版本限制**：官网显示顺序；三者显示值相同，误差区间重叠，不据此宣称显著优劣。 [1](https://deepswe.datacurve.ai/)

## 联系方式

- **公开问题追踪**：https://github.com/datacurve-ai/deep-swe/issues [6](https://github.com/datacurve-ai/deep-swe)

**仍待核实**（不推断为未公开）：

- 公开联系邮箱：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://deepswe.datacurve.ai/)
- 官方社交：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://deepswe.datacurve.ai/)
- 隐私政策：所查正式论文、README、官网链接中，未定位可确认对应维护方的这一公开联系渠道；不猜测邮箱或政策路径。 [1](https://deepswe.datacurve.ai/)

## 原始文件

- **原始PDF**：https://arxiv.org/pdf/2607.07946 [10](https://arxiv.org/pdf/2607.07946)

- **SHA-256**：1d988c90737299c6d844694ba967ff63f4e2aa13c66be20b97b8fa4bd89754ce [10](https://arxiv.org/pdf/2607.07946) 注：实际下载的PDF字节计算；不是外部网页抄录。

- **PDF字节数**：713926 [10](https://arxiv.org/pdf/2607.07946) 注：下载字节数；未上传。

- **其他正式文档**：type：仓库README（v1.1评分隔离）；url：https://github.com/datacurve-ai/deep-swe/blob/main/README.md；type：任务与数据卡；url：https://huggingface.co/datasets/datacurve/deep-swe [6](https://github.com/datacurve-ai/deep-swe) [7](https://huggingface.co/datasets/datacurve/deep-swe)

- **中的论文副本**：待核实 [1](https://deepswe.datacurve.ai/)

**仍待核实**（不推断为未公开）：

- 归档目录：仅在本地生成研究输出与PDF校验，未执行上传；正式归档文件夹链接仍需确认。 [1](https://deepswe.datacurve.ai/)

## 变更记录

- date：2026-11-07；；change：按官方材料新建中文条目；区分热度、质量和不同版本评分。；2026-11-07：逐源深核；重读官方方法、已定位论文PDF、仓库README/LICENSE和HF卡，补齐事实、区分相互冲突版本，重采可读榜单。原游戏私有材料及未定位正式产物继续留空。 [1](https://deepswe.datacurve.ai/)

---

来源访问日期统一为2026-11-07；原始URL见各段链接，结构化逐字段证据见同名JSON。
