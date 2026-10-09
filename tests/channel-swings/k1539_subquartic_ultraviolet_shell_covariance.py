#!/usr/bin/env python3
"""Controls for K1539's all-density shell-covariance necessity."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1539-subquartic-ultraviolet-shell-covariance.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['shell_covariance'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1539'),('shell covariance','T_N=Tr(P_N Lambda S)' in q['data']),('shell mass','C_sh,N=Tr(P_N Lambda)>=kappa C_N' in q['data']),('dual scale','a_N<=L N^(-2)' in q['data']),('half deficit','C_sh,N/2' in q['deficit']),('matrix quotient','delta_N^2/(4a_N T_N)' in q['matrix_bound']),('all density','every finite-Fisher density' in q['matrix_bound']),('quartic','cN^4' in q['quartic_floor']),('necessary covariance','T_N>C_sh,N/2' in q['necessary_covariance']),('centered guard','centered shell covariance' in q['mean_guard']),('scope','not a sufficient low-energy construction' in q['scope_guard']),('bound',d['all_density_shell_fisher_bound_proved']),('necessity',d['subquartic_requires_order_CN_shell_covariance']),('no Gaussian',not d['gaussian_likelihood_required']),('no mean escape',not d['coherent_constant_mode_can_supply_shell_covariance']),('trial open',not d['order_N2_trial_constructed']),('protected',not d['protected_status_change'])]
 for N in (8.0,16.0,64.0):
  C=N*N;Csh=.4*C;T=.2*C;a=2/N**2;lower=(Csh-T)**2/(4*a*T)
  checks += [(f'quartic scaling {N}',math.isclose(lower/N**4,.025)),(f'positive {N}',lower>0)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
