"""Occurrence-aware audited registry merge. Audit proposals are DATA, never code.
An immutable source row binds fixes/merges before ID renames. Entire historical rows
are retained as variants; independent benchmarks sharing IDs are never blindly overwritten.
"""
import copy, hashlib, json, re
from collections import Counter, defaultdict
from pathlib import Path

def merge(directory):
    from common import BASE, norm, read
    directory=Path(directory); occurrences=[]; invalid=[]; conflicts=[]; events=[]
    for f in sorted(directory.glob('*.jsonl')):
        if f.name=='science2.jsonl': continue
        for line_no,line in enumerate(f.read_text().splitlines(),1):
            if not line.strip(): continue
            try:
                x=json.loads(line)
                if not all(x.get(k) for k in ('id','name','domain','sources')): raise ValueError('missing required identity/source')
                if not any(x.get(k) for k in ('paper_url','github_url','homepage')): raise ValueError('missing primary URL')
                occurrences.append({'shard':f.name,'line':line_no,'original':copy.deepcopy(x),'row':copy.deepcopy(x),'fixed':set(),'removed':False})
            except (ValueError,TypeError) as e: invalid.append({'file':f.name,'line':line_no,'error':str(e)})
    input_rows=len(occurrences)
    audits=[]
    audit_dir=BASE/'audit' if directory.resolve()==(BASE/'registry').resolve() else directory.parent/'audit'
    for f in sorted(audit_dir.glob('*.corrections.jsonl')):
        for line_no,line in enumerate(f.read_text().splitlines(),1):
            if line.strip(): audits.append({'file':f.name,'line':line_no,'proposal':json.loads(line)})
    # Bind all actions to immutable original source occurrences BEFORE any field mutation.
    bound=[]; unresolved=[]
    for audit in audits:
        a=audit['proposal']; action=a.get('action')
        if action=='add': bound.append((audit,[])); continue
        candidates=[i for i,o in enumerate(occurrences) if o['original']['id']==a.get('id')]
        if isinstance(a.get('old'),dict) and a.get('field')=='$record':
            candidates=[i for i in candidates if occurrences[i]['original']==a['old']]
        elif audit['file'].startswith('gen-harness'):
            shard=re.search(r'(general|harness)\.jsonl',a.get('reason',''))
            if shard: candidates=[i for i in candidates if occurrences[i]['shard']==shard.group(0)]
        else:
            candidates=[i for i in candidates if occurrences[i]['shard'] in ('science.jsonl','multimodal.jsonl')]
            url=a.get('source_url')
            exact=[i for i in candidates if url and url in json.dumps(occurrences[i]['original'],ensure_ascii=False)]
            if exact: candidates=exact
            elif 'science 与 multimodal' in a.get('reason',''):
                candidates=[i for i in candidates if occurrences[i]['shard']=='multimodal.jsonl']
            elif 'MTEB' in a.get('reason','') or '检索' in a.get('reason',''):
                scoped=[i for i in candidates if occurrences[i]['shard']=='multimodal.jsonl']
                if scoped: candidates=scoped
        if action=='fix' and 'old' in a and a.get('field')!='$record':
            guarded=[i for i in candidates if occurrences[i]['original'].get(a['field'])==a['old']]
            if guarded: candidates=guarded
            elif candidates and all(occurrences[i]['original'].get(a['field'])==a.get('new') for i in candidates):
                events.append({'action':'already_fixed','id':a.get('id'),'field':a.get('field'),'audit':audit['file']}); continue
            else: candidates=[]
        if not candidates:
            unresolved.append({'audit':audit['file'],'line':audit['line'],'id':a.get('id'),'action':action,'reason':'immutable occurrence/old-value guard did not match'}); continue
        if len(candidates)>1 and action in ('drop','merge_into'):
            # Never make a destructive blanket decision across same-ID independent rows.
            signatures={(occurrences[i]['original'].get('arxiv_id'),occurrences[i]['original'].get('paper_url'),occurrences[i]['original'].get('github_url')) for i in candidates}
            if len(signatures)>1:
                unresolved.append({'audit':audit['file'],'line':audit['line'],'id':a.get('id'),'action':action,'reason':'ambiguous occurrence across independent source rows'}); continue
        bound.append((audit,candidates))
    def source(a): return {'url':a['source_url'],'accessed':'2026-11-07'} if a.get('source_url') else None
    for audit,selected in bound:
        a=audit['proposal']
        if a['action']!='fix': continue
        if a.get('new') is None and a.get('field')=='id':
            for i in selected: occurrences[i]['row']['identity_review']='generic_name_pending_official_confirmation'
            events.append({'action':'deferred_naming_review','id':a['id'],'reason':a.get('reason'),'source_url':a.get('source_url')}); continue
        for i in selected:
            o=occurrences[i]; o['row'][a['field']]=copy.deepcopy(a.get('new')); o['fixed'].add(a['field'])
            o.setdefault('audit_history',[]).append({'action':'fix','field':a['field'],'old':a.get('old'),'new':a.get('new'),'reason':a.get('reason'),'source_url':a.get('source_url')})
            ref=source(a)
            if ref and ref not in o['row'].setdefault('sources',[]): o['row']['sources'].append(ref)
            events.append({'action':'fix','id':a['id'],'field':a['field'],'shard':o['shard']})
    for audit,selected in bound:
        a=audit['proposal']
        if a['action']=='add':
            x=copy.deepcopy(a.get('row') or a.get('new'))
            if not isinstance(x,dict): unresolved.append({'id':a.get('id'),'action':'add','reason':'missing complete row'}); continue
            providers={'https://artificialanalysis.ai/evaluations':'Artificial Analysis','https://scale.com/leaderboard':'Scale SEAL','https://www.vals.ai/benchmarks':'Vals'}
            if a.get('source_url') in providers and 'Currently listed on an official evaluator page' in a.get('reason',''):
                x.setdefault('assessment',{})['evaluator_adoptions']={'value':[providers[a['source_url']]],'sources':[source(a)],'basis':'verified current evaluator catalogue in occurrence-aware audit'}
            occurrences.append({'shard':'audit-add:'+audit['file'],'line':audit['line'],'original':copy.deepcopy(x),'row':x,'fixed':{k for k,v in x.items() if v is not None},'removed':False,'audit_history':[{'action':'add','reason':a.get('reason'),'source_url':a.get('source_url')}]})
            events.append({'action':'add','id':x['id']})
    # Apply ONLY science2's actual field deltas after the audits. This is equivalent
    # to science2-first + audit-second and cannot restore stale publication dates.
    improved=directory/'science2.jsonl'; improved_rows=0
    delta_path=BASE/'audit/science2.changes.jsonl'; deltas=defaultdict(list)
    if delta_path.exists() and directory.resolve()==(BASE/'registry').resolve():
        for line in delta_path.read_text().splitlines():
            if line.strip():
                d=json.loads(line); deltas[d['id']].append(d)
    if improved.exists():
        for line_no,line in enumerate(improved.read_text().splitlines(),1):
            if not line.strip(): continue
            x=json.loads(line); improved_rows+=1
            candidates=[o for o in occurrences if o['shard']=='science.jsonl' and o['original']['id']==x['id']]
            if len(candidates)==1:
                o=candidates[0]
                if deltas:
                    for change in deltas.get(x['id'],[]):
                        field=change['field']
                        if field in o['fixed'] and o['row'].get(field)!=change.get('new'):
                            events.append({'action':'science2_delta_superseded_by_audit','id':x['id'],'field':field,'kept':o['row'].get(field)})
                            continue
                        if o['original'].get(field)!=change.get('old') and o['row'].get(field)!=change.get('old'):
                            if o['row'].get(field)==change.get('new'): continue
                            unresolved.append({'action':'science2_fix','id':x['id'],'field':field,'reason':'old-value guard failed'}); continue
                        o['row'][field]=copy.deepcopy(change.get('new'));o['fixed'].add(field)
                else:
                    for field,value in x.items():
                        if field not in ('id','release_date','arxiv_id','doi','paper_url','name') and field not in o['fixed']:
                            o['row'][field]=copy.deepcopy(value);o['fixed'].add(field)
                o['row'].setdefault('sources',[])
                o['row']['sources'] += [z for z in x.get('sources',[]) if z not in o['row']['sources']]
                o.setdefault('audit_history',[]).append({'action':'science2_field_deltas','source_shard':'science2.jsonl','line':line_no,'protected_fields':['release_date','id','paper_url','arxiv_id','doi']})
            else:
                occurrences.append({'shard':'science2.jsonl','line':line_no,'original':copy.deepcopy(x),'row':x,'fixed':{k for k,v in x.items() if v is not None},'removed':False})
    reserved={norm(o['original']['id']) for o in occurrences if o['shard'] in ('general.jsonl','harness.jsonl','frontier.jsonl')}
    def priority(o):
        return (0 if o['shard'].startswith('audit-add:') else 1 if o['shard']=='science2.jsonl' else 2 if o['fixed'] else 3, {'general.jsonl':0,'harness.jsonl':1,'science.jsonl':2,'multimodal.jsonl':3,'frontier.jsonl':4}.get(o['shard'],5),o['line'])
    def add_variant(target,donor,reason):
        snap={'source_shard':donor['shard'],'source_line':donor['line'],'original':copy.deepcopy(donor['original']),'corrected':copy.deepcopy(donor['row']),'audit':copy.deepcopy(donor.get('audit_history',[])),'merge_reason':reason}
        target['row'].setdefault('variants',[]).append(snap)
    def consolidate(target,donor,reason,family=False):
        t,d=target['row'],donor['row']; add_variant(target,donor,reason)
        for key,value in d.items():
            if key in ('id','variants','aliases','metrics','audit_history'): continue
            if key=='sources':
                t.setdefault(key,[]); t[key]+=[z for z in value if z not in t[key]]; continue
            # Family/subtask metadata is historical, NOT evidence about the family as a whole.
            if family: continue
            if key in donor['fixed'] and key not in target['fixed']:
                t[key]=copy.deepcopy(value); target['fixed'].add(key)
            elif key in target['fixed']:
                if value is not None and t.get(key)!=value: conflicts.append({'id':t['id'],'field':key,'values':[t.get(key),value],'source_shard':donor['shard'],'resolved':True,'resolution':'verified_field_including_null_precedence'})
            elif not t.get(key): t[key]=copy.deepcopy(value)
            elif value is not None and t.get(key)!=value and key not in ('description_zh','discovered_via'):
                conflicts.append({'id':t['id'],'field':key,'values':[t.get(key),value],'source_shard':donor['shard'],'resolved':key in target['fixed'],'resolution':'verified_field_precedence' if key in target['fixed'] else 'unresolved_source_conflict'})
        if not family or norm(d['id']) not in reserved or donor['shard'] in ('general.jsonl','harness.jsonl'):
            t.setdefault('aliases',[])
            for alias in [d['id'],d.get('name')]+d.get('aliases',[]):
                if alias and alias not in t['aliases'] and alias!=t['id']: t['aliases'].append(alias)
        donor['removed']=True
    archives=[]; redirects=[]
    for audit,selected in bound:
        a=audit['proposal']; action=a['action']
        if action=='drop':
            for i in selected:
                o=occurrences[i]; o['removed']=True; archives.append({'action':'drop','source_shard':o['shard'],'source_line':o['line'],'original':o['original'],'reason':a.get('reason'),'source_url':a.get('source_url')}); events.append({'action':'drop','id':a['id'],'shard':o['shard']})
        elif action=='merge_into':
            for i in selected:
                donor=occurrences[i]
                if donor['removed']: continue
                targets=[o for j,o in enumerate(occurrences) if j!=i and not o['removed'] and o['row']['id']==a['target_id']]
                if not targets:
                    unresolved.append({'audit':audit['file'],'line':audit['line'],'id':a['id'],'action':action,'reason':'target absent or self-only; retained source'}); continue
                if 'science 与 multimodal' in a.get('reason',''):
                    science_targets=[o for o in targets if o['shard']=='science.jsonl']
                    if science_targets: targets=science_targets
                target=min(targets,key=priority)
                family=audit['file'].startswith('sci-mm') or a['id']!=a['target_id']
                consolidate(target,donor,a.get('reason'),family=family)
                redirects.append({'source_shard':donor['shard'],'old_id':a['id'],'target_id':target['row']['id'],'family':family})
                events.append({'action':'merge_into','id':a['id'],'target':target['row']['id'],'shard':donor['shard']})
    # Conservative exact-ID consolidation after audited collision renames. No alias-based merging.
    final=[]; by_id={}; by_name={}
    for o in sorted([o for o in occurrences if not o['removed']],key=priority):
        x=o['row']; key=norm(x['id']); existing=by_id.get(key)
        if existing is not None:
            prior=final[existing]
            pa=prior['row'].get('arxiv_id'); xa=x.get('arxiv_id')
            if pa and xa and pa.split('v')[0]!=xa.split('v')[0]:
                # Audited fixes prevail only if they explicitly established the canonical identity.
                if 'arxiv_id' in prior['fixed'] or 'arxiv_id' in o['fixed']:
                    consolidate(prior,o,'same-ID secondary occurrence; verified paper identity takes precedence',False)
                else:
                    # Preserve a stable distinct record rather than destroy either independent row.
                    suffix=hashlib.sha256((o['shard']+json.dumps(o['original'],sort_keys=True)).encode()).hexdigest()[:8]
                    x['id']=x['id']+'--'+suffix; x['identity_review']='same_id_different_paper'; final.append(o); by_id[norm(x['id'])]=len(final)-1
                    conflicts.append({'id':prior['row']['id'],'field':'identity_collision','other_id':x['id'],'source_shard':o['shard'],'values':[pa,xa]})
            else: consolidate(prior,o,'same canonical ID; independent source occurrence retained as history',False)
        else:
            by_id[key]=len(final); final.append(o)
    rows=[]
    for o in final:
        x=o['row']; x['audit_history']=o.get('audit_history',[])
        if x.get('curation'): x.pop('curation',None)
        # Additional verified curation is supplemental only; audit conclusions win.
        change=read(BASE/'impact/curations.json',{}).get('items',{}).get(x['id']) if directory.resolve()==(BASE/'registry').resolve() else None
        if change:
            applied={}
            for key,value in change['fields'].items():
                if key in o['fixed']: continue
                if key=='arxiv_id' and x.get(key) and value is None: continue
                applied[key]=x.get(key); x[key]=copy.deepcopy(value)
            if applied:
                x['curation']={'before':applied,'reason_zh':change['reason_zh'],'sources':change['sources'],'resolve_identity_conflict':change.get('resolve_identity_conflict',False)}
                for z in change['sources']:
                    if z not in x['sources']: x['sources'].append(z)
        families=read(BASE/'science2-work/families.json',{}) if directory.resolve()==(BASE/'registry').resolve() else {}
        for family,children in families.items():
            if x['id'] in children: x['family_id']=family; x['entry_type']='explicit_evaluation_subtask'
            elif x['id']==family: x['family_members']=children
        rows.append(x)
    audit_report={'input_rows':input_rows,'merged_count':len(rows),'duplicates_merged':sum(e['action']=='merge_into' for e in events)+sum(len(x.get('variants',[])) for x in rows)-sum(e['action']=='merge_into' for e in events),'invalid_rows':invalid,'conflicts':conflicts,'audit_actions':dict(Counter(e['action'] for e in events)),'audit_unresolved':unresolved,'audit_events':events,'dropped_archive':archives,'occurrence_redirects':redirects,'science2_present':improved.exists(),'science2_rows':improved_rows,'history_preserved':True}
    return sorted(rows,key=lambda x:x['id']),audit_report
