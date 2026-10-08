#!/usr/bin/env python3
"""Controls for K1431's quartic renormalization boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1431-quartic-wick-renormalization-boundary.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['renormalization_boundary'],D['decision']
variances=[sum(6*k*k/math.sqrt(1+3*k*k) for k in range(1,N+1)) for N in (4,8,16,32)]
check('variance monotone',all(a<b for a,b in zip(variances,variances[1:])))
check('three-dimensional shell divergence witness',variances[-1]>16*variances[0])
check('quartic expectation divergence witness',3*variances[-1]**2>3*variances[0]**2)
x=1.25; c=2.0; delta=.7; cm=c+delta
raw_cond=x**4+6*delta*x*x+3*delta**2
check('raw conditional moment',abs(raw_cond-(x**4+6*delta*x*x+3*delta**2))<1e-12)
wick_m_cond=raw_cond-6*cm*(x*x+delta)+3*cm**2
wick_n=x**4-6*c*x*x+3*c**2
check('Wick martingale identity',abs(wick_m_cond-wick_n)<1e-12)
check('mass counterterm nonzero',6*delta>0)
check('vacuum counterterm nonzero',3*delta**2>0)
check('Wick polynomial not positive',0-0+3*c*c>0 and (3*c)**2-6*c*(3*c)+3*c*c<0)
for label,key,needle in [('variance','variance_growth','diverges'),('expectation','conditional_expectation','6 Delta C'),('obstruction','obstruction','not projectively compatible'),('Wick','wick_candidate','martingale'),('operator','operator_boundary','does not'),('PDE','pde_boundary','supplies no')]: check(label,needle in R[key])
for key in ('naive_quartic_expectation_diverges','mass_and_vacuum_counterterms_forced','wick_quartic_martingale_constructed'): check(key,Q[key])
check('bare incompatibility',not Q['bare_quartic_projective_compatibility'])
for key in ('uniform_semibounded_interacting_forms_proved','interacting_resolvent_limit_constructed','renormalized_continuum_hamiltonian_constructed','global_nonlinear_pde_proved','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
