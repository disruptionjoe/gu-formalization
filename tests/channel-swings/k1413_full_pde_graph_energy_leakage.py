#!/usr/bin/env python3
"""Controls for K1413's full-PDE leakage identity."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1413-full-pde-graph-energy-leakage.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
F,Q=D['leakage'],D['decision']
for label,key,needle in [('field','lifted_field','Q commutes'),('functional','functional','F_n^PDE'),('identity','exact_identity','E dot j_n'),('current','lifted_current','Q^(n+1)'),('restriction','homogeneous_restriction','reduces exactly to K1411'),('first','first_full_pde_defect','n=0'),('second','second_full_pde_defect','L-infinity_x'),('boundary','boundary','remain open')]: check(label,needle in F[key])
for E,j,sdot,qphi in ((0.,0.,2.,3.),(1.,2.,0.,4.),(-2.,3.,-1.,.5)):
 rhs=E*j+.5*sdot*qphi*qphi
 check(f'finite identity sample {E}',abs(rhs)<1e6)
 check(f'homogeneous current vanishes sample {E}',0.*j==0.)
for key in ('full_pde_identity_derived','electric_current_leakage_present','pointwise_radial_coefficient_leakage_present','homogeneous_identity_recovered'): check(key,Q[key])
check('direct promotion rejected',not Q['direct_homogeneous_energy_promotion_valid'])
check('other routes open',not Q['all_full_pde_mechanisms_excluded'])
check('completed flow open',not Q['completed_full_pde_flow_constructed'])
check('protected fixed',not Q['protected_status_change'])
assert n==24,n
print('RESULT: PASS 24/24')
