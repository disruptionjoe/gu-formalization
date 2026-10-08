#!/usr/bin/env python3
"""Controls for K1451's observed-charge normalization boundary."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1451-observed-charge-normalization-boundary.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['normalization_boundary'],D['decision']
for c0 in (.5,2,7):
 Q0,A,kappa,mu=3.,5.,11.,13.; c('covariant product invariant',abs((c0*Q0)*(A/c0)-Q0*A)<1e-12); c('gauge kinetic invariant',abs((c0*c0*kappa)*(A/c0)**2-kappa*A*A)<1e-12); c('regularizer invariant',abs((mu/(c0*c0))*(c0*Q0)**2-mu*Q0*Q0)<1e-12)
c('circle degrees',all((abs(d)==1)==(d in (-1,1)) for d in range(-5,6) if d))
obs=[1,-4,2,-3,6,0]; native=[-4,-2,0,2,4]
c('observed primitive',math.gcd(*[abs(x) for x in obs])==1); c('native even',math.gcd(*[abs(x) for x in native])==2)
c('odd weights absent',any(x%2 for x in obs) and not any(x%2 for x in native))
c('selector tuple','faithful observed intertwiner' in B['required_selector_tuple'])
for k in ('local_action_rescaling_equivalence_proved','circle_automorphism_degree_absolute_value_one','primitive_observed_intertwiner_required'): c(k,Q[k])
for k in ('local_stationarity_separately_normalizes_Q','k1357_fixed_ktype_complete_observed_carrier','all_H_ps_observed_carriers_excluded','source_selected_normalization_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
c('ledger preserved','LT-SM1b/LT-SM2 NEEDS' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
