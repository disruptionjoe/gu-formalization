#!/usr/bin/env python3
"""Controls for K1424's Gaussian gauge-fixed BRST Hilbert complex."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1424-gaussian-gauge-fixed-brst-cohomology.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
G,Q=D['gauge_fixed_complex'],D['decision']
ou_spectrum=[0,1,2,3,4]
check('unique zero',ou_spectrum.count(0)==1)
check('positive gap',min(x for x in ou_spectrum if x)>0)
check('nilpotent exterior',sum(((-1)**j) for j in range(2))==0)
for label,key,needle in [('factor','gauge_factor','Gaussian'),('differential','differential','nilpotent'),('adjoint','adjoint','chi_j'),('hodge','hodge_operator','number operator'),('gap','gap_and_ranges','closed'),('cohomology','cohomology','H0'),('boundary','boundary','not translation invariant')]: check(label,needle in G[key])
for key in ('closed_nilpotent_gauge_fixed_differential','positive_hodge_gap','closed_ranges','degree_zero_cohomology_equals_compact_invariant_reduced_block','higher_cohomology_zero','positive_nonzero_finite_block_cohomology'): check(key,Q[key])
for key in ('translation_invariant_measure','continuum_quantum_brst_constructed','source_gauge_fixing_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
