#!/usr/bin/env python3
"""BCI 0.2: evidence-aware, age-normalized multi-dimensional research index.
All inferred quantities are explicitly derived, never raw API observations.
"""
import argparse, hashlib, math
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from common import BASE, now, stamp, read, write, date, norm, merge_registry

DIMENSIONS=[
 ('citations_total','引用积累',.10,'论文引用总数；领域内对数尺度与百分位混合'),
 ('citation_velocity','同龄引用速度',.15,'年龄平滑的月引用速度；领域×年龄组比较'),
 ('github','代码生态',.08,'仓库 star 与实测近月净增速；共享仓库降权'),
 ('huggingface','数据使用',.05,'HF 最近30日下载与点赞；对数尺度与分位数'),
 ('model_adoption','前沿模型采用',.10,'最近20模型报告的去重采用次数'),
 ('evaluator_adoption','评测机构采用',.08,'独立机构实际采用，不把提及或负面审查当采用'),
 ('community','独立社区反馈',.05,'去重讨论、90日issue活跃与第三方复现'),
 ('novelty','研究新颖度（代理）',.12,'相对更早benchmark的文本距离、领域与任务形式稀有度'),
 ('quality','方法与工程质量',.18,'可核验人工审核、污染防护、复现、许可、维护、外审'),
 ('distinctiveness','非同质性',.04,'近邻相似度惩罚；不是语义创新的裁定'),
 ('headroom','未饱和与区分度',.03,'有明确上下界的SOTA余量与头部区分能力'),
 ('maintenance','时效与维护',.02,'最近有效更新的时间衰减；代码push仅代理')]
WEIGHTS={x[0]:x[2] for x in DIMENSIONS}

def avg(values):
    xs=[(v,w) for v,w in values if v is not None]
    return sum(v*w for v,w in xs)/sum(w for _,w in xs) if xs else None

def scale(v, peers):
    if v is None or not peers: return None
    peers=np.asarray([max(0,float(t)) for t in peers],dtype=float); value=max(0,float(v))
    # All zero means observed absence, not a 50th-percentile success.
    if not np.any(peers): return 0.0
    ecdf=(np.sum(peers<value)+.5*np.sum(peers==value))/len(peers)
    p95=float(np.quantile(np.log1p(peers),.95)); logarithm=min(1,math.log1p(value)/p95) if p95 else 0
    return 100*(.5*ecdf+.5*logarithm)

def bucket(months):
    if months is None: return None
    return next((i for i,t in enumerate((3,6,12,24,60)) if months<t),5)

def peer_indices(items,i,key,age=False):
    valid=[j for j,t in enumerate(items) if t['metrics'].get(key) is not None]
    domain=[j for j in valid if items[j]['domain']==items[i]['domain']]
    if age:
        b=bucket(items[i]['metrics'].get('age_months'))
        if b is None: return [],'age_unknown'
        same=[j for j in domain if bucket(items[j]['metrics'].get('age_months'))==b]
        if len(same)>=20: return same,'domain_age'
        same=[j for j in valid if bucket(items[j]['metrics'].get('age_months'))==b]
        if len(same)>=20: return same,'age_only'
        return same,'age_small_sample'
    if len(domain)>=20: return domain,'domain'
    return valid,'global_small_domain'

def audited(x,field):
    """Accept subjective/external metrics only with per-observation public evidence."""
    obj=x.get('assessment',{}).get(field)
    if isinstance(obj,dict) and 'value' in obj and any(isinstance(t,dict) and str(t.get('url','')).startswith(('https://','http://')) and date(t.get('accessed')) for t in obj.get('sources',[])): return obj['value']
    return None

def novelty(items):
    valid=[]; texts=[]
    for i,x in enumerate(items):
        m=x['metrics']; abstract=m.get('paper_abstract') or ''
        description=x.get('description_zh') or x.get('description') or ''
        text=abstract if len(abstract)>=100 else description
        if len(text.strip())>=16:
            valid.append(i); texts.append(text+' '+str(x.get('subdomain') or '')+' '+str(x.get('task_format') or ''))
            m['novelty_text_basis']='paper_abstract' if len(abstract)>=100 else 'registry_description'
    if len(valid)<2: return
    matrix=TfidfVectorizer(analyzer='char',ngram_range=(2,4),sublinear_tf=True,min_df=1,max_features=40000).fit_transform(texts)
    # Cache pair similarities once instead of repeated vector search/date parsing.
    sims=(matrix @ matrix.T).toarray().astype(np.float32)
    np.fill_diagonal(sims,-1)
    releases=[]
    for i in valid:
        dt=date(items[i].get('release_date') or items[i]['metrics'].get('first_submitted_at') or items[i]['metrics'].get('paper_date'))
        releases.append(dt.timestamp() if dt else np.nan)
    releases=np.asarray(releases); domains=np.asarray([str(items[i].get('domain')) for i in valid]); tasks=np.asarray([str(items[i].get('task_format')) for i in valid])
    for row,i in enumerate(valid):
        x=items[i]; m=x['metrics']; nearest=np.argsort(-sims[row])[:3]
        similarity=float(max(0,sims[row].max()))
        m['nearest_similarity']=min(1,similarity); m['nearest_benchmarks']=[items[valid[j]]['id'] for j in nearest]
        m['distinctiveness_score']=100*(1-max(0,similarity-.8)/.2)
        if np.isnan(releases[row]): continue
        earlier=np.flatnonzero(releases<releases[row])
        if not len(earlier): continue
        max_similarity=float(max(0,sims[row,earlier].max())); text_score=100*(1-max_similarity)
        task=x.get('task_format'); domain=x.get('domain')
        tr=100*(1-float(np.mean(tasks[earlier]==str(task)))) if task else None
        dr=100*(1-float(np.mean(domains[earlier]==str(domain)))) if domain else None
        m.update(novelty_score=avg([(text_score,.7),(tr,.15),(dr,.15)]),novelty_text_distance=1-max_similarity,novelty_prior_corpus_size=int(len(earlier)),novelty_task_rarity=tr,novelty_domain_rarity=dr)

def frontier(items,path):
    heat=read(path); ranking=heat.get('ranking',[]) if isinstance(heat,dict) else []
    models={m['id']:m for m in (heat or {}).get('models',[])}
    # Canonical IDs win over aliases. A parent alias must never steal another version's adoption.
    aliases={norm(x['id']):x['id'] for x in items}
    candidates={}
    for x in items:
        for n in [x['name']]+x.get('aliases',[]):
            key=norm(n)
            candidates.setdefault(key,set()).add(x['id'])
    for key,ids in candidates.items():
        if key not in aliases and len(ids)==1: aliases[key]=next(iter(ids))
    mapped={}
    for h in ranking:
        match=aliases.get(norm(h.get('benchmark_id') or h.get('id'))) or aliases.get(norm(h.get('name')))
        if match: mapped[match]=h
    rows=[]
    for x in items:
        m=x['metrics']; m.setdefault('provenance',[]); h=mapped.get(x['id']); m['model_card_mentions']=None; m['industry_heat']=None
        if h:
            mids=list(dict.fromkeys(h.get('models',[]))); m['model_card_mentions']=len(mids) if mids else h.get('count')
            sources=[s for mid in mids for s in models.get(mid,{}).get('sources',[])]+h.get('sources',[])
            m['provenance'].extend({**source,'fields':['model_card_mentions'],'model_ids':mids,'input_file':str(path)} for source in sources if isinstance(source,dict) and source.get('url'))
            weighted=Counter(); age_missing=False
            for mid in mids:
                model=models.get(mid,{}); release=date(model.get('release_date')); org=model.get('organization')
                if release and org: weighted[str(org)]+=2**(-max(0,(now()-release).days)/90)
                else: age_missing=True
            n=len(models)
            if weighted and n and not age_missing:
                s=sum(weighted.values()); ent=-sum((v/s)*math.log(v/s) for v in weighted.values()); eff=math.exp(ent)
                all_orgs={str(t['organization']) for t in models.values() if t.get('organization')}; vmax=len(all_orgs)
                div=.5+.5*min(1,eff/vmax) if vmax else None
                m['industry_heat']=100*s/n*div if div is not None else None
                rows.append({'id':x['id'],'count':m['model_card_mentions'],'score':m['industry_heat'],'weighted_mentions':s,'effective_vendors':eff,'diversity_factor':div})
        # Absence is not zero unless the collector explicitly certifies exhaustive mapping.
        elif heat and heat.get('coverage_complete') is True:
            m['model_card_mentions']=0
    rows.sort(key=lambda r:-r['score'])
    for i,row in enumerate(rows,1): row['rank']=i
    return {'generated_at':stamp(),'method_version':'frontier-heat-weighted-0.1','source_present':bool(heat),'ranking':rows}

def compute(items,heat_path):
    for x in items:
        m=x.setdefault('metrics',{}); m.setdefault('provenance',[])
        for source in m['provenance']:
            ids=source.pop('queried_ids',None)
            if ids is not None: source['batch_ids_count']=len(ids)
        for field,obs in x.get('assessment',{}).items():
            if audited(x,field) is not None:
                for source in obs.get('sources',[]):
                    entry={**source,'fields':[field],'kind':'audited_assessment'}
                    if entry not in m['provenance']: m['provenance'].append(entry)
        release_value=x.get('release_date') or m.get('first_submitted_at') or m.get('paper_date')
        release=date(release_value)
        months=(now()-release).total_seconds()/86400/30.4375 if release and release<=now() else None
        m['age_months']=months
        m['release_date_basis']='registry' if x.get('release_date') else 'arxiv_first_submission_proxy' if m.get('first_submitted_at') else 'paper_api_proxy' if m.get('paper_date') else None
        m['release_date_precision']='month_midpoint' if len(str(release_value or ''))==7 else 'year_midpoint' if len(str(release_value or ''))==4 else 'day_or_missing'
        cit=m.get('citations'); m['citations_per_month']=cit/months if cit is not None and months and months>0 else None
        m['citation_velocity_smoothed']=cit/(months+3) if cit is not None and months is not None else None
        m['evaluator_adoptions']=audited(x,'evaluator_adoptions')
        if isinstance(m['evaluator_adoptions'],list): m['evaluator_adoptions']=len(set(m['evaluator_adoptions']))
        for field in ('community_discussions','issue_activity_90d','third_party_reproductions'):
            m[field]=audited(x,field)
    from enrich import identifiers
    def paper_key(x):
        a,d=identifiers(x)
        return 'arxiv:'+a.lower() if a else 'doi:'+d if d else str(x.get('paper_url') or '') or None
    paper_counts=Counter(paper_key(x) for x in items if paper_key(x))
    for x in items:
        m=x['metrics']; shared=paper_counts.get(paper_key(x),1); m['paper_shared_registry_entries']=shared
        m['attributed_citations']=m.get('citations')/math.sqrt(shared) if m.get('citations') is not None else None
        m['attributed_citation_velocity']=m['attributed_citations']/(m['age_months']+3) if m['attributed_citations'] is not None and m.get('age_months') is not None else None
    heat=frontier(items,heat_path); novelty(items)
    def canonical_repo(x):
        parsed=urlparse(x.get('github_url') or ''); parts=parsed.path.strip('/').split('/')
        return '/'.join(parts[:2]).removesuffix('.git').lower() if parsed.hostname in ('github.com','www.github.com') and len(parts)>=2 else None
    repositories=Counter(canonical_repo(x) for x in items if canonical_repo(x))
    hf_resources=Counter(x.get('hf_dataset') for x in items if x.get('hf_dataset'))
    results=[]
    for i,x in enumerate(items):
        m=x['metrics']; components={k:None for k in WEIGHTS}; rel={k:0 for k in WEIGHTS}; flags=[]; normalization={}
        def normalized(key,age=False):
            peers,group=peer_indices(items,i,key,age); normalization[key]={'group':group,'n':len(peers)}
            if not peers: return None
            return scale(m.get(key),[items[j]['metrics'][key] for j in peers])
        for d,k in [('citations_total','attributed_citations'),('citation_velocity','attributed_citation_velocity'),('model_adoption','model_card_mentions'),('evaluator_adoption','evaluator_adoptions')]:
            components[d]=normalized(k,d=='citation_velocity'); rel[d]=1 if components[d] is not None else 0
            if d=='citation_velocity' and components[d] is not None:
                n=normalization[k]['n']; rel[d]*=min(1,n/20)
                if n<20: flags.append('small_age_cohort')
        stars=normalized('gh_stars'); growth=normalized('gh_stars_per_month')
        shared=repositories.get(str(m.get('gh_repository','')).lower(),1); m['gh_shared_registry_entries']=shared
        components['github']=avg([(stars,.65),(growth,.35)])
        rel['github']=(.65 if stars is not None else 0)+(.35 if growth is not None else 0)
        if components['github'] is not None:
            components['github']/=math.sqrt(shared)
            if shared>1: flags.append('shared_repository')
        dl=normalized('hf_downloads'); likes=normalized('hf_likes')
        components['huggingface']=avg([(dl,.7),(likes,.3)]); rel['huggingface']=(.7 if dl is not None else 0)+(.3 if likes is not None else 0)
        hf_shared=hf_resources.get(x.get('hf_dataset'),1); m['hf_shared_registry_entries']=hf_shared
        if components['huggingface'] is not None and hf_shared>1:
            components['huggingface']/=math.sqrt(hf_shared); flags.append('shared_hf_dataset')
        comm=[(normalized(k),w) for k,w in [('community_discussions',.2),('issue_activity_90d',.2),('third_party_reproductions',.6)]]
        components['community']=avg(comm); rel['community']=sum(w for v,w in comm if v is not None)
        components['novelty']=m.get('novelty_score'); rel['novelty']=.35*(.7+(.15 if m.get('novelty_task_rarity') is not None else 0)+(.15 if m.get('novelty_domain_rarity') is not None else 0)) if components['novelty'] is not None else 0
        components['distinctiveness']=m.get('distinctiveness_score'); rel['distinctiveness']=.35 if components['distinctiveness'] is not None else 0
        if m.get('nearest_similarity',0)>.8: flags.append('homogeneous')
        if m.get('paper_shared_registry_entries',1)>1: flags.append('shared_paper_attribution')
        q=[]
        for key,w in [('human_validation',.2),('contamination_protection',.2),('reproducibility',.2),('license_clarity',.1),('maintenance_review',.1),('external_review',.2)]:
            v=audited(x,key)
            if v is not None and isinstance(v,(int,float,bool)): q.append((max(0,min(100,float(v)*100 if isinstance(v,bool) else float(v))),w))
        # A GitHub code license does NOT establish the dataset's license.
        components['quality']=avg(q); rel['quality']=sum(w for _,w in q)
        flaw=audited(x,'epoch_verdict')
        if str(flaw).lower()=='flawed': flags.append('flawed')
        # Higher-is-better normalized metric only; unbounded/lower-is-better need manual direction conversion.
        sota=audited(x,'sota_score'); floor=audited(x,'metric_floor'); ceiling=audited(x,'metric_ceiling'); discr=audited(x,'discrimination_score')
        discr=max(0,min(100,discr)) if isinstance(discr,(int,float)) else None
        headroom=None
        if all(isinstance(v,(int,float)) for v in (sota,floor,ceiling)) and ceiling>floor:
            fraction=max(0,min(1,(sota-floor)/(ceiling-floor))); headroom=100*(1-fraction)
            if fraction>=.95: flags.append('saturated')
        components['headroom']=avg([(headroom,.7),(discr,.3)]); rel['headroom']=(.7 if headroom is not None else 0)+(.3 if discr is not None else 0)
        update=audited(x,'last_substantive_update') or m.get('gh_pushed_at') or m.get('hf_last_modified')
        t=date(update)
        if t:
            days=max(0,(now()-t).total_seconds()/86400); components['maintenance']=100*2**(-days/365)
            rel['maintenance']=1 if audited(x,'last_substantive_update') else .5
        evidence_weight=sum(WEIGHTS[k]*rel[k] for k in WEIGHTS if components[k] is not None)
        score=sum(WEIGHTS[k]*rel[k]*components[k] for k in WEIGHTS if components[k] is not None)/evidence_weight if evidence_weight else None
        # Proxy text diversity alone is not evidence of academic impact.
        impact_observed=any(m.get(k) is not None for k in ('citations','gh_stars','hf_downloads','hf_likes','model_card_mentions','evaluator_adoptions','third_party_reproductions'))
        if not impact_observed: score=None; flags.append('no_observed_impact_signal')
        m['identity_review']=x.get('identity_review')
        quality_coverage=rel['quality']; eligible=evidence_weight>=.6 and quality_coverage>=.5 and (components['citations_total'] is not None or components['evaluator_adoption'] is not None)
        if x.get('_identity_conflict'):
            flags.append('identity_conflict'); eligible=False; score=None
        if not eligible: flags.append('provisional')
        if m['release_date_precision'] in ('month_midpoint','year_midpoint'): flags.append('approximate_release_date')
        if m['release_date_basis']=='paper_api_proxy': flags.append('paper_date_proxy')
        if m['release_date_basis']=='arxiv_first_submission_proxy': flags.append('arxiv_first_submission_proxy')
        counts=m.get('citations_by_provider',{})
        if len([v for v in counts.values() if v is not None])>1:
            observed=[v for v in counts.values() if v is not None]
            if max(observed)>2*max(1,min(observed)): flags.append('citation_provider_disagreement')
        if m.get('age_months') is not None and m['age_months']<3: flags.append('early_signal')
        if 'flawed' in flags and score is not None: score=min(score,40)
        if components['novelty'] is not None: flags.append('lexical_novelty_proxy')
        components={k:round(max(0,min(100,v)),3) if v is not None else None for k,v in components.items()}
        m['resource_mapping_status']='registry_asserted_not_independently_verified'; m['derived_at']=stamp(); m['normalization']=normalization
        raw={k:v for k,v in m.items() if k not in ('provenance','normalization')}
        results.append({'rank':None,'id':x['id'],'name':x['name'],'domain':x['domain'],'release_date':x.get('release_date'),'score':round(score,3) if score is not None else None,'observed_score':round(score,3) if score is not None else None,'components':components,'raw':raw,'flags':sorted(set(flags)),'confidence':{'coverage':round(evidence_weight,4),'label':'high' if evidence_weight>=.8 else 'medium' if evidence_weight>=.6 else 'low','quality_coverage':round(quality_coverage,3),'dimension_reliability':rel,'official_rank_eligible':eligible,'note':'覆盖度是证据完备程度，不是统计置信区间'},'provenance':m['provenance'],'normalization':normalization})
    # Evidence coverage shrinkage is a published policy, not hand-adjustment of names.
    anchors=[r for r in results if r['observed_score'] is not None and r['confidence']['coverage']>=.4 and 'identity_conflict' not in r['flags'] and not r['raw'].get('identity_review')]
    for row in results:
        cov=row['confidence']['coverage']; b=bucket(row['raw'].get('age_months'))
        peers=[r for r in anchors if r['id']!=row['id'] and r['domain']==row['domain'] and bucket(r['raw'].get('age_months'))==b]
        group='domain_age'
        if len(peers)<5:
            peers=[r for r in anchors if r['id']!=row['id'] and bucket(r['raw'].get('age_months'))==b]; group='age'
            if len(peers)<10: peers=[r for r in anchors if r['id']!=row['id']]; group='global_supported_fallback'
        prior=float(np.median([r['observed_score'] for r in peers])) if peers else 50.0
        shrunk=cov*row['observed_score']+(1-cov)*prior if row['observed_score'] is not None else None
        if shrunk is not None and 'flawed' in row['flags']: shrunk=min(shrunk,40)
        row['shrinkage']={'alpha':cov,'peer_median':round(prior,3),'peer_group':group if peers else 'neutral_50_fallback','peer_n':len(peers),'formula':'coverage * observed_score + (1-coverage) * age_peer_median'}
        supported=cov>=.4 and row['observed_score'] is not None and 'identity_conflict' not in row['flags'] and not row['raw'].get('identity_review')
        row['confidence']['rank_eligible']=supported
        row['shrunk_score']=round(shrunk,3) if shrunk is not None else None
        row['score']=row['shrunk_score'] if supported else None
        row['status']='ranked_provisional' if supported else 'insufficient_evidence'
        if row['raw'].get('identity_review'): row['flags'].append('identity_unverified')
        if not supported: row['flags']=sorted(set(row['flags']+['insufficient_evidence']))
    results.sort(key=lambda r:(r['score'] is None,-(r['score'] or 0),r['id']))
    for rank,row in enumerate(results,1): row['rank']=rank if row['score'] is not None else None
    return {'generated_at':stamp(),'method_version':'bci-0.2-coverage-shrunk','dimensions':[{'key':k,'name_zh':n,'weight':w,'description_zh':d} for k,n,w,d in DIMENSIONS],'ranking':[r for r in results if r['score'] is not None],'unscored':[r for r in results if r['score'] is None],'minimum_ranking_coverage':.4,'official_ranking_count':sum(r['confidence']['official_rank_eligible'] for r in results),'publication_warning_zh':'覆盖≥40%后方进入探索性排序；分数按覆盖度向同龄可信样本中位数收缩。仍缺人工质量审查，不等于权威学术水平认证。','ranking_status':'provisional_evidence_incomplete' if any('provisional' in x['flags'] for x in results) else 'audited','methodology':'METHODOLOGY.md'},heat

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--registry',default=str(BASE/'registry')); ap.add_argument('--heat',default=str(BASE/'frontier/heat.json')); ap.add_argument('--output',default=str(BASE/'impact/index.json')); a=ap.parse_args()
    items,report=merge_registry(a.registry); cached=read(BASE/'impact/enriched.json',{}); cache={x['id']:x.get('metrics',{}) for x in cached.get('items',[])}
    overlay=read(BASE/'impact/metadata-overlay.json',{}).get('items',{})
    arxiv_dates=read(BASE/'impact/arxiv-dates.json',{}).get('items',{})
    for x in items:
        record=read(BASE/'impact/cache/records'/(hashlib.sha256(x['id'].encode()).hexdigest()+'.json'))
        # Metrics are accepted only for an unchanged registry record.
        from common import fingerprint
        x['metrics']=record['metrics'] if record and record.get('fingerprint')==fingerprint(x) else {}
        from enrich import identifiers
        arxiv,doi=identifiers(x); extra=overlay.get(x['id'])
        if arxiv in arxiv_dates:
            first=arxiv_dates[arxiv]; x['metrics']['first_submitted_at']=first.get('first_submitted_at'); x['metrics'].setdefault('provenance',[])
            proof={**first['source'],'fields':['first_submitted_at'],'identity':'official_arxiv_id'}
            if proof not in x['metrics']['provenance']: x['metrics']['provenance'].append(proof)
        if extra and extra.get('identity')=={'arxiv_id':arxiv,'doi':doi}:
            obs=extra.get('observations',{}); chosen=obs.get('openalex') if obs.get('openalex',{}).get('citations') is not None else obs.get('semantic_scholar')
            m=x['metrics']; m.setdefault('provenance',[])
            if chosen:
                m['citations_by_provider']={k:v.get('citations') for k,v in obs.items()}; m['citation_record_selection']='maximum single observed indexed version; never sum providers/versions'
                m.update(citations=chosen.get('citations'),paper_title=chosen.get('title'),paper_id=chosen.get('paper_id'),paper_date=chosen.get('paper_date'),citation_provider='openalex' if chosen is obs.get('openalex') else 'semantic_scholar')
                if chosen.get('counts_by_year') is not None: m['citations_by_year']={str(y['year']):y['cited_by_count'] for y in chosen['counts_by_year']}; m['citations_by_year_complete']=False
            text=next((v['abstract'] for v in obs.values() if v.get('abstract')),None)
            if text: m['paper_abstract']=text
            for source in extra.get('sources',[]):
                if source not in m['provenance']: m['provenance'].append(source)
    identity_conflicts={c['id'] for c in report['conflicts'] if c.get('field') in ('arxiv_id','doi') and all(c.get('values',[])) and not c.get('resolved')}
    for x in items:
        if x['id'] in identity_conflicts and not x.get('curation',{}).get('resolve_identity_conflict'): x['_identity_conflict']=True
    index,heat=compute(items,Path(a.heat)); write(BASE/'impact/audit-application-report.json',report); write(a.output,index); write(BASE/'registry/registry.json',{'generated_at':stamp(),'count':len(items),'items':items}); write(BASE/'impact/industry-heat.json',heat)
    all_rows=index['ranking']+index['unscored']
    dim_coverage={key:{'observed':sum(r['components'][key] is not None for r in all_rows),'total':len(all_rows),'share':sum(r['components'][key] is not None for r in all_rows)/len(all_rows) if all_rows else None} for key in WEIGHTS}
    report.update(dimension_coverage=dim_coverage,generated_at=stamp(),catalogue_count=len(items),ranked=len(index['ranking']),scored=len(index['ranking']),unscored=len(index['unscored']),officially_eligible=sum(r['confidence']['official_rank_eligible'] for r in index['ranking']),frontier_heat_present=heat['source_present'],coverage_mean=sum(r['confidence']['coverage'] for r in index['ranking'])/len(index['ranking']) if index['ranking'] else None,metric_coverage={key:sum(x['metrics'].get(key) is not None for x in items) for key in ('citations','gh_stars','hf_downloads','model_card_mentions','evaluator_adoptions','novelty_score')})
    write(BASE/'impact/compute-report.json',report)
    print('rank\tbenchmark\tscore\tcoverage\tstatus')
    for row in index['ranking'][:20]: print(f"{row['rank']}\t{row['name']}\t{row['score']}\t{row['confidence']['coverage']}\t{'provisional' if 'provisional' in row['flags'] else 'audited'}")
    print('REPORT', {k:v for k,v in report.items() if k not in ('conflicts','invalid_rows','audit_events','dropped_archive','occurrence_redirects','audit_unresolved')}, 'conflicts=',len(report['conflicts']))
if __name__=='__main__': main()
