#!/usr/bin/env python3
"""Controls for K1531's all-Gaussian variational scale."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1531-all-gaussian-variational-scale.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['variational_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1531'),('all Gaussian','every normalized finite-cutoff Gaussian Q-space wavefunction' in q['gaussian_class']),('arbitrary covariance','arbitrary m and S>0' in q['gaussian_class']),('two branch lower','high integrated variance pays Omega_g(N^4)' in q['lower_boundary'] and 'low integrated variance pays Omega(N^4)' in q['lower_boundary']),('nonnegative mean phase','mean and phase costs are nonnegative' in q['lower_boundary']),('vacuum upper','E_N^Gauss=Theta_g(N^4)' in q['vacuum_upper']),('route decision','nonstationary or off-diagonal' in q['route_decision']),('nongaussian survives','genuinely non-Gaussian' in q['surviving_route']),('restricted recentering','not an operator spectral or resolvent bound' in q['restricted_recentering']),('BRST fenced','no continuum interacting BRST charge' in q['brst_transfer']),('corridor preserved','c_gN^2 lower bound' in q['unrestricted_corridor']),('scale decision',d['all_finite_cutoff_gaussian_scale']=='N^4'),('no stationary assumption',not d['stationary_or_diagonal_assumption_required']),('no N2 Gaussian',not d['gaussian_order_N2_trial_exists']),('restricted BRST',d['restricted_brst_transfer']),('asymptotic fenced',not d['unrestricted_ground_energy_asymptotic_proved']),('resolvent fenced',not d['operator_resolvent_consequence_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
