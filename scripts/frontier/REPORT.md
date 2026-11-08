# Benchmark Constitution · Frontier Heat

快照日期：2026-11-07。**暂定/可复核下界，不是已证明全球完整的最新20清单。**

20个模型；240个规范化benchmark家族；2456条来源/位置提及（计入2283，排除173）。所有数字为当前缓存证据的统计。

## 20个模型

| 模型 | 首发日期 | 官方来源 |
|---|---|---|
| Gemini 4 Carbon | 2026-10-28 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon |
| GPT-6.1 Terra | 2026-10-26 | https://deploymentsafety.openai.com/gpt-6-1-terra<br>https://openai.com/index/introducing-gpt-6-1-terra/ |
| Kimi K3.1 Pro | 2026-10-24 | https://www.kimi.com/blog/kimi-k3-1-pro<br>https://huggingface.co/moonshotai/Kimi-K3.1-Pro<br>https://forum.moonshot.ai/t/kimi-k3-1-pro-has-launched-start-exploring-now/629 |
| MiniMax M3.1 Flash | 2026-10-19 | https://www.minimax.io/blog/minimax-m31f |
| DeepSeek-V4.1-Flash-1017 | 2026-10-17 | https://api-docs.deepseek.com/zh-cn/news/news261017/<br>https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017 |
| Muse Spark Open | 2026-10-15 | https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B |
| Muse Wonder | 2026-10-12 | https://research.meta.ai/blog/muse-wonder<br>https://research.meta.ai/static/muse-wonder-model-card |
| Muse Wonder Full | 2026-10-12 | https://research.meta.ai/blog/muse-wonder<br>https://research.meta.ai/static/muse-wonder-model-card |
| Mistral Large 4 | 2026-10-06 | https://mistral.ai/news/mistral-large-4<br>https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B<br>https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/resolve/main/assets/technical_report.pdf |
| Gemini 4 Argon | 2026-09-30 | https://blog.google/intl/en-in/products/gemini-4-argon-our-next-era-of-frontier-intelligence<br>https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf |
| GPT-6.1 Sol | 2026-09-29 | https://deploymentsafety.openai.com/gpt-6-1-sol<br>https://openai.com/index/devday-2026-recap<br>https://openai.com/index/introducing-gpt-6-1-sol/ |
| Claude Sonnet 5.5 | 2026-09-28 | https://www.anthropic.com/claude-sonnet-5-5<br>https://www.anthropic.com/claude-sonnet-5-5-system-card |
| GPT-6 Sol | 2026-09-23 | https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna-in-the-api-codex-and-chatgpt/1399925<br>https://openai.com/index/introducing-gpt-6-sol-and-luna/<br>https://deploymentsafety.openai.com/gpt-6-astra |
| Claude Opus 5.5 | 2026-09-22 | https://www.anthropic.com/claude-opus-5-5<br>https://www.anthropic.com/claude-opus-5-5-system-card |
| Grok 4.7 | 2026-09-21 | https://x.ai/news/grok-4-7<br>https://docs.x.ai/developers/models/grok-4.7 |
| Qwen3.8-Omni-Flash | 2026-09-18 | https://www.alibabacloud.com/en/news/product/qwen38-omni-flash-officially-released-o86<br>https://www.alibabacloud.com/blog/qwen3-8-omni-flash-omni-senses--agentic-delivery-_603580 |
| DeepSeek-V4.1-Flash | 2026-09-10 | https://api-docs.deepseek.com/news/news260910<br>https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/raw/main/README.md<br>https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/resolve/main/DeepSeek_V41_Tech_Report.pdf |
| GPT-6 Astra | 2026-09-03 | https://deploymentsafety.openai.com/gpt-6-astra<br>https://openai.com/index/gpt-6-astra/ |
| Gemini 3.8 Flash | 2026-09-02 | https://deepmind.google/models/model-cards/gemini-3-8-flash/ |
| Muse Spark 1.3 | 2026-09-02 | https://research.meta.ai/blog/introducing-muse-spark-1-3<br>https://research.meta.ai/static/muse-spark-1-3-evaluation-report |

日期按首发，不把后续GA/开权重日期当首发；有UTC原始时间时换算。同日按id排序，9月2日边界并列不意味着日内发布时间已查清。

## 前30（每项至多20；同频按id排序）

| 名次 | Benchmark | 报告模型数 |
|---:|---|---:|
| 1 | DeepSWE | 18 |
| 2 | Terminal-Bench | 17 |
| 3 | AutomationBench-AA | 15 |
| 4 | Humanity’s Last Exam | 15 |
| 5 | OSWorld | 15 |
| 6 | Agents’ Last Exam | 11 |
| 7 | ExploitGym | 11 |
| 8 | ExploitBench | 10 |
| 9 | HealthBench | 10 |
| 10 | GDPval | 9 |
| 11 | GPQA | 9 |
| 12 | Harvey's Legal Agent Benchmark | 9 |
| 13 | AA-Omniscience | 8 |
| 14 | Terminal-Bench-Science | 8 |
| 15 | AA-Briefcase | 7 |
| 16 | Chartography | 7 |
| 17 | GDP.pdf | 7 |
| 18 | ProgramBench | 7 |
| 19 | SWE-bench | 7 |
| 20 | AAV Capsid Packaging Prediction | 6 |
| 21 | CharXiv | 6 |
| 22 | Finance Agent | 6 |
| 23 | SEC-Bench | 6 |
| 24 | BabyVision | 5 |
| 25 | CyScenarioBench | 5 |
| 26 | CyberGym | 5 |
| 27 | FrontierCode | 5 |
| 28 | FrontierSWE | 5 |
| 29 | Indirect Prompt Injection | 5 |
| 30 | MASK | 5 |

## 文件

* ` — SPEC结构，窗口、模型benchmark数组、count/share、rank_change、今日history。
* ` — 模型审核输入。
* ` — 逐条模型、规范化ID、原名、官方URL、正文行/PDF页/图表标签。
* ` — 合并家族、保留原始变体的词表。
* ` — 追加、滚动、去重模型计数、历史与排名变化。
* ` — 8项测试通过。
* ` — 240条名录，未知元数据保留null。
* ` — 页面/图表缓存和实读证据。
* ` — 缺失路径与覆盖限制。

## 缺失/打不开或原路径失败

| URL | 状态 | WebFetch实读补救 |
|---|---|---|
| https://openai.com/index/introducing-gpt-6-cyber/ | 403 | 此路径不可用 |
| https://openai.com/index/introducing-gpt-6-1-terra/ | 403 | 有摘录，可用 |
| https://openai.com/index/devday-2026-recap | 403 | 此路径不可用 |
| https://openai.com/index/gpt-6-for-everyone | 403 | 此路径不可用 |
| https://qwen.ai/blog?id=qwen3.8-omni-flash | 200 | 此路径不可用 |
| https://huggingface.co/Qwen/Qwen3.8-Omni-Flash | 401 | 此路径不可用 |
| https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /deepseek-ai/DeepSeek-V4.1-Flash (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1029)'))) | 此路径不可用 |
| https://openai.com/index/gpt-6-astra/ | 403 | 有摘录，可用 |
| https://qwen.ai/blog?id=qwen3.8-max-0902 | 200 | 此路径不可用 |
| https://research.meta.ai/blog/muse-spark-1-3 | 404 | 此路径不可用 |
| https://z.ai/blog/glm-5.3 | 200 | 此路径不可用 |
| https://z.ai/blog/glm-5.3-flash | 200 | 此路径不可用 |
| https://z.ai/blog | 404 | 此路径不可用 |
| https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/raw/main/README.md | 401 | 此路径不可用 |
| https://deploymentsafety.openai.com/gpt-6-sol-and-luna | 404 | 此路径不可用 |
| https://research.meta.ai/blog/muse-spark-1.3 | 404 | 此路径不可用 |
| https://openai.com/index/introducing-gpt-6-sol-and-luna/ | 403 | 有摘录，可用 |
| https://deploymentsafety.openai.com/gpt-6-sol | 404 | 此路径不可用 |
| https://research.meta.ai/blog/introducing-muse-spark-open | 404 | 此路径不可用 |

Qwen原JS空壳与受限HF页已用阿里云官方完整博客补上；Muse Spark Open公开HF模型卡正文可读，raw路径401不代表卡正文缺失；DeepSeek页面请求异常时已有官方release/HF raw/PDF；错误猜测路径不作存在证据。

## 覆盖与解释边界

- 已审核厂商宇宙中的最近20；未证明全球所有前沿模型均已覆盖。
- 部分图片和文档仍可能有未抽出的具名评测，不能宣称全部提及无遗漏。
- 合并有版本变体的评测家族，但MMLU-Pro和SWE-bench Pro等独立数据集保留独立ID。
- 计数是文档提及的去重模型数，包含上下文提及；不是成绩、实际采用率或质量排名。
- registry原始论文/仓库/独立官网多数待补核，homepage为已读厂商报告信息页并显式标注。
- 未部署每日定时任务；update_heat.py为可复跑的人工审核输入更新器。

未计入专用Cyber/Legal、轻量Haiku/Luna、纯图像/语音或同智力高速SKU。Zhipu未在已核验窗口入选；其他厂商以及临界日期仍须继续做发布日期审计。**不得把本快照标作完全完成全球最新20核验。**

## 每日复跑

见 `update_heat.py` 文件顶部完整流程。每日先人工打开官方新发布并校验日期，再追加models/mentions、补normalization和registry，运行：

```bash
python3 --date YYYY-MM-DD --append-models /path/new_models.json --append-mentions /path/new_mentions.json
python3
```

没有新模型时不加两个append参数即可。脚本不联网，不能代替新发布发现与全文审读。保留旧模型/提及档案，仅榜单窗口移出最旧模型。同日覆盖今日history，不会伪造昨日rank_change；首次均为new。

一次性缓存重建流程（不要作为日常数据更新，bootstrap会覆盖人工维护输入）：
```bash
python3
python3
python3
python3 --date 2026-11-07
```
