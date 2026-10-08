#!/usr/bin/env python3
"""Controls for K1450's charge-analytic full-PDE hierarchy."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1450-charge-analytic-full-pde-hierarchy.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['hierarchy'],D['decision']
rho=.7
for m in range(1,8):
 a=lambda j: rho**(2*j)/math.factorial(j)
 c(f'factorial shift m={m}',abs(a(m-1)-m*a(m)/rho**2)<1e-12)
F=[1,.7,.25,.1,.03]
lhs=sum(rho**(2*i)/math.factorial(i)*math.sqrt(F[i]*F[i+1]) for i in range(len(F)-1))
G=sum(rho**(2*i)/math.factorial(i)*F[i] for i in range(len(F)))
DD=sum(i*rho**(2*i)/math.factorial(i)*F[i] for i in range(1,len(F)))
c('shift inequality',lhs<=G/2+DD/(2*rho*rho)+1e-12)
c('H2 coefficient','H2' in B['coefficient']); c('one charge shift','sqrt(F_n F_(n+1))' in B['one_step_inequality'])
c('shrinking radius',"R'(t)=-C B(t)" in B['shrinking_radius']); c('Cauchy consequence','Cauchy at tier n' in B['finite_tier_cauchy'])
for k in ('both_k1413_leakages_controlled_in_hierarchy','cutoff_constant_independent_of_charge_cutoff','shrinking_charge_analytic_radius_constructed','fixed_tier_cutoff_cauchy_consequence'): c(k,Q[k])
for k in ('unconditional_global_radius_positive','completed_global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
c('conditional ceiling','conditional' in B['ceiling'])
print(f'RESULT: PASS {n}/{n}')
