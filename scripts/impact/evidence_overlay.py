#!/usr/bin/env python3
"""BCI evidence overlay: conservative documentary signals, not expert ratings.
Only public dossier snapshots actually fetched today are scored. Preserve source
quotes, source paths and original dates. No LLM imputation, no new registry rows.
"""
import hashlib,re,json
from pathlib import Path
from urllib.parse import urlparse
from collections import defaultdict,Counter
from common import BASE,read,write,stamp,date
VERSION='documentary-evidence-0.3'
QKEYS=('human_validation','contamination_protection','reproducibility','license_clarity','maintenance_review','external_review')

def usable(v):
 return isinstance(v,str) and v.strip() and not re.match(r'^(待核实|未核实|未知|未公开|不适用|暂无)',v.strip())

def field(d,path):
 x=d
 for k in path.split('.'):x=x.get(k,{}) if isinstance(x,dict) else {}
 return x if isinstance(x,dict) and 'value'in x else {}

def proof(snapshot,path,quote=None):
 f=field(snapshot['data'],path)
 return {'url':snapshot['url'],'accessed':snapshot['accessed'],'field_path':path,
         'quote':quote if quote is not None else f.get('value'),
         'upstream_sources':f.get('sources',[]),'kind':'published_dossier_secondary_evidence',
         'limitation':'Secondary editorial evidence; original sources retain their actual prior access dates, not re-accessed by this collector.'}

def obs(value,sources,rule,**extra):
 return {'value':value,'sources':sources,'rubric_rule':rule,'reviewed_at':stamp(),
         'method':VERSION,'review_type':'machine_assisted_documentary_extraction',**extra}

def quality(snapshot):
 d=snapshot['data'];a={}
 # Treat partial documentary support as 50 by policy, not an estimated probability.
 # Reliability is 0.5: no independent double human review in this run.
 for path in ('construction.review_process','construction.quality_control'):
  text=field(d,path).get('value')
  if usable(text) and re.search(r'(人工.{0,8}(审核|复核|验证|检查|抽查|标注)|专家.{0,12}(审核|复核|验证|检查|抽查)|双人|多人.{0,5}(审核|复核)|human.{0,8}(valid|review)|expert.{0,10}(valid|review))',text,re.I):
   if re.search(r'(未|无|没有).{0,4}(人工|专家).{0,4}(审核|复核|验证|检查)',text):continue
   a['human_validation']=obs(50,[proof(snapshot,path)],'Documented human review process; not an independent reliability audit',reliability=.5);break
 path='construction.decontamination';text=field(d,path).get('value')
 if usable(text):
  # Sentence-level evidence only; warning/negation alone is never a control.
  sentences=re.split(r'[。；\n]',text)
  positive=[s for s in sentences if re.search(r'canary|保持私有|保持.*私密|隐藏测试|测试.*不公开|不公开.*(答案|测试)|保密\d|私有\d|\d.*题.*私有|去除.*(重复|重合)|去重|时间截|时间切|训练.*排除|从.*训练.*排除|不回流上游|dedup|held.out',s,re.I)
            and not re.search(r'未.{0,12}(去重|隔离|检索)|没有.{0,12}(去重|隔离|检索)|不是.{0,12}(去重|隔离)|不构成',s)]
  if positive:a['contamination_protection']=obs(50,[proof(snapshot,path,'；'.join(positive))],'Documented mitigation only; NOT proof of contamination-free models',reliability=.5)
 path='evaluation.official_scripts';text=field(d,path).get('value')
 scoring=field(d,'evaluation.scoring').get('value')
 if usable(text) and re.search(r'https?://',text) and usable(scoring) and not re.search(r'未.*(脚本|开源)|脚本.*待核实|未找到|未能确认|不能把.*(评分|评测)|渲染器',text):
  a['reproducibility']=obs(50,[proof(snapshot,path),proof(snapshot,'evaluation.scoring')],'Published evaluation entry point plus scoring specification; code NOT executed or independently reproduced',reliability=.5)
 path='basic_info.license';text=field(d,path).get('value')
 if usable(text) and re.search(r'CC[- ]?BY|MIT|Apache|BSD|GPL|ODC|CDLA|CC0|MPL',text,re.I) and re.search(r'数据集|数据卡|HF卡|数据库|数据[^；。]{0,18}(CC|MIT|Apache|BSD|GPL)|任务[^；。]{0,15}(CC|MIT|Apache)|原创问答[^；。]{0,8}CC',text,re.I) and not re.search(r'冲突|待核实|未明确|未确认|尚未|不一致|不能确定|不明|未知|unknown|未设置|未指定|尚待|需复核|须核对|需核对|口径差异|官方材料差异|待作者批准|无许可|仅代码|禁止.{0,8}训练|不得.{0,8}训练|不允许.{0,8}训练|仅.{0,4}评测|不能把.*数据许可.*扩大|数据.*许可.*未',text,re.I):
  a['license_clarity']=obs(50,[proof(snapshot,path)],'Documented license statement without an unresolved scope conflict; not a legal audit',reliability=.5)
 # Version metadata is retained as factual context, never promoted into maintenance quality.
 return a

EVALS={'artificialanalysis.ai':'Artificial Analysis','vals.ai':'Vals','evals.vals.ai':'Vals','crfm.stanford.edu':'HELM','scale.com':'Scale SEAL','epoch.ai':'Epoch AI'}
def organization(url):
 host=(urlparse(url).hostname or '').removeprefix('www.')
 return next((name for h,name in EVALS.items() if host==h or host.endswith('.'+h)),None)

def leaderboard(snapshot):
 d=snapshot['data'];rows=field(d,'leaderboard.results').get('value',[]);rows=rows if isinstance(rows,list) else []
 groups=defaultdict(list);independent={}
 homepage=field(d,'basic_info.official_homepage').get('value')or'';official_org=organization(homepage) if isinstance(homepage,str) else None
 for r in rows:
  if not isinstance(r,dict):continue
  url=r.get('source_url')or'';org=organization(url);typ=str(r.get('result_type',''));track=str(r.get('track',''))
  # Only independently measured evaluation tracks; references/model cards are not reproductions.
  if org and org!=official_org and re.search(r'独立评测|第三方|AA.{0,8}(榜|测)|Artificial Analysis|HELM|Vals|Scale.{0,6}SEAL|Epoch.{0,6}评测',track+' '+typ,re.I):
   independent[org]={'url':snapshot['url'],'accessed':snapshot['accessed'],'primary_url':url,'primary_accessed':r.get('collected_at'),'kind':'independent_evaluation_snapshot','model':r.get('model'),'track':track,'original_collected_at':r.get('collected_at'),'dossier_snapshot':snapshot['url']}
  val=r.get('score');metric=str(r.get('metric',''))
  if isinstance(val,bool) or not isinstance(val,(int,float)) or not (0<=val<=100):continue
  # Fixed bounded correctness/success rates only. No win rate, relative Elo, unbounded errors,
  # bare unspecified "score", paper-only baselines or cross-track maxima.
  if not re.search(r'%|百分|percent',metric,re.I):continue
  if not re.search(r'accuracy|准确|正确|pass@|pass\^|all.pass|success|成功|resolved|resolve rate|solve|解决|完成率',metric,re.I):continue
  if re.search(r'win|胜率|error|错误|relative',metric,re.I):continue
  if re.search(r'历史|论文|表\s*\d|paper|baseline|human|人类',track+' '+typ,re.I):continue
  if not url.startswith('https://'):continue
  # Include version/subset/prompt/budget if separately represented; no implicit pooling.
  protocol=tuple(str(r.get(k,'')) for k in ('version','subset','protocol','setting','budget','split'))
  key=(url,track,metric,protocol)
  groups[key].append(r)
 tracks=[]
 for (url,track,metric,protocol),g in groups.items():
  best=max(g,key=lambda r:r['score'])
  tracks.append({'source_url':url,'accessed':snapshot['accessed'],'track':track,'metric':metric,'protocol':list(protocol),'score':best['score'],'model':best.get('model'),'floor':0,'ceiling':100,'n_results':len(g),'original_collected_at':best.get('collected_at'),'source_date':best.get('source_date'),'scope':'best in this source/track snapshot, NOT global SOTA','dossier_snapshot':snapshot['url']})
 # Prefer explicit third party independent evaluations, then the most populated single track.
 tracks.sort(key=lambda t:(organization(t['source_url'])is None,-t['n_results'],t['source_url'],t['track'],t['metric']))
 a={}
 if independent:
  a['third_party_reproductions']=obs(len(independent),list(independent.values()),'Count unique independent evaluator organizations with actual model-result rows; operational re-evaluation evidence, NOT exact protocol reproduction',reliability=.5,organizations=sorted(independent))
 if tracks:
  a['saturation_tracks']=obs(tracks,[{'url':snapshot['url'],'accessed':snapshot['accessed'],'primary_url':t['source_url'],'primary_accessed':t['original_collected_at']} for t in tracks],'Separate all version/source/protocol tracks; never pool maxima across tracks')
  selected=tracks[0];s=[{'url':snapshot['url'],'accessed':snapshot['accessed'],'primary_url':selected['source_url'],'primary_accessed':selected['original_collected_at'],'dossier_snapshot':snapshot['url'],'original_collected_at':selected['original_collected_at'],'track':selected['track'],'metric':selected['metric']}]
  for k,v in [('sota_score',selected['score']),('metric_floor',0),('metric_ceiling',100)]:
   a[k]=obs(v,s,'Selected single-track bounded percentage correctness/success rate; bounds follow metric definition, not human baseline',reliability=.5,selected_track=selected)
 return a

def canonical(x):
 u=urlparse(x.get('github_url')or'');p=u.path.strip('/').split('/')
 return '/'.join(p[:2]).removesuffix('.git').lower() if u.hostname in ('github.com','www.github.com') and len(p)>1 else None

def connector_metadata():
 repos={}
 for p in (BASE/'impact/cache/github-connector').glob('*.json'):
  d=read(p,{})
  for x in d.get('items',[d]):
   if x.get('full_name') and x.get('stargazers_count')is not None:repos[x['full_name'].lower()]={**x,'_observation_source':d.get('_source',{'url':x.get('url'),'accessed':'2026-11-08'})}
 return repos

def apply(items):
 byid={x['id']:x for x in items};report={'version':VERSION,'generated_at':stamp(),'dossiers_fetched':0,'matched':0,'unmatched':[],'signals':Counter(),'github_connector_matches':0,'new_github_observations':0,'limitations':['Documentary extraction is not independent expert review.','No fabricated negative evidence; absent signals stay null.','All roster entries retained; no historical expansion.']}
 # Explicit, reviewed identity aliases only (not fuzzy title matching).
 redirects={'arc-agi-1':'arc-agi','arc-agi-2':'arc-agi-2','realworldqa':'real-world-qa'}
 for p in sorted((BASE/'impact/cache/dossiers').glob('*.json')):
  snap=read(p,{})
  if snap.get('status')!=200 or not snap.get('data'):continue
  if not snap.get('accessed','').startswith('2026-11-08'):continue
  report['dossiers_fetched']+=1;did=snap['data']['id'];x=byid.get(did)or byid.get(redirects.get(did))
  if x is None:report['unmatched'].append(did);continue
  report['matched']+=1
  a={**quality(snap),**leaderboard(snap)}
  # never overwrite pre-existing manually reviewed assessments
  ass=x.setdefault('assessment',{})
  for k,v in a.items():
   if k not in ass:ass[k]=v
  report['signals'].update(a.keys())
  x['assessment_review']={'type':'single_pass_documentary_extraction','independent_reviewers':0,'source_snapshot':snap['url'],'accessed':snap['accessed'],'formal_quality_audit_complete':False}
 repos=connector_metadata()
 for x in items:
  repo=canonical(x);p=repos.get(repo)
  if not p:continue
  report['github_connector_matches']+=1;m=x['metrics']
  existing_dates=[date(v.get('accessed')) for v in m.get('provenance',[]) if 'gh_stars' in v.get('fields',[]) and date(v.get('accessed'))]
  observed=date(p['_observation_source'].get('accessed'))
  if existing_dates and observed and max(existing_dates).date()>observed.date():continue
  if m.get('gh_stars')is None:report['new_github_observations']+=1
  m.update(gh_repository=repo,gh_stars=p['stargazers_count'],gh_forks=p.get('forks_count'),gh_open_issues=p.get('open_issues_count'),gh_created_at=p.get('created_at'),gh_pushed_at=p.get('pushed_at'),gh_archived=p.get('archived'))
  proof={**p['_observation_source'],'repository_url':'https://api.github.com/repos/'+repo,'fields':['gh_stars','gh_forks','gh_open_issues','gh_created_at','gh_pushed_at','gh_archived'],'identity':'exact_canonical_repository_match','method':'authorized_GitHub_connector_public_metadata','scope':'Public search pages/metadata; no repository identities inferred from text search'}
  if proof not in m.setdefault('provenance',[]):m['provenance'].append(proof)
  dest=BASE/'impact/cache/snapshots'/(hashlib.sha256(repo.encode()).hexdigest()+'.json');hist=read(dest,[])
  if not any(s['date'].startswith('2026-11-08') for s in hist):hist.append({'date':'2026-11-08','stars':m['gh_stars'],'source':proof['url'],'date_precision':'day; baseline only, no subday growth'})
  write(dest,hist)
  # This run establishes baseline only. Prior same-calendar-day samples are not a monthly trend.
  m['gh_stars_per_month']=None;m['gh_growth_status']='baseline_recorded; need a second observation at least 24h later'
 # Public dataset card statements: partial license documentation only; never infer
 # human validation from tags, author reputation or the existence of a paper.
 report['hf_card_matches']=0
 byds={}
 for x in items:
  ds=x.get('hf_dataset')
  if isinstance(ds,str):byds.setdefault(ds.removeprefix('https://huggingface.co/datasets/').strip('/'),[]).append(x)
 for path in (BASE/'impact/cache/hf-cards').glob('*.json'):
  rr=read(path,{});data=rr.get('data');ds=rr.get('dataset')
  if rr.get('status')!=200 or not isinstance(data,dict) or data.get('id','').lower()!=str(ds).lower():continue
  card=data.get('cardData')or{};lic=card.get('license') if isinstance(card,dict) else None
  for x in byds.get(ds,[]):
   report['hf_card_matches']+=1;m=x['metrics']
   existing_dates=[date(v.get('accessed')) for v in m.get('provenance',[]) if 'hf_downloads' in v.get('fields',[]) and date(v.get('accessed'))]
   if existing_dates and max(existing_dates).date()>date(rr['accessed']).date():continue
   m.update(hf_downloads=data.get('downloads'),hf_likes=data.get('likes'),hf_last_modified=data.get('lastModified'))
   src={'url':rr['url'],'accessed':rr['accessed'],'fields':['hf_downloads','hf_likes','hf_last_modified'],'identity':'exact_registry_dataset_id','kind':'public_HF_dataset_card'}
   if src not in m.setdefault('provenance',[]):m['provenance'].append(src)
   # If a full dossier exists, its scope/conflict review wins; do not paper over
   # conflicting licenses with an HF metadata tag.
   if x.get('assessment_review'):continue
   recognized={'mit','apache-2.0','cc0-1.0','cc-by-4.0','cc-by-sa-4.0','cc-by-nc-4.0','cc-by-nc-sa-4.0','bsd-3-clause','bsd-2-clause','odc-by','odbl','cdla-permissive-2.0','gpl-3.0'}
   licenses=[lic] if isinstance(lic,str) else lic if isinstance(lic,list) else []
   if len(licenses)==1 and licenses[0].lower() in recognized:
    ass=x.setdefault('assessment',{})
    if 'license_clarity' not in ass:
     ass['license_clarity']=obs(50,[{'url':rr['url'],'accessed':rr['accessed'],'field_path':'cardData.license','quote':lic}],'Explicit public dataset-card license statement; no claim about code or upstream data compatibility',reliability=.5)
     report['signals']['license_clarity']+=1
 for path in (BASE/'impact/cache/github-connector').glob('issues-*.json'):
  rr=read(path,{});d=rr.get('response',{})
  if d.get('incomplete_results')is not False or not isinstance(d.get('total_count'),int):continue
  for x in items:
   if canonical(x)!=rr.get('repo'):continue
   x.setdefault('assessment',{})['issue_threads_90d']=obs(d['total_count'],[{'url':rr['url'],'accessed':rr['accessed']}],'Distinct issue threads last updated in the calendar-day window 2026-08-10 through 2026-11-08; excludes PRs. NOT event counts, sentiment or unique users.',reliability=.5)
   report['signals']['issue_threads_90d']+=1
 report['independent_quality_verdicts']={}
 for review in read(BASE/'impact/independent-quality.json',{}).get('reviews',[]):
  x=byid.get(review['target_id'])
  if not x:continue
  if review['application'].startswith('historical_only'):
   x.setdefault('historical_external_reviews',[]).append(review);continue
  verdict=review['verdict'];ass=x.setdefault('assessment',{})
  ass['epoch_verdict']=obs(verdict,review['sources'],'Published Epoch review, version-specific; review != independent evaluator adoption',reliability=1,reviewed_scope=review['reviewed_scope'])
  if verdict in ('Verified','Flawed'):
   ass['external_review']=obs(100 if verdict=='Verified' else 0,review['sources'],'Normative rubric: independent review passes minimum scoring-validity threshold=100; confirmed threshold failure=0. Not an Epoch numerical score.',reliability=1,reviewed_scope=review['reviewed_scope'],verdict=verdict)
   report['signals']['external_review']+=1
  report['independent_quality_verdicts'][x['id']]=verdict
 report['signals']=dict(report['signals']);write(BASE/'impact/evidence-report.json',report)
 return report

if __name__=='__main__':
 from common import merge_registry
 items,_=merge_registry(BASE/'registry')
 for x in items:x['metrics']={}
 print(apply(items))
