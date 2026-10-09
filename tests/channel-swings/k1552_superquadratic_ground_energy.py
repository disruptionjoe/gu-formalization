#!/usr/bin/env python3
"""Controls for K1552's superquadratic ground-energy boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1552-superquadratic-ground-energy.json').read_text())
def main():
 q,d=D['ground_energy'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1552'),('bootstrap','epsilon N^(8/3)' in q['bootstrap_assumption']),('subquartic','q0=o(N^4)' in q['shell_covariance']),('amplitude exponent','N^(2/3)' in q['amplitude_error']),('relative error','o(C_N)' in q['amplitude_error']),('sign release','eta_g>0' in q['sign_shell_release']),('contradiction','c_g N^(8/3)' in q['interaction_contradiction']),('floor','E_N>=c_g N^(8/3)' in q['variational_floor']),('resolvent','N^(-8/3)' in q['resolvent_consequence']),('scope upper','Theta_g(N^4)' in q['scope_guard']),('scope Mosco','Mosco recovery' in q['scope_guard']),('N2 excluded',d['order_N2_trial_excluded']),('floor decision',d['ground_energy_floor_N8over3_proved']),('shift decision',d['sub_N8over3_recenterings_excluded']),('asymptotic open',not d['matching_ground_energy_asymptotic_proved']),('operator open',not d['continuum_operator_constructed']),('source open',not d['source_owned_gu_hamiltonian']),('protected',not d['protected_status_change'])]
 for N in (16,64,256):
  checks += [(f'8/3 superquadratic N={N}',N**(8/3)>N**2),(f'8/3 subquartic N={N}',N**(8/3)<N**4),(f'amplitude relative N={N}',N**(2/3)/N**2<1)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
