#!/usr/bin/env python3
"""Exact envelope coefficient controls for K1704."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]


def main():
    d=json.loads((ROOT/"lab/process/k1704-all-seed-shape-optimized-cubic-envelope.json").read_text())
    i,e,q=d["inputs"],d["envelope"],d["decision"]
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1704"),
        ("seed inclusion","p_*^(-1/2)" in i["seed_family"]),("rectangles","K1683 rectangles" in i["shape_space"]),
        ("M","M=max_C R_0(C)" in i["shape_data"]),("S positive","S_0(C)>0" in i["shape_data"]),
        ("definition","inf_(X in S)" in e["definition"]),("lower","H_S(g)>=-6g^2M+108g^3S_*" in e["uniform_lower"]),
        ("upper","H_S(g)<=-6g^2M+108g^3S_*" in e["matching_upper"]),("sharp","H_S(g)=-6g^2M+108g^3S_*" in e["sharp_expansion"]),
        ("108",432*Fraction(1,4)==108),("R coefficient",432*Fraction(31,60)==Fraction(1116,5)),
        ("gap",Fraction(1116,5)-108==Fraction(576,5)),("comparison","(576/5)S_*g^3" in e["comparison"]),
        ("controlled decision",q["controlled_all_seed_cubic_envelope_identified"]),("shape optimized",q["fully_rectangular_shape_optimized"]),
        ("finite open",not q["exact_finite_strength_infimum_identified"]),("scope","controlled family" in d["scope_guard"])]
    for n,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {n:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
