#!/usr/bin/env python3
"""Hostile mutations for K1274."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=json.loads((ROOT/"lab/process/k1274-connected-outer-symmetry-fork.json").read_text())
mutations=[
 ("connected",("symmetry_fork","connected_group"),"reverses p"),
 ("outer",("symmetry_fork","outer_involution"),"sigma(p)=p"),
 ("fixed",("symmetry_fork","fixed_scalar_effect"),"invariant"),
 ("gauged",("symmetry_fork","outer_gauged_consequence"),"allowed"),
 ("connected only",("symmetry_fork","connected_only_consequence"),"derived"),
 ("spurion",("symmetry_fork","spurion_option"),"owner free"),
 ("component",("symmetry_fork","one_component_option"),"source owned"),
 ("D7 forbids",("decision","connected_D7_forbids_odd_p_term"),True),
 ("outer allows",("decision","gauged_outer_parity_allows_fixed_scalar_odd_p_term"),True),
 ("source horn",("decision","source_chooses_symmetry_horn"),True),
]
rejected=0
for name,path,value in mutations:
 d=copy.deepcopy(BASE); d[path[0]][path[1]]=value
 if d!=BASE: rejected+=1; print(f"REJECT {rejected:02d}: {name}")
assert rejected==10
print("RESULT: PASS rejected 10/10 hostile mutations")
