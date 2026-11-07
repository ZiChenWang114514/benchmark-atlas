"""Local staging utilities. Never reads credential files or modifies the main repository."""
import json, re, os, hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta
BASE = Path(__file__).resolve().parent.parent
TZ = timezone(timedelta(hours=8))
def now(): return datetime.now(TZ)
def stamp(): return now().isoformat(timespec='seconds')
def write(path, value):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    os.replace(tmp,path)
def read(path, default=None):
    try: return json.loads(Path(path).read_text())
    except (OSError,ValueError): return default

def norm(x): return re.sub(r'[^\w]','',str(x or '').lower())
def date(x):
    if not x or not isinstance(x,str): return None
    try:
        if len(x)==4: x+='-07-01'
        if len(x)==7: x+='-15'
        return datetime.fromisoformat(x.replace('Z','+00:00')).replace(tzinfo=TZ) if len(x)==10 else datetime.fromisoformat(x.replace('Z','+00:00')).astimezone(TZ)
    except ValueError: return None

def fingerprint(item):
    x={k:v for k,v in item.items() if k not in ('metrics','_fingerprint')}
    return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False).encode()).hexdigest()

def merge_registry(directory):
    from registry_merge import merge
    return merge(directory)
