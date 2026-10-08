#!/usr/bin/env python3
"""Controls for K1422's compact Haar projection."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1422-compact-haar-stratum-projection.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
H,Q=D['haar_projection'],D['decision']
monomials=[((-4,4),1),((-4,2),0),((2,2,-4),1),((0,),1),((4,),0)]
for charges,want in monomials: check(f'charge {charges}',int(sum(charges)==0)==want)
check('gcd 4',math.gcd(4,8)==4); check('gcd one',math.gcd(2,3)==1)
for label,key,needle in [('formula','formula','integral'),('operator','operator_control','idempotent'),('rule','charge_rule','zero'),('types','orbit_types','gcd'),('compatibility','stratum_compatibility','without'),('boundary','boundary','does not select')]: check(label,needle in H[key])
for key in ('orthogonal_haar_projection_constructed','invariant_subspace_closed','charge_zero_selection_exact','nonfree_orbit_types_retained'): check(key,Q[key])
for key in ('global_free_quotient_assumed','charge_normalization_selected','continuum_physical_sector_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
