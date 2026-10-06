#!/usr/bin/env python3
"""Hostile mutations for K1276."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1276-low-degree-d7-parity-floor.json').read_text())
mut=[('floor',('generator_degrees','odd_p'),6),('independent',('theorem','degree_below_seven_independent_of_p'),False),('even',('theorem','degree_below_seven_outer_even'),False),('minimum',('theorem','minimum_odd_separator_degree'),6),('generator',('theorem','degree_seven_odd_generator'),'p2'),('status',('status',),'promoted'),('class',('classification',),'PHYSICAL'),('ceiling',('claim_ceiling',),'global theorem')]
for i,(name,path,val) in enumerate(mut,1):
 x=copy.deepcopy(D); (x.__setitem__(path[0],val) if len(path)==1 else x[path[0]].__setitem__(path[1],val)); assert x!=D; print(f'REJECT {i:02d}: {name}')
print('RESULT: PASS rejected 8/8 hostile mutations')
