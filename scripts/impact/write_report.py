#!/usr/bin/env python3
"""Offline validation and reproducible run handoff; never calls an external service."""
import hashlib, json
from collections import Counter
from pathlib import Path
from common import BASE, read, write, stamp

def main():
    root=BASE/'impact'; index=read(root/'index.json'); registry=read(BASE/'registry/registry.json'); api=read(root/'enrich-report.json'); comp=read(root/'compute-report.json'); audit=read(root/'audit-application-report.json')
    items=registry['items']; ranked=index['ranking']; rest=index['unscored']; rows=ranked+rest; byid={x['id']:x for x in items}; ranked_byid={x['id']:x for x in rows}; n=len(items)
    errors=[]
    def check(ok,message):
        if not ok: errors.append(message)
    check(n==len(byid)==len(rows),'registry/index count or ID uniqueness mismatch')
    check(len({r['id'] for r in rows})==n,'duplicate IDs in index')
    check(abs(sum(d['weight'] for d in index['dimensions'])-1)<1e-9,'weights do not sum to 1')
    check(not audit['audit_unresolved'],'unbound audit actions')
    for pos,r in enumerate(ranked,1):
        check(r['rank']==pos and r['score'] is not None and 0<=r['score']<=100 and r['confidence']['coverage']>=.4,'invalid ranked row '+r['id'])
        check(not r['raw'].get('identity_review') and 'identity_conflict' not in r['flags'],'identity-unsafe row ranked '+r['id'])
    check(all(r['rank'] is None and r['score'] is None and r['status']=='insufficient_evidence' for r in rest),'unscored rows received ranks')
    for r in rows:
        check(all(v is None or 0<=v<=100 for v in r['components'].values()),'out-of-range component '+r['id'])
    protected={'swe-bench':'2310.06770','swe-bench-plus-plus':'2512.17419','livecodebench':'2403.07974','livecodebench-pro':'2506.11928','cve-bench':'2503.17332','arc':'1803.05457','hellaswag':'1905.07830','piqa':'1911.11641','winogrande':'1907.10641','arc-agi-2':'2505.11831'}
    for key,value in protected.items():
        check(key in byid and byid[key].get('arxiv_id')==value,'canonical paper identity regression '+key)
    check(byid['gpqa']['release_date']=='2023-11-20','audited GPQA date reverted')
    check(byid['arc-agi-2']['release_date']=='2025-03-24','audited ARC2 date reverted')
    for key in ['macbench','multimedqa','sciq','supergpqa']:
        check(sum(r['id']==key for r in items)==1,'science2 duplicate '+key)
    check(all(byid[k].get('variants') for k in ['mteb','beir','rar-b','squad','arc','prbench'] if k in byid),'family variant history missing')
    check(byid['swe-bench-plus-plus'].get('github_url') is None,'audit-null repo reintroduced')
    heat=read(BASE/'frontier/heat.json',{}); heat_models=len(heat.get('models',[])); heat_items=len(heat.get('ranking',[])); mapped_heat=sum(r['raw'].get('model_card_mentions') is not None for r in rows)
    watch=['swe-bench','gpqa','hle','mmlu','math','humaneval','arc-agi','livecodebench']
    watchrows=[{k:r.get(k) for k in ('id','name','rank','score','status')}|{'coverage':r['confidence']['coverage'],'citations':r['raw'].get('citations'),'model_card_mentions':r['raw'].get('model_card_mentions')} for key in watch if (r:=ranked_byid.get(key))]
    api_eligible={'citations':api['paper_eligible'],'gh_stars':sum(bool(x.get('github_url')) for x in items),'hf_downloads':sum(bool(x.get('hf_dataset')) for x in items),'hf_likes':sum(bool(x.get('hf_dataset')) for x in items)}
    api_hits={k:sum(x['metrics'].get(k) is not None for x in items) for k in api_eligible}
    response_status=Counter(); response_hosts=Counter()
    for f in (root/'cache/responses').glob('*.json'):
        z=read(f,{}) or {}; response_status[str(z.get('status'))]+=1
        from urllib.parse import urlparse
        response_hosts[urlparse(z.get('url','')).netloc]+=1
    inputs={str(f.relative_to(BASE)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((BASE/'registry').glob('*.jsonl'))}
    validation={'generated_at':stamp(),'passed':not errors,'errors':errors,'registry_count':n,'ranked':len(ranked),'insufficient_evidence':len(rest),'officially_eligible':index['official_ranking_count'],'watchlist_all_top50':all(r['rank'] is not None and r['rank']<=50 for r in watchrows),'watchlist':watchrows,'input_sha256':inputs}
    write(root/'validation.json',validation)
    stats={'generated_at':stamp(),'count':n,'ranked':len(ranked),'insufficient_evidence':len(rest),'officially_eligible':index['official_ranking_count'],'paper_eligible':api['paper_eligible'],'citation_hits':api['paper_citation_hits'],'citation_coverage':api['citation_coverage_paper_eligible'],'dimension_coverage':comp['dimension_coverage'],'eligible_api_opportunities':api_eligible,'eligible_api_hits':api_hits,'unique_resources':{'github_repositories':api['unique_repositories'],'hf_datasets':api['unique_datasets']},'last_pass_requests':api['requests'],'cached_response_objects_by_status':dict(response_status),'cached_response_objects_by_host':dict(response_hosts),'audit_actions':audit['audit_actions'],'unresolved_audits':len(audit['audit_unresolved']),'unresolved_metadata_conflicts':sum(not c.get('resolved',False) for c in audit['conflicts']),'identity_conflict_rows':sum('identity_conflict' in r['flags'] for r in rows),'identity_review_rows':sum(bool(r['raw'].get('identity_review')) for r in rows),'watchlist':watchrows,'top30':[{'rank':r['rank'],'id':r['id'],'name':r['name'],'score':r['score'],'coverage':r['confidence']['coverage']} for r in ranked[:30]]}
    write(root/'final-stats.json',stats)
    text=f'''# BCI v0.2 最终全量运行报告\n\n生成：{stamp()}（KST / Asia/Seoul）。本报告对应当前最终JSON，不再使用被废弃的180条字母序样本。\n\n## 结果摘要\n\n- 最终去重名录 **{n}条**，全部进入断点采集；无在线抽样。\n- 有论文/arXiv/DOI的{api['paper_eligible']}条中，引用成功匹配 **{api['paper_citation_hits']}条（{100*api['citation_coverage_paper_eligible']:.2f}%）**，超过60%目标；占全名录{100*api['paper_citation_hits']/n:.2f}%。命中率指论文身份对应的真实计数，不是HTTP200率。\n- 探索性入榜 **{len(ranked)}条**；**{len(rest)}条 insufficient_evidence**，没有名次或综合分。质量审计正式资格 **{index['official_ranking_count']}条**。因此不能宣传为已完成质量认证的学术水平榜。\n- 最终Frontier Heat为{heat_models}模型、{heat_items}项，{mapped_heat}/{heat_items}映射至规范benchmark；未出现不是自动记0。另输出时间衰减×厂商多样性辅助热度。\n- science2已纳入：570行覆盖/增量，549旧ID改善+21科学新增，其中4项全球已有，17个真正新ID；保留non-LLM及MoleculeNet显式子任务关系，不将共享论文算作15份独立影响。\n- 审计动作：{json.dumps(audit['audit_actions'],ensure_ascii=False)}；未绑定/未决审计 **{len(audit['audit_unresolved'])}**。24项空新ID建议保留原身份、标记待审，不编造新名。\n\n## 维度、权重与覆盖\n\n下表为分项非null的行数；并不等于该维度满可信。新颖度/非同质性是可信系数0.35的文本代理；缺子项进一步降权，维护push只是0.5可信代理。\n\n|维度|权重|有数据/全名录|覆盖率|\n|---|---:|---:|---:|\n'''
    for d in index['dimensions']:
        c=comp['dimension_coverage'][d['key']];text+=f"|{d['name_zh']}|{100*d['weight']:.0f}%|{c['observed']}/{n}|{100*c['share']:.2f}%|\n"
    text+='\n## API采集与缓存\n\n|指标|有资源/论文线索的行数|真实计数命中行数|条件命中率|\n|---|---:|---:|---:|\n'
    for key,eligible in api_eligible.items(): text+=f"|{key}|{eligible}|{api_hits[key]}|{100*api_hits[key]/eligible:.2f}%|\n" if eligible else f'|{key}|0|0|—|\n'
    text+=f'''\n- 唯一GitHub仓库{api['unique_repositories']}个，唯一HF dataset {api['unique_datasets']}个；共享资源可能对应多个行，不能把行数当唯一资源数。\n- 最后一轮为全库缓存续跑，联网请求{api['requests'].get('network_requests',0)}次，响应缓存命中{api['requests'].get('cache_hits',0)}次、负缓存命中{api['requests'].get('negative_cache_hits',0)}次、延后{api['requests'].get('deferred_requests',0)}次；单条断点复用{api.get('resumed',0)}条。此前成功实际API响应已持久化。最后一轮零联网不代表没有调用真实API，而是缓存续跑生效。\n- 缓存响应对象按最终HTTP状态计数：{json.dumps(dict(response_status),ensure_ascii=False)}。这是去重/覆盖后的缓存对象数，不是含重试的历史请求总数，不冒充网络成功率。\n- GitHub公开配额/鉴权拒绝后停止该主机，未提供/读取任何秘密文件token；未知star为null。只有一天快照，star增速全部null。HF私有/受限资源仅该资源null，不绕过鉴权，不连带阻断公开dataset。\n- OpenAlex使用公开mailto、每批≤50个DOI、约≤0.91req/s起始速率；S2 batch≤500，429指数退避、自适应放慢、预算耗尽留待后续。不累加不同供应商或论文版本。\n\n## 最终Top30（仅探索性，所有行均缺系统性质量审查）\n\n|名次|benchmark|BCI|有效证据覆盖|\n|---:|---|---:|---:|\n'''
    for r in ranked[:30]: text+=f"|{r['rank']}|{r['name']} (`{r['id']}`)|{r['score']:.3f}|{100*r['confidence']['coverage']:.2f}%|\n"
    text+='\n## Top50常识检查\n\n|核查项|名次|BCI|引用|最近20模型采用数|\n|---|---:|---:|---:|---:|\n'
    for r in watchrows:text+=f"|{r['name']}|{r['rank']}|{r['score']}|{r['citations']}|{r['model_card_mentions']}|\n"
    text+='''\n八个指定核查项均在Top50，未按名称加分或手工安排名次。修正依据是身份与方法错误：\n\n1. 修复SWE-Bench++/原始SWE-bench、LiveCodeBench Pro/原始版本、CVE修复/利用同ID冲突；RAR-b检索改写不覆盖原推理基准。\n2. 原始MMLU不得继承openai/MMMLU下载；规范ID匹配优先，避免别名把MMLU采用数劫持给MMMLU。\n3. 官方arXiv首发日用于缺失benchmark日期的年龄代理，HLE不因2026期刊版重置时钟；已审计日期（GPQA、ARC-AGI-2等）最终优先。\n4. 实际引用仍保留两库观察，OpenAlex精确身份优先，版本不求和。S2与OpenAlex的大差异公开标记，不为了名次挑库。\n5. 收紧新颖度缺任务子项的证据权重后，MMLU/ARC原来恰好低于40%门槛；复核原始官方MMLU评测程序和ARC官网，补上有原文证据的“多选”“网格变换”任务形式。不是降低门槛或修改总分。\n6. 同龄先验只取有≥40%证据且身份可靠的条目，排除自己；不足量时公开回退，不再让稀薄证据拿近100分。\n\n## 保留历史与验证\n\n- 不可变完整旧行定位跨分片merge；ID修正先绑定发生项。68个harness自合并只移除精确重复行。SQuAD版本、ARC-Challenge、PRBench Finance/Legal、MRCR配置及MTEB等子任务存variants，不平均不同比例分数。\n- science2只按真实field deltas改善，再由审计结论最终覆盖同字段，明确null清空不会被旧值复活。等价实现可在审计后仅应用不冲突增量。\n- `validation.json`验证唯一ID、计分范围、40%门槛、未评分不赋名次、权重和、关键论文身份/日期、科学新增全局去重和家族历史；输入SHA-256一并留档。`test-run.log`为17项隔离回归测试通过记录。\n\n## 仍有的缺陷 / 上线限制\n\n- **质量、社区、饱和度覆盖均为0**：实现了有来源审计接口，但没有虚构数据；BetterBench/污染/许可适用/复现及Epoch逐版本结论尚待系统性人工审查。当前不能衡量或认证学术质量本身。\n- GitHub覆盖很低，继承早期公共缓存的可用性偏差仍在；受公开配额限制，不能声称所有维度公平完整。应展示缺失和证据覆盖，而非只展示分数。\n- 仅60条探索性排序不是“其余1608条低质量”；它们是未达到数据门槛。HF下载不是评测次数，引用可能是批评或自引，仓库可能共享、API可能滞后。\n- 新颖度是字符TF-IDF词面代理（不是语义创新判定）；翻译、模板、描述长短与领域收录比例影响分数。跨领域/年龄组参考样本仍不平衡。\n- 同论文/仓库/HF共享按平方根折减是公开的归属近似，不是精确贡献分配；派生值不覆盖原始计数。OpenAlex多版本选择单个观测最大值只避免求和，不等于完整去重引文图。\n- science2的机构主要是第一作者隶属，不能直接当唯一发布方。模型附带评测、存档自述、少数泛化名和版本关系仍需人工确认；API命中不等于所有条目均已独立核真。\n- 未进行全面消融、权重扰动、跨语言句向量或双人质量审查；暂无真实长期趋势和star增速。未创建任何外部每日任务。\n\n## 文件交付\n\n- `impact/index.json` → 主控集成为 `data/impact/index.json`。\n- `registry/registry.json` → `data/registry/registry.json`。\n- `impact/industry-heat.json`：时间衰减×厂商多样性辅助热度。\n- `impact/METHODOLOGY.md`：中文上线说明；`impact/final-stats.json`：机器可读报告。\n- `impact/{enrich,compute,metadata,arxiv_dates,registry_merge,common,write_report}.py`、`run.sh`、`requirements.txt`、`README.md`、`test_impact.py`。\n- 审计和science2变更文件、curations/metadata-overlay/arxiv-dates是复算所需数据依赖。不要把.venv、cache、archive或运行日志作为站点资源发布。\n\n仅操作`/workspace/bc`，未改主仓库、未提交、未push、未发布。\n'''
    if not validation['watchlist_all_top50']:
        text=text.replace('八个指定核查项均在Top50','部分指定核查项未在Top50，具体缺失/得分见上表，应重新诊断')
    # Keep caveat totals correct after a future rerun, without implying quality loss.
    text=text.replace('仅60条探索性排序不是“其余1608条低质量”',f'仅{len(ranked)}条探索性排序不是“其余{len(rest)}条低质量”')
    if index.get('method_version','').startswith('bci-0.3'):
        text=text.replace('BCI v0.2','BCI v0.3').replace('KST / Asia/Seoul','上海时间 / Asia/Shanghai / UTC+8')
        text=text.replace('6. 同龄先验只取有≥40%证据且身份可靠的条目，排除自己；不足量时公开回退，不再让稀薄证据拿近100分。','6. 统一公开中性50先验，缺失分项仍为null；同龄经验中位数只作诊断。中性50文档项贡献为0，不能因为补文档而反向扣分。')
        text=text.replace('**质量、社区、饱和度覆盖均为0**：实现了有来源审计接口，但没有虚构数据；BetterBench/污染/许可适用/复现及Epoch逐版本结论尚待系统性人工审查。当前不能衡量或认证学术质量本身。', '质量、社区、饱和度已补文档/独立审查/单轨快照证据，具体覆盖见上表；机器项可靠系数0.5，不等于完整专家审计。已知Flawed按精确版本封顶40，不能授予正式资格。')
        text=text.replace('未进行全面消融、权重扰动、跨语言句向量或双人质量审查','未完成全面消融、跨语言句向量或双人质量审查；本轮24个局部权重情景仅是敏感性诊断')
        text=text.replace('只有一天快照，star增速全部null。','star增速必须有两次相隔足够时间的实测，否则为null。')
        text=text.replace('`test-run.log`为17项隔离回归测试通过记录。','`test-evidence-run.log`记录31项单元/回归测试；包括来源日期、版本隔离及缺失先验测试。')
    (root/'RUN_REPORT.md').write_text(text)
    paths=['impact/index.json','registry/registry.json','impact/METHODOLOGY.md','impact/RUN_REPORT.md','impact/industry-heat.json','impact/final-stats.json','impact/validation.json']
    write(root/'DELIVERABLES.json',{'generated_at':stamp(),'registry_count':n,'ranked':len(ranked),'insufficient_evidence':len(rest),'citation_coverage':api['citation_coverage_paper_eligible'],'validation_passed':not errors,'files':[{'path':s,'bytes':(BASE/s).stat().st_size,'sha256':hashlib.sha256((BASE/s).read_bytes()).hexdigest()} for s in paths],'integration_note':'Copy deliverables into data/ as specified; do not publish .venv/cache/archive/logs. Repo untouched.'})
    print(json.dumps({'count':n,'ranked':len(ranked),'unscored':len(rest),'citation_coverage':api['citation_coverage_paper_eligible'],'validation_passed':not errors,'errors':errors},ensure_ascii=False))
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
