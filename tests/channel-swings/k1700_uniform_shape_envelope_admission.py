#!/usr/bin/env python3
"""Protected-integration certificate for K1700."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1700-uniform-shape-envelope-admission.json").read_text())
    a,x=d["admission"],d["decision"]
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1700"),
        ("fully optimized","fully channel-strength- and rectangular-shape-optimized" in a["quantum_result"]),
        ("cubic gap","(576/5)S_*g^3+o(g^3)" in a["quantum_result"]),
        ("finite strength wake","finite-strength all-seed scalar infimum" in a["remaining_quantum_gate"]),
        ("Haar wake","translation-Haar saving scale" in a["remaining_quantum_gate"]),
        ("tensor wake","correlated fourth-cumulant tensor" in a["remaining_quantum_gate"]),
        ("lower wake","unrestricted lower bound" in a["remaining_quantum_gate"]),
        ("physical gate","K1145/K1150 remain 0/7" in a["physical_admission"]),
        ("census total","415 rows" in a["bridge_census"]),("census satisfied","336 satisfied" in a["bridge_census"]),
        ("source state","SC-ACT-01/02/06 remain ASSERTS" in a["protected_state"]),
        ("ledger state","33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in a["protected_state"]),
        ("scope","Do not promote" in a["scope_guard"]),("uniform closed",x["uniform_shape_boundary_closed"]),
        ("gap integrated",x["named_seed_global_gap_integrated"]),("coefficient open",x["true_unrestricted_coefficient_open"]),
        ("source unchanged",not x["source_status_changed"]),("ledger unchanged",not x["physics_ledger_changed"]),
        ("public unchanged",not x["canon_or_public_status_changed"])]
    for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
