#!/usr/bin/env python3
"""K952: the singular scalar's principal quotient is not the point algebra."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k952-source-epsilon-principal-ideal-fat-point.json"
PATHS={"k951":ROOT/"lab/process/k951-source-epsilon-singular-scalar-isolation.json"}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def build(): return json.loads(OUTPUT.read_text())
def validate(d):
    t,q=d["theorem"],d["decision"]
    checks=[
        d["result_id"]=="K952-SOURCE-EPSILON-PRINCIPAL-IDEAL-POINT-ALGEBRA-OBSTRUCTION",
        set(d["pinned_inputs"])==set(PATHS),
        all(d["pinned_inputs"][k]["sha256"]==digest(p) for k,p in PATHS.items()),
        t["ambient_regular_local_dimension"]==7,
        t["constraint_order_at_target"]==2,
        t["quadratic_constraint_is_nonzero_nonunit"],
        t["principal_quotient_krull_dimension"]==6,
        t["reduced_point_quotient_krull_dimension"]==0,
        t["cotangent_dimension_of_principal_quotient"]==7,
        t["cotangent_dimension_of_reduced_point"]==0,
        t["linear_coordinate_survives_principal_quotient"],
        t["evaluation_kernel_is_maximal_ideal"],
        not t["ordinary_principal_ideal_is_maximal_ideal"],
        not t["principal_quotient_is_reduced_point_algebra"],
        t["real_radical_of_principal_ideal_is_maximal_ideal"],
        not q["ordinary_principal_ideal_equals_reduced_point_ideal"],
        not q["real_set_isolation_equals_constraint_algebra_selection"],
        not q["single_scalar_degree_zero_quotient_is_point_observable_algebra"],
        not q["SC_ACT_06_proved_or_refuted"],
        d["controls"]["controls_passed"]==24,
        d["controls"]["hostile_mutations_rejected"]==10,
        d["gu_typed_objects"]["target"].startswith("ALGEBRA-TYPE="),
        "LEDGER_UNCHANGED" in d["source_and_ledger_effect"],
        "formal-local" in d["claim_ceiling"],
    ]
    assert len(checks)==24 and all(checks),[i for i,x in enumerate(checks) if not x]
def main():
    p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args();d=build();validate(d)
    if not a.check: print(json.dumps(d,indent=2,sort_keys=True))
    return 0
if __name__=="__main__":raise SystemExit(main())
