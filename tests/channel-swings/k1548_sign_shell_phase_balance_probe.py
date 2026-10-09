#!/usr/bin/env python3
"""Hostile mutations for K1548."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1548-sign-shell-phase-balance.json').read_text())
def valid(x):
 q,d=x['phase_balance'],x['decision'];return all([x['claim_id']=='K1548','||s_N-f_N||_2^2<=delta_N' in q['tail_bridge'],'4p_N(1-p_N)' in q['variance_bridge'],'eta/4' in q['phase_floor'],'eta/8' in q['good_core'],d['universal_tail_bound_proved'],d['shell_phase_balance_proved'],d['macroscopic_core_phases_proved'],not d['transition_defect_exponent_proved'],not d['capacity_computed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1547'),(('phase_balance','tail_bridge'),'changed'),(('phase_balance','variance_bridge'),'changed'),(('phase_balance','phase_floor'),'changed'),(('phase_balance','good_core'),'changed'),(('decision','universal_tail_bound_proved'),False),(('decision','shell_phase_balance_proved'),False),(('decision','macroscopic_core_phases_proved'),False),(('decision','transition_defect_exponent_proved'),True),(('decision','capacity_computed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
