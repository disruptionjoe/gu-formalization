#!/usr/bin/env python3
"""Controls for K1439's fixed free-form-domain obstruction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1439-free-hamiltonian-form-domain-obstruction.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['form_domain_obstruction'],D['decision']
def cone_lower(N,m=1.0):
 count=(N//8+1)**9
 omega=math.sqrt(m*m+3*N*N)
 return 24*count*(1/(2*omega))**4/(1+4*omega)
vals=[cone_lower(N)/N**4 for N in (64,128,256)]
check('positive N4 cone constant',min(vals)>0)
check('N4 scaled lower stabilizes',max(vals)/min(vals)<3)
check('dual identity has free resolvent','(H_0+1)^(-1/2)' in R['dual_norm_identity'])
check('cone lower states N4','N^4' in R['cone_lower_bound'])
check('necessary form test stated','uniformly continuous' in R['necessary_form_test'])
check('orthogonal counterterm sectors','zeroth and second' in R['lower_chaos_counterterms'])
check('fixed-domain conclusion','not uniformly KLMN-form-bounded' in R['conclusion'])
check('operator ceiling preserved','does not exclude' in R['operator_ceiling'])
check('identity decision',Q['free_form_dual_norm_identity_proved'])
check('N4 decision',Q['three_dimensional_free_form_dual_lower_bound_order']=='N^4')
for key in ('uniform_fixed_coupling_free_form_bound','quadratic_and_vacuum_counterterms_cancel_four_particle_sector','all_interacting_resolvent_limits_excluded','source_hamiltonian_identified','protected_status_change'):
 check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
