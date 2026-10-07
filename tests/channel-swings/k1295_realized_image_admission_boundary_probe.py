#!/usr/bin/env python3
"""Independent hostile mutations for K1295."""
import copy,json
from collections import Counter
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1295-realized-image-admission-boundary.json").read_text())
def valid(x):
    c=x["certificate"]; q=x["decision"]; counts=Counter(r["state"] for r in c["rows"])
    return (counts["satisfied"]==c["satisfied_count"]==19 and counts["excluded"]==c["excluded_count"]==6 and
            counts["conditional"]==c["conditional_count"]==4 and counts["missing"]==c["missing_count"]==6 and
            c["k1145_pass_count"]==0 and c["k1150_pass_count"]==0 and not q["formal_ambient_chart_equals_realized_image"] and
            not q["p_sign_is_a_connected_component_label"] and not q["source_selector_owned"] and not q["protected_status_change"])
mut=[(("certificate","satisfied_count"),18),(("certificate","excluded_count"),5),(("certificate","conditional_count"),5),(("certificate","missing_count"),5),(("certificate","k1145_pass_count"),1),(("certificate","k1150_pass_count"),1),(("decision","formal_ambient_chart_equals_realized_image"),True),(("decision","p_sign_is_a_connected_component_label"),True),(("decision","source_selector_owned"),True)]
assert valid(D)
for i,(path,value) in enumerate(mut,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
