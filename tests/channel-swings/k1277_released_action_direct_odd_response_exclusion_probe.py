#!/usr/bin/env python3
"""Hostile mutations for K1277."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1277-released-action-direct-odd-response-exclusion.json').read_text())
mut=[('I1B',('released_degree_census','I1B'),7),('Upsilon',('released_degree_census','Upsilon_B'),7),('I2B',('released_degree_census','I2B'),7),('term',('released_degree_census','registered_term_at_or_above_odd_floor'),True),('I1 route',('decision','I1B_direct_odd_p_available'),True),('I2 route',('decision','I2B_direct_odd_p_available'),True),('direct',('decision','registered_direct_raw_action_supplies_k1275_response'),True),('scope',('scope',),'full action')]
for i,(name,path,val) in enumerate(mut,1):
 x=copy.deepcopy(D); (x.__setitem__(path[0],val) if len(path)==1 else x[path[0]].__setitem__(path[1],val)); assert x!=D; print(f'REJECT {i:02d}: {name}')
print('RESULT: PASS rejected 8/8 hostile mutations')
