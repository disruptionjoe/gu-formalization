#!/usr/bin/env python3
"""Hostile mutations for K1536."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1536-wick-dominant-nongaussian-variational-scale.json').read_text())
def valid(x):
 q,d=x['variational_boundary'],x['decision']
 return all([x['claim_id']=='K1536','0<=beta<c_*' in q['class_lower'],'Omega_g(N^4)' in q['class_lower'],'Theta_g(N^4)' in q['class_upper'],'positive-kurtosis' in q['material_scope'],'outside fixed M_beta' in q['cat_squeeze_boundary'],'-log mu(B_N)=O(N^2)' in q['endpoint_necessity'],'psi_(N,L)' in q['endpoint_candidate'],'8||Pi_N' in q['carré_du_champ'],'full cutoff projector' in q['carré_du_champ'],'weighted boundary quotient' in q['remaining_gate'],'no continuum interacting charge' in q['brst_transfer'],'no unrestricted N^4 theorem' in q['scope_guard'],d['wick_dominant_nongaussian_scale']=='N^4',not d['cat_squeeze_order_N2_escape'],d['endpoint_capacity_gate_identified'],not d['unrestricted_ground_energy_asymptotic_proved'],not d['order_N2_trial_constructed'],d['restricted_brst_transfer'],not d['protected_status_change']])
def main():
 assert valid(D);mut=[(('claim_id',),'K1535'),(('variational_boundary','class_lower'),'changed'),(('variational_boundary','class_upper'),'changed'),(('variational_boundary','material_scope'),'changed'),(('variational_boundary','cat_squeeze_boundary'),'changed'),(('variational_boundary','endpoint_necessity'),'changed'),(('variational_boundary','endpoint_candidate'),'changed'),(('variational_boundary','carré_du_champ'),'changed'),(('variational_boundary','remaining_gate'),'changed'),(('variational_boundary','brst_transfer'),'changed'),(('variational_boundary','scope_guard'),'changed'),(('decision','wick_dominant_nongaussian_scale'),'N^2'),(('decision','cat_squeeze_order_N2_escape'),True),(('decision','endpoint_capacity_gate_identified'),False),(('decision','unrestricted_ground_energy_asymptotic_proved'),True),(('decision','order_N2_trial_constructed'),True),(('decision','restricted_brst_transfer'),False),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(mut,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(mut)}/{len(mut)}')
if __name__=='__main__':main()
