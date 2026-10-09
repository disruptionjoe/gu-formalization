#!/usr/bin/env python3
"""Hostile mutations for K1535."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1535-low-wick-fisher-shell-coercivity.json').read_text())
def valid(x):
 q,d=x['shell_coercivity'],x['decision']
 return all([x['claim_id']=='K1535','Tr(P_N Lambda)>=kappa C_N' in q['shell_constants'],'N^(-2)' in q['shell_constants'],'V_N=Tr(Lambda S)<=eta C_N' in q['low_wick_to_variance'],'(kappa-eta)C_N' in q['shell_deficit'],'delta_N^2<=' in q['frobenius_bound'],'a_N eta C_N' in q['dual_bound'],'(kappa-eta)^2 C_N/(a_N eta)' in q['fisher_consequence'],'kappa C_N/(8a_N)' in q['midpoint'],'moment-defect budget' in q['scope_guard'],d['low_wick_forces_high_fisher_in_M_beta'],d['noncommutative_shell_order_preserved'],not d['stationarity_or_independent_modes_required'],not d['unrestricted_nongaussian_lower_bound_proved'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1534'),(('shell_coercivity','shell_constants'),'changed'),(('shell_coercivity','low_wick_to_variance'),'changed'),(('shell_coercivity','shell_deficit'),'changed'),(('shell_coercivity','frobenius_bound'),'changed'),(('shell_coercivity','dual_bound'),'changed'),(('shell_coercivity','fisher_consequence'),'changed'),(('shell_coercivity','midpoint'),'changed'),(('shell_coercivity','scope_guard'),'changed'),(('decision','low_wick_forces_high_fisher_in_M_beta'),False),(('decision','noncommutative_shell_order_preserved'),False),(('decision','stationarity_or_independent_modes_required'),True),(('decision','unrestricted_nongaussian_lower_bound_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
