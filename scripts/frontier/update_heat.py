#!/usr/bin/env python3
"""Benchmark Constitution: rolling 20-model Frontier Heat (standard library only).

Daily workflow (UTC):
1. Review OFFICIAL release feeds across the declared provider universe. Verify first
   release dates (not GA/weights release/serving acceleration dates). Append distinct
   frontier-capable checkpoints to models.json, marking eligible=false for exclusions.
   The script does NOT discover new releases or pretend model-card extraction is automatic.
2. Actually open each new checkpoint's official release/card/system card/report, OCR
   performance images where necessary, and append audited rows to mentions.json.
   Required: model, benchmark_id, raw_name, url, location. Add accessed, variant and
   evidence_text_file. counted=false is for bibliography, source blocklists and indices.
   Never copy a predecessor's evaluations merely because the new card links its report.
3. Normalize benchmark families in normalization.json and update ../registry/frontier.jsonl.
4. Run `python3 update_heat.py --date YYYY-MM-DD`. Optional --append-models and
   --append-mentions accept JSON arrays/JSONL; the archive is appended/deduplicated,
   while the ranking ALWAYS filters to the latest 20 eligible released model IDs.
5. Review coverage.json and heat.json; publish only after audit. An incomplete source
   does not count as absence: observed frequencies are lower bounds, not true zeros.

Ranking is count(DISTINCT model_id), denominator=actual window size; tie-break id ASC.
Rank change = previous available day rank - current rank (positive=up). Same-day reruns
replace that day's history and compare to an EARLIER day, never to themselves. The
history top array contains the complete ordered ranking, so rank changes below top30
are calculable too. This is DOCUMENT MENTION frequency, not score or quality.
No network, scheduling, repository changes, commits, publishing, or credential access.
"""
from __future__ import annotations
import argparse,datetime,json,os,pathlib,tempfile,collections
from zoneinfo import ZoneInfo

ROOT=pathlib.Path(__file__).resolve().parent
TZ=ZoneInfo('UTC')
RULE=('最近20个已审核eligible前沿级通用/代码/原生多模态独立模型checkpoint，按首发日倒序，'
      '同日按id升序。排除轻量级Haiku/Luna、纯图像/语音、垂直专用Cyber/Legal及同智力加速SKU；'
      '同厂可多项；不设厂商配额。仅为已审核发布宇宙内的窗口，全球最新20完整性仍待复核。')

def read_rows(path):
    p=pathlib.Path(path)
    if not p.exists():return []
    text=p.read_text(encoding='utf-8')
    if not text.strip():return []
    if text.lstrip().startswith('['):return json.loads(text)
    if text.lstrip().startswith('{') and p.suffix!='.jsonl':
        d=json.loads(text)
        return d.get('models',d.get('items',[d]))
    return [json.loads(line) for line in text.splitlines() if line.strip()]

def atomic_json(path,obj):
    p=pathlib.Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.'+p.name,dir=p.parent,text=True)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:
            json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
        os.replace(tmp,p)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

def merge_models(old,extra):
    d={}
    for m in old+extra:
        if not m.get('id'):raise ValueError('model lacks id')
        if m['id'] in d:
            prior=d[m['id']];combined={**prior,**m}
            combined['sources']=list({s['url']:s for s in prior.get('sources',[])+m.get('sources',[])}.values())
            d[m['id']]=combined
        else:d[m['id']]=m
    return list(d.values())

def merge_mentions(old,extra):
    d={}
    for x in old+extra:
        fields=('model','benchmark_id','raw_name','url','location')
        if any(not isinstance(x.get(k),str) or not x[k].strip() for k in fields):
            raise ValueError('mention missing required nonempty string: '+repr(x))
        if not x['url'].startswith(('https://','http://')):raise ValueError('invalid source URL')
        if 'counted' in x and not isinstance(x['counted'],bool):raise ValueError('counted must be boolean')
        d[tuple(x[k] for k in fields)]=x
    return list(d.values())

def compute(models,mentions,registry,old,state,day,n=20,allow_short=False):
    datetime.date.fromisoformat(day)
    by_id={m['id']:m for m in models};reg={b['id']:b for b in registry}
    eligible=[];excluded=[]
    for m in models:
        if not m.get('eligible',True):excluded.append({'id':m['id'],'reason':'ineligible'});continue
        date=m.get('release_date')
        try:datetime.date.fromisoformat(date)
        except (ValueError,TypeError):excluded.append({'id':m['id'],'reason':'release_date_unverified'});continue
        if not m.get('sources'):raise ValueError('model missing official sources: '+m['id'])
        if date<=day:eligible.append(m)
    eligible.sort(key=lambda m:m['id']);eligible.sort(key=lambda m:m['release_date'],reverse=True)
    window=eligible[:n]
    if len(window)<n and not allow_short:raise ValueError(f'Only {len(window)} eligible released models; need {n}')
    ids={m['id'] for m in window};counts=collections.defaultdict(set);model_bench=collections.defaultdict(set)
    first=state.get('first_seen',{}).copy()
    for r in old.get('ranking',[]):first.setdefault(r['benchmark_id'],r.get('first_seen',day))
    for x in mentions:
        if x['model'] not in by_id:raise ValueError('unknown model: '+x['model'])
        if x.get('counted',True) is False:continue
        bid=x['benchmark_id']
        if bid not in reg:raise ValueError('unknown canonical benchmark: '+bid)
        accessed=x.get('accessed',day)
        if accessed>day:continue
        first[bid]=min(first.get(bid,accessed),accessed)
        if x['model'] in ids:
            counts[bid].add(x['model']);model_bench[x['model']].add(bid)
    history_by_date={h['date']:h for h in old.get('history',[]) if h['date']<=day}
    earlier=[h for d,h in history_by_date.items() if d<day]
    prior=max(earlier,key=lambda h:h['date']) if earlier else None
    prior_rank={bid:i for i,bid in enumerate(prior['top'],1)} if prior else {}
    previously_seen={bid for h in earlier for bid in h['top']}
    ordered=sorted(counts,key=lambda bid:(-len(counts[bid]),bid))
    ranking=[]
    for rank,bid in enumerate(ordered,1):
        change=prior_rank[bid]-rank if bid in prior_rank else ('new' if bid not in previously_seen else None)
        ranking.append(dict(rank=rank,benchmark_id=bid,name=reg[bid]['name'],domain=reg[bid]['domain'],count=len(counts[bid]),share=len(counts[bid])/len(window),models=sorted(counts[bid]),first_seen=first[bid],rank_change=change))
    out_models=[{**m,'benchmarks':sorted(model_bench[m['id']])} for m in window]
    history_by_date[day]={'date':day,'top':ordered}
    now=datetime.datetime.now(TZ).isoformat(timespec='seconds')
    result=dict(generated_at=now,window=dict(n_models=len(window),target_n_models=n,rule=RULE),models=out_models,ranking=ranking,history=[history_by_date[d] for d in sorted(history_by_date)])
    result['coverage']={'status':'provisional_lower_bound','interpretation_zh':'统计真实打开官方文档中的具名benchmark提及；不是分数榜，也不等于模型实际采用率。图片/OCR及具名评测遗漏仍可能存在。','latest20_verified_globally':False,'rank_change_reference_date':prior['date'] if prior else None,'excluded_models':excluded}
    return result,{'first_seen':first,'updated_at':now}

def main():
    p=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--date',default=datetime.datetime.now(TZ).date().isoformat())
    p.add_argument('--models',type=pathlib.Path,default=ROOT/'models.json')
    p.add_argument('--mentions',type=pathlib.Path,default=ROOT/'mentions.json')
    p.add_argument('--registry',type=pathlib.Path,default=ROOT.parent/'registry/frontier.jsonl')
    p.add_argument('--output',type=pathlib.Path,default=ROOT/'heat.json')
    p.add_argument('--state',type=pathlib.Path,default=ROOT/'state.json')
    p.add_argument('--append-models',type=pathlib.Path)
    p.add_argument('--append-mentions',type=pathlib.Path)
    p.add_argument('--allow-short-window',action='store_true')
    a=p.parse_args()
    models=merge_models(read_rows(a.models),read_rows(a.append_models) if a.append_models else [])
    mentions=merge_mentions(read_rows(a.mentions),read_rows(a.append_mentions) if a.append_mentions else [])
    old=json.loads(a.output.read_text()) if a.output.exists() else {}
    state=json.loads(a.state.read_text()) if a.state.exists() else {}
    if old.get('history') and max(h['date'] for h in old['history'])>a.date:
        p.error('Refusing to overwrite later history with a backdated run; use a separate --output/--state')
    try:result,newstate=compute(models,mentions,read_rows(a.registry),old,state,a.date,allow_short=a.allow_short_window)
    except (ValueError,KeyError,TypeError) as e:p.error(str(e))
    # Validation precedes every write. Same-day reruns are idempotent except timestamps.
    if a.append_models:atomic_json(a.models,models)
    if a.append_mentions:atomic_json(a.mentions,mentions)
    atomic_json(a.output,result);atomic_json(a.state,newstate)
    print(f"{a.date} UTC: {len(result['models'])} models, {len(result['ranking'])} benchmark families -> {a.output}")

if __name__=='__main__':main()
