#!/usr/bin/env python3
"""Hostile mutations for K1545."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1545-lamellar-ultraviolet-sign-mass.json').read_text())
def valid(x):
 q,d=x['shell_tradeoff'],x['decision'];return all([x['claim_id']=='K1545','sgn(sin(Mx_1))' in q['actual_sign'],'8/pi^2' in q['exact_shell_mass'],'Theta_alpha(M/N)' in q['shell_scale'],'c_alpha H_' in q['coupled_tradeoff'],'Omega(N^4)' in q['fixed_shell_consequence'],'lamellar square-wave sign class only' in q['scope_guard'],d['outer_shell_mass_computed'],d['interaction_shell_tradeoff_proved'],d['fixed_shell_mass_forces_quartic_interaction'],not d['universal_inverse_theorem_proved'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1544'),(('shell_tradeoff','actual_sign'),'changed'),(('shell_tradeoff','exact_shell_mass'),'changed'),(('shell_tradeoff','shell_scale'),'changed'),(('shell_tradeoff','coupled_tradeoff'),'changed'),(('shell_tradeoff','fixed_shell_consequence'),'changed'),(('shell_tradeoff','scope_guard'),'changed'),(('decision','outer_shell_mass_computed'),False),(('decision','interaction_shell_tradeoff_proved'),False),(('decision','fixed_shell_mass_forces_quartic_interaction'),False),(('decision','universal_inverse_theorem_proved'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
