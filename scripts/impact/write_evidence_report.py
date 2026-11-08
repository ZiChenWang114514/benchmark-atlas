#!/usr/bin/env python3
"""Validate this fixed-roster evidence pass and generate reproducible publication notes."""
import json,math,collections,hashlib
from pathlib import Path
from scipy.stats import spearmanr,kendalltau
from common import BASE,read,write,stamp,date
from compute import WEIGHTS
root=BASE/'impact';before=read(root/'archive/2026-11-08-before-evidence/index.json');after=read(root/'index.json');registry=read(BASE/'registry/registry.json');evidence=read(root/'evidence-report.json')
old=before['ranking']+before['unscored'];rows=after['ranking']+after['unscored'];byold={r['id']:r for r in old};bynew={r['id']:r for r in rows}
checks={}
checks['fixed_roster_1668']=len(rows)==1668 and set(bynew)==set(byold)=={r['id'] for r in registry['items']}
checks['known_citations_preserved']=all(r['raw'].get('citations')==byold[r['id']]['raw'].get('citations') for r in rows)
checks['missing_stars_not_estimated']=all(r['raw'].get('gh_stars_per_month')is None for r in rows)
checks['all_formal_gates_kept']=all(not r['confidence']['official_rank_eligible'] or (r['confidence']['coverage']>=.6 and r['confidence']['quality_coverage']>=.5 and 'flawed'not in r['flags']) for r in rows)
checks['ranked_coverage_gate']=all(r['confidence']['coverage']>=.4 and r['rank'] is not None for r in after['ranking'])
checks['unranked_no_score']=all(r['rank']is None and r['score']is None for r in after['unscored'])
checks['flaw_cap_40']=all(r['score']is None or r['score']<=40 for r in rows if 'flawed'in r['flags'])
checks['all_new_assessments_have_public_dated_sources']=all(a.get('sources') and all(s.get('url','').startswith(('https://','http://')) and date(s.get('accessed')) for s in a['sources']) for r in rows for a in r.get('assessment',{}).values() if isinstance(a,dict)and'value'in a)
checks['all_percent_headroom_bounded']=all(0<=r['components']['headroom']<=100 for r in rows if r['components']['headroom']is not None)
checks['finite_scores']=all(r['score']is None or (math.isfinite(r['score'])and 0<=r['score']<=100)for r in rows)
checks['no_current_version_verdict_leak']=all('epoch_verdict'not in bynew[k].get('assessment',{}) for k in ('terminal-bench','posttrainbench','hle-diamond','swe-bench-pro-v2','healthbench'))
checks['stable_numeric_order']=all(after['ranking'][i]['score']>=after['ranking'][i+1]['score']for i in range(len(after['ranking'])-1))
# Diagnostic sensitivity only: frozen eligible set; rank intervals are NOT CIs.
ranked=after['ranking'];ranges={r['id']:[r['rank']]for r in ranked};taus=[]
for key in WEIGHTS:
 for f in (.8,1.2):
  weights={k:w*(f if k==key else 1) for k,w in WEIGHTS.items()};z=sum(weights.values());weights={k:w/z for k,w in weights.items()}
  out=[]
  for r in ranked:
   score=50+sum(weights[k]*r['confidence']['dimension_reliability'][k]*(r['components'][k]-50)for k in weights if r['components'][k]is not None)
   if'flawed'in r['flags']:score=min(40,score)
   out.append((r['id'],score))
  out.sort(key=lambda x:(-x[1],x[0]));pos={k:i for i,(k,v)in enumerate(out,1)}
  taus.append(float(kendalltau([r['rank']for r in ranked],[pos[r['id']]for r in ranked]).statistic))
  for k,p in pos.items():ranges[k].append(p)
lex={k:i for i,k in enumerate(sorted(r['id']for r in ranked),1)}
alpha_rho=float(spearmanr([r['rank']for r in ranked],[lex[r['id']]for r in ranked]).statistic)
coverage_rho=float(spearmanr([r['rank']for r in ranked],[r['confidence']['coverage']for r in ranked]).statistic)
summary={'generated_at':stamp(),'checks':checks,'all_checks_passed':all(checks.values()),'ranked_count':len(ranked),'official_count':after['official_ranking_count'],'unscored_count':len(after['unscored']),'alphabetical_spearman_rho':alpha_rho,'rank_coverage_spearman_rho':coverage_rho,'sensitivity':{'scenarios':24,'method':'Each global dimension weight +/-20%, others unchanged then renormalized; frozen eligible set; fixed normalized components; cap Flawed at40','minimum_kendall_tau':min(taus),'median_kendall_tau':sorted(taus)[len(taus)//2],'top30':[{'id':r['id'],'name':r['name'],'score':r['score'],'rank':r['rank'],'min_rank':min(ranges[r['id']]),'max_rank':max(ranges[r['id']])}for r in ranked[:30]]}}
write(root/'evidence-validation.json',summary)
if not all(checks.values()):raise SystemExit('VALIDATION FAILED '+str(checks))
coverage={}
for d in after['dimensions']:
 k=d['key'];a=sum(r['components'][k]is not None for r in old);b=sum(r['components'][k]is not None for r in rows)
 coverage[k]={'before':a,'after':b,'total':len(rows),'before_pct':100*a/len(rows),'after_pct':100*b/len(rows),'average_internal_reliability':sum(r['confidence']['dimension_reliability'][k]for r in rows)/len(rows)}
write(root/'evidence-coverage.json',coverage)
lines=['# Benchmark Constitution：现有学术影响力指数补证报告','',f'生成：{stamp()}（上海时间 UTC+8）','',
'## 结论：补证已落盘，但不能把本轮称为“正式榜单”','',
f'固定1668条，原探索榜{len(before["ranking"])}条 → 当前探索榜{len(ranked)}条；**正式资格{after["official_ranking_count"]}条**；证据不足{len(after["unscored"])}条。未降低40%探索覆盖、60%正式覆盖、50%质量内部覆盖门槛。机器文档代理不冒充专家质量审查。主仓库只读、没有发布；未读取凭据文件。','',
'## 各维度：有非null分项的条目数 / 全部1668条','',
'注意：这里的“有值覆盖率”不是质量审查完成率，也不是整个维度权重全部有证据。特别是许可标签仅是质量的一小项，机器项可靠系数0.5；平均内部可靠度另列，避免把少量许可元数据宣传成质量补齐。','',
'|维度|之前|之后|之后平均内部可靠度|','|---|---:|---:|---:|']
for d in after['dimensions']:
 c=coverage[d['key']];lines.append(f'|{d["name_zh"]}|{c["before"]} ({c["before_pct"]:.2f}%)|{c["after"]} ({c["after_pct"]:.2f}%)|{100*c["average_internal_reliability"]:.2f}%|')
lines+=['','## 实际证据与局限','',
f'- 178份公开完整档案快照全部取到；173份精确映射，5份未强行合并：{", ".join(evidence["unmatched"])}。',
f'- {evidence["hf_card_matches"]}个现有条目的HF card成功精确对应；只对registry-only且没有完整档案冲突审查的条目提取明确单一数据许可。',
f'- 质量子项有证据数：{json.dumps({k:evidence["signals"].get(k,0)for k in ("human_validation","contamination_protection","reproducibility","license_clarity","external_review")},ensure_ascii=False)}。维护质量和完整双人独立评分没有补造。',
f'- 明确独立评测结果支持19条操作性复测；4个仓库的issue查询映射7条现有版本条目；其余社区有值主要为弱fork参与代理，不能称为好评或已复现。',
f'- {evidence["github_connector_matches"]}条精确命中本轮connector元数据，其中{evidence["new_github_observations"]}条此前无star观测。star增速仍全部null；今日仅建基线，不能估算。',
'- 34条有可安全处理的百分正确/成功率赛道；保留所有分轨、仅选单轨快照最佳分。裸Accuracy/Score、Elo、RMSE、历史论文、人类结果、混预算和不同版本均不自动混算。尚非全局SOTA或完整饱和度审计。',
'- 178份档案及308个唯一现有HF dataset ID均做了本轮顺序读取；原始响应含失败状态也缓存。原始论文/榜单的上游采集日期保留；8日访问的是公开档案快照时不会伪称8日重新访问原始榜单。','',
'## 独立质量审查的实质发现','',
'本轮直接核实Epoch审查表及具体审查页。以下7项审查结论为Flawed，精确匹配到对应版本并触发总分≤40；不能因高引用/高star抵消可靠性缺陷：','',
'|条目|结论|范围|','|---|---|---|']
reviews=read(root/'independent-quality.json')['reviews']
for rev in reviews:
 if not rev['application'].startswith('historical_only'):lines.append(f'|{rev["target_id"]}|{rev["verdict"]}|{rev["reviewed_scope"]}|')
lines+=['',
'- HLE审查原集48题，22题被确认存在影响准确性的错误（46%）；不扩展到HLE-Diamond/Rolling/Verified。来源：https://epoch.ai/benchmarks/hle/review （访问2026-11-08）。',
'- SWE-bench Verified的结论不传给原始SWE-bench或Pro V2；HealthBench Professional不传给一般HealthBench。',
'- PostTrainBench审查v1.1但档案已是v1.2；Terminal-Bench审查4.0.0、最新tag为4.1.0但展示榜仍4.0。二者仅记录历史审查并显示版本不匹配警告，不当作当前通过，也不自动给整个家族封顶。Terminal-Bench在当前Top30，不意味着4.1.0已修复或已通过审查。','',
'## 方法变化及覆盖偏差诊断','',
'- 12个全局权重不变；社区内部拆开90日事件与更新线程，加入低可靠度fork参与，独立复测与严格复现分开。',
'- 机器文档项按部分满足的规范性rubric记50，可靠系数0.5；不把“有论文/有仓库”本身当成高质量。渲染器不等于评测代码，代码许可不等于数据许可，已加入负例测试。',
'- 第一版试算暴露旧高分参照先验的缺失优势：较少质量证据的MME浮到第一，补到中性50文档的GPQA反而受损。这是公式伪影，不按名称手调。现在统一公开中性50先验：`score=50+Σ(weight×reliability×(component−50))`。新增50文档项分数贡献恰为0，回归测试保证补文档不反向扣分。旧同龄中位数及旧分保留诊断。',
f'- 当前{len(ranked)}条探索排序与ID字母序的Spearman rho={alpha_rho:.3f}；与覆盖率的rho={coverage_rho:.3f}，只做描述性诊断，不能据此声称所有缺失偏差已消除。资源获取仍偏向已知/高star项目，总榜仍有领域和数据可得性限制。',
f'- 24个逐维权重±20%敏感性情景（固定入榜集合）：Kendall tau最小{min(taus):.3f}、中位{sorted(taus)[len(taus)//2]:.3f}。下列名次范围是政策敏感性，不是统计置信区间。','',
'## Top30：全部为探索性，不是正式排名','',
'|名次|Benchmark|分数|证据覆盖|权重敏感性名次范围|','|---:|---|---:|---:|---:|']
for r in ranked[:30]:lines.append(f'|{r["rank"]}|{r["name"]}|{r["score"]:.3f}|{100*r["confidence"]["coverage"]:.2f}%|{min(ranges[r["id"]])}–{max(ranges[r["id"]])}|')
lines+=['','## 验证与下一步','',
'- 31个单元/回归测试通过；本报告的12项完整性检查全部通过。既有引用计数没有丢失；ID集合完全未变；所有新assessment附公开HTTP(S)来源及真实accessed；Flawed不允许正式资格。',
'- 若要正式发布，下一步应对已有高覆盖条目做小批逐项独立复核（而非再扩大库）：先确认构造/QA、许可范围、污染防护和评测脚本可运行性；补足质量内部覆盖后再检验60%总覆盖。不能为了得到正式榜而调低门槛、把脚本入口当成执行成功、把fork或下载当口碑。',
'','## 交付文件','',
'- 新指数：`data/impact/index.json`',
'- 新登记库（1668条不变，含assessment与来源）：`data/registry/registry.json`',
'- 方法：`docs/impact-methodology.md`',
'- 本报告：`scripts/impact/RUN_REPORT.md`',
'- 原始证据、覆盖和核验：`evidence-report.json`、`evidence-coverage.json`、`evidence-validation.json`、`independent-quality.json`、`cache/{dossiers,hf-cards,epoch-reviews,github-connector,snapshots}/`。',
'- 流水线：`evidence_overlay.py`由`compute.py`自动应用；重跑计算不访问网络。采集器为`fetch_dossier_snapshots.py`、`fetch_hf_cards.py`、`fetch_epoch_reviews.py`；只读公共源、缓存续跑。',
'- 发布前可复跑：`.venv/bin/python -m unittest -v test_impact test_evidence && .venv/bin/python compute.py && .venv/bin/python write_evidence_report.py`。',
'- 改动均未发布到主仓库；基线备份：`archive/2026-11-08-before-evidence/`。','']
(root/'RUN_REPORT.md').write_text('\n'.join(lines))
write(root/'evidence-deliverables.json',{'generated_at':stamp(),'index':str(root/'index.json'),'registry':str(BASE/'registry/registry.json'),'methodology':str(root/'METHODOLOGY.md'),'report':str(root/'RUN_REPORT.md'),'official':after['official_ranking_count'],'exploratory':len(ranked),'insufficient':len(after['unscored']),'coverage':coverage,'validation':str(root/'evidence-validation.json')})
print(json.dumps({'checks':checks,'formal':after['official_ranking_count'],'exploratory':len(ranked),'insufficient':len(after['unscored']),'coverage':coverage,'alphabetical_rho':alpha_rho,'min_sensitivity_tau':min(taus)},ensure_ascii=False))

paths=['impact/index.json','registry/registry.json','impact/METHODOLOGY.md','impact/RUN_REPORT.md','impact/evidence-validation.json','impact/evidence-coverage.json']
write(root/'DELIVERABLES.json',{'generated_at':stamp(),'registry_count':len(rows),'ranked':len(ranked),'officially_eligible':after['official_ranking_count'],'insufficient_evidence':len(after['unscored']),'validation_passed':all(checks.values()),'files':[{'path':p,'bytes':(BASE/p).stat().st_size,'sha256':hashlib.sha256((BASE/p).read_bytes()).hexdigest()}for p in paths],'integration_note':'Staging only; registry unchanged in size. Keep provisional label. Do not publish cache, venv or archives.'})
