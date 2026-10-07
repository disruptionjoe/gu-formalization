#!/usr/bin/env python3
"""Exact controls for K1301's nonzero-charge shifting parent."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1301-nonzero-charge-shifting-parent.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["construction"]; T=D["theorem"]
check("D7 dimension",C["group_dimension"]==7*13==91)
check("root orbit dimension",C["charge_orbit_dimension"]==91-7==84)
check("shifted parent dimension",C["parent_dimension"]==2*91+84==266)
check("constraint surface dimension",T["constraint_surface_dimension"]==266-91==175)
check("reduced dimension",T["expected_reduced_dimension"]==175-91==84)
check("diagonal moment map","Ad_g^* p+nu" in C["moment_map"])
check("vertical derivative rank",T["vertical_cotangent_derivative_rank"]==91)
check("regular zero",T["zero_is_regular_value"])
check("free action",T["diagonal_action_free"])
check("first class",T["constraint_is_first_class"])
check("charge not selected",not T["charge_parameter_selected_by_construction"])
check("source law absent",not D["decision"]["source_owned_boundary_law_constructed"])
assert n==14
print("RESULT: PASS 14/14")
