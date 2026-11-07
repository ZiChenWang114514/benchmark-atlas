"""Refresh only existing official dataset IDs; public evidence, sequential pacing."""
import hashlib,time
from urllib.parse import quote
import requests
from common import BASE,read,write,stamp,merge_registry
items,_=merge_registry(BASE/'registry');ids=set()
for x in items:
 ds=x.get('hf_dataset')
 if isinstance(ds,str) and '/' in ds:ids.add(ds.removeprefix('https://huggingface.co/datasets/').strip('/'))
root=BASE/'impact/cache/hf-cards';root.mkdir(exist_ok=True);s=requests.Session();s.headers['User-Agent']='BenchmarkConstitution documentary research (public metadata, no auth)'
for i,ds in enumerate(sorted(ids,key=lambda s:hashlib.sha256(s.encode()).hexdigest()),1):
 p=root/(hashlib.sha256(ds.encode()).hexdigest()+'.json')
 if read(p,{}).get('accessed','').startswith('2026-11-08'):continue
 url='https://huggingface.co/api/datasets/'+quote(ds,safe='/')
 try:
  r=s.get(url,timeout=15);res={'url':url,'accessed':stamp(),'status':r.status_code,'dataset':ds,'data':r.json() if r.status_code==200 else None}
 except Exception as e:res={'url':url,'accessed':stamp(),'status':None,'dataset':ds,'error':type(e).__name__}
 write(p,res)
 if i%25==0:print(i,len(ids),res['status'],flush=True)
 if res['status']==429:print('STOP 429; resume later without retry',flush=True);break
 time.sleep(.6)
print('completed pass',flush=True)
