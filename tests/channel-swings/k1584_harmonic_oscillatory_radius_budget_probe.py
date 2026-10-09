#!/usr/bin/env python3
"""Hostile mutations for K1584."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1584-harmonic-oscillatory-radius-budget.json').read_text())
def valid(x):
 q=x['harmonic_split'];z=x['decision'];return all([x['claim_id']=='K1584','A=a+A_perp' in q['decomposition'],'Hodge/Poincare' in q['hodge_control'],'dot a' in q['remainder_budget'],'replaces |e|||a||' in q['remainder_budget'],'L1_t' in q['conditional_radius'],'Static flat holonomy consumes no radius' in q['structural_advance'],'No coupled estimate' in q['scope_guard'],z['harmonic_oscillatory_split_constructed'],z['raw_flat_amplitude_removed'],z['hodge_remainder_typed'],z['conditional_positive_radius'],not z['remainder_integrability_proved'],not z['nonlinear_global_flow'],not z['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1583')]+[(('harmonic_split',k),'changed') for k in ('decomposition','hodge_control','remainder_budget','conditional_radius','structural_advance','scope_guard')]+[(('decision',k),False) for k in ('harmonic_oscillatory_split_constructed','raw_flat_amplitude_removed','hodge_remainder_typed','conditional_positive_radius')]+[(('decision',k),True) for k in ('remainder_integrability_proved','nonlinear_global_flow','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
