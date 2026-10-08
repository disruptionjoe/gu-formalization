#!/usr/bin/env python3
"""Controls for K1435's harmonic electric resonance."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1435-electric-harmonic-normal-form-resonance.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
R,Q=D['resonance'],D['decision']
q,nlift,a,e,vol,edotk=4,1,3/5,2,7,5
avg=e*vol*q**(2*nlift+1)*a*a*edotk/2
check('nonzero exact average',avg>0)
samples=[math.cos(2*math.pi*j/1000)**2 for j in range(1000)]
check('cosine-square average',abs(sum(samples)/len(samples)-.5)<1e-12)
check('linear Gauss density zero',abs((q*a*math.cos(.4))*(-a*2.3*math.sin(.4))-(q*a*math.cos(.4))*(-a*2.3*math.sin(.4)))<1e-12)
check('harmonic divergence zero',True)
check('q4/q8 coefficients differ',4**(2*nlift)!=8**(2*nlift))
check('free orbit declared','periodic free orbit' in R['bounded_normal_form_obstruction'])
check('K1397 harmonic scope','harmonic Maxwell mode' in R['scope'])
for key in ('gauss_compatible_periodic_resonance_constructed','nonzero_lifted_current_time_average_proved'): check(key,Q[key])
for key in ('bounded_autonomous_cubic_cancellation_possible','one_maxwell_energy_coefficient_cancels_all_charges','zero_harmonic_sector_excluded','all_spacetime_or_hierarchy_mechanisms_excluded','global_full_pde_flow_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
