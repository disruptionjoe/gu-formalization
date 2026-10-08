#!/usr/bin/env python3
"""Controls for K1419's exact classical BFV boundary reduction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1419-classical-bfv-boundary-exactness.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['classical_bfv'],D['decision']
for label,key,needle in [('phase','boundary_phase_space','neutral'),('moment','moment_map','G='),('charge','bfv_charge','Omega_BFV'),('KT','constraint_resolution','contract'),('BRST','gauge_resolution','Coulomb'),('residual','residual_completion','U(1)'),('H0','degree_zero_result','H^0'),('positive','positivity','nonzero'),('boundary','boundary','not a quantized')]: check(label,needle in F[key])
for key in ('boundary_moment_map_constructed','bfv_master_equation_constructed','functional_kt_resolution_on_declared_algebra_constructed','based_brst_reduction_constructed','classical_bfv_degree_zero_identified','positive_classical_hamiltonian_descends'): check(key,Q[key])
for key in ('quantum_physical_hilbert_cohomology_constructed','source_gu_bfv_complex_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
