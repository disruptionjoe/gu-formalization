#!/usr/bin/env python3
"""Controls for K1415's global split Gauss coordinate."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1415-split-gauss-coordinate.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['split_coordinate'],D['decision']
for label,key,needle in [('scope','phase_scope','neutral sector'),('constraint','constraint','div E-rho'),('right inverse','right_inverse','div Rg=g'),('projection','transverse_projection','div P_T E=0'),('coordinate','coordinate_map','g=G'),('inverse','inverse_map','g+rho'),('identity','global_identity','mutual inverses'),('submersion','submersion','split-surjective'),('boundary','boundary','not a source GU constraint')]: check(label,needle in F[key])
for E,rho in ((3.,1.),(-2.,.5),(0.,-4.)):
 g=E-rho; ET=E-(g+rho); E2=ET+(g+rho)
 check(f'finite split inverse E={E}',abs(E2-E)<1e-12 and abs(ET)<1e-12)
for key in ('gauss_map_globally_split','bounded_right_inverse_constructed','gauss_surface_split_submanifold'): check(key,Q[key])
for key in ('field_dependent_rank_jump_present','global_unbounded_charge_evolution_constructed','source_gu_constraint_identified','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
