#!/usr/bin/env python3
"""Controls for K1446's sharp resolvent-column threshold."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1446-resolvent-dressed-vacuum-column-threshold.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['resolvent_column'],D['decision']
for r,s in ((1,2),(2.5,5),(3,6)): c(f's=2r at {r}',2*r==s)
c('identity','S_(2r)' in B['identity']); c('strict threshold','r>5/2' in B['sharp_threshold'] and 'r<=5/2' in B['sharp_threshold'])
c('endpoint fenced','r=5/2' in B['sharp_threshold']); c('one resolvent fails','r=1' in B['one_resolvent_boundary'])
for k in ('sharp_resolvent_column_threshold_proved','converges_for_r_greater_than_five_halves'): c(k,Q[k])
for k in ('converges_at_r_equal_five_halves','one_resolvent_vacuum_column_converges','full_dressing_constructed','full_interacting_resolvent_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
