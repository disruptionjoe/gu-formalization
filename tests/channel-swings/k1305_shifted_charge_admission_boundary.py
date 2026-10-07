#!/usr/bin/env python3
"""Exact controls for K1305's shifted-charge admission boundary."""
import hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1305-shifted-charge-admission-boundary.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["certificate"]; Q=D["decision"]; counts=Counter(r["state"] for r in C["rows"])
check("satisfied",counts["satisfied"]==C["satisfied_count"]==3)
check("formal",counts["satisfied_formal"]==C["satisfied_formal_count"]==2)
check("excluded",counts["excluded"]==C["excluded_count"]==1)
check("missing",counts["missing"]==C["missing_count"]==6)
check("finite BFV feasible",Q["finite_nonzero_charge_bfv_feasible"])
check("lock still needed for selection",Q["charge_selection_requires_source_owned_values_or_equivalent_law"])
check("shift does not select",not Q["shifting_trick_selects_charge"])
check("no invariant positive metric",not Q["canonical_invariant_positive_metric_exists"])
check("physical packet absent",not Q["functional_physical_packet_constructed"])
assert n==15
print("RESULT: PASS 15/15")
