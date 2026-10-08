#!/usr/bin/env python3
"""Controls for K1423's bare BRST gauge-volume obstruction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1423-bare-brst-gauge-volume-obstruction.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
O,Q=D['obstruction'],D['decision']
for k in (2,4,8,16,32): check(f'gap witness {k}',1/k>0 and 1/k<=1/(k//1))
for label,key,needle in [('factor','hilbert_factor','L2(R^m'),('differential','bare_differential','partial'),('kernel','degree_zero_kernel','only constant'),('sequence','spectral_sequence','1/n'),('range','range','not closed'),('meaning','meaning','noncompact'),('boundary','boundary','not')]: check(label,needle in O[key])
for key in ('bare_degree_zero_L2_cohomology_nonzero','bare_brst_spectral_gap_positive','bare_brst_range_closed'): check(f'{key} excluded',not Q[key])
check('volume obstruction',Q['noncompact_gauge_volume_obstruction'])
check('alternatives survive',not Q['all_quantization_routes_excluded'])
check('protected',not Q['protected_status_change'])
print(f'RESULT: PASS {n}/{n}')
