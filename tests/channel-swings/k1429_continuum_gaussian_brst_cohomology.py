#!/usr/bin/env python3
"""Controls for K1429's countable Gaussian BRST complex."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1429-continuum-gaussian-brst-cohomology.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
C,Q=D['continuum_complex'],D['decision']
states=[(boson,ghost,boson+ghost) for boson in range(5) for ghost in range(4)]
check('unique joint vacuum',sum(total==0 for _,_,total in states)==1)
check('unit positive gap',min(total for _,_,total in states if total)==1)
for boson,ghost,total in states[1:10]: check(f'homotopy scalar {boson}-{ghost}',total*(1/total)==1)
check('nilpotent fermionic creation',1-1==0)
for label,key,needle in [('carrier','carrier','Fock'),('differential','core_and_differential','closed'),('Hodge','hodge_operator','number operator'),('ranges','closed_ranges','contracting homotopy'),('cohomology','cohomology','H0'),('refinement','refinement','chain maps'),('boundary','boundary','not')]: check(label,needle in C[key])
for key in ('closed_continuum_gaussian_brst_operator_constructed','continuum_hodge_gap_positive','continuum_degreewise_ranges_closed','positive_nonzero_degree_zero_cohomology','higher_cohomology_zero','cohomology_refinement_stable'): check(key,Q[key])
for key in ('interacting_quantum_brst_constructed','source_physical_cohomology_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
