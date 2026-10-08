#!/usr/bin/env python3
"""Mutation probe for K1444."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1444-form-phase-admission.json').read_text())
def validate(x):
 c,q=x['bridge_census'],x['decision']; e=[]
 if c['row_count']!=c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count']: e.append('sum')
 if (c['row_count'],c['satisfied_count'],c['conditional_count'],c['excluded_count'],c['missing_count'])!=(113,76,9,24,4): e.append('values')
 if len(c['new_satisfied_rows'])!=4 or len(c['new_conditional_rows'])!=1 or len(c['new_excluded_rows'])!=2 or len(c['missing_rows'])!=4: e.append('lists')
 if not q['higher_tier_scalar_cauchy_consequence_constructed']: e.append('consequence')
 for k in ('fixed_free_domain_interacting_form_constructed','all_interacting_resolvent_routes_excluded','strict_zero_harmonic_exact_resonance_present','same_tier_zero_harmonic_normal_form_constructed','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'):
  if q[k]: e.append(k)
 if 'LEDGER_UNCHANGED' not in x['source_and_ledger_effect'] or 'K1145/K1150 0/7' not in x['source_and_ledger_effect']: e.append('effects')
 return e
assert not validate(D)
M=[('count',lambda x:x['bridge_census'].__setitem__('row_count',112)),('satisfied-list',lambda x:x['bridge_census'].__setitem__('new_satisfied_rows',[])),('conditional-list',lambda x:x['bridge_census'].__setitem__('new_conditional_rows',[])),('excluded-list',lambda x:x['bridge_census'].__setitem__('new_excluded_rows',[])),('missing',lambda x:x['bridge_census'].__setitem__('missing_rows',[])),('consequence',lambda x:x['decision'].__setitem__('higher_tier_scalar_cauchy_consequence_constructed',False)),('form',lambda x:x['decision'].__setitem__('fixed_free_domain_interacting_form_constructed',True)),('all',lambda x:x['decision'].__setitem__('all_interacting_resolvent_routes_excluded',True)),('resonance',lambda x:x['decision'].__setitem__('strict_zero_harmonic_exact_resonance_present',True)),('same',lambda x:x['decision'].__setitem__('same_tier_zero_harmonic_normal_form_constructed',True)),('flow',lambda x:x['decision'].__setitem__('completed_full_pde_global_flow_constructed',True)),('source',lambda x:x['decision'].__setitem__('source_selected_reduction_constructed',True)),('counts',lambda x:x['decision'].__setitem__('k1145_k1150_candidate_counts_move',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True)),('effects',lambda x:x.__setitem__('source_and_ledger_effect','changed'))]
for i,(label,mutate) in enumerate(M,1):
 x=copy.deepcopy(D); mutate(x); assert validate(x),label; print(f'PASS {i:02d}: rejects {label}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
