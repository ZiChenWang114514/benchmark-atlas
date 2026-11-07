import re,time
from bs4 import BeautifulSoup
import requests
from common import BASE,read,write,stamp
root=BASE/'impact/cache/epoch-reviews';root.mkdir(exist_ok=True)
s=requests.Session();s.headers['User-Agent']='BenchmarkConstitution public independent-review research; no auth'
urls=['https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks','https://epoch.ai/data/benchmark-reviews-documentation/methodology']
urls += ['https://epoch.ai/benchmarks/'+slug+'/review' for slug in ['hle','swe-bench-verified','healthbench-professional','bfcl','deepswe','agents-last-exam','graphwalks','simpleqa-verified','posttrainbench','terminal-bench','swe-bench-pro']]
for url in urls:
 name=url.split('/')[-2] if url.endswith('/review') else url.split('/')[-1];p=root/(name+'.json')
 if read(p,{}).get('accessed','').startswith('2026-11-08'):continue
 try:
  r=s.get(url,timeout=20);soup=BeautifulSoup(r.text,'html.parser');main=soup.find('main')or soup
  res={'url':url,'accessed':stamp(),'status':r.status_code,'text':main.get_text(' ',strip=True) if r.status_code==200 else None}
 except Exception as e:res={'url':url,'accessed':stamp(),'status':None,'error':type(e).__name__}
 write(p,res);print(name,res['status'],flush=True)
 if res['status']in (401,403,429):print('STOP host rejection');break
 time.sleep(.8)
