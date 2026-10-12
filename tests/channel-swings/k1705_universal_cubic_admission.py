#!/usr/bin/env python3
"""Protected-surface controls for K1705."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1705-universal-cubic-admission.json").read_text())
    a,o,q=d["admission"],d["open_frontier"],d["decision"]
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1705"),
        ("five rows",a["new_rows"]==["K1701","K1702","K1703","K1704","K1705"]),
        ("census","420 rows" in a["census"]),("satisfied","341 satisfied" in a["census"]),
        ("conditional","10 conditional" in a["census"]),("excluded","65 excluded" in a["census"]),("missing","4 missing" in a["census"]),
        ("source", "SC-ACT-01/02/06 remain ASSERTS" in a["source_claims"]),("meta", "SC-META-53 remains UNCERTAIN" in a["source_claims"]),
        ("ledger", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in a["physics_ledger"]),
        ("apparatus",a["apparatus"]=="K1145/K1150 remain 0/7."),("protected","public posture unchanged" in a["protected_surfaces"]),
        ("finite open","exact scalar Fisher/MMSE" in o["finite_strength"]),("seed open","growing support" in o["uncontrolled_seeds"]),
        ("Haar open","cutoff-uniform" in o["haar"]),("tensor open","correlated fourth-cumulant tensor" in o["correlated_geometry"]),
        ("lower open","arbitrary-stationary lower bound" in o["lower_bound"]),("no verdict",not q["source_or_ledger_verdict_moved"]),
        ("physical open",not q["physical_admission_closed"])]
    for n,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
