#!/usr/bin/env python3
"""Hostile mutations for K1577."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1577-wick-dominant-profiled-coefficient.json').read_text())
def valid(x):
 q,d=x['coefficient_theorem'],x['decision'];return all([x['claim_id']=='K1577','every cutoff' in q['finite_cutoff_identity'],'h_g^prof' in q['coefficient_limit'],'pi/16' in q['coupling_asymptotics'],'constant phase' in q['rigidity'],'genuinely non-Gaussian' in q['advance'],'No bounded-error recentering' in q['scope_guard'],d['finite_cutoff_class_infimum_identified'],d['matching_class_coefficient_proved'],d['minimizer_rigidity_proved'],not d['unrestricted_ground_energy_ratio_convergence'],not d['bounded_error_recentering'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1576')]+[(('coefficient_theorem',k),'changed') for k in ('finite_cutoff_identity','coefficient_limit','coupling_asymptotics','rigidity','advance','scope_guard')]+[(('decision',k),False) for k in ('finite_cutoff_class_infimum_identified','matching_class_coefficient_proved','minimizer_rigidity_proved')]+[(('decision',k),True) for k in ('unrestricted_ground_energy_ratio_convergence','bounded_error_recentering','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
