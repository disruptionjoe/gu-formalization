#!/usr/bin/env python3
"""Controls for K1516's polynomial Wick variational and recentering boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1516-polynomial-wick-recentering-boundary.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 b,q=D['variational_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1516'),('radius','N^(1/14)/(1+log N)' in b['selected_radius']),('energy','-(1-o(1))g sigma_N R_N' in b['energy_upper_bound']),('all beta','beta<1/14' in b['power_family']),('all coefficients','A>0' in b['power_family']),('necessary liminf','liminf' in b['necessary_recentering'] and '>=1' in b['necessary_recentering']),('excluded limsup','limsup' in b['excluded_window'] and '<1' in b['excluded_window']),('bottoms','minus infinity' in b['excluded_window']),('unit ball','fixed Gaussian unit ball' in b['mosco_failure']),('weak subsequence','weakly convergent subsequences' in b['mosco_failure']),('zero allowed','may be zero' in b['mosco_failure']),('Mosco','Mosco weak liminf failure' in b['mosco_failure']),('BRST','harmonic BRST vacuum' in b['brst_transfer']),('descent proved',q['polynomial_variational_descent_proved']),('sqrt log superseded',q['sqrt_log_boundary_superseded']),('recenter proved',q['polynomial_recentering_necessity_proved']),('Mosco excluded',q['fixed_gaussian_mosco_window_excluded']),('BRST excluded',q['harmonic_brst_window_excluded']),('endpoint fenced',not q['one_fourteenth_endpoint_or_optimal_scale_proved']),('lower fenced',not q['matching_many_chaos_lower_bound_proved']),('limit fenced',not q['ground_energy_recentered_limit_constructed']),('recovery fenced',not q['mosco_recovery_proved']),('changed rep open',not q['changed_representation_excluded']),('protected fenced',not q['protected_status_change'])]
 for beta in (0.01,0.04,0.07):
  ratios=[]
  for t in (1000,2000,4000): ratios.append(math.exp((1/14-beta)*t)/(1+t))
  checks.append((f'beta {beta} radius dominates',ratios[2]>ratios[1]>ratios[0]))
 checks += [('sqrt log dominated',math.exp(400/14)/(401*math.sqrt(400))>1e6)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
