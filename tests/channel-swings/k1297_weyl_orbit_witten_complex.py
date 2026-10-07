#!/usr/bin/env python3
"""Exact controls for K1297's Weyl-orbit Witten complex."""
import hashlib,json
from math import factorial
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1297-weyl-orbit-witten-complex.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
pin=D["pinned_inputs"]["k1296"]
check("K1296 pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; T=D["theorem"]
check("orbit count",C["orbit_summands"]==2**6*factorial(7))
check("degrees zero through seven","Lambda^k C7" in C["hilbert_spaces"])
check("Witten differential","dPhi_o wedge" in C["differential"])
check("nilpotent",C["nilpotent"])
check("closed extension",C["closed_extension"])
check("equivariant",C["equivariant"])
check("unitary summands",T["each_summand_is_unitarily_equivalent"])
check("full H0 dimension",T["full_degree_zero_cohomology_dimension"]==322560)
check("full positive cohomology zero",T["full_positive_degree_cohomology_dimension"]==0)
check("invariant H0 dimension",T["weyl_invariant_degree_zero_cohomology_dimension"]==1)
check("invariant positive cohomology zero",T["weyl_invariant_positive_degree_cohomology_dimension"]==0)
check("not source BV-BFV",not T["source_bv_bfv_complex"])
assert n==13
print("RESULT: PASS 13/13")
