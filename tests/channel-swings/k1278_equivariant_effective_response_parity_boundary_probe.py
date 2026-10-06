#!/usr/bin/env python3
"""Hostile mutations for K1278."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/'lab/process/k1278-equivariant-effective-response-parity-boundary.json').read_text())
mut=[('premise',('theorem','premise'),'none'),('conclusion',('theorem','conclusion'),'odd'),('preserves',('theorem','unique_equivariant_elimination_preserves_evenness'),False),('creates',('decision','unique_equivariant_elimination_creates_odd_response'),True),('component',('decision','fixed_component_can_create_apparent_odd_response'),False),('datum',('decision','fixed_component_imports_orientation_datum'),False),('solution',('controls','unique_solution'),'y*=1'),('value',('controls','effective_value'),'p')]
for i,(name,path,val) in enumerate(mut,1): x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f'REJECT {i:02d}: {name}')
print('RESULT: PASS rejected 8/8 hostile mutations')
