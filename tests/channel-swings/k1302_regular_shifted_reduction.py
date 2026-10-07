#!/usr/bin/env python3
"""Exact controls for K1302's regular shifted reduction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1302-regular-shifted-reduction.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]
check("constraint surface dimension",T["constraint_surface_dimension"]==175)
check("quotient group dimension",T["quotient_group_dimension"]==91)
check("reduced dimension",T["reduced_dimension"]==175-91==84)
check("orbit quotient",T["quotient_is_diffeomorphic_to"]=="O_mu")
check("map well defined",T["quotient_map_well_defined"])
check("map bijective",T["quotient_map_bijective"])
check("smooth quotient",T["quotient_smooth"])
check("KKS sign declared","minus the KKS" in T["reduced_form"])
check("nondegenerate",T["reduced_form_nondegenerate"])
check("invariants constant",T["seven_invariants_constant_on_reduced_orbit"])
check("values not derived",not T["seven_invariant_values_derived"])
assert n==13
print("RESULT: PASS 13/13")
