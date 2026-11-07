#!/usr/bin/env python3
"""Full-registry BCI enrichment. Public read-only APIs, batched identities, persistent
response/entity checkpoints. No credential files are ever opened. Tokens are optional
and accepted only from an already-authorized environment.
"""
import argparse, hashlib, json, os, random, re, time
from collections import Counter, defaultdict
from datetime import timedelta
from pathlib import Path
from urllib.parse import urlparse, quote, unquote
import requests
from common import BASE, now, stamp, write, read, norm, date, merge_registry, fingerprint

MAILTO='ZiChenWang114514@users.noreply.github.com'

def chunks(xs,n):
    for i in range(0,len(xs),n): yield xs[i:i+n]

def identifiers(x):
    a=str(x.get('arxiv_id') or '').strip(); d=str(x.get('doi') or '').strip()
    urls=' '.join(str(x.get(k) or '') for k in ('paper_url','homepage'))
    ma=re.search(r'(\d{4}\.\d{4,5}|[a-zA-Z.-]+/\d{7})(?:v\d+)?',a)
    if not ma: ma=re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}|[a-zA-Z.-]+/\d{7})',urls)
    a=ma.group(1) if ma else None
    d=re.sub(r'^https?://(?:dx\.)?doi\.org/','',d,flags=re.I).strip()
    if not d:
        md=re.search(r'doi\.org/(10\.\d{4,9}/[^\s?#]+)',urls)
        d=unquote(md.group(1)) if md else None
    if d and not d.startswith('10.'): d=None
    return a,d.lower() if d else None

def paper_eligible(x): return bool(x.get('paper_url') or identifiers(x)[0] or identifiers(x)[1])
def fresh(x,key,c):
    if c.args.refresh: return False
    m=x['metrics']
    if m.get(key) is None: return False
    dates=[date(v['accessed']) for v in m.get('provenance',[]) if key in v.get('fields',[]) and v.get('accessed')]
    return bool(dates) and (now()-max(dates)).total_seconds()<86400

def canonical_repo(x):
    u=urlparse(x.get('github_url') or ''); bits=u.path.strip('/').split('/')
    return '/'.join(bits[:2]).removesuffix('.git').lower() if u.hostname in ('github.com','www.github.com') and len(bits)>1 else None

def matched(p,x,strict=True):
    a,d=identifiers(x); ext=p.get('externalIds') or {}
    if a and str(ext.get('ArXiv') or '').split('v')[0].lower()==a.lower(): return True
    pd=re.sub(r'^https?://(?:dx\.)?doi.org/','',str(ext.get('DOI') or p.get('doi') or ''),flags=re.I).lower()
    if d and pd==d: return True
    if a and pd=='10.48550/arxiv.'+a.lower(): return True
    if a:
        for loc in (p.get('locations') or [])+[p.get('primary_location') or {}]:
            if any(re.search(r'arxiv.org/(?:abs|pdf)/'+re.escape(a)+r'(?:v\d+)?(?:\.pdf)?(?:$|[?#/])',loc.get(k) or '',re.I) for k in ('landing_page_url','pdf_url')): return True
    title=norm(p.get('title') or p.get('display_name'))
    for candidate in [x.get('paper_title'),x.get('metrics',{}).get('paper_title'),x.get('name')]+x.get('aliases',[]):
        n=norm(candidate)
        if n and len(n)>=8 and title==n: return True
        if n and len(n)>=8 and title.startswith(n) and len(title)<max(150,5*len(n)): return True
    return False

class Client:
    def __init__(self,args):
        self.args=args; self.root=BASE/'impact/cache'; self.dir=self.root/'responses'; self.dir.mkdir(parents=True,exist_ok=True)
        self.stats=Counter(); self.hosts=Counter(); self.last={}; self.cooldown={}; self.blocked=set(); self.start=time.monotonic()
        self.session=requests.Session(); self.session.headers['User-Agent']='BenchmarkConstitution/BCI-0.2 (research; mailto:'+MAILTO+')'
        self.events=[]; self.pacing={}
        prior=read(BASE/'impact/enrich-report.json',{})
        backoff_file=self.root/'host-backoff.json'
        self.blocked_until=read(backoff_file,{})
        # Migrate once; subsequent resumes preserve the original expiry rather than
        # extending a cooldown simply because another offline/deferred pass ran.
        if 'api.github.com' not in self.blocked_until and 'api.github.com' in prior.get('blocked_auth_hosts',[]) and date(prior.get('generated_at')):
            self.blocked_until['api.github.com']=(date(prior['generated_at'])+timedelta(hours=1)).isoformat()
            write(backoff_file,self.blocked_until)
        for host,until in self.blocked_until.items():
            if date(until) and date(until)>now() and not (host=='api.github.com' and os.environ.get('GH_TOKEN')): self.blocked.add(host)
    def budget(self): return self.args.max_seconds-(time.monotonic()-self.start)
    def request(self,method,url,params=None,body=None):
        host=urlparse(url).netloc; params=dict(params or {})
        # Cache identity excludes the contact metadata but never contains credential material.
        signature=params.copy(); signature.pop('mailto',None)
        key=hashlib.sha256((url+json.dumps(signature,sort_keys=True)+(json.dumps(body,sort_keys=True) if body is not None else '')).encode()).hexdigest()
        path=self.dir/(key+'.json'); old=read(path)
        if old and not self.args.refresh:
            age=(now()-date(old['accessed'])).total_seconds()
            if self.args.offline or (old.get('status')==200 and age<86400):
                self.stats['cache_hits']+=1; return old
            # Retry errors after a short wait, not a 24h null record lockout.
            if old.get('status') not in (429,500,502,503,504) and old.get('status') is not None and age<1800:
                self.stats['negative_cache_hits']+=1; return old
        empty={'url':requests.Request('GET',url,params=params).prepare().url,'method':method,'accessed':stamp(),'status':None,'data':None}
        if body is not None: empty['request_body']=body
        if self.args.offline or host in self.blocked or self.budget()<1:
            self.stats['deferred_requests']+=1; return {**empty,'error':'offline_or_budget_or_auth_block'}
        if self.cooldown.get(host,0)>time.monotonic():
            self.stats['deferred_rate_limited']+=1; return {**empty,'error':'retry_later_after_429','retry_at':self.cooldown[host]}
        headers={}
        if host=='api.github.com' and os.environ.get('GH_TOKEN'): headers['Authorization']='Bearer '+os.environ['GH_TOKEN']
        if host=='api.semanticscholar.org' and os.environ.get('S2_API_KEY'): headers['x-api-key']=os.environ['S2_API_KEY']
        if host=='api.openalex.org' and os.environ.get('OPENALEX_API_KEY'): headers['Authorization']='Bearer '+os.environ['OPENALEX_API_KEY']
        interval={'api.openalex.org':max(1.1,self.args.interval),'api.semanticscholar.org':5.,'api.github.com':1.1,'huggingface.co':.4}.get(host,1.)
        interval=max(interval,self.pacing.get(host,0))
        result=empty
        for attempt in range(self.args.retries+1):
            if self.budget()<2: break
            time.sleep(max(0,interval-(time.monotonic()-self.last.get(host,0))))
            self.last[host]=time.monotonic(); self.stats['network_requests']+=1; self.hosts[host]+=1
            try:
                r=self.session.request(method,url,params=params,json=body if body is not None else None,headers=headers,timeout=(8,35))
                result={**empty,'accessed':stamp(),'status':r.status_code,'data':r.json() if r.status_code==200 else None}
                self.stats['http_'+str(r.status_code)]+=1
                if r.status_code==200: break
                if r.status_code in (401,403):
                    if host=='huggingface.co':
                        self.events.append({'host':host,'status':r.status_code,'url':empty['url'],'action':'private_or_gated_resource_left_null; no retry of this resource','accessed':stamp()}); break
                    self.blocked.add(host); self.blocked_until[host]=(now()+timedelta(hours=1)).isoformat(); write(self.root/'host-backoff.json',self.blocked_until); self.events.append({'host':host,'status':r.status_code,'action':'auth_block_no_retry','accessed':stamp()}); break
                if r.status_code==429 or r.status_code>=500:
                    try: wait=float(r.headers.get('Retry-After',0))
                    except ValueError: wait=0
                    wait=max(wait,min(120,5*2**attempt))+random.uniform(0,.5)
                    interval=min(8,max(interval*2,2.0)); self.pacing[host]=interval
                    self.events.append({'host':host,'status':r.status_code,'backoff_seconds':round(wait,2),'accessed':stamp()})
                    if attempt<self.args.retries and self.budget()>wait+5:
                        print(json.dumps({'event':'polite_backoff','host':host,'seconds':round(wait,2)},ensure_ascii=False),flush=True)
                        time.sleep(wait); continue
                    self.cooldown[host]=time.monotonic()+max(120,wait); break
                break
            except (requests.RequestException,ValueError):
                self.stats['network_errors']+=1; result={**empty,'error':'network_or_json_error'}
                if attempt<self.args.retries and self.budget()>10: time.sleep(min(20,2**attempt)); continue
        write(path,result); return result
    def get(self,url,params=None): return self.request('GET',url,params)
    def post(self,url,body,params=None): return self.request('POST',url,params,body)


def add_observation(m,result,fields,identity):
    entry={'url':result['url'],'accessed':result['accessed'],'fields':fields,'identity':identity}
    if result.get('method')=='POST': entry.update(method='POST',queried_ids=(result.get('request_body') or {}).get('ids',[]))
    if entry not in m['provenance']: m['provenance'].append(entry)

def apply_s2(x,p,result):
    if p.get('citationCount') is None: return False
    m=x['metrics']; old=m.get('citation_provider')
    m.update(citations=p['citationCount'],citation_provider='semantic_scholar',paper_id=p.get('paperId'),paper_title=p.get('title'),paper_date=p.get('publicationDate') or (str(p['year']) if p.get('year') else None),citation_match='external_identifier_batch')
    if old!='semantic_scholar': m['citations_by_year']=None; m['citations_by_year_complete']=False
    add_observation(m,result,['citations','paper_title','paper_date'],'external_identifier_batch')
    return True

def apply_oa(x,p,result,identity):
    if p.get('cited_by_count') is None: return False
    m=x['metrics']
    # Keep full S2 observations if present; do not silently mix provider totals/history.
    if m.get('citation_provider')=='semantic_scholar' and m.get('citations') is not None:
        m['openalex_citations']=p['cited_by_count']; m['openalex_counts_by_year']=p.get('counts_by_year'); return True
    m.update(citations=p['cited_by_count'],citation_provider='openalex',paper_id=p.get('id'),paper_title=p.get('title') or p.get('display_name'),paper_date=p.get('publication_date'),citations_by_year={str(r['year']):r['cited_by_count'] for r in p.get('counts_by_year',[])},citations_by_year_complete=False,openalex_fwci=p.get('fwci'),citation_match=identity)
    add_observation(m,result,['citations','citations_by_year','paper_title','paper_date','openalex_fwci'],identity)
    return True

def checkpoint(x):
    dest=BASE/'impact/cache/records'/(hashlib.sha256(x['id'].encode()).hexdigest()+'.json')
    m=x['metrics']; m['collected_at']=stamp()
    write(dest,{'id':x['id'],'fingerprint':fingerprint(x),'metrics':m})

def batch_s2(c,items):
    ids=defaultdict(list)
    for x in items:
        if fresh(x,'citations',c): continue
        a,d=identifiers(x); ident='ARXIV:'+a if a else 'DOI:'+d if d else None
        if ident: ids[ident].append(x)
    fields='title,year,publicationDate,citationCount,externalIds,url'
    for batch in chunks(sorted(ids),500):
        rr=c.post('https://api.semanticscholar.org/graph/v1/paper/batch',{'ids':batch},{'fields':fields})
        if rr.get('status')==200 and isinstance(rr.get('data'),list):
            for ident,p in zip(batch,rr['data']):
                if not p: continue
                for x in ids[ident]:
                    if apply_s2(x,p,rr): checkpoint(x)
        print(json.dumps({'stage':'s2_batch','identifiers':len(batch),'status':rr.get('status'),'citations_so_far':sum(x['metrics'].get('citations') is not None for x in items)},ensure_ascii=False),flush=True)

def batch_openalex(c,items):
    mapping=defaultdict(list)
    for x in items:
        if fresh(x,'citations',c): continue
        a,d=identifiers(x)
        key=d if d else '10.48550/arxiv.'+a.lower() if a else None
        if key: mapping[key].append(x)
    for batch in chunks(sorted(mapping),50):
        rr=c.get('https://api.openalex.org/works',{'filter':'doi:'+'|'.join(batch),'per_page':100,'mailto':MAILTO})
        if rr.get('status')==200:
            for p in (rr.get('data') or {}).get('results',[]):
                d=re.sub(r'^https?://(?:dx\.)?doi.org/','',str(p.get('doi') or ''),flags=re.I).lower()
                for x in mapping.get(d,[]):
                    if apply_oa(x,p,rr,'exact_doi_batch'): checkpoint(x)
        print(json.dumps({'stage':'openalex_doi_batch','identifiers':len(batch),'status':rr.get('status'),'citations_so_far':sum(x['metrics'].get('citations') is not None for x in items)},ensure_ascii=False),flush=True)

def title_resolution(c,items):
    # Exhaustive, deterministic hash order avoids alphabetic censoring if a budget ends.
    pending=[x for x in items if paper_eligible(x) and x['metrics'].get('citations') is None]
    pending.sort(key=lambda x:hashlib.sha256(x['id'].encode()).hexdigest())
    for num,x in enumerate(pending,1):
        if c.budget()<1: break
        if c.cooldown.get('api.openalex.org',0)>time.monotonic() or 'api.openalex.org' in c.blocked: break
        query=x.get('paper_title') or x['metrics'].get('paper_title') or x['name']
        rr=c.get('https://api.openalex.org/works',{'search':query,'per_page':5,'mailto':MAILTO})
        if rr.get('status')==200:
            candidates=(rr.get('data') or {}).get('results',[])
            p=next((p for p in candidates if matched(p,x)),None)
            if p and apply_oa(x,p,rr,'strict_title_or_canonical_location_match'): checkpoint(x)
        if num%25==0: print(json.dumps({'stage':'title_resolution','attempted':num,'remaining_at_start':len(pending),'citations_so_far':sum(t['metrics'].get('citations') is not None for t in items)},ensure_ascii=False),flush=True)


def resources(c,items):
    repos=defaultdict(list); datasets=defaultdict(list)
    for x in items:
        repo=canonical_repo(x)
        if repo: repos[repo].append(x)
        ds=x.get('hf_dataset')
        if isinstance(ds,str) and '/' in ds:
            ds=re.sub(r'^https://huggingface.co/datasets/','',ds).strip('/')
            datasets[ds].append(x)
    for num,(repo,rows) in enumerate(sorted(repos.items(),key=lambda kv:hashlib.sha256(kv[0].encode()).hexdigest()),1):
        if all(fresh(x,'gh_stars',c) for x in rows): continue
        rr=c.get('https://api.github.com/repos/'+repo); p=rr.get('data')
        if rr.get('status')==200 and isinstance(p,dict):
            for x in rows:
                m=x['metrics']; m.update(gh_repository=repo,gh_stars=p.get('stargazers_count'),gh_created_at=p.get('created_at'),gh_pushed_at=p.get('pushed_at'),gh_archived=p.get('archived'),gh_forks=p.get('forks_count'),gh_open_issues=p.get('open_issues_count'),gh_license=(p.get('license') or {}).get('spdx_id'))
                add_observation(m,rr,['gh_stars','gh_created_at','gh_pushed_at','gh_archived','gh_forks','gh_open_issues','gh_license'],'registry_repository_mapping')
                snaps=BASE/'impact/cache/snapshots'/(hashlib.sha256(repo.encode()).hexdigest()+'.json'); history=read(snaps,[]); t=date(rr['accessed'])
                suitable=[h for h in history if h.get('stars') is not None and 1<=(t-date(h['date'])).total_seconds()/86400<=90]
                if suitable and m['gh_stars'] is not None:
                    h=min(suitable,key=lambda h:abs((t-date(h['date'])).total_seconds()/86400-30)); days=(t-date(h['date'])).total_seconds()/86400
                    m['gh_stars_per_month']=(m['gh_stars']-h['stars'])*30.4375/days; m['gh_growth_window_days']=days
                if m['gh_stars'] is not None and not any(h['date'][:10]==rr['accessed'][:10] for h in history):
                    history.append({'date':rr['accessed'],'stars':m['gh_stars'],'source':rr['url']}); write(snaps,history[-366:])
                checkpoint(x)
        if num%50==0: print(json.dumps({'stage':'github','repository_index':num,'unique_repositories':len(repos)},ensure_ascii=False),flush=True)
    for num,(ds,rows) in enumerate(sorted(datasets.items(),key=lambda kv:hashlib.sha256(kv[0].encode()).hexdigest()),1):
        if all(fresh(x,'hf_downloads',c) for x in rows): continue
        rr=c.get('https://huggingface.co/api/datasets/'+quote(ds,safe='/')); p=rr.get('data')
        if rr.get('status')==200 and isinstance(p,dict):
            for x in rows:
                m=x['metrics']; m.update(hf_downloads=p.get('downloads'),hf_likes=p.get('likes'),hf_last_modified=p.get('lastModified'))
                add_observation(m,rr,['hf_downloads','hf_likes','hf_last_modified'],'registry_dataset_mapping'); checkpoint(x)
        if num%100==0: print(json.dumps({'stage':'huggingface','dataset_index':num,'unique_datasets':len(datasets)},ensure_ascii=False),flush=True)
    return {'unique_repositories':len(repos),'unique_datasets':len(datasets)}


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--registry',default=str(BASE/'registry')); ap.add_argument('--offline',action='store_true'); ap.add_argument('--refresh',action='store_true'); ap.add_argument('--max-seconds',type=float,default=1800); ap.add_argument('--interval',type=float,default=.4); ap.add_argument('--retries',type=int,default=4); ap.add_argument('--passes',type=int,default=2); ap.add_argument('--citations-only',action='store_true'); a=ap.parse_args()
    c=Client(a); items,merge=merge_registry(a.registry); resumed=0
    for x in items:
        dest=BASE/'impact/cache/records'/(hashlib.sha256(x['id'].encode()).hexdigest()+'.json'); old=read(dest)
        if old and old.get('fingerprint')==fingerprint(x): x['metrics']=old['metrics']; resumed+=1
        else: x['metrics']={k:None for k in ('citations','citations_by_year','gh_stars','gh_stars_per_month','hf_downloads','hf_likes')}
        x['metrics'].setdefault('provenance',[])
    # Restore identity-matched paper observations independently of registry prose/source edits.
    overlay=read(BASE/'impact/metadata-overlay.json',{}).get('items',{})
    for x in items:
        ar,do=identifiers(x); entry=overlay.get(x['id'])
        if not entry or entry.get('identity')!={'arxiv_id':ar,'doi':do}: continue
        obs=entry.get('observations',{}); chosen=obs.get('openalex') if obs.get('openalex',{}).get('citations') is not None else obs.get('semantic_scholar')
        if chosen and chosen.get('citations') is not None:
            m=x['metrics']; m.update(citations=chosen['citations'],paper_title=chosen.get('title'),paper_id=chosen.get('paper_id'),paper_date=chosen.get('paper_date'),citation_provider='openalex' if chosen is obs.get('openalex') else 'semantic_scholar')
            if chosen.get('abstract'): m['paper_abstract']=chosen['abstract']
            for source in entry.get('sources',[]):
                if source not in m['provenance']: m['provenance'].append(source)
    initial=sum(x['metrics'].get('citations') is not None for x in items)
    print(json.dumps({'stage':'full_registry_start','count':len(items),'resumed':resumed,'existing_citations':initial,'sampling':'none; all rows'},ensure_ascii=False),flush=True)
    for p in range(a.passes):
        if c.budget()<2: break
        batch_s2(c,items); batch_openalex(c,items)
        if p==0 and not a.citations_only: resource_report=resources(c,items)
        else: resource_report={}
        title_resolution(c,items)
        eligible=[x for x in items if paper_eligible(x)]
        rate=sum(x['metrics'].get('citations') is not None for x in eligible)/len(eligible) if eligible else 0
        print(json.dumps({'stage':'pass_finished','pass':p+1,'paper_eligible':len(eligible),'citation_coverage':rate,'budget_left_seconds':round(c.budget(),1)},ensure_ascii=False),flush=True)
        if rate>=.6 or a.offline: break
        waits=[t-time.monotonic() for h,t in c.cooldown.items() if h in ('api.openalex.org','api.semanticscholar.org') and t>time.monotonic()]
        if waits and c.budget()>min(waits)+30:
            delay=min(waits)+1; print(json.dumps({'event':'retry_later','wait_seconds':round(delay,1)},ensure_ascii=False),flush=True); time.sleep(delay)
    for x in items:
        m=x['metrics']; m['paper_eligible']=paper_eligible(x)
        m['collection_status']='observed' if any(m.get(k) is not None for k in ('citations','gh_stars','hf_downloads')) else 'pending_or_no_match'
        checkpoint(x)
    write(BASE/'impact/enriched.json',{'generated_at':stamp(),'count':len(items),'items':items})
    counts={key:sum(x['metrics'].get(key) is not None for x in items) for key in ('citations','gh_stars','gh_stars_per_month','hf_downloads','hf_likes')}
    eligible=[x for x in items if paper_eligible(x)]; citation_covered=sum(x['metrics'].get('citations') is not None for x in eligible)
    merge.update(generated_at=stamp(),method_version='enrichment-0.2-full-batched',output_count=len(items),processed=len(items),resumed=resumed,sampling='none; exhaustive full registry',paper_eligible=len(eligible),paper_citation_hits=citation_covered,citation_coverage_paper_eligible=citation_covered/len(eligible) if eligible else None,target_citation_coverage=.6,target_met=citation_covered/len(eligible)>=.6 if eligible else False,metric_hits=counts,metric_coverage={k:v/len(items) if items else None for k,v in counts.items()},requests=dict(c.stats),requests_by_host=dict(c.hosts),api_events=c.events,blocked_auth_hosts=sorted(c.blocked),elapsed_seconds=round(time.monotonic()-c.start,2),credential_policy='Environment variables only; no credential files read.',**resource_report)
    write(BASE/'impact/enrich-report.json',merge)
    print(json.dumps({k:v for k,v in merge.items() if k not in ('conflicts','invalid_rows','api_events','audit_events','dropped_archive','occurrence_redirects','audit_unresolved')},ensure_ascii=False),flush=True)
if __name__=='__main__': main()
