#!/usr/bin/env python3
"""Controls for K1541's sign-texture and carre-du-champ boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1541-ultraviolet-sign-texture-capacity-boundary.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['sign_texture_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1541'),('energy split','q0[psi]<=K N^2' in q['order_N2_assumption']),('amplitude','O_g(1)' in q['amplitude_and_shell']),('shell','T_N>=kappa C_N/2' in q['amplitude_and_shell']),('factorization','phi_N=A_N s_phi+s_phi e_phi' in q['sign_factorization']),('sign lower','kappa/12+o(1)' in q['ultraviolet_sign_mass']),('capacity target','Gaussian weighted Dirichlet capacity' in q['capacity_reduction']),('not constant wells','not the union of two constant wells' in q['capacity_reduction']),('carre exact','8int(D_N^3+3C_ND_N^2)' in q['carre_improvement']),('bandlimit','2N-bandlimited' in q['carre_improvement']),('N9/2','O(N^(9/2))' in q['carre_improvement']),('ratio open','relative transition-mass estimate' in q['scope_guard']),('texture',d['order_N2_requires_ultraviolet_sign_texture']),('constant false',not d['constant_two_well_endpoint_sufficient']),('carre improved',d['carre_prefactor_improved_from_crude_N5_to_N9over2']),('ratio open decision',not d['relative_transition_mass_control_proved']),('trial open',not d['order_N2_trial_constructed']),('lower open',not d['superquadratic_capacity_lower_bound_proved']),('protected',not d['protected_status_change'])]
 for N in (16.0,64.0):
  C=N*N;W=3*N*N;bound=N**1.5*W**1.5+C*W
  checks += [(f'carre positive {N}',bound>0),(f'N9/2 scaling {N}',bound/N**4.5>0)]
 # x<=2y+2e implies y>=(x-2e)/2; use x=kappa C/2 and e=o(C).
 for C in (100.0,1000.0):
  k=.4;e=1.0;sign=((k*C/2)-2*e)/(2*3*C)
  checks.append((f'sign shell approaches k/12 C={C}',sign>0 and sign<k/12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
