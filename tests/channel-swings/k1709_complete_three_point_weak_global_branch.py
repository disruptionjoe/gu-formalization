#!/usr/bin/env python3
"""Boundary and global-branch controls for K1709."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1709-complete-three-point-weak-global-branch.json').read_text());q,z=d['global_branch'],d['decision']
 p=(15+math.sqrt(105))/60;u=3-1/p;k6=lambda x:x**-2-15*x**-1+30
 samples=[1/3+10**(-n) for n in (1,2,3,4)]
 checks=[('schema',d['schema_version']=='1.0'),('claim',d['claim_id']=='K1709'),('compact family','[1/3,1]' in q['parameter_space']),
  ('support bound','sqrt(3)' in q['parameter_space']),('strong channel','positive relative Fisher' in q['strong_channel_exclusion']),
  ('endpoint k6 text','kappa_6=-6' in q['vanishing_defect_exclusion']),('endpoint k6 limit',abs(k6(samples[-1])+6)<0.01 and abs(k6(samples[-1])+6)<abs(k6(samples[-2])+6)),
  ('pstar interior',1/3<p<1),('u positive',u>0),('interior strict','nonnegative cubic square is strict' in q['interior_selection']),
  ('unique text','unique global branch' in q['uniqueness']),('family decision',z['complete_negative_kurtosis_three_point_family_controlled']),
  ('defect decision',z['vanishing_fourth_defect_escape_excluded_in_family']),('unique decision',z['unique_small_reward_global_branch']),
  ('general open',not z['general_vanishing_defect_seed_families_controlled']),('scope','only to the symmetric three-point family' in d['scope_guard'])]
 for n,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {n:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
