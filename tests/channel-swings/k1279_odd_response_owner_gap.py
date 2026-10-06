#!/usr/bin/env python3
"""Exact controls for K1279."""
import json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1279-odd-response-owner-gap.json').read_text()); n=0
def c(label,x):
 global n; assert x,label; n+=1; print(f'PASS {n:02d}: {label}')
c('id',D['result_id']=='K1279-ODD-RESPONSE-OWNER-GAP')
c('odd degree',D['requirements']['odd_generator_degree']==7)
c('weight',D['requirements']['coefficient_weight']==21)
c('six shapes',D['requirements']['six_shape_responses']==6)
c('seven rows',D['requirements']['functional_packet_rows']==7)
c('direct absent',D['available']['registered_direct_raw_action'] is False)
c('boundary absent',D['available']['source_owned_boundary_or_Green_law'] is False)
c('branch absent',D['available']['source_owned_branch_orientation'] is False)
c('owner absent',D['decision']['odd_response_owner_found'] is False)
c('functional zero',D['decision']['k1145_pass_count']==D['decision']['k1150_pass_count']==0)
assert n==10; print('RESULT: PASS 10/10')
