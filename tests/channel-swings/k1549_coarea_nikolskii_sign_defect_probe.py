#!/usr/bin/env python3
"""Hostile mutations for K1549."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1549-coarea-nikolskii-sign-defect.json').read_text())
def valid(x):
 q,d=x['inverse_theorem'],x['decision'];return all([x['claim_id']=='K1549','||grad f_N||_4<=C N' in q['gradient_control'],'C N mu(B)^(3/4)' in q['transition_volume'],'I_eta>0' in q['coarea_lower_bound'],'N^(-4/3)' in q['conclusion'],'not a claimed sharp' in q['scope_guard'],d['coarea_interface_bound_proved'],d['l4_bernstein_gradient_bound_proved'],d['universal_fixed_shell_defect_floor_proved'],not d['exponent_sharpness_proved'],not d['capacity_required_for_configuration_exclusion'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1548'),(('inverse_theorem','gradient_control'),'changed'),(('inverse_theorem','coarea_lower_bound'),'changed'),(('inverse_theorem','conclusion'),'changed'),(('inverse_theorem','scope_guard'),'changed'),(('decision','coarea_interface_bound_proved'),False),(('decision','l4_bernstein_gradient_bound_proved'),False),(('decision','universal_fixed_shell_defect_floor_proved'),False),(('decision','exponent_sharpness_proved'),True),(('decision','capacity_required_for_configuration_exclusion'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
