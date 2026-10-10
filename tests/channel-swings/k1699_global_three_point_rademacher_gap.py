#!/usr/bin/env python3
"""Exact comparison controls for K1699."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1699-global-three-point-rademacher-gap.json").read_text())
    c,dec=d["comparison"],d["decision"]
    gap=432*(Fraction(31,60)-Fraction(1,4))
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1699"),
        ("difference", "4/15" in c["coefficient_difference"]),("exact gap",gap==Fraction(576,5)),
        ("envelope gap","(576/5)S_*g^3+o(g^3)" in c["envelope_difference"]),
        ("positive floor","S_*>0" in c["strictness"]),("strict","H_*(g)<H_R(g)" in c["strictness"]),
        ("chain star","h_g^(*-card-up)<h_g^(R-card-up)" in c["chain"]),
        ("chain profile","h_g^card-up<h_g^prof" in c["chain"]),
        ("fixed boundary",dec["fixed_shape_only_boundary_closed"] is True),
        ("shape optimized",dec["fully_rectangular_shape_optimized_strict"] is True),
        ("all seed open",dec["all_seed_scalar_infimum_identified"] is False),
        ("unrestricted open",dec["unrestricted_coefficient_identified"] is False),
        ("correlated open","correlated tensors" in d["scope_guard"]),
        ("lower open","lower bounds remain open" in d["scope_guard"])]
    for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
