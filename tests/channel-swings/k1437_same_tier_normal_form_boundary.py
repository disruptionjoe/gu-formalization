#!/usr/bin/env python3
"""Controls for K1437's joint normal-form boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1437-same-tier-normal-form-boundary.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,Q=D['combined_boundary'],D['decision']
check('admitted class bounded','bounded autonomous' in B['admitted_class'])
check('same-tier scope','same-spatial-tier' in B['admitted_class'])
check('electric resonance imported','periodic-orbit average' in B['electric_result'])
check('charge mismatch imported','q=4/q=8' in B['electric_result'])
check('radial curl imported','nonclosed' in B['radial_result'])
check('two derivative growth imported','K^2' in B['radial_result'])
check('joint conclusion exact','both K1413 leakage terms' in B['joint_conclusion'])
check('four surviving routes',len(B['surviving_routes'])==4)
check('zero-harmonic survives',any('zero-harmonic' in x for x in B['surviving_routes']))
check('spacetime survives',any('spacetime' in x for x in B['surviving_routes']))
check('hierarchy survives',any('hierarchy' in x for x in B['surviving_routes']))
check('claim ceiling','not a no-go' in B['claim_ceiling'])
check('replay',Q['electric_and_radial_leakage_jointly_replayed'])
check('same-tier excluded',not Q['bounded_same_tier_time_local_polynomial_normal_form_closes_both'])
for key in ('zero_harmonic_nonzero_mode_route_open','spacetime_and_hierarchy_routes_open'): check(key,Q[key])
for key in ('finite_tier_cauchy_consequence_constructed','completed_full_pde_flow_constructed','protected_status_change'): check(f'{key} fenced',not Q[key])
print(f'RESULT: PASS {n}/{n}')
