"""Version-checked mapping of independently published reviews inspected 2026-11-08.
No fuzzy mappings; current-version mismatches are historical only.
"""
import re
from common import BASE,read,write,stamp
root=BASE/'impact/cache/epoch-reviews';rows=[]
for slug,target,version in [('hle','hle','original HLE; excludes HLE-Rolling, HLE-Verified and HLE-Diamond'),('swe-bench-verified','swe-bench-verified','500-problem Verified subset'),('healthbench-professional','healthbench-professional','Professional 525-task release; NOT HealthBench general'),('deepswe','deepswe','v1.1'),('agents-last-exam','agents-last-exam','v1.1; 122 public tasks'),('graphwalks','graphwalks','reviewed public 1150-task release; version not separately specified'),('swe-bench-pro','swe-bench-pro','original 731 public / 276 private / 858 held-out; NOT Pro V2')]:
 d=read(root/(slug+'.json'),{})
 if d.get('status')!=200:continue
 text=d['text'];m=re.search(r'Verdict:\s*(Verified|Flawed|Not enough info)',text)
 if not m:continue
 i=text.find('Reviewed:')
 rows.append({'target_id':target,'reviewed_scope':version,'verdict':m.group(1),'sources':[{'url':d['url'],'accessed':d['accessed'],'quote':text[i:i+2600]}],'review_date_text':re.search(r'Reviewed:\s*(.*?) Benchmark creator:',text).group(1),'application':'exact reviewed scope only; no propagation to family/parent/child versions'})
d=read(root/'included-benchmarks.json')
for target,scope,verdict,dt in [('bfcl','BFCL v4','Flawed','2026-09-10'),('simpleqa-verified','SimpleQA Verified; not original SimpleQA','Verified','2026-09-10')]:
 rows.append({'target_id':target,'reviewed_scope':scope,'verdict':verdict,'review_date':dt,'sources':[{'url':d['url'],'accessed':d['accessed'],'table_row_summary':scope+' | '+verdict+' | '+dt}],'application':'exact reviewed scope from official review table; individual guessed route returned 404'})
for target,scope,verdict,dt in [('posttrainbench','v1.1; current dossier is v1.2','Verified','2026-09-09'),('terminal-bench','4.0.0; current latest release 4.1.0, leaderboards still 4.0','Flawed','2026-09-04')]:
 rows.append({'target_id':target,'reviewed_scope':scope,'verdict':verdict,'review_date':dt,'sources':[{'url':d['url'],'accessed':d['accessed'],'table_row_summary':target+' '+scope+' | '+verdict+' | '+dt}],'application':'historical_only; current version mismatch/ambiguity, NO score or flaw cap'})
write(BASE/'impact/independent-quality.json',{'generated_at':stamp(),'reviews':rows})
print([(r['target_id'],r['verdict'])for r in rows])
