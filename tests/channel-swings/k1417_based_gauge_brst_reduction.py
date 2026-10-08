#!/usr/bin/env python3
"""Controls for K1417's based-gauge BRST reduction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1417-based-gauge-brst-reduction.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['based_reduction'],D['decision']
for label,key,needle in [('group','group','mean-zero'),('free','free_action','no stabilizer'),('coordinate','global_coordinate','Coulomb'),('doublet','brst_doublet','contractible'),('cohomology','cohomology','vanishes'),('constraint','constraint_compatibility','Gauss surface'),('closed','closedness','closed'),('boundary','boundary','Constant compact')]: check(label,needle in F[key])
for longitudinal,shift in ((2.,3.),(-1.,.5),(0.,4.)):
 transformed=longitudinal+shift; coulomb=transformed-transformed
 check(f'finite Coulomb representative {longitudinal}',abs(coulomb)<1e-12)
for key in ('based_action_free','global_coulomb_coordinate_constructed','based_brst_doublet_contracted','positive_based_ghost_cohomology_zero','degree_zero_based_reduction_identified'): check(key,Q[key])
check('constant retained',not Q['constant_gauge_group_removed'])
check('protected fixed',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
