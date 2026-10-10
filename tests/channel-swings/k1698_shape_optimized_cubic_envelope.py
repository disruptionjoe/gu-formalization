#!/usr/bin/env python3
"""Exact coefficient controls for K1698."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1698-shape-optimized-cubic-envelope.json").read_text())
    v,e=d["variational_data"],d["envelope"]
    checks=[
        ("schema",d["schema_version"]=="1.0"), ("claim",d["claim_id"]=="K1698"),
        ("R", "ell_0(C)^2/tau_0(C)" in v["leading_shape_functional"]),
        ("M", "M=max_C" in v["leading_maximum"]),
        ("Mset", "argmax" in v["leading_maximizers"]),
        ("S", "ell_0(C)^3/tau_0(C)^2" in v["secondary_shape_functional"]),
        ("S floor", "S_*=min" in v["secondary_minimum"] and ">0" in v["secondary_minimum"]),
        ("definition", "inf_C" in e["definition"]),
        ("leading expansion", "-6g^2M" in e["expansion"]),
        ("cubic expansion", "432c_Xg^3S_*" in e["expansion"]),
        ("remainder", "o(g^3)" in e["expansion"]),
        ("no uniqueness", e["optimizer_uniqueness_required"] is False),
        ("seed coefficients", "c_*=1/4" in e["named_seed_coefficients"] and "c_R=31/60" in e["named_seed_coefficients"]),
        ("star cubic",432*Fraction(1,4)==108),
        ("R cubic",432*Fraction(31,60)==Fraction(1116,5)),
        ("scope", "not the all-seed scalar infimum" in d["scope_guard"]),
    ]
    for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
