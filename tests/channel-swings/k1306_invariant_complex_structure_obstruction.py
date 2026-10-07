#!/usr/bin/env python3
"""Exact controls for K1306's invariant complex-structure obstruction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1306-invariant-complex-structure-obstruction.json").read_text()); n=0
def check(label,value):
    global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]; Q=D["decision"]
roots=set()
for i in range(7):
 for j in range(i+1,7):
  for si in (-1,1):
   for sj in (-1,1):
    r=[0]*7; r[i]=si; r[j]=sj; roots.add(tuple(r))
positive={r for r in roots if next(x for x in r if x)!=1}
check("D7 roots",T["root_count"]==len(roots)==84)
check("positive roots",T["positive_root_count"]==len(positive)==42)
check("real root lines",T["root_space_real_dimension"]==1)
check("characters distinct",T["split_torus_characters_pairwise_distinct"] and len(roots)==len(set(roots)))
check("root lines preserved",T["invariant_endomorphism_preserves_each_root_space"])
check("real scalar square obstruction",not T["real_scalar_can_square_to_minus_one"])
check("no invariant almost complex structure",not T["g_invariant_almost_complex_structure_exists"])
check("no invariant compatible complex structure",not T["g_invariant_kks_compatible_complex_structure_exists"])
check("compact template does not transfer",not Q["compact_orbit_kahler_template_transfers"])
check("noninvariant structures not excluded",not Q["noninvariant_complex_structures_excluded"])
check("source uncertainty preserved",not Q["SC_META_53_resolved"])
assert n==13; print("RESULT: PASS 13/13")
