#!/usr/bin/env python3
"""Integrated controls for K1280."""
import json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1280-released-action-odd-response-admission-boundary.json').read_text()); n=0
def c(label,x):
 global n; assert x,label; n+=1; print(f'PASS {n:02d}: {label}')
rows=D['certificate']['rows']; counts={s:sum(r['state']==s for r in rows) for s in ('satisfied','excluded','conditional','missing')}
c('id',D['result_id']=='K1280-RELEASED-ACTION-ODD-RESPONSE-ADMISSION-BOUNDARY')
c('twenty-one rows',len(rows)==21)
for s in counts: c(s,counts[s]==D['certificate'][s+'_count'])
c('K1145 zero',D['certificate']['k1145_pass_count']==0)
c('K1150 zero',D['certificate']['k1150_pass_count']==0)
c('direct closed',D['decision']['registered_direct_raw_action_route_closed_in_scope'] is True)
c('open routes',D['decision']['boundary_Green_branch_and_new_action_routes_open'] is True)
assert n==10; print('RESULT: PASS 10/10')
