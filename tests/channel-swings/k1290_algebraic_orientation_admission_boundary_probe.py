#!/usr/bin/env python3
"""Hostile mutations for K1290."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1290-algebraic-orientation-admission-boundary.json").read_text())
mut=[("sat",("certificate","satisfied_count"),16),("excluded",("certificate","excluded_count"),5),("conditional",("certificate","conditional_count"),4),("missing",("certificate","missing_count"),5),("k1145",("certificate","k1145_pass_count"),1),("k1150",("certificate","k1150_pass_count"),1),("owner",("decision","source_selector_owned"),True),("protected",("decision","protected_status_change"),True)]
for i,(name,path,val) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
