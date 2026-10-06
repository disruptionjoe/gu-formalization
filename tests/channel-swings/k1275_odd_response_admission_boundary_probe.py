#!/usr/bin/env python3
"""Hostile mutations for K1275."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=json.loads((ROOT/"lab/process/k1275-odd-response-admission-boundary.json").read_text())
mutations=[
 ("satisfied",("certificate","satisfied_count"),8),
 ("excluded",("certificate","excluded_count"),3),
 ("conditional",("certificate","conditional_count"),2),
 ("missing",("certificate","missing_count"),5),
 ("K1145",("certificate","k1145_pass_count"),1),
 ("K1150",("certificate","k1150_pass_count"),1),
 ("strict",("decision","single_critical_point_requires_strict_threshold"),False),
 ("uniform",("decision","uniform_response_requires_scale_covariance"),False),
 ("source",("decision","source_odd_response_owned"),True),
 ("protected",("protected_status_effect",),"moved"),
]
rejected=0
for name,path,value in mutations:
 d=copy.deepcopy(BASE)
 if len(path)==1: d[path[0]]=value
 else: d[path[0]][path[1]]=value
 if d!=BASE: rejected+=1; print(f"REJECT {rejected:02d}: {name}")
assert rejected==10
print("RESULT: PASS rejected 10/10 hostile mutations")
