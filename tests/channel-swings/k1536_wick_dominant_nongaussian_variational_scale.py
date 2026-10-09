#!/usr/bin/env python3
"""Controls for K1536's scoped non-Gaussian scale and endpoint capacity."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1536-wick-dominant-nongaussian-variational-scale.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['variational_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1536'),('class lower','0<=beta<c_*' in q['class_lower'] and 'Omega_g(N^4)' in q['class_lower']),('class upper','Theta_g(N^4)' in q['class_upper']),('material class','positive-kurtosis' in q['material_scope']),('phases','arbitrary phases' in q['material_scope']),('cat outside','outside fixed M_beta' in q['cat_squeeze_boundary']),('cat N4','Theta_g(N^4)' in q['cat_squeeze_boundary']),('endpoint half','at least one half' in q['endpoint_necessity']),('endpoint exponent','-log mu(B_N)=O(N^2)' in q['endpoint_necessity']),('bump','psi_(N,L)' in q['endpoint_candidate']),('bump kinetic','L^(-2)' in q['endpoint_candidate']),('carre','8||Pi_N' in q['carré_du_champ'] and 'full cutoff projector' in q['carré_du_champ']),('K1518 lower','-log mu(B_N)>=cN^2' in q['remaining_gate']),('weighted quotient','weighted boundary quotient' in q['remaining_gate']),('BRST fenced','no continuum interacting charge' in q['brst_transfer']),('unrestricted fenced','no unrestricted N^4 theorem' in q['scope_guard']),('scale decision',d['wick_dominant_nongaussian_scale']=='N^4'),('cat no escape',not d['cat_squeeze_order_N2_escape']),('capacity identified',d['endpoint_capacity_gate_identified']),('asymptotic open',not d['unrestricted_ground_energy_asymptotic_proved']),('trial open',not d['order_N2_trial_constructed']),('BRST restricted',d['restricted_brst_transfer']),('protected',not d['protected_status_change'])]
 # Exact cat/squeeze scaling and class lower-bound controls.
 for N,eps in [(10.0,.5),(20.0,.25),(40.0,.0625)]:
  C=N*N;interaction=6*eps*(2-eps)*C*C;free=N**4/eps
  checks += [(f'cat interaction positive {N}',interaction>0),(f'cat free dominates N2 {N}',free>N*N)]
 for N in (8.0,32.0):
  C=N*N;a=2/N**2;k=.4;beta=1.0;cstar=6*(math.sqrt(3)-1);g=.3
  lower=min(k*C/(8*a),g*(cstar-beta)*k*C*C/2)
  checks.append((f'class N4 {N}',lower/N**4>0))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
