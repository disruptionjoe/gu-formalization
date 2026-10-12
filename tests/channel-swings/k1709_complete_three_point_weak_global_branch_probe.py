#!/usr/bin/env python3
"""Hostile semantic mutations for K1709."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1709-complete-three-point-weak-global-branch.json').read_text())
def valid(x):
 q,z=x.get('global_branch',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1709','[1/3,1]' in q.get('parameter_space',''),'positive relative Fisher' in q.get('strong_channel_exclusion',''),
  'kappa_6=-6' in q.get('vanishing_defect_exclusion',''),'p_*' in q.get('interior_selection',''),'unique global branch' in q.get('uniqueness',''),
  z.get('complete_negative_kurtosis_three_point_family_controlled'),z.get('vanishing_fourth_defect_escape_excluded_in_family'),
  z.get('unique_small_reward_global_branch'),not z.get('general_vanishing_defect_seed_families_controlled'),
  'only to the symmetric three-point family' in x.get('scope_guard','')])
def setp(x,p,v):
 y=copy.deepcopy(x);c=y
 for k in p[:-1]:c=c[k]
 c[p[-1]]=v;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1708'),(('global_branch','parameter_space'),'all seeds'),(('global_branch','strong_channel_exclusion'),'none'),
  (('global_branch','vanishing_defect_exclusion'),'endpoint escapes'),(('global_branch','interior_selection'),'any p'),
  (('global_branch','uniqueness'),'multiple'),(('decision','complete_negative_kurtosis_three_point_family_controlled'),False),
  (('decision','vanishing_fourth_defect_escape_excluded_in_family'),False),(('decision','unique_small_reward_global_branch'),False),
  (('decision','general_vanishing_defect_seed_families_controlled'),True),(('scope_guard',),'all seeds')]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
