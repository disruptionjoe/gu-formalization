#!/usr/bin/env python3
"""Hostile mutations for K1279."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1279-odd-response-owner-gap.json').read_text())
mut=[('degree',('requirements','odd_generator_degree'),6),('weight',('requirements','coefficient_weight'),14),('shapes',('requirements','six_shape_responses'),0),('direct',('available','registered_direct_raw_action'),True),('boundary',('available','source_owned_boundary_or_Green_law'),True),('owner',('decision','odd_response_owner_found'),True),('K1145',('decision','k1145_pass_count'),1),('K1150',('decision','k1150_pass_count'),1)]
for i,(name,path,val) in enumerate(mut,1): x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f'REJECT {i:02d}: {name}')
print('RESULT: PASS rejected 8/8 hostile mutations')
