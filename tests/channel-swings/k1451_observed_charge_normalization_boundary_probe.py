#!/usr/bin/env python3
"""Mutation probe for K1451."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1451-observed-charge-normalization-boundary.json').read_text())
def v(x):
 b,q=x['normalization_boundary'],x['decision']; e=[]
 for key,needle in [('local_rescaling','kappa maps to c^2 kappa'),('local_invariants','Q/sqrt(kappa)'),('global_circle','automorphism exactly for d=plus_or_minus 1'),('required_selector_tuple','faithful observed intertwiner'),('fixed_ktype_exclusion','gcd 2'),('ceiling','Other K-types')]:
  if needle not in b[key]: e.append(key)
 for k in ('local_action_rescaling_equivalence_proved','circle_automorphism_degree_absolute_value_one','primitive_observed_intertwiner_required'):
  if not q[k]: e.append(k)
 for k in ('local_stationarity_separately_normalizes_Q','k1357_fixed_ktype_complete_observed_carrier','all_H_ps_observed_carriers_excluded','source_selected_normalization_constructed','protected_status_change'):
  if q[k]: e.append(k)
 if 'LT-SM1b/LT-SM2 NEEDS' not in x['source_and_ledger_effect']: e.append('ledger')
 return e
assert not v(D)
M=[('scale',lambda x:x['normalization_boundary'].__setitem__('local_rescaling','none')),('invariants',lambda x:x['normalization_boundary'].__setitem__('local_invariants','Q')),('circle',lambda x:x['normalization_boundary'].__setitem__('global_circle','all degrees')),('tuple',lambda x:x['normalization_boundary'].__setitem__('required_selector_tuple','circle only')),('ktype',lambda x:x['normalization_boundary'].__setitem__('fixed_ktype_exclusion','all carriers')),('ceiling',lambda x:x['normalization_boundary'].__setitem__('ceiling','all H_ps excluded')),('rescale',lambda x:x['decision'].__setitem__('local_action_rescaling_equivalence_proved',False)),('normalize',lambda x:x['decision'].__setitem__('local_stationarity_separately_normalizes_Q',True)),('ktype-pass',lambda x:x['decision'].__setitem__('k1357_fixed_ktype_complete_observed_carrier',True)),('all',lambda x:x['decision'].__setitem__('all_H_ps_observed_carriers_excluded',True)),('source',lambda x:x['decision'].__setitem__('source_selected_normalization_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True)),('ledger',lambda x:x.__setitem__('source_and_ledger_effect','changed'))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
