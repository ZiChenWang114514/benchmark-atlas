#!/usr/bin/env python3
"""Official arXiv first-submission dates, batched and politely paced (>=3s).
A paper's later journal publication must not reset benchmark citation-age clocks.
"""
import argparse, hashlib, json, time, xml.etree.ElementTree as ET
from pathlib import Path
import requests
from common import BASE,read,write,stamp,merge_registry
from enrich import identifiers,chunks

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--offline',action='store_true');a=ap.parse_args()
    items,_=merge_registry(BASE/'registry'); ids=sorted(set(identifiers(x)[0] for x in items if identifiers(x)[0])); cache=BASE/'impact/cache/arxiv';cache.mkdir(parents=True,exist_ok=True)
    records={k:v for k,v in read(BASE/'impact/arxiv-dates.json',{}).get('items',{}).items() if k in ids}; statuses={}; start=time.monotonic(); previous=0
    for batch in chunks([k for k in ids if k not in records],75):
        key=hashlib.sha256('|'.join(batch).encode()).hexdigest(); path=cache/(key+'.json'); rr=read(path)
        if not rr and not a.offline:
            time.sleep(max(0,3-(time.monotonic()-previous)));previous=time.monotonic()
            url='https://export.arxiv.org/api/query'; params={'id_list':','.join(batch),'max_results':len(batch)}
            try:
                r=requests.get(url,params=params,headers={'User-Agent':'BenchmarkConstitution/BCI-0.2 (research date metadata)'},timeout=(8,30));rr={'url':r.url,'accessed':stamp(),'status':r.status_code,'text':r.text if r.status_code==200 else None};write(path,rr)
            except requests.RequestException: rr={'status':None}
        rr=rr or {};statuses[str(rr.get('status'))]=statuses.get(str(rr.get('status')),0)+1
        if rr.get('status')==200 and rr.get('text'):
            try:
                root=ET.fromstring(rr['text']);ns={'a':'http://www.w3.org/2005/Atom'}
                for e in root.findall('a:entry',ns):
                    ident=e.findtext('a:id',default='',namespaces=ns).split('/abs/')[-1].split('v')[0]
                    if ident in ids:
                        records[ident]={'first_submitted_at':e.findtext('a:published',namespaces=ns),'title':' '.join(e.findtext('a:title',default='',namespaces=ns).split()),'source':{'url':'https://arxiv.org/abs/'+ident,'accessed':rr['accessed'],'api_url':rr['url']}}
            except ET.ParseError: pass
        elif rr.get('status') in (401,403,429):
            # Stop on provider denial/rate limit, preserve already acquired data; no bypass.
            break
        write(BASE/'impact/arxiv-dates.json',{'generated_at':stamp(),'items':records,'statuses':statuses})
        print(json.dumps({'batch':len(batch),'status':rr.get('status'),'dated':len(records),'total_ids':len(ids)}),flush=True)
    write(BASE/'impact/arxiv-dates.json',{'generated_at':stamp(),'items':records,'statuses':statuses,'elapsed_seconds':time.monotonic()-start})
if __name__=='__main__':main()
