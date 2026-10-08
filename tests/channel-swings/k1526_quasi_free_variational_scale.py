#!/usr/bin/env python3
"""Controls for K1526's restricted quasi-free variational scale."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1526-quasi-free-variational-scale.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['variational_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1526'),('class definition','stationary translation-invariant diagonal quasi-free' in q['restricted_bottom']),('lower N4','E_N^qf>=c_gN^4' in q['restricted_bottom']),('vacuum upper','6gC_N^2=O(N^4)' in q['vacuum_upper']),('theta','E_N^qf=Theta_g(N^4)' in q['vacuum_upper']),('route decision','cannot be met' in q['route_decision']),('surviving nonGaussian','genuinely non-Gaussian correlations' in q['surviving_routes']),('not constructed','none is constructed here' in q['surviving_routes']),('restricted only','not an operator spectral or resolvent bound' in q['restricted_recentering']),('harmonic transfer','harmonic BRST vector' in q['brst_transfer']),('general BRST fenced','without constraining general BRST states' in q['brst_transfer']),('unrestricted lower','c_gN^2 lower bound' in q['unrestricted_corridor']),('asymptotic open','asymptotic, localization, compactness and Mosco recovery remain open' in q['unrestricted_corridor']),('decision N4',d['stationary_diagonal_quasi_free_scale']=='N^4'),('no N2',not d['coherent_or_stationary_diagonal_quasi_free_N2_trial_exists']),('BRST restricted',d['restricted_brst_transfer']),('asymptotic fenced',not d['unrestricted_ground_energy_asymptotic_proved']),('resolvent fenced',not d['operator_resolvent_consequence_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
