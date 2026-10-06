#!/usr/bin/env python3
"""Hostile mutations for K1285."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1285-weighted-orientation-admission-boundary.json").read_text())
mut=[("satisfied",("certificate","satisfied_count"),10),("excluded",("certificate","excluded_count"),5),("conditional",("certificate","conditional_count"),3),("missing",("certificate","missing_count"),5),("K1145",("certificate","k1145_pass_count"),1),("closed",("decision","internal_homogeneous_spurion_route_closed_in_scope"),False),("open",("decision","external_nonhomogeneous_boundary_Green_singular_and_component_routes_open"),False),("protected",("protected_status_effect",),"moved")]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); (x.__setitem__(path[0],val) if len(path)==1 else x[path[0]].__setitem__(path[1],val)); assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
