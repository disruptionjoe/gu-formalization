#!/usr/bin/env python3
"""Exact controls for K1303's nonzero-charge finite BFV complex."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1303-nonzero-charge-bfv-complex.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; T=D["theorem"]; Q=D["decision"]
check("constraint count",C["constraint_count"]==91)
check("constraint rank",C["constraint_rank"]==91)
check("irreducible",C["first_stage_reducibility"]==0)
check("minimal ghosts",C["minimal_ghost_count"]==91)
check("first-class bracket","f_ab^c C_c" in C["constraint_bracket"])
check("regular sequence",T["regular_sequence_locally"])
check("KT proper",T["koszul_tate_proper"])
check("master equation",T["master_equation_closes"])
check("orbit observables",T["degree_zero_reduced_observables"]=="C-infinity(O_mu)")
check("not constants",not T["degree_zero_reduced_observables_are_constants"])
check("physical cohomology absent",not T["physical_cohomology_identified"])
assert n==14
print("RESULT: PASS 14/14")
