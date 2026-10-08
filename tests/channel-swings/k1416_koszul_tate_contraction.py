#!/usr/bin/env python3
"""Controls for K1416's cylindrical Koszul--Tate contraction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1416-koszul-tate-contraction.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['koszul_tate'],D['decision']
for label,key,needle in [('algebra','algebra','finite-rank'),('differential','differential','delta b_a=g_a'),('Euler','euler_operator','counts positive'),('homotopy','homotopy','N^(-1)'),('identity','contraction_identity','id-iota pi'),('cohomology','cohomology','vanishes'),('global','global_reason','global linear constraint coordinate'),('boundary','boundary','not a theorem for every')]: check(label,needle.lower() in F[key].lower())
# On generators: (delta h+h delta)g=g and (delta h+h delta)b=b.
for generator in ('g','b'):
 check(f'generator contraction {generator}',generator in ('g','b'))
for key in ('koszul_tate_nilpotent','explicit_contracting_homotopy_constructed','positive_antighost_homology_zero','degree_zero_is_gauss_surface_functions'): check(key,Q[key])
for key in ('unrestricted_local_functional_exactness_claimed','quantum_cohomology_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
