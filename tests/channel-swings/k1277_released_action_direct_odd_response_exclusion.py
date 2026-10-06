#!/usr/bin/env python3
"""Exact controls for K1277."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1277-released-action-direct-odd-response-exclusion.json').read_text()); n=0
def c(label,x):
 global n; assert x,label; n+=1; print(f'PASS {n:02d}: {label}')
c('id',D['result_id']=='K1277-RELEASED-ACTION-DIRECT-ODD-RESPONSE-EXCLUSION')
for k,v in D['pinned_inputs'].items(): c(f'{k} digest',hashlib.sha256((R/v['path']).read_bytes()).hexdigest()==v['sha256'])
for k in ('I1B','Upsilon_B','I2B'): c(f'{k} below floor',D['released_degree_census'][k]<D['released_degree_census']['odd_floor'])
c('no registered term',D['released_degree_census']['registered_term_at_or_above_odd_floor'] is False)
c('direct route excluded',D['decision']['registered_direct_raw_action_supplies_k1275_response'] is False)
c('boundary open','boundary_or_Green_response' in D['open_routes'])
c('new action open','explicitly_new_action_completion' in D['open_routes'])
assert n==10; print('RESULT: PASS 10/10')
