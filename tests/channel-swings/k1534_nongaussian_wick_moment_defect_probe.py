#!/usr/bin/env python3
"""Hostile mutations for K1534."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1534-nongaussian-wick-moment-defect.json').read_text())
def valid(x):
 q,d=x['moment_defect'],x['decision']
 return all([x['claim_id']=='K1534','4h(x)mu3(x)+mu4(x)-3v(x)^2' in q['exact_identity'],'0<=beta<c_*' in q['wick_dominant_class'],'(c_*-beta)C_N V_N' in q['class_coercivity'],'nonnegative fourth cumulants' in q['non_gaussian_members'],'kappa4(Y)=-2a^4' in q['smooth_two_well_counterexample'],'6epsilon(2-epsilon)C_N^2' in q['cutoff_cat_squeeze'],'Theta(N^4/epsilon)' in q['cat_squeeze_cost'],'platykurtic' in q['scope_guard'],d['exact_nongaussian_moment_identity_proved'],d['material_nongaussian_class_identified'],d['variance_only_wick_coercivity_false'],not d['cat_squeeze_order_N2_trial_exists'],not d['all_nongaussian_states_classified'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1533'),(('moment_defect','exact_identity'),'changed'),(('moment_defect','wick_dominant_class'),'changed'),(('moment_defect','class_coercivity'),'changed'),(('moment_defect','non_gaussian_members'),'changed'),(('moment_defect','smooth_two_well_counterexample'),'changed'),(('moment_defect','cutoff_cat_squeeze'),'changed'),(('moment_defect','cat_squeeze_cost'),'changed'),(('moment_defect','scope_guard'),'changed'),(('decision','exact_nongaussian_moment_identity_proved'),False),(('decision','material_nongaussian_class_identified'),False),(('decision','variance_only_wick_coercivity_false'),False),(('decision','cat_squeeze_order_N2_trial_exists'),True),(('decision','all_nongaussian_states_classified'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
