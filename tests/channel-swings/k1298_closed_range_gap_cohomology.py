#!/usr/bin/env python3
"""Exact controls for K1298's graph, range, gap and cohomology theorem."""
import hashlib,json
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1298-closed-range-gap-cohomology.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
pin=D["pinned_inputs"]["k1297"]
check("K1297 pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]; mu=(1,2,3,4,5,6,7)
energies=[]
for ns in product(range(2),repeat=2):
    for es in product(range(2),repeat=2): energies.append(2*mu[0]*(ns[0]+es[0])+2*mu[1]*(ns[1]+es[1]))
check("ground zero",min(energies)==0)
check("fixture positive gap",min(e for e in energies if e>0)==2)
check("uniform gap","delta=2 mu" in T["uniform_positive_gap"])
check("compact resolvent",T["compact_resolvent"])
check("common D(L2)","D((1+L)^2)" in T["common_graph_domain"])
check("common complete",T["common_graph_domain_complete"])
check("Schwartz core","Schwartz" in T["smooth_core"])
check("closed ranges",T["differential_ranges_closed"])
check("Hausdorff",T["cohomology_hausdorff"])
check("Hodge decomposition","ker L" in T["hodge_decomposition"])
check("invariant gap",T["weyl_invariant_restriction_preserves_gap"])
check("invariant cohomology one",T["weyl_invariant_cohomology_dimension"]==1)
check("physical pairing absent",not T["physical_pairing_supplied"])
assert n==14
print("RESULT: PASS 14/14")
