#!/usr/bin/env python3
"""Real paper-abstract and provider cross-check overlay; never overwrites shard files.
Batches all identifiable papers, not a list of favored benchmark names.
"""
import argparse, hashlib, json, re, time
from collections import defaultdict, Counter
from pathlib import Path
from common import BASE, read, write, stamp, merge_registry, date
from enrich import Client, identifiers, chunks, MAILTO

def abstract(p):
    if p.get('abstract'): return p['abstract']
    inv=p.get('abstract_inverted_index') or {}
    positions={int(pos):word for word,ps in inv.items() for pos in ps}
    return ' '.join(positions[i] for i in sorted(positions)) if positions else None

def keys(p):
    out=[]; ext=p.get('externalIds') or {}
    if ext.get('ArXiv'): out.append('arxiv:'+str(ext['ArXiv']).split('v')[0].lower())
    d=re.sub(r'^https?://(?:dx\.)?doi.org/','',str(ext.get('DOI') or p.get('doi') or ''),flags=re.I).lower()
    if d: out.append('doi:'+d)
    if d.startswith('10.48550/arxiv.'): out.append('arxiv:'+d.split('arxiv.',1)[1])
    for loc in (p.get('locations') or [])+[p.get('primary_location') or {}]:
        for k in ('landing_page_url','pdf_url'):
            m=re.search(r'arxiv.org/(?:abs|pdf)/(\d{4}\.\d{4,5}|[a-zA-Z.-]+/\d{7})',str(loc.get(k) or ''))
            if m: out.append('arxiv:'+m.group(1).lower())
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--offline',action='store_true'); ap.add_argument('--max-seconds',type=float,default=600); ap.add_argument('--openalex-only',action='store_true'); a=ap.parse_args()
    a.refresh=False; a.interval=1.2; a.retries=3
    c=Client(a); c.pacing['api.semanticscholar.org']=30
    items,_=merge_registry(BASE/'registry'); targets=defaultdict(list); id_to_rows=defaultdict(list)
    for x in items:
        arxiv,doi=identifiers(x)
        if arxiv: targets['arxiv:'+arxiv.lower()].append(x); id_to_rows['ARXIV:'+arxiv].append(x)
        if doi: targets['doi:'+doi].append(x)
        elif arxiv: targets['doi:10.48550/arxiv.'+arxiv.lower()].append(x)
        if doi and not arxiv: id_to_rows['DOI:'+doi].append(x)
    entries={}; status=Counter()
    def ingest(p,rr,provider,lookup=None):
        ks=keys(p)
        if lookup and lookup.startswith('ARXIV:'): ks.append('arxiv:'+lookup[6:].lower())
        if lookup and lookup.startswith('DOI:'): ks.append('doi:'+lookup[4:].lower())
        rows={x['id']:x for key in ks for x in targets.get(key,[])}
        for id,x in rows.items():
            ar,do=identifiers(x); e=entries.setdefault(id,{'identity':{'arxiv_id':ar,'doi':do},'observations':{},'sources':[]})
            entry={'observed_at':rr['accessed'],'title':p.get('title') or p.get('display_name'),'citations':p.get('citationCount') if provider=='semantic_scholar' else p.get('cited_by_count'),'paper_id':p.get('paperId') or p.get('id'),'paper_date':p.get('publicationDate') or p.get('publication_date') or (str(p['year']) if p.get('year') else None),'abstract':abstract(p),'counts_by_year':p.get('counts_by_year')}
            versions=e.setdefault('work_versions',{}).setdefault(provider,{})
            work=entry.get('paper_id') or entry.get('title')
            old=versions.get(work)
            if old and old.get('abstract') and not entry.get('abstract'): entry['abstract']=old['abstract']
            if not old or date(entry['observed_at'])>=date(old['observed_at']): versions[work]=entry
            # Freshest observation per work first; then largest SINGLE indexed version.
            e['observations'][provider]=max(versions.values(),key=lambda v:((v.get('citations') if v.get('citations') is not None else -1),str(v.get('paper_id'))))
            source={'url':rr['url'],'accessed':rr['accessed'],'provider':provider,'identity':'exact_external_identifier','fields':['citations','paper_title','paper_date','paper_abstract']}
            if rr.get('method')=='POST': source.update(method='POST',lookup_id=lookup,batch_ids_count=len((rr.get('request_body') or {}).get('ids',[])))
            if source not in e['sources']: e['sources'].append(source)
    # Reuse ALL existing successful raw responses before making new calls.
    for f in (BASE/'impact/cache/responses').glob('*.json'):
        rr=read(f,{})
        if rr.get('status')!=200: continue
        payload=rr.get('data'); url=rr.get('url','')
        if 'api.openalex.org' in url and isinstance(payload,dict):
            for p in payload.get('results',[payload]):
                if isinstance(p,dict): ingest(p,rr,'openalex')
        elif 'api.semanticscholar.org' in url:
            if isinstance(payload,list):
                ids=(rr.get('request_body') or {}).get('ids',[])
                for ident,p in zip(ids,payload):
                    if isinstance(p,dict): ingest(p,rr,'semantic_scholar',ident)
            elif isinstance(payload,dict) and payload.get('paperId'): ingest(payload,rr,'semantic_scholar')
    write(BASE/'impact/metadata-overlay.json',{'generated_at':stamp(),'items':entries})
    # Obtain missing abstract metadata by identity in 500-paper POST batches, slow pacing.
    if not a.openalex_only:
        all_ids=sorted(id_to_rows)
        for batch in chunks(all_ids,500):
            if c.budget()<2: break
            rr=c.post('https://api.semanticscholar.org/graph/v1/paper/batch',{'ids':batch},{'fields':'title,year,publicationDate,citationCount,externalIds,url,abstract'})
            if rr.get('status')==200 and isinstance(rr.get('data'),list):
                for ident,p in zip(batch,rr['data']):
                    if p: ingest(p,rr,'semantic_scholar',ident)
            status['s2_'+str(rr.get('status'))]+=1
            write(BASE/'impact/metadata-overlay.json',{'generated_at':stamp(),'items':entries})
            print(json.dumps({'stage':'abstract_batch','batch':len(batch),'status':rr.get('status'),'mapped':len(entries)},ensure_ascii=False),flush=True)
    # Resolve canonical DOI records even for S2 zero-citation duplicates; choose provider by
    # explicit documented precedence, never sum providers or force any benchmark's rank.
    dois=sorted(key[4:] for key in targets if key.startswith('doi:'))
    for batch in chunks(dois,50):
        if c.budget()<2: break
        rr=c.get('https://api.openalex.org/works',{'filter':'doi:'+'|'.join(batch),'per_page':100,'mailto':MAILTO})
        if rr.get('status')==200:
            for p in (rr.get('data') or {}).get('results',[]): ingest(p,rr,'openalex')
        status['oa_'+str(rr.get('status'))]+=1
        write(BASE/'impact/metadata-overlay.json',{'generated_at':stamp(),'items':entries})
        if rr.get('status') in (401,403): break
        if rr.get('error')=='retry_later_after_429': break
    write(BASE/'impact/metadata-report.json',{'generated_at':stamp(),'mapped':len(entries),'with_abstract':sum(any(o.get('abstract') for o in e['observations'].values()) for e in entries.values()),'status':dict(status),'requests':dict(c.stats),'api_events':c.events,'scope':'all identifiable registry papers; no benchmark-name targeting'})
if __name__=='__main__': main()
