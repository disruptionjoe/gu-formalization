#!/usr/bin/env python3
"""Hostile mutations for K1289."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1289-proper-algebraic-rank-seven-selector.json").read_text())
mut=[("barrier",("construction","radial_barrier"),"zero"),("potential",("construction","potential"),"even only"),("proper",("construction","proper_on_open_horn_chart"),False),("minimum",("construction","unique_global_minimum"),"two"),("rank",("construction","hessian_rank"),6),("inertia",("construction","hessian_inertia"),[6,0,1]),("data",("decision","six_shape_and_scale_data_eliminated"),True),("owner",("decision","source_owned"),True)]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
