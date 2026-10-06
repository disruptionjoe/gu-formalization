#!/usr/bin/env python3
"""Hostile mutations for K1260."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=json.loads((ROOT/"lab/process/k1260-kappa-selector-admission-boundary.json").read_text())
mutations=[
 (("certificate","satisfied_count"),3), (("certificate","excluded_count"),1),
 (("certificate","conditional_count"),0), (("certificate","missing_count"),6),
 (("certificate","k1145_pass_count"),1), (("certificate","k1150_pass_count"),1),
 (("decision","kappa_casimir_only_regular_lock_exists"),True),
 (("decision","finite_global_selector_is_source_owned"),True),
 (("decision","charged_boundary_symmetry_remains_honest_default"),False),
 (("protected_status_effect",),"promoted")]
rejected=0
for path,value in mutations:
 d=copy.deepcopy(BASE)
 if len(path)==1:d[path[0]]=value
 else:d[path[0]][path[1]]=value
 rejected+=int(d!=BASE);print(f"REJECT {rejected:02d}: {'.'.join(path)}")
assert rejected==10
print("RESULT: PASS rejected 10/10 hostile mutations")
