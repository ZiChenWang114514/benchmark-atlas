"""Synthetic unit tests only; fixture values never enter production outputs."""
import unittest, tempfile, json
from pathlib import Path
from common import merge_registry
from compute import compute, scale, WEIGHTS

class Tests(unittest.TestCase):
    def test_weights(self): self.assertAlmostEqual(sum(WEIGHTS.values()),1)
    def test_zero(self): self.assertEqual(scale(0,[0,0]),0)
    def test_monotone(self): self.assertLess(scale(1,[1,2,100]),scale(100,[1,2,100]))
    def test_null(self): self.assertIsNone(scale(None,[1]))
    def test_dedup_alias_does_not_merge_versions(self):
        with tempfile.TemporaryDirectory() as d:
            rows=[dict(id='base',name='Base',domain='代码',sources=[{'url':'https://example.org','accessed':'2026-11-07'}],homepage='https://example.org',aliases=[]),dict(id='base-pro',name='Base Pro',aliases=['Base'],domain='代码',sources=[{'url':'https://example.org','accessed':'2026-11-07'}],homepage='https://example.org')]
            Path(d,'x.jsonl').write_text('\n'.join(json.dumps(r) for r in rows))
            self.assertEqual(len(merge_registry(d)[0]),2)
    def test_missing_impact_not_scored(self):
        x=[dict(id='one',name='One',domain='代码',description_zh='a useful sufficiently long scientific benchmark description',metrics={})]
        index,_=compute(x,Path('/nonexistent'))
        self.assertIsNone(index['unscored'][0]['score'])
        self.assertTrue(all(v is None for v in index['unscored'][0]['components'].values()))
    def test_missing_values_reweight_not_zero(self):
        x=[dict(id='one',name='One',domain='代码',metrics={'gh_stars':100})]
        index,_=compute(x,Path('/nonexistent')); row=index['unscored'][0]
        self.assertIsNone(row['score']); self.assertIsNotNone(row['observed_score']); self.assertIsNone(row['components']['quality']); self.assertEqual(row['status'],'insufficient_evidence')
        self.assertFalse(row['confidence']['official_rank_eligible'])
        self.assertAlmostEqual(row['confidence']['coverage'],.08*.65)
    def test_flawed_cap_requires_evidence(self):
        x=[dict(id='one',name='One',domain='代码',metrics={'gh_stars':100},assessment={'epoch_verdict':{'value':'Flawed','sources':[{'url':'https://epoch.ai/test','accessed':'2026-11-07'}]}})]
        row=compute(x,Path('/nonexistent'))[0]['unscored'][0]
        self.assertLessEqual(row['shrunk_score'],40); self.assertIn('flawed',row['flags'])
    def test_no_title_short_acronym_guess(self):
        from enrich import matched
        self.assertFalse(matched({'title':'MMLU: an unrelated paper'},{'name':'MMLU'}))
        self.assertTrue(matched({'locations':[{'landing_page_url':'https://arxiv.org/abs/2009.03300'}]},{'name':'MMLU','arxiv_id':'2009.03300'}))

    def test_canonical_adoption_beats_parent_alias(self):
        from compute import frontier
        rows=[dict(id='mmlu',name='MMLU',aliases=['MMMLU'],metrics={}),dict(id='mmmlu',name='MMMLU',aliases=['MMLU'],metrics={})]
        with tempfile.TemporaryDirectory() as d:
            p=Path(d,'heat.json'); p.write_text(json.dumps({'models':[],'ranking':[{'benchmark_id':'mmlu','count':2},{'benchmark_id':'mmmlu','count':5}]}))
            frontier(rows,p)
        self.assertEqual(rows[0]['metrics']['model_card_mentions'],2)
        self.assertEqual(rows[1]['metrics']['model_card_mentions'],5)

    def test_audit_occurrence_renaming_before_same_id_merge(self):
        from unittest.mock import patch
        def row(name,paper): return dict(id='collision',name=name,domain='代码',paper_url='https://arxiv.org/abs/'+paper,arxiv_id=paper,homepage='https://example.org',sources=[{'url':'https://example.org','accessed':'2026-11-07'}])
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); reg=root/'registry'; reg.mkdir(); (root/'audit').mkdir(); (root/'impact').mkdir()
            one=row('Different benchmark','2501.00001'); two=row('Original benchmark','2401.00001')
            (reg/'general.jsonl').write_text(json.dumps(one)+'\n'); (reg/'harness.jsonl').write_text(json.dumps(two)+'\n')
            fix={'id':'collision','action':'fix','field':'id','old':'collision','new':'collision-extension','reason':'general.jsonl only. independent benchmark','source_url':'https://example.org'}
            (root/'audit/gen-harness.corrections.jsonl').write_text(json.dumps(fix)+'\n')
            with patch('common.BASE',root): xs,report=merge_registry(reg)
            self.assertEqual({x['id'] for x in xs},{'collision','collision-extension'})
            self.assertEqual({x['arxiv_id'] for x in xs},{'2501.00001','2401.00001'})

    def test_audit_self_merge_removes_only_exact_old_occurrence(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); reg=root/'registry'; reg.mkdir(); (root/'audit').mkdir(); (root/'impact').mkdir()
            one=dict(id='same',name='Same',domain='代码',homepage='https://example.org',sources=[{'url':'https://example.org','accessed':'2026-11-07'}])
            two={**one,'subdomain':'harness prompt variant'}
            (reg/'general.jsonl').write_text(json.dumps(one)+'\n'); (reg/'harness.jsonl').write_text(json.dumps(two)+'\n')
            merge={'id':'same','action':'merge_into','target_id':'same','field':'$record','old':two,'reason':'harness.jsonl occurrence only','source_url':'https://example.org'}
            (root/'audit/gen-harness.corrections.jsonl').write_text(json.dumps(merge)+'\n')
            with patch('common.BASE',root): xs,report=merge_registry(reg)
            self.assertEqual(len(xs),1); self.assertEqual(len(xs[0]['variants']),1)
            self.assertEqual(xs[0]['variants'][0]['original'],two)

    def test_shared_paper_not_summed(self):
        rows=[dict(id='one',name='One',domain='代码',arxiv_id='2401.12345',metrics={'citations':100,'paper_date':'2024-01-01'}),dict(id='two',name='Two',domain='代码',arxiv_id='2401.12345',metrics={'citations':100,'paper_date':'2024-01-01'})]
        compute(rows,Path('/nonexistent'))
        self.assertAlmostEqual(rows[0]['metrics']['attributed_citations'],100/(2**.5))

    def test_insufficient_rows_never_ranked(self):
        rows=[dict(id='one',name='One',domain='代码',metrics={'gh_stars':100})]
        index,_=compute(rows,Path('/nonexistent'))
        self.assertEqual(index['ranking'],[])
        self.assertIsNone(index['unscored'][0]['rank'])
        self.assertEqual(index['minimum_ranking_coverage'],.4)


    def test_science2_deltas_do_not_revert_audited_dates(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); reg=root/'registry'; reg.mkdir(); (root/'audit').mkdir(); (root/'impact').mkdir()
            one=dict(id='science-test',name='Science Test',domain='物理',release_date='2020-01-01',organization=None,homepage='https://example.org',sources=[{'url':'https://example.org','accessed':'2026-11-07'}])
            (reg/'science.jsonl').write_text(json.dumps(one)+'\n')
            (reg/'science2.jsonl').write_text(json.dumps({**one,'organization':'Verified Institute'})+'\n')
            (root/'audit/sci-mm.corrections.jsonl').write_text(json.dumps({'id':'science-test','action':'fix','field':'release_date','old':'2020-01-01','new':'2020-05-01','reason':'verified arxiv v1','source_url':'https://example.org'})+'\n'+json.dumps({'id':'science-test','action':'fix','field':'organization','old':None,'new':'Audit Institute','reason':'verified organization','source_url':'https://example.org'})+'\n')
            (root/'audit/science2.changes.jsonl').write_text(json.dumps({'id':'science-test','field':'organization','old':None,'new':'Verified Institute','source_url':'https://example.org','accessed':'2026-11-07'})+'\n')
            with patch('common.BASE',root): xs,_=merge_registry(reg)
            self.assertEqual(xs[0]['release_date'],'2020-05-01'); self.assertEqual(xs[0]['organization'],'Audit Institute')

    def test_shrinkage_is_convex_and_supported_rows_only(self):
        rows=[dict(id=f'bench-{i}',name=f'Benchmark {i}',domain='代码',release_date=f'2018-{i%12+1:02d}-01',description_zh='A detailed synthetic benchmark evaluating program generation and tests.',metrics={'citations':(i+1)*100,'gh_stars':100+i,'hf_downloads':100+i,'hf_likes':i,'gh_pushed_at':'2026-11-01'}) for i in range(30)]
        index,_=compute(rows,Path('/nonexistent'))
        self.assertTrue(index['ranking'])
        for r in index['ranking']:
            prior=r['shrinkage']['prior']; raw=r['observed_score']
            self.assertGreaterEqual(r['confidence']['coverage'],.4)
            self.assertGreaterEqual(r['score'],min(prior,raw)-.01)
            self.assertLessEqual(r['score'],max(prior,raw)+.01)


    def test_host_cooldown_expiry_is_not_sliding_on_resume(self):
        from unittest.mock import patch
        from types import SimpleNamespace
        from enrich import Client
        from common import stamp
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'impact').mkdir()
            (root/'impact/enrich-report.json').write_text(json.dumps({'generated_at':stamp(),'blocked_auth_hosts':['api.github.com']}))
            with patch('enrich.BASE',root):
                one=Client(SimpleNamespace()); until=one.blocked_until['api.github.com']
                two=Client(SimpleNamespace()); self.assertEqual(two.blocked_until['api.github.com'],until)

if __name__=='__main__': unittest.main()
