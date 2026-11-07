"""Synthetic fixtures only. They are not exported to production evidence."""
import unittest
from pathlib import Path
from evidence_overlay import quality,leaderboard
from compute import compute

def snap(**fields):
 d={}
 for path,value in fields.items():
  x=d;bits=path.split('.')
  for k in bits[:-1]:x=x.setdefault(k,{})
  x[bits[-1]]={'value':value,'sources':[{'url':'https://example.org/primary','accessed':'2026-11-07'}]}
 return {'data':d,'url':'https://example.org/published-dossier.json','accessed':'2026-11-08'}

class EvidenceTests(unittest.TestCase):
 def test_unknown_not_zero(self):
  self.assertEqual(quality(snap(**{'construction.quality_control':'待核实','basic_info.license':'待核实'})),{})
 def test_license_conflict_stays_unknown(self):
  self.assertNotIn('license_clarity',quality(snap(**{'basic_info.license':'MIT与CC BY存在冲突，数据许可待核实'})))
 def test_documentary_not_independent_reproduction(self):
  a=quality(snap(**{'evaluation.official_scripts':'https://example.org/scripts','evaluation.scoring':'accuracy'}))
  self.assertEqual(a['reproducibility']['value'],50);self.assertEqual(a['reproducibility']['reliability'],.5)
 def test_negative_human_claim_not_positive(self):
  self.assertNotIn('human_validation',quality(snap(**{'construction.quality_control':'没有专家审核'})))
 def test_contamination_warning_not_control(self):
  self.assertNotIn('contamination_protection',quality(snap(**{'construction.decontamination':'没有检索式去重；公开题有污染风险'})))
 def test_no_unbounded_error_headroom(self):
  a=leaderboard(snap(**{'leaderboard.results':[{'score':.04,'metric':'RMSE','track':'current','source_url':'https://example.org/board'}]}))
  self.assertNotIn('sota_score',a)
 def test_no_historical_sota(self):
  a=leaderboard(snap(**{'leaderboard.results':[{'score':96,'metric':'Accuracy (%)','track':'论文历史结果','source_url':'https://example.org/board'}]}))
  self.assertNotIn('sota_score',a)
 def test_tracks_never_pool(self):
  rows=[{'score':60,'metric':'Accuracy (%)','track':'version A','source_url':'https://example.org/board'}, {'score':99,'metric':'Accuracy (%)','track':'version B','source_url':'https://example.org/board'}]
  a=leaderboard(snap(**{'leaderboard.results':rows}));self.assertEqual(len(a['saturation_tracks']['value']),2)
  self.assertEqual(a['sota_score']['selected_track']['n_results'],1)
 def test_secondary_access_date_not_forged_primary_access(self):
  a=quality(snap(**{'construction.quality_control':'专家验证'}))['human_validation']['sources'][0]
  self.assertEqual(a['url'],'https://example.org/published-dossier.json');self.assertEqual(a['upstream_sources'][0]['accessed'],'2026-11-07')
 def test_negative_audit_cannot_be_formal(self):
  proof=[{'url':'https://example.org/audit','accessed':'2026-11-08'}]
  assessment={k:{'value':100,'sources':proof} for k in ('human_validation','contamination_protection','reproducibility','license_clarity','maintenance_review','external_review')}
  assessment['epoch_verdict']={'value':'Flawed','sources':proof}
  row={'id':'test','name':'Test','domain':'代码','release_date':'2024-01-01','metrics':{'citations':100,'gh_stars':200,'gh_forks':30,'hf_downloads':300,'hf_likes':20},'assessment':assessment}
  index,_=compute([row],Path('/nonexistent'));out=(index['ranking']+index['unscored'])[0]
  self.assertFalse(out['confidence']['official_rank_eligible']);self.assertLessEqual(out['shrunk_score'],40)
 def test_documentary_quality_reliability_not_full(self):
  q=quality(snap(**{'construction.quality_control':'专家验证','construction.decontamination':'隐藏测试','evaluation.official_scripts':'https://example.org/scripts','evaluation.scoring':'accuracy','basic_info.license':'数据集MIT'}))
  proof=[{'url':'https://example.org/audit','accessed':'2026-11-08'}]
  row={'id':'test','name':'Test','domain':'代码','release_date':'2024-01-01','metrics':{'citations':100},'assessment':q}
  index,_=compute([row],Path('/nonexistent'));out=(index['ranking']+index['unscored'])[0]
  self.assertAlmostEqual(out['confidence']['quality_coverage'],.35);self.assertFalse(out['confidence']['official_rank_eligible'])
 def test_neutral_documentation_cannot_reduce_score(self):
  def entry(assessment=None):
   return {'id':'t','name':'Test','domain':'代码','release_date':'2024-01-01','metrics':{'citations':100,'gh_stars':50,'hf_downloads':100,'hf_likes':20},'assessment':assessment or {}}
  one=compute([entry()],Path('/nonexistent'))[0]
  a={'license_clarity':{'value':50,'reliability':.5,'sources':[{'url':'https://example.org/doc','accessed':'2026-11-08'}]}}
  two=compute([entry(a)],Path('/nonexistent'))[0]
  r1=(one['ranking']+one['unscored'])[0];r2=(two['ranking']+two['unscored'])[0]
  self.assertAlmostEqual(r1['shrunk_score'],r2['shrunk_score'],places=2)
 def test_renderer_is_not_an_evaluation_script(self):
  a=quality(snap(**{'evaluation.official_scripts':'渲染器 https://example.org/render，不能把渲染器当作完整benchmark评分代码','evaluation.scoring':'accuracy'}))
  self.assertNotIn('reproducibility',a)
 def test_code_only_license_cannot_establish_dataset_license(self):
  a=quality(snap(**{'basic_info.license':'Apache-2.0（GitHub仓库代码标示；不自动覆盖原题、第三方材料或私有测试数据）'}))
  self.assertNotIn('license_clarity',a)
if __name__=='__main__':unittest.main()
