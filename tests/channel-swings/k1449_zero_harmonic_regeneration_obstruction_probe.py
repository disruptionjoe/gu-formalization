#!/usr/bin/env python3
"""Mutation probe for K1449."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1449-zero-harmonic-regeneration-obstruction.json').read_text())
def v(x):
 b,q=x['regeneration'],x['decision']; e=[]
 for key,needle in [('averaged_maxwell_equation','partial_t E_h=-bar(j)'),('explicit_data','charge density is zero'),('consequence','partial_t E_h(0) is nonzero'),('relation_to_k1442','remains correct'),('surviving_scope','nongeneric')]:
  if needle not in b[key]: e.append(key)
 if not q['gauss_compatible_regeneration_witness_constructed']: e.append('witness')
 for k in ('gauss_constrains_harmonic_electric_mode','generic_strict_zero_harmonic_sector_invariant','k1442_fixed_nonzero_mode_result_invalidated','all_symmetry_restricted_zero_mode_sectors_excluded','global_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not v(D)
M=[('average',lambda x:x['regeneration'].__setitem__('averaged_maxwell_equation','zero')),('gauss',lambda x:x['regeneration'].__setitem__('explicit_data','not constrained')),('exit',lambda x:x['regeneration'].__setitem__('consequence','invariant')),('k1442',lambda x:x['regeneration'].__setitem__('relation_to_k1442','invalid')),('scope',lambda x:x['regeneration'].__setitem__('surviving_scope','none')),('witness',lambda x:x['decision'].__setitem__('gauss_compatible_regeneration_witness_constructed',False)),('invariant',lambda x:x['decision'].__setitem__('generic_strict_zero_harmonic_sector_invariant',True)),('invalidate',lambda x:x['decision'].__setitem__('k1442_fixed_nonzero_mode_result_invalidated',True)),('all',lambda x:x['decision'].__setitem__('all_symmetry_restricted_zero_mode_sectors_excluded',True)),('flow',lambda x:x['decision'].__setitem__('global_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
