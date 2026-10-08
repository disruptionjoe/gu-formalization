#!/usr/bin/env python3
"""Mutation probe for K1450."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1450-charge-analytic-full-pde-hierarchy.json').read_text())
def v(x):
 b,q=x['hierarchy'],x['decision']; e=[]
 for key,needle in [('coefficient','H2'),('one_step_inequality','sqrt(F_n F_(n+1))'),('analytic_energy','n!'),('shift_identity','a_(n-1)=n a_n/rho^2'),('shrinking_radius',"R'(t)=-C B(t)"),('finite_tier_cauchy','Cauchy at tier n'),('ceiling','conditional')]:
  if needle not in b[key]: e.append(key)
 for k in ('both_k1413_leakages_controlled_in_hierarchy','cutoff_constant_independent_of_charge_cutoff','shrinking_charge_analytic_radius_constructed','fixed_tier_cutoff_cauchy_consequence'):
  if not q[k]: e.append(k)
 for k in ('unconditional_global_radius_positive','completed_global_full_pde_flow_constructed','protected_status_change'):
  if q[k]: e.append(k)
 return e
assert not v(D)
M=[('coef',lambda x:x['hierarchy'].__setitem__('coefficient','energy only')),('shift',lambda x:x['hierarchy'].__setitem__('one_step_inequality','no shift')),('weight',lambda x:x['hierarchy'].__setitem__('analytic_energy','geometric')),('identity',lambda x:x['hierarchy'].__setitem__('shift_identity','unknown')),('radius',lambda x:x['hierarchy'].__setitem__('shrinking_radius','constant')),('cauchy',lambda x:x['hierarchy'].__setitem__('finite_tier_cauchy','none')),('ceiling',lambda x:x['hierarchy'].__setitem__('ceiling','global')),('both',lambda x:x['decision'].__setitem__('both_k1413_leakages_controlled_in_hierarchy',False)),('uniform',lambda x:x['decision'].__setitem__('cutoff_constant_independent_of_charge_cutoff',False)),('global',lambda x:x['decision'].__setitem__('unconditional_global_radius_positive',True)),('flow',lambda x:x['decision'].__setitem__('completed_global_full_pde_flow_constructed',True)),('protected',lambda x:x['decision'].__setitem__('protected_status_change',True))]
for i,(l,m) in enumerate(M,1): x=copy.deepcopy(D); m(x); assert v(x),l; print(f'PASS {i:02d}: rejects {l}')
print(f'RESULT: PASS {len(M)}/{len(M)}')
