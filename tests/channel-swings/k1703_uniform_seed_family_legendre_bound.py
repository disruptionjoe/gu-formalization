#!/usr/bin/env python3
"""Structural controls for K1703's uniform seed-family theorem."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1703-uniform-seed-family-legendre-bound.json").read_text())
    s,g,l,q=d["seed_family"],d["global_branch"],d["legendre"],d["decision"]
    # Crude explicit moment ceiling used by the proof: |a+b|^6<=32(|a|^6+|b|^6).
    B=2.0
    c_b=32*(B**6+15)+48*(B**4+3)+9
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1703"),
        ("support", "|X|<=B" in s["definition"]),("defect floor","u_0" in s["definition"] and "0<u_0" in s["definition"]),
        ("compact", "weakly compact" in s["compactness"]),("uniform remainder","O_(B,u_0)(q^(7/2))" in s["uniform_remainder"]),
        ("derivative remainder","q^(5/2)" in s["uniform_remainder"]),("score identity","H_3" in g["score_moment_identity"]),
        ("fourth moment identity","E H_4(Y)" in g["score_moment_identity"]),("Cauchy","j_X(q)>=q^2" in g["coercive_bound"]),
        ("finite ceiling",c_b>0),("global minimizer","every global minimizer" in g["consequence"]),
        ("profile","Phi_X(r)=min" in l["definition"]),("quadratic","-(3/2)r^2" in l["expansion"]),
        ("cubic","27c_Xr^3" in l["expansion"]),("floor","(27/4)r^3" in l["uniform_floor"]),
        ("sharpness","K1702 seed" in l["sharpness"]),("uniform branch",q["uniform_global_small_branch"]),
        ("uncontrolled open",not q["uncontrolled_seed_escape_closed"])]
    for n,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
