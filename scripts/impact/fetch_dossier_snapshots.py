"""Read-only public dataset snapshots, resumable; no authentication."""
import json,time,hashlib
from pathlib import Path
import requests
from common import write,read,stamp,BASE
root=BASE/'impact/cache/dossiers';root.mkdir(exist_ok=True)
s=requests.Session();s.headers['User-Agent']='BenchmarkConstitution evidence review (public dataset; no auth)'
for i,p in enumerate(sorted(Path('/workspace/benchmark-atlas/data/benchmarks').glob('*.json')),1):
 dest=root/p.name
 if read(dest,{}).get('accessed','').startswith('2026-11-08'):continue
 url='https://raw.githubusercontent.com/ZiChenWang114514/benchmark-constitution/main/data/benchmarks/'+p.name
 try:
  r=s.get(url,timeout=20);obj={'url':url,'accessed':stamp(),'status':r.status_code,'data':r.json() if r.status_code==200 else None}
 except Exception as e:obj={'url':url,'accessed':stamp(),'status':None,'error':type(e).__name__}
 write(dest,obj)
 if i%10==0:print(i,obj['status'],flush=True)
 if obj['status']in (401,403,429): print('STOP host rejected',flush=True);break
 time.sleep(.55)
