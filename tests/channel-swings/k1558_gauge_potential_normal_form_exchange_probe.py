#!/usr/bin/env python3
"""Hostile mutations for K1558."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1558-gauge-potential-normal-form-exchange.json').read_text())
def valid(x):
 q,d=x['normal_form_exchange'],x['decision'];return all([x['claim_id']=='K1558','E=-partial_t A' in q['gauge_convention'],'M_n(t)=int_T3 A(t,x) dot j_n(t,x) dx' in q['cross_term'],"M_n'=-int E dot j_n" in q['product_rule'],'G_n=F_n^PDE+M_n' in q['corrected_identity'],'partial_t||phi||^2' in q['corrected_identity'],q['current_derivative'].count('e Im<')==3,'A=0 at the testing time' in q['k1478_escape'],'exchanged, not eliminated' in q['new_boundary'],'not a gauge-invariant energy' in q['scope_guard'],d['gauge_dependent_correction_constructed'],d['electric_current_term_exactly_exchanged'],d['k1478_ultralocal_no_go_escaped'],not d['differentiated_current_remainder_controlled'],not d['radial_leakage_controlled'],not d['same_tier_coercive_modified_energy_constructed'],not d['global_full_pde_flow_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1557'),(('normal_form_exchange','gauge_convention'),'changed'),(('normal_form_exchange','cross_term'),'changed'),(('normal_form_exchange','product_rule'),'changed'),(('normal_form_exchange','corrected_identity'),'changed'),(('normal_form_exchange','current_derivative'),'changed'),(('normal_form_exchange','k1478_escape'),'changed'),(('normal_form_exchange','new_boundary'),'changed'),(('normal_form_exchange','scope_guard'),'changed'),(('decision','gauge_dependent_correction_constructed'),False),(('decision','electric_current_term_exactly_exchanged'),False),(('decision','k1478_ultralocal_no_go_escaped'),False),(('decision','differentiated_current_remainder_controlled'),True),(('decision','radial_leakage_controlled'),True),(('decision','same_tier_coercive_modified_energy_constructed'),True),(('decision','global_full_pde_flow_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
